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


# 21d revenue growth minus opex growth (gp-derived opex = revenue - gp)
def f25gvc_f25_growth_vs_cost_revvopex_21d_base_v001_signal(revenue, gp, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue growth minus opex growth
def f25gvc_f25_growth_vs_cost_revvopex_63d_base_v002_signal(revenue, gp, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d revenue vs opex growth
def f25gvc_f25_growth_vs_cost_revvopex_126d_base_v003_signal(revenue, gp, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue vs opex growth
def f25gvc_f25_growth_vs_cost_revvopex_252d_base_v004_signal(revenue, gp, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue vs opex growth
def f25gvc_f25_growth_vs_cost_revvopex_504d_base_v005_signal(revenue, gp, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue vs opex (proxy: opex = revenue - opinc)
def f25gvc_f25_growth_vs_cost_revvopinc_21d_base_v006_signal(revenue, opinc, closeadj):
    opex = revenue - opinc
    result = _f25_revenue_vs_opex(revenue, opex, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue vs opinc-derived opex
def f25gvc_f25_growth_vs_cost_revvopinc_63d_base_v007_signal(revenue, opinc, closeadj):
    opex = revenue - opinc
    result = _f25_revenue_vs_opex(revenue, opex, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue vs opinc-derived opex
def f25gvc_f25_growth_vs_cost_revvopinc_252d_base_v008_signal(revenue, opinc, closeadj):
    opex = revenue - opinc
    result = _f25_revenue_vs_opex(revenue, opex, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue vs opinc-derived opex
def f25gvc_f25_growth_vs_cost_revvopinc_504d_base_v009_signal(revenue, opinc, closeadj):
    opex = revenue - opinc
    result = _f25_revenue_vs_opex(revenue, opex, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue vs cogs (revenue - gp)
def f25gvc_f25_growth_vs_cost_revvcogs_63d_base_v010_signal(revenue, gp, closeadj):
    result = _f25_revenue_vs_cogs(revenue, gp, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue vs cogs
def f25gvc_f25_growth_vs_cost_revvcogs_252d_base_v011_signal(revenue, gp, closeadj):
    result = _f25_revenue_vs_cogs(revenue, gp, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue vs cogs
def f25gvc_f25_growth_vs_cost_revvcogs_504d_base_v012_signal(revenue, gp, closeadj):
    result = _f25_revenue_vs_cogs(revenue, gp, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 63d mean of revenue-vs-opex
def f25gvc_f25_growth_vs_cost_gvcmean_63d_base_v013_signal(revenue, gp, closeadj):
    opex = revenue - gp
    result = _mean(_f25_growth_vs_cost(revenue, opex, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 252d mean of revenue-vs-opex
def f25gvc_f25_growth_vs_cost_gvcmean_252d_base_v014_signal(revenue, gp, closeadj):
    opex = revenue - gp
    result = _mean(_f25_growth_vs_cost(revenue, opex, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 63d std of revenue-vs-opex
def f25gvc_f25_growth_vs_cost_gvcstd_63d_base_v015_signal(revenue, gp, closeadj):
    opex = revenue - gp
    result = _std(_f25_growth_vs_cost(revenue, opex, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 252d std of revenue-vs-opex
def f25gvc_f25_growth_vs_cost_gvcstd_252d_base_v016_signal(revenue, gp, closeadj):
    opex = revenue - gp
    result = _std(_f25_growth_vs_cost(revenue, opex, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of revenue-vs-opex
def f25gvc_f25_growth_vs_cost_gvcz_252d_base_v017_signal(revenue, gp, closeadj):
    opex = revenue - gp
    result = _z(_f25_growth_vs_cost(revenue, opex, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of revenue-vs-opex
def f25gvc_f25_growth_vs_cost_gvcz_504d_base_v018_signal(revenue, gp, closeadj):
    opex = revenue - gp
    result = _z(_f25_growth_vs_cost(revenue, opex, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of positive growth-vs-cost periods
def f25gvc_f25_growth_vs_cost_gvcposcount_252d_base_v019_signal(revenue, gp, closeadj):
    opex = revenue - gp
    flag = (_f25_growth_vs_cost(revenue, opex, 63) > 0).astype(float)
    result = flag.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of negative growth-vs-cost periods
def f25gvc_f25_growth_vs_cost_gvcnegcount_504d_base_v020_signal(revenue, gp, closeadj):
    opex = revenue - gp
    flag = (_f25_growth_vs_cost(revenue, opex, 252) < 0).astype(float)
    result = flag.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of high (>5%) growth-vs-cost
def f25gvc_f25_growth_vs_cost_gvchighcount_252d_base_v021_signal(revenue, gp, closeadj):
    opex = revenue - gp
    flag = (_f25_growth_vs_cost(revenue, opex, 63) > 0.05).astype(float)
    result = flag.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d squared growth-vs-cost × close
def f25gvc_f25_growth_vs_cost_gvcsq_21d_base_v022_signal(revenue, gp, closeadj):
    opex = revenue - gp
    g = _f25_growth_vs_cost(revenue, opex, 21)
    result = g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d squared growth-vs-cost × close
def f25gvc_f25_growth_vs_cost_gvcsq_63d_base_v023_signal(revenue, gp, closeadj):
    opex = revenue - gp
    g = _f25_growth_vs_cost(revenue, opex, 63)
    result = g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d squared growth-vs-cost × close
def f25gvc_f25_growth_vs_cost_gvcsq_252d_base_v024_signal(revenue, gp, closeadj):
    opex = revenue - gp
    g = _f25_growth_vs_cost(revenue, opex, 252)
    result = g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue-vs-opex × revenue
def f25gvc_f25_growth_vs_cost_gvcxrev_21d_base_v025_signal(revenue, gp, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 21) * revenue
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue-vs-opex × revenue
def f25gvc_f25_growth_vs_cost_gvcxrev_63d_base_v026_signal(revenue, gp, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 63) * revenue
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-vs-opex × revenue
def f25gvc_f25_growth_vs_cost_gvcxrev_252d_base_v027_signal(revenue, gp, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 252) * revenue
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue-vs-opex × ebitda
def f25gvc_f25_growth_vs_cost_gvcxebitda_21d_base_v028_signal(revenue, gp, ebitda, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 21) * ebitda
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-vs-opex × ebitda
def f25gvc_f25_growth_vs_cost_gvcxebitda_252d_base_v029_signal(revenue, gp, ebitda, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 252) * ebitda
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-vs-opex × netinc
def f25gvc_f25_growth_vs_cost_gvcxni_252d_base_v030_signal(revenue, gp, netinc, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 252) * netinc
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gvc minus 63d gvc (acceleration)
def f25gvc_f25_growth_vs_cost_gvcdiff_21m63_base_v031_signal(revenue, gp, closeadj):
    opex = revenue - gp
    result = (_f25_growth_vs_cost(revenue, opex, 21) - _f25_growth_vs_cost(revenue, opex, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gvc minus 252d gvc
def f25gvc_f25_growth_vs_cost_gvcdiff_63m252_base_v032_signal(revenue, gp, closeadj):
    opex = revenue - gp
    result = (_f25_growth_vs_cost(revenue, opex, 63) - _f25_growth_vs_cost(revenue, opex, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gvc minus 504d gvc
def f25gvc_f25_growth_vs_cost_gvcdiff_252m504_base_v033_signal(revenue, gp, closeadj):
    opex = revenue - gp
    result = (_f25_growth_vs_cost(revenue, opex, 252) - _f25_growth_vs_cost(revenue, opex, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d / 252d gvc ratio × close
def f25gvc_f25_growth_vs_cost_gvcratio_63v252_base_v034_signal(revenue, gp, closeadj):
    opex = revenue - gp
    a = _f25_growth_vs_cost(revenue, opex, 63)
    b = _f25_growth_vs_cost(revenue, opex, 252).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d / 63d gvc ratio × close
def f25gvc_f25_growth_vs_cost_gvcratio_21v63_base_v035_signal(revenue, gp, closeadj):
    opex = revenue - gp
    a = _f25_growth_vs_cost(revenue, opex, 21)
    b = _f25_growth_vs_cost(revenue, opex, 63).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d × 252d gvc product (consistent operating leverage)
def f25gvc_f25_growth_vs_cost_gvcprod_63x252_base_v036_signal(revenue, gp, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 63) * _f25_growth_vs_cost(revenue, opex, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue-vs-cogs × ebitda
def f25gvc_f25_growth_vs_cost_revvcogsxebitda_21d_base_v037_signal(revenue, gp, ebitda, closeadj):
    result = _f25_revenue_vs_cogs(revenue, gp, 21) * ebitda
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-vs-cogs × ebitda
def f25gvc_f25_growth_vs_cost_revvcogsxebitda_252d_base_v038_signal(revenue, gp, ebitda, closeadj):
    result = _f25_revenue_vs_cogs(revenue, gp, 252) * ebitda
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 63d max gvc × close
def f25gvc_f25_growth_vs_cost_gvcmax_63d_base_v039_signal(revenue, gp, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 21).rolling(63, min_periods=21).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 252d max gvc × close
def f25gvc_f25_growth_vs_cost_gvcmax_252d_base_v040_signal(revenue, gp, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 63).rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 63d min gvc × close
def f25gvc_f25_growth_vs_cost_gvcmin_63d_base_v041_signal(revenue, gp, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 21).rolling(63, min_periods=21).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 252d sum of 21d gvc
def f25gvc_f25_growth_vs_cost_gvcsum_252d_base_v042_signal(revenue, gp, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 21).rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gvc area (abs)
def f25gvc_f25_growth_vs_cost_gvcarea_252d_base_v043_signal(revenue, gp, closeadj):
    opex = revenue - gp
    g = _f25_growth_vs_cost(revenue, opex, 63).abs()
    result = g.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d gvc area
def f25gvc_f25_growth_vs_cost_gvcarea_504d_base_v044_signal(revenue, gp, closeadj):
    opex = revenue - gp
    g = _f25_growth_vs_cost(revenue, opex, 252).abs()
    result = g.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gvc × abs(capex)
def f25gvc_f25_growth_vs_cost_gvcxcapex_21d_base_v045_signal(revenue, gp, capex, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 21) * capex.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gvc × abs(capex)
def f25gvc_f25_growth_vs_cost_gvcxcapex_252d_base_v046_signal(revenue, gp, capex, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 252) * capex.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-vs-opex × ncfo
def f25gvc_f25_growth_vs_cost_gvcxncfo_252d_base_v047_signal(revenue, gp, ncfo, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 252) * ncfo
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gvc × fcf
def f25gvc_f25_growth_vs_cost_gvcxfcf_252d_base_v048_signal(revenue, gp, fcf, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 252) * fcf
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gvc EMA × close
def f25gvc_f25_growth_vs_cost_gvcema_21d_base_v049_signal(revenue, gp, closeadj):
    opex = revenue - gp
    g = _f25_growth_vs_cost(revenue, opex, 21)
    result = g.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gvc EMA × close
def f25gvc_f25_growth_vs_cost_gvcema_63d_base_v050_signal(revenue, gp, closeadj):
    opex = revenue - gp
    g = _f25_growth_vs_cost(revenue, opex, 63)
    result = g.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gvc EMA × close
def f25gvc_f25_growth_vs_cost_gvcema_252d_base_v051_signal(revenue, gp, closeadj):
    opex = revenue - gp
    g = _f25_growth_vs_cost(revenue, opex, 252)
    result = g.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d revenue-vs-opex × close
def f25gvc_f25_growth_vs_cost_revvopex_5d_base_v052_signal(revenue, gp, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d revenue-vs-opex × close
def f25gvc_f25_growth_vs_cost_revvopex_10d_base_v053_signal(revenue, gp, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d revenue-vs-opex × close
def f25gvc_f25_growth_vs_cost_revvopex_42d_base_v054_signal(revenue, gp, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d revenue-vs-opex × close
def f25gvc_f25_growth_vs_cost_revvopex_189d_base_v055_signal(revenue, gp, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d revenue-vs-opex × close
def f25gvc_f25_growth_vs_cost_revvopex_378d_base_v056_signal(revenue, gp, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gvc × marketcap proxy
def f25gvc_f25_growth_vs_cost_gvcxmcap_252d_base_v057_signal(revenue, gp, closeadj, sharesbas):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 252) * (closeadj * sharesbas)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gvc × marketcap proxy
def f25gvc_f25_growth_vs_cost_gvcxmcap_63d_base_v058_signal(revenue, gp, closeadj, sharesbas):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 63) * (closeadj * sharesbas)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gvc × equity
def f25gvc_f25_growth_vs_cost_gvcxequity_21d_base_v059_signal(revenue, gp, equity, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 21) * equity
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gvc × equity
def f25gvc_f25_growth_vs_cost_gvcxequity_252d_base_v060_signal(revenue, gp, equity, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 252) * equity
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gvc × assets
def f25gvc_f25_growth_vs_cost_gvcxassets_252d_base_v061_signal(revenue, gp, assets, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 252) * assets
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gvc × debt
def f25gvc_f25_growth_vs_cost_gvcxdebt_252d_base_v062_signal(revenue, gp, debt, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 252) * debt
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gvc × eps × close
def f25gvc_f25_growth_vs_cost_gvcxeps_21d_base_v063_signal(revenue, gp, eps, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 21) * eps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gvc × eps × close
def f25gvc_f25_growth_vs_cost_gvcxeps_252d_base_v064_signal(revenue, gp, eps, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 252) * eps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gvc × workingcapital
def f25gvc_f25_growth_vs_cost_gvcxwc_252d_base_v065_signal(revenue, gp, workingcapital, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 252) * workingcapital
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gvc × currentratio × close
def f25gvc_f25_growth_vs_cost_gvcxcr_21d_base_v066_signal(revenue, gp, currentratio, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 21) * currentratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gvc × currentratio × close
def f25gvc_f25_growth_vs_cost_gvcxcr_252d_base_v067_signal(revenue, gp, currentratio, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 252) * currentratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gvc × liabilities
def f25gvc_f25_growth_vs_cost_gvcxliab_252d_base_v068_signal(revenue, gp, liabilities, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 252) * liabilities
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gvc × retearn
def f25gvc_f25_growth_vs_cost_gvcxre_252d_base_v069_signal(revenue, gp, retearn, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 252) * retearn
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gvc × intexp
def f25gvc_f25_growth_vs_cost_gvcxintexp_252d_base_v070_signal(revenue, gp, intexp, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 252) * intexp
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gvc × taxexp
def f25gvc_f25_growth_vs_cost_gvcxtax_252d_base_v071_signal(revenue, gp, taxexp, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 252) * taxexp
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gvc × abs(ncff)
def f25gvc_f25_growth_vs_cost_gvcxncff_252d_base_v072_signal(revenue, gp, ncff, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 252) * ncff.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gvc × revenue × close
def f25gvc_f25_growth_vs_cost_gvcxrevxprice_252d_base_v073_signal(revenue, gp, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 252) * revenue * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gvc × revenue × close
def f25gvc_f25_growth_vs_cost_gvcxrevxprice_21d_base_v074_signal(revenue, gp, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 21) * revenue * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gvc × ebitda × close
def f25gvc_f25_growth_vs_cost_gvcxebitdaprice_252d_base_v075_signal(revenue, gp, ebitda, closeadj):
    opex = revenue - gp
    result = _f25_growth_vs_cost(revenue, opex, 252) * ebitda * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f25gvc_f25_growth_vs_cost_revvopex_21d_base_v001_signal,
    f25gvc_f25_growth_vs_cost_revvopex_63d_base_v002_signal,
    f25gvc_f25_growth_vs_cost_revvopex_126d_base_v003_signal,
    f25gvc_f25_growth_vs_cost_revvopex_252d_base_v004_signal,
    f25gvc_f25_growth_vs_cost_revvopex_504d_base_v005_signal,
    f25gvc_f25_growth_vs_cost_revvopinc_21d_base_v006_signal,
    f25gvc_f25_growth_vs_cost_revvopinc_63d_base_v007_signal,
    f25gvc_f25_growth_vs_cost_revvopinc_252d_base_v008_signal,
    f25gvc_f25_growth_vs_cost_revvopinc_504d_base_v009_signal,
    f25gvc_f25_growth_vs_cost_revvcogs_63d_base_v010_signal,
    f25gvc_f25_growth_vs_cost_revvcogs_252d_base_v011_signal,
    f25gvc_f25_growth_vs_cost_revvcogs_504d_base_v012_signal,
    f25gvc_f25_growth_vs_cost_gvcmean_63d_base_v013_signal,
    f25gvc_f25_growth_vs_cost_gvcmean_252d_base_v014_signal,
    f25gvc_f25_growth_vs_cost_gvcstd_63d_base_v015_signal,
    f25gvc_f25_growth_vs_cost_gvcstd_252d_base_v016_signal,
    f25gvc_f25_growth_vs_cost_gvcz_252d_base_v017_signal,
    f25gvc_f25_growth_vs_cost_gvcz_504d_base_v018_signal,
    f25gvc_f25_growth_vs_cost_gvcposcount_252d_base_v019_signal,
    f25gvc_f25_growth_vs_cost_gvcnegcount_504d_base_v020_signal,
    f25gvc_f25_growth_vs_cost_gvchighcount_252d_base_v021_signal,
    f25gvc_f25_growth_vs_cost_gvcsq_21d_base_v022_signal,
    f25gvc_f25_growth_vs_cost_gvcsq_63d_base_v023_signal,
    f25gvc_f25_growth_vs_cost_gvcsq_252d_base_v024_signal,
    f25gvc_f25_growth_vs_cost_gvcxrev_21d_base_v025_signal,
    f25gvc_f25_growth_vs_cost_gvcxrev_63d_base_v026_signal,
    f25gvc_f25_growth_vs_cost_gvcxrev_252d_base_v027_signal,
    f25gvc_f25_growth_vs_cost_gvcxebitda_21d_base_v028_signal,
    f25gvc_f25_growth_vs_cost_gvcxebitda_252d_base_v029_signal,
    f25gvc_f25_growth_vs_cost_gvcxni_252d_base_v030_signal,
    f25gvc_f25_growth_vs_cost_gvcdiff_21m63_base_v031_signal,
    f25gvc_f25_growth_vs_cost_gvcdiff_63m252_base_v032_signal,
    f25gvc_f25_growth_vs_cost_gvcdiff_252m504_base_v033_signal,
    f25gvc_f25_growth_vs_cost_gvcratio_63v252_base_v034_signal,
    f25gvc_f25_growth_vs_cost_gvcratio_21v63_base_v035_signal,
    f25gvc_f25_growth_vs_cost_gvcprod_63x252_base_v036_signal,
    f25gvc_f25_growth_vs_cost_revvcogsxebitda_21d_base_v037_signal,
    f25gvc_f25_growth_vs_cost_revvcogsxebitda_252d_base_v038_signal,
    f25gvc_f25_growth_vs_cost_gvcmax_63d_base_v039_signal,
    f25gvc_f25_growth_vs_cost_gvcmax_252d_base_v040_signal,
    f25gvc_f25_growth_vs_cost_gvcmin_63d_base_v041_signal,
    f25gvc_f25_growth_vs_cost_gvcsum_252d_base_v042_signal,
    f25gvc_f25_growth_vs_cost_gvcarea_252d_base_v043_signal,
    f25gvc_f25_growth_vs_cost_gvcarea_504d_base_v044_signal,
    f25gvc_f25_growth_vs_cost_gvcxcapex_21d_base_v045_signal,
    f25gvc_f25_growth_vs_cost_gvcxcapex_252d_base_v046_signal,
    f25gvc_f25_growth_vs_cost_gvcxncfo_252d_base_v047_signal,
    f25gvc_f25_growth_vs_cost_gvcxfcf_252d_base_v048_signal,
    f25gvc_f25_growth_vs_cost_gvcema_21d_base_v049_signal,
    f25gvc_f25_growth_vs_cost_gvcema_63d_base_v050_signal,
    f25gvc_f25_growth_vs_cost_gvcema_252d_base_v051_signal,
    f25gvc_f25_growth_vs_cost_revvopex_5d_base_v052_signal,
    f25gvc_f25_growth_vs_cost_revvopex_10d_base_v053_signal,
    f25gvc_f25_growth_vs_cost_revvopex_42d_base_v054_signal,
    f25gvc_f25_growth_vs_cost_revvopex_189d_base_v055_signal,
    f25gvc_f25_growth_vs_cost_revvopex_378d_base_v056_signal,
    f25gvc_f25_growth_vs_cost_gvcxmcap_252d_base_v057_signal,
    f25gvc_f25_growth_vs_cost_gvcxmcap_63d_base_v058_signal,
    f25gvc_f25_growth_vs_cost_gvcxequity_21d_base_v059_signal,
    f25gvc_f25_growth_vs_cost_gvcxequity_252d_base_v060_signal,
    f25gvc_f25_growth_vs_cost_gvcxassets_252d_base_v061_signal,
    f25gvc_f25_growth_vs_cost_gvcxdebt_252d_base_v062_signal,
    f25gvc_f25_growth_vs_cost_gvcxeps_21d_base_v063_signal,
    f25gvc_f25_growth_vs_cost_gvcxeps_252d_base_v064_signal,
    f25gvc_f25_growth_vs_cost_gvcxwc_252d_base_v065_signal,
    f25gvc_f25_growth_vs_cost_gvcxcr_21d_base_v066_signal,
    f25gvc_f25_growth_vs_cost_gvcxcr_252d_base_v067_signal,
    f25gvc_f25_growth_vs_cost_gvcxliab_252d_base_v068_signal,
    f25gvc_f25_growth_vs_cost_gvcxre_252d_base_v069_signal,
    f25gvc_f25_growth_vs_cost_gvcxintexp_252d_base_v070_signal,
    f25gvc_f25_growth_vs_cost_gvcxtax_252d_base_v071_signal,
    f25gvc_f25_growth_vs_cost_gvcxncff_252d_base_v072_signal,
    f25gvc_f25_growth_vs_cost_gvcxrevxprice_252d_base_v073_signal,
    f25gvc_f25_growth_vs_cost_gvcxrevxprice_21d_base_v074_signal,
    f25gvc_f25_growth_vs_cost_gvcxebitdaprice_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F25_GROWTH_VS_COST_REGISTRY_001_075 = REGISTRY


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
    print(f"OK f25_growth_vs_cost_base_001_075_claude: {n_features} features pass")
