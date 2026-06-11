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


# 21d acceleration of pe_lvl
def f073erm_f073_earnings_multiples_pe_lvl_accel_21d_3d_v001_signal(pe, closeadj):
    base = pe
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of pe_lvl
def f073erm_f073_earnings_multiples_pe_lvl_accel_63d_3d_v002_signal(pe, closeadj):
    base = pe
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of pe_lvl
def f073erm_f073_earnings_multiples_pe_lvl_accel_126d_3d_v003_signal(pe, closeadj):
    base = pe
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of pe_lvl
def f073erm_f073_earnings_multiples_pe_lvl_accel_252d_3d_v004_signal(pe, closeadj):
    base = pe
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of pe1_lvl
def f073erm_f073_earnings_multiples_pe1_lvl_accel_21d_3d_v005_signal(pe1, closeadj):
    base = pe1
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of pe1_lvl
def f073erm_f073_earnings_multiples_pe1_lvl_accel_63d_3d_v006_signal(pe1, closeadj):
    base = pe1
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of pe1_lvl
def f073erm_f073_earnings_multiples_pe1_lvl_accel_126d_3d_v007_signal(pe1, closeadj):
    base = pe1
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of pe1_lvl
def f073erm_f073_earnings_multiples_pe1_lvl_accel_252d_3d_v008_signal(pe1, closeadj):
    base = pe1
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of evebit_lvl
def f073erm_f073_earnings_multiples_evebit_lvl_accel_21d_3d_v009_signal(evebit, closeadj):
    base = evebit
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of evebit_lvl
def f073erm_f073_earnings_multiples_evebit_lvl_accel_63d_3d_v010_signal(evebit, closeadj):
    base = evebit
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of evebit_lvl
def f073erm_f073_earnings_multiples_evebit_lvl_accel_126d_3d_v011_signal(evebit, closeadj):
    base = evebit
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of evebit_lvl
def f073erm_f073_earnings_multiples_evebit_lvl_accel_252d_3d_v012_signal(evebit, closeadj):
    base = evebit
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of evebitda_lvl
def f073erm_f073_earnings_multiples_evebitda_lvl_accel_21d_3d_v013_signal(evebitda, closeadj):
    base = evebitda
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of evebitda_lvl
def f073erm_f073_earnings_multiples_evebitda_lvl_accel_63d_3d_v014_signal(evebitda, closeadj):
    base = evebitda
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of evebitda_lvl
def f073erm_f073_earnings_multiples_evebitda_lvl_accel_126d_3d_v015_signal(evebitda, closeadj):
    base = evebitda
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of evebitda_lvl
def f073erm_f073_earnings_multiples_evebitda_lvl_accel_252d_3d_v016_signal(evebitda, closeadj):
    base = evebitda
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of earn_yield
def f073erm_f073_earnings_multiples_earn_yield_accel_21d_3d_v017_signal(eps, close, closeadj):
    base = eps / close.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of earn_yield
def f073erm_f073_earnings_multiples_earn_yield_accel_63d_3d_v018_signal(eps, close, closeadj):
    base = eps / close.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of earn_yield
def f073erm_f073_earnings_multiples_earn_yield_accel_126d_3d_v019_signal(eps, close, closeadj):
    base = eps / close.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of earn_yield
def f073erm_f073_earnings_multiples_earn_yield_accel_252d_3d_v020_signal(eps, close, closeadj):
    base = eps / close.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of pe_calc
def f073erm_f073_earnings_multiples_pe_calc_accel_21d_3d_v021_signal(close, eps, closeadj):
    base = _f073_pe(close, eps)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of pe_calc
def f073erm_f073_earnings_multiples_pe_calc_accel_63d_3d_v022_signal(close, eps, closeadj):
    base = _f073_pe(close, eps)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of pe_calc
def f073erm_f073_earnings_multiples_pe_calc_accel_126d_3d_v023_signal(close, eps, closeadj):
    base = _f073_pe(close, eps)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of pe_calc
def f073erm_f073_earnings_multiples_pe_calc_accel_252d_3d_v024_signal(close, eps, closeadj):
    base = _f073_pe(close, eps)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ebit_yield
def f073erm_f073_earnings_multiples_ebit_yield_accel_21d_3d_v025_signal(ebit, ev, closeadj):
    base = ebit / ev.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ebit_yield
def f073erm_f073_earnings_multiples_ebit_yield_accel_63d_3d_v026_signal(ebit, ev, closeadj):
    base = ebit / ev.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ebit_yield
def f073erm_f073_earnings_multiples_ebit_yield_accel_126d_3d_v027_signal(ebit, ev, closeadj):
    base = ebit / ev.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ebit_yield
def f073erm_f073_earnings_multiples_ebit_yield_accel_252d_3d_v028_signal(ebit, ev, closeadj):
    base = ebit / ev.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of pe_peer_sector_dist
def f073erm_f073_earnings_multiples_pe_peer_sector_dist_accel_21d_3d_v029_signal(pe, pe_sector_med, closeadj):
    base = (pe - pe_sector_med) / pe_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of pe_peer_sector_dist
