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


# ===== folder domain primitives (hypergrowth = continuous combo of high revgrowth + margin expansion + positive fcf) =====
def _f37_hypergrowth_growth_strength(revenue, w):
    g = revenue.pct_change(w)
    return (g - 0.30) * (g > -0.5).astype(float)


def _f37_hypergrowth_margin_expansion(netinc, revenue, w):
    m = _safe_div(netinc, revenue.abs())
    return _diff(m, w)


def _f37_hypergrowth_fcf_positivity(fcf, revenue, w):
    fm = _safe_div(fcf, revenue.abs())
    return fm * _mean(fm, w).clip(lower=-1.0, upper=1.0)


def _f37_hypergrowth_signature(revenue, netinc, fcf, w):
    g = _f37_hypergrowth_growth_strength(revenue, w)
    me = _f37_hypergrowth_margin_expansion(netinc, revenue, w)
    fp = _f37_hypergrowth_fcf_positivity(fcf, revenue, w)
    return g + me * 5.0 + fp


# 21d hypergrowth growth-strength signal × close
def f37hgs_f37_hypergrowth_signature_growthstrength_21d_base_v001_signal(revenue, closeadj):
    result = _f37_hypergrowth_growth_strength(revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d hypergrowth growth-strength signal × close
def f37hgs_f37_hypergrowth_signature_growthstrength_63d_base_v002_signal(revenue, closeadj):
    result = _f37_hypergrowth_growth_strength(revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d hypergrowth growth-strength signal × close
def f37hgs_f37_hypergrowth_signature_growthstrength_126d_base_v003_signal(revenue, closeadj):
    result = _f37_hypergrowth_growth_strength(revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d hypergrowth growth-strength signal × close
def f37hgs_f37_hypergrowth_signature_growthstrength_252d_base_v004_signal(revenue, closeadj):
    result = _f37_hypergrowth_growth_strength(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d hypergrowth margin-expansion (net) × close
def f37hgs_f37_hypergrowth_signature_marginexpansion_21d_base_v005_signal(netinc, revenue, closeadj):
    result = _f37_hypergrowth_margin_expansion(netinc, revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d hypergrowth margin-expansion × close
def f37hgs_f37_hypergrowth_signature_marginexpansion_63d_base_v006_signal(netinc, revenue, closeadj):
    result = _f37_hypergrowth_margin_expansion(netinc, revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d hypergrowth margin-expansion × close
def f37hgs_f37_hypergrowth_signature_marginexpansion_252d_base_v007_signal(netinc, revenue, closeadj):
    result = _f37_hypergrowth_margin_expansion(netinc, revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF positivity × close
def f37hgs_f37_hypergrowth_signature_fcfpositivity_21d_base_v008_signal(fcf, revenue, closeadj):
    result = _f37_hypergrowth_fcf_positivity(fcf, revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF positivity × close
def f37hgs_f37_hypergrowth_signature_fcfpositivity_63d_base_v009_signal(fcf, revenue, closeadj):
    result = _f37_hypergrowth_fcf_positivity(fcf, revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF positivity × close
def f37hgs_f37_hypergrowth_signature_fcfpositivity_252d_base_v010_signal(fcf, revenue, closeadj):
    result = _f37_hypergrowth_fcf_positivity(fcf, revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d composite signature × close
def f37hgs_f37_hypergrowth_signature_signature_21d_base_v011_signal(revenue, netinc, fcf, closeadj):
    result = _f37_hypergrowth_signature(revenue, netinc, fcf, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite signature × close
def f37hgs_f37_hypergrowth_signature_signature_63d_base_v012_signal(revenue, netinc, fcf, closeadj):
    result = _f37_hypergrowth_signature(revenue, netinc, fcf, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d composite signature × close
def f37hgs_f37_hypergrowth_signature_signature_126d_base_v013_signal(revenue, netinc, fcf, closeadj):
    result = _f37_hypergrowth_signature(revenue, netinc, fcf, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite signature × close
def f37hgs_f37_hypergrowth_signature_signature_252d_base_v014_signal(revenue, netinc, fcf, closeadj):
    result = _f37_hypergrowth_signature(revenue, netinc, fcf, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d composite signature × close
def f37hgs_f37_hypergrowth_signature_signature_504d_base_v015_signal(revenue, netinc, fcf, closeadj):
    result = _f37_hypergrowth_signature(revenue, netinc, fcf, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signature × revenue (size-amplified)
def f37hgs_f37_hypergrowth_signature_signature_xrev_63d_base_v016_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    result = s * revenue.abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signature × revenue
def f37hgs_f37_hypergrowth_signature_signature_xrev_252d_base_v017_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    result = s * revenue.abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signature × ebitda
def f37hgs_f37_hypergrowth_signature_signature_xebitda_63d_base_v018_signal(revenue, netinc, fcf, ebitda, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    result = s * ebitda.abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signature × assets
def f37hgs_f37_hypergrowth_signature_signature_xassets_252d_base_v019_signal(revenue, netinc, fcf, assets, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    result = s * assets.abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signature × eps
def f37hgs_f37_hypergrowth_signature_signature_xeps_63d_base_v020_signal(revenue, netinc, fcf, eps, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    result = s * eps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# growth strength × margin expansion (interaction at 63d)
def f37hgs_f37_hypergrowth_signature_growthxmargin_63d_base_v021_signal(revenue, netinc, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 63)
    me = _f37_hypergrowth_margin_expansion(netinc, revenue, 63)
    result = g * me * closeadj * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


# growth × margin × close at 252d
def f37hgs_f37_hypergrowth_signature_growthxmargin_252d_base_v022_signal(revenue, netinc, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 252)
    me = _f37_hypergrowth_margin_expansion(netinc, revenue, 252)
    result = g * me * closeadj * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


# growth × FCF positivity (63d)
def f37hgs_f37_hypergrowth_signature_growthxfcfpos_63d_base_v023_signal(revenue, fcf, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 63)
    fp = _f37_hypergrowth_fcf_positivity(fcf, revenue, 63)
    result = g * fp * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# growth × FCF positivity (252d)
def f37hgs_f37_hypergrowth_signature_growthxfcfpos_252d_base_v024_signal(revenue, fcf, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 252)
    fp = _f37_hypergrowth_fcf_positivity(fcf, revenue, 252)
    result = g * fp * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# margin expansion × FCF positivity (63d)
def f37hgs_f37_hypergrowth_signature_marginxfcfpos_63d_base_v025_signal(netinc, fcf, revenue, closeadj):
    me = _f37_hypergrowth_margin_expansion(netinc, revenue, 63)
    fp = _f37_hypergrowth_fcf_positivity(fcf, revenue, 63)
    result = me * fp * closeadj * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


# margin expansion × FCF positivity (252d)
def f37hgs_f37_hypergrowth_signature_marginxfcfpos_252d_base_v026_signal(netinc, fcf, revenue, closeadj):
    me = _f37_hypergrowth_margin_expansion(netinc, revenue, 252)
    fp = _f37_hypergrowth_fcf_positivity(fcf, revenue, 252)
    result = me * fp * closeadj * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of growth strength × close
def f37hgs_f37_hypergrowth_signature_growthstrength_z_252d_base_v027_signal(revenue, closeadj):
    result = _z(_f37_hypergrowth_growth_strength(revenue, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of margin expansion × close
def f37hgs_f37_hypergrowth_signature_marginexpansion_z_252d_base_v028_signal(netinc, revenue, closeadj):
    result = _z(_f37_hypergrowth_margin_expansion(netinc, revenue, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of FCF positivity × close
def f37hgs_f37_hypergrowth_signature_fcfpositivity_z_252d_base_v029_signal(fcf, revenue, closeadj):
    result = _z(_f37_hypergrowth_fcf_positivity(fcf, revenue, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of composite signature × close
def f37hgs_f37_hypergrowth_signature_signature_z_252d_base_v030_signal(revenue, netinc, fcf, closeadj):
    result = _z(_f37_hypergrowth_signature(revenue, netinc, fcf, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of signature × close
def f37hgs_f37_hypergrowth_signature_signature_mean_63d_base_v031_signal(revenue, netinc, fcf, closeadj):
    result = _mean(_f37_hypergrowth_signature(revenue, netinc, fcf, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of signature × close
def f37hgs_f37_hypergrowth_signature_signature_mean_252d_base_v032_signal(revenue, netinc, fcf, closeadj):
    result = _mean(_f37_hypergrowth_signature(revenue, netinc, fcf, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of signature × close
def f37hgs_f37_hypergrowth_signature_signature_std_252d_base_v033_signal(revenue, netinc, fcf, closeadj):
    result = _std(_f37_hypergrowth_signature(revenue, netinc, fcf, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA of signature × close
def f37hgs_f37_hypergrowth_signature_signature_ema_21d_base_v034_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 21)
    result = s.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of signature × close
def f37hgs_f37_hypergrowth_signature_signature_ema_252d_base_v035_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    result = s.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of signature × close
def f37hgs_f37_hypergrowth_signature_signature_sum_252d_base_v036_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    result = s.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of signature × close
def f37hgs_f37_hypergrowth_signature_signature_sum_504d_base_v037_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    result = s.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count days where signature > 0 × close (rolling positivity-of-signature)
def f37hgs_f37_hypergrowth_signature_signature_poscount_252d_base_v038_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    result = (s).rolling(252, min_periods=63).mean() * closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count days where growth > 30% × close
def f37hgs_f37_hypergrowth_signature_growthstrength_count_504d_base_v039_signal(revenue, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 63)
    result = (g).rolling(504, min_periods=126).mean() * closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of days margin expansion > 0
def f37hgs_f37_hypergrowth_signature_marginexpansion_poscount_252d_base_v040_signal(netinc, revenue, closeadj):
    me = _f37_hypergrowth_margin_expansion(netinc, revenue, 63)
    result = (me).rolling(252, min_periods=63).mean() * closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of days FCF positivity > 0
def f37hgs_f37_hypergrowth_signature_fcfpositivity_poscount_252d_base_v041_signal(fcf, revenue, closeadj):
    fp = _f37_hypergrowth_fcf_positivity(fcf, revenue, 63)
    result = (fp).rolling(252, min_periods=63).mean() * closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)


# growth strength × ebitda
def f37hgs_f37_hypergrowth_signature_growthstrength_xebitda_63d_base_v042_signal(revenue, ebitda, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 63)
    result = g * ebitda.abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# growth strength × netinc
def f37hgs_f37_hypergrowth_signature_growthstrength_xnetinc_252d_base_v043_signal(revenue, netinc, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 252)
    result = g * netinc.abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# growth strength × dollar volume
def f37hgs_f37_hypergrowth_signature_growthstrength_xdv_63d_base_v044_signal(revenue, closeadj, volume):
    g = _f37_hypergrowth_growth_strength(revenue, 63)
    dv = closeadj * volume
    result = g * dv * 1e-3
    return result.replace([np.inf, -np.inf], np.nan)


# margin expansion × dollar volume
def f37hgs_f37_hypergrowth_signature_marginexpansion_xdv_252d_base_v045_signal(netinc, revenue, closeadj, volume):
    me = _f37_hypergrowth_margin_expansion(netinc, revenue, 252)
    dv = closeadj * volume
    result = me * dv
    return result.replace([np.inf, -np.inf], np.nan)


# FCF positivity × dollar volume
def f37hgs_f37_hypergrowth_signature_fcfpositivity_xdv_63d_base_v046_signal(fcf, revenue, closeadj, volume):
    fp = _f37_hypergrowth_fcf_positivity(fcf, revenue, 63)
    dv = closeadj * volume
    result = fp * dv
    return result.replace([np.inf, -np.inf], np.nan)


# growth × momentum (return) × close
def f37hgs_f37_hypergrowth_signature_growthxmom_63d_base_v047_signal(revenue, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 63)
    mom = closeadj.pct_change(63)
    result = g * mom * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d growth × 252d momentum × close
def f37hgs_f37_hypergrowth_signature_growthxmom_252d_base_v048_signal(revenue, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 252)
    mom = closeadj.pct_change(252)
    result = g * mom * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d signature normalized by retvol × close
def f37hgs_f37_hypergrowth_signature_signature_normretvol_21d_base_v049_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 21)
    rv = _std(closeadj.pct_change(), 21).replace(0, np.nan)
    result = s / rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signature normalized by retvol × close
def f37hgs_f37_hypergrowth_signature_signature_normretvol_252d_base_v050_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    rv = _std(closeadj.pct_change(), 63).replace(0, np.nan)
    result = s / rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d growth × asset turnover
def f37hgs_f37_hypergrowth_signature_growthxato_63d_base_v051_signal(revenue, assets, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 63)
    ato = _safe_div(revenue, assets.abs())
    result = g * ato * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d growth × current ratio
def f37hgs_f37_hypergrowth_signature_growthxcr_252d_base_v052_signal(revenue, currentratio, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 252)
    result = g * currentratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signature × debt (leverage exposure)
def f37hgs_f37_hypergrowth_signature_signature_xdebt_63d_base_v053_signal(revenue, netinc, fcf, debt, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    result = s * debt.abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signature × equity
def f37hgs_f37_hypergrowth_signature_signature_xequity_252d_base_v054_signal(revenue, netinc, fcf, equity, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    result = s * equity.abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signature × ncfo
def f37hgs_f37_hypergrowth_signature_signature_xncfo_63d_base_v055_signal(revenue, netinc, fcf, ncfo, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    result = s * ncfo.abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signature × workingcapital
def f37hgs_f37_hypergrowth_signature_signature_xwc_252d_base_v056_signal(revenue, netinc, fcf, workingcapital, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    result = s * workingcapital.abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signature × volume zscore × close
def f37hgs_f37_hypergrowth_signature_signature_xvolz_63d_base_v057_signal(revenue, netinc, fcf, closeadj, volume):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    result = s * _z(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signature × ATR × close
def f37hgs_f37_hypergrowth_signature_signature_xatr_252d_base_v058_signal(revenue, netinc, fcf, closeadj, high, low):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = s * atr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# growth strength × revenue trend
def f37hgs_f37_hypergrowth_signature_growthxrevtrend_63d_base_v059_signal(revenue, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 63)
    rt = _diff(revenue, 63) / revenue.abs().replace(0, np.nan)
    result = g * rt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d signature - 63d signature (acceleration of signature)
def f37hgs_f37_hypergrowth_signature_signature_diff_21m63_base_v060_signal(revenue, netinc, fcf, closeadj):
    a = _f37_hypergrowth_signature(revenue, netinc, fcf, 21)
    b = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signature - 252d signature
def f37hgs_f37_hypergrowth_signature_signature_diff_63m252_base_v061_signal(revenue, netinc, fcf, closeadj):
    a = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    b = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signature - 504d signature
def f37hgs_f37_hypergrowth_signature_signature_diff_252m504_base_v062_signal(revenue, netinc, fcf, closeadj):
    a = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    b = _f37_hypergrowth_signature(revenue, netinc, fcf, 504)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max signature within 252d window × close
def f37hgs_f37_hypergrowth_signature_signature_max_252d_base_v063_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    result = s.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min signature within 504d × close
def f37hgs_f37_hypergrowth_signature_signature_min_504d_base_v064_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    result = s.rolling(504, min_periods=126).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# growth strength × log(1+rev) × close
def f37hgs_f37_hypergrowth_signature_growthstrength_xlogrev_63d_base_v065_signal(revenue, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 63)
    lr = np.log(revenue.abs() + 1.0)
    result = g * lr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signature × eps trend × close
def f37hgs_f37_hypergrowth_signature_signature_xepstrend_63d_base_v066_signal(revenue, netinc, fcf, eps, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    et = _diff(eps, 63)
    result = s * et * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signature × eps level × close
def f37hgs_f37_hypergrowth_signature_signature_xeps_252d_base_v067_signal(revenue, netinc, fcf, eps, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    result = s * eps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signature × ebitda growth × close
def f37hgs_f37_hypergrowth_signature_signature_xebitdagrowth_63d_base_v068_signal(revenue, netinc, fcf, ebitda, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    g = ebitda.pct_change(63)
    result = s * g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# growth squared × close
def f37hgs_f37_hypergrowth_signature_growthstrength_sq_63d_base_v069_signal(revenue, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 63)
    result = g * g.abs() * closeadj * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d growth squared × close
def f37hgs_f37_hypergrowth_signature_growthstrength_sq_252d_base_v070_signal(revenue, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 252)
    result = g * g.abs() * closeadj * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signature × sharesbas
def f37hgs_f37_hypergrowth_signature_signature_xsharesbas_252d_base_v071_signal(revenue, netinc, fcf, sharesbas, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    result = s * sharesbas * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signature × ncfi (investment activity)
def f37hgs_f37_hypergrowth_signature_signature_xncfi_63d_base_v072_signal(revenue, netinc, fcf, ncfi, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    result = s * ncfi.abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signature × capex (growth investment)
def f37hgs_f37_hypergrowth_signature_signature_xcapex_252d_base_v073_signal(revenue, netinc, fcf, capex, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    result = s * capex.abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# growth strength × FCF positivity × momentum × close
def f37hgs_f37_hypergrowth_signature_triple_252d_base_v074_signal(revenue, fcf, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 252)
    fp = _f37_hypergrowth_fcf_positivity(fcf, revenue, 252)
    mom = closeadj.pct_change(252)
    result = g * fp * mom * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signature × volume sum (institutional flow check)
def f37hgs_f37_hypergrowth_signature_signature_xvolsum_63d_base_v075_signal(revenue, netinc, fcf, closeadj, volume):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    vs = volume.rolling(21, min_periods=5).sum()
    result = s * vs * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f37hgs_f37_hypergrowth_signature_growthstrength_21d_base_v001_signal,
    f37hgs_f37_hypergrowth_signature_growthstrength_63d_base_v002_signal,
    f37hgs_f37_hypergrowth_signature_growthstrength_126d_base_v003_signal,
    f37hgs_f37_hypergrowth_signature_growthstrength_252d_base_v004_signal,
    f37hgs_f37_hypergrowth_signature_marginexpansion_21d_base_v005_signal,
    f37hgs_f37_hypergrowth_signature_marginexpansion_63d_base_v006_signal,
    f37hgs_f37_hypergrowth_signature_marginexpansion_252d_base_v007_signal,
    f37hgs_f37_hypergrowth_signature_fcfpositivity_21d_base_v008_signal,
    f37hgs_f37_hypergrowth_signature_fcfpositivity_63d_base_v009_signal,
    f37hgs_f37_hypergrowth_signature_fcfpositivity_252d_base_v010_signal,
    f37hgs_f37_hypergrowth_signature_signature_21d_base_v011_signal,
    f37hgs_f37_hypergrowth_signature_signature_63d_base_v012_signal,
    f37hgs_f37_hypergrowth_signature_signature_126d_base_v013_signal,
    f37hgs_f37_hypergrowth_signature_signature_252d_base_v014_signal,
    f37hgs_f37_hypergrowth_signature_signature_504d_base_v015_signal,
    f37hgs_f37_hypergrowth_signature_signature_xrev_63d_base_v016_signal,
    f37hgs_f37_hypergrowth_signature_signature_xrev_252d_base_v017_signal,
    f37hgs_f37_hypergrowth_signature_signature_xebitda_63d_base_v018_signal,
    f37hgs_f37_hypergrowth_signature_signature_xassets_252d_base_v019_signal,
    f37hgs_f37_hypergrowth_signature_signature_xeps_63d_base_v020_signal,
    f37hgs_f37_hypergrowth_signature_growthxmargin_63d_base_v021_signal,
    f37hgs_f37_hypergrowth_signature_growthxmargin_252d_base_v022_signal,
    f37hgs_f37_hypergrowth_signature_growthxfcfpos_63d_base_v023_signal,
    f37hgs_f37_hypergrowth_signature_growthxfcfpos_252d_base_v024_signal,
    f37hgs_f37_hypergrowth_signature_marginxfcfpos_63d_base_v025_signal,
    f37hgs_f37_hypergrowth_signature_marginxfcfpos_252d_base_v026_signal,
    f37hgs_f37_hypergrowth_signature_growthstrength_z_252d_base_v027_signal,
    f37hgs_f37_hypergrowth_signature_marginexpansion_z_252d_base_v028_signal,
    f37hgs_f37_hypergrowth_signature_fcfpositivity_z_252d_base_v029_signal,
    f37hgs_f37_hypergrowth_signature_signature_z_252d_base_v030_signal,
    f37hgs_f37_hypergrowth_signature_signature_mean_63d_base_v031_signal,
    f37hgs_f37_hypergrowth_signature_signature_mean_252d_base_v032_signal,
    f37hgs_f37_hypergrowth_signature_signature_std_252d_base_v033_signal,
    f37hgs_f37_hypergrowth_signature_signature_ema_21d_base_v034_signal,
    f37hgs_f37_hypergrowth_signature_signature_ema_252d_base_v035_signal,
    f37hgs_f37_hypergrowth_signature_signature_sum_252d_base_v036_signal,
    f37hgs_f37_hypergrowth_signature_signature_sum_504d_base_v037_signal,
    f37hgs_f37_hypergrowth_signature_signature_poscount_252d_base_v038_signal,
    f37hgs_f37_hypergrowth_signature_growthstrength_count_504d_base_v039_signal,
    f37hgs_f37_hypergrowth_signature_marginexpansion_poscount_252d_base_v040_signal,
    f37hgs_f37_hypergrowth_signature_fcfpositivity_poscount_252d_base_v041_signal,
    f37hgs_f37_hypergrowth_signature_growthstrength_xebitda_63d_base_v042_signal,
    f37hgs_f37_hypergrowth_signature_growthstrength_xnetinc_252d_base_v043_signal,
    f37hgs_f37_hypergrowth_signature_growthstrength_xdv_63d_base_v044_signal,
    f37hgs_f37_hypergrowth_signature_marginexpansion_xdv_252d_base_v045_signal,
    f37hgs_f37_hypergrowth_signature_fcfpositivity_xdv_63d_base_v046_signal,
    f37hgs_f37_hypergrowth_signature_growthxmom_63d_base_v047_signal,
    f37hgs_f37_hypergrowth_signature_growthxmom_252d_base_v048_signal,
    f37hgs_f37_hypergrowth_signature_signature_normretvol_21d_base_v049_signal,
    f37hgs_f37_hypergrowth_signature_signature_normretvol_252d_base_v050_signal,
    f37hgs_f37_hypergrowth_signature_growthxato_63d_base_v051_signal,
    f37hgs_f37_hypergrowth_signature_growthxcr_252d_base_v052_signal,
    f37hgs_f37_hypergrowth_signature_signature_xdebt_63d_base_v053_signal,
    f37hgs_f37_hypergrowth_signature_signature_xequity_252d_base_v054_signal,
    f37hgs_f37_hypergrowth_signature_signature_xncfo_63d_base_v055_signal,
    f37hgs_f37_hypergrowth_signature_signature_xwc_252d_base_v056_signal,
    f37hgs_f37_hypergrowth_signature_signature_xvolz_63d_base_v057_signal,
    f37hgs_f37_hypergrowth_signature_signature_xatr_252d_base_v058_signal,
    f37hgs_f37_hypergrowth_signature_growthxrevtrend_63d_base_v059_signal,
    f37hgs_f37_hypergrowth_signature_signature_diff_21m63_base_v060_signal,
    f37hgs_f37_hypergrowth_signature_signature_diff_63m252_base_v061_signal,
    f37hgs_f37_hypergrowth_signature_signature_diff_252m504_base_v062_signal,
    f37hgs_f37_hypergrowth_signature_signature_max_252d_base_v063_signal,
    f37hgs_f37_hypergrowth_signature_signature_min_504d_base_v064_signal,
    f37hgs_f37_hypergrowth_signature_growthstrength_xlogrev_63d_base_v065_signal,
    f37hgs_f37_hypergrowth_signature_signature_xepstrend_63d_base_v066_signal,
    f37hgs_f37_hypergrowth_signature_signature_xeps_252d_base_v067_signal,
    f37hgs_f37_hypergrowth_signature_signature_xebitdagrowth_63d_base_v068_signal,
    f37hgs_f37_hypergrowth_signature_growthstrength_sq_63d_base_v069_signal,
    f37hgs_f37_hypergrowth_signature_growthstrength_sq_252d_base_v070_signal,
    f37hgs_f37_hypergrowth_signature_signature_xsharesbas_252d_base_v071_signal,
    f37hgs_f37_hypergrowth_signature_signature_xncfi_63d_base_v072_signal,
    f37hgs_f37_hypergrowth_signature_signature_xcapex_252d_base_v073_signal,
    f37hgs_f37_hypergrowth_signature_triple_252d_base_v074_signal,
    f37hgs_f37_hypergrowth_signature_signature_xvolsum_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F37_HYPERGROWTH_SIGNATURE_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    revenue = pd.Series(1e7 * np.exp(np.cumsum(np.random.normal(0.0008, 0.01, n))), name="revenue")
    netinc = pd.Series(1e6 * np.exp(np.cumsum(np.random.normal(0.0006, 0.012, n))) * np.sign(np.random.normal(0.5, 1.0, n)), name="netinc")
    ebitda = pd.Series(2e6 * np.exp(np.cumsum(np.random.normal(0.0006, 0.01, n))) * np.sign(np.random.normal(0.7, 1.0, n)), name="ebitda")
    eps = pd.Series(np.cumsum(np.random.normal(0.001, 0.05, n)) + 1.0, name="eps")
    fcf = pd.Series(8e5 * np.exp(np.cumsum(np.random.normal(0.0005, 0.013, n))) * np.sign(np.random.normal(0.6, 1.0, n)), name="fcf")
    ncfo = pd.Series(1.2e6 * np.exp(np.cumsum(np.random.normal(0.0006, 0.012, n))) * np.sign(np.random.normal(0.8, 1.0, n)), name="ncfo")
    ncfi = pd.Series(7e5 * np.exp(np.cumsum(np.random.normal(0.0003, 0.011, n))) * np.sign(np.random.normal(0.4, 1.0, n)), name="ncfi")
    capex = pd.Series(9e5 * np.exp(np.cumsum(np.random.normal(0.0004, 0.011, n))), name="capex")
    sharesbas = pd.Series(1e7 + np.cumsum(np.random.normal(1e3, 5e3, n)), name="sharesbas")
    assets = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0004, 0.006, n))), name="assets")
    debt = pd.Series(1e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.008, n))), name="debt")
    equity = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0005, 0.007, n))), name="equity")
    workingcapital = pd.Series(8e6 * np.exp(np.cumsum(np.random.normal(0.0004, 0.01, n))) * np.sign(np.random.normal(0.7, 1.0, n)), name="workingcapital")
    currentratio = pd.Series(1.5 + np.cumsum(np.random.normal(0.0, 0.01, n)) * 0.1, name="currentratio")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "netinc": netinc, "ebitda": ebitda, "eps": eps,
        "fcf": fcf, "ncfo": ncfo, "ncfi": ncfi, "capex": capex, "sharesbas": sharesbas,
        "assets": assets, "debt": debt, "equity": equity,
        "workingcapital": workingcapital, "currentratio": currentratio,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f37_hypergrowth_growth_strength", "_f37_hypergrowth_margin_expansion", "_f37_hypergrowth_fcf_positivity", "_f37_hypergrowth_signature")
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
    print(f"OK f37_hypergrowth_signature_base_001_075_claude: {n_features} features pass")
