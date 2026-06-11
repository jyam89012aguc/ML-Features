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
def _f082_flag(is_tech):
    return is_tech.astype(float) if hasattr(is_tech, 'astype') else is_tech


# 21d mean of is_tech scaled by closeadj
def f082sif_f082_sector_industry_tech_filter_is_tech_mean_21d_base_v001_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of is_tech scaled by closeadj
def f082sif_f082_sector_industry_tech_filter_is_tech_mean_63d_base_v002_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of is_tech scaled by closeadj
def f082sif_f082_sector_industry_tech_filter_is_tech_mean_126d_base_v003_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of is_tech scaled by closeadj
def f082sif_f082_sector_industry_tech_filter_is_tech_mean_252d_base_v004_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of is_tech scaled by closeadj
def f082sif_f082_sector_industry_tech_filter_is_tech_mean_504d_base_v005_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of is_software scaled by closeadj
def f082sif_f082_sector_industry_tech_filter_is_software_mean_21d_base_v006_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of is_software scaled by closeadj
def f082sif_f082_sector_industry_tech_filter_is_software_mean_63d_base_v007_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of is_software scaled by closeadj
def f082sif_f082_sector_industry_tech_filter_is_software_mean_126d_base_v008_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of is_software scaled by closeadj
def f082sif_f082_sector_industry_tech_filter_is_software_mean_252d_base_v009_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of is_software scaled by closeadj
def f082sif_f082_sector_industry_tech_filter_is_software_mean_504d_base_v010_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of is_semi scaled by closeadj
def f082sif_f082_sector_industry_tech_filter_is_semi_mean_21d_base_v011_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of is_semi scaled by closeadj
def f082sif_f082_sector_industry_tech_filter_is_semi_mean_63d_base_v012_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of is_semi scaled by closeadj
def f082sif_f082_sector_industry_tech_filter_is_semi_mean_126d_base_v013_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of is_semi scaled by closeadj
def f082sif_f082_sector_industry_tech_filter_is_semi_mean_252d_base_v014_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of is_semi scaled by closeadj
def f082sif_f082_sector_industry_tech_filter_is_semi_mean_504d_base_v015_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of is_hardware scaled by closeadj
def f082sif_f082_sector_industry_tech_filter_is_hardware_mean_21d_base_v016_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of is_hardware scaled by closeadj
def f082sif_f082_sector_industry_tech_filter_is_hardware_mean_63d_base_v017_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of is_hardware scaled by closeadj
def f082sif_f082_sector_industry_tech_filter_is_hardware_mean_126d_base_v018_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of is_hardware scaled by closeadj
def f082sif_f082_sector_industry_tech_filter_is_hardware_mean_252d_base_v019_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of is_hardware scaled by closeadj
def f082sif_f082_sector_industry_tech_filter_is_hardware_mean_504d_base_v020_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of is_it_services scaled by closeadj
def f082sif_f082_sector_industry_tech_filter_is_it_services_mean_21d_base_v021_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of is_it_services scaled by closeadj
def f082sif_f082_sector_industry_tech_filter_is_it_services_mean_63d_base_v022_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of is_it_services scaled by closeadj
def f082sif_f082_sector_industry_tech_filter_is_it_services_mean_126d_base_v023_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of is_it_services scaled by closeadj
def f082sif_f082_sector_industry_tech_filter_is_it_services_mean_252d_base_v024_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of is_it_services scaled by closeadj
def f082sif_f082_sector_industry_tech_filter_is_it_services_mean_504d_base_v025_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sic_code_norm scaled by closeadj
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_mean_21d_base_v026_signal(siccode, closeadj):
    base = siccode / 10000.0
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sic_code_norm scaled by closeadj
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_mean_63d_base_v027_signal(siccode, closeadj):
    base = siccode / 10000.0
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sic_code_norm scaled by closeadj
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_mean_126d_base_v028_signal(siccode, closeadj):
    base = siccode / 10000.0
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sic_code_norm scaled by closeadj
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_mean_252d_base_v029_signal(siccode, closeadj):
    base = siccode / 10000.0
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sic_code_norm scaled by closeadj
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_mean_504d_base_v030_signal(siccode, closeadj):
    base = siccode / 10000.0
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of fama_industry_idx scaled by closeadj
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_mean_21d_base_v031_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of fama_industry_idx scaled by closeadj
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_mean_63d_base_v032_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of fama_industry_idx scaled by closeadj
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_mean_126d_base_v033_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of fama_industry_idx scaled by closeadj
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_mean_252d_base_v034_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of fama_industry_idx scaled by closeadj
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_mean_504d_base_v035_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_median_63d_base_v036_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_median_252d_base_v037_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_median_504d_base_v038_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_median_63d_base_v039_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_median_252d_base_v040_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_median_504d_base_v041_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_median_63d_base_v042_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_median_252d_base_v043_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_median_504d_base_v044_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_median_63d_base_v045_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_median_252d_base_v046_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_median_504d_base_v047_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_median_63d_base_v048_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_median_252d_base_v049_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_median_504d_base_v050_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_median_63d_base_v051_signal(siccode, closeadj):
    base = siccode / 10000.0
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_median_252d_base_v052_signal(siccode, closeadj):
    base = siccode / 10000.0
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_median_504d_base_v053_signal(siccode, closeadj):
    base = siccode / 10000.0
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_median_63d_base_v054_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_median_252d_base_v055_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_median_504d_base_v056_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_rmax_252d_base_v057_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_rmax_504d_base_v058_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_rmax_252d_base_v059_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_rmax_504d_base_v060_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_rmax_252d_base_v061_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_rmax_504d_base_v062_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_rmax_252d_base_v063_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_rmax_504d_base_v064_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_rmax_252d_base_v065_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_rmax_504d_base_v066_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_rmax_252d_base_v067_signal(siccode, closeadj):
    base = siccode / 10000.0
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_rmax_504d_base_v068_signal(siccode, closeadj):
    base = siccode / 10000.0
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_rmax_252d_base_v069_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_rmax_504d_base_v070_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_rmin_252d_base_v071_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_rmin_504d_base_v072_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_rmin_252d_base_v073_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_rmin_504d_base_v074_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_rmin_252d_base_v075_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

