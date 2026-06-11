import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_FIVEYEAR = 1260
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _netdebt(debt, cashneq):
    return debt - cashneq


def _logchg(s, w):
    return np.log(s.replace(0, np.nan)) - np.log(s.shift(w).replace(0, np.nan))


def _debt_ebitda(debt, ebitda):
    return debt / ebitda.replace(0, np.nan)


def _shortmix(debtc, debt):
    return debtc / debt.replace(0, np.nan)


def _longmix(debtnc, debt):
    return debtnc / debt.replace(0, np.nan)


def _paydown_flow(ncfdebt, debt):
    return ncfdebt / debt.replace(0, np.nan)


# ============================================================
def f34dt_f34_debt_leverage_trajectory_debtgrow_63d_jerk_v001_signal(debt):
    base = _logchg(debt, 63)
    d = base - 2.0 * base.shift(42) + base.shift(84)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtgrow_63d_jerk_v002_signal(debt):
    base = _logchg(debt, 63)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtgrow_63d_jerk_v003_signal(debt):
    base = _logchg(debt, 63)
    d = base - 2.0 * base.shift(84) + base.shift(168)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtgrow_63d_jerk_v004_signal(debt):
    base = _logchg(debt, 63)
    d = base - 2.0 * base.shift(126) + base.shift(252)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtgrow_126d_jerk_v005_signal(debt):
    base = _logchg(debt, 126)
    d = base - 2.0 * base.shift(42) + base.shift(84)
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtgrow_126d_jerk_v006_signal(debt):
    base = _logchg(debt, 126)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtgrow_126d_jerk_v007_signal(debt):
    base = _logchg(debt, 126)
    d = base - 2.0 * base.shift(84) + base.shift(168)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtgrow_126d_jerk_v008_signal(debt):
    base = _logchg(debt, 126)
    d = base - 2.0 * base.shift(126) + base.shift(252)
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtgrow_252d_jerk_v009_signal(debt):
    base = _logchg(debt, 252)
    d = base - 2.0 * base.shift(42) + base.shift(84)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtgrow_252d_jerk_v010_signal(debt):
    base = _logchg(debt, 252)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtgrow_252d_jerk_v011_signal(debt):
    base = _logchg(debt, 252)
    d = base - 2.0 * base.shift(84) + base.shift(168)
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtgrow_252d_jerk_v012_signal(debt):
    base = _logchg(debt, 252)
    d = base - 2.0 * base.shift(126) + base.shift(252)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtebitda_42d_jerk_v013_signal(debt, ebitda):
    base = _debt_ebitda(debt, ebitda)
    d = base - 2.0 * base.shift(42) + base.shift(84)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtebitda_63d_jerk_v014_signal(debt, ebitda):
    base = _debt_ebitda(debt, ebitda)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtebitda_84d_jerk_v015_signal(debt, ebitda):
    base = _debt_ebitda(debt, ebitda)
    d = base - 2.0 * base.shift(84) + base.shift(168)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtebitda_126d_jerk_v016_signal(debt, ebitda):
    base = _debt_ebitda(debt, ebitda)
    d = base - 2.0 * base.shift(126) + base.shift(252)
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_netdebt_42d_jerk_v017_signal(debt, cashneq):
    base = _netdebt(debt, cashneq) / debt.replace(0, np.nan)
    d = base - 2.0 * base.shift(42) + base.shift(84)
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_netdebt_63d_jerk_v018_signal(debt, cashneq):
    base = _netdebt(debt, cashneq) / debt.replace(0, np.nan)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_netdebt_84d_jerk_v019_signal(debt, cashneq):
    base = _netdebt(debt, cashneq) / debt.replace(0, np.nan)
    d = base - 2.0 * base.shift(84) + base.shift(168)
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_netdebt_126d_jerk_v020_signal(debt, cashneq):
    base = _netdebt(debt, cashneq) / debt.replace(0, np.nan)
    d = base - 2.0 * base.shift(126) + base.shift(252)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_netlev_42d_jerk_v021_signal(debt, cashneq, ebitda):
    base = _netdebt(debt, cashneq) / ebitda.replace(0, np.nan)
    d = base - 2.0 * base.shift(42) + base.shift(84)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_netlev_63d_jerk_v022_signal(debt, cashneq, ebitda):
    base = _netdebt(debt, cashneq) / ebitda.replace(0, np.nan)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_netlev_84d_jerk_v023_signal(debt, cashneq, ebitda):
    base = _netdebt(debt, cashneq) / ebitda.replace(0, np.nan)
    d = base - 2.0 * base.shift(84) + base.shift(168)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_netlev_126d_jerk_v024_signal(debt, cashneq, ebitda):
    base = _netdebt(debt, cashneq) / ebitda.replace(0, np.nan)
    d = base - 2.0 * base.shift(126) + base.shift(252)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shortmix_42d_jerk_v025_signal(debtc, debt):
    base = _shortmix(debtc, debt)
    d = base - 2.0 * base.shift(42) + base.shift(84)
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shortmix_63d_jerk_v026_signal(debtc, debt):
    base = _shortmix(debtc, debt)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shortmix_84d_jerk_v027_signal(debtc, debt):
    base = _shortmix(debtc, debt)
    d = base - 2.0 * base.shift(84) + base.shift(168)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shortmix_126d_jerk_v028_signal(debtc, debt):
    base = _shortmix(debtc, debt)
    d = base - 2.0 * base.shift(126) + base.shift(252)
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_longmix_42d_jerk_v029_signal(debtnc, debt):
    base = _longmix(debtnc, debt)
    d = base - 2.0 * base.shift(42) + base.shift(84)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_longmix_63d_jerk_v030_signal(debtnc, debt):
    base = _longmix(debtnc, debt)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_longmix_84d_jerk_v031_signal(debtnc, debt):
    base = _longmix(debtnc, debt)
    d = base - 2.0 * base.shift(84) + base.shift(168)
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_longmix_126d_jerk_v032_signal(debtnc, debt):
    base = _longmix(debtnc, debt)
    d = base - 2.0 * base.shift(126) + base.shift(252)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_termskew_42d_jerk_v033_signal(debtnc, debtc, debt):
    base = (debtnc - debtc) / debt.replace(0, np.nan)
    d = base - 2.0 * base.shift(42) + base.shift(84)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_termskew_63d_jerk_v034_signal(debtnc, debtc, debt):
    base = (debtnc - debtc) / debt.replace(0, np.nan)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_termskew_84d_jerk_v035_signal(debtnc, debtc, debt):
    base = (debtnc - debtc) / debt.replace(0, np.nan)
    d = base - 2.0 * base.shift(84) + base.shift(168)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_termskew_126d_jerk_v036_signal(debtnc, debtc, debt):
    base = (debtnc - debtc) / debt.replace(0, np.nan)
    d = base - 2.0 * base.shift(126) + base.shift(252)
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_paydownflow_42d_jerk_v037_signal(ncfdebt, debt):
    base = _paydown_flow(ncfdebt, debt)
    d = base - 2.0 * base.shift(42) + base.shift(84)
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_paydownflow_63d_jerk_v038_signal(ncfdebt, debt):
    base = _paydown_flow(ncfdebt, debt)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_paydownflow_84d_jerk_v039_signal(ncfdebt, debt):
    base = _paydown_flow(ncfdebt, debt)
    d = base - 2.0 * base.shift(84) + base.shift(168)
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_paydownflow_126d_jerk_v040_signal(ncfdebt, debt):
    base = _paydown_flow(ncfdebt, debt)
    d = base - 2.0 * base.shift(126) + base.shift(252)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_cashcover_42d_jerk_v041_signal(cashneq, debt):
    base = cashneq / debt.replace(0, np.nan)
    d = base - 2.0 * base.shift(42) + base.shift(84)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_cashcover_63d_jerk_v042_signal(cashneq, debt):
    base = cashneq / debt.replace(0, np.nan)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_cashcover_84d_jerk_v043_signal(cashneq, debt):
    base = cashneq / debt.replace(0, np.nan)
    d = base - 2.0 * base.shift(84) + base.shift(168)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_cashcover_126d_jerk_v044_signal(cashneq, debt):
    base = cashneq / debt.replace(0, np.nan)
    d = base - 2.0 * base.shift(126) + base.shift(252)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shortcover_42d_jerk_v045_signal(ebitda, debtc):
    base = ebitda / debtc.replace(0, np.nan)
    d = base - 2.0 * base.shift(42) + base.shift(84)
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shortcover_63d_jerk_v046_signal(ebitda, debtc):
    base = ebitda / debtc.replace(0, np.nan)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shortcover_84d_jerk_v047_signal(ebitda, debtc):
    base = ebitda / debtc.replace(0, np.nan)
    d = base - 2.0 * base.shift(84) + base.shift(168)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shortcover_126d_jerk_v048_signal(ebitda, debtc):
    base = ebitda / debtc.replace(0, np.nan)
    d = base - 2.0 * base.shift(126) + base.shift(252)
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_service_42d_jerk_v049_signal(ebitda, debt):
    base = ebitda / debt.replace(0, np.nan)
    d = base - 2.0 * base.shift(42) + base.shift(84)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_service_63d_jerk_v050_signal(ebitda, debt):
    base = ebitda / debt.replace(0, np.nan)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_service_84d_jerk_v051_signal(ebitda, debt):
    base = ebitda / debt.replace(0, np.nan)
    d = base - 2.0 * base.shift(84) + base.shift(168)
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_service_126d_jerk_v052_signal(ebitda, debt):
    base = ebitda / debt.replace(0, np.nan)
    d = base - 2.0 * base.shift(126) + base.shift(252)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shorttocash_42d_jerk_v053_signal(debtc, cashneq):
    base = debtc / cashneq.replace(0, np.nan)
    d = base - 2.0 * base.shift(42) + base.shift(84)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shorttocash_63d_jerk_v054_signal(debtc, cashneq):
    base = debtc / cashneq.replace(0, np.nan)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shorttocash_84d_jerk_v055_signal(debtc, cashneq):
    base = debtc / cashneq.replace(0, np.nan)
    d = base - 2.0 * base.shift(84) + base.shift(168)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shorttocash_126d_jerk_v056_signal(debtc, cashneq):
    base = debtc / cashneq.replace(0, np.nan)
    d = base - 2.0 * base.shift(126) + base.shift(252)
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtext_63d_jerk_v057_signal(debt):
    base = debt / _mean(debt, 63).replace(0, np.nan) - 1.0
    d = base - 2.0 * base.shift(42) + base.shift(84)
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtext_63d_jerk_v058_signal(debt):
    base = debt / _mean(debt, 63).replace(0, np.nan) - 1.0
    d = base - 2.0 * base.shift(63) + base.shift(126)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtext_63d_jerk_v059_signal(debt):
    base = debt / _mean(debt, 63).replace(0, np.nan) - 1.0
    d = base - 2.0 * base.shift(84) + base.shift(168)
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtext_63d_jerk_v060_signal(debt):
    base = debt / _mean(debt, 63).replace(0, np.nan) - 1.0
    d = base - 2.0 * base.shift(126) + base.shift(252)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtext_126d_jerk_v061_signal(debt):
    base = debt / _mean(debt, 126).replace(0, np.nan) - 1.0
    d = base - 2.0 * base.shift(42) + base.shift(84)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtext_126d_jerk_v062_signal(debt):
    base = debt / _mean(debt, 126).replace(0, np.nan) - 1.0
    d = base - 2.0 * base.shift(63) + base.shift(126)
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtext_126d_jerk_v063_signal(debt):
    base = debt / _mean(debt, 126).replace(0, np.nan) - 1.0
    d = base - 2.0 * base.shift(126) + base.shift(252)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtext_252d_jerk_v064_signal(debt):
    base = debt / _mean(debt, 252).replace(0, np.nan) - 1.0
    d = base - 2.0 * base.shift(42) + base.shift(84)
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtext_252d_jerk_v065_signal(debt):
    base = debt / _mean(debt, 252).replace(0, np.nan) - 1.0
    d = base - 2.0 * base.shift(63) + base.shift(126)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtext_252d_jerk_v066_signal(debt):
    base = debt / _mean(debt, 252).replace(0, np.nan) - 1.0
    d = base - 2.0 * base.shift(84) + base.shift(168)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtext_252d_jerk_v067_signal(debt):
    base = debt / _mean(debt, 252).replace(0, np.nan) - 1.0
    d = base - 2.0 * base.shift(126) + base.shift(252)
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levz_63d_jerk_v068_signal(debt, ebitda):
    base = _z(_debt_ebitda(debt, ebitda), 63)
    d = base - 2.0 * base.shift(42) + base.shift(84)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levz_63d_jerk_v069_signal(debt, ebitda):
    base = _z(_debt_ebitda(debt, ebitda), 63)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levz_63d_jerk_v070_signal(debt, ebitda):
    base = _z(_debt_ebitda(debt, ebitda), 63)
    d = base - 2.0 * base.shift(84) + base.shift(168)
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levz_63d_jerk_v071_signal(debt, ebitda):
    base = _z(_debt_ebitda(debt, ebitda), 63)
    d = base - 2.0 * base.shift(126) + base.shift(252)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levz_126d_jerk_v072_signal(debt, ebitda):
    base = _z(_debt_ebitda(debt, ebitda), 126)
    d = base - 2.0 * base.shift(42) + base.shift(84)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levz_126d_jerk_v073_signal(debt, ebitda):
    base = _z(_debt_ebitda(debt, ebitda), 126)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levz_126d_jerk_v074_signal(debt, ebitda):
    base = _z(_debt_ebitda(debt, ebitda), 126)
    d = base - 2.0 * base.shift(84) + base.shift(168)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levz_126d_jerk_v075_signal(debt, ebitda):
    base = _z(_debt_ebitda(debt, ebitda), 126)
    d = base - 2.0 * base.shift(126) + base.shift(252)
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levz_252d_jerk_v076_signal(debt, ebitda):
    base = _z(_debt_ebitda(debt, ebitda), 252)
    d = base - 2.0 * base.shift(42) + base.shift(84)
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levz_252d_jerk_v077_signal(debt, ebitda):
    base = _z(_debt_ebitda(debt, ebitda), 252)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levz_252d_jerk_v078_signal(debt, ebitda):
    base = _z(_debt_ebitda(debt, ebitda), 252)
    d = base - 2.0 * base.shift(84) + base.shift(168)
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levz_252d_jerk_v079_signal(debt, ebitda):
    base = _z(_debt_ebitda(debt, ebitda), 252)
    d = base - 2.0 * base.shift(126) + base.shift(252)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shortgrow_63d_jerk_v080_signal(debtc):
    base = _logchg(debtc, 63)
    d = base - 2.0 * base.shift(42) + base.shift(84)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shortgrow_63d_jerk_v081_signal(debtc):
    base = _logchg(debtc, 63)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shortgrow_63d_jerk_v082_signal(debtc):
    base = _logchg(debtc, 63)
    d = base - 2.0 * base.shift(84) + base.shift(168)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shortgrow_63d_jerk_v083_signal(debtc):
    base = _logchg(debtc, 63)
    d = base - 2.0 * base.shift(126) + base.shift(252)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shortgrow_126d_jerk_v084_signal(debtc):
    base = _logchg(debtc, 126)
    d = base - 2.0 * base.shift(42) + base.shift(84)
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shortgrow_126d_jerk_v085_signal(debtc):
    base = _logchg(debtc, 126)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shortgrow_126d_jerk_v086_signal(debtc):
    base = _logchg(debtc, 126)
    d = base - 2.0 * base.shift(84) + base.shift(168)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shortgrow_126d_jerk_v087_signal(debtc):
    base = _logchg(debtc, 126)
    d = base - 2.0 * base.shift(126) + base.shift(252)
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shortgrow_252d_jerk_v088_signal(debtc):
    base = _logchg(debtc, 252)
    d = base - 2.0 * base.shift(42) + base.shift(84)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shortgrow_252d_jerk_v089_signal(debtc):
    base = _logchg(debtc, 252)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shortgrow_252d_jerk_v090_signal(debtc):
    base = _logchg(debtc, 252)
    d = base - 2.0 * base.shift(84) + base.shift(168)
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shortgrow_252d_jerk_v091_signal(debtc):
    base = _logchg(debtc, 252)
    d = base - 2.0 * base.shift(126) + base.shift(252)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_longgrow_63d_jerk_v092_signal(debtnc):
    base = _logchg(debtnc, 63)
    d = base - 2.0 * base.shift(42) + base.shift(84)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_longgrow_63d_jerk_v093_signal(debtnc):
    base = _logchg(debtnc, 63)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_longgrow_63d_jerk_v094_signal(debtnc):
    base = _logchg(debtnc, 63)
    d = base - 2.0 * base.shift(84) + base.shift(168)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_longgrow_63d_jerk_v095_signal(debtnc):
    base = _logchg(debtnc, 63)
    d = base - 2.0 * base.shift(126) + base.shift(252)
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_longgrow_126d_jerk_v096_signal(debtnc):
    base = _logchg(debtnc, 126)
    d = base - 2.0 * base.shift(42) + base.shift(84)
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_longgrow_126d_jerk_v097_signal(debtnc):
    base = _logchg(debtnc, 126)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_longgrow_126d_jerk_v098_signal(debtnc):
    base = _logchg(debtnc, 126)
    d = base - 2.0 * base.shift(84) + base.shift(168)
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_longgrow_126d_jerk_v099_signal(debtnc):
    base = _logchg(debtnc, 126)
    d = base - 2.0 * base.shift(126) + base.shift(252)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_longgrow_252d_jerk_v100_signal(debtnc):
    base = _logchg(debtnc, 252)
    d = base - 2.0 * base.shift(42) + base.shift(84)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_longgrow_252d_jerk_v101_signal(debtnc):
    base = _logchg(debtnc, 252)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_longgrow_252d_jerk_v102_signal(debtnc):
    base = _logchg(debtnc, 252)
    d = base - 2.0 * base.shift(84) + base.shift(168)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_longgrow_252d_jerk_v103_signal(debtnc):
    base = _logchg(debtnc, 252)
    d = base - 2.0 * base.shift(126) + base.shift(252)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_ebitdagrow_63d_jerk_v104_signal(ebitda):
    base = _logchg(ebitda.abs(), 63)
    d = base - 2.0 * base.shift(42) + base.shift(84)
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_ebitdagrow_63d_jerk_v105_signal(ebitda):
    base = _logchg(ebitda.abs(), 63)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_ebitdagrow_63d_jerk_v106_signal(ebitda):
    base = _logchg(ebitda.abs(), 63)
    d = base - 2.0 * base.shift(84) + base.shift(168)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_ebitdagrow_63d_jerk_v107_signal(ebitda):
    base = _logchg(ebitda.abs(), 63)
    d = base - 2.0 * base.shift(126) + base.shift(252)
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_ebitdagrow_126d_jerk_v108_signal(ebitda):
    base = _logchg(ebitda.abs(), 126)
    d = base - 2.0 * base.shift(42) + base.shift(84)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_ebitdagrow_126d_jerk_v109_signal(ebitda):
    base = _logchg(ebitda.abs(), 126)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_ebitdagrow_126d_jerk_v110_signal(ebitda):
    base = _logchg(ebitda.abs(), 126)
    d = base - 2.0 * base.shift(84) + base.shift(168)
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_ebitdagrow_126d_jerk_v111_signal(ebitda):
    base = _logchg(ebitda.abs(), 126)
    d = base - 2.0 * base.shift(126) + base.shift(252)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_ebitdagrow_252d_jerk_v112_signal(ebitda):
    base = _logchg(ebitda.abs(), 252)
    d = base - 2.0 * base.shift(42) + base.shift(84)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_ebitdagrow_252d_jerk_v113_signal(ebitda):
    base = _logchg(ebitda.abs(), 252)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_ebitdagrow_252d_jerk_v114_signal(ebitda):
    base = _logchg(ebitda.abs(), 252)
    d = base - 2.0 * base.shift(84) + base.shift(168)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_ebitdagrow_252d_jerk_v115_signal(ebitda):
    base = _logchg(ebitda.abs(), 252)
    d = base - 2.0 * base.shift(126) + base.shift(252)
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_cashgrow_63d_jerk_v116_signal(cashneq):
    base = _logchg(cashneq, 63)
    d = base - 2.0 * base.shift(42) + base.shift(84)
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_cashgrow_63d_jerk_v117_signal(cashneq):
    base = _logchg(cashneq, 63)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_cashgrow_63d_jerk_v118_signal(cashneq):
    base = _logchg(cashneq, 63)
    d = base - 2.0 * base.shift(84) + base.shift(168)
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_cashgrow_63d_jerk_v119_signal(cashneq):
    base = _logchg(cashneq, 63)
    d = base - 2.0 * base.shift(126) + base.shift(252)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_cashgrow_126d_jerk_v120_signal(cashneq):
    base = _logchg(cashneq, 126)
    d = base - 2.0 * base.shift(42) + base.shift(84)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_cashgrow_126d_jerk_v121_signal(cashneq):
    base = _logchg(cashneq, 126)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_cashgrow_126d_jerk_v122_signal(cashneq):
    base = _logchg(cashneq, 126)
    d = base - 2.0 * base.shift(84) + base.shift(168)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_cashgrow_126d_jerk_v123_signal(cashneq):
    base = _logchg(cashneq, 126)
    d = base - 2.0 * base.shift(126) + base.shift(252)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_cashgrow_252d_jerk_v124_signal(cashneq):
    base = _logchg(cashneq, 252)
    d = base - 2.0 * base.shift(42) + base.shift(84)
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_cashgrow_252d_jerk_v125_signal(cashneq):
    base = _logchg(cashneq, 252)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_cashgrow_252d_jerk_v126_signal(cashneq):
    base = _logchg(cashneq, 252)
    d = base - 2.0 * base.shift(84) + base.shift(168)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_cashgrow_252d_jerk_v127_signal(cashneq):
    base = _logchg(cashneq, 252)
    d = base - 2.0 * base.shift(126) + base.shift(252)
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levrank_63d_jerk_v128_signal(debt, ebitda):
    base = _rank(_debt_ebitda(debt, ebitda), 63)
    d = base - 2.0 * base.shift(42) + base.shift(84)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levrank_63d_jerk_v129_signal(debt, ebitda):
    base = _rank(_debt_ebitda(debt, ebitda), 63)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levrank_63d_jerk_v130_signal(debt, ebitda):
    base = _rank(_debt_ebitda(debt, ebitda), 63)
    d = base - 2.0 * base.shift(84) + base.shift(168)
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levrank_63d_jerk_v131_signal(debt, ebitda):
    base = _rank(_debt_ebitda(debt, ebitda), 63)
    d = base - 2.0 * base.shift(126) + base.shift(252)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levrank_126d_jerk_v132_signal(debt, ebitda):
    base = _rank(_debt_ebitda(debt, ebitda), 126)
    d = base - 2.0 * base.shift(42) + base.shift(84)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levrank_126d_jerk_v133_signal(debt, ebitda):
    base = _rank(_debt_ebitda(debt, ebitda), 126)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levrank_126d_jerk_v134_signal(debt, ebitda):
    base = _rank(_debt_ebitda(debt, ebitda), 126)
    d = base - 2.0 * base.shift(84) + base.shift(168)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levrank_126d_jerk_v135_signal(debt, ebitda):
    base = _rank(_debt_ebitda(debt, ebitda), 126)
    d = base - 2.0 * base.shift(126) + base.shift(252)
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levrank_252d_jerk_v136_signal(debt, ebitda):
    base = _rank(_debt_ebitda(debt, ebitda), 252)
    d = base - 2.0 * base.shift(42) + base.shift(84)
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levrank_252d_jerk_v137_signal(debt, ebitda):
    base = _rank(_debt_ebitda(debt, ebitda), 252)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levrank_252d_jerk_v138_signal(debt, ebitda):
    base = _rank(_debt_ebitda(debt, ebitda), 252)
    d = base - 2.0 * base.shift(84) + base.shift(168)
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levrank_252d_jerk_v139_signal(debt, ebitda):
    base = _rank(_debt_ebitda(debt, ebitda), 252)
    d = base - 2.0 * base.shift(126) + base.shift(252)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_flowintensity_63d_jerk_v140_signal(ncfdebt, debt):
    base = ncfdebt.rolling(63, min_periods=max(1, 63 // 2)).sum() / debt.replace(0, np.nan)
    d = base - 2.0 * base.shift(42) + base.shift(84)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_flowintensity_63d_jerk_v141_signal(ncfdebt, debt):
    base = ncfdebt.rolling(63, min_periods=max(1, 63 // 2)).sum() / debt.replace(0, np.nan)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_flowintensity_63d_jerk_v142_signal(ncfdebt, debt):
    base = ncfdebt.rolling(63, min_periods=max(1, 63 // 2)).sum() / debt.replace(0, np.nan)
    d = base - 2.0 * base.shift(84) + base.shift(168)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_flowintensity_63d_jerk_v143_signal(ncfdebt, debt):
    base = ncfdebt.rolling(63, min_periods=max(1, 63 // 2)).sum() / debt.replace(0, np.nan)
    d = base - 2.0 * base.shift(126) + base.shift(252)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_flowintensity_126d_jerk_v144_signal(ncfdebt, debt):
    base = ncfdebt.rolling(126, min_periods=max(1, 126 // 2)).sum() / debt.replace(0, np.nan)
    d = base - 2.0 * base.shift(42) + base.shift(84)
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_flowintensity_126d_jerk_v145_signal(ncfdebt, debt):
    base = ncfdebt.rolling(126, min_periods=max(1, 126 // 2)).sum() / debt.replace(0, np.nan)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_flowintensity_126d_jerk_v146_signal(ncfdebt, debt):
    base = ncfdebt.rolling(126, min_periods=max(1, 126 // 2)).sum() / debt.replace(0, np.nan)
    d = base - 2.0 * base.shift(84) + base.shift(168)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_flowintensity_126d_jerk_v147_signal(ncfdebt, debt):
    base = ncfdebt.rolling(126, min_periods=max(1, 126 // 2)).sum() / debt.replace(0, np.nan)
    d = base - 2.0 * base.shift(126) + base.shift(252)
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_flowintensity_252d_jerk_v148_signal(ncfdebt, debt):
    base = ncfdebt.rolling(252, min_periods=max(1, 252 // 2)).sum() / debt.replace(0, np.nan)
    d = base - 2.0 * base.shift(42) + base.shift(84)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_flowintensity_252d_jerk_v149_signal(ncfdebt, debt):
    base = ncfdebt.rolling(252, min_periods=max(1, 252 // 2)).sum() / debt.replace(0, np.nan)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_flowintensity_252d_jerk_v150_signal(ncfdebt, debt):
    base = ncfdebt.rolling(252, min_periods=max(1, 252 // 2)).sum() / debt.replace(0, np.nan)
    d = base - 2.0 * base.shift(84) + base.shift(168)
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f34dt_f34_debt_leverage_trajectory_debtgrow_63d_jerk_v001_signal,
    f34dt_f34_debt_leverage_trajectory_debtgrow_63d_jerk_v002_signal,
    f34dt_f34_debt_leverage_trajectory_debtgrow_63d_jerk_v003_signal,
    f34dt_f34_debt_leverage_trajectory_debtgrow_63d_jerk_v004_signal,
    f34dt_f34_debt_leverage_trajectory_debtgrow_126d_jerk_v005_signal,
    f34dt_f34_debt_leverage_trajectory_debtgrow_126d_jerk_v006_signal,
    f34dt_f34_debt_leverage_trajectory_debtgrow_126d_jerk_v007_signal,
    f34dt_f34_debt_leverage_trajectory_debtgrow_126d_jerk_v008_signal,
    f34dt_f34_debt_leverage_trajectory_debtgrow_252d_jerk_v009_signal,
    f34dt_f34_debt_leverage_trajectory_debtgrow_252d_jerk_v010_signal,
    f34dt_f34_debt_leverage_trajectory_debtgrow_252d_jerk_v011_signal,
    f34dt_f34_debt_leverage_trajectory_debtgrow_252d_jerk_v012_signal,
    f34dt_f34_debt_leverage_trajectory_debtebitda_42d_jerk_v013_signal,
    f34dt_f34_debt_leverage_trajectory_debtebitda_63d_jerk_v014_signal,
    f34dt_f34_debt_leverage_trajectory_debtebitda_84d_jerk_v015_signal,
    f34dt_f34_debt_leverage_trajectory_debtebitda_126d_jerk_v016_signal,
    f34dt_f34_debt_leverage_trajectory_netdebt_42d_jerk_v017_signal,
    f34dt_f34_debt_leverage_trajectory_netdebt_63d_jerk_v018_signal,
    f34dt_f34_debt_leverage_trajectory_netdebt_84d_jerk_v019_signal,
    f34dt_f34_debt_leverage_trajectory_netdebt_126d_jerk_v020_signal,
    f34dt_f34_debt_leverage_trajectory_netlev_42d_jerk_v021_signal,
    f34dt_f34_debt_leverage_trajectory_netlev_63d_jerk_v022_signal,
    f34dt_f34_debt_leverage_trajectory_netlev_84d_jerk_v023_signal,
    f34dt_f34_debt_leverage_trajectory_netlev_126d_jerk_v024_signal,
    f34dt_f34_debt_leverage_trajectory_shortmix_42d_jerk_v025_signal,
    f34dt_f34_debt_leverage_trajectory_shortmix_63d_jerk_v026_signal,
    f34dt_f34_debt_leverage_trajectory_shortmix_84d_jerk_v027_signal,
    f34dt_f34_debt_leverage_trajectory_shortmix_126d_jerk_v028_signal,
    f34dt_f34_debt_leverage_trajectory_longmix_42d_jerk_v029_signal,
    f34dt_f34_debt_leverage_trajectory_longmix_63d_jerk_v030_signal,
    f34dt_f34_debt_leverage_trajectory_longmix_84d_jerk_v031_signal,
    f34dt_f34_debt_leverage_trajectory_longmix_126d_jerk_v032_signal,
    f34dt_f34_debt_leverage_trajectory_termskew_42d_jerk_v033_signal,
    f34dt_f34_debt_leverage_trajectory_termskew_63d_jerk_v034_signal,
    f34dt_f34_debt_leverage_trajectory_termskew_84d_jerk_v035_signal,
    f34dt_f34_debt_leverage_trajectory_termskew_126d_jerk_v036_signal,
    f34dt_f34_debt_leverage_trajectory_paydownflow_42d_jerk_v037_signal,
    f34dt_f34_debt_leverage_trajectory_paydownflow_63d_jerk_v038_signal,
    f34dt_f34_debt_leverage_trajectory_paydownflow_84d_jerk_v039_signal,
    f34dt_f34_debt_leverage_trajectory_paydownflow_126d_jerk_v040_signal,
    f34dt_f34_debt_leverage_trajectory_cashcover_42d_jerk_v041_signal,
    f34dt_f34_debt_leverage_trajectory_cashcover_63d_jerk_v042_signal,
    f34dt_f34_debt_leverage_trajectory_cashcover_84d_jerk_v043_signal,
    f34dt_f34_debt_leverage_trajectory_cashcover_126d_jerk_v044_signal,
    f34dt_f34_debt_leverage_trajectory_shortcover_42d_jerk_v045_signal,
    f34dt_f34_debt_leverage_trajectory_shortcover_63d_jerk_v046_signal,
    f34dt_f34_debt_leverage_trajectory_shortcover_84d_jerk_v047_signal,
    f34dt_f34_debt_leverage_trajectory_shortcover_126d_jerk_v048_signal,
    f34dt_f34_debt_leverage_trajectory_service_42d_jerk_v049_signal,
    f34dt_f34_debt_leverage_trajectory_service_63d_jerk_v050_signal,
    f34dt_f34_debt_leverage_trajectory_service_84d_jerk_v051_signal,
    f34dt_f34_debt_leverage_trajectory_service_126d_jerk_v052_signal,
    f34dt_f34_debt_leverage_trajectory_shorttocash_42d_jerk_v053_signal,
    f34dt_f34_debt_leverage_trajectory_shorttocash_63d_jerk_v054_signal,
    f34dt_f34_debt_leverage_trajectory_shorttocash_84d_jerk_v055_signal,
    f34dt_f34_debt_leverage_trajectory_shorttocash_126d_jerk_v056_signal,
    f34dt_f34_debt_leverage_trajectory_debtext_63d_jerk_v057_signal,
    f34dt_f34_debt_leverage_trajectory_debtext_63d_jerk_v058_signal,
    f34dt_f34_debt_leverage_trajectory_debtext_63d_jerk_v059_signal,
    f34dt_f34_debt_leverage_trajectory_debtext_63d_jerk_v060_signal,
    f34dt_f34_debt_leverage_trajectory_debtext_126d_jerk_v061_signal,
    f34dt_f34_debt_leverage_trajectory_debtext_126d_jerk_v062_signal,
    f34dt_f34_debt_leverage_trajectory_debtext_126d_jerk_v063_signal,
    f34dt_f34_debt_leverage_trajectory_debtext_252d_jerk_v064_signal,
    f34dt_f34_debt_leverage_trajectory_debtext_252d_jerk_v065_signal,
    f34dt_f34_debt_leverage_trajectory_debtext_252d_jerk_v066_signal,
    f34dt_f34_debt_leverage_trajectory_debtext_252d_jerk_v067_signal,
    f34dt_f34_debt_leverage_trajectory_levz_63d_jerk_v068_signal,
    f34dt_f34_debt_leverage_trajectory_levz_63d_jerk_v069_signal,
    f34dt_f34_debt_leverage_trajectory_levz_63d_jerk_v070_signal,
    f34dt_f34_debt_leverage_trajectory_levz_63d_jerk_v071_signal,
    f34dt_f34_debt_leverage_trajectory_levz_126d_jerk_v072_signal,
    f34dt_f34_debt_leverage_trajectory_levz_126d_jerk_v073_signal,
    f34dt_f34_debt_leverage_trajectory_levz_126d_jerk_v074_signal,
    f34dt_f34_debt_leverage_trajectory_levz_126d_jerk_v075_signal,
    f34dt_f34_debt_leverage_trajectory_levz_252d_jerk_v076_signal,
    f34dt_f34_debt_leverage_trajectory_levz_252d_jerk_v077_signal,
    f34dt_f34_debt_leverage_trajectory_levz_252d_jerk_v078_signal,
    f34dt_f34_debt_leverage_trajectory_levz_252d_jerk_v079_signal,
    f34dt_f34_debt_leverage_trajectory_shortgrow_63d_jerk_v080_signal,
    f34dt_f34_debt_leverage_trajectory_shortgrow_63d_jerk_v081_signal,
    f34dt_f34_debt_leverage_trajectory_shortgrow_63d_jerk_v082_signal,
    f34dt_f34_debt_leverage_trajectory_shortgrow_63d_jerk_v083_signal,
    f34dt_f34_debt_leverage_trajectory_shortgrow_126d_jerk_v084_signal,
    f34dt_f34_debt_leverage_trajectory_shortgrow_126d_jerk_v085_signal,
    f34dt_f34_debt_leverage_trajectory_shortgrow_126d_jerk_v086_signal,
    f34dt_f34_debt_leverage_trajectory_shortgrow_126d_jerk_v087_signal,
    f34dt_f34_debt_leverage_trajectory_shortgrow_252d_jerk_v088_signal,
    f34dt_f34_debt_leverage_trajectory_shortgrow_252d_jerk_v089_signal,
    f34dt_f34_debt_leverage_trajectory_shortgrow_252d_jerk_v090_signal,
    f34dt_f34_debt_leverage_trajectory_shortgrow_252d_jerk_v091_signal,
    f34dt_f34_debt_leverage_trajectory_longgrow_63d_jerk_v092_signal,
    f34dt_f34_debt_leverage_trajectory_longgrow_63d_jerk_v093_signal,
    f34dt_f34_debt_leverage_trajectory_longgrow_63d_jerk_v094_signal,
    f34dt_f34_debt_leverage_trajectory_longgrow_63d_jerk_v095_signal,
    f34dt_f34_debt_leverage_trajectory_longgrow_126d_jerk_v096_signal,
    f34dt_f34_debt_leverage_trajectory_longgrow_126d_jerk_v097_signal,
    f34dt_f34_debt_leverage_trajectory_longgrow_126d_jerk_v098_signal,
    f34dt_f34_debt_leverage_trajectory_longgrow_126d_jerk_v099_signal,
    f34dt_f34_debt_leverage_trajectory_longgrow_252d_jerk_v100_signal,
    f34dt_f34_debt_leverage_trajectory_longgrow_252d_jerk_v101_signal,
    f34dt_f34_debt_leverage_trajectory_longgrow_252d_jerk_v102_signal,
    f34dt_f34_debt_leverage_trajectory_longgrow_252d_jerk_v103_signal,
    f34dt_f34_debt_leverage_trajectory_ebitdagrow_63d_jerk_v104_signal,
    f34dt_f34_debt_leverage_trajectory_ebitdagrow_63d_jerk_v105_signal,
    f34dt_f34_debt_leverage_trajectory_ebitdagrow_63d_jerk_v106_signal,
    f34dt_f34_debt_leverage_trajectory_ebitdagrow_63d_jerk_v107_signal,
    f34dt_f34_debt_leverage_trajectory_ebitdagrow_126d_jerk_v108_signal,
    f34dt_f34_debt_leverage_trajectory_ebitdagrow_126d_jerk_v109_signal,
    f34dt_f34_debt_leverage_trajectory_ebitdagrow_126d_jerk_v110_signal,
    f34dt_f34_debt_leverage_trajectory_ebitdagrow_126d_jerk_v111_signal,
    f34dt_f34_debt_leverage_trajectory_ebitdagrow_252d_jerk_v112_signal,
    f34dt_f34_debt_leverage_trajectory_ebitdagrow_252d_jerk_v113_signal,
    f34dt_f34_debt_leverage_trajectory_ebitdagrow_252d_jerk_v114_signal,
    f34dt_f34_debt_leverage_trajectory_ebitdagrow_252d_jerk_v115_signal,
    f34dt_f34_debt_leverage_trajectory_cashgrow_63d_jerk_v116_signal,
    f34dt_f34_debt_leverage_trajectory_cashgrow_63d_jerk_v117_signal,
    f34dt_f34_debt_leverage_trajectory_cashgrow_63d_jerk_v118_signal,
    f34dt_f34_debt_leverage_trajectory_cashgrow_63d_jerk_v119_signal,
    f34dt_f34_debt_leverage_trajectory_cashgrow_126d_jerk_v120_signal,
    f34dt_f34_debt_leverage_trajectory_cashgrow_126d_jerk_v121_signal,
    f34dt_f34_debt_leverage_trajectory_cashgrow_126d_jerk_v122_signal,
    f34dt_f34_debt_leverage_trajectory_cashgrow_126d_jerk_v123_signal,
    f34dt_f34_debt_leverage_trajectory_cashgrow_252d_jerk_v124_signal,
    f34dt_f34_debt_leverage_trajectory_cashgrow_252d_jerk_v125_signal,
    f34dt_f34_debt_leverage_trajectory_cashgrow_252d_jerk_v126_signal,
    f34dt_f34_debt_leverage_trajectory_cashgrow_252d_jerk_v127_signal,
    f34dt_f34_debt_leverage_trajectory_levrank_63d_jerk_v128_signal,
    f34dt_f34_debt_leverage_trajectory_levrank_63d_jerk_v129_signal,
    f34dt_f34_debt_leverage_trajectory_levrank_63d_jerk_v130_signal,
    f34dt_f34_debt_leverage_trajectory_levrank_63d_jerk_v131_signal,
    f34dt_f34_debt_leverage_trajectory_levrank_126d_jerk_v132_signal,
    f34dt_f34_debt_leverage_trajectory_levrank_126d_jerk_v133_signal,
    f34dt_f34_debt_leverage_trajectory_levrank_126d_jerk_v134_signal,
    f34dt_f34_debt_leverage_trajectory_levrank_126d_jerk_v135_signal,
    f34dt_f34_debt_leverage_trajectory_levrank_252d_jerk_v136_signal,
    f34dt_f34_debt_leverage_trajectory_levrank_252d_jerk_v137_signal,
    f34dt_f34_debt_leverage_trajectory_levrank_252d_jerk_v138_signal,
    f34dt_f34_debt_leverage_trajectory_levrank_252d_jerk_v139_signal,
    f34dt_f34_debt_leverage_trajectory_flowintensity_63d_jerk_v140_signal,
    f34dt_f34_debt_leverage_trajectory_flowintensity_63d_jerk_v141_signal,
    f34dt_f34_debt_leverage_trajectory_flowintensity_63d_jerk_v142_signal,
    f34dt_f34_debt_leverage_trajectory_flowintensity_63d_jerk_v143_signal,
    f34dt_f34_debt_leverage_trajectory_flowintensity_126d_jerk_v144_signal,
    f34dt_f34_debt_leverage_trajectory_flowintensity_126d_jerk_v145_signal,
    f34dt_f34_debt_leverage_trajectory_flowintensity_126d_jerk_v146_signal,
    f34dt_f34_debt_leverage_trajectory_flowintensity_126d_jerk_v147_signal,
    f34dt_f34_debt_leverage_trajectory_flowintensity_252d_jerk_v148_signal,
    f34dt_f34_debt_leverage_trajectory_flowintensity_252d_jerk_v149_signal,
    f34dt_f34_debt_leverage_trajectory_flowintensity_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F34_DEBT_LEVERAGE_TRAJECTORY_REGISTRY_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    debt = _fund(101, base=2.0e8, drift=0.02, vol=0.06).rename("debt")
    debtc = _fund(102, base=6.0e7, drift=0.015, vol=0.08).rename("debtc")
    debtnc = _fund(103, base=1.4e8, drift=0.02, vol=0.06).rename("debtnc")
    cashneq = _fund(104, base=1.2e8, drift=0.01, vol=0.09).rename("cashneq")
    ebitda = _fund(105, base=8.0e7, drift=0.02, vol=0.10, allow_neg=True).rename("ebitda")
    ncfdebt = _fund(106, base=3.0e7, drift=0.0, vol=0.20, allow_neg=True).rename("ncfdebt")

    cols = {
        "debt": debt, "debtc": debtc, "debtnc": debtnc,
        "cashneq": cashneq, "ebitda": ebitda, "ncfdebt": ncfdebt,
    }

    ALLOW = {"debt", "debtc", "debtnc", "ncfdebt", "cashneq", "ebitda"}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs %s" % (name, meta["inputs"])
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 20, "%s nunique=%d" % (name, q.nunique())
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        results[name] = y1.iloc[504:]
        n_features += 1

    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), "nan_ok=%d/%d" % (nan_ok, n_features)

    items = list(results.items())
    for i in range(len(items)):
        ni, si = items[i]
        ai = si.dropna()
        for j in range(i + 1, len(items)):
            nj, sj = items[j]
            aj = sj.dropna()
            idx = ai.index.intersection(aj.index)
            if len(idx) < 30:
                continue
            c = ai.loc[idx].corr(aj.loc[idx])
            if c is None or np.isnan(c):
                continue
            assert abs(c) <= 0.97, "CORR %s vs %s = %.4f" % (ni, nj, c)

    print("OK f34_debt_leverage_trajectory_3rd_derivatives_001_150_claude: %d features pass" % n_features)