def f073erm_f073_earnings_multiples_pe_peer_sector_dist_accel_63d_3d_v030_signal(pe, pe_sector_med, closeadj):
    base = (pe - pe_sector_med) / pe_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of pe_peer_sector_dist
def f073erm_f073_earnings_multiples_pe_peer_sector_dist_accel_126d_3d_v031_signal(pe, pe_sector_med, closeadj):
    base = (pe - pe_sector_med) / pe_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of pe_peer_sector_dist
def f073erm_f073_earnings_multiples_pe_peer_sector_dist_accel_252d_3d_v032_signal(pe, pe_sector_med, closeadj):
    base = (pe - pe_sector_med) / pe_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of pe_peer_sector_z
def f073erm_f073_earnings_multiples_pe_peer_sector_z_accel_21d_3d_v033_signal(pe, pe_sector_med, pe_sector_std, closeadj):
    base = (pe - pe_sector_med) / pe_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of pe_peer_sector_z
def f073erm_f073_earnings_multiples_pe_peer_sector_z_accel_63d_3d_v034_signal(pe, pe_sector_med, pe_sector_std, closeadj):
    base = (pe - pe_sector_med) / pe_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of pe_peer_sector_z
def f073erm_f073_earnings_multiples_pe_peer_sector_z_accel_126d_3d_v035_signal(pe, pe_sector_med, pe_sector_std, closeadj):
    base = (pe - pe_sector_med) / pe_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of pe_peer_sector_z
def f073erm_f073_earnings_multiples_pe_peer_sector_z_accel_252d_3d_v036_signal(pe, pe_sector_med, pe_sector_std, closeadj):
    base = (pe - pe_sector_med) / pe_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of pe_peer_industry_dist
def f073erm_f073_earnings_multiples_pe_peer_industry_dist_accel_21d_3d_v037_signal(pe, pe_industry_med, closeadj):
    base = (pe - pe_industry_med) / pe_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of pe_peer_industry_dist
def f073erm_f073_earnings_multiples_pe_peer_industry_dist_accel_63d_3d_v038_signal(pe, pe_industry_med, closeadj):
    base = (pe - pe_industry_med) / pe_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of pe_peer_industry_dist
def f073erm_f073_earnings_multiples_pe_peer_industry_dist_accel_126d_3d_v039_signal(pe, pe_industry_med, closeadj):
    base = (pe - pe_industry_med) / pe_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of pe_peer_industry_dist
def f073erm_f073_earnings_multiples_pe_peer_industry_dist_accel_252d_3d_v040_signal(pe, pe_industry_med, closeadj):
    base = (pe - pe_industry_med) / pe_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of pe_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_pe_peer_mcap_bucket_dist_accel_21d_3d_v041_signal(pe, pe_mcap_med, closeadj):
    base = (pe - pe_mcap_med) / pe_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of pe_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_pe_peer_mcap_bucket_dist_accel_63d_3d_v042_signal(pe, pe_mcap_med, closeadj):
    base = (pe - pe_mcap_med) / pe_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of pe_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_pe_peer_mcap_bucket_dist_accel_126d_3d_v043_signal(pe, pe_mcap_med, closeadj):
    base = (pe - pe_mcap_med) / pe_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of pe_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_pe_peer_mcap_bucket_dist_accel_252d_3d_v044_signal(pe, pe_mcap_med, closeadj):
    base = (pe - pe_mcap_med) / pe_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of pe_peer_sector_pctile
