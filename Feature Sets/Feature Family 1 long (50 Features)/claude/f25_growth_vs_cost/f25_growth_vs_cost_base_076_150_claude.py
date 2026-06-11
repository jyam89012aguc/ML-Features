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


def _f25_growth(s, w):
    base = s.rolling(w, min_periods=max(1, w // 2)).mean()
    return base.diff(periods=w) / base.abs().shift(w).replace(0, np.nan)


# ===== folder domain primitives =====
def _f25_growth_vs_cost(revenue, opex, w):
    rg = _f25_growth(revenue, w)
    og = _f25_growth(opex, w)
    return rg - og


def _f25_revenue_vs_opex(revenue, opex, w):
    return _f25_growth(revenue, w) - _f25_growth(opex, w)


def _f25_revenue_vs_cogs(revenue, gp, w):
    cogs = revenue - gp
    rg = _f25_growth(revenue, w)
    cg = _f25_growth(cogs, w)
    return rg - cg


# 21d gp-derived gvc × marketcap
def f25gvc_f25_growth_vs_cost_gvcxmcap_21d_base_v076_signal(revenue, gp, closeadj, sharesbas):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 21) * (closeadj * sharesbas)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d gp-derived gvc × marketcap
def f25gvc_f25_growth_vs_cost_gvcxmcap_504d_base_v077_signal(revenue, gp, closeadj, sharesbas):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 504) * (closeadj * sharesbas)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-vs-cogs × revenue × close
def f25gvc_f25_growth_vs_cost_revvcogsxrevprice_252d_base_v078_signal(revenue, gp, closeadj):
    result = _f25_revenue_vs_cogs(revenue, gp, 252) * revenue * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue-vs-cogs × revenue × close
def f25gvc_f25_growth_vs_cost_revvcogsxrevprice_21d_base_v079_signal(revenue, gp, closeadj):
    result = _f25_revenue_vs_cogs(revenue, gp, 21) * revenue * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-vs-opinc × revenue × close
def f25gvc_f25_growth_vs_cost_revvopincxrevprice_252d_base_v080_signal(revenue, opinc, closeadj):
    opex = revenue - opinc
    result = _f25_revenue_vs_opex(revenue, opex, 252) * revenue * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gvc weighted by gp ratio (revenue-cost differential)
def f25gvc_f25_growth_vs_cost_gvcminusrvc_252d_base_v081_signal(revenue, gp, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 252)
    weight = gp / revenue.replace(0, np.nan).abs()
    result = base * weight * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gvc minus revenue-vs-cogs
def f25gvc_f25_growth_vs_cost_gvcminusrvc_21d_base_v082_signal(revenue, gp, closeadj):
    opex = revenue - gp
    weight = gp / revenue.replace(0, np.nan).abs()
    result = _f25_growth_vs_cost(revenue, opex, 21) * weight * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gvc anomaly (vs 504d mean) × close
