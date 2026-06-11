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


# 63d z-score of pe_lvl
def f073erm_f073_earnings_multiples_pe_lvl_z_63d_base_v076_signal(pe, closeadj):
    base = pe
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of pe_lvl
def f073erm_f073_earnings_multiples_pe_lvl_z_126d_base_v077_signal(pe, closeadj):
    base = pe
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of pe_lvl
def f073erm_f073_earnings_multiples_pe_lvl_z_252d_base_v078_signal(pe, closeadj):
    base = pe
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of pe_lvl
def f073erm_f073_earnings_multiples_pe_lvl_z_504d_base_v079_signal(pe, closeadj):
    base = pe
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of pe1_lvl
def f073erm_f073_earnings_multiples_pe1_lvl_z_63d_base_v080_signal(pe1, closeadj):
    base = pe1
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of pe1_lvl
def f073erm_f073_earnings_multiples_pe1_lvl_z_126d_base_v081_signal(pe1, closeadj):
    base = pe1
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of pe1_lvl
def f073erm_f073_earnings_multiples_pe1_lvl_z_252d_base_v082_signal(pe1, closeadj):
    base = pe1
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of pe1_lvl
def f073erm_f073_earnings_multiples_pe1_lvl_z_504d_base_v083_signal(pe1, closeadj):
    base = pe1
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of evebit_lvl
def f073erm_f073_earnings_multiples_evebit_lvl_z_63d_base_v084_signal(evebit, closeadj):
    base = evebit
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of evebit_lvl
def f073erm_f073_earnings_multiples_evebit_lvl_z_126d_base_v085_signal(evebit, closeadj):
    base = evebit
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of evebit_lvl
def f073erm_f073_earnings_multiples_evebit_lvl_z_252d_base_v086_signal(evebit, closeadj):
    base = evebit
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of evebit_lvl
def f073erm_f073_earnings_multiples_evebit_lvl_z_504d_base_v087_signal(evebit, closeadj):
    base = evebit
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of evebitda_lvl
def f073erm_f073_earnings_multiples_evebitda_lvl_z_63d_base_v088_signal(evebitda, closeadj):
    base = evebitda
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of evebitda_lvl
def f073erm_f073_earnings_multiples_evebitda_lvl_z_126d_base_v089_signal(evebitda, closeadj):
    base = evebitda
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of evebitda_lvl
def f073erm_f073_earnings_multiples_evebitda_lvl_z_252d_base_v090_signal(evebitda, closeadj):
    base = evebitda
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of evebitda_lvl
def f073erm_f073_earnings_multiples_evebitda_lvl_z_504d_base_v091_signal(evebitda, closeadj):
    base = evebitda
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of earn_yield
def f073erm_f073_earnings_multiples_earn_yield_z_63d_base_v092_signal(eps, close, closeadj):
    base = eps / close.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of earn_yield
def f073erm_f073_earnings_multiples_earn_yield_z_126d_base_v093_signal(eps, close, closeadj):
    base = eps / close.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of earn_yield
def f073erm_f073_earnings_multiples_earn_yield_z_252d_base_v094_signal(eps, close, closeadj):
    base = eps / close.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of earn_yield
def f073erm_f073_earnings_multiples_earn_yield_z_504d_base_v095_signal(eps, close, closeadj):
    base = eps / close.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of pe_calc
def f073erm_f073_earnings_multiples_pe_calc_z_63d_base_v096_signal(close, eps, closeadj):
    base = _f073_pe(close, eps)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of pe_calc
def f073erm_f073_earnings_multiples_pe_calc_z_126d_base_v097_signal(close, eps, closeadj):
    base = _f073_pe(close, eps)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of pe_calc
def f073erm_f073_earnings_multiples_pe_calc_z_252d_base_v098_signal(close, eps, closeadj):
    base = _f073_pe(close, eps)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of pe_calc
def f073erm_f073_earnings_multiples_pe_calc_z_504d_base_v099_signal(close, eps, closeadj):
    base = _f073_pe(close, eps)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ebit_yield
