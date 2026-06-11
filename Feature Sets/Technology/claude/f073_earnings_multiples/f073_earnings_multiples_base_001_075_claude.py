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


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f073_pe(close, eps):
    return close / eps.replace(0, np.nan).abs()


# 21d mean of pe_lvl scaled by closeadj
def f073erm_f073_earnings_multiples_pe_lvl_mean_21d_base_v001_signal(pe, closeadj):
    base = pe
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of pe_lvl scaled by closeadj
def f073erm_f073_earnings_multiples_pe_lvl_mean_63d_base_v002_signal(pe, closeadj):
    base = pe
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of pe_lvl scaled by closeadj
def f073erm_f073_earnings_multiples_pe_lvl_mean_126d_base_v003_signal(pe, closeadj):
    base = pe
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of pe_lvl scaled by closeadj
def f073erm_f073_earnings_multiples_pe_lvl_mean_252d_base_v004_signal(pe, closeadj):
    base = pe
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of pe_lvl scaled by closeadj
def f073erm_f073_earnings_multiples_pe_lvl_mean_504d_base_v005_signal(pe, closeadj):
    base = pe
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of pe1_lvl scaled by closeadj
def f073erm_f073_earnings_multiples_pe1_lvl_mean_21d_base_v006_signal(pe1, closeadj):
    base = pe1
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of pe1_lvl scaled by closeadj
def f073erm_f073_earnings_multiples_pe1_lvl_mean_63d_base_v007_signal(pe1, closeadj):
    base = pe1
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of pe1_lvl scaled by closeadj
def f073erm_f073_earnings_multiples_pe1_lvl_mean_126d_base_v008_signal(pe1, closeadj):
    base = pe1
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of pe1_lvl scaled by closeadj
def f073erm_f073_earnings_multiples_pe1_lvl_mean_252d_base_v009_signal(pe1, closeadj):
    base = pe1
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of pe1_lvl scaled by closeadj
def f073erm_f073_earnings_multiples_pe1_lvl_mean_504d_base_v010_signal(pe1, closeadj):
    base = pe1
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of evebit_lvl scaled by closeadj
def f073erm_f073_earnings_multiples_evebit_lvl_mean_21d_base_v011_signal(evebit, closeadj):
    base = evebit
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of evebit_lvl scaled by closeadj
def f073erm_f073_earnings_multiples_evebit_lvl_mean_63d_base_v012_signal(evebit, closeadj):
    base = evebit
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of evebit_lvl scaled by closeadj
def f073erm_f073_earnings_multiples_evebit_lvl_mean_126d_base_v013_signal(evebit, closeadj):
    base = evebit
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of evebit_lvl scaled by closeadj
def f073erm_f073_earnings_multiples_evebit_lvl_mean_252d_base_v014_signal(evebit, closeadj):
    base = evebit
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of evebit_lvl scaled by closeadj
def f073erm_f073_earnings_multiples_evebit_lvl_mean_504d_base_v015_signal(evebit, closeadj):
    base = evebit
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of evebitda_lvl scaled by closeadj
def f073erm_f073_earnings_multiples_evebitda_lvl_mean_21d_base_v016_signal(evebitda, closeadj):
    base = evebitda
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of evebitda_lvl scaled by closeadj
def f073erm_f073_earnings_multiples_evebitda_lvl_mean_63d_base_v017_signal(evebitda, closeadj):
    base = evebitda
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of evebitda_lvl scaled by closeadj
def f073erm_f073_earnings_multiples_evebitda_lvl_mean_126d_base_v018_signal(evebitda, closeadj):
    base = evebitda
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of evebitda_lvl scaled by closeadj
def f073erm_f073_earnings_multiples_evebitda_lvl_mean_252d_base_v019_signal(evebitda, closeadj):
    base = evebitda
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of evebitda_lvl scaled by closeadj
def f073erm_f073_earnings_multiples_evebitda_lvl_mean_504d_base_v020_signal(evebitda, closeadj):
    base = evebitda
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of earn_yield scaled by closeadj
def f073erm_f073_earnings_multiples_earn_yield_mean_21d_base_v021_signal(eps, close, closeadj):
    base = eps / close.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of earn_yield scaled by closeadj
