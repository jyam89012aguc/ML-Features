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
    return s.ewm(span=w, min_periods=max(1, w // 2)).mean()

# ===== folder domain primitives =====
def _f03_small_base_growth(revenue, w):
    base = revenue.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)
    g = revenue.pct_change(w)
    return g / (1.0 + np.log1p(base / 1e9))


def _f03_revenue_acceleration(revenue, w):
    g1 = revenue.pct_change(w)
    g2 = revenue.pct_change(2 * w)
    return g1 - g2 / 2.0


def _f03_growth_intensity_normalized(revenue, assets, w):
    g = revenue.pct_change(w)
    intens = revenue / assets.replace(0, np.nan)
    return g * intens
def f03nbg_f03_niche_brand_growth_smallbase_21d_base_v001_signal(revenue, closeadj):
    base = _f03_small_base_growth(revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_smallbase_42d_base_v002_signal(revenue, closeadj):
    base = _f03_small_base_growth(revenue, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_smallbase_63d_base_v003_signal(revenue, closeadj):
    base = _f03_small_base_growth(revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_smallbase_126d_base_v004_signal(revenue, closeadj):
    base = _f03_small_base_growth(revenue, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_smallbase_189d_base_v005_signal(revenue, closeadj):
    base = _f03_small_base_growth(revenue, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_smallbase_252d_base_v006_signal(revenue, closeadj):
    base = _f03_small_base_growth(revenue, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_smallbase_378d_base_v007_signal(revenue, closeadj):
    base = _f03_small_base_growth(revenue, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_smallbase_504d_base_v008_signal(revenue, closeadj):
    base = _f03_small_base_growth(revenue, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_smallbase_5d_base_v009_signal(revenue, closeadj):
    base = _f03_small_base_growth(revenue, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_smallbase_10d_base_v010_signal(revenue, closeadj):
    base = _f03_small_base_growth(revenue, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_smallbase_14d_base_v011_signal(revenue, closeadj):
    base = _f03_small_base_growth(revenue, 14)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_smallbase_30d_base_v012_signal(revenue, closeadj):
    base = _f03_small_base_growth(revenue, 30)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_smallbase_84d_base_v013_signal(revenue, closeadj):
    base = _f03_small_base_growth(revenue, 84)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_smallbase_168d_base_v014_signal(revenue, closeadj):
    base = _f03_small_base_growth(revenue, 168)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_smallbase_336d_base_v015_signal(revenue, closeadj):
    base = _f03_small_base_growth(revenue, 336)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_smallbase_7d_base_v016_signal(revenue, closeadj):
    base = _f03_small_base_growth(revenue, 7)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_smallbase_35d_base_v017_signal(revenue, closeadj):
    base = _f03_small_base_growth(revenue, 35)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_smallbase_70d_base_v018_signal(revenue, closeadj):
    base = _f03_small_base_growth(revenue, 70)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_smallbase_100d_base_v019_signal(revenue, closeadj):
    base = _f03_small_base_growth(revenue, 100)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_smallbase_210d_base_v020_signal(revenue, closeadj):
    base = _f03_small_base_growth(revenue, 210)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_smallbase_280d_base_v021_signal(revenue, closeadj):
    base = _f03_small_base_growth(revenue, 280)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_smallbase_350d_base_v022_signal(revenue, closeadj):
    base = _f03_small_base_growth(revenue, 350)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_smallbase_420d_base_v023_signal(revenue, closeadj):
    base = _f03_small_base_growth(revenue, 420)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_smallbase_490d_base_v024_signal(revenue, closeadj):
    base = _f03_small_base_growth(revenue, 490)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_smallbase_11d_base_v025_signal(revenue, closeadj):
    base = _f03_small_base_growth(revenue, 11)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_revaccel_21d_base_v026_signal(revenue, closeadj):
    base = _f03_revenue_acceleration(revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_revaccel_42d_base_v027_signal(revenue, closeadj):
    base = _f03_revenue_acceleration(revenue, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_revaccel_63d_base_v028_signal(revenue, closeadj):
    base = _f03_revenue_acceleration(revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_revaccel_126d_base_v029_signal(revenue, closeadj):
    base = _f03_revenue_acceleration(revenue, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_revaccel_189d_base_v030_signal(revenue, closeadj):
    base = _f03_revenue_acceleration(revenue, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_revaccel_252d_base_v031_signal(revenue, closeadj):
    base = _f03_revenue_acceleration(revenue, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_revaccel_5d_base_v032_signal(revenue, closeadj):
    base = _f03_revenue_acceleration(revenue, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_revaccel_10d_base_v033_signal(revenue, closeadj):
    base = _f03_revenue_acceleration(revenue, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_revaccel_14d_base_v034_signal(revenue, closeadj):
    base = _f03_revenue_acceleration(revenue, 14)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_revaccel_30d_base_v035_signal(revenue, closeadj):
    base = _f03_revenue_acceleration(revenue, 30)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_revaccel_84d_base_v036_signal(revenue, closeadj):
    base = _f03_revenue_acceleration(revenue, 84)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_revaccel_168d_base_v037_signal(revenue, closeadj):
    base = _f03_revenue_acceleration(revenue, 168)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_revaccel_7d_base_v038_signal(revenue, closeadj):
    base = _f03_revenue_acceleration(revenue, 7)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_revaccel_35d_base_v039_signal(revenue, closeadj):
    base = _f03_revenue_acceleration(revenue, 35)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_revaccel_70d_base_v040_signal(revenue, closeadj):
    base = _f03_revenue_acceleration(revenue, 70)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_revaccel_100d_base_v041_signal(revenue, closeadj):
    base = _f03_revenue_acceleration(revenue, 100)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_revaccel_210d_base_v042_signal(revenue, closeadj):
    base = _f03_revenue_acceleration(revenue, 210)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_revaccel_280d_base_v043_signal(revenue, closeadj):
    base = _f03_revenue_acceleration(revenue, 280)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_revaccel_50d_base_v044_signal(revenue, closeadj):
    base = _f03_revenue_acceleration(revenue, 50)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_revaccel_150d_base_v045_signal(revenue, closeadj):
    base = _f03_revenue_acceleration(revenue, 150)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_revaccel_200d_base_v046_signal(revenue, closeadj):
    base = _f03_revenue_acceleration(revenue, 200)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_revaccel_250d_base_v047_signal(revenue, closeadj):
    base = _f03_revenue_acceleration(revenue, 250)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_revaccel_90d_base_v048_signal(revenue, closeadj):
    base = _f03_revenue_acceleration(revenue, 90)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_revaccel_120d_base_v049_signal(revenue, closeadj):
    base = _f03_revenue_acceleration(revenue, 120)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_revaccel_75d_base_v050_signal(revenue, closeadj):
    base = _f03_revenue_acceleration(revenue, 75)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_growthintens_21d_base_v051_signal(revenue, assets, closeadj):
    base = _f03_growth_intensity_normalized(revenue, assets, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_growthintens_42d_base_v052_signal(revenue, assets, closeadj):
    base = _f03_growth_intensity_normalized(revenue, assets, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_growthintens_63d_base_v053_signal(revenue, assets, closeadj):
    base = _f03_growth_intensity_normalized(revenue, assets, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_growthintens_126d_base_v054_signal(revenue, assets, closeadj):
    base = _f03_growth_intensity_normalized(revenue, assets, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_growthintens_189d_base_v055_signal(revenue, assets, closeadj):
    base = _f03_growth_intensity_normalized(revenue, assets, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_growthintens_252d_base_v056_signal(revenue, assets, closeadj):
    base = _f03_growth_intensity_normalized(revenue, assets, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_growthintens_378d_base_v057_signal(revenue, assets, closeadj):
    base = _f03_growth_intensity_normalized(revenue, assets, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_growthintens_504d_base_v058_signal(revenue, assets, closeadj):
    base = _f03_growth_intensity_normalized(revenue, assets, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_growthintens_5d_base_v059_signal(revenue, assets, closeadj):
    base = _f03_growth_intensity_normalized(revenue, assets, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_growthintens_10d_base_v060_signal(revenue, assets, closeadj):
    base = _f03_growth_intensity_normalized(revenue, assets, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_growthintens_14d_base_v061_signal(revenue, assets, closeadj):
    base = _f03_growth_intensity_normalized(revenue, assets, 14)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_growthintens_30d_base_v062_signal(revenue, assets, closeadj):
    base = _f03_growth_intensity_normalized(revenue, assets, 30)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_growthintens_84d_base_v063_signal(revenue, assets, closeadj):
    base = _f03_growth_intensity_normalized(revenue, assets, 84)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_growthintens_168d_base_v064_signal(revenue, assets, closeadj):
    base = _f03_growth_intensity_normalized(revenue, assets, 168)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_growthintens_7d_base_v065_signal(revenue, assets, closeadj):
    base = _f03_growth_intensity_normalized(revenue, assets, 7)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_growthintens_35d_base_v066_signal(revenue, assets, closeadj):
    base = _f03_growth_intensity_normalized(revenue, assets, 35)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_growthintens_70d_base_v067_signal(revenue, assets, closeadj):
    base = _f03_growth_intensity_normalized(revenue, assets, 70)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_growthintens_100d_base_v068_signal(revenue, assets, closeadj):
    base = _f03_growth_intensity_normalized(revenue, assets, 100)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_growthintens_210d_base_v069_signal(revenue, assets, closeadj):
    base = _f03_growth_intensity_normalized(revenue, assets, 210)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_growthintens_280d_base_v070_signal(revenue, assets, closeadj):
    base = _f03_growth_intensity_normalized(revenue, assets, 280)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_growthintens_50d_base_v071_signal(revenue, assets, closeadj):
    base = _f03_growth_intensity_normalized(revenue, assets, 50)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_growthintens_150d_base_v072_signal(revenue, assets, closeadj):
    base = _f03_growth_intensity_normalized(revenue, assets, 150)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_growthintens_200d_base_v073_signal(revenue, assets, closeadj):
    base = _f03_growth_intensity_normalized(revenue, assets, 200)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_growthintens_250d_base_v074_signal(revenue, assets, closeadj):
    base = _f03_growth_intensity_normalized(revenue, assets, 250)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f03nbg_f03_niche_brand_growth_growthintens_90d_base_v075_signal(revenue, assets, closeadj):
    base = _f03_growth_intensity_normalized(revenue, assets, 90)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES = [
    f03nbg_f03_niche_brand_growth_smallbase_21d_base_v001_signal,
    f03nbg_f03_niche_brand_growth_smallbase_42d_base_v002_signal,
    f03nbg_f03_niche_brand_growth_smallbase_63d_base_v003_signal,
    f03nbg_f03_niche_brand_growth_smallbase_126d_base_v004_signal,
    f03nbg_f03_niche_brand_growth_smallbase_189d_base_v005_signal,
    f03nbg_f03_niche_brand_growth_smallbase_252d_base_v006_signal,
    f03nbg_f03_niche_brand_growth_smallbase_378d_base_v007_signal,
    f03nbg_f03_niche_brand_growth_smallbase_504d_base_v008_signal,
    f03nbg_f03_niche_brand_growth_smallbase_5d_base_v009_signal,
    f03nbg_f03_niche_brand_growth_smallbase_10d_base_v010_signal,
    f03nbg_f03_niche_brand_growth_smallbase_14d_base_v011_signal,
    f03nbg_f03_niche_brand_growth_smallbase_30d_base_v012_signal,
    f03nbg_f03_niche_brand_growth_smallbase_84d_base_v013_signal,
    f03nbg_f03_niche_brand_growth_smallbase_168d_base_v014_signal,
    f03nbg_f03_niche_brand_growth_smallbase_336d_base_v015_signal,
    f03nbg_f03_niche_brand_growth_smallbase_7d_base_v016_signal,
    f03nbg_f03_niche_brand_growth_smallbase_35d_base_v017_signal,
    f03nbg_f03_niche_brand_growth_smallbase_70d_base_v018_signal,
    f03nbg_f03_niche_brand_growth_smallbase_100d_base_v019_signal,
    f03nbg_f03_niche_brand_growth_smallbase_210d_base_v020_signal,
    f03nbg_f03_niche_brand_growth_smallbase_280d_base_v021_signal,
    f03nbg_f03_niche_brand_growth_smallbase_350d_base_v022_signal,
    f03nbg_f03_niche_brand_growth_smallbase_420d_base_v023_signal,
    f03nbg_f03_niche_brand_growth_smallbase_490d_base_v024_signal,
    f03nbg_f03_niche_brand_growth_smallbase_11d_base_v025_signal,
    f03nbg_f03_niche_brand_growth_revaccel_21d_base_v026_signal,
    f03nbg_f03_niche_brand_growth_revaccel_42d_base_v027_signal,
    f03nbg_f03_niche_brand_growth_revaccel_63d_base_v028_signal,
    f03nbg_f03_niche_brand_growth_revaccel_126d_base_v029_signal,
    f03nbg_f03_niche_brand_growth_revaccel_189d_base_v030_signal,
    f03nbg_f03_niche_brand_growth_revaccel_252d_base_v031_signal,
    f03nbg_f03_niche_brand_growth_revaccel_5d_base_v032_signal,
    f03nbg_f03_niche_brand_growth_revaccel_10d_base_v033_signal,
    f03nbg_f03_niche_brand_growth_revaccel_14d_base_v034_signal,
    f03nbg_f03_niche_brand_growth_revaccel_30d_base_v035_signal,
    f03nbg_f03_niche_brand_growth_revaccel_84d_base_v036_signal,
    f03nbg_f03_niche_brand_growth_revaccel_168d_base_v037_signal,
    f03nbg_f03_niche_brand_growth_revaccel_7d_base_v038_signal,
    f03nbg_f03_niche_brand_growth_revaccel_35d_base_v039_signal,
    f03nbg_f03_niche_brand_growth_revaccel_70d_base_v040_signal,
    f03nbg_f03_niche_brand_growth_revaccel_100d_base_v041_signal,
    f03nbg_f03_niche_brand_growth_revaccel_210d_base_v042_signal,
    f03nbg_f03_niche_brand_growth_revaccel_280d_base_v043_signal,
    f03nbg_f03_niche_brand_growth_revaccel_50d_base_v044_signal,
    f03nbg_f03_niche_brand_growth_revaccel_150d_base_v045_signal,
    f03nbg_f03_niche_brand_growth_revaccel_200d_base_v046_signal,
    f03nbg_f03_niche_brand_growth_revaccel_250d_base_v047_signal,
    f03nbg_f03_niche_brand_growth_revaccel_90d_base_v048_signal,
    f03nbg_f03_niche_brand_growth_revaccel_120d_base_v049_signal,
    f03nbg_f03_niche_brand_growth_revaccel_75d_base_v050_signal,
    f03nbg_f03_niche_brand_growth_growthintens_21d_base_v051_signal,
    f03nbg_f03_niche_brand_growth_growthintens_42d_base_v052_signal,
    f03nbg_f03_niche_brand_growth_growthintens_63d_base_v053_signal,
    f03nbg_f03_niche_brand_growth_growthintens_126d_base_v054_signal,
    f03nbg_f03_niche_brand_growth_growthintens_189d_base_v055_signal,
    f03nbg_f03_niche_brand_growth_growthintens_252d_base_v056_signal,
    f03nbg_f03_niche_brand_growth_growthintens_378d_base_v057_signal,
    f03nbg_f03_niche_brand_growth_growthintens_504d_base_v058_signal,
    f03nbg_f03_niche_brand_growth_growthintens_5d_base_v059_signal,
    f03nbg_f03_niche_brand_growth_growthintens_10d_base_v060_signal,
    f03nbg_f03_niche_brand_growth_growthintens_14d_base_v061_signal,
    f03nbg_f03_niche_brand_growth_growthintens_30d_base_v062_signal,
    f03nbg_f03_niche_brand_growth_growthintens_84d_base_v063_signal,
    f03nbg_f03_niche_brand_growth_growthintens_168d_base_v064_signal,
    f03nbg_f03_niche_brand_growth_growthintens_7d_base_v065_signal,
    f03nbg_f03_niche_brand_growth_growthintens_35d_base_v066_signal,
    f03nbg_f03_niche_brand_growth_growthintens_70d_base_v067_signal,
    f03nbg_f03_niche_brand_growth_growthintens_100d_base_v068_signal,
    f03nbg_f03_niche_brand_growth_growthintens_210d_base_v069_signal,
    f03nbg_f03_niche_brand_growth_growthintens_280d_base_v070_signal,
    f03nbg_f03_niche_brand_growth_growthintens_50d_base_v071_signal,
    f03nbg_f03_niche_brand_growth_growthintens_150d_base_v072_signal,
    f03nbg_f03_niche_brand_growth_growthintens_200d_base_v073_signal,
    f03nbg_f03_niche_brand_growth_growthintens_250d_base_v074_signal,
    f03nbg_f03_niche_brand_growth_growthintens_90d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F03_NICHE_BRAND_GROWTH_REGISTRY_001_075 = REGISTRY


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
    domain_primitives = ("_f03_small_base_growth", "_f03_revenue_acceleration", "_f03_growth_intensity_normalized")
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
    print(f"OK f03_niche_brand_growth_base_001_075_claude: {n_features} features pass")
