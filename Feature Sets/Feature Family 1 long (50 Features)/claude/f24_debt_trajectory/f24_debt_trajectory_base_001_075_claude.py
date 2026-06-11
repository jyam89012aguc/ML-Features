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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f24_debt_traj(debt, w):
    base = debt.rolling(w, min_periods=max(1, w // 2)).mean()
    return base.diff(periods=w) / base.abs().shift(w).replace(0, np.nan)


def _f24_debt_growth(debt, w):
    return debt.diff(periods=w) / debt.abs().rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)


def _f24_leverage_traj(debt, equity, w):
    lev = debt / equity.replace(0, np.nan)
    return lev.diff(periods=w) / lev.abs().shift(w).replace(0, np.nan)


# 21d debt growth scaled by closeadj
def f24dt_f24_debt_trajectory_debtgrowth_21d_base_v001_signal(debt, closeadj):
    result = _f24_debt_growth(debt, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt growth scaled by closeadj
def f24dt_f24_debt_trajectory_debtgrowth_63d_base_v002_signal(debt, closeadj):
    result = _f24_debt_growth(debt, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d debt growth
def f24dt_f24_debt_trajectory_debtgrowth_126d_base_v003_signal(debt, closeadj):
    result = _f24_debt_growth(debt, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt growth
def f24dt_f24_debt_trajectory_debtgrowth_252d_base_v004_signal(debt, closeadj):
    result = _f24_debt_growth(debt, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d debt growth
def f24dt_f24_debt_trajectory_debtgrowth_504d_base_v005_signal(debt, closeadj):
    result = _f24_debt_growth(debt, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d debt trajectory smoothed
def f24dt_f24_debt_trajectory_debttraj_21d_base_v006_signal(debt, closeadj):
    result = _f24_debt_traj(debt, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt trajectory
def f24dt_f24_debt_trajectory_debttraj_63d_base_v007_signal(debt, closeadj):
    result = _f24_debt_traj(debt, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d debt trajectory
def f24dt_f24_debt_trajectory_debttraj_126d_base_v008_signal(debt, closeadj):
    result = _f24_debt_traj(debt, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt trajectory
def f24dt_f24_debt_trajectory_debttraj_252d_base_v009_signal(debt, closeadj):
    result = _f24_debt_traj(debt, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d debt trajectory
def f24dt_f24_debt_trajectory_debttraj_504d_base_v010_signal(debt, closeadj):
    result = _f24_debt_traj(debt, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d leverage trajectory (debt/equity)
def f24dt_f24_debt_trajectory_levtraj_21d_base_v011_signal(debt, equity, closeadj):
    result = _f24_leverage_traj(debt, equity, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d leverage trajectory
def f24dt_f24_debt_trajectory_levtraj_63d_base_v012_signal(debt, equity, closeadj):
    result = _f24_leverage_traj(debt, equity, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d leverage trajectory
def f24dt_f24_debt_trajectory_levtraj_252d_base_v013_signal(debt, equity, closeadj):
    result = _f24_leverage_traj(debt, equity, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d leverage trajectory
def f24dt_f24_debt_trajectory_levtraj_504d_base_v014_signal(debt, equity, closeadj):
    result = _f24_leverage_traj(debt, equity, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 63d mean of debt growth
def f24dt_f24_debt_trajectory_debtgrowthmean_63d_base_v015_signal(debt, closeadj):
    result = _mean(_f24_debt_growth(debt, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 252d mean of debt growth
def f24dt_f24_debt_trajectory_debtgrowthmean_252d_base_v016_signal(debt, closeadj):
    result = _mean(_f24_debt_growth(debt, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 63d std of debt growth
def f24dt_f24_debt_trajectory_debtgrowthstd_63d_base_v017_signal(debt, closeadj):
    result = _std(_f24_debt_growth(debt, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 252d std of debt growth
def f24dt_f24_debt_trajectory_debtgrowthstd_252d_base_v018_signal(debt, closeadj):
    result = _std(_f24_debt_growth(debt, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of debt growth
def f24dt_f24_debt_trajectory_debtgrowthz_252d_base_v019_signal(debt, closeadj):
    result = _z(_f24_debt_growth(debt, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of debt growth
def f24dt_f24_debt_trajectory_debtgrowthz_504d_base_v020_signal(debt, closeadj):
    result = _z(_f24_debt_growth(debt, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of debt trajectory
def f24dt_f24_debt_trajectory_debttrajz_252d_base_v021_signal(debt, closeadj):
    result = _z(_f24_debt_traj(debt, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of debt trajectory
def f24dt_f24_debt_trajectory_debttrajz_504d_base_v022_signal(debt, closeadj):
    result = _z(_f24_debt_traj(debt, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of high debt growth (>2%)
def f24dt_f24_debt_trajectory_debtgrowthhighcount_252d_base_v023_signal(debt, closeadj):
    flag = (_f24_debt_growth(debt, 63) > 0.02).astype(float)
    result = flag.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of debt deleveraging (<-2%)
def f24dt_f24_debt_trajectory_debtgrowthlowcount_504d_base_v024_signal(debt, closeadj):
    flag = (_f24_debt_growth(debt, 252) < -0.02).astype(float)
    result = flag.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of leverage expansion
def f24dt_f24_debt_trajectory_levtrajexpcount_252d_base_v025_signal(debt, equity, closeadj):
    flag = (_f24_leverage_traj(debt, equity, 63) > 0).astype(float)
    result = flag.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d debt growth squared × close
def f24dt_f24_debt_trajectory_debtgrowthsq_21d_base_v026_signal(debt, closeadj):
    g = _f24_debt_growth(debt, 21)
    result = g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt growth squared × close
def f24dt_f24_debt_trajectory_debtgrowthsq_63d_base_v027_signal(debt, closeadj):
    g = _f24_debt_growth(debt, 63)
    result = g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt growth squared × close
def f24dt_f24_debt_trajectory_debtgrowthsq_252d_base_v028_signal(debt, closeadj):
    g = _f24_debt_growth(debt, 252)
    result = g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d debt trajectory × revenue
def f24dt_f24_debt_trajectory_debttrajxrev_21d_base_v029_signal(debt, revenue, closeadj):
    result = _f24_debt_traj(debt, 21) * revenue
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt trajectory × revenue
def f24dt_f24_debt_trajectory_debttrajxrev_63d_base_v030_signal(debt, revenue, closeadj):
    result = _f24_debt_traj(debt, 63) * revenue
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt growth × revenue
def f24dt_f24_debt_trajectory_debtgrowthxrev_252d_base_v031_signal(debt, revenue, closeadj):
    result = _f24_debt_growth(debt, 252) * revenue
    return result.replace([np.inf, -np.inf], np.nan)


# debt growth diff (21m63) × close
def f24dt_f24_debt_trajectory_debtgrowthdiff_21m63_base_v032_signal(debt, closeadj):
    result = (_f24_debt_growth(debt, 21) - _f24_debt_growth(debt, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# debt growth diff (63m252) × close
def f24dt_f24_debt_trajectory_debtgrowthdiff_63m252_base_v033_signal(debt, closeadj):
    result = (_f24_debt_growth(debt, 63) - _f24_debt_growth(debt, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# debt growth diff (252m504) × close
def f24dt_f24_debt_trajectory_debtgrowthdiff_252m504_base_v034_signal(debt, closeadj):
    result = (_f24_debt_growth(debt, 252) - _f24_debt_growth(debt, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# debt growth ratio 63v252 × close
def f24dt_f24_debt_trajectory_debtgrowthratio_63v252_base_v035_signal(debt, closeadj):
    a = _f24_debt_growth(debt, 63)
    b = _f24_debt_growth(debt, 252).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# debt growth ratio 21v63 × close
def f24dt_f24_debt_trajectory_debtgrowthratio_21v63_base_v036_signal(debt, closeadj):
    a = _f24_debt_growth(debt, 21)
    b = _f24_debt_growth(debt, 63).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt growth × 252d debt growth (consistency)
def f24dt_f24_debt_trajectory_debtgrowthprod_63x252_base_v037_signal(debt, closeadj):
    result = _f24_debt_growth(debt, 63) * _f24_debt_growth(debt, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d debt growth × 21d leverage trajectory
def f24dt_f24_debt_trajectory_debtgrowthxlev_21d_base_v038_signal(debt, equity, closeadj):
    result = _f24_debt_growth(debt, 21) * _f24_leverage_traj(debt, equity, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt growth × 252d leverage trajectory
def f24dt_f24_debt_trajectory_debtgrowthxlev_252d_base_v039_signal(debt, equity, closeadj):
    result = _f24_debt_growth(debt, 252) * _f24_leverage_traj(debt, equity, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d debt growth × ebitda (debt service capacity context)
def f24dt_f24_debt_trajectory_debtgrowthxebitda_21d_base_v040_signal(debt, ebitda, closeadj):
    result = _f24_debt_growth(debt, 21) * ebitda
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt growth × ebitda
def f24dt_f24_debt_trajectory_debtgrowthxebitda_63d_base_v041_signal(debt, ebitda, closeadj):
    result = _f24_debt_growth(debt, 63) * ebitda
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt growth × ebitda
def f24dt_f24_debt_trajectory_debtgrowthxebitda_252d_base_v042_signal(debt, ebitda, closeadj):
    result = _f24_debt_growth(debt, 252) * ebitda
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt traj × netinc
def f24dt_f24_debt_trajectory_debttrajxnetinc_63d_base_v043_signal(debt, netinc, closeadj):
    result = _f24_debt_traj(debt, 63) * netinc
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt traj × netinc
def f24dt_f24_debt_trajectory_debttrajxnetinc_252d_base_v044_signal(debt, netinc, closeadj):
    result = _f24_debt_traj(debt, 252) * netinc
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 63d max debt growth × close
def f24dt_f24_debt_trajectory_debtgrowthmax_63d_base_v045_signal(debt, closeadj):
    result = _f24_debt_growth(debt, 21).rolling(63, min_periods=21).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 252d max debt growth × close
def f24dt_f24_debt_trajectory_debtgrowthmax_252d_base_v046_signal(debt, closeadj):
    result = _f24_debt_growth(debt, 63).rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 63d sum of debt growth × close
def f24dt_f24_debt_trajectory_debtgrowthsum_63d_base_v047_signal(debt, closeadj):
    result = _f24_debt_growth(debt, 21).rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 252d sum of debt growth × close
def f24dt_f24_debt_trajectory_debtgrowthsum_252d_base_v048_signal(debt, closeadj):
    result = _f24_debt_growth(debt, 63).rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 252d sum of debt traj × close
def f24dt_f24_debt_trajectory_debttrajsum_252d_base_v049_signal(debt, closeadj):
    result = _f24_debt_traj(debt, 21).rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt growth × abs(capex)
def f24dt_f24_debt_trajectory_debtgrowthxcapex_63d_base_v050_signal(debt, capex, closeadj):
    result = _f24_debt_growth(debt, 63) * capex.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt growth × abs(capex)
def f24dt_f24_debt_trajectory_debtgrowthxcapex_252d_base_v051_signal(debt, capex, closeadj):
    result = _f24_debt_growth(debt, 252) * capex.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt traj × abs(capex)
def f24dt_f24_debt_trajectory_debttrajxcapex_63d_base_v052_signal(debt, capex, closeadj):
    result = _f24_debt_traj(debt, 63) * capex.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d debt growth × abs(ncff)
def f24dt_f24_debt_trajectory_debtgrowthxncff_21d_base_v053_signal(debt, ncff, closeadj):
    result = _f24_debt_growth(debt, 21) * ncff.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt growth × abs(ncff)
def f24dt_f24_debt_trajectory_debtgrowthxncff_252d_base_v054_signal(debt, ncff, closeadj):
    result = _f24_debt_growth(debt, 252) * ncff.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of debt growth × close
def f24dt_f24_debt_trajectory_debtgrowthema_63d_base_v055_signal(debt, closeadj):
    g = _f24_debt_growth(debt, 63)
    result = g.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of debt growth × close
def f24dt_f24_debt_trajectory_debtgrowthema_252d_base_v056_signal(debt, closeadj):
    g = _f24_debt_growth(debt, 252)
    result = g.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of debt traj × close
def f24dt_f24_debt_trajectory_debttrajema_63d_base_v057_signal(debt, closeadj):
    g = _f24_debt_traj(debt, 63)
    result = g.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of debt traj × close
def f24dt_f24_debt_trajectory_debttrajema_252d_base_v058_signal(debt, closeadj):
    g = _f24_debt_traj(debt, 252)
    result = g.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d leverage traj × ebitda
def f24dt_f24_debt_trajectory_levtrajxebitda_21d_base_v059_signal(debt, equity, ebitda, closeadj):
    result = _f24_leverage_traj(debt, equity, 21) * ebitda
    return result.replace([np.inf, -np.inf], np.nan)


# 63d leverage traj × ebitda
def f24dt_f24_debt_trajectory_levtrajxebitda_63d_base_v060_signal(debt, equity, ebitda, closeadj):
    result = _f24_leverage_traj(debt, equity, 63) * ebitda
    return result.replace([np.inf, -np.inf], np.nan)


# 252d leverage traj × revenue
def f24dt_f24_debt_trajectory_levtrajxrev_252d_base_v061_signal(debt, equity, revenue, closeadj):
    result = _f24_leverage_traj(debt, equity, 252) * revenue
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of leverage traj
def f24dt_f24_debt_trajectory_levtrajz_252d_base_v062_signal(debt, equity, closeadj):
    result = _z(_f24_leverage_traj(debt, equity, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of leverage traj
def f24dt_f24_debt_trajectory_levtrajz_504d_base_v063_signal(debt, equity, closeadj):
    result = _z(_f24_leverage_traj(debt, equity, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d debt growth × close
def f24dt_f24_debt_trajectory_debtgrowth_5d_base_v064_signal(debt, closeadj):
    result = _f24_debt_growth(debt, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d debt growth × close
def f24dt_f24_debt_trajectory_debtgrowth_10d_base_v065_signal(debt, closeadj):
    result = _f24_debt_growth(debt, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d debt growth × close
def f24dt_f24_debt_trajectory_debtgrowth_42d_base_v066_signal(debt, closeadj):
    result = _f24_debt_growth(debt, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d debt growth × close
def f24dt_f24_debt_trajectory_debtgrowth_189d_base_v067_signal(debt, closeadj):
    result = _f24_debt_growth(debt, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d debt growth × close
def f24dt_f24_debt_trajectory_debtgrowth_378d_base_v068_signal(debt, closeadj):
    result = _f24_debt_growth(debt, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt growth area
def f24dt_f24_debt_trajectory_debtgrowtharea_252d_base_v069_signal(debt, closeadj):
    g = _f24_debt_growth(debt, 63).abs()
    result = g.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d debt growth area
def f24dt_f24_debt_trajectory_debtgrowtharea_504d_base_v070_signal(debt, closeadj):
    g = _f24_debt_growth(debt, 252).abs()
    result = g.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt growth × marketcap
def f24dt_f24_debt_trajectory_debtgrowthxmcap_252d_base_v071_signal(debt, closeadj, sharesbas):
    result = _f24_debt_growth(debt, 252) * (closeadj * sharesbas)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt growth × marketcap
def f24dt_f24_debt_trajectory_debtgrowthxmcap_63d_base_v072_signal(debt, closeadj, sharesbas):
    result = _f24_debt_growth(debt, 63) * (closeadj * sharesbas)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d debt growth × equity
def f24dt_f24_debt_trajectory_debtgrowthxequity_21d_base_v073_signal(debt, equity, closeadj):
    result = _f24_debt_growth(debt, 21) * equity
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt growth × equity
def f24dt_f24_debt_trajectory_debtgrowthxequity_252d_base_v074_signal(debt, equity, closeadj):
    result = _f24_debt_growth(debt, 252) * equity
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt growth × assets
def f24dt_f24_debt_trajectory_debtgrowthxassets_252d_base_v075_signal(debt, assets, closeadj):
    result = _f24_debt_growth(debt, 252) * assets
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f24dt_f24_debt_trajectory_debtgrowth_21d_base_v001_signal,
    f24dt_f24_debt_trajectory_debtgrowth_63d_base_v002_signal,
    f24dt_f24_debt_trajectory_debtgrowth_126d_base_v003_signal,
    f24dt_f24_debt_trajectory_debtgrowth_252d_base_v004_signal,
    f24dt_f24_debt_trajectory_debtgrowth_504d_base_v005_signal,
    f24dt_f24_debt_trajectory_debttraj_21d_base_v006_signal,
    f24dt_f24_debt_trajectory_debttraj_63d_base_v007_signal,
    f24dt_f24_debt_trajectory_debttraj_126d_base_v008_signal,
    f24dt_f24_debt_trajectory_debttraj_252d_base_v009_signal,
    f24dt_f24_debt_trajectory_debttraj_504d_base_v010_signal,
    f24dt_f24_debt_trajectory_levtraj_21d_base_v011_signal,
    f24dt_f24_debt_trajectory_levtraj_63d_base_v012_signal,
    f24dt_f24_debt_trajectory_levtraj_252d_base_v013_signal,
    f24dt_f24_debt_trajectory_levtraj_504d_base_v014_signal,
    f24dt_f24_debt_trajectory_debtgrowthmean_63d_base_v015_signal,
    f24dt_f24_debt_trajectory_debtgrowthmean_252d_base_v016_signal,
    f24dt_f24_debt_trajectory_debtgrowthstd_63d_base_v017_signal,
    f24dt_f24_debt_trajectory_debtgrowthstd_252d_base_v018_signal,
    f24dt_f24_debt_trajectory_debtgrowthz_252d_base_v019_signal,
    f24dt_f24_debt_trajectory_debtgrowthz_504d_base_v020_signal,
    f24dt_f24_debt_trajectory_debttrajz_252d_base_v021_signal,
    f24dt_f24_debt_trajectory_debttrajz_504d_base_v022_signal,
    f24dt_f24_debt_trajectory_debtgrowthhighcount_252d_base_v023_signal,
    f24dt_f24_debt_trajectory_debtgrowthlowcount_504d_base_v024_signal,
    f24dt_f24_debt_trajectory_levtrajexpcount_252d_base_v025_signal,
    f24dt_f24_debt_trajectory_debtgrowthsq_21d_base_v026_signal,
    f24dt_f24_debt_trajectory_debtgrowthsq_63d_base_v027_signal,
    f24dt_f24_debt_trajectory_debtgrowthsq_252d_base_v028_signal,
    f24dt_f24_debt_trajectory_debttrajxrev_21d_base_v029_signal,
    f24dt_f24_debt_trajectory_debttrajxrev_63d_base_v030_signal,
    f24dt_f24_debt_trajectory_debtgrowthxrev_252d_base_v031_signal,
    f24dt_f24_debt_trajectory_debtgrowthdiff_21m63_base_v032_signal,
    f24dt_f24_debt_trajectory_debtgrowthdiff_63m252_base_v033_signal,
    f24dt_f24_debt_trajectory_debtgrowthdiff_252m504_base_v034_signal,
    f24dt_f24_debt_trajectory_debtgrowthratio_63v252_base_v035_signal,
    f24dt_f24_debt_trajectory_debtgrowthratio_21v63_base_v036_signal,
    f24dt_f24_debt_trajectory_debtgrowthprod_63x252_base_v037_signal,
    f24dt_f24_debt_trajectory_debtgrowthxlev_21d_base_v038_signal,
    f24dt_f24_debt_trajectory_debtgrowthxlev_252d_base_v039_signal,
    f24dt_f24_debt_trajectory_debtgrowthxebitda_21d_base_v040_signal,
    f24dt_f24_debt_trajectory_debtgrowthxebitda_63d_base_v041_signal,
    f24dt_f24_debt_trajectory_debtgrowthxebitda_252d_base_v042_signal,
    f24dt_f24_debt_trajectory_debttrajxnetinc_63d_base_v043_signal,
    f24dt_f24_debt_trajectory_debttrajxnetinc_252d_base_v044_signal,
    f24dt_f24_debt_trajectory_debtgrowthmax_63d_base_v045_signal,
    f24dt_f24_debt_trajectory_debtgrowthmax_252d_base_v046_signal,
    f24dt_f24_debt_trajectory_debtgrowthsum_63d_base_v047_signal,
    f24dt_f24_debt_trajectory_debtgrowthsum_252d_base_v048_signal,
    f24dt_f24_debt_trajectory_debttrajsum_252d_base_v049_signal,
    f24dt_f24_debt_trajectory_debtgrowthxcapex_63d_base_v050_signal,
    f24dt_f24_debt_trajectory_debtgrowthxcapex_252d_base_v051_signal,
    f24dt_f24_debt_trajectory_debttrajxcapex_63d_base_v052_signal,
    f24dt_f24_debt_trajectory_debtgrowthxncff_21d_base_v053_signal,
    f24dt_f24_debt_trajectory_debtgrowthxncff_252d_base_v054_signal,
    f24dt_f24_debt_trajectory_debtgrowthema_63d_base_v055_signal,
    f24dt_f24_debt_trajectory_debtgrowthema_252d_base_v056_signal,
    f24dt_f24_debt_trajectory_debttrajema_63d_base_v057_signal,
    f24dt_f24_debt_trajectory_debttrajema_252d_base_v058_signal,
    f24dt_f24_debt_trajectory_levtrajxebitda_21d_base_v059_signal,
    f24dt_f24_debt_trajectory_levtrajxebitda_63d_base_v060_signal,
    f24dt_f24_debt_trajectory_levtrajxrev_252d_base_v061_signal,
    f24dt_f24_debt_trajectory_levtrajz_252d_base_v062_signal,
    f24dt_f24_debt_trajectory_levtrajz_504d_base_v063_signal,
    f24dt_f24_debt_trajectory_debtgrowth_5d_base_v064_signal,
    f24dt_f24_debt_trajectory_debtgrowth_10d_base_v065_signal,
    f24dt_f24_debt_trajectory_debtgrowth_42d_base_v066_signal,
    f24dt_f24_debt_trajectory_debtgrowth_189d_base_v067_signal,
    f24dt_f24_debt_trajectory_debtgrowth_378d_base_v068_signal,
    f24dt_f24_debt_trajectory_debtgrowtharea_252d_base_v069_signal,
    f24dt_f24_debt_trajectory_debtgrowtharea_504d_base_v070_signal,
    f24dt_f24_debt_trajectory_debtgrowthxmcap_252d_base_v071_signal,
    f24dt_f24_debt_trajectory_debtgrowthxmcap_63d_base_v072_signal,
    f24dt_f24_debt_trajectory_debtgrowthxequity_21d_base_v073_signal,
    f24dt_f24_debt_trajectory_debtgrowthxequity_252d_base_v074_signal,
    f24dt_f24_debt_trajectory_debtgrowthxassets_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F24_DEBT_TRAJECTORY_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    revenue = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="revenue")
    netinc = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="netinc")
    ncff = pd.Series(-2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="ncff")
    equity = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.004, n))), name="equity")
    debt = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.005, n))), name="debt")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.003, n))), name="assets")
    ebitda = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.006, n))), name="ebitda")
    capex = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="capex")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.002, n))), name="sharesbas")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "netinc": netinc, "ncff": ncff,
        "equity": equity, "debt": debt, "assets": assets, "ebitda": ebitda,
        "capex": capex, "sharesbas": sharesbas,
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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f24_debt_trajectory_base_001_075_claude: {n_features} features pass")
