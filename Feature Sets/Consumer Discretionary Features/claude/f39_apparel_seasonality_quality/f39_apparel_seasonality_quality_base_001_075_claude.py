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


def f39asq_f39_apparel_seasonality_quality_seasinv_5d_base_v001_signal(inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 5)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinv_10d_base_v002_signal(inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 10)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinv_21d_base_v003_signal(inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 21)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinv_42d_base_v004_signal(inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 42)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinv_63d_base_v005_signal(inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 63)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinv_126d_base_v006_signal(inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 126)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinv_189d_base_v007_signal(inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 189)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinv_252d_base_v008_signal(inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 252)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinv_378d_base_v009_signal(inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 378)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinv_504d_base_v010_signal(inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 504)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsync_21d_base_v011_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 21)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsync_42d_base_v012_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 42)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsync_63d_base_v013_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 63)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsync_126d_base_v014_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 126)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsync_189d_base_v015_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 189)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsync_252d_base_v016_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 252)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsync_378d_base_v017_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 378)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsync_504d_base_v018_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 504)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsync_100d_base_v019_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 100)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsync_150d_base_v020_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 150)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqual_21d_base_v021_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 21)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqual_42d_base_v022_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 42)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqual_63d_base_v023_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 63)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqual_126d_base_v024_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 126)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqual_189d_base_v025_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 189)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqual_252d_base_v026_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 252)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqual_378d_base_v027_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 378)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqual_504d_base_v028_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 504)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqual_100d_base_v029_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 100)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqual_150d_base_v030_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 150)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvsq_21d_base_v031_signal(inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 21)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvsq_63d_base_v032_signal(inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 63)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvsq_126d_base_v033_signal(inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 126)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvsq_189d_base_v034_signal(inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 189)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvsq_252d_base_v035_signal(inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 252)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvsq_504d_base_v036_signal(inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 504)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsyncz_63d_base_v037_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 63)
    result = _z(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsyncz_126d_base_v038_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 63)
    result = _z(d, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsyncz_189d_base_v039_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 63)
    result = _z(d, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsyncz_252d_base_v040_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 63)
    result = _z(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsyncz_378d_base_v041_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 63)
    result = _z(d, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsyncz_504d_base_v042_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 63)
    result = _z(d, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqualema_21d_base_v043_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 63)
    result = _ema(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqualema_63d_base_v044_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 63)
    result = _ema(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqualema_126d_base_v045_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 63)
    result = _ema(d, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqualema_189d_base_v046_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 63)
    result = _ema(d, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqualema_252d_base_v047_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 63)
    result = _ema(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqualema_504d_base_v048_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 63)
    result = _ema(d, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrev_21d_base_v049_signal(revenue, inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 21)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrev_63d_base_v050_signal(revenue, inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 63)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrev_126d_base_v051_signal(revenue, inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 126)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrev_189d_base_v052_signal(revenue, inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 189)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrev_252d_base_v053_signal(revenue, inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 252)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrev_504d_base_v054_signal(revenue, inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 504)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsyncxinv_21d_base_v055_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 21)
    result = d * (inventory / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsyncxinv_63d_base_v056_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 63)
    result = d * (inventory / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsyncxinv_126d_base_v057_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 126)
    result = d * (inventory / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsyncxinv_189d_base_v058_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 189)
    result = d * (inventory / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsyncxinv_252d_base_v059_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 252)
    result = d * (inventory / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsyncxinv_504d_base_v060_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 504)
    result = d * (inventory / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqualchg_21d_base_v061_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 63)
    result = d.diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqualchg_63d_base_v062_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 63)
    result = d.diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqualchg_126d_base_v063_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 63)
    result = d.diff(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqualchg_189d_base_v064_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 63)
    result = d.diff(189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqualchg_252d_base_v065_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 63)
    result = d.diff(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqualchg_504d_base_v066_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 63)
    result = d.diff(504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvstd_63d_base_v067_signal(inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 63)
    result = _std(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvstd_252d_base_v068_signal(inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 63)
    result = _std(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsyncstd_252d_base_v069_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 63)
    result = _std(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqualstd_252d_base_v070_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 63)
    result = _std(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvmean_189d_base_v071_signal(inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 63)
    result = _mean(d, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsyncmean_252d_base_v072_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 63)
    result = _mean(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqualmean_252d_base_v073_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 63)
    result = _mean(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvabs_252d_base_v074_signal(inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 63)
    result = d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsyncema_252d_base_v075_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 63)
    result = _ema(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f39asq_f39_apparel_seasonality_quality_seasinv_5d_base_v001_signal,
    f39asq_f39_apparel_seasonality_quality_seasinv_10d_base_v002_signal,
    f39asq_f39_apparel_seasonality_quality_seasinv_21d_base_v003_signal,
    f39asq_f39_apparel_seasonality_quality_seasinv_42d_base_v004_signal,
    f39asq_f39_apparel_seasonality_quality_seasinv_63d_base_v005_signal,
    f39asq_f39_apparel_seasonality_quality_seasinv_126d_base_v006_signal,
    f39asq_f39_apparel_seasonality_quality_seasinv_189d_base_v007_signal,
    f39asq_f39_apparel_seasonality_quality_seasinv_252d_base_v008_signal,
    f39asq_f39_apparel_seasonality_quality_seasinv_378d_base_v009_signal,
    f39asq_f39_apparel_seasonality_quality_seasinv_504d_base_v010_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsync_21d_base_v011_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsync_42d_base_v012_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsync_63d_base_v013_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsync_126d_base_v014_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsync_189d_base_v015_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsync_252d_base_v016_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsync_378d_base_v017_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsync_504d_base_v018_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsync_100d_base_v019_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsync_150d_base_v020_signal,
    f39asq_f39_apparel_seasonality_quality_seasqual_21d_base_v021_signal,
    f39asq_f39_apparel_seasonality_quality_seasqual_42d_base_v022_signal,
    f39asq_f39_apparel_seasonality_quality_seasqual_63d_base_v023_signal,
    f39asq_f39_apparel_seasonality_quality_seasqual_126d_base_v024_signal,
    f39asq_f39_apparel_seasonality_quality_seasqual_189d_base_v025_signal,
    f39asq_f39_apparel_seasonality_quality_seasqual_252d_base_v026_signal,
    f39asq_f39_apparel_seasonality_quality_seasqual_378d_base_v027_signal,
    f39asq_f39_apparel_seasonality_quality_seasqual_504d_base_v028_signal,
    f39asq_f39_apparel_seasonality_quality_seasqual_100d_base_v029_signal,
    f39asq_f39_apparel_seasonality_quality_seasqual_150d_base_v030_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvsq_21d_base_v031_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvsq_63d_base_v032_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvsq_126d_base_v033_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvsq_189d_base_v034_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvsq_252d_base_v035_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvsq_504d_base_v036_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsyncz_63d_base_v037_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsyncz_126d_base_v038_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsyncz_189d_base_v039_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsyncz_252d_base_v040_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsyncz_378d_base_v041_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsyncz_504d_base_v042_signal,
    f39asq_f39_apparel_seasonality_quality_seasqualema_21d_base_v043_signal,
    f39asq_f39_apparel_seasonality_quality_seasqualema_63d_base_v044_signal,
    f39asq_f39_apparel_seasonality_quality_seasqualema_126d_base_v045_signal,
    f39asq_f39_apparel_seasonality_quality_seasqualema_189d_base_v046_signal,
    f39asq_f39_apparel_seasonality_quality_seasqualema_252d_base_v047_signal,
    f39asq_f39_apparel_seasonality_quality_seasqualema_504d_base_v048_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrev_21d_base_v049_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrev_63d_base_v050_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrev_126d_base_v051_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrev_189d_base_v052_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrev_252d_base_v053_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrev_504d_base_v054_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsyncxinv_21d_base_v055_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsyncxinv_63d_base_v056_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsyncxinv_126d_base_v057_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsyncxinv_189d_base_v058_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsyncxinv_252d_base_v059_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsyncxinv_504d_base_v060_signal,
    f39asq_f39_apparel_seasonality_quality_seasqualchg_21d_base_v061_signal,
    f39asq_f39_apparel_seasonality_quality_seasqualchg_63d_base_v062_signal,
    f39asq_f39_apparel_seasonality_quality_seasqualchg_126d_base_v063_signal,
    f39asq_f39_apparel_seasonality_quality_seasqualchg_189d_base_v064_signal,
    f39asq_f39_apparel_seasonality_quality_seasqualchg_252d_base_v065_signal,
    f39asq_f39_apparel_seasonality_quality_seasqualchg_504d_base_v066_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvstd_63d_base_v067_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvstd_252d_base_v068_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsyncstd_252d_base_v069_signal,
    f39asq_f39_apparel_seasonality_quality_seasqualstd_252d_base_v070_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvmean_189d_base_v071_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsyncmean_252d_base_v072_signal,
    f39asq_f39_apparel_seasonality_quality_seasqualmean_252d_base_v073_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvabs_252d_base_v074_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsyncema_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F39_APPAREL_SEASONALITY_QUALITY_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f39_apparel_seasonality_quality_001_075_claude: {n_features} features pass")
