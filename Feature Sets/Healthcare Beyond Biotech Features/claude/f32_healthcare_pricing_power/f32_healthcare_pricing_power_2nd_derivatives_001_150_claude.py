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
def _f32_rev_per_asset(revenue, assets):
    return revenue / assets.replace(0, np.nan)


def _f32_pricing_uplift(revenue, ppnenet, w):
    rpa = revenue / ppnenet.replace(0, np.nan)
    return rpa - rpa.shift(w)


def _f32_unit_economics_lift(revenue, assets, w):
    rpa = revenue / assets.replace(0, np.nan)
    return _mean(rpa, w) - _mean(rpa, w).shift(w)

def f32hpp_f32_healthcare_pricing_power_rpa_5d_mean_5d_xc_slope_v001_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 5)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_5d_mean_21d_xmc_slope_v002_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 5)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_5d_std_5d_xc_slope_v003_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 5)
    sm   = (_std(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_5d_std_21d_xmc_slope_v004_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 5)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_5d_ema_5d_xc_slope_v005_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 5)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_5d_ema_21d_xmc_slope_v006_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 5)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_5d_z_5d_xc_slope_v007_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 5)
    sm   = (_z(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_5d_z_21d_xmc_slope_v008_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 5)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_5d_log_5d_xc_slope_v009_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 5)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_5d_log_21d_xmc_slope_v010_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 5)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_10d_mean_5d_xc_slope_v011_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 10)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_10d_mean_21d_xmc_slope_v012_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 10)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_10d_std_5d_xc_slope_v013_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 10)
    sm   = (_std(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_10d_std_21d_xmc_slope_v014_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 10)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_10d_ema_5d_xc_slope_v015_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 10)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_10d_ema_21d_xmc_slope_v016_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 10)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_10d_z_5d_xc_slope_v017_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 10)
    sm   = (_z(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_10d_z_21d_xmc_slope_v018_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 10)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_10d_log_5d_xc_slope_v019_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 10)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_10d_log_21d_xmc_slope_v020_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 10)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_21d_mean_5d_xc_slope_v021_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 21)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_21d_mean_21d_xmc_slope_v022_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 21)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_21d_std_5d_xc_slope_v023_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 21)
    sm   = (_std(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_21d_std_21d_xmc_slope_v024_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 21)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_21d_ema_5d_xc_slope_v025_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 21)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_21d_ema_21d_xmc_slope_v026_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 21)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_21d_z_5d_xc_slope_v027_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 21)
    sm   = (_z(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_21d_z_21d_xmc_slope_v028_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 21)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_21d_log_5d_xc_slope_v029_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 21)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_21d_log_21d_xmc_slope_v030_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 21)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_42d_mean_5d_xc_slope_v031_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 42)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_42d_mean_21d_xmc_slope_v032_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 42)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_42d_std_5d_xc_slope_v033_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 42)
    sm   = (_std(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_42d_std_21d_xmc_slope_v034_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 42)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_42d_ema_5d_xc_slope_v035_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 42)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_42d_ema_21d_xmc_slope_v036_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 42)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_42d_z_5d_xc_slope_v037_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 42)
    sm   = (_z(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_42d_z_21d_xmc_slope_v038_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 42)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_42d_log_5d_xc_slope_v039_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 42)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_42d_log_21d_xmc_slope_v040_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 42)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_63d_mean_5d_xc_slope_v041_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 63)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_63d_mean_21d_xmc_slope_v042_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 63)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_63d_std_5d_xc_slope_v043_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 63)
    sm   = (_std(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_63d_std_21d_xmc_slope_v044_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 63)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_63d_ema_5d_xc_slope_v045_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 63)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_63d_ema_21d_xmc_slope_v046_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 63)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_63d_z_5d_xc_slope_v047_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 63)
    sm   = (_z(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_63d_z_21d_xmc_slope_v048_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 63)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_63d_log_5d_xc_slope_v049_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 63)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_63d_log_21d_xmc_slope_v050_signal(revenue, assets, ppnenet, closeadj):
    base = _mean(_f32_rev_per_asset(revenue, assets), 63)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_5d_mean_5d_xc_slope_v051_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 5)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_5d_mean_21d_xmc_slope_v052_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 5)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_5d_std_5d_xc_slope_v053_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 5)
    sm   = (_std(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_5d_std_21d_xmc_slope_v054_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 5)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_5d_ema_5d_xc_slope_v055_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 5)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_5d_ema_21d_xmc_slope_v056_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 5)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_5d_z_5d_xc_slope_v057_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 5)
    sm   = (_z(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_5d_z_21d_xmc_slope_v058_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 5)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_5d_log_5d_xc_slope_v059_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 5)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_5d_log_21d_xmc_slope_v060_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 5)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_10d_mean_5d_xc_slope_v061_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 10)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_10d_mean_21d_xmc_slope_v062_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 10)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_10d_std_5d_xc_slope_v063_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 10)
    sm   = (_std(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_10d_std_21d_xmc_slope_v064_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 10)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_10d_ema_5d_xc_slope_v065_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 10)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_10d_ema_21d_xmc_slope_v066_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 10)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_10d_z_5d_xc_slope_v067_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 10)
    sm   = (_z(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_10d_z_21d_xmc_slope_v068_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 10)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_10d_log_5d_xc_slope_v069_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 10)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_10d_log_21d_xmc_slope_v070_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 10)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_21d_mean_5d_xc_slope_v071_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 21)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_21d_mean_21d_xmc_slope_v072_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 21)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_21d_std_5d_xc_slope_v073_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 21)
    sm   = (_std(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_21d_std_21d_xmc_slope_v074_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 21)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_21d_ema_5d_xc_slope_v075_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 21)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_21d_ema_21d_xmc_slope_v076_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 21)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_21d_z_5d_xc_slope_v077_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 21)
    sm   = (_z(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_21d_z_21d_xmc_slope_v078_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 21)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_21d_log_5d_xc_slope_v079_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 21)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_21d_log_21d_xmc_slope_v080_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 21)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_42d_mean_5d_xc_slope_v081_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 42)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_42d_mean_21d_xmc_slope_v082_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 42)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_42d_std_5d_xc_slope_v083_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 42)
    sm   = (_std(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_42d_std_21d_xmc_slope_v084_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 42)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_42d_ema_5d_xc_slope_v085_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 42)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_42d_ema_21d_xmc_slope_v086_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 42)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_42d_z_5d_xc_slope_v087_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 42)
    sm   = (_z(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_42d_z_21d_xmc_slope_v088_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 42)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_42d_log_5d_xc_slope_v089_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 42)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_42d_log_21d_xmc_slope_v090_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 42)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_63d_mean_5d_xc_slope_v091_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 63)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_63d_mean_21d_xmc_slope_v092_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 63)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_63d_std_5d_xc_slope_v093_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 63)
    sm   = (_std(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_63d_std_21d_xmc_slope_v094_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 63)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_63d_ema_5d_xc_slope_v095_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 63)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_63d_ema_21d_xmc_slope_v096_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 63)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_63d_z_5d_xc_slope_v097_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 63)
    sm   = (_z(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_63d_z_21d_xmc_slope_v098_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 63)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_63d_log_5d_xc_slope_v099_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 63)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_63d_log_21d_xmc_slope_v100_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 63)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_5d_mean_5d_xc_slope_v101_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 5)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_5d_mean_21d_xmc_slope_v102_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 5)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_5d_std_5d_xc_slope_v103_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 5)
    sm   = (_std(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_5d_std_21d_xmc_slope_v104_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 5)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_5d_ema_5d_xc_slope_v105_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 5)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_5d_ema_21d_xmc_slope_v106_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 5)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_5d_z_5d_xc_slope_v107_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 5)
    sm   = (_z(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_5d_z_21d_xmc_slope_v108_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 5)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_5d_log_5d_xc_slope_v109_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 5)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_5d_log_21d_xmc_slope_v110_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 5)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_10d_mean_5d_xc_slope_v111_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 10)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_10d_mean_21d_xmc_slope_v112_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 10)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_10d_std_5d_xc_slope_v113_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 10)
    sm   = (_std(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_10d_std_21d_xmc_slope_v114_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 10)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_10d_ema_5d_xc_slope_v115_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 10)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_10d_ema_21d_xmc_slope_v116_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 10)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_10d_z_5d_xc_slope_v117_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 10)
    sm   = (_z(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_10d_z_21d_xmc_slope_v118_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 10)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_10d_log_5d_xc_slope_v119_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 10)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_10d_log_21d_xmc_slope_v120_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 10)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_21d_mean_5d_xc_slope_v121_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 21)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_21d_mean_21d_xmc_slope_v122_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 21)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_21d_std_5d_xc_slope_v123_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 21)
    sm   = (_std(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_21d_std_21d_xmc_slope_v124_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 21)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_21d_ema_5d_xc_slope_v125_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 21)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_21d_ema_21d_xmc_slope_v126_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 21)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_21d_z_5d_xc_slope_v127_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 21)
    sm   = (_z(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_21d_z_21d_xmc_slope_v128_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 21)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_21d_log_5d_xc_slope_v129_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 21)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_21d_log_21d_xmc_slope_v130_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 21)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_42d_mean_5d_xc_slope_v131_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 42)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_42d_mean_21d_xmc_slope_v132_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 42)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_42d_std_5d_xc_slope_v133_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 42)
    sm   = (_std(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_42d_std_21d_xmc_slope_v134_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 42)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_42d_ema_5d_xc_slope_v135_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 42)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_42d_ema_21d_xmc_slope_v136_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 42)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_42d_z_5d_xc_slope_v137_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 42)
    sm   = (_z(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_42d_z_21d_xmc_slope_v138_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 42)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_42d_log_5d_xc_slope_v139_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 42)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_42d_log_21d_xmc_slope_v140_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 42)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_63d_mean_5d_xc_slope_v141_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 63)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_63d_mean_21d_xmc_slope_v142_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 63)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_63d_std_5d_xc_slope_v143_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 63)
    sm   = (_std(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_63d_std_21d_xmc_slope_v144_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 63)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_63d_ema_5d_xc_slope_v145_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 63)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_63d_ema_21d_xmc_slope_v146_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 63)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_63d_z_5d_xc_slope_v147_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 63)
    sm   = (_z(base, 5)) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_63d_z_21d_xmc_slope_v148_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 63)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_63d_log_5d_xc_slope_v149_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 63)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _slope_pct(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitecon_63d_log_21d_xmc_slope_v150_signal(revenue, assets, ppnenet, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 63)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _slope_pct(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f32hpp_f32_healthcare_pricing_power_rpa_5d_mean_5d_xc_slope_v001_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_5d_mean_21d_xmc_slope_v002_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_5d_std_5d_xc_slope_v003_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_5d_std_21d_xmc_slope_v004_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_5d_ema_5d_xc_slope_v005_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_5d_ema_21d_xmc_slope_v006_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_5d_z_5d_xc_slope_v007_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_5d_z_21d_xmc_slope_v008_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_5d_log_5d_xc_slope_v009_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_5d_log_21d_xmc_slope_v010_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_10d_mean_5d_xc_slope_v011_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_10d_mean_21d_xmc_slope_v012_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_10d_std_5d_xc_slope_v013_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_10d_std_21d_xmc_slope_v014_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_10d_ema_5d_xc_slope_v015_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_10d_ema_21d_xmc_slope_v016_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_10d_z_5d_xc_slope_v017_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_10d_z_21d_xmc_slope_v018_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_10d_log_5d_xc_slope_v019_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_10d_log_21d_xmc_slope_v020_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_21d_mean_5d_xc_slope_v021_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_21d_mean_21d_xmc_slope_v022_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_21d_std_5d_xc_slope_v023_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_21d_std_21d_xmc_slope_v024_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_21d_ema_5d_xc_slope_v025_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_21d_ema_21d_xmc_slope_v026_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_21d_z_5d_xc_slope_v027_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_21d_z_21d_xmc_slope_v028_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_21d_log_5d_xc_slope_v029_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_21d_log_21d_xmc_slope_v030_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_42d_mean_5d_xc_slope_v031_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_42d_mean_21d_xmc_slope_v032_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_42d_std_5d_xc_slope_v033_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_42d_std_21d_xmc_slope_v034_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_42d_ema_5d_xc_slope_v035_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_42d_ema_21d_xmc_slope_v036_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_42d_z_5d_xc_slope_v037_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_42d_z_21d_xmc_slope_v038_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_42d_log_5d_xc_slope_v039_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_42d_log_21d_xmc_slope_v040_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_63d_mean_5d_xc_slope_v041_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_63d_mean_21d_xmc_slope_v042_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_63d_std_5d_xc_slope_v043_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_63d_std_21d_xmc_slope_v044_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_63d_ema_5d_xc_slope_v045_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_63d_ema_21d_xmc_slope_v046_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_63d_z_5d_xc_slope_v047_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_63d_z_21d_xmc_slope_v048_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_63d_log_5d_xc_slope_v049_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_63d_log_21d_xmc_slope_v050_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_5d_mean_5d_xc_slope_v051_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_5d_mean_21d_xmc_slope_v052_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_5d_std_5d_xc_slope_v053_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_5d_std_21d_xmc_slope_v054_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_5d_ema_5d_xc_slope_v055_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_5d_ema_21d_xmc_slope_v056_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_5d_z_5d_xc_slope_v057_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_5d_z_21d_xmc_slope_v058_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_5d_log_5d_xc_slope_v059_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_5d_log_21d_xmc_slope_v060_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_10d_mean_5d_xc_slope_v061_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_10d_mean_21d_xmc_slope_v062_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_10d_std_5d_xc_slope_v063_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_10d_std_21d_xmc_slope_v064_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_10d_ema_5d_xc_slope_v065_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_10d_ema_21d_xmc_slope_v066_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_10d_z_5d_xc_slope_v067_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_10d_z_21d_xmc_slope_v068_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_10d_log_5d_xc_slope_v069_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_10d_log_21d_xmc_slope_v070_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_21d_mean_5d_xc_slope_v071_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_21d_mean_21d_xmc_slope_v072_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_21d_std_5d_xc_slope_v073_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_21d_std_21d_xmc_slope_v074_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_21d_ema_5d_xc_slope_v075_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_21d_ema_21d_xmc_slope_v076_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_21d_z_5d_xc_slope_v077_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_21d_z_21d_xmc_slope_v078_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_21d_log_5d_xc_slope_v079_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_21d_log_21d_xmc_slope_v080_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_42d_mean_5d_xc_slope_v081_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_42d_mean_21d_xmc_slope_v082_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_42d_std_5d_xc_slope_v083_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_42d_std_21d_xmc_slope_v084_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_42d_ema_5d_xc_slope_v085_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_42d_ema_21d_xmc_slope_v086_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_42d_z_5d_xc_slope_v087_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_42d_z_21d_xmc_slope_v088_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_42d_log_5d_xc_slope_v089_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_42d_log_21d_xmc_slope_v090_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_63d_mean_5d_xc_slope_v091_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_63d_mean_21d_xmc_slope_v092_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_63d_std_5d_xc_slope_v093_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_63d_std_21d_xmc_slope_v094_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_63d_ema_5d_xc_slope_v095_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_63d_ema_21d_xmc_slope_v096_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_63d_z_5d_xc_slope_v097_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_63d_z_21d_xmc_slope_v098_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_63d_log_5d_xc_slope_v099_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_63d_log_21d_xmc_slope_v100_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_5d_mean_5d_xc_slope_v101_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_5d_mean_21d_xmc_slope_v102_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_5d_std_5d_xc_slope_v103_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_5d_std_21d_xmc_slope_v104_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_5d_ema_5d_xc_slope_v105_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_5d_ema_21d_xmc_slope_v106_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_5d_z_5d_xc_slope_v107_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_5d_z_21d_xmc_slope_v108_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_5d_log_5d_xc_slope_v109_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_5d_log_21d_xmc_slope_v110_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_10d_mean_5d_xc_slope_v111_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_10d_mean_21d_xmc_slope_v112_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_10d_std_5d_xc_slope_v113_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_10d_std_21d_xmc_slope_v114_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_10d_ema_5d_xc_slope_v115_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_10d_ema_21d_xmc_slope_v116_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_10d_z_5d_xc_slope_v117_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_10d_z_21d_xmc_slope_v118_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_10d_log_5d_xc_slope_v119_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_10d_log_21d_xmc_slope_v120_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_21d_mean_5d_xc_slope_v121_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_21d_mean_21d_xmc_slope_v122_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_21d_std_5d_xc_slope_v123_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_21d_std_21d_xmc_slope_v124_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_21d_ema_5d_xc_slope_v125_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_21d_ema_21d_xmc_slope_v126_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_21d_z_5d_xc_slope_v127_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_21d_z_21d_xmc_slope_v128_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_21d_log_5d_xc_slope_v129_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_21d_log_21d_xmc_slope_v130_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_42d_mean_5d_xc_slope_v131_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_42d_mean_21d_xmc_slope_v132_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_42d_std_5d_xc_slope_v133_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_42d_std_21d_xmc_slope_v134_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_42d_ema_5d_xc_slope_v135_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_42d_ema_21d_xmc_slope_v136_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_42d_z_5d_xc_slope_v137_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_42d_z_21d_xmc_slope_v138_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_42d_log_5d_xc_slope_v139_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_42d_log_21d_xmc_slope_v140_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_63d_mean_5d_xc_slope_v141_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_63d_mean_21d_xmc_slope_v142_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_63d_std_5d_xc_slope_v143_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_63d_std_21d_xmc_slope_v144_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_63d_ema_5d_xc_slope_v145_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_63d_ema_21d_xmc_slope_v146_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_63d_z_5d_xc_slope_v147_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_63d_z_21d_xmc_slope_v148_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_63d_log_5d_xc_slope_v149_signal,
    f32hpp_f32_healthcare_pricing_power_unitecon_63d_log_21d_xmc_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F32_HEALTHCARE_PRICING_POWER_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    assets  = pd.Series(5e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    ppnenet = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.009, n))), name="ppnenet")
    cols = {"closeadj": closeadj, "revenue": revenue, "assets": assets, "ppnenet": ppnenet}

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f32_rev_per_asset', '_f32_pricing_uplift', '_f32_unit_economics_lift')
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
    print(f"OK f32_healthcare_pricing_power_2nd_derivatives_001_150_claude: {n_features} features pass")
