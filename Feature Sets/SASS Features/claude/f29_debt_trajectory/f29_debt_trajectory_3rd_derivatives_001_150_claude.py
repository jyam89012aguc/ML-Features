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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _roc(s, w):
    # 1st math derivative: rate of change over w
    return s - s.shift(w)


def _jerk(s, w):
    # 2nd math derivative: change of the rate of change over w
    return s - 2.0 * s.shift(w) + s.shift(2 * w)


# ===== folder domain primitives (debt trajectory) =====
def _f29_growth(d, w):
    return np.log(d.replace(0, np.nan) / d.shift(w).replace(0, np.nan))


def _f29_pctchg(d, w):
    return d / d.shift(w).replace(0, np.nan) - 1.0


def _f29_netdebt(debt, cashneq):
    return debt - cashneq


def _f29_st_share(debtc, debt):
    return debtc / debt.replace(0, np.nan)


def _f29_lt_share(debtnc, debt):
    return debtnc / debt.replace(0, np.nan)


def _f29_cov(cashneq, debt):
    return cashneq / debt.replace(0, np.nan)


def f29dt_f29_debt_trajectory_buildvsmeddd_504d_jerk_v001_signal(debt):
    med = debt.rolling(504, min_periods=252).median()
    X = debt / med.replace(0, np.nan) - 1.0
    b = _jerk(X, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_buildvsmeddddev_504d_jerk_v002_signal(debt):
    med = debt.rolling(504, min_periods=252).median()
    X = debt / med.replace(0, np.nan) - 1.0
    j0 = _jerk(X, 126)
    b = j0 - _mean(j0, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_buildvsmedddema_504d_jerk_v003_signal(debt):
    med = debt.rolling(504, min_periods=252).median()
    X = debt / med.replace(0, np.nan) - 1.0
    b = _jerk(X, 126).ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_buildvsmedddrank_504d_jerk_v004_signal(debt):
    med = debt.rolling(504, min_periods=252).median()
    X = debt / med.replace(0, np.nan) - 1.0
    b = _rank(_jerk(X, 126), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_buildvsmedddtanh_504d_jerk_v005_signal(debt):
    med = debt.rolling(504, min_periods=252).median()
    X = debt / med.replace(0, np.nan) - 1.0
    b = np.tanh(2.0 * _z(_jerk(X, 126), 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_buildvsmedddvol_504d_jerk_v006_signal(debt):
    med = debt.rolling(504, min_periods=252).median()
    X = debt / med.replace(0, np.nan) - 1.0
    j0 = _jerk(X, 126)
    b = j0 / _std(_roc(X, 126), 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashcovdd_126d_jerk_v007_signal(cashneq, debt):
    X = _f29_cov(cashneq, debt)
    b = _jerk(X, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashcovdddev_126d_jerk_v008_signal(cashneq, debt):
    X = _f29_cov(cashneq, debt)
    j0 = _jerk(X, 63)
    b = j0 - _mean(j0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashcovddema_126d_jerk_v009_signal(cashneq, debt):
    X = _f29_cov(cashneq, debt)
    b = _jerk(X, 63).ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashcovddrank_126d_jerk_v010_signal(cashneq, debt):
    X = _f29_cov(cashneq, debt)
    b = _rank(_jerk(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashcovddsgnmag_126d_jerk_v011_signal(cashneq, debt):
    X = _f29_cov(cashneq, debt)
    j0 = _jerk(X, 63)
    b = np.sign(j0) * (j0.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashcovddvol_126d_jerk_v012_signal(cashneq, debt):
    X = _f29_cov(cashneq, debt)
    j0 = _jerk(X, 63)
    b = j0 / _std(_roc(X, 63), 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashdebtrankdd_252d_jerk_v013_signal(cashneq, debt):
    X = _rank(_f29_cov(cashneq, debt), 252)
    b = _jerk(X, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashdebtrankdddev_252d_jerk_v014_signal(cashneq, debt):
    X = _rank(_f29_cov(cashneq, debt), 252)
    j0 = _jerk(X, 63)
    b = j0 - _mean(j0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashdebtrankddema_252d_jerk_v015_signal(cashneq, debt):
    X = _rank(_f29_cov(cashneq, debt), 252)
    b = _jerk(X, 63).ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashdebtrankddrank_252d_jerk_v016_signal(cashneq, debt):
    X = _rank(_f29_cov(cashneq, debt), 252)
    b = _rank(_jerk(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashdebtrankddvol_252d_jerk_v017_signal(cashneq, debt):
    X = _rank(_f29_cov(cashneq, debt), 252)
    j0 = _jerk(X, 63)
    b = j0 / _std(_roc(X, 63), 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashgrowdd_126d_jerk_v018_signal(cashneq):
    c = cashneq.clip(lower=1.0)
    X = np.log(c) - np.log(c.shift(126))
    b = _jerk(X, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashgrowdddev_126d_jerk_v019_signal(cashneq):
    c = cashneq.clip(lower=1.0)
    X = np.log(c) - np.log(c.shift(126))
    j0 = _jerk(X, 63)
    b = j0 - _mean(j0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashgrowddema_126d_jerk_v020_signal(cashneq):
    c = cashneq.clip(lower=1.0)
    X = np.log(c) - np.log(c.shift(126))
    b = _jerk(X, 63).ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashgrowddrank_126d_jerk_v021_signal(cashneq):
    c = cashneq.clip(lower=1.0)
    X = np.log(c) - np.log(c.shift(126))
    b = _rank(_jerk(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashgrowddvol_126d_jerk_v022_signal(cashneq):
    c = cashneq.clip(lower=1.0)
    X = np.log(c) - np.log(c.shift(126))
    j0 = _jerk(X, 63)
    b = j0 / _std(_roc(X, 63), 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashgrowdd_252d_jerk_v023_signal(cashneq):
    c = cashneq.clip(lower=1.0)
    X = np.log(c) - np.log(c.shift(252))
    b = _jerk(X, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashgrowdddev_252d_jerk_v024_signal(cashneq):
    c = cashneq.clip(lower=1.0)
    X = np.log(c) - np.log(c.shift(252))
    j0 = _jerk(X, 63)
    b = j0 - _mean(j0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashgrowddema_252d_jerk_v025_signal(cashneq):
    c = cashneq.clip(lower=1.0)
    X = np.log(c) - np.log(c.shift(252))
    b = _jerk(X, 63).ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashgrowddrank_252d_jerk_v026_signal(cashneq):
    c = cashneq.clip(lower=1.0)
    X = np.log(c) - np.log(c.shift(252))
    b = _rank(_jerk(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashgrowddvol_252d_jerk_v027_signal(cashneq):
    c = cashneq.clip(lower=1.0)
    X = np.log(c) - np.log(c.shift(252))
    j0 = _jerk(X, 63)
    b = j0 / _std(_roc(X, 63), 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_compgapdd_126d_jerk_v028_signal(debtc, debtnc, debt):
    X = (debtc + debtnc - debt) / debt.replace(0, np.nan)
    b = _jerk(X, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_compgapdddev_126d_jerk_v029_signal(debtc, debtnc, debt):
    X = (debtc + debtnc - debt) / debt.replace(0, np.nan)
    j0 = _jerk(X, 63)
    b = j0 - _mean(j0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_compgapddema_126d_jerk_v030_signal(debtc, debtnc, debt):
    X = (debtc + debtnc - debt) / debt.replace(0, np.nan)
    b = _jerk(X, 63).ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_compgapddrank_126d_jerk_v031_signal(debtc, debtnc, debt):
    X = (debtc + debtnc - debt) / debt.replace(0, np.nan)
    b = _rank(_jerk(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_compgapddvol_126d_jerk_v032_signal(debtc, debtnc, debt):
    X = (debtc + debtnc - debt) / debt.replace(0, np.nan)
    j0 = _jerk(X, 63)
    b = j0 / _std(_roc(X, 63), 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_covzdd_252d_jerk_v033_signal(cashneq, debt):
    X = _z(_f29_cov(cashneq, debt), 252)
    b = _jerk(X, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_covzdddev_252d_jerk_v034_signal(cashneq, debt):
    X = _z(_f29_cov(cashneq, debt), 252)
    j0 = _jerk(X, 63)
    b = j0 - _mean(j0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_covzddema_252d_jerk_v035_signal(cashneq, debt):
    X = _z(_f29_cov(cashneq, debt), 252)
    b = _jerk(X, 63).ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_covzddrank_252d_jerk_v036_signal(cashneq, debt):
    X = _z(_f29_cov(cashneq, debt), 252)
    b = _rank(_jerk(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_covzddvol_252d_jerk_v037_signal(cashneq, debt):
    X = _z(_f29_cov(cashneq, debt), 252)
    j0 = _jerk(X, 63)
    b = j0 / _std(_roc(X, 63), 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_debtcvdd_252d_jerk_v038_signal(debt):
    X = _std(debt, 252) / _mean(debt, 252).replace(0, np.nan)
    b = _jerk(X, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_debtcvdddev_252d_jerk_v039_signal(debt):
    X = _std(debt, 252) / _mean(debt, 252).replace(0, np.nan)
    j0 = _jerk(X, 63)
    b = j0 - _mean(j0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_debtcvddema_252d_jerk_v040_signal(debt):
    X = _std(debt, 252) / _mean(debt, 252).replace(0, np.nan)
    b = _jerk(X, 63).ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_debtcvddrank_252d_jerk_v041_signal(debt):
    X = _std(debt, 252) / _mean(debt, 252).replace(0, np.nan)
    b = _rank(_jerk(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_debtcvddvol_252d_jerk_v042_signal(debt):
    X = _std(debt, 252) / _mean(debt, 252).replace(0, np.nan)
    j0 = _jerk(X, 63)
    b = j0 / _std(_roc(X, 63), 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowdd_63d_jerk_v043_signal(debt):
    X = _f29_growth(debt, 63)
    b = _jerk(X, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowdddev_63d_jerk_v044_signal(debt):
    X = _f29_growth(debt, 63)
    j0 = _jerk(X, 21)
    b = j0 - _mean(j0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowddema_63d_jerk_v045_signal(debt):
    X = _f29_growth(debt, 63)
    b = _jerk(X, 21).ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowddrank_63d_jerk_v046_signal(debt):
    X = _f29_growth(debt, 63)
    b = _rank(_jerk(X, 21), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowddsgnmag_63d_jerk_v047_signal(debt):
    X = _f29_growth(debt, 63)
    j0 = _jerk(X, 21)
    b = np.sign(j0) * (j0.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowddtanh_63d_jerk_v048_signal(debt):
    X = _f29_growth(debt, 63)
    b = np.tanh(2.0 * _z(_jerk(X, 21), 63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowddvol_63d_jerk_v049_signal(debt):
    X = _f29_growth(debt, 63)
    j0 = _jerk(X, 21)
    b = j0 / _std(_roc(X, 21), 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowddz_63d_jerk_v050_signal(debt):
    X = _f29_growth(debt, 63)
    b = _z(_jerk(X, 21), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowdd_126d_jerk_v051_signal(debt):
    X = _f29_growth(debt, 126)
    b = _jerk(X, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowdddev_126d_jerk_v052_signal(debt):
    X = _f29_growth(debt, 126)
    j0 = _jerk(X, 63)
    b = j0 - _mean(j0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowddema_126d_jerk_v053_signal(debt):
    X = _f29_growth(debt, 126)
    b = _jerk(X, 63).ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowddrank_126d_jerk_v054_signal(debt):
    X = _f29_growth(debt, 126)
    b = _rank(_jerk(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowddvol_126d_jerk_v055_signal(debt):
    X = _f29_growth(debt, 126)
    j0 = _jerk(X, 63)
    b = j0 / _std(_roc(X, 63), 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowdd_252d_jerk_v056_signal(debt):
    X = _f29_growth(debt, 252)
    b = _jerk(X, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowdddev_252d_jerk_v057_signal(debt):
    X = _f29_growth(debt, 252)
    j0 = _jerk(X, 63)
    b = j0 - _mean(j0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowddema_252d_jerk_v058_signal(debt):
    X = _f29_growth(debt, 252)
    b = _jerk(X, 63).ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowddrank_252d_jerk_v059_signal(debt):
    X = _f29_growth(debt, 252)
    b = _rank(_jerk(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowddvol_252d_jerk_v060_signal(debt):
    X = _f29_growth(debt, 252)
    j0 = _jerk(X, 63)
    b = j0 / _std(_roc(X, 63), 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowdd_504d_jerk_v061_signal(debt):
    X = _f29_growth(debt, 504)
    b = _jerk(X, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowdddev_504d_jerk_v062_signal(debt):
    X = _f29_growth(debt, 504)
    j0 = _jerk(X, 126)
    b = j0 - _mean(j0, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowddema_504d_jerk_v063_signal(debt):
    X = _f29_growth(debt, 504)
    b = _jerk(X, 126).ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowddrank_504d_jerk_v064_signal(debt):
    X = _f29_growth(debt, 504)
    b = _rank(_jerk(X, 126), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowddvol_504d_jerk_v065_signal(debt):
    X = _f29_growth(debt, 504)
    j0 = _jerk(X, 126)
    b = j0 / _std(_roc(X, 126), 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowzdd_252d_jerk_v066_signal(debt):
    X = _z(_f29_growth(debt, 252), 252)
    b = _jerk(X, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowzdddev_252d_jerk_v067_signal(debt):
    X = _z(_f29_growth(debt, 252), 252)
    j0 = _jerk(X, 63)
    b = j0 - _mean(j0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowzddema_252d_jerk_v068_signal(debt):
    X = _z(_f29_growth(debt, 252), 252)
    b = _jerk(X, 63).ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowzddrank_252d_jerk_v069_signal(debt):
    X = _z(_f29_growth(debt, 252), 252)
    b = _rank(_jerk(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowzddvol_252d_jerk_v070_signal(debt):
    X = _z(_f29_growth(debt, 252), 252)
    j0 = _jerk(X, 63)
    b = j0 / _std(_roc(X, 63), 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dpctddrank_63d_jerk_v071_signal(debt):
    X = _f29_pctchg(debt, 63)
    b = _rank(_jerk(X, 21), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dusdextenddd_252d_jerk_v072_signal(debtusd):
    mn = _mean(debtusd, 252)
    X = (debtusd - mn) / mn.replace(0, np.nan)
    b = _jerk(X, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dusdextenddddev_252d_jerk_v073_signal(debtusd):
    mn = _mean(debtusd, 252)
    X = (debtusd - mn) / mn.replace(0, np.nan)
    j0 = _jerk(X, 63)
    b = j0 - _mean(j0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dusdextendddema_252d_jerk_v074_signal(debtusd):
    mn = _mean(debtusd, 252)
    X = (debtusd - mn) / mn.replace(0, np.nan)
    b = _jerk(X, 63).ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dusdextendddrank_252d_jerk_v075_signal(debtusd):
    mn = _mean(debtusd, 252)
    X = (debtusd - mn) / mn.replace(0, np.nan)
    b = _rank(_jerk(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dusdextendddvol_252d_jerk_v076_signal(debtusd):
    mn = _mean(debtusd, 252)
    X = (debtusd - mn) / mn.replace(0, np.nan)
    j0 = _jerk(X, 63)
    b = j0 / _std(_roc(X, 63), 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dusdgrowdd_63d_jerk_v077_signal(debtusd):
    X = _f29_growth(debtusd, 63)
    b = _jerk(X, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dusdgrowdddev_63d_jerk_v078_signal(debtusd):
    X = _f29_growth(debtusd, 63)
    j0 = _jerk(X, 21)
    b = j0 - _mean(j0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dusdgrowddema_63d_jerk_v079_signal(debtusd):
    X = _f29_growth(debtusd, 63)
    b = _jerk(X, 21).ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dusdgrowddrank_63d_jerk_v080_signal(debtusd):
    X = _f29_growth(debtusd, 63)
    b = _rank(_jerk(X, 21), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dusdgrowddtanh_63d_jerk_v081_signal(debtusd):
    X = _f29_growth(debtusd, 63)
    b = np.tanh(2.0 * _z(_jerk(X, 21), 63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dusdgrowddvol_63d_jerk_v082_signal(debtusd):
    X = _f29_growth(debtusd, 63)
    j0 = _jerk(X, 21)
    b = j0 / _std(_roc(X, 21), 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dusdgrowdd_252d_jerk_v083_signal(debtusd):
    X = _f29_growth(debtusd, 252)
    b = _jerk(X, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dusdgrowdddev_252d_jerk_v084_signal(debtusd):
    X = _f29_growth(debtusd, 252)
    j0 = _jerk(X, 63)
    b = j0 - _mean(j0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dusdgrowddema_252d_jerk_v085_signal(debtusd):
    X = _f29_growth(debtusd, 252)
    b = _jerk(X, 63).ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dusdgrowddrank_252d_jerk_v086_signal(debtusd):
    X = _f29_growth(debtusd, 252)
    b = _rank(_jerk(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dusdgrowddvol_252d_jerk_v087_signal(debtusd):
    X = _f29_growth(debtusd, 252)
    j0 = _jerk(X, 63)
    b = j0 / _std(_roc(X, 63), 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_emadispdd_126d_jerk_v088_signal(debt):
    e = debt.ewm(span=126, min_periods=31).mean()
    X = debt / e.replace(0, np.nan) - 1.0
    b = _jerk(X, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_emadispdddev_126d_jerk_v089_signal(debt):
    e = debt.ewm(span=126, min_periods=31).mean()
    X = debt / e.replace(0, np.nan) - 1.0
    j0 = _jerk(X, 63)
    b = j0 - _mean(j0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_emadispddema_126d_jerk_v090_signal(debt):
    e = debt.ewm(span=126, min_periods=31).mean()
    X = debt / e.replace(0, np.nan) - 1.0
    b = _jerk(X, 63).ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_emadispddrank_126d_jerk_v091_signal(debt):
    e = debt.ewm(span=126, min_periods=31).mean()
    X = debt / e.replace(0, np.nan) - 1.0
    b = _rank(_jerk(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_emadispddvol_126d_jerk_v092_signal(debt):
    e = debt.ewm(span=126, min_periods=31).mean()
    X = debt / e.replace(0, np.nan) - 1.0
    j0 = _jerk(X, 63)
    b = j0 / _std(_roc(X, 63), 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_emadispddsgnmag_252d_jerk_v093_signal(debt):
    e = debt.ewm(span=252, min_periods=63).mean()
    X = debt / e.replace(0, np.nan) - 1.0
    j0 = _jerk(X, 63)
    b = np.sign(j0) * (j0.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_emadispddtanh_252d_jerk_v094_signal(debt):
    e = debt.ewm(span=252, min_periods=63).mean()
    X = debt / e.replace(0, np.nan) - 1.0
    b = np.tanh(2.0 * _z(_jerk(X, 63), 63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_emadispddvol_252d_jerk_v095_signal(debt):
    e = debt.ewm(span=252, min_periods=63).mean()
    X = debt / e.replace(0, np.nan) - 1.0
    j0 = _jerk(X, 63)
    b = j0 / _std(_roc(X, 63), 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_extenddddev_252d_jerk_v096_signal(debt):
    mn = _mean(debt, 252)
    X = (debt - mn) / mn.replace(0, np.nan)
    j0 = _jerk(X, 63)
    b = j0 - _mean(j0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_extendddema_252d_jerk_v097_signal(debt):
    mn = _mean(debt, 252)
    X = (debt - mn) / mn.replace(0, np.nan)
    b = _jerk(X, 63).ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_extendddtanh_252d_jerk_v098_signal(debt):
    mn = _mean(debt, 252)
    X = (debt - mn) / mn.replace(0, np.nan)
    b = np.tanh(2.0 * _z(_jerk(X, 63), 63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_extendddvol_252d_jerk_v099_signal(debt):
    mn = _mean(debt, 252)
    X = (debt - mn) / mn.replace(0, np.nan)
    j0 = _jerk(X, 63)
    b = j0 / _std(_roc(X, 63), 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_extendddz_252d_jerk_v100_signal(debt):
    mn = _mean(debt, 252)
    X = (debt - mn) / mn.replace(0, np.nan)
    b = _z(_jerk(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_growsnrdd_252d_jerk_v101_signal(debt):
    g = _f29_growth(debt, 252)
    vol = _std(_f29_growth(debt, 21), 252)
    X = g / vol.replace(0, np.nan)
    b = _jerk(X, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_growsnrdddev_252d_jerk_v102_signal(debt):
    g = _f29_growth(debt, 252)
    vol = _std(_f29_growth(debt, 21), 252)
    X = g / vol.replace(0, np.nan)
    j0 = _jerk(X, 63)
    b = j0 - _mean(j0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_growsnrddema_252d_jerk_v103_signal(debt):
    g = _f29_growth(debt, 252)
    vol = _std(_f29_growth(debt, 21), 252)
    X = g / vol.replace(0, np.nan)
    b = _jerk(X, 63).ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_growsnrddrank_252d_jerk_v104_signal(debt):
    g = _f29_growth(debt, 252)
    vol = _std(_f29_growth(debt, 21), 252)
    X = g / vol.replace(0, np.nan)
    b = _rank(_jerk(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_growsnrddsgnmag_252d_jerk_v105_signal(debt):
    g = _f29_growth(debt, 252)
    vol = _std(_f29_growth(debt, 21), 252)
    X = g / vol.replace(0, np.nan)
    j0 = _jerk(X, 63)
    b = np.sign(j0) * (j0.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_growsnrddvol_252d_jerk_v106_signal(debt):
    g = _f29_growth(debt, 252)
    vol = _std(_f29_growth(debt, 21), 252)
    X = g / vol.replace(0, np.nan)
    j0 = _jerk(X, 63)
    b = j0 / _std(_roc(X, 63), 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ltcratiodd_252d_jerk_v107_signal(debtnc, debtc):
    X = np.log((debtnc / debtc.replace(0, np.nan)).replace(0, np.nan))
    b = _jerk(X, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ltcratiodddev_252d_jerk_v108_signal(debtnc, debtc):
    X = np.log((debtnc / debtc.replace(0, np.nan)).replace(0, np.nan))
    j0 = _jerk(X, 63)
    b = j0 - _mean(j0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ltcratioddema_252d_jerk_v109_signal(debtnc, debtc):
    X = np.log((debtnc / debtc.replace(0, np.nan)).replace(0, np.nan))
    b = _jerk(X, 63).ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ltcratioddrank_252d_jerk_v110_signal(debtnc, debtc):
    X = np.log((debtnc / debtc.replace(0, np.nan)).replace(0, np.nan))
    b = _rank(_jerk(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ltcratioddtanh_252d_jerk_v111_signal(debtnc, debtc):
    X = np.log((debtnc / debtc.replace(0, np.nan)).replace(0, np.nan))
    b = np.tanh(2.0 * _z(_jerk(X, 63), 63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ltcratioddvol_252d_jerk_v112_signal(debtnc, debtc):
    X = np.log((debtnc / debtc.replace(0, np.nan)).replace(0, np.nan))
    j0 = _jerk(X, 63)
    b = j0 / _std(_roc(X, 63), 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ltgrowdd_126d_jerk_v113_signal(debtnc):
    X = _f29_growth(debtnc, 126)
    b = _jerk(X, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ltgrowdddev_126d_jerk_v114_signal(debtnc):
    X = _f29_growth(debtnc, 126)
    j0 = _jerk(X, 63)
    b = j0 - _mean(j0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ltgrowddema_126d_jerk_v115_signal(debtnc):
    X = _f29_growth(debtnc, 126)
    b = _jerk(X, 63).ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ltgrowddrank_126d_jerk_v116_signal(debtnc):
    X = _f29_growth(debtnc, 126)
    b = _rank(_jerk(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ltgrowddtanh_126d_jerk_v117_signal(debtnc):
    X = _f29_growth(debtnc, 126)
    b = np.tanh(2.0 * _z(_jerk(X, 63), 63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ltgrowddvol_126d_jerk_v118_signal(debtnc):
    X = _f29_growth(debtnc, 126)
    j0 = _jerk(X, 63)
    b = j0 / _std(_roc(X, 63), 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ltgrowddz_126d_jerk_v119_signal(debtnc):
    X = _f29_growth(debtnc, 126)
    b = _z(_jerk(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ltgrowdd_252d_jerk_v120_signal(debtnc):
    X = _f29_growth(debtnc, 252)
    b = _jerk(X, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ltgrowdddev_252d_jerk_v121_signal(debtnc):
    X = _f29_growth(debtnc, 252)
    j0 = _jerk(X, 63)
    b = j0 - _mean(j0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ltgrowddema_252d_jerk_v122_signal(debtnc):
    X = _f29_growth(debtnc, 252)
    b = _jerk(X, 63).ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ltgrowddrank_252d_jerk_v123_signal(debtnc):
    X = _f29_growth(debtnc, 252)
    b = _rank(_jerk(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ltgrowddvol_252d_jerk_v124_signal(debtnc):
    X = _f29_growth(debtnc, 252)
    j0 = _jerk(X, 63)
    b = j0 / _std(_roc(X, 63), 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ltshareddrank_252d_jerk_v125_signal(debtnc, debt):
    X = _f29_lt_share(debtnc, debt)
    b = _rank(_jerk(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ltshareddsgnmag_252d_jerk_v126_signal(debtnc, debt):
    X = _f29_lt_share(debtnc, debt)
    j0 = _jerk(X, 63)
    b = np.sign(j0) * (j0.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ltshareddvol_252d_jerk_v127_signal(debtnc, debt):
    X = _f29_lt_share(debtnc, debt)
    j0 = _jerk(X, 63)
    b = j0 / _std(_roc(X, 63), 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_maturitymixdd_252d_jerk_v128_signal(debtc, debt):
    sh = _f29_st_share(debtc, debt)
    X = 0.5 - (sh - 0.5).abs()
    b = _jerk(X, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_maturitymixdddev_252d_jerk_v129_signal(debtc, debt):
    sh = _f29_st_share(debtc, debt)
    X = 0.5 - (sh - 0.5).abs()
    j0 = _jerk(X, 63)
    b = j0 - _mean(j0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_maturitymixddema_252d_jerk_v130_signal(debtc, debt):
    sh = _f29_st_share(debtc, debt)
    X = 0.5 - (sh - 0.5).abs()
    b = _jerk(X, 63).ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_maturitymixddrank_252d_jerk_v131_signal(debtc, debt):
    sh = _f29_st_share(debtc, debt)
    X = 0.5 - (sh - 0.5).abs()
    b = _rank(_jerk(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_maturitymixddvol_252d_jerk_v132_signal(debtc, debt):
    sh = _f29_st_share(debtc, debt)
    X = 0.5 - (sh - 0.5).abs()
    j0 = _jerk(X, 63)
    b = j0 / _std(_roc(X, 63), 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ncfcumdd_252d_jerk_v133_signal(ncfdebt, debt):
    X = ncfdebt.rolling(252, min_periods=126).sum() / debt.replace(0, np.nan)
    b = _jerk(X, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ncfcumdddev_252d_jerk_v134_signal(ncfdebt, debt):
    X = ncfdebt.rolling(252, min_periods=126).sum() / debt.replace(0, np.nan)
    j0 = _jerk(X, 63)
    b = j0 - _mean(j0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ncfcumddema_252d_jerk_v135_signal(ncfdebt, debt):
    X = ncfdebt.rolling(252, min_periods=126).sum() / debt.replace(0, np.nan)
    b = _jerk(X, 63).ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ncfcumddrank_252d_jerk_v136_signal(ncfdebt, debt):
    X = ncfdebt.rolling(252, min_periods=126).sum() / debt.replace(0, np.nan)
    b = _rank(_jerk(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ncfcumddvol_252d_jerk_v137_signal(ncfdebt, debt):
    X = ncfdebt.rolling(252, min_periods=126).sum() / debt.replace(0, np.nan)
    j0 = _jerk(X, 63)
    b = j0 / _std(_roc(X, 63), 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ncfcumdd_504d_jerk_v138_signal(ncfdebt, debt):
    X = ncfdebt.rolling(504, min_periods=252).sum() / debt.replace(0, np.nan)
    b = _jerk(X, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ncfcumdddev_504d_jerk_v139_signal(ncfdebt, debt):
    X = ncfdebt.rolling(504, min_periods=252).sum() / debt.replace(0, np.nan)
    j0 = _jerk(X, 126)
    b = j0 - _mean(j0, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ncfcumddema_504d_jerk_v140_signal(ncfdebt, debt):
    X = ncfdebt.rolling(504, min_periods=252).sum() / debt.replace(0, np.nan)
    b = _jerk(X, 126).ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ncfcumddrank_504d_jerk_v141_signal(ncfdebt, debt):
    X = ncfdebt.rolling(504, min_periods=252).sum() / debt.replace(0, np.nan)
    b = _rank(_jerk(X, 126), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ncfcumddvol_504d_jerk_v142_signal(ncfdebt, debt):
    X = ncfdebt.rolling(504, min_periods=252).sum() / debt.replace(0, np.nan)
    j0 = _jerk(X, 126)
    b = j0 / _std(_roc(X, 126), 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ncfflowdd_63d_jerk_v143_signal(ncfdebt, debt):
    X = _mean(ncfdebt, 63) / debt.replace(0, np.nan)
    b = _jerk(X, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ncfflowdddev_63d_jerk_v144_signal(ncfdebt, debt):
    X = _mean(ncfdebt, 63) / debt.replace(0, np.nan)
    j0 = _jerk(X, 21)
    b = j0 - _mean(j0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ncfflowddema_63d_jerk_v145_signal(ncfdebt, debt):
    X = _mean(ncfdebt, 63) / debt.replace(0, np.nan)
    b = _jerk(X, 21).ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ncfflowddrank_63d_jerk_v146_signal(ncfdebt, debt):
    X = _mean(ncfdebt, 63) / debt.replace(0, np.nan)
    b = _rank(_jerk(X, 21), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ncfflowddtanh_63d_jerk_v147_signal(ncfdebt, debt):
    X = _mean(ncfdebt, 63) / debt.replace(0, np.nan)
    b = np.tanh(2.0 * _z(_jerk(X, 21), 63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ncfflowddvol_63d_jerk_v148_signal(ncfdebt, debt):
    X = _mean(ncfdebt, 63) / debt.replace(0, np.nan)
    j0 = _jerk(X, 21)
    b = j0 / _std(_roc(X, 21), 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ncfflowddz_63d_jerk_v149_signal(ncfdebt, debt):
    X = _mean(ncfdebt, 63) / debt.replace(0, np.nan)
    b = _z(_jerk(X, 21), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ncfflowdd_126d_jerk_v150_signal(ncfdebt, debt):
    X = _mean(ncfdebt, 126) / debt.replace(0, np.nan)
    b = _jerk(X, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f29dt_f29_debt_trajectory_buildvsmeddd_504d_jerk_v001_signal,
    f29dt_f29_debt_trajectory_buildvsmeddddev_504d_jerk_v002_signal,
    f29dt_f29_debt_trajectory_buildvsmedddema_504d_jerk_v003_signal,
    f29dt_f29_debt_trajectory_buildvsmedddrank_504d_jerk_v004_signal,
    f29dt_f29_debt_trajectory_buildvsmedddtanh_504d_jerk_v005_signal,
    f29dt_f29_debt_trajectory_buildvsmedddvol_504d_jerk_v006_signal,
    f29dt_f29_debt_trajectory_cashcovdd_126d_jerk_v007_signal,
    f29dt_f29_debt_trajectory_cashcovdddev_126d_jerk_v008_signal,
    f29dt_f29_debt_trajectory_cashcovddema_126d_jerk_v009_signal,
    f29dt_f29_debt_trajectory_cashcovddrank_126d_jerk_v010_signal,
    f29dt_f29_debt_trajectory_cashcovddsgnmag_126d_jerk_v011_signal,
    f29dt_f29_debt_trajectory_cashcovddvol_126d_jerk_v012_signal,
    f29dt_f29_debt_trajectory_cashdebtrankdd_252d_jerk_v013_signal,
    f29dt_f29_debt_trajectory_cashdebtrankdddev_252d_jerk_v014_signal,
    f29dt_f29_debt_trajectory_cashdebtrankddema_252d_jerk_v015_signal,
    f29dt_f29_debt_trajectory_cashdebtrankddrank_252d_jerk_v016_signal,
    f29dt_f29_debt_trajectory_cashdebtrankddvol_252d_jerk_v017_signal,
    f29dt_f29_debt_trajectory_cashgrowdd_126d_jerk_v018_signal,
    f29dt_f29_debt_trajectory_cashgrowdddev_126d_jerk_v019_signal,
    f29dt_f29_debt_trajectory_cashgrowddema_126d_jerk_v020_signal,
    f29dt_f29_debt_trajectory_cashgrowddrank_126d_jerk_v021_signal,
    f29dt_f29_debt_trajectory_cashgrowddvol_126d_jerk_v022_signal,
    f29dt_f29_debt_trajectory_cashgrowdd_252d_jerk_v023_signal,
    f29dt_f29_debt_trajectory_cashgrowdddev_252d_jerk_v024_signal,
    f29dt_f29_debt_trajectory_cashgrowddema_252d_jerk_v025_signal,
    f29dt_f29_debt_trajectory_cashgrowddrank_252d_jerk_v026_signal,
    f29dt_f29_debt_trajectory_cashgrowddvol_252d_jerk_v027_signal,
    f29dt_f29_debt_trajectory_compgapdd_126d_jerk_v028_signal,
    f29dt_f29_debt_trajectory_compgapdddev_126d_jerk_v029_signal,
    f29dt_f29_debt_trajectory_compgapddema_126d_jerk_v030_signal,
    f29dt_f29_debt_trajectory_compgapddrank_126d_jerk_v031_signal,
    f29dt_f29_debt_trajectory_compgapddvol_126d_jerk_v032_signal,
    f29dt_f29_debt_trajectory_covzdd_252d_jerk_v033_signal,
    f29dt_f29_debt_trajectory_covzdddev_252d_jerk_v034_signal,
    f29dt_f29_debt_trajectory_covzddema_252d_jerk_v035_signal,
    f29dt_f29_debt_trajectory_covzddrank_252d_jerk_v036_signal,
    f29dt_f29_debt_trajectory_covzddvol_252d_jerk_v037_signal,
    f29dt_f29_debt_trajectory_debtcvdd_252d_jerk_v038_signal,
    f29dt_f29_debt_trajectory_debtcvdddev_252d_jerk_v039_signal,
    f29dt_f29_debt_trajectory_debtcvddema_252d_jerk_v040_signal,
    f29dt_f29_debt_trajectory_debtcvddrank_252d_jerk_v041_signal,
    f29dt_f29_debt_trajectory_debtcvddvol_252d_jerk_v042_signal,
    f29dt_f29_debt_trajectory_dgrowdd_63d_jerk_v043_signal,
    f29dt_f29_debt_trajectory_dgrowdddev_63d_jerk_v044_signal,
    f29dt_f29_debt_trajectory_dgrowddema_63d_jerk_v045_signal,
    f29dt_f29_debt_trajectory_dgrowddrank_63d_jerk_v046_signal,
    f29dt_f29_debt_trajectory_dgrowddsgnmag_63d_jerk_v047_signal,
    f29dt_f29_debt_trajectory_dgrowddtanh_63d_jerk_v048_signal,
    f29dt_f29_debt_trajectory_dgrowddvol_63d_jerk_v049_signal,
    f29dt_f29_debt_trajectory_dgrowddz_63d_jerk_v050_signal,
    f29dt_f29_debt_trajectory_dgrowdd_126d_jerk_v051_signal,
    f29dt_f29_debt_trajectory_dgrowdddev_126d_jerk_v052_signal,
    f29dt_f29_debt_trajectory_dgrowddema_126d_jerk_v053_signal,
    f29dt_f29_debt_trajectory_dgrowddrank_126d_jerk_v054_signal,
    f29dt_f29_debt_trajectory_dgrowddvol_126d_jerk_v055_signal,
    f29dt_f29_debt_trajectory_dgrowdd_252d_jerk_v056_signal,
    f29dt_f29_debt_trajectory_dgrowdddev_252d_jerk_v057_signal,
    f29dt_f29_debt_trajectory_dgrowddema_252d_jerk_v058_signal,
    f29dt_f29_debt_trajectory_dgrowddrank_252d_jerk_v059_signal,
    f29dt_f29_debt_trajectory_dgrowddvol_252d_jerk_v060_signal,
    f29dt_f29_debt_trajectory_dgrowdd_504d_jerk_v061_signal,
    f29dt_f29_debt_trajectory_dgrowdddev_504d_jerk_v062_signal,
    f29dt_f29_debt_trajectory_dgrowddema_504d_jerk_v063_signal,
    f29dt_f29_debt_trajectory_dgrowddrank_504d_jerk_v064_signal,
    f29dt_f29_debt_trajectory_dgrowddvol_504d_jerk_v065_signal,
    f29dt_f29_debt_trajectory_dgrowzdd_252d_jerk_v066_signal,
    f29dt_f29_debt_trajectory_dgrowzdddev_252d_jerk_v067_signal,
    f29dt_f29_debt_trajectory_dgrowzddema_252d_jerk_v068_signal,
    f29dt_f29_debt_trajectory_dgrowzddrank_252d_jerk_v069_signal,
    f29dt_f29_debt_trajectory_dgrowzddvol_252d_jerk_v070_signal,
    f29dt_f29_debt_trajectory_dpctddrank_63d_jerk_v071_signal,
    f29dt_f29_debt_trajectory_dusdextenddd_252d_jerk_v072_signal,
    f29dt_f29_debt_trajectory_dusdextenddddev_252d_jerk_v073_signal,
    f29dt_f29_debt_trajectory_dusdextendddema_252d_jerk_v074_signal,
    f29dt_f29_debt_trajectory_dusdextendddrank_252d_jerk_v075_signal,
    f29dt_f29_debt_trajectory_dusdextendddvol_252d_jerk_v076_signal,
    f29dt_f29_debt_trajectory_dusdgrowdd_63d_jerk_v077_signal,
    f29dt_f29_debt_trajectory_dusdgrowdddev_63d_jerk_v078_signal,
    f29dt_f29_debt_trajectory_dusdgrowddema_63d_jerk_v079_signal,
    f29dt_f29_debt_trajectory_dusdgrowddrank_63d_jerk_v080_signal,
    f29dt_f29_debt_trajectory_dusdgrowddtanh_63d_jerk_v081_signal,
    f29dt_f29_debt_trajectory_dusdgrowddvol_63d_jerk_v082_signal,
    f29dt_f29_debt_trajectory_dusdgrowdd_252d_jerk_v083_signal,
    f29dt_f29_debt_trajectory_dusdgrowdddev_252d_jerk_v084_signal,
    f29dt_f29_debt_trajectory_dusdgrowddema_252d_jerk_v085_signal,
    f29dt_f29_debt_trajectory_dusdgrowddrank_252d_jerk_v086_signal,
    f29dt_f29_debt_trajectory_dusdgrowddvol_252d_jerk_v087_signal,
    f29dt_f29_debt_trajectory_emadispdd_126d_jerk_v088_signal,
    f29dt_f29_debt_trajectory_emadispdddev_126d_jerk_v089_signal,
    f29dt_f29_debt_trajectory_emadispddema_126d_jerk_v090_signal,
    f29dt_f29_debt_trajectory_emadispddrank_126d_jerk_v091_signal,
    f29dt_f29_debt_trajectory_emadispddvol_126d_jerk_v092_signal,
    f29dt_f29_debt_trajectory_emadispddsgnmag_252d_jerk_v093_signal,
    f29dt_f29_debt_trajectory_emadispddtanh_252d_jerk_v094_signal,
    f29dt_f29_debt_trajectory_emadispddvol_252d_jerk_v095_signal,
    f29dt_f29_debt_trajectory_extenddddev_252d_jerk_v096_signal,
    f29dt_f29_debt_trajectory_extendddema_252d_jerk_v097_signal,
    f29dt_f29_debt_trajectory_extendddtanh_252d_jerk_v098_signal,
    f29dt_f29_debt_trajectory_extendddvol_252d_jerk_v099_signal,
    f29dt_f29_debt_trajectory_extendddz_252d_jerk_v100_signal,
    f29dt_f29_debt_trajectory_growsnrdd_252d_jerk_v101_signal,
    f29dt_f29_debt_trajectory_growsnrdddev_252d_jerk_v102_signal,
    f29dt_f29_debt_trajectory_growsnrddema_252d_jerk_v103_signal,
    f29dt_f29_debt_trajectory_growsnrddrank_252d_jerk_v104_signal,
    f29dt_f29_debt_trajectory_growsnrddsgnmag_252d_jerk_v105_signal,
    f29dt_f29_debt_trajectory_growsnrddvol_252d_jerk_v106_signal,
    f29dt_f29_debt_trajectory_ltcratiodd_252d_jerk_v107_signal,
    f29dt_f29_debt_trajectory_ltcratiodddev_252d_jerk_v108_signal,
    f29dt_f29_debt_trajectory_ltcratioddema_252d_jerk_v109_signal,
    f29dt_f29_debt_trajectory_ltcratioddrank_252d_jerk_v110_signal,
    f29dt_f29_debt_trajectory_ltcratioddtanh_252d_jerk_v111_signal,
    f29dt_f29_debt_trajectory_ltcratioddvol_252d_jerk_v112_signal,
    f29dt_f29_debt_trajectory_ltgrowdd_126d_jerk_v113_signal,
    f29dt_f29_debt_trajectory_ltgrowdddev_126d_jerk_v114_signal,
    f29dt_f29_debt_trajectory_ltgrowddema_126d_jerk_v115_signal,
    f29dt_f29_debt_trajectory_ltgrowddrank_126d_jerk_v116_signal,
    f29dt_f29_debt_trajectory_ltgrowddtanh_126d_jerk_v117_signal,
    f29dt_f29_debt_trajectory_ltgrowddvol_126d_jerk_v118_signal,
    f29dt_f29_debt_trajectory_ltgrowddz_126d_jerk_v119_signal,
    f29dt_f29_debt_trajectory_ltgrowdd_252d_jerk_v120_signal,
    f29dt_f29_debt_trajectory_ltgrowdddev_252d_jerk_v121_signal,
    f29dt_f29_debt_trajectory_ltgrowddema_252d_jerk_v122_signal,
    f29dt_f29_debt_trajectory_ltgrowddrank_252d_jerk_v123_signal,
    f29dt_f29_debt_trajectory_ltgrowddvol_252d_jerk_v124_signal,
    f29dt_f29_debt_trajectory_ltshareddrank_252d_jerk_v125_signal,
    f29dt_f29_debt_trajectory_ltshareddsgnmag_252d_jerk_v126_signal,
    f29dt_f29_debt_trajectory_ltshareddvol_252d_jerk_v127_signal,
    f29dt_f29_debt_trajectory_maturitymixdd_252d_jerk_v128_signal,
    f29dt_f29_debt_trajectory_maturitymixdddev_252d_jerk_v129_signal,
    f29dt_f29_debt_trajectory_maturitymixddema_252d_jerk_v130_signal,
    f29dt_f29_debt_trajectory_maturitymixddrank_252d_jerk_v131_signal,
    f29dt_f29_debt_trajectory_maturitymixddvol_252d_jerk_v132_signal,
    f29dt_f29_debt_trajectory_ncfcumdd_252d_jerk_v133_signal,
    f29dt_f29_debt_trajectory_ncfcumdddev_252d_jerk_v134_signal,
    f29dt_f29_debt_trajectory_ncfcumddema_252d_jerk_v135_signal,
    f29dt_f29_debt_trajectory_ncfcumddrank_252d_jerk_v136_signal,
    f29dt_f29_debt_trajectory_ncfcumddvol_252d_jerk_v137_signal,
    f29dt_f29_debt_trajectory_ncfcumdd_504d_jerk_v138_signal,
    f29dt_f29_debt_trajectory_ncfcumdddev_504d_jerk_v139_signal,
    f29dt_f29_debt_trajectory_ncfcumddema_504d_jerk_v140_signal,
    f29dt_f29_debt_trajectory_ncfcumddrank_504d_jerk_v141_signal,
    f29dt_f29_debt_trajectory_ncfcumddvol_504d_jerk_v142_signal,
    f29dt_f29_debt_trajectory_ncfflowdd_63d_jerk_v143_signal,
    f29dt_f29_debt_trajectory_ncfflowdddev_63d_jerk_v144_signal,
    f29dt_f29_debt_trajectory_ncfflowddema_63d_jerk_v145_signal,
    f29dt_f29_debt_trajectory_ncfflowddrank_63d_jerk_v146_signal,
    f29dt_f29_debt_trajectory_ncfflowddtanh_63d_jerk_v147_signal,
    f29dt_f29_debt_trajectory_ncfflowddvol_63d_jerk_v148_signal,
    f29dt_f29_debt_trajectory_ncfflowddz_63d_jerk_v149_signal,
    f29dt_f29_debt_trajectory_ncfflowdd_126d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F29_DEBT_TRAJECTORY_REGISTRY_001_150 = REGISTRY


def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False, n=1500):
    g = np.random.default_rng(seed)
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.3
    return pd.Series(s, name=None)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    debt = _fund(101, base=1.2e9, drift=0.015, vol=0.06).rename("debt")
    debtusd = _fund(102, base=1.2e9, drift=0.015, vol=0.06).rename("debtusd")
    debtc = _fund(103, base=3.0e8, drift=0.01, vol=0.08).rename("debtc")
    debtnc = _fund(104, base=9.0e8, drift=0.018, vol=0.05).rename("debtnc")
    cashneq = _fund(105, base=4.0e8, drift=0.02, vol=0.09).rename("cashneq")
    _dwalk = _fund(106, base=8.0e8, drift=0.0, vol=0.12, allow_neg=True)
    ncfdebt = _dwalk.diff().fillna(0.0)
    ncfdebt = ncfdebt + pd.Series(np.random.normal(0, 5e5, n), index=ncfdebt.index)
    ncfdebt = ncfdebt.rename("ncfdebt")

    cols = {"debt": debt, "debtusd": debtusd, "debtc": debtc,
            "debtnc": debtnc, "cashneq": cashneq, "ncfdebt": ncfdebt}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, "%s nunique=%d" % (name, q.nunique())
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

    print("OK f29_debt_trajectory_3rd_derivatives_001_150_claude: %d features pass" % n_features)