def f25gvc_f25_growth_vs_cost_gvcanom_252d_base_v083_signal(revenue, gp, closeadj):
    opex = revenue - gp
    g = _f25_growth_vs_cost(revenue, opex, 252)
    base = _mean(_f25_growth_vs_cost(revenue, opex, 504), 504)
    result = (g - base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gvc anomaly × close
def f25gvc_f25_growth_vs_cost_gvcanom_63d_base_v084_signal(revenue, gp, closeadj):
    opex = revenue - gp
    g = _f25_growth_vs_cost(revenue, opex, 63)
    base = _mean(_f25_growth_vs_cost(revenue, opex, 252), 252)
    result = (g - base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gvc rank over 252d × close
def f25gvc_f25_growth_vs_cost_gvcrank_252d_base_v085_signal(revenue, gp, closeadj):
    opex = revenue - gp
    g = _f25_growth_vs_cost(revenue, opex, 21)
    result = g.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gvc rank over 252d × close
def f25gvc_f25_growth_vs_cost_gvcrank63_252d_base_v086_signal(revenue, gp, closeadj):
    opex = revenue - gp
    g = _f25_growth_vs_cost(revenue, opex, 63)
    result = g.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# expanding worst (most negative) gvc × close
def f25gvc_f25_growth_vs_cost_gvcworst_504d_base_v087_signal(revenue, gp, closeadj):
    opex = revenue - gp
    g = _f25_growth_vs_cost(revenue, opex, 252)
    result = g.expanding(min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# expanding best gvc × close
def f25gvc_f25_growth_vs_cost_gvcbest_504d_base_v088_signal(revenue, gp, closeadj):
    opex = revenue - gp
    g = _f25_growth_vs_cost(revenue, opex, 252)
    result = g.expanding(min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gvc × ebitda × close
def f25gvc_f25_growth_vs_cost_gvcxebitdaprice_21d_base_v089_signal(revenue, gp, ebitda, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 21) * ebitda * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gvc × ebitda × close
def f25gvc_f25_growth_vs_cost_gvcxebitdaprice_63d_base_v090_signal(revenue, gp, ebitda, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 63) * ebitda * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gvc × (gp - opinc) × close
def f25gvc_f25_growth_vs_cost_gvcxgpopgap_252d_base_v091_signal(revenue, gp, opinc, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 252) * (gp - opinc) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gvc × (assets - debt)
def f25gvc_f25_growth_vs_cost_gvcxnet_252d_base_v092_signal(revenue, gp, assets, debt, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 252) * (assets - debt)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gvc × (assets - liabilities)
def f25gvc_f25_growth_vs_cost_gvcxnetal_252d_base_v093_signal(revenue, gp, assets, liabilities, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 252) * (assets - liabilities)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gvc × (revenue - capex)
def f25gvc_f25_growth_vs_cost_gvcxrevcapex_252d_base_v094_signal(revenue, gp, capex, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 252) * (revenue - capex.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue-vs-opinc × ebitda
def f25gvc_f25_growth_vs_cost_revvopincxebitda_21d_base_v095_signal(revenue, opinc, ebitda, closeadj):
    opex = revenue - opinc
    result = _f25_revenue_vs_opex(revenue, opex, 21) * ebitda
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-vs-opinc × ebitda
def f25gvc_f25_growth_vs_cost_revvopincxebitda_252d_base_v096_signal(revenue, opinc, ebitda, closeadj):
    opex = revenue - opinc
    result = _f25_revenue_vs_opex(revenue, opex, 252) * ebitda
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-vs-opinc × revenue
def f25gvc_f25_growth_vs_cost_revvopincxrev_252d_base_v097_signal(revenue, opinc, closeadj):
    opex = revenue - opinc
    result = _f25_revenue_vs_opex(revenue, opex, 252) * revenue
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue-vs-cogs × marketcap
def f25gvc_f25_growth_vs_cost_revvcogsxmcap_21d_base_v098_signal(revenue, gp, closeadj, sharesbas):
    result = _f25_revenue_vs_cogs(revenue, gp, 21) * (closeadj * sharesbas)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-vs-cogs × marketcap
def f25gvc_f25_growth_vs_cost_revvcogsxmcap_252d_base_v099_signal(revenue, gp, closeadj, sharesbas):
    result = _f25_revenue_vs_cogs(revenue, gp, 252) * (closeadj * sharesbas)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue-vs-cogs × marketcap
def f25gvc_f25_growth_vs_cost_revvcogsxmcap_504d_base_v100_signal(revenue, gp, closeadj, sharesbas):
    result = _f25_revenue_vs_cogs(revenue, gp, 504) * (closeadj * sharesbas)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gvc × intexp
def f25gvc_f25_growth_vs_cost_gvcxintexp_21d_base_v101_signal(revenue, gp, intexp, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 21) * intexp
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gvc × taxexp
def f25gvc_f25_growth_vs_cost_gvcxtax_21d_base_v102_signal(revenue, gp, taxexp, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 21) * taxexp
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gvc × ncfo
def f25gvc_f25_growth_vs_cost_gvcxncfo_21d_base_v103_signal(revenue, gp, ncfo, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 21) * ncfo
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gvc × fcf
def f25gvc_f25_growth_vs_cost_gvcxfcf_21d_base_v104_signal(revenue, gp, fcf, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 21) * fcf
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gvc × netinc
def f25gvc_f25_growth_vs_cost_gvcxni_21d_base_v105_signal(revenue, gp, netinc, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 21) * netinc
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gvc × netinc
def f25gvc_f25_growth_vs_cost_gvcxni_63d_base_v106_signal(revenue, gp, netinc, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 63) * netinc
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gvc × workingcapital
def f25gvc_f25_growth_vs_cost_gvcxwc_21d_base_v107_signal(revenue, gp, workingcapital, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 21) * workingcapital
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gvc × debt
def f25gvc_f25_growth_vs_cost_gvcxdebt_63d_base_v108_signal(revenue, gp, debt, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 63) * debt
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gvc × assets
def f25gvc_f25_growth_vs_cost_gvcxassets_63d_base_v109_signal(revenue, gp, assets, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 63) * assets
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gvc × equity
def f25gvc_f25_growth_vs_cost_gvcxequity_63d_base_v110_signal(revenue, gp, equity, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 63) * equity
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gvc × liabilities
def f25gvc_f25_growth_vs_cost_gvcxliab_63d_base_v111_signal(revenue, gp, liabilities, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 63) * liabilities
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gvc × retearn
def f25gvc_f25_growth_vs_cost_gvcxre_63d_base_v112_signal(revenue, gp, retearn, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 63) * retearn
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gvc × ebitda
def f25gvc_f25_growth_vs_cost_gvcxebitda_63d_base_v113_signal(revenue, gp, ebitda, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 63) * ebitda
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gvc × ncfo
def f25gvc_f25_growth_vs_cost_gvcxncfo_63d_base_v114_signal(revenue, gp, ncfo, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 63) * ncfo
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gvc × fcf
def f25gvc_f25_growth_vs_cost_gvcxfcf_63d_base_v115_signal(revenue, gp, fcf, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 63) * fcf
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gvc × abs(ncff)
def f25gvc_f25_growth_vs_cost_gvcxncff_21d_base_v116_signal(revenue, gp, ncff, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 21) * ncff.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-vs-cogs × ncfo
def f25gvc_f25_growth_vs_cost_revvcogsxncfo_252d_base_v117_signal(revenue, gp, ncfo, closeadj):
    result = _f25_revenue_vs_cogs(revenue, gp, 252) * ncfo
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue-vs-cogs × close
def f25gvc_f25_growth_vs_cost_revvcogsxprice_21d_base_v118_signal(revenue, gp, closeadj):
    result = _f25_revenue_vs_cogs(revenue, gp, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue-vs-cogs × ebitda × close
def f25gvc_f25_growth_vs_cost_revvcogsxebitdaprice_21d_base_v119_signal(revenue, gp, ebitda, closeadj):
    result = _f25_revenue_vs_cogs(revenue, gp, 21) * ebitda * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-vs-cogs × ebitda × close
def f25gvc_f25_growth_vs_cost_revvcogsxebitdaprice_252d_base_v120_signal(revenue, gp, ebitda, closeadj):
    result = _f25_revenue_vs_cogs(revenue, gp, 252) * ebitda * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue-vs-opinc × close
def f25gvc_f25_growth_vs_cost_revvopincprice_21d_base_v121_signal(revenue, opinc, closeadj):
    opex = revenue - opinc
    result = _f25_revenue_vs_opex(revenue, opex, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue-vs-opinc × revenue × close
def f25gvc_f25_growth_vs_cost_revvopincxrevprice_21d_base_v122_signal(revenue, opinc, closeadj):
    opex = revenue - opinc
    result = _f25_revenue_vs_opex(revenue, opex, 21) * revenue * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-vs-opinc × marketcap
def f25gvc_f25_growth_vs_cost_revvopincxmcap_252d_base_v123_signal(revenue, opinc, closeadj, sharesbas):
    opex = revenue - opinc
    result = _f25_revenue_vs_opex(revenue, opex, 252) * (closeadj * sharesbas)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue-vs-opinc × marketcap
def f25gvc_f25_growth_vs_cost_revvopincxmcap_21d_base_v124_signal(revenue, opinc, closeadj, sharesbas):
    opex = revenue - opinc
    result = _f25_revenue_vs_opex(revenue, opex, 21) * (closeadj * sharesbas)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-vs-opinc × debt
def f25gvc_f25_growth_vs_cost_revvopincxdebt_252d_base_v125_signal(revenue, opinc, debt, closeadj):
    opex = revenue - opinc
    result = _f25_revenue_vs_opex(revenue, opex, 252) * debt
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-vs-opinc × equity
def f25gvc_f25_growth_vs_cost_revvopincxequity_252d_base_v126_signal(revenue, opinc, equity, closeadj):
    opex = revenue - opinc
    result = _f25_revenue_vs_opex(revenue, opex, 252) * equity
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-vs-opinc × assets
def f25gvc_f25_growth_vs_cost_revvopincxassets_252d_base_v127_signal(revenue, opinc, assets, closeadj):
    opex = revenue - opinc
    result = _f25_revenue_vs_opex(revenue, opex, 252) * assets
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-vs-opinc × eps × close
def f25gvc_f25_growth_vs_cost_revvopincxeps_252d_base_v128_signal(revenue, opinc, eps, closeadj):
    opex = revenue - opinc
    result = _f25_revenue_vs_opex(revenue, opex, 252) * eps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-vs-opinc × workingcapital
def f25gvc_f25_growth_vs_cost_revvopincxwc_252d_base_v129_signal(revenue, opinc, workingcapital, closeadj):
    opex = revenue - opinc
    result = _f25_revenue_vs_opex(revenue, opex, 252) * workingcapital
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-vs-opinc × currentratio × close
def f25gvc_f25_growth_vs_cost_revvopincxcr_252d_base_v130_signal(revenue, opinc, currentratio, closeadj):
    opex = revenue - opinc
    result = _f25_revenue_vs_opex(revenue, opex, 252) * currentratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-vs-opinc × intexp
def f25gvc_f25_growth_vs_cost_revvopincxintexp_252d_base_v131_signal(revenue, opinc, intexp, closeadj):
    opex = revenue - opinc
    result = _f25_revenue_vs_opex(revenue, opex, 252) * intexp
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-vs-opinc × taxexp
def f25gvc_f25_growth_vs_cost_revvopincxtax_252d_base_v132_signal(revenue, opinc, taxexp, closeadj):
    opex = revenue - opinc
    result = _f25_revenue_vs_opex(revenue, opex, 252) * taxexp
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-vs-opinc × liabilities
def f25gvc_f25_growth_vs_cost_revvopincxliab_252d_base_v133_signal(revenue, opinc, liabilities, closeadj):
    opex = revenue - opinc
    result = _f25_revenue_vs_opex(revenue, opex, 252) * liabilities
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-vs-opinc × retearn
def f25gvc_f25_growth_vs_cost_revvopincxre_252d_base_v134_signal(revenue, opinc, retearn, closeadj):
    opex = revenue - opinc
    result = _f25_revenue_vs_opex(revenue, opex, 252) * retearn
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-vs-opinc × ncfo
def f25gvc_f25_growth_vs_cost_revvopincxncfo_252d_base_v135_signal(revenue, opinc, ncfo, closeadj):
    opex = revenue - opinc
    result = _f25_revenue_vs_opex(revenue, opex, 252) * ncfo
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-vs-opinc × fcf
def f25gvc_f25_growth_vs_cost_revvopincxfcf_252d_base_v136_signal(revenue, opinc, fcf, closeadj):
    opex = revenue - opinc
    result = _f25_revenue_vs_opex(revenue, opex, 252) * fcf
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-vs-opinc × netinc
def f25gvc_f25_growth_vs_cost_revvopincxni_252d_base_v137_signal(revenue, opinc, netinc, closeadj):
    opex = revenue - opinc
    result = _f25_revenue_vs_opex(revenue, opex, 252) * netinc
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-vs-opinc × abs(capex)
def f25gvc_f25_growth_vs_cost_revvopincxcapex_252d_base_v138_signal(revenue, opinc, capex, closeadj):
    opex = revenue - opinc
    result = _f25_revenue_vs_opex(revenue, opex, 252) * capex.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-vs-opinc × abs(ncff)
def f25gvc_f25_growth_vs_cost_revvopincxncff_252d_base_v139_signal(revenue, opinc, ncff, closeadj):
    opex = revenue - opinc
    result = _f25_revenue_vs_opex(revenue, opex, 252) * ncff.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue-vs-opinc × eps × close
def f25gvc_f25_growth_vs_cost_revvopincxeps_21d_base_v140_signal(revenue, opinc, eps, closeadj):
    opex = revenue - opinc
    result = _f25_revenue_vs_opex(revenue, opex, 21) * eps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-vs-opinc anomaly × close
def f25gvc_f25_growth_vs_cost_revvopincanom_252d_base_v141_signal(revenue, opinc, closeadj):
    opex = revenue - opinc
    g = _f25_revenue_vs_opex(revenue, opex, 252)
    base = _mean(_f25_revenue_vs_opex(revenue, opex, 504), 504)
    result = (g - base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-vs-cogs anomaly × close
def f25gvc_f25_growth_vs_cost_revvcogsanom_252d_base_v142_signal(revenue, gp, closeadj):
    g = _f25_revenue_vs_cogs(revenue, gp, 252)
    base = _mean(_f25_revenue_vs_cogs(revenue, gp, 504), 504)
    result = (g - base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-vs-opinc rank × close
def f25gvc_f25_growth_vs_cost_revvopincrank_252d_base_v143_signal(revenue, opinc, closeadj):
    opex = revenue - opinc
    g = _f25_revenue_vs_opex(revenue, opex, 63)
    result = g.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-vs-cogs rank × close
def f25gvc_f25_growth_vs_cost_revvcogsrank_252d_base_v144_signal(revenue, gp, closeadj):
    g = _f25_revenue_vs_cogs(revenue, gp, 63)
    result = g.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-vs-opinc EMA × close
def f25gvc_f25_growth_vs_cost_revvopincema_252d_base_v145_signal(revenue, opinc, closeadj):
    opex = revenue - opinc
    g = _f25_revenue_vs_opex(revenue, opex, 252)
    result = g.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue-vs-opinc EMA × close
def f25gvc_f25_growth_vs_cost_revvopincema_21d_base_v146_signal(revenue, opinc, closeadj):
    opex = revenue - opinc
    g = _f25_revenue_vs_opex(revenue, opex, 21)
    result = g.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-vs-cogs EMA × close
def f25gvc_f25_growth_vs_cost_revvcogsema_252d_base_v147_signal(revenue, gp, closeadj):
    g = _f25_revenue_vs_cogs(revenue, gp, 252)
    result = g.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue-vs-cogs EMA × close
def f25gvc_f25_growth_vs_cost_revvcogsema_21d_base_v148_signal(revenue, gp, closeadj):
    g = _f25_revenue_vs_cogs(revenue, gp, 21)
    result = g.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# composite: 252d gvc + 252d revenue-vs-cogs × revenue × close
def f25gvc_f25_growth_vs_cost_compositetraj_252d_base_v149_signal(revenue, gp, closeadj):
    opex = revenue - gp
    result = (_f25_growth_vs_cost(revenue, opex, 252) + _f25_revenue_vs_cogs(revenue, gp, 252)) * revenue * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# composite: 252d gvc + 252d revenue-vs-opinc × revenue × close
def f25gvc_f25_growth_vs_cost_compositetraj2_252d_base_v150_signal(revenue, gp, opinc, closeadj):
    opex_g = revenue - gp
    opex_o = revenue - opinc
    result = (_f25_growth_vs_cost(revenue, opex_g, 252) + _f25_revenue_vs_opex(revenue, opex_o, 252)) * revenue * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f25gvc_f25_growth_vs_cost_gvcxmcap_21d_base_v076_signal,
    f25gvc_f25_growth_vs_cost_gvcxmcap_504d_base_v077_signal,
    f25gvc_f25_growth_vs_cost_revvcogsxrevprice_252d_base_v078_signal,
    f25gvc_f25_growth_vs_cost_revvcogsxrevprice_21d_base_v079_signal,
    f25gvc_f25_growth_vs_cost_revvopincxrevprice_252d_base_v080_signal,
    f25gvc_f25_growth_vs_cost_gvcminusrvc_252d_base_v081_signal,
    f25gvc_f25_growth_vs_cost_gvcminusrvc_21d_base_v082_signal,
    f25gvc_f25_growth_vs_cost_gvcanom_252d_base_v083_signal,
    f25gvc_f25_growth_vs_cost_gvcanom_63d_base_v084_signal,
    f25gvc_f25_growth_vs_cost_gvcrank_252d_base_v085_signal,
    f25gvc_f25_growth_vs_cost_gvcrank63_252d_base_v086_signal,
    f25gvc_f25_growth_vs_cost_gvcworst_504d_base_v087_signal,
    f25gvc_f25_growth_vs_cost_gvcbest_504d_base_v088_signal,
    f25gvc_f25_growth_vs_cost_gvcxebitdaprice_21d_base_v089_signal,
    f25gvc_f25_growth_vs_cost_gvcxebitdaprice_63d_base_v090_signal,
    f25gvc_f25_growth_vs_cost_gvcxgpopgap_252d_base_v091_signal,
    f25gvc_f25_growth_vs_cost_gvcxnet_252d_base_v092_signal,
    f25gvc_f25_growth_vs_cost_gvcxnetal_252d_base_v093_signal,
    f25gvc_f25_growth_vs_cost_gvcxrevcapex_252d_base_v094_signal,
    f25gvc_f25_growth_vs_cost_revvopincxebitda_21d_base_v095_signal,
    f25gvc_f25_growth_vs_cost_revvopincxebitda_252d_base_v096_signal,
    f25gvc_f25_growth_vs_cost_revvopincxrev_252d_base_v097_signal,
    f25gvc_f25_growth_vs_cost_revvcogsxmcap_21d_base_v098_signal,
    f25gvc_f25_growth_vs_cost_revvcogsxmcap_252d_base_v099_signal,
    f25gvc_f25_growth_vs_cost_revvcogsxmcap_504d_base_v100_signal,
    f25gvc_f25_growth_vs_cost_gvcxintexp_21d_base_v101_signal,
    f25gvc_f25_growth_vs_cost_gvcxtax_21d_base_v102_signal,
    f25gvc_f25_growth_vs_cost_gvcxncfo_21d_base_v103_signal,
    f25gvc_f25_growth_vs_cost_gvcxfcf_21d_base_v104_signal,
    f25gvc_f25_growth_vs_cost_gvcxni_21d_base_v105_signal,
    f25gvc_f25_growth_vs_cost_gvcxni_63d_base_v106_signal,
    f25gvc_f25_growth_vs_cost_gvcxwc_21d_base_v107_signal,
    f25gvc_f25_growth_vs_cost_gvcxdebt_63d_base_v108_signal,
    f25gvc_f25_growth_vs_cost_gvcxassets_63d_base_v109_signal,
    f25gvc_f25_growth_vs_cost_gvcxequity_63d_base_v110_signal,
    f25gvc_f25_growth_vs_cost_gvcxliab_63d_base_v111_signal,
    f25gvc_f25_growth_vs_cost_gvcxre_63d_base_v112_signal,
    f25gvc_f25_growth_vs_cost_gvcxebitda_63d_base_v113_signal,
    f25gvc_f25_growth_vs_cost_gvcxncfo_63d_base_v114_signal,
    f25gvc_f25_growth_vs_cost_gvcxfcf_63d_base_v115_signal,
    f25gvc_f25_growth_vs_cost_gvcxncff_21d_base_v116_signal,
    f25gvc_f25_growth_vs_cost_revvcogsxncfo_252d_base_v117_signal,
    f25gvc_f25_growth_vs_cost_revvcogsxprice_21d_base_v118_signal,
    f25gvc_f25_growth_vs_cost_revvcogsxebitdaprice_21d_base_v119_signal,
    f25gvc_f25_growth_vs_cost_revvcogsxebitdaprice_252d_base_v120_signal,
    f25gvc_f25_growth_vs_cost_revvopincprice_21d_base_v121_signal,
    f25gvc_f25_growth_vs_cost_revvopincxrevprice_21d_base_v122_signal,
    f25gvc_f25_growth_vs_cost_revvopincxmcap_252d_base_v123_signal,
    f25gvc_f25_growth_vs_cost_revvopincxmcap_21d_base_v124_signal,
    f25gvc_f25_growth_vs_cost_revvopincxdebt_252d_base_v125_signal,
    f25gvc_f25_growth_vs_cost_revvopincxequity_252d_base_v126_signal,
    f25gvc_f25_growth_vs_cost_revvopincxassets_252d_base_v127_signal,
    f25gvc_f25_growth_vs_cost_revvopincxeps_252d_base_v128_signal,
    f25gvc_f25_growth_vs_cost_revvopincxwc_252d_base_v129_signal,
    f25gvc_f25_growth_vs_cost_revvopincxcr_252d_base_v130_signal,
    f25gvc_f25_growth_vs_cost_revvopincxintexp_252d_base_v131_signal,
    f25gvc_f25_growth_vs_cost_revvopincxtax_252d_base_v132_signal,
    f25gvc_f25_growth_vs_cost_revvopincxliab_252d_base_v133_signal,
    f25gvc_f25_growth_vs_cost_revvopincxre_252d_base_v134_signal,
    f25gvc_f25_growth_vs_cost_revvopincxncfo_252d_base_v135_signal,
    f25gvc_f25_growth_vs_cost_revvopincxfcf_252d_base_v136_signal,
    f25gvc_f25_growth_vs_cost_revvopincxni_252d_base_v137_signal,
    f25gvc_f25_growth_vs_cost_revvopincxcapex_252d_base_v138_signal,
    f25gvc_f25_growth_vs_cost_revvopincxncff_252d_base_v139_signal,
    f25gvc_f25_growth_vs_cost_revvopincxeps_21d_base_v140_signal,
    f25gvc_f25_growth_vs_cost_revvopincanom_252d_base_v141_signal,
    f25gvc_f25_growth_vs_cost_revvcogsanom_252d_base_v142_signal,
    f25gvc_f25_growth_vs_cost_revvopincrank_252d_base_v143_signal,
    f25gvc_f25_growth_vs_cost_revvcogsrank_252d_base_v144_signal,
    f25gvc_f25_growth_vs_cost_revvopincema_252d_base_v145_signal,
    f25gvc_f25_growth_vs_cost_revvopincema_21d_base_v146_signal,
    f25gvc_f25_growth_vs_cost_revvcogsema_252d_base_v147_signal,
    f25gvc_f25_growth_vs_cost_revvcogsema_21d_base_v148_signal,
    f25gvc_f25_growth_vs_cost_compositetraj_252d_base_v149_signal,
    f25gvc_f25_growth_vs_cost_compositetraj2_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F25_GROWTH_VS_COST_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f25_growth_vs_cost", "_f25_revenue_vs_opex", "_f25_revenue_vs_cogs")
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
    print(f"OK f25_growth_vs_cost_base_076_150_claude: {n_features} features pass")
