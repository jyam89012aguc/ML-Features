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
def _f082_flag(is_tech):
    return is_tech.astype(float) if hasattr(is_tech, 'astype') else is_tech


# 21d slope of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_slope_21d_2d_v001_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_slope_63d_2d_v002_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_slope_126d_2d_v003_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_slope_252d_2d_v004_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_slope_504d_2d_v005_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_slope_21d_2d_v006_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_slope_63d_2d_v007_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_slope_126d_2d_v008_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_slope_252d_2d_v009_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_slope_504d_2d_v010_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_slope_21d_2d_v011_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_slope_63d_2d_v012_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_slope_126d_2d_v013_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_slope_252d_2d_v014_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_slope_504d_2d_v015_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_slope_21d_2d_v016_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_slope_63d_2d_v017_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_slope_126d_2d_v018_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_slope_252d_2d_v019_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_slope_504d_2d_v020_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_slope_21d_2d_v021_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_slope_63d_2d_v022_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_slope_126d_2d_v023_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_slope_252d_2d_v024_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_slope_504d_2d_v025_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_slope_21d_2d_v026_signal(siccode, closeadj):
    base = siccode / 10000.0
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_slope_63d_2d_v027_signal(siccode, closeadj):
    base = siccode / 10000.0
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_slope_126d_2d_v028_signal(siccode, closeadj):
    base = siccode / 10000.0
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_slope_252d_2d_v029_signal(siccode, closeadj):
    base = siccode / 10000.0
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_slope_504d_2d_v030_signal(siccode, closeadj):
    base = siccode / 10000.0
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_slope_21d_2d_v031_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_slope_63d_2d_v032_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_slope_126d_2d_v033_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_slope_252d_2d_v034_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_slope_504d_2d_v035_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_sm21_sl21_2d_v036_signal(is_tech_flag, closeadj):
    base = _mean(_f082_flag(is_tech_flag), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_sm63_sl21_2d_v037_signal(is_tech_flag, closeadj):
    base = _mean(_f082_flag(is_tech_flag), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_sm63_sl63_2d_v038_signal(is_tech_flag, closeadj):
    base = _mean(_f082_flag(is_tech_flag), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_sm252_sl63_2d_v039_signal(is_tech_flag, closeadj):
    base = _mean(_f082_flag(is_tech_flag), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_sm252_sl126_2d_v040_signal(is_tech_flag, closeadj):
    base = _mean(_f082_flag(is_tech_flag), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_sm21_sl21_2d_v041_signal(is_software_flag, closeadj):
    base = _mean(_f082_flag(is_software_flag), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_sm63_sl21_2d_v042_signal(is_software_flag, closeadj):
    base = _mean(_f082_flag(is_software_flag), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_sm63_sl63_2d_v043_signal(is_software_flag, closeadj):
    base = _mean(_f082_flag(is_software_flag), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_sm252_sl63_2d_v044_signal(is_software_flag, closeadj):
    base = _mean(_f082_flag(is_software_flag), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_sm252_sl126_2d_v045_signal(is_software_flag, closeadj):
    base = _mean(_f082_flag(is_software_flag), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_sm21_sl21_2d_v046_signal(is_semi_flag, closeadj):
    base = _mean(_f082_flag(is_semi_flag), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_sm63_sl21_2d_v047_signal(is_semi_flag, closeadj):
    base = _mean(_f082_flag(is_semi_flag), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_sm63_sl63_2d_v048_signal(is_semi_flag, closeadj):
    base = _mean(_f082_flag(is_semi_flag), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_sm252_sl63_2d_v049_signal(is_semi_flag, closeadj):
    base = _mean(_f082_flag(is_semi_flag), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_sm252_sl126_2d_v050_signal(is_semi_flag, closeadj):
    base = _mean(_f082_flag(is_semi_flag), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_sm21_sl21_2d_v051_signal(is_hardware_flag, closeadj):
    base = _mean(_f082_flag(is_hardware_flag), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_sm63_sl21_2d_v052_signal(is_hardware_flag, closeadj):
    base = _mean(_f082_flag(is_hardware_flag), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_sm63_sl63_2d_v053_signal(is_hardware_flag, closeadj):
    base = _mean(_f082_flag(is_hardware_flag), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_sm252_sl63_2d_v054_signal(is_hardware_flag, closeadj):
    base = _mean(_f082_flag(is_hardware_flag), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_sm252_sl126_2d_v055_signal(is_hardware_flag, closeadj):
    base = _mean(_f082_flag(is_hardware_flag), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_sm21_sl21_2d_v056_signal(is_itsvc_flag, closeadj):
    base = _mean(_f082_flag(is_itsvc_flag), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_sm63_sl21_2d_v057_signal(is_itsvc_flag, closeadj):
    base = _mean(_f082_flag(is_itsvc_flag), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_sm63_sl63_2d_v058_signal(is_itsvc_flag, closeadj):
    base = _mean(_f082_flag(is_itsvc_flag), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_sm252_sl63_2d_v059_signal(is_itsvc_flag, closeadj):
    base = _mean(_f082_flag(is_itsvc_flag), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_sm252_sl126_2d_v060_signal(is_itsvc_flag, closeadj):
    base = _mean(_f082_flag(is_itsvc_flag), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_sm21_sl21_2d_v061_signal(siccode, closeadj):
    base = _mean(siccode / 10000.0, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_sm63_sl21_2d_v062_signal(siccode, closeadj):
    base = _mean(siccode / 10000.0, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_sm63_sl63_2d_v063_signal(siccode, closeadj):
    base = _mean(siccode / 10000.0, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_sm252_sl63_2d_v064_signal(siccode, closeadj):
    base = _mean(siccode / 10000.0, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_sm252_sl126_2d_v065_signal(siccode, closeadj):
    base = _mean(siccode / 10000.0, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_sm21_sl21_2d_v066_signal(fama_industry_idx, closeadj):
    base = _mean(fama_industry_idx, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_sm63_sl21_2d_v067_signal(fama_industry_idx, closeadj):
    base = _mean(fama_industry_idx, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_sm63_sl63_2d_v068_signal(fama_industry_idx, closeadj):
    base = _mean(fama_industry_idx, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_sm252_sl63_2d_v069_signal(fama_industry_idx, closeadj):
    base = _mean(fama_industry_idx, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_sm252_sl126_2d_v070_signal(fama_industry_idx, closeadj):
    base = _mean(fama_industry_idx, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_pctslope_21d_2d_v071_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_pctslope_63d_2d_v072_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_pctslope_252d_2d_v073_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_pctslope_21d_2d_v074_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_pctslope_63d_2d_v075_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_pctslope_252d_2d_v076_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_pctslope_21d_2d_v077_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_pctslope_63d_2d_v078_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_pctslope_252d_2d_v079_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_pctslope_21d_2d_v080_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_pctslope_63d_2d_v081_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_pctslope_252d_2d_v082_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_pctslope_21d_2d_v083_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_pctslope_63d_2d_v084_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_pctslope_252d_2d_v085_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_pctslope_21d_2d_v086_signal(siccode, closeadj):
    base = siccode / 10000.0
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_pctslope_63d_2d_v087_signal(siccode, closeadj):
    base = siccode / 10000.0
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_pctslope_252d_2d_v088_signal(siccode, closeadj):
    base = siccode / 10000.0
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_pctslope_21d_2d_v089_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_pctslope_63d_2d_v090_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_pctslope_252d_2d_v091_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_sgnslope_21d_2d_v092_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_sgnslope_63d_2d_v093_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_sgnslope_252d_2d_v094_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_sgnslope_21d_2d_v095_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_sgnslope_63d_2d_v096_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_sgnslope_252d_2d_v097_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_sgnslope_21d_2d_v098_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_sgnslope_63d_2d_v099_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_sgnslope_252d_2d_v100_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_sgnslope_21d_2d_v101_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_sgnslope_63d_2d_v102_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_sgnslope_252d_2d_v103_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_sgnslope_21d_2d_v104_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_sgnslope_63d_2d_v105_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_sgnslope_252d_2d_v106_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_sgnslope_21d_2d_v107_signal(siccode, closeadj):
    base = siccode / 10000.0
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_sgnslope_63d_2d_v108_signal(siccode, closeadj):
    base = siccode / 10000.0
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_sgnslope_252d_2d_v109_signal(siccode, closeadj):
    base = siccode / 10000.0
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_sgnslope_21d_2d_v110_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_sgnslope_63d_2d_v111_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_sgnslope_252d_2d_v112_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_logmagslope_21d_2d_v113_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_logmagslope_63d_2d_v114_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_logmagslope_252d_2d_v115_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_logmagslope_21d_2d_v116_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_logmagslope_63d_2d_v117_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_logmagslope_252d_2d_v118_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_logmagslope_21d_2d_v119_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_logmagslope_63d_2d_v120_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_logmagslope_252d_2d_v121_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_logmagslope_21d_2d_v122_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_logmagslope_63d_2d_v123_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_logmagslope_252d_2d_v124_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_logmagslope_21d_2d_v125_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_logmagslope_63d_2d_v126_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_logmagslope_252d_2d_v127_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_logmagslope_21d_2d_v128_signal(siccode, closeadj):
    base = siccode / 10000.0
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_logmagslope_63d_2d_v129_signal(siccode, closeadj):
    base = siccode / 10000.0
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_logmagslope_252d_2d_v130_signal(siccode, closeadj):
    base = siccode / 10000.0
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_logmagslope_21d_2d_v131_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_logmagslope_63d_2d_v132_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_logmagslope_252d_2d_v133_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|is_tech|
def f082sif_f082_sector_industry_tech_filter_is_tech_logslope_63d_2d_v134_signal(is_tech_flag, closeadj):
    base = np.log((_f082_flag(is_tech_flag)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|is_tech|
def f082sif_f082_sector_industry_tech_filter_is_tech_logslope_252d_2d_v135_signal(is_tech_flag, closeadj):
    base = np.log((_f082_flag(is_tech_flag)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|is_software|
def f082sif_f082_sector_industry_tech_filter_is_software_logslope_63d_2d_v136_signal(is_software_flag, closeadj):
    base = np.log((_f082_flag(is_software_flag)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|is_software|
def f082sif_f082_sector_industry_tech_filter_is_software_logslope_252d_2d_v137_signal(is_software_flag, closeadj):
    base = np.log((_f082_flag(is_software_flag)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|is_semi|
def f082sif_f082_sector_industry_tech_filter_is_semi_logslope_63d_2d_v138_signal(is_semi_flag, closeadj):
    base = np.log((_f082_flag(is_semi_flag)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|is_semi|
def f082sif_f082_sector_industry_tech_filter_is_semi_logslope_252d_2d_v139_signal(is_semi_flag, closeadj):
    base = np.log((_f082_flag(is_semi_flag)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|is_hardware|
def f082sif_f082_sector_industry_tech_filter_is_hardware_logslope_63d_2d_v140_signal(is_hardware_flag, closeadj):
    base = np.log((_f082_flag(is_hardware_flag)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|is_hardware|
def f082sif_f082_sector_industry_tech_filter_is_hardware_logslope_252d_2d_v141_signal(is_hardware_flag, closeadj):
    base = np.log((_f082_flag(is_hardware_flag)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|is_it_services|
def f082sif_f082_sector_industry_tech_filter_is_it_services_logslope_63d_2d_v142_signal(is_itsvc_flag, closeadj):
    base = np.log((_f082_flag(is_itsvc_flag)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|is_it_services|
def f082sif_f082_sector_industry_tech_filter_is_it_services_logslope_252d_2d_v143_signal(is_itsvc_flag, closeadj):
    base = np.log((_f082_flag(is_itsvc_flag)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|sic_code_norm|
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_logslope_63d_2d_v144_signal(siccode, closeadj):
    base = np.log((siccode / 10000.0).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|sic_code_norm|
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_logslope_252d_2d_v145_signal(siccode, closeadj):
    base = np.log((siccode / 10000.0).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|fama_industry_idx|
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_logslope_63d_2d_v146_signal(fama_industry_idx, closeadj):
    base = np.log((fama_industry_idx).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|fama_industry_idx|
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_logslope_252d_2d_v147_signal(fama_industry_idx, closeadj):
    base = np.log((fama_industry_idx).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

