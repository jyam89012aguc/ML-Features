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


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


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


# 5d slope of 21d gvc × close
def f25gvc_f25_growth_vs_cost_revvopex_21d_slope_v001_signal(revenue, gp, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d gvc × close
def f25gvc_f25_growth_vs_cost_revvopex_21d_slope_v002_signal(revenue, gp, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d gvc × close
def f25gvc_f25_growth_vs_cost_revvopex_63d_slope_v003_signal(revenue, gp, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d gvc × close
def f25gvc_f25_growth_vs_cost_revvopex_63d_slope_v004_signal(revenue, gp, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d gvc × close
def f25gvc_f25_growth_vs_cost_revvopex_126d_slope_v005_signal(revenue, gp, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d gvc × close
def f25gvc_f25_growth_vs_cost_revvopex_126d_slope_v006_signal(revenue, gp, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d gvc × close
def f25gvc_f25_growth_vs_cost_revvopex_252d_slope_v007_signal(revenue, gp, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d gvc × close
def f25gvc_f25_growth_vs_cost_revvopex_252d_slope_v008_signal(revenue, gp, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d gvc × close
def f25gvc_f25_growth_vs_cost_revvopex_504d_slope_v009_signal(revenue, gp, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d gvc × close
def f25gvc_f25_growth_vs_cost_revvopex_504d_slope_v010_signal(revenue, gp, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d revenue-vs-opinc × close
def f25gvc_f25_growth_vs_cost_revvopinc_21d_slope_v011_signal(revenue, opinc, closeadj):
    opex = revenue - opinc
    base = _f25_revenue_vs_opex(revenue, opex, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d revenue-vs-opinc × close
def f25gvc_f25_growth_vs_cost_revvopinc_63d_slope_v012_signal(revenue, opinc, closeadj):
    opex = revenue - opinc
    base = _f25_revenue_vs_opex(revenue, opex, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d revenue-vs-opinc × close
def f25gvc_f25_growth_vs_cost_revvopinc_252d_slope_v013_signal(revenue, opinc, closeadj):
    opex = revenue - opinc
    base = _f25_revenue_vs_opex(revenue, opex, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d revenue-vs-opinc × close
def f25gvc_f25_growth_vs_cost_revvopinc_504d_slope_v014_signal(revenue, opinc, closeadj):
    opex = revenue - opinc
    base = _f25_revenue_vs_opex(revenue, opex, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d revenue-vs-cogs × close
def f25gvc_f25_growth_vs_cost_revvcogs_63d_slope_v015_signal(revenue, gp, closeadj):
    base = _f25_revenue_vs_cogs(revenue, gp, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d revenue-vs-cogs × close
def f25gvc_f25_growth_vs_cost_revvcogs_252d_slope_v016_signal(revenue, gp, closeadj):
    base = _f25_revenue_vs_cogs(revenue, gp, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d revenue-vs-cogs × close
def f25gvc_f25_growth_vs_cost_revvcogs_504d_slope_v017_signal(revenue, gp, closeadj):
    base = _f25_revenue_vs_cogs(revenue, gp, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d gvc mean × close
def f25gvc_f25_growth_vs_cost_gvcmean_63d_slope_v018_signal(revenue, gp, closeadj):
    opex = revenue - gp
    base = _mean(_f25_growth_vs_cost(revenue, opex, 63), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d gvc mean × close
def f25gvc_f25_growth_vs_cost_gvcmean_252d_slope_v019_signal(revenue, gp, closeadj):
    opex = revenue - gp
    base = _mean(_f25_growth_vs_cost(revenue, opex, 252), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d gvc std × close
def f25gvc_f25_growth_vs_cost_gvcstd_63d_slope_v020_signal(revenue, gp, closeadj):
    opex = revenue - gp
    base = _std(_f25_growth_vs_cost(revenue, opex, 63), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d gvc std × close
def f25gvc_f25_growth_vs_cost_gvcstd_252d_slope_v021_signal(revenue, gp, closeadj):
    opex = revenue - gp
    base = _std(_f25_growth_vs_cost(revenue, opex, 252), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d gvc zscore
def f25gvc_f25_growth_vs_cost_gvcz_252d_slope_v022_signal(revenue, gp, closeadj):
    opex = revenue - gp
    base = _z(_f25_growth_vs_cost(revenue, opex, 63), 252)
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d gvc zscore
def f25gvc_f25_growth_vs_cost_gvcz_504d_slope_v023_signal(revenue, gp, closeadj):
    opex = revenue - gp
    base = _z(_f25_growth_vs_cost(revenue, opex, 252), 504)
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d gvc pos count × close
def f25gvc_f25_growth_vs_cost_gvcposcount_252d_slope_v024_signal(revenue, gp, closeadj):
    opex = revenue - gp
    flag = (_f25_growth_vs_cost(revenue, opex, 63) > 0).astype(float)
    base = flag.rolling(252, min_periods=63).sum() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d gvc neg count × close
def f25gvc_f25_growth_vs_cost_gvcnegcount_504d_slope_v025_signal(revenue, gp, closeadj):
    opex = revenue - gp
    flag = (_f25_growth_vs_cost(revenue, opex, 252) < 0).astype(float)
    base = flag.rolling(504, min_periods=126).sum() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d gvc high count × close
def f25gvc_f25_growth_vs_cost_gvchighcount_252d_slope_v026_signal(revenue, gp, closeadj):
    opex = revenue - gp
    flag = (_f25_growth_vs_cost(revenue, opex, 63) > 0.05).astype(float)
    base = flag.rolling(252, min_periods=63).sum() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d gvc squared × close
def f25gvc_f25_growth_vs_cost_gvcsq_21d_slope_v027_signal(revenue, gp, closeadj):
    opex = revenue - gp
    g = _f25_growth_vs_cost(revenue, opex, 21)
    base = g * g.abs() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d gvc squared × close
def f25gvc_f25_growth_vs_cost_gvcsq_63d_slope_v028_signal(revenue, gp, closeadj):
    opex = revenue - gp
    g = _f25_growth_vs_cost(revenue, opex, 63)
    base = g * g.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d gvc squared × close
def f25gvc_f25_growth_vs_cost_gvcsq_252d_slope_v029_signal(revenue, gp, closeadj):
    opex = revenue - gp
    g = _f25_growth_vs_cost(revenue, opex, 252)
    base = g * g.abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d gvc × revenue
def f25gvc_f25_growth_vs_cost_gvcxrev_21d_slope_v030_signal(revenue, gp, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 21) * revenue
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d gvc × revenue
def f25gvc_f25_growth_vs_cost_gvcxrev_63d_slope_v031_signal(revenue, gp, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 63) * revenue
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d gvc × revenue
def f25gvc_f25_growth_vs_cost_gvcxrev_252d_slope_v032_signal(revenue, gp, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 252) * revenue
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d gvc × ebitda
def f25gvc_f25_growth_vs_cost_gvcxebitda_21d_slope_v033_signal(revenue, gp, ebitda, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 21) * ebitda
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d gvc × ebitda
def f25gvc_f25_growth_vs_cost_gvcxebitda_252d_slope_v034_signal(revenue, gp, ebitda, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 252) * ebitda
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d gvc × netinc
def f25gvc_f25_growth_vs_cost_gvcxni_252d_slope_v035_signal(revenue, gp, netinc, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 252) * netinc
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of gvc diff 21m63 × close
def f25gvc_f25_growth_vs_cost_gvcdiff_21m63_slope_v036_signal(revenue, gp, closeadj):
    opex = revenue - gp
    base = (_f25_growth_vs_cost(revenue, opex, 21) - _f25_growth_vs_cost(revenue, opex, 63)) * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of gvc diff 63m252 × close
def f25gvc_f25_growth_vs_cost_gvcdiff_63m252_slope_v037_signal(revenue, gp, closeadj):
    opex = revenue - gp
    base = (_f25_growth_vs_cost(revenue, opex, 63) - _f25_growth_vs_cost(revenue, opex, 252)) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gvc diff 252m504 × close
def f25gvc_f25_growth_vs_cost_gvcdiff_252m504_slope_v038_signal(revenue, gp, closeadj):
    opex = revenue - gp
    base = (_f25_growth_vs_cost(revenue, opex, 252) - _f25_growth_vs_cost(revenue, opex, 504)) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of gvc ratio 63v252 × close
def f25gvc_f25_growth_vs_cost_gvcratio_63v252_slope_v039_signal(revenue, gp, closeadj):
    opex = revenue - gp
    a = _f25_growth_vs_cost(revenue, opex, 63)
    b = _f25_growth_vs_cost(revenue, opex, 252).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of gvc ratio 21v63 × close
def f25gvc_f25_growth_vs_cost_gvcratio_21v63_slope_v040_signal(revenue, gp, closeadj):
    opex = revenue - gp
    a = _f25_growth_vs_cost(revenue, opex, 21)
    b = _f25_growth_vs_cost(revenue, opex, 63).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gvc product 63x252 × close
def f25gvc_f25_growth_vs_cost_gvcprod_63x252_slope_v041_signal(revenue, gp, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 63) * _f25_growth_vs_cost(revenue, opex, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d revenue-vs-cogs × ebitda
def f25gvc_f25_growth_vs_cost_revvcogsxebitda_21d_slope_v042_signal(revenue, gp, ebitda, closeadj):
    base = _f25_revenue_vs_cogs(revenue, gp, 21) * ebitda
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d revenue-vs-cogs × ebitda
def f25gvc_f25_growth_vs_cost_revvcogsxebitda_252d_slope_v043_signal(revenue, gp, ebitda, closeadj):
    base = _f25_revenue_vs_cogs(revenue, gp, 252) * ebitda
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d max gvc × close
def f25gvc_f25_growth_vs_cost_gvcmax_63d_slope_v044_signal(revenue, gp, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 21).rolling(63, min_periods=21).max() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d max gvc × close
def f25gvc_f25_growth_vs_cost_gvcmax_252d_slope_v045_signal(revenue, gp, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 63).rolling(252, min_periods=63).max() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d min gvc × close
def f25gvc_f25_growth_vs_cost_gvcmin_63d_slope_v046_signal(revenue, gp, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 21).rolling(63, min_periods=21).min() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sum gvc × close
def f25gvc_f25_growth_vs_cost_gvcsum_252d_slope_v047_signal(revenue, gp, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 21).rolling(252, min_periods=63).sum() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d gvc area × close
def f25gvc_f25_growth_vs_cost_gvcarea_252d_slope_v048_signal(revenue, gp, closeadj):
    opex = revenue - gp
    g = _f25_growth_vs_cost(revenue, opex, 63).abs()
    base = g.rolling(252, min_periods=63).sum() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d gvc area × close
def f25gvc_f25_growth_vs_cost_gvcarea_504d_slope_v049_signal(revenue, gp, closeadj):
    opex = revenue - gp
    g = _f25_growth_vs_cost(revenue, opex, 252).abs()
    base = g.rolling(504, min_periods=126).sum() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d gvc × capex
def f25gvc_f25_growth_vs_cost_gvcxcapex_21d_slope_v050_signal(revenue, gp, capex, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 21) * capex.abs()
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d gvc × capex
def f25gvc_f25_growth_vs_cost_gvcxcapex_252d_slope_v051_signal(revenue, gp, capex, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 252) * capex.abs()
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d gvc × ncfo
def f25gvc_f25_growth_vs_cost_gvcxncfo_252d_slope_v052_signal(revenue, gp, ncfo, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 252) * ncfo
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d gvc × fcf
def f25gvc_f25_growth_vs_cost_gvcxfcf_252d_slope_v053_signal(revenue, gp, fcf, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 252) * fcf
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d gvc EMA × close
def f25gvc_f25_growth_vs_cost_gvcema_21d_slope_v054_signal(revenue, gp, closeadj):
    opex = revenue - gp
    g = _f25_growth_vs_cost(revenue, opex, 21)
    base = g.ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d gvc EMA × close
def f25gvc_f25_growth_vs_cost_gvcema_63d_slope_v055_signal(revenue, gp, closeadj):
    opex = revenue - gp
    g = _f25_growth_vs_cost(revenue, opex, 63)
    base = g.ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d gvc EMA × close
def f25gvc_f25_growth_vs_cost_gvcema_252d_slope_v056_signal(revenue, gp, closeadj):
    opex = revenue - gp
    g = _f25_growth_vs_cost(revenue, opex, 252)
    base = g.ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 5d gvc × close
def f25gvc_f25_growth_vs_cost_revvopex_5d_slope_v057_signal(revenue, gp, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 5) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 10d gvc × close
def f25gvc_f25_growth_vs_cost_revvopex_10d_slope_v058_signal(revenue, gp, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 10) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 42d gvc × close
def f25gvc_f25_growth_vs_cost_revvopex_42d_slope_v059_signal(revenue, gp, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 42) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 189d gvc × close
def f25gvc_f25_growth_vs_cost_revvopex_189d_slope_v060_signal(revenue, gp, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 189) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 378d gvc × close
def f25gvc_f25_growth_vs_cost_revvopex_378d_slope_v061_signal(revenue, gp, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d gvc × mcap
def f25gvc_f25_growth_vs_cost_gvcxmcap_252d_slope_v062_signal(revenue, gp, closeadj, sharesbas):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 252) * (closeadj * sharesbas)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d gvc × mcap
def f25gvc_f25_growth_vs_cost_gvcxmcap_63d_slope_v063_signal(revenue, gp, closeadj, sharesbas):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 63) * (closeadj * sharesbas)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d gvc × equity
def f25gvc_f25_growth_vs_cost_gvcxequity_21d_slope_v064_signal(revenue, gp, equity, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 21) * equity
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d gvc × equity
def f25gvc_f25_growth_vs_cost_gvcxequity_252d_slope_v065_signal(revenue, gp, equity, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 252) * equity
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d gvc × assets
def f25gvc_f25_growth_vs_cost_gvcxassets_252d_slope_v066_signal(revenue, gp, assets, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 252) * assets
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d gvc × debt
def f25gvc_f25_growth_vs_cost_gvcxdebt_252d_slope_v067_signal(revenue, gp, debt, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 252) * debt
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d gvc × eps × close
def f25gvc_f25_growth_vs_cost_gvcxeps_21d_slope_v068_signal(revenue, gp, eps, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 21) * eps * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d gvc × eps × close
def f25gvc_f25_growth_vs_cost_gvcxeps_252d_slope_v069_signal(revenue, gp, eps, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 252) * eps * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d gvc × wc
def f25gvc_f25_growth_vs_cost_gvcxwc_252d_slope_v070_signal(revenue, gp, workingcapital, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 252) * workingcapital
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d gvc × cr × close
def f25gvc_f25_growth_vs_cost_gvcxcr_21d_slope_v071_signal(revenue, gp, currentratio, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 21) * currentratio * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d gvc × cr × close
def f25gvc_f25_growth_vs_cost_gvcxcr_252d_slope_v072_signal(revenue, gp, currentratio, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 252) * currentratio * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d gvc × liab
def f25gvc_f25_growth_vs_cost_gvcxliab_252d_slope_v073_signal(revenue, gp, liabilities, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 252) * liabilities
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d gvc × retearn
def f25gvc_f25_growth_vs_cost_gvcxre_252d_slope_v074_signal(revenue, gp, retearn, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 252) * retearn
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d gvc × intexp
def f25gvc_f25_growth_vs_cost_gvcxintexp_252d_slope_v075_signal(revenue, gp, intexp, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 252) * intexp
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d gvc × tax
def f25gvc_f25_growth_vs_cost_gvcxtax_252d_slope_v076_signal(revenue, gp, taxexp, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 252) * taxexp
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d gvc × ncff
def f25gvc_f25_growth_vs_cost_gvcxncff_252d_slope_v077_signal(revenue, gp, ncff, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 252) * ncff.abs()
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d gvc × rev × close
def f25gvc_f25_growth_vs_cost_gvcxrevxprice_252d_slope_v078_signal(revenue, gp, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 252) * revenue * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d gvc × rev × close
def f25gvc_f25_growth_vs_cost_gvcxrevxprice_21d_slope_v079_signal(revenue, gp, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 21) * revenue * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d gvc × ebitda × close
def f25gvc_f25_growth_vs_cost_gvcxebitdaprice_252d_slope_v080_signal(revenue, gp, ebitda, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 252) * ebitda * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d gvc × mcap
def f25gvc_f25_growth_vs_cost_gvcxmcap_21d_slope_v081_signal(revenue, gp, closeadj, sharesbas):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 21) * (closeadj * sharesbas)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d gvc × mcap
def f25gvc_f25_growth_vs_cost_gvcxmcap_504d_slope_v082_signal(revenue, gp, closeadj, sharesbas):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 504) * (closeadj * sharesbas)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d revenue-vs-cogs × rev × close
def f25gvc_f25_growth_vs_cost_revvcogsxrevprice_252d_slope_v083_signal(revenue, gp, closeadj):
    base = _f25_revenue_vs_cogs(revenue, gp, 252) * revenue * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d revenue-vs-cogs × rev × close
def f25gvc_f25_growth_vs_cost_revvcogsxrevprice_21d_slope_v084_signal(revenue, gp, closeadj):
    base = _f25_revenue_vs_cogs(revenue, gp, 21) * revenue * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d revenue-vs-opinc × rev × close
def f25gvc_f25_growth_vs_cost_revvopincxrevprice_252d_slope_v085_signal(revenue, opinc, closeadj):
    opex = revenue - opinc
    base = _f25_revenue_vs_opex(revenue, opex, 252) * revenue * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d gvc weighted by gp ratio × close
def f25gvc_f25_growth_vs_cost_gvcminusrvc_252d_slope_v086_signal(revenue, gp, closeadj):
    opex = revenue - gp
    weight = gp / revenue.replace(0, np.nan).abs()
    base = _f25_growth_vs_cost(revenue, opex, 252) * weight * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d (gvc - revvcogs) × close
def f25gvc_f25_growth_vs_cost_gvcminusrvc_21d_slope_v087_signal(revenue, gp, closeadj):
    opex = revenue - gp
    weight = gp / revenue.replace(0, np.nan).abs()
    base = _f25_growth_vs_cost(revenue, opex, 21) * weight * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d gvc anomaly × close
def f25gvc_f25_growth_vs_cost_gvcanom_252d_slope_v088_signal(revenue, gp, closeadj):
    opex = revenue - gp
    g = _f25_growth_vs_cost(revenue, opex, 252)
    base = (g - _mean(_f25_growth_vs_cost(revenue, opex, 504), 504)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d gvc anomaly × close
def f25gvc_f25_growth_vs_cost_gvcanom_63d_slope_v089_signal(revenue, gp, closeadj):
    opex = revenue - gp
    g = _f25_growth_vs_cost(revenue, opex, 63)
    base = (g - _mean(_f25_growth_vs_cost(revenue, opex, 252), 252)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d gvc rank × close
def f25gvc_f25_growth_vs_cost_gvcrank_252d_slope_v090_signal(revenue, gp, closeadj):
    opex = revenue - gp
    g = _f25_growth_vs_cost(revenue, opex, 21)
    base = g.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d gvc rank63 × close
def f25gvc_f25_growth_vs_cost_gvcrank63_252d_slope_v091_signal(revenue, gp, closeadj):
    opex = revenue - gp
    g = _f25_growth_vs_cost(revenue, opex, 63)
    base = g.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of expanding worst gvc × close
def f25gvc_f25_growth_vs_cost_gvcworst_504d_slope_v092_signal(revenue, gp, closeadj):
    opex = revenue - gp
    g = _f25_growth_vs_cost(revenue, opex, 252)
    base = g.expanding(min_periods=63).min() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of expanding best gvc × close
def f25gvc_f25_growth_vs_cost_gvcbest_504d_slope_v093_signal(revenue, gp, closeadj):
    opex = revenue - gp
    g = _f25_growth_vs_cost(revenue, opex, 252)
    base = g.expanding(min_periods=63).max() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d gvc × ebitda × close
def f25gvc_f25_growth_vs_cost_gvcxebitdaprice_21d_slope_v094_signal(revenue, gp, ebitda, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 21) * ebitda * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d gvc × ebitda × close
def f25gvc_f25_growth_vs_cost_gvcxebitdaprice_63d_slope_v095_signal(revenue, gp, ebitda, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 63) * ebitda * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d gvc × (gp - opinc) × close
def f25gvc_f25_growth_vs_cost_gvcxgpopgap_252d_slope_v096_signal(revenue, gp, opinc, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 252) * (gp - opinc) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d gvc × (assets - debt)
def f25gvc_f25_growth_vs_cost_gvcxnet_252d_slope_v097_signal(revenue, gp, assets, debt, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 252) * (assets - debt)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d gvc × (assets - liab)
def f25gvc_f25_growth_vs_cost_gvcxnetal_252d_slope_v098_signal(revenue, gp, assets, liabilities, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 252) * (assets - liabilities)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d gvc × (rev - capex)
def f25gvc_f25_growth_vs_cost_gvcxrevcapex_252d_slope_v099_signal(revenue, gp, capex, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 252) * (revenue - capex.abs())
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d revenue-vs-opinc × ebitda
def f25gvc_f25_growth_vs_cost_revvopincxebitda_21d_slope_v100_signal(revenue, opinc, ebitda, closeadj):
    opex = revenue - opinc
    base = _f25_revenue_vs_opex(revenue, opex, 21) * ebitda
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d revenue-vs-opinc × ebitda
def f25gvc_f25_growth_vs_cost_revvopincxebitda_252d_slope_v101_signal(revenue, opinc, ebitda, closeadj):
    opex = revenue - opinc
    base = _f25_revenue_vs_opex(revenue, opex, 252) * ebitda
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d revenue-vs-opinc × revenue
def f25gvc_f25_growth_vs_cost_revvopincxrev_252d_slope_v102_signal(revenue, opinc, closeadj):
    opex = revenue - opinc
    base = _f25_revenue_vs_opex(revenue, opex, 252) * revenue
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d revenue-vs-cogs × mcap
def f25gvc_f25_growth_vs_cost_revvcogsxmcap_21d_slope_v103_signal(revenue, gp, closeadj, sharesbas):
    base = _f25_revenue_vs_cogs(revenue, gp, 21) * (closeadj * sharesbas)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d revenue-vs-cogs × mcap
def f25gvc_f25_growth_vs_cost_revvcogsxmcap_252d_slope_v104_signal(revenue, gp, closeadj, sharesbas):
    base = _f25_revenue_vs_cogs(revenue, gp, 252) * (closeadj * sharesbas)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d revenue-vs-cogs × mcap
def f25gvc_f25_growth_vs_cost_revvcogsxmcap_504d_slope_v105_signal(revenue, gp, closeadj, sharesbas):
    base = _f25_revenue_vs_cogs(revenue, gp, 504) * (closeadj * sharesbas)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d gvc × intexp
def f25gvc_f25_growth_vs_cost_gvcxintexp_21d_slope_v106_signal(revenue, gp, intexp, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 21) * intexp
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d gvc × tax
def f25gvc_f25_growth_vs_cost_gvcxtax_21d_slope_v107_signal(revenue, gp, taxexp, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 21) * taxexp
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d gvc × ncfo
def f25gvc_f25_growth_vs_cost_gvcxncfo_21d_slope_v108_signal(revenue, gp, ncfo, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 21) * ncfo
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d gvc × fcf
def f25gvc_f25_growth_vs_cost_gvcxfcf_21d_slope_v109_signal(revenue, gp, fcf, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 21) * fcf
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d gvc × netinc
def f25gvc_f25_growth_vs_cost_gvcxni_21d_slope_v110_signal(revenue, gp, netinc, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 21) * netinc
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d gvc × netinc
def f25gvc_f25_growth_vs_cost_gvcxni_63d_slope_v111_signal(revenue, gp, netinc, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 63) * netinc
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d gvc × wc
def f25gvc_f25_growth_vs_cost_gvcxwc_21d_slope_v112_signal(revenue, gp, workingcapital, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 21) * workingcapital
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d gvc × debt
def f25gvc_f25_growth_vs_cost_gvcxdebt_63d_slope_v113_signal(revenue, gp, debt, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 63) * debt
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d gvc × assets
def f25gvc_f25_growth_vs_cost_gvcxassets_63d_slope_v114_signal(revenue, gp, assets, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 63) * assets
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d gvc × equity
def f25gvc_f25_growth_vs_cost_gvcxequity_63d_slope_v115_signal(revenue, gp, equity, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 63) * equity
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d gvc × liab
def f25gvc_f25_growth_vs_cost_gvcxliab_63d_slope_v116_signal(revenue, gp, liabilities, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 63) * liabilities
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d gvc × retearn
def f25gvc_f25_growth_vs_cost_gvcxre_63d_slope_v117_signal(revenue, gp, retearn, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 63) * retearn
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d gvc × ebitda
def f25gvc_f25_growth_vs_cost_gvcxebitda_63d_slope_v118_signal(revenue, gp, ebitda, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 63) * ebitda
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d gvc × ncfo
def f25gvc_f25_growth_vs_cost_gvcxncfo_63d_slope_v119_signal(revenue, gp, ncfo, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 63) * ncfo
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d gvc × fcf
def f25gvc_f25_growth_vs_cost_gvcxfcf_63d_slope_v120_signal(revenue, gp, fcf, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 63) * fcf
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d gvc × ncff
def f25gvc_f25_growth_vs_cost_gvcxncff_21d_slope_v121_signal(revenue, gp, ncff, closeadj):
    opex = revenue - gp
    base = _f25_growth_vs_cost(revenue, opex, 21) * ncff.abs()
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d revenue-vs-cogs × ncfo
def f25gvc_f25_growth_vs_cost_revvcogsxncfo_252d_slope_v122_signal(revenue, gp, ncfo, closeadj):
    base = _f25_revenue_vs_cogs(revenue, gp, 252) * ncfo
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d revenue-vs-cogs × close
def f25gvc_f25_growth_vs_cost_revvcogsxprice_21d_slope_v123_signal(revenue, gp, closeadj):
    base = _f25_revenue_vs_cogs(revenue, gp, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d revenue-vs-cogs × ebitda × close
def f25gvc_f25_growth_vs_cost_revvcogsxebitdaprice_21d_slope_v124_signal(revenue, gp, ebitda, closeadj):
    base = _f25_revenue_vs_cogs(revenue, gp, 21) * ebitda * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d revenue-vs-cogs × ebitda × close
def f25gvc_f25_growth_vs_cost_revvcogsxebitdaprice_252d_slope_v125_signal(revenue, gp, ebitda, closeadj):
    base = _f25_revenue_vs_cogs(revenue, gp, 252) * ebitda * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d revenue-vs-opinc × close
def f25gvc_f25_growth_vs_cost_revvopincprice_21d_slope_v126_signal(revenue, opinc, closeadj):
    opex = revenue - opinc
    base = _f25_revenue_vs_opex(revenue, opex, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d revenue-vs-opinc × rev × close
def f25gvc_f25_growth_vs_cost_revvopincxrevprice_21d_slope_v127_signal(revenue, opinc, closeadj):
    opex = revenue - opinc
    base = _f25_revenue_vs_opex(revenue, opex, 21) * revenue * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d revenue-vs-opinc × mcap
def f25gvc_f25_growth_vs_cost_revvopincxmcap_252d_slope_v128_signal(revenue, opinc, closeadj, sharesbas):
    opex = revenue - opinc
    base = _f25_revenue_vs_opex(revenue, opex, 252) * (closeadj * sharesbas)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d revenue-vs-opinc × mcap
def f25gvc_f25_growth_vs_cost_revvopincxmcap_21d_slope_v129_signal(revenue, opinc, closeadj, sharesbas):
    opex = revenue - opinc
    base = _f25_revenue_vs_opex(revenue, opex, 21) * (closeadj * sharesbas)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d revenue-vs-opinc × debt
def f25gvc_f25_growth_vs_cost_revvopincxdebt_252d_slope_v130_signal(revenue, opinc, debt, closeadj):
    opex = revenue - opinc
    base = _f25_revenue_vs_opex(revenue, opex, 252) * debt
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d revenue-vs-opinc × equity
def f25gvc_f25_growth_vs_cost_revvopincxequity_252d_slope_v131_signal(revenue, opinc, equity, closeadj):
    opex = revenue - opinc
    base = _f25_revenue_vs_opex(revenue, opex, 252) * equity
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d revenue-vs-opinc × assets
def f25gvc_f25_growth_vs_cost_revvopincxassets_252d_slope_v132_signal(revenue, opinc, assets, closeadj):
    opex = revenue - opinc
    base = _f25_revenue_vs_opex(revenue, opex, 252) * assets
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d revenue-vs-opinc × eps × close
def f25gvc_f25_growth_vs_cost_revvopincxeps_252d_slope_v133_signal(revenue, opinc, eps, closeadj):
    opex = revenue - opinc
    base = _f25_revenue_vs_opex(revenue, opex, 252) * eps * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d revenue-vs-opinc × wc
def f25gvc_f25_growth_vs_cost_revvopincxwc_252d_slope_v134_signal(revenue, opinc, workingcapital, closeadj):
    opex = revenue - opinc
    base = _f25_revenue_vs_opex(revenue, opex, 252) * workingcapital
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d revenue-vs-opinc × cr × close
def f25gvc_f25_growth_vs_cost_revvopincxcr_252d_slope_v135_signal(revenue, opinc, currentratio, closeadj):
    opex = revenue - opinc
    base = _f25_revenue_vs_opex(revenue, opex, 252) * currentratio * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d revenue-vs-opinc × intexp
def f25gvc_f25_growth_vs_cost_revvopincxintexp_252d_slope_v136_signal(revenue, opinc, intexp, closeadj):
    opex = revenue - opinc
    base = _f25_revenue_vs_opex(revenue, opex, 252) * intexp
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d revenue-vs-opinc × tax
def f25gvc_f25_growth_vs_cost_revvopincxtax_252d_slope_v137_signal(revenue, opinc, taxexp, closeadj):
    opex = revenue - opinc
    base = _f25_revenue_vs_opex(revenue, opex, 252) * taxexp
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d revenue-vs-opinc × liab
def f25gvc_f25_growth_vs_cost_revvopincxliab_252d_slope_v138_signal(revenue, opinc, liabilities, closeadj):
    opex = revenue - opinc
    base = _f25_revenue_vs_opex(revenue, opex, 252) * liabilities
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d revenue-vs-opinc × retearn
def f25gvc_f25_growth_vs_cost_revvopincxre_252d_slope_v139_signal(revenue, opinc, retearn, closeadj):
    opex = revenue - opinc
    base = _f25_revenue_vs_opex(revenue, opex, 252) * retearn
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d revenue-vs-opinc × ncfo
def f25gvc_f25_growth_vs_cost_revvopincxncfo_252d_slope_v140_signal(revenue, opinc, ncfo, closeadj):
    opex = revenue - opinc
    base = _f25_revenue_vs_opex(revenue, opex, 252) * ncfo
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d revenue-vs-opinc × fcf
def f25gvc_f25_growth_vs_cost_revvopincxfcf_252d_slope_v141_signal(revenue, opinc, fcf, closeadj):
    opex = revenue - opinc
    base = _f25_revenue_vs_opex(revenue, opex, 252) * fcf
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d revenue-vs-opinc × ni
def f25gvc_f25_growth_vs_cost_revvopincxni_252d_slope_v142_signal(revenue, opinc, netinc, closeadj):
    opex = revenue - opinc
    base = _f25_revenue_vs_opex(revenue, opex, 252) * netinc
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d revenue-vs-opinc × capex
def f25gvc_f25_growth_vs_cost_revvopincxcapex_252d_slope_v143_signal(revenue, opinc, capex, closeadj):
    opex = revenue - opinc
    base = _f25_revenue_vs_opex(revenue, opex, 252) * capex.abs()
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d revenue-vs-opinc × ncff
def f25gvc_f25_growth_vs_cost_revvopincxncff_252d_slope_v144_signal(revenue, opinc, ncff, closeadj):
    opex = revenue - opinc
    base = _f25_revenue_vs_opex(revenue, opex, 252) * ncff.abs()
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d revenue-vs-opinc × eps × close
def f25gvc_f25_growth_vs_cost_revvopincxeps_21d_slope_v145_signal(revenue, opinc, eps, closeadj):
    opex = revenue - opinc
    base = _f25_revenue_vs_opex(revenue, opex, 21) * eps * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d revenue-vs-opinc anomaly × close
def f25gvc_f25_growth_vs_cost_revvopincanom_252d_slope_v146_signal(revenue, opinc, closeadj):
    opex = revenue - opinc
    g = _f25_revenue_vs_opex(revenue, opex, 252)
    base = (g - _mean(_f25_revenue_vs_opex(revenue, opex, 504), 504)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d revenue-vs-cogs anomaly × close
def f25gvc_f25_growth_vs_cost_revvcogsanom_252d_slope_v147_signal(revenue, gp, closeadj):
    g = _f25_revenue_vs_cogs(revenue, gp, 252)
    base = (g - _mean(_f25_revenue_vs_cogs(revenue, gp, 504), 504)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d revenue-vs-opinc rank × close
def f25gvc_f25_growth_vs_cost_revvopincrank_252d_slope_v148_signal(revenue, opinc, closeadj):
    opex = revenue - opinc
    g = _f25_revenue_vs_opex(revenue, opex, 63)
    base = g.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d composite × revenue × close
def f25gvc_f25_growth_vs_cost_compositetraj_252d_slope_v149_signal(revenue, gp, closeadj):
    opex = revenue - gp
    base = (_f25_growth_vs_cost(revenue, opex, 252) + _f25_revenue_vs_cogs(revenue, gp, 252)) * revenue * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d composite2 × revenue × close
def f25gvc_f25_growth_vs_cost_compositetraj2_252d_slope_v150_signal(revenue, gp, opinc, closeadj):
    opex_g = revenue - gp
    opex_o = revenue - opinc
    base = (_f25_growth_vs_cost(revenue, opex_g, 252) + _f25_revenue_vs_opex(revenue, opex_o, 252)) * revenue * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f25gvc_f25_growth_vs_cost_revvopex_21d_slope_v001_signal,
    f25gvc_f25_growth_vs_cost_revvopex_21d_slope_v002_signal,
    f25gvc_f25_growth_vs_cost_revvopex_63d_slope_v003_signal,
    f25gvc_f25_growth_vs_cost_revvopex_63d_slope_v004_signal,
    f25gvc_f25_growth_vs_cost_revvopex_126d_slope_v005_signal,
    f25gvc_f25_growth_vs_cost_revvopex_126d_slope_v006_signal,
    f25gvc_f25_growth_vs_cost_revvopex_252d_slope_v007_signal,
    f25gvc_f25_growth_vs_cost_revvopex_252d_slope_v008_signal,
    f25gvc_f25_growth_vs_cost_revvopex_504d_slope_v009_signal,
    f25gvc_f25_growth_vs_cost_revvopex_504d_slope_v010_signal,
    f25gvc_f25_growth_vs_cost_revvopinc_21d_slope_v011_signal,
    f25gvc_f25_growth_vs_cost_revvopinc_63d_slope_v012_signal,
    f25gvc_f25_growth_vs_cost_revvopinc_252d_slope_v013_signal,
    f25gvc_f25_growth_vs_cost_revvopinc_504d_slope_v014_signal,
    f25gvc_f25_growth_vs_cost_revvcogs_63d_slope_v015_signal,
    f25gvc_f25_growth_vs_cost_revvcogs_252d_slope_v016_signal,
    f25gvc_f25_growth_vs_cost_revvcogs_504d_slope_v017_signal,
    f25gvc_f25_growth_vs_cost_gvcmean_63d_slope_v018_signal,
    f25gvc_f25_growth_vs_cost_gvcmean_252d_slope_v019_signal,
    f25gvc_f25_growth_vs_cost_gvcstd_63d_slope_v020_signal,
    f25gvc_f25_growth_vs_cost_gvcstd_252d_slope_v021_signal,
    f25gvc_f25_growth_vs_cost_gvcz_252d_slope_v022_signal,
    f25gvc_f25_growth_vs_cost_gvcz_504d_slope_v023_signal,
    f25gvc_f25_growth_vs_cost_gvcposcount_252d_slope_v024_signal,
    f25gvc_f25_growth_vs_cost_gvcnegcount_504d_slope_v025_signal,
    f25gvc_f25_growth_vs_cost_gvchighcount_252d_slope_v026_signal,
    f25gvc_f25_growth_vs_cost_gvcsq_21d_slope_v027_signal,
    f25gvc_f25_growth_vs_cost_gvcsq_63d_slope_v028_signal,
    f25gvc_f25_growth_vs_cost_gvcsq_252d_slope_v029_signal,
    f25gvc_f25_growth_vs_cost_gvcxrev_21d_slope_v030_signal,
    f25gvc_f25_growth_vs_cost_gvcxrev_63d_slope_v031_signal,
    f25gvc_f25_growth_vs_cost_gvcxrev_252d_slope_v032_signal,
    f25gvc_f25_growth_vs_cost_gvcxebitda_21d_slope_v033_signal,
    f25gvc_f25_growth_vs_cost_gvcxebitda_252d_slope_v034_signal,
    f25gvc_f25_growth_vs_cost_gvcxni_252d_slope_v035_signal,
    f25gvc_f25_growth_vs_cost_gvcdiff_21m63_slope_v036_signal,
    f25gvc_f25_growth_vs_cost_gvcdiff_63m252_slope_v037_signal,
    f25gvc_f25_growth_vs_cost_gvcdiff_252m504_slope_v038_signal,
    f25gvc_f25_growth_vs_cost_gvcratio_63v252_slope_v039_signal,
    f25gvc_f25_growth_vs_cost_gvcratio_21v63_slope_v040_signal,
    f25gvc_f25_growth_vs_cost_gvcprod_63x252_slope_v041_signal,
    f25gvc_f25_growth_vs_cost_revvcogsxebitda_21d_slope_v042_signal,
    f25gvc_f25_growth_vs_cost_revvcogsxebitda_252d_slope_v043_signal,
    f25gvc_f25_growth_vs_cost_gvcmax_63d_slope_v044_signal,
    f25gvc_f25_growth_vs_cost_gvcmax_252d_slope_v045_signal,
    f25gvc_f25_growth_vs_cost_gvcmin_63d_slope_v046_signal,
    f25gvc_f25_growth_vs_cost_gvcsum_252d_slope_v047_signal,
    f25gvc_f25_growth_vs_cost_gvcarea_252d_slope_v048_signal,
    f25gvc_f25_growth_vs_cost_gvcarea_504d_slope_v049_signal,
    f25gvc_f25_growth_vs_cost_gvcxcapex_21d_slope_v050_signal,
    f25gvc_f25_growth_vs_cost_gvcxcapex_252d_slope_v051_signal,
    f25gvc_f25_growth_vs_cost_gvcxncfo_252d_slope_v052_signal,
    f25gvc_f25_growth_vs_cost_gvcxfcf_252d_slope_v053_signal,
    f25gvc_f25_growth_vs_cost_gvcema_21d_slope_v054_signal,
    f25gvc_f25_growth_vs_cost_gvcema_63d_slope_v055_signal,
    f25gvc_f25_growth_vs_cost_gvcema_252d_slope_v056_signal,
    f25gvc_f25_growth_vs_cost_revvopex_5d_slope_v057_signal,
    f25gvc_f25_growth_vs_cost_revvopex_10d_slope_v058_signal,
    f25gvc_f25_growth_vs_cost_revvopex_42d_slope_v059_signal,
    f25gvc_f25_growth_vs_cost_revvopex_189d_slope_v060_signal,
    f25gvc_f25_growth_vs_cost_revvopex_378d_slope_v061_signal,
    f25gvc_f25_growth_vs_cost_gvcxmcap_252d_slope_v062_signal,
    f25gvc_f25_growth_vs_cost_gvcxmcap_63d_slope_v063_signal,
    f25gvc_f25_growth_vs_cost_gvcxequity_21d_slope_v064_signal,
    f25gvc_f25_growth_vs_cost_gvcxequity_252d_slope_v065_signal,
    f25gvc_f25_growth_vs_cost_gvcxassets_252d_slope_v066_signal,
    f25gvc_f25_growth_vs_cost_gvcxdebt_252d_slope_v067_signal,
    f25gvc_f25_growth_vs_cost_gvcxeps_21d_slope_v068_signal,
    f25gvc_f25_growth_vs_cost_gvcxeps_252d_slope_v069_signal,
    f25gvc_f25_growth_vs_cost_gvcxwc_252d_slope_v070_signal,
    f25gvc_f25_growth_vs_cost_gvcxcr_21d_slope_v071_signal,
    f25gvc_f25_growth_vs_cost_gvcxcr_252d_slope_v072_signal,
    f25gvc_f25_growth_vs_cost_gvcxliab_252d_slope_v073_signal,
    f25gvc_f25_growth_vs_cost_gvcxre_252d_slope_v074_signal,
    f25gvc_f25_growth_vs_cost_gvcxintexp_252d_slope_v075_signal,
    f25gvc_f25_growth_vs_cost_gvcxtax_252d_slope_v076_signal,
    f25gvc_f25_growth_vs_cost_gvcxncff_252d_slope_v077_signal,
    f25gvc_f25_growth_vs_cost_gvcxrevxprice_252d_slope_v078_signal,
    f25gvc_f25_growth_vs_cost_gvcxrevxprice_21d_slope_v079_signal,
    f25gvc_f25_growth_vs_cost_gvcxebitdaprice_252d_slope_v080_signal,
    f25gvc_f25_growth_vs_cost_gvcxmcap_21d_slope_v081_signal,
    f25gvc_f25_growth_vs_cost_gvcxmcap_504d_slope_v082_signal,
    f25gvc_f25_growth_vs_cost_revvcogsxrevprice_252d_slope_v083_signal,
    f25gvc_f25_growth_vs_cost_revvcogsxrevprice_21d_slope_v084_signal,
    f25gvc_f25_growth_vs_cost_revvopincxrevprice_252d_slope_v085_signal,
    f25gvc_f25_growth_vs_cost_gvcminusrvc_252d_slope_v086_signal,
    f25gvc_f25_growth_vs_cost_gvcminusrvc_21d_slope_v087_signal,
    f25gvc_f25_growth_vs_cost_gvcanom_252d_slope_v088_signal,
    f25gvc_f25_growth_vs_cost_gvcanom_63d_slope_v089_signal,
    f25gvc_f25_growth_vs_cost_gvcrank_252d_slope_v090_signal,
    f25gvc_f25_growth_vs_cost_gvcrank63_252d_slope_v091_signal,
    f25gvc_f25_growth_vs_cost_gvcworst_504d_slope_v092_signal,
    f25gvc_f25_growth_vs_cost_gvcbest_504d_slope_v093_signal,
    f25gvc_f25_growth_vs_cost_gvcxebitdaprice_21d_slope_v094_signal,
    f25gvc_f25_growth_vs_cost_gvcxebitdaprice_63d_slope_v095_signal,
    f25gvc_f25_growth_vs_cost_gvcxgpopgap_252d_slope_v096_signal,
    f25gvc_f25_growth_vs_cost_gvcxnet_252d_slope_v097_signal,
    f25gvc_f25_growth_vs_cost_gvcxnetal_252d_slope_v098_signal,
    f25gvc_f25_growth_vs_cost_gvcxrevcapex_252d_slope_v099_signal,
    f25gvc_f25_growth_vs_cost_revvopincxebitda_21d_slope_v100_signal,
    f25gvc_f25_growth_vs_cost_revvopincxebitda_252d_slope_v101_signal,
    f25gvc_f25_growth_vs_cost_revvopincxrev_252d_slope_v102_signal,
    f25gvc_f25_growth_vs_cost_revvcogsxmcap_21d_slope_v103_signal,
    f25gvc_f25_growth_vs_cost_revvcogsxmcap_252d_slope_v104_signal,
    f25gvc_f25_growth_vs_cost_revvcogsxmcap_504d_slope_v105_signal,
    f25gvc_f25_growth_vs_cost_gvcxintexp_21d_slope_v106_signal,
    f25gvc_f25_growth_vs_cost_gvcxtax_21d_slope_v107_signal,
    f25gvc_f25_growth_vs_cost_gvcxncfo_21d_slope_v108_signal,
    f25gvc_f25_growth_vs_cost_gvcxfcf_21d_slope_v109_signal,
    f25gvc_f25_growth_vs_cost_gvcxni_21d_slope_v110_signal,
    f25gvc_f25_growth_vs_cost_gvcxni_63d_slope_v111_signal,
    f25gvc_f25_growth_vs_cost_gvcxwc_21d_slope_v112_signal,
    f25gvc_f25_growth_vs_cost_gvcxdebt_63d_slope_v113_signal,
    f25gvc_f25_growth_vs_cost_gvcxassets_63d_slope_v114_signal,
    f25gvc_f25_growth_vs_cost_gvcxequity_63d_slope_v115_signal,
    f25gvc_f25_growth_vs_cost_gvcxliab_63d_slope_v116_signal,
    f25gvc_f25_growth_vs_cost_gvcxre_63d_slope_v117_signal,
    f25gvc_f25_growth_vs_cost_gvcxebitda_63d_slope_v118_signal,
    f25gvc_f25_growth_vs_cost_gvcxncfo_63d_slope_v119_signal,
    f25gvc_f25_growth_vs_cost_gvcxfcf_63d_slope_v120_signal,
    f25gvc_f25_growth_vs_cost_gvcxncff_21d_slope_v121_signal,
    f25gvc_f25_growth_vs_cost_revvcogsxncfo_252d_slope_v122_signal,
    f25gvc_f25_growth_vs_cost_revvcogsxprice_21d_slope_v123_signal,
    f25gvc_f25_growth_vs_cost_revvcogsxebitdaprice_21d_slope_v124_signal,
    f25gvc_f25_growth_vs_cost_revvcogsxebitdaprice_252d_slope_v125_signal,
    f25gvc_f25_growth_vs_cost_revvopincprice_21d_slope_v126_signal,
    f25gvc_f25_growth_vs_cost_revvopincxrevprice_21d_slope_v127_signal,
    f25gvc_f25_growth_vs_cost_revvopincxmcap_252d_slope_v128_signal,
    f25gvc_f25_growth_vs_cost_revvopincxmcap_21d_slope_v129_signal,
    f25gvc_f25_growth_vs_cost_revvopincxdebt_252d_slope_v130_signal,
    f25gvc_f25_growth_vs_cost_revvopincxequity_252d_slope_v131_signal,
    f25gvc_f25_growth_vs_cost_revvopincxassets_252d_slope_v132_signal,
    f25gvc_f25_growth_vs_cost_revvopincxeps_252d_slope_v133_signal,
    f25gvc_f25_growth_vs_cost_revvopincxwc_252d_slope_v134_signal,
    f25gvc_f25_growth_vs_cost_revvopincxcr_252d_slope_v135_signal,
    f25gvc_f25_growth_vs_cost_revvopincxintexp_252d_slope_v136_signal,
    f25gvc_f25_growth_vs_cost_revvopincxtax_252d_slope_v137_signal,
    f25gvc_f25_growth_vs_cost_revvopincxliab_252d_slope_v138_signal,
    f25gvc_f25_growth_vs_cost_revvopincxre_252d_slope_v139_signal,
    f25gvc_f25_growth_vs_cost_revvopincxncfo_252d_slope_v140_signal,
    f25gvc_f25_growth_vs_cost_revvopincxfcf_252d_slope_v141_signal,
    f25gvc_f25_growth_vs_cost_revvopincxni_252d_slope_v142_signal,
    f25gvc_f25_growth_vs_cost_revvopincxcapex_252d_slope_v143_signal,
    f25gvc_f25_growth_vs_cost_revvopincxncff_252d_slope_v144_signal,
    f25gvc_f25_growth_vs_cost_revvopincxeps_21d_slope_v145_signal,
    f25gvc_f25_growth_vs_cost_revvopincanom_252d_slope_v146_signal,
    f25gvc_f25_growth_vs_cost_revvcogsanom_252d_slope_v147_signal,
    f25gvc_f25_growth_vs_cost_revvopincrank_252d_slope_v148_signal,
    f25gvc_f25_growth_vs_cost_compositetraj_252d_slope_v149_signal,
    f25gvc_f25_growth_vs_cost_compositetraj2_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F25_GROWTH_VS_COST_REGISTRY_SLOPE = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f25_growth_vs_cost_2nd_derivatives_001_150_claude: {n_features} features pass")
