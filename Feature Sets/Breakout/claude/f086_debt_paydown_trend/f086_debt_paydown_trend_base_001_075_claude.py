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


# ===== folder domain primitives =====
def _f086_debt_change(debt, w):
    return debt.diff(periods=w)


def _f086_debt_paydown(debt, w):
    base = debt.rolling(w, min_periods=max(1, w // 2)).mean()
    return -(debt - base.shift(w)) / base.shift(w).abs().replace(0, np.nan)


def _f086_deleverage_score(debt, equity, w):
    lev = debt / equity.replace(0, np.nan)
    return -(lev - lev.shift(w)) / lev.abs().shift(w).replace(0, np.nan)


# v001 21d debt change scaled by close
def f086dpt_f086_debt_paydown_trend_debtchg_21d_base_v001_signal(debt, closeadj):
    result = _f086_debt_change(debt, 21) / debt.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v002 63d debt change scaled by close
def f086dpt_f086_debt_paydown_trend_debtchg_63d_base_v002_signal(debt, closeadj):
    result = _f086_debt_change(debt, 63) / debt.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v003 126d debt change scaled by close
def f086dpt_f086_debt_paydown_trend_debtchg_126d_base_v003_signal(debt, closeadj):
    result = _f086_debt_change(debt, 126) / debt.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v004 252d debt change scaled by close
def f086dpt_f086_debt_paydown_trend_debtchg_252d_base_v004_signal(debt, closeadj):
    result = _f086_debt_change(debt, 252) / debt.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v005 504d debt change scaled by close
def f086dpt_f086_debt_paydown_trend_debtchg_504d_base_v005_signal(debt, closeadj):
    result = _f086_debt_change(debt, 504) / debt.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v006 21d debt paydown rate × close
def f086dpt_f086_debt_paydown_trend_paydown_21d_base_v006_signal(debt, closeadj):
    result = _f086_debt_paydown(debt, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v007 63d debt paydown rate × close
def f086dpt_f086_debt_paydown_trend_paydown_63d_base_v007_signal(debt, closeadj):
    result = _f086_debt_paydown(debt, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v008 126d debt paydown rate × close
def f086dpt_f086_debt_paydown_trend_paydown_126d_base_v008_signal(debt, closeadj):
    result = _f086_debt_paydown(debt, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v009 252d debt paydown rate × close
def f086dpt_f086_debt_paydown_trend_paydown_252d_base_v009_signal(debt, closeadj):
    result = _f086_debt_paydown(debt, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v010 504d debt paydown rate × close
def f086dpt_f086_debt_paydown_trend_paydown_504d_base_v010_signal(debt, closeadj):
    result = _f086_debt_paydown(debt, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v011 21d deleverage score × close
def f086dpt_f086_debt_paydown_trend_delev_21d_base_v011_signal(debt, equity, closeadj):
    result = _f086_deleverage_score(debt, equity, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v012 63d deleverage score × close
def f086dpt_f086_debt_paydown_trend_delev_63d_base_v012_signal(debt, equity, closeadj):
    result = _f086_deleverage_score(debt, equity, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v013 126d deleverage score × close
def f086dpt_f086_debt_paydown_trend_delev_126d_base_v013_signal(debt, equity, closeadj):
    result = _f086_deleverage_score(debt, equity, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v014 252d deleverage score × close
def f086dpt_f086_debt_paydown_trend_delev_252d_base_v014_signal(debt, equity, closeadj):
    result = _f086_deleverage_score(debt, equity, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v015 504d deleverage score × close
def f086dpt_f086_debt_paydown_trend_delev_504d_base_v015_signal(debt, equity, closeadj):
    result = _f086_deleverage_score(debt, equity, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v016 21d debt change × equity ratio
def f086dpt_f086_debt_paydown_trend_chgxeq_21d_base_v016_signal(debt, equity, closeadj):
    base = _f086_debt_change(debt, 21) / equity.abs().replace(0, np.nan)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v017 63d debt change × equity ratio
def f086dpt_f086_debt_paydown_trend_chgxeq_63d_base_v017_signal(debt, equity, closeadj):
    base = _f086_debt_change(debt, 63) / equity.abs().replace(0, np.nan)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v018 252d debt change × equity ratio
def f086dpt_f086_debt_paydown_trend_chgxeq_252d_base_v018_signal(debt, equity, closeadj):
    base = _f086_debt_change(debt, 252) / equity.abs().replace(0, np.nan)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v019 504d debt change × equity ratio
def f086dpt_f086_debt_paydown_trend_chgxeq_504d_base_v019_signal(debt, equity, closeadj):
    base = _f086_debt_change(debt, 504) / equity.abs().replace(0, np.nan)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v020 21d EMA of paydown × close
def f086dpt_f086_debt_paydown_trend_paydownema_21d_base_v020_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 21)
    result = base.ewm(span=21, min_periods=10).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v021 63d EMA of paydown × close
def f086dpt_f086_debt_paydown_trend_paydownema_63d_base_v021_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 63)
    result = base.ewm(span=63, min_periods=30).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v022 252d EMA of paydown × close
def f086dpt_f086_debt_paydown_trend_paydownema_252d_base_v022_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 252)
    result = base.ewm(span=126, min_periods=60).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v023 21d zscore of debt change × close (252d window)
def f086dpt_f086_debt_paydown_trend_chgz_21d_base_v023_signal(debt, closeadj):
    base = _f086_debt_change(debt, 21) / debt.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v024 63d zscore of debt change × close
def f086dpt_f086_debt_paydown_trend_chgz_63d_base_v024_signal(debt, closeadj):
    base = _f086_debt_change(debt, 63) / debt.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v025 252d zscore of debt change × close
def f086dpt_f086_debt_paydown_trend_chgz_252d_base_v025_signal(debt, closeadj):
    base = _f086_debt_change(debt, 252) / debt.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v026 21d zscore of paydown × close
def f086dpt_f086_debt_paydown_trend_paydownz_21d_base_v026_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 21)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v027 63d zscore of paydown × close
def f086dpt_f086_debt_paydown_trend_paydownz_63d_base_v027_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v028 252d zscore of paydown × close
def f086dpt_f086_debt_paydown_trend_paydownz_252d_base_v028_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v029 21d std of debt change × close
def f086dpt_f086_debt_paydown_trend_chgstd_21d_base_v029_signal(debt, closeadj):
    base = _f086_debt_change(debt, 21) / debt.abs().replace(0, np.nan)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v030 63d std of debt change × close
def f086dpt_f086_debt_paydown_trend_chgstd_63d_base_v030_signal(debt, closeadj):
    base = _f086_debt_change(debt, 63) / debt.abs().replace(0, np.nan)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v031 252d std of debt change × close
def f086dpt_f086_debt_paydown_trend_chgstd_252d_base_v031_signal(debt, closeadj):
    base = _f086_debt_change(debt, 252) / debt.abs().replace(0, np.nan)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v032 21d paydown × equity scale
def f086dpt_f086_debt_paydown_trend_paydownxeq_21d_base_v032_signal(debt, equity, closeadj):
    base = _f086_debt_paydown(debt, 21) * equity / debt.abs().replace(0, np.nan)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v033 63d paydown × equity scale
def f086dpt_f086_debt_paydown_trend_paydownxeq_63d_base_v033_signal(debt, equity, closeadj):
    base = _f086_debt_paydown(debt, 63) * equity / debt.abs().replace(0, np.nan)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v034 252d paydown × equity scale
def f086dpt_f086_debt_paydown_trend_paydownxeq_252d_base_v034_signal(debt, equity, closeadj):
    base = _f086_debt_paydown(debt, 252) * equity / debt.abs().replace(0, np.nan)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v035 21d deleverage zscore × close
def f086dpt_f086_debt_paydown_trend_delevz_21d_base_v035_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 21)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v036 63d deleverage zscore × close
def f086dpt_f086_debt_paydown_trend_delevz_63d_base_v036_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v037 252d deleverage zscore × close
def f086dpt_f086_debt_paydown_trend_delevz_252d_base_v037_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v038 21d deleverage EMA × close
def f086dpt_f086_debt_paydown_trend_delevema_21d_base_v038_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 21)
    result = base.ewm(span=21, min_periods=10).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v039 63d deleverage EMA × close
def f086dpt_f086_debt_paydown_trend_delevema_63d_base_v039_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 63)
    result = base.ewm(span=63, min_periods=30).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v040 252d deleverage EMA × close
def f086dpt_f086_debt_paydown_trend_delevema_252d_base_v040_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 252)
    result = base.ewm(span=126, min_periods=60).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v041 21d debt change × close × sign
def f086dpt_f086_debt_paydown_trend_chgsign_21d_base_v041_signal(debt, closeadj):
    base = _f086_debt_change(debt, 21) / debt.abs().replace(0, np.nan)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v042 63d debt change sign × sqrt magnitude × close
def f086dpt_f086_debt_paydown_trend_chgsign_63d_base_v042_signal(debt, closeadj):
    base = _f086_debt_change(debt, 63) / debt.abs().replace(0, np.nan)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v043 252d debt change sign × sqrt magnitude × close
def f086dpt_f086_debt_paydown_trend_chgsign_252d_base_v043_signal(debt, closeadj):
    base = _f086_debt_change(debt, 252) / debt.abs().replace(0, np.nan)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v044 21d 5d window debt change × close
def f086dpt_f086_debt_paydown_trend_debtchg_5d_base_v044_signal(debt, closeadj):
    result = _f086_debt_change(debt, 5) / debt.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v045 10d window debt change × close
def f086dpt_f086_debt_paydown_trend_debtchg_10d_base_v045_signal(debt, closeadj):
    result = _f086_debt_change(debt, 10) / debt.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v046 42d window debt change × close
def f086dpt_f086_debt_paydown_trend_debtchg_42d_base_v046_signal(debt, closeadj):
    result = _f086_debt_change(debt, 42) / debt.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v047 189d window debt change × close
def f086dpt_f086_debt_paydown_trend_debtchg_189d_base_v047_signal(debt, closeadj):
    result = _f086_debt_change(debt, 189) / debt.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v048 378d window debt change × close
def f086dpt_f086_debt_paydown_trend_debtchg_378d_base_v048_signal(debt, closeadj):
    result = _f086_debt_change(debt, 378) / debt.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v049 5d paydown × close
def f086dpt_f086_debt_paydown_trend_paydown_5d_base_v049_signal(debt, closeadj):
    result = _f086_debt_paydown(debt, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v050 10d paydown × close
def f086dpt_f086_debt_paydown_trend_paydown_10d_base_v050_signal(debt, closeadj):
    result = _f086_debt_paydown(debt, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v051 42d paydown × close
def f086dpt_f086_debt_paydown_trend_paydown_42d_base_v051_signal(debt, closeadj):
    result = _f086_debt_paydown(debt, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v052 189d paydown × close
def f086dpt_f086_debt_paydown_trend_paydown_189d_base_v052_signal(debt, closeadj):
    result = _f086_debt_paydown(debt, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v053 378d paydown × close
def f086dpt_f086_debt_paydown_trend_paydown_378d_base_v053_signal(debt, closeadj):
    result = _f086_debt_paydown(debt, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v054 42d deleverage × close
def f086dpt_f086_debt_paydown_trend_delev_42d_base_v054_signal(debt, equity, closeadj):
    result = _f086_deleverage_score(debt, equity, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v055 189d deleverage × close
def f086dpt_f086_debt_paydown_trend_delev_189d_base_v055_signal(debt, equity, closeadj):
    result = _f086_deleverage_score(debt, equity, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v056 378d deleverage × close
def f086dpt_f086_debt_paydown_trend_delev_378d_base_v056_signal(debt, equity, closeadj):
    result = _f086_deleverage_score(debt, equity, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v057 21d mean of paydown × close
def f086dpt_f086_debt_paydown_trend_paydownmean_21d_base_v057_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v058 63d mean of paydown × close
def f086dpt_f086_debt_paydown_trend_paydownmean_63d_base_v058_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v059 252d mean of paydown × close
def f086dpt_f086_debt_paydown_trend_paydownmean_252d_base_v059_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v060 21d paydown × log(close)
def f086dpt_f086_debt_paydown_trend_paydownxlog_21d_base_v060_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 21)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# v061 63d paydown × log(close)
def f086dpt_f086_debt_paydown_trend_paydownxlog_63d_base_v061_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 63)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# v062 252d paydown × log(close)
def f086dpt_f086_debt_paydown_trend_paydownxlog_252d_base_v062_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 252)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# v063 21d paydown × close/equity
def f086dpt_f086_debt_paydown_trend_paydownxce_21d_base_v063_signal(debt, equity, closeadj):
    base = _f086_debt_paydown(debt, 21)
    result = base * closeadj * 1e8 / equity.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v064 63d paydown × close/equity
def f086dpt_f086_debt_paydown_trend_paydownxce_63d_base_v064_signal(debt, equity, closeadj):
    base = _f086_debt_paydown(debt, 63)
    result = base * closeadj * 1e8 / equity.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v065 252d paydown × close/equity
def f086dpt_f086_debt_paydown_trend_paydownxce_252d_base_v065_signal(debt, equity, closeadj):
    base = _f086_debt_paydown(debt, 252)
    result = base * closeadj * 1e8 / equity.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v066 21d paydown squared × close
def f086dpt_f086_debt_paydown_trend_paydownsq_21d_base_v066_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 21)
    result = (base * base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v067 63d paydown squared × close
def f086dpt_f086_debt_paydown_trend_paydownsq_63d_base_v067_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 63)
    result = (base * base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v068 252d paydown squared × close
def f086dpt_f086_debt_paydown_trend_paydownsq_252d_base_v068_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 252)
    result = (base * base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v069 21d max paydown × close
def f086dpt_f086_debt_paydown_trend_paydownmax_21d_base_v069_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 21)
    result = base.rolling(63, min_periods=21).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v070 63d max paydown × close
def f086dpt_f086_debt_paydown_trend_paydownmax_63d_base_v070_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 63)
    result = base.rolling(126, min_periods=42).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v071 252d max paydown × close
def f086dpt_f086_debt_paydown_trend_paydownmax_252d_base_v071_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 252)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v072 21d sum of paydown × close
def f086dpt_f086_debt_paydown_trend_paydownsum_21d_base_v072_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 21)
    result = base.rolling(63, min_periods=21).sum() * closeadj / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


# v073 63d sum of paydown × close
def f086dpt_f086_debt_paydown_trend_paydownsum_63d_base_v073_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 63)
    result = base.rolling(126, min_periods=42).sum() * closeadj / 126.0
    return result.replace([np.inf, -np.inf], np.nan)


# v074 252d sum of paydown × close
def f086dpt_f086_debt_paydown_trend_paydownsum_252d_base_v074_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 252)
    result = base.rolling(252, min_periods=63).sum() * closeadj / 252.0
    return result.replace([np.inf, -np.inf], np.nan)


# v075 21d paydown × equity growth (composite deleverage)
def f086dpt_f086_debt_paydown_trend_compdelev_21d_base_v075_signal(debt, equity, closeadj):
    base = _f086_debt_paydown(debt, 21)
    eq_g = (equity - equity.shift(21)) / equity.abs().shift(21).replace(0, np.nan)
    result = (base + eq_g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f086dpt_f086_debt_paydown_trend_debtchg_21d_base_v001_signal,
    f086dpt_f086_debt_paydown_trend_debtchg_63d_base_v002_signal,
    f086dpt_f086_debt_paydown_trend_debtchg_126d_base_v003_signal,
    f086dpt_f086_debt_paydown_trend_debtchg_252d_base_v004_signal,
    f086dpt_f086_debt_paydown_trend_debtchg_504d_base_v005_signal,
    f086dpt_f086_debt_paydown_trend_paydown_21d_base_v006_signal,
    f086dpt_f086_debt_paydown_trend_paydown_63d_base_v007_signal,
    f086dpt_f086_debt_paydown_trend_paydown_126d_base_v008_signal,
    f086dpt_f086_debt_paydown_trend_paydown_252d_base_v009_signal,
    f086dpt_f086_debt_paydown_trend_paydown_504d_base_v010_signal,
    f086dpt_f086_debt_paydown_trend_delev_21d_base_v011_signal,
    f086dpt_f086_debt_paydown_trend_delev_63d_base_v012_signal,
    f086dpt_f086_debt_paydown_trend_delev_126d_base_v013_signal,
    f086dpt_f086_debt_paydown_trend_delev_252d_base_v014_signal,
    f086dpt_f086_debt_paydown_trend_delev_504d_base_v015_signal,
    f086dpt_f086_debt_paydown_trend_chgxeq_21d_base_v016_signal,
    f086dpt_f086_debt_paydown_trend_chgxeq_63d_base_v017_signal,
    f086dpt_f086_debt_paydown_trend_chgxeq_252d_base_v018_signal,
    f086dpt_f086_debt_paydown_trend_chgxeq_504d_base_v019_signal,
    f086dpt_f086_debt_paydown_trend_paydownema_21d_base_v020_signal,
    f086dpt_f086_debt_paydown_trend_paydownema_63d_base_v021_signal,
    f086dpt_f086_debt_paydown_trend_paydownema_252d_base_v022_signal,
    f086dpt_f086_debt_paydown_trend_chgz_21d_base_v023_signal,
    f086dpt_f086_debt_paydown_trend_chgz_63d_base_v024_signal,
    f086dpt_f086_debt_paydown_trend_chgz_252d_base_v025_signal,
    f086dpt_f086_debt_paydown_trend_paydownz_21d_base_v026_signal,
    f086dpt_f086_debt_paydown_trend_paydownz_63d_base_v027_signal,
    f086dpt_f086_debt_paydown_trend_paydownz_252d_base_v028_signal,
    f086dpt_f086_debt_paydown_trend_chgstd_21d_base_v029_signal,
    f086dpt_f086_debt_paydown_trend_chgstd_63d_base_v030_signal,
    f086dpt_f086_debt_paydown_trend_chgstd_252d_base_v031_signal,
    f086dpt_f086_debt_paydown_trend_paydownxeq_21d_base_v032_signal,
    f086dpt_f086_debt_paydown_trend_paydownxeq_63d_base_v033_signal,
    f086dpt_f086_debt_paydown_trend_paydownxeq_252d_base_v034_signal,
    f086dpt_f086_debt_paydown_trend_delevz_21d_base_v035_signal,
    f086dpt_f086_debt_paydown_trend_delevz_63d_base_v036_signal,
    f086dpt_f086_debt_paydown_trend_delevz_252d_base_v037_signal,
    f086dpt_f086_debt_paydown_trend_delevema_21d_base_v038_signal,
    f086dpt_f086_debt_paydown_trend_delevema_63d_base_v039_signal,
    f086dpt_f086_debt_paydown_trend_delevema_252d_base_v040_signal,
    f086dpt_f086_debt_paydown_trend_chgsign_21d_base_v041_signal,
    f086dpt_f086_debt_paydown_trend_chgsign_63d_base_v042_signal,
    f086dpt_f086_debt_paydown_trend_chgsign_252d_base_v043_signal,
    f086dpt_f086_debt_paydown_trend_debtchg_5d_base_v044_signal,
    f086dpt_f086_debt_paydown_trend_debtchg_10d_base_v045_signal,
    f086dpt_f086_debt_paydown_trend_debtchg_42d_base_v046_signal,
    f086dpt_f086_debt_paydown_trend_debtchg_189d_base_v047_signal,
    f086dpt_f086_debt_paydown_trend_debtchg_378d_base_v048_signal,
    f086dpt_f086_debt_paydown_trend_paydown_5d_base_v049_signal,
    f086dpt_f086_debt_paydown_trend_paydown_10d_base_v050_signal,
    f086dpt_f086_debt_paydown_trend_paydown_42d_base_v051_signal,
    f086dpt_f086_debt_paydown_trend_paydown_189d_base_v052_signal,
    f086dpt_f086_debt_paydown_trend_paydown_378d_base_v053_signal,
    f086dpt_f086_debt_paydown_trend_delev_42d_base_v054_signal,
    f086dpt_f086_debt_paydown_trend_delev_189d_base_v055_signal,
    f086dpt_f086_debt_paydown_trend_delev_378d_base_v056_signal,
    f086dpt_f086_debt_paydown_trend_paydownmean_21d_base_v057_signal,
    f086dpt_f086_debt_paydown_trend_paydownmean_63d_base_v058_signal,
    f086dpt_f086_debt_paydown_trend_paydownmean_252d_base_v059_signal,
    f086dpt_f086_debt_paydown_trend_paydownxlog_21d_base_v060_signal,
    f086dpt_f086_debt_paydown_trend_paydownxlog_63d_base_v061_signal,
    f086dpt_f086_debt_paydown_trend_paydownxlog_252d_base_v062_signal,
    f086dpt_f086_debt_paydown_trend_paydownxce_21d_base_v063_signal,
    f086dpt_f086_debt_paydown_trend_paydownxce_63d_base_v064_signal,
    f086dpt_f086_debt_paydown_trend_paydownxce_252d_base_v065_signal,
    f086dpt_f086_debt_paydown_trend_paydownsq_21d_base_v066_signal,
    f086dpt_f086_debt_paydown_trend_paydownsq_63d_base_v067_signal,
    f086dpt_f086_debt_paydown_trend_paydownsq_252d_base_v068_signal,
    f086dpt_f086_debt_paydown_trend_paydownmax_21d_base_v069_signal,
    f086dpt_f086_debt_paydown_trend_paydownmax_63d_base_v070_signal,
    f086dpt_f086_debt_paydown_trend_paydownmax_252d_base_v071_signal,
    f086dpt_f086_debt_paydown_trend_paydownsum_21d_base_v072_signal,
    f086dpt_f086_debt_paydown_trend_paydownsum_63d_base_v073_signal,
    f086dpt_f086_debt_paydown_trend_paydownsum_252d_base_v074_signal,
    f086dpt_f086_debt_paydown_trend_compdelev_21d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F086_DEBT_PAYDOWN_TREND_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f086_debt_paydown_trend_base_001_075_claude: {n_features} features pass")