def f073erm_f073_earnings_multiples_ebit_yield_z_63d_base_v100_signal(ebit, ev, closeadj):
    base = ebit / ev.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ebit_yield
def f073erm_f073_earnings_multiples_ebit_yield_z_126d_base_v101_signal(ebit, ev, closeadj):
    base = ebit / ev.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ebit_yield
def f073erm_f073_earnings_multiples_ebit_yield_z_252d_base_v102_signal(ebit, ev, closeadj):
    base = ebit / ev.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ebit_yield
def f073erm_f073_earnings_multiples_ebit_yield_z_504d_base_v103_signal(ebit, ev, closeadj):
    base = ebit / ev.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of pe_peer_sector_dist
def f073erm_f073_earnings_multiples_pe_peer_sector_dist_z_63d_base_v104_signal(pe, pe_sector_med, closeadj):
    base = (pe - pe_sector_med) / pe_sector_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of pe_peer_sector_dist
def f073erm_f073_earnings_multiples_pe_peer_sector_dist_z_126d_base_v105_signal(pe, pe_sector_med, closeadj):
    base = (pe - pe_sector_med) / pe_sector_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of pe_peer_sector_dist
def f073erm_f073_earnings_multiples_pe_peer_sector_dist_z_252d_base_v106_signal(pe, pe_sector_med, closeadj):
    base = (pe - pe_sector_med) / pe_sector_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of pe_peer_sector_dist
def f073erm_f073_earnings_multiples_pe_peer_sector_dist_z_504d_base_v107_signal(pe, pe_sector_med, closeadj):
    base = (pe - pe_sector_med) / pe_sector_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of pe_peer_sector_z
def f073erm_f073_earnings_multiples_pe_peer_sector_z_z_63d_base_v108_signal(pe, pe_sector_med, pe_sector_std, closeadj):
    base = (pe - pe_sector_med) / pe_sector_std.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of pe_peer_sector_z
def f073erm_f073_earnings_multiples_pe_peer_sector_z_z_126d_base_v109_signal(pe, pe_sector_med, pe_sector_std, closeadj):
    base = (pe - pe_sector_med) / pe_sector_std.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of pe_peer_sector_z
def f073erm_f073_earnings_multiples_pe_peer_sector_z_z_252d_base_v110_signal(pe, pe_sector_med, pe_sector_std, closeadj):
    base = (pe - pe_sector_med) / pe_sector_std.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of pe_peer_sector_z
def f073erm_f073_earnings_multiples_pe_peer_sector_z_z_504d_base_v111_signal(pe, pe_sector_med, pe_sector_std, closeadj):
    base = (pe - pe_sector_med) / pe_sector_std.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of pe_peer_industry_dist
def f073erm_f073_earnings_multiples_pe_peer_industry_dist_z_63d_base_v112_signal(pe, pe_industry_med, closeadj):
    base = (pe - pe_industry_med) / pe_industry_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of pe_peer_industry_dist
def f073erm_f073_earnings_multiples_pe_peer_industry_dist_z_126d_base_v113_signal(pe, pe_industry_med, closeadj):
    base = (pe - pe_industry_med) / pe_industry_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of pe_peer_industry_dist
def f073erm_f073_earnings_multiples_pe_peer_industry_dist_z_252d_base_v114_signal(pe, pe_industry_med, closeadj):
    base = (pe - pe_industry_med) / pe_industry_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of pe_peer_industry_dist
def f073erm_f073_earnings_multiples_pe_peer_industry_dist_z_504d_base_v115_signal(pe, pe_industry_med, closeadj):
    base = (pe - pe_industry_med) / pe_industry_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of pe_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_pe_peer_mcap_bucket_dist_z_63d_base_v116_signal(pe, pe_mcap_med, closeadj):
    base = (pe - pe_mcap_med) / pe_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of pe_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_pe_peer_mcap_bucket_dist_z_126d_base_v117_signal(pe, pe_mcap_med, closeadj):
    base = (pe - pe_mcap_med) / pe_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of pe_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_pe_peer_mcap_bucket_dist_z_252d_base_v118_signal(pe, pe_mcap_med, closeadj):
    base = (pe - pe_mcap_med) / pe_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of pe_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_pe_peer_mcap_bucket_dist_z_504d_base_v119_signal(pe, pe_mcap_med, closeadj):
    base = (pe - pe_mcap_med) / pe_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of pe_peer_sector_pctile
