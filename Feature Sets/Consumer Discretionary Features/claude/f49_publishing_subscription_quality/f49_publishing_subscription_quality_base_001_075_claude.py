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



# ===== folder domain primitives =====
def _f49_deferred_rev_quality(deferredrev, revenue):
    return deferredrev / revenue.replace(0, np.nan)


def _f49_subscription_growth(deferredrev, w):
    return deferredrev.pct_change(periods=w)


def _f49_subscription_durability(deferredrev, revenue, w):
    ratio = deferredrev / revenue.replace(0, np.nan)
    mean = ratio.rolling(w, min_periods=max(1, w // 2)).mean()
    std = ratio.rolling(w, min_periods=max(1, w // 2)).std()
    return mean / std.replace(0, np.nan)



def f49psq_f49_publishing_subscription_quality_drq_21d_raw_base_v001_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_21d_mean_base_v002_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_21d_std_base_v003_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_21d_z_base_v004_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_42d_raw_base_v005_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_42d_mean_base_v006_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 42)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_42d_std_base_v007_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 42)
    result = _std(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_42d_z_base_v008_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 42)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_63d_raw_base_v009_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_63d_mean_base_v010_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_63d_std_base_v011_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_63d_z_base_v012_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_126d_raw_base_v013_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_126d_mean_base_v014_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 126)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_126d_std_base_v015_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 126)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_126d_z_base_v016_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 126)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_189d_raw_base_v017_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_189d_mean_base_v018_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 189)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_189d_std_base_v019_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 189)
    result = _std(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_189d_z_base_v020_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 189)
    result = _z(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_252d_raw_base_v021_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_252d_mean_base_v022_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_252d_std_base_v023_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 252)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_252d_z_base_v024_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_378d_raw_base_v025_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_378d_mean_base_v026_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 378)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_378d_std_base_v027_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 378)
    result = _std(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_378d_z_base_v028_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 378)
    result = _z(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_504d_raw_base_v029_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_504d_mean_base_v030_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 504)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_504d_std_base_v031_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 504)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_504d_z_base_v032_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 504)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_21d_raw_base_v033_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_21d_mean_base_v034_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_21d_std_base_v035_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_21d_z_base_v036_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_42d_raw_base_v037_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_42d_mean_base_v038_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 42)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_42d_std_base_v039_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 42)
    result = _std(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_42d_z_base_v040_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 42)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_63d_raw_base_v041_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_63d_mean_base_v042_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_63d_std_base_v043_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_63d_z_base_v044_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_126d_raw_base_v045_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_126d_mean_base_v046_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 126)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_126d_std_base_v047_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 126)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_126d_z_base_v048_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 126)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_189d_raw_base_v049_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_189d_mean_base_v050_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 189)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_189d_std_base_v051_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 189)
    result = _std(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_189d_z_base_v052_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 189)
    result = _z(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_252d_raw_base_v053_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_252d_mean_base_v054_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_252d_std_base_v055_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 252)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_252d_z_base_v056_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_378d_raw_base_v057_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_378d_mean_base_v058_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 378)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_378d_std_base_v059_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 378)
    result = _std(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_378d_z_base_v060_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 378)
    result = _z(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_504d_raw_base_v061_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_504d_mean_base_v062_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 504)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_504d_std_base_v063_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 504)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_504d_z_base_v064_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 504)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subdur_21d_raw_base_v065_signal(deferredrev, revenue, closeadj):
    base = _f49_subscription_durability(deferredrev, revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subdur_21d_mean_base_v066_signal(deferredrev, revenue, closeadj):
    base = _f49_subscription_durability(deferredrev, revenue, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subdur_21d_std_base_v067_signal(deferredrev, revenue, closeadj):
    base = _f49_subscription_durability(deferredrev, revenue, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subdur_21d_z_base_v068_signal(deferredrev, revenue, closeadj):
    base = _f49_subscription_durability(deferredrev, revenue, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subdur_42d_raw_base_v069_signal(deferredrev, revenue, closeadj):
    base = _f49_subscription_durability(deferredrev, revenue, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subdur_42d_mean_base_v070_signal(deferredrev, revenue, closeadj):
    base = _f49_subscription_durability(deferredrev, revenue, 42)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subdur_42d_std_base_v071_signal(deferredrev, revenue, closeadj):
    base = _f49_subscription_durability(deferredrev, revenue, 42)
    result = _std(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subdur_42d_z_base_v072_signal(deferredrev, revenue, closeadj):
    base = _f49_subscription_durability(deferredrev, revenue, 42)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subdur_63d_raw_base_v073_signal(deferredrev, revenue, closeadj):
    base = _f49_subscription_durability(deferredrev, revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subdur_63d_mean_base_v074_signal(deferredrev, revenue, closeadj):
    base = _f49_subscription_durability(deferredrev, revenue, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subdur_63d_std_base_v075_signal(deferredrev, revenue, closeadj):
    base = _f49_subscription_durability(deferredrev, revenue, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f49psq_f49_publishing_subscription_quality_drq_21d_raw_base_v001_signal,
    f49psq_f49_publishing_subscription_quality_drq_21d_mean_base_v002_signal,
    f49psq_f49_publishing_subscription_quality_drq_21d_std_base_v003_signal,
    f49psq_f49_publishing_subscription_quality_drq_21d_z_base_v004_signal,
    f49psq_f49_publishing_subscription_quality_drq_42d_raw_base_v005_signal,
    f49psq_f49_publishing_subscription_quality_drq_42d_mean_base_v006_signal,
    f49psq_f49_publishing_subscription_quality_drq_42d_std_base_v007_signal,
    f49psq_f49_publishing_subscription_quality_drq_42d_z_base_v008_signal,
    f49psq_f49_publishing_subscription_quality_drq_63d_raw_base_v009_signal,
    f49psq_f49_publishing_subscription_quality_drq_63d_mean_base_v010_signal,
    f49psq_f49_publishing_subscription_quality_drq_63d_std_base_v011_signal,
    f49psq_f49_publishing_subscription_quality_drq_63d_z_base_v012_signal,
    f49psq_f49_publishing_subscription_quality_drq_126d_raw_base_v013_signal,
    f49psq_f49_publishing_subscription_quality_drq_126d_mean_base_v014_signal,
    f49psq_f49_publishing_subscription_quality_drq_126d_std_base_v015_signal,
    f49psq_f49_publishing_subscription_quality_drq_126d_z_base_v016_signal,
    f49psq_f49_publishing_subscription_quality_drq_189d_raw_base_v017_signal,
    f49psq_f49_publishing_subscription_quality_drq_189d_mean_base_v018_signal,
    f49psq_f49_publishing_subscription_quality_drq_189d_std_base_v019_signal,
    f49psq_f49_publishing_subscription_quality_drq_189d_z_base_v020_signal,
    f49psq_f49_publishing_subscription_quality_drq_252d_raw_base_v021_signal,
    f49psq_f49_publishing_subscription_quality_drq_252d_mean_base_v022_signal,
    f49psq_f49_publishing_subscription_quality_drq_252d_std_base_v023_signal,
    f49psq_f49_publishing_subscription_quality_drq_252d_z_base_v024_signal,
    f49psq_f49_publishing_subscription_quality_drq_378d_raw_base_v025_signal,
    f49psq_f49_publishing_subscription_quality_drq_378d_mean_base_v026_signal,
    f49psq_f49_publishing_subscription_quality_drq_378d_std_base_v027_signal,
    f49psq_f49_publishing_subscription_quality_drq_378d_z_base_v028_signal,
    f49psq_f49_publishing_subscription_quality_drq_504d_raw_base_v029_signal,
    f49psq_f49_publishing_subscription_quality_drq_504d_mean_base_v030_signal,
    f49psq_f49_publishing_subscription_quality_drq_504d_std_base_v031_signal,
    f49psq_f49_publishing_subscription_quality_drq_504d_z_base_v032_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_21d_raw_base_v033_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_21d_mean_base_v034_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_21d_std_base_v035_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_21d_z_base_v036_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_42d_raw_base_v037_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_42d_mean_base_v038_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_42d_std_base_v039_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_42d_z_base_v040_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_63d_raw_base_v041_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_63d_mean_base_v042_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_63d_std_base_v043_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_63d_z_base_v044_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_126d_raw_base_v045_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_126d_mean_base_v046_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_126d_std_base_v047_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_126d_z_base_v048_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_189d_raw_base_v049_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_189d_mean_base_v050_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_189d_std_base_v051_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_189d_z_base_v052_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_252d_raw_base_v053_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_252d_mean_base_v054_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_252d_std_base_v055_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_252d_z_base_v056_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_378d_raw_base_v057_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_378d_mean_base_v058_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_378d_std_base_v059_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_378d_z_base_v060_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_504d_raw_base_v061_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_504d_mean_base_v062_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_504d_std_base_v063_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_504d_z_base_v064_signal,
    f49psq_f49_publishing_subscription_quality_subdur_21d_raw_base_v065_signal,
    f49psq_f49_publishing_subscription_quality_subdur_21d_mean_base_v066_signal,
    f49psq_f49_publishing_subscription_quality_subdur_21d_std_base_v067_signal,
    f49psq_f49_publishing_subscription_quality_subdur_21d_z_base_v068_signal,
    f49psq_f49_publishing_subscription_quality_subdur_42d_raw_base_v069_signal,
    f49psq_f49_publishing_subscription_quality_subdur_42d_mean_base_v070_signal,
    f49psq_f49_publishing_subscription_quality_subdur_42d_std_base_v071_signal,
    f49psq_f49_publishing_subscription_quality_subdur_42d_z_base_v072_signal,
    f49psq_f49_publishing_subscription_quality_subdur_63d_raw_base_v073_signal,
    f49psq_f49_publishing_subscription_quality_subdur_63d_mean_base_v074_signal,
    f49psq_f49_publishing_subscription_quality_subdur_63d_std_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F49_PUBLISHING_SUBSCRIPTION_QUALITY_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")

    cols = {"closeadj": closeadj, "deferredrev": deferredrev, "revenue": revenue}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f49_deferred_rev_quality", "_f49_subscription_growth", "_f49_subscription_durability")
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
    print(f"OK f49_publishing_subscription_quality_base_001_075_claude: {n_features} features pass")
