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


# 63d z-score of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_z_63d_base_v076_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_z_126d_base_v077_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_z_252d_base_v078_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_z_504d_base_v079_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_z_63d_base_v080_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_z_126d_base_v081_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_z_252d_base_v082_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_z_504d_base_v083_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_z_63d_base_v084_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_z_126d_base_v085_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_z_252d_base_v086_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_z_504d_base_v087_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_z_63d_base_v088_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_z_126d_base_v089_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_z_252d_base_v090_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_z_504d_base_v091_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_z_63d_base_v092_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_z_126d_base_v093_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_z_252d_base_v094_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_z_504d_base_v095_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_z_63d_base_v096_signal(siccode, closeadj):
    base = siccode / 10000.0
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_z_126d_base_v097_signal(siccode, closeadj):
    base = siccode / 10000.0
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_z_252d_base_v098_signal(siccode, closeadj):
    base = siccode / 10000.0
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_z_504d_base_v099_signal(siccode, closeadj):
    base = siccode / 10000.0
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_z_63d_base_v100_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_z_126d_base_v101_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_z_252d_base_v102_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_z_504d_base_v103_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_distmax_252d_base_v104_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_distmax_504d_base_v105_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_distmax_252d_base_v106_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_distmax_504d_base_v107_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_distmax_252d_base_v108_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_distmax_504d_base_v109_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_distmax_252d_base_v110_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_distmax_504d_base_v111_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_distmax_252d_base_v112_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_distmax_504d_base_v113_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_distmax_252d_base_v114_signal(siccode, closeadj):
    base = siccode / 10000.0
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_distmax_504d_base_v115_signal(siccode, closeadj):
    base = siccode / 10000.0
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_distmax_252d_base_v116_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_distmax_504d_base_v117_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_distmed_126d_base_v118_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_distmed_252d_base_v119_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_distmed_504d_base_v120_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_distmed_126d_base_v121_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_distmed_252d_base_v122_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of is_software
def f082sif_f082_sector_industry_tech_filter_is_software_distmed_504d_base_v123_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_distmed_126d_base_v124_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_distmed_252d_base_v125_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_distmed_504d_base_v126_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_distmed_126d_base_v127_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_distmed_252d_base_v128_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_distmed_504d_base_v129_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_distmed_126d_base_v130_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_distmed_252d_base_v131_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_distmed_504d_base_v132_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_distmed_126d_base_v133_signal(siccode, closeadj):
    base = siccode / 10000.0
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_distmed_252d_base_v134_signal(siccode, closeadj):
    base = siccode / 10000.0
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_distmed_504d_base_v135_signal(siccode, closeadj):
    base = siccode / 10000.0
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_distmed_126d_base_v136_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_distmed_252d_base_v137_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of fama_industry_idx
def f082sif_f082_sector_industry_tech_filter_fama_industry_idx_distmed_504d_base_v138_signal(fama_industry_idx, closeadj):
    base = fama_industry_idx
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_chg_63d_base_v139_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in is_tech
def f082sif_f082_sector_industry_tech_filter_is_tech_chg_252d_base_v140_signal(is_tech_flag, closeadj):
    base = _f082_flag(is_tech_flag)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in is_software
def f082sif_f082_sector_industry_tech_filter_is_software_chg_63d_base_v141_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in is_software
def f082sif_f082_sector_industry_tech_filter_is_software_chg_252d_base_v142_signal(is_software_flag, closeadj):
    base = _f082_flag(is_software_flag)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_chg_63d_base_v143_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in is_semi
def f082sif_f082_sector_industry_tech_filter_is_semi_chg_252d_base_v144_signal(is_semi_flag, closeadj):
    base = _f082_flag(is_semi_flag)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_chg_63d_base_v145_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in is_hardware
def f082sif_f082_sector_industry_tech_filter_is_hardware_chg_252d_base_v146_signal(is_hardware_flag, closeadj):
    base = _f082_flag(is_hardware_flag)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_chg_63d_base_v147_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in is_it_services
def f082sif_f082_sector_industry_tech_filter_is_it_services_chg_252d_base_v148_signal(is_itsvc_flag, closeadj):
    base = _f082_flag(is_itsvc_flag)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_chg_63d_base_v149_signal(siccode, closeadj):
    base = siccode / 10000.0
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in sic_code_norm
def f082sif_f082_sector_industry_tech_filter_sic_code_norm_chg_252d_base_v150_signal(siccode, closeadj):
    base = siccode / 10000.0
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

