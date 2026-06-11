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
def _f23_cashflow_traj(s, w):
    return s.diff(periods=w) / s.abs().rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)


def _f23_fcf_growth(fcf, w):
    base = fcf.rolling(w, min_periods=max(1, w // 2)).mean()
    return base.diff(periods=w) / base.abs().shift(w).replace(0, np.nan)


def _f23_fcf_acceleration(fcf, w):
    g1 = _f23_fcf_growth(fcf, w)
    return g1.diff(periods=w)


# 21d FCF growth scaled by closeadj
def f23cft_f23_cash_flow_trajectory_fcfgrowth_21d_base_v001_signal(fcf, closeadj):
    result = _f23_fcf_growth(fcf, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF growth scaled by closeadj
def f23cft_f23_cash_flow_trajectory_fcfgrowth_63d_base_v002_signal(fcf, closeadj):
    result = _f23_fcf_growth(fcf, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d FCF growth scaled by closeadj
def f23cft_f23_cash_flow_trajectory_fcfgrowth_126d_base_v003_signal(fcf, closeadj):
    result = _f23_fcf_growth(fcf, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF growth scaled by closeadj
def f23cft_f23_cash_flow_trajectory_fcfgrowth_252d_base_v004_signal(fcf, closeadj):
    result = _f23_fcf_growth(fcf, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d FCF growth scaled by closeadj
def f23cft_f23_cash_flow_trajectory_fcfgrowth_504d_base_v005_signal(fcf, closeadj):
    result = _f23_fcf_growth(fcf, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ncfo cash flow trajectory
def f23cft_f23_cash_flow_trajectory_ncfotraj_21d_base_v006_signal(ncfo, closeadj):
    result = _f23_cashflow_traj(ncfo, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo cash flow trajectory
def f23cft_f23_cash_flow_trajectory_ncfotraj_63d_base_v007_signal(ncfo, closeadj):
    result = _f23_cashflow_traj(ncfo, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ncfo cash flow trajectory
def f23cft_f23_cash_flow_trajectory_ncfotraj_126d_base_v008_signal(ncfo, closeadj):
    result = _f23_cashflow_traj(ncfo, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo cash flow trajectory
def f23cft_f23_cash_flow_trajectory_ncfotraj_252d_base_v009_signal(ncfo, closeadj):
    result = _f23_cashflow_traj(ncfo, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncfo cash flow trajectory
def f23cft_f23_cash_flow_trajectory_ncfotraj_504d_base_v010_signal(ncfo, closeadj):
    result = _f23_cashflow_traj(ncfo, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF acceleration scaled by closeadj
def f23cft_f23_cash_flow_trajectory_fcfaccel_21d_base_v011_signal(fcf, closeadj):
    result = _f23_fcf_acceleration(fcf, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF acceleration scaled by closeadj
def f23cft_f23_cash_flow_trajectory_fcfaccel_63d_base_v012_signal(fcf, closeadj):
    result = _f23_fcf_acceleration(fcf, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d FCF acceleration scaled by closeadj
def f23cft_f23_cash_flow_trajectory_fcfaccel_126d_base_v013_signal(fcf, closeadj):
    result = _f23_fcf_acceleration(fcf, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF acceleration scaled by closeadj
def f23cft_f23_cash_flow_trajectory_fcfaccel_252d_base_v014_signal(fcf, closeadj):
    result = _f23_fcf_acceleration(fcf, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 63d mean FCF growth times closeadj
def f23cft_f23_cash_flow_trajectory_fcfgrowthmean_63d_base_v015_signal(fcf, closeadj):
    result = _mean(_f23_fcf_growth(fcf, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 252d mean FCF growth times closeadj
def f23cft_f23_cash_flow_trajectory_fcfgrowthmean_252d_base_v016_signal(fcf, closeadj):
    result = _mean(_f23_fcf_growth(fcf, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 63d std FCF growth times closeadj
def f23cft_f23_cash_flow_trajectory_fcfgrowthstd_63d_base_v017_signal(fcf, closeadj):
    result = _std(_f23_fcf_growth(fcf, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 252d std FCF growth times closeadj
def f23cft_f23_cash_flow_trajectory_fcfgrowthstd_252d_base_v018_signal(fcf, closeadj):
    result = _std(_f23_fcf_growth(fcf, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of FCF growth
def f23cft_f23_cash_flow_trajectory_fcfgrowthz_252d_base_v019_signal(fcf, closeadj):
    result = _z(_f23_fcf_growth(fcf, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of FCF growth
def f23cft_f23_cash_flow_trajectory_fcfgrowthz_504d_base_v020_signal(fcf, closeadj):
    result = _z(_f23_fcf_growth(fcf, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of ncfo trajectory
def f23cft_f23_cash_flow_trajectory_ncfotrajz_252d_base_v021_signal(ncfo, closeadj):
    result = _z(_f23_cashflow_traj(ncfo, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of ncfo trajectory
def f23cft_f23_cash_flow_trajectory_ncfotrajz_504d_base_v022_signal(ncfo, closeadj):
    result = _z(_f23_cashflow_traj(ncfo, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of positive 63d FCF growth periods
def f23cft_f23_cash_flow_trajectory_fcfgrowthposcount_252d_base_v023_signal(fcf, closeadj):
    flag = (_f23_fcf_growth(fcf, 63) > 0).astype(float)
    result = flag.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of positive 252d FCF growth periods
def f23cft_f23_cash_flow_trajectory_fcfgrowthposcount_504d_base_v024_signal(fcf, closeadj):
    flag = (_f23_fcf_growth(fcf, 252) > 0).astype(float)
    result = flag.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of negative 63d ncfo trajectory periods
def f23cft_f23_cash_flow_trajectory_ncfotrajnegcount_252d_base_v025_signal(ncfo, closeadj):
    flag = (_f23_cashflow_traj(ncfo, 63) < 0).astype(float)
    result = flag.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF growth squared scaled by closeadj
def f23cft_f23_cash_flow_trajectory_fcfgrowthsq_21d_base_v026_signal(fcf, closeadj):
    g = _f23_fcf_growth(fcf, 21)
    result = g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF growth squared scaled by closeadj
def f23cft_f23_cash_flow_trajectory_fcfgrowthsq_63d_base_v027_signal(fcf, closeadj):
    g = _f23_fcf_growth(fcf, 63)
    result = g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF growth squared scaled by closeadj
def f23cft_f23_cash_flow_trajectory_fcfgrowthsq_252d_base_v028_signal(fcf, closeadj):
    g = _f23_fcf_growth(fcf, 252)
    result = g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ncfo trajectory weighted by current revenue
def f23cft_f23_cash_flow_trajectory_ncfotrajxrev_21d_base_v029_signal(ncfo, revenue, closeadj):
    result = _f23_cashflow_traj(ncfo, 21) * revenue
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo trajectory weighted by current revenue
def f23cft_f23_cash_flow_trajectory_ncfotrajxrev_63d_base_v030_signal(ncfo, revenue, closeadj):
    result = _f23_cashflow_traj(ncfo, 63) * revenue
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF growth weighted by current revenue
def f23cft_f23_cash_flow_trajectory_fcfgrowthxrev_252d_base_v031_signal(fcf, revenue, closeadj):
    result = _f23_fcf_growth(fcf, 252) * revenue
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ncfo trajectory minus 63d (cash flow short vs long)
def f23cft_f23_cash_flow_trajectory_ncfotrajdiff_21m63_base_v032_signal(ncfo, closeadj):
    result = (_f23_cashflow_traj(ncfo, 21) - _f23_cashflow_traj(ncfo, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF growth minus 252d FCF growth
def f23cft_f23_cash_flow_trajectory_fcfgrowthdiff_63m252_base_v033_signal(fcf, closeadj):
    result = (_f23_fcf_growth(fcf, 63) - _f23_fcf_growth(fcf, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF growth minus 504d FCF growth
def f23cft_f23_cash_flow_trajectory_fcfgrowthdiff_252m504_base_v034_signal(fcf, closeadj):
    result = (_f23_fcf_growth(fcf, 252) - _f23_fcf_growth(fcf, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF growth divided by 252d FCF growth
def f23cft_f23_cash_flow_trajectory_fcfgrowthratio_63v252_base_v035_signal(fcf, closeadj):
    a = _f23_fcf_growth(fcf, 63)
    b = _f23_fcf_growth(fcf, 252).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ncfo trajectory divided by 63d ncfo trajectory
def f23cft_f23_cash_flow_trajectory_ncfotrajratio_21v63_base_v036_signal(ncfo, closeadj):
    a = _f23_cashflow_traj(ncfo, 21)
    b = _f23_cashflow_traj(ncfo, 63).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF growth × 252d FCF growth (composite trend)
def f23cft_f23_cash_flow_trajectory_fcfgrowthprod_63x252_base_v037_signal(fcf, closeadj):
    result = _f23_fcf_growth(fcf, 63) * _f23_fcf_growth(fcf, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF growth × 63d ncfo trajectory
def f23cft_f23_cash_flow_trajectory_fcfgrowthxncfo_21d_base_v038_signal(fcf, ncfo, closeadj):
    result = _f23_fcf_growth(fcf, 21) * _f23_cashflow_traj(ncfo, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF growth × 252d ncfo trajectory
def f23cft_f23_cash_flow_trajectory_fcfgrowthxncfo_252d_base_v039_signal(fcf, ncfo, closeadj):
    result = _f23_fcf_growth(fcf, 252) * _f23_cashflow_traj(ncfo, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF growth weighted by ebitda
def f23cft_f23_cash_flow_trajectory_fcfgrowthxebitda_21d_base_v040_signal(fcf, ebitda, closeadj):
    result = _f23_fcf_growth(fcf, 21) * ebitda
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF growth weighted by ebitda
def f23cft_f23_cash_flow_trajectory_fcfgrowthxebitda_63d_base_v041_signal(fcf, ebitda, closeadj):
    result = _f23_fcf_growth(fcf, 63) * ebitda
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF growth weighted by ebitda
def f23cft_f23_cash_flow_trajectory_fcfgrowthxebitda_252d_base_v042_signal(fcf, ebitda, closeadj):
    result = _f23_fcf_growth(fcf, 252) * ebitda
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo trajectory weighted by netinc
def f23cft_f23_cash_flow_trajectory_ncfotrajxnetinc_63d_base_v043_signal(ncfo, netinc, closeadj):
    result = _f23_cashflow_traj(ncfo, 63) * netinc
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo trajectory weighted by netinc
def f23cft_f23_cash_flow_trajectory_ncfotrajxnetinc_252d_base_v044_signal(ncfo, netinc, closeadj):
    result = _f23_cashflow_traj(ncfo, 252) * netinc
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 21d max FCF growth in 63d window
def f23cft_f23_cash_flow_trajectory_fcfgrowthmax_63d_base_v045_signal(fcf, closeadj):
    result = _f23_fcf_growth(fcf, 21).rolling(63, min_periods=21).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 63d max FCF growth in 252d window
def f23cft_f23_cash_flow_trajectory_fcfgrowthmax_252d_base_v046_signal(fcf, closeadj):
    result = _f23_fcf_growth(fcf, 63).rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 63d sum of 21d FCF growth (cumulative trajectory)
def f23cft_f23_cash_flow_trajectory_fcfgrowthsum_63d_base_v047_signal(fcf, closeadj):
    result = _f23_fcf_growth(fcf, 21).rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 252d sum of 63d FCF growth
def f23cft_f23_cash_flow_trajectory_fcfgrowthsum_252d_base_v048_signal(fcf, closeadj):
    result = _f23_fcf_growth(fcf, 63).rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 252d sum of 21d ncfo trajectory
def f23cft_f23_cash_flow_trajectory_ncfotrajsum_252d_base_v049_signal(ncfo, closeadj):
    result = _f23_cashflow_traj(ncfo, 21).rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF growth weighted by absolute capex (investment intensity)
def f23cft_f23_cash_flow_trajectory_fcfgrowthxcapex_63d_base_v050_signal(fcf, capex, closeadj):
    result = _f23_fcf_growth(fcf, 63) * capex.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF growth weighted by absolute capex
def f23cft_f23_cash_flow_trajectory_fcfgrowthxcapex_252d_base_v051_signal(fcf, capex, closeadj):
    result = _f23_fcf_growth(fcf, 252) * capex.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo trajectory weighted by capex (operating vs invest)
def f23cft_f23_cash_flow_trajectory_ncfotrajxcapex_63d_base_v052_signal(ncfo, capex, closeadj):
    result = _f23_cashflow_traj(ncfo, 63) * capex.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF growth weighted by ncff (financing flow context)
def f23cft_f23_cash_flow_trajectory_fcfgrowthxncff_21d_base_v053_signal(fcf, ncff, closeadj):
    result = _f23_fcf_growth(fcf, 21) * ncff.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF growth weighted by ncff
def f23cft_f23_cash_flow_trajectory_fcfgrowthxncff_252d_base_v054_signal(fcf, ncff, closeadj):
    result = _f23_fcf_growth(fcf, 252) * ncff.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of FCF growth scaled by closeadj
def f23cft_f23_cash_flow_trajectory_fcfgrowthema_63d_base_v055_signal(fcf, closeadj):
    g = _f23_fcf_growth(fcf, 63)
    result = g.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of FCF growth scaled by closeadj
def f23cft_f23_cash_flow_trajectory_fcfgrowthema_252d_base_v056_signal(fcf, closeadj):
    g = _f23_fcf_growth(fcf, 252)
    result = g.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of ncfo trajectory scaled by closeadj
def f23cft_f23_cash_flow_trajectory_ncfotrajema_63d_base_v057_signal(ncfo, closeadj):
    g = _f23_cashflow_traj(ncfo, 63)
    result = g.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of ncfo trajectory scaled by closeadj
def f23cft_f23_cash_flow_trajectory_ncfotrajema_252d_base_v058_signal(ncfo, closeadj):
    g = _f23_cashflow_traj(ncfo, 252)
    result = g.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF acceleration scaled by ebitda
def f23cft_f23_cash_flow_trajectory_fcfaccelxebitda_21d_base_v059_signal(fcf, ebitda, closeadj):
    result = _f23_fcf_acceleration(fcf, 21) * ebitda
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF acceleration scaled by ebitda
def f23cft_f23_cash_flow_trajectory_fcfaccelxebitda_63d_base_v060_signal(fcf, ebitda, closeadj):
    result = _f23_fcf_acceleration(fcf, 63) * ebitda
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF acceleration scaled by revenue
def f23cft_f23_cash_flow_trajectory_fcfaccelxrev_252d_base_v061_signal(fcf, revenue, closeadj):
    result = _f23_fcf_acceleration(fcf, 252) * revenue
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of FCF acceleration
def f23cft_f23_cash_flow_trajectory_fcfaccelz_252d_base_v062_signal(fcf, closeadj):
    result = _z(_f23_fcf_acceleration(fcf, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of FCF acceleration
def f23cft_f23_cash_flow_trajectory_fcfaccelz_504d_base_v063_signal(fcf, closeadj):
    result = _z(_f23_fcf_acceleration(fcf, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d FCF growth scaled by closeadj (intraweek)
def f23cft_f23_cash_flow_trajectory_fcfgrowth_5d_base_v064_signal(fcf, closeadj):
    result = _f23_fcf_growth(fcf, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d FCF growth scaled by closeadj
def f23cft_f23_cash_flow_trajectory_fcfgrowth_10d_base_v065_signal(fcf, closeadj):
    result = _f23_fcf_growth(fcf, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d FCF growth (~2 month)
def f23cft_f23_cash_flow_trajectory_fcfgrowth_42d_base_v066_signal(fcf, closeadj):
    result = _f23_fcf_growth(fcf, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d FCF growth (~9mo)
def f23cft_f23_cash_flow_trajectory_fcfgrowth_189d_base_v067_signal(fcf, closeadj):
    result = _f23_fcf_growth(fcf, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d FCF growth (~1.5y)
def f23cft_f23_cash_flow_trajectory_fcfgrowth_378d_base_v068_signal(fcf, closeadj):
    result = _f23_fcf_growth(fcf, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF growth area (sum of magnitude over window)
def f23cft_f23_cash_flow_trajectory_fcfgrowtharea_252d_base_v069_signal(fcf, closeadj):
    g = _f23_fcf_growth(fcf, 63).abs()
    result = g.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d FCF growth area
def f23cft_f23_cash_flow_trajectory_fcfgrowtharea_504d_base_v070_signal(fcf, closeadj):
    g = _f23_fcf_growth(fcf, 252).abs()
    result = g.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF growth × current marketcap proxy (closeadj × sharesbas)
def f23cft_f23_cash_flow_trajectory_fcfgrowthxmcap_252d_base_v071_signal(fcf, closeadj, sharesbas):
    result = _f23_fcf_growth(fcf, 252) * (closeadj * sharesbas)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF growth × current marketcap proxy
def f23cft_f23_cash_flow_trajectory_fcfgrowthxmcap_63d_base_v072_signal(fcf, closeadj, sharesbas):
    result = _f23_fcf_growth(fcf, 63) * (closeadj * sharesbas)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF growth times equity (capital trajectory)
def f23cft_f23_cash_flow_trajectory_fcfgrowthxequity_21d_base_v073_signal(fcf, equity, closeadj):
    result = _f23_fcf_growth(fcf, 21) * equity
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF growth times equity
def f23cft_f23_cash_flow_trajectory_fcfgrowthxequity_252d_base_v074_signal(fcf, equity, closeadj):
    result = _f23_fcf_growth(fcf, 252) * equity
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF growth scaled by current assets
def f23cft_f23_cash_flow_trajectory_fcfgrowthxassets_252d_base_v075_signal(fcf, assets, closeadj):
    result = _f23_fcf_growth(fcf, 252) * assets
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f23cft_f23_cash_flow_trajectory_fcfgrowth_21d_base_v001_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowth_63d_base_v002_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowth_126d_base_v003_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowth_252d_base_v004_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowth_504d_base_v005_signal,
    f23cft_f23_cash_flow_trajectory_ncfotraj_21d_base_v006_signal,
    f23cft_f23_cash_flow_trajectory_ncfotraj_63d_base_v007_signal,
    f23cft_f23_cash_flow_trajectory_ncfotraj_126d_base_v008_signal,
    f23cft_f23_cash_flow_trajectory_ncfotraj_252d_base_v009_signal,
    f23cft_f23_cash_flow_trajectory_ncfotraj_504d_base_v010_signal,
    f23cft_f23_cash_flow_trajectory_fcfaccel_21d_base_v011_signal,
    f23cft_f23_cash_flow_trajectory_fcfaccel_63d_base_v012_signal,
    f23cft_f23_cash_flow_trajectory_fcfaccel_126d_base_v013_signal,
    f23cft_f23_cash_flow_trajectory_fcfaccel_252d_base_v014_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthmean_63d_base_v015_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthmean_252d_base_v016_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthstd_63d_base_v017_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthstd_252d_base_v018_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthz_252d_base_v019_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthz_504d_base_v020_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajz_252d_base_v021_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajz_504d_base_v022_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthposcount_252d_base_v023_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthposcount_504d_base_v024_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajnegcount_252d_base_v025_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthsq_21d_base_v026_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthsq_63d_base_v027_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthsq_252d_base_v028_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajxrev_21d_base_v029_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajxrev_63d_base_v030_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxrev_252d_base_v031_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajdiff_21m63_base_v032_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthdiff_63m252_base_v033_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthdiff_252m504_base_v034_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthratio_63v252_base_v035_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajratio_21v63_base_v036_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthprod_63x252_base_v037_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxncfo_21d_base_v038_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxncfo_252d_base_v039_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxebitda_21d_base_v040_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxebitda_63d_base_v041_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxebitda_252d_base_v042_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajxnetinc_63d_base_v043_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajxnetinc_252d_base_v044_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthmax_63d_base_v045_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthmax_252d_base_v046_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthsum_63d_base_v047_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthsum_252d_base_v048_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajsum_252d_base_v049_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxcapex_63d_base_v050_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxcapex_252d_base_v051_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajxcapex_63d_base_v052_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxncff_21d_base_v053_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxncff_252d_base_v054_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthema_63d_base_v055_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthema_252d_base_v056_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajema_63d_base_v057_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajema_252d_base_v058_signal,
    f23cft_f23_cash_flow_trajectory_fcfaccelxebitda_21d_base_v059_signal,
    f23cft_f23_cash_flow_trajectory_fcfaccelxebitda_63d_base_v060_signal,
    f23cft_f23_cash_flow_trajectory_fcfaccelxrev_252d_base_v061_signal,
    f23cft_f23_cash_flow_trajectory_fcfaccelz_252d_base_v062_signal,
    f23cft_f23_cash_flow_trajectory_fcfaccelz_504d_base_v063_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowth_5d_base_v064_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowth_10d_base_v065_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowth_42d_base_v066_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowth_189d_base_v067_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowth_378d_base_v068_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowtharea_252d_base_v069_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowtharea_504d_base_v070_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxmcap_252d_base_v071_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxmcap_63d_base_v072_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxequity_21d_base_v073_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxequity_252d_base_v074_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxassets_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F23_CASH_FLOW_TRAJECTORY_REGISTRY_001_075 = REGISTRY


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
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.003, n))), name="assets")
    ebitda = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.006, n))), name="ebitda")
    capex = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="capex")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.002, n))), name="sharesbas")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "ncff": ncff, "equity": equity, "assets": assets,
        "ebitda": ebitda, "capex": capex, "sharesbas": sharesbas,
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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f23_cash_flow_trajectory_base_001_075_claude: {n_features} features pass")
