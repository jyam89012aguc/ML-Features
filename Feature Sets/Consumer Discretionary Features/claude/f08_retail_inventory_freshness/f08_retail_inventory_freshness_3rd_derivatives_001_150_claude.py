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
def _f08_inventory_turnover(inventory, cor):
    return cor / inventory.replace(0, np.nan)


def _f08_inventory_freshness(inventory, revenue, w):
    inv_per_rev = inventory / revenue.replace(0, np.nan)
    m = inv_per_rev.rolling(w, min_periods=max(1, w // 2)).mean()
    return inv_per_rev - m


def _f08_inv_velocity(inventory, cor, w):
    turn = cor / inventory.replace(0, np.nan)
    return turn.pct_change(periods=w)

def f08rif_f08_retail_inventory_freshness_turn_mean_5d_jerk_v001_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = _mean(t, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_mean_10d_jerk_v002_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = _mean(t, 10) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_mean_21d_jerk_v003_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = _mean(t, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_mean_42d_jerk_v004_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = _mean(t, 42) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_mean_63d_jerk_v005_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = _mean(t, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_mean_126d_jerk_v006_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = _mean(t, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_mean_189d_jerk_v007_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = _mean(t, 189) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_mean_252d_jerk_v008_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = _mean(t, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_mean_378d_jerk_v009_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = _mean(t, 378) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_mean_504d_jerk_v010_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = _mean(t, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_std_5d_jerk_v011_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = _std(t, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_std_10d_jerk_v012_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = _std(t, 10) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_std_21d_jerk_v013_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = _std(t, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_std_42d_jerk_v014_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = _std(t, 42) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_std_63d_jerk_v015_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = _std(t, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_std_126d_jerk_v016_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = _std(t, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_std_189d_jerk_v017_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = _std(t, 189) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_std_252d_jerk_v018_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = _std(t, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_std_378d_jerk_v019_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = _std(t, 378) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_std_504d_jerk_v020_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = _std(t, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_z_5d_jerk_v021_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = _z(t, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_z_10d_jerk_v022_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = _z(t, 10) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_z_21d_jerk_v023_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = _z(t, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_z_42d_jerk_v024_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = _z(t, 42) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_z_63d_jerk_v025_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = _z(t, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_z_126d_jerk_v026_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = _z(t, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_z_189d_jerk_v027_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = _z(t, 189) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_z_252d_jerk_v028_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = _z(t, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_z_378d_jerk_v029_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = _z(t, 378) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_z_504d_jerk_v030_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = _z(t, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_ema_5d_jerk_v031_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = _ema(t, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_ema_10d_jerk_v032_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = _ema(t, 10) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_ema_21d_jerk_v033_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = _ema(t, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_ema_42d_jerk_v034_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = _ema(t, 42) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_ema_63d_jerk_v035_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = _ema(t, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_ema_126d_jerk_v036_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = _ema(t, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_ema_189d_jerk_v037_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = _ema(t, 189) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_ema_252d_jerk_v038_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = _ema(t, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_ema_378d_jerk_v039_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = _ema(t, 378) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_ema_504d_jerk_v040_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = _ema(t, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_diff_5d_jerk_v041_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = (t - t.shift(5)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_diff_10d_jerk_v042_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = (t - t.shift(10)) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_diff_21d_jerk_v043_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = (t - t.shift(21)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_diff_42d_jerk_v044_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = (t - t.shift(42)) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_diff_63d_jerk_v045_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = (t - t.shift(63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_diff_126d_jerk_v046_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = (t - t.shift(126)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_diff_189d_jerk_v047_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = (t - t.shift(189)) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_diff_252d_jerk_v048_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = (t - t.shift(252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_diff_378d_jerk_v049_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = (t - t.shift(378)) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_turn_diff_504d_jerk_v050_signal(inventory, cor, closeadj):
    t = _f08_inventory_turnover(inventory, cor)
    base = (t - t.shift(504)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_5d_jerk_v051_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 5)
    base = f * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_10d_jerk_v052_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 10)
    base = f * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_21d_jerk_v053_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 21)
    base = f * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_42d_jerk_v054_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 42)
    base = f * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_63d_jerk_v055_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 63)
    base = f * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_126d_jerk_v056_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 126)
    base = f * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_189d_jerk_v057_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 189)
    base = f * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_252d_jerk_v058_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 252)
    base = f * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_378d_jerk_v059_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 378)
    base = f * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_504d_jerk_v060_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 504)
    base = f * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_mean_5d_jerk_v061_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 5)
    base = _mean(f, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_mean_10d_jerk_v062_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 10)
    base = _mean(f, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_mean_21d_jerk_v063_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 21)
    base = _mean(f, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_mean_42d_jerk_v064_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 42)
    base = _mean(f, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_mean_63d_jerk_v065_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 63)
    base = _mean(f, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_mean_126d_jerk_v066_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 126)
    base = _mean(f, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_mean_189d_jerk_v067_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 189)
    base = _mean(f, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_mean_252d_jerk_v068_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 252)
    base = _mean(f, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_mean_378d_jerk_v069_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 378)
    base = _mean(f, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_mean_504d_jerk_v070_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 504)
    base = _mean(f, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_std_5d_jerk_v071_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 5)
    base = _std(f, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_std_10d_jerk_v072_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 10)
    base = _std(f, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_std_21d_jerk_v073_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 21)
    base = _std(f, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_std_42d_jerk_v074_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 42)
    base = _std(f, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_std_63d_jerk_v075_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 63)
    base = _std(f, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_std_126d_jerk_v076_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 126)
    base = _std(f, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_std_189d_jerk_v077_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 189)
    base = _std(f, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_std_252d_jerk_v078_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 252)
    base = _std(f, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_std_378d_jerk_v079_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 378)
    base = _std(f, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_std_504d_jerk_v080_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 504)
    base = _std(f, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_z_5d_jerk_v081_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 5)
    base = _z(f, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_z_10d_jerk_v082_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 10)
    base = _z(f, 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_z_21d_jerk_v083_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 21)
    base = _z(f, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_z_42d_jerk_v084_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 42)
    base = _z(f, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_z_63d_jerk_v085_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 63)
    base = _z(f, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_z_126d_jerk_v086_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 126)
    base = _z(f, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_z_189d_jerk_v087_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 189)
    base = _z(f, 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_z_252d_jerk_v088_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 252)
    base = _z(f, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_z_378d_jerk_v089_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 378)
    base = _z(f, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_z_504d_jerk_v090_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 504)
    base = _z(f, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_ema_5d_jerk_v091_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 5)
    base = _ema(f, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_ema_10d_jerk_v092_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 10)
    base = _ema(f, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_ema_21d_jerk_v093_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 21)
    base = _ema(f, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_ema_42d_jerk_v094_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 42)
    base = _ema(f, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_ema_63d_jerk_v095_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 63)
    base = _ema(f, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_ema_126d_jerk_v096_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 126)
    base = _ema(f, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_ema_189d_jerk_v097_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 189)
    base = _ema(f, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_ema_252d_jerk_v098_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 252)
    base = _ema(f, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_ema_378d_jerk_v099_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 378)
    base = _ema(f, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_ema_504d_jerk_v100_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 504)
    base = _ema(f, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_5d_jerk_v101_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 5)
    base = v * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_10d_jerk_v102_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 10)
    base = v * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_21d_jerk_v103_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 21)
    base = v * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_42d_jerk_v104_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 42)
    base = v * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_63d_jerk_v105_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 63)
    base = v * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_126d_jerk_v106_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 126)
    base = v * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_189d_jerk_v107_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 189)
    base = v * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_252d_jerk_v108_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 252)
    base = v * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_378d_jerk_v109_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 378)
    base = v * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_504d_jerk_v110_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 504)
    base = v * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_mean_5d_jerk_v111_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 5)
    base = _mean(v, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_mean_10d_jerk_v112_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 10)
    base = _mean(v, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_mean_21d_jerk_v113_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 21)
    base = _mean(v, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_mean_42d_jerk_v114_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 42)
    base = _mean(v, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_mean_63d_jerk_v115_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 63)
    base = _mean(v, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_mean_126d_jerk_v116_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 126)
    base = _mean(v, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_mean_189d_jerk_v117_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 189)
    base = _mean(v, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_mean_252d_jerk_v118_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 252)
    base = _mean(v, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_mean_378d_jerk_v119_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 378)
    base = _mean(v, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_mean_504d_jerk_v120_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 504)
    base = _mean(v, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_std_5d_jerk_v121_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 5)
    base = _std(v, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_std_10d_jerk_v122_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 10)
    base = _std(v, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_std_21d_jerk_v123_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 21)
    base = _std(v, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_std_42d_jerk_v124_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 42)
    base = _std(v, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_std_63d_jerk_v125_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 63)
    base = _std(v, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_std_126d_jerk_v126_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 126)
    base = _std(v, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_std_189d_jerk_v127_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 189)
    base = _std(v, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_std_252d_jerk_v128_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 252)
    base = _std(v, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_std_378d_jerk_v129_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 378)
    base = _std(v, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_std_504d_jerk_v130_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 504)
    base = _std(v, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_xrev_5d_jerk_v131_signal(inventory, cor, revenue, closeadj):
    v = _f08_inv_velocity(inventory, cor, 5)
    base = v * (revenue / 1e9) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_xrev_10d_jerk_v132_signal(inventory, cor, revenue, closeadj):
    v = _f08_inv_velocity(inventory, cor, 10)
    base = v * (revenue / 1e9) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_xrev_21d_jerk_v133_signal(inventory, cor, revenue, closeadj):
    v = _f08_inv_velocity(inventory, cor, 21)
    base = v * (revenue / 1e9) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_xrev_42d_jerk_v134_signal(inventory, cor, revenue, closeadj):
    v = _f08_inv_velocity(inventory, cor, 42)
    base = v * (revenue / 1e9) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_xrev_63d_jerk_v135_signal(inventory, cor, revenue, closeadj):
    v = _f08_inv_velocity(inventory, cor, 63)
    base = v * (revenue / 1e9) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_xrev_126d_jerk_v136_signal(inventory, cor, revenue, closeadj):
    v = _f08_inv_velocity(inventory, cor, 126)
    base = v * (revenue / 1e9) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_xrev_189d_jerk_v137_signal(inventory, cor, revenue, closeadj):
    v = _f08_inv_velocity(inventory, cor, 189)
    base = v * (revenue / 1e9) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_xrev_252d_jerk_v138_signal(inventory, cor, revenue, closeadj):
    v = _f08_inv_velocity(inventory, cor, 252)
    base = v * (revenue / 1e9) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_xrev_378d_jerk_v139_signal(inventory, cor, revenue, closeadj):
    v = _f08_inv_velocity(inventory, cor, 378)
    base = v * (revenue / 1e9) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_xrev_504d_jerk_v140_signal(inventory, cor, revenue, closeadj):
    v = _f08_inv_velocity(inventory, cor, 504)
    base = v * (revenue / 1e9) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_xinv_5d_jerk_v141_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 5)
    base = v * (inventory / 1e8) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_xinv_10d_jerk_v142_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 10)
    base = v * (inventory / 1e8) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_xinv_21d_jerk_v143_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 21)
    base = v * (inventory / 1e8) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_xinv_42d_jerk_v144_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 42)
    base = v * (inventory / 1e8) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_xinv_63d_jerk_v145_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 63)
    base = v * (inventory / 1e8) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_xinv_126d_jerk_v146_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 126)
    base = v * (inventory / 1e8) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_xinv_189d_jerk_v147_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 189)
    base = v * (inventory / 1e8) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_xinv_252d_jerk_v148_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 252)
    base = v * (inventory / 1e8) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_xinv_378d_jerk_v149_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 378)
    base = v * (inventory / 1e8) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_xinv_504d_jerk_v150_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 504)
    base = v * (inventory / 1e8) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f08rif_f08_retail_inventory_freshness_turn_mean_5d_jerk_v001_signal,
    f08rif_f08_retail_inventory_freshness_turn_mean_10d_jerk_v002_signal,
    f08rif_f08_retail_inventory_freshness_turn_mean_21d_jerk_v003_signal,
    f08rif_f08_retail_inventory_freshness_turn_mean_42d_jerk_v004_signal,
    f08rif_f08_retail_inventory_freshness_turn_mean_63d_jerk_v005_signal,
    f08rif_f08_retail_inventory_freshness_turn_mean_126d_jerk_v006_signal,
    f08rif_f08_retail_inventory_freshness_turn_mean_189d_jerk_v007_signal,
    f08rif_f08_retail_inventory_freshness_turn_mean_252d_jerk_v008_signal,
    f08rif_f08_retail_inventory_freshness_turn_mean_378d_jerk_v009_signal,
    f08rif_f08_retail_inventory_freshness_turn_mean_504d_jerk_v010_signal,
    f08rif_f08_retail_inventory_freshness_turn_std_5d_jerk_v011_signal,
    f08rif_f08_retail_inventory_freshness_turn_std_10d_jerk_v012_signal,
    f08rif_f08_retail_inventory_freshness_turn_std_21d_jerk_v013_signal,
    f08rif_f08_retail_inventory_freshness_turn_std_42d_jerk_v014_signal,
    f08rif_f08_retail_inventory_freshness_turn_std_63d_jerk_v015_signal,
    f08rif_f08_retail_inventory_freshness_turn_std_126d_jerk_v016_signal,
    f08rif_f08_retail_inventory_freshness_turn_std_189d_jerk_v017_signal,
    f08rif_f08_retail_inventory_freshness_turn_std_252d_jerk_v018_signal,
    f08rif_f08_retail_inventory_freshness_turn_std_378d_jerk_v019_signal,
    f08rif_f08_retail_inventory_freshness_turn_std_504d_jerk_v020_signal,
    f08rif_f08_retail_inventory_freshness_turn_z_5d_jerk_v021_signal,
    f08rif_f08_retail_inventory_freshness_turn_z_10d_jerk_v022_signal,
    f08rif_f08_retail_inventory_freshness_turn_z_21d_jerk_v023_signal,
    f08rif_f08_retail_inventory_freshness_turn_z_42d_jerk_v024_signal,
    f08rif_f08_retail_inventory_freshness_turn_z_63d_jerk_v025_signal,
    f08rif_f08_retail_inventory_freshness_turn_z_126d_jerk_v026_signal,
    f08rif_f08_retail_inventory_freshness_turn_z_189d_jerk_v027_signal,
    f08rif_f08_retail_inventory_freshness_turn_z_252d_jerk_v028_signal,
    f08rif_f08_retail_inventory_freshness_turn_z_378d_jerk_v029_signal,
    f08rif_f08_retail_inventory_freshness_turn_z_504d_jerk_v030_signal,
    f08rif_f08_retail_inventory_freshness_turn_ema_5d_jerk_v031_signal,
    f08rif_f08_retail_inventory_freshness_turn_ema_10d_jerk_v032_signal,
    f08rif_f08_retail_inventory_freshness_turn_ema_21d_jerk_v033_signal,
    f08rif_f08_retail_inventory_freshness_turn_ema_42d_jerk_v034_signal,
    f08rif_f08_retail_inventory_freshness_turn_ema_63d_jerk_v035_signal,
    f08rif_f08_retail_inventory_freshness_turn_ema_126d_jerk_v036_signal,
    f08rif_f08_retail_inventory_freshness_turn_ema_189d_jerk_v037_signal,
    f08rif_f08_retail_inventory_freshness_turn_ema_252d_jerk_v038_signal,
    f08rif_f08_retail_inventory_freshness_turn_ema_378d_jerk_v039_signal,
    f08rif_f08_retail_inventory_freshness_turn_ema_504d_jerk_v040_signal,
    f08rif_f08_retail_inventory_freshness_turn_diff_5d_jerk_v041_signal,
    f08rif_f08_retail_inventory_freshness_turn_diff_10d_jerk_v042_signal,
    f08rif_f08_retail_inventory_freshness_turn_diff_21d_jerk_v043_signal,
    f08rif_f08_retail_inventory_freshness_turn_diff_42d_jerk_v044_signal,
    f08rif_f08_retail_inventory_freshness_turn_diff_63d_jerk_v045_signal,
    f08rif_f08_retail_inventory_freshness_turn_diff_126d_jerk_v046_signal,
    f08rif_f08_retail_inventory_freshness_turn_diff_189d_jerk_v047_signal,
    f08rif_f08_retail_inventory_freshness_turn_diff_252d_jerk_v048_signal,
    f08rif_f08_retail_inventory_freshness_turn_diff_378d_jerk_v049_signal,
    f08rif_f08_retail_inventory_freshness_turn_diff_504d_jerk_v050_signal,
    f08rif_f08_retail_inventory_freshness_fresh_5d_jerk_v051_signal,
    f08rif_f08_retail_inventory_freshness_fresh_10d_jerk_v052_signal,
    f08rif_f08_retail_inventory_freshness_fresh_21d_jerk_v053_signal,
    f08rif_f08_retail_inventory_freshness_fresh_42d_jerk_v054_signal,
    f08rif_f08_retail_inventory_freshness_fresh_63d_jerk_v055_signal,
    f08rif_f08_retail_inventory_freshness_fresh_126d_jerk_v056_signal,
    f08rif_f08_retail_inventory_freshness_fresh_189d_jerk_v057_signal,
    f08rif_f08_retail_inventory_freshness_fresh_252d_jerk_v058_signal,
    f08rif_f08_retail_inventory_freshness_fresh_378d_jerk_v059_signal,
    f08rif_f08_retail_inventory_freshness_fresh_504d_jerk_v060_signal,
    f08rif_f08_retail_inventory_freshness_fresh_mean_5d_jerk_v061_signal,
    f08rif_f08_retail_inventory_freshness_fresh_mean_10d_jerk_v062_signal,
    f08rif_f08_retail_inventory_freshness_fresh_mean_21d_jerk_v063_signal,
    f08rif_f08_retail_inventory_freshness_fresh_mean_42d_jerk_v064_signal,
    f08rif_f08_retail_inventory_freshness_fresh_mean_63d_jerk_v065_signal,
    f08rif_f08_retail_inventory_freshness_fresh_mean_126d_jerk_v066_signal,
    f08rif_f08_retail_inventory_freshness_fresh_mean_189d_jerk_v067_signal,
    f08rif_f08_retail_inventory_freshness_fresh_mean_252d_jerk_v068_signal,
    f08rif_f08_retail_inventory_freshness_fresh_mean_378d_jerk_v069_signal,
    f08rif_f08_retail_inventory_freshness_fresh_mean_504d_jerk_v070_signal,
    f08rif_f08_retail_inventory_freshness_fresh_std_5d_jerk_v071_signal,
    f08rif_f08_retail_inventory_freshness_fresh_std_10d_jerk_v072_signal,
    f08rif_f08_retail_inventory_freshness_fresh_std_21d_jerk_v073_signal,
    f08rif_f08_retail_inventory_freshness_fresh_std_42d_jerk_v074_signal,
    f08rif_f08_retail_inventory_freshness_fresh_std_63d_jerk_v075_signal,
    f08rif_f08_retail_inventory_freshness_fresh_std_126d_jerk_v076_signal,
    f08rif_f08_retail_inventory_freshness_fresh_std_189d_jerk_v077_signal,
    f08rif_f08_retail_inventory_freshness_fresh_std_252d_jerk_v078_signal,
    f08rif_f08_retail_inventory_freshness_fresh_std_378d_jerk_v079_signal,
    f08rif_f08_retail_inventory_freshness_fresh_std_504d_jerk_v080_signal,
    f08rif_f08_retail_inventory_freshness_fresh_z_5d_jerk_v081_signal,
    f08rif_f08_retail_inventory_freshness_fresh_z_10d_jerk_v082_signal,
    f08rif_f08_retail_inventory_freshness_fresh_z_21d_jerk_v083_signal,
    f08rif_f08_retail_inventory_freshness_fresh_z_42d_jerk_v084_signal,
    f08rif_f08_retail_inventory_freshness_fresh_z_63d_jerk_v085_signal,
    f08rif_f08_retail_inventory_freshness_fresh_z_126d_jerk_v086_signal,
    f08rif_f08_retail_inventory_freshness_fresh_z_189d_jerk_v087_signal,
    f08rif_f08_retail_inventory_freshness_fresh_z_252d_jerk_v088_signal,
    f08rif_f08_retail_inventory_freshness_fresh_z_378d_jerk_v089_signal,
    f08rif_f08_retail_inventory_freshness_fresh_z_504d_jerk_v090_signal,
    f08rif_f08_retail_inventory_freshness_fresh_ema_5d_jerk_v091_signal,
    f08rif_f08_retail_inventory_freshness_fresh_ema_10d_jerk_v092_signal,
    f08rif_f08_retail_inventory_freshness_fresh_ema_21d_jerk_v093_signal,
    f08rif_f08_retail_inventory_freshness_fresh_ema_42d_jerk_v094_signal,
    f08rif_f08_retail_inventory_freshness_fresh_ema_63d_jerk_v095_signal,
    f08rif_f08_retail_inventory_freshness_fresh_ema_126d_jerk_v096_signal,
    f08rif_f08_retail_inventory_freshness_fresh_ema_189d_jerk_v097_signal,
    f08rif_f08_retail_inventory_freshness_fresh_ema_252d_jerk_v098_signal,
    f08rif_f08_retail_inventory_freshness_fresh_ema_378d_jerk_v099_signal,
    f08rif_f08_retail_inventory_freshness_fresh_ema_504d_jerk_v100_signal,
    f08rif_f08_retail_inventory_freshness_velo_5d_jerk_v101_signal,
    f08rif_f08_retail_inventory_freshness_velo_10d_jerk_v102_signal,
    f08rif_f08_retail_inventory_freshness_velo_21d_jerk_v103_signal,
    f08rif_f08_retail_inventory_freshness_velo_42d_jerk_v104_signal,
    f08rif_f08_retail_inventory_freshness_velo_63d_jerk_v105_signal,
    f08rif_f08_retail_inventory_freshness_velo_126d_jerk_v106_signal,
    f08rif_f08_retail_inventory_freshness_velo_189d_jerk_v107_signal,
    f08rif_f08_retail_inventory_freshness_velo_252d_jerk_v108_signal,
    f08rif_f08_retail_inventory_freshness_velo_378d_jerk_v109_signal,
    f08rif_f08_retail_inventory_freshness_velo_504d_jerk_v110_signal,
    f08rif_f08_retail_inventory_freshness_velo_mean_5d_jerk_v111_signal,
    f08rif_f08_retail_inventory_freshness_velo_mean_10d_jerk_v112_signal,
    f08rif_f08_retail_inventory_freshness_velo_mean_21d_jerk_v113_signal,
    f08rif_f08_retail_inventory_freshness_velo_mean_42d_jerk_v114_signal,
    f08rif_f08_retail_inventory_freshness_velo_mean_63d_jerk_v115_signal,
    f08rif_f08_retail_inventory_freshness_velo_mean_126d_jerk_v116_signal,
    f08rif_f08_retail_inventory_freshness_velo_mean_189d_jerk_v117_signal,
    f08rif_f08_retail_inventory_freshness_velo_mean_252d_jerk_v118_signal,
    f08rif_f08_retail_inventory_freshness_velo_mean_378d_jerk_v119_signal,
    f08rif_f08_retail_inventory_freshness_velo_mean_504d_jerk_v120_signal,
    f08rif_f08_retail_inventory_freshness_velo_std_5d_jerk_v121_signal,
    f08rif_f08_retail_inventory_freshness_velo_std_10d_jerk_v122_signal,
    f08rif_f08_retail_inventory_freshness_velo_std_21d_jerk_v123_signal,
    f08rif_f08_retail_inventory_freshness_velo_std_42d_jerk_v124_signal,
    f08rif_f08_retail_inventory_freshness_velo_std_63d_jerk_v125_signal,
    f08rif_f08_retail_inventory_freshness_velo_std_126d_jerk_v126_signal,
    f08rif_f08_retail_inventory_freshness_velo_std_189d_jerk_v127_signal,
    f08rif_f08_retail_inventory_freshness_velo_std_252d_jerk_v128_signal,
    f08rif_f08_retail_inventory_freshness_velo_std_378d_jerk_v129_signal,
    f08rif_f08_retail_inventory_freshness_velo_std_504d_jerk_v130_signal,
    f08rif_f08_retail_inventory_freshness_velo_xrev_5d_jerk_v131_signal,
    f08rif_f08_retail_inventory_freshness_velo_xrev_10d_jerk_v132_signal,
    f08rif_f08_retail_inventory_freshness_velo_xrev_21d_jerk_v133_signal,
    f08rif_f08_retail_inventory_freshness_velo_xrev_42d_jerk_v134_signal,
    f08rif_f08_retail_inventory_freshness_velo_xrev_63d_jerk_v135_signal,
    f08rif_f08_retail_inventory_freshness_velo_xrev_126d_jerk_v136_signal,
    f08rif_f08_retail_inventory_freshness_velo_xrev_189d_jerk_v137_signal,
    f08rif_f08_retail_inventory_freshness_velo_xrev_252d_jerk_v138_signal,
    f08rif_f08_retail_inventory_freshness_velo_xrev_378d_jerk_v139_signal,
    f08rif_f08_retail_inventory_freshness_velo_xrev_504d_jerk_v140_signal,
    f08rif_f08_retail_inventory_freshness_velo_xinv_5d_jerk_v141_signal,
    f08rif_f08_retail_inventory_freshness_velo_xinv_10d_jerk_v142_signal,
    f08rif_f08_retail_inventory_freshness_velo_xinv_21d_jerk_v143_signal,
    f08rif_f08_retail_inventory_freshness_velo_xinv_42d_jerk_v144_signal,
    f08rif_f08_retail_inventory_freshness_velo_xinv_63d_jerk_v145_signal,
    f08rif_f08_retail_inventory_freshness_velo_xinv_126d_jerk_v146_signal,
    f08rif_f08_retail_inventory_freshness_velo_xinv_189d_jerk_v147_signal,
    f08rif_f08_retail_inventory_freshness_velo_xinv_252d_jerk_v148_signal,
    f08rif_f08_retail_inventory_freshness_velo_xinv_378d_jerk_v149_signal,
    f08rif_f08_retail_inventory_freshness_velo_xinv_504d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F08_RETAIL_INVENTORY_FRESHNESS_REGISTRY_JERK_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f08_retail_inventory_freshness_jerk_001_150_claude: {n_features} features pass")
