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


def _accel(s, w):
    return s.diff(periods=w).diff(periods=w)


# ===== folder domain primitives =====
def _f073_pe(close, eps):
    return close / eps.replace(0, np.nan).abs()


# 21d slope of pe_lvl
def f073erm_f073_earnings_multiples_pe_lvl_slope_21d_2d_v001_signal(pe, closeadj):
    base = pe
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of pe_lvl
def f073erm_f073_earnings_multiples_pe_lvl_slope_63d_2d_v002_signal(pe, closeadj):
    base = pe
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of pe_lvl
def f073erm_f073_earnings_multiples_pe_lvl_slope_126d_2d_v003_signal(pe, closeadj):
    base = pe
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of pe_lvl
def f073erm_f073_earnings_multiples_pe_lvl_slope_252d_2d_v004_signal(pe, closeadj):
    base = pe
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of pe_lvl
def f073erm_f073_earnings_multiples_pe_lvl_slope_504d_2d_v005_signal(pe, closeadj):
    base = pe
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of pe1_lvl
def f073erm_f073_earnings_multiples_pe1_lvl_slope_21d_2d_v006_signal(pe1, closeadj):
    base = pe1
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of pe1_lvl
def f073erm_f073_earnings_multiples_pe1_lvl_slope_63d_2d_v007_signal(pe1, closeadj):
    base = pe1
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of pe1_lvl
def f073erm_f073_earnings_multiples_pe1_lvl_slope_126d_2d_v008_signal(pe1, closeadj):
    base = pe1
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of pe1_lvl
def f073erm_f073_earnings_multiples_pe1_lvl_slope_252d_2d_v009_signal(pe1, closeadj):
    base = pe1
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of pe1_lvl
def f073erm_f073_earnings_multiples_pe1_lvl_slope_504d_2d_v010_signal(pe1, closeadj):
    base = pe1
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of evebit_lvl
def f073erm_f073_earnings_multiples_evebit_lvl_slope_21d_2d_v011_signal(evebit, closeadj):
    base = evebit
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of evebit_lvl
def f073erm_f073_earnings_multiples_evebit_lvl_slope_63d_2d_v012_signal(evebit, closeadj):
    base = evebit
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of evebit_lvl
def f073erm_f073_earnings_multiples_evebit_lvl_slope_126d_2d_v013_signal(evebit, closeadj):
    base = evebit
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of evebit_lvl
def f073erm_f073_earnings_multiples_evebit_lvl_slope_252d_2d_v014_signal(evebit, closeadj):
    base = evebit
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of evebit_lvl
def f073erm_f073_earnings_multiples_evebit_lvl_slope_504d_2d_v015_signal(evebit, closeadj):
    base = evebit
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of evebitda_lvl
def f073erm_f073_earnings_multiples_evebitda_lvl_slope_21d_2d_v016_signal(evebitda, closeadj):
    base = evebitda
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of evebitda_lvl
def f073erm_f073_earnings_multiples_evebitda_lvl_slope_63d_2d_v017_signal(evebitda, closeadj):
    base = evebitda
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of evebitda_lvl
def f073erm_f073_earnings_multiples_evebitda_lvl_slope_126d_2d_v018_signal(evebitda, closeadj):
    base = evebitda
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of evebitda_lvl
def f073erm_f073_earnings_multiples_evebitda_lvl_slope_252d_2d_v019_signal(evebitda, closeadj):
    base = evebitda
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of evebitda_lvl
def f073erm_f073_earnings_multiples_evebitda_lvl_slope_504d_2d_v020_signal(evebitda, closeadj):
    base = evebitda
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of earn_yield
def f073erm_f073_earnings_multiples_earn_yield_slope_21d_2d_v021_signal(eps, close, closeadj):
    base = eps / close.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of earn_yield
def f073erm_f073_earnings_multiples_earn_yield_slope_63d_2d_v022_signal(eps, close, closeadj):
    base = eps / close.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of earn_yield
def f073erm_f073_earnings_multiples_earn_yield_slope_126d_2d_v023_signal(eps, close, closeadj):
    base = eps / close.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of earn_yield
def f073erm_f073_earnings_multiples_earn_yield_slope_252d_2d_v024_signal(eps, close, closeadj):
    base = eps / close.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of earn_yield
def f073erm_f073_earnings_multiples_earn_yield_slope_504d_2d_v025_signal(eps, close, closeadj):
    base = eps / close.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of pe_calc
def f073erm_f073_earnings_multiples_pe_calc_slope_21d_2d_v026_signal(close, eps, closeadj):
    base = _f073_pe(close, eps)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of pe_calc
def f073erm_f073_earnings_multiples_pe_calc_slope_63d_2d_v027_signal(close, eps, closeadj):
    base = _f073_pe(close, eps)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of pe_calc
def f073erm_f073_earnings_multiples_pe_calc_slope_126d_2d_v028_signal(close, eps, closeadj):
    base = _f073_pe(close, eps)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of pe_calc
def f073erm_f073_earnings_multiples_pe_calc_slope_252d_2d_v029_signal(close, eps, closeadj):
    base = _f073_pe(close, eps)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of pe_calc
def f073erm_f073_earnings_multiples_pe_calc_slope_504d_2d_v030_signal(close, eps, closeadj):
    base = _f073_pe(close, eps)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ebit_yield