def f073erm_f073_earnings_multiples_earn_yield_mean_63d_base_v022_signal(eps, close, closeadj):
    base = eps / close.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of earn_yield scaled by closeadj
def f073erm_f073_earnings_multiples_earn_yield_mean_126d_base_v023_signal(eps, close, closeadj):
    base = eps / close.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of earn_yield scaled by closeadj
def f073erm_f073_earnings_multiples_earn_yield_mean_252d_base_v024_signal(eps, close, closeadj):
    base = eps / close.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of earn_yield scaled by closeadj
def f073erm_f073_earnings_multiples_earn_yield_mean_504d_base_v025_signal(eps, close, closeadj):
    base = eps / close.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of pe_calc scaled by closeadj
def f073erm_f073_earnings_multiples_pe_calc_mean_21d_base_v026_signal(close, eps, closeadj):
    base = _f073_pe(close, eps)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of pe_calc scaled by closeadj
def f073erm_f073_earnings_multiples_pe_calc_mean_63d_base_v027_signal(close, eps, closeadj):
    base = _f073_pe(close, eps)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of pe_calc scaled by closeadj
def f073erm_f073_earnings_multiples_pe_calc_mean_126d_base_v028_signal(close, eps, closeadj):
    base = _f073_pe(close, eps)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of pe_calc scaled by closeadj
def f073erm_f073_earnings_multiples_pe_calc_mean_252d_base_v029_signal(close, eps, closeadj):
    base = _f073_pe(close, eps)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of pe_calc scaled by closeadj
def f073erm_f073_earnings_multiples_pe_calc_mean_504d_base_v030_signal(close, eps, closeadj):
    base = _f073_pe(close, eps)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ebit_yield scaled by closeadj
def f073erm_f073_earnings_multiples_ebit_yield_mean_21d_base_v031_signal(ebit, ev, closeadj):
    base = ebit / ev.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ebit_yield scaled by closeadj
def f073erm_f073_earnings_multiples_ebit_yield_mean_63d_base_v032_signal(ebit, ev, closeadj):
    base = ebit / ev.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ebit_yield scaled by closeadj
def f073erm_f073_earnings_multiples_ebit_yield_mean_126d_base_v033_signal(ebit, ev, closeadj):
    base = ebit / ev.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ebit_yield scaled by closeadj
def f073erm_f073_earnings_multiples_ebit_yield_mean_252d_base_v034_signal(ebit, ev, closeadj):
    base = ebit / ev.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ebit_yield scaled by closeadj
def f073erm_f073_earnings_multiples_ebit_yield_mean_504d_base_v035_signal(ebit, ev, closeadj):
    base = ebit / ev.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of pe_peer_sector_dist scaled by closeadj
def f073erm_f073_earnings_multiples_pe_peer_sector_dist_mean_21d_base_v036_signal(pe, pe_sector_med, closeadj):
    base = (pe - pe_sector_med) / pe_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of pe_peer_sector_dist scaled by closeadj
def f073erm_f073_earnings_multiples_pe_peer_sector_dist_mean_63d_base_v037_signal(pe, pe_sector_med, closeadj):
    base = (pe - pe_sector_med) / pe_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of pe_peer_sector_dist scaled by closeadj
def f073erm_f073_earnings_multiples_pe_peer_sector_dist_mean_126d_base_v038_signal(pe, pe_sector_med, closeadj):
    base = (pe - pe_sector_med) / pe_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of pe_peer_sector_dist scaled by closeadj
