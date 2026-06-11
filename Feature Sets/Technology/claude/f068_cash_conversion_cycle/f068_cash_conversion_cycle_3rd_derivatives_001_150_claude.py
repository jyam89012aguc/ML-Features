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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _accel(s, w):
    return s.diff(periods=w).diff(periods=w)


# ===== folder domain primitives =====
def _f068_dso(receivables, revenue):
    return 365 * receivables / revenue.abs().replace(0, np.nan)


# 21d acceleration of dso
def f068ccc_f068_cash_conversion_cycle_dso_accel_21d_3d_v001_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dso
def f068ccc_f068_cash_conversion_cycle_dso_accel_63d_3d_v002_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of dso
def f068ccc_f068_cash_conversion_cycle_dso_accel_126d_3d_v003_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dso
def f068ccc_f068_cash_conversion_cycle_dso_accel_252d_3d_v004_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of dio
def f068ccc_f068_cash_conversion_cycle_dio_accel_21d_3d_v005_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dio
def f068ccc_f068_cash_conversion_cycle_dio_accel_63d_3d_v006_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of dio
def f068ccc_f068_cash_conversion_cycle_dio_accel_126d_3d_v007_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dio
def f068ccc_f068_cash_conversion_cycle_dio_accel_252d_3d_v008_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_accel_21d_3d_v009_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_accel_63d_3d_v010_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_accel_126d_3d_v011_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_accel_252d_3d_v012_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_accel_21d_3d_v013_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_accel_63d_3d_v014_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_accel_126d_3d_v015_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_accel_252d_3d_v016_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_accel_21d_3d_v017_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_accel_63d_3d_v018_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_accel_126d_3d_v019_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_accel_252d_3d_v020_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_accel_21d_3d_v021_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_accel_63d_3d_v022_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_accel_126d_3d_v023_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_accel_252d_3d_v024_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_accel_21d_3d_v025_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_accel_63d_3d_v026_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_accel_126d_3d_v027_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_accel_252d_3d_v028_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of dso
def f068ccc_f068_cash_conversion_cycle_dso_slopez_21d_z126_3d_v029_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of dso
def f068ccc_f068_cash_conversion_cycle_dso_slopez_63d_z252_3d_v030_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of dso
def f068ccc_f068_cash_conversion_cycle_dso_slopez_126d_z252_3d_v031_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of dso
def f068ccc_f068_cash_conversion_cycle_dso_slopez_252d_z504_3d_v032_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of dio
def f068ccc_f068_cash_conversion_cycle_dio_slopez_21d_z126_3d_v033_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of dio
def f068ccc_f068_cash_conversion_cycle_dio_slopez_63d_z252_3d_v034_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of dio
def f068ccc_f068_cash_conversion_cycle_dio_slopez_126d_z252_3d_v035_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of dio
def f068ccc_f068_cash_conversion_cycle_dio_slopez_252d_z504_3d_v036_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_slopez_21d_z126_3d_v037_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_slopez_63d_z252_3d_v038_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_slopez_126d_z252_3d_v039_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_slopez_252d_z504_3d_v040_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_slopez_21d_z126_3d_v041_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_slopez_63d_z252_3d_v042_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_slopez_126d_z252_3d_v043_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_slopez_252d_z504_3d_v044_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_slopez_21d_z126_3d_v045_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_slopez_63d_z252_3d_v046_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_slopez_126d_z252_3d_v047_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_slopez_252d_z504_3d_v048_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_slopez_21d_z126_3d_v049_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_slopez_63d_z252_3d_v050_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_slopez_126d_z252_3d_v051_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_slopez_252d_z504_3d_v052_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_slopez_21d_z126_3d_v053_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_slopez_63d_z252_3d_v054_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_slopez_126d_z252_3d_v055_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_slopez_252d_z504_3d_v056_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of dso
def f068ccc_f068_cash_conversion_cycle_dso_jerk_21d_3d_v057_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of dso
def f068ccc_f068_cash_conversion_cycle_dso_jerk_63d_3d_v058_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of dso
def f068ccc_f068_cash_conversion_cycle_dso_jerk_126d_3d_v059_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of dio
def f068ccc_f068_cash_conversion_cycle_dio_jerk_21d_3d_v060_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of dio
def f068ccc_f068_cash_conversion_cycle_dio_jerk_63d_3d_v061_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of dio
def f068ccc_f068_cash_conversion_cycle_dio_jerk_126d_3d_v062_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_jerk_21d_3d_v063_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_jerk_63d_3d_v064_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_jerk_126d_3d_v065_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_jerk_21d_3d_v066_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_jerk_63d_3d_v067_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_jerk_126d_3d_v068_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_jerk_21d_3d_v069_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_jerk_63d_3d_v070_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_jerk_126d_3d_v071_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_jerk_21d_3d_v072_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_jerk_63d_3d_v073_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_jerk_126d_3d_v074_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_jerk_21d_3d_v075_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_jerk_63d_3d_v076_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_jerk_126d_3d_v077_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of dso smoothed over 252d
def f068ccc_f068_cash_conversion_cycle_dso_smoothaccel_63d_sm252_3d_v078_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of dso smoothed over 504d
def f068ccc_f068_cash_conversion_cycle_dso_smoothaccel_252d_sm504_3d_v079_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of dio smoothed over 252d
def f068ccc_f068_cash_conversion_cycle_dio_smoothaccel_63d_sm252_3d_v080_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of dio smoothed over 504d
def f068ccc_f068_cash_conversion_cycle_dio_smoothaccel_252d_sm504_3d_v081_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of dpo smoothed over 252d
def f068ccc_f068_cash_conversion_cycle_dpo_smoothaccel_63d_sm252_3d_v082_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of dpo smoothed over 504d
def f068ccc_f068_cash_conversion_cycle_dpo_smoothaccel_252d_sm504_3d_v083_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ccc smoothed over 252d
def f068ccc_f068_cash_conversion_cycle_ccc_smoothaccel_63d_sm252_3d_v084_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ccc smoothed over 504d
def f068ccc_f068_cash_conversion_cycle_ccc_smoothaccel_252d_sm504_3d_v085_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ccc_chg_y smoothed over 252d
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_smoothaccel_63d_sm252_3d_v086_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ccc_chg_y smoothed over 504d
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_smoothaccel_252d_sm504_3d_v087_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of dso_yoy smoothed over 252d
def f068ccc_f068_cash_conversion_cycle_dso_yoy_smoothaccel_63d_sm252_3d_v088_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of dso_yoy smoothed over 504d
def f068ccc_f068_cash_conversion_cycle_dso_yoy_smoothaccel_252d_sm504_3d_v089_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of dio_yoy smoothed over 252d
def f068ccc_f068_cash_conversion_cycle_dio_yoy_smoothaccel_63d_sm252_3d_v090_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of dio_yoy smoothed over 504d
def f068ccc_f068_cash_conversion_cycle_dio_yoy_smoothaccel_252d_sm504_3d_v091_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of dso
def f068ccc_f068_cash_conversion_cycle_dso_accelz_21d_z252_3d_v092_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of dso
def f068ccc_f068_cash_conversion_cycle_dso_accelz_63d_z504_3d_v093_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of dio
def f068ccc_f068_cash_conversion_cycle_dio_accelz_21d_z252_3d_v094_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of dio
def f068ccc_f068_cash_conversion_cycle_dio_accelz_63d_z504_3d_v095_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_accelz_21d_z252_3d_v096_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_accelz_63d_z504_3d_v097_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_accelz_21d_z252_3d_v098_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_accelz_63d_z504_3d_v099_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_accelz_21d_z252_3d_v100_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_accelz_63d_z504_3d_v101_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_accelz_21d_z252_3d_v102_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_accelz_63d_z504_3d_v103_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_accelz_21d_z252_3d_v104_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_accelz_63d_z504_3d_v105_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in dso (raw count, no price scaling)
def f068ccc_f068_cash_conversion_cycle_dso_signflip_63d_3d_v106_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in dso (raw count, no price scaling)
def f068ccc_f068_cash_conversion_cycle_dso_signflip_252d_3d_v107_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in dio (raw count, no price scaling)
def f068ccc_f068_cash_conversion_cycle_dio_signflip_63d_3d_v108_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in dio (raw count, no price scaling)
def f068ccc_f068_cash_conversion_cycle_dio_signflip_252d_3d_v109_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in dpo (raw count, no price scaling)
def f068ccc_f068_cash_conversion_cycle_dpo_signflip_63d_3d_v110_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in dpo (raw count, no price scaling)
def f068ccc_f068_cash_conversion_cycle_dpo_signflip_252d_3d_v111_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ccc (raw count, no price scaling)
def f068ccc_f068_cash_conversion_cycle_ccc_signflip_63d_3d_v112_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ccc (raw count, no price scaling)
def f068ccc_f068_cash_conversion_cycle_ccc_signflip_252d_3d_v113_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ccc_chg_y (raw count, no price scaling)
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_signflip_63d_3d_v114_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ccc_chg_y (raw count, no price scaling)
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_signflip_252d_3d_v115_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in dso_yoy (raw count, no price scaling)
def f068ccc_f068_cash_conversion_cycle_dso_yoy_signflip_63d_3d_v116_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in dso_yoy (raw count, no price scaling)
def f068ccc_f068_cash_conversion_cycle_dso_yoy_signflip_252d_3d_v117_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in dio_yoy (raw count, no price scaling)
def f068ccc_f068_cash_conversion_cycle_dio_yoy_signflip_63d_3d_v118_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in dio_yoy (raw count, no price scaling)
def f068ccc_f068_cash_conversion_cycle_dio_yoy_signflip_252d_3d_v119_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dso normalized by 252d range
def f068ccc_f068_cash_conversion_cycle_dso_rngaccel_63d_r252_3d_v120_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dso normalized by 504d range
def f068ccc_f068_cash_conversion_cycle_dso_rngaccel_252d_r504_3d_v121_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dio normalized by 252d range
def f068ccc_f068_cash_conversion_cycle_dio_rngaccel_63d_r252_3d_v122_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dio normalized by 504d range
def f068ccc_f068_cash_conversion_cycle_dio_rngaccel_252d_r504_3d_v123_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dpo normalized by 252d range
def f068ccc_f068_cash_conversion_cycle_dpo_rngaccel_63d_r252_3d_v124_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dpo normalized by 504d range
def f068ccc_f068_cash_conversion_cycle_dpo_rngaccel_252d_r504_3d_v125_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ccc normalized by 252d range
def f068ccc_f068_cash_conversion_cycle_ccc_rngaccel_63d_r252_3d_v126_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ccc normalized by 504d range
def f068ccc_f068_cash_conversion_cycle_ccc_rngaccel_252d_r504_3d_v127_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ccc_chg_y normalized by 252d range
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_rngaccel_63d_r252_3d_v128_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ccc_chg_y normalized by 504d range
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_rngaccel_252d_r504_3d_v129_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dso_yoy normalized by 252d range
def f068ccc_f068_cash_conversion_cycle_dso_yoy_rngaccel_63d_r252_3d_v130_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dso_yoy normalized by 504d range
def f068ccc_f068_cash_conversion_cycle_dso_yoy_rngaccel_252d_r504_3d_v131_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dio_yoy normalized by 252d range
def f068ccc_f068_cash_conversion_cycle_dio_yoy_rngaccel_63d_r252_3d_v132_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dio_yoy normalized by 504d range
def f068ccc_f068_cash_conversion_cycle_dio_yoy_rngaccel_252d_r504_3d_v133_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of dso
def f068ccc_f068_cash_conversion_cycle_dso_cumslope_21d_3d_v134_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of dso
def f068ccc_f068_cash_conversion_cycle_dso_cumslope_63d_3d_v135_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of dso
def f068ccc_f068_cash_conversion_cycle_dso_cumslope_252d_3d_v136_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of dio
def f068ccc_f068_cash_conversion_cycle_dio_cumslope_21d_3d_v137_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of dio
def f068ccc_f068_cash_conversion_cycle_dio_cumslope_63d_3d_v138_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of dio
def f068ccc_f068_cash_conversion_cycle_dio_cumslope_252d_3d_v139_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_cumslope_21d_3d_v140_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_cumslope_63d_3d_v141_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_cumslope_252d_3d_v142_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_cumslope_21d_3d_v143_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_cumslope_63d_3d_v144_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_cumslope_252d_3d_v145_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_cumslope_21d_3d_v146_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_cumslope_63d_3d_v147_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_cumslope_252d_3d_v148_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_cumslope_21d_3d_v149_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_cumslope_63d_3d_v150_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

