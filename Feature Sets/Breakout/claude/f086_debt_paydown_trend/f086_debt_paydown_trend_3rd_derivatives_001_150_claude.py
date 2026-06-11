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


def _jerk(s, w):
    return s.pct_change(periods=w)


def _jerk(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f086_debt_change(debt, w):
    return debt.diff(periods=w)


def _f086_debt_paydown(debt, w):
    base = debt.rolling(w, min_periods=max(1, w // 2)).mean()
    return -(debt - base.shift(w)) / base.shift(w).abs().replace(0, np.nan)


def _f086_deleverage_score(debt, equity, w):
    lev = debt / equity.replace(0, np.nan)
    return -(lev - lev.shift(w)) / lev.abs().shift(w).replace(0, np.nan)


# v001 5d jerk of 21d debt change × close
def f086dpt_f086_debt_paydown_trend_debtchg_21d_jerk_v001_signal(debt, closeadj):
    base = _f086_debt_change(debt, 21) / debt.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v002 21d jerk of 21d debt change × close
def f086dpt_f086_debt_paydown_trend_debtchg_21d_jerk_v002_signal(debt, closeadj):
    base = _f086_debt_change(debt, 21) / debt.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v003 21d jerk of 63d debt change × close
def f086dpt_f086_debt_paydown_trend_debtchg_63d_jerk_v003_signal(debt, closeadj):
    base = _f086_debt_change(debt, 63) / debt.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v004 63d jerk of 126d debt change × close
def f086dpt_f086_debt_paydown_trend_debtchg_126d_jerk_v004_signal(debt, closeadj):
    base = _f086_debt_change(debt, 126) / debt.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v005 63d jerk of 252d debt change × close
def f086dpt_f086_debt_paydown_trend_debtchg_252d_jerk_v005_signal(debt, closeadj):
    base = _f086_debt_change(debt, 252) / debt.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v006 63d jerk of 504d debt change × close
def f086dpt_f086_debt_paydown_trend_debtchg_504d_jerk_v006_signal(debt, closeadj):
    base = _f086_debt_change(debt, 504) / debt.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v007 5d jerk of 21d paydown × close
def f086dpt_f086_debt_paydown_trend_paydown_21d_jerk_v007_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v008 21d jerk of 21d paydown × close
def f086dpt_f086_debt_paydown_trend_paydown_21d_jerk_v008_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v009 21d jerk of 63d paydown × close
def f086dpt_f086_debt_paydown_trend_paydown_63d_jerk_v009_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v010 63d jerk of 126d paydown × close
def f086dpt_f086_debt_paydown_trend_paydown_126d_jerk_v010_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v011 63d jerk of 252d paydown × close
def f086dpt_f086_debt_paydown_trend_paydown_252d_jerk_v011_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v012 63d jerk of 504d paydown × close
def f086dpt_f086_debt_paydown_trend_paydown_504d_jerk_v012_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v013 21d jerk of 21d deleverage × close
def f086dpt_f086_debt_paydown_trend_delev_21d_jerk_v013_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v014 21d jerk of 63d deleverage × close
def f086dpt_f086_debt_paydown_trend_delev_63d_jerk_v014_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v015 63d jerk of 126d deleverage × close
def f086dpt_f086_debt_paydown_trend_delev_126d_jerk_v015_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v016 63d jerk of 252d deleverage × close
def f086dpt_f086_debt_paydown_trend_delev_252d_jerk_v016_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v017 63d jerk of 504d deleverage × close
def f086dpt_f086_debt_paydown_trend_delev_504d_jerk_v017_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v018 21d jerk of 21d debt change × equity ratio
def f086dpt_f086_debt_paydown_trend_chgxeq_21d_jerk_v018_signal(debt, equity, closeadj):
    base = _f086_debt_change(debt, 21) / equity.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v019 21d jerk of 63d debt change × equity ratio
def f086dpt_f086_debt_paydown_trend_chgxeq_63d_jerk_v019_signal(debt, equity, closeadj):
    base = _f086_debt_change(debt, 63) / equity.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v020 63d jerk of 252d debt change × equity ratio
def f086dpt_f086_debt_paydown_trend_chgxeq_252d_jerk_v020_signal(debt, equity, closeadj):
    base = _f086_debt_change(debt, 252) / equity.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v021 63d jerk of 504d debt change × equity ratio
def f086dpt_f086_debt_paydown_trend_chgxeq_504d_jerk_v021_signal(debt, equity, closeadj):
    base = _f086_debt_change(debt, 504) / equity.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v022 21d jerk of 21d paydown EMA × close
def f086dpt_f086_debt_paydown_trend_paydownema_21d_jerk_v022_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 21).ewm(span=21, min_periods=10).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v023 21d jerk of 63d paydown EMA × close
def f086dpt_f086_debt_paydown_trend_paydownema_63d_jerk_v023_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 63).ewm(span=63, min_periods=30).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v024 63d jerk of 252d paydown EMA × close
def f086dpt_f086_debt_paydown_trend_paydownema_252d_jerk_v024_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 252).ewm(span=126, min_periods=60).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v025 21d jerk of 21d chg z × close
def f086dpt_f086_debt_paydown_trend_chgz_21d_jerk_v025_signal(debt, closeadj):
    base = _f086_debt_change(debt, 21) / debt.abs().replace(0, np.nan)
    base = _z(base, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v026 21d jerk of 63d chg z × close
def f086dpt_f086_debt_paydown_trend_chgz_63d_jerk_v026_signal(debt, closeadj):
    base = _f086_debt_change(debt, 63) / debt.abs().replace(0, np.nan)
    base = _z(base, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v027 63d jerk of 252d chg z × close
def f086dpt_f086_debt_paydown_trend_chgz_252d_jerk_v027_signal(debt, closeadj):
    base = _f086_debt_change(debt, 252) / debt.abs().replace(0, np.nan)
    base = _z(base, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v028 21d jerk of 21d paydown z × close
def f086dpt_f086_debt_paydown_trend_paydownz_21d_jerk_v028_signal(debt, closeadj):
    base = _z(_f086_debt_paydown(debt, 21), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v029 21d jerk of 63d paydown z × close
def f086dpt_f086_debt_paydown_trend_paydownz_63d_jerk_v029_signal(debt, closeadj):
    base = _z(_f086_debt_paydown(debt, 63), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v030 63d jerk of 252d paydown z × close
def f086dpt_f086_debt_paydown_trend_paydownz_252d_jerk_v030_signal(debt, closeadj):
    base = _z(_f086_debt_paydown(debt, 252), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v031 21d jerk of 21d chg std × close
def f086dpt_f086_debt_paydown_trend_chgstd_21d_jerk_v031_signal(debt, closeadj):
    base = _f086_debt_change(debt, 21) / debt.abs().replace(0, np.nan)
    base = _std(base, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v032 21d jerk of 63d chg std × close
def f086dpt_f086_debt_paydown_trend_chgstd_63d_jerk_v032_signal(debt, closeadj):
    base = _f086_debt_change(debt, 63) / debt.abs().replace(0, np.nan)
    base = _std(base, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v033 63d jerk of 252d chg std × close
def f086dpt_f086_debt_paydown_trend_chgstd_252d_jerk_v033_signal(debt, closeadj):
    base = _f086_debt_change(debt, 252) / debt.abs().replace(0, np.nan)
    base = _std(base, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v034 21d jerk of 21d paydown × equity × close
def f086dpt_f086_debt_paydown_trend_paydownxeq_21d_jerk_v034_signal(debt, equity, closeadj):
    base = _f086_debt_paydown(debt, 21) * equity / debt.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v035 21d jerk of 63d paydown × equity × close
def f086dpt_f086_debt_paydown_trend_paydownxeq_63d_jerk_v035_signal(debt, equity, closeadj):
    base = _f086_debt_paydown(debt, 63) * equity / debt.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v036 63d jerk of 252d paydown × equity × close
def f086dpt_f086_debt_paydown_trend_paydownxeq_252d_jerk_v036_signal(debt, equity, closeadj):
    base = _f086_debt_paydown(debt, 252) * equity / debt.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v037 21d jerk of 21d deleverage z × close
def f086dpt_f086_debt_paydown_trend_delevz_21d_jerk_v037_signal(debt, equity, closeadj):
    base = _z(_f086_deleverage_score(debt, equity, 21), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v038 21d jerk of 63d deleverage z × close
def f086dpt_f086_debt_paydown_trend_delevz_63d_jerk_v038_signal(debt, equity, closeadj):
    base = _z(_f086_deleverage_score(debt, equity, 63), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v039 63d jerk of 252d deleverage z × close
def f086dpt_f086_debt_paydown_trend_delevz_252d_jerk_v039_signal(debt, equity, closeadj):
    base = _z(_f086_deleverage_score(debt, equity, 252), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v040 21d jerk of 21d deleverage EMA × close
def f086dpt_f086_debt_paydown_trend_delevema_21d_jerk_v040_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 21).ewm(span=21, min_periods=10).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v041 21d jerk of 63d deleverage EMA × close
def f086dpt_f086_debt_paydown_trend_delevema_63d_jerk_v041_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 63).ewm(span=63, min_periods=30).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v042 63d jerk of 252d deleverage EMA × close
def f086dpt_f086_debt_paydown_trend_delevema_252d_jerk_v042_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 252).ewm(span=126, min_periods=60).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v043 21d jerk of 21d sign-sqrt debt change × close
def f086dpt_f086_debt_paydown_trend_chgsign_21d_jerk_v043_signal(debt, closeadj):
    b = _f086_debt_change(debt, 21) / debt.abs().replace(0, np.nan)
    base = np.sign(b) * b.abs().pow(0.5) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v044 21d jerk of 63d sign-sqrt debt change × close
def f086dpt_f086_debt_paydown_trend_chgsign_63d_jerk_v044_signal(debt, closeadj):
    b = _f086_debt_change(debt, 63) / debt.abs().replace(0, np.nan)
    base = np.sign(b) * b.abs().pow(0.5) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v045 63d jerk of 252d sign-sqrt debt change × close
def f086dpt_f086_debt_paydown_trend_chgsign_252d_jerk_v045_signal(debt, closeadj):
    b = _f086_debt_change(debt, 252) / debt.abs().replace(0, np.nan)
    base = np.sign(b) * b.abs().pow(0.5) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v046 5d jerk of 5d debt change × close
def f086dpt_f086_debt_paydown_trend_debtchg_5d_jerk_v046_signal(debt, closeadj):
    base = _f086_debt_change(debt, 5) / debt.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v047 5d jerk of 10d debt change × close
def f086dpt_f086_debt_paydown_trend_debtchg_10d_jerk_v047_signal(debt, closeadj):
    base = _f086_debt_change(debt, 10) / debt.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v048 21d jerk of 42d debt change × close
def f086dpt_f086_debt_paydown_trend_debtchg_42d_jerk_v048_signal(debt, closeadj):
    base = _f086_debt_change(debt, 42) / debt.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v049 63d jerk of 189d debt change × close
def f086dpt_f086_debt_paydown_trend_debtchg_189d_jerk_v049_signal(debt, closeadj):
    base = _f086_debt_change(debt, 189) / debt.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v050 63d jerk of 378d debt change × close
def f086dpt_f086_debt_paydown_trend_debtchg_378d_jerk_v050_signal(debt, closeadj):
    base = _f086_debt_change(debt, 378) / debt.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v051 5d jerk of 5d paydown × close
def f086dpt_f086_debt_paydown_trend_paydown_5d_jerk_v051_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v052 5d jerk of 10d paydown × close
def f086dpt_f086_debt_paydown_trend_paydown_10d_jerk_v052_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v053 21d jerk of 42d paydown × close
def f086dpt_f086_debt_paydown_trend_paydown_42d_jerk_v053_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v054 63d jerk of 189d paydown × close
def f086dpt_f086_debt_paydown_trend_paydown_189d_jerk_v054_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v055 63d jerk of 378d paydown × close
def f086dpt_f086_debt_paydown_trend_paydown_378d_jerk_v055_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v056 21d jerk of 42d deleverage × close
def f086dpt_f086_debt_paydown_trend_delev_42d_jerk_v056_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v057 63d jerk of 189d deleverage × close
def f086dpt_f086_debt_paydown_trend_delev_189d_jerk_v057_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v058 63d jerk of 378d deleverage × close
def f086dpt_f086_debt_paydown_trend_delev_378d_jerk_v058_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v059 21d jerk of 21d paydown mean × close
def f086dpt_f086_debt_paydown_trend_paydownmean_21d_jerk_v059_signal(debt, closeadj):
    base = _mean(_f086_debt_paydown(debt, 21), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v060 21d jerk of 63d paydown mean × close
def f086dpt_f086_debt_paydown_trend_paydownmean_63d_jerk_v060_signal(debt, closeadj):
    base = _mean(_f086_debt_paydown(debt, 63), 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v061 63d jerk of 252d paydown mean × close
def f086dpt_f086_debt_paydown_trend_paydownmean_252d_jerk_v061_signal(debt, closeadj):
    base = _mean(_f086_debt_paydown(debt, 252), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v062 21d jerk of 21d paydown × log close
def f086dpt_f086_debt_paydown_trend_paydownxlog_21d_jerk_v062_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 21) * np.log(closeadj.abs().replace(0, np.nan))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v063 21d jerk of 63d paydown × log close
def f086dpt_f086_debt_paydown_trend_paydownxlog_63d_jerk_v063_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 63) * np.log(closeadj.abs().replace(0, np.nan))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v064 63d jerk of 252d paydown × log close
def f086dpt_f086_debt_paydown_trend_paydownxlog_252d_jerk_v064_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 252) * np.log(closeadj.abs().replace(0, np.nan))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v065 21d jerk of 21d paydown × close/equity
def f086dpt_f086_debt_paydown_trend_paydownxce_21d_jerk_v065_signal(debt, equity, closeadj):
    base = _f086_debt_paydown(debt, 21) * closeadj * 1e8 / equity.abs().replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v066 21d jerk of 63d paydown × close/equity
def f086dpt_f086_debt_paydown_trend_paydownxce_63d_jerk_v066_signal(debt, equity, closeadj):
    base = _f086_debt_paydown(debt, 63) * closeadj * 1e8 / equity.abs().replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v067 63d jerk of 252d paydown × close/equity
def f086dpt_f086_debt_paydown_trend_paydownxce_252d_jerk_v067_signal(debt, equity, closeadj):
    base = _f086_debt_paydown(debt, 252) * closeadj * 1e8 / equity.abs().replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v068 21d jerk of 21d paydown squared × close
def f086dpt_f086_debt_paydown_trend_paydownsq_21d_jerk_v068_signal(debt, closeadj):
    b = _f086_debt_paydown(debt, 21)
    base = (b * b.abs()) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v069 21d jerk of 63d paydown squared × close
def f086dpt_f086_debt_paydown_trend_paydownsq_63d_jerk_v069_signal(debt, closeadj):
    b = _f086_debt_paydown(debt, 63)
    base = (b * b.abs()) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v070 63d jerk of 252d paydown squared × close
def f086dpt_f086_debt_paydown_trend_paydownsq_252d_jerk_v070_signal(debt, closeadj):
    b = _f086_debt_paydown(debt, 252)
    base = (b * b.abs()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v071 21d jerk of 21d paydown max × close
def f086dpt_f086_debt_paydown_trend_paydownmax_21d_jerk_v071_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 21).rolling(63, min_periods=21).max() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v072 21d jerk of 63d paydown max × close
def f086dpt_f086_debt_paydown_trend_paydownmax_63d_jerk_v072_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 63).rolling(126, min_periods=42).max() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v073 63d jerk of 252d paydown max × close
def f086dpt_f086_debt_paydown_trend_paydownmax_252d_jerk_v073_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 252).rolling(252, min_periods=63).max() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v074 21d jerk of 21d paydown sum × close
def f086dpt_f086_debt_paydown_trend_paydownsum_21d_jerk_v074_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 21).rolling(63, min_periods=21).sum() * closeadj / 63.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v075 63d jerk of 252d paydown sum × close
def f086dpt_f086_debt_paydown_trend_paydownsum_252d_jerk_v075_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 252).rolling(252, min_periods=63).sum() * closeadj / 252.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v076 21d jerk of 21d composite delev × close
def f086dpt_f086_debt_paydown_trend_compdelev_21d_jerk_v076_signal(debt, equity, closeadj):
    a = _f086_debt_paydown(debt, 21)
    eq_g = (equity - equity.shift(21)) / equity.abs().shift(21).replace(0, np.nan)
    base = (a + eq_g) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v077 21d jerk of 21d chg smoothed × close
def f086dpt_f086_debt_paydown_trend_chgsm_21d_jerk_v077_signal(debt, closeadj):
    base = _f086_debt_change(debt, 21) / debt.abs().replace(0, np.nan)
    base = _mean(base, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v078 21d jerk of 63d chg smoothed × close
def f086dpt_f086_debt_paydown_trend_chgsm_63d_jerk_v078_signal(debt, closeadj):
    base = _f086_debt_change(debt, 63) / debt.abs().replace(0, np.nan)
    base = _mean(base, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v079 63d jerk of 252d chg smoothed × close
def f086dpt_f086_debt_paydown_trend_chgsm_252d_jerk_v079_signal(debt, closeadj):
    base = _f086_debt_change(debt, 252) / debt.abs().replace(0, np.nan)
    base = _mean(base, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v080 21d jerk of 21d delev × log close
def f086dpt_f086_debt_paydown_trend_delevxlog_21d_jerk_v080_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 21) * np.log(closeadj.abs().replace(0, np.nan))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v081 21d jerk of 63d delev × log close
def f086dpt_f086_debt_paydown_trend_delevxlog_63d_jerk_v081_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 63) * np.log(closeadj.abs().replace(0, np.nan))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v082 63d jerk of 252d delev × log close
def f086dpt_f086_debt_paydown_trend_delevxlog_252d_jerk_v082_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 252) * np.log(closeadj.abs().replace(0, np.nan))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v083 21d jerk of 21d paydown lag × close
def f086dpt_f086_debt_paydown_trend_paydownlag_21d_jerk_v083_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 21).shift(5) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v084 21d jerk of 63d paydown lag × close
def f086dpt_f086_debt_paydown_trend_paydownlag_63d_jerk_v084_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 63).shift(21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v085 63d jerk of 252d paydown lag × close
def f086dpt_f086_debt_paydown_trend_paydownlag_252d_jerk_v085_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 252).shift(63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v086 21d jerk of 21d paydown tanh × close
def f086dpt_f086_debt_paydown_trend_paydowntanh_21d_jerk_v086_signal(debt, closeadj):
    base = np.tanh(_f086_debt_paydown(debt, 21) * 3.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v087 21d jerk of 63d paydown tanh × close
def f086dpt_f086_debt_paydown_trend_paydowntanh_63d_jerk_v087_signal(debt, closeadj):
    base = np.tanh(_f086_debt_paydown(debt, 63) * 3.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v088 63d jerk of 252d paydown tanh × close
def f086dpt_f086_debt_paydown_trend_paydowntanh_252d_jerk_v088_signal(debt, closeadj):
    base = np.tanh(_f086_debt_paydown(debt, 252) * 3.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v089 21d jerk of 21d chg × close²
def f086dpt_f086_debt_paydown_trend_chgxcsq_21d_jerk_v089_signal(debt, closeadj):
    base = _f086_debt_change(debt, 21) / debt.abs().replace(0, np.nan) * closeadj * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v090 21d jerk of 63d chg × close²
def f086dpt_f086_debt_paydown_trend_chgxcsq_63d_jerk_v090_signal(debt, closeadj):
    base = _f086_debt_change(debt, 63) / debt.abs().replace(0, np.nan) * closeadj * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v091 63d jerk of 252d chg × close²
def f086dpt_f086_debt_paydown_trend_chgxcsq_252d_jerk_v091_signal(debt, closeadj):
    base = _f086_debt_change(debt, 252) / debt.abs().replace(0, np.nan) * closeadj * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v092 21d jerk of 21d paydown sharpe × close
def f086dpt_f086_debt_paydown_trend_paydownsharpe_21d_jerk_v092_signal(debt, closeadj):
    b = _f086_debt_paydown(debt, 21)
    s = _std(b, 252).replace(0, np.nan)
    base = (b / s) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v093 21d jerk of 63d paydown sharpe × close
def f086dpt_f086_debt_paydown_trend_paydownsharpe_63d_jerk_v093_signal(debt, closeadj):
    b = _f086_debt_paydown(debt, 63)
    s = _std(b, 252).replace(0, np.nan)
    base = (b / s) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v094 63d jerk of 252d paydown sharpe × close
def f086dpt_f086_debt_paydown_trend_paydownsharpe_252d_jerk_v094_signal(debt, closeadj):
    b = _f086_debt_paydown(debt, 252)
    s = _std(b, 504).replace(0, np.nan)
    base = (b / s) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v095 21d jerk of 21d paydown efficiency × close
def f086dpt_f086_debt_paydown_trend_paydowneff_21d_jerk_v095_signal(debt, closeadj):
    pd_ = _f086_debt_paydown(debt, 21)
    chg = _f086_debt_change(debt, 21).abs() / debt.abs().replace(0, np.nan) + 1e-9
    base = (pd_ / chg) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v096 21d jerk of 63d paydown efficiency × close
def f086dpt_f086_debt_paydown_trend_paydowneff_63d_jerk_v096_signal(debt, closeadj):
    pd_ = _f086_debt_paydown(debt, 63)
    chg = _f086_debt_change(debt, 63).abs() / debt.abs().replace(0, np.nan) + 1e-9
    base = (pd_ / chg) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v097 63d jerk of 252d paydown efficiency × close
def f086dpt_f086_debt_paydown_trend_paydowneff_252d_jerk_v097_signal(debt, closeadj):
    pd_ = _f086_debt_paydown(debt, 252)
    chg = _f086_debt_change(debt, 252).abs() / debt.abs().replace(0, np.nan) + 1e-9
    base = (pd_ / chg) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v098 21d jerk of 21d delev+paydown × close
def f086dpt_f086_debt_paydown_trend_delevpd_21d_jerk_v098_signal(debt, equity, closeadj):
    a = _f086_deleverage_score(debt, equity, 21)
    b = _f086_debt_paydown(debt, 21)
    base = (a + b) * 0.5 * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v099 21d jerk of 63d delev+paydown × close
def f086dpt_f086_debt_paydown_trend_delevpd_63d_jerk_v099_signal(debt, equity, closeadj):
    a = _f086_deleverage_score(debt, equity, 63)
    b = _f086_debt_paydown(debt, 63)
    base = (a + b) * 0.5 * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v100 63d jerk of 252d delev+paydown × close
def f086dpt_f086_debt_paydown_trend_delevpd_252d_jerk_v100_signal(debt, equity, closeadj):
    a = _f086_deleverage_score(debt, equity, 252)
    b = _f086_debt_paydown(debt, 252)
    base = (a + b) * 0.5 * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v101 21d jerk of 21d chg × equity/debt × close
def f086dpt_f086_debt_paydown_trend_chgxer_21d_jerk_v101_signal(debt, equity, closeadj):
    b = _f086_debt_change(debt, 21) / debt.abs().replace(0, np.nan)
    eqr = (equity / debt.replace(0, np.nan)).clip(-10, 10)
    base = b * eqr * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v102 21d jerk of 63d chg × equity/debt × close
def f086dpt_f086_debt_paydown_trend_chgxer_63d_jerk_v102_signal(debt, equity, closeadj):
    b = _f086_debt_change(debt, 63) / debt.abs().replace(0, np.nan)
    eqr = (equity / debt.replace(0, np.nan)).clip(-10, 10)
    base = b * eqr * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v103 63d jerk of 252d chg × equity/debt × close
def f086dpt_f086_debt_paydown_trend_chgxer_252d_jerk_v103_signal(debt, equity, closeadj):
    b = _f086_debt_change(debt, 252) / debt.abs().replace(0, np.nan)
    eqr = (equity / debt.replace(0, np.nan)).clip(-10, 10)
    base = b * eqr * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v104 21d jerk of 21d paydown × abs equity delta × close
def f086dpt_f086_debt_paydown_trend_pdxeqd_21d_jerk_v104_signal(debt, equity, closeadj):
    a = _f086_debt_paydown(debt, 21)
    eqd = (equity - equity.shift(21)) / equity.abs().shift(21).replace(0, np.nan)
    base = a * eqd.abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v105 21d jerk of 63d paydown × abs equity delta × close
def f086dpt_f086_debt_paydown_trend_pdxeqd_63d_jerk_v105_signal(debt, equity, closeadj):
    a = _f086_debt_paydown(debt, 63)
    eqd = (equity - equity.shift(63)) / equity.abs().shift(63).replace(0, np.nan)
    base = a * eqd.abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v106 63d jerk of 252d paydown × abs equity delta × close
def f086dpt_f086_debt_paydown_trend_pdxeqd_252d_jerk_v106_signal(debt, equity, closeadj):
    a = _f086_debt_paydown(debt, 252)
    eqd = (equity - equity.shift(252)) / equity.abs().shift(252).replace(0, np.nan)
    base = a * eqd.abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v107 63d jerk of cumulative paydown 252d × close
def f086dpt_f086_debt_paydown_trend_paydowncum_252d_jerk_v107_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 21).rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v108 63d jerk of cumulative paydown 504d × close
def f086dpt_f086_debt_paydown_trend_paydowncum_504d_jerk_v108_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 63).rolling(504, min_periods=126).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v109 21d jerk of 21d paydown range-norm × close
def f086dpt_f086_debt_paydown_trend_paydownrange_21d_jerk_v109_signal(debt, closeadj):
    b = _f086_debt_paydown(debt, 21)
    mx = b.rolling(252, min_periods=63).max()
    mn = b.rolling(252, min_periods=63).min()
    rng = (mx - mn).replace(0, np.nan)
    base = ((b - mn) / rng) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v110 21d jerk of 63d paydown range-norm × close
def f086dpt_f086_debt_paydown_trend_paydownrange_63d_jerk_v110_signal(debt, closeadj):
    b = _f086_debt_paydown(debt, 63)
    mx = b.rolling(252, min_periods=63).max()
    mn = b.rolling(252, min_periods=63).min()
    rng = (mx - mn).replace(0, np.nan)
    base = ((b - mn) / rng) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v111 63d jerk of 252d paydown range-norm × close
def f086dpt_f086_debt_paydown_trend_paydownrange_252d_jerk_v111_signal(debt, closeadj):
    b = _f086_debt_paydown(debt, 252)
    mx = b.rolling(504, min_periods=126).max()
    mn = b.rolling(504, min_periods=126).min()
    rng = (mx - mn).replace(0, np.nan)
    base = ((b - mn) / rng) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v112 21d jerk of 21d paydown/delev ratio × close
def f086dpt_f086_debt_paydown_trend_pddelevratio_21d_jerk_v112_signal(debt, equity, closeadj):
    a = _f086_debt_paydown(debt, 21)
    b = _f086_deleverage_score(debt, equity, 21).abs() + 1e-9
    base = (a / b) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v113 21d jerk of 63d paydown/delev ratio × close
def f086dpt_f086_debt_paydown_trend_pddelevratio_63d_jerk_v113_signal(debt, equity, closeadj):
    a = _f086_debt_paydown(debt, 63)
    b = _f086_deleverage_score(debt, equity, 63).abs() + 1e-9
    base = (a / b) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v114 63d jerk of 252d paydown/delev ratio × close
def f086dpt_f086_debt_paydown_trend_pddelevratio_252d_jerk_v114_signal(debt, equity, closeadj):
    a = _f086_debt_paydown(debt, 252)
    b = _f086_deleverage_score(debt, equity, 252).abs() + 1e-9
    base = (a / b) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v115 21d jerk of 21d chg × close × log equity
def f086dpt_f086_debt_paydown_trend_chgxleq_21d_jerk_v115_signal(debt, equity, closeadj):
    base = _f086_debt_change(debt, 21) / debt.abs().replace(0, np.nan) * closeadj * np.log(equity.abs().replace(0, np.nan))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v116 21d jerk of 63d chg × close × log equity
def f086dpt_f086_debt_paydown_trend_chgxleq_63d_jerk_v116_signal(debt, equity, closeadj):
    base = _f086_debt_change(debt, 63) / debt.abs().replace(0, np.nan) * closeadj * np.log(equity.abs().replace(0, np.nan))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v117 63d jerk of 252d chg × close × log equity
def f086dpt_f086_debt_paydown_trend_chgxleq_252d_jerk_v117_signal(debt, equity, closeadj):
    base = _f086_debt_change(debt, 252) / debt.abs().replace(0, np.nan) * closeadj * np.log(equity.abs().replace(0, np.nan))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v118 21d jerk of 21d delev × sqrt eq/debt × close
def f086dpt_f086_debt_paydown_trend_delevxsqr_21d_jerk_v118_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 21)
    ratio = (equity / debt.replace(0, np.nan)).clip(lower=0).pow(0.5)
    base = base * ratio * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v119 21d jerk of 63d delev × sqrt eq/debt × close
def f086dpt_f086_debt_paydown_trend_delevxsqr_63d_jerk_v119_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 63)
    ratio = (equity / debt.replace(0, np.nan)).clip(lower=0).pow(0.5)
    base = base * ratio * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v120 63d jerk of 252d delev × sqrt eq/debt × close
def f086dpt_f086_debt_paydown_trend_delevxsqr_252d_jerk_v120_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 252)
    ratio = (equity / debt.replace(0, np.nan)).clip(lower=0).pow(0.5)
    base = base * ratio * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v121 21d jerk of 21d short/long paydown ratio × close
def f086dpt_f086_debt_paydown_trend_pdratio_21v252_jerk_v121_signal(debt, closeadj):
    a = _f086_debt_paydown(debt, 21)
    b = _f086_debt_paydown(debt, 252).abs() + 1e-9
    base = (a / b) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v122 63d jerk of 63d short/long paydown ratio × close
def f086dpt_f086_debt_paydown_trend_pdratio_63v504_jerk_v122_signal(debt, closeadj):
    a = _f086_debt_paydown(debt, 63)
    b = _f086_debt_paydown(debt, 504).abs() + 1e-9
    base = (a / b) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v123 21d jerk of 21d-63d paydown diff × close
def f086dpt_f086_debt_paydown_trend_pddiff_21m63_jerk_v123_signal(debt, closeadj):
    a = _f086_debt_paydown(debt, 21)
    b = _f086_debt_paydown(debt, 63)
    base = (a - b) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v124 63d jerk of 63d-252d paydown diff × close
def f086dpt_f086_debt_paydown_trend_pddiff_63m252_jerk_v124_signal(debt, closeadj):
    a = _f086_debt_paydown(debt, 63)
    b = _f086_debt_paydown(debt, 252)
    base = (a - b) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v125 63d jerk of 21d-252d paydown diff × close
def f086dpt_f086_debt_paydown_trend_pddiff_21m252_jerk_v125_signal(debt, closeadj):
    a = _f086_debt_paydown(debt, 21)
    b = _f086_debt_paydown(debt, 252)
    base = (a - b) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v126 21d jerk of 21d delev min × close
def f086dpt_f086_debt_paydown_trend_delevmin_21d_jerk_v126_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 21).rolling(63, min_periods=21).min() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v127 21d jerk of 63d delev min × close
def f086dpt_f086_debt_paydown_trend_delevmin_63d_jerk_v127_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 63).rolling(126, min_periods=42).min() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v128 63d jerk of 252d delev min × close
def f086dpt_f086_debt_paydown_trend_delevmin_252d_jerk_v128_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 252).rolling(252, min_periods=63).min() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v129 21d jerk of 21d delev range × close
def f086dpt_f086_debt_paydown_trend_delevrange_21d_jerk_v129_signal(debt, equity, closeadj):
    b = _f086_deleverage_score(debt, equity, 21)
    rng = b.rolling(126, min_periods=42).max() - b.rolling(126, min_periods=42).min()
    base = rng * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v130 21d jerk of 63d delev range × close