def f073erm_f073_earnings_multiples_pe_peer_sector_dist_mean_252d_base_v039_signal(pe, pe_sector_med, closeadj):
    base = (pe - pe_sector_med) / pe_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of pe_peer_sector_dist scaled by closeadj
def f073erm_f073_earnings_multiples_pe_peer_sector_dist_mean_504d_base_v040_signal(pe, pe_sector_med, closeadj):
    base = (pe - pe_sector_med) / pe_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of pe_peer_sector_z scaled by closeadj
def f073erm_f073_earnings_multiples_pe_peer_sector_z_mean_21d_base_v041_signal(pe, pe_sector_med, pe_sector_std, closeadj):
    base = (pe - pe_sector_med) / pe_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of pe_peer_sector_z scaled by closeadj
def f073erm_f073_earnings_multiples_pe_peer_sector_z_mean_63d_base_v042_signal(pe, pe_sector_med, pe_sector_std, closeadj):
    base = (pe - pe_sector_med) / pe_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of pe_peer_sector_z scaled by closeadj
def f073erm_f073_earnings_multiples_pe_peer_sector_z_mean_126d_base_v043_signal(pe, pe_sector_med, pe_sector_std, closeadj):
    base = (pe - pe_sector_med) / pe_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of pe_peer_sector_z scaled by closeadj
def f073erm_f073_earnings_multiples_pe_peer_sector_z_mean_252d_base_v044_signal(pe, pe_sector_med, pe_sector_std, closeadj):
    base = (pe - pe_sector_med) / pe_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of pe_peer_sector_z scaled by closeadj
def f073erm_f073_earnings_multiples_pe_peer_sector_z_mean_504d_base_v045_signal(pe, pe_sector_med, pe_sector_std, closeadj):
    base = (pe - pe_sector_med) / pe_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of pe_peer_industry_dist scaled by closeadj
def f073erm_f073_earnings_multiples_pe_peer_industry_dist_mean_21d_base_v046_signal(pe, pe_industry_med, closeadj):
    base = (pe - pe_industry_med) / pe_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of pe_peer_industry_dist scaled by closeadj
def f073erm_f073_earnings_multiples_pe_peer_industry_dist_mean_63d_base_v047_signal(pe, pe_industry_med, closeadj):
    base = (pe - pe_industry_med) / pe_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of pe_peer_industry_dist scaled by closeadj
def f073erm_f073_earnings_multiples_pe_peer_industry_dist_mean_126d_base_v048_signal(pe, pe_industry_med, closeadj):
    base = (pe - pe_industry_med) / pe_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of pe_peer_industry_dist scaled by closeadj
def f073erm_f073_earnings_multiples_pe_peer_industry_dist_mean_252d_base_v049_signal(pe, pe_industry_med, closeadj):
    base = (pe - pe_industry_med) / pe_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of pe_peer_industry_dist scaled by closeadj
def f073erm_f073_earnings_multiples_pe_peer_industry_dist_mean_504d_base_v050_signal(pe, pe_industry_med, closeadj):
    base = (pe - pe_industry_med) / pe_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of pe_peer_mcap_bucket_dist scaled by closeadj
def f073erm_f073_earnings_multiples_pe_peer_mcap_bucket_dist_mean_21d_base_v051_signal(pe, pe_mcap_med, closeadj):
    base = (pe - pe_mcap_med) / pe_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of pe_peer_mcap_bucket_dist scaled by closeadj
def f073erm_f073_earnings_multiples_pe_peer_mcap_bucket_dist_mean_63d_base_v052_signal(pe, pe_mcap_med, closeadj):
    base = (pe - pe_mcap_med) / pe_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of pe_peer_mcap_bucket_dist scaled by closeadj
def f073erm_f073_earnings_multiples_pe_peer_mcap_bucket_dist_mean_126d_base_v053_signal(pe, pe_mcap_med, closeadj):
    base = (pe - pe_mcap_med) / pe_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of pe_peer_mcap_bucket_dist scaled by closeadj
