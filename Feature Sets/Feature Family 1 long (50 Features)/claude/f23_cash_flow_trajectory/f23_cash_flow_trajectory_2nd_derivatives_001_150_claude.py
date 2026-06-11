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


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f23_cashflow_traj(s, w):
    return s.diff(periods=w) / s.abs().rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)


def _f23_fcf_growth(fcf, w):
    base = fcf.rolling(w, min_periods=max(1, w // 2)).mean()
    return base.diff(periods=w) / base.abs().shift(w).replace(0, np.nan)


def _f23_fcf_acceleration(fcf, w):
    g1 = _f23_fcf_growth(fcf, w)
    return g1.diff(periods=w)


# 5d slope of 21d FCF growth
def f23cft_f23_cash_flow_trajectory_fcfgrowth_21d_slope_v001_signal(fcf, closeadj):
    base = _f23_fcf_growth(fcf, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d FCF growth
def f23cft_f23_cash_flow_trajectory_fcfgrowth_21d_slope_v002_signal(fcf, closeadj):
    base = _f23_fcf_growth(fcf, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d FCF growth
def f23cft_f23_cash_flow_trajectory_fcfgrowth_63d_slope_v003_signal(fcf, closeadj):
    base = _f23_fcf_growth(fcf, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d FCF growth
def f23cft_f23_cash_flow_trajectory_fcfgrowth_63d_slope_v004_signal(fcf, closeadj):
    base = _f23_fcf_growth(fcf, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d FCF growth
def f23cft_f23_cash_flow_trajectory_fcfgrowth_63d_slope_v005_signal(fcf, closeadj):
    base = _f23_fcf_growth(fcf, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d FCF growth
def f23cft_f23_cash_flow_trajectory_fcfgrowth_126d_slope_v006_signal(fcf, closeadj):
    base = _f23_fcf_growth(fcf, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d FCF growth
def f23cft_f23_cash_flow_trajectory_fcfgrowth_126d_slope_v007_signal(fcf, closeadj):
    base = _f23_fcf_growth(fcf, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d FCF growth
def f23cft_f23_cash_flow_trajectory_fcfgrowth_252d_slope_v008_signal(fcf, closeadj):
    base = _f23_fcf_growth(fcf, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF growth
def f23cft_f23_cash_flow_trajectory_fcfgrowth_252d_slope_v009_signal(fcf, closeadj):
    base = _f23_fcf_growth(fcf, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d FCF growth
def f23cft_f23_cash_flow_trajectory_fcfgrowth_504d_slope_v010_signal(fcf, closeadj):
    base = _f23_fcf_growth(fcf, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d FCF growth
def f23cft_f23_cash_flow_trajectory_fcfgrowth_504d_slope_v011_signal(fcf, closeadj):
    base = _f23_fcf_growth(fcf, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ncfo trajectory
def f23cft_f23_cash_flow_trajectory_ncfotraj_21d_slope_v012_signal(ncfo, closeadj):
    base = _f23_cashflow_traj(ncfo, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ncfo trajectory
def f23cft_f23_cash_flow_trajectory_ncfotraj_63d_slope_v013_signal(ncfo, closeadj):
    base = _f23_cashflow_traj(ncfo, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ncfo trajectory
def f23cft_f23_cash_flow_trajectory_ncfotraj_126d_slope_v014_signal(ncfo, closeadj):
    base = _f23_cashflow_traj(ncfo, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ncfo trajectory
def f23cft_f23_cash_flow_trajectory_ncfotraj_252d_slope_v015_signal(ncfo, closeadj):
    base = _f23_cashflow_traj(ncfo, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ncfo trajectory
def f23cft_f23_cash_flow_trajectory_ncfotraj_504d_slope_v016_signal(ncfo, closeadj):
    base = _f23_cashflow_traj(ncfo, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d FCF accel
def f23cft_f23_cash_flow_trajectory_fcfaccel_21d_slope_v017_signal(fcf, closeadj):
    base = _f23_fcf_acceleration(fcf, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d FCF accel
def f23cft_f23_cash_flow_trajectory_fcfaccel_63d_slope_v018_signal(fcf, closeadj):
    base = _f23_fcf_acceleration(fcf, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF accel
def f23cft_f23_cash_flow_trajectory_fcfaccel_252d_slope_v019_signal(fcf, closeadj):
    base = _f23_fcf_acceleration(fcf, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d mean FCF growth
def f23cft_f23_cash_flow_trajectory_fcfgrowthmean_63d_slope_v020_signal(fcf, closeadj):
    base = _mean(_f23_fcf_growth(fcf, 63), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d mean FCF growth
def f23cft_f23_cash_flow_trajectory_fcfgrowthmean_252d_slope_v021_signal(fcf, closeadj):
    base = _mean(_f23_fcf_growth(fcf, 252), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std FCF growth
def f23cft_f23_cash_flow_trajectory_fcfgrowthstd_63d_slope_v022_signal(fcf, closeadj):
    base = _std(_f23_fcf_growth(fcf, 63), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std FCF growth
def f23cft_f23_cash_flow_trajectory_fcfgrowthstd_252d_slope_v023_signal(fcf, closeadj):
    base = _std(_f23_fcf_growth(fcf, 252), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d FCF growth zscore
def f23cft_f23_cash_flow_trajectory_fcfgrowthz_252d_slope_v024_signal(fcf, closeadj):
    base = _z(_f23_fcf_growth(fcf, 63), 252)
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d FCF growth zscore
def f23cft_f23_cash_flow_trajectory_fcfgrowthz_504d_slope_v025_signal(fcf, closeadj):
    base = _z(_f23_fcf_growth(fcf, 252), 504)
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ncfo trajectory zscore
def f23cft_f23_cash_flow_trajectory_ncfotrajz_252d_slope_v026_signal(ncfo, closeadj):
    base = _z(_f23_cashflow_traj(ncfo, 63), 252)
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ncfo trajectory zscore
def f23cft_f23_cash_flow_trajectory_ncfotrajz_504d_slope_v027_signal(ncfo, closeadj):
    base = _z(_f23_cashflow_traj(ncfo, 252), 504)
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d FCF growth pos count
def f23cft_f23_cash_flow_trajectory_fcfgrowthposcount_252d_slope_v028_signal(fcf, closeadj):
    flag = (_f23_fcf_growth(fcf, 63) > 0).astype(float)
    base = flag.rolling(252, min_periods=63).sum() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d FCF growth pos count
def f23cft_f23_cash_flow_trajectory_fcfgrowthposcount_504d_slope_v029_signal(fcf, closeadj):
    flag = (_f23_fcf_growth(fcf, 252) > 0).astype(float)
    base = flag.rolling(504, min_periods=126).sum() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ncfo neg count
def f23cft_f23_cash_flow_trajectory_ncfotrajnegcount_252d_slope_v030_signal(ncfo, closeadj):
    flag = (_f23_cashflow_traj(ncfo, 63) < 0).astype(float)
    base = flag.rolling(252, min_periods=63).sum() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d FCF growth squared
def f23cft_f23_cash_flow_trajectory_fcfgrowthsq_21d_slope_v031_signal(fcf, closeadj):
    g = _f23_fcf_growth(fcf, 21)
    base = g * g.abs() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d FCF growth squared
def f23cft_f23_cash_flow_trajectory_fcfgrowthsq_63d_slope_v032_signal(fcf, closeadj):
    g = _f23_fcf_growth(fcf, 63)
    base = g * g.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF growth squared
def f23cft_f23_cash_flow_trajectory_fcfgrowthsq_252d_slope_v033_signal(fcf, closeadj):
    g = _f23_fcf_growth(fcf, 252)
    base = g * g.abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ncfo traj × revenue
def f23cft_f23_cash_flow_trajectory_ncfotrajxrev_21d_slope_v034_signal(ncfo, revenue, closeadj):
    base = _f23_cashflow_traj(ncfo, 21) * revenue
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ncfo traj × revenue
def f23cft_f23_cash_flow_trajectory_ncfotrajxrev_63d_slope_v035_signal(ncfo, revenue, closeadj):
    base = _f23_cashflow_traj(ncfo, 63) * revenue
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF growth × revenue
def f23cft_f23_cash_flow_trajectory_fcfgrowthxrev_252d_slope_v036_signal(fcf, revenue, closeadj):
    base = _f23_fcf_growth(fcf, 252) * revenue
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ncfo traj diff (21m63)
def f23cft_f23_cash_flow_trajectory_ncfotrajdiff_21m63_slope_v037_signal(ncfo, closeadj):
    base = (_f23_cashflow_traj(ncfo, 21) - _f23_cashflow_traj(ncfo, 63)) * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of FCF growth diff 63m252
def f23cft_f23_cash_flow_trajectory_fcfgrowthdiff_63m252_slope_v038_signal(fcf, closeadj):
    base = (_f23_fcf_growth(fcf, 63) - _f23_fcf_growth(fcf, 252)) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF growth diff 252m504
def f23cft_f23_cash_flow_trajectory_fcfgrowthdiff_252m504_slope_v039_signal(fcf, closeadj):
    base = (_f23_fcf_growth(fcf, 252) - _f23_fcf_growth(fcf, 504)) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of FCF growth ratio 63v252
def f23cft_f23_cash_flow_trajectory_fcfgrowthratio_63v252_slope_v040_signal(fcf, closeadj):
    a = _f23_fcf_growth(fcf, 63)
    b = _f23_fcf_growth(fcf, 252).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of ncfo traj ratio 21v63
def f23cft_f23_cash_flow_trajectory_ncfotrajratio_21v63_slope_v041_signal(ncfo, closeadj):
    a = _f23_cashflow_traj(ncfo, 21)
    b = _f23_cashflow_traj(ncfo, 63).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF growth product 63x252
def f23cft_f23_cash_flow_trajectory_fcfgrowthprod_63x252_slope_v042_signal(fcf, closeadj):
    base = _f23_fcf_growth(fcf, 63) * _f23_fcf_growth(fcf, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d FCF growth × ncfo traj
def f23cft_f23_cash_flow_trajectory_fcfgrowthxncfo_21d_slope_v043_signal(fcf, ncfo, closeadj):
    base = _f23_fcf_growth(fcf, 21) * _f23_cashflow_traj(ncfo, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF growth × ncfo traj
def f23cft_f23_cash_flow_trajectory_fcfgrowthxncfo_252d_slope_v044_signal(fcf, ncfo, closeadj):
    base = _f23_fcf_growth(fcf, 252) * _f23_cashflow_traj(ncfo, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d FCF growth × ebitda
def f23cft_f23_cash_flow_trajectory_fcfgrowthxebitda_21d_slope_v045_signal(fcf, ebitda, closeadj):
    base = _f23_fcf_growth(fcf, 21) * ebitda
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d FCF growth × ebitda
def f23cft_f23_cash_flow_trajectory_fcfgrowthxebitda_63d_slope_v046_signal(fcf, ebitda, closeadj):
    base = _f23_fcf_growth(fcf, 63) * ebitda
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF growth × ebitda
def f23cft_f23_cash_flow_trajectory_fcfgrowthxebitda_252d_slope_v047_signal(fcf, ebitda, closeadj):
    base = _f23_fcf_growth(fcf, 252) * ebitda
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ncfo traj × netinc
def f23cft_f23_cash_flow_trajectory_ncfotrajxnetinc_63d_slope_v048_signal(ncfo, netinc, closeadj):
    base = _f23_cashflow_traj(ncfo, 63) * netinc
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ncfo traj × netinc
def f23cft_f23_cash_flow_trajectory_ncfotrajxnetinc_252d_slope_v049_signal(ncfo, netinc, closeadj):
    base = _f23_cashflow_traj(ncfo, 252) * netinc
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d max FCF growth
def f23cft_f23_cash_flow_trajectory_fcfgrowthmax_63d_slope_v050_signal(fcf, closeadj):
    base = _f23_fcf_growth(fcf, 21).rolling(63, min_periods=21).max() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d max FCF growth
def f23cft_f23_cash_flow_trajectory_fcfgrowthmax_252d_slope_v051_signal(fcf, closeadj):
    base = _f23_fcf_growth(fcf, 63).rolling(252, min_periods=63).max() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sum FCF growth
def f23cft_f23_cash_flow_trajectory_fcfgrowthsum_63d_slope_v052_signal(fcf, closeadj):
    base = _f23_fcf_growth(fcf, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sum FCF growth
def f23cft_f23_cash_flow_trajectory_fcfgrowthsum_252d_slope_v053_signal(fcf, closeadj):
    base = _f23_fcf_growth(fcf, 63).rolling(252, min_periods=63).sum() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sum ncfo traj
def f23cft_f23_cash_flow_trajectory_ncfotrajsum_252d_slope_v054_signal(ncfo, closeadj):
    base = _f23_cashflow_traj(ncfo, 21).rolling(252, min_periods=63).sum() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d FCF growth × capex
def f23cft_f23_cash_flow_trajectory_fcfgrowthxcapex_63d_slope_v055_signal(fcf, capex, closeadj):
    base = _f23_fcf_growth(fcf, 63) * capex.abs()
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF growth × capex
def f23cft_f23_cash_flow_trajectory_fcfgrowthxcapex_252d_slope_v056_signal(fcf, capex, closeadj):
    base = _f23_fcf_growth(fcf, 252) * capex.abs()
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ncfo traj × capex
def f23cft_f23_cash_flow_trajectory_ncfotrajxcapex_63d_slope_v057_signal(ncfo, capex, closeadj):
    base = _f23_cashflow_traj(ncfo, 63) * capex.abs()
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d FCF growth × ncff
def f23cft_f23_cash_flow_trajectory_fcfgrowthxncff_21d_slope_v058_signal(fcf, ncff, closeadj):
    base = _f23_fcf_growth(fcf, 21) * ncff.abs()
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF growth × ncff
def f23cft_f23_cash_flow_trajectory_fcfgrowthxncff_252d_slope_v059_signal(fcf, ncff, closeadj):
    base = _f23_fcf_growth(fcf, 252) * ncff.abs()
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d FCF growth EMA
def f23cft_f23_cash_flow_trajectory_fcfgrowthema_63d_slope_v060_signal(fcf, closeadj):
    g = _f23_fcf_growth(fcf, 63)
    base = g.ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF growth EMA
def f23cft_f23_cash_flow_trajectory_fcfgrowthema_252d_slope_v061_signal(fcf, closeadj):
    g = _f23_fcf_growth(fcf, 252)
    base = g.ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ncfo traj EMA
def f23cft_f23_cash_flow_trajectory_ncfotrajema_63d_slope_v062_signal(ncfo, closeadj):
    g = _f23_cashflow_traj(ncfo, 63)
    base = g.ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ncfo traj EMA
def f23cft_f23_cash_flow_trajectory_ncfotrajema_252d_slope_v063_signal(ncfo, closeadj):
    g = _f23_cashflow_traj(ncfo, 252)
    base = g.ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d FCF accel × ebitda
def f23cft_f23_cash_flow_trajectory_fcfaccelxebitda_21d_slope_v064_signal(fcf, ebitda, closeadj):
    base = _f23_fcf_acceleration(fcf, 21) * ebitda
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d FCF accel × ebitda
def f23cft_f23_cash_flow_trajectory_fcfaccelxebitda_63d_slope_v065_signal(fcf, ebitda, closeadj):
    base = _f23_fcf_acceleration(fcf, 63) * ebitda
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF accel × revenue
def f23cft_f23_cash_flow_trajectory_fcfaccelxrev_252d_slope_v066_signal(fcf, revenue, closeadj):
    base = _f23_fcf_acceleration(fcf, 252) * revenue
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d FCF accel zscore
def f23cft_f23_cash_flow_trajectory_fcfaccelz_252d_slope_v067_signal(fcf, closeadj):
    base = _z(_f23_fcf_acceleration(fcf, 63), 252)
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d FCF accel zscore
def f23cft_f23_cash_flow_trajectory_fcfaccelz_504d_slope_v068_signal(fcf, closeadj):
    base = _z(_f23_fcf_acceleration(fcf, 252), 504)
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 5d FCF growth
def f23cft_f23_cash_flow_trajectory_fcfgrowth_5d_slope_v069_signal(fcf, closeadj):
    base = _f23_fcf_growth(fcf, 5) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 10d FCF growth
def f23cft_f23_cash_flow_trajectory_fcfgrowth_10d_slope_v070_signal(fcf, closeadj):
    base = _f23_fcf_growth(fcf, 10) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 42d FCF growth
def f23cft_f23_cash_flow_trajectory_fcfgrowth_42d_slope_v071_signal(fcf, closeadj):
    base = _f23_fcf_growth(fcf, 42) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 189d FCF growth
def f23cft_f23_cash_flow_trajectory_fcfgrowth_189d_slope_v072_signal(fcf, closeadj):
    base = _f23_fcf_growth(fcf, 189) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 378d FCF growth
def f23cft_f23_cash_flow_trajectory_fcfgrowth_378d_slope_v073_signal(fcf, closeadj):
    base = _f23_fcf_growth(fcf, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF growth area
def f23cft_f23_cash_flow_trajectory_fcfgrowtharea_252d_slope_v074_signal(fcf, closeadj):
    g = _f23_fcf_growth(fcf, 63).abs()
    base = g.rolling(252, min_periods=63).sum() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d FCF growth area
def f23cft_f23_cash_flow_trajectory_fcfgrowtharea_504d_slope_v075_signal(fcf, closeadj):
    g = _f23_fcf_growth(fcf, 252).abs()
    base = g.rolling(504, min_periods=126).sum() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF growth × mcap
def f23cft_f23_cash_flow_trajectory_fcfgrowthxmcap_252d_slope_v076_signal(fcf, closeadj, sharesbas):
    base = _f23_fcf_growth(fcf, 252) * (closeadj * sharesbas)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d FCF growth × mcap
def f23cft_f23_cash_flow_trajectory_fcfgrowthxmcap_63d_slope_v077_signal(fcf, closeadj, sharesbas):
    base = _f23_fcf_growth(fcf, 63) * (closeadj * sharesbas)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d FCF growth × equity
def f23cft_f23_cash_flow_trajectory_fcfgrowthxequity_21d_slope_v078_signal(fcf, equity, closeadj):
    base = _f23_fcf_growth(fcf, 21) * equity
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF growth × equity
def f23cft_f23_cash_flow_trajectory_fcfgrowthxequity_252d_slope_v079_signal(fcf, equity, closeadj):
    base = _f23_fcf_growth(fcf, 252) * equity
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF growth × assets
def f23cft_f23_cash_flow_trajectory_fcfgrowthxassets_252d_slope_v080_signal(fcf, assets, closeadj):
    base = _f23_fcf_growth(fcf, 252) * assets
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF growth × debt
def f23cft_f23_cash_flow_trajectory_fcfgrowthxdebt_252d_slope_v081_signal(fcf, debt, closeadj):
    base = _f23_fcf_growth(fcf, 252) * debt
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ncfo traj × debt
def f23cft_f23_cash_flow_trajectory_ncfotrajxdebt_63d_slope_v082_signal(ncfo, debt, closeadj):
    base = _f23_cashflow_traj(ncfo, 63) * debt
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF growth × gp
def f23cft_f23_cash_flow_trajectory_fcfgrowthxgp_252d_slope_v083_signal(fcf, gp, closeadj):
    base = _f23_fcf_growth(fcf, 252) * gp
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d FCF growth × gp
def f23cft_f23_cash_flow_trajectory_fcfgrowthxgp_63d_slope_v084_signal(fcf, gp, closeadj):
    base = _f23_fcf_growth(fcf, 63) * gp
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF growth × opinc
def f23cft_f23_cash_flow_trajectory_fcfgrowthxopinc_252d_slope_v085_signal(fcf, opinc, closeadj):
    base = _f23_fcf_growth(fcf, 252) * opinc
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d FCF growth × opinc
def f23cft_f23_cash_flow_trajectory_fcfgrowthxopinc_63d_slope_v086_signal(fcf, opinc, closeadj):
    base = _f23_fcf_growth(fcf, 63) * opinc
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF growth × eps
def f23cft_f23_cash_flow_trajectory_fcfgrowthxeps_252d_slope_v087_signal(fcf, eps, closeadj):
    base = _f23_fcf_growth(fcf, 252) * eps * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ncfo traj × eps
def f23cft_f23_cash_flow_trajectory_ncfotrajxeps_63d_slope_v088_signal(ncfo, eps, closeadj):
    base = _f23_cashflow_traj(ncfo, 63) * eps * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF growth × wc
def f23cft_f23_cash_flow_trajectory_fcfgrowthxwc_252d_slope_v089_signal(fcf, workingcapital, closeadj):
    base = _f23_fcf_growth(fcf, 252) * workingcapital
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ncfo traj × wc
def f23cft_f23_cash_flow_trajectory_ncfotrajxwc_63d_slope_v090_signal(ncfo, workingcapital, closeadj):
    base = _f23_cashflow_traj(ncfo, 63) * workingcapital
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d FCF growth × cr
def f23cft_f23_cash_flow_trajectory_fcfgrowthxcr_21d_slope_v091_signal(fcf, currentratio, closeadj):
    base = _f23_fcf_growth(fcf, 21) * currentratio * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF growth × cr
def f23cft_f23_cash_flow_trajectory_fcfgrowthxcr_252d_slope_v092_signal(fcf, currentratio, closeadj):
    base = _f23_fcf_growth(fcf, 252) * currentratio * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ncfo traj × cr
def f23cft_f23_cash_flow_trajectory_ncfotrajxcr_252d_slope_v093_signal(ncfo, currentratio, closeadj):
    base = _f23_cashflow_traj(ncfo, 252) * currentratio * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d FCF growth × liab
def f23cft_f23_cash_flow_trajectory_fcfgrowthxliab_63d_slope_v094_signal(fcf, liabilities, closeadj):
    base = _f23_fcf_growth(fcf, 63) * liabilities
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF growth × liab
def f23cft_f23_cash_flow_trajectory_fcfgrowthxliab_252d_slope_v095_signal(fcf, liabilities, closeadj):
    base = _f23_fcf_growth(fcf, 252) * liabilities
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ncfo traj × retearn
def f23cft_f23_cash_flow_trajectory_ncfotrajxre_63d_slope_v096_signal(ncfo, retearn, closeadj):
    base = _f23_cashflow_traj(ncfo, 63) * retearn
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF growth × retearn
def f23cft_f23_cash_flow_trajectory_fcfgrowthxre_252d_slope_v097_signal(fcf, retearn, closeadj):
    base = _f23_fcf_growth(fcf, 252) * retearn
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ncfo traj × intexp
def f23cft_f23_cash_flow_trajectory_ncfotrajxintexp_63d_slope_v098_signal(ncfo, intexp, closeadj):
    base = _f23_cashflow_traj(ncfo, 63) * intexp
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF growth × intexp
def f23cft_f23_cash_flow_trajectory_fcfgrowthxintexp_252d_slope_v099_signal(fcf, intexp, closeadj):
    base = _f23_fcf_growth(fcf, 252) * intexp
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF growth × tax
def f23cft_f23_cash_flow_trajectory_fcfgrowthxtax_252d_slope_v100_signal(fcf, taxexp, closeadj):
    base = _f23_fcf_growth(fcf, 252) * taxexp
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ncfo traj squared
def f23cft_f23_cash_flow_trajectory_ncfotrajsq_21d_slope_v101_signal(ncfo, closeadj):
    g = _f23_cashflow_traj(ncfo, 21)
    base = g * g.abs() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ncfo traj squared
def f23cft_f23_cash_flow_trajectory_ncfotrajsq_252d_slope_v102_signal(ncfo, closeadj):
    g = _f23_cashflow_traj(ncfo, 252)
    base = g * g.abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ncfo traj area
def f23cft_f23_cash_flow_trajectory_ncfotrajarea_63d_slope_v103_signal(ncfo, closeadj):
    g = _f23_cashflow_traj(ncfo, 21).abs()
    base = g.rolling(63, min_periods=21).sum() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ncfo traj area
def f23cft_f23_cash_flow_trajectory_ncfotrajarea_252d_slope_v104_signal(ncfo, closeadj):
    g = _f23_cashflow_traj(ncfo, 63).abs()
    base = g.rolling(252, min_periods=63).sum() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ncfo traj area
def f23cft_f23_cash_flow_trajectory_ncfotrajarea_504d_slope_v105_signal(ncfo, closeadj):
    g = _f23_cashflow_traj(ncfo, 252).abs()
    base = g.rolling(504, min_periods=126).sum() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF growth - ncfo traj
def f23cft_f23_cash_flow_trajectory_fcfminusncfo_252d_slope_v106_signal(fcf, ncfo, closeadj):
    base = (_f23_fcf_growth(fcf, 252) - _f23_cashflow_traj(ncfo, 252)) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d FCF growth - ncfo traj
def f23cft_f23_cash_flow_trajectory_fcfminusncfo_63d_slope_v107_signal(fcf, ncfo, closeadj):
    base = (_f23_fcf_growth(fcf, 63) - _f23_cashflow_traj(ncfo, 63)) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF growth + ncfo traj
def f23cft_f23_cash_flow_trajectory_fcfplusncfo_252d_slope_v108_signal(fcf, ncfo, closeadj):
    base = (_f23_fcf_growth(fcf, 252) + _f23_cashflow_traj(ncfo, 252)) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of expanding worst FCF growth × close
def f23cft_f23_cash_flow_trajectory_fcfgrowthworst_504d_slope_v109_signal(fcf, closeadj):
    g = _f23_fcf_growth(fcf, 252)
    base = g.expanding(min_periods=63).min() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of expanding best FCF growth × close
def f23cft_f23_cash_flow_trajectory_fcfgrowthbest_504d_slope_v110_signal(fcf, closeadj):
    g = _f23_fcf_growth(fcf, 252)
    base = g.expanding(min_periods=63).max() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d max ncfo traj
def f23cft_f23_cash_flow_trajectory_ncfotrajmax_63d_slope_v111_signal(ncfo, closeadj):
    base = _f23_cashflow_traj(ncfo, 21).rolling(63, min_periods=21).max() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d max ncfo traj
def f23cft_f23_cash_flow_trajectory_ncfotrajmax_252d_slope_v112_signal(ncfo, closeadj):
    base = _f23_cashflow_traj(ncfo, 63).rolling(252, min_periods=63).max() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d min ncfo traj
def f23cft_f23_cash_flow_trajectory_ncfotrajmin_63d_slope_v113_signal(ncfo, closeadj):
    base = _f23_cashflow_traj(ncfo, 21).rolling(63, min_periods=21).min() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d min ncfo traj
def f23cft_f23_cash_flow_trajectory_ncfotrajmin_252d_slope_v114_signal(ncfo, closeadj):
    base = _f23_cashflow_traj(ncfo, 63).rolling(252, min_periods=63).min() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d FCF growth EMA × ebitda
def f23cft_f23_cash_flow_trajectory_fcfgrowthemaebitda_21d_slope_v115_signal(fcf, ebitda, closeadj):
    g = _f23_fcf_growth(fcf, 21)
    base = g.ewm(span=21, adjust=False).mean() * ebitda
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF growth EMA × ebitda
def f23cft_f23_cash_flow_trajectory_fcfgrowthemaebitda_252d_slope_v116_signal(fcf, ebitda, closeadj):
    g = _f23_fcf_growth(fcf, 252)
    base = g.ewm(span=252, adjust=False).mean() * ebitda
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF growth area × mcap
def f23cft_f23_cash_flow_trajectory_fcfgrowthareaxmcap_252d_slope_v117_signal(fcf, closeadj, sharesbas):
    g = _f23_fcf_growth(fcf, 63).abs()
    base = g.rolling(252, min_periods=63).sum() * (closeadj * sharesbas)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ncfo traj anomaly
def f23cft_f23_cash_flow_trajectory_ncfotrajanom_63d_slope_v118_signal(ncfo, closeadj):
    base = (_f23_cashflow_traj(ncfo, 63) - _mean(_f23_cashflow_traj(ncfo, 252), 252)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ncfo traj anomaly
def f23cft_f23_cash_flow_trajectory_ncfotrajanom_252d_slope_v119_signal(ncfo, closeadj):
    base = (_f23_cashflow_traj(ncfo, 252) - _mean(_f23_cashflow_traj(ncfo, 504), 504)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d FCF growth anomaly
def f23cft_f23_cash_flow_trajectory_fcfgrowthanom_63d_slope_v120_signal(fcf, closeadj):
    base = (_f23_fcf_growth(fcf, 63) - _mean(_f23_fcf_growth(fcf, 252), 252)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF growth anomaly
def f23cft_f23_cash_flow_trajectory_fcfgrowthanom_252d_slope_v121_signal(fcf, closeadj):
    base = (_f23_fcf_growth(fcf, 252) - _mean(_f23_fcf_growth(fcf, 504), 504)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d FCF growth × rev × close
def f23cft_f23_cash_flow_trajectory_fcfgrowthxrevxprice_21d_slope_v122_signal(fcf, revenue, closeadj):
    base = _f23_fcf_growth(fcf, 21) * revenue * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF growth × rev × close
def f23cft_f23_cash_flow_trajectory_fcfgrowthxrevxprice_252d_slope_v123_signal(fcf, revenue, closeadj):
    base = _f23_fcf_growth(fcf, 252) * revenue * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF accel × mcap
def f23cft_f23_cash_flow_trajectory_fcfaccelxmcap_252d_slope_v124_signal(fcf, closeadj, sharesbas):
    base = _f23_fcf_acceleration(fcf, 252) * (closeadj * sharesbas)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d FCF accel × mcap
def f23cft_f23_cash_flow_trajectory_fcfaccelxmcap_63d_slope_v125_signal(fcf, closeadj, sharesbas):
    base = _f23_fcf_acceleration(fcf, 63) * (closeadj * sharesbas)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d FCF growth × ncfo level
def f23cft_f23_cash_flow_trajectory_fcfgrowthxncfolvl_21d_slope_v126_signal(fcf, ncfo, closeadj):
    base = _f23_fcf_growth(fcf, 21) * ncfo * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF growth × ncfo level
def f23cft_f23_cash_flow_trajectory_fcfgrowthxncfolvl_252d_slope_v127_signal(fcf, ncfo, closeadj):
    base = _f23_fcf_growth(fcf, 252) * ncfo * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ncfo traj × ebitda × close
def f23cft_f23_cash_flow_trajectory_ncfotrajxebitdaprice_252d_slope_v128_signal(ncfo, ebitda, closeadj):
    base = _f23_cashflow_traj(ncfo, 252) * ebitda * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF growth × ebitda × close
def f23cft_f23_cash_flow_trajectory_fcfgrowthxebitdaprice_252d_slope_v129_signal(fcf, ebitda, closeadj):
    base = _f23_fcf_growth(fcf, 252) * ebitda * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF gap × ebitda
def f23cft_f23_cash_flow_trajectory_fcfgapxebitda_252d_slope_v130_signal(fcf, ebitda, capex, closeadj):
    base = _f23_fcf_growth(fcf, 252) * (ebitda - capex.abs()) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ncfo traj × net assets
def f23cft_f23_cash_flow_trajectory_ncfotrajxnet_252d_slope_v131_signal(ncfo, assets, liabilities, closeadj):
    base = _f23_cashflow_traj(ncfo, 252) * (assets - liabilities)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d FCF growth EMA × close
def f23cft_f23_cash_flow_trajectory_fcfgrowthema_21d_slope_v132_signal(fcf, closeadj):
    g = _f23_fcf_growth(fcf, 21)
    base = g.ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ncfo traj EMA × close
def f23cft_f23_cash_flow_trajectory_ncfotrajema_21d_slope_v133_signal(ncfo, closeadj):
    g = _f23_cashflow_traj(ncfo, 21)
    base = g.ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d FCF growth rank × close
def f23cft_f23_cash_flow_trajectory_fcfgrowthrank_252d_slope_v134_signal(fcf, closeadj):
    g = _f23_fcf_growth(fcf, 21)
    base = g.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ncfo traj rank × close
def f23cft_f23_cash_flow_trajectory_ncfotrajrank_252d_slope_v135_signal(ncfo, closeadj):
    g = _f23_cashflow_traj(ncfo, 63)
    base = g.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d FCF growth high count
def f23cft_f23_cash_flow_trajectory_fcfgrowthhighcount_252d_slope_v136_signal(fcf, closeadj):
    flag = (_f23_fcf_growth(fcf, 63) > 0.05).astype(float)
    base = flag.rolling(252, min_periods=63).sum() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d FCF growth low count
def f23cft_f23_cash_flow_trajectory_fcfgrowthlowcount_504d_slope_v137_signal(fcf, closeadj):
    flag = (_f23_fcf_growth(fcf, 63) < -0.05).astype(float)
    base = flag.rolling(504, min_periods=126).sum() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ncfo traj exp count
def f23cft_f23_cash_flow_trajectory_ncfotrajexpcount_252d_slope_v138_signal(ncfo, closeadj):
    flag = (_f23_cashflow_traj(ncfo, 63) > 0.02).astype(float)
    base = flag.rolling(252, min_periods=63).sum() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF growth × vol
def f23cft_f23_cash_flow_trajectory_fcfgrowthxvol_252d_slope_v139_signal(fcf, closeadj):
    g = _f23_fcf_growth(fcf, 252)
    sd = _std(_f23_fcf_growth(fcf, 63), 252)
    base = g * sd * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ncfo traj × vol
def f23cft_f23_cash_flow_trajectory_ncfotrajxvol_63d_slope_v140_signal(ncfo, closeadj):
    g = _f23_cashflow_traj(ncfo, 63)
    sd = _std(_f23_cashflow_traj(ncfo, 21), 63)
    base = g * sd * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d composite score
def f23cft_f23_cash_flow_trajectory_compositescore_252d_slope_v141_signal(fcf, ncfo, closeadj):
    a = _f23_fcf_growth(fcf, 252)
    b = _f23_cashflow_traj(ncfo, 252)
    c = _f23_fcf_acceleration(fcf, 252)
    base = (a + b + c) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d FCF growth × sales/price
def f23cft_f23_cash_flow_trajectory_fcfgrowthxsales_63d_slope_v142_signal(fcf, revenue, closeadj):
    base = _f23_fcf_growth(fcf, 63) * (revenue / closeadj.replace(0, np.nan))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF growth × ni × close
def f23cft_f23_cash_flow_trajectory_fcfgrowthxni_252d_slope_v143_signal(fcf, netinc, closeadj):
    base = _f23_fcf_growth(fcf, 252) * netinc * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ncfo traj × ni × close
def f23cft_f23_cash_flow_trajectory_ncfotrajxnini_21d_slope_v144_signal(ncfo, netinc, closeadj):
    base = _f23_cashflow_traj(ncfo, 21) * netinc * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of expanding mean FCF growth × close
def f23cft_f23_cash_flow_trajectory_fcfgrowthexp_252d_slope_v145_signal(fcf, closeadj):
    g = _f23_fcf_growth(fcf, 252)
    base = g.expanding(min_periods=63).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of expanding mean ncfo traj × close
def f23cft_f23_cash_flow_trajectory_ncfotrajexp_252d_slope_v146_signal(ncfo, closeadj):
    g = _f23_cashflow_traj(ncfo, 252)
    base = g.expanding(min_periods=63).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF growth × net (assets - debt)
def f23cft_f23_cash_flow_trajectory_fcfgrowthxnet_252d_slope_v147_signal(fcf, assets, debt, closeadj):
    base = _f23_fcf_growth(fcf, 252) * (assets - debt)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ncfo traj × (rev - capex)
def f23cft_f23_cash_flow_trajectory_ncfotrajxrevcapex_63d_slope_v148_signal(ncfo, revenue, capex, closeadj):
    base = _f23_cashflow_traj(ncfo, 63) * (revenue - capex.abs())
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF growth × (gp - opinc) × close
def f23cft_f23_cash_flow_trajectory_fcfgrowthxgpopgap_252d_slope_v149_signal(fcf, gp, opinc, closeadj):
    base = _f23_fcf_growth(fcf, 252) * (gp - opinc) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d composite trajectory
def f23cft_f23_cash_flow_trajectory_compositetraj_252d_slope_v150_signal(fcf, ncfo, revenue, closeadj):
    base = (_f23_fcf_growth(fcf, 252) + _f23_cashflow_traj(ncfo, 252)) * revenue * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f23cft_f23_cash_flow_trajectory_fcfgrowth_21d_slope_v001_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowth_21d_slope_v002_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowth_63d_slope_v003_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowth_63d_slope_v004_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowth_63d_slope_v005_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowth_126d_slope_v006_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowth_126d_slope_v007_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowth_252d_slope_v008_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowth_252d_slope_v009_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowth_504d_slope_v010_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowth_504d_slope_v011_signal,
    f23cft_f23_cash_flow_trajectory_ncfotraj_21d_slope_v012_signal,
    f23cft_f23_cash_flow_trajectory_ncfotraj_63d_slope_v013_signal,
    f23cft_f23_cash_flow_trajectory_ncfotraj_126d_slope_v014_signal,
    f23cft_f23_cash_flow_trajectory_ncfotraj_252d_slope_v015_signal,
    f23cft_f23_cash_flow_trajectory_ncfotraj_504d_slope_v016_signal,
    f23cft_f23_cash_flow_trajectory_fcfaccel_21d_slope_v017_signal,
    f23cft_f23_cash_flow_trajectory_fcfaccel_63d_slope_v018_signal,
    f23cft_f23_cash_flow_trajectory_fcfaccel_252d_slope_v019_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthmean_63d_slope_v020_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthmean_252d_slope_v021_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthstd_63d_slope_v022_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthstd_252d_slope_v023_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthz_252d_slope_v024_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthz_504d_slope_v025_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajz_252d_slope_v026_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajz_504d_slope_v027_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthposcount_252d_slope_v028_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthposcount_504d_slope_v029_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajnegcount_252d_slope_v030_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthsq_21d_slope_v031_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthsq_63d_slope_v032_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthsq_252d_slope_v033_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajxrev_21d_slope_v034_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajxrev_63d_slope_v035_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxrev_252d_slope_v036_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajdiff_21m63_slope_v037_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthdiff_63m252_slope_v038_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthdiff_252m504_slope_v039_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthratio_63v252_slope_v040_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajratio_21v63_slope_v041_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthprod_63x252_slope_v042_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxncfo_21d_slope_v043_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxncfo_252d_slope_v044_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxebitda_21d_slope_v045_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxebitda_63d_slope_v046_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxebitda_252d_slope_v047_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajxnetinc_63d_slope_v048_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajxnetinc_252d_slope_v049_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthmax_63d_slope_v050_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthmax_252d_slope_v051_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthsum_63d_slope_v052_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthsum_252d_slope_v053_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajsum_252d_slope_v054_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxcapex_63d_slope_v055_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxcapex_252d_slope_v056_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajxcapex_63d_slope_v057_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxncff_21d_slope_v058_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxncff_252d_slope_v059_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthema_63d_slope_v060_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthema_252d_slope_v061_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajema_63d_slope_v062_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajema_252d_slope_v063_signal,
    f23cft_f23_cash_flow_trajectory_fcfaccelxebitda_21d_slope_v064_signal,
    f23cft_f23_cash_flow_trajectory_fcfaccelxebitda_63d_slope_v065_signal,
    f23cft_f23_cash_flow_trajectory_fcfaccelxrev_252d_slope_v066_signal,
    f23cft_f23_cash_flow_trajectory_fcfaccelz_252d_slope_v067_signal,
    f23cft_f23_cash_flow_trajectory_fcfaccelz_504d_slope_v068_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowth_5d_slope_v069_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowth_10d_slope_v070_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowth_42d_slope_v071_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowth_189d_slope_v072_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowth_378d_slope_v073_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowtharea_252d_slope_v074_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowtharea_504d_slope_v075_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxmcap_252d_slope_v076_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxmcap_63d_slope_v077_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxequity_21d_slope_v078_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxequity_252d_slope_v079_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxassets_252d_slope_v080_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxdebt_252d_slope_v081_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajxdebt_63d_slope_v082_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxgp_252d_slope_v083_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxgp_63d_slope_v084_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxopinc_252d_slope_v085_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxopinc_63d_slope_v086_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxeps_252d_slope_v087_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajxeps_63d_slope_v088_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxwc_252d_slope_v089_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajxwc_63d_slope_v090_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxcr_21d_slope_v091_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxcr_252d_slope_v092_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajxcr_252d_slope_v093_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxliab_63d_slope_v094_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxliab_252d_slope_v095_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajxre_63d_slope_v096_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxre_252d_slope_v097_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajxintexp_63d_slope_v098_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxintexp_252d_slope_v099_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxtax_252d_slope_v100_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajsq_21d_slope_v101_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajsq_252d_slope_v102_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajarea_63d_slope_v103_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajarea_252d_slope_v104_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajarea_504d_slope_v105_signal,
    f23cft_f23_cash_flow_trajectory_fcfminusncfo_252d_slope_v106_signal,
    f23cft_f23_cash_flow_trajectory_fcfminusncfo_63d_slope_v107_signal,
    f23cft_f23_cash_flow_trajectory_fcfplusncfo_252d_slope_v108_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthworst_504d_slope_v109_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthbest_504d_slope_v110_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajmax_63d_slope_v111_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajmax_252d_slope_v112_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajmin_63d_slope_v113_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajmin_252d_slope_v114_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthemaebitda_21d_slope_v115_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthemaebitda_252d_slope_v116_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthareaxmcap_252d_slope_v117_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajanom_63d_slope_v118_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajanom_252d_slope_v119_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthanom_63d_slope_v120_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthanom_252d_slope_v121_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxrevxprice_21d_slope_v122_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxrevxprice_252d_slope_v123_signal,
    f23cft_f23_cash_flow_trajectory_fcfaccelxmcap_252d_slope_v124_signal,
    f23cft_f23_cash_flow_trajectory_fcfaccelxmcap_63d_slope_v125_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxncfolvl_21d_slope_v126_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxncfolvl_252d_slope_v127_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajxebitdaprice_252d_slope_v128_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxebitdaprice_252d_slope_v129_signal,
    f23cft_f23_cash_flow_trajectory_fcfgapxebitda_252d_slope_v130_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajxnet_252d_slope_v131_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthema_21d_slope_v132_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajema_21d_slope_v133_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthrank_252d_slope_v134_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajrank_252d_slope_v135_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthhighcount_252d_slope_v136_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthlowcount_504d_slope_v137_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajexpcount_252d_slope_v138_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxvol_252d_slope_v139_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajxvol_63d_slope_v140_signal,
    f23cft_f23_cash_flow_trajectory_compositescore_252d_slope_v141_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxsales_63d_slope_v142_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxni_252d_slope_v143_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajxnini_21d_slope_v144_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthexp_252d_slope_v145_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajexp_252d_slope_v146_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxnet_252d_slope_v147_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajxrevcapex_63d_slope_v148_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxgpopgap_252d_slope_v149_signal,
    f23cft_f23_cash_flow_trajectory_compositetraj_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F23_CASH_FLOW_TRAJECTORY_REGISTRY_SLOPE = REGISTRY


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
    domain_primitives = ("_f23_cashflow_traj", "_f23_fcf_growth", "_f23_fcf_acceleration")
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
    print(f"OK f23_cash_flow_trajectory_2nd_derivatives_001_150_claude: {n_features} features pass")
