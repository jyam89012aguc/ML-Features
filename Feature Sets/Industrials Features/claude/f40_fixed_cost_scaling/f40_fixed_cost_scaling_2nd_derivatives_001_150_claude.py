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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _ema(s, w):
    return s.ewm(span=w, adjust=False, min_periods=max(1, w // 2)).mean()


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f40_sgna_intensity(sgna, revenue):
    """SG&A as fraction of revenue."""
    return sgna / revenue.replace(0, np.nan)


def _f40_sgna_revenue_gap(sgna, revenue, w):
    """SG&A growth minus revenue growth over window."""
    sgna_g = sgna.pct_change(periods=w)
    rev_g = revenue.pct_change(periods=w)
    return sgna_g - rev_g


def _f40_fixed_cost_leverage(sgna, revenue, w):
    """Operating leverage from SG&A: incremental SG&A per incremental revenue."""
    ds = sgna.diff(periods=w)
    dr = revenue.diff(periods=w)
    return ds / dr.replace(0, np.nan)


def f40fcs_f40_fixed_cost_scaling_sgnaintensity_5d_5d_slope_v001_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _mean(s, 5) * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_sgnaintensity_10d_21d_slope_v002_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _mean(s, 10) * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_sgnaintensity_21d_63d_slope_v003_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _mean(s, 21) * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_sgnaintensity_42d_126d_slope_v004_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _mean(s, 42) * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_sgnaintensity_63d_252d_slope_v005_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _mean(s, 63) * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_sgnaintensity_126d_5d_slope_v006_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _mean(s, 126) * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_sgnaintensity_189d_21d_slope_v007_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _mean(s, 189) * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_sgnaintensity_252d_63d_slope_v008_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _mean(s, 252) * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_sgnaintensity_378d_126d_slope_v009_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _mean(s, 378) * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_sgnaintensity_504d_252d_slope_v010_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _mean(s, 504) * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_sgnarevgap_5d_5d_slope_v011_signal(sgna, revenue, closeadj):
    g = _f40_sgna_revenue_gap(sgna, revenue, 5)
    base_ = g * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_sgnarevgap_10d_21d_slope_v012_signal(sgna, revenue, closeadj):
    g = _f40_sgna_revenue_gap(sgna, revenue, 10)
    base_ = g * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_sgnarevgap_21d_63d_slope_v013_signal(sgna, revenue, closeadj):
    g = _f40_sgna_revenue_gap(sgna, revenue, 21)
    base_ = g * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_sgnarevgap_42d_126d_slope_v014_signal(sgna, revenue, closeadj):
    g = _f40_sgna_revenue_gap(sgna, revenue, 42)
    base_ = g * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_sgnarevgap_63d_252d_slope_v015_signal(sgna, revenue, closeadj):
    g = _f40_sgna_revenue_gap(sgna, revenue, 63)
    base_ = g * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_sgnarevgap_126d_5d_slope_v016_signal(sgna, revenue, closeadj):
    g = _f40_sgna_revenue_gap(sgna, revenue, 126)
    base_ = g * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_sgnarevgap_189d_21d_slope_v017_signal(sgna, revenue, closeadj):
    g = _f40_sgna_revenue_gap(sgna, revenue, 189)
    base_ = g * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_sgnarevgap_252d_63d_slope_v018_signal(sgna, revenue, closeadj):
    g = _f40_sgna_revenue_gap(sgna, revenue, 252)
    base_ = g * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_sgnarevgap_378d_126d_slope_v019_signal(sgna, revenue, closeadj):
    g = _f40_sgna_revenue_gap(sgna, revenue, 378)
    base_ = g * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_sgnarevgap_504d_252d_slope_v020_signal(sgna, revenue, closeadj):
    g = _f40_sgna_revenue_gap(sgna, revenue, 504)
    base_ = g * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_fixedlev_5d_5d_slope_v021_signal(sgna, revenue, closeadj):
    l = _f40_fixed_cost_leverage(sgna, revenue, 5)
    base_ = l.clip(-100, 100) * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_fixedlev_10d_21d_slope_v022_signal(sgna, revenue, closeadj):
    l = _f40_fixed_cost_leverage(sgna, revenue, 10)
    base_ = l.clip(-100, 100) * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_fixedlev_21d_63d_slope_v023_signal(sgna, revenue, closeadj):
    l = _f40_fixed_cost_leverage(sgna, revenue, 21)
    base_ = l.clip(-100, 100) * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_fixedlev_42d_126d_slope_v024_signal(sgna, revenue, closeadj):
    l = _f40_fixed_cost_leverage(sgna, revenue, 42)
    base_ = l.clip(-100, 100) * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_fixedlev_63d_252d_slope_v025_signal(sgna, revenue, closeadj):
    l = _f40_fixed_cost_leverage(sgna, revenue, 63)
    base_ = l.clip(-100, 100) * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_fixedlev_126d_5d_slope_v026_signal(sgna, revenue, closeadj):
    l = _f40_fixed_cost_leverage(sgna, revenue, 126)
    base_ = l.clip(-100, 100) * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_fixedlev_189d_21d_slope_v027_signal(sgna, revenue, closeadj):
    l = _f40_fixed_cost_leverage(sgna, revenue, 189)
    base_ = l.clip(-100, 100) * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_fixedlev_252d_63d_slope_v028_signal(sgna, revenue, closeadj):
    l = _f40_fixed_cost_leverage(sgna, revenue, 252)
    base_ = l.clip(-100, 100) * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_fixedlev_378d_126d_slope_v029_signal(sgna, revenue, closeadj):
    l = _f40_fixed_cost_leverage(sgna, revenue, 378)
    base_ = l.clip(-100, 100) * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_fixedlev_504d_252d_slope_v030_signal(sgna, revenue, closeadj):
    l = _f40_fixed_cost_leverage(sgna, revenue, 504)
    base_ = l.clip(-100, 100) * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_sgnaintdiff_5d_5d_slope_v031_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = s.diff(5) * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_sgnaintdiff_10d_21d_slope_v032_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = s.diff(10) * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_sgnaintdiff_21d_63d_slope_v033_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = s.diff(21) * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_sgnaintdiff_42d_126d_slope_v034_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = s.diff(42) * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_sgnaintdiff_63d_252d_slope_v035_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = s.diff(63) * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_sgnaintdiff_126d_5d_slope_v036_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = s.diff(126) * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_sgnaintdiff_189d_21d_slope_v037_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = s.diff(189) * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_sgnaintdiff_252d_63d_slope_v038_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = s.diff(252) * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_sgnaintdiff_378d_126d_slope_v039_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = s.diff(378) * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_sgnaintdiff_504d_252d_slope_v040_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = s.diff(504) * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_sgnaintxopex_5d_5d_slope_v041_signal(sgna, revenue, opex, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _mean(s, 5) * _safe_div(opex, revenue) * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_sgnaintxopex_10d_21d_slope_v042_signal(sgna, revenue, opex, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _mean(s, 10) * _safe_div(opex, revenue) * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_sgnaintxopex_21d_63d_slope_v043_signal(sgna, revenue, opex, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _mean(s, 21) * _safe_div(opex, revenue) * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_sgnaintxopex_42d_126d_slope_v044_signal(sgna, revenue, opex, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _mean(s, 42) * _safe_div(opex, revenue) * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_sgnaintxopex_63d_252d_slope_v045_signal(sgna, revenue, opex, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _mean(s, 63) * _safe_div(opex, revenue) * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_sgnaintxopex_126d_5d_slope_v046_signal(sgna, revenue, opex, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _mean(s, 126) * _safe_div(opex, revenue) * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_sgnaintxopex_189d_21d_slope_v047_signal(sgna, revenue, opex, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _mean(s, 189) * _safe_div(opex, revenue) * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_sgnaintxopex_252d_63d_slope_v048_signal(sgna, revenue, opex, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _mean(s, 252) * _safe_div(opex, revenue) * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_sgnaintxopex_378d_126d_slope_v049_signal(sgna, revenue, opex, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _mean(s, 378) * _safe_div(opex, revenue) * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_sgnaintxopex_504d_252d_slope_v050_signal(sgna, revenue, opex, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _mean(s, 504) * _safe_div(opex, revenue) * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_gapxint_5d_5d_slope_v051_signal(sgna, revenue, closeadj):
    g = _f40_sgna_revenue_gap(sgna, revenue, 5)
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = (g * s) * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_gapxint_10d_21d_slope_v052_signal(sgna, revenue, closeadj):
    g = _f40_sgna_revenue_gap(sgna, revenue, 10)
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = (g * s) * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_gapxint_21d_63d_slope_v053_signal(sgna, revenue, closeadj):
    g = _f40_sgna_revenue_gap(sgna, revenue, 21)
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = (g * s) * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_gapxint_42d_126d_slope_v054_signal(sgna, revenue, closeadj):
    g = _f40_sgna_revenue_gap(sgna, revenue, 42)
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = (g * s) * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_gapxint_63d_252d_slope_v055_signal(sgna, revenue, closeadj):
    g = _f40_sgna_revenue_gap(sgna, revenue, 63)
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = (g * s) * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_gapxint_126d_5d_slope_v056_signal(sgna, revenue, closeadj):
    g = _f40_sgna_revenue_gap(sgna, revenue, 126)
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = (g * s) * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_gapxint_189d_21d_slope_v057_signal(sgna, revenue, closeadj):
    g = _f40_sgna_revenue_gap(sgna, revenue, 189)
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = (g * s) * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_gapxint_252d_63d_slope_v058_signal(sgna, revenue, closeadj):
    g = _f40_sgna_revenue_gap(sgna, revenue, 252)
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = (g * s) * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_gapxint_378d_126d_slope_v059_signal(sgna, revenue, closeadj):
    g = _f40_sgna_revenue_gap(sgna, revenue, 378)
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = (g * s) * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_gapxint_504d_252d_slope_v060_signal(sgna, revenue, closeadj):
    g = _f40_sgna_revenue_gap(sgna, revenue, 504)
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = (g * s) * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_fixedlevz_21_252_5d_slope_v061_signal(sgna, revenue, closeadj):
    l = _f40_fixed_cost_leverage(sgna, revenue, 21)
    base_ = _z(l.clip(-100, 100), 252) * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_fixedlevz_63_252_21d_slope_v062_signal(sgna, revenue, closeadj):
    l = _f40_fixed_cost_leverage(sgna, revenue, 63)
    base_ = _z(l.clip(-100, 100), 252) * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_fixedlevz_126_252_63d_slope_v063_signal(sgna, revenue, closeadj):
    l = _f40_fixed_cost_leverage(sgna, revenue, 126)
    base_ = _z(l.clip(-100, 100), 252) * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_fixedlevz_21_504_126d_slope_v064_signal(sgna, revenue, closeadj):
    l = _f40_fixed_cost_leverage(sgna, revenue, 21)
    base_ = _z(l.clip(-100, 100), 504) * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_fixedlevz_63_504_252d_slope_v065_signal(sgna, revenue, closeadj):
    l = _f40_fixed_cost_leverage(sgna, revenue, 63)
    base_ = _z(l.clip(-100, 100), 504) * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_fixedlevz_126_504_5d_slope_v066_signal(sgna, revenue, closeadj):
    l = _f40_fixed_cost_leverage(sgna, revenue, 126)
    base_ = _z(l.clip(-100, 100), 504) * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_gapsm_63d_21d_slope_v067_signal(sgna, revenue, closeadj):
    g = _f40_sgna_revenue_gap(sgna, revenue, 63)
    base_ = _mean(g, 21) * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_gapsm_126d_63d_slope_v068_signal(sgna, revenue, closeadj):
    g = _f40_sgna_revenue_gap(sgna, revenue, 126)
    base_ = _mean(g, 21) * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_gapsm_189d_126d_slope_v069_signal(sgna, revenue, closeadj):
    g = _f40_sgna_revenue_gap(sgna, revenue, 189)
    base_ = _mean(g, 21) * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_gapsm_252d_252d_slope_v070_signal(sgna, revenue, closeadj):
    g = _f40_sgna_revenue_gap(sgna, revenue, 252)
    base_ = _mean(g, 21) * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_gapsm_378d_5d_slope_v071_signal(sgna, revenue, closeadj):
    g = _f40_sgna_revenue_gap(sgna, revenue, 378)
    base_ = _mean(g, 21) * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_gapsm_504d_21d_slope_v072_signal(sgna, revenue, closeadj):
    g = _f40_sgna_revenue_gap(sgna, revenue, 504)
    base_ = _mean(g, 21) * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_intensityema_5d_63d_slope_v073_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _ema(s, 5) * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_intensityema_10d_126d_slope_v074_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _ema(s, 10) * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_intensityema_21d_252d_slope_v075_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _ema(s, 21) * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_intensityema_42d_5d_slope_v076_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _ema(s, 42) * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_intensityema_63d_21d_slope_v077_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _ema(s, 63) * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_intensityema_126d_63d_slope_v078_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _ema(s, 126) * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_intensityema_189d_126d_slope_v079_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _ema(s, 189) * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_intensityema_252d_252d_slope_v080_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _ema(s, 252) * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_intensityema_378d_5d_slope_v081_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _ema(s, 378) * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_intensityema_504d_21d_slope_v082_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _ema(s, 504) * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_intensitystd_63d_63d_slope_v083_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _std(s, 63) * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_intensitystd_126d_126d_slope_v084_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _std(s, 126) * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_intensitystd_189d_252d_slope_v085_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _std(s, 189) * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_intensitystd_252d_5d_slope_v086_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _std(s, 252) * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_intensitystd_378d_21d_slope_v087_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _std(s, 378) * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_intensitystd_504d_63d_slope_v088_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _std(s, 504) * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_gapxrevpct_5d_126d_slope_v089_signal(sgna, revenue, closeadj):
    g = _f40_sgna_revenue_gap(sgna, revenue, 5)
    base_ = g * revenue.pct_change(5) * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_gapxrevpct_10d_252d_slope_v090_signal(sgna, revenue, closeadj):
    g = _f40_sgna_revenue_gap(sgna, revenue, 10)
    base_ = g * revenue.pct_change(10) * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_gapxrevpct_21d_5d_slope_v091_signal(sgna, revenue, closeadj):
    g = _f40_sgna_revenue_gap(sgna, revenue, 21)
    base_ = g * revenue.pct_change(21) * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_gapxrevpct_42d_21d_slope_v092_signal(sgna, revenue, closeadj):
    g = _f40_sgna_revenue_gap(sgna, revenue, 42)
    base_ = g * revenue.pct_change(42) * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_gapxrevpct_63d_63d_slope_v093_signal(sgna, revenue, closeadj):
    g = _f40_sgna_revenue_gap(sgna, revenue, 63)
    base_ = g * revenue.pct_change(63) * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_gapxrevpct_126d_126d_slope_v094_signal(sgna, revenue, closeadj):
    g = _f40_sgna_revenue_gap(sgna, revenue, 126)
    base_ = g * revenue.pct_change(126) * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_gapxrevpct_189d_252d_slope_v095_signal(sgna, revenue, closeadj):
    g = _f40_sgna_revenue_gap(sgna, revenue, 189)
    base_ = g * revenue.pct_change(189) * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_gapxrevpct_252d_5d_slope_v096_signal(sgna, revenue, closeadj):
    g = _f40_sgna_revenue_gap(sgna, revenue, 252)
    base_ = g * revenue.pct_change(252) * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_gapxrevpct_378d_21d_slope_v097_signal(sgna, revenue, closeadj):
    g = _f40_sgna_revenue_gap(sgna, revenue, 378)
    base_ = g * revenue.pct_change(378) * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_gapxrevpct_504d_63d_slope_v098_signal(sgna, revenue, closeadj):
    g = _f40_sgna_revenue_gap(sgna, revenue, 504)
    base_ = g * revenue.pct_change(504) * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_fixedlevxopex_5d_126d_slope_v099_signal(sgna, revenue, opex, closeadj):
    l = _f40_fixed_cost_leverage(sgna, revenue, 5)
    base_ = l.clip(-100, 100) * _safe_div(opex, revenue) * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_fixedlevxopex_10d_252d_slope_v100_signal(sgna, revenue, opex, closeadj):
    l = _f40_fixed_cost_leverage(sgna, revenue, 10)
    base_ = l.clip(-100, 100) * _safe_div(opex, revenue) * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_fixedlevxopex_21d_5d_slope_v101_signal(sgna, revenue, opex, closeadj):
    l = _f40_fixed_cost_leverage(sgna, revenue, 21)
    base_ = l.clip(-100, 100) * _safe_div(opex, revenue) * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_fixedlevxopex_42d_21d_slope_v102_signal(sgna, revenue, opex, closeadj):
    l = _f40_fixed_cost_leverage(sgna, revenue, 42)
    base_ = l.clip(-100, 100) * _safe_div(opex, revenue) * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_fixedlevxopex_63d_63d_slope_v103_signal(sgna, revenue, opex, closeadj):
    l = _f40_fixed_cost_leverage(sgna, revenue, 63)
    base_ = l.clip(-100, 100) * _safe_div(opex, revenue) * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_fixedlevxopex_126d_126d_slope_v104_signal(sgna, revenue, opex, closeadj):
    l = _f40_fixed_cost_leverage(sgna, revenue, 126)
    base_ = l.clip(-100, 100) * _safe_div(opex, revenue) * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_fixedlevxopex_189d_252d_slope_v105_signal(sgna, revenue, opex, closeadj):
    l = _f40_fixed_cost_leverage(sgna, revenue, 189)
    base_ = l.clip(-100, 100) * _safe_div(opex, revenue) * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_fixedlevxopex_252d_5d_slope_v106_signal(sgna, revenue, opex, closeadj):
    l = _f40_fixed_cost_leverage(sgna, revenue, 252)
    base_ = l.clip(-100, 100) * _safe_div(opex, revenue) * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_fixedlevxopex_378d_21d_slope_v107_signal(sgna, revenue, opex, closeadj):
    l = _f40_fixed_cost_leverage(sgna, revenue, 378)
    base_ = l.clip(-100, 100) * _safe_div(opex, revenue) * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_fixedlevxopex_504d_63d_slope_v108_signal(sgna, revenue, opex, closeadj):
    l = _f40_fixed_cost_leverage(sgna, revenue, 504)
    base_ = l.clip(-100, 100) * _safe_div(opex, revenue) * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_opexrevgap_5d_126d_slope_v109_signal(opex, revenue, closeadj):
    g = _f40_sgna_revenue_gap(opex, revenue, 5)
    base_ = g * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_opexrevgap_10d_252d_slope_v110_signal(opex, revenue, closeadj):
    g = _f40_sgna_revenue_gap(opex, revenue, 10)
    base_ = g * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_opexrevgap_21d_5d_slope_v111_signal(opex, revenue, closeadj):
    g = _f40_sgna_revenue_gap(opex, revenue, 21)
    base_ = g * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_opexrevgap_42d_21d_slope_v112_signal(opex, revenue, closeadj):
    g = _f40_sgna_revenue_gap(opex, revenue, 42)
    base_ = g * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_opexrevgap_63d_63d_slope_v113_signal(opex, revenue, closeadj):
    g = _f40_sgna_revenue_gap(opex, revenue, 63)
    base_ = g * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_opexrevgap_126d_126d_slope_v114_signal(opex, revenue, closeadj):
    g = _f40_sgna_revenue_gap(opex, revenue, 126)
    base_ = g * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_opexrevgap_189d_252d_slope_v115_signal(opex, revenue, closeadj):
    g = _f40_sgna_revenue_gap(opex, revenue, 189)
    base_ = g * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_opexrevgap_252d_5d_slope_v116_signal(opex, revenue, closeadj):
    g = _f40_sgna_revenue_gap(opex, revenue, 252)
    base_ = g * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_opexrevgap_378d_21d_slope_v117_signal(opex, revenue, closeadj):
    g = _f40_sgna_revenue_gap(opex, revenue, 378)
    base_ = g * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_opexrevgap_504d_63d_slope_v118_signal(opex, revenue, closeadj):
    g = _f40_sgna_revenue_gap(opex, revenue, 504)
    base_ = g * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_intensitysq_5d_126d_slope_v119_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _mean(s, 5) * s * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_intensitysq_10d_252d_slope_v120_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _mean(s, 10) * s * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_intensitysq_21d_5d_slope_v121_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _mean(s, 21) * s * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_intensitysq_42d_21d_slope_v122_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _mean(s, 42) * s * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_intensitysq_63d_63d_slope_v123_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _mean(s, 63) * s * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_intensitysq_126d_126d_slope_v124_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _mean(s, 126) * s * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_intensitysq_189d_252d_slope_v125_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _mean(s, 189) * s * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_intensitysq_252d_5d_slope_v126_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _mean(s, 252) * s * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_intensitysq_378d_21d_slope_v127_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _mean(s, 378) * s * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_intensitysq_504d_63d_slope_v128_signal(sgna, revenue, closeadj):
    s = _f40_sgna_intensity(sgna, revenue)
    base_ = _mean(s, 504) * s * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_fixedlevdiff_5d_126d_slope_v129_signal(sgna, revenue, closeadj):
    l = _f40_fixed_cost_leverage(sgna, revenue, 5)
    base_ = l.clip(-100, 100).diff(21) * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_fixedlevdiff_10d_252d_slope_v130_signal(sgna, revenue, closeadj):
    l = _f40_fixed_cost_leverage(sgna, revenue, 10)
    base_ = l.clip(-100, 100).diff(21) * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_fixedlevdiff_21d_5d_slope_v131_signal(sgna, revenue, closeadj):
    l = _f40_fixed_cost_leverage(sgna, revenue, 21)
    base_ = l.clip(-100, 100).diff(21) * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_fixedlevdiff_42d_21d_slope_v132_signal(sgna, revenue, closeadj):
    l = _f40_fixed_cost_leverage(sgna, revenue, 42)
    base_ = l.clip(-100, 100).diff(21) * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_fixedlevdiff_63d_63d_slope_v133_signal(sgna, revenue, closeadj):
    l = _f40_fixed_cost_leverage(sgna, revenue, 63)
    base_ = l.clip(-100, 100).diff(21) * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_fixedlevdiff_126d_126d_slope_v134_signal(sgna, revenue, closeadj):
    l = _f40_fixed_cost_leverage(sgna, revenue, 126)
    base_ = l.clip(-100, 100).diff(21) * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_fixedlevdiff_189d_252d_slope_v135_signal(sgna, revenue, closeadj):
    l = _f40_fixed_cost_leverage(sgna, revenue, 189)
    base_ = l.clip(-100, 100).diff(21) * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_fixedlevdiff_252d_5d_slope_v136_signal(sgna, revenue, closeadj):
    l = _f40_fixed_cost_leverage(sgna, revenue, 252)
    base_ = l.clip(-100, 100).diff(21) * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_fixedlevdiff_378d_21d_slope_v137_signal(sgna, revenue, closeadj):
    l = _f40_fixed_cost_leverage(sgna, revenue, 378)
    base_ = l.clip(-100, 100).diff(21) * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_fixedlevdiff_504d_63d_slope_v138_signal(sgna, revenue, closeadj):
    l = _f40_fixed_cost_leverage(sgna, revenue, 504)
    base_ = l.clip(-100, 100).diff(21) * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_opexfixedlev_5d_126d_slope_v139_signal(opex, revenue, closeadj):
    l = _f40_fixed_cost_leverage(opex, revenue, 5)
    base_ = l.clip(-100, 100) * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_opexfixedlev_10d_252d_slope_v140_signal(opex, revenue, closeadj):
    l = _f40_fixed_cost_leverage(opex, revenue, 10)
    base_ = l.clip(-100, 100) * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_opexfixedlev_21d_5d_slope_v141_signal(opex, revenue, closeadj):
    l = _f40_fixed_cost_leverage(opex, revenue, 21)
    base_ = l.clip(-100, 100) * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_opexfixedlev_42d_21d_slope_v142_signal(opex, revenue, closeadj):
    l = _f40_fixed_cost_leverage(opex, revenue, 42)
    base_ = l.clip(-100, 100) * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_opexfixedlev_63d_63d_slope_v143_signal(opex, revenue, closeadj):
    l = _f40_fixed_cost_leverage(opex, revenue, 63)
    base_ = l.clip(-100, 100) * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_opexfixedlev_126d_126d_slope_v144_signal(opex, revenue, closeadj):
    l = _f40_fixed_cost_leverage(opex, revenue, 126)
    base_ = l.clip(-100, 100) * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_opexfixedlev_189d_252d_slope_v145_signal(opex, revenue, closeadj):
    l = _f40_fixed_cost_leverage(opex, revenue, 189)
    base_ = l.clip(-100, 100) * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_opexfixedlev_252d_5d_slope_v146_signal(opex, revenue, closeadj):
    l = _f40_fixed_cost_leverage(opex, revenue, 252)
    base_ = l.clip(-100, 100) * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_opexfixedlev_378d_21d_slope_v147_signal(opex, revenue, closeadj):
    l = _f40_fixed_cost_leverage(opex, revenue, 378)
    base_ = l.clip(-100, 100) * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_opexfixedlev_504d_63d_slope_v148_signal(opex, revenue, closeadj):
    l = _f40_fixed_cost_leverage(opex, revenue, 504)
    base_ = l.clip(-100, 100) * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_gapz_21_252_126d_slope_v149_signal(sgna, revenue, closeadj):
    g = _f40_sgna_revenue_gap(sgna, revenue, 21)
    base_ = _z(g, 252) * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f40fcs_f40_fixed_cost_scaling_gapz_63_252_252d_slope_v150_signal(sgna, revenue, closeadj):
    g = _f40_sgna_revenue_gap(sgna, revenue, 63)
    base_ = _z(g, 252) * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f40fcs_f40_fixed_cost_scaling_sgnaintensity_5d_5d_slope_v001_signal,
    f40fcs_f40_fixed_cost_scaling_sgnaintensity_10d_21d_slope_v002_signal,
    f40fcs_f40_fixed_cost_scaling_sgnaintensity_21d_63d_slope_v003_signal,
    f40fcs_f40_fixed_cost_scaling_sgnaintensity_42d_126d_slope_v004_signal,
    f40fcs_f40_fixed_cost_scaling_sgnaintensity_63d_252d_slope_v005_signal,
    f40fcs_f40_fixed_cost_scaling_sgnaintensity_126d_5d_slope_v006_signal,
    f40fcs_f40_fixed_cost_scaling_sgnaintensity_189d_21d_slope_v007_signal,
    f40fcs_f40_fixed_cost_scaling_sgnaintensity_252d_63d_slope_v008_signal,
    f40fcs_f40_fixed_cost_scaling_sgnaintensity_378d_126d_slope_v009_signal,
    f40fcs_f40_fixed_cost_scaling_sgnaintensity_504d_252d_slope_v010_signal,
    f40fcs_f40_fixed_cost_scaling_sgnarevgap_5d_5d_slope_v011_signal,
    f40fcs_f40_fixed_cost_scaling_sgnarevgap_10d_21d_slope_v012_signal,
    f40fcs_f40_fixed_cost_scaling_sgnarevgap_21d_63d_slope_v013_signal,
    f40fcs_f40_fixed_cost_scaling_sgnarevgap_42d_126d_slope_v014_signal,
    f40fcs_f40_fixed_cost_scaling_sgnarevgap_63d_252d_slope_v015_signal,
    f40fcs_f40_fixed_cost_scaling_sgnarevgap_126d_5d_slope_v016_signal,
    f40fcs_f40_fixed_cost_scaling_sgnarevgap_189d_21d_slope_v017_signal,
    f40fcs_f40_fixed_cost_scaling_sgnarevgap_252d_63d_slope_v018_signal,
    f40fcs_f40_fixed_cost_scaling_sgnarevgap_378d_126d_slope_v019_signal,
    f40fcs_f40_fixed_cost_scaling_sgnarevgap_504d_252d_slope_v020_signal,
    f40fcs_f40_fixed_cost_scaling_fixedlev_5d_5d_slope_v021_signal,
    f40fcs_f40_fixed_cost_scaling_fixedlev_10d_21d_slope_v022_signal,
    f40fcs_f40_fixed_cost_scaling_fixedlev_21d_63d_slope_v023_signal,
    f40fcs_f40_fixed_cost_scaling_fixedlev_42d_126d_slope_v024_signal,
    f40fcs_f40_fixed_cost_scaling_fixedlev_63d_252d_slope_v025_signal,
    f40fcs_f40_fixed_cost_scaling_fixedlev_126d_5d_slope_v026_signal,
    f40fcs_f40_fixed_cost_scaling_fixedlev_189d_21d_slope_v027_signal,
    f40fcs_f40_fixed_cost_scaling_fixedlev_252d_63d_slope_v028_signal,
    f40fcs_f40_fixed_cost_scaling_fixedlev_378d_126d_slope_v029_signal,
    f40fcs_f40_fixed_cost_scaling_fixedlev_504d_252d_slope_v030_signal,
    f40fcs_f40_fixed_cost_scaling_sgnaintdiff_5d_5d_slope_v031_signal,
    f40fcs_f40_fixed_cost_scaling_sgnaintdiff_10d_21d_slope_v032_signal,
    f40fcs_f40_fixed_cost_scaling_sgnaintdiff_21d_63d_slope_v033_signal,
    f40fcs_f40_fixed_cost_scaling_sgnaintdiff_42d_126d_slope_v034_signal,
    f40fcs_f40_fixed_cost_scaling_sgnaintdiff_63d_252d_slope_v035_signal,
    f40fcs_f40_fixed_cost_scaling_sgnaintdiff_126d_5d_slope_v036_signal,
    f40fcs_f40_fixed_cost_scaling_sgnaintdiff_189d_21d_slope_v037_signal,
    f40fcs_f40_fixed_cost_scaling_sgnaintdiff_252d_63d_slope_v038_signal,
    f40fcs_f40_fixed_cost_scaling_sgnaintdiff_378d_126d_slope_v039_signal,
    f40fcs_f40_fixed_cost_scaling_sgnaintdiff_504d_252d_slope_v040_signal,
    f40fcs_f40_fixed_cost_scaling_sgnaintxopex_5d_5d_slope_v041_signal,
    f40fcs_f40_fixed_cost_scaling_sgnaintxopex_10d_21d_slope_v042_signal,
    f40fcs_f40_fixed_cost_scaling_sgnaintxopex_21d_63d_slope_v043_signal,
    f40fcs_f40_fixed_cost_scaling_sgnaintxopex_42d_126d_slope_v044_signal,
    f40fcs_f40_fixed_cost_scaling_sgnaintxopex_63d_252d_slope_v045_signal,
    f40fcs_f40_fixed_cost_scaling_sgnaintxopex_126d_5d_slope_v046_signal,
    f40fcs_f40_fixed_cost_scaling_sgnaintxopex_189d_21d_slope_v047_signal,
    f40fcs_f40_fixed_cost_scaling_sgnaintxopex_252d_63d_slope_v048_signal,
    f40fcs_f40_fixed_cost_scaling_sgnaintxopex_378d_126d_slope_v049_signal,
    f40fcs_f40_fixed_cost_scaling_sgnaintxopex_504d_252d_slope_v050_signal,
    f40fcs_f40_fixed_cost_scaling_gapxint_5d_5d_slope_v051_signal,
    f40fcs_f40_fixed_cost_scaling_gapxint_10d_21d_slope_v052_signal,
    f40fcs_f40_fixed_cost_scaling_gapxint_21d_63d_slope_v053_signal,
    f40fcs_f40_fixed_cost_scaling_gapxint_42d_126d_slope_v054_signal,
    f40fcs_f40_fixed_cost_scaling_gapxint_63d_252d_slope_v055_signal,
    f40fcs_f40_fixed_cost_scaling_gapxint_126d_5d_slope_v056_signal,
    f40fcs_f40_fixed_cost_scaling_gapxint_189d_21d_slope_v057_signal,
    f40fcs_f40_fixed_cost_scaling_gapxint_252d_63d_slope_v058_signal,
    f40fcs_f40_fixed_cost_scaling_gapxint_378d_126d_slope_v059_signal,
    f40fcs_f40_fixed_cost_scaling_gapxint_504d_252d_slope_v060_signal,
    f40fcs_f40_fixed_cost_scaling_fixedlevz_21_252_5d_slope_v061_signal,
    f40fcs_f40_fixed_cost_scaling_fixedlevz_63_252_21d_slope_v062_signal,
    f40fcs_f40_fixed_cost_scaling_fixedlevz_126_252_63d_slope_v063_signal,
    f40fcs_f40_fixed_cost_scaling_fixedlevz_21_504_126d_slope_v064_signal,
    f40fcs_f40_fixed_cost_scaling_fixedlevz_63_504_252d_slope_v065_signal,
    f40fcs_f40_fixed_cost_scaling_fixedlevz_126_504_5d_slope_v066_signal,
    f40fcs_f40_fixed_cost_scaling_gapsm_63d_21d_slope_v067_signal,
    f40fcs_f40_fixed_cost_scaling_gapsm_126d_63d_slope_v068_signal,
    f40fcs_f40_fixed_cost_scaling_gapsm_189d_126d_slope_v069_signal,
    f40fcs_f40_fixed_cost_scaling_gapsm_252d_252d_slope_v070_signal,
    f40fcs_f40_fixed_cost_scaling_gapsm_378d_5d_slope_v071_signal,
    f40fcs_f40_fixed_cost_scaling_gapsm_504d_21d_slope_v072_signal,
    f40fcs_f40_fixed_cost_scaling_intensityema_5d_63d_slope_v073_signal,
    f40fcs_f40_fixed_cost_scaling_intensityema_10d_126d_slope_v074_signal,
    f40fcs_f40_fixed_cost_scaling_intensityema_21d_252d_slope_v075_signal,
    f40fcs_f40_fixed_cost_scaling_intensityema_42d_5d_slope_v076_signal,
    f40fcs_f40_fixed_cost_scaling_intensityema_63d_21d_slope_v077_signal,
    f40fcs_f40_fixed_cost_scaling_intensityema_126d_63d_slope_v078_signal,
    f40fcs_f40_fixed_cost_scaling_intensityema_189d_126d_slope_v079_signal,
    f40fcs_f40_fixed_cost_scaling_intensityema_252d_252d_slope_v080_signal,
    f40fcs_f40_fixed_cost_scaling_intensityema_378d_5d_slope_v081_signal,
    f40fcs_f40_fixed_cost_scaling_intensityema_504d_21d_slope_v082_signal,
    f40fcs_f40_fixed_cost_scaling_intensitystd_63d_63d_slope_v083_signal,
    f40fcs_f40_fixed_cost_scaling_intensitystd_126d_126d_slope_v084_signal,
    f40fcs_f40_fixed_cost_scaling_intensitystd_189d_252d_slope_v085_signal,
    f40fcs_f40_fixed_cost_scaling_intensitystd_252d_5d_slope_v086_signal,
    f40fcs_f40_fixed_cost_scaling_intensitystd_378d_21d_slope_v087_signal,
    f40fcs_f40_fixed_cost_scaling_intensitystd_504d_63d_slope_v088_signal,
    f40fcs_f40_fixed_cost_scaling_gapxrevpct_5d_126d_slope_v089_signal,
    f40fcs_f40_fixed_cost_scaling_gapxrevpct_10d_252d_slope_v090_signal,
    f40fcs_f40_fixed_cost_scaling_gapxrevpct_21d_5d_slope_v091_signal,
    f40fcs_f40_fixed_cost_scaling_gapxrevpct_42d_21d_slope_v092_signal,
    f40fcs_f40_fixed_cost_scaling_gapxrevpct_63d_63d_slope_v093_signal,
    f40fcs_f40_fixed_cost_scaling_gapxrevpct_126d_126d_slope_v094_signal,
    f40fcs_f40_fixed_cost_scaling_gapxrevpct_189d_252d_slope_v095_signal,
    f40fcs_f40_fixed_cost_scaling_gapxrevpct_252d_5d_slope_v096_signal,
    f40fcs_f40_fixed_cost_scaling_gapxrevpct_378d_21d_slope_v097_signal,
    f40fcs_f40_fixed_cost_scaling_gapxrevpct_504d_63d_slope_v098_signal,
    f40fcs_f40_fixed_cost_scaling_fixedlevxopex_5d_126d_slope_v099_signal,
    f40fcs_f40_fixed_cost_scaling_fixedlevxopex_10d_252d_slope_v100_signal,
    f40fcs_f40_fixed_cost_scaling_fixedlevxopex_21d_5d_slope_v101_signal,
    f40fcs_f40_fixed_cost_scaling_fixedlevxopex_42d_21d_slope_v102_signal,
    f40fcs_f40_fixed_cost_scaling_fixedlevxopex_63d_63d_slope_v103_signal,
    f40fcs_f40_fixed_cost_scaling_fixedlevxopex_126d_126d_slope_v104_signal,
    f40fcs_f40_fixed_cost_scaling_fixedlevxopex_189d_252d_slope_v105_signal,
    f40fcs_f40_fixed_cost_scaling_fixedlevxopex_252d_5d_slope_v106_signal,
    f40fcs_f40_fixed_cost_scaling_fixedlevxopex_378d_21d_slope_v107_signal,
    f40fcs_f40_fixed_cost_scaling_fixedlevxopex_504d_63d_slope_v108_signal,
    f40fcs_f40_fixed_cost_scaling_opexrevgap_5d_126d_slope_v109_signal,
    f40fcs_f40_fixed_cost_scaling_opexrevgap_10d_252d_slope_v110_signal,
    f40fcs_f40_fixed_cost_scaling_opexrevgap_21d_5d_slope_v111_signal,
    f40fcs_f40_fixed_cost_scaling_opexrevgap_42d_21d_slope_v112_signal,
    f40fcs_f40_fixed_cost_scaling_opexrevgap_63d_63d_slope_v113_signal,
    f40fcs_f40_fixed_cost_scaling_opexrevgap_126d_126d_slope_v114_signal,
    f40fcs_f40_fixed_cost_scaling_opexrevgap_189d_252d_slope_v115_signal,
    f40fcs_f40_fixed_cost_scaling_opexrevgap_252d_5d_slope_v116_signal,
    f40fcs_f40_fixed_cost_scaling_opexrevgap_378d_21d_slope_v117_signal,
    f40fcs_f40_fixed_cost_scaling_opexrevgap_504d_63d_slope_v118_signal,
    f40fcs_f40_fixed_cost_scaling_intensitysq_5d_126d_slope_v119_signal,
    f40fcs_f40_fixed_cost_scaling_intensitysq_10d_252d_slope_v120_signal,
    f40fcs_f40_fixed_cost_scaling_intensitysq_21d_5d_slope_v121_signal,
    f40fcs_f40_fixed_cost_scaling_intensitysq_42d_21d_slope_v122_signal,
    f40fcs_f40_fixed_cost_scaling_intensitysq_63d_63d_slope_v123_signal,
    f40fcs_f40_fixed_cost_scaling_intensitysq_126d_126d_slope_v124_signal,
    f40fcs_f40_fixed_cost_scaling_intensitysq_189d_252d_slope_v125_signal,
    f40fcs_f40_fixed_cost_scaling_intensitysq_252d_5d_slope_v126_signal,
    f40fcs_f40_fixed_cost_scaling_intensitysq_378d_21d_slope_v127_signal,
    f40fcs_f40_fixed_cost_scaling_intensitysq_504d_63d_slope_v128_signal,
    f40fcs_f40_fixed_cost_scaling_fixedlevdiff_5d_126d_slope_v129_signal,
    f40fcs_f40_fixed_cost_scaling_fixedlevdiff_10d_252d_slope_v130_signal,
    f40fcs_f40_fixed_cost_scaling_fixedlevdiff_21d_5d_slope_v131_signal,
    f40fcs_f40_fixed_cost_scaling_fixedlevdiff_42d_21d_slope_v132_signal,
    f40fcs_f40_fixed_cost_scaling_fixedlevdiff_63d_63d_slope_v133_signal,
    f40fcs_f40_fixed_cost_scaling_fixedlevdiff_126d_126d_slope_v134_signal,
    f40fcs_f40_fixed_cost_scaling_fixedlevdiff_189d_252d_slope_v135_signal,
    f40fcs_f40_fixed_cost_scaling_fixedlevdiff_252d_5d_slope_v136_signal,
    f40fcs_f40_fixed_cost_scaling_fixedlevdiff_378d_21d_slope_v137_signal,
    f40fcs_f40_fixed_cost_scaling_fixedlevdiff_504d_63d_slope_v138_signal,
    f40fcs_f40_fixed_cost_scaling_opexfixedlev_5d_126d_slope_v139_signal,
    f40fcs_f40_fixed_cost_scaling_opexfixedlev_10d_252d_slope_v140_signal,
    f40fcs_f40_fixed_cost_scaling_opexfixedlev_21d_5d_slope_v141_signal,
    f40fcs_f40_fixed_cost_scaling_opexfixedlev_42d_21d_slope_v142_signal,
    f40fcs_f40_fixed_cost_scaling_opexfixedlev_63d_63d_slope_v143_signal,
    f40fcs_f40_fixed_cost_scaling_opexfixedlev_126d_126d_slope_v144_signal,
    f40fcs_f40_fixed_cost_scaling_opexfixedlev_189d_252d_slope_v145_signal,
    f40fcs_f40_fixed_cost_scaling_opexfixedlev_252d_5d_slope_v146_signal,
    f40fcs_f40_fixed_cost_scaling_opexfixedlev_378d_21d_slope_v147_signal,
    f40fcs_f40_fixed_cost_scaling_opexfixedlev_504d_63d_slope_v148_signal,
    f40fcs_f40_fixed_cost_scaling_gapz_21_252_126d_slope_v149_signal,
    f40fcs_f40_fixed_cost_scaling_gapz_63_252_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F40_FIXED_COST_SCALING_REGISTRY_SLOPE_001_150 = REGISTRY


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

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    assetsc      = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsc")
    assetsnc     = pd.Series(1.2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsnc")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    liabilitiesc = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesc")
    liabilitiesnc= pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesnc")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    equityusd    = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equityusd")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    debtc        = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtc")
    debtnc       = pd.Series(4.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtnc")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    intangibles  = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    tangibles    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="tangibles")
    invcap       = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")
    retearn      = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="retearn")
    sbcomp       = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="sbcomp")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    shareswadil  = pd.Series(1.02e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswadil")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    epsdil       = pd.Series(0.98 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="epsdil")
    bvps         = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="bvps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    sps          = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="sps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    pe           = pd.Series(closeadj / eps.replace(0, np.nan).abs(), name="pe")
    pb           = pd.Series(closeadj / bvps.replace(0, np.nan).abs(), name="pb")
    ps           = pd.Series(closeadj / sps.replace(0, np.nan).abs(), name="ps")
    evebit       = pd.Series(ev / ebit.replace(0, np.nan).abs(), name="evebit")
    evebitda     = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ros          = pd.Series(0.08 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ros")
    currentratio = pd.Series(1.5 + 0.3*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="currentratio")
    de           = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    divyield     = pd.Series(0.02 + 0.005*np.sin(np.arange(n)/250.0) + 0.001*np.random.randn(n), name="divyield")
    assetturnover= pd.Series(0.7 + 0.15*np.sin(np.arange(n)/250.0) + 0.02*np.random.randn(n), name="assetturnover")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "assets": assets, "assetsc": assetsc, "assetsnc": assetsnc,
        "liabilities": liabilities, "liabilitiesc": liabilitiesc, "liabilitiesnc": liabilitiesnc,
        "equity": equity, "equityusd": equityusd,
        "debt": debt, "debtc": debtc, "debtnc": debtnc, "cashneq": cashneq,
        "inventory": inventory, "receivables": receivables, "payables": payables,
        "deferredrev": deferredrev, "workingcapital": workingcapital,
        "ppnenet": ppnenet, "intangibles": intangibles, "tangibles": tangibles,
        "invcap": invcap, "retearn": retearn, "sbcomp": sbcomp,
        "sharesbas": sharesbas, "shareswa": shareswa, "shareswadil": shareswadil,
        "eps": eps, "epsdil": epsdil, "bvps": bvps, "fcfps": fcfps, "sps": sps, "dps": dps,
        "marketcap": marketcap, "ev": ev,
        "pe": pe, "pb": pb, "ps": ps, "evebit": evebit, "evebitda": evebitda,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
        "roa": roa, "roe": roe, "roic": roic, "ros": ros,
        "currentratio": currentratio, "de": de,
        "payoutratio": payoutratio, "divyield": divyield, "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f40_sgna_intensity", "_f40_sgna_revenue_gap", "_f40_fixed_cost_leverage")
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
    print(f"OK f40_fixed_cost_scaling_2nd_derivatives_001_150_claude: {n_features} features pass")
