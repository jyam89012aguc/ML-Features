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


# 63d z-score of dso
def f068ccc_f068_cash_conversion_cycle_dso_z_63d_base_v076_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of dso
def f068ccc_f068_cash_conversion_cycle_dso_z_126d_base_v077_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of dso
def f068ccc_f068_cash_conversion_cycle_dso_z_252d_base_v078_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of dso
def f068ccc_f068_cash_conversion_cycle_dso_z_504d_base_v079_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of dio
def f068ccc_f068_cash_conversion_cycle_dio_z_63d_base_v080_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of dio
def f068ccc_f068_cash_conversion_cycle_dio_z_126d_base_v081_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of dio
def f068ccc_f068_cash_conversion_cycle_dio_z_252d_base_v082_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of dio
def f068ccc_f068_cash_conversion_cycle_dio_z_504d_base_v083_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_z_63d_base_v084_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_z_126d_base_v085_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_z_252d_base_v086_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_z_504d_base_v087_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_z_63d_base_v088_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_z_126d_base_v089_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_z_252d_base_v090_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_z_504d_base_v091_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_z_63d_base_v092_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_z_126d_base_v093_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_z_252d_base_v094_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_z_504d_base_v095_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_z_63d_base_v096_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_z_126d_base_v097_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_z_252d_base_v098_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_z_504d_base_v099_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_z_63d_base_v100_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_z_126d_base_v101_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_z_252d_base_v102_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_z_504d_base_v103_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of dso
def f068ccc_f068_cash_conversion_cycle_dso_distmax_252d_base_v104_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of dso
def f068ccc_f068_cash_conversion_cycle_dso_distmax_504d_base_v105_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of dio
def f068ccc_f068_cash_conversion_cycle_dio_distmax_252d_base_v106_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of dio
def f068ccc_f068_cash_conversion_cycle_dio_distmax_504d_base_v107_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_distmax_252d_base_v108_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_distmax_504d_base_v109_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_distmax_252d_base_v110_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_distmax_504d_base_v111_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_distmax_252d_base_v112_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_distmax_504d_base_v113_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_distmax_252d_base_v114_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_distmax_504d_base_v115_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_distmax_252d_base_v116_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_distmax_504d_base_v117_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of dso
def f068ccc_f068_cash_conversion_cycle_dso_distmed_126d_base_v118_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of dso
def f068ccc_f068_cash_conversion_cycle_dso_distmed_252d_base_v119_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of dso
def f068ccc_f068_cash_conversion_cycle_dso_distmed_504d_base_v120_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of dio
def f068ccc_f068_cash_conversion_cycle_dio_distmed_126d_base_v121_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of dio
def f068ccc_f068_cash_conversion_cycle_dio_distmed_252d_base_v122_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of dio
def f068ccc_f068_cash_conversion_cycle_dio_distmed_504d_base_v123_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_distmed_126d_base_v124_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_distmed_252d_base_v125_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of dpo
def f068ccc_f068_cash_conversion_cycle_dpo_distmed_504d_base_v126_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_distmed_126d_base_v127_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_distmed_252d_base_v128_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ccc
def f068ccc_f068_cash_conversion_cycle_ccc_distmed_504d_base_v129_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_distmed_126d_base_v130_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_distmed_252d_base_v131_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_distmed_504d_base_v132_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_distmed_126d_base_v133_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_distmed_252d_base_v134_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_distmed_504d_base_v135_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_distmed_126d_base_v136_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_distmed_252d_base_v137_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of dio_yoy
def f068ccc_f068_cash_conversion_cycle_dio_yoy_distmed_504d_base_v138_signal(inventory, cor, closeadj):
    base = (365 * inventory / cor.abs().replace(0, np.nan)).diff(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in dso
def f068ccc_f068_cash_conversion_cycle_dso_chg_63d_base_v139_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in dso
def f068ccc_f068_cash_conversion_cycle_dso_chg_252d_base_v140_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in dio
def f068ccc_f068_cash_conversion_cycle_dio_chg_63d_base_v141_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in dio
def f068ccc_f068_cash_conversion_cycle_dio_chg_252d_base_v142_signal(inventory, cor, closeadj):
    base = 365 * inventory / cor.abs().replace(0, np.nan)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in dpo
def f068ccc_f068_cash_conversion_cycle_dpo_chg_63d_base_v143_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in dpo
def f068ccc_f068_cash_conversion_cycle_dpo_chg_252d_base_v144_signal(payables, opex, closeadj):
    base = 365 * payables / opex.abs().replace(0, np.nan)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in ccc
def f068ccc_f068_cash_conversion_cycle_ccc_chg_63d_base_v145_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in ccc
def f068ccc_f068_cash_conversion_cycle_ccc_chg_252d_base_v146_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = _f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_chg_63d_base_v147_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in ccc_chg_y
def f068ccc_f068_cash_conversion_cycle_ccc_chg_y_chg_252d_base_v148_signal(receivables, revenue, inventory, cor, payables, opex, closeadj):
    base = (_f068_dso(receivables, revenue) + 365*inventory/cor.abs().replace(0, np.nan) - 365*payables/opex.abs().replace(0, np.nan)).diff(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_chg_63d_base_v149_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in dso_yoy
def f068ccc_f068_cash_conversion_cycle_dso_yoy_chg_252d_base_v150_signal(receivables, revenue, closeadj):
    base = _f068_dso(receivables, revenue).diff(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

