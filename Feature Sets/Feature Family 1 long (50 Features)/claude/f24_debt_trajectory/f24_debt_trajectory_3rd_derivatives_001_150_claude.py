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
def _f24_debt_traj(debt, w):
    base = debt.rolling(w, min_periods=max(1, w // 2)).mean()
    return base.diff(periods=w) / base.abs().shift(w).replace(0, np.nan)


def _f24_debt_growth(debt, w):
    return debt.diff(periods=w) / debt.abs().rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)


def _f24_leverage_traj(debt, equity, w):
    lev = debt / equity.replace(0, np.nan)
    return lev.diff(periods=w) / lev.abs().shift(w).replace(0, np.nan)


# 5d jerk of 21d debt growth × close
def f24dt_f24_debt_trajectory_debtgrowth_21d_jerk_v001_signal(debt, closeadj):
    base = _f24_debt_growth(debt, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d debt growth × close
def f24dt_f24_debt_trajectory_debtgrowth_21d_jerk_v002_signal(debt, closeadj):
    base = _f24_debt_growth(debt, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 63d debt growth × close
def f24dt_f24_debt_trajectory_debtgrowth_63d_jerk_v003_signal(debt, closeadj):
    base = _f24_debt_growth(debt, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d debt growth × close
def f24dt_f24_debt_trajectory_debtgrowth_63d_jerk_v004_signal(debt, closeadj):
    base = _f24_debt_growth(debt, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d debt growth × close
def f24dt_f24_debt_trajectory_debtgrowth_63d_jerk_v005_signal(debt, closeadj):
    base = _f24_debt_growth(debt, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 126d debt growth × close
def f24dt_f24_debt_trajectory_debtgrowth_126d_jerk_v006_signal(debt, closeadj):
    base = _f24_debt_growth(debt, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 126d debt growth × close
def f24dt_f24_debt_trajectory_debtgrowth_126d_jerk_v007_signal(debt, closeadj):
    base = _f24_debt_growth(debt, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d debt growth × close
def f24dt_f24_debt_trajectory_debtgrowth_252d_jerk_v008_signal(debt, closeadj):
    base = _f24_debt_growth(debt, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt growth × close
def f24dt_f24_debt_trajectory_debtgrowth_252d_jerk_v009_signal(debt, closeadj):
    base = _f24_debt_growth(debt, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 504d debt growth × close
def f24dt_f24_debt_trajectory_debtgrowth_504d_jerk_v010_signal(debt, closeadj):
    base = _f24_debt_growth(debt, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d debt growth × close
def f24dt_f24_debt_trajectory_debtgrowth_504d_jerk_v011_signal(debt, closeadj):
    base = _f24_debt_growth(debt, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d debt traj × close
def f24dt_f24_debt_trajectory_debttraj_21d_jerk_v012_signal(debt, closeadj):
    base = _f24_debt_traj(debt, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d debt traj × close
def f24dt_f24_debt_trajectory_debttraj_63d_jerk_v013_signal(debt, closeadj):
    base = _f24_debt_traj(debt, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 126d debt traj × close
def f24dt_f24_debt_trajectory_debttraj_126d_jerk_v014_signal(debt, closeadj):
    base = _f24_debt_traj(debt, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt traj × close
def f24dt_f24_debt_trajectory_debttraj_252d_jerk_v015_signal(debt, closeadj):
    base = _f24_debt_traj(debt, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d debt traj × close
def f24dt_f24_debt_trajectory_debttraj_504d_jerk_v016_signal(debt, closeadj):
    base = _f24_debt_traj(debt, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d leverage traj × close
def f24dt_f24_debt_trajectory_levtraj_21d_jerk_v017_signal(debt, equity, closeadj):
    base = _f24_leverage_traj(debt, equity, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d leverage traj × close
def f24dt_f24_debt_trajectory_levtraj_63d_jerk_v018_signal(debt, equity, closeadj):
    base = _f24_leverage_traj(debt, equity, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d leverage traj × close
def f24dt_f24_debt_trajectory_levtraj_252d_jerk_v019_signal(debt, equity, closeadj):
    base = _f24_leverage_traj(debt, equity, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d mean debt growth × close
def f24dt_f24_debt_trajectory_debtgrowthmean_63d_jerk_v020_signal(debt, closeadj):
    base = _mean(_f24_debt_growth(debt, 63), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d mean debt growth × close
def f24dt_f24_debt_trajectory_debtgrowthmean_252d_jerk_v021_signal(debt, closeadj):
    base = _mean(_f24_debt_growth(debt, 252), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d std debt growth × close
def f24dt_f24_debt_trajectory_debtgrowthstd_63d_jerk_v022_signal(debt, closeadj):
    base = _std(_f24_debt_growth(debt, 63), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d std debt growth × close
def f24dt_f24_debt_trajectory_debtgrowthstd_252d_jerk_v023_signal(debt, closeadj):
    base = _std(_f24_debt_growth(debt, 252), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d debt growth zscore
def f24dt_f24_debt_trajectory_debtgrowthz_252d_jerk_v024_signal(debt, closeadj):
    base = _z(_f24_debt_growth(debt, 63), 252)
    sl = base.diff(periods=21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d debt growth zscore
def f24dt_f24_debt_trajectory_debtgrowthz_504d_jerk_v025_signal(debt, closeadj):
    base = _z(_f24_debt_growth(debt, 252), 504)
    sl = base.diff(periods=63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d debt traj zscore
def f24dt_f24_debt_trajectory_debttrajz_252d_jerk_v026_signal(debt, closeadj):
    base = _z(_f24_debt_traj(debt, 63), 252)
    sl = base.diff(periods=21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d debt traj zscore
def f24dt_f24_debt_trajectory_debttrajz_504d_jerk_v027_signal(debt, closeadj):
    base = _z(_f24_debt_traj(debt, 252), 504)
    sl = base.diff(periods=63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d debt growth high count × close
def f24dt_f24_debt_trajectory_debtgrowthhighcount_252d_jerk_v028_signal(debt, closeadj):
    flag = (_f24_debt_growth(debt, 63) > 0.02).astype(float)
    base = flag.rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d debt growth low count × close
def f24dt_f24_debt_trajectory_debtgrowthlowcount_504d_jerk_v029_signal(debt, closeadj):
    flag = (_f24_debt_growth(debt, 252) < -0.02).astype(float)
    base = flag.rolling(504, min_periods=126).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d leverage traj exp count × close
def f24dt_f24_debt_trajectory_levtrajexpcount_252d_jerk_v030_signal(debt, equity, closeadj):
    flag = (_f24_leverage_traj(debt, equity, 63) > 0).astype(float)
    base = flag.rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d debt growth squared × close
def f24dt_f24_debt_trajectory_debtgrowthsq_21d_jerk_v031_signal(debt, closeadj):
    g = _f24_debt_growth(debt, 21)
    base = g * g.abs() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d debt growth squared × close
def f24dt_f24_debt_trajectory_debtgrowthsq_63d_jerk_v032_signal(debt, closeadj):
    g = _f24_debt_growth(debt, 63)
    base = g * g.abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt growth squared × close
def f24dt_f24_debt_trajectory_debtgrowthsq_252d_jerk_v033_signal(debt, closeadj):
    g = _f24_debt_growth(debt, 252)
    base = g * g.abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d debt traj × revenue
def f24dt_f24_debt_trajectory_debttrajxrev_21d_jerk_v034_signal(debt, revenue, closeadj):
    base = _f24_debt_traj(debt, 21) * revenue
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d debt traj × revenue
def f24dt_f24_debt_trajectory_debttrajxrev_63d_jerk_v035_signal(debt, revenue, closeadj):
    base = _f24_debt_traj(debt, 63) * revenue
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt growth × revenue
def f24dt_f24_debt_trajectory_debtgrowthxrev_252d_jerk_v036_signal(debt, revenue, closeadj):
    base = _f24_debt_growth(debt, 252) * revenue
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of debt growth diff 21m63 × close
def f24dt_f24_debt_trajectory_debtgrowthdiff_21m63_jerk_v037_signal(debt, closeadj):
    base = (_f24_debt_growth(debt, 21) - _f24_debt_growth(debt, 63)) * closeadj
    sl = base.diff(periods=5)
    result = sl.diff(periods=5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of debt growth diff 63m252 × close
def f24dt_f24_debt_trajectory_debtgrowthdiff_63m252_jerk_v038_signal(debt, closeadj):
    base = (_f24_debt_growth(debt, 63) - _f24_debt_growth(debt, 252)) * closeadj
    sl = base.diff(periods=21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of debt growth diff 252m504 × close
def f24dt_f24_debt_trajectory_debtgrowthdiff_252m504_jerk_v039_signal(debt, closeadj):
    base = (_f24_debt_growth(debt, 252) - _f24_debt_growth(debt, 504)) * closeadj
    sl = base.diff(periods=63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of debt growth ratio 63v252
def f24dt_f24_debt_trajectory_debtgrowthratio_63v252_jerk_v040_signal(debt, closeadj):
    a = _f24_debt_growth(debt, 63)
    b = _f24_debt_growth(debt, 252).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of debt growth ratio 21v63
def f24dt_f24_debt_trajectory_debtgrowthratio_21v63_jerk_v041_signal(debt, closeadj):
    a = _f24_debt_growth(debt, 21)
    b = _f24_debt_growth(debt, 63).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of debt growth product 63x252
def f24dt_f24_debt_trajectory_debtgrowthprod_63x252_jerk_v042_signal(debt, closeadj):
    base = _f24_debt_growth(debt, 63) * _f24_debt_growth(debt, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d debt growth × leverage traj
def f24dt_f24_debt_trajectory_debtgrowthxlev_21d_jerk_v043_signal(debt, equity, closeadj):
    base = _f24_debt_growth(debt, 21) * _f24_leverage_traj(debt, equity, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt growth × leverage traj
def f24dt_f24_debt_trajectory_debtgrowthxlev_252d_jerk_v044_signal(debt, equity, closeadj):
    base = _f24_debt_growth(debt, 252) * _f24_leverage_traj(debt, equity, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d debt growth × ebitda
def f24dt_f24_debt_trajectory_debtgrowthxebitda_21d_jerk_v045_signal(debt, ebitda, closeadj):
    base = _f24_debt_growth(debt, 21) * ebitda
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d debt growth × ebitda
def f24dt_f24_debt_trajectory_debtgrowthxebitda_63d_jerk_v046_signal(debt, ebitda, closeadj):
    base = _f24_debt_growth(debt, 63) * ebitda
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt growth × ebitda
def f24dt_f24_debt_trajectory_debtgrowthxebitda_252d_jerk_v047_signal(debt, ebitda, closeadj):
    base = _f24_debt_growth(debt, 252) * ebitda
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d debt traj × netinc
def f24dt_f24_debt_trajectory_debttrajxnetinc_63d_jerk_v048_signal(debt, netinc, closeadj):
    base = _f24_debt_traj(debt, 63) * netinc
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt traj × netinc
def f24dt_f24_debt_trajectory_debttrajxnetinc_252d_jerk_v049_signal(debt, netinc, closeadj):
    base = _f24_debt_traj(debt, 252) * netinc
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d max debt growth × close
def f24dt_f24_debt_trajectory_debtgrowthmax_63d_jerk_v050_signal(debt, closeadj):
    base = _f24_debt_growth(debt, 21).rolling(63, min_periods=21).max() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d max debt growth × close
def f24dt_f24_debt_trajectory_debtgrowthmax_252d_jerk_v051_signal(debt, closeadj):
    base = _f24_debt_growth(debt, 63).rolling(252, min_periods=63).max() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d sum debt growth × close
def f24dt_f24_debt_trajectory_debtgrowthsum_63d_jerk_v052_signal(debt, closeadj):
    base = _f24_debt_growth(debt, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d sum debt growth × close
def f24dt_f24_debt_trajectory_debtgrowthsum_252d_jerk_v053_signal(debt, closeadj):
    base = _f24_debt_growth(debt, 63).rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d sum debt traj × close
def f24dt_f24_debt_trajectory_debttrajsum_252d_jerk_v054_signal(debt, closeadj):
    base = _f24_debt_traj(debt, 21).rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d debt growth × capex
def f24dt_f24_debt_trajectory_debtgrowthxcapex_63d_jerk_v055_signal(debt, capex, closeadj):
    base = _f24_debt_growth(debt, 63) * capex.abs()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt growth × capex
def f24dt_f24_debt_trajectory_debtgrowthxcapex_252d_jerk_v056_signal(debt, capex, closeadj):
    base = _f24_debt_growth(debt, 252) * capex.abs()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d debt traj × capex
def f24dt_f24_debt_trajectory_debttrajxcapex_63d_jerk_v057_signal(debt, capex, closeadj):
    base = _f24_debt_traj(debt, 63) * capex.abs()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d debt growth × ncff
def f24dt_f24_debt_trajectory_debtgrowthxncff_21d_jerk_v058_signal(debt, ncff, closeadj):
    base = _f24_debt_growth(debt, 21) * ncff.abs()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt growth × ncff
def f24dt_f24_debt_trajectory_debtgrowthxncff_252d_jerk_v059_signal(debt, ncff, closeadj):
    base = _f24_debt_growth(debt, 252) * ncff.abs()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d debt growth EMA × close
def f24dt_f24_debt_trajectory_debtgrowthema_63d_jerk_v060_signal(debt, closeadj):
    g = _f24_debt_growth(debt, 63)
    base = g.ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt growth EMA × close
def f24dt_f24_debt_trajectory_debtgrowthema_252d_jerk_v061_signal(debt, closeadj):
    g = _f24_debt_growth(debt, 252)
    base = g.ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d debt traj EMA × close
def f24dt_f24_debt_trajectory_debttrajema_63d_jerk_v062_signal(debt, closeadj):
    g = _f24_debt_traj(debt, 63)
    base = g.ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt traj EMA × close
def f24dt_f24_debt_trajectory_debttrajema_252d_jerk_v063_signal(debt, closeadj):
    g = _f24_debt_traj(debt, 252)
    base = g.ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d leverage traj × ebitda
def f24dt_f24_debt_trajectory_levtrajxebitda_21d_jerk_v064_signal(debt, equity, ebitda, closeadj):
    base = _f24_leverage_traj(debt, equity, 21) * ebitda
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d leverage traj × ebitda
def f24dt_f24_debt_trajectory_levtrajxebitda_63d_jerk_v065_signal(debt, equity, ebitda, closeadj):
    base = _f24_leverage_traj(debt, equity, 63) * ebitda
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d leverage traj × revenue
def f24dt_f24_debt_trajectory_levtrajxrev_252d_jerk_v066_signal(debt, equity, revenue, closeadj):
    base = _f24_leverage_traj(debt, equity, 252) * revenue
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d leverage traj zscore
def f24dt_f24_debt_trajectory_levtrajz_252d_jerk_v067_signal(debt, equity, closeadj):
    base = _z(_f24_leverage_traj(debt, equity, 63), 252)
    sl = base.diff(periods=21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d leverage traj zscore
def f24dt_f24_debt_trajectory_levtrajz_504d_jerk_v068_signal(debt, equity, closeadj):
    base = _z(_f24_leverage_traj(debt, equity, 252), 504)
    sl = base.diff(periods=63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 5d debt growth × close
def f24dt_f24_debt_trajectory_debtgrowth_5d_jerk_v069_signal(debt, closeadj):
    base = _f24_debt_growth(debt, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 10d debt growth × close
def f24dt_f24_debt_trajectory_debtgrowth_10d_jerk_v070_signal(debt, closeadj):
    base = _f24_debt_growth(debt, 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 42d debt growth × close
def f24dt_f24_debt_trajectory_debtgrowth_42d_jerk_v071_signal(debt, closeadj):
    base = _f24_debt_growth(debt, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 189d debt growth × close
def f24dt_f24_debt_trajectory_debtgrowth_189d_jerk_v072_signal(debt, closeadj):
    base = _f24_debt_growth(debt, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 378d debt growth × close
def f24dt_f24_debt_trajectory_debtgrowth_378d_jerk_v073_signal(debt, closeadj):
    base = _f24_debt_growth(debt, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt growth area × close
def f24dt_f24_debt_trajectory_debtgrowtharea_252d_jerk_v074_signal(debt, closeadj):
    g = _f24_debt_growth(debt, 63).abs()
    base = g.rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d debt growth area × close
def f24dt_f24_debt_trajectory_debtgrowtharea_504d_jerk_v075_signal(debt, closeadj):
    g = _f24_debt_growth(debt, 252).abs()
    base = g.rolling(504, min_periods=126).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt growth × mcap
def f24dt_f24_debt_trajectory_debtgrowthxmcap_252d_jerk_v076_signal(debt, closeadj, sharesbas):
    base = _f24_debt_growth(debt, 252) * (closeadj * sharesbas)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d debt growth × mcap
def f24dt_f24_debt_trajectory_debtgrowthxmcap_63d_jerk_v077_signal(debt, closeadj, sharesbas):
    base = _f24_debt_growth(debt, 63) * (closeadj * sharesbas)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d debt growth × equity
def f24dt_f24_debt_trajectory_debtgrowthxequity_21d_jerk_v078_signal(debt, equity, closeadj):
    base = _f24_debt_growth(debt, 21) * equity
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt growth × equity
def f24dt_f24_debt_trajectory_debtgrowthxequity_252d_jerk_v079_signal(debt, equity, closeadj):
    base = _f24_debt_growth(debt, 252) * equity
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt growth × assets
def f24dt_f24_debt_trajectory_debtgrowthxassets_252d_jerk_v080_signal(debt, assets, closeadj):
    base = _f24_debt_growth(debt, 252) * assets
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt growth × gp
def f24dt_f24_debt_trajectory_debtgrowthxgp_252d_jerk_v081_signal(debt, gp, closeadj):
    base = _f24_debt_growth(debt, 252) * gp
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d debt growth × gp
def f24dt_f24_debt_trajectory_debtgrowthxgp_63d_jerk_v082_signal(debt, gp, closeadj):
    base = _f24_debt_growth(debt, 63) * gp
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt growth × opinc
def f24dt_f24_debt_trajectory_debtgrowthxopinc_252d_jerk_v083_signal(debt, opinc, closeadj):
    base = _f24_debt_growth(debt, 252) * opinc
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d debt growth × opinc
def f24dt_f24_debt_trajectory_debtgrowthxopinc_63d_jerk_v084_signal(debt, opinc, closeadj):
    base = _f24_debt_growth(debt, 63) * opinc
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt growth × ncfo
def f24dt_f24_debt_trajectory_debtgrowthxncfo_252d_jerk_v085_signal(debt, ncfo, closeadj):
    base = _f24_debt_growth(debt, 252) * ncfo
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt growth × fcf
def f24dt_f24_debt_trajectory_debtgrowthxfcf_252d_jerk_v086_signal(debt, fcf, closeadj):
    base = _f24_debt_growth(debt, 252) * fcf
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt growth × eps × close
def f24dt_f24_debt_trajectory_debtgrowthxeps_252d_jerk_v087_signal(debt, eps, closeadj):
    base = _f24_debt_growth(debt, 252) * eps * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d debt traj × eps × close
def f24dt_f24_debt_trajectory_debttrajxeps_63d_jerk_v088_signal(debt, eps, closeadj):
    base = _f24_debt_traj(debt, 63) * eps * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt growth × wc
def f24dt_f24_debt_trajectory_debtgrowthxwc_252d_jerk_v089_signal(debt, workingcapital, closeadj):
    base = _f24_debt_growth(debt, 252) * workingcapital
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d debt traj × wc
def f24dt_f24_debt_trajectory_debttrajxwc_63d_jerk_v090_signal(debt, workingcapital, closeadj):
    base = _f24_debt_traj(debt, 63) * workingcapital
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d debt growth × cr × close
def f24dt_f24_debt_trajectory_debtgrowthxcr_21d_jerk_v091_signal(debt, currentratio, closeadj):
    base = _f24_debt_growth(debt, 21) * currentratio * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt growth × cr × close
def f24dt_f24_debt_trajectory_debtgrowthxcr_252d_jerk_v092_signal(debt, currentratio, closeadj):
    base = _f24_debt_growth(debt, 252) * currentratio * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt traj × cr × close
def f24dt_f24_debt_trajectory_debttrajxcr_252d_jerk_v093_signal(debt, currentratio, closeadj):
    base = _f24_debt_traj(debt, 252) * currentratio * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d debt growth × liab
def f24dt_f24_debt_trajectory_debtgrowthxliab_63d_jerk_v094_signal(debt, liabilities, closeadj):
    base = _f24_debt_growth(debt, 63) * liabilities
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt growth × liab
def f24dt_f24_debt_trajectory_debtgrowthxliab_252d_jerk_v095_signal(debt, liabilities, closeadj):
    base = _f24_debt_growth(debt, 252) * liabilities
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d debt traj × retearn
def f24dt_f24_debt_trajectory_debttrajxre_63d_jerk_v096_signal(debt, retearn, closeadj):
    base = _f24_debt_traj(debt, 63) * retearn
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt growth × retearn
def f24dt_f24_debt_trajectory_debtgrowthxre_252d_jerk_v097_signal(debt, retearn, closeadj):
    base = _f24_debt_growth(debt, 252) * retearn
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d debt traj × intexp
def f24dt_f24_debt_trajectory_debttrajxintexp_63d_jerk_v098_signal(debt, intexp, closeadj):
    base = _f24_debt_traj(debt, 63) * intexp
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt growth × intexp
def f24dt_f24_debt_trajectory_debtgrowthxintexp_252d_jerk_v099_signal(debt, intexp, closeadj):
    base = _f24_debt_growth(debt, 252) * intexp
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt growth × tax
def f24dt_f24_debt_trajectory_debtgrowthxtax_252d_jerk_v100_signal(debt, taxexp, closeadj):
    base = _f24_debt_growth(debt, 252) * taxexp
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d debt traj squared × close
def f24dt_f24_debt_trajectory_debttrajsq_21d_jerk_v101_signal(debt, closeadj):
    g = _f24_debt_traj(debt, 21)
    base = g * g.abs() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt traj squared × close
def f24dt_f24_debt_trajectory_debttrajsq_252d_jerk_v102_signal(debt, closeadj):
    g = _f24_debt_traj(debt, 252)
    base = g * g.abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d debt traj area × close
def f24dt_f24_debt_trajectory_debttrajarea_63d_jerk_v103_signal(debt, closeadj):
    g = _f24_debt_traj(debt, 21).abs()
    base = g.rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt traj area × close
def f24dt_f24_debt_trajectory_debttrajarea_252d_jerk_v104_signal(debt, closeadj):
    g = _f24_debt_traj(debt, 63).abs()
    base = g.rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d debt traj area × close
def f24dt_f24_debt_trajectory_debttrajarea_504d_jerk_v105_signal(debt, closeadj):
    g = _f24_debt_traj(debt, 252).abs()
    base = g.rolling(504, min_periods=126).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt - ncfo growth × close
def f24dt_f24_debt_trajectory_debtminusncfo_252d_jerk_v106_signal(debt, ncfo, closeadj):
    a = _f24_debt_growth(debt, 252)
    b = ncfo.diff(periods=252) / ncfo.abs().rolling(252, min_periods=63).mean().replace(0, np.nan)
    base = (a - b) * closeadj
    sl = base.diff(periods=63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d debt - fcf growth × close
def f24dt_f24_debt_trajectory_debtminusfcf_63d_jerk_v107_signal(debt, fcf, closeadj):
    a = _f24_debt_growth(debt, 63)
    b = fcf.diff(periods=63) / fcf.abs().rolling(63, min_periods=21).mean().replace(0, np.nan)
    base = (a - b) * closeadj
    sl = base.diff(periods=21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt + leverage traj × close
def f24dt_f24_debt_trajectory_debtpluslev_252d_jerk_v108_signal(debt, equity, closeadj):
    base = (_f24_debt_growth(debt, 252) + _f24_leverage_traj(debt, equity, 252)) * closeadj
    sl = base.diff(periods=63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of expanding worst debt growth × close
def f24dt_f24_debt_trajectory_debtgrowthworst_504d_jerk_v109_signal(debt, closeadj):
    g = _f24_debt_growth(debt, 252)
    base = g.expanding(min_periods=63).max() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of expanding best debt growth × close
def f24dt_f24_debt_trajectory_debtgrowthbest_504d_jerk_v110_signal(debt, closeadj):
    g = _f24_debt_growth(debt, 252)
    base = g.expanding(min_periods=63).min() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d max debt traj × close
def f24dt_f24_debt_trajectory_debttrajmax_63d_jerk_v111_signal(debt, closeadj):
    base = _f24_debt_traj(debt, 21).rolling(63, min_periods=21).max() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d max debt traj × close
def f24dt_f24_debt_trajectory_debttrajmax_252d_jerk_v112_signal(debt, closeadj):
    base = _f24_debt_traj(debt, 63).rolling(252, min_periods=63).max() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d min debt traj × close
def f24dt_f24_debt_trajectory_debttrajmin_63d_jerk_v113_signal(debt, closeadj):
    base = _f24_debt_traj(debt, 21).rolling(63, min_periods=21).min() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d min debt traj × close
def f24dt_f24_debt_trajectory_debttrajmin_252d_jerk_v114_signal(debt, closeadj):
    base = _f24_debt_traj(debt, 63).rolling(252, min_periods=63).min() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d debt growth EMA × ebitda
def f24dt_f24_debt_trajectory_debtgrowthemaebitda_21d_jerk_v115_signal(debt, ebitda, closeadj):
    g = _f24_debt_growth(debt, 21)
    base = g.ewm(span=21, adjust=False).mean() * ebitda
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt growth EMA × ebitda
def f24dt_f24_debt_trajectory_debtgrowthemaebitda_252d_jerk_v116_signal(debt, ebitda, closeadj):
    g = _f24_debt_growth(debt, 252)
    base = g.ewm(span=252, adjust=False).mean() * ebitda
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt growth area × mcap
def f24dt_f24_debt_trajectory_debtgrowthareaxmcap_252d_jerk_v117_signal(debt, closeadj, sharesbas):
    g = _f24_debt_growth(debt, 63).abs()
    base = g.rolling(252, min_periods=63).sum() * (closeadj * sharesbas)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d debt traj anomaly × close
def f24dt_f24_debt_trajectory_debttrajanom_63d_jerk_v118_signal(debt, closeadj):
    base = (_f24_debt_traj(debt, 63) - _mean(_f24_debt_traj(debt, 252), 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt traj anomaly × close
def f24dt_f24_debt_trajectory_debttrajanom_252d_jerk_v119_signal(debt, closeadj):
    base = (_f24_debt_traj(debt, 252) - _mean(_f24_debt_traj(debt, 504), 504)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d debt growth anomaly × close
def f24dt_f24_debt_trajectory_debtgrowthanom_63d_jerk_v120_signal(debt, closeadj):
    base = (_f24_debt_growth(debt, 63) - _mean(_f24_debt_growth(debt, 252), 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt growth anomaly × close
def f24dt_f24_debt_trajectory_debtgrowthanom_252d_jerk_v121_signal(debt, closeadj):
    base = (_f24_debt_growth(debt, 252) - _mean(_f24_debt_growth(debt, 504), 504)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d debt growth × rev × close
def f24dt_f24_debt_trajectory_debtgrowthxrevxprice_21d_jerk_v122_signal(debt, revenue, closeadj):
    base = _f24_debt_growth(debt, 21) * revenue * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt growth × rev × close
def f24dt_f24_debt_trajectory_debtgrowthxrevxprice_252d_jerk_v123_signal(debt, revenue, closeadj):
    base = _f24_debt_growth(debt, 252) * revenue * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d leverage traj × mcap
def f24dt_f24_debt_trajectory_levtrajxmcap_252d_jerk_v124_signal(debt, equity, closeadj, sharesbas):
    base = _f24_leverage_traj(debt, equity, 252) * (closeadj * sharesbas)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d leverage traj × mcap
def f24dt_f24_debt_trajectory_levtrajxmcap_63d_jerk_v125_signal(debt, equity, closeadj, sharesbas):
    base = _f24_leverage_traj(debt, equity, 63) * (closeadj * sharesbas)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d debt growth × debt level × close
def f24dt_f24_debt_trajectory_debtgrowthxdebtlvl_21d_jerk_v126_signal(debt, closeadj):
    base = _f24_debt_growth(debt, 21) * debt * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt growth × debt level × close
def f24dt_f24_debt_trajectory_debtgrowthxdebtlvl_252d_jerk_v127_signal(debt, closeadj):
    base = _f24_debt_growth(debt, 252) * debt * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt traj × ebitda × close
def f24dt_f24_debt_trajectory_debttrajxebitdaprice_252d_jerk_v128_signal(debt, ebitda, closeadj):
    base = _f24_debt_traj(debt, 252) * ebitda * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt growth × ebitda × close
def f24dt_f24_debt_trajectory_debtgrowthxebitdaprice_252d_jerk_v129_signal(debt, ebitda, closeadj):
    base = _f24_debt_growth(debt, 252) * ebitda * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt growth × (ebitda - capex)
def f24dt_f24_debt_trajectory_debtgrowthxebitdacapex_252d_jerk_v130_signal(debt, ebitda, capex, closeadj):
    base = _f24_debt_growth(debt, 252) * (ebitda - capex.abs()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt traj × (assets - liab)
def f24dt_f24_debt_trajectory_debttrajxnet_252d_jerk_v131_signal(debt, assets, liabilities, closeadj):
    base = _f24_debt_traj(debt, 252) * (assets - liabilities)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d debt growth EMA × close
def f24dt_f24_debt_trajectory_debtgrowthema_21d_jerk_v132_signal(debt, closeadj):
    g = _f24_debt_growth(debt, 21)
    base = g.ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d debt traj EMA × close
def f24dt_f24_debt_trajectory_debttrajema_21d_jerk_v133_signal(debt, closeadj):
    g = _f24_debt_traj(debt, 21)
    base = g.ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d debt growth rank × close
def f24dt_f24_debt_trajectory_debtgrowthrank_252d_jerk_v134_signal(debt, closeadj):
    g = _f24_debt_growth(debt, 21)
    base = g.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt traj rank × close
def f24dt_f24_debt_trajectory_debttrajrank_252d_jerk_v135_signal(debt, closeadj):
    g = _f24_debt_traj(debt, 63)
    base = g.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d debt paydown count × close
def f24dt_f24_debt_trajectory_debtpaydowncount_252d_jerk_v136_signal(debt, closeadj):
    flag = (_f24_debt_growth(debt, 63) < 0).astype(float)
    base = flag.rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d debt spike count × close
def f24dt_f24_debt_trajectory_debtspikecount_504d_jerk_v137_signal(debt, closeadj):
    flag = (_f24_debt_growth(debt, 63) > 0.05).astype(float)
    base = flag.rolling(504, min_periods=126).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d leverage traj contr count × close
def f24dt_f24_debt_trajectory_levtrajcontrcount_252d_jerk_v138_signal(debt, equity, closeadj):
    flag = (_f24_leverage_traj(debt, equity, 63) < -0.02).astype(float)
    base = flag.rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt growth × vol × close
def f24dt_f24_debt_trajectory_debtgrowthxvol_252d_jerk_v139_signal(debt, closeadj):
    g = _f24_debt_growth(debt, 252)
    sd = _std(_f24_debt_growth(debt, 63), 252)
    base = g * sd * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d debt traj × vol × close
def f24dt_f24_debt_trajectory_debttrajxvol_63d_jerk_v140_signal(debt, closeadj):
    g = _f24_debt_traj(debt, 63)
    sd = _std(_f24_debt_traj(debt, 21), 63)
    base = g * sd * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d composite score × close
def f24dt_f24_debt_trajectory_compositescore_252d_jerk_v141_signal(debt, equity, closeadj):
    a = _f24_debt_growth(debt, 252)
    b = _f24_debt_traj(debt, 252)
    c = _f24_leverage_traj(debt, equity, 252)
    base = (a + b + c) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d debt growth × sales/price
def f24dt_f24_debt_trajectory_debtgrowthxsales_63d_jerk_v142_signal(debt, revenue, closeadj):
    base = _f24_debt_growth(debt, 63) * (revenue / closeadj.replace(0, np.nan))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt growth × ni × close
def f24dt_f24_debt_trajectory_debtgrowthxni_252d_jerk_v143_signal(debt, netinc, closeadj):
    base = _f24_debt_growth(debt, 252) * netinc * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d debt traj × ni × close
def f24dt_f24_debt_trajectory_debttrajxnini_21d_jerk_v144_signal(debt, netinc, closeadj):
    base = _f24_debt_traj(debt, 21) * netinc * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of expanding mean debt growth × close
def f24dt_f24_debt_trajectory_debtgrowthexp_252d_jerk_v145_signal(debt, closeadj):
    g = _f24_debt_growth(debt, 252)
    base = g.expanding(min_periods=63).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of expanding mean debt traj × close
def f24dt_f24_debt_trajectory_debttrajexp_252d_jerk_v146_signal(debt, closeadj):
    g = _f24_debt_traj(debt, 252)
    base = g.expanding(min_periods=63).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt growth × (assets - debt)
def f24dt_f24_debt_trajectory_debtgrowthxnet_252d_jerk_v147_signal(debt, assets, closeadj):
    base = _f24_debt_growth(debt, 252) * (assets - debt)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d debt traj × (rev - capex)
def f24dt_f24_debt_trajectory_debttrajxrevcapex_63d_jerk_v148_signal(debt, revenue, capex, closeadj):
    base = _f24_debt_traj(debt, 63) * (revenue - capex.abs())
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d debt growth × (gp - opinc) × close
def f24dt_f24_debt_trajectory_debtgrowthxgpopgap_252d_jerk_v149_signal(debt, gp, opinc, closeadj):
    base = _f24_debt_growth(debt, 252) * (gp - opinc) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d composite trajectory
def f24dt_f24_debt_trajectory_compositetraj_252d_jerk_v150_signal(debt, equity, revenue, closeadj):
    base = (_f24_debt_growth(debt, 252) + _f24_leverage_traj(debt, equity, 252)) * revenue * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f24dt_f24_debt_trajectory_debtgrowth_21d_jerk_v001_signal,
    f24dt_f24_debt_trajectory_debtgrowth_21d_jerk_v002_signal,
    f24dt_f24_debt_trajectory_debtgrowth_63d_jerk_v003_signal,
    f24dt_f24_debt_trajectory_debtgrowth_63d_jerk_v004_signal,
    f24dt_f24_debt_trajectory_debtgrowth_63d_jerk_v005_signal,
    f24dt_f24_debt_trajectory_debtgrowth_126d_jerk_v006_signal,
    f24dt_f24_debt_trajectory_debtgrowth_126d_jerk_v007_signal,
    f24dt_f24_debt_trajectory_debtgrowth_252d_jerk_v008_signal,
    f24dt_f24_debt_trajectory_debtgrowth_252d_jerk_v009_signal,
    f24dt_f24_debt_trajectory_debtgrowth_504d_jerk_v010_signal,
    f24dt_f24_debt_trajectory_debtgrowth_504d_jerk_v011_signal,
    f24dt_f24_debt_trajectory_debttraj_21d_jerk_v012_signal,
    f24dt_f24_debt_trajectory_debttraj_63d_jerk_v013_signal,
    f24dt_f24_debt_trajectory_debttraj_126d_jerk_v014_signal,
    f24dt_f24_debt_trajectory_debttraj_252d_jerk_v015_signal,
    f24dt_f24_debt_trajectory_debttraj_504d_jerk_v016_signal,
    f24dt_f24_debt_trajectory_levtraj_21d_jerk_v017_signal,
    f24dt_f24_debt_trajectory_levtraj_63d_jerk_v018_signal,
    f24dt_f24_debt_trajectory_levtraj_252d_jerk_v019_signal,
    f24dt_f24_debt_trajectory_debtgrowthmean_63d_jerk_v020_signal,
    f24dt_f24_debt_trajectory_debtgrowthmean_252d_jerk_v021_signal,
    f24dt_f24_debt_trajectory_debtgrowthstd_63d_jerk_v022_signal,
    f24dt_f24_debt_trajectory_debtgrowthstd_252d_jerk_v023_signal,
    f24dt_f24_debt_trajectory_debtgrowthz_252d_jerk_v024_signal,
    f24dt_f24_debt_trajectory_debtgrowthz_504d_jerk_v025_signal,
    f24dt_f24_debt_trajectory_debttrajz_252d_jerk_v026_signal,
    f24dt_f24_debt_trajectory_debttrajz_504d_jerk_v027_signal,
    f24dt_f24_debt_trajectory_debtgrowthhighcount_252d_jerk_v028_signal,
    f24dt_f24_debt_trajectory_debtgrowthlowcount_504d_jerk_v029_signal,
    f24dt_f24_debt_trajectory_levtrajexpcount_252d_jerk_v030_signal,
    f24dt_f24_debt_trajectory_debtgrowthsq_21d_jerk_v031_signal,
    f24dt_f24_debt_trajectory_debtgrowthsq_63d_jerk_v032_signal,
    f24dt_f24_debt_trajectory_debtgrowthsq_252d_jerk_v033_signal,
    f24dt_f24_debt_trajectory_debttrajxrev_21d_jerk_v034_signal,
    f24dt_f24_debt_trajectory_debttrajxrev_63d_jerk_v035_signal,
    f24dt_f24_debt_trajectory_debtgrowthxrev_252d_jerk_v036_signal,
    f24dt_f24_debt_trajectory_debtgrowthdiff_21m63_jerk_v037_signal,
    f24dt_f24_debt_trajectory_debtgrowthdiff_63m252_jerk_v038_signal,
    f24dt_f24_debt_trajectory_debtgrowthdiff_252m504_jerk_v039_signal,
    f24dt_f24_debt_trajectory_debtgrowthratio_63v252_jerk_v040_signal,
    f24dt_f24_debt_trajectory_debtgrowthratio_21v63_jerk_v041_signal,
    f24dt_f24_debt_trajectory_debtgrowthprod_63x252_jerk_v042_signal,
    f24dt_f24_debt_trajectory_debtgrowthxlev_21d_jerk_v043_signal,
    f24dt_f24_debt_trajectory_debtgrowthxlev_252d_jerk_v044_signal,
    f24dt_f24_debt_trajectory_debtgrowthxebitda_21d_jerk_v045_signal,
    f24dt_f24_debt_trajectory_debtgrowthxebitda_63d_jerk_v046_signal,
    f24dt_f24_debt_trajectory_debtgrowthxebitda_252d_jerk_v047_signal,
    f24dt_f24_debt_trajectory_debttrajxnetinc_63d_jerk_v048_signal,
    f24dt_f24_debt_trajectory_debttrajxnetinc_252d_jerk_v049_signal,
    f24dt_f24_debt_trajectory_debtgrowthmax_63d_jerk_v050_signal,
    f24dt_f24_debt_trajectory_debtgrowthmax_252d_jerk_v051_signal,
    f24dt_f24_debt_trajectory_debtgrowthsum_63d_jerk_v052_signal,
    f24dt_f24_debt_trajectory_debtgrowthsum_252d_jerk_v053_signal,
    f24dt_f24_debt_trajectory_debttrajsum_252d_jerk_v054_signal,
    f24dt_f24_debt_trajectory_debtgrowthxcapex_63d_jerk_v055_signal,
    f24dt_f24_debt_trajectory_debtgrowthxcapex_252d_jerk_v056_signal,
    f24dt_f24_debt_trajectory_debttrajxcapex_63d_jerk_v057_signal,
    f24dt_f24_debt_trajectory_debtgrowthxncff_21d_jerk_v058_signal,
    f24dt_f24_debt_trajectory_debtgrowthxncff_252d_jerk_v059_signal,
    f24dt_f24_debt_trajectory_debtgrowthema_63d_jerk_v060_signal,
    f24dt_f24_debt_trajectory_debtgrowthema_252d_jerk_v061_signal,
    f24dt_f24_debt_trajectory_debttrajema_63d_jerk_v062_signal,
    f24dt_f24_debt_trajectory_debttrajema_252d_jerk_v063_signal,
    f24dt_f24_debt_trajectory_levtrajxebitda_21d_jerk_v064_signal,
    f24dt_f24_debt_trajectory_levtrajxebitda_63d_jerk_v065_signal,
    f24dt_f24_debt_trajectory_levtrajxrev_252d_jerk_v066_signal,
    f24dt_f24_debt_trajectory_levtrajz_252d_jerk_v067_signal,
    f24dt_f24_debt_trajectory_levtrajz_504d_jerk_v068_signal,
    f24dt_f24_debt_trajectory_debtgrowth_5d_jerk_v069_signal,
    f24dt_f24_debt_trajectory_debtgrowth_10d_jerk_v070_signal,
    f24dt_f24_debt_trajectory_debtgrowth_42d_jerk_v071_signal,
    f24dt_f24_debt_trajectory_debtgrowth_189d_jerk_v072_signal,
    f24dt_f24_debt_trajectory_debtgrowth_378d_jerk_v073_signal,
    f24dt_f24_debt_trajectory_debtgrowtharea_252d_jerk_v074_signal,
    f24dt_f24_debt_trajectory_debtgrowtharea_504d_jerk_v075_signal,
    f24dt_f24_debt_trajectory_debtgrowthxmcap_252d_jerk_v076_signal,
    f24dt_f24_debt_trajectory_debtgrowthxmcap_63d_jerk_v077_signal,
    f24dt_f24_debt_trajectory_debtgrowthxequity_21d_jerk_v078_signal,
    f24dt_f24_debt_trajectory_debtgrowthxequity_252d_jerk_v079_signal,
    f24dt_f24_debt_trajectory_debtgrowthxassets_252d_jerk_v080_signal,
    f24dt_f24_debt_trajectory_debtgrowthxgp_252d_jerk_v081_signal,
    f24dt_f24_debt_trajectory_debtgrowthxgp_63d_jerk_v082_signal,
    f24dt_f24_debt_trajectory_debtgrowthxopinc_252d_jerk_v083_signal,
    f24dt_f24_debt_trajectory_debtgrowthxopinc_63d_jerk_v084_signal,
    f24dt_f24_debt_trajectory_debtgrowthxncfo_252d_jerk_v085_signal,
    f24dt_f24_debt_trajectory_debtgrowthxfcf_252d_jerk_v086_signal,
    f24dt_f24_debt_trajectory_debtgrowthxeps_252d_jerk_v087_signal,
    f24dt_f24_debt_trajectory_debttrajxeps_63d_jerk_v088_signal,
    f24dt_f24_debt_trajectory_debtgrowthxwc_252d_jerk_v089_signal,
    f24dt_f24_debt_trajectory_debttrajxwc_63d_jerk_v090_signal,
    f24dt_f24_debt_trajectory_debtgrowthxcr_21d_jerk_v091_signal,
    f24dt_f24_debt_trajectory_debtgrowthxcr_252d_jerk_v092_signal,
    f24dt_f24_debt_trajectory_debttrajxcr_252d_jerk_v093_signal,
    f24dt_f24_debt_trajectory_debtgrowthxliab_63d_jerk_v094_signal,
    f24dt_f24_debt_trajectory_debtgrowthxliab_252d_jerk_v095_signal,
    f24dt_f24_debt_trajectory_debttrajxre_63d_jerk_v096_signal,
    f24dt_f24_debt_trajectory_debtgrowthxre_252d_jerk_v097_signal,
    f24dt_f24_debt_trajectory_debttrajxintexp_63d_jerk_v098_signal,
    f24dt_f24_debt_trajectory_debtgrowthxintexp_252d_jerk_v099_signal,
    f24dt_f24_debt_trajectory_debtgrowthxtax_252d_jerk_v100_signal,
    f24dt_f24_debt_trajectory_debttrajsq_21d_jerk_v101_signal,
    f24dt_f24_debt_trajectory_debttrajsq_252d_jerk_v102_signal,
    f24dt_f24_debt_trajectory_debttrajarea_63d_jerk_v103_signal,
    f24dt_f24_debt_trajectory_debttrajarea_252d_jerk_v104_signal,
    f24dt_f24_debt_trajectory_debttrajarea_504d_jerk_v105_signal,
    f24dt_f24_debt_trajectory_debtminusncfo_252d_jerk_v106_signal,
    f24dt_f24_debt_trajectory_debtminusfcf_63d_jerk_v107_signal,
    f24dt_f24_debt_trajectory_debtpluslev_252d_jerk_v108_signal,
    f24dt_f24_debt_trajectory_debtgrowthworst_504d_jerk_v109_signal,
    f24dt_f24_debt_trajectory_debtgrowthbest_504d_jerk_v110_signal,
    f24dt_f24_debt_trajectory_debttrajmax_63d_jerk_v111_signal,
    f24dt_f24_debt_trajectory_debttrajmax_252d_jerk_v112_signal,
    f24dt_f24_debt_trajectory_debttrajmin_63d_jerk_v113_signal,
    f24dt_f24_debt_trajectory_debttrajmin_252d_jerk_v114_signal,
    f24dt_f24_debt_trajectory_debtgrowthemaebitda_21d_jerk_v115_signal,
    f24dt_f24_debt_trajectory_debtgrowthemaebitda_252d_jerk_v116_signal,
    f24dt_f24_debt_trajectory_debtgrowthareaxmcap_252d_jerk_v117_signal,
    f24dt_f24_debt_trajectory_debttrajanom_63d_jerk_v118_signal,
    f24dt_f24_debt_trajectory_debttrajanom_252d_jerk_v119_signal,
    f24dt_f24_debt_trajectory_debtgrowthanom_63d_jerk_v120_signal,
    f24dt_f24_debt_trajectory_debtgrowthanom_252d_jerk_v121_signal,
    f24dt_f24_debt_trajectory_debtgrowthxrevxprice_21d_jerk_v122_signal,
    f24dt_f24_debt_trajectory_debtgrowthxrevxprice_252d_jerk_v123_signal,
    f24dt_f24_debt_trajectory_levtrajxmcap_252d_jerk_v124_signal,
    f24dt_f24_debt_trajectory_levtrajxmcap_63d_jerk_v125_signal,
    f24dt_f24_debt_trajectory_debtgrowthxdebtlvl_21d_jerk_v126_signal,
    f24dt_f24_debt_trajectory_debtgrowthxdebtlvl_252d_jerk_v127_signal,
    f24dt_f24_debt_trajectory_debttrajxebitdaprice_252d_jerk_v128_signal,
    f24dt_f24_debt_trajectory_debtgrowthxebitdaprice_252d_jerk_v129_signal,
    f24dt_f24_debt_trajectory_debtgrowthxebitdacapex_252d_jerk_v130_signal,
    f24dt_f24_debt_trajectory_debttrajxnet_252d_jerk_v131_signal,
    f24dt_f24_debt_trajectory_debtgrowthema_21d_jerk_v132_signal,
    f24dt_f24_debt_trajectory_debttrajema_21d_jerk_v133_signal,
    f24dt_f24_debt_trajectory_debtgrowthrank_252d_jerk_v134_signal,
    f24dt_f24_debt_trajectory_debttrajrank_252d_jerk_v135_signal,
    f24dt_f24_debt_trajectory_debtpaydowncount_252d_jerk_v136_signal,
    f24dt_f24_debt_trajectory_debtspikecount_504d_jerk_v137_signal,
    f24dt_f24_debt_trajectory_levtrajcontrcount_252d_jerk_v138_signal,
    f24dt_f24_debt_trajectory_debtgrowthxvol_252d_jerk_v139_signal,
    f24dt_f24_debt_trajectory_debttrajxvol_63d_jerk_v140_signal,
    f24dt_f24_debt_trajectory_compositescore_252d_jerk_v141_signal,
    f24dt_f24_debt_trajectory_debtgrowthxsales_63d_jerk_v142_signal,
    f24dt_f24_debt_trajectory_debtgrowthxni_252d_jerk_v143_signal,
    f24dt_f24_debt_trajectory_debttrajxnini_21d_jerk_v144_signal,
    f24dt_f24_debt_trajectory_debtgrowthexp_252d_jerk_v145_signal,
    f24dt_f24_debt_trajectory_debttrajexp_252d_jerk_v146_signal,
    f24dt_f24_debt_trajectory_debtgrowthxnet_252d_jerk_v147_signal,
    f24dt_f24_debt_trajectory_debttrajxrevcapex_63d_jerk_v148_signal,
    f24dt_f24_debt_trajectory_debtgrowthxgpopgap_252d_jerk_v149_signal,
    f24dt_f24_debt_trajectory_compositetraj_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F24_DEBT_TRAJECTORY_REGISTRY_JERK = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    revenue = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="revenue")
    netinc = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="netinc")
    fcf = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcf")
    ncfo = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ncfo")
    ncff = pd.Series(-2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="ncff")
    equity = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.004, n))), name="equity")
    debt = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.005, n))), name="debt")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.003, n))), name="assets")
    ebitda = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.006, n))), name="ebitda")
    capex = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="capex")
    eps = pd.Series(1.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="eps")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.002, n))), name="sharesbas")
    opinc = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.007, n))), name="opinc")
    gp = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="gp")
    workingcapital = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.006, n))), name="workingcapital")
    currentratio = pd.Series(1.8 * np.exp(np.cumsum(np.random.normal(0.0, 0.003, n))), name="currentratio")
    intexp = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0001, 0.005, n))), name="intexp")
    retearn = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.004, n))), name="retearn")
    liabilities = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.004, n))), name="liabilities")
    taxexp = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="taxexp")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "ncff": ncff, "equity": equity, "debt": debt, "assets": assets,
        "ebitda": ebitda, "capex": capex, "eps": eps, "sharesbas": sharesbas,
        "opinc": opinc, "gp": gp, "workingcapital": workingcapital,
        "currentratio": currentratio, "intexp": intexp, "retearn": retearn,
        "liabilities": liabilities, "taxexp": taxexp,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f24_debt_traj", "_f24_debt_growth", "_f24_leverage_traj")
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
    print(f"OK f24_debt_trajectory_3rd_derivatives_001_150_claude: {n_features} features pass")
