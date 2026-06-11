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


# 21d acceleration of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_accel_21d_3d_v001_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_accel_63d_3d_v002_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_accel_126d_3d_v003_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_accel_252d_3d_v004_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_accel_21d_3d_v005_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_accel_63d_3d_v006_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_accel_126d_3d_v007_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_accel_252d_3d_v008_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_accel_21d_3d_v009_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_accel_63d_3d_v010_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_accel_126d_3d_v011_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_accel_252d_3d_v012_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_accel_21d_3d_v013_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_accel_63d_3d_v014_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_accel_126d_3d_v015_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_accel_252d_3d_v016_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_accel_21d_3d_v017_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_accel_63d_3d_v018_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_accel_126d_3d_v019_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_accel_252d_3d_v020_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_accel_21d_3d_v021_signal(siccode, closeadj):
    base = siccode / 10000.0
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_accel_63d_3d_v022_signal(siccode, closeadj):
    base = siccode / 10000.0
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_accel_126d_3d_v023_signal(siccode, closeadj):
    base = siccode / 10000.0
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_accel_252d_3d_v024_signal(siccode, closeadj):
    base = siccode / 10000.0
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_accel_21d_3d_v025_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_accel_63d_3d_v026_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_accel_126d_3d_v027_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_accel_252d_3d_v028_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_slopez_21d_z126_3d_v029_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_slopez_63d_z252_3d_v030_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_slopez_126d_z252_3d_v031_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_slopez_252d_z504_3d_v032_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_slopez_21d_z126_3d_v033_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_slopez_63d_z252_3d_v034_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_slopez_126d_z252_3d_v035_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_slopez_252d_z504_3d_v036_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_slopez_21d_z126_3d_v037_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_slopez_63d_z252_3d_v038_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_slopez_126d_z252_3d_v039_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_slopez_252d_z504_3d_v040_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_slopez_21d_z126_3d_v041_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_slopez_63d_z252_3d_v042_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_slopez_126d_z252_3d_v043_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_slopez_252d_z504_3d_v044_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_slopez_21d_z126_3d_v045_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_slopez_63d_z252_3d_v046_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_slopez_126d_z252_3d_v047_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_slopez_252d_z504_3d_v048_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_slopez_21d_z126_3d_v049_signal(siccode, closeadj):
    base = siccode / 10000.0
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_slopez_63d_z252_3d_v050_signal(siccode, closeadj):
    base = siccode / 10000.0
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_slopez_126d_z252_3d_v051_signal(siccode, closeadj):
    base = siccode / 10000.0
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_slopez_252d_z504_3d_v052_signal(siccode, closeadj):
    base = siccode / 10000.0
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_slopez_21d_z126_3d_v053_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_slopez_63d_z252_3d_v054_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_slopez_126d_z252_3d_v055_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_slopez_252d_z504_3d_v056_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_jerk_21d_3d_v057_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_jerk_63d_3d_v058_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_jerk_126d_3d_v059_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_jerk_21d_3d_v060_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_jerk_63d_3d_v061_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_jerk_126d_3d_v062_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_jerk_21d_3d_v063_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_jerk_63d_3d_v064_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_jerk_126d_3d_v065_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_jerk_21d_3d_v066_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_jerk_63d_3d_v067_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_jerk_126d_3d_v068_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_jerk_21d_3d_v069_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_jerk_63d_3d_v070_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_jerk_126d_3d_v071_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_jerk_21d_3d_v072_signal(siccode, closeadj):
    base = siccode / 10000.0
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_jerk_63d_3d_v073_signal(siccode, closeadj):
    base = siccode / 10000.0
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_jerk_126d_3d_v074_signal(siccode, closeadj):
    base = siccode / 10000.0
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_jerk_21d_3d_v075_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_jerk_63d_3d_v076_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_jerk_126d_3d_v077_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of is_tech smoothed over 252d
def f082sif_f082_sector_industry_tech_filter_is_tech_smoothaccel_63d_sm252_3d_v078_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of is_tech smoothed over 504d
def f082sif_f082_sector_industry_tech_filter_is_tech_smoothaccel_252d_sm504_3d_v079_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of is_software smoothed over 252d
def f082sif_f082_sector_industry_tech_filter_is_software_smoothaccel_63d_sm252_3d_v080_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of is_software smoothed over 504d
def f082sif_f082_sector_industry_tech_filter_is_software_smoothaccel_252d_sm504_3d_v081_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of is_semi smoothed over 252d
def f082sif_f082_sector_industry_tech_filter_is_semi_smoothaccel_63d_sm252_3d_v082_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of is_semi smoothed over 504d
def f082sif_f082_sector_industry_tech_filter_is_semi_smoothaccel_252d_sm504_3d_v083_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of is_hardware smoothed over 252d
def f082sif_f082_sector_industry_tech_filter_is_hardware_smoothaccel_63d_sm252_3d_v084_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of is_hardware smoothed over 504d
def f082sif_f082_sector_industry_tech_filter_is_hardware_smoothaccel_252d_sm504_3d_v085_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of is_it_services smoothed over 252d
def f082sif_f082_sector_industry_tech_filter_is_it_services_smoothaccel_63d_sm252_3d_v086_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of is_it_services smoothed over 504d
def f082sif_f082_sector_industry_tech_filter_is_it_services_smoothaccel_252d_sm504_3d_v087_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of sic_code_norm smoothed over 252d
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_smoothaccel_63d_sm252_3d_v088_signal(siccode, closeadj):
    base = siccode / 10000.0
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of sic_code_norm smoothed over 504d
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_smoothaccel_252d_sm504_3d_v089_signal(siccode, closeadj):
    base = siccode / 10000.0
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of fama_industry_idx smoothed over 252d
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_smoothaccel_63d_sm252_3d_v090_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of fama_industry_idx smoothed over 504d
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_smoothaccel_252d_sm504_3d_v091_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_accelz_21d_z252_3d_v092_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_accelz_63d_z504_3d_v093_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_accelz_21d_z252_3d_v094_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_accelz_63d_z504_3d_v095_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_accelz_21d_z252_3d_v096_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_accelz_63d_z504_3d_v097_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_accelz_21d_z252_3d_v098_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_accelz_63d_z504_3d_v099_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_accelz_21d_z252_3d_v100_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_accelz_63d_z504_3d_v101_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_accelz_21d_z252_3d_v102_signal(siccode, closeadj):
    base = siccode / 10000.0
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_accelz_63d_z504_3d_v103_signal(siccode, closeadj):
    base = siccode / 10000.0
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_accelz_21d_z252_3d_v104_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_accelz_63d_z504_3d_v105_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in is_tech (raw count, no price scaling)
def f082sif_f082_sector_industry_tech_filter_is_tech_signflip_63d_3d_v106_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in is_tech (raw count, no price scaling)
def f082sif_f082_sector_industry_tech_filter_is_tech_signflip_252d_3d_v107_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in is_software (raw count, no price scaling)
def f082sif_f082_sector_industry_tech_filter_is_software_signflip_63d_3d_v108_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in is_software (raw count, no price scaling)
def f082sif_f082_sector_industry_tech_filter_is_software_signflip_252d_3d_v109_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in is_semi (raw count, no price scaling)
def f082sif_f082_sector_industry_tech_filter_is_semi_signflip_63d_3d_v110_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in is_semi (raw count, no price scaling)
def f082sif_f082_sector_industry_tech_filter_is_semi_signflip_252d_3d_v111_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in is_hardware (raw count, no price scaling)
def f082sif_f082_sector_industry_tech_filter_is_hardware_signflip_63d_3d_v112_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in is_hardware (raw count, no price scaling)
def f082sif_f082_sector_industry_tech_filter_is_hardware_signflip_252d_3d_v113_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in is_it_services (raw count, no price scaling)
def f082sif_f082_sector_industry_tech_filter_is_it_services_signflip_63d_3d_v114_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in is_it_services (raw count, no price scaling)
def f082sif_f082_sector_industry_tech_filter_is_it_services_signflip_252d_3d_v115_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in sic_code_norm (raw count, no price scaling)
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_signflip_63d_3d_v116_signal(siccode, closeadj):
    base = siccode / 10000.0
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in sic_code_norm (raw count, no price scaling)
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_signflip_252d_3d_v117_signal(siccode, closeadj):
    base = siccode / 10000.0
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in fama_industry_idx (raw count, no price scaling)
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_signflip_63d_3d_v118_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in fama_industry_idx (raw count, no price scaling)
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_signflip_252d_3d_v119_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of is_tech normalized by 252d range
def f082sif_f082_sector_industry_tech_filter_is_tech_rngaccel_63d_r252_3d_v120_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of is_tech normalized by 504d range
def f082sif_f082_sector_industry_tech_filter_is_tech_rngaccel_252d_r504_3d_v121_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of is_software normalized by 252d range
def f082sif_f082_sector_industry_tech_filter_is_software_rngaccel_63d_r252_3d_v122_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of is_software normalized by 504d range
def f082sif_f082_sector_industry_tech_filter_is_software_rngaccel_252d_r504_3d_v123_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of is_semi normalized by 252d range
def f082sif_f082_sector_industry_tech_filter_is_semi_rngaccel_63d_r252_3d_v124_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of is_semi normalized by 504d range
def f082sif_f082_sector_industry_tech_filter_is_semi_rngaccel_252d_r504_3d_v125_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of is_hardware normalized by 252d range
def f082sif_f082_sector_industry_tech_filter_is_hardware_rngaccel_63d_r252_3d_v126_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of is_hardware normalized by 504d range
def f082sif_f082_sector_industry_tech_filter_is_hardware_rngaccel_252d_r504_3d_v127_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of is_it_services normalized by 252d range
def f082sif_f082_sector_industry_tech_filter_is_it_services_rngaccel_63d_r252_3d_v128_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of is_it_services normalized by 504d range
def f082sif_f082_sector_industry_tech_filter_is_it_services_rngaccel_252d_r504_3d_v129_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sic_code_norm normalized by 252d range
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_rngaccel_63d_r252_3d_v130_signal(siccode, closeadj):
    base = siccode / 10000.0
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sic_code_norm normalized by 504d range
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_rngaccel_252d_r504_3d_v131_signal(siccode, closeadj):
    base = siccode / 10000.0
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fama_industry_idx normalized by 252d range
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_rngaccel_63d_r252_3d_v132_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fama_industry_idx normalized by 504d range
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_rngaccel_252d_r504_3d_v133_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_cumslope_21d_3d_v134_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_cumslope_63d_3d_v135_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_cumslope_252d_3d_v136_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_cumslope_21d_3d_v137_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_cumslope_63d_3d_v138_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_cumslope_252d_3d_v139_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_cumslope_21d_3d_v140_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_cumslope_63d_3d_v141_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_cumslope_252d_3d_v142_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_cumslope_21d_3d_v143_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_cumslope_63d_3d_v144_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_cumslope_252d_3d_v145_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_cumslope_21d_3d_v146_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_cumslope_63d_3d_v147_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_cumslope_252d_3d_v148_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_cumslope_21d_3d_v149_signal(siccode, closeadj):
    base = siccode / 10000.0
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_cumslope_63d_3d_v150_signal(siccode, closeadj):
    base = siccode / 10000.0
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

