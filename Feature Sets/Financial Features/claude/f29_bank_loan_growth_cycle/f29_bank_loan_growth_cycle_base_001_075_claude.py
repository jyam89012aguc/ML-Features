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
def _f29_loan_growth_proxy(assets, w):
    return assets.pct_change(periods=w)


def _f29_growth_acceleration(assets, w):
    g = assets.pct_change(periods=w)
    return g - g.rolling(w, min_periods=max(1, w // 2)).mean()


def _f29_loan_cycle_score(assets, equity, w):
    lev = assets / equity.replace(0, np.nan)
    return lev - lev.rolling(w, min_periods=max(1, w // 2)).mean()


def f29blg_f29_bank_loan_growth_cycle_loangrowraw_21d_base_v001_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowsm_21d_base_v002_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowstd_21d_base_v003_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowz_21d_base_v004_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowabs_21d_base_v005_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowsq_21d_base_v006_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowsign_21d_base_v007_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    result = np.sign(base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowlog_21d_base_v008_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowrng_21d_base_v009_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    rng = base.rolling(21, min_periods=max(1, 21 // 2)).max() - base.rolling(21, min_periods=max(1, 21 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowdv_21d_base_v010_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowpos_21d_base_v011_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    med = base.rolling(21, min_periods=max(1, 21 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowneg_21d_base_v012_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    med = base.rolling(21, min_periods=max(1, 21 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 21) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelraw_21d_base_v013_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelsm_21d_base_v014_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelstd_21d_base_v015_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelz_21d_base_v016_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelabs_21d_base_v017_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelsq_21d_base_v018_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelsign_21d_base_v019_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    result = np.sign(base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccellog_21d_base_v020_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelrng_21d_base_v021_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    rng = base.rolling(21, min_periods=max(1, 21 // 2)).max() - base.rolling(21, min_periods=max(1, 21 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growacceldv_21d_base_v022_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelpos_21d_base_v023_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    med = base.rolling(21, min_periods=max(1, 21 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelneg_21d_base_v024_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    med = base.rolling(21, min_periods=max(1, 21 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 21) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancycleraw_21d_base_v025_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclesm_21d_base_v026_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclestd_21d_base_v027_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclez_21d_base_v028_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancycleabs_21d_base_v029_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclesq_21d_base_v030_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclesign_21d_base_v031_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    result = np.sign(base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclelog_21d_base_v032_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclerng_21d_base_v033_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    rng = base.rolling(21, min_periods=max(1, 21 // 2)).max() - base.rolling(21, min_periods=max(1, 21 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancycledv_21d_base_v034_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclepos_21d_base_v035_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    med = base.rolling(21, min_periods=max(1, 21 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancycleneg_21d_base_v036_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    med = base.rolling(21, min_periods=max(1, 21 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 21) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowraw_42d_base_v037_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowsm_21d_base_v038_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowstd_21d_base_v039_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowz_21d_base_v040_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowabs_42d_base_v041_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowsq_42d_base_v042_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 42)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowsign_21d_base_v043_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    result = np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowlog_42d_base_v044_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 42)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowrng_21d_base_v045_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    rng = base.rolling(63, min_periods=max(1, 63 // 2)).max() - base.rolling(63, min_periods=max(1, 63 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowdv_21d_base_v046_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowpos_21d_base_v047_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    med = base.rolling(63, min_periods=max(1, 63 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowneg_21d_base_v048_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    med = base.rolling(63, min_periods=max(1, 63 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 63) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelraw_42d_base_v049_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelsm_21d_base_v050_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelstd_21d_base_v051_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelz_21d_base_v052_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelabs_42d_base_v053_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelsq_42d_base_v054_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 42)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelsign_21d_base_v055_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    result = np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccellog_42d_base_v056_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 42)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelrng_21d_base_v057_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    rng = base.rolling(63, min_periods=max(1, 63 // 2)).max() - base.rolling(63, min_periods=max(1, 63 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growacceldv_21d_base_v058_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelpos_21d_base_v059_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    med = base.rolling(63, min_periods=max(1, 63 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelneg_21d_base_v060_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    med = base.rolling(63, min_periods=max(1, 63 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 63) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancycleraw_42d_base_v061_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclesm_21d_base_v062_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclestd_21d_base_v063_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclez_21d_base_v064_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancycleabs_42d_base_v065_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclesq_42d_base_v066_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 42)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclesign_21d_base_v067_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    result = np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclelog_42d_base_v068_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 42)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclerng_21d_base_v069_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    rng = base.rolling(63, min_periods=max(1, 63 // 2)).max() - base.rolling(63, min_periods=max(1, 63 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancycledv_21d_base_v070_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclepos_21d_base_v071_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    med = base.rolling(63, min_periods=max(1, 63 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancycleneg_21d_base_v072_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    med = base.rolling(63, min_periods=max(1, 63 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 63) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowraw_63d_base_v073_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowsm_21d_base_v074_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowstd_21d_base_v075_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f29blg_f29_bank_loan_growth_cycle_loangrowraw_21d_base_v001_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowsm_21d_base_v002_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowstd_21d_base_v003_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowz_21d_base_v004_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowabs_21d_base_v005_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowsq_21d_base_v006_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowsign_21d_base_v007_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowlog_21d_base_v008_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowrng_21d_base_v009_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowdv_21d_base_v010_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowpos_21d_base_v011_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowneg_21d_base_v012_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelraw_21d_base_v013_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelsm_21d_base_v014_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelstd_21d_base_v015_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelz_21d_base_v016_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelabs_21d_base_v017_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelsq_21d_base_v018_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelsign_21d_base_v019_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccellog_21d_base_v020_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelrng_21d_base_v021_signal,
    f29blg_f29_bank_loan_growth_cycle_growacceldv_21d_base_v022_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelpos_21d_base_v023_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelneg_21d_base_v024_signal,
    f29blg_f29_bank_loan_growth_cycle_loancycleraw_21d_base_v025_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclesm_21d_base_v026_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclestd_21d_base_v027_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclez_21d_base_v028_signal,
    f29blg_f29_bank_loan_growth_cycle_loancycleabs_21d_base_v029_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclesq_21d_base_v030_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclesign_21d_base_v031_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclelog_21d_base_v032_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclerng_21d_base_v033_signal,
    f29blg_f29_bank_loan_growth_cycle_loancycledv_21d_base_v034_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclepos_21d_base_v035_signal,
    f29blg_f29_bank_loan_growth_cycle_loancycleneg_21d_base_v036_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowraw_42d_base_v037_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowsm_21d_base_v038_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowstd_21d_base_v039_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowz_21d_base_v040_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowabs_42d_base_v041_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowsq_42d_base_v042_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowsign_21d_base_v043_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowlog_42d_base_v044_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowrng_21d_base_v045_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowdv_21d_base_v046_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowpos_21d_base_v047_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowneg_21d_base_v048_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelraw_42d_base_v049_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelsm_21d_base_v050_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelstd_21d_base_v051_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelz_21d_base_v052_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelabs_42d_base_v053_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelsq_42d_base_v054_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelsign_21d_base_v055_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccellog_42d_base_v056_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelrng_21d_base_v057_signal,
    f29blg_f29_bank_loan_growth_cycle_growacceldv_21d_base_v058_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelpos_21d_base_v059_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelneg_21d_base_v060_signal,
    f29blg_f29_bank_loan_growth_cycle_loancycleraw_42d_base_v061_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclesm_21d_base_v062_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclestd_21d_base_v063_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclez_21d_base_v064_signal,
    f29blg_f29_bank_loan_growth_cycle_loancycleabs_42d_base_v065_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclesq_42d_base_v066_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclesign_21d_base_v067_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclelog_42d_base_v068_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclerng_21d_base_v069_signal,
    f29blg_f29_bank_loan_growth_cycle_loancycledv_21d_base_v070_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclepos_21d_base_v071_signal,
    f29blg_f29_bank_loan_growth_cycle_loancycleneg_21d_base_v072_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowraw_63d_base_v073_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowsm_21d_base_v074_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowstd_21d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F29_BANK_LOAN_GROWTH_CYCLE_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f29_bank_loan_growth_cycle_base_001_075_claude: {n_features} features pass")
