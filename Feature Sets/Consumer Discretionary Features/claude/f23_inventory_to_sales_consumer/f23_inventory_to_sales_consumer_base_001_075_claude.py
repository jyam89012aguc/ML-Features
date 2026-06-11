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
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


# ===== folder domain primitives =====
def _f23_inv_days(inventory, cor):
    return inventory / cor.replace(0, np.nan) * 365.0


def _f23_inv_sales_gap(inventory, revenue, w):
    ig = inventory.pct_change(periods=w)
    sg = revenue.pct_change(periods=w)
    return ig - sg


def _f23_inv_dynamics(inventory, revenue, cor, w):
    days = inventory / cor.replace(0, np.nan) * 365.0
    m = days.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = days.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)
    z = (days - m) / sd
    gap = inventory.pct_change(periods=w) - revenue.pct_change(periods=w)
    return z + gap

# ===== features =====

def f23iss_f23_inventory_to_sales_consumer_invdays_5d_base_v001_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _mean(base, 5) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdays_10d_base_v002_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _mean(base, 10) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdays_21d_base_v003_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _mean(base, 21) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdays_42d_base_v004_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _mean(base, 42) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdays_63d_base_v005_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _mean(base, 63) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdays_84d_base_v006_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _mean(base, 84) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdays_126d_base_v007_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _mean(base, 126) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdays_168d_base_v008_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _mean(base, 168) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdays_189d_base_v009_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _mean(base, 189) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdays_252d_base_v010_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _mean(base, 252) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdays_315d_base_v011_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _mean(base, 315) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdays_378d_base_v012_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _mean(base, 378) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdays_504d_base_v013_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _mean(base, 504) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysstd_5d_base_v014_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _std(base, 5) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysstd_10d_base_v015_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _std(base, 10) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysstd_21d_base_v016_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _std(base, 21) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysstd_42d_base_v017_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _std(base, 42) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysstd_63d_base_v018_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _std(base, 63) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysstd_84d_base_v019_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _std(base, 84) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysstd_126d_base_v020_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _std(base, 126) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysstd_168d_base_v021_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _std(base, 168) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysstd_189d_base_v022_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _std(base, 189) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysstd_252d_base_v023_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _std(base, 252) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysstd_315d_base_v024_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _std(base, 315) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysstd_378d_base_v025_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _std(base, 378) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysstd_504d_base_v026_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _std(base, 504) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgap_5d_base_v027_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgap_10d_base_v028_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgap_21d_base_v029_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgap_42d_base_v030_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgap_63d_base_v031_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgap_84d_base_v032_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 84)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgap_126d_base_v033_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgap_168d_base_v034_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 168)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgap_189d_base_v035_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgap_252d_base_v036_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgap_315d_base_v037_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 315)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgap_378d_base_v038_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgap_504d_base_v039_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_5d_base_v040_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 5)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_10d_base_v041_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 10)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_21d_base_v042_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_42d_base_v043_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 42)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_63d_base_v044_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_84d_base_v045_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 84)
    result = _mean(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_126d_base_v046_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 126)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_168d_base_v047_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 168)
    result = _mean(base, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_189d_base_v048_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 189)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_252d_base_v049_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_315d_base_v050_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 315)
    result = _mean(base, 315) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_378d_base_v051_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 378)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_504d_base_v052_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 504)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_5d_base_v053_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 5)
    result = _std(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_10d_base_v054_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 10)
    result = _std(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_21d_base_v055_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_42d_base_v056_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 42)
    result = _std(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_63d_base_v057_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_84d_base_v058_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 84)
    result = _std(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_126d_base_v059_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 126)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_168d_base_v060_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 168)
    result = _std(base, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_189d_base_v061_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 189)
    result = _std(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_252d_base_v062_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 252)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_315d_base_v063_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 315)
    result = _std(base, 315) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_378d_base_v064_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 378)
    result = _std(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_504d_base_v065_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 504)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdyn_5d_base_v066_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdyn_10d_base_v067_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdyn_21d_base_v068_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdyn_42d_base_v069_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdyn_63d_base_v070_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdyn_84d_base_v071_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 84)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdyn_126d_base_v072_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdyn_168d_base_v073_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 168)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdyn_189d_base_v074_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdyn_252d_base_v075_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f23iss_f23_inventory_to_sales_consumer_invdays_5d_base_v001_signal,
    f23iss_f23_inventory_to_sales_consumer_invdays_10d_base_v002_signal,
    f23iss_f23_inventory_to_sales_consumer_invdays_21d_base_v003_signal,
    f23iss_f23_inventory_to_sales_consumer_invdays_42d_base_v004_signal,
    f23iss_f23_inventory_to_sales_consumer_invdays_63d_base_v005_signal,
    f23iss_f23_inventory_to_sales_consumer_invdays_84d_base_v006_signal,
    f23iss_f23_inventory_to_sales_consumer_invdays_126d_base_v007_signal,
    f23iss_f23_inventory_to_sales_consumer_invdays_168d_base_v008_signal,
    f23iss_f23_inventory_to_sales_consumer_invdays_189d_base_v009_signal,
    f23iss_f23_inventory_to_sales_consumer_invdays_252d_base_v010_signal,
    f23iss_f23_inventory_to_sales_consumer_invdays_315d_base_v011_signal,
    f23iss_f23_inventory_to_sales_consumer_invdays_378d_base_v012_signal,
    f23iss_f23_inventory_to_sales_consumer_invdays_504d_base_v013_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysstd_5d_base_v014_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysstd_10d_base_v015_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysstd_21d_base_v016_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysstd_42d_base_v017_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysstd_63d_base_v018_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysstd_84d_base_v019_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysstd_126d_base_v020_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysstd_168d_base_v021_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysstd_189d_base_v022_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysstd_252d_base_v023_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysstd_315d_base_v024_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysstd_378d_base_v025_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysstd_504d_base_v026_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgap_5d_base_v027_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgap_10d_base_v028_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgap_21d_base_v029_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgap_42d_base_v030_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgap_63d_base_v031_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgap_84d_base_v032_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgap_126d_base_v033_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgap_168d_base_v034_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgap_189d_base_v035_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgap_252d_base_v036_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgap_315d_base_v037_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgap_378d_base_v038_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgap_504d_base_v039_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_5d_base_v040_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_10d_base_v041_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_21d_base_v042_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_42d_base_v043_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_63d_base_v044_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_84d_base_v045_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_126d_base_v046_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_168d_base_v047_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_189d_base_v048_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_252d_base_v049_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_315d_base_v050_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_378d_base_v051_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_504d_base_v052_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_5d_base_v053_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_10d_base_v054_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_21d_base_v055_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_42d_base_v056_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_63d_base_v057_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_84d_base_v058_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_126d_base_v059_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_168d_base_v060_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_189d_base_v061_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_252d_base_v062_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_315d_base_v063_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_378d_base_v064_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_504d_base_v065_signal,
    f23iss_f23_inventory_to_sales_consumer_invdyn_5d_base_v066_signal,
    f23iss_f23_inventory_to_sales_consumer_invdyn_10d_base_v067_signal,
    f23iss_f23_inventory_to_sales_consumer_invdyn_21d_base_v068_signal,
    f23iss_f23_inventory_to_sales_consumer_invdyn_42d_base_v069_signal,
    f23iss_f23_inventory_to_sales_consumer_invdyn_63d_base_v070_signal,
    f23iss_f23_inventory_to_sales_consumer_invdyn_84d_base_v071_signal,
    f23iss_f23_inventory_to_sales_consumer_invdyn_126d_base_v072_signal,
    f23iss_f23_inventory_to_sales_consumer_invdyn_168d_base_v073_signal,
    f23iss_f23_inventory_to_sales_consumer_invdyn_189d_base_v074_signal,
    f23iss_f23_inventory_to_sales_consumer_invdyn_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F23_INVENTORY_TO_SALES_CONSUMER_REGISTRY_001_075 = REGISTRY


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
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "inventory": inventory,
        "cor": cor,
        "closeadj": closeadj,
        "revenue": revenue,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f23_inv_days", "_f23_inv_sales_gap", "_f23_inv_dynamics",)
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
    print(f"OK f23_inventory_to_sales_consumer_base_001_075_claude: {n_features} features pass")
