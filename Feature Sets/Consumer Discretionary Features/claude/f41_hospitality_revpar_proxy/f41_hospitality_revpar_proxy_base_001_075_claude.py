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


def _f41_revenue_per_asset(revenue, ppnenet):
    return revenue / ppnenet.replace(0, np.nan)


def _f41_revpar_growth(revenue, ppnenet, w):
    r = revenue / ppnenet.replace(0, np.nan)
    return r.pct_change(periods=w)


def _f41_asset_utilization(revenue, assets, w):
    r = revenue / assets.replace(0, np.nan)
    return r.rolling(w, min_periods=max(1, w // 2)).mean()


def f41hrp_f41_hospitality_revpar_proxy_rpa_mean_5d_base_v001_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = _mean(r, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_mean_10d_base_v002_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = _mean(r, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_mean_21d_base_v003_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = _mean(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_mean_42d_base_v004_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = _mean(r, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_mean_63d_base_v005_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = _mean(r, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_mean_126d_base_v006_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = _mean(r, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_mean_189d_base_v007_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = _mean(r, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_mean_252d_base_v008_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = _mean(r, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_mean_378d_base_v009_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = _mean(r, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_mean_504d_base_v010_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = _mean(r, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_ema_5d_base_v011_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = _ema(r, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_ema_10d_base_v012_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = _ema(r, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_ema_21d_base_v013_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = _ema(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_ema_42d_base_v014_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = _ema(r, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_ema_63d_base_v015_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = _ema(r, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_ema_126d_base_v016_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = _ema(r, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_ema_189d_base_v017_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = _ema(r, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_ema_252d_base_v018_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = _ema(r, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_ema_378d_base_v019_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = _ema(r, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_ema_504d_base_v020_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = _ema(r, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_z_21d_base_v021_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = _z(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_z_42d_base_v022_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = _z(r, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_z_63d_base_v023_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = _z(r, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_z_126d_base_v024_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = _z(r, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_z_189d_base_v025_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = _z(r, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_z_252d_base_v026_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = _z(r, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_z_378d_base_v027_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = _z(r, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpa_z_504d_base_v028_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = _z(r, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpaxvol_21d_base_v029_signal(revenue, ppnenet, volume):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = _mean(r, 21) * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpaxvol_63d_base_v030_signal(revenue, ppnenet, volume):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = _mean(r, 63) * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpaxvol_252d_base_v031_signal(revenue, ppnenet, volume):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = _mean(r, 252) * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpg_5d_base_v032_signal(revenue, ppnenet, closeadj):
    result = _f41_revpar_growth(revenue, ppnenet, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpg_10d_base_v033_signal(revenue, ppnenet, closeadj):
    result = _f41_revpar_growth(revenue, ppnenet, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpg_21d_base_v034_signal(revenue, ppnenet, closeadj):
    result = _f41_revpar_growth(revenue, ppnenet, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpg_42d_base_v035_signal(revenue, ppnenet, closeadj):
    result = _f41_revpar_growth(revenue, ppnenet, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpg_63d_base_v036_signal(revenue, ppnenet, closeadj):
    result = _f41_revpar_growth(revenue, ppnenet, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpg_126d_base_v037_signal(revenue, ppnenet, closeadj):
    result = _f41_revpar_growth(revenue, ppnenet, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpg_189d_base_v038_signal(revenue, ppnenet, closeadj):
    result = _f41_revpar_growth(revenue, ppnenet, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpg_252d_base_v039_signal(revenue, ppnenet, closeadj):
    result = _f41_revpar_growth(revenue, ppnenet, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpg_378d_base_v040_signal(revenue, ppnenet, closeadj):
    result = _f41_revpar_growth(revenue, ppnenet, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpg_504d_base_v041_signal(revenue, ppnenet, closeadj):
    result = _f41_revpar_growth(revenue, ppnenet, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgsmooth_21o63_base_v042_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 21)
    result = _mean(g, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgsmooth_63o126_base_v043_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 63)
    result = _mean(g, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgsmooth_126o252_base_v044_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 126)
    result = _mean(g, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgsmooth_252o252_base_v045_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 252)
    result = _mean(g, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgsmooth_63o252_base_v046_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 63)
    result = _mean(g, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgz_63o252_base_v047_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 63)
    result = _z(g, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgz_252o504_base_v048_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 252)
    result = _z(g, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgz_21o126_base_v049_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 21)
    result = _z(g, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgz_42o252_base_v050_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 42)
    result = _z(g, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_au_5d_base_v051_signal(revenue, assets, closeadj):
    result = _f41_asset_utilization(revenue, assets, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_au_10d_base_v052_signal(revenue, assets, closeadj):
    result = _f41_asset_utilization(revenue, assets, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_au_21d_base_v053_signal(revenue, assets, closeadj):
    result = _f41_asset_utilization(revenue, assets, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_au_42d_base_v054_signal(revenue, assets, closeadj):
    result = _f41_asset_utilization(revenue, assets, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_au_63d_base_v055_signal(revenue, assets, closeadj):
    result = _f41_asset_utilization(revenue, assets, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_au_126d_base_v056_signal(revenue, assets, closeadj):
    result = _f41_asset_utilization(revenue, assets, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_au_189d_base_v057_signal(revenue, assets, closeadj):
    result = _f41_asset_utilization(revenue, assets, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_au_252d_base_v058_signal(revenue, assets, closeadj):
    result = _f41_asset_utilization(revenue, assets, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_au_378d_base_v059_signal(revenue, assets, closeadj):
    result = _f41_asset_utilization(revenue, assets, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_au_504d_base_v060_signal(revenue, assets, closeadj):
    result = _f41_asset_utilization(revenue, assets, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_audiff_21m63_base_v061_signal(revenue, assets, closeadj):
    s = _f41_asset_utilization(revenue, assets, 21)
    l = _f41_asset_utilization(revenue, assets, 63)
    result = (s - l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_audiff_63m252_base_v062_signal(revenue, assets, closeadj):
    s = _f41_asset_utilization(revenue, assets, 63)
    l = _f41_asset_utilization(revenue, assets, 252)
    result = (s - l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_audiff_252m504_base_v063_signal(revenue, assets, closeadj):
    s = _f41_asset_utilization(revenue, assets, 252)
    l = _f41_asset_utilization(revenue, assets, 504)
    result = (s - l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_audiff_21m252_base_v064_signal(revenue, assets, closeadj):
    s = _f41_asset_utilization(revenue, assets, 21)
    l = _f41_asset_utilization(revenue, assets, 252)
    result = (s - l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_aurat_63v252_base_v065_signal(revenue, assets, closeadj):
    s = _f41_asset_utilization(revenue, assets, 63)
    l = _f41_asset_utilization(revenue, assets, 252).replace(0, np.nan)
    result = (s / l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_aurat_21v63_base_v066_signal(revenue, assets, closeadj):
    s = _f41_asset_utilization(revenue, assets, 21)
    l = _f41_asset_utilization(revenue, assets, 63).replace(0, np.nan)
    result = (s / l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_aurat_252v504_base_v067_signal(revenue, assets, closeadj):
    s = _f41_asset_utilization(revenue, assets, 252)
    l = _f41_asset_utilization(revenue, assets, 504).replace(0, np.nan)
    result = (s / l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_auz_63o252_base_v068_signal(revenue, assets, closeadj):
    au = _f41_asset_utilization(revenue, assets, 63)
    result = _z(au, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_auz_252o504_base_v069_signal(revenue, assets, closeadj):
    au = _f41_asset_utilization(revenue, assets, 252)
    result = _z(au, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_auz_21o126_base_v070_signal(revenue, assets, closeadj):
    au = _f41_asset_utilization(revenue, assets, 21)
    result = _z(au, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpastd_21d_base_v071_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = _std(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpastd_63d_base_v072_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = _std(r, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpastd_126d_base_v073_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = _std(r, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpastd_252d_base_v074_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = _std(r, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpastd_504d_base_v075_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = _std(r, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f41hrp_f41_hospitality_revpar_proxy_rpa_mean_5d_base_v001_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_mean_10d_base_v002_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_mean_21d_base_v003_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_mean_42d_base_v004_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_mean_63d_base_v005_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_mean_126d_base_v006_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_mean_189d_base_v007_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_mean_252d_base_v008_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_mean_378d_base_v009_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_mean_504d_base_v010_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_ema_5d_base_v011_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_ema_10d_base_v012_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_ema_21d_base_v013_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_ema_42d_base_v014_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_ema_63d_base_v015_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_ema_126d_base_v016_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_ema_189d_base_v017_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_ema_252d_base_v018_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_ema_378d_base_v019_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_ema_504d_base_v020_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_z_21d_base_v021_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_z_42d_base_v022_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_z_63d_base_v023_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_z_126d_base_v024_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_z_189d_base_v025_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_z_252d_base_v026_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_z_378d_base_v027_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpa_z_504d_base_v028_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpaxvol_21d_base_v029_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpaxvol_63d_base_v030_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpaxvol_252d_base_v031_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpg_5d_base_v032_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpg_10d_base_v033_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpg_21d_base_v034_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpg_42d_base_v035_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpg_63d_base_v036_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpg_126d_base_v037_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpg_189d_base_v038_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpg_252d_base_v039_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpg_378d_base_v040_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpg_504d_base_v041_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgsmooth_21o63_base_v042_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgsmooth_63o126_base_v043_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgsmooth_126o252_base_v044_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgsmooth_252o252_base_v045_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgsmooth_63o252_base_v046_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgz_63o252_base_v047_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgz_252o504_base_v048_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgz_21o126_base_v049_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgz_42o252_base_v050_signal,
    f41hrp_f41_hospitality_revpar_proxy_au_5d_base_v051_signal,
    f41hrp_f41_hospitality_revpar_proxy_au_10d_base_v052_signal,
    f41hrp_f41_hospitality_revpar_proxy_au_21d_base_v053_signal,
    f41hrp_f41_hospitality_revpar_proxy_au_42d_base_v054_signal,
    f41hrp_f41_hospitality_revpar_proxy_au_63d_base_v055_signal,
    f41hrp_f41_hospitality_revpar_proxy_au_126d_base_v056_signal,
    f41hrp_f41_hospitality_revpar_proxy_au_189d_base_v057_signal,
    f41hrp_f41_hospitality_revpar_proxy_au_252d_base_v058_signal,
    f41hrp_f41_hospitality_revpar_proxy_au_378d_base_v059_signal,
    f41hrp_f41_hospitality_revpar_proxy_au_504d_base_v060_signal,
    f41hrp_f41_hospitality_revpar_proxy_audiff_21m63_base_v061_signal,
    f41hrp_f41_hospitality_revpar_proxy_audiff_63m252_base_v062_signal,
    f41hrp_f41_hospitality_revpar_proxy_audiff_252m504_base_v063_signal,
    f41hrp_f41_hospitality_revpar_proxy_audiff_21m252_base_v064_signal,
    f41hrp_f41_hospitality_revpar_proxy_aurat_63v252_base_v065_signal,
    f41hrp_f41_hospitality_revpar_proxy_aurat_21v63_base_v066_signal,
    f41hrp_f41_hospitality_revpar_proxy_aurat_252v504_base_v067_signal,
    f41hrp_f41_hospitality_revpar_proxy_auz_63o252_base_v068_signal,
    f41hrp_f41_hospitality_revpar_proxy_auz_252o504_base_v069_signal,
    f41hrp_f41_hospitality_revpar_proxy_auz_21o126_base_v070_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpastd_21d_base_v071_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpastd_63d_base_v072_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpastd_126d_base_v073_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpastd_252d_base_v074_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpastd_504d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F41_HOSPITALITY_REVPAR_PROXY_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK hospitality_revpar_proxy_base_001_075_claude: {n_features} features pass")