def f073erm_f073_earnings_multiples_pe_peer_sector_pctile_z_63d_base_v120_signal(pe_sector_pctile, closeadj):
    base = pe_sector_pctile
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of pe_peer_sector_pctile
def f073erm_f073_earnings_multiples_pe_peer_sector_pctile_z_126d_base_v121_signal(pe_sector_pctile, closeadj):
    base = pe_sector_pctile
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of pe_peer_sector_pctile
def f073erm_f073_earnings_multiples_pe_peer_sector_pctile_z_252d_base_v122_signal(pe_sector_pctile, closeadj):
    base = pe_sector_pctile
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of pe_peer_sector_pctile
def f073erm_f073_earnings_multiples_pe_peer_sector_pctile_z_504d_base_v123_signal(pe_sector_pctile, closeadj):
    base = pe_sector_pctile
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of pe_peer_industry_pctile
def f073erm_f073_earnings_multiples_pe_peer_industry_pctile_z_63d_base_v124_signal(pe_industry_pctile, closeadj):
    base = pe_industry_pctile
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of pe_peer_industry_pctile
def f073erm_f073_earnings_multiples_pe_peer_industry_pctile_z_126d_base_v125_signal(pe_industry_pctile, closeadj):
    base = pe_industry_pctile
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of pe_peer_industry_pctile
def f073erm_f073_earnings_multiples_pe_peer_industry_pctile_z_252d_base_v126_signal(pe_industry_pctile, closeadj):
    base = pe_industry_pctile
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of pe_peer_industry_pctile
def f073erm_f073_earnings_multiples_pe_peer_industry_pctile_z_504d_base_v127_signal(pe_industry_pctile, closeadj):
    base = pe_industry_pctile
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of evebitda_peer_sector_dist
def f073erm_f073_earnings_multiples_evebitda_peer_sector_dist_z_63d_base_v128_signal(evebitda, evebitda_sector_med, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of evebitda_peer_sector_dist
def f073erm_f073_earnings_multiples_evebitda_peer_sector_dist_z_126d_base_v129_signal(evebitda, evebitda_sector_med, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of evebitda_peer_sector_dist
def f073erm_f073_earnings_multiples_evebitda_peer_sector_dist_z_252d_base_v130_signal(evebitda, evebitda_sector_med, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of evebitda_peer_sector_dist
def f073erm_f073_earnings_multiples_evebitda_peer_sector_dist_z_504d_base_v131_signal(evebitda, evebitda_sector_med, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of evebitda_peer_sector_z
def f073erm_f073_earnings_multiples_evebitda_peer_sector_z_z_63d_base_v132_signal(evebitda, evebitda_sector_med, evebitda_sector_std, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_std.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of evebitda_peer_sector_z
def f073erm_f073_earnings_multiples_evebitda_peer_sector_z_z_126d_base_v133_signal(evebitda, evebitda_sector_med, evebitda_sector_std, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_std.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of evebitda_peer_sector_z
def f073erm_f073_earnings_multiples_evebitda_peer_sector_z_z_252d_base_v134_signal(evebitda, evebitda_sector_med, evebitda_sector_std, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_std.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of evebitda_peer_sector_z
def f073erm_f073_earnings_multiples_evebitda_peer_sector_z_z_504d_base_v135_signal(evebitda, evebitda_sector_med, evebitda_sector_std, closeadj):
    base = (evebitda - evebitda_sector_med) / evebitda_sector_std.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of evebitda_peer_industry_dist
def f073erm_f073_earnings_multiples_evebitda_peer_industry_dist_z_63d_base_v136_signal(evebitda, evebitda_industry_med, closeadj):
    base = (evebitda - evebitda_industry_med) / evebitda_industry_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of evebitda_peer_industry_dist
def f073erm_f073_earnings_multiples_evebitda_peer_industry_dist_z_126d_base_v137_signal(evebitda, evebitda_industry_med, closeadj):
    base = (evebitda - evebitda_industry_med) / evebitda_industry_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of evebitda_peer_industry_dist
def f073erm_f073_earnings_multiples_evebitda_peer_industry_dist_z_252d_base_v138_signal(evebitda, evebitda_industry_med, closeadj):
    base = (evebitda - evebitda_industry_med) / evebitda_industry_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of evebitda_peer_industry_dist
def f073erm_f073_earnings_multiples_evebitda_peer_industry_dist_z_504d_base_v139_signal(evebitda, evebitda_industry_med, closeadj):
    base = (evebitda - evebitda_industry_med) / evebitda_industry_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of evebitda_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_evebitda_peer_mcap_bucket_dist_z_63d_base_v140_signal(evebitda, evebitda_mcap_med, closeadj):
    base = (evebitda - evebitda_mcap_med) / evebitda_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of evebitda_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_evebitda_peer_mcap_bucket_dist_z_126d_base_v141_signal(evebitda, evebitda_mcap_med, closeadj):
    base = (evebitda - evebitda_mcap_med) / evebitda_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of evebitda_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_evebitda_peer_mcap_bucket_dist_z_252d_base_v142_signal(evebitda, evebitda_mcap_med, closeadj):
    base = (evebitda - evebitda_mcap_med) / evebitda_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of evebitda_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_evebitda_peer_mcap_bucket_dist_z_504d_base_v143_signal(evebitda, evebitda_mcap_med, closeadj):
    base = (evebitda - evebitda_mcap_med) / evebitda_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of evebitda_peer_sector_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_sector_pctile_z_63d_base_v144_signal(evebitda_sector_pctile, closeadj):
    base = evebitda_sector_pctile
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of evebitda_peer_sector_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_sector_pctile_z_126d_base_v145_signal(evebitda_sector_pctile, closeadj):
    base = evebitda_sector_pctile
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of evebitda_peer_sector_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_sector_pctile_z_252d_base_v146_signal(evebitda_sector_pctile, closeadj):
    base = evebitda_sector_pctile
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of evebitda_peer_sector_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_sector_pctile_z_504d_base_v147_signal(evebitda_sector_pctile, closeadj):
    base = evebitda_sector_pctile
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of evebitda_peer_industry_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_industry_pctile_z_63d_base_v148_signal(evebitda_industry_pctile, closeadj):
    base = evebitda_industry_pctile
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of evebitda_peer_industry_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_industry_pctile_z_126d_base_v149_signal(evebitda_industry_pctile, closeadj):
    base = evebitda_industry_pctile
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of evebitda_peer_industry_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_industry_pctile_z_252d_base_v150_signal(evebitda_industry_pctile, closeadj):
    base = evebitda_industry_pctile
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of evebitda_peer_industry_pctile
def f073erm_f073_earnings_multiples_evebitda_peer_industry_pctile_z_504d_base_v151_signal(evebitda_industry_pctile, closeadj):
    base = evebitda_industry_pctile
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of pe_lvl
def f073erm_f073_earnings_multiples_pe_lvl_distmax_252d_base_v152_signal(pe, closeadj):
    base = pe
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of pe_lvl
def f073erm_f073_earnings_multiples_pe_lvl_distmax_504d_base_v153_signal(pe, closeadj):
    base = pe
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of pe1_lvl
def f073erm_f073_earnings_multiples_pe1_lvl_distmax_252d_base_v154_signal(pe1, closeadj):
    base = pe1
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of pe1_lvl
def f073erm_f073_earnings_multiples_pe1_lvl_distmax_504d_base_v155_signal(pe1, closeadj):
    base = pe1
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of evebit_lvl
def f073erm_f073_earnings_multiples_evebit_lvl_distmax_252d_base_v156_signal(evebit, closeadj):
    base = evebit
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of evebit_lvl
def f073erm_f073_earnings_multiples_evebit_lvl_distmax_504d_base_v157_signal(evebit, closeadj):
    base = evebit
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of evebitda_lvl
def f073erm_f073_earnings_multiples_evebitda_lvl_distmax_252d_base_v158_signal(evebitda, closeadj):
    base = evebitda
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of evebitda_lvl
def f073erm_f073_earnings_multiples_evebitda_lvl_distmax_504d_base_v159_signal(evebitda, closeadj):
    base = evebitda
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of earn_yield
def f073erm_f073_earnings_multiples_earn_yield_distmax_252d_base_v160_signal(eps, close, closeadj):
    base = eps / close.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of earn_yield
def f073erm_f073_earnings_multiples_earn_yield_distmax_504d_base_v161_signal(eps, close, closeadj):
    base = eps / close.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of pe_calc
def f073erm_f073_earnings_multiples_pe_calc_distmax_252d_base_v162_signal(close, eps, closeadj):
    base = _f073_pe(close, eps)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of pe_calc
def f073erm_f073_earnings_multiples_pe_calc_distmax_504d_base_v163_signal(close, eps, closeadj):
    base = _f073_pe(close, eps)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ebit_yield
def f073erm_f073_earnings_multiples_ebit_yield_distmax_252d_base_v164_signal(ebit, ev, closeadj):
    base = ebit / ev.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ebit_yield
def f073erm_f073_earnings_multiples_ebit_yield_distmax_504d_base_v165_signal(ebit, ev, closeadj):
    base = ebit / ev.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of pe_peer_sector_dist
def f073erm_f073_earnings_multiples_pe_peer_sector_dist_distmax_252d_base_v166_signal(pe, pe_sector_med, closeadj):
    base = (pe - pe_sector_med) / pe_sector_med.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of pe_peer_sector_dist
def f073erm_f073_earnings_multiples_pe_peer_sector_dist_distmax_504d_base_v167_signal(pe, pe_sector_med, closeadj):
    base = (pe - pe_sector_med) / pe_sector_med.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of pe_peer_sector_z
def f073erm_f073_earnings_multiples_pe_peer_sector_z_distmax_252d_base_v168_signal(pe, pe_sector_med, pe_sector_std, closeadj):
    base = (pe - pe_sector_med) / pe_sector_std.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of pe_peer_sector_z
def f073erm_f073_earnings_multiples_pe_peer_sector_z_distmax_504d_base_v169_signal(pe, pe_sector_med, pe_sector_std, closeadj):
    base = (pe - pe_sector_med) / pe_sector_std.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of pe_peer_industry_dist
def f073erm_f073_earnings_multiples_pe_peer_industry_dist_distmax_252d_base_v170_signal(pe, pe_industry_med, closeadj):
    base = (pe - pe_industry_med) / pe_industry_med.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of pe_peer_industry_dist
def f073erm_f073_earnings_multiples_pe_peer_industry_dist_distmax_504d_base_v171_signal(pe, pe_industry_med, closeadj):
    base = (pe - pe_industry_med) / pe_industry_med.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of pe_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_pe_peer_mcap_bucket_dist_distmax_252d_base_v172_signal(pe, pe_mcap_med, closeadj):
    base = (pe - pe_mcap_med) / pe_mcap_med.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of pe_peer_mcap_bucket_dist
def f073erm_f073_earnings_multiples_pe_peer_mcap_bucket_dist_distmax_504d_base_v173_signal(pe, pe_mcap_med, closeadj):
    base = (pe - pe_mcap_med) / pe_mcap_med.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of pe_peer_sector_pctile
def f073erm_f073_earnings_multiples_pe_peer_sector_pctile_distmax_252d_base_v174_signal(pe_sector_pctile, closeadj):
    base = pe_sector_pctile
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of pe_peer_sector_pctile
def f073erm_f073_earnings_multiples_pe_peer_sector_pctile_distmax_504d_base_v175_signal(pe_sector_pctile, closeadj):
    base = pe_sector_pctile
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

