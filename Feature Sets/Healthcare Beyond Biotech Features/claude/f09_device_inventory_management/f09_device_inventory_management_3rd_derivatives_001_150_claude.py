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
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


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
def _f09_inv_turnover(inventory, cor):
    return cor / inventory.replace(0, np.nan)


def _f09_inv_to_revenue(inventory, revenue):
    return inventory / revenue.replace(0, np.nan)


def _f09_inv_dynamics(inventory, revenue, w):
    r = inventory / revenue.replace(0, np.nan)
    return r.rolling(w, min_periods=max(1, w // 2)).std()

def f09dim_f09_device_inventory_management_p0bw21xclosejw5sm_5d_jerk_v001_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor) * closeadj
    base = _mean(base, 21)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw21xclosejw21em_21d_jerk_v002_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor) * closeadj
    base = _ema(base, 21)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw21xclosejw63sm_63d_jerk_v003_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor) * closeadj
    base = _mean(base, 21)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw21xclosejw126em_126d_jerk_v004_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor) * closeadj
    base = _ema(base, 21)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw21xclosejw252sm_252d_jerk_v005_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor) * closeadj
    base = _mean(base, 21)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw21xrevjw5em_5d_jerk_v006_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor)
    base = base * closeadj
    base = _ema(base, 21)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw21xrevjw21sm_21d_jerk_v007_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor)
    base = base * closeadj
    base = _mean(base, 21)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw21xrevjw63em_63d_jerk_v008_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor)
    base = base * closeadj
    base = _ema(base, 21)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw21xrevjw126sm_126d_jerk_v009_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor)
    base = base * closeadj
    base = _mean(base, 21)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw21xrevjw252em_252d_jerk_v010_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor)
    base = base * closeadj
    base = _ema(base, 21)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw63xclosejw5sm_5d_jerk_v011_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor) * closeadj
    base = _mean(base, 63)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw63xclosejw21em_21d_jerk_v012_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor) * closeadj
    base = _ema(base, 63)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw63xclosejw63sm_63d_jerk_v013_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor) * closeadj
    base = _mean(base, 63)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw63xclosejw126em_126d_jerk_v014_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor) * closeadj
    base = _ema(base, 63)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw63xclosejw252sm_252d_jerk_v015_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor) * closeadj
    base = _mean(base, 63)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw63xrevjw5em_5d_jerk_v016_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor)
    base = base * closeadj
    base = _ema(base, 63)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw63xrevjw21sm_21d_jerk_v017_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor)
    base = base * closeadj
    base = _mean(base, 63)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw63xrevjw63em_63d_jerk_v018_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor)
    base = base * closeadj
    base = _ema(base, 63)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw63xrevjw126sm_126d_jerk_v019_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor)
    base = base * closeadj
    base = _mean(base, 63)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw63xrevjw252em_252d_jerk_v020_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor)
    base = base * closeadj
    base = _ema(base, 63)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw126xclosejw5sm_5d_jerk_v021_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor) * closeadj
    base = _mean(base, 126)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw126xclosejw21em_21d_jerk_v022_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor) * closeadj
    base = _ema(base, 126)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw126xclosejw63sm_63d_jerk_v023_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor) * closeadj
    base = _mean(base, 126)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw126xclosejw126em_126d_jerk_v024_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor) * closeadj
    base = _ema(base, 126)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw126xclosejw252sm_252d_jerk_v025_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor) * closeadj
    base = _mean(base, 126)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw126xrevjw5em_5d_jerk_v026_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor)
    base = base * closeadj
    base = _ema(base, 126)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw126xrevjw21sm_21d_jerk_v027_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor)
    base = base * closeadj
    base = _mean(base, 126)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw126xrevjw63em_63d_jerk_v028_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor)
    base = base * closeadj
    base = _ema(base, 126)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw126xrevjw126sm_126d_jerk_v029_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor)
    base = base * closeadj
    base = _mean(base, 126)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw126xrevjw252em_252d_jerk_v030_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor)
    base = base * closeadj
    base = _ema(base, 126)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw252xclosejw5sm_5d_jerk_v031_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor) * closeadj
    base = _mean(base, 252)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw252xclosejw21em_21d_jerk_v032_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor) * closeadj
    base = _ema(base, 252)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw252xclosejw63sm_63d_jerk_v033_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor) * closeadj
    base = _mean(base, 252)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw252xclosejw126em_126d_jerk_v034_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor) * closeadj
    base = _ema(base, 252)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw252xclosejw252sm_252d_jerk_v035_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor) * closeadj
    base = _mean(base, 252)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw252xrevjw5em_5d_jerk_v036_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor)
    base = base * closeadj
    base = _ema(base, 252)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw252xrevjw21sm_21d_jerk_v037_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor)
    base = base * closeadj
    base = _mean(base, 252)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw252xrevjw63em_63d_jerk_v038_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor)
    base = base * closeadj
    base = _ema(base, 252)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw252xrevjw126sm_126d_jerk_v039_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor)
    base = base * closeadj
    base = _mean(base, 252)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw252xrevjw252em_252d_jerk_v040_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor)
    base = base * closeadj
    base = _ema(base, 252)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw504xclosejw5sm_5d_jerk_v041_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor) * closeadj
    base = _mean(base, 504)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw504xclosejw21em_21d_jerk_v042_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor) * closeadj
    base = _ema(base, 504)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw504xclosejw63sm_63d_jerk_v043_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor) * closeadj
    base = _mean(base, 504)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw504xclosejw126em_126d_jerk_v044_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor) * closeadj
    base = _ema(base, 504)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw504xclosejw252sm_252d_jerk_v045_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor) * closeadj
    base = _mean(base, 504)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw504xrevjw5em_5d_jerk_v046_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor)
    base = base * closeadj
    base = _ema(base, 504)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw504xrevjw21sm_21d_jerk_v047_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor)
    base = base * closeadj
    base = _mean(base, 504)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw504xrevjw63em_63d_jerk_v048_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor)
    base = base * closeadj
    base = _ema(base, 504)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw504xrevjw126sm_126d_jerk_v049_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor)
    base = base * closeadj
    base = _mean(base, 504)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p0bw504xrevjw252em_252d_jerk_v050_signal(inventory, cor, closeadj):
    base = _f09_inv_turnover(inventory, cor)
    base = base * closeadj
    base = _ema(base, 504)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw21xclosejw5sm_5d_jerk_v051_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj
    base = _mean(base, 21)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw21xclosejw21em_21d_jerk_v052_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj
    base = _ema(base, 21)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw21xclosejw63sm_63d_jerk_v053_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj
    base = _mean(base, 21)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw21xclosejw126em_126d_jerk_v054_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj
    base = _ema(base, 21)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw21xclosejw252sm_252d_jerk_v055_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj
    base = _mean(base, 21)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw21xrevjw5em_5d_jerk_v056_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue)
    base = base * closeadj
    base = _ema(base, 21)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw21xrevjw21sm_21d_jerk_v057_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue)
    base = base * closeadj
    base = _mean(base, 21)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw21xrevjw63em_63d_jerk_v058_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue)
    base = base * closeadj
    base = _ema(base, 21)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw21xrevjw126sm_126d_jerk_v059_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue)
    base = base * closeadj
    base = _mean(base, 21)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw21xrevjw252em_252d_jerk_v060_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue)
    base = base * closeadj
    base = _ema(base, 21)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw63xclosejw5sm_5d_jerk_v061_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj
    base = _mean(base, 63)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw63xclosejw21em_21d_jerk_v062_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj
    base = _ema(base, 63)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw63xclosejw63sm_63d_jerk_v063_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj
    base = _mean(base, 63)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw63xclosejw126em_126d_jerk_v064_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj
    base = _ema(base, 63)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw63xclosejw252sm_252d_jerk_v065_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj
    base = _mean(base, 63)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw63xrevjw5em_5d_jerk_v066_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue)
    base = base * closeadj
    base = _ema(base, 63)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw63xrevjw21sm_21d_jerk_v067_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue)
    base = base * closeadj
    base = _mean(base, 63)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw63xrevjw63em_63d_jerk_v068_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue)
    base = base * closeadj
    base = _ema(base, 63)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw63xrevjw126sm_126d_jerk_v069_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue)
    base = base * closeadj
    base = _mean(base, 63)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw63xrevjw252em_252d_jerk_v070_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue)
    base = base * closeadj
    base = _ema(base, 63)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw126xclosejw5sm_5d_jerk_v071_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj
    base = _mean(base, 126)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw126xclosejw21em_21d_jerk_v072_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj
    base = _ema(base, 126)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw126xclosejw63sm_63d_jerk_v073_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj
    base = _mean(base, 126)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw126xclosejw126em_126d_jerk_v074_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj
    base = _ema(base, 126)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw126xclosejw252sm_252d_jerk_v075_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj
    base = _mean(base, 126)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw126xrevjw5em_5d_jerk_v076_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue)
    base = base * closeadj
    base = _ema(base, 126)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw126xrevjw21sm_21d_jerk_v077_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue)
    base = base * closeadj
    base = _mean(base, 126)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw126xrevjw63em_63d_jerk_v078_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue)
    base = base * closeadj
    base = _ema(base, 126)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw126xrevjw126sm_126d_jerk_v079_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue)
    base = base * closeadj
    base = _mean(base, 126)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw126xrevjw252em_252d_jerk_v080_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue)
    base = base * closeadj
    base = _ema(base, 126)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw252xclosejw5sm_5d_jerk_v081_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj
    base = _mean(base, 252)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw252xclosejw21em_21d_jerk_v082_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj
    base = _ema(base, 252)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw252xclosejw63sm_63d_jerk_v083_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj
    base = _mean(base, 252)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw252xclosejw126em_126d_jerk_v084_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj
    base = _ema(base, 252)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw252xclosejw252sm_252d_jerk_v085_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj
    base = _mean(base, 252)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw252xrevjw5em_5d_jerk_v086_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue)
    base = base * closeadj
    base = _ema(base, 252)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw252xrevjw21sm_21d_jerk_v087_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue)
    base = base * closeadj
    base = _mean(base, 252)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw252xrevjw63em_63d_jerk_v088_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue)
    base = base * closeadj
    base = _ema(base, 252)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw252xrevjw126sm_126d_jerk_v089_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue)
    base = base * closeadj
    base = _mean(base, 252)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw252xrevjw252em_252d_jerk_v090_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue)
    base = base * closeadj
    base = _ema(base, 252)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw504xclosejw5sm_5d_jerk_v091_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj
    base = _mean(base, 504)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw504xclosejw21em_21d_jerk_v092_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj
    base = _ema(base, 504)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw504xclosejw63sm_63d_jerk_v093_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj
    base = _mean(base, 504)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw504xclosejw126em_126d_jerk_v094_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj
    base = _ema(base, 504)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw504xclosejw252sm_252d_jerk_v095_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj
    base = _mean(base, 504)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw504xrevjw5em_5d_jerk_v096_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue)
    base = base * closeadj
    base = _ema(base, 504)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw504xrevjw21sm_21d_jerk_v097_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue)
    base = base * closeadj
    base = _mean(base, 504)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw504xrevjw63em_63d_jerk_v098_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue)
    base = base * closeadj
    base = _ema(base, 504)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw504xrevjw126sm_126d_jerk_v099_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue)
    base = base * closeadj
    base = _mean(base, 504)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p1bw504xrevjw252em_252d_jerk_v100_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue)
    base = base * closeadj
    base = _ema(base, 504)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw21xclosejw5sm_5d_jerk_v101_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 21) * closeadj
    base = _mean(base, 21)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw21xclosejw21em_21d_jerk_v102_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 21) * closeadj
    base = _ema(base, 21)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw21xclosejw63sm_63d_jerk_v103_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 21) * closeadj
    base = _mean(base, 21)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw21xclosejw126em_126d_jerk_v104_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 21) * closeadj
    base = _ema(base, 21)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw21xclosejw252sm_252d_jerk_v105_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 21) * closeadj
    base = _mean(base, 21)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw21xrevjw5em_5d_jerk_v106_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 21)
    base = base * closeadj
    base = _ema(base, 21)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw21xrevjw21sm_21d_jerk_v107_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 21)
    base = base * closeadj
    base = _mean(base, 21)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw21xrevjw63em_63d_jerk_v108_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 21)
    base = base * closeadj
    base = _ema(base, 21)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw21xrevjw126sm_126d_jerk_v109_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 21)
    base = base * closeadj
    base = _mean(base, 21)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw21xrevjw252em_252d_jerk_v110_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 21)
    base = base * closeadj
    base = _ema(base, 21)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw63xclosejw5sm_5d_jerk_v111_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 63) * closeadj
    base = _mean(base, 63)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw63xclosejw21em_21d_jerk_v112_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 63) * closeadj
    base = _ema(base, 63)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw63xclosejw63sm_63d_jerk_v113_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 63) * closeadj
    base = _mean(base, 63)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw63xclosejw126em_126d_jerk_v114_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 63) * closeadj
    base = _ema(base, 63)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw63xclosejw252sm_252d_jerk_v115_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 63) * closeadj
    base = _mean(base, 63)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw63xrevjw5em_5d_jerk_v116_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 63)
    base = base * closeadj
    base = _ema(base, 63)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw63xrevjw21sm_21d_jerk_v117_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 63)
    base = base * closeadj
    base = _mean(base, 63)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw63xrevjw63em_63d_jerk_v118_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 63)
    base = base * closeadj
    base = _ema(base, 63)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw63xrevjw126sm_126d_jerk_v119_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 63)
    base = base * closeadj
    base = _mean(base, 63)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw63xrevjw252em_252d_jerk_v120_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 63)
    base = base * closeadj
    base = _ema(base, 63)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw126xclosejw5sm_5d_jerk_v121_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 126) * closeadj
    base = _mean(base, 126)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw126xclosejw21em_21d_jerk_v122_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 126) * closeadj
    base = _ema(base, 126)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw126xclosejw63sm_63d_jerk_v123_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 126) * closeadj
    base = _mean(base, 126)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw126xclosejw126em_126d_jerk_v124_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 126) * closeadj
    base = _ema(base, 126)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw126xclosejw252sm_252d_jerk_v125_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 126) * closeadj
    base = _mean(base, 126)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw126xrevjw5em_5d_jerk_v126_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 126)
    base = base * closeadj
    base = _ema(base, 126)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw126xrevjw21sm_21d_jerk_v127_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 126)
    base = base * closeadj
    base = _mean(base, 126)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw126xrevjw63em_63d_jerk_v128_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 126)
    base = base * closeadj
    base = _ema(base, 126)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw126xrevjw126sm_126d_jerk_v129_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 126)
    base = base * closeadj
    base = _mean(base, 126)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw126xrevjw252em_252d_jerk_v130_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 126)
    base = base * closeadj
    base = _ema(base, 126)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw252xclosejw5sm_5d_jerk_v131_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 252) * closeadj
    base = _mean(base, 252)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw252xclosejw21em_21d_jerk_v132_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 252) * closeadj
    base = _ema(base, 252)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw252xclosejw63sm_63d_jerk_v133_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 252) * closeadj
    base = _mean(base, 252)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw252xclosejw126em_126d_jerk_v134_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 252) * closeadj
    base = _ema(base, 252)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw252xclosejw252sm_252d_jerk_v135_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 252) * closeadj
    base = _mean(base, 252)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw252xrevjw5em_5d_jerk_v136_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 252)
    base = base * closeadj
    base = _ema(base, 252)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw252xrevjw21sm_21d_jerk_v137_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 252)
    base = base * closeadj
    base = _mean(base, 252)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw252xrevjw63em_63d_jerk_v138_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 252)
    base = base * closeadj
    base = _ema(base, 252)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw252xrevjw126sm_126d_jerk_v139_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 252)
    base = base * closeadj
    base = _mean(base, 252)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw252xrevjw252em_252d_jerk_v140_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 252)
    base = base * closeadj
    base = _ema(base, 252)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw504xclosejw5sm_5d_jerk_v141_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 504) * closeadj
    base = _mean(base, 504)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw504xclosejw21em_21d_jerk_v142_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 504) * closeadj
    base = _ema(base, 504)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw504xclosejw63sm_63d_jerk_v143_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 504) * closeadj
    base = _mean(base, 504)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw504xclosejw126em_126d_jerk_v144_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 504) * closeadj
    base = _ema(base, 504)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw504xclosejw252sm_252d_jerk_v145_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 504) * closeadj
    base = _mean(base, 504)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw504xrevjw5em_5d_jerk_v146_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 504)
    base = base * closeadj
    base = _ema(base, 504)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw504xrevjw21sm_21d_jerk_v147_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 504)
    base = base * closeadj
    base = _mean(base, 504)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw504xrevjw63em_63d_jerk_v148_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 504)
    base = base * closeadj
    base = _ema(base, 504)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw504xrevjw126sm_126d_jerk_v149_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 504)
    base = base * closeadj
    base = _mean(base, 504)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09dim_f09_device_inventory_management_p2bw504xrevjw252em_252d_jerk_v150_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 504)
    base = base * closeadj
    base = _ema(base, 504)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f09dim_f09_device_inventory_management_p0bw21xclosejw5sm_5d_jerk_v001_signal,
    f09dim_f09_device_inventory_management_p0bw21xclosejw21em_21d_jerk_v002_signal,
    f09dim_f09_device_inventory_management_p0bw21xclosejw63sm_63d_jerk_v003_signal,
    f09dim_f09_device_inventory_management_p0bw21xclosejw126em_126d_jerk_v004_signal,
    f09dim_f09_device_inventory_management_p0bw21xclosejw252sm_252d_jerk_v005_signal,
    f09dim_f09_device_inventory_management_p0bw21xrevjw5em_5d_jerk_v006_signal,
    f09dim_f09_device_inventory_management_p0bw21xrevjw21sm_21d_jerk_v007_signal,
    f09dim_f09_device_inventory_management_p0bw21xrevjw63em_63d_jerk_v008_signal,
    f09dim_f09_device_inventory_management_p0bw21xrevjw126sm_126d_jerk_v009_signal,
    f09dim_f09_device_inventory_management_p0bw21xrevjw252em_252d_jerk_v010_signal,
    f09dim_f09_device_inventory_management_p0bw63xclosejw5sm_5d_jerk_v011_signal,
    f09dim_f09_device_inventory_management_p0bw63xclosejw21em_21d_jerk_v012_signal,
    f09dim_f09_device_inventory_management_p0bw63xclosejw63sm_63d_jerk_v013_signal,
    f09dim_f09_device_inventory_management_p0bw63xclosejw126em_126d_jerk_v014_signal,
    f09dim_f09_device_inventory_management_p0bw63xclosejw252sm_252d_jerk_v015_signal,
    f09dim_f09_device_inventory_management_p0bw63xrevjw5em_5d_jerk_v016_signal,
    f09dim_f09_device_inventory_management_p0bw63xrevjw21sm_21d_jerk_v017_signal,
    f09dim_f09_device_inventory_management_p0bw63xrevjw63em_63d_jerk_v018_signal,
    f09dim_f09_device_inventory_management_p0bw63xrevjw126sm_126d_jerk_v019_signal,
    f09dim_f09_device_inventory_management_p0bw63xrevjw252em_252d_jerk_v020_signal,
    f09dim_f09_device_inventory_management_p0bw126xclosejw5sm_5d_jerk_v021_signal,
    f09dim_f09_device_inventory_management_p0bw126xclosejw21em_21d_jerk_v022_signal,
    f09dim_f09_device_inventory_management_p0bw126xclosejw63sm_63d_jerk_v023_signal,
    f09dim_f09_device_inventory_management_p0bw126xclosejw126em_126d_jerk_v024_signal,
    f09dim_f09_device_inventory_management_p0bw126xclosejw252sm_252d_jerk_v025_signal,
    f09dim_f09_device_inventory_management_p0bw126xrevjw5em_5d_jerk_v026_signal,
    f09dim_f09_device_inventory_management_p0bw126xrevjw21sm_21d_jerk_v027_signal,
    f09dim_f09_device_inventory_management_p0bw126xrevjw63em_63d_jerk_v028_signal,
    f09dim_f09_device_inventory_management_p0bw126xrevjw126sm_126d_jerk_v029_signal,
    f09dim_f09_device_inventory_management_p0bw126xrevjw252em_252d_jerk_v030_signal,
    f09dim_f09_device_inventory_management_p0bw252xclosejw5sm_5d_jerk_v031_signal,
    f09dim_f09_device_inventory_management_p0bw252xclosejw21em_21d_jerk_v032_signal,
    f09dim_f09_device_inventory_management_p0bw252xclosejw63sm_63d_jerk_v033_signal,
    f09dim_f09_device_inventory_management_p0bw252xclosejw126em_126d_jerk_v034_signal,
    f09dim_f09_device_inventory_management_p0bw252xclosejw252sm_252d_jerk_v035_signal,
    f09dim_f09_device_inventory_management_p0bw252xrevjw5em_5d_jerk_v036_signal,
    f09dim_f09_device_inventory_management_p0bw252xrevjw21sm_21d_jerk_v037_signal,
    f09dim_f09_device_inventory_management_p0bw252xrevjw63em_63d_jerk_v038_signal,
    f09dim_f09_device_inventory_management_p0bw252xrevjw126sm_126d_jerk_v039_signal,
    f09dim_f09_device_inventory_management_p0bw252xrevjw252em_252d_jerk_v040_signal,
    f09dim_f09_device_inventory_management_p0bw504xclosejw5sm_5d_jerk_v041_signal,
    f09dim_f09_device_inventory_management_p0bw504xclosejw21em_21d_jerk_v042_signal,
    f09dim_f09_device_inventory_management_p0bw504xclosejw63sm_63d_jerk_v043_signal,
    f09dim_f09_device_inventory_management_p0bw504xclosejw126em_126d_jerk_v044_signal,
    f09dim_f09_device_inventory_management_p0bw504xclosejw252sm_252d_jerk_v045_signal,
    f09dim_f09_device_inventory_management_p0bw504xrevjw5em_5d_jerk_v046_signal,
    f09dim_f09_device_inventory_management_p0bw504xrevjw21sm_21d_jerk_v047_signal,
    f09dim_f09_device_inventory_management_p0bw504xrevjw63em_63d_jerk_v048_signal,
    f09dim_f09_device_inventory_management_p0bw504xrevjw126sm_126d_jerk_v049_signal,
    f09dim_f09_device_inventory_management_p0bw504xrevjw252em_252d_jerk_v050_signal,
    f09dim_f09_device_inventory_management_p1bw21xclosejw5sm_5d_jerk_v051_signal,
    f09dim_f09_device_inventory_management_p1bw21xclosejw21em_21d_jerk_v052_signal,
    f09dim_f09_device_inventory_management_p1bw21xclosejw63sm_63d_jerk_v053_signal,
    f09dim_f09_device_inventory_management_p1bw21xclosejw126em_126d_jerk_v054_signal,
    f09dim_f09_device_inventory_management_p1bw21xclosejw252sm_252d_jerk_v055_signal,
    f09dim_f09_device_inventory_management_p1bw21xrevjw5em_5d_jerk_v056_signal,
    f09dim_f09_device_inventory_management_p1bw21xrevjw21sm_21d_jerk_v057_signal,
    f09dim_f09_device_inventory_management_p1bw21xrevjw63em_63d_jerk_v058_signal,
    f09dim_f09_device_inventory_management_p1bw21xrevjw126sm_126d_jerk_v059_signal,
    f09dim_f09_device_inventory_management_p1bw21xrevjw252em_252d_jerk_v060_signal,
    f09dim_f09_device_inventory_management_p1bw63xclosejw5sm_5d_jerk_v061_signal,
    f09dim_f09_device_inventory_management_p1bw63xclosejw21em_21d_jerk_v062_signal,
    f09dim_f09_device_inventory_management_p1bw63xclosejw63sm_63d_jerk_v063_signal,
    f09dim_f09_device_inventory_management_p1bw63xclosejw126em_126d_jerk_v064_signal,
    f09dim_f09_device_inventory_management_p1bw63xclosejw252sm_252d_jerk_v065_signal,
    f09dim_f09_device_inventory_management_p1bw63xrevjw5em_5d_jerk_v066_signal,
    f09dim_f09_device_inventory_management_p1bw63xrevjw21sm_21d_jerk_v067_signal,
    f09dim_f09_device_inventory_management_p1bw63xrevjw63em_63d_jerk_v068_signal,
    f09dim_f09_device_inventory_management_p1bw63xrevjw126sm_126d_jerk_v069_signal,
    f09dim_f09_device_inventory_management_p1bw63xrevjw252em_252d_jerk_v070_signal,
    f09dim_f09_device_inventory_management_p1bw126xclosejw5sm_5d_jerk_v071_signal,
    f09dim_f09_device_inventory_management_p1bw126xclosejw21em_21d_jerk_v072_signal,
    f09dim_f09_device_inventory_management_p1bw126xclosejw63sm_63d_jerk_v073_signal,
    f09dim_f09_device_inventory_management_p1bw126xclosejw126em_126d_jerk_v074_signal,
    f09dim_f09_device_inventory_management_p1bw126xclosejw252sm_252d_jerk_v075_signal,
    f09dim_f09_device_inventory_management_p1bw126xrevjw5em_5d_jerk_v076_signal,
    f09dim_f09_device_inventory_management_p1bw126xrevjw21sm_21d_jerk_v077_signal,
    f09dim_f09_device_inventory_management_p1bw126xrevjw63em_63d_jerk_v078_signal,
    f09dim_f09_device_inventory_management_p1bw126xrevjw126sm_126d_jerk_v079_signal,
    f09dim_f09_device_inventory_management_p1bw126xrevjw252em_252d_jerk_v080_signal,
    f09dim_f09_device_inventory_management_p1bw252xclosejw5sm_5d_jerk_v081_signal,
    f09dim_f09_device_inventory_management_p1bw252xclosejw21em_21d_jerk_v082_signal,
    f09dim_f09_device_inventory_management_p1bw252xclosejw63sm_63d_jerk_v083_signal,
    f09dim_f09_device_inventory_management_p1bw252xclosejw126em_126d_jerk_v084_signal,
    f09dim_f09_device_inventory_management_p1bw252xclosejw252sm_252d_jerk_v085_signal,
    f09dim_f09_device_inventory_management_p1bw252xrevjw5em_5d_jerk_v086_signal,
    f09dim_f09_device_inventory_management_p1bw252xrevjw21sm_21d_jerk_v087_signal,
    f09dim_f09_device_inventory_management_p1bw252xrevjw63em_63d_jerk_v088_signal,
    f09dim_f09_device_inventory_management_p1bw252xrevjw126sm_126d_jerk_v089_signal,
    f09dim_f09_device_inventory_management_p1bw252xrevjw252em_252d_jerk_v090_signal,
    f09dim_f09_device_inventory_management_p1bw504xclosejw5sm_5d_jerk_v091_signal,
    f09dim_f09_device_inventory_management_p1bw504xclosejw21em_21d_jerk_v092_signal,
    f09dim_f09_device_inventory_management_p1bw504xclosejw63sm_63d_jerk_v093_signal,
    f09dim_f09_device_inventory_management_p1bw504xclosejw126em_126d_jerk_v094_signal,
    f09dim_f09_device_inventory_management_p1bw504xclosejw252sm_252d_jerk_v095_signal,
    f09dim_f09_device_inventory_management_p1bw504xrevjw5em_5d_jerk_v096_signal,
    f09dim_f09_device_inventory_management_p1bw504xrevjw21sm_21d_jerk_v097_signal,
    f09dim_f09_device_inventory_management_p1bw504xrevjw63em_63d_jerk_v098_signal,
    f09dim_f09_device_inventory_management_p1bw504xrevjw126sm_126d_jerk_v099_signal,
    f09dim_f09_device_inventory_management_p1bw504xrevjw252em_252d_jerk_v100_signal,
    f09dim_f09_device_inventory_management_p2bw21xclosejw5sm_5d_jerk_v101_signal,
    f09dim_f09_device_inventory_management_p2bw21xclosejw21em_21d_jerk_v102_signal,
    f09dim_f09_device_inventory_management_p2bw21xclosejw63sm_63d_jerk_v103_signal,
    f09dim_f09_device_inventory_management_p2bw21xclosejw126em_126d_jerk_v104_signal,
    f09dim_f09_device_inventory_management_p2bw21xclosejw252sm_252d_jerk_v105_signal,
    f09dim_f09_device_inventory_management_p2bw21xrevjw5em_5d_jerk_v106_signal,
    f09dim_f09_device_inventory_management_p2bw21xrevjw21sm_21d_jerk_v107_signal,
    f09dim_f09_device_inventory_management_p2bw21xrevjw63em_63d_jerk_v108_signal,
    f09dim_f09_device_inventory_management_p2bw21xrevjw126sm_126d_jerk_v109_signal,
    f09dim_f09_device_inventory_management_p2bw21xrevjw252em_252d_jerk_v110_signal,
    f09dim_f09_device_inventory_management_p2bw63xclosejw5sm_5d_jerk_v111_signal,
    f09dim_f09_device_inventory_management_p2bw63xclosejw21em_21d_jerk_v112_signal,
    f09dim_f09_device_inventory_management_p2bw63xclosejw63sm_63d_jerk_v113_signal,
    f09dim_f09_device_inventory_management_p2bw63xclosejw126em_126d_jerk_v114_signal,
    f09dim_f09_device_inventory_management_p2bw63xclosejw252sm_252d_jerk_v115_signal,
    f09dim_f09_device_inventory_management_p2bw63xrevjw5em_5d_jerk_v116_signal,
    f09dim_f09_device_inventory_management_p2bw63xrevjw21sm_21d_jerk_v117_signal,
    f09dim_f09_device_inventory_management_p2bw63xrevjw63em_63d_jerk_v118_signal,
    f09dim_f09_device_inventory_management_p2bw63xrevjw126sm_126d_jerk_v119_signal,
    f09dim_f09_device_inventory_management_p2bw63xrevjw252em_252d_jerk_v120_signal,
    f09dim_f09_device_inventory_management_p2bw126xclosejw5sm_5d_jerk_v121_signal,
    f09dim_f09_device_inventory_management_p2bw126xclosejw21em_21d_jerk_v122_signal,
    f09dim_f09_device_inventory_management_p2bw126xclosejw63sm_63d_jerk_v123_signal,
    f09dim_f09_device_inventory_management_p2bw126xclosejw126em_126d_jerk_v124_signal,
    f09dim_f09_device_inventory_management_p2bw126xclosejw252sm_252d_jerk_v125_signal,
    f09dim_f09_device_inventory_management_p2bw126xrevjw5em_5d_jerk_v126_signal,
    f09dim_f09_device_inventory_management_p2bw126xrevjw21sm_21d_jerk_v127_signal,
    f09dim_f09_device_inventory_management_p2bw126xrevjw63em_63d_jerk_v128_signal,
    f09dim_f09_device_inventory_management_p2bw126xrevjw126sm_126d_jerk_v129_signal,
    f09dim_f09_device_inventory_management_p2bw126xrevjw252em_252d_jerk_v130_signal,
    f09dim_f09_device_inventory_management_p2bw252xclosejw5sm_5d_jerk_v131_signal,
    f09dim_f09_device_inventory_management_p2bw252xclosejw21em_21d_jerk_v132_signal,
    f09dim_f09_device_inventory_management_p2bw252xclosejw63sm_63d_jerk_v133_signal,
    f09dim_f09_device_inventory_management_p2bw252xclosejw126em_126d_jerk_v134_signal,
    f09dim_f09_device_inventory_management_p2bw252xclosejw252sm_252d_jerk_v135_signal,
    f09dim_f09_device_inventory_management_p2bw252xrevjw5em_5d_jerk_v136_signal,
    f09dim_f09_device_inventory_management_p2bw252xrevjw21sm_21d_jerk_v137_signal,
    f09dim_f09_device_inventory_management_p2bw252xrevjw63em_63d_jerk_v138_signal,
    f09dim_f09_device_inventory_management_p2bw252xrevjw126sm_126d_jerk_v139_signal,
    f09dim_f09_device_inventory_management_p2bw252xrevjw252em_252d_jerk_v140_signal,
    f09dim_f09_device_inventory_management_p2bw504xclosejw5sm_5d_jerk_v141_signal,
    f09dim_f09_device_inventory_management_p2bw504xclosejw21em_21d_jerk_v142_signal,
    f09dim_f09_device_inventory_management_p2bw504xclosejw63sm_63d_jerk_v143_signal,
    f09dim_f09_device_inventory_management_p2bw504xclosejw126em_126d_jerk_v144_signal,
    f09dim_f09_device_inventory_management_p2bw504xclosejw252sm_252d_jerk_v145_signal,
    f09dim_f09_device_inventory_management_p2bw504xrevjw5em_5d_jerk_v146_signal,
    f09dim_f09_device_inventory_management_p2bw504xrevjw21sm_21d_jerk_v147_signal,
    f09dim_f09_device_inventory_management_p2bw504xrevjw63em_63d_jerk_v148_signal,
    f09dim_f09_device_inventory_management_p2bw504xrevjw126sm_126d_jerk_v149_signal,
    f09dim_f09_device_inventory_management_p2bw504xrevjw252em_252d_jerk_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F09_DEVICE_INVENTORY_MANAGEMENT_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    assets  = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    ppnenet = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    inventory   = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")

    cols = {
        "closeadj": closeadj,
        "revenue": revenue, "assets": assets, "ppnenet": ppnenet, "capex": capex,
        "inventory": inventory, "receivables": receivables, "cor": cor,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f09_inv_turnover", "_f09_inv_to_revenue", "_f09_inv_dynamics",)
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
    print(f"OK f09_device_inventory_management_3rd_derivatives_001_150_claude: {n_features} features pass")
