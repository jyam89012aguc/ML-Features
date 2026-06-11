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
    return s.ewm(span=w, min_periods=max(1, w // 2)).mean()


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _f41_revenue_per_asset(revenue, ppnenet):
    return revenue / ppnenet.replace(0, np.nan)


def _f41_revpar_growth(revenue, ppnenet, w):
    r = revenue / ppnenet.replace(0, np.nan)
    return r.pct_change(periods=w)


def _f41_asset_utilization(revenue, assets, w):
    r = revenue / assets.replace(0, np.nan)
    return r.rolling(w, min_periods=max(1, w // 2)).mean()


def f41hrp_f41_hospitality_revpar_proxy_rpa_mean_5d_slope_v001_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _mean(r, 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_mean_5d_slope_v002_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _mean(r, 5) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_mean_5d_slope_v003_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _mean(r, 5) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_mean_10d_slope_v004_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _mean(r, 10) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_mean_10d_slope_v005_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _mean(r, 10) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_mean_10d_slope_v006_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _mean(r, 10) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_mean_21d_slope_v007_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _mean(r, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_mean_21d_slope_v008_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _mean(r, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_mean_21d_slope_v009_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _mean(r, 21) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_mean_42d_slope_v010_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _mean(r, 42) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_mean_42d_slope_v011_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _mean(r, 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_mean_42d_slope_v012_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _mean(r, 42) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_mean_63d_slope_v013_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _mean(r, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_mean_63d_slope_v014_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _mean(r, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_mean_63d_slope_v015_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _mean(r, 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_mean_126d_slope_v016_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _mean(r, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_mean_126d_slope_v017_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _mean(r, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_mean_126d_slope_v018_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _mean(r, 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_mean_189d_slope_v019_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _mean(r, 189) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_mean_189d_slope_v020_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _mean(r, 189) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_mean_189d_slope_v021_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _mean(r, 189) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_mean_252d_slope_v022_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _mean(r, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_mean_252d_slope_v023_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _mean(r, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_mean_252d_slope_v024_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _mean(r, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_mean_378d_slope_v025_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _mean(r, 378) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_mean_378d_slope_v026_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _mean(r, 378) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_mean_378d_slope_v027_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _mean(r, 378) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_mean_504d_slope_v028_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _mean(r, 504) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_mean_504d_slope_v029_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _mean(r, 504) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_mean_504d_slope_v030_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _mean(r, 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_ema_5d_slope_v031_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _ema(r, 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_ema_5d_slope_v032_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _ema(r, 5) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_ema_5d_slope_v033_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _ema(r, 5) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_ema_10d_slope_v034_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _ema(r, 10) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_ema_10d_slope_v035_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _ema(r, 10) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_ema_10d_slope_v036_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _ema(r, 10) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_ema_21d_slope_v037_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _ema(r, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_ema_21d_slope_v038_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _ema(r, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_ema_21d_slope_v039_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _ema(r, 21) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_ema_42d_slope_v040_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _ema(r, 42) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_ema_42d_slope_v041_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _ema(r, 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_ema_42d_slope_v042_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _ema(r, 42) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_ema_63d_slope_v043_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _ema(r, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_ema_63d_slope_v044_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _ema(r, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_ema_63d_slope_v045_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _ema(r, 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_ema_126d_slope_v046_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _ema(r, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_ema_126d_slope_v047_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _ema(r, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_ema_126d_slope_v048_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _ema(r, 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_ema_189d_slope_v049_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _ema(r, 189) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_ema_189d_slope_v050_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _ema(r, 189) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_ema_189d_slope_v051_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _ema(r, 189) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_ema_252d_slope_v052_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _ema(r, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_ema_252d_slope_v053_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _ema(r, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_ema_252d_slope_v054_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _ema(r, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_ema_378d_slope_v055_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _ema(r, 378) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_ema_378d_slope_v056_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _ema(r, 378) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_ema_378d_slope_v057_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _ema(r, 378) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_ema_504d_slope_v058_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _ema(r, 504) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_ema_504d_slope_v059_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _ema(r, 504) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_ema_504d_slope_v060_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _ema(r, 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_z_21d_slope_v061_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _z(r, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_z_21d_slope_v062_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _z(r, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_z_21d_slope_v063_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _z(r, 21) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_z_42d_slope_v064_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _z(r, 42) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_z_42d_slope_v065_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _z(r, 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_z_42d_slope_v066_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _z(r, 42) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_z_63d_slope_v067_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _z(r, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_z_63d_slope_v068_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _z(r, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_z_63d_slope_v069_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _z(r, 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_z_126d_slope_v070_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _z(r, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_z_126d_slope_v071_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _z(r, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_z_126d_slope_v072_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _z(r, 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_z_189d_slope_v073_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _z(r, 189) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_z_189d_slope_v074_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _z(r, 189) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_z_189d_slope_v075_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _z(r, 189) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_z_252d_slope_v076_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _z(r, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_z_252d_slope_v077_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _z(r, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_z_252d_slope_v078_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _z(r, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_z_378d_slope_v079_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _z(r, 378) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_z_378d_slope_v080_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _z(r, 378) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_z_378d_slope_v081_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _z(r, 378) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_z_504d_slope_v082_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _z(r, 504) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_z_504d_slope_v083_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _z(r, 504) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_z_504d_slope_v084_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _z(r, 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpaxvol_21d_slope_v085_signal(revenue, ppnenet, volume):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _mean(r, 21) * volume
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpaxvol_21d_slope_v086_signal(revenue, ppnenet, volume):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _mean(r, 21) * volume
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpaxvol_21d_slope_v087_signal(revenue, ppnenet, volume):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _mean(r, 21) * volume
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpaxvol_63d_slope_v088_signal(revenue, ppnenet, volume):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _mean(r, 63) * volume
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpaxvol_63d_slope_v089_signal(revenue, ppnenet, volume):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _mean(r, 63) * volume
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpaxvol_63d_slope_v090_signal(revenue, ppnenet, volume):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _mean(r, 63) * volume
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpaxvol_252d_slope_v091_signal(revenue, ppnenet, volume):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _mean(r, 252) * volume
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpaxvol_252d_slope_v092_signal(revenue, ppnenet, volume):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _mean(r, 252) * volume
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpaxvol_252d_slope_v093_signal(revenue, ppnenet, volume):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    base = _mean(r, 252) * volume
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpg_5d_slope_v094_signal(revenue, ppnenet, closeadj):
    base = _f41_revpar_growth(revenue, ppnenet, 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpg_5d_slope_v095_signal(revenue, ppnenet, closeadj):
    base = _f41_revpar_growth(revenue, ppnenet, 5) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpg_5d_slope_v096_signal(revenue, ppnenet, closeadj):
    base = _f41_revpar_growth(revenue, ppnenet, 5) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpg_10d_slope_v097_signal(revenue, ppnenet, closeadj):
    base = _f41_revpar_growth(revenue, ppnenet, 10) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpg_10d_slope_v098_signal(revenue, ppnenet, closeadj):
    base = _f41_revpar_growth(revenue, ppnenet, 10) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpg_10d_slope_v099_signal(revenue, ppnenet, closeadj):
    base = _f41_revpar_growth(revenue, ppnenet, 10) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpg_21d_slope_v100_signal(revenue, ppnenet, closeadj):
    base = _f41_revpar_growth(revenue, ppnenet, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpg_21d_slope_v101_signal(revenue, ppnenet, closeadj):
    base = _f41_revpar_growth(revenue, ppnenet, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpg_21d_slope_v102_signal(revenue, ppnenet, closeadj):
    base = _f41_revpar_growth(revenue, ppnenet, 21) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpg_42d_slope_v103_signal(revenue, ppnenet, closeadj):
    base = _f41_revpar_growth(revenue, ppnenet, 42) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpg_42d_slope_v104_signal(revenue, ppnenet, closeadj):
    base = _f41_revpar_growth(revenue, ppnenet, 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpg_42d_slope_v105_signal(revenue, ppnenet, closeadj):
    base = _f41_revpar_growth(revenue, ppnenet, 42) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpg_63d_slope_v106_signal(revenue, ppnenet, closeadj):
    base = _f41_revpar_growth(revenue, ppnenet, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpg_63d_slope_v107_signal(revenue, ppnenet, closeadj):
    base = _f41_revpar_growth(revenue, ppnenet, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpg_63d_slope_v108_signal(revenue, ppnenet, closeadj):
    base = _f41_revpar_growth(revenue, ppnenet, 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpg_126d_slope_v109_signal(revenue, ppnenet, closeadj):
    base = _f41_revpar_growth(revenue, ppnenet, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpg_126d_slope_v110_signal(revenue, ppnenet, closeadj):
    base = _f41_revpar_growth(revenue, ppnenet, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpg_126d_slope_v111_signal(revenue, ppnenet, closeadj):
    base = _f41_revpar_growth(revenue, ppnenet, 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpg_189d_slope_v112_signal(revenue, ppnenet, closeadj):
    base = _f41_revpar_growth(revenue, ppnenet, 189) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpg_189d_slope_v113_signal(revenue, ppnenet, closeadj):
    base = _f41_revpar_growth(revenue, ppnenet, 189) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpg_189d_slope_v114_signal(revenue, ppnenet, closeadj):
    base = _f41_revpar_growth(revenue, ppnenet, 189) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpg_252d_slope_v115_signal(revenue, ppnenet, closeadj):
    base = _f41_revpar_growth(revenue, ppnenet, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpg_252d_slope_v116_signal(revenue, ppnenet, closeadj):
    base = _f41_revpar_growth(revenue, ppnenet, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpg_252d_slope_v117_signal(revenue, ppnenet, closeadj):
    base = _f41_revpar_growth(revenue, ppnenet, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpg_378d_slope_v118_signal(revenue, ppnenet, closeadj):
    base = _f41_revpar_growth(revenue, ppnenet, 378) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpg_378d_slope_v119_signal(revenue, ppnenet, closeadj):
    base = _f41_revpar_growth(revenue, ppnenet, 378) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpg_378d_slope_v120_signal(revenue, ppnenet, closeadj):
    base = _f41_revpar_growth(revenue, ppnenet, 378) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpg_504d_slope_v121_signal(revenue, ppnenet, closeadj):
    base = _f41_revpar_growth(revenue, ppnenet, 504) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpg_504d_slope_v122_signal(revenue, ppnenet, closeadj):
    base = _f41_revpar_growth(revenue, ppnenet, 504) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpg_504d_slope_v123_signal(revenue, ppnenet, closeadj):
    base = _f41_revpar_growth(revenue, ppnenet, 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgsmooth_21o63_slope_v124_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 21)
    base = _mean(g, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgsmooth_21o63_slope_v125_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 21)
    base = _mean(g, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgsmooth_21o63_slope_v126_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 21)
    base = _mean(g, 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgsmooth_63o126_slope_v127_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 63)
    base = _mean(g, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgsmooth_63o126_slope_v128_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 63)
    base = _mean(g, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgsmooth_63o126_slope_v129_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 63)
    base = _mean(g, 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgsmooth_126o252_slope_v130_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 126)
    base = _mean(g, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgsmooth_126o252_slope_v131_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 126)
    base = _mean(g, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgsmooth_126o252_slope_v132_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 126)
    base = _mean(g, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgsmooth_252o252_slope_v133_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 252)
    base = _mean(g, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgsmooth_252o252_slope_v134_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 252)
    base = _mean(g, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgsmooth_252o252_slope_v135_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 252)
    base = _mean(g, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgsmooth_63o252_slope_v136_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 63)
    base = _mean(g, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgsmooth_63o252_slope_v137_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 63)
    base = _mean(g, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgsmooth_63o252_slope_v138_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 63)
    base = _mean(g, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgz_63o252_slope_v139_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 63)
    base = _z(g, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgz_63o252_slope_v140_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 63)
    base = _z(g, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgz_63o252_slope_v141_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 63)
    base = _z(g, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgz_252o504_slope_v142_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 252)
    base = _z(g, 504) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgz_252o504_slope_v143_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 252)
    base = _z(g, 504) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgz_252o504_slope_v144_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 252)
    base = _z(g, 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgz_21o126_slope_v145_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 21)
    base = _z(g, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgz_21o126_slope_v146_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 21)
    base = _z(g, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgz_21o126_slope_v147_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 21)
    base = _z(g, 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgz_42o252_slope_v148_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 42)
    base = _z(g, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgz_42o252_slope_v149_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 42)
    base = _z(g, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgz_42o252_slope_v150_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 42)
    base = _z(g, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f41hrp_f41_hospitality_revpar_proxy_rpa_mean_5d_slope_v001_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_mean_5d_slope_v002_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_mean_5d_slope_v003_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_mean_10d_slope_v004_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_mean_10d_slope_v005_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_mean_10d_slope_v006_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_mean_21d_slope_v007_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_mean_21d_slope_v008_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_mean_21d_slope_v009_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_mean_42d_slope_v010_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_mean_42d_slope_v011_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_mean_42d_slope_v012_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_mean_63d_slope_v013_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_mean_63d_slope_v014_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_mean_63d_slope_v015_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_mean_126d_slope_v016_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_mean_126d_slope_v017_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_mean_126d_slope_v018_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_mean_189d_slope_v019_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_mean_189d_slope_v020_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_mean_189d_slope_v021_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_mean_252d_slope_v022_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_mean_252d_slope_v023_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_mean_252d_slope_v024_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_mean_378d_slope_v025_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_mean_378d_slope_v026_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_mean_378d_slope_v027_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_mean_504d_slope_v028_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_mean_504d_slope_v029_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_mean_504d_slope_v030_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_ema_5d_slope_v031_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_ema_5d_slope_v032_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_ema_5d_slope_v033_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_ema_10d_slope_v034_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_ema_10d_slope_v035_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_ema_10d_slope_v036_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_ema_21d_slope_v037_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_ema_21d_slope_v038_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_ema_21d_slope_v039_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_ema_42d_slope_v040_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_ema_42d_slope_v041_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_ema_42d_slope_v042_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_ema_63d_slope_v043_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_ema_63d_slope_v044_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_ema_63d_slope_v045_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_ema_126d_slope_v046_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_ema_126d_slope_v047_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_ema_126d_slope_v048_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_ema_189d_slope_v049_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_ema_189d_slope_v050_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_ema_189d_slope_v051_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_ema_252d_slope_v052_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_ema_252d_slope_v053_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_ema_252d_slope_v054_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_ema_378d_slope_v055_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_ema_378d_slope_v056_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_ema_378d_slope_v057_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_ema_504d_slope_v058_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_ema_504d_slope_v059_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_ema_504d_slope_v060_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_z_21d_slope_v061_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_z_21d_slope_v062_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_z_21d_slope_v063_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_z_42d_slope_v064_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_z_42d_slope_v065_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_z_42d_slope_v066_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_z_63d_slope_v067_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_z_63d_slope_v068_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_z_63d_slope_v069_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_z_126d_slope_v070_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_z_126d_slope_v071_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_z_126d_slope_v072_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_z_189d_slope_v073_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_z_189d_slope_v074_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_z_189d_slope_v075_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_z_252d_slope_v076_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_z_252d_slope_v077_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_z_252d_slope_v078_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_z_378d_slope_v079_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_z_378d_slope_v080_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_z_378d_slope_v081_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_z_504d_slope_v082_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_z_504d_slope_v083_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_z_504d_slope_v084_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpaxvol_21d_slope_v085_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpaxvol_21d_slope_v086_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpaxvol_21d_slope_v087_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpaxvol_63d_slope_v088_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpaxvol_63d_slope_v089_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpaxvol_63d_slope_v090_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpaxvol_252d_slope_v091_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpaxvol_252d_slope_v092_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpaxvol_252d_slope_v093_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpg_5d_slope_v094_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpg_5d_slope_v095_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpg_5d_slope_v096_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpg_10d_slope_v097_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpg_10d_slope_v098_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpg_10d_slope_v099_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpg_21d_slope_v100_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpg_21d_slope_v101_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpg_21d_slope_v102_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpg_42d_slope_v103_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpg_42d_slope_v104_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpg_42d_slope_v105_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpg_63d_slope_v106_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpg_63d_slope_v107_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpg_63d_slope_v108_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpg_126d_slope_v109_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpg_126d_slope_v110_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpg_126d_slope_v111_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpg_189d_slope_v112_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpg_189d_slope_v113_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpg_189d_slope_v114_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpg_252d_slope_v115_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpg_252d_slope_v116_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpg_252d_slope_v117_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpg_378d_slope_v118_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpg_378d_slope_v119_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpg_378d_slope_v120_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpg_504d_slope_v121_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpg_504d_slope_v122_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpg_504d_slope_v123_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgsmooth_21o63_slope_v124_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgsmooth_21o63_slope_v125_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgsmooth_21o63_slope_v126_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgsmooth_63o126_slope_v127_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgsmooth_63o126_slope_v128_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgsmooth_63o126_slope_v129_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgsmooth_126o252_slope_v130_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgsmooth_126o252_slope_v131_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgsmooth_126o252_slope_v132_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgsmooth_252o252_slope_v133_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgsmooth_252o252_slope_v134_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgsmooth_252o252_slope_v135_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgsmooth_63o252_slope_v136_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgsmooth_63o252_slope_v137_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgsmooth_63o252_slope_v138_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgz_63o252_slope_v139_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgz_63o252_slope_v140_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgz_63o252_slope_v141_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgz_252o504_slope_v142_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgz_252o504_slope_v143_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgz_252o504_slope_v144_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgz_21o126_slope_v145_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgz_21o126_slope_v146_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgz_21o126_slope_v147_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgz_42o252_slope_v148_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgz_42o252_slope_v149_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgz_42o252_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F41_HOSPITALITY_REVPAR_PROXY_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = pd.Series((closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))).values, name="high")
    low = pd.Series((closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))).values, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ppnenet = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")

    cols = { "closeadj": closeadj, "high": high, "low": low, "volume": volume, "revenue": revenue, "ppnenet": ppnenet, "assets": assets }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f41_revenue_per_asset", "_f41_revpar_growth", "_f41_asset_utilization")
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
    print(f"OK hospitality_revpar_proxy_2nd_derivatives_001_150_claude: {n_features} features pass")