def f073erm_f073_earnings_multiples_ebit_yield_slope_21d_2d_v031_signal(ebit, ev, closeadj):
    base = ebit / ev.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ebit_yield
def f073erm_f073_earnings_multiples_ebit_yield_slope_63d_2d_v032_signal(ebit, ev, closeadj):
    base = ebit / ev.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ebit_yield
def f073erm_f073_earnings_multiples_ebit_yield_slope_126d_2d_v033_signal(ebit, ev, closeadj):
    base = ebit / ev.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ebit_yield
def f073erm_f073_earnings_multiples_ebit_yield_slope_252d_2d_v034_signal(ebit, ev, closeadj):
    base = ebit / ev.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ebit_yield
def f073erm_f073_earnings_multiples_ebit_yield_slope_504d_2d_v035_signal(ebit, ev, closeadj):
    base = ebit / ev.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of pe_peer_sector_dist
def f073erm_f073_earnings_multiples_pe_peer_sector_dist_slope_21d_2d_v036_signal(pe, pe_sector_med, closeadj):
    base = (pe - pe_sector_med) / pe_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of pe_peer_sector_dist
def f073erm_f073_earnings_multiples_pe_peer_sector_dist_slope_63d_2d_v037_signal(pe, pe_sector_med, closeadj):
    base = (pe - pe_sector_med) / pe_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of pe_peer_sector_dist
def f073erm_f073_earnings_multiples_pe_peer_sector_dist_slope_126d_2d_v038_signal(pe, pe_sector_med, closeadj):
    base = (pe - pe_sector_med) / pe_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of pe_peer_sector_dist
def f073erm_f073_earnings_multiples_pe_peer_sector_dist_slope_252d_2d_v039_signal(pe, pe_sector_med, closeadj):
    base = (pe - pe_sector_med) / pe_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of pe_peer_sector_dist
def f073erm_f073_earnings_multiples_pe_peer_sector_dist_slope_504d_2d_v040_signal(pe, pe_sector_med, closeadj):
    base = (pe - pe_sector_med) / pe_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of pe_peer_sector_z
def f073erm_f073_earnings_multiples_pe_peer_sector_z_slope_21d_2d_v041_signal(pe, pe_sector_med, pe_sector_std, closeadj):
    base = (pe - pe_sector_med) / pe_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of pe_peer_sector_z
def f073erm_f073_earnings_multiples_pe_peer_sector_z_slope_63d_2d_v042_signal(pe, pe_sector_med, pe_sector_std, closeadj):
    base = (pe - pe_sector_med) / pe_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of pe_peer_sector_z
def f073erm_f073_earnings_multiples_pe_peer_sector_z_slope_126d_2d_v043_signal(pe, pe_sector_med, pe_sector_std, closeadj):
    base = (pe - pe_sector_med) / pe_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of pe_peer_sector_z
def f073erm_f073_earnings_multiples_pe_peer_sector_z_slope_252d_2d_v044_signal(pe, pe_sector_med, pe_sector_std, closeadj):
    base = (pe - pe_sector_med) / pe_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of pe_peer_sector_z
def f073erm_f073_earnings_multiples_pe_peer_sector_z_slope_504d_2d_v045_signal(pe, pe_sector_med, pe_sector_std, closeadj):
    base = (pe - pe_sector_med) / pe_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of pe_peer_industry_dist
def f073erm_f073_earnings_multiples_pe_peer_industry_dist_slope_21d_2d_v046_signal(pe, pe_industry_med, closeadj):
    base = (pe - pe_industry_med) / pe_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of pe_peer_industry_dist
def f073erm_f073_earnings_multiples_pe_peer_industry_dist_slope_63d_2d_v047_signal(pe, pe_industry_med, closeadj):
    base = (pe - pe_industry_med) / pe_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of pe_peer_industry_dist
def f073erm_f073_earnings_multiples_pe_peer_industry_dist_slope_126d_2d_v048_signal(pe, pe_industry_med, closeadj):
    base = (pe - pe_industry_med) / pe_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of pe_peer_industry_dist
def f073erm_f073_earnings_multiples_pe_peer_industry_dist_slope_252d_2d_v049_signal(pe, pe_industry_med, closeadj):
    base = (pe - pe_industry_med) / pe_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of pe_peer_industry_dist
def f073erm_f073_earnings_multiples_pe_peer_industry_dist_slope_504d_2d_v050_signal(pe, pe_industry_med, closeadj):
    base = (pe - pe_industry_med) / pe_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of pe_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_pe_peer_mcap_bucket_dist_slope_21d_2d_v051_signal(pe, pe_mcap_med, closeadj):
    base = (pe - pe_mcap_med) / pe_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of pe_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_pe_peer_mcap_bucket_dist_slope_63d_2d_v052_signal(pe, pe_mcap_med, closeadj):
    base = (pe - pe_mcap_med) / pe_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of pe_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_pe_peer_mcap_bucket_dist_slope_126d_2d_v053_signal(pe, pe_mcap_med, closeadj):
    base = (pe - pe_mcap_med) / pe_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of pe_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_pe_peer_mcap_bucket_dist_slope_252d_2d_v054_signal(pe, pe_mcap_med, closeadj):
    base = (pe - pe_mcap_med) / pe_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of pe_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_pe_peer_mcap_bucket_dist_slope_504d_2d_v055_signal(pe, pe_mcap_med, closeadj):
    base = (pe - pe_mcap_med) / pe_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of pe_peer_sector_pctile
