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


def f29dt_f29_debt_trajectory_buildvsmedd_504d_slope_v001_signal(debt):
    med = debt.rolling(504, min_periods=252).median()
    X = debt / med.replace(0, np.nan) - 1.0
    b = _roc(X, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_buildvsmedddev_504d_slope_v002_signal(debt):
    med = debt.rolling(504, min_periods=252).median()
    X = debt / med.replace(0, np.nan) - 1.0
    r0 = _roc(X, 126)
    b = r0 - _mean(r0, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_buildvsmeddema_504d_slope_v003_signal(debt):
    med = debt.rolling(504, min_periods=252).median()
    X = debt / med.replace(0, np.nan) - 1.0
    b = _roc(X, 126).ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_buildvsmeddrank_504d_slope_v004_signal(debt):
    med = debt.rolling(504, min_periods=252).median()
    X = debt / med.replace(0, np.nan) - 1.0
    b = _rank(_roc(X, 126), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_buildvsmeddtanh_504d_slope_v005_signal(debt):
    med = debt.rolling(504, min_periods=252).median()
    X = debt / med.replace(0, np.nan) - 1.0
    b = np.tanh(2.0 * _z(_roc(X, 126), 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_buildvsmeddvol_504d_slope_v006_signal(debt):
    med = debt.rolling(504, min_periods=252).median()
    X = debt / med.replace(0, np.nan) - 1.0
    r0 = _roc(X, 126)
    b = r0 / _std(X, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_buildvsmeddz_504d_slope_v007_signal(debt):
    med = debt.rolling(504, min_periods=252).median()
    X = debt / med.replace(0, np.nan) - 1.0
    b = _z(_roc(X, 126), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashcovd_126d_slope_v008_signal(cashneq, debt):
    X = _f29_cov(cashneq, debt)
    b = _roc(X, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashcovddev_126d_slope_v009_signal(cashneq, debt):
    X = _f29_cov(cashneq, debt)
    r0 = _roc(X, 63)
    b = r0 - _mean(r0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashcovdema_126d_slope_v010_signal(cashneq, debt):
    X = _f29_cov(cashneq, debt)
    b = _roc(X, 63).ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashcovdrank_126d_slope_v011_signal(cashneq, debt):
    X = _f29_cov(cashneq, debt)
    b = _rank(_roc(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashcovdvol_126d_slope_v012_signal(cashneq, debt):
    X = _f29_cov(cashneq, debt)
    r0 = _roc(X, 63)
    b = r0 / _std(X, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashdebtrankd_252d_slope_v013_signal(cashneq, debt):
    X = _rank(_f29_cov(cashneq, debt), 252)
    b = _roc(X, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashdebtrankddev_252d_slope_v014_signal(cashneq, debt):
    X = _rank(_f29_cov(cashneq, debt), 252)
    r0 = _roc(X, 63)
    b = r0 - _mean(r0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashdebtrankdema_252d_slope_v015_signal(cashneq, debt):
    X = _rank(_f29_cov(cashneq, debt), 252)
    b = _roc(X, 63).ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashdebtrankdrank_252d_slope_v016_signal(cashneq, debt):
    X = _rank(_f29_cov(cashneq, debt), 252)
    b = _rank(_roc(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashdebtrankdvol_252d_slope_v017_signal(cashneq, debt):
    X = _rank(_f29_cov(cashneq, debt), 252)
    r0 = _roc(X, 63)
    b = r0 / _std(X, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashdebtrankdz_252d_slope_v018_signal(cashneq, debt):
    X = _rank(_f29_cov(cashneq, debt), 252)
    b = _z(_roc(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashgrowd_126d_slope_v019_signal(cashneq):
    c = cashneq.clip(lower=1.0)
    X = np.log(c) - np.log(c.shift(126))
    b = _roc(X, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashgrowddev_126d_slope_v020_signal(cashneq):
    c = cashneq.clip(lower=1.0)
    X = np.log(c) - np.log(c.shift(126))
    r0 = _roc(X, 63)
    b = r0 - _mean(r0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashgrowdema_126d_slope_v021_signal(cashneq):
    c = cashneq.clip(lower=1.0)
    X = np.log(c) - np.log(c.shift(126))
    b = _roc(X, 63).ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashgrowdrank_126d_slope_v022_signal(cashneq):
    c = cashneq.clip(lower=1.0)
    X = np.log(c) - np.log(c.shift(126))
    b = _rank(_roc(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashgrowdvol_126d_slope_v023_signal(cashneq):
    c = cashneq.clip(lower=1.0)
    X = np.log(c) - np.log(c.shift(126))
    r0 = _roc(X, 63)
    b = r0 / _std(X, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashgrowd_252d_slope_v024_signal(cashneq):
    c = cashneq.clip(lower=1.0)
    X = np.log(c) - np.log(c.shift(252))
    b = _roc(X, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashgrowddev_252d_slope_v025_signal(cashneq):
    c = cashneq.clip(lower=1.0)
    X = np.log(c) - np.log(c.shift(252))
    r0 = _roc(X, 63)
    b = r0 - _mean(r0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashgrowdema_252d_slope_v026_signal(cashneq):
    c = cashneq.clip(lower=1.0)
    X = np.log(c) - np.log(c.shift(252))
    b = _roc(X, 63).ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashgrowdrank_252d_slope_v027_signal(cashneq):
    c = cashneq.clip(lower=1.0)
    X = np.log(c) - np.log(c.shift(252))
    b = _rank(_roc(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_cashgrowdvol_252d_slope_v028_signal(cashneq):
    c = cashneq.clip(lower=1.0)
    X = np.log(c) - np.log(c.shift(252))
    r0 = _roc(X, 63)
    b = r0 / _std(X, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_compgapd_126d_slope_v029_signal(debtc, debtnc, debt):
    X = (debtc + debtnc - debt) / debt.replace(0, np.nan)
    b = _roc(X, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_compgapddev_126d_slope_v030_signal(debtc, debtnc, debt):
    X = (debtc + debtnc - debt) / debt.replace(0, np.nan)
    r0 = _roc(X, 63)
    b = r0 - _mean(r0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_compgapdema_126d_slope_v031_signal(debtc, debtnc, debt):
    X = (debtc + debtnc - debt) / debt.replace(0, np.nan)
    b = _roc(X, 63).ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_compgapdrank_126d_slope_v032_signal(debtc, debtnc, debt):
    X = (debtc + debtnc - debt) / debt.replace(0, np.nan)
    b = _rank(_roc(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_covzd_252d_slope_v033_signal(cashneq, debt):
    X = _z(_f29_cov(cashneq, debt), 252)
    b = _roc(X, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_covzddev_252d_slope_v034_signal(cashneq, debt):
    X = _z(_f29_cov(cashneq, debt), 252)
    r0 = _roc(X, 63)
    b = r0 - _mean(r0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_covzdema_252d_slope_v035_signal(cashneq, debt):
    X = _z(_f29_cov(cashneq, debt), 252)
    b = _roc(X, 63).ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_covzdrank_252d_slope_v036_signal(cashneq, debt):
    X = _z(_f29_cov(cashneq, debt), 252)
    b = _rank(_roc(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_covzdvol_252d_slope_v037_signal(cashneq, debt):
    X = _z(_f29_cov(cashneq, debt), 252)
    r0 = _roc(X, 63)
    b = r0 / _std(X, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_debtcashlrdrank_126d_slope_v038_signal(debt, cashneq):
    X = np.log(debt.replace(0, np.nan)) - np.log(cashneq.replace(0, np.nan))
    b = _rank(_roc(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_debtcvd_252d_slope_v039_signal(debt):
    X = _std(debt, 252) / _mean(debt, 252).replace(0, np.nan)
    b = _roc(X, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_debtcvddev_252d_slope_v040_signal(debt):
    X = _std(debt, 252) / _mean(debt, 252).replace(0, np.nan)
    r0 = _roc(X, 63)
    b = r0 - _mean(r0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_debtcvdema_252d_slope_v041_signal(debt):
    X = _std(debt, 252) / _mean(debt, 252).replace(0, np.nan)
    b = _roc(X, 63).ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_debtcvdrank_252d_slope_v042_signal(debt):
    X = _std(debt, 252) / _mean(debt, 252).replace(0, np.nan)
    b = _rank(_roc(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_debtcvdvol_252d_slope_v043_signal(debt):
    X = _std(debt, 252) / _mean(debt, 252).replace(0, np.nan)
    r0 = _roc(X, 63)
    b = r0 / _std(X, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowd_63d_slope_v044_signal(debt):
    X = _f29_growth(debt, 63)
    b = _roc(X, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowddev_63d_slope_v045_signal(debt):
    X = _f29_growth(debt, 63)
    r0 = _roc(X, 21)
    b = r0 - _mean(r0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowdema_63d_slope_v046_signal(debt):
    X = _f29_growth(debt, 63)
    b = _roc(X, 21).ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowdrank_63d_slope_v047_signal(debt):
    X = _f29_growth(debt, 63)
    b = _rank(_roc(X, 21), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowdtanh_63d_slope_v048_signal(debt):
    X = _f29_growth(debt, 63)
    b = np.tanh(2.0 * _z(_roc(X, 21), 63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowdvol_63d_slope_v049_signal(debt):
    X = _f29_growth(debt, 63)
    r0 = _roc(X, 21)
    b = r0 / _std(X, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowdz_63d_slope_v050_signal(debt):
    X = _f29_growth(debt, 63)
    b = _z(_roc(X, 21), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowd_126d_slope_v051_signal(debt):
    X = _f29_growth(debt, 126)
    b = _roc(X, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowddev_126d_slope_v052_signal(debt):
    X = _f29_growth(debt, 126)
    r0 = _roc(X, 63)
    b = r0 - _mean(r0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowdema_126d_slope_v053_signal(debt):
    X = _f29_growth(debt, 126)
    b = _roc(X, 63).ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowdrank_126d_slope_v054_signal(debt):
    X = _f29_growth(debt, 126)
    b = _rank(_roc(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowdvol_126d_slope_v055_signal(debt):
    X = _f29_growth(debt, 126)
    r0 = _roc(X, 63)
    b = r0 / _std(X, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowd_252d_slope_v056_signal(debt):
    X = _f29_growth(debt, 252)
    b = _roc(X, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowddev_252d_slope_v057_signal(debt):
    X = _f29_growth(debt, 252)
    r0 = _roc(X, 63)
    b = r0 - _mean(r0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowdema_252d_slope_v058_signal(debt):
    X = _f29_growth(debt, 252)
    b = _roc(X, 63).ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowdrank_252d_slope_v059_signal(debt):
    X = _f29_growth(debt, 252)
    b = _rank(_roc(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowdvol_252d_slope_v060_signal(debt):
    X = _f29_growth(debt, 252)
    r0 = _roc(X, 63)
    b = r0 / _std(X, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowd_504d_slope_v061_signal(debt):
    X = _f29_growth(debt, 504)
    b = _roc(X, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowddev_504d_slope_v062_signal(debt):
    X = _f29_growth(debt, 504)
    r0 = _roc(X, 126)
    b = r0 - _mean(r0, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowdema_504d_slope_v063_signal(debt):
    X = _f29_growth(debt, 504)
    b = _roc(X, 126).ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowdrank_504d_slope_v064_signal(debt):
    X = _f29_growth(debt, 504)
    b = _rank(_roc(X, 126), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowdtanh_504d_slope_v065_signal(debt):
    X = _f29_growth(debt, 504)
    b = np.tanh(2.0 * _z(_roc(X, 126), 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowdvol_504d_slope_v066_signal(debt):
    X = _f29_growth(debt, 504)
    r0 = _roc(X, 126)
    b = r0 / _std(X, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowzd_252d_slope_v067_signal(debt):
    X = _z(_f29_growth(debt, 252), 252)
    b = _roc(X, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowzddev_252d_slope_v068_signal(debt):
    X = _z(_f29_growth(debt, 252), 252)
    r0 = _roc(X, 63)
    b = r0 - _mean(r0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowzdema_252d_slope_v069_signal(debt):
    X = _z(_f29_growth(debt, 252), 252)
    b = _roc(X, 63).ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowzdrank_252d_slope_v070_signal(debt):
    X = _z(_f29_growth(debt, 252), 252)
    b = _rank(_roc(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dgrowzdvol_252d_slope_v071_signal(debt):
    X = _z(_f29_growth(debt, 252), 252)
    r0 = _roc(X, 63)
    b = r0 / _std(X, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dpctdrank_63d_slope_v072_signal(debt):
    X = _f29_pctchg(debt, 63)
    b = _rank(_roc(X, 21), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dusdextendd_252d_slope_v073_signal(debtusd):
    mn = _mean(debtusd, 252)
    X = (debtusd - mn) / mn.replace(0, np.nan)
    b = _roc(X, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dusdextendddev_252d_slope_v074_signal(debtusd):
    mn = _mean(debtusd, 252)
    X = (debtusd - mn) / mn.replace(0, np.nan)
    r0 = _roc(X, 63)
    b = r0 - _mean(r0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dusdextenddema_252d_slope_v075_signal(debtusd):
    mn = _mean(debtusd, 252)
    X = (debtusd - mn) / mn.replace(0, np.nan)
    b = _roc(X, 63).ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dusdextenddrank_252d_slope_v076_signal(debtusd):
    mn = _mean(debtusd, 252)
    X = (debtusd - mn) / mn.replace(0, np.nan)
    b = _rank(_roc(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dusdextenddvol_252d_slope_v077_signal(debtusd):
    mn = _mean(debtusd, 252)
    X = (debtusd - mn) / mn.replace(0, np.nan)
    r0 = _roc(X, 63)
    b = r0 / _std(X, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dusdgrowd_63d_slope_v078_signal(debtusd):
    X = _f29_growth(debtusd, 63)
    b = _roc(X, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dusdgrowddev_63d_slope_v079_signal(debtusd):
    X = _f29_growth(debtusd, 63)
    r0 = _roc(X, 21)
    b = r0 - _mean(r0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dusdgrowdrank_63d_slope_v080_signal(debtusd):
    X = _f29_growth(debtusd, 63)
    b = _rank(_roc(X, 21), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dusdgrowdtanh_63d_slope_v081_signal(debtusd):
    X = _f29_growth(debtusd, 63)
    b = np.tanh(2.0 * _z(_roc(X, 21), 63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dusdgrowdvol_63d_slope_v082_signal(debtusd):
    X = _f29_growth(debtusd, 63)
    r0 = _roc(X, 21)
    b = r0 / _std(X, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dusdgrowdz_63d_slope_v083_signal(debtusd):
    X = _f29_growth(debtusd, 63)
    b = _z(_roc(X, 21), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dusdgrowd_252d_slope_v084_signal(debtusd):
    X = _f29_growth(debtusd, 252)
    b = _roc(X, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dusdgrowddev_252d_slope_v085_signal(debtusd):
    X = _f29_growth(debtusd, 252)
    r0 = _roc(X, 63)
    b = r0 - _mean(r0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dusdgrowdema_252d_slope_v086_signal(debtusd):
    X = _f29_growth(debtusd, 252)
    b = _roc(X, 63).ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dusdgrowdrank_252d_slope_v087_signal(debtusd):
    X = _f29_growth(debtusd, 252)
    b = _rank(_roc(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_dusdgrowdvol_252d_slope_v088_signal(debtusd):
    X = _f29_growth(debtusd, 252)
    r0 = _roc(X, 63)
    b = r0 / _std(X, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_emadispd_126d_slope_v089_signal(debt):
    e = debt.ewm(span=126, min_periods=31).mean()
    X = debt / e.replace(0, np.nan) - 1.0
    b = _roc(X, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_emadispddev_126d_slope_v090_signal(debt):
    e = debt.ewm(span=126, min_periods=31).mean()
    X = debt / e.replace(0, np.nan) - 1.0
    r0 = _roc(X, 63)
    b = r0 - _mean(r0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_emadispdema_126d_slope_v091_signal(debt):
    e = debt.ewm(span=126, min_periods=31).mean()
    X = debt / e.replace(0, np.nan) - 1.0
    b = _roc(X, 63).ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_emadispdrank_126d_slope_v092_signal(debt):
    e = debt.ewm(span=126, min_periods=31).mean()
    X = debt / e.replace(0, np.nan) - 1.0
    b = _rank(_roc(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_emadispdvol_126d_slope_v093_signal(debt):
    e = debt.ewm(span=126, min_periods=31).mean()
    X = debt / e.replace(0, np.nan) - 1.0
    r0 = _roc(X, 63)
    b = r0 / _std(X, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_emadispdz_126d_slope_v094_signal(debt):
    e = debt.ewm(span=126, min_periods=31).mean()
    X = debt / e.replace(0, np.nan) - 1.0
    b = _z(_roc(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_emadispdema_252d_slope_v095_signal(debt):
    e = debt.ewm(span=252, min_periods=63).mean()
    X = debt / e.replace(0, np.nan) - 1.0
    b = _roc(X, 63).ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_emadispdsgnmag_252d_slope_v096_signal(debt):
    e = debt.ewm(span=252, min_periods=63).mean()
    X = debt / e.replace(0, np.nan) - 1.0
    r0 = _roc(X, 63)
    b = np.sign(r0) * (r0.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_emadispdtanh_252d_slope_v097_signal(debt):
    e = debt.ewm(span=252, min_periods=63).mean()
    X = debt / e.replace(0, np.nan) - 1.0
    b = np.tanh(2.0 * _z(_roc(X, 63), 63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_emadispdvol_252d_slope_v098_signal(debt):
    e = debt.ewm(span=252, min_periods=63).mean()
    X = debt / e.replace(0, np.nan) - 1.0
    r0 = _roc(X, 63)
    b = r0 / _std(X, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_emadispdz_252d_slope_v099_signal(debt):
    e = debt.ewm(span=252, min_periods=63).mean()
    X = debt / e.replace(0, np.nan) - 1.0
    b = _z(_roc(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_extenddrank_126d_slope_v100_signal(debt):
    mn = _mean(debt, 126)
    X = (debt - mn) / mn.replace(0, np.nan)
    b = _rank(_roc(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_extenddsgnmag_126d_slope_v101_signal(debt):
    mn = _mean(debt, 126)
    X = (debt - mn) / mn.replace(0, np.nan)
    r0 = _roc(X, 63)
    b = np.sign(r0) * (r0.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_extendd_252d_slope_v102_signal(debt):
    mn = _mean(debt, 252)
    X = (debt - mn) / mn.replace(0, np.nan)
    b = _roc(X, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_extenddrank_252d_slope_v103_signal(debt):
    mn = _mean(debt, 252)
    X = (debt - mn) / mn.replace(0, np.nan)
    b = _rank(_roc(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_extenddvol_252d_slope_v104_signal(debt):
    mn = _mean(debt, 252)
    X = (debt - mn) / mn.replace(0, np.nan)
    r0 = _roc(X, 63)
    b = r0 / _std(X, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_growsnrd_252d_slope_v105_signal(debt):
    g = _f29_growth(debt, 252)
    vol = _std(_f29_growth(debt, 21), 252)
    X = g / vol.replace(0, np.nan)
    b = _roc(X, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_growsnrddev_252d_slope_v106_signal(debt):
    g = _f29_growth(debt, 252)
    vol = _std(_f29_growth(debt, 21), 252)
    X = g / vol.replace(0, np.nan)
    r0 = _roc(X, 63)
    b = r0 - _mean(r0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_growsnrdema_252d_slope_v107_signal(debt):
    g = _f29_growth(debt, 252)
    vol = _std(_f29_growth(debt, 21), 252)
    X = g / vol.replace(0, np.nan)
    b = _roc(X, 63).ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_growsnrdsgnmag_252d_slope_v108_signal(debt):
    g = _f29_growth(debt, 252)
    vol = _std(_f29_growth(debt, 21), 252)
    X = g / vol.replace(0, np.nan)
    r0 = _roc(X, 63)
    b = np.sign(r0) * (r0.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_growsnrdtanh_252d_slope_v109_signal(debt):
    g = _f29_growth(debt, 252)
    vol = _std(_f29_growth(debt, 21), 252)
    X = g / vol.replace(0, np.nan)
    b = np.tanh(2.0 * _z(_roc(X, 63), 63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ltcratiod_252d_slope_v110_signal(debtnc, debtc):
    X = np.log((debtnc / debtc.replace(0, np.nan)).replace(0, np.nan))
    b = _roc(X, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ltcratioddev_252d_slope_v111_signal(debtnc, debtc):
    X = np.log((debtnc / debtc.replace(0, np.nan)).replace(0, np.nan))
    r0 = _roc(X, 63)
    b = r0 - _mean(r0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ltcratiodema_252d_slope_v112_signal(debtnc, debtc):
    X = np.log((debtnc / debtc.replace(0, np.nan)).replace(0, np.nan))
    b = _roc(X, 63).ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ltcratiodrank_252d_slope_v113_signal(debtnc, debtc):
    X = np.log((debtnc / debtc.replace(0, np.nan)).replace(0, np.nan))
    b = _rank(_roc(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ltcratiodvol_252d_slope_v114_signal(debtnc, debtc):
    X = np.log((debtnc / debtc.replace(0, np.nan)).replace(0, np.nan))
    r0 = _roc(X, 63)
    b = r0 / _std(X, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ltgrowd_126d_slope_v115_signal(debtnc):
    X = _f29_growth(debtnc, 126)
    b = _roc(X, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ltgrowddev_126d_slope_v116_signal(debtnc):
    X = _f29_growth(debtnc, 126)
    r0 = _roc(X, 63)
    b = r0 - _mean(r0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ltgrowdema_126d_slope_v117_signal(debtnc):
    X = _f29_growth(debtnc, 126)
    b = _roc(X, 63).ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ltgrowdrank_126d_slope_v118_signal(debtnc):
    X = _f29_growth(debtnc, 126)
    b = _rank(_roc(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ltgrowdvol_126d_slope_v119_signal(debtnc):
    X = _f29_growth(debtnc, 126)
    r0 = _roc(X, 63)
    b = r0 / _std(X, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ltgrowd_252d_slope_v120_signal(debtnc):
    X = _f29_growth(debtnc, 252)
    b = _roc(X, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ltgrowddev_252d_slope_v121_signal(debtnc):
    X = _f29_growth(debtnc, 252)
    r0 = _roc(X, 63)
    b = r0 - _mean(r0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ltgrowdema_252d_slope_v122_signal(debtnc):
    X = _f29_growth(debtnc, 252)
    b = _roc(X, 63).ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ltgrowdrank_252d_slope_v123_signal(debtnc):
    X = _f29_growth(debtnc, 252)
    b = _rank(_roc(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ltgrowdvol_252d_slope_v124_signal(debtnc):
    X = _f29_growth(debtnc, 252)
    r0 = _roc(X, 63)
    b = r0 / _std(X, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ltsharedrank_252d_slope_v125_signal(debtnc, debt):
    X = _f29_lt_share(debtnc, debt)
    b = _rank(_roc(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ltsharedtanh_252d_slope_v126_signal(debtnc, debt):
    X = _f29_lt_share(debtnc, debt)
    b = np.tanh(2.0 * _z(_roc(X, 63), 63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ltsharedz_252d_slope_v127_signal(debtnc, debt):
    X = _f29_lt_share(debtnc, debt)
    b = _z(_roc(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_maturitymixd_252d_slope_v128_signal(debtc, debt):
    sh = _f29_st_share(debtc, debt)
    X = 0.5 - (sh - 0.5).abs()
    b = _roc(X, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_maturitymixddev_252d_slope_v129_signal(debtc, debt):
    sh = _f29_st_share(debtc, debt)
    X = 0.5 - (sh - 0.5).abs()
    r0 = _roc(X, 63)
    b = r0 - _mean(r0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_maturitymixdema_252d_slope_v130_signal(debtc, debt):
    sh = _f29_st_share(debtc, debt)
    X = 0.5 - (sh - 0.5).abs()
    b = _roc(X, 63).ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_maturitymixdrank_252d_slope_v131_signal(debtc, debt):
    sh = _f29_st_share(debtc, debt)
    X = 0.5 - (sh - 0.5).abs()
    b = _rank(_roc(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_maturitymixdvol_252d_slope_v132_signal(debtc, debt):
    sh = _f29_st_share(debtc, debt)
    X = 0.5 - (sh - 0.5).abs()
    r0 = _roc(X, 63)
    b = r0 / _std(X, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ncfcumd_252d_slope_v133_signal(ncfdebt, debt):
    X = ncfdebt.rolling(252, min_periods=126).sum() / debt.replace(0, np.nan)
    b = _roc(X, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ncfcumddev_252d_slope_v134_signal(ncfdebt, debt):
    X = ncfdebt.rolling(252, min_periods=126).sum() / debt.replace(0, np.nan)
    r0 = _roc(X, 63)
    b = r0 - _mean(r0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ncfcumdema_252d_slope_v135_signal(ncfdebt, debt):
    X = ncfdebt.rolling(252, min_periods=126).sum() / debt.replace(0, np.nan)
    b = _roc(X, 63).ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ncfcumdrank_252d_slope_v136_signal(ncfdebt, debt):
    X = ncfdebt.rolling(252, min_periods=126).sum() / debt.replace(0, np.nan)
    b = _rank(_roc(X, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ncfcumdvol_252d_slope_v137_signal(ncfdebt, debt):
    X = ncfdebt.rolling(252, min_periods=126).sum() / debt.replace(0, np.nan)
    r0 = _roc(X, 63)
    b = r0 / _std(X, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ncfcumd_504d_slope_v138_signal(ncfdebt, debt):
    X = ncfdebt.rolling(504, min_periods=252).sum() / debt.replace(0, np.nan)
    b = _roc(X, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ncfcumddev_504d_slope_v139_signal(ncfdebt, debt):
    X = ncfdebt.rolling(504, min_periods=252).sum() / debt.replace(0, np.nan)
    r0 = _roc(X, 126)
    b = r0 - _mean(r0, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ncfcumdema_504d_slope_v140_signal(ncfdebt, debt):
    X = ncfdebt.rolling(504, min_periods=252).sum() / debt.replace(0, np.nan)
    b = _roc(X, 126).ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ncfcumdrank_504d_slope_v141_signal(ncfdebt, debt):
    X = ncfdebt.rolling(504, min_periods=252).sum() / debt.replace(0, np.nan)
    b = _rank(_roc(X, 126), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ncfcumdvol_504d_slope_v142_signal(ncfdebt, debt):
    X = ncfdebt.rolling(504, min_periods=252).sum() / debt.replace(0, np.nan)
    r0 = _roc(X, 126)
    b = r0 / _std(X, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ncfflowd_63d_slope_v143_signal(ncfdebt, debt):
    X = _mean(ncfdebt, 63) / debt.replace(0, np.nan)
    b = _roc(X, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ncfflowddev_63d_slope_v144_signal(ncfdebt, debt):
    X = _mean(ncfdebt, 63) / debt.replace(0, np.nan)
    r0 = _roc(X, 21)
    b = r0 - _mean(r0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ncfflowdema_63d_slope_v145_signal(ncfdebt, debt):
    X = _mean(ncfdebt, 63) / debt.replace(0, np.nan)
    b = _roc(X, 21).ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ncfflowdrank_63d_slope_v146_signal(ncfdebt, debt):
    X = _mean(ncfdebt, 63) / debt.replace(0, np.nan)
    b = _rank(_roc(X, 21), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ncfflowdtanh_63d_slope_v147_signal(ncfdebt, debt):
    X = _mean(ncfdebt, 63) / debt.replace(0, np.nan)
    b = np.tanh(2.0 * _z(_roc(X, 21), 63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ncfflowdvol_63d_slope_v148_signal(ncfdebt, debt):
    X = _mean(ncfdebt, 63) / debt.replace(0, np.nan)
    r0 = _roc(X, 21)
    b = r0 / _std(X, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ncfflowdz_63d_slope_v149_signal(ncfdebt, debt):
    X = _mean(ncfdebt, 63) / debt.replace(0, np.nan)
    b = _z(_roc(X, 21), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f29dt_f29_debt_trajectory_ncfflowd_126d_slope_v150_signal(ncfdebt, debt):
    X = _mean(ncfdebt, 126) / debt.replace(0, np.nan)
    b = _roc(X, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f29dt_f29_debt_trajectory_buildvsmedd_504d_slope_v001_signal,
    f29dt_f29_debt_trajectory_buildvsmedddev_504d_slope_v002_signal,
    f29dt_f29_debt_trajectory_buildvsmeddema_504d_slope_v003_signal,
    f29dt_f29_debt_trajectory_buildvsmeddrank_504d_slope_v004_signal,
    f29dt_f29_debt_trajectory_buildvsmeddtanh_504d_slope_v005_signal,
    f29dt_f29_debt_trajectory_buildvsmeddvol_504d_slope_v006_signal,
    f29dt_f29_debt_trajectory_buildvsmeddz_504d_slope_v007_signal,
    f29dt_f29_debt_trajectory_cashcovd_126d_slope_v008_signal,
    f29dt_f29_debt_trajectory_cashcovddev_126d_slope_v009_signal,
    f29dt_f29_debt_trajectory_cashcovdema_126d_slope_v010_signal,
    f29dt_f29_debt_trajectory_cashcovdrank_126d_slope_v011_signal,
    f29dt_f29_debt_trajectory_cashcovdvol_126d_slope_v012_signal,
    f29dt_f29_debt_trajectory_cashdebtrankd_252d_slope_v013_signal,
    f29dt_f29_debt_trajectory_cashdebtrankddev_252d_slope_v014_signal,
    f29dt_f29_debt_trajectory_cashdebtrankdema_252d_slope_v015_signal,
    f29dt_f29_debt_trajectory_cashdebtrankdrank_252d_slope_v016_signal,
    f29dt_f29_debt_trajectory_cashdebtrankdvol_252d_slope_v017_signal,
    f29dt_f29_debt_trajectory_cashdebtrankdz_252d_slope_v018_signal,
    f29dt_f29_debt_trajectory_cashgrowd_126d_slope_v019_signal,
    f29dt_f29_debt_trajectory_cashgrowddev_126d_slope_v020_signal,
    f29dt_f29_debt_trajectory_cashgrowdema_126d_slope_v021_signal,
    f29dt_f29_debt_trajectory_cashgrowdrank_126d_slope_v022_signal,
    f29dt_f29_debt_trajectory_cashgrowdvol_126d_slope_v023_signal,
    f29dt_f29_debt_trajectory_cashgrowd_252d_slope_v024_signal,
    f29dt_f29_debt_trajectory_cashgrowddev_252d_slope_v025_signal,
    f29dt_f29_debt_trajectory_cashgrowdema_252d_slope_v026_signal,
    f29dt_f29_debt_trajectory_cashgrowdrank_252d_slope_v027_signal,
    f29dt_f29_debt_trajectory_cashgrowdvol_252d_slope_v028_signal,
    f29dt_f29_debt_trajectory_compgapd_126d_slope_v029_signal,
    f29dt_f29_debt_trajectory_compgapddev_126d_slope_v030_signal,
    f29dt_f29_debt_trajectory_compgapdema_126d_slope_v031_signal,
    f29dt_f29_debt_trajectory_compgapdrank_126d_slope_v032_signal,
    f29dt_f29_debt_trajectory_covzd_252d_slope_v033_signal,
    f29dt_f29_debt_trajectory_covzddev_252d_slope_v034_signal,
    f29dt_f29_debt_trajectory_covzdema_252d_slope_v035_signal,
    f29dt_f29_debt_trajectory_covzdrank_252d_slope_v036_signal,
    f29dt_f29_debt_trajectory_covzdvol_252d_slope_v037_signal,
    f29dt_f29_debt_trajectory_debtcashlrdrank_126d_slope_v038_signal,
    f29dt_f29_debt_trajectory_debtcvd_252d_slope_v039_signal,
    f29dt_f29_debt_trajectory_debtcvddev_252d_slope_v040_signal,
    f29dt_f29_debt_trajectory_debtcvdema_252d_slope_v041_signal,
    f29dt_f29_debt_trajectory_debtcvdrank_252d_slope_v042_signal,
    f29dt_f29_debt_trajectory_debtcvdvol_252d_slope_v043_signal,
    f29dt_f29_debt_trajectory_dgrowd_63d_slope_v044_signal,
    f29dt_f29_debt_trajectory_dgrowddev_63d_slope_v045_signal,
    f29dt_f29_debt_trajectory_dgrowdema_63d_slope_v046_signal,
    f29dt_f29_debt_trajectory_dgrowdrank_63d_slope_v047_signal,
    f29dt_f29_debt_trajectory_dgrowdtanh_63d_slope_v048_signal,
    f29dt_f29_debt_trajectory_dgrowdvol_63d_slope_v049_signal,
    f29dt_f29_debt_trajectory_dgrowdz_63d_slope_v050_signal,
    f29dt_f29_debt_trajectory_dgrowd_126d_slope_v051_signal,
    f29dt_f29_debt_trajectory_dgrowddev_126d_slope_v052_signal,
    f29dt_f29_debt_trajectory_dgrowdema_126d_slope_v053_signal,
    f29dt_f29_debt_trajectory_dgrowdrank_126d_slope_v054_signal,
    f29dt_f29_debt_trajectory_dgrowdvol_126d_slope_v055_signal,
    f29dt_f29_debt_trajectory_dgrowd_252d_slope_v056_signal,
    f29dt_f29_debt_trajectory_dgrowddev_252d_slope_v057_signal,
    f29dt_f29_debt_trajectory_dgrowdema_252d_slope_v058_signal,
    f29dt_f29_debt_trajectory_dgrowdrank_252d_slope_v059_signal,
    f29dt_f29_debt_trajectory_dgrowdvol_252d_slope_v060_signal,
    f29dt_f29_debt_trajectory_dgrowd_504d_slope_v061_signal,
    f29dt_f29_debt_trajectory_dgrowddev_504d_slope_v062_signal,
    f29dt_f29_debt_trajectory_dgrowdema_504d_slope_v063_signal,
    f29dt_f29_debt_trajectory_dgrowdrank_504d_slope_v064_signal,
    f29dt_f29_debt_trajectory_dgrowdtanh_504d_slope_v065_signal,
    f29dt_f29_debt_trajectory_dgrowdvol_504d_slope_v066_signal,
    f29dt_f29_debt_trajectory_dgrowzd_252d_slope_v067_signal,
    f29dt_f29_debt_trajectory_dgrowzddev_252d_slope_v068_signal,
    f29dt_f29_debt_trajectory_dgrowzdema_252d_slope_v069_signal,
    f29dt_f29_debt_trajectory_dgrowzdrank_252d_slope_v070_signal,
    f29dt_f29_debt_trajectory_dgrowzdvol_252d_slope_v071_signal,
    f29dt_f29_debt_trajectory_dpctdrank_63d_slope_v072_signal,
    f29dt_f29_debt_trajectory_dusdextendd_252d_slope_v073_signal,
    f29dt_f29_debt_trajectory_dusdextendddev_252d_slope_v074_signal,
    f29dt_f29_debt_trajectory_dusdextenddema_252d_slope_v075_signal,
    f29dt_f29_debt_trajectory_dusdextenddrank_252d_slope_v076_signal,
    f29dt_f29_debt_trajectory_dusdextenddvol_252d_slope_v077_signal,
    f29dt_f29_debt_trajectory_dusdgrowd_63d_slope_v078_signal,
    f29dt_f29_debt_trajectory_dusdgrowddev_63d_slope_v079_signal,
    f29dt_f29_debt_trajectory_dusdgrowdrank_63d_slope_v080_signal,
    f29dt_f29_debt_trajectory_dusdgrowdtanh_63d_slope_v081_signal,
    f29dt_f29_debt_trajectory_dusdgrowdvol_63d_slope_v082_signal,
    f29dt_f29_debt_trajectory_dusdgrowdz_63d_slope_v083_signal,
    f29dt_f29_debt_trajectory_dusdgrowd_252d_slope_v084_signal,
    f29dt_f29_debt_trajectory_dusdgrowddev_252d_slope_v085_signal,
    f29dt_f29_debt_trajectory_dusdgrowdema_252d_slope_v086_signal,
    f29dt_f29_debt_trajectory_dusdgrowdrank_252d_slope_v087_signal,
    f29dt_f29_debt_trajectory_dusdgrowdvol_252d_slope_v088_signal,
    f29dt_f29_debt_trajectory_emadispd_126d_slope_v089_signal,
    f29dt_f29_debt_trajectory_emadispddev_126d_slope_v090_signal,
    f29dt_f29_debt_trajectory_emadispdema_126d_slope_v091_signal,
    f29dt_f29_debt_trajectory_emadispdrank_126d_slope_v092_signal,
    f29dt_f29_debt_trajectory_emadispdvol_126d_slope_v093_signal,
    f29dt_f29_debt_trajectory_emadispdz_126d_slope_v094_signal,
    f29dt_f29_debt_trajectory_emadispdema_252d_slope_v095_signal,
    f29dt_f29_debt_trajectory_emadispdsgnmag_252d_slope_v096_signal,
    f29dt_f29_debt_trajectory_emadispdtanh_252d_slope_v097_signal,
    f29dt_f29_debt_trajectory_emadispdvol_252d_slope_v098_signal,
    f29dt_f29_debt_trajectory_emadispdz_252d_slope_v099_signal,
    f29dt_f29_debt_trajectory_extenddrank_126d_slope_v100_signal,
    f29dt_f29_debt_trajectory_extenddsgnmag_126d_slope_v101_signal,
    f29dt_f29_debt_trajectory_extendd_252d_slope_v102_signal,
    f29dt_f29_debt_trajectory_extenddrank_252d_slope_v103_signal,
    f29dt_f29_debt_trajectory_extenddvol_252d_slope_v104_signal,
    f29dt_f29_debt_trajectory_growsnrd_252d_slope_v105_signal,
    f29dt_f29_debt_trajectory_growsnrddev_252d_slope_v106_signal,
    f29dt_f29_debt_trajectory_growsnrdema_252d_slope_v107_signal,
    f29dt_f29_debt_trajectory_growsnrdsgnmag_252d_slope_v108_signal,
    f29dt_f29_debt_trajectory_growsnrdtanh_252d_slope_v109_signal,
    f29dt_f29_debt_trajectory_ltcratiod_252d_slope_v110_signal,
    f29dt_f29_debt_trajectory_ltcratioddev_252d_slope_v111_signal,
    f29dt_f29_debt_trajectory_ltcratiodema_252d_slope_v112_signal,
    f29dt_f29_debt_trajectory_ltcratiodrank_252d_slope_v113_signal,
    f29dt_f29_debt_trajectory_ltcratiodvol_252d_slope_v114_signal,
    f29dt_f29_debt_trajectory_ltgrowd_126d_slope_v115_signal,
    f29dt_f29_debt_trajectory_ltgrowddev_126d_slope_v116_signal,
    f29dt_f29_debt_trajectory_ltgrowdema_126d_slope_v117_signal,
    f29dt_f29_debt_trajectory_ltgrowdrank_126d_slope_v118_signal,
    f29dt_f29_debt_trajectory_ltgrowdvol_126d_slope_v119_signal,
    f29dt_f29_debt_trajectory_ltgrowd_252d_slope_v120_signal,
    f29dt_f29_debt_trajectory_ltgrowddev_252d_slope_v121_signal,
    f29dt_f29_debt_trajectory_ltgrowdema_252d_slope_v122_signal,
    f29dt_f29_debt_trajectory_ltgrowdrank_252d_slope_v123_signal,
    f29dt_f29_debt_trajectory_ltgrowdvol_252d_slope_v124_signal,
    f29dt_f29_debt_trajectory_ltsharedrank_252d_slope_v125_signal,
    f29dt_f29_debt_trajectory_ltsharedtanh_252d_slope_v126_signal,
    f29dt_f29_debt_trajectory_ltsharedz_252d_slope_v127_signal,
    f29dt_f29_debt_trajectory_maturitymixd_252d_slope_v128_signal,
    f29dt_f29_debt_trajectory_maturitymixddev_252d_slope_v129_signal,
    f29dt_f29_debt_trajectory_maturitymixdema_252d_slope_v130_signal,
    f29dt_f29_debt_trajectory_maturitymixdrank_252d_slope_v131_signal,
    f29dt_f29_debt_trajectory_maturitymixdvol_252d_slope_v132_signal,
    f29dt_f29_debt_trajectory_ncfcumd_252d_slope_v133_signal,
    f29dt_f29_debt_trajectory_ncfcumddev_252d_slope_v134_signal,
    f29dt_f29_debt_trajectory_ncfcumdema_252d_slope_v135_signal,
    f29dt_f29_debt_trajectory_ncfcumdrank_252d_slope_v136_signal,
    f29dt_f29_debt_trajectory_ncfcumdvol_252d_slope_v137_signal,
    f29dt_f29_debt_trajectory_ncfcumd_504d_slope_v138_signal,
    f29dt_f29_debt_trajectory_ncfcumddev_504d_slope_v139_signal,
    f29dt_f29_debt_trajectory_ncfcumdema_504d_slope_v140_signal,
    f29dt_f29_debt_trajectory_ncfcumdrank_504d_slope_v141_signal,
    f29dt_f29_debt_trajectory_ncfcumdvol_504d_slope_v142_signal,
    f29dt_f29_debt_trajectory_ncfflowd_63d_slope_v143_signal,
    f29dt_f29_debt_trajectory_ncfflowddev_63d_slope_v144_signal,
    f29dt_f29_debt_trajectory_ncfflowdema_63d_slope_v145_signal,
    f29dt_f29_debt_trajectory_ncfflowdrank_63d_slope_v146_signal,
    f29dt_f29_debt_trajectory_ncfflowdtanh_63d_slope_v147_signal,
    f29dt_f29_debt_trajectory_ncfflowdvol_63d_slope_v148_signal,
    f29dt_f29_debt_trajectory_ncfflowdz_63d_slope_v149_signal,
    f29dt_f29_debt_trajectory_ncfflowd_126d_slope_v150_signal,
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

    print("OK f29_debt_trajectory_2nd_derivatives_001_150_claude: %d features pass" % n_features)
