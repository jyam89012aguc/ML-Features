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
def _f08_inventory_turnover(inventory, cor):
    return cor / inventory.replace(0, np.nan)


def _f08_inventory_freshness(inventory, revenue, w):
    inv_per_rev = inventory / revenue.replace(0, np.nan)
    m = inv_per_rev.rolling(w, min_periods=max(1, w // 2)).mean()
    return inv_per_rev - m


def _f08_inv_velocity(inventory, cor, w):
    turn = cor / inventory.replace(0, np.nan)
    return turn.pct_change(periods=w)

def f08rif_f08_retail_inventory_freshness_turn_mean_5d_base_v001_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = _mean(t, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_mean_10d_base_v002_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = _mean(t, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_mean_21d_base_v003_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = _mean(t, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_mean_42d_base_v004_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = _mean(t, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_mean_63d_base_v005_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = _mean(t, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_mean_126d_base_v006_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = _mean(t, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_mean_189d_base_v007_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = _mean(t, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_mean_252d_base_v008_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = _mean(t, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_mean_378d_base_v009_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = _mean(t, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_mean_504d_base_v010_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = _mean(t, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_std_5d_base_v011_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = _std(t, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_std_10d_base_v012_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = _std(t, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_std_21d_base_v013_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = _std(t, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_std_42d_base_v014_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = _std(t, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_std_63d_base_v015_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = _std(t, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_std_126d_base_v016_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = _std(t, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_std_189d_base_v017_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = _std(t, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_std_252d_base_v018_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = _std(t, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_std_378d_base_v019_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = _std(t, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_std_504d_base_v020_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = _std(t, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_z_5d_base_v021_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = _z(t, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_z_10d_base_v022_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = _z(t, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_z_21d_base_v023_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = _z(t, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_z_42d_base_v024_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = _z(t, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_z_63d_base_v025_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = _z(t, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_z_126d_base_v026_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = _z(t, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_z_189d_base_v027_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = _z(t, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_z_252d_base_v028_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = _z(t, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_z_378d_base_v029_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = _z(t, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_z_504d_base_v030_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = _z(t, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_ema_5d_base_v031_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = _ema(t, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_ema_10d_base_v032_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = _ema(t, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_ema_21d_base_v033_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = _ema(t, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_ema_42d_base_v034_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = _ema(t, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_ema_63d_base_v035_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = _ema(t, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_ema_126d_base_v036_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = _ema(t, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_ema_189d_base_v037_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = _ema(t, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_ema_252d_base_v038_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = _ema(t, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_ema_378d_base_v039_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = _ema(t, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_ema_504d_base_v040_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = _ema(t, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_diff_5d_base_v041_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = (t - t.shift(5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_diff_10d_base_v042_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = (t - t.shift(10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_diff_21d_base_v043_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = (t - t.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_diff_42d_base_v044_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = (t - t.shift(42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_diff_63d_base_v045_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = (t - t.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_diff_126d_base_v046_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = (t - t.shift(126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_diff_189d_base_v047_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = (t - t.shift(189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_diff_252d_base_v048_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = (t - t.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_diff_378d_base_v049_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = (t - t.shift(378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_diff_504d_base_v050_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    result = (t - t.shift(504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_5d_base_v051_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 5)
    result = f * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_10d_base_v052_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 10)
    result = f * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_21d_base_v053_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 21)
    result = f * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_42d_base_v054_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 42)
    result = f * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_63d_base_v055_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 63)
    result = f * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_126d_base_v056_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 126)
    result = f * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_189d_base_v057_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 189)
    result = f * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_252d_base_v058_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 252)
    result = f * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_378d_base_v059_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 378)
    result = f * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_504d_base_v060_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 504)
    result = f * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_mean_5d_base_v061_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 5)
    result = _mean(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_mean_10d_base_v062_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 10)
    result = _mean(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_mean_21d_base_v063_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 21)
    result = _mean(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_mean_42d_base_v064_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 42)
    result = _mean(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_mean_63d_base_v065_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 63)
    result = _mean(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_mean_126d_base_v066_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 126)
    result = _mean(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_mean_189d_base_v067_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 189)
    result = _mean(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_mean_252d_base_v068_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 252)
    result = _mean(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_mean_378d_base_v069_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 378)
    result = _mean(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_mean_504d_base_v070_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 504)
    result = _mean(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_std_5d_base_v071_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 5)
    result = _std(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_std_10d_base_v072_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 10)
    result = _std(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_std_21d_base_v073_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 21)
    result = _std(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_std_42d_base_v074_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 42)
    result = _std(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_std_63d_base_v075_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 63)
    result = _std(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f08rif_f08_retail_inventory_freshness_turn_mean_5d_base_v001_signal,
    f08rif_f08_retail_inventory_freshness_turn_mean_10d_base_v002_signal,
    f08rif_f08_retail_inventory_freshness_turn_mean_21d_base_v003_signal,
    f08rif_f08_retail_inventory_freshness_turn_mean_42d_base_v004_signal,
    f08rif_f08_retail_inventory_freshness_turn_mean_63d_base_v005_signal,
    f08rif_f08_retail_inventory_freshness_turn_mean_126d_base_v006_signal,
    f08rif_f08_retail_inventory_freshness_turn_mean_189d_base_v007_signal,
    f08rif_f08_retail_inventory_freshness_turn_mean_252d_base_v008_signal,
    f08rif_f08_retail_inventory_freshness_turn_mean_378d_base_v009_signal,
    f08rif_f08_retail_inventory_freshness_turn_mean_504d_base_v010_signal,
    f08rif_f08_retail_inventory_freshness_turn_std_5d_base_v011_signal,
    f08rif_f08_retail_inventory_freshness_turn_std_10d_base_v012_signal,
    f08rif_f08_retail_inventory_freshness_turn_std_21d_base_v013_signal,
    f08rif_f08_retail_inventory_freshness_turn_std_42d_base_v014_signal,
    f08rif_f08_retail_inventory_freshness_turn_std_63d_base_v015_signal,
    f08rif_f08_retail_inventory_freshness_turn_std_126d_base_v016_signal,
    f08rif_f08_retail_inventory_freshness_turn_std_189d_base_v017_signal,
    f08rif_f08_retail_inventory_freshness_turn_std_252d_base_v018_signal,
    f08rif_f08_retail_inventory_freshness_turn_std_378d_base_v019_signal,
    f08rif_f08_retail_inventory_freshness_turn_std_504d_base_v020_signal,
    f08rif_f08_retail_inventory_freshness_turn_z_5d_base_v021_signal,
    f08rif_f08_retail_inventory_freshness_turn_z_10d_base_v022_signal,
    f08rif_f08_retail_inventory_freshness_turn_z_21d_base_v023_signal,
    f08rif_f08_retail_inventory_freshness_turn_z_42d_base_v024_signal,
    f08rif_f08_retail_inventory_freshness_turn_z_63d_base_v025_signal,
    f08rif_f08_retail_inventory_freshness_turn_z_126d_base_v026_signal,
    f08rif_f08_retail_inventory_freshness_turn_z_189d_base_v027_signal,
    f08rif_f08_retail_inventory_freshness_turn_z_252d_base_v028_signal,
    f08rif_f08_retail_inventory_freshness_turn_z_378d_base_v029_signal,
    f08rif_f08_retail_inventory_freshness_turn_z_504d_base_v030_signal,
    f08rif_f08_retail_inventory_freshness_turn_ema_5d_base_v031_signal,
    f08rif_f08_retail_inventory_freshness_turn_ema_10d_base_v032_signal,
    f08rif_f08_retail_inventory_freshness_turn_ema_21d_base_v033_signal,
    f08rif_f08_retail_inventory_freshness_turn_ema_42d_base_v034_signal,
    f08rif_f08_retail_inventory_freshness_turn_ema_63d_base_v035_signal,
    f08rif_f08_retail_inventory_freshness_turn_ema_126d_base_v036_signal,
    f08rif_f08_retail_inventory_freshness_turn_ema_189d_base_v037_signal,
    f08rif_f08_retail_inventory_freshness_turn_ema_252d_base_v038_signal,
    f08rif_f08_retail_inventory_freshness_turn_ema_378d_base_v039_signal,
    f08rif_f08_retail_inventory_freshness_turn_ema_504d_base_v040_signal,
    f08rif_f08_retail_inventory_freshness_turn_diff_5d_base_v041_signal,
    f08rif_f08_retail_inventory_freshness_turn_diff_10d_base_v042_signal,
    f08rif_f08_retail_inventory_freshness_turn_diff_21d_base_v043_signal,
    f08rif_f08_retail_inventory_freshness_turn_diff_42d_base_v044_signal,
    f08rif_f08_retail_inventory_freshness_turn_diff_63d_base_v045_signal,
    f08rif_f08_retail_inventory_freshness_turn_diff_126d_base_v046_signal,
    f08rif_f08_retail_inventory_freshness_turn_diff_189d_base_v047_signal,
    f08rif_f08_retail_inventory_freshness_turn_diff_252d_base_v048_signal,
    f08rif_f08_retail_inventory_freshness_turn_diff_378d_base_v049_signal,
    f08rif_f08_retail_inventory_freshness_turn_diff_504d_base_v050_signal,
    f08rif_f08_retail_inventory_freshness_fresh_5d_base_v051_signal,
    f08rif_f08_retail_inventory_freshness_fresh_10d_base_v052_signal,
    f08rif_f08_retail_inventory_freshness_fresh_21d_base_v053_signal,
    f08rif_f08_retail_inventory_freshness_fresh_42d_base_v054_signal,
    f08rif_f08_retail_inventory_freshness_fresh_63d_base_v055_signal,
    f08rif_f08_retail_inventory_freshness_fresh_126d_base_v056_signal,
    f08rif_f08_retail_inventory_freshness_fresh_189d_base_v057_signal,
    f08rif_f08_retail_inventory_freshness_fresh_252d_base_v058_signal,
    f08rif_f08_retail_inventory_freshness_fresh_378d_base_v059_signal,
    f08rif_f08_retail_inventory_freshness_fresh_504d_base_v060_signal,
    f08rif_f08_retail_inventory_freshness_fresh_mean_5d_base_v061_signal,
    f08rif_f08_retail_inventory_freshness_fresh_mean_10d_base_v062_signal,
    f08rif_f08_retail_inventory_freshness_fresh_mean_21d_base_v063_signal,
    f08rif_f08_retail_inventory_freshness_fresh_mean_42d_base_v064_signal,
    f08rif_f08_retail_inventory_freshness_fresh_mean_63d_base_v065_signal,
    f08rif_f08_retail_inventory_freshness_fresh_mean_126d_base_v066_signal,
    f08rif_f08_retail_inventory_freshness_fresh_mean_189d_base_v067_signal,
    f08rif_f08_retail_inventory_freshness_fresh_mean_252d_base_v068_signal,
    f08rif_f08_retail_inventory_freshness_fresh_mean_378d_base_v069_signal,
    f08rif_f08_retail_inventory_freshness_fresh_mean_504d_base_v070_signal,
    f08rif_f08_retail_inventory_freshness_fresh_std_5d_base_v071_signal,
    f08rif_f08_retail_inventory_freshness_fresh_std_10d_base_v072_signal,
    f08rif_f08_retail_inventory_freshness_fresh_std_21d_base_v073_signal,
    f08rif_f08_retail_inventory_freshness_fresh_std_42d_base_v074_signal,
    f08rif_f08_retail_inventory_freshness_fresh_std_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F08_RETAIL_INVENTORY_FRESHNESS_REGISTRY_001_075 = REGISTRY


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
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "inventory": inventory, "ppnenet": ppnenet,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f08_inventory_turnover", "_f08_inventory_freshness", "_f08_inv_velocity")
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
    print(f"OK f08_retail_inventory_freshness_001_075_claude: {n_features} features pass")