def f073erm_f073_earnings_multiples_pe_peer_mcap_bucket_dist_mean_252d_base_v054_signal(pe, pe_mcap_med, closeadj):
    base = (pe - pe_mcap_med) / pe_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of pe_peer_mcap_bucket_dist scaled by closeadj
def f073erm_f073_earnings_multiples_pe_peer_mcap_bucket_dist_mean_504d_base_v055_signal(pe, pe_mcap_med, closeadj):
    base = (pe - pe_mcap_med) / pe_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of pe_peer_sector_pctile scaled by closeadj
def f073erm_f073_earnings_multiples_pe_peer_sector_pctile_mean_21d_base_v056_signal(pe_sector_pctile, closeadj):
    base = pe_sector_pctile
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of pe_peer_sector_pctile scaled by closeadj
def f073erm_f073_earnings_multiples_pe_peer_sector_pctile_mean_63d_base_v057_signal(pe_sector_pctile, closeadj):
    base = pe_sector_pctile
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of pe_peer_sector_pctile scaled by closeadj
def f073erm_f073_earnings_multiples_pe_peer_sector_pctile_mean_126d_base_v058_signal(pe_sector_pctile, closeadj):
    base = pe_sector_pctile
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of pe_peer_sector_pctile scaled by closeadj
def f073erm_f073_earnings_multiples_pe_peer_sector_pctile_mean_252d_base_v059_signal(pe_sector_pctile, closeadj):
    base = pe_sector_pctile
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of pe_peer_sector_pctile scaled by closeadj
def f073erm_f073_earnings_multiples_pe_peer_sector_pctile_mean_504d_base_v060_signal(pe_sector_pctile, closeadj):
    base = pe_sector_pctile
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of pe_peer_industry_pctile scaled by closeadj
def f073erm_f073_earnings_multiples_pe_peer_industry_pctile_mean_21d_base_v061_signal(pe_industry_pctile, closeadj):
    base = pe_industry_pctile
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of pe_peer_industry_pctile scaled by closeadj
def f073erm_f073_earnings_multiples_pe_peer_industry_pctile_mean_63d_base_v062_signal(pe_industry_pctile, closeadj):
    base = pe_industry_pctile
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of pe_peer_industry_pctile scaled by closeadj
def f073erm_f073_earnings_multiples_pe_peer_industry_pctile_mean_126d_base_v063_signal(pe_industry_pctile, closeadj):
    base = pe_industry_pctile
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of pe_peer_industry_pctile scaled by closeadj
def f073erm_f073_earnings_multiples_pe_peer_industry_pctile_mean_252d_base_v064_signal(pe_industry_pctile, closeadj):
    base = pe_industry_pctile
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of pe_peer_industry_pctile scaled by closeadj
def f073erm_f073_earnings_multiples_pe_peer_industry_pctile_mean_504d_base_v065_signal(pe_industry_pctile, closeadj):
    base = pe_industry_pctile
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of evebitda_peer_sector_dist scaled by closeadj
def f073erm_f073_earnings_multiples_evebitda_peer_sector_dist_mean_21d_base_v066_signal(evebitda, evebitda_sector_med, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of evebitda_peer_sector_dist scaled by closeadj
def f073erm_f073_earnings_multiples_evebitda_peer_sector_dist_mean_63d_base_v067_signal(evebitda, evebitda_sector_med, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of evebitda_peer_sector_dist scaled by closeadj
def f073erm_f073_earnings_multiples_evebitda_peer_sector_dist_mean_126d_base_v068_signal(evebitda, evebitda_sector_med, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of evebitda_peer_sector_dist scaled by closeadj
def f073erm_f073_earnings_multiples_evebitda_peer_sector_dist_mean_252d_base_v069_signal(evebitda, evebitda_sector_med, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of evebitda_peer_sector_dist scaled by closeadj
def f073erm_f073_earnings_multiples_evebitda_peer_sector_dist_mean_504d_base_v070_signal(evebitda, evebitda_sector_med, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of evebitda_peer_sector_z scaled by closeadj
def f073erm_f073_earnings_multiples_evebitda_peer_sector_z_mean_21d_base_v071_signal(evebitda, evebitda_sector_med, evebitda_sector_std, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of evebitda_peer_sector_z scaled by closeadj
def f073erm_f073_earnings_multiples_evebitda_peer_sector_z_mean_63d_base_v072_signal(evebitda, evebitda_sector_med, evebitda_sector_std, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of evebitda_peer_sector_z scaled by closeadj
def f073erm_f073_earnings_multiples_evebitda_peer_sector_z_mean_126d_base_v073_signal(evebitda, evebitda_sector_med, evebitda_sector_std, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of evebitda_peer_sector_z scaled by closeadj
def f073erm_f073_earnings_multiples_evebitda_peer_sector_z_mean_252d_base_v074_signal(evebitda, evebitda_sector_med, evebitda_sector_std, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of evebitda_peer_sector_z scaled by closeadj
def f073erm_f073_earnings_multiples_evebitda_peer_sector_z_mean_504d_base_v075_signal(evebitda, evebitda_sector_med, evebitda_sector_std, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of evebitda_peer_industry_dist scaled by closeadj
def f073erm_f073_earnings_multiples_evebitda_peer_industry_dist_mean_21d_base_v076_signal(evebitda, evebitda_industry_med, closeadj):
    base = (evebitda - evebitda_industry_med) / evebitda_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of evebitda_peer_industry_dist scaled by closeadj
def f073erm_f073_earnings_multiples_evebitda_peer_industry_dist_mean_63d_base_v077_signal(evebitda, evebitda_industry_med, closeadj):
    base = (evebitda - evebitda_industry_med) / evebitda_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of evebitda_peer_industry_dist scaled by closeadj
def f073erm_f073_earnings_multiples_evebitda_peer_industry_dist_mean_126d_base_v078_signal(evebitda, evebitda_industry_med, closeadj):
    base = (evebitda - evebitda_industry_med) / evebitda_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of evebitda_peer_industry_dist scaled by closeadj
def f073erm_f073_earnings_multiples_evebitda_peer_industry_dist_mean_252d_base_v079_signal(evebitda, evebitda_industry_med, closeadj):
    base = (evebitda - evebitda_industry_med) / evebitda_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of evebitda_peer_industry_dist scaled by closeadj
def f073erm_f073_earnings_multiples_evebitda_peer_industry_dist_mean_504d_base_v080_signal(evebitda, evebitda_industry_med, closeadj):
    base = (evebitda - evebitda_industry_med) / evebitda_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of evebitda_peer_mcap_bucket_dist scaled by closeadj
def f073erm_f073_earnings_multiples_evebitda_peer_mcap_bucket_dist_mean_21d_base_v081_signal(evebitda, evebitda_mcap_med, closeadj):
    base = (evebitda - evebitda_mcap_med) / evebitda_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of evebitda_peer_mcap_bucket_dist scaled by closeadj
def f073erm_f073_earnings_multiples_evebitda_peer_mcap_bucket_dist_mean_63d_base_v082_signal(evebitda, evebitda_mcap_med, closeadj):
    base = (evebitda - evebitda_mcap_med) / evebitda_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of evebitda_peer_mcap_bucket_dist scaled by closeadj
def f073erm_f073_earnings_multiples_evebitda_peer_mcap_bucket_dist_mean_126d_base_v083_signal(evebitda, evebitda_mcap_med, closeadj):
    base = (evebitda - evebitda_mcap_med) / evebitda_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of evebitda_peer_mcap_bucket_dist scaled by closeadj
def f073erm_f073_earnings_multiples_evebitda_peer_mcap_bucket_dist_mean_252d_base_v084_signal(evebitda, evebitda_mcap_med, closeadj):
    base = (evebitda - evebitda_mcap_med) / evebitda_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of evebitda_peer_mcap_bucket_dist scaled by closeadj
def f073erm_f073_earnings_multiples_evebitda_peer_mcap_bucket_dist_mean_504d_base_v085_signal(evebitda, evebitda_mcap_med, closeadj):
    base = (evebitda - evebitda_mcap_med) / evebitda_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of evebitda_peer_sector_pctile scaled by closeadj
def f073erm_f073_earnings_multiples_evebitda_peer_sector_pctile_mean_21d_base_v086_signal(evebitda_sector_pctile, closeadj):
    base = evebitda_sector_pctile
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of evebitda_peer_sector_pctile scaled by closeadj
def f073erm_f073_earnings_multiples_evebitda_peer_sector_pctile_mean_63d_base_v087_signal(evebitda_sector_pctile, closeadj):
    base = evebitda_sector_pctile
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of evebitda_peer_sector_pctile scaled by closeadj
def f073erm_f073_earnings_multiples_evebitda_peer_sector_pctile_mean_126d_base_v088_signal(evebitda_sector_pctile, closeadj):
    base = evebitda_sector_pctile
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of evebitda_peer_sector_pctile scaled by closeadj
def f073erm_f073_earnings_multiples_evebitda_peer_sector_pctile_mean_252d_base_v089_signal(evebitda_sector_pctile, closeadj):
    base = evebitda_sector_pctile
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of evebitda_peer_sector_pctile scaled by closeadj
def f073erm_f073_earnings_multiples_evebitda_peer_sector_pctile_mean_504d_base_v090_signal(evebitda_sector_pctile, closeadj):
    base = evebitda_sector_pctile
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of evebitda_peer_industry_pctile scaled by closeadj
def f073erm_f073_earnings_multiples_evebitda_peer_industry_pctile_mean_21d_base_v091_signal(evebitda_industry_pctile, closeadj):
    base = evebitda_industry_pctile
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of evebitda_peer_industry_pctile scaled by closeadj
def f073erm_f073_earnings_multiples_evebitda_peer_industry_pctile_mean_63d_base_v092_signal(evebitda_industry_pctile, closeadj):
    base = evebitda_industry_pctile
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of evebitda_peer_industry_pctile scaled by closeadj
def f073erm_f073_earnings_multiples_evebitda_peer_industry_pctile_mean_126d_base_v093_signal(evebitda_industry_pctile, closeadj):
    base = evebitda_industry_pctile
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of evebitda_peer_industry_pctile scaled by closeadj
def f073erm_f073_earnings_multiples_evebitda_peer_industry_pctile_mean_252d_base_v094_signal(evebitda_industry_pctile, closeadj):
    base = evebitda_industry_pctile
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of evebitda_peer_industry_pctile scaled by closeadj
def f073erm_f073_earnings_multiples_evebitda_peer_industry_pctile_mean_504d_base_v095_signal(evebitda_industry_pctile, closeadj):
    base = evebitda_industry_pctile
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of pe_lvl
def f073erm_f073_earnings_multiples_pe_lvl_median_63d_base_v096_signal(pe, closeadj):
    base = pe
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of pe_lvl
def f073erm_f073_earnings_multiples_pe_lvl_median_252d_base_v097_signal(pe, closeadj):
    base = pe
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of pe_lvl
def f073erm_f073_earnings_multiples_pe_lvl_median_504d_base_v098_signal(pe, closeadj):
    base = pe
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of pe1_lvl
def f073erm_f073_earnings_multiples_pe1_lvl_median_63d_base_v099_signal(pe1, closeadj):
    base = pe1
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of pe1_lvl
def f073erm_f073_earnings_multiples_pe1_lvl_median_252d_base_v100_signal(pe1, closeadj):
    base = pe1
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