def f073erm_f073_earnings_multiples_pe_peer_sector_pctile_slope_21d_2d_v056_signal(pe_sector_pctile, closeadj):
    base = pe_sector_pctile
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of pe_peer_sector_pctile
def f073erm_f073_earnings_multiples_pe_peer_sector_pctile_slope_63d_2d_v057_signal(pe_sector_pctile, closeadj):
    base = pe_sector_pctile
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of pe_peer_sector_pctile
def f073erm_f073_earnings_multiples_pe_peer_sector_pctile_slope_126d_2d_v058_signal(pe_sector_pctile, closeadj):
    base = pe_sector_pctile
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of pe_peer_sector_pctile
def f073erm_f073_earnings_multiples_pe_peer_sector_pctile_slope_252d_2d_v059_signal(pe_sector_pctile, closeadj):
    base = pe_sector_pctile
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of pe_peer_sector_pctile
def f073erm_f073_earnings_multiples_pe_peer_sector_pctile_slope_504d_2d_v060_signal(pe_sector_pctile, closeadj):
    base = pe_sector_pctile
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of pe_peer_industry_pctile
def f073erm_f073_earnings_multiples_pe_peer_industry_pctile_slope_21d_2d_v061_signal(pe_industry_pctile, closeadj):
    base = pe_industry_pctile
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of pe_peer_industry_pctile
def f073erm_f073_earnings_multiples_pe_peer_industry_pctile_slope_63d_2d_v062_signal(pe_industry_pctile, closeadj):
    base = pe_industry_pctile
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of pe_peer_industry_pctile
def f073erm_f073_earnings_multiples_pe_peer_industry_pctile_slope_126d_2d_v063_signal(pe_industry_pctile, closeadj):
    base = pe_industry_pctile
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of pe_peer_industry_pctile
def f073erm_f073_earnings_multiples_pe_peer_industry_pctile_slope_252d_2d_v064_signal(pe_industry_pctile, closeadj):
    base = pe_industry_pctile
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of pe_peer_industry_pctile
def f073erm_f073_earnings_multiples_pe_peer_industry_pctile_slope_504d_2d_v065_signal(pe_industry_pctile, closeadj):
    base = pe_industry_pctile
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of evebitda_peer_sector_dist
def f073erm_f073_earnings_multiples_evebitda_peer_sector_dist_slope_21d_2d_v066_signal(evebitda, evebitda_sector_med, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of evebitda_peer_sector_dist
def f073erm_f073_earnings_multiples_evebitda_peer_sector_dist_slope_63d_2d_v067_signal(evebitda, evebitda_sector_med, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of evebitda_peer_sector_dist
def f073erm_f073_earnings_multiples_evebitda_peer_sector_dist_slope_126d_2d_v068_signal(evebitda, evebitda_sector_med, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of evebitda_peer_sector_dist
def f073erm_f073_earnings_multiples_evebitda_peer_sector_dist_slope_252d_2d_v069_signal(evebitda, evebitda_sector_med, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of evebitda_peer_sector_dist
def f073erm_f073_earnings_multiples_evebitda_peer_sector_dist_slope_504d_2d_v070_signal(evebitda, evebitda_sector_med, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of evebitda_peer_sector_z
def f073erm_f073_earnings_multiples_evebitda_peer_sector_z_slope_21d_2d_v071_signal(evebitda, evebitda_sector_med, evebitda_sector_std, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of evebitda_peer_sector_z
def f073erm_f073_earnings_multiples_evebitda_peer_sector_z_slope_63d_2d_v072_signal(evebitda, evebitda_sector_med, evebitda_sector_std, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of evebitda_peer_sector_z
def f073erm_f073_earnings_multiples_evebitda_peer_sector_z_slope_126d_2d_v073_signal(evebitda, evebitda_sector_med, evebitda_sector_std, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of evebitda_peer_sector_z
def f073erm_f073_earnings_multiples_evebitda_peer_sector_z_slope_252d_2d_v074_signal(evebitda, evebitda_sector_med, evebitda_sector_std, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of evebitda_peer_sector_z
def f073erm_f073_earnings_multiples_evebitda_peer_sector_z_slope_504d_2d_v075_signal(evebitda, evebitda_sector_med, evebitda_sector_std, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of evebitda_peer_industry_dist
def f073erm_f073_earnings_multiples_evebitda_peer_industry_dist_slope_21d_2d_v076_signal(evebitda, evebitda_industry_med, closeadj):
    base = (evebitda - evebitda_industry_med) / evebitda_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of evebitda_peer_industry_dist
def f073erm_f073_earnings_multiples_evebitda_peer_industry_dist_slope_63d_2d_v077_signal(evebitda, evebitda_industry_med, closeadj):
    base = (evebitda - evebitda_industry_med) / evebitda_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of evebitda_peer_industry_dist
def f073erm_f073_earnings_multiples_evebitda_peer_industry_dist_slope_126d_2d_v078_signal(evebitda, evebitda_industry_med, closeadj):
    base = (evebitda - evebitda_industry_med) / evebitda_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of evebitda_peer_industry_dist
def f073erm_f073_earnings_multiples_evebitda_peer_industry_dist_slope_252d_2d_v079_signal(evebitda, evebitda_industry_med, closeadj):
    base = (evebitda - evebitda_industry_med) / evebitda_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of evebitda_peer_industry_dist
def f073erm_f073_earnings_multiples_evebitda_peer_industry_dist_slope_504d_2d_v080_signal(evebitda, evebitda_industry_med, closeadj):
    base = (evebitda - evebitda_industry_med) / evebitda_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of evebitda_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_evebitda_peer_mcap_bucket_dist_slope_21d_2d_v081_signal(evebitda, evebitda_mcap_med, closeadj):
    base = (evebitda - evebitda_mcap_med) / evebitda_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of evebitda_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_evebitda_peer_mcap_bucket_dist_slope_63d_2d_v082_signal(evebitda, evebitda_mcap_med, closeadj):
    base = (evebitda - evebitda_mcap_med) / evebitda_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of evebitda_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_evebitda_peer_mcap_bucket_dist_slope_126d_2d_v083_signal(evebitda, evebitda_mcap_med, closeadj):
    base = (evebitda - evebitda_mcap_med) / evebitda_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of evebitda_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_evebitda_peer_mcap_bucket_dist_slope_252d_2d_v084_signal(evebitda, evebitda_mcap_med, closeadj):
    base = (evebitda - evebitda_mcap_med) / evebitda_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of evebitda_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_evebitda_peer_mcap_bucket_dist_slope_504d_2d_v085_signal(evebitda, evebitda_mcap_med, closeadj):
    base = (evebitda - evebitda_mcap_med) / evebitda_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of evebitda_peer_sector_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_sector_pctile_slope_21d_2d_v086_signal(evebitda_sector_pctile, closeadj):
    base = evebitda_sector_pctile
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of evebitda_peer_sector_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_sector_pctile_slope_63d_2d_v087_signal(evebitda_sector_pctile, closeadj):
    base = evebitda_sector_pctile
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of evebitda_peer_sector_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_sector_pctile_slope_126d_2d_v088_signal(evebitda_sector_pctile, closeadj):
    base = evebitda_sector_pctile
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of evebitda_peer_sector_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_sector_pctile_slope_252d_2d_v089_signal(evebitda_sector_pctile, closeadj):
    base = evebitda_sector_pctile
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of evebitda_peer_sector_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_sector_pctile_slope_504d_2d_v090_signal(evebitda_sector_pctile, closeadj):
    base = evebitda_sector_pctile
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of evebitda_peer_industry_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_industry_pctile_slope_21d_2d_v091_signal(evebitda_industry_pctile, closeadj):
    base = evebitda_industry_pctile
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of evebitda_peer_industry_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_industry_pctile_slope_63d_2d_v092_signal(evebitda_industry_pctile, closeadj):
    base = evebitda_industry_pctile
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of evebitda_peer_industry_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_industry_pctile_slope_126d_2d_v093_signal(evebitda_industry_pctile, closeadj):
    base = evebitda_industry_pctile
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of evebitda_peer_industry_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_industry_pctile_slope_252d_2d_v094_signal(evebitda_industry_pctile, closeadj):
    base = evebitda_industry_pctile
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of evebitda_peer_industry_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_industry_pctile_slope_504d_2d_v095_signal(evebitda_industry_pctile, closeadj):
    base = evebitda_industry_pctile
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of pe_lvl
def f073erm_f073_earnings_multiples_pe_lvl_sm21_sl21_2d_v096_signal(pe, closeadj):
    base = _mean(pe, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of pe_lvl
def f073erm_f073_earnings_multiples_pe_lvl_sm63_sl21_2d_v097_signal(pe, closeadj):
    base = _mean(pe, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of pe_lvl
def f073erm_f073_earnings_multiples_pe_lvl_sm63_sl63_2d_v098_signal(pe, closeadj):
    base = _mean(pe, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of pe_lvl
def f073erm_f073_earnings_multiples_pe_lvl_sm252_sl63_2d_v099_signal(pe, closeadj):
    base = _mean(pe, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of pe_lvl
def f073erm_f073_earnings_multiples_pe_lvl_sm252_sl126_2d_v100_signal(pe, closeadj):
    base = _mean(pe, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of pe1_lvl
def f073erm_f073_earnings_multiples_pe1_lvl_sm21_sl21_2d_v101_signal(pe1, closeadj):
    base = _mean(pe1, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of pe1_lvl
def f073erm_f073_earnings_multiples_pe1_lvl_sm63_sl21_2d_v102_signal(pe1, closeadj):
    base = _mean(pe1, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of pe1_lvl
def f073erm_f073_earnings_multiples_pe1_lvl_sm63_sl63_2d_v103_signal(pe1, closeadj):
    base = _mean(pe1, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of pe1_lvl
def f073erm_f073_earnings_multiples_pe1_lvl_sm252_sl63_2d_v104_signal(pe1, closeadj):
    base = _mean(pe1, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of pe1_lvl
def f073erm_f073_earnings_multiples_pe1_lvl_sm252_sl126_2d_v105_signal(pe1, closeadj):
    base = _mean(pe1, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of evebit_lvl
def f073erm_f073_earnings_multiples_evebit_lvl_sm21_sl21_2d_v106_signal(evebit, closeadj):
    base = _mean(evebit, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of evebit_lvl
def f073erm_f073_earnings_multiples_evebit_lvl_sm63_sl21_2d_v107_signal(evebit, closeadj):
    base = _mean(evebit, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of evebit_lvl
def f073erm_f073_earnings_multiples_evebit_lvl_sm63_sl63_2d_v108_signal(evebit, closeadj):
    base = _mean(evebit, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of evebit_lvl
def f073erm_f073_earnings_multiples_evebit_lvl_sm252_sl63_2d_v109_signal(evebit, closeadj):
    base = _mean(evebit, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of evebit_lvl
def f073erm_f073_earnings_multiples_evebit_lvl_sm252_sl126_2d_v110_signal(evebit, closeadj):
    base = _mean(evebit, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of evebitda_lvl
def f073erm_f073_earnings_multiples_evebitda_lvl_sm21_sl21_2d_v111_signal(evebitda, closeadj):
    base = _mean(evebitda, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of evebitda_lvl
def f073erm_f073_earnings_multiples_evebitda_lvl_sm63_sl21_2d_v112_signal(evebitda, closeadj):
    base = _mean(evebitda, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of evebitda_lvl
def f073erm_f073_earnings_multiples_evebitda_lvl_sm63_sl63_2d_v113_signal(evebitda, closeadj):
    base = _mean(evebitda, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of evebitda_lvl
def f073erm_f073_earnings_multiples_evebitda_lvl_sm252_sl63_2d_v114_signal(evebitda, closeadj):
    base = _mean(evebitda, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of evebitda_lvl
def f073erm_f073_earnings_multiples_evebitda_lvl_sm252_sl126_2d_v115_signal(evebitda, closeadj):
    base = _mean(evebitda, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of earn_yield
def f073erm_f073_earnings_multiples_earn_yield_sm21_sl21_2d_v116_signal(eps, close, closeadj):
    base = _mean(eps / close.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of earn_yield
def f073erm_f073_earnings_multiples_earn_yield_sm63_sl21_2d_v117_signal(eps, close, closeadj):
    base = _mean(eps / close.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of earn_yield
def f073erm_f073_earnings_multiples_earn_yield_sm63_sl63_2d_v118_signal(eps, close, closeadj):
    base = _mean(eps / close.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of earn_yield
def f073erm_f073_earnings_multiples_earn_yield_sm252_sl63_2d_v119_signal(eps, close, closeadj):
    base = _mean(eps / close.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of earn_yield
def f073erm_f073_earnings_multiples_earn_yield_sm252_sl126_2d_v120_signal(eps, close, closeadj):
    base = _mean(eps / close.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of pe_calc
def f073erm_f073_earnings_multiples_pe_calc_sm21_sl21_2d_v121_signal(close, eps, closeadj):
    base = _mean(_f073_pe(close, eps), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of pe_calc
def f073erm_f073_earnings_multiples_pe_calc_sm63_sl21_2d_v122_signal(close, eps, closeadj):
    base = _mean(_f073_pe(close, eps), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of pe_calc
def f073erm_f073_earnings_multiples_pe_calc_sm63_sl63_2d_v123_signal(close, eps, closeadj):
    base = _mean(_f073_pe(close, eps), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of pe_calc
def f073erm_f073_earnings_multiples_pe_calc_sm252_sl63_2d_v124_signal(close, eps, closeadj):
    base = _mean(_f073_pe(close, eps), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of pe_calc
def f073erm_f073_earnings_multiples_pe_calc_sm252_sl126_2d_v125_signal(close, eps, closeadj):
    base = _mean(_f073_pe(close, eps), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ebit_yield
def f073erm_f073_earnings_multiples_ebit_yield_sm21_sl21_2d_v126_signal(ebit, ev, closeadj):
    base = _mean(ebit / ev.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ebit_yield
def f073erm_f073_earnings_multiples_ebit_yield_sm63_sl21_2d_v127_signal(ebit, ev, closeadj):
    base = _mean(ebit / ev.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ebit_yield
def f073erm_f073_earnings_multiples_ebit_yield_sm63_sl63_2d_v128_signal(ebit, ev, closeadj):
    base = _mean(ebit / ev.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ebit_yield
def f073erm_f073_earnings_multiples_ebit_yield_sm252_sl63_2d_v129_signal(ebit, ev, closeadj):
    base = _mean(ebit / ev.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ebit_yield
def f073erm_f073_earnings_multiples_ebit_yield_sm252_sl126_2d_v130_signal(ebit, ev, closeadj):
    base = _mean(ebit / ev.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of pe_peer_sector_dist
def f073erm_f073_earnings_multiples_pe_peer_sector_dist_sm21_sl21_2d_v131_signal(pe, pe_sector_med, closeadj):
    base = _mean((pe - pe_sector_med) / pe_sector_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of pe_peer_sector_dist
def f073erm_f073_earnings_multiples_pe_peer_sector_dist_sm63_sl21_2d_v132_signal(pe, pe_sector_med, closeadj):
    base = _mean((pe - pe_sector_med) / pe_sector_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of pe_peer_sector_dist
def f073erm_f073_earnings_multiples_pe_peer_sector_dist_sm63_sl63_2d_v133_signal(pe, pe_sector_med, closeadj):
    base = _mean((pe - pe_sector_med) / pe_sector_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of pe_peer_sector_dist
def f073erm_f073_earnings_multiples_pe_peer_sector_dist_sm252_sl63_2d_v134_signal(pe, pe_sector_med, closeadj):
    base = _mean((pe - pe_sector_med) / pe_sector_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of pe_peer_sector_dist
def f073erm_f073_earnings_multiples_pe_peer_sector_dist_sm252_sl126_2d_v135_signal(pe, pe_sector_med, closeadj):
    base = _mean((pe - pe_sector_med) / pe_sector_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of pe_peer_sector_z
def f073erm_f073_earnings_multiples_pe_peer_sector_z_sm21_sl21_2d_v136_signal(pe, pe_sector_med, pe_sector_std, closeadj):
    base = _mean((pe - pe_sector_med) / pe_sector_std.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of pe_peer_sector_z
def f073erm_f073_earnings_multiples_pe_peer_sector_z_sm63_sl21_2d_v137_signal(pe, pe_sector_med, pe_sector_std, closeadj):
    base = _mean((pe - pe_sector_med) / pe_sector_std.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of pe_peer_sector_z
def f073erm_f073_earnings_multiples_pe_peer_sector_z_sm63_sl63_2d_v138_signal(pe, pe_sector_med, pe_sector_std, closeadj):
    base = _mean((pe - pe_sector_med) / pe_sector_std.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of pe_peer_sector_z
def f073erm_f073_earnings_multiples_pe_peer_sector_z_sm252_sl63_2d_v139_signal(pe, pe_sector_med, pe_sector_std, closeadj):
    base = _mean((pe - pe_sector_med) / pe_sector_std.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of pe_peer_sector_z
def f073erm_f073_earnings_multiples_pe_peer_sector_z_sm252_sl126_2d_v140_signal(pe, pe_sector_med, pe_sector_std, closeadj):
    base = _mean((pe - pe_sector_med) / pe_sector_std.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of pe_peer_industry_dist
def f073erm_f073_earnings_multiples_pe_peer_industry_dist_sm21_sl21_2d_v141_signal(pe, pe_industry_med, closeadj):
    base = _mean((pe - pe_industry_med) / pe_industry_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of pe_peer_industry_dist
def f073erm_f073_earnings_multiples_pe_peer_industry_dist_sm63_sl21_2d_v142_signal(pe, pe_industry_med, closeadj):
    base = _mean((pe - pe_industry_med) / pe_industry_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of pe_peer_industry_dist
def f073erm_f073_earnings_multiples_pe_peer_industry_dist_sm63_sl63_2d_v143_signal(pe, pe_industry_med, closeadj):
    base = _mean((pe - pe_industry_med) / pe_industry_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of pe_peer_industry_dist
def f073erm_f073_earnings_multiples_pe_peer_industry_dist_sm252_sl63_2d_v144_signal(pe, pe_industry_med, closeadj):
    base = _mean((pe - pe_industry_med) / pe_industry_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of pe_peer_industry_dist
def f073erm_f073_earnings_multiples_pe_peer_industry_dist_sm252_sl126_2d_v145_signal(pe, pe_industry_med, closeadj):
    base = _mean((pe - pe_industry_med) / pe_industry_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of pe_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_pe_peer_mcap_bucket_dist_sm21_sl21_2d_v146_signal(pe, pe_mcap_med, closeadj):
    base = _mean((pe - pe_mcap_med) / pe_mcap_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of pe_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_pe_peer_mcap_bucket_dist_sm63_sl21_2d_v147_signal(pe, pe_mcap_med, closeadj):
    base = _mean((pe - pe_mcap_med) / pe_mcap_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of pe_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_pe_peer_mcap_bucket_dist_sm63_sl63_2d_v148_signal(pe, pe_mcap_med, closeadj):
    base = _mean((pe - pe_mcap_med) / pe_mcap_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of pe_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_pe_peer_mcap_bucket_dist_sm252_sl63_2d_v149_signal(pe, pe_mcap_med, closeadj):
    base = _mean((pe - pe_mcap_med) / pe_mcap_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of pe_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_pe_peer_mcap_bucket_dist_sm252_sl126_2d_v150_signal(pe, pe_mcap_med, closeadj):
    base = _mean((pe - pe_mcap_med) / pe_mcap_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of pe_peer_sector_pctile
def f073erm_f073_earnings_multiples_pe_peer_sector_pctile_sm21_sl21_2d_v151_signal(pe_sector_pctile, closeadj):
    base = _mean(pe_sector_pctile, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of pe_peer_sector_pctile
def f073erm_f073_earnings_multiples_pe_peer_sector_pctile_sm63_sl21_2d_v152_signal(pe_sector_pctile, closeadj):
    base = _mean(pe_sector_pctile, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of pe_peer_sector_pctile
def f073erm_f073_earnings_multiples_pe_peer_sector_pctile_sm63_sl63_2d_v153_signal(pe_sector_pctile, closeadj):
    base = _mean(pe_sector_pctile, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of pe_peer_sector_pctile
def f073erm_f073_earnings_multiples_pe_peer_sector_pctile_sm252_sl63_2d_v154_signal(pe_sector_pctile, closeadj):
    base = _mean(pe_sector_pctile, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of pe_peer_sector_pctile
def f073erm_f073_earnings_multiples_pe_peer_sector_pctile_sm252_sl126_2d_v155_signal(pe_sector_pctile, closeadj):
    base = _mean(pe_sector_pctile, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of pe_peer_industry_pctile
def f073erm_f073_earnings_multiples_pe_peer_industry_pctile_sm21_sl21_2d_v156_signal(pe_industry_pctile, closeadj):
    base = _mean(pe_industry_pctile, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of pe_peer_industry_pctile
def f073erm_f073_earnings_multiples_pe_peer_industry_pctile_sm63_sl21_2d_v157_signal(pe_industry_pctile, closeadj):
    base = _mean(pe_industry_pctile, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of pe_peer_industry_pctile
def f073erm_f073_earnings_multiples_pe_peer_industry_pctile_sm63_sl63_2d_v158_signal(pe_industry_pctile, closeadj):
    base = _mean(pe_industry_pctile, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of pe_peer_industry_pctile
def f073erm_f073_earnings_multiples_pe_peer_industry_pctile_sm252_sl63_2d_v159_signal(pe_industry_pctile, closeadj):
    base = _mean(pe_industry_pctile, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of pe_peer_industry_pctile
def f073erm_f073_earnings_multiples_pe_peer_industry_pctile_sm252_sl126_2d_v160_signal(pe_industry_pctile, closeadj):
    base = _mean(pe_industry_pctile, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of evebitda_peer_sector_dist
def f073erm_f073_earnings_multiples_evebitda_peer_sector_dist_sm21_sl21_2d_v161_signal(evebitda, evebitda_sector_med, closeadj):
    base = _mean((evebitda - evebitda_sector_med) / evebitda_sector_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of evebitda_peer_sector_dist
def f073erm_f073_earnings_multiples_evebitda_peer_sector_dist_sm63_sl21_2d_v162_signal(evebitda, evebitda_sector_med, closeadj):
    base = _mean((evebitda - evebitda_sector_med) / evebitda_sector_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of evebitda_peer_sector_dist
def f073erm_f073_earnings_multiples_evebitda_peer_sector_dist_sm63_sl63_2d_v163_signal(evebitda, evebitda_sector_med, closeadj):
    base = _mean((evebitda - evebitda_sector_med) / evebitda_sector_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of evebitda_peer_sector_dist
def f073erm_f073_earnings_multiples_evebitda_peer_sector_dist_sm252_sl63_2d_v164_signal(evebitda, evebitda_sector_med, closeadj):
    base = _mean((evebitda - evebitda_sector_med) / evebitda_sector_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of evebitda_peer_sector_dist
def f073erm_f073_earnings_multiples_evebitda_peer_sector_dist_sm252_sl126_2d_v165_signal(evebitda, evebitda_sector_med, closeadj):
    base = _mean((evebitda - evebitda_sector_med) / evebitda_sector_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of evebitda_peer_sector_z
def f073erm_f073_earnings_multiples_evebitda_peer_sector_z_sm21_sl21_2d_v166_signal(evebitda, evebitda_sector_med, evebitda_sector_std, closeadj):
    base = _mean((evebitda - evebitda_sector_med) / evebitda_sector_std.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of evebitda_peer_sector_z
def f073erm_f073_earnings_multiples_evebitda_peer_sector_z_sm63_sl21_2d_v167_signal(evebitda, evebitda_sector_med, evebitda_sector_std, closeadj):
    base = _mean((evebitda - evebitda_sector_med) / evebitda_sector_std.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of evebitda_peer_sector_z
def f073erm_f073_earnings_multiples_evebitda_peer_sector_z_sm63_sl63_2d_v168_signal(evebitda, evebitda_sector_med, evebitda_sector_std, closeadj):
    base = _mean((evebitda - evebitda_sector_med) / evebitda_sector_std.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of evebitda_peer_sector_z
def f073erm_f073_earnings_multiples_evebitda_peer_sector_z_sm252_sl63_2d_v169_signal(evebitda, evebitda_sector_med, evebitda_sector_std, closeadj):
    base = _mean((evebitda - evebitda_sector_med) / evebitda_sector_std.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of evebitda_peer_sector_z
def f073erm_f073_earnings_multiples_evebitda_peer_sector_z_sm252_sl126_2d_v170_signal(evebitda, evebitda_sector_med, evebitda_sector_std, closeadj):
    base = _mean((evebitda - evebitda_sector_med) / evebitda_sector_std.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of evebitda_peer_industry_dist
def f073erm_f073_earnings_multiples_evebitda_peer_industry_dist_sm21_sl21_2d_v171_signal(evebitda, evebitda_industry_med, closeadj):
    base = _mean((evebitda - evebitda_industry_med) / evebitda_industry_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of evebitda_peer_industry_dist
def f073erm_f073_earnings_multiples_evebitda_peer_industry_dist_sm63_sl21_2d_v172_signal(evebitda, evebitda_industry_med, closeadj):
    base = _mean((evebitda - evebitda_industry_med) / evebitda_industry_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of evebitda_peer_industry_dist
def f073erm_f073_earnings_multiples_evebitda_peer_industry_dist_sm63_sl63_2d_v173_signal(evebitda, evebitda_industry_med, closeadj):
    base = _mean((evebitda - evebitda_industry_med) / evebitda_industry_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of evebitda_peer_industry_dist
def f073erm_f073_earnings_multiples_evebitda_peer_industry_dist_sm252_sl63_2d_v174_signal(evebitda, evebitda_industry_med, closeadj):
    base = _mean((evebitda - evebitda_industry_med) / evebitda_industry_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of evebitda_peer_industry_dist
def f073erm_f073_earnings_multiples_evebitda_peer_industry_dist_sm252_sl126_2d_v175_signal(evebitda, evebitda_industry_med, closeadj):
    base = _mean((evebitda - evebitda_industry_med) / evebitda_industry_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of evebitda_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_evebitda_peer_mcap_bucket_dist_sm21_sl21_2d_v176_signal(evebitda, evebitda_mcap_med, closeadj):
    base = _mean((evebitda - evebitda_mcap_med) / evebitda_mcap_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of evebitda_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_evebitda_peer_mcap_bucket_dist_sm63_sl21_2d_v177_signal(evebitda, evebitda_mcap_med, closeadj):
    base = _mean((evebitda - evebitda_mcap_med) / evebitda_mcap_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of evebitda_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_evebitda_peer_mcap_bucket_dist_sm63_sl63_2d_v178_signal(evebitda, evebitda_mcap_med, closeadj):
    base = _mean((evebitda - evebitda_mcap_med) / evebitda_mcap_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of evebitda_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_evebitda_peer_mcap_bucket_dist_sm252_sl63_2d_v179_signal(evebitda, evebitda_mcap_med, closeadj):
    base = _mean((evebitda - evebitda_mcap_med) / evebitda_mcap_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of evebitda_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_evebitda_peer_mcap_bucket_dist_sm252_sl126_2d_v180_signal(evebitda, evebitda_mcap_med, closeadj):
    base = _mean((evebitda - evebitda_mcap_med) / evebitda_mcap_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of evebitda_peer_sector_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_sector_pctile_sm21_sl21_2d_v181_signal(evebitda_sector_pctile, closeadj):
    base = _mean(evebitda_sector_pctile, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of evebitda_peer_sector_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_sector_pctile_sm63_sl21_2d_v182_signal(evebitda_sector_pctile, closeadj):
    base = _mean(evebitda_sector_pctile, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of evebitda_peer_sector_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_sector_pctile_sm63_sl63_2d_v183_signal(evebitda_sector_pctile, closeadj):
    base = _mean(evebitda_sector_pctile, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of evebitda_peer_sector_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_sector_pctile_sm252_sl63_2d_v184_signal(evebitda_sector_pctile, closeadj):
    base = _mean(evebitda_sector_pctile, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of evebitda_peer_sector_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_sector_pctile_sm252_sl126_2d_v185_signal(evebitda_sector_pctile, closeadj):
    base = _mean(evebitda_sector_pctile, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of evebitda_peer_industry_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_industry_pctile_sm21_sl21_2d_v186_signal(evebitda_industry_pctile, closeadj):
    base = _mean(evebitda_industry_pctile, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of evebitda_peer_industry_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_industry_pctile_sm63_sl21_2d_v187_signal(evebitda_industry_pctile, closeadj):
    base = _mean(evebitda_industry_pctile, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of evebitda_peer_industry_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_industry_pctile_sm63_sl63_2d_v188_signal(evebitda_industry_pctile, closeadj):
    base = _mean(evebitda_industry_pctile, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of evebitda_peer_industry_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_industry_pctile_sm252_sl63_2d_v189_signal(evebitda_industry_pctile, closeadj):
    base = _mean(evebitda_industry_pctile, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of evebitda_peer_industry_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_industry_pctile_sm252_sl126_2d_v190_signal(evebitda_industry_pctile, closeadj):
    base = _mean(evebitda_industry_pctile, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of pe_lvl
def f073erm_f073_earnings_multiples_pe_lvl_pctslope_21d_2d_v191_signal(pe, closeadj):
    base = pe
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of pe_lvl
def f073erm_f073_earnings_multiples_pe_lvl_pctslope_63d_2d_v192_signal(pe, closeadj):
    base = pe
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of pe_lvl
def f073erm_f073_earnings_multiples_pe_lvl_pctslope_252d_2d_v193_signal(pe, closeadj):
    base = pe
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of pe1_lvl
def f073erm_f073_earnings_multiples_pe1_lvl_pctslope_21d_2d_v194_signal(pe1, closeadj):
    base = pe1
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of pe1_lvl
def f073erm_f073_earnings_multiples_pe1_lvl_pctslope_63d_2d_v195_signal(pe1, closeadj):
    base = pe1
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of pe1_lvl
def f073erm_f073_earnings_multiples_pe1_lvl_pctslope_252d_2d_v196_signal(pe1, closeadj):
    base = pe1
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of evebit_lvl
def f073erm_f073_earnings_multiples_evebit_lvl_pctslope_21d_2d_v197_signal(evebit, closeadj):
    base = evebit
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of evebit_lvl
def f073erm_f073_earnings_multiples_evebit_lvl_pctslope_63d_2d_v198_signal(evebit, closeadj):
    base = evebit
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of evebit_lvl
def f073erm_f073_earnings_multiples_evebit_lvl_pctslope_252d_2d_v199_signal(evebit, closeadj):
    base = evebit
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of evebitda_lvl
def f073erm_f073_earnings_multiples_evebitda_lvl_pctslope_21d_2d_v200_signal(evebitda, closeadj):
    base = evebitda
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

