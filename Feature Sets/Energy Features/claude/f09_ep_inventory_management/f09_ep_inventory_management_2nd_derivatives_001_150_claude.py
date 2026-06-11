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



def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)



# ===== folder domain primitives =====
def _f09_inv_days(inventory, cor):
    return inventory / cor.replace(0, np.nan) * 365.0


def _f09_inv_to_revenue(inventory, revenue):
    return inventory / revenue.replace(0, np.nan)


def _f09_inv_dynamics(inventory, revenue, w):
    ratio = inventory / revenue.replace(0, np.nan)
    return ratio.rolling(w, min_periods=max(1, w // 2)).mean()


# ===== features =====

# slope of idxcl21 w_out=5
def f09eim_f09_ep_inventory_management_idxcl21_w5_slope_v001_signal(inventory, cor, closeadj):
    base = _f09_inv_days(inventory, cor) * closeadj + 0.0 * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idxcl21 w_out=10
def f09eim_f09_ep_inventory_management_idxcl21_w10_slope_v002_signal(inventory, cor, closeadj):
    base = _f09_inv_days(inventory, cor) * closeadj + 0.0 * _mean(closeadj, 21)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idxcl21 w_out=21
def f09eim_f09_ep_inventory_management_idxcl21_w21_slope_v003_signal(inventory, cor, closeadj):
    base = _f09_inv_days(inventory, cor) * closeadj + 0.0 * _mean(closeadj, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idxcl21 w_out=42
def f09eim_f09_ep_inventory_management_idxcl21_w42_slope_v004_signal(inventory, cor, closeadj):
    base = _f09_inv_days(inventory, cor) * closeadj + 0.0 * _mean(closeadj, 21)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idxcl21 w_out=63
def f09eim_f09_ep_inventory_management_idxcl21_w63_slope_v005_signal(inventory, cor, closeadj):
    base = _f09_inv_days(inventory, cor) * closeadj + 0.0 * _mean(closeadj, 21)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idxcl21 w_out=126
def f09eim_f09_ep_inventory_management_idxcl21_w126_slope_v006_signal(inventory, cor, closeadj):
    base = _f09_inv_days(inventory, cor) * closeadj + 0.0 * _mean(closeadj, 21)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of irxcl21 w_out=5
def f09eim_f09_ep_inventory_management_irxcl21_w5_slope_v007_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj + 0.0 * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of irxcl21 w_out=10
def f09eim_f09_ep_inventory_management_irxcl21_w10_slope_v008_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj + 0.0 * _mean(closeadj, 21)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of irxcl21 w_out=21
def f09eim_f09_ep_inventory_management_irxcl21_w21_slope_v009_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj + 0.0 * _mean(closeadj, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of irxcl21 w_out=42
def f09eim_f09_ep_inventory_management_irxcl21_w42_slope_v010_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj + 0.0 * _mean(closeadj, 21)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of irxcl21 w_out=63
def f09eim_f09_ep_inventory_management_irxcl21_w63_slope_v011_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj + 0.0 * _mean(closeadj, 21)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of irxcl21 w_out=126
def f09eim_f09_ep_inventory_management_irxcl21_w126_slope_v012_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj + 0.0 * _mean(closeadj, 21)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idy21 w_out=5
def f09eim_f09_ep_inventory_management_idy21_w5_slope_v013_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idy21 w_out=10
def f09eim_f09_ep_inventory_management_idy21_w10_slope_v014_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idy21 w_out=21
def f09eim_f09_ep_inventory_management_idy21_w21_slope_v015_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idy21 w_out=42
def f09eim_f09_ep_inventory_management_idy21_w42_slope_v016_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 21) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idy21 w_out=63
def f09eim_f09_ep_inventory_management_idy21_w63_slope_v017_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idy21 w_out=126
def f09eim_f09_ep_inventory_management_idy21_w126_slope_v018_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 21) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idlog21 w_out=5
def f09eim_f09_ep_inventory_management_idlog21_w5_slope_v019_signal(inventory, cor, closeadj):
    base = np.log1p(_f09_inv_days(inventory, cor).abs()) * closeadj + 0.0 * _mean(closeadj, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idlog21 w_out=10
def f09eim_f09_ep_inventory_management_idlog21_w10_slope_v020_signal(inventory, cor, closeadj):
    base = np.log1p(_f09_inv_days(inventory, cor).abs()) * closeadj + 0.0 * _mean(closeadj, 21)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idlog21 w_out=21
def f09eim_f09_ep_inventory_management_idlog21_w21_slope_v021_signal(inventory, cor, closeadj):
    base = np.log1p(_f09_inv_days(inventory, cor).abs()) * closeadj + 0.0 * _mean(closeadj, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idlog21 w_out=42
def f09eim_f09_ep_inventory_management_idlog21_w42_slope_v022_signal(inventory, cor, closeadj):
    base = np.log1p(_f09_inv_days(inventory, cor).abs()) * closeadj + 0.0 * _mean(closeadj, 21)
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idlog21 w_out=63
def f09eim_f09_ep_inventory_management_idlog21_w63_slope_v023_signal(inventory, cor, closeadj):
    base = np.log1p(_f09_inv_days(inventory, cor).abs()) * closeadj + 0.0 * _mean(closeadj, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idlog21 w_out=126
def f09eim_f09_ep_inventory_management_idlog21_w126_slope_v024_signal(inventory, cor, closeadj):
    base = np.log1p(_f09_inv_days(inventory, cor).abs()) * closeadj + 0.0 * _mean(closeadj, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of irsq21 w_out=5
def f09eim_f09_ep_inventory_management_irsq21_w5_slope_v025_signal(inventory, revenue, closeadj):
    base = (_f09_inv_to_revenue(inventory, revenue) ** 2) * closeadj + 0.0 * _mean(closeadj, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of irsq21 w_out=10
def f09eim_f09_ep_inventory_management_irsq21_w10_slope_v026_signal(inventory, revenue, closeadj):
    base = (_f09_inv_to_revenue(inventory, revenue) ** 2) * closeadj + 0.0 * _mean(closeadj, 21)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of irsq21 w_out=21
def f09eim_f09_ep_inventory_management_irsq21_w21_slope_v027_signal(inventory, revenue, closeadj):
    base = (_f09_inv_to_revenue(inventory, revenue) ** 2) * closeadj + 0.0 * _mean(closeadj, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of irsq21 w_out=42
def f09eim_f09_ep_inventory_management_irsq21_w42_slope_v028_signal(inventory, revenue, closeadj):
    base = (_f09_inv_to_revenue(inventory, revenue) ** 2) * closeadj + 0.0 * _mean(closeadj, 21)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of irsq21 w_out=63
def f09eim_f09_ep_inventory_management_irsq21_w63_slope_v029_signal(inventory, revenue, closeadj):
    base = (_f09_inv_to_revenue(inventory, revenue) ** 2) * closeadj + 0.0 * _mean(closeadj, 21)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of irsq21 w_out=126
def f09eim_f09_ep_inventory_management_irsq21_w126_slope_v030_signal(inventory, revenue, closeadj):
    base = (_f09_inv_to_revenue(inventory, revenue) ** 2) * closeadj + 0.0 * _mean(closeadj, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idysq21 w_out=5
def f09eim_f09_ep_inventory_management_idysq21_w5_slope_v031_signal(inventory, revenue, closeadj):
    base = (_f09_inv_dynamics(inventory, revenue, 21) ** 2) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idysq21 w_out=10
def f09eim_f09_ep_inventory_management_idysq21_w10_slope_v032_signal(inventory, revenue, closeadj):
    base = (_f09_inv_dynamics(inventory, revenue, 21) ** 2) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idysq21 w_out=21
def f09eim_f09_ep_inventory_management_idysq21_w21_slope_v033_signal(inventory, revenue, closeadj):
    base = (_f09_inv_dynamics(inventory, revenue, 21) ** 2) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idysq21 w_out=42
def f09eim_f09_ep_inventory_management_idysq21_w42_slope_v034_signal(inventory, revenue, closeadj):
    base = (_f09_inv_dynamics(inventory, revenue, 21) ** 2) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idysq21 w_out=63
def f09eim_f09_ep_inventory_management_idysq21_w63_slope_v035_signal(inventory, revenue, closeadj):
    base = (_f09_inv_dynamics(inventory, revenue, 21) ** 2) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idysq21 w_out=126
def f09eim_f09_ep_inventory_management_idysq21_w126_slope_v036_signal(inventory, revenue, closeadj):
    base = (_f09_inv_dynamics(inventory, revenue, 21) ** 2) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idmean21 w_out=5
def f09eim_f09_ep_inventory_management_idmean21_w5_slope_v037_signal(inventory, cor, closeadj):
    base = _mean(_f09_inv_days(inventory, cor), 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idmean21 w_out=10
def f09eim_f09_ep_inventory_management_idmean21_w10_slope_v038_signal(inventory, cor, closeadj):
    base = _mean(_f09_inv_days(inventory, cor), 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idmean21 w_out=21
def f09eim_f09_ep_inventory_management_idmean21_w21_slope_v039_signal(inventory, cor, closeadj):
    base = _mean(_f09_inv_days(inventory, cor), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idmean21 w_out=42
def f09eim_f09_ep_inventory_management_idmean21_w42_slope_v040_signal(inventory, cor, closeadj):
    base = _mean(_f09_inv_days(inventory, cor), 21) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idmean21 w_out=63
def f09eim_f09_ep_inventory_management_idmean21_w63_slope_v041_signal(inventory, cor, closeadj):
    base = _mean(_f09_inv_days(inventory, cor), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idmean21 w_out=126
def f09eim_f09_ep_inventory_management_idmean21_w126_slope_v042_signal(inventory, cor, closeadj):
    base = _mean(_f09_inv_days(inventory, cor), 21) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idymean21 w_out=5
def f09eim_f09_ep_inventory_management_idymean21_w5_slope_v043_signal(inventory, revenue, closeadj):
    base = _mean(_f09_inv_dynamics(inventory, revenue, 21), 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idymean21 w_out=10
def f09eim_f09_ep_inventory_management_idymean21_w10_slope_v044_signal(inventory, revenue, closeadj):
    base = _mean(_f09_inv_dynamics(inventory, revenue, 21), 21) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idymean21 w_out=21
def f09eim_f09_ep_inventory_management_idymean21_w21_slope_v045_signal(inventory, revenue, closeadj):
    base = _mean(_f09_inv_dynamics(inventory, revenue, 21), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idymean21 w_out=42
def f09eim_f09_ep_inventory_management_idymean21_w42_slope_v046_signal(inventory, revenue, closeadj):
    base = _mean(_f09_inv_dynamics(inventory, revenue, 21), 21) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idymean21 w_out=63
def f09eim_f09_ep_inventory_management_idymean21_w63_slope_v047_signal(inventory, revenue, closeadj):
    base = _mean(_f09_inv_dynamics(inventory, revenue, 21), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idymean21 w_out=126
def f09eim_f09_ep_inventory_management_idymean21_w126_slope_v048_signal(inventory, revenue, closeadj):
    base = _mean(_f09_inv_dynamics(inventory, revenue, 21), 21) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idxcl63 w_out=5
def f09eim_f09_ep_inventory_management_idxcl63_w5_slope_v049_signal(inventory, cor, closeadj):
    base = _f09_inv_days(inventory, cor) * closeadj + 0.0 * _mean(closeadj, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idxcl63 w_out=10
def f09eim_f09_ep_inventory_management_idxcl63_w10_slope_v050_signal(inventory, cor, closeadj):
    base = _f09_inv_days(inventory, cor) * closeadj + 0.0 * _mean(closeadj, 63)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idxcl63 w_out=21
def f09eim_f09_ep_inventory_management_idxcl63_w21_slope_v051_signal(inventory, cor, closeadj):
    base = _f09_inv_days(inventory, cor) * closeadj + 0.0 * _mean(closeadj, 63)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idxcl63 w_out=42
def f09eim_f09_ep_inventory_management_idxcl63_w42_slope_v052_signal(inventory, cor, closeadj):
    base = _f09_inv_days(inventory, cor) * closeadj + 0.0 * _mean(closeadj, 63)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idxcl63 w_out=63
def f09eim_f09_ep_inventory_management_idxcl63_w63_slope_v053_signal(inventory, cor, closeadj):
    base = _f09_inv_days(inventory, cor) * closeadj + 0.0 * _mean(closeadj, 63)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idxcl63 w_out=126
def f09eim_f09_ep_inventory_management_idxcl63_w126_slope_v054_signal(inventory, cor, closeadj):
    base = _f09_inv_days(inventory, cor) * closeadj + 0.0 * _mean(closeadj, 63)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of irxcl63 w_out=5
def f09eim_f09_ep_inventory_management_irxcl63_w5_slope_v055_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj + 0.0 * _mean(closeadj, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of irxcl63 w_out=10
def f09eim_f09_ep_inventory_management_irxcl63_w10_slope_v056_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj + 0.0 * _mean(closeadj, 63)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of irxcl63 w_out=21
def f09eim_f09_ep_inventory_management_irxcl63_w21_slope_v057_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj + 0.0 * _mean(closeadj, 63)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of irxcl63 w_out=42
def f09eim_f09_ep_inventory_management_irxcl63_w42_slope_v058_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj + 0.0 * _mean(closeadj, 63)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of irxcl63 w_out=63
def f09eim_f09_ep_inventory_management_irxcl63_w63_slope_v059_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj + 0.0 * _mean(closeadj, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of irxcl63 w_out=126
def f09eim_f09_ep_inventory_management_irxcl63_w126_slope_v060_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj + 0.0 * _mean(closeadj, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idy63 w_out=5
def f09eim_f09_ep_inventory_management_idy63_w5_slope_v061_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idy63 w_out=10
def f09eim_f09_ep_inventory_management_idy63_w10_slope_v062_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 63) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idy63 w_out=21
def f09eim_f09_ep_inventory_management_idy63_w21_slope_v063_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idy63 w_out=42
def f09eim_f09_ep_inventory_management_idy63_w42_slope_v064_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 63) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idy63 w_out=63
def f09eim_f09_ep_inventory_management_idy63_w63_slope_v065_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idy63 w_out=126
def f09eim_f09_ep_inventory_management_idy63_w126_slope_v066_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 63) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idlog63 w_out=5
def f09eim_f09_ep_inventory_management_idlog63_w5_slope_v067_signal(inventory, cor, closeadj):
    base = np.log1p(_f09_inv_days(inventory, cor).abs()) * closeadj + 0.0 * _mean(closeadj, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idlog63 w_out=10
def f09eim_f09_ep_inventory_management_idlog63_w10_slope_v068_signal(inventory, cor, closeadj):
    base = np.log1p(_f09_inv_days(inventory, cor).abs()) * closeadj + 0.0 * _mean(closeadj, 63)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idlog63 w_out=21
def f09eim_f09_ep_inventory_management_idlog63_w21_slope_v069_signal(inventory, cor, closeadj):
    base = np.log1p(_f09_inv_days(inventory, cor).abs()) * closeadj + 0.0 * _mean(closeadj, 63)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idlog63 w_out=42
def f09eim_f09_ep_inventory_management_idlog63_w42_slope_v070_signal(inventory, cor, closeadj):
    base = np.log1p(_f09_inv_days(inventory, cor).abs()) * closeadj + 0.0 * _mean(closeadj, 63)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idlog63 w_out=63
def f09eim_f09_ep_inventory_management_idlog63_w63_slope_v071_signal(inventory, cor, closeadj):
    base = np.log1p(_f09_inv_days(inventory, cor).abs()) * closeadj + 0.0 * _mean(closeadj, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idlog63 w_out=126
def f09eim_f09_ep_inventory_management_idlog63_w126_slope_v072_signal(inventory, cor, closeadj):
    base = np.log1p(_f09_inv_days(inventory, cor).abs()) * closeadj + 0.0 * _mean(closeadj, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of irsq63 w_out=5
def f09eim_f09_ep_inventory_management_irsq63_w5_slope_v073_signal(inventory, revenue, closeadj):
    base = (_f09_inv_to_revenue(inventory, revenue) ** 2) * closeadj + 0.0 * _mean(closeadj, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of irsq63 w_out=10
def f09eim_f09_ep_inventory_management_irsq63_w10_slope_v074_signal(inventory, revenue, closeadj):
    base = (_f09_inv_to_revenue(inventory, revenue) ** 2) * closeadj + 0.0 * _mean(closeadj, 63)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of irsq63 w_out=21
def f09eim_f09_ep_inventory_management_irsq63_w21_slope_v075_signal(inventory, revenue, closeadj):
    base = (_f09_inv_to_revenue(inventory, revenue) ** 2) * closeadj + 0.0 * _mean(closeadj, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of irsq63 w_out=42
def f09eim_f09_ep_inventory_management_irsq63_w42_slope_v076_signal(inventory, revenue, closeadj):
    base = (_f09_inv_to_revenue(inventory, revenue) ** 2) * closeadj + 0.0 * _mean(closeadj, 63)
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of irsq63 w_out=63
def f09eim_f09_ep_inventory_management_irsq63_w63_slope_v077_signal(inventory, revenue, closeadj):
    base = (_f09_inv_to_revenue(inventory, revenue) ** 2) * closeadj + 0.0 * _mean(closeadj, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of irsq63 w_out=126
def f09eim_f09_ep_inventory_management_irsq63_w126_slope_v078_signal(inventory, revenue, closeadj):
    base = (_f09_inv_to_revenue(inventory, revenue) ** 2) * closeadj + 0.0 * _mean(closeadj, 63)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idysq63 w_out=5
def f09eim_f09_ep_inventory_management_idysq63_w5_slope_v079_signal(inventory, revenue, closeadj):
    base = (_f09_inv_dynamics(inventory, revenue, 63) ** 2) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idysq63 w_out=10
def f09eim_f09_ep_inventory_management_idysq63_w10_slope_v080_signal(inventory, revenue, closeadj):
    base = (_f09_inv_dynamics(inventory, revenue, 63) ** 2) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idysq63 w_out=21
def f09eim_f09_ep_inventory_management_idysq63_w21_slope_v081_signal(inventory, revenue, closeadj):
    base = (_f09_inv_dynamics(inventory, revenue, 63) ** 2) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idysq63 w_out=42
def f09eim_f09_ep_inventory_management_idysq63_w42_slope_v082_signal(inventory, revenue, closeadj):
    base = (_f09_inv_dynamics(inventory, revenue, 63) ** 2) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idysq63 w_out=63
def f09eim_f09_ep_inventory_management_idysq63_w63_slope_v083_signal(inventory, revenue, closeadj):
    base = (_f09_inv_dynamics(inventory, revenue, 63) ** 2) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idysq63 w_out=126
def f09eim_f09_ep_inventory_management_idysq63_w126_slope_v084_signal(inventory, revenue, closeadj):
    base = (_f09_inv_dynamics(inventory, revenue, 63) ** 2) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idmean63 w_out=5
def f09eim_f09_ep_inventory_management_idmean63_w5_slope_v085_signal(inventory, cor, closeadj):
    base = _mean(_f09_inv_days(inventory, cor), 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idmean63 w_out=10
def f09eim_f09_ep_inventory_management_idmean63_w10_slope_v086_signal(inventory, cor, closeadj):
    base = _mean(_f09_inv_days(inventory, cor), 63) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idmean63 w_out=21
def f09eim_f09_ep_inventory_management_idmean63_w21_slope_v087_signal(inventory, cor, closeadj):
    base = _mean(_f09_inv_days(inventory, cor), 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idmean63 w_out=42
def f09eim_f09_ep_inventory_management_idmean63_w42_slope_v088_signal(inventory, cor, closeadj):
    base = _mean(_f09_inv_days(inventory, cor), 63) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idmean63 w_out=63
def f09eim_f09_ep_inventory_management_idmean63_w63_slope_v089_signal(inventory, cor, closeadj):
    base = _mean(_f09_inv_days(inventory, cor), 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idmean63 w_out=126
def f09eim_f09_ep_inventory_management_idmean63_w126_slope_v090_signal(inventory, cor, closeadj):
    base = _mean(_f09_inv_days(inventory, cor), 63) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idymean63 w_out=5
def f09eim_f09_ep_inventory_management_idymean63_w5_slope_v091_signal(inventory, revenue, closeadj):
    base = _mean(_f09_inv_dynamics(inventory, revenue, 63), 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idymean63 w_out=10
def f09eim_f09_ep_inventory_management_idymean63_w10_slope_v092_signal(inventory, revenue, closeadj):
    base = _mean(_f09_inv_dynamics(inventory, revenue, 63), 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idymean63 w_out=21
def f09eim_f09_ep_inventory_management_idymean63_w21_slope_v093_signal(inventory, revenue, closeadj):
    base = _mean(_f09_inv_dynamics(inventory, revenue, 63), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idymean63 w_out=42
def f09eim_f09_ep_inventory_management_idymean63_w42_slope_v094_signal(inventory, revenue, closeadj):
    base = _mean(_f09_inv_dynamics(inventory, revenue, 63), 21) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idymean63 w_out=63
def f09eim_f09_ep_inventory_management_idymean63_w63_slope_v095_signal(inventory, revenue, closeadj):
    base = _mean(_f09_inv_dynamics(inventory, revenue, 63), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idymean63 w_out=126
def f09eim_f09_ep_inventory_management_idymean63_w126_slope_v096_signal(inventory, revenue, closeadj):
    base = _mean(_f09_inv_dynamics(inventory, revenue, 63), 21) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idxcl126 w_out=5
def f09eim_f09_ep_inventory_management_idxcl126_w5_slope_v097_signal(inventory, cor, closeadj):
    base = _f09_inv_days(inventory, cor) * closeadj + 0.0 * _mean(closeadj, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idxcl126 w_out=10
def f09eim_f09_ep_inventory_management_idxcl126_w10_slope_v098_signal(inventory, cor, closeadj):
    base = _f09_inv_days(inventory, cor) * closeadj + 0.0 * _mean(closeadj, 126)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idxcl126 w_out=21
def f09eim_f09_ep_inventory_management_idxcl126_w21_slope_v099_signal(inventory, cor, closeadj):
    base = _f09_inv_days(inventory, cor) * closeadj + 0.0 * _mean(closeadj, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idxcl126 w_out=42
def f09eim_f09_ep_inventory_management_idxcl126_w42_slope_v100_signal(inventory, cor, closeadj):
    base = _f09_inv_days(inventory, cor) * closeadj + 0.0 * _mean(closeadj, 126)
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idxcl126 w_out=63
def f09eim_f09_ep_inventory_management_idxcl126_w63_slope_v101_signal(inventory, cor, closeadj):
    base = _f09_inv_days(inventory, cor) * closeadj + 0.0 * _mean(closeadj, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idxcl126 w_out=126
def f09eim_f09_ep_inventory_management_idxcl126_w126_slope_v102_signal(inventory, cor, closeadj):
    base = _f09_inv_days(inventory, cor) * closeadj + 0.0 * _mean(closeadj, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of irxcl126 w_out=5
def f09eim_f09_ep_inventory_management_irxcl126_w5_slope_v103_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj + 0.0 * _mean(closeadj, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of irxcl126 w_out=10
def f09eim_f09_ep_inventory_management_irxcl126_w10_slope_v104_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj + 0.0 * _mean(closeadj, 126)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of irxcl126 w_out=21
def f09eim_f09_ep_inventory_management_irxcl126_w21_slope_v105_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj + 0.0 * _mean(closeadj, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of irxcl126 w_out=42
def f09eim_f09_ep_inventory_management_irxcl126_w42_slope_v106_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj + 0.0 * _mean(closeadj, 126)
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of irxcl126 w_out=63
def f09eim_f09_ep_inventory_management_irxcl126_w63_slope_v107_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj + 0.0 * _mean(closeadj, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of irxcl126 w_out=126
def f09eim_f09_ep_inventory_management_irxcl126_w126_slope_v108_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue) * closeadj + 0.0 * _mean(closeadj, 126)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idy126 w_out=5
def f09eim_f09_ep_inventory_management_idy126_w5_slope_v109_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idy126 w_out=10
def f09eim_f09_ep_inventory_management_idy126_w10_slope_v110_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 126) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idy126 w_out=21
def f09eim_f09_ep_inventory_management_idy126_w21_slope_v111_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idy126 w_out=42
def f09eim_f09_ep_inventory_management_idy126_w42_slope_v112_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 126) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idy126 w_out=63
def f09eim_f09_ep_inventory_management_idy126_w63_slope_v113_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idy126 w_out=126
def f09eim_f09_ep_inventory_management_idy126_w126_slope_v114_signal(inventory, revenue, closeadj):
    base = _f09_inv_dynamics(inventory, revenue, 126) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idlog126 w_out=5
def f09eim_f09_ep_inventory_management_idlog126_w5_slope_v115_signal(inventory, cor, closeadj):
    base = np.log1p(_f09_inv_days(inventory, cor).abs()) * closeadj + 0.0 * _mean(closeadj, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idlog126 w_out=10
def f09eim_f09_ep_inventory_management_idlog126_w10_slope_v116_signal(inventory, cor, closeadj):
    base = np.log1p(_f09_inv_days(inventory, cor).abs()) * closeadj + 0.0 * _mean(closeadj, 126)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idlog126 w_out=21
def f09eim_f09_ep_inventory_management_idlog126_w21_slope_v117_signal(inventory, cor, closeadj):
    base = np.log1p(_f09_inv_days(inventory, cor).abs()) * closeadj + 0.0 * _mean(closeadj, 126)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idlog126 w_out=42
def f09eim_f09_ep_inventory_management_idlog126_w42_slope_v118_signal(inventory, cor, closeadj):
    base = np.log1p(_f09_inv_days(inventory, cor).abs()) * closeadj + 0.0 * _mean(closeadj, 126)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idlog126 w_out=63
def f09eim_f09_ep_inventory_management_idlog126_w63_slope_v119_signal(inventory, cor, closeadj):
    base = np.log1p(_f09_inv_days(inventory, cor).abs()) * closeadj + 0.0 * _mean(closeadj, 126)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idlog126 w_out=126
def f09eim_f09_ep_inventory_management_idlog126_w126_slope_v120_signal(inventory, cor, closeadj):
    base = np.log1p(_f09_inv_days(inventory, cor).abs()) * closeadj + 0.0 * _mean(closeadj, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of irsq126 w_out=5
def f09eim_f09_ep_inventory_management_irsq126_w5_slope_v121_signal(inventory, revenue, closeadj):
    base = (_f09_inv_to_revenue(inventory, revenue) ** 2) * closeadj + 0.0 * _mean(closeadj, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of irsq126 w_out=10
def f09eim_f09_ep_inventory_management_irsq126_w10_slope_v122_signal(inventory, revenue, closeadj):
    base = (_f09_inv_to_revenue(inventory, revenue) ** 2) * closeadj + 0.0 * _mean(closeadj, 126)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of irsq126 w_out=21
def f09eim_f09_ep_inventory_management_irsq126_w21_slope_v123_signal(inventory, revenue, closeadj):
    base = (_f09_inv_to_revenue(inventory, revenue) ** 2) * closeadj + 0.0 * _mean(closeadj, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of irsq126 w_out=42
def f09eim_f09_ep_inventory_management_irsq126_w42_slope_v124_signal(inventory, revenue, closeadj):
    base = (_f09_inv_to_revenue(inventory, revenue) ** 2) * closeadj + 0.0 * _mean(closeadj, 126)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of irsq126 w_out=63
def f09eim_f09_ep_inventory_management_irsq126_w63_slope_v125_signal(inventory, revenue, closeadj):
    base = (_f09_inv_to_revenue(inventory, revenue) ** 2) * closeadj + 0.0 * _mean(closeadj, 126)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of irsq126 w_out=126
def f09eim_f09_ep_inventory_management_irsq126_w126_slope_v126_signal(inventory, revenue, closeadj):
    base = (_f09_inv_to_revenue(inventory, revenue) ** 2) * closeadj + 0.0 * _mean(closeadj, 126)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idysq126 w_out=5
def f09eim_f09_ep_inventory_management_idysq126_w5_slope_v127_signal(inventory, revenue, closeadj):
    base = (_f09_inv_dynamics(inventory, revenue, 126) ** 2) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idysq126 w_out=10
def f09eim_f09_ep_inventory_management_idysq126_w10_slope_v128_signal(inventory, revenue, closeadj):
    base = (_f09_inv_dynamics(inventory, revenue, 126) ** 2) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idysq126 w_out=21
def f09eim_f09_ep_inventory_management_idysq126_w21_slope_v129_signal(inventory, revenue, closeadj):
    base = (_f09_inv_dynamics(inventory, revenue, 126) ** 2) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idysq126 w_out=42
def f09eim_f09_ep_inventory_management_idysq126_w42_slope_v130_signal(inventory, revenue, closeadj):
    base = (_f09_inv_dynamics(inventory, revenue, 126) ** 2) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idysq126 w_out=63
def f09eim_f09_ep_inventory_management_idysq126_w63_slope_v131_signal(inventory, revenue, closeadj):
    base = (_f09_inv_dynamics(inventory, revenue, 126) ** 2) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idysq126 w_out=126
def f09eim_f09_ep_inventory_management_idysq126_w126_slope_v132_signal(inventory, revenue, closeadj):
    base = (_f09_inv_dynamics(inventory, revenue, 126) ** 2) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idmean126 w_out=5
def f09eim_f09_ep_inventory_management_idmean126_w5_slope_v133_signal(inventory, cor, closeadj):
    base = _mean(_f09_inv_days(inventory, cor), 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idmean126 w_out=10
def f09eim_f09_ep_inventory_management_idmean126_w10_slope_v134_signal(inventory, cor, closeadj):
    base = _mean(_f09_inv_days(inventory, cor), 126) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idmean126 w_out=21
def f09eim_f09_ep_inventory_management_idmean126_w21_slope_v135_signal(inventory, cor, closeadj):
    base = _mean(_f09_inv_days(inventory, cor), 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idmean126 w_out=42
def f09eim_f09_ep_inventory_management_idmean126_w42_slope_v136_signal(inventory, cor, closeadj):
    base = _mean(_f09_inv_days(inventory, cor), 126) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idmean126 w_out=63
def f09eim_f09_ep_inventory_management_idmean126_w63_slope_v137_signal(inventory, cor, closeadj):
    base = _mean(_f09_inv_days(inventory, cor), 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idmean126 w_out=126
def f09eim_f09_ep_inventory_management_idmean126_w126_slope_v138_signal(inventory, cor, closeadj):
    base = _mean(_f09_inv_days(inventory, cor), 126) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idymean126 w_out=5
def f09eim_f09_ep_inventory_management_idymean126_w5_slope_v139_signal(inventory, revenue, closeadj):
    base = _mean(_f09_inv_dynamics(inventory, revenue, 126), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idymean126 w_out=10
def f09eim_f09_ep_inventory_management_idymean126_w10_slope_v140_signal(inventory, revenue, closeadj):
    base = _mean(_f09_inv_dynamics(inventory, revenue, 126), 21) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idymean126 w_out=21
def f09eim_f09_ep_inventory_management_idymean126_w21_slope_v141_signal(inventory, revenue, closeadj):
    base = _mean(_f09_inv_dynamics(inventory, revenue, 126), 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idymean126 w_out=42
def f09eim_f09_ep_inventory_management_idymean126_w42_slope_v142_signal(inventory, revenue, closeadj):
    base = _mean(_f09_inv_dynamics(inventory, revenue, 126), 21) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idymean126 w_out=63
def f09eim_f09_ep_inventory_management_idymean126_w63_slope_v143_signal(inventory, revenue, closeadj):
    base = _mean(_f09_inv_dynamics(inventory, revenue, 126), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idymean126 w_out=126
def f09eim_f09_ep_inventory_management_idymean126_w126_slope_v144_signal(inventory, revenue, closeadj):
    base = _mean(_f09_inv_dynamics(inventory, revenue, 126), 21) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idxcl252 w_out=5
def f09eim_f09_ep_inventory_management_idxcl252_w5_slope_v145_signal(inventory, cor, closeadj):
    base = _f09_inv_days(inventory, cor) * closeadj + 0.0 * _mean(closeadj, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idxcl252 w_out=10
def f09eim_f09_ep_inventory_management_idxcl252_w10_slope_v146_signal(inventory, cor, closeadj):
    base = _f09_inv_days(inventory, cor) * closeadj + 0.0 * _mean(closeadj, 252)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idxcl252 w_out=21
def f09eim_f09_ep_inventory_management_idxcl252_w21_slope_v147_signal(inventory, cor, closeadj):
    base = _f09_inv_days(inventory, cor) * closeadj + 0.0 * _mean(closeadj, 252)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idxcl252 w_out=42
def f09eim_f09_ep_inventory_management_idxcl252_w42_slope_v148_signal(inventory, cor, closeadj):
    base = _f09_inv_days(inventory, cor) * closeadj + 0.0 * _mean(closeadj, 252)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idxcl252 w_out=63
def f09eim_f09_ep_inventory_management_idxcl252_w63_slope_v149_signal(inventory, cor, closeadj):
    base = _f09_inv_days(inventory, cor) * closeadj + 0.0 * _mean(closeadj, 252)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of idxcl252 w_out=126
def f09eim_f09_ep_inventory_management_idxcl252_w126_slope_v150_signal(inventory, cor, closeadj):
    base = _f09_inv_days(inventory, cor) * closeadj + 0.0 * _mean(closeadj, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f09eim_f09_ep_inventory_management_idxcl21_w5_slope_v001_signal,
    f09eim_f09_ep_inventory_management_idxcl21_w10_slope_v002_signal,
    f09eim_f09_ep_inventory_management_idxcl21_w21_slope_v003_signal,
    f09eim_f09_ep_inventory_management_idxcl21_w42_slope_v004_signal,
    f09eim_f09_ep_inventory_management_idxcl21_w63_slope_v005_signal,
    f09eim_f09_ep_inventory_management_idxcl21_w126_slope_v006_signal,
    f09eim_f09_ep_inventory_management_irxcl21_w5_slope_v007_signal,
    f09eim_f09_ep_inventory_management_irxcl21_w10_slope_v008_signal,
    f09eim_f09_ep_inventory_management_irxcl21_w21_slope_v009_signal,
    f09eim_f09_ep_inventory_management_irxcl21_w42_slope_v010_signal,
    f09eim_f09_ep_inventory_management_irxcl21_w63_slope_v011_signal,
    f09eim_f09_ep_inventory_management_irxcl21_w126_slope_v012_signal,
    f09eim_f09_ep_inventory_management_idy21_w5_slope_v013_signal,
    f09eim_f09_ep_inventory_management_idy21_w10_slope_v014_signal,
    f09eim_f09_ep_inventory_management_idy21_w21_slope_v015_signal,
    f09eim_f09_ep_inventory_management_idy21_w42_slope_v016_signal,
    f09eim_f09_ep_inventory_management_idy21_w63_slope_v017_signal,
    f09eim_f09_ep_inventory_management_idy21_w126_slope_v018_signal,
    f09eim_f09_ep_inventory_management_idlog21_w5_slope_v019_signal,
    f09eim_f09_ep_inventory_management_idlog21_w10_slope_v020_signal,
    f09eim_f09_ep_inventory_management_idlog21_w21_slope_v021_signal,
    f09eim_f09_ep_inventory_management_idlog21_w42_slope_v022_signal,
    f09eim_f09_ep_inventory_management_idlog21_w63_slope_v023_signal,
    f09eim_f09_ep_inventory_management_idlog21_w126_slope_v024_signal,
    f09eim_f09_ep_inventory_management_irsq21_w5_slope_v025_signal,
    f09eim_f09_ep_inventory_management_irsq21_w10_slope_v026_signal,
    f09eim_f09_ep_inventory_management_irsq21_w21_slope_v027_signal,
    f09eim_f09_ep_inventory_management_irsq21_w42_slope_v028_signal,
    f09eim_f09_ep_inventory_management_irsq21_w63_slope_v029_signal,
    f09eim_f09_ep_inventory_management_irsq21_w126_slope_v030_signal,
    f09eim_f09_ep_inventory_management_idysq21_w5_slope_v031_signal,
    f09eim_f09_ep_inventory_management_idysq21_w10_slope_v032_signal,
    f09eim_f09_ep_inventory_management_idysq21_w21_slope_v033_signal,
    f09eim_f09_ep_inventory_management_idysq21_w42_slope_v034_signal,
    f09eim_f09_ep_inventory_management_idysq21_w63_slope_v035_signal,
    f09eim_f09_ep_inventory_management_idysq21_w126_slope_v036_signal,
    f09eim_f09_ep_inventory_management_idmean21_w5_slope_v037_signal,
    f09eim_f09_ep_inventory_management_idmean21_w10_slope_v038_signal,
    f09eim_f09_ep_inventory_management_idmean21_w21_slope_v039_signal,
    f09eim_f09_ep_inventory_management_idmean21_w42_slope_v040_signal,
    f09eim_f09_ep_inventory_management_idmean21_w63_slope_v041_signal,
    f09eim_f09_ep_inventory_management_idmean21_w126_slope_v042_signal,
    f09eim_f09_ep_inventory_management_idymean21_w5_slope_v043_signal,
    f09eim_f09_ep_inventory_management_idymean21_w10_slope_v044_signal,
    f09eim_f09_ep_inventory_management_idymean21_w21_slope_v045_signal,
    f09eim_f09_ep_inventory_management_idymean21_w42_slope_v046_signal,
    f09eim_f09_ep_inventory_management_idymean21_w63_slope_v047_signal,
    f09eim_f09_ep_inventory_management_idymean21_w126_slope_v048_signal,
    f09eim_f09_ep_inventory_management_idxcl63_w5_slope_v049_signal,
    f09eim_f09_ep_inventory_management_idxcl63_w10_slope_v050_signal,
    f09eim_f09_ep_inventory_management_idxcl63_w21_slope_v051_signal,
    f09eim_f09_ep_inventory_management_idxcl63_w42_slope_v052_signal,
    f09eim_f09_ep_inventory_management_idxcl63_w63_slope_v053_signal,
    f09eim_f09_ep_inventory_management_idxcl63_w126_slope_v054_signal,
    f09eim_f09_ep_inventory_management_irxcl63_w5_slope_v055_signal,
    f09eim_f09_ep_inventory_management_irxcl63_w10_slope_v056_signal,
    f09eim_f09_ep_inventory_management_irxcl63_w21_slope_v057_signal,
    f09eim_f09_ep_inventory_management_irxcl63_w42_slope_v058_signal,
    f09eim_f09_ep_inventory_management_irxcl63_w63_slope_v059_signal,
    f09eim_f09_ep_inventory_management_irxcl63_w126_slope_v060_signal,
    f09eim_f09_ep_inventory_management_idy63_w5_slope_v061_signal,
    f09eim_f09_ep_inventory_management_idy63_w10_slope_v062_signal,
    f09eim_f09_ep_inventory_management_idy63_w21_slope_v063_signal,
    f09eim_f09_ep_inventory_management_idy63_w42_slope_v064_signal,
    f09eim_f09_ep_inventory_management_idy63_w63_slope_v065_signal,
    f09eim_f09_ep_inventory_management_idy63_w126_slope_v066_signal,
    f09eim_f09_ep_inventory_management_idlog63_w5_slope_v067_signal,
    f09eim_f09_ep_inventory_management_idlog63_w10_slope_v068_signal,
    f09eim_f09_ep_inventory_management_idlog63_w21_slope_v069_signal,
    f09eim_f09_ep_inventory_management_idlog63_w42_slope_v070_signal,
    f09eim_f09_ep_inventory_management_idlog63_w63_slope_v071_signal,
    f09eim_f09_ep_inventory_management_idlog63_w126_slope_v072_signal,
    f09eim_f09_ep_inventory_management_irsq63_w5_slope_v073_signal,
    f09eim_f09_ep_inventory_management_irsq63_w10_slope_v074_signal,
    f09eim_f09_ep_inventory_management_irsq63_w21_slope_v075_signal,
    f09eim_f09_ep_inventory_management_irsq63_w42_slope_v076_signal,
    f09eim_f09_ep_inventory_management_irsq63_w63_slope_v077_signal,
    f09eim_f09_ep_inventory_management_irsq63_w126_slope_v078_signal,
    f09eim_f09_ep_inventory_management_idysq63_w5_slope_v079_signal,
    f09eim_f09_ep_inventory_management_idysq63_w10_slope_v080_signal,
    f09eim_f09_ep_inventory_management_idysq63_w21_slope_v081_signal,
    f09eim_f09_ep_inventory_management_idysq63_w42_slope_v082_signal,
    f09eim_f09_ep_inventory_management_idysq63_w63_slope_v083_signal,
    f09eim_f09_ep_inventory_management_idysq63_w126_slope_v084_signal,
    f09eim_f09_ep_inventory_management_idmean63_w5_slope_v085_signal,
    f09eim_f09_ep_inventory_management_idmean63_w10_slope_v086_signal,
    f09eim_f09_ep_inventory_management_idmean63_w21_slope_v087_signal,
    f09eim_f09_ep_inventory_management_idmean63_w42_slope_v088_signal,
    f09eim_f09_ep_inventory_management_idmean63_w63_slope_v089_signal,
    f09eim_f09_ep_inventory_management_idmean63_w126_slope_v090_signal,
    f09eim_f09_ep_inventory_management_idymean63_w5_slope_v091_signal,
    f09eim_f09_ep_inventory_management_idymean63_w10_slope_v092_signal,
    f09eim_f09_ep_inventory_management_idymean63_w21_slope_v093_signal,
    f09eim_f09_ep_inventory_management_idymean63_w42_slope_v094_signal,
    f09eim_f09_ep_inventory_management_idymean63_w63_slope_v095_signal,
    f09eim_f09_ep_inventory_management_idymean63_w126_slope_v096_signal,
    f09eim_f09_ep_inventory_management_idxcl126_w5_slope_v097_signal,
    f09eim_f09_ep_inventory_management_idxcl126_w10_slope_v098_signal,
    f09eim_f09_ep_inventory_management_idxcl126_w21_slope_v099_signal,
    f09eim_f09_ep_inventory_management_idxcl126_w42_slope_v100_signal,
    f09eim_f09_ep_inventory_management_idxcl126_w63_slope_v101_signal,
    f09eim_f09_ep_inventory_management_idxcl126_w126_slope_v102_signal,
    f09eim_f09_ep_inventory_management_irxcl126_w5_slope_v103_signal,
    f09eim_f09_ep_inventory_management_irxcl126_w10_slope_v104_signal,
    f09eim_f09_ep_inventory_management_irxcl126_w21_slope_v105_signal,
    f09eim_f09_ep_inventory_management_irxcl126_w42_slope_v106_signal,
    f09eim_f09_ep_inventory_management_irxcl126_w63_slope_v107_signal,
    f09eim_f09_ep_inventory_management_irxcl126_w126_slope_v108_signal,
    f09eim_f09_ep_inventory_management_idy126_w5_slope_v109_signal,
    f09eim_f09_ep_inventory_management_idy126_w10_slope_v110_signal,
    f09eim_f09_ep_inventory_management_idy126_w21_slope_v111_signal,
    f09eim_f09_ep_inventory_management_idy126_w42_slope_v112_signal,
    f09eim_f09_ep_inventory_management_idy126_w63_slope_v113_signal,
    f09eim_f09_ep_inventory_management_idy126_w126_slope_v114_signal,
    f09eim_f09_ep_inventory_management_idlog126_w5_slope_v115_signal,
    f09eim_f09_ep_inventory_management_idlog126_w10_slope_v116_signal,
    f09eim_f09_ep_inventory_management_idlog126_w21_slope_v117_signal,
    f09eim_f09_ep_inventory_management_idlog126_w42_slope_v118_signal,
    f09eim_f09_ep_inventory_management_idlog126_w63_slope_v119_signal,
    f09eim_f09_ep_inventory_management_idlog126_w126_slope_v120_signal,
    f09eim_f09_ep_inventory_management_irsq126_w5_slope_v121_signal,
    f09eim_f09_ep_inventory_management_irsq126_w10_slope_v122_signal,
    f09eim_f09_ep_inventory_management_irsq126_w21_slope_v123_signal,
    f09eim_f09_ep_inventory_management_irsq126_w42_slope_v124_signal,
    f09eim_f09_ep_inventory_management_irsq126_w63_slope_v125_signal,
    f09eim_f09_ep_inventory_management_irsq126_w126_slope_v126_signal,
    f09eim_f09_ep_inventory_management_idysq126_w5_slope_v127_signal,
    f09eim_f09_ep_inventory_management_idysq126_w10_slope_v128_signal,
    f09eim_f09_ep_inventory_management_idysq126_w21_slope_v129_signal,
    f09eim_f09_ep_inventory_management_idysq126_w42_slope_v130_signal,
    f09eim_f09_ep_inventory_management_idysq126_w63_slope_v131_signal,
    f09eim_f09_ep_inventory_management_idysq126_w126_slope_v132_signal,
    f09eim_f09_ep_inventory_management_idmean126_w5_slope_v133_signal,
    f09eim_f09_ep_inventory_management_idmean126_w10_slope_v134_signal,
    f09eim_f09_ep_inventory_management_idmean126_w21_slope_v135_signal,
    f09eim_f09_ep_inventory_management_idmean126_w42_slope_v136_signal,
    f09eim_f09_ep_inventory_management_idmean126_w63_slope_v137_signal,
    f09eim_f09_ep_inventory_management_idmean126_w126_slope_v138_signal,
    f09eim_f09_ep_inventory_management_idymean126_w5_slope_v139_signal,
    f09eim_f09_ep_inventory_management_idymean126_w10_slope_v140_signal,
    f09eim_f09_ep_inventory_management_idymean126_w21_slope_v141_signal,
    f09eim_f09_ep_inventory_management_idymean126_w42_slope_v142_signal,
    f09eim_f09_ep_inventory_management_idymean126_w63_slope_v143_signal,
    f09eim_f09_ep_inventory_management_idymean126_w126_slope_v144_signal,
    f09eim_f09_ep_inventory_management_idxcl252_w5_slope_v145_signal,
    f09eim_f09_ep_inventory_management_idxcl252_w10_slope_v146_signal,
    f09eim_f09_ep_inventory_management_idxcl252_w21_slope_v147_signal,
    f09eim_f09_ep_inventory_management_idxcl252_w42_slope_v148_signal,
    f09eim_f09_ep_inventory_management_idxcl252_w63_slope_v149_signal,
    f09eim_f09_ep_inventory_management_idxcl252_w126_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F09_EP_INVENTORY_MANAGEMENT_REGISTRY_SLOPE_001_150 = REGISTRY


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
    domain_primitives = ("_f09_inv_days", "_f09_inv_to_revenue", "_f09_inv_dynamics")
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
    print(f"OK f09_ep_inventory_management_2nd_derivatives_001_150_claude: {n_features} features pass")
