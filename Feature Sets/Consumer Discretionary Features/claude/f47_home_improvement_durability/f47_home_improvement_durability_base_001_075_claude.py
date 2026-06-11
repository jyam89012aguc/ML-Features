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
def _f47_revenue_floor(revenue, w):
    return revenue.rolling(w, min_periods=max(1, w // 2)).min() / revenue.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)


def _f47_non_cyclical_share(revenue, w):
    mn = revenue.rolling(w, min_periods=max(1, w // 2)).min()
    mx = revenue.rolling(w, min_periods=max(1, w // 2)).max()
    return mn / mx.replace(0, np.nan)


def _f47_durability_score(revenue, ebitdamargin, w):
    floor = revenue.rolling(w, min_periods=max(1, w // 2)).min() / revenue.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)
    mstable = 1.0 - ebitdamargin.rolling(w, min_periods=max(1, w // 2)).std().fillna(0) / ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan).abs()
    return floor * mstable



def f47hid_f47_home_improvement_durability_floor_21d_raw_base_v001_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_21d_mean_base_v002_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_21d_std_base_v003_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_21d_z_base_v004_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_42d_raw_base_v005_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_42d_mean_base_v006_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 42)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_42d_std_base_v007_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 42)
    result = _std(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_42d_z_base_v008_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 42)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_63d_raw_base_v009_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_63d_mean_base_v010_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_63d_std_base_v011_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_63d_z_base_v012_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_126d_raw_base_v013_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_126d_mean_base_v014_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 126)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_126d_std_base_v015_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 126)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_126d_z_base_v016_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 126)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_189d_raw_base_v017_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_189d_mean_base_v018_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 189)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_189d_std_base_v019_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 189)
    result = _std(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_189d_z_base_v020_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 189)
    result = _z(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_252d_raw_base_v021_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_252d_mean_base_v022_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_252d_std_base_v023_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 252)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_252d_z_base_v024_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_378d_raw_base_v025_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_378d_mean_base_v026_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 378)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_378d_std_base_v027_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 378)
    result = _std(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_378d_z_base_v028_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 378)
    result = _z(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_504d_raw_base_v029_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_504d_mean_base_v030_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 504)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_504d_std_base_v031_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 504)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_504d_z_base_v032_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 504)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_21d_raw_base_v033_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_21d_mean_base_v034_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_21d_std_base_v035_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_21d_z_base_v036_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_42d_raw_base_v037_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_42d_mean_base_v038_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 42)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_42d_std_base_v039_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 42)
    result = _std(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_42d_z_base_v040_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 42)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_63d_raw_base_v041_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_63d_mean_base_v042_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_63d_std_base_v043_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_63d_z_base_v044_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_126d_raw_base_v045_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_126d_mean_base_v046_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 126)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_126d_std_base_v047_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 126)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_126d_z_base_v048_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 126)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_189d_raw_base_v049_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_189d_mean_base_v050_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 189)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_189d_std_base_v051_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 189)
    result = _std(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_189d_z_base_v052_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 189)
    result = _z(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_252d_raw_base_v053_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_252d_mean_base_v054_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_252d_std_base_v055_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 252)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_252d_z_base_v056_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_378d_raw_base_v057_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_378d_mean_base_v058_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 378)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_378d_std_base_v059_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 378)
    result = _std(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_378d_z_base_v060_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 378)
    result = _z(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_504d_raw_base_v061_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_504d_mean_base_v062_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 504)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_504d_std_base_v063_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 504)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_504d_z_base_v064_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 504)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_durab_21d_raw_base_v065_signal(revenue, ebitdamargin, closeadj):
    base = _f47_durability_score(revenue, ebitdamargin, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_durab_21d_mean_base_v066_signal(revenue, ebitdamargin, closeadj):
    base = _f47_durability_score(revenue, ebitdamargin, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_durab_21d_std_base_v067_signal(revenue, ebitdamargin, closeadj):
    base = _f47_durability_score(revenue, ebitdamargin, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_durab_21d_z_base_v068_signal(revenue, ebitdamargin, closeadj):
    base = _f47_durability_score(revenue, ebitdamargin, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_durab_42d_raw_base_v069_signal(revenue, ebitdamargin, closeadj):
    base = _f47_durability_score(revenue, ebitdamargin, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_durab_42d_mean_base_v070_signal(revenue, ebitdamargin, closeadj):
    base = _f47_durability_score(revenue, ebitdamargin, 42)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_durab_42d_std_base_v071_signal(revenue, ebitdamargin, closeadj):
    base = _f47_durability_score(revenue, ebitdamargin, 42)
    result = _std(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_durab_42d_z_base_v072_signal(revenue, ebitdamargin, closeadj):
    base = _f47_durability_score(revenue, ebitdamargin, 42)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_durab_63d_raw_base_v073_signal(revenue, ebitdamargin, closeadj):
    base = _f47_durability_score(revenue, ebitdamargin, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_durab_63d_mean_base_v074_signal(revenue, ebitdamargin, closeadj):
    base = _f47_durability_score(revenue, ebitdamargin, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_durab_63d_std_base_v075_signal(revenue, ebitdamargin, closeadj):
    base = _f47_durability_score(revenue, ebitdamargin, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f47hid_f47_home_improvement_durability_floor_21d_raw_base_v001_signal,
    f47hid_f47_home_improvement_durability_floor_21d_mean_base_v002_signal,
    f47hid_f47_home_improvement_durability_floor_21d_std_base_v003_signal,
    f47hid_f47_home_improvement_durability_floor_21d_z_base_v004_signal,
    f47hid_f47_home_improvement_durability_floor_42d_raw_base_v005_signal,
    f47hid_f47_home_improvement_durability_floor_42d_mean_base_v006_signal,
    f47hid_f47_home_improvement_durability_floor_42d_std_base_v007_signal,
    f47hid_f47_home_improvement_durability_floor_42d_z_base_v008_signal,
    f47hid_f47_home_improvement_durability_floor_63d_raw_base_v009_signal,
    f47hid_f47_home_improvement_durability_floor_63d_mean_base_v010_signal,
    f47hid_f47_home_improvement_durability_floor_63d_std_base_v011_signal,
    f47hid_f47_home_improvement_durability_floor_63d_z_base_v012_signal,
    f47hid_f47_home_improvement_durability_floor_126d_raw_base_v013_signal,
    f47hid_f47_home_improvement_durability_floor_126d_mean_base_v014_signal,
    f47hid_f47_home_improvement_durability_floor_126d_std_base_v015_signal,
    f47hid_f47_home_improvement_durability_floor_126d_z_base_v016_signal,
    f47hid_f47_home_improvement_durability_floor_189d_raw_base_v017_signal,
    f47hid_f47_home_improvement_durability_floor_189d_mean_base_v018_signal,
    f47hid_f47_home_improvement_durability_floor_189d_std_base_v019_signal,
    f47hid_f47_home_improvement_durability_floor_189d_z_base_v020_signal,
    f47hid_f47_home_improvement_durability_floor_252d_raw_base_v021_signal,
    f47hid_f47_home_improvement_durability_floor_252d_mean_base_v022_signal,
    f47hid_f47_home_improvement_durability_floor_252d_std_base_v023_signal,
    f47hid_f47_home_improvement_durability_floor_252d_z_base_v024_signal,
    f47hid_f47_home_improvement_durability_floor_378d_raw_base_v025_signal,
    f47hid_f47_home_improvement_durability_floor_378d_mean_base_v026_signal,
    f47hid_f47_home_improvement_durability_floor_378d_std_base_v027_signal,
    f47hid_f47_home_improvement_durability_floor_378d_z_base_v028_signal,
    f47hid_f47_home_improvement_durability_floor_504d_raw_base_v029_signal,
    f47hid_f47_home_improvement_durability_floor_504d_mean_base_v030_signal,
    f47hid_f47_home_improvement_durability_floor_504d_std_base_v031_signal,
    f47hid_f47_home_improvement_durability_floor_504d_z_base_v032_signal,
    f47hid_f47_home_improvement_durability_ncshare_21d_raw_base_v033_signal,
    f47hid_f47_home_improvement_durability_ncshare_21d_mean_base_v034_signal,
    f47hid_f47_home_improvement_durability_ncshare_21d_std_base_v035_signal,
    f47hid_f47_home_improvement_durability_ncshare_21d_z_base_v036_signal,
    f47hid_f47_home_improvement_durability_ncshare_42d_raw_base_v037_signal,
    f47hid_f47_home_improvement_durability_ncshare_42d_mean_base_v038_signal,
    f47hid_f47_home_improvement_durability_ncshare_42d_std_base_v039_signal,
    f47hid_f47_home_improvement_durability_ncshare_42d_z_base_v040_signal,
    f47hid_f47_home_improvement_durability_ncshare_63d_raw_base_v041_signal,
    f47hid_f47_home_improvement_durability_ncshare_63d_mean_base_v042_signal,
    f47hid_f47_home_improvement_durability_ncshare_63d_std_base_v043_signal,
    f47hid_f47_home_improvement_durability_ncshare_63d_z_base_v044_signal,
    f47hid_f47_home_improvement_durability_ncshare_126d_raw_base_v045_signal,
    f47hid_f47_home_improvement_durability_ncshare_126d_mean_base_v046_signal,
    f47hid_f47_home_improvement_durability_ncshare_126d_std_base_v047_signal,
    f47hid_f47_home_improvement_durability_ncshare_126d_z_base_v048_signal,
    f47hid_f47_home_improvement_durability_ncshare_189d_raw_base_v049_signal,
    f47hid_f47_home_improvement_durability_ncshare_189d_mean_base_v050_signal,
    f47hid_f47_home_improvement_durability_ncshare_189d_std_base_v051_signal,
    f47hid_f47_home_improvement_durability_ncshare_189d_z_base_v052_signal,
    f47hid_f47_home_improvement_durability_ncshare_252d_raw_base_v053_signal,
    f47hid_f47_home_improvement_durability_ncshare_252d_mean_base_v054_signal,
    f47hid_f47_home_improvement_durability_ncshare_252d_std_base_v055_signal,
    f47hid_f47_home_improvement_durability_ncshare_252d_z_base_v056_signal,
    f47hid_f47_home_improvement_durability_ncshare_378d_raw_base_v057_signal,
    f47hid_f47_home_improvement_durability_ncshare_378d_mean_base_v058_signal,
    f47hid_f47_home_improvement_durability_ncshare_378d_std_base_v059_signal,
    f47hid_f47_home_improvement_durability_ncshare_378d_z_base_v060_signal,
    f47hid_f47_home_improvement_durability_ncshare_504d_raw_base_v061_signal,
    f47hid_f47_home_improvement_durability_ncshare_504d_mean_base_v062_signal,
    f47hid_f47_home_improvement_durability_ncshare_504d_std_base_v063_signal,
    f47hid_f47_home_improvement_durability_ncshare_504d_z_base_v064_signal,
    f47hid_f47_home_improvement_durability_durab_21d_raw_base_v065_signal,
    f47hid_f47_home_improvement_durability_durab_21d_mean_base_v066_signal,
    f47hid_f47_home_improvement_durability_durab_21d_std_base_v067_signal,
    f47hid_f47_home_improvement_durability_durab_21d_z_base_v068_signal,
    f47hid_f47_home_improvement_durability_durab_42d_raw_base_v069_signal,
    f47hid_f47_home_improvement_durability_durab_42d_mean_base_v070_signal,
    f47hid_f47_home_improvement_durability_durab_42d_std_base_v071_signal,
    f47hid_f47_home_improvement_durability_durab_42d_z_base_v072_signal,
    f47hid_f47_home_improvement_durability_durab_63d_raw_base_v073_signal,
    f47hid_f47_home_improvement_durability_durab_63d_mean_base_v074_signal,
    f47hid_f47_home_improvement_durability_durab_63d_std_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F47_HOME_IMPROVEMENT_DURABILITY_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {"closeadj": closeadj, "ebitdamargin": ebitdamargin, "revenue": revenue}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f47_revenue_floor", "_f47_non_cyclical_share", "_f47_durability_score")
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
    print(f"OK f47_home_improvement_durability_base_001_075_claude: {n_features} features pass")