def f073erm_f073_earnings_multiples_pe_peer_sector_pctile_accel_21d_3d_v045_signal(pe_sector_pctile, closeadj):
    base = pe_sector_pctile
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of pe_peer_sector_pctile
def f073erm_f073_earnings_multiples_pe_peer_sector_pctile_accel_63d_3d_v046_signal(pe_sector_pctile, closeadj):
    base = pe_sector_pctile
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of pe_peer_sector_pctile
def f073erm_f073_earnings_multiples_pe_peer_sector_pctile_accel_126d_3d_v047_signal(pe_sector_pctile, closeadj):
    base = pe_sector_pctile
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of pe_peer_sector_pctile
def f073erm_f073_earnings_multiples_pe_peer_sector_pctile_accel_252d_3d_v048_signal(pe_sector_pctile, closeadj):
    base = pe_sector_pctile
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of pe_peer_industry_pctile
def f073erm_f073_earnings_multiples_pe_peer_industry_pctile_accel_21d_3d_v049_signal(pe_industry_pctile, closeadj):
    base = pe_industry_pctile
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of pe_peer_industry_pctile
def f073erm_f073_earnings_multiples_pe_peer_industry_pctile_accel_63d_3d_v050_signal(pe_industry_pctile, closeadj):
    base = pe_industry_pctile
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of pe_peer_industry_pctile
def f073erm_f073_earnings_multiples_pe_peer_industry_pctile_accel_126d_3d_v051_signal(pe_industry_pctile, closeadj):
    base = pe_industry_pctile
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of pe_peer_industry_pctile
def f073erm_f073_earnings_multiples_pe_peer_industry_pctile_accel_252d_3d_v052_signal(pe_industry_pctile, closeadj):
    base = pe_industry_pctile
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of evebitda_peer_sector_dist
def f073erm_f073_earnings_multiples_evebitda_peer_sector_dist_accel_21d_3d_v053_signal(evebitda, evebitda_sector_med, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of evebitda_peer_sector_dist
def f073erm_f073_earnings_multiples_evebitda_peer_sector_dist_accel_63d_3d_v054_signal(evebitda, evebitda_sector_med, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of evebitda_peer_sector_dist
def f073erm_f073_earnings_multiples_evebitda_peer_sector_dist_accel_126d_3d_v055_signal(evebitda, evebitda_sector_med, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of evebitda_peer_sector_dist
def f073erm_f073_earnings_multiples_evebitda_peer_sector_dist_accel_252d_3d_v056_signal(evebitda, evebitda_sector_med, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of evebitda_peer_sector_z
def f073erm_f073_earnings_multiples_evebitda_peer_sector_z_accel_21d_3d_v057_signal(evebitda, evebitda_sector_med, evebitda_sector_std, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of evebitda_peer_sector_z
def f073erm_f073_earnings_multiples_evebitda_peer_sector_z_accel_63d_3d_v058_signal(evebitda, evebitda_sector_med, evebitda_sector_std, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of evebitda_peer_sector_z
def f073erm_f073_earnings_multiples_evebitda_peer_sector_z_accel_126d_3d_v059_signal(evebitda, evebitda_sector_med, evebitda_sector_std, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of evebitda_peer_sector_z
def f073erm_f073_earnings_multiples_evebitda_peer_sector_z_accel_252d_3d_v060_signal(evebitda, evebitda_sector_med, evebitda_sector_std, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of evebitda_peer_industry_dist
def f073erm_f073_earnings_multiples_evebitda_peer_industry_dist_accel_21d_3d_v061_signal(evebitda, evebitda_industry_med, closeadj):
    base = (evebitda - evebitda_industry_med) / evebitda_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of evebitda_peer_industry_dist
def f073erm_f073_earnings_multiples_evebitda_peer_industry_dist_accel_63d_3d_v062_signal(evebitda, evebitda_industry_med, closeadj):
    base = (evebitda - evebitda_industry_med) / evebitda_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of evebitda_peer_industry_dist
def f073erm_f073_earnings_multiples_evebitda_peer_industry_dist_accel_126d_3d_v063_signal(evebitda, evebitda_industry_med, closeadj):
    base = (evebitda - evebitda_industry_med) / evebitda_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of evebitda_peer_industry_dist
def f073erm_f073_earnings_multiples_evebitda_peer_industry_dist_accel_252d_3d_v064_signal(evebitda, evebitda_industry_med, closeadj):
    base = (evebitda - evebitda_industry_med) / evebitda_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of evebitda_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_evebitda_peer_mcap_bucket_dist_accel_21d_3d_v065_signal(evebitda, evebitda_mcap_med, closeadj):
    base = (evebitda - evebitda_mcap_med) / evebitda_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of evebitda_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_evebitda_peer_mcap_bucket_dist_accel_63d_3d_v066_signal(evebitda, evebitda_mcap_med, closeadj):
    base = (evebitda - evebitda_mcap_med) / evebitda_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of evebitda_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_evebitda_peer_mcap_bucket_dist_accel_126d_3d_v067_signal(evebitda, evebitda_mcap_med, closeadj):
    base = (evebitda - evebitda_mcap_med) / evebitda_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of evebitda_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_evebitda_peer_mcap_bucket_dist_accel_252d_3d_v068_signal(evebitda, evebitda_mcap_med, closeadj):
    base = (evebitda - evebitda_mcap_med) / evebitda_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of evebitda_peer_sector_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_sector_pctile_accel_21d_3d_v069_signal(evebitda_sector_pctile, closeadj):
    base = evebitda_sector_pctile
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of evebitda_peer_sector_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_sector_pctile_accel_63d_3d_v070_signal(evebitda_sector_pctile, closeadj):
    base = evebitda_sector_pctile
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of evebitda_peer_sector_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_sector_pctile_accel_126d_3d_v071_signal(evebitda_sector_pctile, closeadj):
    base = evebitda_sector_pctile
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of evebitda_peer_sector_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_sector_pctile_accel_252d_3d_v072_signal(evebitda_sector_pctile, closeadj):
    base = evebitda_sector_pctile
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of evebitda_peer_industry_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_industry_pctile_accel_21d_3d_v073_signal(evebitda_industry_pctile, closeadj):
    base = evebitda_industry_pctile
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of evebitda_peer_industry_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_industry_pctile_accel_63d_3d_v074_signal(evebitda_industry_pctile, closeadj):
    base = evebitda_industry_pctile
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of evebitda_peer_industry_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_industry_pctile_accel_126d_3d_v075_signal(evebitda_industry_pctile, closeadj):
    base = evebitda_industry_pctile
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of evebitda_peer_industry_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_industry_pctile_accel_252d_3d_v076_signal(evebitda_industry_pctile, closeadj):
    base = evebitda_industry_pctile
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of pe_lvl
def f073erm_f073_earnings_multiples_pe_lvl_slopez_21d_z126_3d_v077_signal(pe, closeadj):
    base = pe
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of pe_lvl
def f073erm_f073_earnings_multiples_pe_lvl_slopez_63d_z252_3d_v078_signal(pe, closeadj):
    base = pe
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of pe_lvl
def f073erm_f073_earnings_multiples_pe_lvl_slopez_126d_z252_3d_v079_signal(pe, closeadj):
    base = pe
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of pe_lvl
def f073erm_f073_earnings_multiples_pe_lvl_slopez_252d_z504_3d_v080_signal(pe, closeadj):
    base = pe
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of pe1_lvl
def f073erm_f073_earnings_multiples_pe1_lvl_slopez_21d_z126_3d_v081_signal(pe1, closeadj):
    base = pe1
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of pe1_lvl
def f073erm_f073_earnings_multiples_pe1_lvl_slopez_63d_z252_3d_v082_signal(pe1, closeadj):
    base = pe1
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of pe1_lvl
def f073erm_f073_earnings_multiples_pe1_lvl_slopez_126d_z252_3d_v083_signal(pe1, closeadj):
    base = pe1
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of pe1_lvl
def f073erm_f073_earnings_multiples_pe1_lvl_slopez_252d_z504_3d_v084_signal(pe1, closeadj):
    base = pe1
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of evebit_lvl
def f073erm_f073_earnings_multiples_evebit_lvl_slopez_21d_z126_3d_v085_signal(evebit, closeadj):
    base = evebit
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of evebit_lvl
def f073erm_f073_earnings_multiples_evebit_lvl_slopez_63d_z252_3d_v086_signal(evebit, closeadj):
    base = evebit
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of evebit_lvl
def f073erm_f073_earnings_multiples_evebit_lvl_slopez_126d_z252_3d_v087_signal(evebit, closeadj):
    base = evebit
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of evebit_lvl
def f073erm_f073_earnings_multiples_evebit_lvl_slopez_252d_z504_3d_v088_signal(evebit, closeadj):
    base = evebit
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of evebitda_lvl
def f073erm_f073_earnings_multiples_evebitda_lvl_slopez_21d_z126_3d_v089_signal(evebitda, closeadj):
    base = evebitda
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of evebitda_lvl
def f073erm_f073_earnings_multiples_evebitda_lvl_slopez_63d_z252_3d_v090_signal(evebitda, closeadj):
    base = evebitda
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of evebitda_lvl
def f073erm_f073_earnings_multiples_evebitda_lvl_slopez_126d_z252_3d_v091_signal(evebitda, closeadj):
    base = evebitda
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of evebitda_lvl
def f073erm_f073_earnings_multiples_evebitda_lvl_slopez_252d_z504_3d_v092_signal(evebitda, closeadj):
    base = evebitda
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of earn_yield
def f073erm_f073_earnings_multiples_earn_yield_slopez_21d_z126_3d_v093_signal(eps, close, closeadj):
    base = eps / close.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of earn_yield
def f073erm_f073_earnings_multiples_earn_yield_slopez_63d_z252_3d_v094_signal(eps, close, closeadj):
    base = eps / close.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of earn_yield
def f073erm_f073_earnings_multiples_earn_yield_slopez_126d_z252_3d_v095_signal(eps, close, closeadj):
    base = eps / close.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of earn_yield
def f073erm_f073_earnings_multiples_earn_yield_slopez_252d_z504_3d_v096_signal(eps, close, closeadj):
    base = eps / close.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of pe_calc
def f073erm_f073_earnings_multiples_pe_calc_slopez_21d_z126_3d_v097_signal(close, eps, closeadj):
    base = _f073_pe(close, eps)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of pe_calc
def f073erm_f073_earnings_multiples_pe_calc_slopez_63d_z252_3d_v098_signal(close, eps, closeadj):
    base = _f073_pe(close, eps)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of pe_calc
def f073erm_f073_earnings_multiples_pe_calc_slopez_126d_z252_3d_v099_signal(close, eps, closeadj):
    base = _f073_pe(close, eps)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of pe_calc
def f073erm_f073_earnings_multiples_pe_calc_slopez_252d_z504_3d_v100_signal(close, eps, closeadj):
    base = _f073_pe(close, eps)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ebit_yield
def f073erm_f073_earnings_multiples_ebit_yield_slopez_21d_z126_3d_v101_signal(ebit, ev, closeadj):
    base = ebit / ev.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ebit_yield
def f073erm_f073_earnings_multiples_ebit_yield_slopez_63d_z252_3d_v102_signal(ebit, ev, closeadj):
    base = ebit / ev.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ebit_yield
def f073erm_f073_earnings_multiples_ebit_yield_slopez_126d_z252_3d_v103_signal(ebit, ev, closeadj):
    base = ebit / ev.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ebit_yield
def f073erm_f073_earnings_multiples_ebit_yield_slopez_252d_z504_3d_v104_signal(ebit, ev, closeadj):
    base = ebit / ev.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of pe_peer_sector_dist
def f073erm_f073_earnings_multiples_pe_peer_sector_dist_slopez_21d_z126_3d_v105_signal(pe, pe_sector_med, closeadj):
    base = (pe - pe_sector_med) / pe_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of pe_peer_sector_dist
def f073erm_f073_earnings_multiples_pe_peer_sector_dist_slopez_63d_z252_3d_v106_signal(pe, pe_sector_med, closeadj):
    base = (pe - pe_sector_med) / pe_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of pe_peer_sector_dist
def f073erm_f073_earnings_multiples_pe_peer_sector_dist_slopez_126d_z252_3d_v107_signal(pe, pe_sector_med, closeadj):
    base = (pe - pe_sector_med) / pe_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of pe_peer_sector_dist
def f073erm_f073_earnings_multiples_pe_peer_sector_dist_slopez_252d_z504_3d_v108_signal(pe, pe_sector_med, closeadj):
    base = (pe - pe_sector_med) / pe_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of pe_peer_sector_z
def f073erm_f073_earnings_multiples_pe_peer_sector_z_slopez_21d_z126_3d_v109_signal(pe, pe_sector_med, pe_sector_std, closeadj):
    base = (pe - pe_sector_med) / pe_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of pe_peer_sector_z
def f073erm_f073_earnings_multiples_pe_peer_sector_z_slopez_63d_z252_3d_v110_signal(pe, pe_sector_med, pe_sector_std, closeadj):
    base = (pe - pe_sector_med) / pe_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of pe_peer_sector_z
def f073erm_f073_earnings_multiples_pe_peer_sector_z_slopez_126d_z252_3d_v111_signal(pe, pe_sector_med, pe_sector_std, closeadj):
    base = (pe - pe_sector_med) / pe_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of pe_peer_sector_z
def f073erm_f073_earnings_multiples_pe_peer_sector_z_slopez_252d_z504_3d_v112_signal(pe, pe_sector_med, pe_sector_std, closeadj):
    base = (pe - pe_sector_med) / pe_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of pe_peer_industry_dist
def f073erm_f073_earnings_multiples_pe_peer_industry_dist_slopez_21d_z126_3d_v113_signal(pe, pe_industry_med, closeadj):
    base = (pe - pe_industry_med) / pe_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of pe_peer_industry_dist
def f073erm_f073_earnings_multiples_pe_peer_industry_dist_slopez_63d_z252_3d_v114_signal(pe, pe_industry_med, closeadj):
    base = (pe - pe_industry_med) / pe_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of pe_peer_industry_dist
def f073erm_f073_earnings_multiples_pe_peer_industry_dist_slopez_126d_z252_3d_v115_signal(pe, pe_industry_med, closeadj):
    base = (pe - pe_industry_med) / pe_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of pe_peer_industry_dist
def f073erm_f073_earnings_multiples_pe_peer_industry_dist_slopez_252d_z504_3d_v116_signal(pe, pe_industry_med, closeadj):
    base = (pe - pe_industry_med) / pe_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of pe_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_pe_peer_mcap_bucket_dist_slopez_21d_z126_3d_v117_signal(pe, pe_mcap_med, closeadj):
    base = (pe - pe_mcap_med) / pe_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of pe_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_pe_peer_mcap_bucket_dist_slopez_63d_z252_3d_v118_signal(pe, pe_mcap_med, closeadj):
    base = (pe - pe_mcap_med) / pe_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of pe_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_pe_peer_mcap_bucket_dist_slopez_126d_z252_3d_v119_signal(pe, pe_mcap_med, closeadj):
    base = (pe - pe_mcap_med) / pe_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of pe_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_pe_peer_mcap_bucket_dist_slopez_252d_z504_3d_v120_signal(pe, pe_mcap_med, closeadj):
    base = (pe - pe_mcap_med) / pe_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of pe_peer_sector_pctile
def f073erm_f073_earnings_multiples_pe_peer_sector_pctile_slopez_21d_z126_3d_v121_signal(pe_sector_pctile, closeadj):
    base = pe_sector_pctile
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of pe_peer_sector_pctile
def f073erm_f073_earnings_multiples_pe_peer_sector_pctile_slopez_63d_z252_3d_v122_signal(pe_sector_pctile, closeadj):
    base = pe_sector_pctile
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of pe_peer_sector_pctile
def f073erm_f073_earnings_multiples_pe_peer_sector_pctile_slopez_126d_z252_3d_v123_signal(pe_sector_pctile, closeadj):
    base = pe_sector_pctile
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of pe_peer_sector_pctile
def f073erm_f073_earnings_multiples_pe_peer_sector_pctile_slopez_252d_z504_3d_v124_signal(pe_sector_pctile, closeadj):
    base = pe_sector_pctile
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of pe_peer_industry_pctile
def f073erm_f073_earnings_multiples_pe_peer_industry_pctile_slopez_21d_z126_3d_v125_signal(pe_industry_pctile, closeadj):
    base = pe_industry_pctile
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of pe_peer_industry_pctile
def f073erm_f073_earnings_multiples_pe_peer_industry_pctile_slopez_63d_z252_3d_v126_signal(pe_industry_pctile, closeadj):
    base = pe_industry_pctile
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of pe_peer_industry_pctile
def f073erm_f073_earnings_multiples_pe_peer_industry_pctile_slopez_126d_z252_3d_v127_signal(pe_industry_pctile, closeadj):
    base = pe_industry_pctile
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of pe_peer_industry_pctile
def f073erm_f073_earnings_multiples_pe_peer_industry_pctile_slopez_252d_z504_3d_v128_signal(pe_industry_pctile, closeadj):
    base = pe_industry_pctile
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of evebitda_peer_sector_dist
def f073erm_f073_earnings_multiples_evebitda_peer_sector_dist_slopez_21d_z126_3d_v129_signal(evebitda, evebitda_sector_med, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of evebitda_peer_sector_dist
def f073erm_f073_earnings_multiples_evebitda_peer_sector_dist_slopez_63d_z252_3d_v130_signal(evebitda, evebitda_sector_med, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of evebitda_peer_sector_dist
def f073erm_f073_earnings_multiples_evebitda_peer_sector_dist_slopez_126d_z252_3d_v131_signal(evebitda, evebitda_sector_med, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of evebitda_peer_sector_dist
def f073erm_f073_earnings_multiples_evebitda_peer_sector_dist_slopez_252d_z504_3d_v132_signal(evebitda, evebitda_sector_med, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of evebitda_peer_sector_z
def f073erm_f073_earnings_multiples_evebitda_peer_sector_z_slopez_21d_z126_3d_v133_signal(evebitda, evebitda_sector_med, evebitda_sector_std, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of evebitda_peer_sector_z
def f073erm_f073_earnings_multiples_evebitda_peer_sector_z_slopez_63d_z252_3d_v134_signal(evebitda, evebitda_sector_med, evebitda_sector_std, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of evebitda_peer_sector_z
def f073erm_f073_earnings_multiples_evebitda_peer_sector_z_slopez_126d_z252_3d_v135_signal(evebitda, evebitda_sector_med, evebitda_sector_std, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of evebitda_peer_sector_z
def f073erm_f073_earnings_multiples_evebitda_peer_sector_z_slopez_252d_z504_3d_v136_signal(evebitda, evebitda_sector_med, evebitda_sector_std, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of evebitda_peer_industry_dist
def f073erm_f073_earnings_multiples_evebitda_peer_industry_dist_slopez_21d_z126_3d_v137_signal(evebitda, evebitda_industry_med, closeadj):
    base = (evebitda - evebitda_industry_med) / evebitda_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of evebitda_peer_industry_dist
def f073erm_f073_earnings_multiples_evebitda_peer_industry_dist_slopez_63d_z252_3d_v138_signal(evebitda, evebitda_industry_med, closeadj):
    base = (evebitda - evebitda_industry_med) / evebitda_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of evebitda_peer_industry_dist
def f073erm_f073_earnings_multiples_evebitda_peer_industry_dist_slopez_126d_z252_3d_v139_signal(evebitda, evebitda_industry_med, closeadj):
    base = (evebitda - evebitda_industry_med) / evebitda_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of evebitda_peer_industry_dist
def f073erm_f073_earnings_multiples_evebitda_peer_industry_dist_slopez_252d_z504_3d_v140_signal(evebitda, evebitda_industry_med, closeadj):
    base = (evebitda - evebitda_industry_med) / evebitda_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of evebitda_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_evebitda_peer_mcap_bucket_dist_slopez_21d_z126_3d_v141_signal(evebitda, evebitda_mcap_med, closeadj):
    base = (evebitda - evebitda_mcap_med) / evebitda_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of evebitda_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_evebitda_peer_mcap_bucket_dist_slopez_63d_z252_3d_v142_signal(evebitda, evebitda_mcap_med, closeadj):
    base = (evebitda - evebitda_mcap_med) / evebitda_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of evebitda_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_evebitda_peer_mcap_bucket_dist_slopez_126d_z252_3d_v143_signal(evebitda, evebitda_mcap_med, closeadj):
    base = (evebitda - evebitda_mcap_med) / evebitda_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of evebitda_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_evebitda_peer_mcap_bucket_dist_slopez_252d_z504_3d_v144_signal(evebitda, evebitda_mcap_med, closeadj):
    base = (evebitda - evebitda_mcap_med) / evebitda_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of evebitda_peer_sector_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_sector_pctile_slopez_21d_z126_3d_v145_signal(evebitda_sector_pctile, closeadj):
    base = evebitda_sector_pctile
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of evebitda_peer_sector_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_sector_pctile_slopez_63d_z252_3d_v146_signal(evebitda_sector_pctile, closeadj):
    base = evebitda_sector_pctile
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of evebitda_peer_sector_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_sector_pctile_slopez_126d_z252_3d_v147_signal(evebitda_sector_pctile, closeadj):
    base = evebitda_sector_pctile
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of evebitda_peer_sector_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_sector_pctile_slopez_252d_z504_3d_v148_signal(evebitda_sector_pctile, closeadj):
    base = evebitda_sector_pctile
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of evebitda_peer_industry_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_industry_pctile_slopez_21d_z126_3d_v149_signal(evebitda_industry_pctile, closeadj):
    base = evebitda_industry_pctile
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of evebitda_peer_industry_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_industry_pctile_slopez_63d_z252_3d_v150_signal(evebitda_industry_pctile, closeadj):
    base = evebitda_industry_pctile
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of evebitda_peer_industry_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_industry_pctile_slopez_126d_z252_3d_v151_signal(evebitda_industry_pctile, closeadj):
    base = evebitda_industry_pctile
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of evebitda_peer_industry_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_industry_pctile_slopez_252d_z504_3d_v152_signal(evebitda_industry_pctile, closeadj):
    base = evebitda_industry_pctile
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of pe_lvl
def f073erm_f073_earnings_multiples_pe_lvl_jerk_21d_3d_v153_signal(pe, closeadj):
    base = pe
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of pe_lvl
def f073erm_f073_earnings_multiples_pe_lvl_jerk_63d_3d_v154_signal(pe, closeadj):
    base = pe
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of pe_lvl
def f073erm_f073_earnings_multiples_pe_lvl_jerk_126d_3d_v155_signal(pe, closeadj):
    base = pe
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of pe1_lvl
def f073erm_f073_earnings_multiples_pe1_lvl_jerk_21d_3d_v156_signal(pe1, closeadj):
    base = pe1
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of pe1_lvl
def f073erm_f073_earnings_multiples_pe1_lvl_jerk_63d_3d_v157_signal(pe1, closeadj):
    base = pe1
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of pe1_lvl
def f073erm_f073_earnings_multiples_pe1_lvl_jerk_126d_3d_v158_signal(pe1, closeadj):
    base = pe1
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of evebit_lvl
def f073erm_f073_earnings_multiples_evebit_lvl_jerk_21d_3d_v159_signal(evebit, closeadj):
    base = evebit
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of evebit_lvl
def f073erm_f073_earnings_multiples_evebit_lvl_jerk_63d_3d_v160_signal(evebit, closeadj):
    base = evebit
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of evebit_lvl
def f073erm_f073_earnings_multiples_evebit_lvl_jerk_126d_3d_v161_signal(evebit, closeadj):
    base = evebit
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of evebitda_lvl
def f073erm_f073_earnings_multiples_evebitda_lvl_jerk_21d_3d_v162_signal(evebitda, closeadj):
    base = evebitda
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of evebitda_lvl
def f073erm_f073_earnings_multiples_evebitda_lvl_jerk_63d_3d_v163_signal(evebitda, closeadj):
    base = evebitda
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of evebitda_lvl
def f073erm_f073_earnings_multiples_evebitda_lvl_jerk_126d_3d_v164_signal(evebitda, closeadj):
    base = evebitda
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of earn_yield
def f073erm_f073_earnings_multiples_earn_yield_jerk_21d_3d_v165_signal(eps, close, closeadj):
    base = eps / close.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of earn_yield
def f073erm_f073_earnings_multiples_earn_yield_jerk_63d_3d_v166_signal(eps, close, closeadj):
    base = eps / close.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of earn_yield
def f073erm_f073_earnings_multiples_earn_yield_jerk_126d_3d_v167_signal(eps, close, closeadj):
    base = eps / close.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of pe_calc
def f073erm_f073_earnings_multiples_pe_calc_jerk_21d_3d_v168_signal(close, eps, closeadj):
    base = _f073_pe(close, eps)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of pe_calc
def f073erm_f073_earnings_multiples_pe_calc_jerk_63d_3d_v169_signal(close, eps, closeadj):
    base = _f073_pe(close, eps)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of pe_calc
def f073erm_f073_earnings_multiples_pe_calc_jerk_126d_3d_v170_signal(close, eps, closeadj):
    base = _f073_pe(close, eps)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ebit_yield
def f073erm_f073_earnings_multiples_ebit_yield_jerk_21d_3d_v171_signal(ebit, ev, closeadj):
    base = ebit / ev.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ebit_yield
def f073erm_f073_earnings_multiples_ebit_yield_jerk_63d_3d_v172_signal(ebit, ev, closeadj):
    base = ebit / ev.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ebit_yield
def f073erm_f073_earnings_multiples_ebit_yield_jerk_126d_3d_v173_signal(ebit, ev, closeadj):
    base = ebit / ev.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of pe_peer_sector_dist
def f073erm_f073_earnings_multiples_pe_peer_sector_dist_jerk_21d_3d_v174_signal(pe, pe_sector_med, closeadj):
    base = (pe - pe_sector_med) / pe_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of pe_peer_sector_dist
def f073erm_f073_earnings_multiples_pe_peer_sector_dist_jerk_63d_3d_v175_signal(pe, pe_sector_med, closeadj):
    base = (pe - pe_sector_med) / pe_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of pe_peer_sector_dist
def f073erm_f073_earnings_multiples_pe_peer_sector_dist_jerk_126d_3d_v176_signal(pe, pe_sector_med, closeadj):
    base = (pe - pe_sector_med) / pe_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of pe_peer_sector_z
def f073erm_f073_earnings_multiples_pe_peer_sector_z_jerk_21d_3d_v177_signal(pe, pe_sector_med, pe_sector_std, closeadj):
    base = (pe - pe_sector_med) / pe_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of pe_peer_sector_z
def f073erm_f073_earnings_multiples_pe_peer_sector_z_jerk_63d_3d_v178_signal(pe, pe_sector_med, pe_sector_std, closeadj):
    base = (pe - pe_sector_med) / pe_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of pe_peer_sector_z
def f073erm_f073_earnings_multiples_pe_peer_sector_z_jerk_126d_3d_v179_signal(pe, pe_sector_med, pe_sector_std, closeadj):
    base = (pe - pe_sector_med) / pe_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of pe_peer_industry_dist
def f073erm_f073_earnings_multiples_pe_peer_industry_dist_jerk_21d_3d_v180_signal(pe, pe_industry_med, closeadj):
    base = (pe - pe_industry_med) / pe_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of pe_peer_industry_dist
def f073erm_f073_earnings_multiples_pe_peer_industry_dist_jerk_63d_3d_v181_signal(pe, pe_industry_med, closeadj):
    base = (pe - pe_industry_med) / pe_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of pe_peer_industry_dist
def f073erm_f073_earnings_multiples_pe_peer_industry_dist_jerk_126d_3d_v182_signal(pe, pe_industry_med, closeadj):
    base = (pe - pe_industry_med) / pe_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of pe_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_pe_peer_mcap_bucket_dist_jerk_21d_3d_v183_signal(pe, pe_mcap_med, closeadj):
    base = (pe - pe_mcap_med) / pe_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of pe_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_pe_peer_mcap_bucket_dist_jerk_63d_3d_v184_signal(pe, pe_mcap_med, closeadj):
    base = (pe - pe_mcap_med) / pe_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of pe_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_pe_peer_mcap_bucket_dist_jerk_126d_3d_v185_signal(pe, pe_mcap_med, closeadj):
    base = (pe - pe_mcap_med) / pe_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of pe_peer_sector_pctile
def f073erm_f073_earnings_multiples_pe_peer_sector_pctile_jerk_21d_3d_v186_signal(pe_sector_pctile, closeadj):
    base = pe_sector_pctile
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of pe_peer_sector_pctile
def f073erm_f073_earnings_multiples_pe_peer_sector_pctile_jerk_63d_3d_v187_signal(pe_sector_pctile, closeadj):
    base = pe_sector_pctile
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of pe_peer_sector_pctile
def f073erm_f073_earnings_multiples_pe_peer_sector_pctile_jerk_126d_3d_v188_signal(pe_sector_pctile, closeadj):
    base = pe_sector_pctile
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of pe_peer_industry_pctile
def f073erm_f073_earnings_multiples_pe_peer_industry_pctile_jerk_21d_3d_v189_signal(pe_industry_pctile, closeadj):
    base = pe_industry_pctile
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of pe_peer_industry_pctile
def f073erm_f073_earnings_multiples_pe_peer_industry_pctile_jerk_63d_3d_v190_signal(pe_industry_pctile, closeadj):
    base = pe_industry_pctile
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of pe_peer_industry_pctile
def f073erm_f073_earnings_multiples_pe_peer_industry_pctile_jerk_126d_3d_v191_signal(pe_industry_pctile, closeadj):
    base = pe_industry_pctile
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of evebitda_peer_sector_dist
def f073erm_f073_earnings_multiples_evebitda_peer_sector_dist_jerk_21d_3d_v192_signal(evebitda, evebitda_sector_med, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of evebitda_peer_sector_dist
def f073erm_f073_earnings_multiples_evebitda_peer_sector_dist_jerk_63d_3d_v193_signal(evebitda, evebitda_sector_med, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of evebitda_peer_sector_dist
def f073erm_f073_earnings_multiples_evebitda_peer_sector_dist_jerk_126d_3d_v194_signal(evebitda, evebitda_sector_med, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of evebitda_peer_sector_z
def f073erm_f073_earnings_multiples_evebitda_peer_sector_z_jerk_21d_3d_v195_signal(evebitda, evebitda_sector_med, evebitda_sector_std, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of evebitda_peer_sector_z
def f073erm_f073_earnings_multiples_evebitda_peer_sector_z_jerk_63d_3d_v196_signal(evebitda, evebitda_sector_med, evebitda_sector_std, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of evebitda_peer_sector_z
def f073erm_f073_earnings_multiples_evebitda_peer_sector_z_jerk_126d_3d_v197_signal(evebitda, evebitda_sector_med, evebitda_sector_std, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of evebitda_peer_industry_dist
def f073erm_f073_earnings_multiples_evebitda_peer_industry_dist_jerk_21d_3d_v198_signal(evebitda, evebitda_industry_med, closeadj):
    base = (evebitda - evebitda_industry_med) / evebitda_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of evebitda_peer_industry_dist
def f073erm_f073_earnings_multiples_evebitda_peer_industry_dist_jerk_63d_3d_v199_signal(evebitda, evebitda_industry_med, closeadj):
    base = (evebitda - evebitda_industry_med) / evebitda_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of evebitda_peer_industry_dist
def f073erm_f073_earnings_multiples_evebitda_peer_industry_dist_jerk_126d_3d_v200_signal(evebitda, evebitda_industry_med, closeadj):
    base = (evebitda - evebitda_industry_med) / evebitda_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

