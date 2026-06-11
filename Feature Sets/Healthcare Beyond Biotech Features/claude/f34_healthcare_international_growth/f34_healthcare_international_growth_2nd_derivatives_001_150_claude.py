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


def _ema(s, w):
    return s.ewm(span=w, adjust=False).mean()


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)

# ===== folder domain primitives =====
def _f34_revenue_compound(revenue, w):
    return np.log(revenue.replace(0, np.nan).abs()).diff(w)


def _f34_multi_horizon_growth(revenue, w):
    g_short = revenue.pct_change(w)
    g_long = revenue.pct_change(w * 2)
    return _mean(g_short, w) + _mean(g_long, w) * 0.5


def _f34_international_proxy(revenue, ebitdamargin, w):
    rg = revenue.pct_change(w)
    return _mean(rg * (1.0 + ebitdamargin), w)

def f34hig_f34_healthcare_international_growth_compound_5d_mean_5d_xc_slope_v001_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 5)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_5d_mean_21d_xmc_slope_v002_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 5)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_5d_std_5d_xc_slope_v003_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 5)
    sm   = (_std(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_5d_std_21d_xmc_slope_v004_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 5)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_5d_ema_5d_xc_slope_v005_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 5)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_5d_ema_21d_xmc_slope_v006_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 5)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_5d_z_5d_xc_slope_v007_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 5)
    sm   = (_z(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_5d_z_21d_xmc_slope_v008_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 5)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_5d_log_5d_xc_slope_v009_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 5)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_5d_log_21d_xmc_slope_v010_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 5)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_10d_mean_5d_xc_slope_v011_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 10)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_10d_mean_21d_xmc_slope_v012_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 10)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_10d_std_5d_xc_slope_v013_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 10)
    sm   = (_std(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_10d_std_21d_xmc_slope_v014_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 10)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_10d_ema_5d_xc_slope_v015_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 10)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_10d_ema_21d_xmc_slope_v016_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 10)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_10d_z_5d_xc_slope_v017_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 10)
    sm   = (_z(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_10d_z_21d_xmc_slope_v018_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 10)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_10d_log_5d_xc_slope_v019_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 10)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_10d_log_21d_xmc_slope_v020_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 10)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_21d_mean_5d_xc_slope_v021_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 21)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_21d_mean_21d_xmc_slope_v022_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 21)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_21d_std_5d_xc_slope_v023_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 21)
    sm   = (_std(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_21d_std_21d_xmc_slope_v024_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 21)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_21d_ema_5d_xc_slope_v025_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 21)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_21d_ema_21d_xmc_slope_v026_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 21)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_21d_z_5d_xc_slope_v027_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 21)
    sm   = (_z(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_21d_z_21d_xmc_slope_v028_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 21)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_21d_log_5d_xc_slope_v029_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 21)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_21d_log_21d_xmc_slope_v030_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 21)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_42d_mean_5d_xc_slope_v031_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 42)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_42d_mean_21d_xmc_slope_v032_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 42)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_42d_std_5d_xc_slope_v033_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 42)
    sm   = (_std(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_42d_std_21d_xmc_slope_v034_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 42)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_42d_ema_5d_xc_slope_v035_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 42)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_42d_ema_21d_xmc_slope_v036_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 42)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_42d_z_5d_xc_slope_v037_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 42)
    sm   = (_z(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_42d_z_21d_xmc_slope_v038_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 42)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_42d_log_5d_xc_slope_v039_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 42)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_42d_log_21d_xmc_slope_v040_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 42)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_63d_mean_5d_xc_slope_v041_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 63)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_63d_mean_21d_xmc_slope_v042_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 63)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_63d_std_5d_xc_slope_v043_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 63)
    sm   = (_std(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_63d_std_21d_xmc_slope_v044_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 63)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_63d_ema_5d_xc_slope_v045_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 63)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_63d_ema_21d_xmc_slope_v046_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 63)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_63d_z_5d_xc_slope_v047_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 63)
    sm   = (_z(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_63d_z_21d_xmc_slope_v048_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 63)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_63d_log_5d_xc_slope_v049_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 63)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_63d_log_21d_xmc_slope_v050_signal(revenue, ebitdamargin, closeadj):
    base = _f34_revenue_compound(revenue, 63)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_5d_mean_5d_xc_slope_v051_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 5)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_5d_mean_21d_xmc_slope_v052_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 5)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_5d_std_5d_xc_slope_v053_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 5)
    sm   = (_std(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_5d_std_21d_xmc_slope_v054_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 5)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_5d_ema_5d_xc_slope_v055_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 5)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_5d_ema_21d_xmc_slope_v056_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 5)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_5d_z_5d_xc_slope_v057_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 5)
    sm   = (_z(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_5d_z_21d_xmc_slope_v058_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 5)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_5d_log_5d_xc_slope_v059_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 5)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_5d_log_21d_xmc_slope_v060_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 5)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_10d_mean_5d_xc_slope_v061_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 10)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_10d_mean_21d_xmc_slope_v062_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 10)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_10d_std_5d_xc_slope_v063_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 10)
    sm   = (_std(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_10d_std_21d_xmc_slope_v064_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 10)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_10d_ema_5d_xc_slope_v065_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 10)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_10d_ema_21d_xmc_slope_v066_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 10)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_10d_z_5d_xc_slope_v067_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 10)
    sm   = (_z(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_10d_z_21d_xmc_slope_v068_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 10)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_10d_log_5d_xc_slope_v069_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 10)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_10d_log_21d_xmc_slope_v070_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 10)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_21d_mean_5d_xc_slope_v071_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 21)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_21d_mean_21d_xmc_slope_v072_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 21)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_21d_std_5d_xc_slope_v073_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 21)
    sm   = (_std(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_21d_std_21d_xmc_slope_v074_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 21)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_21d_ema_5d_xc_slope_v075_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 21)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_21d_ema_21d_xmc_slope_v076_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 21)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_21d_z_5d_xc_slope_v077_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 21)
    sm   = (_z(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_21d_z_21d_xmc_slope_v078_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 21)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_21d_log_5d_xc_slope_v079_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 21)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_21d_log_21d_xmc_slope_v080_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 21)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_42d_mean_5d_xc_slope_v081_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 42)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_42d_mean_21d_xmc_slope_v082_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 42)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_42d_std_5d_xc_slope_v083_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 42)
    sm   = (_std(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_42d_std_21d_xmc_slope_v084_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 42)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_42d_ema_5d_xc_slope_v085_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 42)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_42d_ema_21d_xmc_slope_v086_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 42)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_42d_z_5d_xc_slope_v087_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 42)
    sm   = (_z(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_42d_z_21d_xmc_slope_v088_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 42)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_42d_log_5d_xc_slope_v089_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 42)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_42d_log_21d_xmc_slope_v090_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 42)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_63d_mean_5d_xc_slope_v091_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 63)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_63d_mean_21d_xmc_slope_v092_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 63)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_63d_std_5d_xc_slope_v093_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 63)
    sm   = (_std(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_63d_std_21d_xmc_slope_v094_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 63)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_63d_ema_5d_xc_slope_v095_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 63)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_63d_ema_21d_xmc_slope_v096_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 63)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_63d_z_5d_xc_slope_v097_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 63)
    sm   = (_z(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_63d_z_21d_xmc_slope_v098_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 63)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_63d_log_5d_xc_slope_v099_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 63)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multih_63d_log_21d_xmc_slope_v100_signal(revenue, ebitdamargin, closeadj):
    base = _f34_multi_horizon_growth(revenue, 63)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_5d_mean_5d_xc_slope_v101_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 5)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_5d_mean_21d_xmc_slope_v102_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 5)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_5d_std_5d_xc_slope_v103_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 5)
    sm   = (_std(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_5d_std_21d_xmc_slope_v104_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 5)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_5d_ema_5d_xc_slope_v105_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 5)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_5d_ema_21d_xmc_slope_v106_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 5)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_5d_z_5d_xc_slope_v107_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 5)
    sm   = (_z(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_5d_z_21d_xmc_slope_v108_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 5)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_5d_log_5d_xc_slope_v109_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 5)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_5d_log_21d_xmc_slope_v110_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 5)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_10d_mean_5d_xc_slope_v111_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 10)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_10d_mean_21d_xmc_slope_v112_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 10)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_10d_std_5d_xc_slope_v113_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 10)
    sm   = (_std(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_10d_std_21d_xmc_slope_v114_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 10)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_10d_ema_5d_xc_slope_v115_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 10)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_10d_ema_21d_xmc_slope_v116_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 10)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_10d_z_5d_xc_slope_v117_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 10)
    sm   = (_z(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_10d_z_21d_xmc_slope_v118_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 10)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_10d_log_5d_xc_slope_v119_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 10)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_10d_log_21d_xmc_slope_v120_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 10)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_21d_mean_5d_xc_slope_v121_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 21)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_21d_mean_21d_xmc_slope_v122_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 21)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_21d_std_5d_xc_slope_v123_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 21)
    sm   = (_std(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_21d_std_21d_xmc_slope_v124_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 21)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_21d_ema_5d_xc_slope_v125_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 21)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_21d_ema_21d_xmc_slope_v126_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 21)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_21d_z_5d_xc_slope_v127_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 21)
    sm   = (_z(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_21d_z_21d_xmc_slope_v128_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 21)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_21d_log_5d_xc_slope_v129_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 21)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_21d_log_21d_xmc_slope_v130_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 21)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_42d_mean_5d_xc_slope_v131_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 42)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_42d_mean_21d_xmc_slope_v132_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 42)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_42d_std_5d_xc_slope_v133_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 42)
    sm   = (_std(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_42d_std_21d_xmc_slope_v134_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 42)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_42d_ema_5d_xc_slope_v135_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 42)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_42d_ema_21d_xmc_slope_v136_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 42)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_42d_z_5d_xc_slope_v137_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 42)
    sm   = (_z(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_42d_z_21d_xmc_slope_v138_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 42)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_42d_log_5d_xc_slope_v139_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 42)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_42d_log_21d_xmc_slope_v140_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 42)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_63d_mean_5d_xc_slope_v141_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 63)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_63d_mean_21d_xmc_slope_v142_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 63)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_63d_std_5d_xc_slope_v143_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 63)
    sm   = (_std(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_63d_std_21d_xmc_slope_v144_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 63)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_63d_ema_5d_xc_slope_v145_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 63)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_63d_ema_21d_xmc_slope_v146_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 63)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_63d_z_5d_xc_slope_v147_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 63)
    sm   = (_z(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_63d_z_21d_xmc_slope_v148_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 63)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_63d_log_5d_xc_slope_v149_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 63)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlproxy_63d_log_21d_xmc_slope_v150_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 63)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f34hig_f34_healthcare_international_growth_compound_5d_mean_5d_xc_slope_v001_signal,
    f34hig_f34_healthcare_international_growth_compound_5d_mean_21d_xmc_slope_v002_signal,
    f34hig_f34_healthcare_international_growth_compound_5d_std_5d_xc_slope_v003_signal,
    f34hig_f34_healthcare_international_growth_compound_5d_std_21d_xmc_slope_v004_signal,
    f34hig_f34_healthcare_international_growth_compound_5d_ema_5d_xc_slope_v005_signal,
    f34hig_f34_healthcare_international_growth_compound_5d_ema_21d_xmc_slope_v006_signal,
    f34hig_f34_healthcare_international_growth_compound_5d_z_5d_xc_slope_v007_signal,
    f34hig_f34_healthcare_international_growth_compound_5d_z_21d_xmc_slope_v008_signal,
    f34hig_f34_healthcare_international_growth_compound_5d_log_5d_xc_slope_v009_signal,
    f34hig_f34_healthcare_international_growth_compound_5d_log_21d_xmc_slope_v010_signal,
    f34hig_f34_healthcare_international_growth_compound_10d_mean_5d_xc_slope_v011_signal,
    f34hig_f34_healthcare_international_growth_compound_10d_mean_21d_xmc_slope_v012_signal,
    f34hig_f34_healthcare_international_growth_compound_10d_std_5d_xc_slope_v013_signal,
    f34hig_f34_healthcare_international_growth_compound_10d_std_21d_xmc_slope_v014_signal,
    f34hig_f34_healthcare_international_growth_compound_10d_ema_5d_xc_slope_v015_signal,
    f34hig_f34_healthcare_international_growth_compound_10d_ema_21d_xmc_slope_v016_signal,
    f34hig_f34_healthcare_international_growth_compound_10d_z_5d_xc_slope_v017_signal,
    f34hig_f34_healthcare_international_growth_compound_10d_z_21d_xmc_slope_v018_signal,
    f34hig_f34_healthcare_international_growth_compound_10d_log_5d_xc_slope_v019_signal,
    f34hig_f34_healthcare_international_growth_compound_10d_log_21d_xmc_slope_v020_signal,
    f34hig_f34_healthcare_international_growth_compound_21d_mean_5d_xc_slope_v021_signal,
    f34hig_f34_healthcare_international_growth_compound_21d_mean_21d_xmc_slope_v022_signal,
    f34hig_f34_healthcare_international_growth_compound_21d_std_5d_xc_slope_v023_signal,
    f34hig_f34_healthcare_international_growth_compound_21d_std_21d_xmc_slope_v024_signal,
    f34hig_f34_healthcare_international_growth_compound_21d_ema_5d_xc_slope_v025_signal,
    f34hig_f34_healthcare_international_growth_compound_21d_ema_21d_xmc_slope_v026_signal,
    f34hig_f34_healthcare_international_growth_compound_21d_z_5d_xc_slope_v027_signal,
    f34hig_f34_healthcare_international_growth_compound_21d_z_21d_xmc_slope_v028_signal,
    f34hig_f34_healthcare_international_growth_compound_21d_log_5d_xc_slope_v029_signal,
    f34hig_f34_healthcare_international_growth_compound_21d_log_21d_xmc_slope_v030_signal,
    f34hig_f34_healthcare_international_growth_compound_42d_mean_5d_xc_slope_v031_signal,
    f34hig_f34_healthcare_international_growth_compound_42d_mean_21d_xmc_slope_v032_signal,
    f34hig_f34_healthcare_international_growth_compound_42d_std_5d_xc_slope_v033_signal,
    f34hig_f34_healthcare_international_growth_compound_42d_std_21d_xmc_slope_v034_signal,
    f34hig_f34_healthcare_international_growth_compound_42d_ema_5d_xc_slope_v035_signal,
    f34hig_f34_healthcare_international_growth_compound_42d_ema_21d_xmc_slope_v036_signal,
    f34hig_f34_healthcare_international_growth_compound_42d_z_5d_xc_slope_v037_signal,
    f34hig_f34_healthcare_international_growth_compound_42d_z_21d_xmc_slope_v038_signal,
    f34hig_f34_healthcare_international_growth_compound_42d_log_5d_xc_slope_v039_signal,
    f34hig_f34_healthcare_international_growth_compound_42d_log_21d_xmc_slope_v040_signal,
    f34hig_f34_healthcare_international_growth_compound_63d_mean_5d_xc_slope_v041_signal,
    f34hig_f34_healthcare_international_growth_compound_63d_mean_21d_xmc_slope_v042_signal,
    f34hig_f34_healthcare_international_growth_compound_63d_std_5d_xc_slope_v043_signal,
    f34hig_f34_healthcare_international_growth_compound_63d_std_21d_xmc_slope_v044_signal,
    f34hig_f34_healthcare_international_growth_compound_63d_ema_5d_xc_slope_v045_signal,
    f34hig_f34_healthcare_international_growth_compound_63d_ema_21d_xmc_slope_v046_signal,
    f34hig_f34_healthcare_international_growth_compound_63d_z_5d_xc_slope_v047_signal,
    f34hig_f34_healthcare_international_growth_compound_63d_z_21d_xmc_slope_v048_signal,
    f34hig_f34_healthcare_international_growth_compound_63d_log_5d_xc_slope_v049_signal,
    f34hig_f34_healthcare_international_growth_compound_63d_log_21d_xmc_slope_v050_signal,
    f34hig_f34_healthcare_international_growth_multih_5d_mean_5d_xc_slope_v051_signal,
    f34hig_f34_healthcare_international_growth_multih_5d_mean_21d_xmc_slope_v052_signal,
    f34hig_f34_healthcare_international_growth_multih_5d_std_5d_xc_slope_v053_signal,
    f34hig_f34_healthcare_international_growth_multih_5d_std_21d_xmc_slope_v054_signal,
    f34hig_f34_healthcare_international_growth_multih_5d_ema_5d_xc_slope_v055_signal,
    f34hig_f34_healthcare_international_growth_multih_5d_ema_21d_xmc_slope_v056_signal,
    f34hig_f34_healthcare_international_growth_multih_5d_z_5d_xc_slope_v057_signal,
    f34hig_f34_healthcare_international_growth_multih_5d_z_21d_xmc_slope_v058_signal,
    f34hig_f34_healthcare_international_growth_multih_5d_log_5d_xc_slope_v059_signal,
    f34hig_f34_healthcare_international_growth_multih_5d_log_21d_xmc_slope_v060_signal,
    f34hig_f34_healthcare_international_growth_multih_10d_mean_5d_xc_slope_v061_signal,
    f34hig_f34_healthcare_international_growth_multih_10d_mean_21d_xmc_slope_v062_signal,
    f34hig_f34_healthcare_international_growth_multih_10d_std_5d_xc_slope_v063_signal,
    f34hig_f34_healthcare_international_growth_multih_10d_std_21d_xmc_slope_v064_signal,
    f34hig_f34_healthcare_international_growth_multih_10d_ema_5d_xc_slope_v065_signal,
    f34hig_f34_healthcare_international_growth_multih_10d_ema_21d_xmc_slope_v066_signal,
    f34hig_f34_healthcare_international_growth_multih_10d_z_5d_xc_slope_v067_signal,
    f34hig_f34_healthcare_international_growth_multih_10d_z_21d_xmc_slope_v068_signal,
    f34hig_f34_healthcare_international_growth_multih_10d_log_5d_xc_slope_v069_signal,
    f34hig_f34_healthcare_international_growth_multih_10d_log_21d_xmc_slope_v070_signal,
    f34hig_f34_healthcare_international_growth_multih_21d_mean_5d_xc_slope_v071_signal,
    f34hig_f34_healthcare_international_growth_multih_21d_mean_21d_xmc_slope_v072_signal,
    f34hig_f34_healthcare_international_growth_multih_21d_std_5d_xc_slope_v073_signal,
    f34hig_f34_healthcare_international_growth_multih_21d_std_21d_xmc_slope_v074_signal,
    f34hig_f34_healthcare_international_growth_multih_21d_ema_5d_xc_slope_v075_signal,
    f34hig_f34_healthcare_international_growth_multih_21d_ema_21d_xmc_slope_v076_signal,
    f34hig_f34_healthcare_international_growth_multih_21d_z_5d_xc_slope_v077_signal,
    f34hig_f34_healthcare_international_growth_multih_21d_z_21d_xmc_slope_v078_signal,
    f34hig_f34_healthcare_international_growth_multih_21d_log_5d_xc_slope_v079_signal,
    f34hig_f34_healthcare_international_growth_multih_21d_log_21d_xmc_slope_v080_signal,
    f34hig_f34_healthcare_international_growth_multih_42d_mean_5d_xc_slope_v081_signal,
    f34hig_f34_healthcare_international_growth_multih_42d_mean_21d_xmc_slope_v082_signal,
    f34hig_f34_healthcare_international_growth_multih_42d_std_5d_xc_slope_v083_signal,
    f34hig_f34_healthcare_international_growth_multih_42d_std_21d_xmc_slope_v084_signal,
    f34hig_f34_healthcare_international_growth_multih_42d_ema_5d_xc_slope_v085_signal,
    f34hig_f34_healthcare_international_growth_multih_42d_ema_21d_xmc_slope_v086_signal,
    f34hig_f34_healthcare_international_growth_multih_42d_z_5d_xc_slope_v087_signal,
    f34hig_f34_healthcare_international_growth_multih_42d_z_21d_xmc_slope_v088_signal,
    f34hig_f34_healthcare_international_growth_multih_42d_log_5d_xc_slope_v089_signal,
    f34hig_f34_healthcare_international_growth_multih_42d_log_21d_xmc_slope_v090_signal,
    f34hig_f34_healthcare_international_growth_multih_63d_mean_5d_xc_slope_v091_signal,
    f34hig_f34_healthcare_international_growth_multih_63d_mean_21d_xmc_slope_v092_signal,
    f34hig_f34_healthcare_international_growth_multih_63d_std_5d_xc_slope_v093_signal,
    f34hig_f34_healthcare_international_growth_multih_63d_std_21d_xmc_slope_v094_signal,
    f34hig_f34_healthcare_international_growth_multih_63d_ema_5d_xc_slope_v095_signal,
    f34hig_f34_healthcare_international_growth_multih_63d_ema_21d_xmc_slope_v096_signal,
    f34hig_f34_healthcare_international_growth_multih_63d_z_5d_xc_slope_v097_signal,
    f34hig_f34_healthcare_international_growth_multih_63d_z_21d_xmc_slope_v098_signal,
    f34hig_f34_healthcare_international_growth_multih_63d_log_5d_xc_slope_v099_signal,
    f34hig_f34_healthcare_international_growth_multih_63d_log_21d_xmc_slope_v100_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_5d_mean_5d_xc_slope_v101_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_5d_mean_21d_xmc_slope_v102_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_5d_std_5d_xc_slope_v103_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_5d_std_21d_xmc_slope_v104_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_5d_ema_5d_xc_slope_v105_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_5d_ema_21d_xmc_slope_v106_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_5d_z_5d_xc_slope_v107_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_5d_z_21d_xmc_slope_v108_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_5d_log_5d_xc_slope_v109_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_5d_log_21d_xmc_slope_v110_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_10d_mean_5d_xc_slope_v111_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_10d_mean_21d_xmc_slope_v112_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_10d_std_5d_xc_slope_v113_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_10d_std_21d_xmc_slope_v114_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_10d_ema_5d_xc_slope_v115_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_10d_ema_21d_xmc_slope_v116_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_10d_z_5d_xc_slope_v117_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_10d_z_21d_xmc_slope_v118_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_10d_log_5d_xc_slope_v119_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_10d_log_21d_xmc_slope_v120_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_21d_mean_5d_xc_slope_v121_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_21d_mean_21d_xmc_slope_v122_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_21d_std_5d_xc_slope_v123_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_21d_std_21d_xmc_slope_v124_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_21d_ema_5d_xc_slope_v125_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_21d_ema_21d_xmc_slope_v126_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_21d_z_5d_xc_slope_v127_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_21d_z_21d_xmc_slope_v128_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_21d_log_5d_xc_slope_v129_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_21d_log_21d_xmc_slope_v130_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_42d_mean_5d_xc_slope_v131_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_42d_mean_21d_xmc_slope_v132_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_42d_std_5d_xc_slope_v133_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_42d_std_21d_xmc_slope_v134_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_42d_ema_5d_xc_slope_v135_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_42d_ema_21d_xmc_slope_v136_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_42d_z_5d_xc_slope_v137_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_42d_z_21d_xmc_slope_v138_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_42d_log_5d_xc_slope_v139_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_42d_log_21d_xmc_slope_v140_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_63d_mean_5d_xc_slope_v141_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_63d_mean_21d_xmc_slope_v142_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_63d_std_5d_xc_slope_v143_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_63d_std_21d_xmc_slope_v144_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_63d_ema_5d_xc_slope_v145_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_63d_ema_21d_xmc_slope_v146_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_63d_z_5d_xc_slope_v147_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_63d_z_21d_xmc_slope_v148_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_63d_log_5d_xc_slope_v149_signal,
    f34hig_f34_healthcare_international_growth_intlproxy_63d_log_21d_xmc_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F34_HEALTHCARE_INTERNATIONAL_GROWTH_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitdamargin = pd.Series(0.15 + 0.05 * np.cumsum(np.random.normal(0, 0.002, n)), name="ebitdamargin")
    cols = {"closeadj": closeadj, "revenue": revenue, "ebitdamargin": ebitdamargin}

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f34_revenue_compound', '_f34_multi_horizon_growth', '_f34_international_proxy')
    import hashlib
    body_hashes = set()
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
        body = "\n".join(l.strip() for l in src.splitlines()
                          if l.strip() and not l.strip().startswith("#")
                          and not l.strip().startswith("def "))
        h = hashlib.sha1(body.encode()).hexdigest()
        assert h not in body_hashes, f"DUP body: {name}"
        body_hashes.add(h)
        n_features += 1
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f34_healthcare_international_growth_2nd_derivatives_001_150_claude: {n_features} features pass")
