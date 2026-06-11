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


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f068_dso(receivables, revenue):
    return 365 * receivables / revenue.abs().replace(0, np.nan)


# 21d mean of dso scaled by closeadj
def f068ccc_f068_cash_conversion_cycle_dso_mean_21d_base_v001_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of dso scaled by closeadj
def f068ccc_f068_cash_conversion_cycle_dso_mean_63d_base_v002_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of dso scaled by closeadj
def f068ccc_f068_cash_conversion_cycle_dso_mean_126d_base_v003_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of dso scaled by closeadj
def f068ccc_f068_cash_conversion_cycle_dso_mean_252d_base_v004_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of dso scaled by closeadj
def f068ccc_f068_cash_conversion_cycle_dso_mean_504d_base_v005_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of dio scaled by closeadj
def f068ccc_f068_cash_conversion_cycle_dio_mean_21d_base_v006_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of dio scaled by closeadj
def f068ccc_f068_cash_conversion_cycle_dio_mean_63d_base_v007_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of dio scaled by closeadj
def f068ccc_f068_cash_conversion_cycle_dio_mean_126d_base_v008_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of dio scaled by closeadj
def f068ccc_f068_cash_conversion_cycle_dio_mean_252d_base_v009_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of dio scaled by closeadj
def f068ccc_f068_cash_conversion_cycle_dio_mean_504d_base_v010_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of dpo scaled by closeadj
def f068ccc_f068_cash_conversion_cycle_dpo_mean_21d_base_v011_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of dpo scaled by closeadj
def f068ccc_f068_cash_conversion_cycle_dpo_mean_63d_base_v012_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of dpo scaled by closeadj
def f068ccc_f068_cash_conversion_cycle_dpo_mean_126d_base_v013_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of dpo scaled by closeadj
def f068ccc_f068_cash_conversion_cycle_dpo_mean_252d_base_v014_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of dpo scaled by closeadj
def f068ccc_f068_cash_conversion_cycle_dpo_mean_504d_base_v015_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ccc scaled by closeadj
def f068ccc_f068_cash_conversion_cycle_ccc_mean_21d_base_v016_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ccc scaled by closeadj
def f068ccc_f068_cash_conversion_cycle_ccc_mean_63d_base_v017_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ccc scaled by closeadj
def f068ccc_f068_cash_conversion_cycle_ccc_mean_126d_base_v018_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ccc scaled by closeadj
def f068ccc_f068_cash_conversion_cycle_ccc_mean_252d_base_v019_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ccc scaled by closeadj
def f068ccc_f068_cash_conversion_cycle_ccc_mean_504d_base_v020_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ccc_chg_y scaled by closeadj
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_mean_21d_base_v021_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ccc_chg_y scaled by closeadj
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_mean_63d_base_v022_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ccc_chg_y scaled by closeadj
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_mean_126d_base_v023_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ccc_chg_y scaled by closeadj
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_mean_252d_base_v024_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ccc_chg_y scaled by closeadj
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_mean_504d_base_v025_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of dso_yoy scaled by closeadj
def f068ccc_f068_cash_conversion_cycle_dso_yoy_mean_21d_base_v026_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of dso_yoy scaled by closeadj
def f068ccc_f068_cash_conversion_cycle_dso_yoy_mean_63d_base_v027_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of dso_yoy scaled by closeadj
def f068ccc_f068_cash_conversion_cycle_dso_yoy_mean_126d_base_v028_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of dso_yoy scaled by closeadj
def f068ccc_f068_cash_conversion_cycle_dso_yoy_mean_252d_base_v029_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of dso_yoy scaled by closeadj
def f068ccc_f068_cash_conversion_cycle_dso_yoy_mean_504d_base_v030_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of dio_yoy scaled by closeadj
def f068ccc_f068_cash_conversion_cycle_dio_yoy_mean_21d_base_v031_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of dio_yoy scaled by closeadj
def f068ccc_f068_cash_conversion_cycle_dio_yoy_mean_63d_base_v032_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of dio_yoy scaled by closeadj
def f068ccc_f068_cash_conversion_cycle_dio_yoy_mean_126d_base_v033_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of dio_yoy scaled by closeadj
def f068ccc_f068_cash_conversion_cycle_dio_yoy_mean_252d_base_v034_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of dio_yoy scaled by closeadj
def f068ccc_f068_cash_conversion_cycle_dio_yoy_mean_504d_base_v035_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of dso
def f068ccc_f068_cash_conversion_cycle_dso_median_63d_base_v036_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of dso
def f068ccc_f068_cash_conversion_cycle_dso_median_252d_base_v037_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of dso
def f068ccc_f068_cash_conversion_cycle_dso_median_504d_base_v038_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of dio
def f068ccc_f068_cash_conversion_cycle_dio_median_63d_base_v039_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of dio
def f068ccc_f068_cash_conversion_cycle_dio_median_252d_base_v040_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of dio
def f068ccc_f068_cash_conversion_cycle_dio_median_504d_base_v041_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_median_63d_base_v042_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_median_252d_base_v043_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_median_504d_base_v044_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_median_63d_base_v045_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_median_252d_base_v046_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_median_504d_base_v047_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_median_63d_base_v048_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_median_252d_base_v049_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_median_504d_base_v050_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_median_63d_base_v051_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_median_252d_base_v052_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_median_504d_base_v053_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_median_63d_base_v054_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_median_252d_base_v055_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_median_504d_base_v056_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of dso
def f068ccc_f068_cash_conversion_cycle_dso_rmax_252d_base_v057_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of dso
def f068ccc_f068_cash_conversion_cycle_dso_rmax_504d_base_v058_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of dio
def f068ccc_f068_cash_conversion_cycle_dio_rmax_252d_base_v059_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of dio
def f068ccc_f068_cash_conversion_cycle_dio_rmax_504d_base_v060_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_rmax_252d_base_v061_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_rmax_504d_base_v062_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_rmax_252d_base_v063_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_rmax_504d_base_v064_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_rmax_252d_base_v065_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_rmax_504d_base_v066_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_rmax_252d_base_v067_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_rmax_504d_base_v068_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_rmax_252d_base_v069_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_rmax_504d_base_v070_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of dso
def f068ccc_f068_cash_conversion_cycle_dso_rmin_252d_base_v071_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of dso
def f068ccc_f068_cash_conversion_cycle_dso_rmin_504d_base_v072_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of dio
def f068ccc_f068_cash_conversion_cycle_dio_rmin_252d_base_v073_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of dio
def f068ccc_f068_cash_conversion_cycle_dio_rmin_504d_base_v074_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_rmin_252d_base_v075_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

