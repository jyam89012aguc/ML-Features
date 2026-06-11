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


# 21d slope of dso
def f068ccc_f068_cash_conversion_cycle_dso_slope_21d_2d_v001_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of dso
def f068ccc_f068_cash_conversion_cycle_dso_slope_63d_2d_v002_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of dso
def f068ccc_f068_cash_conversion_cycle_dso_slope_126d_2d_v003_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of dso
def f068ccc_f068_cash_conversion_cycle_dso_slope_252d_2d_v004_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of dso
def f068ccc_f068_cash_conversion_cycle_dso_slope_504d_2d_v005_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of dio
def f068ccc_f068_cash_conversion_cycle_dio_slope_21d_2d_v006_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of dio
def f068ccc_f068_cash_conversion_cycle_dio_slope_63d_2d_v007_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of dio
def f068ccc_f068_cash_conversion_cycle_dio_slope_126d_2d_v008_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of dio
def f068ccc_f068_cash_conversion_cycle_dio_slope_252d_2d_v009_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of dio
def f068ccc_f068_cash_conversion_cycle_dio_slope_504d_2d_v010_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_slope_21d_2d_v011_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_slope_63d_2d_v012_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_slope_126d_2d_v013_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_slope_252d_2d_v014_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_slope_504d_2d_v015_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_slope_21d_2d_v016_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_slope_63d_2d_v017_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_slope_126d_2d_v018_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_slope_252d_2d_v019_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_slope_504d_2d_v020_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_slope_21d_2d_v021_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_slope_63d_2d_v022_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_slope_126d_2d_v023_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_slope_252d_2d_v024_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_slope_504d_2d_v025_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_slope_21d_2d_v026_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_slope_63d_2d_v027_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_slope_126d_2d_v028_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_slope_252d_2d_v029_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_slope_504d_2d_v030_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_slope_21d_2d_v031_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_slope_63d_2d_v032_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_slope_126d_2d_v033_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_slope_252d_2d_v034_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_slope_504d_2d_v035_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of dso
def f068ccc_f068_cash_conversion_cycle_dso_sm21_sl21_2d_v036_signal(receivables, revenue, closeadj):
    base = _mean(_f068_dso(receivables, revenue), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of dso
def f068ccc_f068_cash_conversion_cycle_dso_sm63_sl21_2d_v037_signal(receivables, revenue, closeadj):
    base = _mean(_f068_dso(receivables, revenue), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of dso
def f068ccc_f068_cash_conversion_cycle_dso_sm63_sl63_2d_v038_signal(receivables, revenue, closeadj):
    base = _mean(_f068_dso(receivables, revenue), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of dso
def f068ccc_f068_cash_conversion_cycle_dso_sm252_sl63_2d_v039_signal(receivables, revenue, closeadj):
    base = _mean(_f068_dso(receivables, revenue), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of dso
def f068ccc_f068_cash_conversion_cycle_dso_sm252_sl126_2d_v040_signal(receivables, revenue, closeadj):
    base = _mean(_f068_dso(receivables, revenue), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of dio
def f068ccc_f068_cash_conversion_cycle_dio_sm21_sl21_2d_v041_signal(inventory, cor, closeadj):
    base = _mean(365 * inventory / cor.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of dio
def f068ccc_f068_cash_conversion_cycle_dio_sm63_sl21_2d_v042_signal(inventory, cor, closeadj):
    base = _mean(365 * inventory / cor.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of dio
def f068ccc_f068_cash_conversion_cycle_dio_sm63_sl63_2d_v043_signal(inventory, cor, closeadj):
    base = _mean(365 * inventory / cor.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of dio
def f068ccc_f068_cash_conversion_cycle_dio_sm252_sl63_2d_v044_signal(inventory, cor, closeadj):
    base = _mean(365 * inventory / cor.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of dio
def f068ccc_f068_cash_conversion_cycle_dio_sm252_sl126_2d_v045_signal(inventory, cor, closeadj):
    base = _mean(365 * inventory / cor.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_sm21_sl21_2d_v046_signal(payables, opex, closeadj):
    base = _mean(365 * payables / opex.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_sm63_sl21_2d_v047_signal(payables, opex, closeadj):
    base = _mean(365 * payables / opex.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_sm63_sl63_2d_v048_signal(payables, opex, closeadj):
    base = _mean(365 * payables / opex.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_sm252_sl63_2d_v049_signal(payables, opex, closeadj):
    base = _mean(365 * payables / opex.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_sm252_sl126_2d_v050_signal(payables, opex, closeadj):
    base = _mean(365 * payables / opex.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_sm21_sl21_2d_v051_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _mean(_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_sm63_sl21_2d_v052_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _mean(_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_sm63_sl63_2d_v053_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _mean(_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_sm252_sl63_2d_v054_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _mean(_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_sm252_sl126_2d_v055_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _mean(_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_sm21_sl21_2d_v056_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _mean((_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_sm63_sl21_2d_v057_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _mean((_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_sm63_sl63_2d_v058_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _mean((_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_sm252_sl63_2d_v059_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _mean((_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_sm252_sl126_2d_v060_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _mean((_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_sm21_sl21_2d_v061_signal(receivables, revenue, closeadj):
    base = _mean(_f068_dso(receivables, revenue).diff(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_sm63_sl21_2d_v062_signal(receivables, revenue, closeadj):
    base = _mean(_f068_dso(receivables, revenue).diff(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_sm63_sl63_2d_v063_signal(receivables, revenue, closeadj):
    base = _mean(_f068_dso(receivables, revenue).diff(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_sm252_sl63_2d_v064_signal(receivables, revenue, closeadj):
    base = _mean(_f068_dso(receivables, revenue).diff(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_sm252_sl126_2d_v065_signal(receivables, revenue, closeadj):
    base = _mean(_f068_dso(receivables, revenue).diff(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_sm21_sl21_2d_v066_signal(inventory, cor, closeadj):
    base = _mean((365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_sm63_sl21_2d_v067_signal(inventory, cor, closeadj):
    base = _mean((365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_sm63_sl63_2d_v068_signal(inventory, cor, closeadj):
    base = _mean((365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_sm252_sl63_2d_v069_signal(inventory, cor, closeadj):
    base = _mean((365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_sm252_sl126_2d_v070_signal(inventory, cor, closeadj):
    base = _mean((365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of dso
def f068ccc_f068_cash_conversion_cycle_dso_pctslope_21d_2d_v071_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of dso
def f068ccc_f068_cash_conversion_cycle_dso_pctslope_63d_2d_v072_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of dso
def f068ccc_f068_cash_conversion_cycle_dso_pctslope_252d_2d_v073_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of dio
def f068ccc_f068_cash_conversion_cycle_dio_pctslope_21d_2d_v074_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of dio
def f068ccc_f068_cash_conversion_cycle_dio_pctslope_63d_2d_v075_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of dio
def f068ccc_f068_cash_conversion_cycle_dio_pctslope_252d_2d_v076_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_pctslope_21d_2d_v077_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_pctslope_63d_2d_v078_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_pctslope_252d_2d_v079_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_pctslope_21d_2d_v080_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_pctslope_63d_2d_v081_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_pctslope_252d_2d_v082_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_pctslope_21d_2d_v083_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_pctslope_63d_2d_v084_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_pctslope_252d_2d_v085_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_pctslope_21d_2d_v086_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_pctslope_63d_2d_v087_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_pctslope_252d_2d_v088_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_pctslope_21d_2d_v089_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_pctslope_63d_2d_v090_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_pctslope_252d_2d_v091_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of dso
def f068ccc_f068_cash_conversion_cycle_dso_sgnslope_21d_2d_v092_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of dso
def f068ccc_f068_cash_conversion_cycle_dso_sgnslope_63d_2d_v093_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of dso
def f068ccc_f068_cash_conversion_cycle_dso_sgnslope_252d_2d_v094_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of dio
def f068ccc_f068_cash_conversion_cycle_dio_sgnslope_21d_2d_v095_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of dio
def f068ccc_f068_cash_conversion_cycle_dio_sgnslope_63d_2d_v096_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of dio
def f068ccc_f068_cash_conversion_cycle_dio_sgnslope_252d_2d_v097_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_sgnslope_21d_2d_v098_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_sgnslope_63d_2d_v099_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_sgnslope_252d_2d_v100_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_sgnslope_21d_2d_v101_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_sgnslope_63d_2d_v102_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_sgnslope_252d_2d_v103_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_sgnslope_21d_2d_v104_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_sgnslope_63d_2d_v105_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_sgnslope_252d_2d_v106_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_sgnslope_21d_2d_v107_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_sgnslope_63d_2d_v108_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_sgnslope_252d_2d_v109_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_sgnslope_21d_2d_v110_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_sgnslope_63d_2d_v111_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_sgnslope_252d_2d_v112_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of dso
def f068ccc_f068_cash_conversion_cycle_dso_logmagslope_21d_2d_v113_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of dso
def f068ccc_f068_cash_conversion_cycle_dso_logmagslope_63d_2d_v114_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of dso
def f068ccc_f068_cash_conversion_cycle_dso_logmagslope_252d_2d_v115_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of dio
def f068ccc_f068_cash_conversion_cycle_dio_logmagslope_21d_2d_v116_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of dio
def f068ccc_f068_cash_conversion_cycle_dio_logmagslope_63d_2d_v117_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of dio
def f068ccc_f068_cash_conversion_cycle_dio_logmagslope_252d_2d_v118_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_logmagslope_21d_2d_v119_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_logmagslope_63d_2d_v120_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_logmagslope_252d_2d_v121_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_logmagslope_21d_2d_v122_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_logmagslope_63d_2d_v123_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_logmagslope_252d_2d_v124_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_logmagslope_21d_2d_v125_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_logmagslope_63d_2d_v126_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_logmagslope_252d_2d_v127_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_logmagslope_21d_2d_v128_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_logmagslope_63d_2d_v129_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_logmagslope_252d_2d_v130_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_logmagslope_21d_2d_v131_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_logmagslope_63d_2d_v132_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_logmagslope_252d_2d_v133_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|dso|
def f068ccc_f068_cash_conversion_cycle_dso_logslope_63d_2d_v134_signal(receivables, revenue, closeadj):
    base = np.log((_f068_dso(receivables, revenue)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|dso|
def f068ccc_f068_cash_conversion_cycle_dso_logslope_252d_2d_v135_signal(receivables, revenue, closeadj):
    base = np.log((_f068_dso(receivables, revenue)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|dio|
def f068ccc_f068_cash_conversion_cycle_dio_logslope_63d_2d_v136_signal(inventory, cor, closeadj):
    base = np.log((365 * inventory / cor.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|dio|
def f068ccc_f068_cash_conversion_cycle_dio_logslope_252d_2d_v137_signal(inventory, cor, closeadj):
    base = np.log((365 * inventory / cor.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|dpo|
def f068ccc_f068_cash_conversion_cycle_dpo_logslope_63d_2d_v138_signal(payables, opex, closeadj):
    base = np.log((365 * payables / opex.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|dpo|
def f068ccc_f068_cash_conversion_cycle_dpo_logslope_252d_2d_v139_signal(payables, opex, closeadj):
    base = np.log((365 * payables / opex.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ccc|
def f068ccc_f068_cash_conversion_cycle_ccc_logslope_63d_2d_v140_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = np.log((_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ccc|
def f068ccc_f068_cash_conversion_cycle_ccc_logslope_252d_2d_v141_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = np.log((_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ccc_chg_y|
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_logslope_63d_2d_v142_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = np.log(((_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ccc_chg_y|
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_logslope_252d_2d_v143_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = np.log(((_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|dso_yoy|
def f068ccc_f068_cash_conversion_cycle_dso_yoy_logslope_63d_2d_v144_signal(receivables, revenue, closeadj):
    base = np.log((_f068_dso(receivables, revenue).diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|dso_yoy|
def f068ccc_f068_cash_conversion_cycle_dso_yoy_logslope_252d_2d_v145_signal(receivables, revenue, closeadj):
    base = np.log((_f068_dso(receivables, revenue).diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|dio_yoy|
def f068ccc_f068_cash_conversion_cycle_dio_yoy_logslope_63d_2d_v146_signal(inventory, cor, closeadj):
    base = np.log(((365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|dio_yoy|
def f068ccc_f068_cash_conversion_cycle_dio_yoy_logslope_252d_2d_v147_signal(inventory, cor, closeadj):
    base = np.log(((365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

