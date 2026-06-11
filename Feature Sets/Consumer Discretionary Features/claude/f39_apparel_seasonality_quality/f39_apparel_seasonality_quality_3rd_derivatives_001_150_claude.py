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


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f39_seasonal_inv_pattern(inventory, w):
    # Detrended inventory: deviation from rolling mean
    return (inventory - _mean(inventory, w)) / _mean(inventory, w).replace(0, np.nan)


def _f39_revenue_inv_sync(revenue, inventory, w):
    # Rolling correlation of revenue & inventory growth
    rg = revenue.pct_change()
    ig = inventory.pct_change()
    return rg.rolling(w, min_periods=max(1, w // 2)).corr(ig)


def _f39_seasonality_quality(revenue, inventory, w):
    # High sync + low residual => good seasonal management
    rg = revenue.pct_change()
    ig = inventory.pct_change()
    corr = rg.rolling(w, min_periods=max(1, w // 2)).corr(ig)
    resid_std = _std(ig - rg, w)
    return corr / resid_std.replace(0, np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinv_21d_jerk_v001_signal(inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 21)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinv_21d_jerk_v002_signal(inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 21)
    result = _jerk(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinv_21d_jerk_v003_signal(inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 21)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinv_21d_jerk_v004_signal(inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 21)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinv_21d_jerk_v005_signal(inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 21)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinv_21d_jerk_v006_signal(inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 21)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinv_63d_jerk_v007_signal(inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 63)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinv_63d_jerk_v008_signal(inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 63)
    result = _jerk(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinv_63d_jerk_v009_signal(inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 63)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinv_63d_jerk_v010_signal(inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 63)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinv_63d_jerk_v011_signal(inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 63)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinv_63d_jerk_v012_signal(inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 63)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinv_126d_jerk_v013_signal(inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 126)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinv_126d_jerk_v014_signal(inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 126)
    result = _jerk(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinv_126d_jerk_v015_signal(inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 126)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinv_126d_jerk_v016_signal(inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 126)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinv_126d_jerk_v017_signal(inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 126)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinv_126d_jerk_v018_signal(inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 126)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinv_252d_jerk_v019_signal(inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 252)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinv_252d_jerk_v020_signal(inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 252)
    result = _jerk(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinv_252d_jerk_v021_signal(inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 252)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinv_252d_jerk_v022_signal(inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 252)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinv_252d_jerk_v023_signal(inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 252)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinv_252d_jerk_v024_signal(inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 252)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinv_378d_jerk_v025_signal(inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 378)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinv_378d_jerk_v026_signal(inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 378)
    result = _jerk(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinv_378d_jerk_v027_signal(inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 378)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinv_378d_jerk_v028_signal(inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 378)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinv_378d_jerk_v029_signal(inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 378)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinv_378d_jerk_v030_signal(inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 378)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsync_21d_jerk_v031_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 21)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsync_21d_jerk_v032_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 21)
    result = _jerk(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsync_21d_jerk_v033_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 21)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsync_21d_jerk_v034_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 21)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsync_21d_jerk_v035_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 21)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsync_21d_jerk_v036_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 21)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsync_63d_jerk_v037_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 63)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsync_63d_jerk_v038_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 63)
    result = _jerk(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsync_63d_jerk_v039_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 63)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsync_63d_jerk_v040_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 63)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsync_63d_jerk_v041_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 63)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsync_63d_jerk_v042_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 63)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsync_126d_jerk_v043_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 126)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsync_126d_jerk_v044_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 126)
    result = _jerk(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsync_126d_jerk_v045_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 126)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsync_126d_jerk_v046_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 126)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsync_126d_jerk_v047_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 126)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsync_126d_jerk_v048_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 126)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsync_252d_jerk_v049_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 252)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsync_252d_jerk_v050_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 252)
    result = _jerk(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsync_252d_jerk_v051_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 252)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsync_252d_jerk_v052_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 252)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsync_252d_jerk_v053_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 252)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsync_252d_jerk_v054_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 252)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsync_378d_jerk_v055_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 378)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsync_378d_jerk_v056_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 378)
    result = _jerk(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsync_378d_jerk_v057_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 378)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsync_378d_jerk_v058_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 378)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsync_378d_jerk_v059_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 378)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsync_378d_jerk_v060_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 378)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqual_21d_jerk_v061_signal(revenue, inventory, closeadj):
    base = _f39_seasonality_quality(revenue, inventory, 21)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqual_21d_jerk_v062_signal(revenue, inventory, closeadj):
    base = _f39_seasonality_quality(revenue, inventory, 21)
    result = _jerk(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqual_21d_jerk_v063_signal(revenue, inventory, closeadj):
    base = _f39_seasonality_quality(revenue, inventory, 21)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqual_21d_jerk_v064_signal(revenue, inventory, closeadj):
    base = _f39_seasonality_quality(revenue, inventory, 21)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqual_21d_jerk_v065_signal(revenue, inventory, closeadj):
    base = _f39_seasonality_quality(revenue, inventory, 21)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqual_21d_jerk_v066_signal(revenue, inventory, closeadj):
    base = _f39_seasonality_quality(revenue, inventory, 21)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqual_63d_jerk_v067_signal(revenue, inventory, closeadj):
    base = _f39_seasonality_quality(revenue, inventory, 63)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqual_63d_jerk_v068_signal(revenue, inventory, closeadj):
    base = _f39_seasonality_quality(revenue, inventory, 63)
    result = _jerk(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqual_63d_jerk_v069_signal(revenue, inventory, closeadj):
    base = _f39_seasonality_quality(revenue, inventory, 63)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqual_63d_jerk_v070_signal(revenue, inventory, closeadj):
    base = _f39_seasonality_quality(revenue, inventory, 63)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqual_63d_jerk_v071_signal(revenue, inventory, closeadj):
    base = _f39_seasonality_quality(revenue, inventory, 63)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqual_63d_jerk_v072_signal(revenue, inventory, closeadj):
    base = _f39_seasonality_quality(revenue, inventory, 63)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqual_126d_jerk_v073_signal(revenue, inventory, closeadj):
    base = _f39_seasonality_quality(revenue, inventory, 126)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqual_126d_jerk_v074_signal(revenue, inventory, closeadj):
    base = _f39_seasonality_quality(revenue, inventory, 126)
    result = _jerk(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqual_126d_jerk_v075_signal(revenue, inventory, closeadj):
    base = _f39_seasonality_quality(revenue, inventory, 126)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqual_126d_jerk_v076_signal(revenue, inventory, closeadj):
    base = _f39_seasonality_quality(revenue, inventory, 126)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqual_126d_jerk_v077_signal(revenue, inventory, closeadj):
    base = _f39_seasonality_quality(revenue, inventory, 126)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqual_126d_jerk_v078_signal(revenue, inventory, closeadj):
    base = _f39_seasonality_quality(revenue, inventory, 126)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqual_252d_jerk_v079_signal(revenue, inventory, closeadj):
    base = _f39_seasonality_quality(revenue, inventory, 252)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqual_252d_jerk_v080_signal(revenue, inventory, closeadj):
    base = _f39_seasonality_quality(revenue, inventory, 252)
    result = _jerk(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqual_252d_jerk_v081_signal(revenue, inventory, closeadj):
    base = _f39_seasonality_quality(revenue, inventory, 252)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqual_252d_jerk_v082_signal(revenue, inventory, closeadj):
    base = _f39_seasonality_quality(revenue, inventory, 252)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqual_252d_jerk_v083_signal(revenue, inventory, closeadj):
    base = _f39_seasonality_quality(revenue, inventory, 252)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqual_252d_jerk_v084_signal(revenue, inventory, closeadj):
    base = _f39_seasonality_quality(revenue, inventory, 252)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqual_378d_jerk_v085_signal(revenue, inventory, closeadj):
    base = _f39_seasonality_quality(revenue, inventory, 378)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqual_378d_jerk_v086_signal(revenue, inventory, closeadj):
    base = _f39_seasonality_quality(revenue, inventory, 378)
    result = _jerk(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqual_378d_jerk_v087_signal(revenue, inventory, closeadj):
    base = _f39_seasonality_quality(revenue, inventory, 378)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqual_378d_jerk_v088_signal(revenue, inventory, closeadj):
    base = _f39_seasonality_quality(revenue, inventory, 378)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqual_378d_jerk_v089_signal(revenue, inventory, closeadj):
    base = _f39_seasonality_quality(revenue, inventory, 378)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqual_378d_jerk_v090_signal(revenue, inventory, closeadj):
    base = _f39_seasonality_quality(revenue, inventory, 378)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrev_21d_jerk_v091_signal(revenue, inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 21) * (revenue / 1e9)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrev_21d_jerk_v092_signal(revenue, inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 21) * (revenue / 1e9)
    result = _jerk(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrev_21d_jerk_v093_signal(revenue, inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 21) * (revenue / 1e9)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrev_21d_jerk_v094_signal(revenue, inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 21) * (revenue / 1e9)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrev_21d_jerk_v095_signal(revenue, inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 21) * (revenue / 1e9)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrev_21d_jerk_v096_signal(revenue, inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 21) * (revenue / 1e9)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrev_63d_jerk_v097_signal(revenue, inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 63) * (revenue / 1e9)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrev_63d_jerk_v098_signal(revenue, inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 63) * (revenue / 1e9)
    result = _jerk(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrev_63d_jerk_v099_signal(revenue, inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 63) * (revenue / 1e9)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrev_63d_jerk_v100_signal(revenue, inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 63) * (revenue / 1e9)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrev_63d_jerk_v101_signal(revenue, inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 63) * (revenue / 1e9)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrev_63d_jerk_v102_signal(revenue, inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 63) * (revenue / 1e9)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrev_126d_jerk_v103_signal(revenue, inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 126) * (revenue / 1e9)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrev_126d_jerk_v104_signal(revenue, inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 126) * (revenue / 1e9)
    result = _jerk(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrev_126d_jerk_v105_signal(revenue, inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 126) * (revenue / 1e9)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrev_126d_jerk_v106_signal(revenue, inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 126) * (revenue / 1e9)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrev_126d_jerk_v107_signal(revenue, inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 126) * (revenue / 1e9)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrev_126d_jerk_v108_signal(revenue, inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 126) * (revenue / 1e9)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrev_252d_jerk_v109_signal(revenue, inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 252) * (revenue / 1e9)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrev_252d_jerk_v110_signal(revenue, inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 252) * (revenue / 1e9)
    result = _jerk(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrev_252d_jerk_v111_signal(revenue, inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 252) * (revenue / 1e9)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrev_252d_jerk_v112_signal(revenue, inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 252) * (revenue / 1e9)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrev_252d_jerk_v113_signal(revenue, inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 252) * (revenue / 1e9)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrev_252d_jerk_v114_signal(revenue, inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 252) * (revenue / 1e9)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrev_378d_jerk_v115_signal(revenue, inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 378) * (revenue / 1e9)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrev_378d_jerk_v116_signal(revenue, inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 378) * (revenue / 1e9)
    result = _jerk(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrev_378d_jerk_v117_signal(revenue, inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 378) * (revenue / 1e9)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrev_378d_jerk_v118_signal(revenue, inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 378) * (revenue / 1e9)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrev_378d_jerk_v119_signal(revenue, inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 378) * (revenue / 1e9)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrev_378d_jerk_v120_signal(revenue, inventory, closeadj):
    base = _f39_seasonal_inv_pattern(inventory, 378) * (revenue / 1e9)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_syncxinv_21d_jerk_v121_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 21) * (inventory / 1e8)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_syncxinv_21d_jerk_v122_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 21) * (inventory / 1e8)
    result = _jerk(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_syncxinv_21d_jerk_v123_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 21) * (inventory / 1e8)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_syncxinv_21d_jerk_v124_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 21) * (inventory / 1e8)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_syncxinv_21d_jerk_v125_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 21) * (inventory / 1e8)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_syncxinv_21d_jerk_v126_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 21) * (inventory / 1e8)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_syncxinv_63d_jerk_v127_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 63) * (inventory / 1e8)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_syncxinv_63d_jerk_v128_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 63) * (inventory / 1e8)
    result = _jerk(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_syncxinv_63d_jerk_v129_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 63) * (inventory / 1e8)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_syncxinv_63d_jerk_v130_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 63) * (inventory / 1e8)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_syncxinv_63d_jerk_v131_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 63) * (inventory / 1e8)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_syncxinv_63d_jerk_v132_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 63) * (inventory / 1e8)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_syncxinv_126d_jerk_v133_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 126) * (inventory / 1e8)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_syncxinv_126d_jerk_v134_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 126) * (inventory / 1e8)
    result = _jerk(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_syncxinv_126d_jerk_v135_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 126) * (inventory / 1e8)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_syncxinv_126d_jerk_v136_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 126) * (inventory / 1e8)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_syncxinv_126d_jerk_v137_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 126) * (inventory / 1e8)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_syncxinv_126d_jerk_v138_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 126) * (inventory / 1e8)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_syncxinv_252d_jerk_v139_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 252) * (inventory / 1e8)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_syncxinv_252d_jerk_v140_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 252) * (inventory / 1e8)
    result = _jerk(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_syncxinv_252d_jerk_v141_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 252) * (inventory / 1e8)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_syncxinv_252d_jerk_v142_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 252) * (inventory / 1e8)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_syncxinv_252d_jerk_v143_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 252) * (inventory / 1e8)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_syncxinv_252d_jerk_v144_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 252) * (inventory / 1e8)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_syncxinv_378d_jerk_v145_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 378) * (inventory / 1e8)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_syncxinv_378d_jerk_v146_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 378) * (inventory / 1e8)
    result = _jerk(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_syncxinv_378d_jerk_v147_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 378) * (inventory / 1e8)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_syncxinv_378d_jerk_v148_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 378) * (inventory / 1e8)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_syncxinv_378d_jerk_v149_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 378) * (inventory / 1e8)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_syncxinv_378d_jerk_v150_signal(revenue, inventory, closeadj):
    base = _f39_revenue_inv_sync(revenue, inventory, 378) * (inventory / 1e8)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f39asq_f39_apparel_seasonality_quality_seasinv_21d_jerk_v001_signal,
    f39asq_f39_apparel_seasonality_quality_seasinv_21d_jerk_v002_signal,
    f39asq_f39_apparel_seasonality_quality_seasinv_21d_jerk_v003_signal,
    f39asq_f39_apparel_seasonality_quality_seasinv_21d_jerk_v004_signal,
    f39asq_f39_apparel_seasonality_quality_seasinv_21d_jerk_v005_signal,
    f39asq_f39_apparel_seasonality_quality_seasinv_21d_jerk_v006_signal,
    f39asq_f39_apparel_seasonality_quality_seasinv_63d_jerk_v007_signal,
    f39asq_f39_apparel_seasonality_quality_seasinv_63d_jerk_v008_signal,
    f39asq_f39_apparel_seasonality_quality_seasinv_63d_jerk_v009_signal,
    f39asq_f39_apparel_seasonality_quality_seasinv_63d_jerk_v010_signal,
    f39asq_f39_apparel_seasonality_quality_seasinv_63d_jerk_v011_signal,
    f39asq_f39_apparel_seasonality_quality_seasinv_63d_jerk_v012_signal,
    f39asq_f39_apparel_seasonality_quality_seasinv_126d_jerk_v013_signal,
    f39asq_f39_apparel_seasonality_quality_seasinv_126d_jerk_v014_signal,
    f39asq_f39_apparel_seasonality_quality_seasinv_126d_jerk_v015_signal,
    f39asq_f39_apparel_seasonality_quality_seasinv_126d_jerk_v016_signal,
    f39asq_f39_apparel_seasonality_quality_seasinv_126d_jerk_v017_signal,
    f39asq_f39_apparel_seasonality_quality_seasinv_126d_jerk_v018_signal,
    f39asq_f39_apparel_seasonality_quality_seasinv_252d_jerk_v019_signal,
    f39asq_f39_apparel_seasonality_quality_seasinv_252d_jerk_v020_signal,
    f39asq_f39_apparel_seasonality_quality_seasinv_252d_jerk_v021_signal,
    f39asq_f39_apparel_seasonality_quality_seasinv_252d_jerk_v022_signal,
    f39asq_f39_apparel_seasonality_quality_seasinv_252d_jerk_v023_signal,
    f39asq_f39_apparel_seasonality_quality_seasinv_252d_jerk_v024_signal,
    f39asq_f39_apparel_seasonality_quality_seasinv_378d_jerk_v025_signal,
    f39asq_f39_apparel_seasonality_quality_seasinv_378d_jerk_v026_signal,
    f39asq_f39_apparel_seasonality_quality_seasinv_378d_jerk_v027_signal,
    f39asq_f39_apparel_seasonality_quality_seasinv_378d_jerk_v028_signal,
    f39asq_f39_apparel_seasonality_quality_seasinv_378d_jerk_v029_signal,
    f39asq_f39_apparel_seasonality_quality_seasinv_378d_jerk_v030_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsync_21d_jerk_v031_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsync_21d_jerk_v032_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsync_21d_jerk_v033_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsync_21d_jerk_v034_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsync_21d_jerk_v035_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsync_21d_jerk_v036_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsync_63d_jerk_v037_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsync_63d_jerk_v038_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsync_63d_jerk_v039_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsync_63d_jerk_v040_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsync_63d_jerk_v041_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsync_63d_jerk_v042_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsync_126d_jerk_v043_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsync_126d_jerk_v044_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsync_126d_jerk_v045_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsync_126d_jerk_v046_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsync_126d_jerk_v047_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsync_126d_jerk_v048_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsync_252d_jerk_v049_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsync_252d_jerk_v050_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsync_252d_jerk_v051_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsync_252d_jerk_v052_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsync_252d_jerk_v053_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsync_252d_jerk_v054_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsync_378d_jerk_v055_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsync_378d_jerk_v056_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsync_378d_jerk_v057_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsync_378d_jerk_v058_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsync_378d_jerk_v059_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsync_378d_jerk_v060_signal,
    f39asq_f39_apparel_seasonality_quality_seasqual_21d_jerk_v061_signal,
    f39asq_f39_apparel_seasonality_quality_seasqual_21d_jerk_v062_signal,
    f39asq_f39_apparel_seasonality_quality_seasqual_21d_jerk_v063_signal,
    f39asq_f39_apparel_seasonality_quality_seasqual_21d_jerk_v064_signal,
    f39asq_f39_apparel_seasonality_quality_seasqual_21d_jerk_v065_signal,
    f39asq_f39_apparel_seasonality_quality_seasqual_21d_jerk_v066_signal,
    f39asq_f39_apparel_seasonality_quality_seasqual_63d_jerk_v067_signal,
    f39asq_f39_apparel_seasonality_quality_seasqual_63d_jerk_v068_signal,
    f39asq_f39_apparel_seasonality_quality_seasqual_63d_jerk_v069_signal,
    f39asq_f39_apparel_seasonality_quality_seasqual_63d_jerk_v070_signal,
    f39asq_f39_apparel_seasonality_quality_seasqual_63d_jerk_v071_signal,
    f39asq_f39_apparel_seasonality_quality_seasqual_63d_jerk_v072_signal,
    f39asq_f39_apparel_seasonality_quality_seasqual_126d_jerk_v073_signal,
    f39asq_f39_apparel_seasonality_quality_seasqual_126d_jerk_v074_signal,
    f39asq_f39_apparel_seasonality_quality_seasqual_126d_jerk_v075_signal,
    f39asq_f39_apparel_seasonality_quality_seasqual_126d_jerk_v076_signal,
    f39asq_f39_apparel_seasonality_quality_seasqual_126d_jerk_v077_signal,
    f39asq_f39_apparel_seasonality_quality_seasqual_126d_jerk_v078_signal,
    f39asq_f39_apparel_seasonality_quality_seasqual_252d_jerk_v079_signal,
    f39asq_f39_apparel_seasonality_quality_seasqual_252d_jerk_v080_signal,
    f39asq_f39_apparel_seasonality_quality_seasqual_252d_jerk_v081_signal,
    f39asq_f39_apparel_seasonality_quality_seasqual_252d_jerk_v082_signal,
    f39asq_f39_apparel_seasonality_quality_seasqual_252d_jerk_v083_signal,
    f39asq_f39_apparel_seasonality_quality_seasqual_252d_jerk_v084_signal,
    f39asq_f39_apparel_seasonality_quality_seasqual_378d_jerk_v085_signal,
    f39asq_f39_apparel_seasonality_quality_seasqual_378d_jerk_v086_signal,
    f39asq_f39_apparel_seasonality_quality_seasqual_378d_jerk_v087_signal,
    f39asq_f39_apparel_seasonality_quality_seasqual_378d_jerk_v088_signal,
    f39asq_f39_apparel_seasonality_quality_seasqual_378d_jerk_v089_signal,
    f39asq_f39_apparel_seasonality_quality_seasqual_378d_jerk_v090_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrev_21d_jerk_v091_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrev_21d_jerk_v092_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrev_21d_jerk_v093_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrev_21d_jerk_v094_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrev_21d_jerk_v095_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrev_21d_jerk_v096_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrev_63d_jerk_v097_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrev_63d_jerk_v098_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrev_63d_jerk_v099_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrev_63d_jerk_v100_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrev_63d_jerk_v101_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrev_63d_jerk_v102_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrev_126d_jerk_v103_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrev_126d_jerk_v104_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrev_126d_jerk_v105_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrev_126d_jerk_v106_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrev_126d_jerk_v107_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrev_126d_jerk_v108_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrev_252d_jerk_v109_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrev_252d_jerk_v110_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrev_252d_jerk_v111_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrev_252d_jerk_v112_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrev_252d_jerk_v113_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrev_252d_jerk_v114_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrev_378d_jerk_v115_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrev_378d_jerk_v116_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrev_378d_jerk_v117_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrev_378d_jerk_v118_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrev_378d_jerk_v119_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrev_378d_jerk_v120_signal,
    f39asq_f39_apparel_seasonality_quality_syncxinv_21d_jerk_v121_signal,
    f39asq_f39_apparel_seasonality_quality_syncxinv_21d_jerk_v122_signal,
    f39asq_f39_apparel_seasonality_quality_syncxinv_21d_jerk_v123_signal,
    f39asq_f39_apparel_seasonality_quality_syncxinv_21d_jerk_v124_signal,
    f39asq_f39_apparel_seasonality_quality_syncxinv_21d_jerk_v125_signal,
    f39asq_f39_apparel_seasonality_quality_syncxinv_21d_jerk_v126_signal,
    f39asq_f39_apparel_seasonality_quality_syncxinv_63d_jerk_v127_signal,
    f39asq_f39_apparel_seasonality_quality_syncxinv_63d_jerk_v128_signal,
    f39asq_f39_apparel_seasonality_quality_syncxinv_63d_jerk_v129_signal,
    f39asq_f39_apparel_seasonality_quality_syncxinv_63d_jerk_v130_signal,
    f39asq_f39_apparel_seasonality_quality_syncxinv_63d_jerk_v131_signal,
    f39asq_f39_apparel_seasonality_quality_syncxinv_63d_jerk_v132_signal,
    f39asq_f39_apparel_seasonality_quality_syncxinv_126d_jerk_v133_signal,
    f39asq_f39_apparel_seasonality_quality_syncxinv_126d_jerk_v134_signal,
    f39asq_f39_apparel_seasonality_quality_syncxinv_126d_jerk_v135_signal,
    f39asq_f39_apparel_seasonality_quality_syncxinv_126d_jerk_v136_signal,
    f39asq_f39_apparel_seasonality_quality_syncxinv_126d_jerk_v137_signal,
    f39asq_f39_apparel_seasonality_quality_syncxinv_126d_jerk_v138_signal,
    f39asq_f39_apparel_seasonality_quality_syncxinv_252d_jerk_v139_signal,
    f39asq_f39_apparel_seasonality_quality_syncxinv_252d_jerk_v140_signal,
    f39asq_f39_apparel_seasonality_quality_syncxinv_252d_jerk_v141_signal,
    f39asq_f39_apparel_seasonality_quality_syncxinv_252d_jerk_v142_signal,
    f39asq_f39_apparel_seasonality_quality_syncxinv_252d_jerk_v143_signal,
    f39asq_f39_apparel_seasonality_quality_syncxinv_252d_jerk_v144_signal,
    f39asq_f39_apparel_seasonality_quality_syncxinv_378d_jerk_v145_signal,
    f39asq_f39_apparel_seasonality_quality_syncxinv_378d_jerk_v146_signal,
    f39asq_f39_apparel_seasonality_quality_syncxinv_378d_jerk_v147_signal,
    f39asq_f39_apparel_seasonality_quality_syncxinv_378d_jerk_v148_signal,
    f39asq_f39_apparel_seasonality_quality_syncxinv_378d_jerk_v149_signal,
    f39asq_f39_apparel_seasonality_quality_syncxinv_378d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F39_APPAREL_SEASONALITY_QUALITY_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")

    cols = {
        "closeadj": closeadj, "volume": volume,
        "revenue": revenue, "cor": cor, "inventory": inventory,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
    }


    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f39_seasonal_inv_pattern", "_f39_revenue_inv_sync", "_f39_seasonality_quality",)
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
    print(f"OK f39_apparel_seasonality_quality_jerk_001_150_claude: {n_features} features pass")
