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


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)

# ===== folder domain primitives =====
def _f33_volume_proxy(revenue, ppnenet, w):
    rp = revenue / ppnenet.replace(0, np.nan)
    return _mean(rp, w)


def _f33_price_proxy(revenue, assets, w):
    ra = revenue / assets.replace(0, np.nan)
    return _mean(ra, w)


def _f33_volume_price_gap(revenue, ppnenet, assets, w):
    vp = revenue / ppnenet.replace(0, np.nan)
    pp = revenue / assets.replace(0, np.nan)
    return _mean(vp, w) - _mean(pp, w)

def f33hvp_f33_healthcare_volume_vs_price_volp_5d_mean_5d_xc_jerk_v001_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 5)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_5d_mean_21d_xmc_jerk_v002_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 5)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_5d_std_5d_xc_jerk_v003_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 5)
    sm   = (_std(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_5d_std_21d_xmc_jerk_v004_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 5)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_5d_ema_5d_xc_jerk_v005_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 5)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_5d_ema_21d_xmc_jerk_v006_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 5)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_5d_z_5d_xc_jerk_v007_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 5)
    sm   = (_z(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_5d_z_21d_xmc_jerk_v008_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 5)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_5d_log_5d_xc_jerk_v009_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 5)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_5d_log_21d_xmc_jerk_v010_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 5)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_10d_mean_5d_xc_jerk_v011_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 10)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_10d_mean_21d_xmc_jerk_v012_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 10)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_10d_std_5d_xc_jerk_v013_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 10)
    sm   = (_std(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_10d_std_21d_xmc_jerk_v014_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 10)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_10d_ema_5d_xc_jerk_v015_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 10)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_10d_ema_21d_xmc_jerk_v016_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 10)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_10d_z_5d_xc_jerk_v017_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 10)
    sm   = (_z(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_10d_z_21d_xmc_jerk_v018_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 10)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_10d_log_5d_xc_jerk_v019_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 10)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_10d_log_21d_xmc_jerk_v020_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 10)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_21d_mean_5d_xc_jerk_v021_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 21)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_21d_mean_21d_xmc_jerk_v022_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 21)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_21d_std_5d_xc_jerk_v023_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 21)
    sm   = (_std(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_21d_std_21d_xmc_jerk_v024_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 21)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_21d_ema_5d_xc_jerk_v025_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 21)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_21d_ema_21d_xmc_jerk_v026_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 21)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_21d_z_5d_xc_jerk_v027_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 21)
    sm   = (_z(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_21d_z_21d_xmc_jerk_v028_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 21)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_21d_log_5d_xc_jerk_v029_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 21)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_21d_log_21d_xmc_jerk_v030_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 21)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_42d_mean_5d_xc_jerk_v031_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 42)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_42d_mean_21d_xmc_jerk_v032_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 42)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_42d_std_5d_xc_jerk_v033_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 42)
    sm   = (_std(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_42d_std_21d_xmc_jerk_v034_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 42)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_42d_ema_5d_xc_jerk_v035_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 42)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_42d_ema_21d_xmc_jerk_v036_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 42)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_42d_z_5d_xc_jerk_v037_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 42)
    sm   = (_z(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_42d_z_21d_xmc_jerk_v038_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 42)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_42d_log_5d_xc_jerk_v039_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 42)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_42d_log_21d_xmc_jerk_v040_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 42)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_63d_mean_5d_xc_jerk_v041_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 63)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_63d_mean_21d_xmc_jerk_v042_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 63)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_63d_std_5d_xc_jerk_v043_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 63)
    sm   = (_std(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_63d_std_21d_xmc_jerk_v044_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 63)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_63d_ema_5d_xc_jerk_v045_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 63)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_63d_ema_21d_xmc_jerk_v046_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 63)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_63d_z_5d_xc_jerk_v047_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 63)
    sm   = (_z(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_63d_z_21d_xmc_jerk_v048_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 63)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_63d_log_5d_xc_jerk_v049_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 63)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_63d_log_21d_xmc_jerk_v050_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 63)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_5d_mean_5d_xc_jerk_v051_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 5)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_5d_mean_21d_xmc_jerk_v052_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 5)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_5d_std_5d_xc_jerk_v053_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 5)
    sm   = (_std(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_5d_std_21d_xmc_jerk_v054_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 5)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_5d_ema_5d_xc_jerk_v055_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 5)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_5d_ema_21d_xmc_jerk_v056_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 5)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_5d_z_5d_xc_jerk_v057_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 5)
    sm   = (_z(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_5d_z_21d_xmc_jerk_v058_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 5)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_5d_log_5d_xc_jerk_v059_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 5)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_5d_log_21d_xmc_jerk_v060_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 5)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_10d_mean_5d_xc_jerk_v061_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 10)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_10d_mean_21d_xmc_jerk_v062_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 10)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_10d_std_5d_xc_jerk_v063_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 10)
    sm   = (_std(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_10d_std_21d_xmc_jerk_v064_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 10)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_10d_ema_5d_xc_jerk_v065_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 10)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_10d_ema_21d_xmc_jerk_v066_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 10)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_10d_z_5d_xc_jerk_v067_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 10)
    sm   = (_z(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_10d_z_21d_xmc_jerk_v068_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 10)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_10d_log_5d_xc_jerk_v069_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 10)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_10d_log_21d_xmc_jerk_v070_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 10)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_21d_mean_5d_xc_jerk_v071_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 21)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_21d_mean_21d_xmc_jerk_v072_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 21)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_21d_std_5d_xc_jerk_v073_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 21)
    sm   = (_std(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_21d_std_21d_xmc_jerk_v074_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 21)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_21d_ema_5d_xc_jerk_v075_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 21)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_21d_ema_21d_xmc_jerk_v076_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 21)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_21d_z_5d_xc_jerk_v077_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 21)
    sm   = (_z(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_21d_z_21d_xmc_jerk_v078_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 21)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_21d_log_5d_xc_jerk_v079_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 21)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_21d_log_21d_xmc_jerk_v080_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 21)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_42d_mean_5d_xc_jerk_v081_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 42)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_42d_mean_21d_xmc_jerk_v082_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 42)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_42d_std_5d_xc_jerk_v083_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 42)
    sm   = (_std(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_42d_std_21d_xmc_jerk_v084_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 42)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_42d_ema_5d_xc_jerk_v085_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 42)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_42d_ema_21d_xmc_jerk_v086_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 42)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_42d_z_5d_xc_jerk_v087_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 42)
    sm   = (_z(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_42d_z_21d_xmc_jerk_v088_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 42)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_42d_log_5d_xc_jerk_v089_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 42)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_42d_log_21d_xmc_jerk_v090_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 42)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_63d_mean_5d_xc_jerk_v091_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 63)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_63d_mean_21d_xmc_jerk_v092_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 63)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_63d_std_5d_xc_jerk_v093_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 63)
    sm   = (_std(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_63d_std_21d_xmc_jerk_v094_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 63)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_63d_ema_5d_xc_jerk_v095_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 63)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_63d_ema_21d_xmc_jerk_v096_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 63)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_63d_z_5d_xc_jerk_v097_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 63)
    sm   = (_z(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_63d_z_21d_xmc_jerk_v098_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 63)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_63d_log_5d_xc_jerk_v099_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 63)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_pricep_63d_log_21d_xmc_jerk_v100_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 63)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_5d_mean_5d_xc_jerk_v101_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 5)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_5d_mean_21d_xmc_jerk_v102_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 5)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_5d_std_5d_xc_jerk_v103_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 5)
    sm   = (_std(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_5d_std_21d_xmc_jerk_v104_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 5)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_5d_ema_5d_xc_jerk_v105_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 5)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_5d_ema_21d_xmc_jerk_v106_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 5)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_5d_z_5d_xc_jerk_v107_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 5)
    sm   = (_z(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_5d_z_21d_xmc_jerk_v108_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 5)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_5d_log_5d_xc_jerk_v109_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 5)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_5d_log_21d_xmc_jerk_v110_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 5)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_10d_mean_5d_xc_jerk_v111_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 10)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_10d_mean_21d_xmc_jerk_v112_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 10)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_10d_std_5d_xc_jerk_v113_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 10)
    sm   = (_std(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_10d_std_21d_xmc_jerk_v114_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 10)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_10d_ema_5d_xc_jerk_v115_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 10)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_10d_ema_21d_xmc_jerk_v116_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 10)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_10d_z_5d_xc_jerk_v117_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 10)
    sm   = (_z(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_10d_z_21d_xmc_jerk_v118_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 10)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_10d_log_5d_xc_jerk_v119_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 10)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_10d_log_21d_xmc_jerk_v120_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 10)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_21d_mean_5d_xc_jerk_v121_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 21)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_21d_mean_21d_xmc_jerk_v122_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 21)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_21d_std_5d_xc_jerk_v123_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 21)
    sm   = (_std(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_21d_std_21d_xmc_jerk_v124_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 21)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_21d_ema_5d_xc_jerk_v125_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 21)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_21d_ema_21d_xmc_jerk_v126_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 21)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_21d_z_5d_xc_jerk_v127_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 21)
    sm   = (_z(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_21d_z_21d_xmc_jerk_v128_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 21)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_21d_log_5d_xc_jerk_v129_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 21)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_21d_log_21d_xmc_jerk_v130_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 21)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_42d_mean_5d_xc_jerk_v131_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 42)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_42d_mean_21d_xmc_jerk_v132_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 42)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_42d_std_5d_xc_jerk_v133_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 42)
    sm   = (_std(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_42d_std_21d_xmc_jerk_v134_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 42)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_42d_ema_5d_xc_jerk_v135_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 42)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_42d_ema_21d_xmc_jerk_v136_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 42)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_42d_z_5d_xc_jerk_v137_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 42)
    sm   = (_z(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_42d_z_21d_xmc_jerk_v138_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 42)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_42d_log_5d_xc_jerk_v139_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 42)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_42d_log_21d_xmc_jerk_v140_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 42)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_63d_mean_5d_xc_jerk_v141_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 63)
    sm   = (_mean(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_63d_mean_21d_xmc_jerk_v142_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 63)
    sm   = (_mean(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_63d_std_5d_xc_jerk_v143_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 63)
    sm   = (_std(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_63d_std_21d_xmc_jerk_v144_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 63)
    sm   = (_std(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_63d_ema_5d_xc_jerk_v145_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 63)
    sm   = (_ema(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_63d_ema_21d_xmc_jerk_v146_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 63)
    sm   = (_ema(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_63d_z_5d_xc_jerk_v147_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 63)
    sm   = (_z(base, 5)) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_63d_z_21d_xmc_jerk_v148_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 63)
    sm   = (_z(base, 21)) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_63d_log_5d_xc_jerk_v149_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 63)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 5) * 0.0) * (closeadj)
    result = _jerk(sm, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_63d_log_21d_xmc_jerk_v150_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 63)
    sm   = (np.sign(base) * np.log1p(base.abs()) + _mean(base, 21) * 0.0) * (_mean(closeadj, 21))
    result = _jerk(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f33hvp_f33_healthcare_volume_vs_price_volp_5d_mean_5d_xc_jerk_v001_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_5d_mean_21d_xmc_jerk_v002_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_5d_std_5d_xc_jerk_v003_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_5d_std_21d_xmc_jerk_v004_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_5d_ema_5d_xc_jerk_v005_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_5d_ema_21d_xmc_jerk_v006_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_5d_z_5d_xc_jerk_v007_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_5d_z_21d_xmc_jerk_v008_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_5d_log_5d_xc_jerk_v009_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_5d_log_21d_xmc_jerk_v010_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_10d_mean_5d_xc_jerk_v011_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_10d_mean_21d_xmc_jerk_v012_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_10d_std_5d_xc_jerk_v013_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_10d_std_21d_xmc_jerk_v014_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_10d_ema_5d_xc_jerk_v015_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_10d_ema_21d_xmc_jerk_v016_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_10d_z_5d_xc_jerk_v017_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_10d_z_21d_xmc_jerk_v018_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_10d_log_5d_xc_jerk_v019_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_10d_log_21d_xmc_jerk_v020_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_21d_mean_5d_xc_jerk_v021_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_21d_mean_21d_xmc_jerk_v022_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_21d_std_5d_xc_jerk_v023_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_21d_std_21d_xmc_jerk_v024_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_21d_ema_5d_xc_jerk_v025_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_21d_ema_21d_xmc_jerk_v026_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_21d_z_5d_xc_jerk_v027_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_21d_z_21d_xmc_jerk_v028_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_21d_log_5d_xc_jerk_v029_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_21d_log_21d_xmc_jerk_v030_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_42d_mean_5d_xc_jerk_v031_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_42d_mean_21d_xmc_jerk_v032_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_42d_std_5d_xc_jerk_v033_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_42d_std_21d_xmc_jerk_v034_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_42d_ema_5d_xc_jerk_v035_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_42d_ema_21d_xmc_jerk_v036_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_42d_z_5d_xc_jerk_v037_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_42d_z_21d_xmc_jerk_v038_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_42d_log_5d_xc_jerk_v039_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_42d_log_21d_xmc_jerk_v040_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_63d_mean_5d_xc_jerk_v041_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_63d_mean_21d_xmc_jerk_v042_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_63d_std_5d_xc_jerk_v043_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_63d_std_21d_xmc_jerk_v044_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_63d_ema_5d_xc_jerk_v045_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_63d_ema_21d_xmc_jerk_v046_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_63d_z_5d_xc_jerk_v047_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_63d_z_21d_xmc_jerk_v048_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_63d_log_5d_xc_jerk_v049_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_63d_log_21d_xmc_jerk_v050_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_5d_mean_5d_xc_jerk_v051_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_5d_mean_21d_xmc_jerk_v052_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_5d_std_5d_xc_jerk_v053_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_5d_std_21d_xmc_jerk_v054_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_5d_ema_5d_xc_jerk_v055_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_5d_ema_21d_xmc_jerk_v056_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_5d_z_5d_xc_jerk_v057_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_5d_z_21d_xmc_jerk_v058_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_5d_log_5d_xc_jerk_v059_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_5d_log_21d_xmc_jerk_v060_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_10d_mean_5d_xc_jerk_v061_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_10d_mean_21d_xmc_jerk_v062_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_10d_std_5d_xc_jerk_v063_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_10d_std_21d_xmc_jerk_v064_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_10d_ema_5d_xc_jerk_v065_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_10d_ema_21d_xmc_jerk_v066_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_10d_z_5d_xc_jerk_v067_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_10d_z_21d_xmc_jerk_v068_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_10d_log_5d_xc_jerk_v069_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_10d_log_21d_xmc_jerk_v070_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_21d_mean_5d_xc_jerk_v071_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_21d_mean_21d_xmc_jerk_v072_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_21d_std_5d_xc_jerk_v073_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_21d_std_21d_xmc_jerk_v074_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_21d_ema_5d_xc_jerk_v075_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_21d_ema_21d_xmc_jerk_v076_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_21d_z_5d_xc_jerk_v077_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_21d_z_21d_xmc_jerk_v078_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_21d_log_5d_xc_jerk_v079_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_21d_log_21d_xmc_jerk_v080_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_42d_mean_5d_xc_jerk_v081_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_42d_mean_21d_xmc_jerk_v082_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_42d_std_5d_xc_jerk_v083_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_42d_std_21d_xmc_jerk_v084_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_42d_ema_5d_xc_jerk_v085_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_42d_ema_21d_xmc_jerk_v086_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_42d_z_5d_xc_jerk_v087_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_42d_z_21d_xmc_jerk_v088_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_42d_log_5d_xc_jerk_v089_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_42d_log_21d_xmc_jerk_v090_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_63d_mean_5d_xc_jerk_v091_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_63d_mean_21d_xmc_jerk_v092_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_63d_std_5d_xc_jerk_v093_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_63d_std_21d_xmc_jerk_v094_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_63d_ema_5d_xc_jerk_v095_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_63d_ema_21d_xmc_jerk_v096_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_63d_z_5d_xc_jerk_v097_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_63d_z_21d_xmc_jerk_v098_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_63d_log_5d_xc_jerk_v099_signal,
    f33hvp_f33_healthcare_volume_vs_price_pricep_63d_log_21d_xmc_jerk_v100_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_5d_mean_5d_xc_jerk_v101_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_5d_mean_21d_xmc_jerk_v102_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_5d_std_5d_xc_jerk_v103_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_5d_std_21d_xmc_jerk_v104_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_5d_ema_5d_xc_jerk_v105_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_5d_ema_21d_xmc_jerk_v106_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_5d_z_5d_xc_jerk_v107_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_5d_z_21d_xmc_jerk_v108_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_5d_log_5d_xc_jerk_v109_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_5d_log_21d_xmc_jerk_v110_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_10d_mean_5d_xc_jerk_v111_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_10d_mean_21d_xmc_jerk_v112_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_10d_std_5d_xc_jerk_v113_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_10d_std_21d_xmc_jerk_v114_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_10d_ema_5d_xc_jerk_v115_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_10d_ema_21d_xmc_jerk_v116_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_10d_z_5d_xc_jerk_v117_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_10d_z_21d_xmc_jerk_v118_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_10d_log_5d_xc_jerk_v119_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_10d_log_21d_xmc_jerk_v120_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_21d_mean_5d_xc_jerk_v121_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_21d_mean_21d_xmc_jerk_v122_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_21d_std_5d_xc_jerk_v123_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_21d_std_21d_xmc_jerk_v124_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_21d_ema_5d_xc_jerk_v125_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_21d_ema_21d_xmc_jerk_v126_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_21d_z_5d_xc_jerk_v127_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_21d_z_21d_xmc_jerk_v128_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_21d_log_5d_xc_jerk_v129_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_21d_log_21d_xmc_jerk_v130_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_42d_mean_5d_xc_jerk_v131_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_42d_mean_21d_xmc_jerk_v132_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_42d_std_5d_xc_jerk_v133_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_42d_std_21d_xmc_jerk_v134_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_42d_ema_5d_xc_jerk_v135_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_42d_ema_21d_xmc_jerk_v136_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_42d_z_5d_xc_jerk_v137_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_42d_z_21d_xmc_jerk_v138_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_42d_log_5d_xc_jerk_v139_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_42d_log_21d_xmc_jerk_v140_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_63d_mean_5d_xc_jerk_v141_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_63d_mean_21d_xmc_jerk_v142_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_63d_std_5d_xc_jerk_v143_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_63d_std_21d_xmc_jerk_v144_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_63d_ema_5d_xc_jerk_v145_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_63d_ema_21d_xmc_jerk_v146_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_63d_z_5d_xc_jerk_v147_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_63d_z_21d_xmc_jerk_v148_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_63d_log_5d_xc_jerk_v149_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_63d_log_21d_xmc_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F33_HEALTHCARE_VOLUME_VS_PRICE_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ppnenet = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.009, n))), name="ppnenet")
    assets  = pd.Series(5e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    cols = {"closeadj": closeadj, "revenue": revenue, "ppnenet": ppnenet, "assets": assets}

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f33_volume_proxy', '_f33_price_proxy', '_f33_volume_price_gap')
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
    print(f"OK f33_healthcare_volume_vs_price_3rd_derivatives_001_150_claude: {n_features} features pass")
