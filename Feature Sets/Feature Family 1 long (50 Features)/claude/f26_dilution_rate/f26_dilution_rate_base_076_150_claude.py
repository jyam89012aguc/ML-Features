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
def _f26_dilution_rate(sharesbas, w):
    base = sharesbas.rolling(w, min_periods=max(1, w // 2)).mean()
    return base.diff(periods=w) / base.abs().shift(w).replace(0, np.nan)


def _f26_share_growth(sharesbas, w):
    return sharesbas.diff(periods=w) / sharesbas.abs().rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)


def _f26_dilution_acceleration(sharesbas, w):
    g = _f26_dilution_rate(sharesbas, w)
    return g.diff(periods=w)


# 252d dilution × debt
def f26dr_f26_dilution_rate_dilxdebt_252d_base_v076_signal(sharesbas, debt, closeadj):
    result = _f26_dilution_rate(sharesbas, 252) * debt
    return result.replace([np.inf, -np.inf], np.nan)


# 63d share growth × debt
def f26dr_f26_dilution_rate_sharegrowthxdebt_63d_base_v077_signal(sharesbas, debt, closeadj):
    result = _f26_share_growth(sharesbas, 63) * debt
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution × gp
def f26dr_f26_dilution_rate_dilxgp_252d_base_v078_signal(sharesbas, gp, closeadj):
    result = _f26_dilution_rate(sharesbas, 252) * gp
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dilution × gp
def f26dr_f26_dilution_rate_dilxgp_63d_base_v079_signal(sharesbas, gp, closeadj):
    result = _f26_dilution_rate(sharesbas, 63) * gp
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution × opinc
def f26dr_f26_dilution_rate_dilxopinc_252d_base_v080_signal(sharesbas, opinc, closeadj):
    result = _f26_dilution_rate(sharesbas, 252) * opinc
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dilution × opinc
def f26dr_f26_dilution_rate_dilxopinc_63d_base_v081_signal(sharesbas, opinc, closeadj):
    result = _f26_dilution_rate(sharesbas, 63) * opinc
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution × eps × close
def f26dr_f26_dilution_rate_dilxeps_252d_base_v082_signal(sharesbas, eps, closeadj):
    result = _f26_dilution_rate(sharesbas, 252) * eps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d share growth × eps × close
def f26dr_f26_dilution_rate_sharegrowthxeps_63d_base_v083_signal(sharesbas, eps, closeadj):
    result = _f26_share_growth(sharesbas, 63) * eps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution × wc
def f26dr_f26_dilution_rate_dilxwc_252d_base_v084_signal(sharesbas, workingcapital, closeadj):
    result = _f26_dilution_rate(sharesbas, 252) * workingcapital
    return result.replace([np.inf, -np.inf], np.nan)


# 63d share growth × wc
def f26dr_f26_dilution_rate_sharegrowthxwc_63d_base_v085_signal(sharesbas, workingcapital, closeadj):
    result = _f26_share_growth(sharesbas, 63) * workingcapital
    return result.replace([np.inf, -np.inf], np.nan)


# 21d dilution × cr × close
def f26dr_f26_dilution_rate_dilxcr_21d_base_v086_signal(sharesbas, currentratio, closeadj):
    result = _f26_dilution_rate(sharesbas, 21) * currentratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution × cr × close
def f26dr_f26_dilution_rate_dilxcr_252d_base_v087_signal(sharesbas, currentratio, closeadj):
    result = _f26_dilution_rate(sharesbas, 252) * currentratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d share growth × cr × close
def f26dr_f26_dilution_rate_sharegrowthxcr_252d_base_v088_signal(sharesbas, currentratio, closeadj):
    result = _f26_share_growth(sharesbas, 252) * currentratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dilution × liab
def f26dr_f26_dilution_rate_dilxliab_63d_base_v089_signal(sharesbas, liabilities, closeadj):
    result = _f26_dilution_rate(sharesbas, 63) * liabilities
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution × liab
def f26dr_f26_dilution_rate_dilxliab_252d_base_v090_signal(sharesbas, liabilities, closeadj):
    result = _f26_dilution_rate(sharesbas, 252) * liabilities
    return result.replace([np.inf, -np.inf], np.nan)


# 63d share growth × retearn
def f26dr_f26_dilution_rate_sharegrowthxre_63d_base_v091_signal(sharesbas, retearn, closeadj):
    result = _f26_share_growth(sharesbas, 63) * retearn
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution × retearn
def f26dr_f26_dilution_rate_dilxre_252d_base_v092_signal(sharesbas, retearn, closeadj):
    result = _f26_dilution_rate(sharesbas, 252) * retearn
    return result.replace([np.inf, -np.inf], np.nan)


# 63d share growth × intexp
def f26dr_f26_dilution_rate_sharegrowthxintexp_63d_base_v093_signal(sharesbas, intexp, closeadj):
    result = _f26_share_growth(sharesbas, 63) * intexp
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution × intexp
def f26dr_f26_dilution_rate_dilxintexp_252d_base_v094_signal(sharesbas, intexp, closeadj):
    result = _f26_dilution_rate(sharesbas, 252) * intexp
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution × tax
def f26dr_f26_dilution_rate_dilxtax_252d_base_v095_signal(sharesbas, taxexp, closeadj):
    result = _f26_dilution_rate(sharesbas, 252) * taxexp
    return result.replace([np.inf, -np.inf], np.nan)


# 21d share growth squared × close
def f26dr_f26_dilution_rate_sharegrowthsq_21d_base_v096_signal(sharesbas, closeadj):
    g = _f26_share_growth(sharesbas, 21)
    result = g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d share growth squared × close
def f26dr_f26_dilution_rate_sharegrowthsq_252d_base_v097_signal(sharesbas, closeadj):
    g = _f26_share_growth(sharesbas, 252)
    result = g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d share growth area × close
def f26dr_f26_dilution_rate_sharegrowtharea_63d_base_v098_signal(sharesbas, closeadj):
    g = _f26_share_growth(sharesbas, 21).abs()
    result = g.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d share growth area × close
def f26dr_f26_dilution_rate_sharegrowtharea_252d_base_v099_signal(sharesbas, closeadj):
    g = _f26_share_growth(sharesbas, 63).abs()
    result = g.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d share growth area × close
def f26dr_f26_dilution_rate_sharegrowtharea_504d_base_v100_signal(sharesbas, closeadj):
    g = _f26_share_growth(sharesbas, 252).abs()
    result = g.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution - ncfo growth (issuance vs operating cash)
def f26dr_f26_dilution_rate_dilminusncfo_252d_base_v101_signal(sharesbas, ncfo, closeadj):
    a = _f26_dilution_rate(sharesbas, 252)
    b = ncfo.diff(periods=252) / ncfo.abs().rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dilution - fcf growth
def f26dr_f26_dilution_rate_dilminusfcf_63d_base_v102_signal(sharesbas, fcf, closeadj):
    a = _f26_dilution_rate(sharesbas, 63)
    b = fcf.diff(periods=63) / fcf.abs().rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution + share growth
def f26dr_f26_dilution_rate_dilplussg_252d_base_v103_signal(sharesbas, closeadj):
    result = (_f26_dilution_rate(sharesbas, 252) + _f26_share_growth(sharesbas, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# expanding worst (max) dilution × close
def f26dr_f26_dilution_rate_dilworst_504d_base_v104_signal(sharesbas, closeadj):
    g = _f26_dilution_rate(sharesbas, 252)
    result = g.expanding(min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# expanding best (min) dilution × close
def f26dr_f26_dilution_rate_dilbest_504d_base_v105_signal(sharesbas, closeadj):
    g = _f26_dilution_rate(sharesbas, 252)
    result = g.expanding(min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max share growth in 63d × close
def f26dr_f26_dilution_rate_sharegrowthmax_63d_base_v106_signal(sharesbas, closeadj):
    result = _f26_share_growth(sharesbas, 21).rolling(63, min_periods=21).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max share growth in 252d × close
def f26dr_f26_dilution_rate_sharegrowthmax_252d_base_v107_signal(sharesbas, closeadj):
    result = _f26_share_growth(sharesbas, 63).rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min share growth in 63d × close (deepest buyback)
def f26dr_f26_dilution_rate_sharegrowthmin_63d_base_v108_signal(sharesbas, closeadj):
    result = _f26_share_growth(sharesbas, 21).rolling(63, min_periods=21).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min share growth in 252d × close
def f26dr_f26_dilution_rate_sharegrowthmin_252d_base_v109_signal(sharesbas, closeadj):
    result = _f26_share_growth(sharesbas, 63).rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA dilution × ebitda
def f26dr_f26_dilution_rate_dilemaebitda_21d_base_v110_signal(sharesbas, ebitda, closeadj):
    g = _f26_dilution_rate(sharesbas, 21)
    result = g.ewm(span=21, adjust=False).mean() * ebitda
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA dilution × ebitda
def f26dr_f26_dilution_rate_dilemaebitda_252d_base_v111_signal(sharesbas, ebitda, closeadj):
    g = _f26_dilution_rate(sharesbas, 252)
    result = g.ewm(span=252, adjust=False).mean() * ebitda
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution area × marketcap
def f26dr_f26_dilution_rate_dilareaxmcap_252d_base_v112_signal(sharesbas, closeadj):
    g = _f26_dilution_rate(sharesbas, 63).abs()
    result = g.rolling(252, min_periods=63).sum() * (closeadj * sharesbas)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d share growth anomaly × close
def f26dr_f26_dilution_rate_sharegrowthanom_63d_base_v113_signal(sharesbas, closeadj):
    g = _f26_share_growth(sharesbas, 63)
    base = _mean(_f26_share_growth(sharesbas, 252), 252)
    result = (g - base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d share growth anomaly × close
def f26dr_f26_dilution_rate_sharegrowthanom_252d_base_v114_signal(sharesbas, closeadj):
    g = _f26_share_growth(sharesbas, 252)
    base = _mean(_f26_share_growth(sharesbas, 504), 504)
    result = (g - base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dilution anomaly × close
def f26dr_f26_dilution_rate_dilanom_63d_base_v115_signal(sharesbas, closeadj):
    g = _f26_dilution_rate(sharesbas, 63)
    base = _mean(_f26_dilution_rate(sharesbas, 252), 252)
    result = (g - base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution anomaly × close
def f26dr_f26_dilution_rate_dilanom_252d_base_v116_signal(sharesbas, closeadj):
    g = _f26_dilution_rate(sharesbas, 252)
    base = _mean(_f26_dilution_rate(sharesbas, 504), 504)
    result = (g - base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d dilution × revenue × close
def f26dr_f26_dilution_rate_dilxrevxprice_21d_base_v117_signal(sharesbas, revenue, closeadj):
    result = _f26_dilution_rate(sharesbas, 21) * revenue * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution × revenue × close
def f26dr_f26_dilution_rate_dilxrevxprice_252d_base_v118_signal(sharesbas, revenue, closeadj):
    result = _f26_dilution_rate(sharesbas, 252) * revenue * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution accel × marketcap
def f26dr_f26_dilution_rate_dilaccelxmcap_252d_base_v119_signal(sharesbas, closeadj):
    result = _f26_dilution_acceleration(sharesbas, 252) * (closeadj * sharesbas)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dilution accel × marketcap
def f26dr_f26_dilution_rate_dilaccelxmcap_63d_base_v120_signal(sharesbas, closeadj):
    result = _f26_dilution_acceleration(sharesbas, 63) * (closeadj * sharesbas)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d dilution × shares level × close
def f26dr_f26_dilution_rate_dilxshareslvl_21d_base_v121_signal(sharesbas, closeadj):
    result = _f26_dilution_rate(sharesbas, 21) * sharesbas * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution × shares level × close
def f26dr_f26_dilution_rate_dilxshareslvl_252d_base_v122_signal(sharesbas, closeadj):
    result = _f26_dilution_rate(sharesbas, 252) * sharesbas * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d share growth × ebitda × close
def f26dr_f26_dilution_rate_sharegrowthxebitdaprice_252d_base_v123_signal(sharesbas, ebitda, closeadj):
    result = _f26_share_growth(sharesbas, 252) * ebitda * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution × ebitda × close
def f26dr_f26_dilution_rate_dilxebitdaprice_252d_base_v124_signal(sharesbas, ebitda, closeadj):
    result = _f26_dilution_rate(sharesbas, 252) * ebitda * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution × (ebitda - capex) × close
def f26dr_f26_dilution_rate_dilxebitdacapex_252d_base_v125_signal(sharesbas, ebitda, capex, closeadj):
    result = _f26_dilution_rate(sharesbas, 252) * (ebitda - capex.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d share growth × (assets - liab)
def f26dr_f26_dilution_rate_sharegrowthxnet_252d_base_v126_signal(sharesbas, assets, liabilities, closeadj):
    result = _f26_share_growth(sharesbas, 252) * (assets - liabilities)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA dilution × close
def f26dr_f26_dilution_rate_dilema_21d_base_v127_signal(sharesbas, closeadj):
    g = _f26_dilution_rate(sharesbas, 21)
    result = g.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA share growth × close
def f26dr_f26_dilution_rate_sharegrowthema_21d_base_v128_signal(sharesbas, closeadj):
    g = _f26_share_growth(sharesbas, 21)
    result = g.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d dilution rank over 252d × close
def f26dr_f26_dilution_rate_dilrank_252d_base_v129_signal(sharesbas, closeadj):
    g = _f26_dilution_rate(sharesbas, 21)
    result = g.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d share growth rank over 252d × close
def f26dr_f26_dilution_rate_sharegrowthrank_252d_base_v130_signal(sharesbas, closeadj):
    g = _f26_share_growth(sharesbas, 63)
    result = g.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean dilution × closeadj (continuous)
def f26dr_f26_dilution_rate_dilextremecount_252d_base_v131_signal(sharesbas, closeadj):
    base = _f26_dilution_rate(sharesbas, 63)
    result = base.rolling(252, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of buyback strong (<-2%)
def f26dr_f26_dilution_rate_buybackstrongcount_504d_base_v132_signal(sharesbas, closeadj):
    flag = (_f26_dilution_rate(sharesbas, 63) < -0.02).astype(float)
    result = flag.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of share growth above >2%
def f26dr_f26_dilution_rate_sharegrowthhighcount_252d_base_v133_signal(sharesbas, closeadj):
    flag = (_f26_share_growth(sharesbas, 63) > 0.02).astype(float)
    result = flag.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution × std × close
def f26dr_f26_dilution_rate_dilxvol_252d_base_v134_signal(sharesbas, closeadj):
    g = _f26_dilution_rate(sharesbas, 252)
    sd = _std(_f26_dilution_rate(sharesbas, 63), 252)
    result = g * sd * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d share growth × std × close
def f26dr_f26_dilution_rate_sharegrowthxvol_63d_base_v135_signal(sharesbas, closeadj):
    g = _f26_share_growth(sharesbas, 63)
    sd = _std(_f26_share_growth(sharesbas, 21), 63)
    result = g * sd * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# composite: dilution + share growth + accel × close
def f26dr_f26_dilution_rate_compositescore_252d_base_v136_signal(sharesbas, closeadj):
    a = _f26_dilution_rate(sharesbas, 252)
    b = _f26_share_growth(sharesbas, 252)
    c = _f26_dilution_acceleration(sharesbas, 252)
    result = (a + b + c) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dilution × revenue per share
def f26dr_f26_dilution_rate_dilxsales_63d_base_v137_signal(sharesbas, revenue, closeadj):
    result = _f26_dilution_rate(sharesbas, 63) * (revenue / closeadj.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution × ni × close
def f26dr_f26_dilution_rate_dilxni_252d_base_v138_signal(sharesbas, netinc, closeadj):
    result = _f26_dilution_rate(sharesbas, 252) * netinc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d share growth × ni × close
def f26dr_f26_dilution_rate_sharegrowthxnini_21d_base_v139_signal(sharesbas, netinc, closeadj):
    result = _f26_share_growth(sharesbas, 21) * netinc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# expanding mean dilution × close
def f26dr_f26_dilution_rate_dilexp_252d_base_v140_signal(sharesbas, closeadj):
    g = _f26_dilution_rate(sharesbas, 252)
    result = g.expanding(min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# expanding mean share growth × close
def f26dr_f26_dilution_rate_sharegrowthexp_252d_base_v141_signal(sharesbas, closeadj):
    g = _f26_share_growth(sharesbas, 252)
    result = g.expanding(min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dilution × current ratio × close
def f26dr_f26_dilution_rate_dilcrprice_63d_base_v142_signal(sharesbas, currentratio, closeadj):
    result = _f26_dilution_rate(sharesbas, 63) * currentratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d share growth × wc × close
def f26dr_f26_dilution_rate_sharegrowthwcprice_21d_base_v143_signal(sharesbas, workingcapital, closeadj):
    result = _f26_share_growth(sharesbas, 21) * workingcapital * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d / 252d dilution ratio × close
def f26dr_f26_dilution_rate_dilratio_21v252_base_v144_signal(sharesbas, closeadj):
    a = _f26_dilution_rate(sharesbas, 21)
    b = _f26_dilution_rate(sharesbas, 252).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d / 504d share growth ratio × close
def f26dr_f26_dilution_rate_sharegrowthratio_252v504_base_v145_signal(sharesbas, closeadj):
    a = _f26_share_growth(sharesbas, 252)
    b = _f26_share_growth(sharesbas, 504).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution × (assets - debt)
def f26dr_f26_dilution_rate_dilxnet_252d_base_v146_signal(sharesbas, assets, debt, closeadj):
    result = _f26_dilution_rate(sharesbas, 252) * (assets - debt)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d share growth × (revenue - capex)
def f26dr_f26_dilution_rate_sharegrowthxrevcapex_63d_base_v147_signal(sharesbas, revenue, capex, closeadj):
    result = _f26_share_growth(sharesbas, 63) * (revenue - capex.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution × (gp - opinc) × close
def f26dr_f26_dilution_rate_dilxgpopgap_252d_base_v148_signal(sharesbas, gp, opinc, closeadj):
    result = _f26_dilution_rate(sharesbas, 252) * (gp - opinc) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution × (equity - debt)
def f26dr_f26_dilution_rate_dilxneteq_252d_base_v149_signal(sharesbas, equity, debt, closeadj):
    result = _f26_dilution_rate(sharesbas, 252) * (equity - debt)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: (dilution + share growth) × revenue × close
def f26dr_f26_dilution_rate_compositetraj_252d_base_v150_signal(sharesbas, revenue, closeadj):
    result = (_f26_dilution_rate(sharesbas, 252) + _f26_share_growth(sharesbas, 252)) * revenue * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f26dr_f26_dilution_rate_dilxdebt_252d_base_v076_signal,
    f26dr_f26_dilution_rate_sharegrowthxdebt_63d_base_v077_signal,
    f26dr_f26_dilution_rate_dilxgp_252d_base_v078_signal,
    f26dr_f26_dilution_rate_dilxgp_63d_base_v079_signal,
    f26dr_f26_dilution_rate_dilxopinc_252d_base_v080_signal,
    f26dr_f26_dilution_rate_dilxopinc_63d_base_v081_signal,
    f26dr_f26_dilution_rate_dilxeps_252d_base_v082_signal,
    f26dr_f26_dilution_rate_sharegrowthxeps_63d_base_v083_signal,
    f26dr_f26_dilution_rate_dilxwc_252d_base_v084_signal,
    f26dr_f26_dilution_rate_sharegrowthxwc_63d_base_v085_signal,
    f26dr_f26_dilution_rate_dilxcr_21d_base_v086_signal,
    f26dr_f26_dilution_rate_dilxcr_252d_base_v087_signal,
    f26dr_f26_dilution_rate_sharegrowthxcr_252d_base_v088_signal,
    f26dr_f26_dilution_rate_dilxliab_63d_base_v089_signal,
    f26dr_f26_dilution_rate_dilxliab_252d_base_v090_signal,
    f26dr_f26_dilution_rate_sharegrowthxre_63d_base_v091_signal,
    f26dr_f26_dilution_rate_dilxre_252d_base_v092_signal,
    f26dr_f26_dilution_rate_sharegrowthxintexp_63d_base_v093_signal,
    f26dr_f26_dilution_rate_dilxintexp_252d_base_v094_signal,
    f26dr_f26_dilution_rate_dilxtax_252d_base_v095_signal,
    f26dr_f26_dilution_rate_sharegrowthsq_21d_base_v096_signal,
    f26dr_f26_dilution_rate_sharegrowthsq_252d_base_v097_signal,
    f26dr_f26_dilution_rate_sharegrowtharea_63d_base_v098_signal,
    f26dr_f26_dilution_rate_sharegrowtharea_252d_base_v099_signal,
    f26dr_f26_dilution_rate_sharegrowtharea_504d_base_v100_signal,
    f26dr_f26_dilution_rate_dilminusncfo_252d_base_v101_signal,
    f26dr_f26_dilution_rate_dilminusfcf_63d_base_v102_signal,
    f26dr_f26_dilution_rate_dilplussg_252d_base_v103_signal,
    f26dr_f26_dilution_rate_dilworst_504d_base_v104_signal,
    f26dr_f26_dilution_rate_dilbest_504d_base_v105_signal,
    f26dr_f26_dilution_rate_sharegrowthmax_63d_base_v106_signal,
    f26dr_f26_dilution_rate_sharegrowthmax_252d_base_v107_signal,
    f26dr_f26_dilution_rate_sharegrowthmin_63d_base_v108_signal,
    f26dr_f26_dilution_rate_sharegrowthmin_252d_base_v109_signal,
    f26dr_f26_dilution_rate_dilemaebitda_21d_base_v110_signal,
    f26dr_f26_dilution_rate_dilemaebitda_252d_base_v111_signal,
    f26dr_f26_dilution_rate_dilareaxmcap_252d_base_v112_signal,
    f26dr_f26_dilution_rate_sharegrowthanom_63d_base_v113_signal,
    f26dr_f26_dilution_rate_sharegrowthanom_252d_base_v114_signal,
    f26dr_f26_dilution_rate_dilanom_63d_base_v115_signal,
    f26dr_f26_dilution_rate_dilanom_252d_base_v116_signal,
    f26dr_f26_dilution_rate_dilxrevxprice_21d_base_v117_signal,
    f26dr_f26_dilution_rate_dilxrevxprice_252d_base_v118_signal,
    f26dr_f26_dilution_rate_dilaccelxmcap_252d_base_v119_signal,
    f26dr_f26_dilution_rate_dilaccelxmcap_63d_base_v120_signal,
    f26dr_f26_dilution_rate_dilxshareslvl_21d_base_v121_signal,
    f26dr_f26_dilution_rate_dilxshareslvl_252d_base_v122_signal,
    f26dr_f26_dilution_rate_sharegrowthxebitdaprice_252d_base_v123_signal,
    f26dr_f26_dilution_rate_dilxebitdaprice_252d_base_v124_signal,
    f26dr_f26_dilution_rate_dilxebitdacapex_252d_base_v125_signal,
    f26dr_f26_dilution_rate_sharegrowthxnet_252d_base_v126_signal,
    f26dr_f26_dilution_rate_dilema_21d_base_v127_signal,
    f26dr_f26_dilution_rate_sharegrowthema_21d_base_v128_signal,
    f26dr_f26_dilution_rate_dilrank_252d_base_v129_signal,
    f26dr_f26_dilution_rate_sharegrowthrank_252d_base_v130_signal,
    f26dr_f26_dilution_rate_dilextremecount_252d_base_v131_signal,
    f26dr_f26_dilution_rate_buybackstrongcount_504d_base_v132_signal,
    f26dr_f26_dilution_rate_sharegrowthhighcount_252d_base_v133_signal,
    f26dr_f26_dilution_rate_dilxvol_252d_base_v134_signal,
    f26dr_f26_dilution_rate_sharegrowthxvol_63d_base_v135_signal,
    f26dr_f26_dilution_rate_compositescore_252d_base_v136_signal,
    f26dr_f26_dilution_rate_dilxsales_63d_base_v137_signal,
    f26dr_f26_dilution_rate_dilxni_252d_base_v138_signal,
    f26dr_f26_dilution_rate_sharegrowthxnini_21d_base_v139_signal,
    f26dr_f26_dilution_rate_dilexp_252d_base_v140_signal,
    f26dr_f26_dilution_rate_sharegrowthexp_252d_base_v141_signal,
    f26dr_f26_dilution_rate_dilcrprice_63d_base_v142_signal,
    f26dr_f26_dilution_rate_sharegrowthwcprice_21d_base_v143_signal,
    f26dr_f26_dilution_rate_dilratio_21v252_base_v144_signal,
    f26dr_f26_dilution_rate_sharegrowthratio_252v504_base_v145_signal,
    f26dr_f26_dilution_rate_dilxnet_252d_base_v146_signal,
    f26dr_f26_dilution_rate_sharegrowthxrevcapex_63d_base_v147_signal,
    f26dr_f26_dilution_rate_dilxgpopgap_252d_base_v148_signal,
    f26dr_f26_dilution_rate_dilxneteq_252d_base_v149_signal,
    f26dr_f26_dilution_rate_compositetraj_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F26_DILUTION_RATE_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f26_dilution_rate", "_f26_share_growth", "_f26_dilution_acceleration")
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
    print(f"OK f26_dilution_rate_base_076_150_claude: {n_features} features pass")
