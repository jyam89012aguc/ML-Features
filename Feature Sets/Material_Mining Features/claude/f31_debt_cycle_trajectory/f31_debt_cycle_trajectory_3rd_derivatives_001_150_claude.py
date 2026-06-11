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



def f31dt_f31_debt_cycle_trajectory_debtz_42d_jerk_v001_signal(debt):
    base = _z(debt, 42)
    d1 = base - base.shift(10)
    d2 = d1 - d1.shift(10)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_debtz_126d_jerk_v002_signal(debt):
    base = _z(debt, 126)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_debtz_252d_jerk_v003_signal(debt):
    base = _z(debt, 252)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_debtz_378d_jerk_v004_signal(debt):
    base = _z(debt, 378)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_debtz_504d_jerk_v005_signal(debt):
    base = _z(debt, 504)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_debtslope_42d_jerk_v006_signal(debt):
    base = np.log(debt.replace(0, np.nan)) - np.log(debt.shift(42).replace(0, np.nan))
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_debtslope_126d_jerk_v007_signal(debt):
    base = np.log(debt.replace(0, np.nan)) - np.log(debt.shift(126).replace(0, np.nan))
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_debtslope_252d_jerk_v008_signal(debt):
    base = np.log(debt.replace(0, np.nan)) - np.log(debt.shift(252).replace(0, np.nan))
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_debtslope_378d_jerk_v009_signal(debt):
    base = np.log(debt.replace(0, np.nan)) - np.log(debt.shift(378).replace(0, np.nan))
    d1 = base - base.shift(84)
    d2 = d1 - d1.shift(84)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_debtslope_504d_jerk_v010_signal(debt):
    base = np.log(debt.replace(0, np.nan)) - np.log(debt.shift(504).replace(0, np.nan))
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_netz_42d_jerk_v011_signal(debt, cashneq):
    nd = debt - cashneq
    base = _z(nd, 42)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_netz_126d_jerk_v012_signal(debt, cashneq):
    nd = debt - cashneq
    base = _z(nd, 126)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_netz_252d_jerk_v013_signal(debt, cashneq):
    nd = debt - cashneq
    base = _z(nd, 252)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_netz_378d_jerk_v014_signal(debt, cashneq):
    nd = debt - cashneq
    base = _z(nd, 378)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_netz_504d_jerk_v015_signal(debt, cashneq):
    nd = debt - cashneq
    base = _z(nd, 504)
    d1 = base - base.shift(84)
    d2 = d1 - d1.shift(84)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_netchg_42d_jerk_v016_signal(debt, cashneq):
    nd = debt - cashneq
    base = (nd - nd.shift(42)) / nd.shift(42).abs().replace(0, np.nan)
    d1 = base - base.shift(10)
    d2 = d1 - d1.shift(10)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_netchg_126d_jerk_v017_signal(debt, cashneq):
    nd = debt - cashneq
    base = (nd - nd.shift(126)) / nd.shift(126).abs().replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_netchg_252d_jerk_v018_signal(debt, cashneq):
    nd = debt - cashneq
    base = (nd - nd.shift(252)) / nd.shift(252).abs().replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_netchg_378d_jerk_v019_signal(debt, cashneq):
    nd = debt - cashneq
    base = (nd - nd.shift(378)) / nd.shift(378).abs().replace(0, np.nan)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_netchg_504d_jerk_v020_signal(debt, cashneq):
    nd = debt - cashneq
    base = (nd - nd.shift(504)) / nd.shift(504).abs().replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_shortsh_42d_jerk_v021_signal(debtc, debtnc):
    tot = (debtc + debtnc).replace(0, np.nan)
    base = (debtc / tot).rolling(42, min_periods=max(1, 42 // 2)).mean()
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_shortsh_126d_jerk_v022_signal(debtc, debtnc):
    tot = (debtc + debtnc).replace(0, np.nan)
    base = (debtc / tot).rolling(126, min_periods=max(1, 126 // 2)).mean()
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_shortsh_252d_jerk_v023_signal(debtc, debtnc):
    tot = (debtc + debtnc).replace(0, np.nan)
    base = (debtc / tot).rolling(252, min_periods=max(1, 252 // 2)).mean()
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_shortsh_378d_jerk_v024_signal(debtc, debtnc):
    tot = (debtc + debtnc).replace(0, np.nan)
    base = (debtc / tot).rolling(378, min_periods=max(1, 378 // 2)).mean()
    d1 = base - base.shift(84)
    d2 = d1 - d1.shift(84)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_shortsh_504d_jerk_v025_signal(debtc, debtnc):
    tot = (debtc + debtnc).replace(0, np.nan)
    base = (debtc / tot).rolling(504, min_periods=max(1, 504 // 2)).mean()
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_cashcov_42d_jerk_v026_signal(debt, cashneq):
    cov = cashneq / debt.replace(0, np.nan)
    base = cov.rolling(42, min_periods=max(1, 42 // 2)).mean()
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_cashcov_126d_jerk_v027_signal(debt, cashneq):
    cov = cashneq / debt.replace(0, np.nan)
    base = cov.rolling(126, min_periods=max(1, 126 // 2)).mean()
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_cashcov_252d_jerk_v028_signal(debt, cashneq):
    cov = cashneq / debt.replace(0, np.nan)
    base = cov.rolling(252, min_periods=max(1, 252 // 2)).mean()
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_cashcov_378d_jerk_v029_signal(debt, cashneq):
    cov = cashneq / debt.replace(0, np.nan)
    base = cov.rolling(378, min_periods=max(1, 378 // 2)).mean()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_cashcov_504d_jerk_v030_signal(debt, cashneq):
    cov = cashneq / debt.replace(0, np.nan)
    base = cov.rolling(504, min_periods=max(1, 504 // 2)).mean()
    d1 = base - base.shift(84)
    d2 = d1 - d1.shift(84)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_dcashrank_42d_jerk_v031_signal(debt, cashneq):
    r = debt / cashneq.replace(0, np.nan)
    base = r.rolling(42, min_periods=max(1, 42 // 2)).rank(pct=True) - 0.5
    d1 = base - base.shift(10)
    d2 = d1 - d1.shift(10)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_dcashrank_126d_jerk_v032_signal(debt, cashneq):
    r = debt / cashneq.replace(0, np.nan)
    base = r.rolling(126, min_periods=max(1, 126 // 2)).rank(pct=True) - 0.5
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_dcashrank_252d_jerk_v033_signal(debt, cashneq):
    r = debt / cashneq.replace(0, np.nan)
    base = r.rolling(252, min_periods=max(1, 252 // 2)).rank(pct=True) - 0.5
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_dcashrank_378d_jerk_v034_signal(debt, cashneq):
    r = debt / cashneq.replace(0, np.nan)
    base = r.rolling(378, min_periods=max(1, 378 // 2)).rank(pct=True) - 0.5
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_dcashrank_504d_jerk_v035_signal(debt, cashneq):
    r = debt / cashneq.replace(0, np.nan)
    base = r.rolling(504, min_periods=max(1, 504 // 2)).rank(pct=True) - 0.5
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_flowsm_42d_jerk_v036_signal(ncfdebt, debt):
    base = ncfdebt.rolling(42, min_periods=max(1, 42 // 2)).mean() / debt.replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_flowsm_126d_jerk_v037_signal(ncfdebt, debt):
    base = ncfdebt.rolling(126, min_periods=max(1, 126 // 2)).mean() / debt.replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_flowsm_252d_jerk_v038_signal(ncfdebt, debt):
    base = ncfdebt.rolling(252, min_periods=max(1, 252 // 2)).mean() / debt.replace(0, np.nan)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_flowsm_378d_jerk_v039_signal(ncfdebt, debt):
    base = ncfdebt.rolling(378, min_periods=max(1, 378 // 2)).mean() / debt.replace(0, np.nan)
    d1 = base - base.shift(84)
    d2 = d1 - d1.shift(84)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_flowsm_504d_jerk_v040_signal(ncfdebt, debt):
    base = ncfdebt.rolling(504, min_periods=max(1, 504 // 2)).mean() / debt.replace(0, np.nan)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_peakdist_42d_jerk_v041_signal(debt):
    hi = debt.rolling(42, min_periods=max(1, 42 // 2)).max()
    base = debt / hi.replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_peakdist_126d_jerk_v042_signal(debt):
    hi = debt.rolling(126, min_periods=max(1, 126 // 2)).max()
    base = debt / hi.replace(0, np.nan)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_peakdist_252d_jerk_v043_signal(debt):
    hi = debt.rolling(252, min_periods=max(1, 252 // 2)).max()
    base = debt / hi.replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_peakdist_378d_jerk_v044_signal(debt):
    hi = debt.rolling(378, min_periods=max(1, 378 // 2)).max()
    base = debt / hi.replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_peakdist_504d_jerk_v045_signal(debt):
    hi = debt.rolling(504, min_periods=max(1, 504 // 2)).max()
    base = debt / hi.replace(0, np.nan)
    d1 = base - base.shift(84)
    d2 = d1 - d1.shift(84)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_debtcyc_42d_jerk_v046_signal(debt):
    hi = debt.rolling(42, min_periods=max(1, 42 // 2)).max()
    lo = debt.rolling(42, min_periods=max(1, 42 // 2)).min()
    base = (debt - lo) / (hi - lo).replace(0, np.nan)
    d1 = base - base.shift(10)
    d2 = d1 - d1.shift(10)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_debtcyc_126d_jerk_v047_signal(debt):
    hi = debt.rolling(126, min_periods=max(1, 126 // 2)).max()
    lo = debt.rolling(126, min_periods=max(1, 126 // 2)).min()
    base = (debt - lo) / (hi - lo).replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_debtcyc_252d_jerk_v048_signal(debt):
    hi = debt.rolling(252, min_periods=max(1, 252 // 2)).max()
    lo = debt.rolling(252, min_periods=max(1, 252 // 2)).min()
    base = (debt - lo) / (hi - lo).replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_debtcyc_378d_jerk_v049_signal(debt):
    hi = debt.rolling(378, min_periods=max(1, 378 // 2)).max()
    lo = debt.rolling(378, min_periods=max(1, 378 // 2)).min()
    base = (debt - lo) / (hi - lo).replace(0, np.nan)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_debtcyc_504d_jerk_v050_signal(debt):
    hi = debt.rolling(504, min_periods=max(1, 504 // 2)).max()
    lo = debt.rolling(504, min_periods=max(1, 504 // 2)).min()
    base = (debt - lo) / (hi - lo).replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_netcyc_42d_jerk_v051_signal(debt, cashneq):
    nd = debt - cashneq
    hi = nd.rolling(42, min_periods=max(1, 42 // 2)).max()
    lo = nd.rolling(42, min_periods=max(1, 42 // 2)).min()
    base = (nd - lo) / (hi - lo).replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_netcyc_126d_jerk_v052_signal(debt, cashneq):
    nd = debt - cashneq
    hi = nd.rolling(126, min_periods=max(1, 126 // 2)).max()
    lo = nd.rolling(126, min_periods=max(1, 126 // 2)).min()
    base = (nd - lo) / (hi - lo).replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_netcyc_252d_jerk_v053_signal(debt, cashneq):
    nd = debt - cashneq
    hi = nd.rolling(252, min_periods=max(1, 252 // 2)).max()
    lo = nd.rolling(252, min_periods=max(1, 252 // 2)).min()
    base = (nd - lo) / (hi - lo).replace(0, np.nan)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_netcyc_378d_jerk_v054_signal(debt, cashneq):
    nd = debt - cashneq
    hi = nd.rolling(378, min_periods=max(1, 378 // 2)).max()
    lo = nd.rolling(378, min_periods=max(1, 378 // 2)).min()
    base = (nd - lo) / (hi - lo).replace(0, np.nan)
    d1 = base - base.shift(84)
    d2 = d1 - d1.shift(84)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_netcyc_504d_jerk_v055_signal(debt, cashneq):
    nd = debt - cashneq
    hi = nd.rolling(504, min_periods=max(1, 504 // 2)).max()
    lo = nd.rolling(504, min_periods=max(1, 504 // 2)).min()
    base = (nd - lo) / (hi - lo).replace(0, np.nan)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_usdz_42d_jerk_v056_signal(debtusd):
    base = _z(debtusd, 42)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_usdz_126d_jerk_v057_signal(debtusd):
    base = _z(debtusd, 126)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_usdz_252d_jerk_v058_signal(debtusd):
    base = _z(debtusd, 252)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_usdz_378d_jerk_v059_signal(debtusd):
    base = _z(debtusd, 378)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_usdz_504d_jerk_v060_signal(debtusd):
    base = _z(debtusd, 504)
    d1 = base - base.shift(84)
    d2 = d1 - d1.shift(84)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_usdslope_42d_jerk_v061_signal(debtusd):
    base = np.log(debtusd.replace(0, np.nan)) - np.log(debtusd.shift(42).replace(0, np.nan))
    d1 = base - base.shift(10)
    d2 = d1 - d1.shift(10)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_usdslope_126d_jerk_v062_signal(debtusd):
    base = np.log(debtusd.replace(0, np.nan)) - np.log(debtusd.shift(126).replace(0, np.nan))
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_usdslope_252d_jerk_v063_signal(debtusd):
    base = np.log(debtusd.replace(0, np.nan)) - np.log(debtusd.shift(252).replace(0, np.nan))
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_usdslope_378d_jerk_v064_signal(debtusd):
    base = np.log(debtusd.replace(0, np.nan)) - np.log(debtusd.shift(378).replace(0, np.nan))
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_usdslope_504d_jerk_v065_signal(debtusd):
    base = np.log(debtusd.replace(0, np.nan)) - np.log(debtusd.shift(504).replace(0, np.nan))
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_shortz_42d_jerk_v066_signal(debtc):
    base = _z(debtc, 42)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_shortz_126d_jerk_v067_signal(debtc):
    base = _z(debtc, 126)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_shortz_252d_jerk_v068_signal(debtc):
    base = _z(debtc, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_shortz_378d_jerk_v069_signal(debtc):
    base = _z(debtc, 378)
    d1 = base - base.shift(84)
    d2 = d1 - d1.shift(84)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_shortz_504d_jerk_v070_signal(debtc):
    base = _z(debtc, 504)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_longz_42d_jerk_v071_signal(debtnc):
    base = _z(debtnc, 42)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_longz_126d_jerk_v072_signal(debtnc):
    base = _z(debtnc, 126)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_longz_252d_jerk_v073_signal(debtnc):
    base = _z(debtnc, 252)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_longz_378d_jerk_v074_signal(debtnc):
    base = _z(debtnc, 378)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_longz_504d_jerk_v075_signal(debtnc):
    base = _z(debtnc, 504)
    d1 = base - base.shift(84)
    d2 = d1 - d1.shift(84)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_shortslope_42d_jerk_v076_signal(debtc):
    base = np.log(debtc.replace(0, np.nan)) - np.log(debtc.shift(42).replace(0, np.nan))
    d1 = base - base.shift(10)
    d2 = d1 - d1.shift(10)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_shortslope_126d_jerk_v077_signal(debtc):
    base = np.log(debtc.replace(0, np.nan)) - np.log(debtc.shift(126).replace(0, np.nan))
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_shortslope_252d_jerk_v078_signal(debtc):
    base = np.log(debtc.replace(0, np.nan)) - np.log(debtc.shift(252).replace(0, np.nan))
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_shortslope_378d_jerk_v079_signal(debtc):
    base = np.log(debtc.replace(0, np.nan)) - np.log(debtc.shift(378).replace(0, np.nan))
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_shortslope_504d_jerk_v080_signal(debtc):
    base = np.log(debtc.replace(0, np.nan)) - np.log(debtc.shift(504).replace(0, np.nan))
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_longslope_42d_jerk_v081_signal(debtnc):
    base = np.log(debtnc.replace(0, np.nan)) - np.log(debtnc.shift(42).replace(0, np.nan))
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_longslope_126d_jerk_v082_signal(debtnc):
    base = np.log(debtnc.replace(0, np.nan)) - np.log(debtnc.shift(126).replace(0, np.nan))
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_longslope_252d_jerk_v083_signal(debtnc):
    base = np.log(debtnc.replace(0, np.nan)) - np.log(debtnc.shift(252).replace(0, np.nan))
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_longslope_378d_jerk_v084_signal(debtnc):
    base = np.log(debtnc.replace(0, np.nan)) - np.log(debtnc.shift(378).replace(0, np.nan))
    d1 = base - base.shift(84)
    d2 = d1 - d1.shift(84)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_longslope_504d_jerk_v085_signal(debtnc):
    base = np.log(debtnc.replace(0, np.nan)) - np.log(debtnc.shift(504).replace(0, np.nan))
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_cashshort_42d_jerk_v086_signal(cashneq, debtc):
    r = cashneq / debtc.replace(0, np.nan)
    base = r.rolling(42, min_periods=max(1, 42 // 2)).mean()
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_cashshort_126d_jerk_v087_signal(cashneq, debtc):
    r = cashneq / debtc.replace(0, np.nan)
    base = r.rolling(126, min_periods=max(1, 126 // 2)).mean()
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_cashshort_252d_jerk_v088_signal(cashneq, debtc):
    r = cashneq / debtc.replace(0, np.nan)
    base = r.rolling(252, min_periods=max(1, 252 // 2)).mean()
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_cashshort_378d_jerk_v089_signal(cashneq, debtc):
    r = cashneq / debtc.replace(0, np.nan)
    base = r.rolling(378, min_periods=max(1, 378 // 2)).mean()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_cashshort_504d_jerk_v090_signal(cashneq, debtc):
    r = cashneq / debtc.replace(0, np.nan)
    base = r.rolling(504, min_periods=max(1, 504 // 2)).mean()
    d1 = base - base.shift(84)
    d2 = d1 - d1.shift(84)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_mixslopediv_42d_jerk_v091_signal(debtc, debtnc):
    ss = np.log(debtc.replace(0, np.nan)) - np.log(debtc.shift(42).replace(0, np.nan))
    ls = np.log(debtnc.replace(0, np.nan)) - np.log(debtnc.shift(42).replace(0, np.nan))
    base = ss - ls
    d1 = base - base.shift(10)
    d2 = d1 - d1.shift(10)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_mixslopediv_126d_jerk_v092_signal(debtc, debtnc):
    ss = np.log(debtc.replace(0, np.nan)) - np.log(debtc.shift(126).replace(0, np.nan))
    ls = np.log(debtnc.replace(0, np.nan)) - np.log(debtnc.shift(126).replace(0, np.nan))
    base = ss - ls
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_mixslopediv_252d_jerk_v093_signal(debtc, debtnc):
    ss = np.log(debtc.replace(0, np.nan)) - np.log(debtc.shift(252).replace(0, np.nan))
    ls = np.log(debtnc.replace(0, np.nan)) - np.log(debtnc.shift(252).replace(0, np.nan))
    base = ss - ls
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_mixslopediv_378d_jerk_v094_signal(debtc, debtnc):
    ss = np.log(debtc.replace(0, np.nan)) - np.log(debtc.shift(378).replace(0, np.nan))
    ls = np.log(debtnc.replace(0, np.nan)) - np.log(debtnc.shift(378).replace(0, np.nan))
    base = ss - ls
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_mixslopediv_504d_jerk_v095_signal(debtc, debtnc):
    ss = np.log(debtc.replace(0, np.nan)) - np.log(debtc.shift(504).replace(0, np.nan))
    ls = np.log(debtnc.replace(0, np.nan)) - np.log(debtnc.shift(504).replace(0, np.nan))
    base = ss - ls
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_flowvol_42d_jerk_v096_signal(ncfdebt, debt):
    base = ncfdebt.rolling(42, min_periods=max(1, 42 // 2)).std() / debt.replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_flowvol_126d_jerk_v097_signal(ncfdebt, debt):
    base = ncfdebt.rolling(126, min_periods=max(1, 126 // 2)).std() / debt.replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_flowvol_252d_jerk_v098_signal(ncfdebt, debt):
    base = ncfdebt.rolling(252, min_periods=max(1, 252 // 2)).std() / debt.replace(0, np.nan)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_flowvol_378d_jerk_v099_signal(ncfdebt, debt):
    base = ncfdebt.rolling(378, min_periods=max(1, 378 // 2)).std() / debt.replace(0, np.nan)
    d1 = base - base.shift(84)
    d2 = d1 - d1.shift(84)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_flowvol_504d_jerk_v100_signal(ncfdebt, debt):
    base = ncfdebt.rolling(504, min_periods=max(1, 504 // 2)).std() / debt.replace(0, np.nan)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_debtema_42d_jerk_v101_signal(debt):
    fast = debt.ewm(span=42, min_periods=max(1, 42 // 4)).mean()
    slow = debt.ewm(span=231, min_periods=max(1, 42 // 4)).mean()
    base = fast / slow.replace(0, np.nan) - 1.0
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_debtema_126d_jerk_v102_signal(debt):
    fast = debt.ewm(span=126, min_periods=max(1, 126 // 4)).mean()
    slow = debt.ewm(span=315, min_periods=max(1, 126 // 4)).mean()
    base = fast / slow.replace(0, np.nan) - 1.0
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_debtema_252d_jerk_v103_signal(debt):
    fast = debt.ewm(span=252, min_periods=max(1, 252 // 4)).mean()
    slow = debt.ewm(span=441, min_periods=max(1, 252 // 4)).mean()
    base = fast / slow.replace(0, np.nan) - 1.0
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_debtema_378d_jerk_v104_signal(debt):
    fast = debt.ewm(span=378, min_periods=max(1, 378 // 4)).mean()
    slow = debt.ewm(span=567, min_periods=max(1, 378 // 4)).mean()
    base = fast / slow.replace(0, np.nan) - 1.0
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_debtema_504d_jerk_v105_signal(debt):
    fast = debt.ewm(span=504, min_periods=max(1, 504 // 4)).mean()
    slow = debt.ewm(span=693, min_periods=max(1, 504 // 4)).mean()
    base = fast / slow.replace(0, np.nan) - 1.0
    d1 = base - base.shift(84)
    d2 = d1 - d1.shift(84)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_netema_42d_jerk_v106_signal(debt, cashneq):
    nd = debt - cashneq
    fast = nd.ewm(span=42, min_periods=max(1, 42 // 4)).mean()
    slow = nd.ewm(span=231, min_periods=max(1, 42 // 4)).mean()
    base = (fast - slow) / debt.replace(0, np.nan)
    d1 = base - base.shift(10)
    d2 = d1 - d1.shift(10)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_netema_126d_jerk_v107_signal(debt, cashneq):
    nd = debt - cashneq
    fast = nd.ewm(span=126, min_periods=max(1, 126 // 4)).mean()
    slow = nd.ewm(span=315, min_periods=max(1, 126 // 4)).mean()
    base = (fast - slow) / debt.replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_netema_252d_jerk_v108_signal(debt, cashneq):
    nd = debt - cashneq
    fast = nd.ewm(span=252, min_periods=max(1, 252 // 4)).mean()
    slow = nd.ewm(span=441, min_periods=max(1, 252 // 4)).mean()
    base = (fast - slow) / debt.replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_netema_378d_jerk_v109_signal(debt, cashneq):
    nd = debt - cashneq
    fast = nd.ewm(span=378, min_periods=max(1, 378 // 4)).mean()
    slow = nd.ewm(span=567, min_periods=max(1, 378 // 4)).mean()
    base = (fast - slow) / debt.replace(0, np.nan)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_netema_504d_jerk_v110_signal(debt, cashneq):
    nd = debt - cashneq
    fast = nd.ewm(span=504, min_periods=max(1, 504 // 4)).mean()
    slow = nd.ewm(span=693, min_periods=max(1, 504 // 4)).mean()
    base = (fast - slow) / debt.replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_mixlr_42d_jerk_v111_signal(debtc, debtnc):
    lr = np.log(debtc.replace(0, np.nan)) - np.log(debtnc.replace(0, np.nan))
    base = _z(lr, 42)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_mixlr_126d_jerk_v112_signal(debtc, debtnc):
    lr = np.log(debtc.replace(0, np.nan)) - np.log(debtnc.replace(0, np.nan))
    base = _z(lr, 126)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_mixlr_252d_jerk_v113_signal(debtc, debtnc):
    lr = np.log(debtc.replace(0, np.nan)) - np.log(debtnc.replace(0, np.nan))
    base = _z(lr, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_mixlr_378d_jerk_v114_signal(debtc, debtnc):
    lr = np.log(debtc.replace(0, np.nan)) - np.log(debtnc.replace(0, np.nan))
    base = _z(lr, 378)
    d1 = base - base.shift(84)
    d2 = d1 - d1.shift(84)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_mixlr_504d_jerk_v115_signal(debtc, debtnc):
    lr = np.log(debtc.replace(0, np.nan)) - np.log(debtnc.replace(0, np.nan))
    base = _z(lr, 504)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_covrecov_42d_jerk_v116_signal(debt, cashneq):
    cov = cashneq / debt.replace(0, np.nan)
    lo = cov.rolling(42, min_periods=max(1, 42 // 2)).min()
    base = cov / lo.replace(0, np.nan) - 1.0
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_covrecov_126d_jerk_v117_signal(debt, cashneq):
    cov = cashneq / debt.replace(0, np.nan)
    lo = cov.rolling(126, min_periods=max(1, 126 // 2)).min()
    base = cov / lo.replace(0, np.nan) - 1.0
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_covrecov_252d_jerk_v118_signal(debt, cashneq):
    cov = cashneq / debt.replace(0, np.nan)
    lo = cov.rolling(252, min_periods=max(1, 252 // 2)).min()
    base = cov / lo.replace(0, np.nan) - 1.0
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_covrecov_378d_jerk_v119_signal(debt, cashneq):
    cov = cashneq / debt.replace(0, np.nan)
    lo = cov.rolling(378, min_periods=max(1, 378 // 2)).min()
    base = cov / lo.replace(0, np.nan) - 1.0
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_covrecov_504d_jerk_v120_signal(debt, cashneq):
    cov = cashneq / debt.replace(0, np.nan)
    lo = cov.rolling(504, min_periods=max(1, 504 // 2)).min()
    base = cov / lo.replace(0, np.nan) - 1.0
    d1 = base - base.shift(84)
    d2 = d1 - d1.shift(84)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_debtamp_42d_jerk_v121_signal(debt):
    hi = debt.rolling(42, min_periods=max(1, 42 // 2)).max()
    lo = debt.rolling(42, min_periods=max(1, 42 // 2)).min()
    mn = debt.rolling(42, min_periods=max(1, 42 // 2)).mean()
    base = (hi - lo) / mn.replace(0, np.nan)
    d1 = base - base.shift(10)
    d2 = d1 - d1.shift(10)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_debtamp_126d_jerk_v122_signal(debt):
    hi = debt.rolling(126, min_periods=max(1, 126 // 2)).max()
    lo = debt.rolling(126, min_periods=max(1, 126 // 2)).min()
    mn = debt.rolling(126, min_periods=max(1, 126 // 2)).mean()
    base = (hi - lo) / mn.replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_debtamp_252d_jerk_v123_signal(debt):
    hi = debt.rolling(252, min_periods=max(1, 252 // 2)).max()
    lo = debt.rolling(252, min_periods=max(1, 252 // 2)).min()
    mn = debt.rolling(252, min_periods=max(1, 252 // 2)).mean()
    base = (hi - lo) / mn.replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_debtamp_378d_jerk_v124_signal(debt):
    hi = debt.rolling(378, min_periods=max(1, 378 // 2)).max()
    lo = debt.rolling(378, min_periods=max(1, 378 // 2)).min()
    mn = debt.rolling(378, min_periods=max(1, 378 // 2)).mean()
    base = (hi - lo) / mn.replace(0, np.nan)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_debtamp_504d_jerk_v125_signal(debt):
    hi = debt.rolling(504, min_periods=max(1, 504 // 2)).max()
    lo = debt.rolling(504, min_periods=max(1, 504 // 2)).min()
    mn = debt.rolling(504, min_periods=max(1, 504 // 2)).mean()
    base = (hi - lo) / mn.replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_flowz_42d_jerk_v126_signal(ncfdebt):
    base = _z(ncfdebt, 42)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_flowz_126d_jerk_v127_signal(ncfdebt):
    base = _z(ncfdebt, 126)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_flowz_252d_jerk_v128_signal(ncfdebt):
    base = _z(ncfdebt, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_flowz_378d_jerk_v129_signal(ncfdebt):
    base = _z(ncfdebt, 378)
    d1 = base - base.shift(84)
    d2 = d1 - d1.shift(84)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_flowz_504d_jerk_v130_signal(ncfdebt):
    base = _z(ncfdebt, 504)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_cashz_42d_jerk_v131_signal(cashneq):
    base = _z(cashneq, 42)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_cashz_126d_jerk_v132_signal(cashneq):
    base = _z(cashneq, 126)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_cashz_252d_jerk_v133_signal(cashneq):
    base = _z(cashneq, 252)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_cashz_378d_jerk_v134_signal(cashneq):
    base = _z(cashneq, 378)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_cashz_504d_jerk_v135_signal(cashneq):
    base = _z(cashneq, 504)
    d1 = base - base.shift(84)
    d2 = d1 - d1.shift(84)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_nettrough_42d_jerk_v136_signal(debt, cashneq):
    nd = debt - cashneq
    lo = nd.rolling(42, min_periods=max(1, 42 // 2)).min()
    base = (nd - lo) / debt.replace(0, np.nan)
    d1 = base - base.shift(10)
    d2 = d1 - d1.shift(10)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_nettrough_126d_jerk_v137_signal(debt, cashneq):
    nd = debt - cashneq
    lo = nd.rolling(126, min_periods=max(1, 126 // 2)).min()
    base = (nd - lo) / debt.replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_nettrough_252d_jerk_v138_signal(debt, cashneq):
    nd = debt - cashneq
    lo = nd.rolling(252, min_periods=max(1, 252 // 2)).min()
    base = (nd - lo) / debt.replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_nettrough_378d_jerk_v139_signal(debt, cashneq):
    nd = debt - cashneq
    lo = nd.rolling(378, min_periods=max(1, 378 // 2)).min()
    base = (nd - lo) / debt.replace(0, np.nan)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_nettrough_504d_jerk_v140_signal(debt, cashneq):
    nd = debt - cashneq
    lo = nd.rolling(504, min_periods=max(1, 504 // 2)).min()
    base = (nd - lo) / debt.replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_shortgross_42d_jerk_v141_signal(debtc, debt):
    base = (debtc / debt.replace(0, np.nan)).rolling(42, min_periods=max(1, 42 // 2)).mean()
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_shortgross_126d_jerk_v142_signal(debtc, debt):
    base = (debtc / debt.replace(0, np.nan)).rolling(126, min_periods=max(1, 126 // 2)).mean()
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_shortgross_252d_jerk_v143_signal(debtc, debt):
    base = (debtc / debt.replace(0, np.nan)).rolling(252, min_periods=max(1, 252 // 2)).mean()
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_shortgross_378d_jerk_v144_signal(debtc, debt):
    base = (debtc / debt.replace(0, np.nan)).rolling(378, min_periods=max(1, 378 // 2)).mean()
    d1 = base - base.shift(84)
    d2 = d1 - d1.shift(84)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_shortgross_504d_jerk_v145_signal(debtc, debt):
    base = (debtc / debt.replace(0, np.nan)).rolling(504, min_periods=max(1, 504 // 2)).mean()
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_debtmed_42d_jerk_v146_signal(debt):
    med = debt.rolling(42, min_periods=max(1, 42 // 2)).median()
    base = debt / med.replace(0, np.nan) - 1.0
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_debtmed_126d_jerk_v147_signal(debt):
    med = debt.rolling(126, min_periods=max(1, 126 // 2)).median()
    base = debt / med.replace(0, np.nan) - 1.0
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_debtmed_252d_jerk_v148_signal(debt):
    med = debt.rolling(252, min_periods=max(1, 252 // 2)).median()
    base = debt / med.replace(0, np.nan) - 1.0
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_debtmed_378d_jerk_v149_signal(debt):
    med = debt.rolling(378, min_periods=max(1, 378 // 2)).median()
    base = debt / med.replace(0, np.nan) - 1.0
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f31dt_f31_debt_cycle_trajectory_debtmed_504d_jerk_v150_signal(debt):
    med = debt.rolling(504, min_periods=max(1, 504 // 2)).median()
    base = debt / med.replace(0, np.nan) - 1.0
    d1 = base - base.shift(84)
    d2 = d1 - d1.shift(84)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f31dt_f31_debt_cycle_trajectory_debtz_42d_jerk_v001_signal,
    f31dt_f31_debt_cycle_trajectory_debtz_126d_jerk_v002_signal,
    f31dt_f31_debt_cycle_trajectory_debtz_252d_jerk_v003_signal,
    f31dt_f31_debt_cycle_trajectory_debtz_378d_jerk_v004_signal,
    f31dt_f31_debt_cycle_trajectory_debtz_504d_jerk_v005_signal,
    f31dt_f31_debt_cycle_trajectory_debtslope_42d_jerk_v006_signal,
    f31dt_f31_debt_cycle_trajectory_debtslope_126d_jerk_v007_signal,
    f31dt_f31_debt_cycle_trajectory_debtslope_252d_jerk_v008_signal,
    f31dt_f31_debt_cycle_trajectory_debtslope_378d_jerk_v009_signal,
    f31dt_f31_debt_cycle_trajectory_debtslope_504d_jerk_v010_signal,
    f31dt_f31_debt_cycle_trajectory_netz_42d_jerk_v011_signal,
    f31dt_f31_debt_cycle_trajectory_netz_126d_jerk_v012_signal,
    f31dt_f31_debt_cycle_trajectory_netz_252d_jerk_v013_signal,
    f31dt_f31_debt_cycle_trajectory_netz_378d_jerk_v014_signal,
    f31dt_f31_debt_cycle_trajectory_netz_504d_jerk_v015_signal,
    f31dt_f31_debt_cycle_trajectory_netchg_42d_jerk_v016_signal,
    f31dt_f31_debt_cycle_trajectory_netchg_126d_jerk_v017_signal,
    f31dt_f31_debt_cycle_trajectory_netchg_252d_jerk_v018_signal,
    f31dt_f31_debt_cycle_trajectory_netchg_378d_jerk_v019_signal,
    f31dt_f31_debt_cycle_trajectory_netchg_504d_jerk_v020_signal,
    f31dt_f31_debt_cycle_trajectory_shortsh_42d_jerk_v021_signal,
    f31dt_f31_debt_cycle_trajectory_shortsh_126d_jerk_v022_signal,
    f31dt_f31_debt_cycle_trajectory_shortsh_252d_jerk_v023_signal,
    f31dt_f31_debt_cycle_trajectory_shortsh_378d_jerk_v024_signal,
    f31dt_f31_debt_cycle_trajectory_shortsh_504d_jerk_v025_signal,
    f31dt_f31_debt_cycle_trajectory_cashcov_42d_jerk_v026_signal,
    f31dt_f31_debt_cycle_trajectory_cashcov_126d_jerk_v027_signal,
    f31dt_f31_debt_cycle_trajectory_cashcov_252d_jerk_v028_signal,
    f31dt_f31_debt_cycle_trajectory_cashcov_378d_jerk_v029_signal,
    f31dt_f31_debt_cycle_trajectory_cashcov_504d_jerk_v030_signal,
    f31dt_f31_debt_cycle_trajectory_dcashrank_42d_jerk_v031_signal,
    f31dt_f31_debt_cycle_trajectory_dcashrank_126d_jerk_v032_signal,
    f31dt_f31_debt_cycle_trajectory_dcashrank_252d_jerk_v033_signal,
    f31dt_f31_debt_cycle_trajectory_dcashrank_378d_jerk_v034_signal,
    f31dt_f31_debt_cycle_trajectory_dcashrank_504d_jerk_v035_signal,
    f31dt_f31_debt_cycle_trajectory_flowsm_42d_jerk_v036_signal,
    f31dt_f31_debt_cycle_trajectory_flowsm_126d_jerk_v037_signal,
    f31dt_f31_debt_cycle_trajectory_flowsm_252d_jerk_v038_signal,
    f31dt_f31_debt_cycle_trajectory_flowsm_378d_jerk_v039_signal,
    f31dt_f31_debt_cycle_trajectory_flowsm_504d_jerk_v040_signal,
    f31dt_f31_debt_cycle_trajectory_peakdist_42d_jerk_v041_signal,
    f31dt_f31_debt_cycle_trajectory_peakdist_126d_jerk_v042_signal,
    f31dt_f31_debt_cycle_trajectory_peakdist_252d_jerk_v043_signal,
    f31dt_f31_debt_cycle_trajectory_peakdist_378d_jerk_v044_signal,
    f31dt_f31_debt_cycle_trajectory_peakdist_504d_jerk_v045_signal,
    f31dt_f31_debt_cycle_trajectory_debtcyc_42d_jerk_v046_signal,
    f31dt_f31_debt_cycle_trajectory_debtcyc_126d_jerk_v047_signal,
    f31dt_f31_debt_cycle_trajectory_debtcyc_252d_jerk_v048_signal,
    f31dt_f31_debt_cycle_trajectory_debtcyc_378d_jerk_v049_signal,
    f31dt_f31_debt_cycle_trajectory_debtcyc_504d_jerk_v050_signal,
    f31dt_f31_debt_cycle_trajectory_netcyc_42d_jerk_v051_signal,
    f31dt_f31_debt_cycle_trajectory_netcyc_126d_jerk_v052_signal,
    f31dt_f31_debt_cycle_trajectory_netcyc_252d_jerk_v053_signal,
    f31dt_f31_debt_cycle_trajectory_netcyc_378d_jerk_v054_signal,
    f31dt_f31_debt_cycle_trajectory_netcyc_504d_jerk_v055_signal,
    f31dt_f31_debt_cycle_trajectory_usdz_42d_jerk_v056_signal,
    f31dt_f31_debt_cycle_trajectory_usdz_126d_jerk_v057_signal,
    f31dt_f31_debt_cycle_trajectory_usdz_252d_jerk_v058_signal,
    f31dt_f31_debt_cycle_trajectory_usdz_378d_jerk_v059_signal,
    f31dt_f31_debt_cycle_trajectory_usdz_504d_jerk_v060_signal,
    f31dt_f31_debt_cycle_trajectory_usdslope_42d_jerk_v061_signal,
    f31dt_f31_debt_cycle_trajectory_usdslope_126d_jerk_v062_signal,
    f31dt_f31_debt_cycle_trajectory_usdslope_252d_jerk_v063_signal,
    f31dt_f31_debt_cycle_trajectory_usdslope_378d_jerk_v064_signal,
    f31dt_f31_debt_cycle_trajectory_usdslope_504d_jerk_v065_signal,
    f31dt_f31_debt_cycle_trajectory_shortz_42d_jerk_v066_signal,
    f31dt_f31_debt_cycle_trajectory_shortz_126d_jerk_v067_signal,
    f31dt_f31_debt_cycle_trajectory_shortz_252d_jerk_v068_signal,
    f31dt_f31_debt_cycle_trajectory_shortz_378d_jerk_v069_signal,
    f31dt_f31_debt_cycle_trajectory_shortz_504d_jerk_v070_signal,
    f31dt_f31_debt_cycle_trajectory_longz_42d_jerk_v071_signal,
    f31dt_f31_debt_cycle_trajectory_longz_126d_jerk_v072_signal,
    f31dt_f31_debt_cycle_trajectory_longz_252d_jerk_v073_signal,
    f31dt_f31_debt_cycle_trajectory_longz_378d_jerk_v074_signal,
    f31dt_f31_debt_cycle_trajectory_longz_504d_jerk_v075_signal,
    f31dt_f31_debt_cycle_trajectory_shortslope_42d_jerk_v076_signal,
    f31dt_f31_debt_cycle_trajectory_shortslope_126d_jerk_v077_signal,
    f31dt_f31_debt_cycle_trajectory_shortslope_252d_jerk_v078_signal,
    f31dt_f31_debt_cycle_trajectory_shortslope_378d_jerk_v079_signal,
    f31dt_f31_debt_cycle_trajectory_shortslope_504d_jerk_v080_signal,
    f31dt_f31_debt_cycle_trajectory_longslope_42d_jerk_v081_signal,
    f31dt_f31_debt_cycle_trajectory_longslope_126d_jerk_v082_signal,
    f31dt_f31_debt_cycle_trajectory_longslope_252d_jerk_v083_signal,
    f31dt_f31_debt_cycle_trajectory_longslope_378d_jerk_v084_signal,
    f31dt_f31_debt_cycle_trajectory_longslope_504d_jerk_v085_signal,
    f31dt_f31_debt_cycle_trajectory_cashshort_42d_jerk_v086_signal,
    f31dt_f31_debt_cycle_trajectory_cashshort_126d_jerk_v087_signal,
    f31dt_f31_debt_cycle_trajectory_cashshort_252d_jerk_v088_signal,
    f31dt_f31_debt_cycle_trajectory_cashshort_378d_jerk_v089_signal,
    f31dt_f31_debt_cycle_trajectory_cashshort_504d_jerk_v090_signal,
    f31dt_f31_debt_cycle_trajectory_mixslopediv_42d_jerk_v091_signal,
    f31dt_f31_debt_cycle_trajectory_mixslopediv_126d_jerk_v092_signal,
    f31dt_f31_debt_cycle_trajectory_mixslopediv_252d_jerk_v093_signal,
    f31dt_f31_debt_cycle_trajectory_mixslopediv_378d_jerk_v094_signal,
    f31dt_f31_debt_cycle_trajectory_mixslopediv_504d_jerk_v095_signal,
    f31dt_f31_debt_cycle_trajectory_flowvol_42d_jerk_v096_signal,
    f31dt_f31_debt_cycle_trajectory_flowvol_126d_jerk_v097_signal,
    f31dt_f31_debt_cycle_trajectory_flowvol_252d_jerk_v098_signal,
    f31dt_f31_debt_cycle_trajectory_flowvol_378d_jerk_v099_signal,
    f31dt_f31_debt_cycle_trajectory_flowvol_504d_jerk_v100_signal,
    f31dt_f31_debt_cycle_trajectory_debtema_42d_jerk_v101_signal,
    f31dt_f31_debt_cycle_trajectory_debtema_126d_jerk_v102_signal,
    f31dt_f31_debt_cycle_trajectory_debtema_252d_jerk_v103_signal,
    f31dt_f31_debt_cycle_trajectory_debtema_378d_jerk_v104_signal,
    f31dt_f31_debt_cycle_trajectory_debtema_504d_jerk_v105_signal,
    f31dt_f31_debt_cycle_trajectory_netema_42d_jerk_v106_signal,
    f31dt_f31_debt_cycle_trajectory_netema_126d_jerk_v107_signal,
    f31dt_f31_debt_cycle_trajectory_netema_252d_jerk_v108_signal,
    f31dt_f31_debt_cycle_trajectory_netema_378d_jerk_v109_signal,
    f31dt_f31_debt_cycle_trajectory_netema_504d_jerk_v110_signal,
    f31dt_f31_debt_cycle_trajectory_mixlr_42d_jerk_v111_signal,
    f31dt_f31_debt_cycle_trajectory_mixlr_126d_jerk_v112_signal,
    f31dt_f31_debt_cycle_trajectory_mixlr_252d_jerk_v113_signal,
    f31dt_f31_debt_cycle_trajectory_mixlr_378d_jerk_v114_signal,
    f31dt_f31_debt_cycle_trajectory_mixlr_504d_jerk_v115_signal,
    f31dt_f31_debt_cycle_trajectory_covrecov_42d_jerk_v116_signal,
    f31dt_f31_debt_cycle_trajectory_covrecov_126d_jerk_v117_signal,
    f31dt_f31_debt_cycle_trajectory_covrecov_252d_jerk_v118_signal,
    f31dt_f31_debt_cycle_trajectory_covrecov_378d_jerk_v119_signal,
    f31dt_f31_debt_cycle_trajectory_covrecov_504d_jerk_v120_signal,
    f31dt_f31_debt_cycle_trajectory_debtamp_42d_jerk_v121_signal,
    f31dt_f31_debt_cycle_trajectory_debtamp_126d_jerk_v122_signal,
    f31dt_f31_debt_cycle_trajectory_debtamp_252d_jerk_v123_signal,
    f31dt_f31_debt_cycle_trajectory_debtamp_378d_jerk_v124_signal,
    f31dt_f31_debt_cycle_trajectory_debtamp_504d_jerk_v125_signal,
    f31dt_f31_debt_cycle_trajectory_flowz_42d_jerk_v126_signal,
    f31dt_f31_debt_cycle_trajectory_flowz_126d_jerk_v127_signal,
    f31dt_f31_debt_cycle_trajectory_flowz_252d_jerk_v128_signal,
    f31dt_f31_debt_cycle_trajectory_flowz_378d_jerk_v129_signal,
    f31dt_f31_debt_cycle_trajectory_flowz_504d_jerk_v130_signal,
    f31dt_f31_debt_cycle_trajectory_cashz_42d_jerk_v131_signal,
    f31dt_f31_debt_cycle_trajectory_cashz_126d_jerk_v132_signal,
    f31dt_f31_debt_cycle_trajectory_cashz_252d_jerk_v133_signal,
    f31dt_f31_debt_cycle_trajectory_cashz_378d_jerk_v134_signal,
    f31dt_f31_debt_cycle_trajectory_cashz_504d_jerk_v135_signal,
    f31dt_f31_debt_cycle_trajectory_nettrough_42d_jerk_v136_signal,
    f31dt_f31_debt_cycle_trajectory_nettrough_126d_jerk_v137_signal,
    f31dt_f31_debt_cycle_trajectory_nettrough_252d_jerk_v138_signal,
    f31dt_f31_debt_cycle_trajectory_nettrough_378d_jerk_v139_signal,
    f31dt_f31_debt_cycle_trajectory_nettrough_504d_jerk_v140_signal,
    f31dt_f31_debt_cycle_trajectory_shortgross_42d_jerk_v141_signal,
    f31dt_f31_debt_cycle_trajectory_shortgross_126d_jerk_v142_signal,
    f31dt_f31_debt_cycle_trajectory_shortgross_252d_jerk_v143_signal,
    f31dt_f31_debt_cycle_trajectory_shortgross_378d_jerk_v144_signal,
    f31dt_f31_debt_cycle_trajectory_shortgross_504d_jerk_v145_signal,
    f31dt_f31_debt_cycle_trajectory_debtmed_42d_jerk_v146_signal,
    f31dt_f31_debt_cycle_trajectory_debtmed_126d_jerk_v147_signal,
    f31dt_f31_debt_cycle_trajectory_debtmed_252d_jerk_v148_signal,
    f31dt_f31_debt_cycle_trajectory_debtmed_378d_jerk_v149_signal,
    f31dt_f31_debt_cycle_trajectory_debtmed_504d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F31_DEBT_CYCLE_TRAJECTORY_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.0, vol=0.08, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.5
        return pd.Series(s, name=None)

    debt = _fund(301, base=5e8, drift=0.01, vol=0.10).rename("debt")
    debtusd = (_fund(302, base=5e8, drift=0.01, vol=0.10) * 1.02).rename("debtusd")
    debtc = _fund(303, base=1.5e8, drift=0.005, vol=0.12).rename("debtc")
    debtnc = _fund(304, base=3.5e8, drift=0.008, vol=0.09).rename("debtnc")
    cashneq = _fund(305, base=2e8, drift=0.0, vol=0.15).rename("cashneq")
    ncfdebt = _fund(306, base=8e7, drift=0.0, vol=0.30, allow_neg=True).rename("ncfdebt")

    cols = {"debt": debt, "debtusd": debtusd, "debtc": debtc, "debtnc": debtnc,
            "cashneq": cashneq, "ncfdebt": ncfdebt}

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

    print("OK f31_debt_cycle_trajectory_3rd_derivatives_001_150_claude: %d features pass" % n_features)
