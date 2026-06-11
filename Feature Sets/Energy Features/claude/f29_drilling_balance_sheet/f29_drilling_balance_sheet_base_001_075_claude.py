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
def _f29_net_debt(debt, cashneq):
    return debt - cashneq


def _f29_leverage_dynamics(debt, equity, w):
    lev = debt / equity.replace(0, np.nan)
    return lev.rolling(w, min_periods=max(1, w // 2)).mean()


def _f29_balance_sheet_resilience(debt, ebitda, w):
    ratio = ebitda / debt.replace(0, np.nan)
    return ratio.rolling(w, min_periods=max(1, w // 2)).mean()


# ===== features =====

def f29dbs_f29_drilling_balance_sheet_netdebt_base_xc_base_v001_signal(debt, cashneq, closeadj):
    base = _f29_net_debt(debt, cashneq)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_5d_base_xc_base_v002_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 5)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_5d_base_xc_base_v003_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 5)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_10d_base_xc_base_v004_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 10)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_10d_base_xc_base_v005_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 10)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_21d_base_xc_base_v006_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 21)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_21d_base_xc_base_v007_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 21)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_42d_base_xc_base_v008_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 42)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_42d_base_xc_base_v009_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 42)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_63d_base_xc_base_v010_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 63)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_63d_base_xc_base_v011_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 63)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_84d_base_xc_base_v012_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 84)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_84d_base_xc_base_v013_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 84)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_126d_base_xc_base_v014_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 126)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_126d_base_xc_base_v015_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 126)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_189d_base_xc_base_v016_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 189)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_189d_base_xc_base_v017_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 189)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_252d_base_xc_base_v018_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 252)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_252d_base_xc_base_v019_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 252)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_378d_base_xc_base_v020_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 378)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_378d_base_xc_base_v021_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 378)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_504d_base_xc_base_v022_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 504)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_504d_base_xc_base_v023_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 504)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_netdebt_base_xc2_base_v024_signal(debt, cashneq, closeadj):
    base = _f29_net_debt(debt, cashneq)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_5d_base_xc2_base_v025_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 5)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_5d_base_xc2_base_v026_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 5)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_10d_base_xc2_base_v027_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 10)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_10d_base_xc2_base_v028_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 10)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_21d_base_xc2_base_v029_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 21)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_21d_base_xc2_base_v030_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 21)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_42d_base_xc2_base_v031_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 42)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_42d_base_xc2_base_v032_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 42)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_63d_base_xc2_base_v033_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 63)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_63d_base_xc2_base_v034_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 63)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_84d_base_xc2_base_v035_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 84)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_84d_base_xc2_base_v036_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 84)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_126d_base_xc2_base_v037_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 126)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_126d_base_xc2_base_v038_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 126)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_189d_base_xc2_base_v039_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 189)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_189d_base_xc2_base_v040_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 189)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_252d_base_xc2_base_v041_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 252)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_252d_base_xc2_base_v042_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 252)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_378d_base_xc2_base_v043_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 378)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_378d_base_xc2_base_v044_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 378)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_504d_base_xc2_base_v045_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 504)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_504d_base_xc2_base_v046_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 504)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_netdebt_base_xmc_base_v047_signal(debt, cashneq, closeadj):
    base = _f29_net_debt(debt, cashneq)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_5d_base_xmc_base_v048_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 5)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_5d_base_xmc_base_v049_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 5)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_10d_base_xmc_base_v050_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 10)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_10d_base_xmc_base_v051_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 10)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_21d_base_xmc_base_v052_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 21)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_21d_base_xmc_base_v053_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 21)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_42d_base_xmc_base_v054_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 42)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_42d_base_xmc_base_v055_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 42)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_63d_base_xmc_base_v056_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 63)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_63d_base_xmc_base_v057_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 63)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_84d_base_xmc_base_v058_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 84)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_84d_base_xmc_base_v059_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 84)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_126d_base_xmc_base_v060_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 126)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_126d_base_xmc_base_v061_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 126)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_189d_base_xmc_base_v062_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 189)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_189d_base_xmc_base_v063_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 189)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_252d_base_xmc_base_v064_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 252)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_252d_base_xmc_base_v065_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 252)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_378d_base_xmc_base_v066_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 378)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_378d_base_xmc_base_v067_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 378)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_504d_base_xmc_base_v068_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 504)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_504d_base_xmc_base_v069_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 504)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_netdebt_base_xzc_base_v070_signal(debt, cashneq, closeadj):
    base = _f29_net_debt(debt, cashneq)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_5d_base_xzc_base_v071_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 5)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_5d_base_xzc_base_v072_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 5)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_10d_base_xzc_base_v073_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 10)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_10d_base_xzc_base_v074_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 10)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_21d_base_xzc_base_v075_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 21)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f29dbs_f29_drilling_balance_sheet_netdebt_base_xc_base_v001_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_5d_base_xc_base_v002_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_5d_base_xc_base_v003_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_10d_base_xc_base_v004_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_10d_base_xc_base_v005_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_21d_base_xc_base_v006_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_21d_base_xc_base_v007_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_42d_base_xc_base_v008_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_42d_base_xc_base_v009_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_63d_base_xc_base_v010_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_63d_base_xc_base_v011_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_84d_base_xc_base_v012_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_84d_base_xc_base_v013_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_126d_base_xc_base_v014_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_126d_base_xc_base_v015_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_189d_base_xc_base_v016_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_189d_base_xc_base_v017_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_252d_base_xc_base_v018_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_252d_base_xc_base_v019_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_378d_base_xc_base_v020_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_378d_base_xc_base_v021_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_504d_base_xc_base_v022_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_504d_base_xc_base_v023_signal,
    f29dbs_f29_drilling_balance_sheet_netdebt_base_xc2_base_v024_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_5d_base_xc2_base_v025_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_5d_base_xc2_base_v026_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_10d_base_xc2_base_v027_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_10d_base_xc2_base_v028_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_21d_base_xc2_base_v029_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_21d_base_xc2_base_v030_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_42d_base_xc2_base_v031_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_42d_base_xc2_base_v032_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_63d_base_xc2_base_v033_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_63d_base_xc2_base_v034_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_84d_base_xc2_base_v035_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_84d_base_xc2_base_v036_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_126d_base_xc2_base_v037_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_126d_base_xc2_base_v038_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_189d_base_xc2_base_v039_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_189d_base_xc2_base_v040_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_252d_base_xc2_base_v041_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_252d_base_xc2_base_v042_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_378d_base_xc2_base_v043_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_378d_base_xc2_base_v044_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_504d_base_xc2_base_v045_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_504d_base_xc2_base_v046_signal,
    f29dbs_f29_drilling_balance_sheet_netdebt_base_xmc_base_v047_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_5d_base_xmc_base_v048_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_5d_base_xmc_base_v049_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_10d_base_xmc_base_v050_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_10d_base_xmc_base_v051_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_21d_base_xmc_base_v052_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_21d_base_xmc_base_v053_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_42d_base_xmc_base_v054_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_42d_base_xmc_base_v055_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_63d_base_xmc_base_v056_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_63d_base_xmc_base_v057_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_84d_base_xmc_base_v058_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_84d_base_xmc_base_v059_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_126d_base_xmc_base_v060_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_126d_base_xmc_base_v061_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_189d_base_xmc_base_v062_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_189d_base_xmc_base_v063_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_252d_base_xmc_base_v064_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_252d_base_xmc_base_v065_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_378d_base_xmc_base_v066_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_378d_base_xmc_base_v067_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_504d_base_xmc_base_v068_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_504d_base_xmc_base_v069_signal,
    f29dbs_f29_drilling_balance_sheet_netdebt_base_xzc_base_v070_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_5d_base_xzc_base_v071_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_5d_base_xzc_base_v072_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_10d_base_xzc_base_v073_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_10d_base_xzc_base_v074_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_21d_base_xzc_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F29_DRILLING_BALANCE_SHEET_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda,
        "assets": assets, "equity": equity, "debt": debt, "cashneq": cashneq,
        "deferredrev": deferredrev, "ppnenet": ppnenet, "ebitdamargin": ebitdamargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f29_net_debt', '_f29_leverage_dynamics', '_f29_balance_sheet_resilience',)
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
    print(f"OK f29_drilling_balance_sheet_base_001_075_claude: {n_features} features pass")
