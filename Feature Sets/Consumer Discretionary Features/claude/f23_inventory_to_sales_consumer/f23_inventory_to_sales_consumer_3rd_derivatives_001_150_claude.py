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

def f23iss_f23_inventory_to_sales_consumer_invdays_5d_jw5_jerk_v001_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _mean(base, 5) * (closeadj / 100.0)
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdays_10d_jw10_jerk_v002_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _mean(base, 10) * (closeadj / 100.0)
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdays_21d_jw21_jerk_v003_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _mean(base, 21) * (closeadj / 100.0)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdays_42d_jw42_jerk_v004_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _mean(base, 42) * (closeadj / 100.0)
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdays_63d_jw63_jerk_v005_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _mean(base, 63) * (closeadj / 100.0)
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdays_84d_jw126_jerk_v006_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _mean(base, 84) * (closeadj / 100.0)
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdays_126d_jw5_jerk_v007_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _mean(base, 126) * (closeadj / 100.0)
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdays_168d_jw10_jerk_v008_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _mean(base, 168) * (closeadj / 100.0)
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdays_189d_jw21_jerk_v009_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _mean(base, 189) * (closeadj / 100.0)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdays_252d_jw42_jerk_v010_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _mean(base, 252) * (closeadj / 100.0)
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdays_315d_jw63_jerk_v011_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _mean(base, 315) * (closeadj / 100.0)
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdays_378d_jw126_jerk_v012_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _mean(base, 378) * (closeadj / 100.0)
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdays_504d_jw5_jerk_v013_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _mean(base, 504) * (closeadj / 100.0)
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysstd_5d_jw10_jerk_v014_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _std(base, 5) * (closeadj / 100.0)
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysstd_10d_jw21_jerk_v015_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _std(base, 10) * (closeadj / 100.0)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysstd_21d_jw42_jerk_v016_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _std(base, 21) * (closeadj / 100.0)
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysstd_42d_jw63_jerk_v017_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _std(base, 42) * (closeadj / 100.0)
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysstd_63d_jw126_jerk_v018_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _std(base, 63) * (closeadj / 100.0)
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysstd_84d_jw5_jerk_v019_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _std(base, 84) * (closeadj / 100.0)
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysstd_126d_jw10_jerk_v020_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _std(base, 126) * (closeadj / 100.0)
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysstd_168d_jw21_jerk_v021_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _std(base, 168) * (closeadj / 100.0)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysstd_189d_jw42_jerk_v022_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _std(base, 189) * (closeadj / 100.0)
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysstd_252d_jw63_jerk_v023_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _std(base, 252) * (closeadj / 100.0)
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysstd_315d_jw126_jerk_v024_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _std(base, 315) * (closeadj / 100.0)
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysstd_378d_jw5_jerk_v025_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _std(base, 378) * (closeadj / 100.0)
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysstd_504d_jw10_jerk_v026_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _std(base, 504) * (closeadj / 100.0)
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgap_5d_jw21_jerk_v027_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 5)
    result = base * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgap_10d_jw42_jerk_v028_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 10)
    result = base * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgap_21d_jw63_jerk_v029_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 21)
    result = base * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgap_42d_jw126_jerk_v030_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 42)
    result = base * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgap_63d_jw5_jerk_v031_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 63)
    result = base * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgap_84d_jw10_jerk_v032_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 84)
    result = base * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgap_126d_jw21_jerk_v033_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 126)
    result = base * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgap_168d_jw42_jerk_v034_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 168)
    result = base * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgap_189d_jw63_jerk_v035_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 189)
    result = base * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgap_252d_jw126_jerk_v036_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 252)
    result = base * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgap_315d_jw5_jerk_v037_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 315)
    result = base * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgap_378d_jw10_jerk_v038_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 378)
    result = base * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgap_504d_jw21_jerk_v039_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 504)
    result = base * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_5d_jw42_jerk_v040_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 5)
    result = _mean(base, 5) * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_10d_jw63_jerk_v041_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 10)
    result = _mean(base, 10) * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_21d_jw126_jerk_v042_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 21)
    result = _mean(base, 21) * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_42d_jw5_jerk_v043_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 42)
    result = _mean(base, 42) * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_63d_jw10_jerk_v044_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 63)
    result = _mean(base, 63) * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_84d_jw21_jerk_v045_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 84)
    result = _mean(base, 84) * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_126d_jw42_jerk_v046_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 126)
    result = _mean(base, 126) * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_168d_jw63_jerk_v047_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 168)
    result = _mean(base, 168) * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_189d_jw126_jerk_v048_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 189)
    result = _mean(base, 189) * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_252d_jw5_jerk_v049_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 252)
    result = _mean(base, 252) * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_315d_jw10_jerk_v050_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 315)
    result = _mean(base, 315) * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_378d_jw21_jerk_v051_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 378)
    result = _mean(base, 378) * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_504d_jw42_jerk_v052_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 504)
    result = _mean(base, 504) * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_5d_jw63_jerk_v053_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 5)
    result = _std(base, 5) * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_10d_jw126_jerk_v054_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 10)
    result = _std(base, 10) * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_21d_jw5_jerk_v055_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 21)
    result = _std(base, 21) * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_42d_jw10_jerk_v056_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 42)
    result = _std(base, 42) * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_63d_jw21_jerk_v057_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 63)
    result = _std(base, 63) * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_84d_jw42_jerk_v058_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 84)
    result = _std(base, 84) * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_126d_jw63_jerk_v059_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 126)
    result = _std(base, 126) * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_168d_jw126_jerk_v060_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 168)
    result = _std(base, 168) * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_189d_jw5_jerk_v061_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 189)
    result = _std(base, 189) * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_252d_jw10_jerk_v062_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 252)
    result = _std(base, 252) * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_315d_jw21_jerk_v063_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 315)
    result = _std(base, 315) * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_378d_jw42_jerk_v064_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 378)
    result = _std(base, 378) * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_504d_jw63_jerk_v065_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 504)
    result = _std(base, 504) * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdyn_5d_jw126_jerk_v066_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 5)
    result = base * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdyn_10d_jw5_jerk_v067_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 10)
    result = base * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdyn_21d_jw10_jerk_v068_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 21)
    result = base * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdyn_42d_jw21_jerk_v069_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 42)
    result = base * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdyn_63d_jw42_jerk_v070_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 63)
    result = base * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdyn_84d_jw63_jerk_v071_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 84)
    result = base * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdyn_126d_jw126_jerk_v072_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 126)
    result = base * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdyn_168d_jw5_jerk_v073_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 168)
    result = base * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdyn_189d_jw10_jerk_v074_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 189)
    result = base * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdyn_252d_jw21_jerk_v075_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 252)
    result = base * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdyn_315d_jw42_jerk_v076_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 315)
    result = base * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdyn_378d_jw63_jerk_v077_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 378)
    result = base * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdyn_504d_jw126_jerk_v078_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 504)
    result = base * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdynema_5d_jw5_jerk_v079_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 5)
    result = _ema(base, 5) * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdynema_10d_jw10_jerk_v080_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 10)
    result = _ema(base, 10) * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdynema_21d_jw21_jerk_v081_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 21)
    result = _ema(base, 21) * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdynema_42d_jw42_jerk_v082_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 42)
    result = _ema(base, 42) * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdynema_63d_jw63_jerk_v083_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 63)
    result = _ema(base, 63) * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdynema_84d_jw126_jerk_v084_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 84)
    result = _ema(base, 84) * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdynema_126d_jw5_jerk_v085_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 126)
    result = _ema(base, 126) * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdynema_168d_jw10_jerk_v086_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 168)
    result = _ema(base, 168) * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdynema_189d_jw21_jerk_v087_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 189)
    result = _ema(base, 189) * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdynema_252d_jw42_jerk_v088_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 252)
    result = _ema(base, 252) * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdynema_315d_jw63_jerk_v089_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 315)
    result = _ema(base, 315) * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdynema_378d_jw126_jerk_v090_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 378)
    result = _ema(base, 378) * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdynema_504d_jw5_jerk_v091_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 504)
    result = _ema(base, 504) * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapabs_5d_jw10_jerk_v092_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 5)
    result = base.abs() * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapabs_10d_jw21_jerk_v093_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 10)
    result = base.abs() * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapabs_21d_jw42_jerk_v094_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 21)
    result = base.abs() * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapabs_42d_jw63_jerk_v095_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 42)
    result = base.abs() * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapabs_63d_jw126_jerk_v096_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 63)
    result = base.abs() * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapabs_84d_jw5_jerk_v097_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 84)
    result = base.abs() * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapabs_126d_jw10_jerk_v098_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 126)
    result = base.abs() * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapabs_168d_jw21_jerk_v099_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 168)
    result = base.abs() * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapabs_189d_jw42_jerk_v100_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 189)
    result = base.abs() * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapabs_252d_jw63_jerk_v101_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 252)
    result = base.abs() * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapabs_315d_jw126_jerk_v102_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 315)
    result = base.abs() * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapabs_378d_jw5_jerk_v103_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 378)
    result = base.abs() * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invsalesgapabs_504d_jw10_jerk_v104_signal(inventory, revenue, closeadj):
    base = _f23_inv_sales_gap(inventory, revenue, 504)
    result = base.abs() * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysxrev_5d_jw21_jerk_v105_signal(inventory, cor, revenue, closeadj):
    base = _f23_inv_days(inventory, cor)
    rg = revenue.pct_change(periods=5)
    result = base * rg * (closeadj / 100.0)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysxrev_10d_jw42_jerk_v106_signal(inventory, cor, revenue, closeadj):
    base = _f23_inv_days(inventory, cor)
    rg = revenue.pct_change(periods=10)
    result = base * rg * (closeadj / 100.0)
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysxrev_21d_jw63_jerk_v107_signal(inventory, cor, revenue, closeadj):
    base = _f23_inv_days(inventory, cor)
    rg = revenue.pct_change(periods=21)
    result = base * rg * (closeadj / 100.0)
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysxrev_42d_jw126_jerk_v108_signal(inventory, cor, revenue, closeadj):
    base = _f23_inv_days(inventory, cor)
    rg = revenue.pct_change(periods=42)
    result = base * rg * (closeadj / 100.0)
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysxrev_63d_jw5_jerk_v109_signal(inventory, cor, revenue, closeadj):
    base = _f23_inv_days(inventory, cor)
    rg = revenue.pct_change(periods=63)
    result = base * rg * (closeadj / 100.0)
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysxrev_84d_jw10_jerk_v110_signal(inventory, cor, revenue, closeadj):
    base = _f23_inv_days(inventory, cor)
    rg = revenue.pct_change(periods=84)
    result = base * rg * (closeadj / 100.0)
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysxrev_126d_jw21_jerk_v111_signal(inventory, cor, revenue, closeadj):
    base = _f23_inv_days(inventory, cor)
    rg = revenue.pct_change(periods=126)
    result = base * rg * (closeadj / 100.0)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysxrev_168d_jw42_jerk_v112_signal(inventory, cor, revenue, closeadj):
    base = _f23_inv_days(inventory, cor)
    rg = revenue.pct_change(periods=168)
    result = base * rg * (closeadj / 100.0)
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysxrev_189d_jw63_jerk_v113_signal(inventory, cor, revenue, closeadj):
    base = _f23_inv_days(inventory, cor)
    rg = revenue.pct_change(periods=189)
    result = base * rg * (closeadj / 100.0)
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysxrev_252d_jw126_jerk_v114_signal(inventory, cor, revenue, closeadj):
    base = _f23_inv_days(inventory, cor)
    rg = revenue.pct_change(periods=252)
    result = base * rg * (closeadj / 100.0)
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysxrev_315d_jw5_jerk_v115_signal(inventory, cor, revenue, closeadj):
    base = _f23_inv_days(inventory, cor)
    rg = revenue.pct_change(periods=315)
    result = base * rg * (closeadj / 100.0)
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysxrev_378d_jw10_jerk_v116_signal(inventory, cor, revenue, closeadj):
    base = _f23_inv_days(inventory, cor)
    rg = revenue.pct_change(periods=378)
    result = base * rg * (closeadj / 100.0)
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysxrev_504d_jw21_jerk_v117_signal(inventory, cor, revenue, closeadj):
    base = _f23_inv_days(inventory, cor)
    rg = revenue.pct_change(periods=504)
    result = base * rg * (closeadj / 100.0)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysz_5d_jw42_jerk_v118_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _z(base, 5) * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysz_10d_jw63_jerk_v119_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _z(base, 10) * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysz_21d_jw126_jerk_v120_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _z(base, 21) * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysz_42d_jw5_jerk_v121_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _z(base, 42) * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysz_63d_jw10_jerk_v122_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _z(base, 63) * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysz_84d_jw21_jerk_v123_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _z(base, 84) * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysz_126d_jw42_jerk_v124_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _z(base, 126) * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysz_168d_jw63_jerk_v125_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _z(base, 168) * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysz_189d_jw126_jerk_v126_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _z(base, 189) * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysz_252d_jw5_jerk_v127_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _z(base, 252) * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysz_315d_jw10_jerk_v128_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _z(base, 315) * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysz_378d_jw21_jerk_v129_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _z(base, 378) * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysz_504d_jw42_jerk_v130_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _z(base, 504) * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdyn_z_5d_jw63_jerk_v131_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 5)
    result = _z(base, 5) * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdyn_z_10d_jw126_jerk_v132_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 10)
    result = _z(base, 10) * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdyn_z_21d_jw5_jerk_v133_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 21)
    result = _z(base, 21) * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdyn_z_42d_jw10_jerk_v134_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 42)
    result = _z(base, 42) * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdyn_z_63d_jw21_jerk_v135_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 63)
    result = _z(base, 63) * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdyn_z_84d_jw42_jerk_v136_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 84)
    result = _z(base, 84) * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdyn_z_126d_jw63_jerk_v137_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 126)
    result = _z(base, 126) * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdyn_z_168d_jw126_jerk_v138_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 168)
    result = _z(base, 168) * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdyn_z_189d_jw5_jerk_v139_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 189)
    result = _z(base, 189) * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdyn_z_252d_jw10_jerk_v140_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 252)
    result = _z(base, 252) * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdyn_z_315d_jw21_jerk_v141_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 315)
    result = _z(base, 315) * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdyn_z_378d_jw42_jerk_v142_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 378)
    result = _z(base, 378) * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdyn_z_504d_jw63_jerk_v143_signal(inventory, revenue, cor, closeadj):
    base = _f23_inv_dynamics(inventory, revenue, cor, 504)
    result = _z(base, 504) * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysema_5d_jw126_jerk_v144_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _ema(base, 5) * (closeadj / 100.0)
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysema_10d_jw5_jerk_v145_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _ema(base, 10) * (closeadj / 100.0)
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysema_21d_jw10_jerk_v146_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _ema(base, 21) * (closeadj / 100.0)
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysema_42d_jw21_jerk_v147_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _ema(base, 42) * (closeadj / 100.0)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysema_63d_jw42_jerk_v148_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _ema(base, 63) * (closeadj / 100.0)
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysema_84d_jw63_jerk_v149_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _ema(base, 84) * (closeadj / 100.0)
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23iss_f23_inventory_to_sales_consumer_invdaysema_126d_jw126_jerk_v150_signal(inventory, cor, closeadj):
    base = _f23_inv_days(inventory, cor)
    result = _ema(base, 126) * (closeadj / 100.0)
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f23iss_f23_inventory_to_sales_consumer_invdays_5d_jw5_jerk_v001_signal,
    f23iss_f23_inventory_to_sales_consumer_invdays_10d_jw10_jerk_v002_signal,
    f23iss_f23_inventory_to_sales_consumer_invdays_21d_jw21_jerk_v003_signal,
    f23iss_f23_inventory_to_sales_consumer_invdays_42d_jw42_jerk_v004_signal,
    f23iss_f23_inventory_to_sales_consumer_invdays_63d_jw63_jerk_v005_signal,
    f23iss_f23_inventory_to_sales_consumer_invdays_84d_jw126_jerk_v006_signal,
    f23iss_f23_inventory_to_sales_consumer_invdays_126d_jw5_jerk_v007_signal,
    f23iss_f23_inventory_to_sales_consumer_invdays_168d_jw10_jerk_v008_signal,
    f23iss_f23_inventory_to_sales_consumer_invdays_189d_jw21_jerk_v009_signal,
    f23iss_f23_inventory_to_sales_consumer_invdays_252d_jw42_jerk_v010_signal,
    f23iss_f23_inventory_to_sales_consumer_invdays_315d_jw63_jerk_v011_signal,
    f23iss_f23_inventory_to_sales_consumer_invdays_378d_jw126_jerk_v012_signal,
    f23iss_f23_inventory_to_sales_consumer_invdays_504d_jw5_jerk_v013_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysstd_5d_jw10_jerk_v014_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysstd_10d_jw21_jerk_v015_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysstd_21d_jw42_jerk_v016_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysstd_42d_jw63_jerk_v017_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysstd_63d_jw126_jerk_v018_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysstd_84d_jw5_jerk_v019_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysstd_126d_jw10_jerk_v020_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysstd_168d_jw21_jerk_v021_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysstd_189d_jw42_jerk_v022_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysstd_252d_jw63_jerk_v023_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysstd_315d_jw126_jerk_v024_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysstd_378d_jw5_jerk_v025_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysstd_504d_jw10_jerk_v026_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgap_5d_jw21_jerk_v027_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgap_10d_jw42_jerk_v028_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgap_21d_jw63_jerk_v029_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgap_42d_jw126_jerk_v030_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgap_63d_jw5_jerk_v031_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgap_84d_jw10_jerk_v032_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgap_126d_jw21_jerk_v033_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgap_168d_jw42_jerk_v034_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgap_189d_jw63_jerk_v035_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgap_252d_jw126_jerk_v036_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgap_315d_jw5_jerk_v037_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgap_378d_jw10_jerk_v038_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgap_504d_jw21_jerk_v039_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_5d_jw42_jerk_v040_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_10d_jw63_jerk_v041_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_21d_jw126_jerk_v042_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_42d_jw5_jerk_v043_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_63d_jw10_jerk_v044_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_84d_jw21_jerk_v045_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_126d_jw42_jerk_v046_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_168d_jw63_jerk_v047_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_189d_jw126_jerk_v048_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_252d_jw5_jerk_v049_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_315d_jw10_jerk_v050_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_378d_jw21_jerk_v051_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapmean_504d_jw42_jerk_v052_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_5d_jw63_jerk_v053_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_10d_jw126_jerk_v054_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_21d_jw5_jerk_v055_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_42d_jw10_jerk_v056_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_63d_jw21_jerk_v057_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_84d_jw42_jerk_v058_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_126d_jw63_jerk_v059_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_168d_jw126_jerk_v060_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_189d_jw5_jerk_v061_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_252d_jw10_jerk_v062_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_315d_jw21_jerk_v063_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_378d_jw42_jerk_v064_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapstd_504d_jw63_jerk_v065_signal,
    f23iss_f23_inventory_to_sales_consumer_invdyn_5d_jw126_jerk_v066_signal,
    f23iss_f23_inventory_to_sales_consumer_invdyn_10d_jw5_jerk_v067_signal,
    f23iss_f23_inventory_to_sales_consumer_invdyn_21d_jw10_jerk_v068_signal,
    f23iss_f23_inventory_to_sales_consumer_invdyn_42d_jw21_jerk_v069_signal,
    f23iss_f23_inventory_to_sales_consumer_invdyn_63d_jw42_jerk_v070_signal,
    f23iss_f23_inventory_to_sales_consumer_invdyn_84d_jw63_jerk_v071_signal,
    f23iss_f23_inventory_to_sales_consumer_invdyn_126d_jw126_jerk_v072_signal,
    f23iss_f23_inventory_to_sales_consumer_invdyn_168d_jw5_jerk_v073_signal,
    f23iss_f23_inventory_to_sales_consumer_invdyn_189d_jw10_jerk_v074_signal,
    f23iss_f23_inventory_to_sales_consumer_invdyn_252d_jw21_jerk_v075_signal,
    f23iss_f23_inventory_to_sales_consumer_invdyn_315d_jw42_jerk_v076_signal,
    f23iss_f23_inventory_to_sales_consumer_invdyn_378d_jw63_jerk_v077_signal,
    f23iss_f23_inventory_to_sales_consumer_invdyn_504d_jw126_jerk_v078_signal,
    f23iss_f23_inventory_to_sales_consumer_invdynema_5d_jw5_jerk_v079_signal,
    f23iss_f23_inventory_to_sales_consumer_invdynema_10d_jw10_jerk_v080_signal,
    f23iss_f23_inventory_to_sales_consumer_invdynema_21d_jw21_jerk_v081_signal,
    f23iss_f23_inventory_to_sales_consumer_invdynema_42d_jw42_jerk_v082_signal,
    f23iss_f23_inventory_to_sales_consumer_invdynema_63d_jw63_jerk_v083_signal,
    f23iss_f23_inventory_to_sales_consumer_invdynema_84d_jw126_jerk_v084_signal,
    f23iss_f23_inventory_to_sales_consumer_invdynema_126d_jw5_jerk_v085_signal,
    f23iss_f23_inventory_to_sales_consumer_invdynema_168d_jw10_jerk_v086_signal,
    f23iss_f23_inventory_to_sales_consumer_invdynema_189d_jw21_jerk_v087_signal,
    f23iss_f23_inventory_to_sales_consumer_invdynema_252d_jw42_jerk_v088_signal,
    f23iss_f23_inventory_to_sales_consumer_invdynema_315d_jw63_jerk_v089_signal,
    f23iss_f23_inventory_to_sales_consumer_invdynema_378d_jw126_jerk_v090_signal,
    f23iss_f23_inventory_to_sales_consumer_invdynema_504d_jw5_jerk_v091_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapabs_5d_jw10_jerk_v092_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapabs_10d_jw21_jerk_v093_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapabs_21d_jw42_jerk_v094_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapabs_42d_jw63_jerk_v095_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapabs_63d_jw126_jerk_v096_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapabs_84d_jw5_jerk_v097_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapabs_126d_jw10_jerk_v098_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapabs_168d_jw21_jerk_v099_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapabs_189d_jw42_jerk_v100_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapabs_252d_jw63_jerk_v101_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapabs_315d_jw126_jerk_v102_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapabs_378d_jw5_jerk_v103_signal,
    f23iss_f23_inventory_to_sales_consumer_invsalesgapabs_504d_jw10_jerk_v104_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysxrev_5d_jw21_jerk_v105_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysxrev_10d_jw42_jerk_v106_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysxrev_21d_jw63_jerk_v107_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysxrev_42d_jw126_jerk_v108_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysxrev_63d_jw5_jerk_v109_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysxrev_84d_jw10_jerk_v110_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysxrev_126d_jw21_jerk_v111_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysxrev_168d_jw42_jerk_v112_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysxrev_189d_jw63_jerk_v113_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysxrev_252d_jw126_jerk_v114_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysxrev_315d_jw5_jerk_v115_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysxrev_378d_jw10_jerk_v116_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysxrev_504d_jw21_jerk_v117_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysz_5d_jw42_jerk_v118_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysz_10d_jw63_jerk_v119_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysz_21d_jw126_jerk_v120_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysz_42d_jw5_jerk_v121_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysz_63d_jw10_jerk_v122_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysz_84d_jw21_jerk_v123_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysz_126d_jw42_jerk_v124_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysz_168d_jw63_jerk_v125_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysz_189d_jw126_jerk_v126_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysz_252d_jw5_jerk_v127_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysz_315d_jw10_jerk_v128_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysz_378d_jw21_jerk_v129_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysz_504d_jw42_jerk_v130_signal,
    f23iss_f23_inventory_to_sales_consumer_invdyn_z_5d_jw63_jerk_v131_signal,
    f23iss_f23_inventory_to_sales_consumer_invdyn_z_10d_jw126_jerk_v132_signal,
    f23iss_f23_inventory_to_sales_consumer_invdyn_z_21d_jw5_jerk_v133_signal,
    f23iss_f23_inventory_to_sales_consumer_invdyn_z_42d_jw10_jerk_v134_signal,
    f23iss_f23_inventory_to_sales_consumer_invdyn_z_63d_jw21_jerk_v135_signal,
    f23iss_f23_inventory_to_sales_consumer_invdyn_z_84d_jw42_jerk_v136_signal,
    f23iss_f23_inventory_to_sales_consumer_invdyn_z_126d_jw63_jerk_v137_signal,
    f23iss_f23_inventory_to_sales_consumer_invdyn_z_168d_jw126_jerk_v138_signal,
    f23iss_f23_inventory_to_sales_consumer_invdyn_z_189d_jw5_jerk_v139_signal,
    f23iss_f23_inventory_to_sales_consumer_invdyn_z_252d_jw10_jerk_v140_signal,
    f23iss_f23_inventory_to_sales_consumer_invdyn_z_315d_jw21_jerk_v141_signal,
    f23iss_f23_inventory_to_sales_consumer_invdyn_z_378d_jw42_jerk_v142_signal,
    f23iss_f23_inventory_to_sales_consumer_invdyn_z_504d_jw63_jerk_v143_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysema_5d_jw126_jerk_v144_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysema_10d_jw5_jerk_v145_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysema_21d_jw10_jerk_v146_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysema_42d_jw21_jerk_v147_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysema_63d_jw42_jerk_v148_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysema_84d_jw63_jerk_v149_signal,
    f23iss_f23_inventory_to_sales_consumer_invdaysema_126d_jw126_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F23_INVENTORY_TO_SALES_CONSUMER_REGISTRY_JERK_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f23_inventory_to_sales_consumer_3rd_derivatives_001_150_claude: {n_features} features pass")