def f086dpt_f086_debt_paydown_trend_delevrange_63d_jerk_v130_signal(debt, equity, closeadj):
    b = _f086_deleverage_score(debt, equity, 63)
    rng = b.rolling(252, min_periods=63).max() - b.rolling(252, min_periods=63).min()
    base = rng * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v131 63d jerk of 252d delev range × close
def f086dpt_f086_debt_paydown_trend_delevrange_252d_jerk_v131_signal(debt, equity, closeadj):
    b = _f086_deleverage_score(debt, equity, 252)
    rng = b.rolling(504, min_periods=126).max() - b.rolling(504, min_periods=126).min()
    base = rng * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v132 21d jerk of 21d paydown count × close
def f086dpt_f086_debt_paydown_trend_paydowncount_21d_jerk_v132_signal(debt, closeadj):
    b = _f086_debt_paydown(debt, 21)
    cnt = (b > 0).astype(float).rolling(126, min_periods=21).sum()
    base = cnt * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v133 21d jerk of 63d paydown count × close
def f086dpt_f086_debt_paydown_trend_paydowncount_63d_jerk_v133_signal(debt, closeadj):
    b = _f086_debt_paydown(debt, 63)
    cnt = (b > 0).astype(float).rolling(252, min_periods=63).sum()
    base = cnt * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v134 63d jerk of 252d paydown count × close
