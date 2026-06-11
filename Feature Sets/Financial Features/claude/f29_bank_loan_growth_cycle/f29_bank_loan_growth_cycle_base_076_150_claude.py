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


def f29blg_f29_bank_loan_growth_cycle_loangrowz_21d_base_v076_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowabs_63d_base_v077_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowsq_63d_base_v078_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowsign_21d_base_v079_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    result = np.sign(base) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowlog_63d_base_v080_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 63)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowrng_21d_base_v081_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    rng = base.rolling(126, min_periods=max(1, 126 // 2)).max() - base.rolling(126, min_periods=max(1, 126 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowdv_21d_base_v082_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    result = base * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowpos_21d_base_v083_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    med = base.rolling(126, min_periods=max(1, 126 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowneg_21d_base_v084_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    med = base.rolling(126, min_periods=max(1, 126 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 126) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelraw_63d_base_v085_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelsm_21d_base_v086_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelstd_21d_base_v087_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelz_21d_base_v088_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelabs_63d_base_v089_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelsq_63d_base_v090_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelsign_21d_base_v091_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    result = np.sign(base) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccellog_63d_base_v092_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 63)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelrng_21d_base_v093_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    rng = base.rolling(126, min_periods=max(1, 126 // 2)).max() - base.rolling(126, min_periods=max(1, 126 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growacceldv_21d_base_v094_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    result = base * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelpos_21d_base_v095_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    med = base.rolling(126, min_periods=max(1, 126 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelneg_21d_base_v096_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    med = base.rolling(126, min_periods=max(1, 126 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 126) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancycleraw_63d_base_v097_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclesm_21d_base_v098_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclestd_21d_base_v099_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclez_21d_base_v100_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancycleabs_63d_base_v101_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclesq_63d_base_v102_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclesign_21d_base_v103_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    result = np.sign(base) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclelog_63d_base_v104_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 63)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclerng_21d_base_v105_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    rng = base.rolling(126, min_periods=max(1, 126 // 2)).max() - base.rolling(126, min_periods=max(1, 126 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancycledv_21d_base_v106_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    result = base * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclepos_21d_base_v107_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    med = base.rolling(126, min_periods=max(1, 126 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancycleneg_21d_base_v108_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    med = base.rolling(126, min_periods=max(1, 126 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 126) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowraw_126d_base_v109_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowsm_21d_base_v110_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowstd_21d_base_v111_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowz_21d_base_v112_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowabs_126d_base_v113_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowsq_126d_base_v114_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 126)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowsign_21d_base_v115_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    result = np.sign(base) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowlog_126d_base_v116_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 126)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowrng_21d_base_v117_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    rng = base.rolling(252, min_periods=max(1, 252 // 2)).max() - base.rolling(252, min_periods=max(1, 252 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowdv_21d_base_v118_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowpos_21d_base_v119_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    med = base.rolling(252, min_periods=max(1, 252 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowneg_21d_base_v120_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    med = base.rolling(252, min_periods=max(1, 252 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 252) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelraw_126d_base_v121_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelsm_21d_base_v122_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelstd_21d_base_v123_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelz_21d_base_v124_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelabs_126d_base_v125_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelsq_126d_base_v126_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 126)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelsign_21d_base_v127_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    result = np.sign(base) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccellog_126d_base_v128_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 126)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelrng_21d_base_v129_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    rng = base.rolling(252, min_periods=max(1, 252 // 2)).max() - base.rolling(252, min_periods=max(1, 252 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growacceldv_21d_base_v130_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelpos_21d_base_v131_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    med = base.rolling(252, min_periods=max(1, 252 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_growaccelneg_21d_base_v132_signal(assets, closeadj):
    base = _f29_growth_acceleration(assets, 21)
    med = base.rolling(252, min_periods=max(1, 252 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 252) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancycleraw_126d_base_v133_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclesm_21d_base_v134_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclestd_21d_base_v135_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclez_21d_base_v136_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancycleabs_126d_base_v137_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclesq_126d_base_v138_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 126)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclesign_21d_base_v139_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    result = np.sign(base) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclelog_126d_base_v140_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 126)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclerng_21d_base_v141_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    rng = base.rolling(252, min_periods=max(1, 252 // 2)).max() - base.rolling(252, min_periods=max(1, 252 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancycledv_21d_base_v142_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancyclepos_21d_base_v143_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    med = base.rolling(252, min_periods=max(1, 252 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loancycleneg_21d_base_v144_signal(assets, equity, closeadj):
    base = _f29_loan_cycle_score(assets, equity, 21)
    med = base.rolling(252, min_periods=max(1, 252 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 252) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowraw_189d_base_v145_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowsm_21d_base_v146_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowstd_21d_base_v147_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowz_21d_base_v148_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 21)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowabs_189d_base_v149_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f29blg_f29_bank_loan_growth_cycle_loangrowsq_189d_base_v150_signal(assets, closeadj):
    base = _f29_loan_growth_proxy(assets, 189)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f29blg_f29_bank_loan_growth_cycle_loangrowz_21d_base_v076_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowabs_63d_base_v077_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowsq_63d_base_v078_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowsign_21d_base_v079_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowlog_63d_base_v080_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowrng_21d_base_v081_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowdv_21d_base_v082_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowpos_21d_base_v083_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowneg_21d_base_v084_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelraw_63d_base_v085_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelsm_21d_base_v086_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelstd_21d_base_v087_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelz_21d_base_v088_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelabs_63d_base_v089_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelsq_63d_base_v090_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelsign_21d_base_v091_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccellog_63d_base_v092_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelrng_21d_base_v093_signal,
    f29blg_f29_bank_loan_growth_cycle_growacceldv_21d_base_v094_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelpos_21d_base_v095_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelneg_21d_base_v096_signal,
    f29blg_f29_bank_loan_growth_cycle_loancycleraw_63d_base_v097_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclesm_21d_base_v098_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclestd_21d_base_v099_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclez_21d_base_v100_signal,
    f29blg_f29_bank_loan_growth_cycle_loancycleabs_63d_base_v101_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclesq_63d_base_v102_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclesign_21d_base_v103_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclelog_63d_base_v104_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclerng_21d_base_v105_signal,
    f29blg_f29_bank_loan_growth_cycle_loancycledv_21d_base_v106_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclepos_21d_base_v107_signal,
    f29blg_f29_bank_loan_growth_cycle_loancycleneg_21d_base_v108_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowraw_126d_base_v109_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowsm_21d_base_v110_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowstd_21d_base_v111_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowz_21d_base_v112_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowabs_126d_base_v113_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowsq_126d_base_v114_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowsign_21d_base_v115_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowlog_126d_base_v116_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowrng_21d_base_v117_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowdv_21d_base_v118_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowpos_21d_base_v119_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowneg_21d_base_v120_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelraw_126d_base_v121_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelsm_21d_base_v122_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelstd_21d_base_v123_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelz_21d_base_v124_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelabs_126d_base_v125_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelsq_126d_base_v126_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelsign_21d_base_v127_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccellog_126d_base_v128_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelrng_21d_base_v129_signal,
    f29blg_f29_bank_loan_growth_cycle_growacceldv_21d_base_v130_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelpos_21d_base_v131_signal,
    f29blg_f29_bank_loan_growth_cycle_growaccelneg_21d_base_v132_signal,
    f29blg_f29_bank_loan_growth_cycle_loancycleraw_126d_base_v133_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclesm_21d_base_v134_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclestd_21d_base_v135_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclez_21d_base_v136_signal,
    f29blg_f29_bank_loan_growth_cycle_loancycleabs_126d_base_v137_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclesq_126d_base_v138_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclesign_21d_base_v139_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclelog_126d_base_v140_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclerng_21d_base_v141_signal,
    f29blg_f29_bank_loan_growth_cycle_loancycledv_21d_base_v142_signal,
    f29blg_f29_bank_loan_growth_cycle_loancyclepos_21d_base_v143_signal,
    f29blg_f29_bank_loan_growth_cycle_loancycleneg_21d_base_v144_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowraw_189d_base_v145_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowsm_21d_base_v146_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowstd_21d_base_v147_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowz_21d_base_v148_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowabs_189d_base_v149_signal,
    f29blg_f29_bank_loan_growth_cycle_loangrowsq_189d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F29_BANK_LOAN_GROWTH_CYCLE_REGISTRY_076_150 = REGISTRY


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
    print(f"OK f29_bank_loan_growth_cycle_base_076_150_claude: {n_features} features pass")
