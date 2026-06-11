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

def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)

# ===== folder domain primitives =====
def _f23_commercial_debt(debt, assets):
    return debt / assets.replace(0, np.nan).abs()


def _f23_lending_revenue(revenue, debt, w):
    r = revenue / debt.replace(0, np.nan).abs()
    return r.rolling(w, min_periods=max(1, w // 2)).mean()


def _f23_lending_cycle(debt, revenue, w):
    dg = debt.pct_change(periods=w)
    rg = revenue.pct_change(periods=w)
    return dg - rg

def f23cld_f23_commercial_lending_dynamics_cdebt_5d_5d_sp_slope_v001_signal(assets, debt, closeadj):
    base = _f23_commercial_debt(debt, assets)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebt_10d_10d_sp_slope_v002_signal(assets, debt, closeadj):
    base = _f23_commercial_debt(debt, assets)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebt_21d_21d_sp_slope_v003_signal(assets, debt, closeadj):
    base = _f23_commercial_debt(debt, assets)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebt_42d_42d_sp_slope_v004_signal(assets, debt, closeadj):
    base = _f23_commercial_debt(debt, assets)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebt_63d_63d_sp_slope_v005_signal(assets, debt, closeadj):
    base = _f23_commercial_debt(debt, assets)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebt_126d_126d_sp_slope_v006_signal(assets, debt, closeadj):
    base = _f23_commercial_debt(debt, assets)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_5d_5d_sp_slope_v007_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 5)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_10d_5d_sp_slope_v008_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 10)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_10d_10d_sp_slope_v009_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 10)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_21d_5d_sp_slope_v010_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_21d_10d_sp_slope_v011_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 21)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_21d_21d_sp_slope_v012_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_42d_5d_sp_slope_v013_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 42)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_42d_10d_sp_slope_v014_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 42)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_42d_21d_sp_slope_v015_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 42)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_42d_42d_sp_slope_v016_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 42)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_63d_5d_sp_slope_v017_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_63d_10d_sp_slope_v018_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 63)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_63d_21d_sp_slope_v019_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 63)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_63d_42d_sp_slope_v020_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 63)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_63d_63d_sp_slope_v021_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 63)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_126d_5d_sp_slope_v022_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_126d_10d_sp_slope_v023_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 126)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_126d_21d_sp_slope_v024_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 126)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_126d_42d_sp_slope_v025_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 126)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_126d_63d_sp_slope_v026_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 126)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_126d_126d_sp_slope_v027_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 126)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_189d_5d_sp_slope_v028_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 189)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_189d_10d_sp_slope_v029_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 189)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_189d_21d_sp_slope_v030_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 189)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_189d_42d_sp_slope_v031_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 189)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_189d_63d_sp_slope_v032_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 189)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_189d_126d_sp_slope_v033_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 189)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_252d_5d_sp_slope_v034_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_252d_10d_sp_slope_v035_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 252)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_252d_21d_sp_slope_v036_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 252)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_252d_42d_sp_slope_v037_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 252)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_252d_63d_sp_slope_v038_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 252)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_252d_126d_sp_slope_v039_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 252)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_378d_5d_sp_slope_v040_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 378)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_378d_10d_sp_slope_v041_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 378)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_378d_21d_sp_slope_v042_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 378)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_378d_42d_sp_slope_v043_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 378)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_378d_63d_sp_slope_v044_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 378)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_378d_126d_sp_slope_v045_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 378)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_504d_5d_sp_slope_v046_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 504)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_504d_10d_sp_slope_v047_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 504)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_504d_21d_sp_slope_v048_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 504)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_504d_42d_sp_slope_v049_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 504)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_504d_63d_sp_slope_v050_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 504)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtroll_504d_126d_sp_slope_v051_signal(assets, debt, closeadj):
    base = _mean(_f23_commercial_debt(debt, assets), 504)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_5d_5d_sp_slope_v052_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 5)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_10d_5d_sp_slope_v053_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 10)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_10d_10d_sp_slope_v054_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 10)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_21d_5d_sp_slope_v055_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_21d_10d_sp_slope_v056_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 21)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_21d_21d_sp_slope_v057_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_42d_5d_sp_slope_v058_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 42)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_42d_10d_sp_slope_v059_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 42)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_42d_21d_sp_slope_v060_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 42)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_42d_42d_sp_slope_v061_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 42)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_63d_5d_sp_slope_v062_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_63d_10d_sp_slope_v063_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 63)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_63d_21d_sp_slope_v064_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 63)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_63d_42d_sp_slope_v065_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 63)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_63d_63d_sp_slope_v066_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 63)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_126d_5d_sp_slope_v067_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_126d_10d_sp_slope_v068_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 126)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_126d_21d_sp_slope_v069_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 126)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_126d_42d_sp_slope_v070_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 126)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_126d_63d_sp_slope_v071_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 126)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_126d_126d_sp_slope_v072_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 126)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_189d_5d_sp_slope_v073_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 189)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_189d_10d_sp_slope_v074_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 189)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_189d_21d_sp_slope_v075_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 189)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_189d_42d_sp_slope_v076_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 189)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_189d_63d_sp_slope_v077_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 189)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_189d_126d_sp_slope_v078_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 189)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_252d_5d_sp_slope_v079_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_252d_10d_sp_slope_v080_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 252)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_252d_21d_sp_slope_v081_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 252)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_252d_42d_sp_slope_v082_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 252)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_252d_63d_sp_slope_v083_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 252)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_252d_126d_sp_slope_v084_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 252)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_378d_5d_sp_slope_v085_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 378)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_378d_10d_sp_slope_v086_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 378)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_378d_21d_sp_slope_v087_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 378)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_378d_42d_sp_slope_v088_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 378)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_378d_63d_sp_slope_v089_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 378)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_378d_126d_sp_slope_v090_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 378)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_504d_5d_sp_slope_v091_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 504)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_504d_10d_sp_slope_v092_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 504)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_504d_21d_sp_slope_v093_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 504)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_504d_42d_sp_slope_v094_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 504)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_504d_63d_sp_slope_v095_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 504)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendrev_504d_126d_sp_slope_v096_signal(revenue, debt, closeadj):
    base = _f23_lending_revenue(revenue, debt, 504)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_5d_5d_sp_slope_v097_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 5)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_10d_5d_sp_slope_v098_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 10)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_10d_10d_sp_slope_v099_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 10)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_21d_5d_sp_slope_v100_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_21d_10d_sp_slope_v101_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 21)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_21d_21d_sp_slope_v102_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_42d_5d_sp_slope_v103_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 42)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_42d_10d_sp_slope_v104_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 42)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_42d_21d_sp_slope_v105_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 42)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_42d_42d_sp_slope_v106_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 42)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_63d_5d_sp_slope_v107_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_63d_10d_sp_slope_v108_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 63)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_63d_21d_sp_slope_v109_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 63)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_63d_42d_sp_slope_v110_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 63)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_63d_63d_sp_slope_v111_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 63)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_126d_5d_sp_slope_v112_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_126d_10d_sp_slope_v113_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 126)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_126d_21d_sp_slope_v114_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 126)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_126d_42d_sp_slope_v115_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 126)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_126d_63d_sp_slope_v116_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 126)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_126d_126d_sp_slope_v117_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 126)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_189d_5d_sp_slope_v118_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 189)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_189d_10d_sp_slope_v119_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 189)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_189d_21d_sp_slope_v120_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 189)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_189d_42d_sp_slope_v121_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 189)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_189d_63d_sp_slope_v122_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 189)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_189d_126d_sp_slope_v123_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 189)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_252d_5d_sp_slope_v124_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_252d_10d_sp_slope_v125_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 252)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_252d_21d_sp_slope_v126_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 252)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_252d_42d_sp_slope_v127_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 252)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_252d_63d_sp_slope_v128_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 252)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_252d_126d_sp_slope_v129_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 252)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_378d_5d_sp_slope_v130_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 378)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_378d_10d_sp_slope_v131_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 378)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_378d_21d_sp_slope_v132_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 378)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_378d_42d_sp_slope_v133_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 378)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_378d_63d_sp_slope_v134_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 378)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_378d_126d_sp_slope_v135_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 378)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_504d_5d_sp_slope_v136_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 504)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_504d_10d_sp_slope_v137_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 504)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_504d_21d_sp_slope_v138_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 504)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_504d_42d_sp_slope_v139_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 504)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_504d_63d_sp_slope_v140_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 504)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_lendcyc_504d_126d_sp_slope_v141_signal(revenue, debt, closeadj):
    base = _f23_lending_cycle(debt, revenue, 504)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtstd_5d_5d_sp_slope_v142_signal(assets, debt, closeadj):
    base = _std(_f23_commercial_debt(debt, assets), 5)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtstd_10d_5d_sp_slope_v143_signal(assets, debt, closeadj):
    base = _std(_f23_commercial_debt(debt, assets), 10)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtstd_10d_10d_sp_slope_v144_signal(assets, debt, closeadj):
    base = _std(_f23_commercial_debt(debt, assets), 10)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtstd_21d_5d_sp_slope_v145_signal(assets, debt, closeadj):
    base = _std(_f23_commercial_debt(debt, assets), 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtstd_21d_10d_sp_slope_v146_signal(assets, debt, closeadj):
    base = _std(_f23_commercial_debt(debt, assets), 21)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtstd_21d_21d_sp_slope_v147_signal(assets, debt, closeadj):
    base = _std(_f23_commercial_debt(debt, assets), 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtstd_42d_5d_sp_slope_v148_signal(assets, debt, closeadj):
    base = _std(_f23_commercial_debt(debt, assets), 42)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtstd_42d_10d_sp_slope_v149_signal(assets, debt, closeadj):
    base = _std(_f23_commercial_debt(debt, assets), 42)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f23cld_f23_commercial_lending_dynamics_cdebtstd_42d_21d_sp_slope_v150_signal(assets, debt, closeadj):
    base = _std(_f23_commercial_debt(debt, assets), 42)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f23cld_f23_commercial_lending_dynamics_cdebt_5d_5d_sp_slope_v001_signal,
    f23cld_f23_commercial_lending_dynamics_cdebt_10d_10d_sp_slope_v002_signal,
    f23cld_f23_commercial_lending_dynamics_cdebt_21d_21d_sp_slope_v003_signal,
    f23cld_f23_commercial_lending_dynamics_cdebt_42d_42d_sp_slope_v004_signal,
    f23cld_f23_commercial_lending_dynamics_cdebt_63d_63d_sp_slope_v005_signal,
    f23cld_f23_commercial_lending_dynamics_cdebt_126d_126d_sp_slope_v006_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_5d_5d_sp_slope_v007_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_10d_5d_sp_slope_v008_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_10d_10d_sp_slope_v009_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_21d_5d_sp_slope_v010_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_21d_10d_sp_slope_v011_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_21d_21d_sp_slope_v012_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_42d_5d_sp_slope_v013_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_42d_10d_sp_slope_v014_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_42d_21d_sp_slope_v015_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_42d_42d_sp_slope_v016_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_63d_5d_sp_slope_v017_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_63d_10d_sp_slope_v018_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_63d_21d_sp_slope_v019_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_63d_42d_sp_slope_v020_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_63d_63d_sp_slope_v021_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_126d_5d_sp_slope_v022_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_126d_10d_sp_slope_v023_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_126d_21d_sp_slope_v024_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_126d_42d_sp_slope_v025_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_126d_63d_sp_slope_v026_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_126d_126d_sp_slope_v027_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_189d_5d_sp_slope_v028_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_189d_10d_sp_slope_v029_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_189d_21d_sp_slope_v030_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_189d_42d_sp_slope_v031_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_189d_63d_sp_slope_v032_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_189d_126d_sp_slope_v033_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_252d_5d_sp_slope_v034_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_252d_10d_sp_slope_v035_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_252d_21d_sp_slope_v036_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_252d_42d_sp_slope_v037_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_252d_63d_sp_slope_v038_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_252d_126d_sp_slope_v039_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_378d_5d_sp_slope_v040_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_378d_10d_sp_slope_v041_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_378d_21d_sp_slope_v042_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_378d_42d_sp_slope_v043_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_378d_63d_sp_slope_v044_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_378d_126d_sp_slope_v045_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_504d_5d_sp_slope_v046_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_504d_10d_sp_slope_v047_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_504d_21d_sp_slope_v048_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_504d_42d_sp_slope_v049_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_504d_63d_sp_slope_v050_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtroll_504d_126d_sp_slope_v051_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_5d_5d_sp_slope_v052_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_10d_5d_sp_slope_v053_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_10d_10d_sp_slope_v054_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_21d_5d_sp_slope_v055_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_21d_10d_sp_slope_v056_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_21d_21d_sp_slope_v057_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_42d_5d_sp_slope_v058_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_42d_10d_sp_slope_v059_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_42d_21d_sp_slope_v060_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_42d_42d_sp_slope_v061_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_63d_5d_sp_slope_v062_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_63d_10d_sp_slope_v063_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_63d_21d_sp_slope_v064_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_63d_42d_sp_slope_v065_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_63d_63d_sp_slope_v066_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_126d_5d_sp_slope_v067_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_126d_10d_sp_slope_v068_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_126d_21d_sp_slope_v069_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_126d_42d_sp_slope_v070_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_126d_63d_sp_slope_v071_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_126d_126d_sp_slope_v072_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_189d_5d_sp_slope_v073_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_189d_10d_sp_slope_v074_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_189d_21d_sp_slope_v075_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_189d_42d_sp_slope_v076_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_189d_63d_sp_slope_v077_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_189d_126d_sp_slope_v078_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_252d_5d_sp_slope_v079_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_252d_10d_sp_slope_v080_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_252d_21d_sp_slope_v081_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_252d_42d_sp_slope_v082_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_252d_63d_sp_slope_v083_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_252d_126d_sp_slope_v084_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_378d_5d_sp_slope_v085_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_378d_10d_sp_slope_v086_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_378d_21d_sp_slope_v087_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_378d_42d_sp_slope_v088_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_378d_63d_sp_slope_v089_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_378d_126d_sp_slope_v090_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_504d_5d_sp_slope_v091_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_504d_10d_sp_slope_v092_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_504d_21d_sp_slope_v093_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_504d_42d_sp_slope_v094_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_504d_63d_sp_slope_v095_signal,
    f23cld_f23_commercial_lending_dynamics_lendrev_504d_126d_sp_slope_v096_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_5d_5d_sp_slope_v097_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_10d_5d_sp_slope_v098_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_10d_10d_sp_slope_v099_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_21d_5d_sp_slope_v100_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_21d_10d_sp_slope_v101_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_21d_21d_sp_slope_v102_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_42d_5d_sp_slope_v103_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_42d_10d_sp_slope_v104_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_42d_21d_sp_slope_v105_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_42d_42d_sp_slope_v106_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_63d_5d_sp_slope_v107_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_63d_10d_sp_slope_v108_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_63d_21d_sp_slope_v109_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_63d_42d_sp_slope_v110_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_63d_63d_sp_slope_v111_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_126d_5d_sp_slope_v112_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_126d_10d_sp_slope_v113_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_126d_21d_sp_slope_v114_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_126d_42d_sp_slope_v115_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_126d_63d_sp_slope_v116_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_126d_126d_sp_slope_v117_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_189d_5d_sp_slope_v118_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_189d_10d_sp_slope_v119_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_189d_21d_sp_slope_v120_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_189d_42d_sp_slope_v121_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_189d_63d_sp_slope_v122_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_189d_126d_sp_slope_v123_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_252d_5d_sp_slope_v124_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_252d_10d_sp_slope_v125_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_252d_21d_sp_slope_v126_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_252d_42d_sp_slope_v127_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_252d_63d_sp_slope_v128_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_252d_126d_sp_slope_v129_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_378d_5d_sp_slope_v130_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_378d_10d_sp_slope_v131_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_378d_21d_sp_slope_v132_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_378d_42d_sp_slope_v133_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_378d_63d_sp_slope_v134_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_378d_126d_sp_slope_v135_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_504d_5d_sp_slope_v136_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_504d_10d_sp_slope_v137_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_504d_21d_sp_slope_v138_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_504d_42d_sp_slope_v139_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_504d_63d_sp_slope_v140_signal,
    f23cld_f23_commercial_lending_dynamics_lendcyc_504d_126d_sp_slope_v141_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtstd_5d_5d_sp_slope_v142_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtstd_10d_5d_sp_slope_v143_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtstd_10d_10d_sp_slope_v144_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtstd_21d_5d_sp_slope_v145_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtstd_21d_10d_sp_slope_v146_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtstd_21d_21d_sp_slope_v147_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtstd_42d_5d_sp_slope_v148_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtstd_42d_10d_sp_slope_v149_signal,
    f23cld_f23_commercial_lending_dynamics_cdebtstd_42d_21d_sp_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F23_COMMERCIAL_LENDING_DYNAMICS_REGISTRY_SLOPE_001_150 = REGISTRY


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
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    assetsc      = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsc")
    assetsnc     = pd.Series(1.2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsnc")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    liabilitiesc = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesc")
    liabilitiesnc= pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesnc")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    equityusd    = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equityusd")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    debtc        = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtc")
    debtnc       = pd.Series(4.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtnc")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    intangibles  = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    tangibles    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="tangibles")
    invcap       = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")
    retearn      = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="retearn")
    sbcomp       = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="sbcomp")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    shareswadil  = pd.Series(1.02e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswadil")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    epsdil       = pd.Series(0.98 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="epsdil")
    bvps         = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="bvps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    sps          = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="sps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    pe           = pd.Series(closeadj / eps.replace(0, np.nan).abs(), name="pe")
    pb           = pd.Series(closeadj / bvps.replace(0, np.nan).abs(), name="pb")
    ps           = pd.Series(closeadj / sps.replace(0, np.nan).abs(), name="ps")
    evebit       = pd.Series(ev / ebit.replace(0, np.nan).abs(), name="evebit")
    evebitda     = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ros          = pd.Series(0.08 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ros")
    currentratio = pd.Series(1.5 + 0.3*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="currentratio")
    de           = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    divyield     = pd.Series(0.02 + 0.005*np.sin(np.arange(n)/250.0) + 0.001*np.random.randn(n), name="divyield")
    assetturnover= pd.Series(0.7 + 0.15*np.sin(np.arange(n)/250.0) + 0.02*np.random.randn(n), name="assetturnover")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "assets": assets, "assetsc": assetsc, "assetsnc": assetsnc,
        "liabilities": liabilities, "liabilitiesc": liabilitiesc, "liabilitiesnc": liabilitiesnc,
        "equity": equity, "equityusd": equityusd,
        "debt": debt, "debtc": debtc, "debtnc": debtnc, "cashneq": cashneq,
        "inventory": inventory, "receivables": receivables, "payables": payables,
        "deferredrev": deferredrev, "workingcapital": workingcapital,
        "ppnenet": ppnenet, "intangibles": intangibles, "tangibles": tangibles,
        "invcap": invcap, "retearn": retearn, "sbcomp": sbcomp,
        "sharesbas": sharesbas, "shareswa": shareswa, "shareswadil": shareswadil,
        "eps": eps, "epsdil": epsdil, "bvps": bvps, "fcfps": fcfps, "sps": sps, "dps": dps,
        "marketcap": marketcap, "ev": ev,
        "pe": pe, "pb": pb, "ps": ps, "evebit": evebit, "evebitda": evebitda,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
        "roa": roa, "roe": roe, "roic": roic, "ros": ros,
        "currentratio": currentratio, "de": de,
        "payoutratio": payoutratio, "divyield": divyield, "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f23_commercial_debt", "_f23_lending_revenue", "_f23_lending_cycle")
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
    print(f"OK f23_commercial_lending_dynamics: {n_features} features pass")