def f086dpt_f086_debt_paydown_trend_paydowncount_252d_jerk_v134_signal(debt, closeadj):
    b = _f086_debt_paydown(debt, 252)
    cnt = (b > 0).astype(float).rolling(504, min_periods=126).sum()
    base = cnt * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v135 21d jerk of 21d paydown × eqf × close
def f086dpt_f086_debt_paydown_trend_paydownxeqf_21d_jerk_v135_signal(debt, equity, closeadj):
    b = _f086_debt_paydown(debt, 21)
    f = (equity / equity.shift(252).replace(0, np.nan)).clip(0.1, 5.0)
    base = b * f * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v136 21d jerk of 63d paydown × eqf × close
def f086dpt_f086_debt_paydown_trend_paydownxeqf_63d_jerk_v136_signal(debt, equity, closeadj):
    b = _f086_debt_paydown(debt, 63)
    f = (equity / equity.shift(252).replace(0, np.nan)).clip(0.1, 5.0)
    base = b * f * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v137 63d jerk of 252d paydown × eqf × close
def f086dpt_f086_debt_paydown_trend_paydownxeqf_252d_jerk_v137_signal(debt, equity, closeadj):
    b = _f086_debt_paydown(debt, 252)
    f = (equity / equity.shift(252).replace(0, np.nan)).clip(0.1, 5.0)
    base = b * f * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v138 21d jerk of 21d delev × paydown × close
