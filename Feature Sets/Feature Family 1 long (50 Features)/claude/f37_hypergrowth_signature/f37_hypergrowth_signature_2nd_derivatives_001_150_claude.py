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


def _slope(s, w):
    return s.diff(periods=w)


# ===== folder domain primitives =====
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


def _make_slope_growth_w(w_base, w_slope):
    def fn(revenue, closeadj):
        base = _f37_hypergrowth_growth_strength(revenue, w_base) * closeadj
        result = _slope(base, w_slope)
        return result.replace([np.inf, -np.inf], np.nan)
    return fn


# Slope features as expanded def blocks
# 5d slope of 21d growth strength × close
def f37hgs_f37_hypergrowth_signature_growthstrength_21d_slope_v001_signal(revenue, closeadj):
    base = _f37_hypergrowth_growth_strength(revenue, 21) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d growth strength × close
def f37hgs_f37_hypergrowth_signature_growthstrength_21d_slope_v002_signal(revenue, closeadj):
    base = _f37_hypergrowth_growth_strength(revenue, 21) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d growth strength × close
def f37hgs_f37_hypergrowth_signature_growthstrength_63d_slope_v003_signal(revenue, closeadj):
    base = _f37_hypergrowth_growth_strength(revenue, 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d growth strength × close
def f37hgs_f37_hypergrowth_signature_growthstrength_63d_slope_v004_signal(revenue, closeadj):
    base = _f37_hypergrowth_growth_strength(revenue, 63) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d growth strength × close
def f37hgs_f37_hypergrowth_signature_growthstrength_126d_slope_v005_signal(revenue, closeadj):
    base = _f37_hypergrowth_growth_strength(revenue, 126) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d growth strength × close
def f37hgs_f37_hypergrowth_signature_growthstrength_126d_slope_v006_signal(revenue, closeadj):
    base = _f37_hypergrowth_growth_strength(revenue, 126) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d growth strength × close
def f37hgs_f37_hypergrowth_signature_growthstrength_252d_slope_v007_signal(revenue, closeadj):
    base = _f37_hypergrowth_growth_strength(revenue, 252) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d growth strength × close
def f37hgs_f37_hypergrowth_signature_growthstrength_252d_slope_v008_signal(revenue, closeadj):
    base = _f37_hypergrowth_growth_strength(revenue, 252) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d margin expansion × close
def f37hgs_f37_hypergrowth_signature_marginexpansion_21d_slope_v009_signal(netinc, revenue, closeadj):
    base = _f37_hypergrowth_margin_expansion(netinc, revenue, 21) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d margin expansion × close
def f37hgs_f37_hypergrowth_signature_marginexpansion_21d_slope_v010_signal(netinc, revenue, closeadj):
    base = _f37_hypergrowth_margin_expansion(netinc, revenue, 21) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d margin expansion × close
def f37hgs_f37_hypergrowth_signature_marginexpansion_63d_slope_v011_signal(netinc, revenue, closeadj):
    base = _f37_hypergrowth_margin_expansion(netinc, revenue, 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d margin expansion × close
def f37hgs_f37_hypergrowth_signature_marginexpansion_63d_slope_v012_signal(netinc, revenue, closeadj):
    base = _f37_hypergrowth_margin_expansion(netinc, revenue, 63) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d margin expansion × close
def f37hgs_f37_hypergrowth_signature_marginexpansion_252d_slope_v013_signal(netinc, revenue, closeadj):
    base = _f37_hypergrowth_margin_expansion(netinc, revenue, 252) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d margin expansion × close
def f37hgs_f37_hypergrowth_signature_marginexpansion_252d_slope_v014_signal(netinc, revenue, closeadj):
    base = _f37_hypergrowth_margin_expansion(netinc, revenue, 252) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d FCF positivity × close
def f37hgs_f37_hypergrowth_signature_fcfpositivity_21d_slope_v015_signal(fcf, revenue, closeadj):
    base = _f37_hypergrowth_fcf_positivity(fcf, revenue, 21) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d FCF positivity × close
def f37hgs_f37_hypergrowth_signature_fcfpositivity_21d_slope_v016_signal(fcf, revenue, closeadj):
    base = _f37_hypergrowth_fcf_positivity(fcf, revenue, 21) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d FCF positivity × close
def f37hgs_f37_hypergrowth_signature_fcfpositivity_63d_slope_v017_signal(fcf, revenue, closeadj):
    base = _f37_hypergrowth_fcf_positivity(fcf, revenue, 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d FCF positivity × close
def f37hgs_f37_hypergrowth_signature_fcfpositivity_63d_slope_v018_signal(fcf, revenue, closeadj):
    base = _f37_hypergrowth_fcf_positivity(fcf, revenue, 63) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF positivity × close
def f37hgs_f37_hypergrowth_signature_fcfpositivity_252d_slope_v019_signal(fcf, revenue, closeadj):
    base = _f37_hypergrowth_fcf_positivity(fcf, revenue, 252) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d signature × close
def f37hgs_f37_hypergrowth_signature_signature_21d_slope_v020_signal(revenue, netinc, fcf, closeadj):
    base = _f37_hypergrowth_signature(revenue, netinc, fcf, 21) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d signature × close
def f37hgs_f37_hypergrowth_signature_signature_63d_slope_v021_signal(revenue, netinc, fcf, closeadj):
    base = _f37_hypergrowth_signature(revenue, netinc, fcf, 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d signature × close
def f37hgs_f37_hypergrowth_signature_signature_63d_slope_v022_signal(revenue, netinc, fcf, closeadj):
    base = _f37_hypergrowth_signature(revenue, netinc, fcf, 63) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d signature × close
def f37hgs_f37_hypergrowth_signature_signature_126d_slope_v023_signal(revenue, netinc, fcf, closeadj):
    base = _f37_hypergrowth_signature(revenue, netinc, fcf, 126) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d signature × close
def f37hgs_f37_hypergrowth_signature_signature_126d_slope_v024_signal(revenue, netinc, fcf, closeadj):
    base = _f37_hypergrowth_signature(revenue, netinc, fcf, 126) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d signature × close
def f37hgs_f37_hypergrowth_signature_signature_252d_slope_v025_signal(revenue, netinc, fcf, closeadj):
    base = _f37_hypergrowth_signature(revenue, netinc, fcf, 252) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d signature × close
def f37hgs_f37_hypergrowth_signature_signature_252d_slope_v026_signal(revenue, netinc, fcf, closeadj):
    base = _f37_hypergrowth_signature(revenue, netinc, fcf, 252) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d signature × close
def f37hgs_f37_hypergrowth_signature_signature_504d_slope_v027_signal(revenue, netinc, fcf, closeadj):
    base = _f37_hypergrowth_signature(revenue, netinc, fcf, 504) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d signature × revenue × close
def f37hgs_f37_hypergrowth_signature_signature_xrev_63d_slope_v028_signal(revenue, netinc, fcf, closeadj):
    base = _f37_hypergrowth_signature(revenue, netinc, fcf, 63) * revenue.abs() * closeadj * 1e-6
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d signature × revenue × close
def f37hgs_f37_hypergrowth_signature_signature_xrev_252d_slope_v029_signal(revenue, netinc, fcf, closeadj):
    base = _f37_hypergrowth_signature(revenue, netinc, fcf, 252) * revenue.abs() * closeadj * 1e-6
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of signature × ebitda × close
def f37hgs_f37_hypergrowth_signature_signature_xebitda_63d_slope_v030_signal(revenue, netinc, fcf, ebitda, closeadj):
    base = _f37_hypergrowth_signature(revenue, netinc, fcf, 63) * ebitda.abs() * closeadj * 1e-6
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of signature × assets × close
def f37hgs_f37_hypergrowth_signature_signature_xassets_252d_slope_v031_signal(revenue, netinc, fcf, assets, closeadj):
    base = _f37_hypergrowth_signature(revenue, netinc, fcf, 252) * assets.abs() * closeadj * 1e-6
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of signature × eps × close
def f37hgs_f37_hypergrowth_signature_signature_xeps_63d_slope_v032_signal(revenue, netinc, fcf, eps, closeadj):
    base = _f37_hypergrowth_signature(revenue, netinc, fcf, 63) * eps * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of growth × margin × close
def f37hgs_f37_hypergrowth_signature_growthxmargin_63d_slope_v033_signal(revenue, netinc, closeadj):
    base = _f37_hypergrowth_growth_strength(revenue, 63) * _f37_hypergrowth_margin_expansion(netinc, revenue, 63) * closeadj * 10.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d growth × margin × close
def f37hgs_f37_hypergrowth_signature_growthxmargin_252d_slope_v034_signal(revenue, netinc, closeadj):
    base = _f37_hypergrowth_growth_strength(revenue, 252) * _f37_hypergrowth_margin_expansion(netinc, revenue, 252) * closeadj * 10.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of growth × FCF positivity × close
def f37hgs_f37_hypergrowth_signature_growthxfcfpos_63d_slope_v035_signal(revenue, fcf, closeadj):
    base = _f37_hypergrowth_growth_strength(revenue, 63) * _f37_hypergrowth_fcf_positivity(fcf, revenue, 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d growth × FCF positivity × close
def f37hgs_f37_hypergrowth_signature_growthxfcfpos_252d_slope_v036_signal(revenue, fcf, closeadj):
    base = _f37_hypergrowth_growth_strength(revenue, 252) * _f37_hypergrowth_fcf_positivity(fcf, revenue, 252) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of margin × FCF positivity × close
def f37hgs_f37_hypergrowth_signature_marginxfcfpos_63d_slope_v037_signal(netinc, fcf, revenue, closeadj):
    base = _f37_hypergrowth_margin_expansion(netinc, revenue, 63) * _f37_hypergrowth_fcf_positivity(fcf, revenue, 63) * closeadj * 10.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d margin × FCF positivity × close
def f37hgs_f37_hypergrowth_signature_marginxfcfpos_252d_slope_v038_signal(netinc, fcf, revenue, closeadj):
    base = _f37_hypergrowth_margin_expansion(netinc, revenue, 252) * _f37_hypergrowth_fcf_positivity(fcf, revenue, 252) * closeadj * 10.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of growth strength z × close
def f37hgs_f37_hypergrowth_signature_growthstrength_z_252d_slope_v039_signal(revenue, closeadj):
    base = _z(_f37_hypergrowth_growth_strength(revenue, 63), 252) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of margin expansion z × close
def f37hgs_f37_hypergrowth_signature_marginexpansion_z_252d_slope_v040_signal(netinc, revenue, closeadj):
    base = _z(_f37_hypergrowth_margin_expansion(netinc, revenue, 63), 252) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF positivity z × close
def f37hgs_f37_hypergrowth_signature_fcfpositivity_z_252d_slope_v041_signal(fcf, revenue, closeadj):
    base = _z(_f37_hypergrowth_fcf_positivity(fcf, revenue, 63), 252) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of signature z × close
def f37hgs_f37_hypergrowth_signature_signature_z_252d_slope_v042_signal(revenue, netinc, fcf, closeadj):
    base = _z(_f37_hypergrowth_signature(revenue, netinc, fcf, 63), 252) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of signature mean × close
def f37hgs_f37_hypergrowth_signature_signature_mean_63d_slope_v043_signal(revenue, netinc, fcf, closeadj):
    base = _mean(_f37_hypergrowth_signature(revenue, netinc, fcf, 63), 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of signature mean × close
def f37hgs_f37_hypergrowth_signature_signature_mean_252d_slope_v044_signal(revenue, netinc, fcf, closeadj):
    base = _mean(_f37_hypergrowth_signature(revenue, netinc, fcf, 252), 252) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of signature std × close
def f37hgs_f37_hypergrowth_signature_signature_std_252d_slope_v045_signal(revenue, netinc, fcf, closeadj):
    base = _std(_f37_hypergrowth_signature(revenue, netinc, fcf, 63), 252) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of signature EMA (21d) × close
def f37hgs_f37_hypergrowth_signature_signature_ema_21d_slope_v046_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 21)
    base = s.ewm(span=21, adjust=False).mean() * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of signature EMA (252d) × close
def f37hgs_f37_hypergrowth_signature_signature_ema_252d_slope_v047_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    base = s.ewm(span=252, adjust=False).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of signature sum × close
def f37hgs_f37_hypergrowth_signature_signature_sum_252d_slope_v048_signal(revenue, netinc, fcf, closeadj):
    base = _f37_hypergrowth_signature(revenue, netinc, fcf, 63).rolling(252, min_periods=63).sum() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of signature sum (504d) × close
def f37hgs_f37_hypergrowth_signature_signature_sum_504d_slope_v049_signal(revenue, netinc, fcf, closeadj):
    base = _f37_hypergrowth_signature(revenue, netinc, fcf, 63).rolling(504, min_periods=126).sum() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of signature poscount × close
def f37hgs_f37_hypergrowth_signature_signature_poscount_252d_slope_v050_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    base = (s).rolling(252, min_periods=63).mean() * closeadj * 0.001
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of growth count × close
def f37hgs_f37_hypergrowth_signature_growthstrength_count_504d_slope_v051_signal(revenue, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 63)
    base = (g).rolling(504, min_periods=126).mean() * closeadj * 0.001
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of margin expansion poscount × close
def f37hgs_f37_hypergrowth_signature_marginexpansion_poscount_252d_slope_v052_signal(netinc, revenue, closeadj):
    me = _f37_hypergrowth_margin_expansion(netinc, revenue, 63)
    base = (me).rolling(252, min_periods=63).mean() * closeadj * 0.001
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of fcfpositivity poscount × close
def f37hgs_f37_hypergrowth_signature_fcfpositivity_poscount_252d_slope_v053_signal(fcf, revenue, closeadj):
    fp = _f37_hypergrowth_fcf_positivity(fcf, revenue, 63)
    base = (fp).rolling(252, min_periods=63).mean() * closeadj * 0.001
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of growth × ebitda × close
def f37hgs_f37_hypergrowth_signature_growthstrength_xebitda_63d_slope_v054_signal(revenue, ebitda, closeadj):
    base = _f37_hypergrowth_growth_strength(revenue, 63) * ebitda.abs() * closeadj * 1e-6
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of growth × netinc × close
def f37hgs_f37_hypergrowth_signature_growthstrength_xnetinc_252d_slope_v055_signal(revenue, netinc, closeadj):
    base = _f37_hypergrowth_growth_strength(revenue, 252) * netinc.abs() * closeadj * 1e-6
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of growth × dollar volume
def f37hgs_f37_hypergrowth_signature_growthstrength_xdv_63d_slope_v056_signal(revenue, closeadj, volume):
    g = _f37_hypergrowth_growth_strength(revenue, 63)
    dv = closeadj * volume
    base = g * dv * 1e-3
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of margin expansion × dollar volume
def f37hgs_f37_hypergrowth_signature_marginexpansion_xdv_252d_slope_v057_signal(netinc, revenue, closeadj, volume):
    me = _f37_hypergrowth_margin_expansion(netinc, revenue, 252)
    dv = closeadj * volume
    base = me * dv
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of FCF positivity × dollar volume
def f37hgs_f37_hypergrowth_signature_fcfpositivity_xdv_63d_slope_v058_signal(fcf, revenue, closeadj, volume):
    fp = _f37_hypergrowth_fcf_positivity(fcf, revenue, 63)
    dv = closeadj * volume
    base = fp * dv
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of growth × momentum × close
def f37hgs_f37_hypergrowth_signature_growthxmom_63d_slope_v059_signal(revenue, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 63)
    mom = closeadj.pct_change(63)
    base = g * mom * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d growth × momentum × close
def f37hgs_f37_hypergrowth_signature_growthxmom_252d_slope_v060_signal(revenue, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 252)
    mom = closeadj.pct_change(252)
    base = g * mom * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of signature normretvol (21d) × close
def f37hgs_f37_hypergrowth_signature_signature_normretvol_21d_slope_v061_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 21)
    rv = _std(closeadj.pct_change(), 21).replace(0, np.nan)
    base = s / rv * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of signature normretvol (252d) × close
def f37hgs_f37_hypergrowth_signature_signature_normretvol_252d_slope_v062_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    rv = _std(closeadj.pct_change(), 63).replace(0, np.nan)
    base = s / rv * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of growth × ato × close
def f37hgs_f37_hypergrowth_signature_growthxato_63d_slope_v063_signal(revenue, assets, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 63)
    ato = _safe_div(revenue, assets.abs())
    base = g * ato * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of growth × cr × close
def f37hgs_f37_hypergrowth_signature_growthxcr_252d_slope_v064_signal(revenue, currentratio, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 252)
    base = g * currentratio * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of signature × debt × close
def f37hgs_f37_hypergrowth_signature_signature_xdebt_63d_slope_v065_signal(revenue, netinc, fcf, debt, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    base = s * debt.abs() * closeadj * 1e-6
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of signature × equity × close
def f37hgs_f37_hypergrowth_signature_signature_xequity_252d_slope_v066_signal(revenue, netinc, fcf, equity, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    base = s * equity.abs() * closeadj * 1e-6
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of signature × ncfo × close
def f37hgs_f37_hypergrowth_signature_signature_xncfo_63d_slope_v067_signal(revenue, netinc, fcf, ncfo, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    base = s * ncfo.abs() * closeadj * 1e-6
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of signature × wc × close
def f37hgs_f37_hypergrowth_signature_signature_xwc_252d_slope_v068_signal(revenue, netinc, fcf, workingcapital, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    base = s * workingcapital.abs() * closeadj * 1e-6
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of signature × volz × close
def f37hgs_f37_hypergrowth_signature_signature_xvolz_63d_slope_v069_signal(revenue, netinc, fcf, closeadj, volume):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    base = s * _z(volume, 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of signature × ATR × close
def f37hgs_f37_hypergrowth_signature_signature_xatr_252d_slope_v070_signal(revenue, netinc, fcf, closeadj, high, low):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    atr = (high - low).rolling(63, min_periods=21).mean()
    base = s * atr * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of growth × revtrend × close
def f37hgs_f37_hypergrowth_signature_growthxrevtrend_63d_slope_v071_signal(revenue, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 63)
    rt = _diff(revenue, 63) / revenue.abs().replace(0, np.nan)
    base = g * rt * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of signature diff (21m63) × close
def f37hgs_f37_hypergrowth_signature_signature_diff_21m63_slope_v072_signal(revenue, netinc, fcf, closeadj):
    base = (_f37_hypergrowth_signature(revenue, netinc, fcf, 21) - _f37_hypergrowth_signature(revenue, netinc, fcf, 63)) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of signature diff (63m252) × close
def f37hgs_f37_hypergrowth_signature_signature_diff_63m252_slope_v073_signal(revenue, netinc, fcf, closeadj):
    base = (_f37_hypergrowth_signature(revenue, netinc, fcf, 63) - _f37_hypergrowth_signature(revenue, netinc, fcf, 252)) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of signature diff (252m504) × close
def f37hgs_f37_hypergrowth_signature_signature_diff_252m504_slope_v074_signal(revenue, netinc, fcf, closeadj):
    base = (_f37_hypergrowth_signature(revenue, netinc, fcf, 252) - _f37_hypergrowth_signature(revenue, netinc, fcf, 504)) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of signature max in 252d × close
def f37hgs_f37_hypergrowth_signature_signature_max_252d_slope_v075_signal(revenue, netinc, fcf, closeadj):
    base = _f37_hypergrowth_signature(revenue, netinc, fcf, 63).rolling(252, min_periods=63).max() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of signature min (504d) × close
def f37hgs_f37_hypergrowth_signature_signature_min_504d_slope_v076_signal(revenue, netinc, fcf, closeadj):
    base = _f37_hypergrowth_signature(revenue, netinc, fcf, 252).rolling(504, min_periods=126).min() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of growth × log(rev) × close
def f37hgs_f37_hypergrowth_signature_growthstrength_xlogrev_63d_slope_v077_signal(revenue, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 63)
    lr = np.log(revenue.abs() + 1.0)
    base = g * lr * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of signature × eps trend × close
def f37hgs_f37_hypergrowth_signature_signature_xepstrend_63d_slope_v078_signal(revenue, netinc, fcf, eps, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    et = _diff(eps, 63)
    base = s * et * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of signature × eps × close
def f37hgs_f37_hypergrowth_signature_signature_xeps_252d_slope_v079_signal(revenue, netinc, fcf, eps, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    base = s * eps * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of signature × ebitda growth × close
def f37hgs_f37_hypergrowth_signature_signature_xebitdagrowth_63d_slope_v080_signal(revenue, netinc, fcf, ebitda, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    g = ebitda.pct_change(63)
    base = s * g * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of growth squared × close
def f37hgs_f37_hypergrowth_signature_growthstrength_sq_63d_slope_v081_signal(revenue, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 63)
    base = g * g.abs() * closeadj * 10.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d growth squared × close
def f37hgs_f37_hypergrowth_signature_growthstrength_sq_252d_slope_v082_signal(revenue, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 252)
    base = g * g.abs() * closeadj * 10.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of signature × sharesbas × close
def f37hgs_f37_hypergrowth_signature_signature_xsharesbas_252d_slope_v083_signal(revenue, netinc, fcf, sharesbas, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    base = s * sharesbas * closeadj * 1e-6
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of signature × ncfi × close
def f37hgs_f37_hypergrowth_signature_signature_xncfi_63d_slope_v084_signal(revenue, netinc, fcf, ncfi, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    base = s * ncfi.abs() * closeadj * 1e-6
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of signature × capex × close
def f37hgs_f37_hypergrowth_signature_signature_xcapex_252d_slope_v085_signal(revenue, netinc, fcf, capex, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    base = s * capex.abs() * closeadj * 1e-6
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of triple (growth×fcfpos×mom) × close
def f37hgs_f37_hypergrowth_signature_triple_252d_slope_v086_signal(revenue, fcf, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 252)
    fp = _f37_hypergrowth_fcf_positivity(fcf, revenue, 252)
    mom = closeadj.pct_change(252)
    base = g * fp * mom * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of signature × volume sum × close
def f37hgs_f37_hypergrowth_signature_signature_xvolsum_63d_slope_v087_signal(revenue, netinc, fcf, closeadj, volume):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    vs = volume.rolling(21, min_periods=5).sum()
    base = s * vs * closeadj * 1e-6
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 5d growth strength × close
def f37hgs_f37_hypergrowth_signature_growthstrength_5d_slope_v088_signal(revenue, closeadj):
    base = _f37_hypergrowth_growth_strength(revenue, 5) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 10d growth strength × close
def f37hgs_f37_hypergrowth_signature_growthstrength_10d_slope_v089_signal(revenue, closeadj):
    base = _f37_hypergrowth_growth_strength(revenue, 10) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 42d growth strength × close
def f37hgs_f37_hypergrowth_signature_growthstrength_42d_slope_v090_signal(revenue, closeadj):
    base = _f37_hypergrowth_growth_strength(revenue, 42) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 189d growth strength × close
def f37hgs_f37_hypergrowth_signature_growthstrength_189d_slope_v091_signal(revenue, closeadj):
    base = _f37_hypergrowth_growth_strength(revenue, 189) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d growth strength × close
def f37hgs_f37_hypergrowth_signature_growthstrength_504d_slope_v092_signal(revenue, closeadj):
    base = _f37_hypergrowth_growth_strength(revenue, 504) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 5d margin expansion (op) × close
def f37hgs_f37_hypergrowth_signature_marginexpansion_op_5d_slope_v093_signal(opinc, revenue, closeadj):
    base = _f37_hypergrowth_margin_expansion(opinc, revenue, 5) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d margin expansion (op) × close
def f37hgs_f37_hypergrowth_signature_marginexpansion_op_21d_slope_v094_signal(opinc, revenue, closeadj):
    base = _f37_hypergrowth_margin_expansion(opinc, revenue, 21) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d margin expansion (op) × close
def f37hgs_f37_hypergrowth_signature_marginexpansion_op_63d_slope_v095_signal(opinc, revenue, closeadj):
    base = _f37_hypergrowth_margin_expansion(opinc, revenue, 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d margin expansion (op) × close
def f37hgs_f37_hypergrowth_signature_marginexpansion_op_252d_slope_v096_signal(opinc, revenue, closeadj):
    base = _f37_hypergrowth_margin_expansion(opinc, revenue, 252) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d margin expansion (gp) × close
def f37hgs_f37_hypergrowth_signature_marginexpansion_gp_21d_slope_v097_signal(gp, revenue, closeadj):
    base = _f37_hypergrowth_margin_expansion(gp, revenue, 21) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d margin expansion (gp) × close
def f37hgs_f37_hypergrowth_signature_marginexpansion_gp_252d_slope_v098_signal(gp, revenue, closeadj):
    base = _f37_hypergrowth_margin_expansion(gp, revenue, 252) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d margin expansion (ebitda) × close
def f37hgs_f37_hypergrowth_signature_marginexpansion_ebitda_63d_slope_v099_signal(ebitda, revenue, closeadj):
    base = _f37_hypergrowth_margin_expansion(ebitda, revenue, 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d margin expansion (ebitda) × close
def f37hgs_f37_hypergrowth_signature_marginexpansion_ebitda_252d_slope_v100_signal(ebitda, revenue, closeadj):
    base = _f37_hypergrowth_margin_expansion(ebitda, revenue, 252) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 5d FCF positivity × close
def f37hgs_f37_hypergrowth_signature_fcfpositivity_5d_slope_v101_signal(fcf, revenue, closeadj):
    base = _f37_hypergrowth_fcf_positivity(fcf, revenue, 5) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 42d FCF positivity × close
def f37hgs_f37_hypergrowth_signature_fcfpositivity_42d_slope_v102_signal(fcf, revenue, closeadj):
    base = _f37_hypergrowth_fcf_positivity(fcf, revenue, 42) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d FCF positivity × close
def f37hgs_f37_hypergrowth_signature_fcfpositivity_504d_slope_v103_signal(fcf, revenue, closeadj):
    base = _f37_hypergrowth_fcf_positivity(fcf, revenue, 504) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d signature with op × close
def f37hgs_f37_hypergrowth_signature_signature_op_21d_slope_v104_signal(revenue, opinc, fcf, closeadj):
    base = _f37_hypergrowth_signature(revenue, opinc, fcf, 21) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d signature with op × close
def f37hgs_f37_hypergrowth_signature_signature_op_252d_slope_v105_signal(revenue, opinc, fcf, closeadj):
    base = _f37_hypergrowth_signature(revenue, opinc, fcf, 252) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d signature with gp × close
def f37hgs_f37_hypergrowth_signature_signature_gp_252d_slope_v106_signal(revenue, gp, fcf, closeadj):
    base = _f37_hypergrowth_signature(revenue, gp, fcf, 252) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d signature with ebitda × close
def f37hgs_f37_hypergrowth_signature_signature_ebitda_252d_slope_v107_signal(revenue, ebitda, fcf, closeadj):
    base = _f37_hypergrowth_signature(revenue, ebitda, fcf, 252) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d signature with ncfo × close
def f37hgs_f37_hypergrowth_signature_signature_ncfo_63d_slope_v108_signal(revenue, netinc, ncfo, closeadj):
    base = _f37_hypergrowth_signature(revenue, netinc, ncfo, 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d signature with ncfo × close
def f37hgs_f37_hypergrowth_signature_signature_ncfo_252d_slope_v109_signal(revenue, netinc, ncfo, closeadj):
    base = _f37_hypergrowth_signature(revenue, netinc, ncfo, 252) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of triple product (63d) × close
def f37hgs_f37_hypergrowth_signature_tripleproduct_63d_slope_v110_signal(revenue, netinc, fcf, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 63)
    me = _f37_hypergrowth_margin_expansion(netinc, revenue, 63)
    fp = _f37_hypergrowth_fcf_positivity(fcf, revenue, 63)
    base = g * me * fp * closeadj * 100.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of triple product (252d) × close
def f37hgs_f37_hypergrowth_signature_tripleproduct_252d_slope_v111_signal(revenue, netinc, fcf, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 252)
    me = _f37_hypergrowth_margin_expansion(netinc, revenue, 252)
    fp = _f37_hypergrowth_fcf_positivity(fcf, revenue, 252)
    base = g * me * fp * closeadj * 100.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of triple product (504d) × close
def f37hgs_f37_hypergrowth_signature_tripleproduct_504d_slope_v112_signal(revenue, netinc, fcf, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 504)
    me = _f37_hypergrowth_margin_expansion(netinc, revenue, 504)
    fp = _f37_hypergrowth_fcf_positivity(fcf, revenue, 504)
    base = g * me * fp * closeadj * 100.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of signature × log(rev) × close
def f37hgs_f37_hypergrowth_signature_signature_xlogrev_252d_slope_v113_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    lr = np.log(revenue.abs() + 1.0)
    base = s * lr * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of growth × dvsum (63d) × close
def f37hgs_f37_hypergrowth_signature_growthstrength_xdvsum_63d_slope_v114_signal(revenue, closeadj, volume):
    g = _f37_hypergrowth_growth_strength(revenue, 63)
    dvs = (closeadj * volume).rolling(21, min_periods=5).sum()
    base = g * dvs * 1e-3
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of growth × dvsum (252d) × close
def f37hgs_f37_hypergrowth_signature_growthstrength_xdvsum_252d_slope_v115_signal(revenue, closeadj, volume):
    g = _f37_hypergrowth_growth_strength(revenue, 252)
    dvs = (closeadj * volume).rolling(63, min_periods=21).sum()
    base = g * dvs * 1e-3
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of signature × taxexp × close
def f37hgs_f37_hypergrowth_signature_signature_xtaxexp_63d_slope_v116_signal(revenue, netinc, fcf, taxexp, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    base = s * taxexp.abs() * closeadj * 1e-5
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of signature × intexp × close
def f37hgs_f37_hypergrowth_signature_signature_xintexp_252d_slope_v117_signal(revenue, netinc, fcf, intexp, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    base = s * intexp.abs() * closeadj * 1e-5
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of signature × short-mom × close
def f37hgs_f37_hypergrowth_signature_signature_xshortmom_21d_slope_v118_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 21)
    mom = closeadj.pct_change(21)
    base = s * mom * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of signature × long-mom × close
def f37hgs_f37_hypergrowth_signature_signature_xlongmom_252d_slope_v119_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    mom = closeadj.pct_change(252)
    base = s * mom * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of signature × close zscore × close
def f37hgs_f37_hypergrowth_signature_signature_xclosez_63d_slope_v120_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    cz = _z(closeadj, 252)
    base = s * cz * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of signature × close zscore × close
def f37hgs_f37_hypergrowth_signature_signature_xclosez_252d_slope_v121_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    cz = _z(closeadj, 504)
    base = s * cz * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of growth × ebitda growth × close
def f37hgs_f37_hypergrowth_signature_growthxebitdagrowth_63d_slope_v122_signal(revenue, ebitda, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 63)
    eg = ebitda.pct_change(63)
    base = g * eg * closeadj * 10.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d growth × ebitda growth × close
def f37hgs_f37_hypergrowth_signature_growthxebitdagrowth_252d_slope_v123_signal(revenue, ebitda, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 252)
    eg = ebitda.pct_change(252)
    base = g * eg * closeadj * 10.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of signature × volume sum (252d) × close
def f37hgs_f37_hypergrowth_signature_signature_xvolsum_252d_slope_v124_signal(revenue, netinc, fcf, closeadj, volume):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    vs = volume.rolling(63, min_periods=21).sum()
    base = s * vs * closeadj * 1e-6
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of signature × range × close
def f37hgs_f37_hypergrowth_signature_signature_xrange_63d_slope_v125_signal(revenue, netinc, fcf, closeadj, high, low):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    rng = (high - low).rolling(21, min_periods=5).mean()
    base = s * rng * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of growth × range × close
def f37hgs_f37_hypergrowth_signature_growthxrange_21d_slope_v126_signal(revenue, closeadj, high, low):
    g = _f37_hypergrowth_growth_strength(revenue, 21)
    rng = (high - low).rolling(21, min_periods=5).mean()
    base = g * rng * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of signature × log(assets) × close
def f37hgs_f37_hypergrowth_signature_signature_xlogassets_252d_slope_v127_signal(revenue, netinc, fcf, assets, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    la = np.log(assets.abs() + 1.0)
    base = s * la * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of magnitudesum (21d) × close
def f37hgs_f37_hypergrowth_signature_magnitudesum_21d_slope_v128_signal(revenue, netinc, fcf, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 21).abs()
    me = _f37_hypergrowth_margin_expansion(netinc, revenue, 21).abs() * 5.0
    fp = _f37_hypergrowth_fcf_positivity(fcf, revenue, 21).abs()
    base = (g + me + fp) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of magnitudesum (252d) × close
def f37hgs_f37_hypergrowth_signature_magnitudesum_252d_slope_v129_signal(revenue, netinc, fcf, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 252).abs()
    me = _f37_hypergrowth_margin_expansion(netinc, revenue, 252).abs() * 5.0
    fp = _f37_hypergrowth_fcf_positivity(fcf, revenue, 252).abs()
    base = (g + me + fp) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of signature × cr × close
def f37hgs_f37_hypergrowth_signature_signature_xcr_63d_slope_v130_signal(revenue, netinc, fcf, currentratio, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    base = s * currentratio * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of signature × ato × close
def f37hgs_f37_hypergrowth_signature_signature_xato_252d_slope_v131_signal(revenue, netinc, fcf, assets, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    ato = _safe_div(revenue, assets.abs())
    base = s * ato * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of signature dispersion (63d) × close
def f37hgs_f37_hypergrowth_signature_signature_dispersion_63d_slope_v132_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 21)
    base = _std(s, 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of signature dispersion (252d) × close
def f37hgs_f37_hypergrowth_signature_signature_dispersion_252d_slope_v133_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    base = _std(s, 252) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of signature range × close
def f37hgs_f37_hypergrowth_signature_signature_range_252d_slope_v134_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 21)
    rng = s.rolling(252, min_periods=63).max() - s.rolling(252, min_periods=63).min()
    base = rng * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of signature × eps level × close
def f37hgs_f37_hypergrowth_signature_signature_xepslevel_63d_slope_v135_signal(revenue, netinc, fcf, eps, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    base = s * eps * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of signature × retearn × close
def f37hgs_f37_hypergrowth_signature_signature_xretearn_252d_slope_v136_signal(revenue, netinc, fcf, retearn, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    base = s * retearn.abs() * closeadj * 1e-6
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of signature × shortret × close
def f37hgs_f37_hypergrowth_signature_signature_xshortret_21d_slope_v137_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 21)
    r = closeadj.pct_change(5)
    base = s * r * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of growth × cr × close
def f37hgs_f37_hypergrowth_signature_growthxcr_21d_slope_v138_signal(revenue, currentratio, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 21)
    base = g * currentratio * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of growth × wc × close
def f37hgs_f37_hypergrowth_signature_growthxwc_63d_slope_v139_signal(revenue, workingcapital, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 63)
    base = g * workingcapital.abs() * closeadj * 1e-6
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of margin × wc × close
def f37hgs_f37_hypergrowth_signature_marginxwc_63d_slope_v140_signal(netinc, revenue, workingcapital, closeadj):
    me = _f37_hypergrowth_margin_expansion(netinc, revenue, 63)
    base = me * workingcapital.abs() * closeadj * 1e-5
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of fcfpos × log(assets) × close
def f37hgs_f37_hypergrowth_signature_fcfposxlogassets_252d_slope_v141_signal(fcf, revenue, assets, closeadj):
    fp = _f37_hypergrowth_fcf_positivity(fcf, revenue, 252)
    la = np.log(assets.abs() + 1.0)
    base = fp * la * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of (short growth + long signature) × close
def f37hgs_f37_hypergrowth_signature_shortplus_long_252d_slope_v142_signal(revenue, netinc, fcf, closeadj):
    g_short = _f37_hypergrowth_growth_strength(revenue, 21)
    s_long = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    base = (g_short + s_long) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of signature × revenue scale × close
def f37hgs_f37_hypergrowth_signature_signature_xrevscale_63d_slope_v143_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    rs = revenue.abs() ** 0.5
    base = s * rs * closeadj * 1e-3
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of signature × revenue scale × close
def f37hgs_f37_hypergrowth_signature_signature_xrevscale_252d_slope_v144_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    rs = revenue.abs() ** 0.5
    base = s * rs * closeadj * 1e-3
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of growth × FCF margin (with positivity) × close
def f37hgs_f37_hypergrowth_signature_growthxfcfmargin_63d_slope_v145_signal(revenue, fcf, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 63)
    fm = _safe_div(fcf, revenue.abs())
    base = g * fm * closeadj * _f37_hypergrowth_fcf_positivity(fcf, revenue, 63).clip(-1.0, 1.0)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of growth × FCF margin (252d) × close
def f37hgs_f37_hypergrowth_signature_growthxfcfmargin_252d_slope_v146_signal(revenue, fcf, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 252)
    fm = _safe_div(fcf, revenue.abs())
    base = g * fm * closeadj * _f37_hypergrowth_fcf_positivity(fcf, revenue, 252).clip(-1.0, 1.0)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of signature × ncfi × close
def f37hgs_f37_hypergrowth_signature_signature_xncfi_252d_slope_v147_signal(revenue, netinc, fcf, ncfi, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    base = s * ncfi.abs() * closeadj * 1e-6
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of signature × ncff × close
def f37hgs_f37_hypergrowth_signature_signature_xncff_63d_slope_v148_signal(revenue, netinc, fcf, ncff, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    base = s * ncff.abs() * closeadj * 1e-6
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of signature × log(equity) × close
def f37hgs_f37_hypergrowth_signature_signature_xlogequity_252d_slope_v149_signal(revenue, netinc, fcf, equity, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    le = np.log(equity.abs() + 1.0)
    base = s * le * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of signature × volume × close
def f37hgs_f37_hypergrowth_signature_signature_xvol_21d_slope_v150_signal(revenue, netinc, fcf, closeadj, volume):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 21)
    base = s * volume * closeadj * 1e-6
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f37hgs_f37_hypergrowth_signature_growthstrength_21d_slope_v001_signal,
    f37hgs_f37_hypergrowth_signature_growthstrength_21d_slope_v002_signal,
    f37hgs_f37_hypergrowth_signature_growthstrength_63d_slope_v003_signal,
    f37hgs_f37_hypergrowth_signature_growthstrength_63d_slope_v004_signal,
    f37hgs_f37_hypergrowth_signature_growthstrength_126d_slope_v005_signal,
    f37hgs_f37_hypergrowth_signature_growthstrength_126d_slope_v006_signal,
    f37hgs_f37_hypergrowth_signature_growthstrength_252d_slope_v007_signal,
    f37hgs_f37_hypergrowth_signature_growthstrength_252d_slope_v008_signal,
    f37hgs_f37_hypergrowth_signature_marginexpansion_21d_slope_v009_signal,
    f37hgs_f37_hypergrowth_signature_marginexpansion_21d_slope_v010_signal,
    f37hgs_f37_hypergrowth_signature_marginexpansion_63d_slope_v011_signal,
    f37hgs_f37_hypergrowth_signature_marginexpansion_63d_slope_v012_signal,
    f37hgs_f37_hypergrowth_signature_marginexpansion_252d_slope_v013_signal,
    f37hgs_f37_hypergrowth_signature_marginexpansion_252d_slope_v014_signal,
    f37hgs_f37_hypergrowth_signature_fcfpositivity_21d_slope_v015_signal,
    f37hgs_f37_hypergrowth_signature_fcfpositivity_21d_slope_v016_signal,
    f37hgs_f37_hypergrowth_signature_fcfpositivity_63d_slope_v017_signal,
    f37hgs_f37_hypergrowth_signature_fcfpositivity_63d_slope_v018_signal,
    f37hgs_f37_hypergrowth_signature_fcfpositivity_252d_slope_v019_signal,
    f37hgs_f37_hypergrowth_signature_signature_21d_slope_v020_signal,
    f37hgs_f37_hypergrowth_signature_signature_63d_slope_v021_signal,
    f37hgs_f37_hypergrowth_signature_signature_63d_slope_v022_signal,
    f37hgs_f37_hypergrowth_signature_signature_126d_slope_v023_signal,
    f37hgs_f37_hypergrowth_signature_signature_126d_slope_v024_signal,
    f37hgs_f37_hypergrowth_signature_signature_252d_slope_v025_signal,
    f37hgs_f37_hypergrowth_signature_signature_252d_slope_v026_signal,
    f37hgs_f37_hypergrowth_signature_signature_504d_slope_v027_signal,
    f37hgs_f37_hypergrowth_signature_signature_xrev_63d_slope_v028_signal,
    f37hgs_f37_hypergrowth_signature_signature_xrev_252d_slope_v029_signal,
    f37hgs_f37_hypergrowth_signature_signature_xebitda_63d_slope_v030_signal,
    f37hgs_f37_hypergrowth_signature_signature_xassets_252d_slope_v031_signal,
    f37hgs_f37_hypergrowth_signature_signature_xeps_63d_slope_v032_signal,
    f37hgs_f37_hypergrowth_signature_growthxmargin_63d_slope_v033_signal,
    f37hgs_f37_hypergrowth_signature_growthxmargin_252d_slope_v034_signal,
    f37hgs_f37_hypergrowth_signature_growthxfcfpos_63d_slope_v035_signal,
    f37hgs_f37_hypergrowth_signature_growthxfcfpos_252d_slope_v036_signal,
    f37hgs_f37_hypergrowth_signature_marginxfcfpos_63d_slope_v037_signal,
    f37hgs_f37_hypergrowth_signature_marginxfcfpos_252d_slope_v038_signal,
    f37hgs_f37_hypergrowth_signature_growthstrength_z_252d_slope_v039_signal,
    f37hgs_f37_hypergrowth_signature_marginexpansion_z_252d_slope_v040_signal,
    f37hgs_f37_hypergrowth_signature_fcfpositivity_z_252d_slope_v041_signal,
    f37hgs_f37_hypergrowth_signature_signature_z_252d_slope_v042_signal,
    f37hgs_f37_hypergrowth_signature_signature_mean_63d_slope_v043_signal,
    f37hgs_f37_hypergrowth_signature_signature_mean_252d_slope_v044_signal,
    f37hgs_f37_hypergrowth_signature_signature_std_252d_slope_v045_signal,
    f37hgs_f37_hypergrowth_signature_signature_ema_21d_slope_v046_signal,
    f37hgs_f37_hypergrowth_signature_signature_ema_252d_slope_v047_signal,
    f37hgs_f37_hypergrowth_signature_signature_sum_252d_slope_v048_signal,
    f37hgs_f37_hypergrowth_signature_signature_sum_504d_slope_v049_signal,
    f37hgs_f37_hypergrowth_signature_signature_poscount_252d_slope_v050_signal,
    f37hgs_f37_hypergrowth_signature_growthstrength_count_504d_slope_v051_signal,
    f37hgs_f37_hypergrowth_signature_marginexpansion_poscount_252d_slope_v052_signal,
    f37hgs_f37_hypergrowth_signature_fcfpositivity_poscount_252d_slope_v053_signal,
    f37hgs_f37_hypergrowth_signature_growthstrength_xebitda_63d_slope_v054_signal,
    f37hgs_f37_hypergrowth_signature_growthstrength_xnetinc_252d_slope_v055_signal,
    f37hgs_f37_hypergrowth_signature_growthstrength_xdv_63d_slope_v056_signal,
    f37hgs_f37_hypergrowth_signature_marginexpansion_xdv_252d_slope_v057_signal,
    f37hgs_f37_hypergrowth_signature_fcfpositivity_xdv_63d_slope_v058_signal,
    f37hgs_f37_hypergrowth_signature_growthxmom_63d_slope_v059_signal,
    f37hgs_f37_hypergrowth_signature_growthxmom_252d_slope_v060_signal,
    f37hgs_f37_hypergrowth_signature_signature_normretvol_21d_slope_v061_signal,
    f37hgs_f37_hypergrowth_signature_signature_normretvol_252d_slope_v062_signal,
    f37hgs_f37_hypergrowth_signature_growthxato_63d_slope_v063_signal,
    f37hgs_f37_hypergrowth_signature_growthxcr_252d_slope_v064_signal,
    f37hgs_f37_hypergrowth_signature_signature_xdebt_63d_slope_v065_signal,
    f37hgs_f37_hypergrowth_signature_signature_xequity_252d_slope_v066_signal,
    f37hgs_f37_hypergrowth_signature_signature_xncfo_63d_slope_v067_signal,
    f37hgs_f37_hypergrowth_signature_signature_xwc_252d_slope_v068_signal,
    f37hgs_f37_hypergrowth_signature_signature_xvolz_63d_slope_v069_signal,
    f37hgs_f37_hypergrowth_signature_signature_xatr_252d_slope_v070_signal,
    f37hgs_f37_hypergrowth_signature_growthxrevtrend_63d_slope_v071_signal,
    f37hgs_f37_hypergrowth_signature_signature_diff_21m63_slope_v072_signal,
    f37hgs_f37_hypergrowth_signature_signature_diff_63m252_slope_v073_signal,
    f37hgs_f37_hypergrowth_signature_signature_diff_252m504_slope_v074_signal,
    f37hgs_f37_hypergrowth_signature_signature_max_252d_slope_v075_signal,
    f37hgs_f37_hypergrowth_signature_signature_min_504d_slope_v076_signal,
    f37hgs_f37_hypergrowth_signature_growthstrength_xlogrev_63d_slope_v077_signal,
    f37hgs_f37_hypergrowth_signature_signature_xepstrend_63d_slope_v078_signal,
    f37hgs_f37_hypergrowth_signature_signature_xeps_252d_slope_v079_signal,
    f37hgs_f37_hypergrowth_signature_signature_xebitdagrowth_63d_slope_v080_signal,
    f37hgs_f37_hypergrowth_signature_growthstrength_sq_63d_slope_v081_signal,
    f37hgs_f37_hypergrowth_signature_growthstrength_sq_252d_slope_v082_signal,
    f37hgs_f37_hypergrowth_signature_signature_xsharesbas_252d_slope_v083_signal,
    f37hgs_f37_hypergrowth_signature_signature_xncfi_63d_slope_v084_signal,
    f37hgs_f37_hypergrowth_signature_signature_xcapex_252d_slope_v085_signal,
    f37hgs_f37_hypergrowth_signature_triple_252d_slope_v086_signal,
    f37hgs_f37_hypergrowth_signature_signature_xvolsum_63d_slope_v087_signal,
    f37hgs_f37_hypergrowth_signature_growthstrength_5d_slope_v088_signal,
    f37hgs_f37_hypergrowth_signature_growthstrength_10d_slope_v089_signal,
    f37hgs_f37_hypergrowth_signature_growthstrength_42d_slope_v090_signal,
    f37hgs_f37_hypergrowth_signature_growthstrength_189d_slope_v091_signal,
    f37hgs_f37_hypergrowth_signature_growthstrength_504d_slope_v092_signal,
    f37hgs_f37_hypergrowth_signature_marginexpansion_op_5d_slope_v093_signal,
    f37hgs_f37_hypergrowth_signature_marginexpansion_op_21d_slope_v094_signal,
    f37hgs_f37_hypergrowth_signature_marginexpansion_op_63d_slope_v095_signal,
    f37hgs_f37_hypergrowth_signature_marginexpansion_op_252d_slope_v096_signal,
    f37hgs_f37_hypergrowth_signature_marginexpansion_gp_21d_slope_v097_signal,
    f37hgs_f37_hypergrowth_signature_marginexpansion_gp_252d_slope_v098_signal,
    f37hgs_f37_hypergrowth_signature_marginexpansion_ebitda_63d_slope_v099_signal,
    f37hgs_f37_hypergrowth_signature_marginexpansion_ebitda_252d_slope_v100_signal,
    f37hgs_f37_hypergrowth_signature_fcfpositivity_5d_slope_v101_signal,
    f37hgs_f37_hypergrowth_signature_fcfpositivity_42d_slope_v102_signal,
    f37hgs_f37_hypergrowth_signature_fcfpositivity_504d_slope_v103_signal,
    f37hgs_f37_hypergrowth_signature_signature_op_21d_slope_v104_signal,
    f37hgs_f37_hypergrowth_signature_signature_op_252d_slope_v105_signal,
    f37hgs_f37_hypergrowth_signature_signature_gp_252d_slope_v106_signal,
    f37hgs_f37_hypergrowth_signature_signature_ebitda_252d_slope_v107_signal,
    f37hgs_f37_hypergrowth_signature_signature_ncfo_63d_slope_v108_signal,
    f37hgs_f37_hypergrowth_signature_signature_ncfo_252d_slope_v109_signal,
    f37hgs_f37_hypergrowth_signature_tripleproduct_63d_slope_v110_signal,
    f37hgs_f37_hypergrowth_signature_tripleproduct_252d_slope_v111_signal,
    f37hgs_f37_hypergrowth_signature_tripleproduct_504d_slope_v112_signal,
    f37hgs_f37_hypergrowth_signature_signature_xlogrev_252d_slope_v113_signal,
    f37hgs_f37_hypergrowth_signature_growthstrength_xdvsum_63d_slope_v114_signal,
    f37hgs_f37_hypergrowth_signature_growthstrength_xdvsum_252d_slope_v115_signal,
    f37hgs_f37_hypergrowth_signature_signature_xtaxexp_63d_slope_v116_signal,
    f37hgs_f37_hypergrowth_signature_signature_xintexp_252d_slope_v117_signal,
    f37hgs_f37_hypergrowth_signature_signature_xshortmom_21d_slope_v118_signal,
    f37hgs_f37_hypergrowth_signature_signature_xlongmom_252d_slope_v119_signal,
    f37hgs_f37_hypergrowth_signature_signature_xclosez_63d_slope_v120_signal,
    f37hgs_f37_hypergrowth_signature_signature_xclosez_252d_slope_v121_signal,
    f37hgs_f37_hypergrowth_signature_growthxebitdagrowth_63d_slope_v122_signal,
    f37hgs_f37_hypergrowth_signature_growthxebitdagrowth_252d_slope_v123_signal,
    f37hgs_f37_hypergrowth_signature_signature_xvolsum_252d_slope_v124_signal,
    f37hgs_f37_hypergrowth_signature_signature_xrange_63d_slope_v125_signal,
    f37hgs_f37_hypergrowth_signature_growthxrange_21d_slope_v126_signal,
    f37hgs_f37_hypergrowth_signature_signature_xlogassets_252d_slope_v127_signal,
    f37hgs_f37_hypergrowth_signature_magnitudesum_21d_slope_v128_signal,
    f37hgs_f37_hypergrowth_signature_magnitudesum_252d_slope_v129_signal,
    f37hgs_f37_hypergrowth_signature_signature_xcr_63d_slope_v130_signal,
    f37hgs_f37_hypergrowth_signature_signature_xato_252d_slope_v131_signal,
    f37hgs_f37_hypergrowth_signature_signature_dispersion_63d_slope_v132_signal,
    f37hgs_f37_hypergrowth_signature_signature_dispersion_252d_slope_v133_signal,
    f37hgs_f37_hypergrowth_signature_signature_range_252d_slope_v134_signal,
    f37hgs_f37_hypergrowth_signature_signature_xepslevel_63d_slope_v135_signal,
    f37hgs_f37_hypergrowth_signature_signature_xretearn_252d_slope_v136_signal,
    f37hgs_f37_hypergrowth_signature_signature_xshortret_21d_slope_v137_signal,
    f37hgs_f37_hypergrowth_signature_growthxcr_21d_slope_v138_signal,
    f37hgs_f37_hypergrowth_signature_growthxwc_63d_slope_v139_signal,
    f37hgs_f37_hypergrowth_signature_marginxwc_63d_slope_v140_signal,
    f37hgs_f37_hypergrowth_signature_fcfposxlogassets_252d_slope_v141_signal,
    f37hgs_f37_hypergrowth_signature_shortplus_long_252d_slope_v142_signal,
    f37hgs_f37_hypergrowth_signature_signature_xrevscale_63d_slope_v143_signal,
    f37hgs_f37_hypergrowth_signature_signature_xrevscale_252d_slope_v144_signal,
    f37hgs_f37_hypergrowth_signature_growthxfcfmargin_63d_slope_v145_signal,
    f37hgs_f37_hypergrowth_signature_growthxfcfmargin_252d_slope_v146_signal,
    f37hgs_f37_hypergrowth_signature_signature_xncfi_252d_slope_v147_signal,
    f37hgs_f37_hypergrowth_signature_signature_xncff_63d_slope_v148_signal,
    f37hgs_f37_hypergrowth_signature_signature_xlogequity_252d_slope_v149_signal,
    f37hgs_f37_hypergrowth_signature_signature_xvol_21d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F37_HYPERGROWTH_SIGNATURE_REGISTRY_SLOPE = REGISTRY


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
    opinc = pd.Series(1.5e6 * np.exp(np.cumsum(np.random.normal(0.0006, 0.011, n))) * np.sign(np.random.normal(0.6, 1.0, n)), name="opinc")
    gp = pd.Series(3e6 * np.exp(np.cumsum(np.random.normal(0.0007, 0.009, n))), name="gp")
    ebitda = pd.Series(2e6 * np.exp(np.cumsum(np.random.normal(0.0006, 0.01, n))) * np.sign(np.random.normal(0.7, 1.0, n)), name="ebitda")
    eps = pd.Series(np.cumsum(np.random.normal(0.001, 0.05, n)) + 1.0, name="eps")
    fcf = pd.Series(8e5 * np.exp(np.cumsum(np.random.normal(0.0005, 0.013, n))) * np.sign(np.random.normal(0.6, 1.0, n)), name="fcf")
    ncfo = pd.Series(1.2e6 * np.exp(np.cumsum(np.random.normal(0.0006, 0.012, n))) * np.sign(np.random.normal(0.8, 1.0, n)), name="ncfo")
    ncfi = pd.Series(7e5 * np.exp(np.cumsum(np.random.normal(0.0003, 0.011, n))) * np.sign(np.random.normal(0.4, 1.0, n)), name="ncfi")
    ncff = pd.Series(6e5 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))) * np.sign(np.random.normal(0.3, 1.0, n)), name="ncff")
    capex = pd.Series(9e5 * np.exp(np.cumsum(np.random.normal(0.0004, 0.011, n))), name="capex")
    intexp = pd.Series(2e5 * np.exp(np.cumsum(np.random.normal(0.0003, 0.008, n))), name="intexp")
    taxexp = pd.Series(3e5 * np.exp(np.cumsum(np.random.normal(0.0004, 0.009, n))), name="taxexp")
    sharesbas = pd.Series(1e7 + np.cumsum(np.random.normal(1e3, 5e3, n)), name="sharesbas")
    assets = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0004, 0.006, n))), name="assets")
    debt = pd.Series(1e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.008, n))), name="debt")
    equity = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0005, 0.007, n))), name="equity")
    workingcapital = pd.Series(8e6 * np.exp(np.cumsum(np.random.normal(0.0004, 0.01, n))) * np.sign(np.random.normal(0.7, 1.0, n)), name="workingcapital")
    currentratio = pd.Series(1.5 + np.cumsum(np.random.normal(0.0, 0.01, n)) * 0.1, name="currentratio")
    retearn = pd.Series(1e7 * np.exp(np.cumsum(np.random.normal(0.0004, 0.009, n))) * np.sign(np.random.normal(0.7, 1.0, n)), name="retearn")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "netinc": netinc, "opinc": opinc, "gp": gp, "ebitda": ebitda,
        "eps": eps, "fcf": fcf, "ncfo": ncfo, "ncfi": ncfi, "ncff": ncff, "capex": capex,
        "intexp": intexp, "taxexp": taxexp, "sharesbas": sharesbas,
        "assets": assets, "debt": debt, "equity": equity,
        "workingcapital": workingcapital, "currentratio": currentratio, "retearn": retearn,
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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f37_hypergrowth_signature_2nd_derivatives_001_150_claude: {n_features} features pass")
