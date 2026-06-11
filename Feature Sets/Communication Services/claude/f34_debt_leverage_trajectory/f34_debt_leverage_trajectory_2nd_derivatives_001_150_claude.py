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
def f34dt_f34_debt_leverage_trajectory_debtgrow_63d_slope_v001_signal(debt):
    base = _logchg(debt, 63)
    d = (base - base.shift(21)) / 21.0
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtgrow_63d_slope_v002_signal(debt):
    base = _logchg(debt, 63)
    d = (base - base.shift(42)) / 42.0
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtgrow_63d_slope_v003_signal(debt):
    base = _logchg(debt, 63)
    d = (base - base.shift(63)) / 63.0
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtgrow_63d_slope_v004_signal(debt):
    base = _logchg(debt, 63)
    d = (base - base.shift(126)) / 126.0
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtgrow_126d_slope_v005_signal(debt):
    base = _logchg(debt, 126)
    d = (base - base.shift(21)) / 21.0
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtgrow_126d_slope_v006_signal(debt):
    base = _logchg(debt, 126)
    d = (base - base.shift(42)) / 42.0
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtgrow_126d_slope_v007_signal(debt):
    base = _logchg(debt, 126)
    d = (base - base.shift(126)) / 126.0
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtgrow_252d_slope_v008_signal(debt):
    base = _logchg(debt, 252)
    d = (base - base.shift(21)) / 21.0
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtgrow_252d_slope_v009_signal(debt):
    base = _logchg(debt, 252)
    d = (base - base.shift(42)) / 42.0
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtgrow_252d_slope_v010_signal(debt):
    base = _logchg(debt, 252)
    d = (base - base.shift(63)) / 63.0
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtgrow_252d_slope_v011_signal(debt):
    base = _logchg(debt, 252)
    d = (base - base.shift(126)) / 126.0
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtebitda_21d_slope_v012_signal(debt, ebitda):
    base = _debt_ebitda(debt, ebitda)
    d = (base - base.shift(21)) / 21.0
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtebitda_42d_slope_v013_signal(debt, ebitda):
    base = _debt_ebitda(debt, ebitda)
    d = (base - base.shift(42)) / 42.0
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtebitda_63d_slope_v014_signal(debt, ebitda):
    base = _debt_ebitda(debt, ebitda)
    d = (base - base.shift(63)) / 63.0
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtebitda_126d_slope_v015_signal(debt, ebitda):
    base = _debt_ebitda(debt, ebitda)
    d = (base - base.shift(126)) / 126.0
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_netdebt_21d_slope_v016_signal(debt, cashneq):
    base = _netdebt(debt, cashneq) / debt.replace(0, np.nan)
    d = (base - base.shift(21)) / 21.0
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_netdebt_42d_slope_v017_signal(debt, cashneq):
    base = _netdebt(debt, cashneq) / debt.replace(0, np.nan)
    d = (base - base.shift(42)) / 42.0
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_netdebt_63d_slope_v018_signal(debt, cashneq):
    base = _netdebt(debt, cashneq) / debt.replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_netdebt_126d_slope_v019_signal(debt, cashneq):
    base = _netdebt(debt, cashneq) / debt.replace(0, np.nan)
    d = (base - base.shift(126)) / 126.0
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_netlev_21d_slope_v020_signal(debt, cashneq, ebitda):
    base = _netdebt(debt, cashneq) / ebitda.replace(0, np.nan)
    d = (base - base.shift(21)) / 21.0
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_netlev_42d_slope_v021_signal(debt, cashneq, ebitda):
    base = _netdebt(debt, cashneq) / ebitda.replace(0, np.nan)
    d = (base - base.shift(42)) / 42.0
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_netlev_63d_slope_v022_signal(debt, cashneq, ebitda):
    base = _netdebt(debt, cashneq) / ebitda.replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_netlev_126d_slope_v023_signal(debt, cashneq, ebitda):
    base = _netdebt(debt, cashneq) / ebitda.replace(0, np.nan)
    d = (base - base.shift(126)) / 126.0
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shortmix_21d_slope_v024_signal(debtc, debt):
    base = _shortmix(debtc, debt)
    d = (base - base.shift(21)) / 21.0
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shortmix_42d_slope_v025_signal(debtc, debt):
    base = _shortmix(debtc, debt)
    d = (base - base.shift(42)) / 42.0
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shortmix_63d_slope_v026_signal(debtc, debt):
    base = _shortmix(debtc, debt)
    d = (base - base.shift(63)) / 63.0
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shortmix_126d_slope_v027_signal(debtc, debt):
    base = _shortmix(debtc, debt)
    d = (base - base.shift(126)) / 126.0
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_longmix_21d_slope_v028_signal(debtnc, debt):
    base = _longmix(debtnc, debt)
    d = (base - base.shift(21)) / 21.0
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_longmix_42d_slope_v029_signal(debtnc, debt):
    base = _longmix(debtnc, debt)
    d = (base - base.shift(42)) / 42.0
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_longmix_63d_slope_v030_signal(debtnc, debt):
    base = _longmix(debtnc, debt)
    d = (base - base.shift(63)) / 63.0
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_longmix_126d_slope_v031_signal(debtnc, debt):
    base = _longmix(debtnc, debt)
    d = (base - base.shift(126)) / 126.0
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_termskew_21d_slope_v032_signal(debtnc, debtc, debt):
    base = (debtnc - debtc) / debt.replace(0, np.nan)
    d = (base - base.shift(21)) / 21.0
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_termskew_42d_slope_v033_signal(debtnc, debtc, debt):
    base = (debtnc - debtc) / debt.replace(0, np.nan)
    d = (base - base.shift(42)) / 42.0
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_termskew_63d_slope_v034_signal(debtnc, debtc, debt):
    base = (debtnc - debtc) / debt.replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_termskew_126d_slope_v035_signal(debtnc, debtc, debt):
    base = (debtnc - debtc) / debt.replace(0, np.nan)
    d = (base - base.shift(126)) / 126.0
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_paydownflow_21d_slope_v036_signal(ncfdebt, debt):
    base = _paydown_flow(ncfdebt, debt)
    d = (base - base.shift(21)) / 21.0
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_paydownflow_42d_slope_v037_signal(ncfdebt, debt):
    base = _paydown_flow(ncfdebt, debt)
    d = (base - base.shift(42)) / 42.0
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_paydownflow_63d_slope_v038_signal(ncfdebt, debt):
    base = _paydown_flow(ncfdebt, debt)
    d = (base - base.shift(63)) / 63.0
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_paydownflow_126d_slope_v039_signal(ncfdebt, debt):
    base = _paydown_flow(ncfdebt, debt)
    d = (base - base.shift(126)) / 126.0
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_cashcover_21d_slope_v040_signal(cashneq, debt):
    base = cashneq / debt.replace(0, np.nan)
    d = (base - base.shift(21)) / 21.0
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_cashcover_42d_slope_v041_signal(cashneq, debt):
    base = cashneq / debt.replace(0, np.nan)
    d = (base - base.shift(42)) / 42.0
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_cashcover_63d_slope_v042_signal(cashneq, debt):
    base = cashneq / debt.replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_cashcover_126d_slope_v043_signal(cashneq, debt):
    base = cashneq / debt.replace(0, np.nan)
    d = (base - base.shift(126)) / 126.0
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shortcover_21d_slope_v044_signal(ebitda, debtc):
    base = ebitda / debtc.replace(0, np.nan)
    d = (base - base.shift(21)) / 21.0
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shortcover_42d_slope_v045_signal(ebitda, debtc):
    base = ebitda / debtc.replace(0, np.nan)
    d = (base - base.shift(42)) / 42.0
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shortcover_63d_slope_v046_signal(ebitda, debtc):
    base = ebitda / debtc.replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shortcover_126d_slope_v047_signal(ebitda, debtc):
    base = ebitda / debtc.replace(0, np.nan)
    d = (base - base.shift(126)) / 126.0
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_service_21d_slope_v048_signal(ebitda, debt):
    base = ebitda / debt.replace(0, np.nan)
    d = (base - base.shift(21)) / 21.0
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_service_42d_slope_v049_signal(ebitda, debt):
    base = ebitda / debt.replace(0, np.nan)
    d = (base - base.shift(42)) / 42.0
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_service_63d_slope_v050_signal(ebitda, debt):
    base = ebitda / debt.replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_service_126d_slope_v051_signal(ebitda, debt):
    base = ebitda / debt.replace(0, np.nan)
    d = (base - base.shift(126)) / 126.0
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shorttocash_21d_slope_v052_signal(debtc, cashneq):
    base = debtc / cashneq.replace(0, np.nan)
    d = (base - base.shift(21)) / 21.0
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shorttocash_42d_slope_v053_signal(debtc, cashneq):
    base = debtc / cashneq.replace(0, np.nan)
    d = (base - base.shift(42)) / 42.0
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shorttocash_63d_slope_v054_signal(debtc, cashneq):
    base = debtc / cashneq.replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shorttocash_126d_slope_v055_signal(debtc, cashneq):
    base = debtc / cashneq.replace(0, np.nan)
    d = (base - base.shift(126)) / 126.0
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtext_63d_slope_v056_signal(debt):
    base = debt / _mean(debt, 63).replace(0, np.nan) - 1.0
    d = (base - base.shift(21)) / 21.0
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtext_126d_slope_v057_signal(debt):
    base = debt / _mean(debt, 126).replace(0, np.nan) - 1.0
    d = (base - base.shift(21)) / 21.0
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtext_126d_slope_v058_signal(debt):
    base = debt / _mean(debt, 126).replace(0, np.nan) - 1.0
    d = (base - base.shift(42)) / 42.0
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtext_126d_slope_v059_signal(debt):
    base = debt / _mean(debt, 126).replace(0, np.nan) - 1.0
    d = (base - base.shift(126)) / 126.0
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtext_252d_slope_v060_signal(debt):
    base = debt / _mean(debt, 252).replace(0, np.nan) - 1.0
    d = (base - base.shift(21)) / 21.0
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtext_252d_slope_v061_signal(debt):
    base = debt / _mean(debt, 252).replace(0, np.nan) - 1.0
    d = (base - base.shift(42)) / 42.0
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtext_252d_slope_v062_signal(debt):
    base = debt / _mean(debt, 252).replace(0, np.nan) - 1.0
    d = (base - base.shift(63)) / 63.0
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_debtext_252d_slope_v063_signal(debt):
    base = debt / _mean(debt, 252).replace(0, np.nan) - 1.0
    d = (base - base.shift(126)) / 126.0
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levz_63d_slope_v064_signal(debt, ebitda):
    base = _z(_debt_ebitda(debt, ebitda), 63)
    d = (base - base.shift(21)) / 21.0
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levz_63d_slope_v065_signal(debt, ebitda):
    base = _z(_debt_ebitda(debt, ebitda), 63)
    d = (base - base.shift(42)) / 42.0
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levz_63d_slope_v066_signal(debt, ebitda):
    base = _z(_debt_ebitda(debt, ebitda), 63)
    d = (base - base.shift(63)) / 63.0
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levz_63d_slope_v067_signal(debt, ebitda):
    base = _z(_debt_ebitda(debt, ebitda), 63)
    d = (base - base.shift(126)) / 126.0
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levz_126d_slope_v068_signal(debt, ebitda):
    base = _z(_debt_ebitda(debt, ebitda), 126)
    d = (base - base.shift(21)) / 21.0
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levz_126d_slope_v069_signal(debt, ebitda):
    base = _z(_debt_ebitda(debt, ebitda), 126)
    d = (base - base.shift(42)) / 42.0
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levz_126d_slope_v070_signal(debt, ebitda):
    base = _z(_debt_ebitda(debt, ebitda), 126)
    d = (base - base.shift(63)) / 63.0
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levz_126d_slope_v071_signal(debt, ebitda):
    base = _z(_debt_ebitda(debt, ebitda), 126)
    d = (base - base.shift(126)) / 126.0
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levz_252d_slope_v072_signal(debt, ebitda):
    base = _z(_debt_ebitda(debt, ebitda), 252)
    d = (base - base.shift(21)) / 21.0
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levz_252d_slope_v073_signal(debt, ebitda):
    base = _z(_debt_ebitda(debt, ebitda), 252)
    d = (base - base.shift(42)) / 42.0
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levz_252d_slope_v074_signal(debt, ebitda):
    base = _z(_debt_ebitda(debt, ebitda), 252)
    d = (base - base.shift(63)) / 63.0
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levz_252d_slope_v075_signal(debt, ebitda):
    base = _z(_debt_ebitda(debt, ebitda), 252)
    d = (base - base.shift(126)) / 126.0
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shortgrow_63d_slope_v076_signal(debtc):
    base = _logchg(debtc, 63)
    d = (base - base.shift(21)) / 21.0
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shortgrow_63d_slope_v077_signal(debtc):
    base = _logchg(debtc, 63)
    d = (base - base.shift(42)) / 42.0
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shortgrow_63d_slope_v078_signal(debtc):
    base = _logchg(debtc, 63)
    d = (base - base.shift(63)) / 63.0
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shortgrow_63d_slope_v079_signal(debtc):
    base = _logchg(debtc, 63)
    d = (base - base.shift(126)) / 126.0
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shortgrow_126d_slope_v080_signal(debtc):
    base = _logchg(debtc, 126)
    d = (base - base.shift(21)) / 21.0
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shortgrow_126d_slope_v081_signal(debtc):
    base = _logchg(debtc, 126)
    d = (base - base.shift(42)) / 42.0
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shortgrow_126d_slope_v082_signal(debtc):
    base = _logchg(debtc, 126)
    d = (base - base.shift(126)) / 126.0
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shortgrow_252d_slope_v083_signal(debtc):
    base = _logchg(debtc, 252)
    d = (base - base.shift(21)) / 21.0
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shortgrow_252d_slope_v084_signal(debtc):
    base = _logchg(debtc, 252)
    d = (base - base.shift(42)) / 42.0
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shortgrow_252d_slope_v085_signal(debtc):
    base = _logchg(debtc, 252)
    d = (base - base.shift(63)) / 63.0
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_shortgrow_252d_slope_v086_signal(debtc):
    base = _logchg(debtc, 252)
    d = (base - base.shift(126)) / 126.0
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_longgrow_63d_slope_v087_signal(debtnc):
    base = _logchg(debtnc, 63)
    d = (base - base.shift(21)) / 21.0
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_longgrow_63d_slope_v088_signal(debtnc):
    base = _logchg(debtnc, 63)
    d = (base - base.shift(42)) / 42.0
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_longgrow_63d_slope_v089_signal(debtnc):
    base = _logchg(debtnc, 63)
    d = (base - base.shift(63)) / 63.0
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_longgrow_63d_slope_v090_signal(debtnc):
    base = _logchg(debtnc, 63)
    d = (base - base.shift(126)) / 126.0
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_longgrow_126d_slope_v091_signal(debtnc):
    base = _logchg(debtnc, 126)
    d = (base - base.shift(21)) / 21.0
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_longgrow_126d_slope_v092_signal(debtnc):
    base = _logchg(debtnc, 126)
    d = (base - base.shift(42)) / 42.0
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_longgrow_126d_slope_v093_signal(debtnc):
    base = _logchg(debtnc, 126)
    d = (base - base.shift(126)) / 126.0
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_longgrow_252d_slope_v094_signal(debtnc):
    base = _logchg(debtnc, 252)
    d = (base - base.shift(21)) / 21.0
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_longgrow_252d_slope_v095_signal(debtnc):
    base = _logchg(debtnc, 252)
    d = (base - base.shift(42)) / 42.0
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_longgrow_252d_slope_v096_signal(debtnc):
    base = _logchg(debtnc, 252)
    d = (base - base.shift(63)) / 63.0
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_longgrow_252d_slope_v097_signal(debtnc):
    base = _logchg(debtnc, 252)
    d = (base - base.shift(126)) / 126.0
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_ebitdagrow_63d_slope_v098_signal(ebitda):
    base = _logchg(ebitda.abs(), 63)
    d = (base - base.shift(21)) / 21.0
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_ebitdagrow_63d_slope_v099_signal(ebitda):
    base = _logchg(ebitda.abs(), 63)
    d = (base - base.shift(42)) / 42.0
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_ebitdagrow_63d_slope_v100_signal(ebitda):
    base = _logchg(ebitda.abs(), 63)
    d = (base - base.shift(63)) / 63.0
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_ebitdagrow_63d_slope_v101_signal(ebitda):
    base = _logchg(ebitda.abs(), 63)
    d = (base - base.shift(126)) / 126.0
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_ebitdagrow_126d_slope_v102_signal(ebitda):
    base = _logchg(ebitda.abs(), 126)
    d = (base - base.shift(21)) / 21.0
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_ebitdagrow_126d_slope_v103_signal(ebitda):
    base = _logchg(ebitda.abs(), 126)
    d = (base - base.shift(42)) / 42.0
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_ebitdagrow_126d_slope_v104_signal(ebitda):
    base = _logchg(ebitda.abs(), 126)
    d = (base - base.shift(126)) / 126.0
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_ebitdagrow_252d_slope_v105_signal(ebitda):
    base = _logchg(ebitda.abs(), 252)
    d = (base - base.shift(21)) / 21.0
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_ebitdagrow_252d_slope_v106_signal(ebitda):
    base = _logchg(ebitda.abs(), 252)
    d = (base - base.shift(42)) / 42.0
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_ebitdagrow_252d_slope_v107_signal(ebitda):
    base = _logchg(ebitda.abs(), 252)
    d = (base - base.shift(63)) / 63.0
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_ebitdagrow_252d_slope_v108_signal(ebitda):
    base = _logchg(ebitda.abs(), 252)
    d = (base - base.shift(126)) / 126.0
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_cashgrow_63d_slope_v109_signal(cashneq):
    base = _logchg(cashneq, 63)
    d = (base - base.shift(21)) / 21.0
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_cashgrow_63d_slope_v110_signal(cashneq):
    base = _logchg(cashneq, 63)
    d = (base - base.shift(42)) / 42.0
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_cashgrow_63d_slope_v111_signal(cashneq):
    base = _logchg(cashneq, 63)
    d = (base - base.shift(63)) / 63.0
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_cashgrow_63d_slope_v112_signal(cashneq):
    base = _logchg(cashneq, 63)
    d = (base - base.shift(126)) / 126.0
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_cashgrow_126d_slope_v113_signal(cashneq):
    base = _logchg(cashneq, 126)
    d = (base - base.shift(21)) / 21.0
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_cashgrow_126d_slope_v114_signal(cashneq):
    base = _logchg(cashneq, 126)
    d = (base - base.shift(42)) / 42.0
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_cashgrow_126d_slope_v115_signal(cashneq):
    base = _logchg(cashneq, 126)
    d = (base - base.shift(126)) / 126.0
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_cashgrow_252d_slope_v116_signal(cashneq):
    base = _logchg(cashneq, 252)
    d = (base - base.shift(21)) / 21.0
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_cashgrow_252d_slope_v117_signal(cashneq):
    base = _logchg(cashneq, 252)
    d = (base - base.shift(42)) / 42.0
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_cashgrow_252d_slope_v118_signal(cashneq):
    base = _logchg(cashneq, 252)
    d = (base - base.shift(63)) / 63.0
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_cashgrow_252d_slope_v119_signal(cashneq):
    base = _logchg(cashneq, 252)
    d = (base - base.shift(126)) / 126.0
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levrank_63d_slope_v120_signal(debt, ebitda):
    base = _rank(_debt_ebitda(debt, ebitda), 63)
    d = (base - base.shift(21)) / 21.0
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levrank_63d_slope_v121_signal(debt, ebitda):
    base = _rank(_debt_ebitda(debt, ebitda), 63)
    d = (base - base.shift(42)) / 42.0
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levrank_63d_slope_v122_signal(debt, ebitda):
    base = _rank(_debt_ebitda(debt, ebitda), 63)
    d = (base - base.shift(63)) / 63.0
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levrank_63d_slope_v123_signal(debt, ebitda):
    base = _rank(_debt_ebitda(debt, ebitda), 63)
    d = (base - base.shift(126)) / 126.0
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levrank_126d_slope_v124_signal(debt, ebitda):
    base = _rank(_debt_ebitda(debt, ebitda), 126)
    d = (base - base.shift(21)) / 21.0
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levrank_126d_slope_v125_signal(debt, ebitda):
    base = _rank(_debt_ebitda(debt, ebitda), 126)
    d = (base - base.shift(42)) / 42.0
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levrank_126d_slope_v126_signal(debt, ebitda):
    base = _rank(_debt_ebitda(debt, ebitda), 126)
    d = (base - base.shift(63)) / 63.0
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levrank_126d_slope_v127_signal(debt, ebitda):
    base = _rank(_debt_ebitda(debt, ebitda), 126)
    d = (base - base.shift(126)) / 126.0
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levrank_252d_slope_v128_signal(debt, ebitda):
    base = _rank(_debt_ebitda(debt, ebitda), 252)
    d = (base - base.shift(21)) / 21.0
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levrank_252d_slope_v129_signal(debt, ebitda):
    base = _rank(_debt_ebitda(debt, ebitda), 252)
    d = (base - base.shift(42)) / 42.0
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levrank_252d_slope_v130_signal(debt, ebitda):
    base = _rank(_debt_ebitda(debt, ebitda), 252)
    d = (base - base.shift(63)) / 63.0
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_levrank_252d_slope_v131_signal(debt, ebitda):
    base = _rank(_debt_ebitda(debt, ebitda), 252)
    d = (base - base.shift(126)) / 126.0
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_flowintensity_63d_slope_v132_signal(ncfdebt, debt):
    base = ncfdebt.rolling(63, min_periods=max(1, 63 // 2)).sum() / debt.replace(0, np.nan)
    d = (base - base.shift(21)) / 21.0
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_flowintensity_63d_slope_v133_signal(ncfdebt, debt):
    base = ncfdebt.rolling(63, min_periods=max(1, 63 // 2)).sum() / debt.replace(0, np.nan)
    d = (base - base.shift(42)) / 42.0
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_flowintensity_63d_slope_v134_signal(ncfdebt, debt):
    base = ncfdebt.rolling(63, min_periods=max(1, 63 // 2)).sum() / debt.replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_flowintensity_63d_slope_v135_signal(ncfdebt, debt):
    base = ncfdebt.rolling(63, min_periods=max(1, 63 // 2)).sum() / debt.replace(0, np.nan)
    d = (base - base.shift(126)) / 126.0
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_flowintensity_126d_slope_v136_signal(ncfdebt, debt):
    base = ncfdebt.rolling(126, min_periods=max(1, 126 // 2)).sum() / debt.replace(0, np.nan)
    d = (base - base.shift(21)) / 21.0
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_flowintensity_126d_slope_v137_signal(ncfdebt, debt):
    base = ncfdebt.rolling(126, min_periods=max(1, 126 // 2)).sum() / debt.replace(0, np.nan)
    d = (base - base.shift(42)) / 42.0
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_flowintensity_126d_slope_v138_signal(ncfdebt, debt):
    base = ncfdebt.rolling(126, min_periods=max(1, 126 // 2)).sum() / debt.replace(0, np.nan)
    d = (base - base.shift(126)) / 126.0
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_flowintensity_252d_slope_v139_signal(ncfdebt, debt):
    base = ncfdebt.rolling(252, min_periods=max(1, 252 // 2)).sum() / debt.replace(0, np.nan)
    d = (base - base.shift(21)) / 21.0
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_flowintensity_252d_slope_v140_signal(ncfdebt, debt):
    base = ncfdebt.rolling(252, min_periods=max(1, 252 // 2)).sum() / debt.replace(0, np.nan)
    d = (base - base.shift(42)) / 42.0
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_flowintensity_252d_slope_v141_signal(ncfdebt, debt):
    base = ncfdebt.rolling(252, min_periods=max(1, 252 // 2)).sum() / debt.replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_flowintensity_252d_slope_v142_signal(ncfdebt, debt):
    base = ncfdebt.rolling(252, min_periods=max(1, 252 // 2)).sum() / debt.replace(0, np.nan)
    d = (base - base.shift(126)) / 126.0
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_sltilt_21d_slope_v143_signal(debtc, debtnc):
    base = debtc / debtnc.replace(0, np.nan)
    d = (base - base.shift(21)) / 21.0
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_sltilt_42d_slope_v144_signal(debtc, debtnc):
    base = debtc / debtnc.replace(0, np.nan)
    d = (base - base.shift(42)) / 42.0
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_sltilt_63d_slope_v145_signal(debtc, debtnc):
    base = debtc / debtnc.replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_cashtoshort_21d_slope_v146_signal(cashneq, debtc):
    base = cashneq / debtc.replace(0, np.nan)
    d = (base - base.shift(21)) / 21.0
    out = _rank(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_cashtoshort_42d_slope_v147_signal(cashneq, debtc):
    base = cashneq / debtc.replace(0, np.nan)
    d = (base - base.shift(42)) / 42.0
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_cashtoshort_63d_slope_v148_signal(cashneq, debtc):
    base = cashneq / debtc.replace(0, np.nan)
    d = (base - base.shift(63)) / 63.0
    scale = d.abs().rolling(252, min_periods=63).median().replace(0, np.nan)
    out = np.tanh(d / scale)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_cashtoshort_126d_slope_v149_signal(cashneq, debtc):
    base = cashneq / debtc.replace(0, np.nan)
    d = (base - base.shift(126)) / 126.0
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f34dt_f34_debt_leverage_trajectory_netdebtmag_63d_slope_v150_signal(debt, cashneq):
    base = _logchg((debt - cashneq).abs(), 63)
    d = (base - base.shift(21)) / 21.0
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f34dt_f34_debt_leverage_trajectory_debtgrow_63d_slope_v001_signal,
    f34dt_f34_debt_leverage_trajectory_debtgrow_63d_slope_v002_signal,
    f34dt_f34_debt_leverage_trajectory_debtgrow_63d_slope_v003_signal,
    f34dt_f34_debt_leverage_trajectory_debtgrow_63d_slope_v004_signal,
    f34dt_f34_debt_leverage_trajectory_debtgrow_126d_slope_v005_signal,
    f34dt_f34_debt_leverage_trajectory_debtgrow_126d_slope_v006_signal,
    f34dt_f34_debt_leverage_trajectory_debtgrow_126d_slope_v007_signal,
    f34dt_f34_debt_leverage_trajectory_debtgrow_252d_slope_v008_signal,
    f34dt_f34_debt_leverage_trajectory_debtgrow_252d_slope_v009_signal,
    f34dt_f34_debt_leverage_trajectory_debtgrow_252d_slope_v010_signal,
    f34dt_f34_debt_leverage_trajectory_debtgrow_252d_slope_v011_signal,
    f34dt_f34_debt_leverage_trajectory_debtebitda_21d_slope_v012_signal,
    f34dt_f34_debt_leverage_trajectory_debtebitda_42d_slope_v013_signal,
    f34dt_f34_debt_leverage_trajectory_debtebitda_63d_slope_v014_signal,
    f34dt_f34_debt_leverage_trajectory_debtebitda_126d_slope_v015_signal,
    f34dt_f34_debt_leverage_trajectory_netdebt_21d_slope_v016_signal,
    f34dt_f34_debt_leverage_trajectory_netdebt_42d_slope_v017_signal,
    f34dt_f34_debt_leverage_trajectory_netdebt_63d_slope_v018_signal,
    f34dt_f34_debt_leverage_trajectory_netdebt_126d_slope_v019_signal,
    f34dt_f34_debt_leverage_trajectory_netlev_21d_slope_v020_signal,
    f34dt_f34_debt_leverage_trajectory_netlev_42d_slope_v021_signal,
    f34dt_f34_debt_leverage_trajectory_netlev_63d_slope_v022_signal,
    f34dt_f34_debt_leverage_trajectory_netlev_126d_slope_v023_signal,
    f34dt_f34_debt_leverage_trajectory_shortmix_21d_slope_v024_signal,
    f34dt_f34_debt_leverage_trajectory_shortmix_42d_slope_v025_signal,
    f34dt_f34_debt_leverage_trajectory_shortmix_63d_slope_v026_signal,
    f34dt_f34_debt_leverage_trajectory_shortmix_126d_slope_v027_signal,
    f34dt_f34_debt_leverage_trajectory_longmix_21d_slope_v028_signal,
    f34dt_f34_debt_leverage_trajectory_longmix_42d_slope_v029_signal,
    f34dt_f34_debt_leverage_trajectory_longmix_63d_slope_v030_signal,
    f34dt_f34_debt_leverage_trajectory_longmix_126d_slope_v031_signal,
    f34dt_f34_debt_leverage_trajectory_termskew_21d_slope_v032_signal,
    f34dt_f34_debt_leverage_trajectory_termskew_42d_slope_v033_signal,
    f34dt_f34_debt_leverage_trajectory_termskew_63d_slope_v034_signal,
    f34dt_f34_debt_leverage_trajectory_termskew_126d_slope_v035_signal,
    f34dt_f34_debt_leverage_trajectory_paydownflow_21d_slope_v036_signal,
    f34dt_f34_debt_leverage_trajectory_paydownflow_42d_slope_v037_signal,
    f34dt_f34_debt_leverage_trajectory_paydownflow_63d_slope_v038_signal,
    f34dt_f34_debt_leverage_trajectory_paydownflow_126d_slope_v039_signal,
    f34dt_f34_debt_leverage_trajectory_cashcover_21d_slope_v040_signal,
    f34dt_f34_debt_leverage_trajectory_cashcover_42d_slope_v041_signal,
    f34dt_f34_debt_leverage_trajectory_cashcover_63d_slope_v042_signal,
    f34dt_f34_debt_leverage_trajectory_cashcover_126d_slope_v043_signal,
    f34dt_f34_debt_leverage_trajectory_shortcover_21d_slope_v044_signal,
    f34dt_f34_debt_leverage_trajectory_shortcover_42d_slope_v045_signal,
    f34dt_f34_debt_leverage_trajectory_shortcover_63d_slope_v046_signal,
    f34dt_f34_debt_leverage_trajectory_shortcover_126d_slope_v047_signal,
    f34dt_f34_debt_leverage_trajectory_service_21d_slope_v048_signal,
    f34dt_f34_debt_leverage_trajectory_service_42d_slope_v049_signal,
    f34dt_f34_debt_leverage_trajectory_service_63d_slope_v050_signal,
    f34dt_f34_debt_leverage_trajectory_service_126d_slope_v051_signal,
    f34dt_f34_debt_leverage_trajectory_shorttocash_21d_slope_v052_signal,
    f34dt_f34_debt_leverage_trajectory_shorttocash_42d_slope_v053_signal,
    f34dt_f34_debt_leverage_trajectory_shorttocash_63d_slope_v054_signal,
    f34dt_f34_debt_leverage_trajectory_shorttocash_126d_slope_v055_signal,
    f34dt_f34_debt_leverage_trajectory_debtext_63d_slope_v056_signal,
    f34dt_f34_debt_leverage_trajectory_debtext_126d_slope_v057_signal,
    f34dt_f34_debt_leverage_trajectory_debtext_126d_slope_v058_signal,
    f34dt_f34_debt_leverage_trajectory_debtext_126d_slope_v059_signal,
    f34dt_f34_debt_leverage_trajectory_debtext_252d_slope_v060_signal,
    f34dt_f34_debt_leverage_trajectory_debtext_252d_slope_v061_signal,
    f34dt_f34_debt_leverage_trajectory_debtext_252d_slope_v062_signal,
    f34dt_f34_debt_leverage_trajectory_debtext_252d_slope_v063_signal,
    f34dt_f34_debt_leverage_trajectory_levz_63d_slope_v064_signal,
    f34dt_f34_debt_leverage_trajectory_levz_63d_slope_v065_signal,
    f34dt_f34_debt_leverage_trajectory_levz_63d_slope_v066_signal,
    f34dt_f34_debt_leverage_trajectory_levz_63d_slope_v067_signal,
    f34dt_f34_debt_leverage_trajectory_levz_126d_slope_v068_signal,
    f34dt_f34_debt_leverage_trajectory_levz_126d_slope_v069_signal,
    f34dt_f34_debt_leverage_trajectory_levz_126d_slope_v070_signal,
    f34dt_f34_debt_leverage_trajectory_levz_126d_slope_v071_signal,
    f34dt_f34_debt_leverage_trajectory_levz_252d_slope_v072_signal,
    f34dt_f34_debt_leverage_trajectory_levz_252d_slope_v073_signal,
    f34dt_f34_debt_leverage_trajectory_levz_252d_slope_v074_signal,
    f34dt_f34_debt_leverage_trajectory_levz_252d_slope_v075_signal,
    f34dt_f34_debt_leverage_trajectory_shortgrow_63d_slope_v076_signal,
    f34dt_f34_debt_leverage_trajectory_shortgrow_63d_slope_v077_signal,
    f34dt_f34_debt_leverage_trajectory_shortgrow_63d_slope_v078_signal,
    f34dt_f34_debt_leverage_trajectory_shortgrow_63d_slope_v079_signal,
    f34dt_f34_debt_leverage_trajectory_shortgrow_126d_slope_v080_signal,
    f34dt_f34_debt_leverage_trajectory_shortgrow_126d_slope_v081_signal,
    f34dt_f34_debt_leverage_trajectory_shortgrow_126d_slope_v082_signal,
    f34dt_f34_debt_leverage_trajectory_shortgrow_252d_slope_v083_signal,
    f34dt_f34_debt_leverage_trajectory_shortgrow_252d_slope_v084_signal,
    f34dt_f34_debt_leverage_trajectory_shortgrow_252d_slope_v085_signal,
    f34dt_f34_debt_leverage_trajectory_shortgrow_252d_slope_v086_signal,
    f34dt_f34_debt_leverage_trajectory_longgrow_63d_slope_v087_signal,
    f34dt_f34_debt_leverage_trajectory_longgrow_63d_slope_v088_signal,
    f34dt_f34_debt_leverage_trajectory_longgrow_63d_slope_v089_signal,
    f34dt_f34_debt_leverage_trajectory_longgrow_63d_slope_v090_signal,
    f34dt_f34_debt_leverage_trajectory_longgrow_126d_slope_v091_signal,
    f34dt_f34_debt_leverage_trajectory_longgrow_126d_slope_v092_signal,
    f34dt_f34_debt_leverage_trajectory_longgrow_126d_slope_v093_signal,
    f34dt_f34_debt_leverage_trajectory_longgrow_252d_slope_v094_signal,
    f34dt_f34_debt_leverage_trajectory_longgrow_252d_slope_v095_signal,
    f34dt_f34_debt_leverage_trajectory_longgrow_252d_slope_v096_signal,
    f34dt_f34_debt_leverage_trajectory_longgrow_252d_slope_v097_signal,
    f34dt_f34_debt_leverage_trajectory_ebitdagrow_63d_slope_v098_signal,
    f34dt_f34_debt_leverage_trajectory_ebitdagrow_63d_slope_v099_signal,
    f34dt_f34_debt_leverage_trajectory_ebitdagrow_63d_slope_v100_signal,
    f34dt_f34_debt_leverage_trajectory_ebitdagrow_63d_slope_v101_signal,
    f34dt_f34_debt_leverage_trajectory_ebitdagrow_126d_slope_v102_signal,
    f34dt_f34_debt_leverage_trajectory_ebitdagrow_126d_slope_v103_signal,
    f34dt_f34_debt_leverage_trajectory_ebitdagrow_126d_slope_v104_signal,
    f34dt_f34_debt_leverage_trajectory_ebitdagrow_252d_slope_v105_signal,
    f34dt_f34_debt_leverage_trajectory_ebitdagrow_252d_slope_v106_signal,
    f34dt_f34_debt_leverage_trajectory_ebitdagrow_252d_slope_v107_signal,
    f34dt_f34_debt_leverage_trajectory_ebitdagrow_252d_slope_v108_signal,
    f34dt_f34_debt_leverage_trajectory_cashgrow_63d_slope_v109_signal,
    f34dt_f34_debt_leverage_trajectory_cashgrow_63d_slope_v110_signal,
    f34dt_f34_debt_leverage_trajectory_cashgrow_63d_slope_v111_signal,
    f34dt_f34_debt_leverage_trajectory_cashgrow_63d_slope_v112_signal,
    f34dt_f34_debt_leverage_trajectory_cashgrow_126d_slope_v113_signal,
    f34dt_f34_debt_leverage_trajectory_cashgrow_126d_slope_v114_signal,
    f34dt_f34_debt_leverage_trajectory_cashgrow_126d_slope_v115_signal,
    f34dt_f34_debt_leverage_trajectory_cashgrow_252d_slope_v116_signal,
    f34dt_f34_debt_leverage_trajectory_cashgrow_252d_slope_v117_signal,
    f34dt_f34_debt_leverage_trajectory_cashgrow_252d_slope_v118_signal,
    f34dt_f34_debt_leverage_trajectory_cashgrow_252d_slope_v119_signal,
    f34dt_f34_debt_leverage_trajectory_levrank_63d_slope_v120_signal,
    f34dt_f34_debt_leverage_trajectory_levrank_63d_slope_v121_signal,
    f34dt_f34_debt_leverage_trajectory_levrank_63d_slope_v122_signal,
    f34dt_f34_debt_leverage_trajectory_levrank_63d_slope_v123_signal,
    f34dt_f34_debt_leverage_trajectory_levrank_126d_slope_v124_signal,
    f34dt_f34_debt_leverage_trajectory_levrank_126d_slope_v125_signal,
    f34dt_f34_debt_leverage_trajectory_levrank_126d_slope_v126_signal,
    f34dt_f34_debt_leverage_trajectory_levrank_126d_slope_v127_signal,
    f34dt_f34_debt_leverage_trajectory_levrank_252d_slope_v128_signal,
    f34dt_f34_debt_leverage_trajectory_levrank_252d_slope_v129_signal,
    f34dt_f34_debt_leverage_trajectory_levrank_252d_slope_v130_signal,
    f34dt_f34_debt_leverage_trajectory_levrank_252d_slope_v131_signal,
    f34dt_f34_debt_leverage_trajectory_flowintensity_63d_slope_v132_signal,
    f34dt_f34_debt_leverage_trajectory_flowintensity_63d_slope_v133_signal,
    f34dt_f34_debt_leverage_trajectory_flowintensity_63d_slope_v134_signal,
    f34dt_f34_debt_leverage_trajectory_flowintensity_63d_slope_v135_signal,
    f34dt_f34_debt_leverage_trajectory_flowintensity_126d_slope_v136_signal,
    f34dt_f34_debt_leverage_trajectory_flowintensity_126d_slope_v137_signal,
    f34dt_f34_debt_leverage_trajectory_flowintensity_126d_slope_v138_signal,
    f34dt_f34_debt_leverage_trajectory_flowintensity_252d_slope_v139_signal,
    f34dt_f34_debt_leverage_trajectory_flowintensity_252d_slope_v140_signal,
    f34dt_f34_debt_leverage_trajectory_flowintensity_252d_slope_v141_signal,
    f34dt_f34_debt_leverage_trajectory_flowintensity_252d_slope_v142_signal,
    f34dt_f34_debt_leverage_trajectory_sltilt_21d_slope_v143_signal,
    f34dt_f34_debt_leverage_trajectory_sltilt_42d_slope_v144_signal,
    f34dt_f34_debt_leverage_trajectory_sltilt_63d_slope_v145_signal,
    f34dt_f34_debt_leverage_trajectory_cashtoshort_21d_slope_v146_signal,
    f34dt_f34_debt_leverage_trajectory_cashtoshort_42d_slope_v147_signal,
    f34dt_f34_debt_leverage_trajectory_cashtoshort_63d_slope_v148_signal,
    f34dt_f34_debt_leverage_trajectory_cashtoshort_126d_slope_v149_signal,
    f34dt_f34_debt_leverage_trajectory_netdebtmag_63d_slope_v150_signal,
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

    print("OK f34_debt_leverage_trajectory_2nd_derivatives_001_150_claude: %d features pass" % n_features)