def f086dpt_f086_debt_paydown_trend_delevxpd_21d_jerk_v138_signal(debt, equity, closeadj):
    a = _f086_deleverage_score(debt, equity, 21)
    b = _f086_debt_paydown(debt, 21)
    base = (a * b) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v139 21d jerk of 63d delev × paydown × close
def f086dpt_f086_debt_paydown_trend_delevxpd_63d_jerk_v139_signal(debt, equity, closeadj):
    a = _f086_deleverage_score(debt, equity, 63)
    b = _f086_debt_paydown(debt, 63)
    base = (a * b) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v140 63d jerk of 252d delev × paydown × close
def f086dpt_f086_debt_paydown_trend_delevxpd_252d_jerk_v140_signal(debt, equity, closeadj):
    a = _f086_deleverage_score(debt, equity, 252)
    b = _f086_debt_paydown(debt, 252)
    base = (a * b) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v141 21d jerk of 21d paydown × log debt × close
def f086dpt_f086_debt_paydown_trend_paydownxld_21d_jerk_v141_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 21) * np.log(debt.abs().replace(0, np.nan)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v142 21d jerk of 63d paydown × log debt × close
def f086dpt_f086_debt_paydown_trend_paydownxld_63d_jerk_v142_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 63) * np.log(debt.abs().replace(0, np.nan)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v143 63d jerk of 252d paydown × log debt × close
def f086dpt_f086_debt_paydown_trend_paydownxld_252d_jerk_v143_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 252) * np.log(debt.abs().replace(0, np.nan)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v144 63d jerk of 21d composite × close × log close
def f086dpt_f086_debt_paydown_trend_pdcomp_21d_jerk_v144_signal(debt, equity, closeadj):
    a = _f086_deleverage_score(debt, equity, 21)
    b = _f086_debt_paydown(debt, 21)
    base = (a + b) * closeadj * np.log(closeadj.abs().replace(0, np.nan))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v145 63d jerk of 252d composite × close × log close
def f086dpt_f086_debt_paydown_trend_pdcomp_252d_jerk_v145_signal(debt, equity, closeadj):
    a = _f086_deleverage_score(debt, equity, 252)
    b = _f086_debt_paydown(debt, 252)
    base = (a + b) * closeadj * np.log(closeadj.abs().replace(0, np.nan))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v146 5d jerk of 21d delev × close (short fast)
def f086dpt_f086_debt_paydown_trend_delevfast_21d_jerk_v146_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v147 10d jerk of 42d delev × close
def f086dpt_f086_debt_paydown_trend_delevfast_42d_jerk_v147_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 42) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# v148 42d jerk of 126d delev × close
def f086dpt_f086_debt_paydown_trend_delevmid_126d_jerk_v148_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 126) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# v149 126d jerk of 252d delev × close
def f086dpt_f086_debt_paydown_trend_delevslow_252d_jerk_v149_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# v150 126d jerk of 504d delev × close
def f086dpt_f086_debt_paydown_trend_delevslow_504d_jerk_v150_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 504) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f086dpt_f086_debt_paydown_trend_debtchg_21d_jerk_v001_signal,
    f086dpt_f086_debt_paydown_trend_debtchg_21d_jerk_v002_signal,
    f086dpt_f086_debt_paydown_trend_debtchg_63d_jerk_v003_signal,
    f086dpt_f086_debt_paydown_trend_debtchg_126d_jerk_v004_signal,
    f086dpt_f086_debt_paydown_trend_debtchg_252d_jerk_v005_signal,
    f086dpt_f086_debt_paydown_trend_debtchg_504d_jerk_v006_signal,
    f086dpt_f086_debt_paydown_trend_paydown_21d_jerk_v007_signal,
    f086dpt_f086_debt_paydown_trend_paydown_21d_jerk_v008_signal,
    f086dpt_f086_debt_paydown_trend_paydown_63d_jerk_v009_signal,
    f086dpt_f086_debt_paydown_trend_paydown_126d_jerk_v010_signal,
    f086dpt_f086_debt_paydown_trend_paydown_252d_jerk_v011_signal,
    f086dpt_f086_debt_paydown_trend_paydown_504d_jerk_v012_signal,
    f086dpt_f086_debt_paydown_trend_delev_21d_jerk_v013_signal,
    f086dpt_f086_debt_paydown_trend_delev_63d_jerk_v014_signal,
    f086dpt_f086_debt_paydown_trend_delev_126d_jerk_v015_signal,
    f086dpt_f086_debt_paydown_trend_delev_252d_jerk_v016_signal,
    f086dpt_f086_debt_paydown_trend_delev_504d_jerk_v017_signal,
    f086dpt_f086_debt_paydown_trend_chgxeq_21d_jerk_v018_signal,
    f086dpt_f086_debt_paydown_trend_chgxeq_63d_jerk_v019_signal,
    f086dpt_f086_debt_paydown_trend_chgxeq_252d_jerk_v020_signal,
    f086dpt_f086_debt_paydown_trend_chgxeq_504d_jerk_v021_signal,
    f086dpt_f086_debt_paydown_trend_paydownema_21d_jerk_v022_signal,
    f086dpt_f086_debt_paydown_trend_paydownema_63d_jerk_v023_signal,
    f086dpt_f086_debt_paydown_trend_paydownema_252d_jerk_v024_signal,
    f086dpt_f086_debt_paydown_trend_chgz_21d_jerk_v025_signal,
    f086dpt_f086_debt_paydown_trend_chgz_63d_jerk_v026_signal,
    f086dpt_f086_debt_paydown_trend_chgz_252d_jerk_v027_signal,
    f086dpt_f086_debt_paydown_trend_paydownz_21d_jerk_v028_signal,
    f086dpt_f086_debt_paydown_trend_paydownz_63d_jerk_v029_signal,
    f086dpt_f086_debt_paydown_trend_paydownz_252d_jerk_v030_signal,
    f086dpt_f086_debt_paydown_trend_chgstd_21d_jerk_v031_signal,
    f086dpt_f086_debt_paydown_trend_chgstd_63d_jerk_v032_signal,
    f086dpt_f086_debt_paydown_trend_chgstd_252d_jerk_v033_signal,
    f086dpt_f086_debt_paydown_trend_paydownxeq_21d_jerk_v034_signal,
    f086dpt_f086_debt_paydown_trend_paydownxeq_63d_jerk_v035_signal,
    f086dpt_f086_debt_paydown_trend_paydownxeq_252d_jerk_v036_signal,
    f086dpt_f086_debt_paydown_trend_delevz_21d_jerk_v037_signal,
    f086dpt_f086_debt_paydown_trend_delevz_63d_jerk_v038_signal,
    f086dpt_f086_debt_paydown_trend_delevz_252d_jerk_v039_signal,
    f086dpt_f086_debt_paydown_trend_delevema_21d_jerk_v040_signal,
    f086dpt_f086_debt_paydown_trend_delevema_63d_jerk_v041_signal,
    f086dpt_f086_debt_paydown_trend_delevema_252d_jerk_v042_signal,
    f086dpt_f086_debt_paydown_trend_chgsign_21d_jerk_v043_signal,
    f086dpt_f086_debt_paydown_trend_chgsign_63d_jerk_v044_signal,
    f086dpt_f086_debt_paydown_trend_chgsign_252d_jerk_v045_signal,
    f086dpt_f086_debt_paydown_trend_debtchg_5d_jerk_v046_signal,
    f086dpt_f086_debt_paydown_trend_debtchg_10d_jerk_v047_signal,
    f086dpt_f086_debt_paydown_trend_debtchg_42d_jerk_v048_signal,
    f086dpt_f086_debt_paydown_trend_debtchg_189d_jerk_v049_signal,
    f086dpt_f086_debt_paydown_trend_debtchg_378d_jerk_v050_signal,
    f086dpt_f086_debt_paydown_trend_paydown_5d_jerk_v051_signal,
    f086dpt_f086_debt_paydown_trend_paydown_10d_jerk_v052_signal,
    f086dpt_f086_debt_paydown_trend_paydown_42d_jerk_v053_signal,
    f086dpt_f086_debt_paydown_trend_paydown_189d_jerk_v054_signal,
    f086dpt_f086_debt_paydown_trend_paydown_378d_jerk_v055_signal,
    f086dpt_f086_debt_paydown_trend_delev_42d_jerk_v056_signal,
    f086dpt_f086_debt_paydown_trend_delev_189d_jerk_v057_signal,
    f086dpt_f086_debt_paydown_trend_delev_378d_jerk_v058_signal,
    f086dpt_f086_debt_paydown_trend_paydownmean_21d_jerk_v059_signal,
    f086dpt_f086_debt_paydown_trend_paydownmean_63d_jerk_v060_signal,
    f086dpt_f086_debt_paydown_trend_paydownmean_252d_jerk_v061_signal,
    f086dpt_f086_debt_paydown_trend_paydownxlog_21d_jerk_v062_signal,
    f086dpt_f086_debt_paydown_trend_paydownxlog_63d_jerk_v063_signal,
    f086dpt_f086_debt_paydown_trend_paydownxlog_252d_jerk_v064_signal,
    f086dpt_f086_debt_paydown_trend_paydownxce_21d_jerk_v065_signal,
    f086dpt_f086_debt_paydown_trend_paydownxce_63d_jerk_v066_signal,
    f086dpt_f086_debt_paydown_trend_paydownxce_252d_jerk_v067_signal,
    f086dpt_f086_debt_paydown_trend_paydownsq_21d_jerk_v068_signal,
    f086dpt_f086_debt_paydown_trend_paydownsq_63d_jerk_v069_signal,
    f086dpt_f086_debt_paydown_trend_paydownsq_252d_jerk_v070_signal,
    f086dpt_f086_debt_paydown_trend_paydownmax_21d_jerk_v071_signal,
    f086dpt_f086_debt_paydown_trend_paydownmax_63d_jerk_v072_signal,
    f086dpt_f086_debt_paydown_trend_paydownmax_252d_jerk_v073_signal,
    f086dpt_f086_debt_paydown_trend_paydownsum_21d_jerk_v074_signal,
    f086dpt_f086_debt_paydown_trend_paydownsum_252d_jerk_v075_signal,
    f086dpt_f086_debt_paydown_trend_compdelev_21d_jerk_v076_signal,
    f086dpt_f086_debt_paydown_trend_chgsm_21d_jerk_v077_signal,
    f086dpt_f086_debt_paydown_trend_chgsm_63d_jerk_v078_signal,
    f086dpt_f086_debt_paydown_trend_chgsm_252d_jerk_v079_signal,
    f086dpt_f086_debt_paydown_trend_delevxlog_21d_jerk_v080_signal,
    f086dpt_f086_debt_paydown_trend_delevxlog_63d_jerk_v081_signal,
    f086dpt_f086_debt_paydown_trend_delevxlog_252d_jerk_v082_signal,
    f086dpt_f086_debt_paydown_trend_paydownlag_21d_jerk_v083_signal,
    f086dpt_f086_debt_paydown_trend_paydownlag_63d_jerk_v084_signal,
    f086dpt_f086_debt_paydown_trend_paydownlag_252d_jerk_v085_signal,
    f086dpt_f086_debt_paydown_trend_paydowntanh_21d_jerk_v086_signal,
    f086dpt_f086_debt_paydown_trend_paydowntanh_63d_jerk_v087_signal,
    f086dpt_f086_debt_paydown_trend_paydowntanh_252d_jerk_v088_signal,
    f086dpt_f086_debt_paydown_trend_chgxcsq_21d_jerk_v089_signal,
    f086dpt_f086_debt_paydown_trend_chgxcsq_63d_jerk_v090_signal,
    f086dpt_f086_debt_paydown_trend_chgxcsq_252d_jerk_v091_signal,
    f086dpt_f086_debt_paydown_trend_paydownsharpe_21d_jerk_v092_signal,
    f086dpt_f086_debt_paydown_trend_paydownsharpe_63d_jerk_v093_signal,
    f086dpt_f086_debt_paydown_trend_paydownsharpe_252d_jerk_v094_signal,
    f086dpt_f086_debt_paydown_trend_paydowneff_21d_jerk_v095_signal,
    f086dpt_f086_debt_paydown_trend_paydowneff_63d_jerk_v096_signal,
    f086dpt_f086_debt_paydown_trend_paydowneff_252d_jerk_v097_signal,
    f086dpt_f086_debt_paydown_trend_delevpd_21d_jerk_v098_signal,
    f086dpt_f086_debt_paydown_trend_delevpd_63d_jerk_v099_signal,
    f086dpt_f086_debt_paydown_trend_delevpd_252d_jerk_v100_signal,
    f086dpt_f086_debt_paydown_trend_chgxer_21d_jerk_v101_signal,
    f086dpt_f086_debt_paydown_trend_chgxer_63d_jerk_v102_signal,
    f086dpt_f086_debt_paydown_trend_chgxer_252d_jerk_v103_signal,
    f086dpt_f086_debt_paydown_trend_pdxeqd_21d_jerk_v104_signal,
    f086dpt_f086_debt_paydown_trend_pdxeqd_63d_jerk_v105_signal,
    f086dpt_f086_debt_paydown_trend_pdxeqd_252d_jerk_v106_signal,
    f086dpt_f086_debt_paydown_trend_paydowncum_252d_jerk_v107_signal,
    f086dpt_f086_debt_paydown_trend_paydowncum_504d_jerk_v108_signal,
    f086dpt_f086_debt_paydown_trend_paydownrange_21d_jerk_v109_signal,
    f086dpt_f086_debt_paydown_trend_paydownrange_63d_jerk_v110_signal,
    f086dpt_f086_debt_paydown_trend_paydownrange_252d_jerk_v111_signal,
    f086dpt_f086_debt_paydown_trend_pddelevratio_21d_jerk_v112_signal,
    f086dpt_f086_debt_paydown_trend_pddelevratio_63d_jerk_v113_signal,
    f086dpt_f086_debt_paydown_trend_pddelevratio_252d_jerk_v114_signal,
    f086dpt_f086_debt_paydown_trend_chgxleq_21d_jerk_v115_signal,
    f086dpt_f086_debt_paydown_trend_chgxleq_63d_jerk_v116_signal,
    f086dpt_f086_debt_paydown_trend_chgxleq_252d_jerk_v117_signal,
    f086dpt_f086_debt_paydown_trend_delevxsqr_21d_jerk_v118_signal,
    f086dpt_f086_debt_paydown_trend_delevxsqr_63d_jerk_v119_signal,
    f086dpt_f086_debt_paydown_trend_delevxsqr_252d_jerk_v120_signal,
    f086dpt_f086_debt_paydown_trend_pdratio_21v252_jerk_v121_signal,
    f086dpt_f086_debt_paydown_trend_pdratio_63v504_jerk_v122_signal,
    f086dpt_f086_debt_paydown_trend_pddiff_21m63_jerk_v123_signal,
    f086dpt_f086_debt_paydown_trend_pddiff_63m252_jerk_v124_signal,
    f086dpt_f086_debt_paydown_trend_pddiff_21m252_jerk_v125_signal,
    f086dpt_f086_debt_paydown_trend_delevmin_21d_jerk_v126_signal,
    f086dpt_f086_debt_paydown_trend_delevmin_63d_jerk_v127_signal,
    f086dpt_f086_debt_paydown_trend_delevmin_252d_jerk_v128_signal,
    f086dpt_f086_debt_paydown_trend_delevrange_21d_jerk_v129_signal,
    f086dpt_f086_debt_paydown_trend_delevrange_63d_jerk_v130_signal,
    f086dpt_f086_debt_paydown_trend_delevrange_252d_jerk_v131_signal,
    f086dpt_f086_debt_paydown_trend_paydowncount_21d_jerk_v132_signal,
    f086dpt_f086_debt_paydown_trend_paydowncount_63d_jerk_v133_signal,
    f086dpt_f086_debt_paydown_trend_paydowncount_252d_jerk_v134_signal,
    f086dpt_f086_debt_paydown_trend_paydownxeqf_21d_jerk_v135_signal,
    f086dpt_f086_debt_paydown_trend_paydownxeqf_63d_jerk_v136_signal,
    f086dpt_f086_debt_paydown_trend_paydownxeqf_252d_jerk_v137_signal,
    f086dpt_f086_debt_paydown_trend_delevxpd_21d_jerk_v138_signal,
    f086dpt_f086_debt_paydown_trend_delevxpd_63d_jerk_v139_signal,
    f086dpt_f086_debt_paydown_trend_delevxpd_252d_jerk_v140_signal,
    f086dpt_f086_debt_paydown_trend_paydownxld_21d_jerk_v141_signal,
    f086dpt_f086_debt_paydown_trend_paydownxld_63d_jerk_v142_signal,
    f086dpt_f086_debt_paydown_trend_paydownxld_252d_jerk_v143_signal,
    f086dpt_f086_debt_paydown_trend_pdcomp_21d_jerk_v144_signal,
    f086dpt_f086_debt_paydown_trend_pdcomp_252d_jerk_v145_signal,
    f086dpt_f086_debt_paydown_trend_delevfast_21d_jerk_v146_signal,
    f086dpt_f086_debt_paydown_trend_delevfast_42d_jerk_v147_signal,
    f086dpt_f086_debt_paydown_trend_delevmid_126d_jerk_v148_signal,
    f086dpt_f086_debt_paydown_trend_delevslow_252d_jerk_v149_signal,
    f086dpt_f086_debt_paydown_trend_delevslow_504d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F086_DEBT_PAYDOWN_TREND_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    debt = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    equity = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")

    cols = {"closeadj": closeadj, "debt": debt, "equity": equity}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f086_debt_change", "_f086_debt_paydown", "_f086_deleverage_score")
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
    print(f"OK f086_debt_paydown_trend_3rd_derivatives_001_150_claude: {n_features} features pass")
