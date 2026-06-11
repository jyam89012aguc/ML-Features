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


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f29_loan_growth_proxy(assets, w):
    return assets.pct_change(periods=w)


def _f29_growth_acceleration(assets, w):
    g = assets.pct_change(periods=w)
    return g - g.rolling(w, min_periods=max(1, w // 2)).mean()


def _f29_loan_cycle_score(assets, equity, w):
    lev = assets / equity.replace(0, np.nan)
    return lev - lev.rolling(w, min_periods=max(1, w // 2)).mean()


def f29blg_f29_bank_loan_growth_cycle_loangrowraw_21d_jerk_v001_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowsm_21d_jerk_v002_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    base = _mean(base, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowz_21d_jerk_v003_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    base = _z(base, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowabs_21d_jerk_v004_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    base = base.abs()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowscaled_21d_jerk_v005_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    base = base * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelraw_21d_jerk_v006_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelsm_21d_jerk_v007_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    base = _mean(base, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelz_21d_jerk_v008_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    base = _z(base, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelabs_21d_jerk_v009_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    base = base.abs()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelscaled_21d_jerk_v010_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    base = base * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancycleraw_21d_jerk_v011_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclesm_21d_jerk_v012_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    base = _mean(base, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclez_21d_jerk_v013_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    base = _z(base, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancycleabs_21d_jerk_v014_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    base = base.abs()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclescaled_21d_jerk_v015_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    base = base * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowraw_21d_jerk_v016_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowsm_21d_jerk_v017_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    base = _mean(base, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowz_21d_jerk_v018_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    base = _z(base, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowabs_21d_jerk_v019_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    base = base.abs()
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowscaled_21d_jerk_v020_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    base = base * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelraw_21d_jerk_v021_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelsm_21d_jerk_v022_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    base = _mean(base, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelz_21d_jerk_v023_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    base = _z(base, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelabs_21d_jerk_v024_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    base = base.abs()
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelscaled_21d_jerk_v025_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    base = base * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancycleraw_21d_jerk_v026_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclesm_21d_jerk_v027_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    base = _mean(base, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclez_21d_jerk_v028_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    base = _z(base, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancycleabs_21d_jerk_v029_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    base = base.abs()
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclescaled_21d_jerk_v030_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    base = base * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowraw_21d_jerk_v031_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowsm_21d_jerk_v032_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    base = _mean(base, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowz_21d_jerk_v033_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    base = _z(base, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowabs_21d_jerk_v034_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    base = base.abs()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowscaled_21d_jerk_v035_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    base = base * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelraw_21d_jerk_v036_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelsm_21d_jerk_v037_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    base = _mean(base, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelz_21d_jerk_v038_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    base = _z(base, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelabs_21d_jerk_v039_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    base = base.abs()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelscaled_21d_jerk_v040_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    base = base * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancycleraw_21d_jerk_v041_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclesm_21d_jerk_v042_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    base = _mean(base, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclez_21d_jerk_v043_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    base = _z(base, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancycleabs_21d_jerk_v044_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    base = base.abs()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclescaled_21d_jerk_v045_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    base = base * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowraw_21d_jerk_v046_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowsm_21d_jerk_v047_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    base = _mean(base, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowz_21d_jerk_v048_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    base = _z(base, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowabs_21d_jerk_v049_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    base = base.abs()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowscaled_21d_jerk_v050_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    base = base * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelraw_21d_jerk_v051_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelsm_21d_jerk_v052_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    base = _mean(base, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelz_21d_jerk_v053_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    base = _z(base, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelabs_21d_jerk_v054_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    base = base.abs()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelscaled_21d_jerk_v055_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    base = base * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancycleraw_21d_jerk_v056_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclesm_21d_jerk_v057_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    base = _mean(base, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclez_21d_jerk_v058_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    base = _z(base, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancycleabs_21d_jerk_v059_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    base = base.abs()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclescaled_21d_jerk_v060_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    base = base * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowraw_21d_jerk_v061_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowsm_21d_jerk_v062_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    base = _mean(base, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowz_21d_jerk_v063_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    base = _z(base, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowabs_21d_jerk_v064_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    base = base.abs()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowscaled_21d_jerk_v065_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    base = base * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelraw_21d_jerk_v066_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelsm_21d_jerk_v067_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    base = _mean(base, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelz_21d_jerk_v068_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    base = _z(base, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelabs_21d_jerk_v069_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    base = base.abs()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelscaled_21d_jerk_v070_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    base = base * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancycleraw_21d_jerk_v071_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclesm_21d_jerk_v072_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    base = _mean(base, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclez_21d_jerk_v073_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    base = _z(base, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancycleabs_21d_jerk_v074_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    base = base.abs()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclescaled_21d_jerk_v075_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    base = base * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowraw_21d_jerk_v076_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowsm_21d_jerk_v077_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    base = _mean(base, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowz_21d_jerk_v078_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    base = _z(base, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowabs_21d_jerk_v079_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    base = base.abs()
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowscaled_21d_jerk_v080_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    base = base * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelraw_21d_jerk_v081_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelsm_21d_jerk_v082_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    base = _mean(base, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelz_21d_jerk_v083_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    base = _z(base, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelabs_21d_jerk_v084_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    base = base.abs()
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelscaled_21d_jerk_v085_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    base = base * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancycleraw_21d_jerk_v086_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclesm_21d_jerk_v087_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    base = _mean(base, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclez_21d_jerk_v088_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    base = _z(base, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancycleabs_21d_jerk_v089_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    base = base.abs()
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclescaled_21d_jerk_v090_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    base = base * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowraw_42d_jerk_v091_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 42)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowsm_21d_jerk_v092_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    base = _mean(base, 126)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowz_21d_jerk_v093_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    base = _z(base, 126)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowabs_42d_jerk_v094_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 42)
    base = base.abs()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowscaled_42d_jerk_v095_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 42)
    base = base * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelraw_42d_jerk_v096_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 42)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelsm_21d_jerk_v097_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    base = _mean(base, 126)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelz_21d_jerk_v098_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    base = _z(base, 126)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelabs_42d_jerk_v099_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 42)
    base = base.abs()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelscaled_42d_jerk_v100_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 42)
    base = base * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancycleraw_42d_jerk_v101_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 42)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclesm_21d_jerk_v102_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    base = _mean(base, 126)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclez_21d_jerk_v103_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    base = _z(base, 126)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancycleabs_42d_jerk_v104_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 42)
    base = base.abs()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclescaled_42d_jerk_v105_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 42)
    base = base * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowraw_42d_jerk_v106_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 42)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowsm_21d_jerk_v107_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    base = _mean(base, 252)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowz_21d_jerk_v108_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    base = _z(base, 252)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowabs_42d_jerk_v109_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 42)
    base = base.abs()
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowscaled_42d_jerk_v110_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 42)
    base = base * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelraw_42d_jerk_v111_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 42)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelsm_21d_jerk_v112_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    base = _mean(base, 252)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelz_21d_jerk_v113_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    base = _z(base, 252)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelabs_42d_jerk_v114_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 42)
    base = base.abs()
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelscaled_42d_jerk_v115_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 42)
    base = base * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancycleraw_42d_jerk_v116_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 42)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclesm_21d_jerk_v117_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    base = _mean(base, 252)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclez_21d_jerk_v118_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    base = _z(base, 252)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancycleabs_42d_jerk_v119_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 42)
    base = base.abs()
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclescaled_42d_jerk_v120_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 42)
    base = base * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowraw_42d_jerk_v121_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 42)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowsm_21d_jerk_v122_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    base = _mean(base, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowz_21d_jerk_v123_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    base = _z(base, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowabs_42d_jerk_v124_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 42)
    base = base.abs()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowscaled_42d_jerk_v125_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 42)
    base = base * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelraw_42d_jerk_v126_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 42)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelsm_21d_jerk_v127_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    base = _mean(base, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelz_21d_jerk_v128_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    base = _z(base, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelabs_42d_jerk_v129_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 42)
    base = base.abs()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelscaled_42d_jerk_v130_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 42)
    base = base * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancycleraw_42d_jerk_v131_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 42)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclesm_21d_jerk_v132_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    base = _mean(base, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclez_21d_jerk_v133_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    base = _z(base, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancycleabs_42d_jerk_v134_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 42)
    base = base.abs()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclescaled_42d_jerk_v135_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 42)
    base = base * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowraw_42d_jerk_v136_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 42)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowsm_21d_jerk_v137_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    base = _mean(base, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowz_21d_jerk_v138_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    base = _z(base, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowabs_42d_jerk_v139_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 42)
    base = base.abs()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowscaled_42d_jerk_v140_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 42)
    base = base * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelraw_42d_jerk_v141_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 42)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelsm_21d_jerk_v142_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    base = _mean(base, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelz_21d_jerk_v143_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    base = _z(base, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelabs_42d_jerk_v144_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 42)
    base = base.abs()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelscaled_42d_jerk_v145_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 42)
    base = base * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancycleraw_42d_jerk_v146_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 42)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclesm_21d_jerk_v147_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    base = _mean(base, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclez_21d_jerk_v148_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    base = _z(base, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancycleabs_42d_jerk_v149_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 42)
    base = base.abs()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclescaled_42d_jerk_v150_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 42)
    base = base * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f29blg_f29_bank_loan_growth_cycle_loangrowraw_21d_jerk_v001_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowsm_21d_jerk_v002_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowz_21d_jerk_v003_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowabs_21d_jerk_v004_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowscaled_21d_jerk_v005_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelraw_21d_jerk_v006_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelsm_21d_jerk_v007_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelz_21d_jerk_v008_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelabs_21d_jerk_v009_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelscaled_21d_jerk_v010_signal,
    f29blg_f29_bank_loan_growth_cycle_loancycleraw_21d_jerk_v011_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclesm_21d_jerk_v012_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclez_21d_jerk_v013_signal,
    f29blg_f29_bank_loan_growth_cycle_loancycleabs_21d_jerk_v014_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclescaled_21d_jerk_v015_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowraw_21d_jerk_v016_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowsm_21d_jerk_v017_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowz_21d_jerk_v018_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowabs_21d_jerk_v019_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowscaled_21d_jerk_v020_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelraw_21d_jerk_v021_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelsm_21d_jerk_v022_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelz_21d_jerk_v023_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelabs_21d_jerk_v024_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelscaled_21d_jerk_v025_signal,
    f29blg_f29_bank_loan_growth_cycle_loancycleraw_21d_jerk_v026_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclesm_21d_jerk_v027_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclez_21d_jerk_v028_signal,
    f29blg_f29_bank_loan_growth_cycle_loancycleabs_21d_jerk_v029_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclescaled_21d_jerk_v030_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowraw_21d_jerk_v031_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowsm_21d_jerk_v032_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowz_21d_jerk_v033_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowabs_21d_jerk_v034_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowscaled_21d_jerk_v035_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelraw_21d_jerk_v036_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelsm_21d_jerk_v037_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelz_21d_jerk_v038_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelabs_21d_jerk_v039_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelscaled_21d_jerk_v040_signal,
    f29blg_f29_bank_loan_growth_cycle_loancycleraw_21d_jerk_v041_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclesm_21d_jerk_v042_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclez_21d_jerk_v043_signal,
    f29blg_f29_bank_loan_growth_cycle_loancycleabs_21d_jerk_v044_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclescaled_21d_jerk_v045_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowraw_21d_jerk_v046_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowsm_21d_jerk_v047_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowz_21d_jerk_v048_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowabs_21d_jerk_v049_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowscaled_21d_jerk_v050_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelraw_21d_jerk_v051_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelsm_21d_jerk_v052_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelz_21d_jerk_v053_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelabs_21d_jerk_v054_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelscaled_21d_jerk_v055_signal,
    f29blg_f29_bank_loan_growth_cycle_loancycleraw_21d_jerk_v056_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclesm_21d_jerk_v057_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclez_21d_jerk_v058_signal,
    f29blg_f29_bank_loan_growth_cycle_loancycleabs_21d_jerk_v059_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclescaled_21d_jerk_v060_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowraw_21d_jerk_v061_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowsm_21d_jerk_v062_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowz_21d_jerk_v063_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowabs_21d_jerk_v064_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowscaled_21d_jerk_v065_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelraw_21d_jerk_v066_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelsm_21d_jerk_v067_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelz_21d_jerk_v068_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelabs_21d_jerk_v069_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelscaled_21d_jerk_v070_signal,
    f29blg_f29_bank_loan_growth_cycle_loancycleraw_21d_jerk_v071_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclesm_21d_jerk_v072_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclez_21d_jerk_v073_signal,
    f29blg_f29_bank_loan_growth_cycle_loancycleabs_21d_jerk_v074_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclescaled_21d_jerk_v075_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowraw_21d_jerk_v076_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowsm_21d_jerk_v077_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowz_21d_jerk_v078_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowabs_21d_jerk_v079_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowscaled_21d_jerk_v080_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelraw_21d_jerk_v081_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelsm_21d_jerk_v082_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelz_21d_jerk_v083_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelabs_21d_jerk_v084_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelscaled_21d_jerk_v085_signal,
    f29blg_f29_bank_loan_growth_cycle_loancycleraw_21d_jerk_v086_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclesm_21d_jerk_v087_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclez_21d_jerk_v088_signal,
    f29blg_f29_bank_loan_growth_cycle_loancycleabs_21d_jerk_v089_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclescaled_21d_jerk_v090_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowraw_42d_jerk_v091_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowsm_21d_jerk_v092_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowz_21d_jerk_v093_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowabs_42d_jerk_v094_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowscaled_42d_jerk_v095_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelraw_42d_jerk_v096_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelsm_21d_jerk_v097_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelz_21d_jerk_v098_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelabs_42d_jerk_v099_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelscaled_42d_jerk_v100_signal,
    f29blg_f29_bank_loan_growth_cycle_loancycleraw_42d_jerk_v101_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclesm_21d_jerk_v102_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclez_21d_jerk_v103_signal,
    f29blg_f29_bank_loan_growth_cycle_loancycleabs_42d_jerk_v104_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclescaled_42d_jerk_v105_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowraw_42d_jerk_v106_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowsm_21d_jerk_v107_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowz_21d_jerk_v108_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowabs_42d_jerk_v109_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowscaled_42d_jerk_v110_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelraw_42d_jerk_v111_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelsm_21d_jerk_v112_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelz_21d_jerk_v113_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelabs_42d_jerk_v114_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelscaled_42d_jerk_v115_signal,
    f29blg_f29_bank_loan_growth_cycle_loancycleraw_42d_jerk_v116_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclesm_21d_jerk_v117_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclez_21d_jerk_v118_signal,
    f29blg_f29_bank_loan_growth_cycle_loancycleabs_42d_jerk_v119_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclescaled_42d_jerk_v120_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowraw_42d_jerk_v121_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowsm_21d_jerk_v122_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowz_21d_jerk_v123_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowabs_42d_jerk_v124_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowscaled_42d_jerk_v125_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelraw_42d_jerk_v126_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelsm_21d_jerk_v127_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelz_21d_jerk_v128_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelabs_42d_jerk_v129_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelscaled_42d_jerk_v130_signal,
    f29blg_f29_bank_loan_growth_cycle_loancycleraw_42d_jerk_v131_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclesm_21d_jerk_v132_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclez_21d_jerk_v133_signal,
    f29blg_f29_bank_loan_growth_cycle_loancycleabs_42d_jerk_v134_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclescaled_42d_jerk_v135_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowraw_42d_jerk_v136_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowsm_21d_jerk_v137_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowz_21d_jerk_v138_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowabs_42d_jerk_v139_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowscaled_42d_jerk_v140_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelraw_42d_jerk_v141_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelsm_21d_jerk_v142_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelz_21d_jerk_v143_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelabs_42d_jerk_v144_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelscaled_42d_jerk_v145_signal,
    f29blg_f29_bank_loan_growth_cycle_loancycleraw_42d_jerk_v146_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclesm_21d_jerk_v147_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclez_21d_jerk_v148_signal,
    f29blg_f29_bank_loan_growth_cycle_loancycleabs_42d_jerk_v149_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclescaled_42d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F29_BANK_LOAN_GROWTH_CYCLE_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    equity = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")

    cols = {"assets": assets, "equity": equity, "closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f29_loan_growth_proxy", "_f29_growth_acceleration", "_f29_loan_cycle_score")
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
    print(f"OK f29_bank_loan_growth_cycle_3rd_derivatives_001_150_claude: {n_features} features pass")
