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


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    denom = s.shift(w).abs().replace(0, np.nan)
    return s.diff(periods=w) / denom


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives (f11 defense_revenue_stability) =====
def _f11_revenue_vol(revenue, w):
    rg = revenue.pct_change()
    return rg.rolling(w, min_periods=max(1, w // 2)).std()


def _f11_revenue_consistency(revenue, w):
    rg = revenue.pct_change()
    m = rg.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = rg.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan)


def _f11_revenue_stability_score(revenue, w):
    rg = revenue.pct_change()
    sd = rg.rolling(w, min_periods=max(1, w // 2)).std()
    return 1.0 / (1.0 + sd.replace(0, np.nan))


def drs_f11_defense_revenue_stability_revvol_5d_rmean5_slpct5_xc_v001_signal(revenue, closeadj):
    base = _mean(_f11_revenue_vol(revenue, 5), 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_5d_rstd5_sldiff10_xlc_v002_signal(revenue, closeadj):
    base = _std(_f11_revenue_vol(revenue, 5), 5) * np.log1p(closeadj.abs())
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_5d_ema5_slpct21_xmc_v003_signal(revenue, closeadj):
    base = _ema(_f11_revenue_vol(revenue, 5), 5) * _mean(closeadj, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_5d_z5_sldiff63_xrr_v004_signal(revenue, closeadj):
    base = _z(_f11_revenue_vol(revenue, 5), 5) * (revenue / _mean(revenue, 63).replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_5d_logm5_slpct126_xc_v005_signal(revenue, closeadj):
    base = np.log1p(_mean(_f11_revenue_vol(revenue, 5), 5).clip(lower=0)) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_5d_sgnsq5_sldiff252_xlc_v006_signal(revenue, closeadj):
    base = (np.sign(_mean(_f11_revenue_vol(revenue, 5), 5)) * np.sqrt(_mean(_f11_revenue_vol(revenue, 5), 5).abs())) * np.log1p(closeadj.abs())
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_5d_diffx5_slpct5_xmc_v007_signal(revenue, closeadj):
    base = _diff(_f11_revenue_vol(revenue, 5), 5) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_10d_rmean7_sldiff10_xrr_v008_signal(revenue, closeadj):
    base = _mean(_f11_revenue_vol(revenue, 10), 7) * (revenue / _mean(revenue, 63).replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_10d_rstd7_slpct21_xc_v009_signal(revenue, closeadj):
    base = _std(_f11_revenue_vol(revenue, 10), 7) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_10d_ema7_sldiff63_xlc_v010_signal(revenue, closeadj):
    base = _ema(_f11_revenue_vol(revenue, 10), 7) * np.log1p(closeadj.abs())
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_10d_z7_slpct126_xmc_v011_signal(revenue, closeadj):
    base = _z(_f11_revenue_vol(revenue, 10), 7) * _mean(closeadj, 21)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_10d_logm7_sldiff252_xrr_v012_signal(revenue, closeadj):
    base = np.log1p(_mean(_f11_revenue_vol(revenue, 10), 7).clip(lower=0)) * (revenue / _mean(revenue, 63).replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_10d_sgnsq7_slpct5_xc_v013_signal(revenue, closeadj):
    base = (np.sign(_mean(_f11_revenue_vol(revenue, 10), 7)) * np.sqrt(_mean(_f11_revenue_vol(revenue, 10), 7).abs())) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_10d_diffx7_sldiff10_xlc_v014_signal(revenue, closeadj):
    base = _diff(_f11_revenue_vol(revenue, 10), 7) * np.log1p(closeadj.abs())
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_21d_rmean10_slpct21_xmc_v015_signal(revenue, closeadj):
    base = _mean(_f11_revenue_vol(revenue, 21), 10) * _mean(closeadj, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_21d_rstd10_sldiff63_xrr_v016_signal(revenue, closeadj):
    base = _std(_f11_revenue_vol(revenue, 21), 10) * (revenue / _mean(revenue, 63).replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_21d_ema10_slpct126_xc_v017_signal(revenue, closeadj):
    base = _ema(_f11_revenue_vol(revenue, 21), 10) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_21d_z10_sldiff252_xlc_v018_signal(revenue, closeadj):
    base = _z(_f11_revenue_vol(revenue, 21), 10) * np.log1p(closeadj.abs())
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_21d_logm10_slpct5_xmc_v019_signal(revenue, closeadj):
    base = np.log1p(_mean(_f11_revenue_vol(revenue, 21), 10).clip(lower=0)) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_21d_sgnsq10_sldiff10_xrr_v020_signal(revenue, closeadj):
    base = (np.sign(_mean(_f11_revenue_vol(revenue, 21), 10)) * np.sqrt(_mean(_f11_revenue_vol(revenue, 21), 10).abs())) * (revenue / _mean(revenue, 63).replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_21d_diffx10_slpct21_xc_v021_signal(revenue, closeadj):
    base = _diff(_f11_revenue_vol(revenue, 21), 10) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_42d_rmean21_sldiff63_xlc_v022_signal(revenue, closeadj):
    base = _mean(_f11_revenue_vol(revenue, 42), 21) * np.log1p(closeadj.abs())
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_42d_rstd21_slpct126_xmc_v023_signal(revenue, closeadj):
    base = _std(_f11_revenue_vol(revenue, 42), 21) * _mean(closeadj, 21)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_42d_ema21_sldiff252_xrr_v024_signal(revenue, closeadj):
    base = _ema(_f11_revenue_vol(revenue, 42), 21) * (revenue / _mean(revenue, 63).replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_42d_z21_slpct5_xc_v025_signal(revenue, closeadj):
    base = _z(_f11_revenue_vol(revenue, 42), 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_42d_logm21_sldiff10_xlc_v026_signal(revenue, closeadj):
    base = np.log1p(_mean(_f11_revenue_vol(revenue, 42), 21).clip(lower=0)) * np.log1p(closeadj.abs())
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_42d_sgnsq21_slpct21_xmc_v027_signal(revenue, closeadj):
    base = (np.sign(_mean(_f11_revenue_vol(revenue, 42), 21)) * np.sqrt(_mean(_f11_revenue_vol(revenue, 42), 21).abs())) * _mean(closeadj, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_42d_diffx21_sldiff63_xrr_v028_signal(revenue, closeadj):
    base = _diff(_f11_revenue_vol(revenue, 42), 21) * (revenue / _mean(revenue, 63).replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_63d_rmean31_slpct126_xc_v029_signal(revenue, closeadj):
    base = _mean(_f11_revenue_vol(revenue, 63), 31) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_63d_rstd31_sldiff252_xlc_v030_signal(revenue, closeadj):
    base = _std(_f11_revenue_vol(revenue, 63), 31) * np.log1p(closeadj.abs())
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_63d_ema31_slpct5_xmc_v031_signal(revenue, closeadj):
    base = _ema(_f11_revenue_vol(revenue, 63), 31) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_63d_z31_sldiff10_xrr_v032_signal(revenue, closeadj):
    base = _z(_f11_revenue_vol(revenue, 63), 31) * (revenue / _mean(revenue, 63).replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_63d_logm31_slpct21_xc_v033_signal(revenue, closeadj):
    base = np.log1p(_mean(_f11_revenue_vol(revenue, 63), 31).clip(lower=0)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_63d_sgnsq31_sldiff63_xlc_v034_signal(revenue, closeadj):
    base = (np.sign(_mean(_f11_revenue_vol(revenue, 63), 31)) * np.sqrt(_mean(_f11_revenue_vol(revenue, 63), 31).abs())) * np.log1p(closeadj.abs())
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_63d_diffx31_slpct126_xmc_v035_signal(revenue, closeadj):
    base = _diff(_f11_revenue_vol(revenue, 63), 31) * _mean(closeadj, 21)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_126d_rmean63_sldiff252_xrr_v036_signal(revenue, closeadj):
    base = _mean(_f11_revenue_vol(revenue, 126), 63) * (revenue / _mean(revenue, 63).replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_126d_rstd63_slpct5_xc_v037_signal(revenue, closeadj):
    base = _std(_f11_revenue_vol(revenue, 126), 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_126d_ema63_sldiff10_xlc_v038_signal(revenue, closeadj):
    base = _ema(_f11_revenue_vol(revenue, 126), 63) * np.log1p(closeadj.abs())
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_126d_z63_slpct21_xmc_v039_signal(revenue, closeadj):
    base = _z(_f11_revenue_vol(revenue, 126), 63) * _mean(closeadj, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_126d_logm63_sldiff63_xrr_v040_signal(revenue, closeadj):
    base = np.log1p(_mean(_f11_revenue_vol(revenue, 126), 63).clip(lower=0)) * (revenue / _mean(revenue, 63).replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_126d_sgnsq63_slpct126_xc_v041_signal(revenue, closeadj):
    base = (np.sign(_mean(_f11_revenue_vol(revenue, 126), 63)) * np.sqrt(_mean(_f11_revenue_vol(revenue, 126), 63).abs())) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_126d_diffx63_sldiff252_xlc_v042_signal(revenue, closeadj):
    base = _diff(_f11_revenue_vol(revenue, 126), 63) * np.log1p(closeadj.abs())
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_252d_rmean126_slpct5_xmc_v043_signal(revenue, closeadj):
    base = _mean(_f11_revenue_vol(revenue, 252), 126) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_252d_rstd126_sldiff10_xrr_v044_signal(revenue, closeadj):
    base = _std(_f11_revenue_vol(revenue, 252), 126) * (revenue / _mean(revenue, 63).replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_252d_ema126_slpct21_xc_v045_signal(revenue, closeadj):
    base = _ema(_f11_revenue_vol(revenue, 252), 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_252d_z126_sldiff63_xlc_v046_signal(revenue, closeadj):
    base = _z(_f11_revenue_vol(revenue, 252), 126) * np.log1p(closeadj.abs())
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_252d_logm126_slpct126_xmc_v047_signal(revenue, closeadj):
    base = np.log1p(_mean(_f11_revenue_vol(revenue, 252), 126).clip(lower=0)) * _mean(closeadj, 21)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_252d_sgnsq126_sldiff252_xrr_v048_signal(revenue, closeadj):
    base = (np.sign(_mean(_f11_revenue_vol(revenue, 252), 126)) * np.sqrt(_mean(_f11_revenue_vol(revenue, 252), 126).abs())) * (revenue / _mean(revenue, 63).replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_252d_diffx126_slpct5_xc_v049_signal(revenue, closeadj):
    base = _diff(_f11_revenue_vol(revenue, 252), 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_5d_rmean5_sldiff10_xlc_v050_signal(revenue, closeadj):
    base = _mean(_f11_revenue_consistency(revenue, 5), 5) * np.log1p(closeadj.abs())
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_5d_rstd5_slpct21_xmc_v051_signal(revenue, closeadj):
    base = _std(_f11_revenue_consistency(revenue, 5), 5) * _mean(closeadj, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_5d_ema5_sldiff63_xrr_v052_signal(revenue, closeadj):
    base = _ema(_f11_revenue_consistency(revenue, 5), 5) * (revenue / _mean(revenue, 63).replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_5d_z5_slpct126_xc_v053_signal(revenue, closeadj):
    base = _z(_f11_revenue_consistency(revenue, 5), 5) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_5d_logm5_sldiff252_xlc_v054_signal(revenue, closeadj):
    base = np.log1p(_mean(_f11_revenue_consistency(revenue, 5), 5).clip(lower=0)) * np.log1p(closeadj.abs())
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_5d_sgnsq5_slpct5_xmc_v055_signal(revenue, closeadj):
    base = (np.sign(_mean(_f11_revenue_consistency(revenue, 5), 5)) * np.sqrt(_mean(_f11_revenue_consistency(revenue, 5), 5).abs())) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_5d_diffx5_sldiff10_xrr_v056_signal(revenue, closeadj):
    base = _diff(_f11_revenue_consistency(revenue, 5), 5) * (revenue / _mean(revenue, 63).replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_10d_rmean7_slpct21_xc_v057_signal(revenue, closeadj):
    base = _mean(_f11_revenue_consistency(revenue, 10), 7) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_10d_rstd7_sldiff63_xlc_v058_signal(revenue, closeadj):
    base = _std(_f11_revenue_consistency(revenue, 10), 7) * np.log1p(closeadj.abs())
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_10d_ema7_slpct126_xmc_v059_signal(revenue, closeadj):
    base = _ema(_f11_revenue_consistency(revenue, 10), 7) * _mean(closeadj, 21)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_10d_z7_sldiff252_xrr_v060_signal(revenue, closeadj):
    base = _z(_f11_revenue_consistency(revenue, 10), 7) * (revenue / _mean(revenue, 63).replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_10d_logm7_slpct5_xc_v061_signal(revenue, closeadj):
    base = np.log1p(_mean(_f11_revenue_consistency(revenue, 10), 7).clip(lower=0)) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_10d_sgnsq7_sldiff10_xlc_v062_signal(revenue, closeadj):
    base = (np.sign(_mean(_f11_revenue_consistency(revenue, 10), 7)) * np.sqrt(_mean(_f11_revenue_consistency(revenue, 10), 7).abs())) * np.log1p(closeadj.abs())
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_10d_diffx7_slpct21_xmc_v063_signal(revenue, closeadj):
    base = _diff(_f11_revenue_consistency(revenue, 10), 7) * _mean(closeadj, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_21d_rmean10_sldiff63_xrr_v064_signal(revenue, closeadj):
    base = _mean(_f11_revenue_consistency(revenue, 21), 10) * (revenue / _mean(revenue, 63).replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_21d_rstd10_slpct126_xc_v065_signal(revenue, closeadj):
    base = _std(_f11_revenue_consistency(revenue, 21), 10) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_21d_ema10_sldiff252_xlc_v066_signal(revenue, closeadj):
    base = _ema(_f11_revenue_consistency(revenue, 21), 10) * np.log1p(closeadj.abs())
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_21d_z10_slpct5_xmc_v067_signal(revenue, closeadj):
    base = _z(_f11_revenue_consistency(revenue, 21), 10) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_21d_logm10_sldiff10_xrr_v068_signal(revenue, closeadj):
    base = np.log1p(_mean(_f11_revenue_consistency(revenue, 21), 10).clip(lower=0)) * (revenue / _mean(revenue, 63).replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_21d_sgnsq10_slpct21_xc_v069_signal(revenue, closeadj):
    base = (np.sign(_mean(_f11_revenue_consistency(revenue, 21), 10)) * np.sqrt(_mean(_f11_revenue_consistency(revenue, 21), 10).abs())) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_21d_diffx10_sldiff63_xlc_v070_signal(revenue, closeadj):
    base = _diff(_f11_revenue_consistency(revenue, 21), 10) * np.log1p(closeadj.abs())
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_42d_rmean21_slpct126_xmc_v071_signal(revenue, closeadj):
    base = _mean(_f11_revenue_consistency(revenue, 42), 21) * _mean(closeadj, 21)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_42d_rstd21_sldiff252_xrr_v072_signal(revenue, closeadj):
    base = _std(_f11_revenue_consistency(revenue, 42), 21) * (revenue / _mean(revenue, 63).replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_42d_ema21_slpct5_xc_v073_signal(revenue, closeadj):
    base = _ema(_f11_revenue_consistency(revenue, 42), 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_42d_z21_sldiff10_xlc_v074_signal(revenue, closeadj):
    base = _z(_f11_revenue_consistency(revenue, 42), 21) * np.log1p(closeadj.abs())
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_42d_logm21_slpct21_xmc_v075_signal(revenue, closeadj):
    base = np.log1p(_mean(_f11_revenue_consistency(revenue, 42), 21).clip(lower=0)) * _mean(closeadj, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_42d_sgnsq21_sldiff63_xrr_v076_signal(revenue, closeadj):
    base = (np.sign(_mean(_f11_revenue_consistency(revenue, 42), 21)) * np.sqrt(_mean(_f11_revenue_consistency(revenue, 42), 21).abs())) * (revenue / _mean(revenue, 63).replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_42d_diffx21_slpct126_xc_v077_signal(revenue, closeadj):
    base = _diff(_f11_revenue_consistency(revenue, 42), 21) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_63d_rmean31_sldiff252_xlc_v078_signal(revenue, closeadj):
    base = _mean(_f11_revenue_consistency(revenue, 63), 31) * np.log1p(closeadj.abs())
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_63d_rstd31_slpct5_xmc_v079_signal(revenue, closeadj):
    base = _std(_f11_revenue_consistency(revenue, 63), 31) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_63d_ema31_sldiff10_xrr_v080_signal(revenue, closeadj):
    base = _ema(_f11_revenue_consistency(revenue, 63), 31) * (revenue / _mean(revenue, 63).replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_63d_z31_slpct21_xc_v081_signal(revenue, closeadj):
    base = _z(_f11_revenue_consistency(revenue, 63), 31) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_63d_logm31_sldiff63_xlc_v082_signal(revenue, closeadj):
    base = np.log1p(_mean(_f11_revenue_consistency(revenue, 63), 31).clip(lower=0)) * np.log1p(closeadj.abs())
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_63d_sgnsq31_slpct126_xmc_v083_signal(revenue, closeadj):
    base = (np.sign(_mean(_f11_revenue_consistency(revenue, 63), 31)) * np.sqrt(_mean(_f11_revenue_consistency(revenue, 63), 31).abs())) * _mean(closeadj, 21)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_63d_diffx31_sldiff252_xrr_v084_signal(revenue, closeadj):
    base = _diff(_f11_revenue_consistency(revenue, 63), 31) * (revenue / _mean(revenue, 63).replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_126d_rmean63_slpct5_xc_v085_signal(revenue, closeadj):
    base = _mean(_f11_revenue_consistency(revenue, 126), 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_126d_rstd63_sldiff10_xlc_v086_signal(revenue, closeadj):
    base = _std(_f11_revenue_consistency(revenue, 126), 63) * np.log1p(closeadj.abs())
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_126d_ema63_slpct21_xmc_v087_signal(revenue, closeadj):
    base = _ema(_f11_revenue_consistency(revenue, 126), 63) * _mean(closeadj, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_126d_z63_sldiff63_xrr_v088_signal(revenue, closeadj):
    base = _z(_f11_revenue_consistency(revenue, 126), 63) * (revenue / _mean(revenue, 63).replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_126d_logm63_slpct126_xc_v089_signal(revenue, closeadj):
    base = np.log1p(_mean(_f11_revenue_consistency(revenue, 126), 63).clip(lower=0)) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_126d_sgnsq63_sldiff252_xlc_v090_signal(revenue, closeadj):
    base = (np.sign(_mean(_f11_revenue_consistency(revenue, 126), 63)) * np.sqrt(_mean(_f11_revenue_consistency(revenue, 126), 63).abs())) * np.log1p(closeadj.abs())
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_126d_diffx63_slpct5_xmc_v091_signal(revenue, closeadj):
    base = _diff(_f11_revenue_consistency(revenue, 126), 63) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_252d_rmean126_sldiff10_xrr_v092_signal(revenue, closeadj):
    base = _mean(_f11_revenue_consistency(revenue, 252), 126) * (revenue / _mean(revenue, 63).replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_252d_rstd126_slpct21_xc_v093_signal(revenue, closeadj):
    base = _std(_f11_revenue_consistency(revenue, 252), 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_252d_ema126_sldiff63_xlc_v094_signal(revenue, closeadj):
    base = _ema(_f11_revenue_consistency(revenue, 252), 126) * np.log1p(closeadj.abs())
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_252d_z126_slpct126_xmc_v095_signal(revenue, closeadj):
    base = _z(_f11_revenue_consistency(revenue, 252), 126) * _mean(closeadj, 21)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_252d_logm126_sldiff252_xrr_v096_signal(revenue, closeadj):
    base = np.log1p(_mean(_f11_revenue_consistency(revenue, 252), 126).clip(lower=0)) * (revenue / _mean(revenue, 63).replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_252d_sgnsq126_slpct5_xc_v097_signal(revenue, closeadj):
    base = (np.sign(_mean(_f11_revenue_consistency(revenue, 252), 126)) * np.sqrt(_mean(_f11_revenue_consistency(revenue, 252), 126).abs())) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_252d_diffx126_sldiff10_xlc_v098_signal(revenue, closeadj):
    base = _diff(_f11_revenue_consistency(revenue, 252), 126) * np.log1p(closeadj.abs())
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_5d_rmean5_slpct21_xmc_v099_signal(revenue, closeadj):
    base = _mean(_f11_revenue_stability_score(revenue, 5), 5) * _mean(closeadj, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_5d_rstd5_sldiff63_xrr_v100_signal(revenue, closeadj):
    base = _std(_f11_revenue_stability_score(revenue, 5), 5) * (revenue / _mean(revenue, 63).replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_5d_ema5_slpct126_xc_v101_signal(revenue, closeadj):
    base = _ema(_f11_revenue_stability_score(revenue, 5), 5) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_5d_z5_sldiff252_xlc_v102_signal(revenue, closeadj):
    base = _z(_f11_revenue_stability_score(revenue, 5), 5) * np.log1p(closeadj.abs())
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_5d_logm5_slpct5_xmc_v103_signal(revenue, closeadj):
    base = np.log1p(_mean(_f11_revenue_stability_score(revenue, 5), 5).clip(lower=0)) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_5d_sgnsq5_sldiff10_xrr_v104_signal(revenue, closeadj):
    base = (np.sign(_mean(_f11_revenue_stability_score(revenue, 5), 5)) * np.sqrt(_mean(_f11_revenue_stability_score(revenue, 5), 5).abs())) * (revenue / _mean(revenue, 63).replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_5d_diffx5_slpct21_xc_v105_signal(revenue, closeadj):
    base = _diff(_f11_revenue_stability_score(revenue, 5), 5) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_10d_rmean7_sldiff63_xlc_v106_signal(revenue, closeadj):
    base = _mean(_f11_revenue_stability_score(revenue, 10), 7) * np.log1p(closeadj.abs())
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_10d_rstd7_slpct126_xmc_v107_signal(revenue, closeadj):
    base = _std(_f11_revenue_stability_score(revenue, 10), 7) * _mean(closeadj, 21)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_10d_ema7_sldiff252_xrr_v108_signal(revenue, closeadj):
    base = _ema(_f11_revenue_stability_score(revenue, 10), 7) * (revenue / _mean(revenue, 63).replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_10d_z7_slpct5_xc_v109_signal(revenue, closeadj):
    base = _z(_f11_revenue_stability_score(revenue, 10), 7) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_10d_logm7_sldiff10_xlc_v110_signal(revenue, closeadj):
    base = np.log1p(_mean(_f11_revenue_stability_score(revenue, 10), 7).clip(lower=0)) * np.log1p(closeadj.abs())
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_10d_sgnsq7_slpct21_xmc_v111_signal(revenue, closeadj):
    base = (np.sign(_mean(_f11_revenue_stability_score(revenue, 10), 7)) * np.sqrt(_mean(_f11_revenue_stability_score(revenue, 10), 7).abs())) * _mean(closeadj, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_10d_diffx7_sldiff63_xrr_v112_signal(revenue, closeadj):
    base = _diff(_f11_revenue_stability_score(revenue, 10), 7) * (revenue / _mean(revenue, 63).replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_21d_rmean10_slpct126_xc_v113_signal(revenue, closeadj):
    base = _mean(_f11_revenue_stability_score(revenue, 21), 10) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_21d_rstd10_sldiff252_xlc_v114_signal(revenue, closeadj):
    base = _std(_f11_revenue_stability_score(revenue, 21), 10) * np.log1p(closeadj.abs())
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_21d_ema10_slpct5_xmc_v115_signal(revenue, closeadj):
    base = _ema(_f11_revenue_stability_score(revenue, 21), 10) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_21d_z10_sldiff10_xrr_v116_signal(revenue, closeadj):
    base = _z(_f11_revenue_stability_score(revenue, 21), 10) * (revenue / _mean(revenue, 63).replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_21d_logm10_slpct21_xc_v117_signal(revenue, closeadj):
    base = np.log1p(_mean(_f11_revenue_stability_score(revenue, 21), 10).clip(lower=0)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_21d_sgnsq10_sldiff63_xlc_v118_signal(revenue, closeadj):
    base = (np.sign(_mean(_f11_revenue_stability_score(revenue, 21), 10)) * np.sqrt(_mean(_f11_revenue_stability_score(revenue, 21), 10).abs())) * np.log1p(closeadj.abs())
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_21d_diffx10_slpct126_xmc_v119_signal(revenue, closeadj):
    base = _diff(_f11_revenue_stability_score(revenue, 21), 10) * _mean(closeadj, 21)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_42d_rmean21_sldiff252_xrr_v120_signal(revenue, closeadj):
    base = _mean(_f11_revenue_stability_score(revenue, 42), 21) * (revenue / _mean(revenue, 63).replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_42d_rstd21_slpct5_xc_v121_signal(revenue, closeadj):
    base = _std(_f11_revenue_stability_score(revenue, 42), 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_42d_ema21_sldiff10_xlc_v122_signal(revenue, closeadj):
    base = _ema(_f11_revenue_stability_score(revenue, 42), 21) * np.log1p(closeadj.abs())
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_42d_z21_slpct21_xmc_v123_signal(revenue, closeadj):
    base = _z(_f11_revenue_stability_score(revenue, 42), 21) * _mean(closeadj, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_42d_logm21_sldiff63_xrr_v124_signal(revenue, closeadj):
    base = np.log1p(_mean(_f11_revenue_stability_score(revenue, 42), 21).clip(lower=0)) * (revenue / _mean(revenue, 63).replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_42d_sgnsq21_slpct126_xc_v125_signal(revenue, closeadj):
    base = (np.sign(_mean(_f11_revenue_stability_score(revenue, 42), 21)) * np.sqrt(_mean(_f11_revenue_stability_score(revenue, 42), 21).abs())) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_42d_diffx21_sldiff252_xlc_v126_signal(revenue, closeadj):
    base = _diff(_f11_revenue_stability_score(revenue, 42), 21) * np.log1p(closeadj.abs())
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_63d_rmean31_slpct5_xmc_v127_signal(revenue, closeadj):
    base = _mean(_f11_revenue_stability_score(revenue, 63), 31) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_63d_rstd31_sldiff10_xrr_v128_signal(revenue, closeadj):
    base = _std(_f11_revenue_stability_score(revenue, 63), 31) * (revenue / _mean(revenue, 63).replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_63d_ema31_slpct21_xc_v129_signal(revenue, closeadj):
    base = _ema(_f11_revenue_stability_score(revenue, 63), 31) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_63d_z31_sldiff63_xlc_v130_signal(revenue, closeadj):
    base = _z(_f11_revenue_stability_score(revenue, 63), 31) * np.log1p(closeadj.abs())
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_63d_logm31_slpct126_xmc_v131_signal(revenue, closeadj):
    base = np.log1p(_mean(_f11_revenue_stability_score(revenue, 63), 31).clip(lower=0)) * _mean(closeadj, 21)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_63d_sgnsq31_sldiff252_xrr_v132_signal(revenue, closeadj):
    base = (np.sign(_mean(_f11_revenue_stability_score(revenue, 63), 31)) * np.sqrt(_mean(_f11_revenue_stability_score(revenue, 63), 31).abs())) * (revenue / _mean(revenue, 63).replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_63d_diffx31_slpct5_xc_v133_signal(revenue, closeadj):
    base = _diff(_f11_revenue_stability_score(revenue, 63), 31) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_126d_rmean63_sldiff10_xlc_v134_signal(revenue, closeadj):
    base = _mean(_f11_revenue_stability_score(revenue, 126), 63) * np.log1p(closeadj.abs())
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_126d_rstd63_slpct21_xmc_v135_signal(revenue, closeadj):
    base = _std(_f11_revenue_stability_score(revenue, 126), 63) * _mean(closeadj, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_126d_ema63_sldiff63_xrr_v136_signal(revenue, closeadj):
    base = _ema(_f11_revenue_stability_score(revenue, 126), 63) * (revenue / _mean(revenue, 63).replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_126d_z63_slpct126_xc_v137_signal(revenue, closeadj):
    base = _z(_f11_revenue_stability_score(revenue, 126), 63) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_126d_logm63_sldiff252_xlc_v138_signal(revenue, closeadj):
    base = np.log1p(_mean(_f11_revenue_stability_score(revenue, 126), 63).clip(lower=0)) * np.log1p(closeadj.abs())
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_126d_sgnsq63_slpct5_xmc_v139_signal(revenue, closeadj):
    base = (np.sign(_mean(_f11_revenue_stability_score(revenue, 126), 63)) * np.sqrt(_mean(_f11_revenue_stability_score(revenue, 126), 63).abs())) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_126d_diffx63_sldiff10_xrr_v140_signal(revenue, closeadj):
    base = _diff(_f11_revenue_stability_score(revenue, 126), 63) * (revenue / _mean(revenue, 63).replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_252d_rmean126_slpct21_xc_v141_signal(revenue, closeadj):
    base = _mean(_f11_revenue_stability_score(revenue, 252), 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_252d_rstd126_sldiff63_xlc_v142_signal(revenue, closeadj):
    base = _std(_f11_revenue_stability_score(revenue, 252), 126) * np.log1p(closeadj.abs())
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_252d_ema126_slpct126_xmc_v143_signal(revenue, closeadj):
    base = _ema(_f11_revenue_stability_score(revenue, 252), 126) * _mean(closeadj, 21)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_252d_z126_sldiff252_xrr_v144_signal(revenue, closeadj):
    base = _z(_f11_revenue_stability_score(revenue, 252), 126) * (revenue / _mean(revenue, 63).replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_252d_logm126_slpct5_xc_v145_signal(revenue, closeadj):
    base = np.log1p(_mean(_f11_revenue_stability_score(revenue, 252), 126).clip(lower=0)) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_252d_sgnsq126_sldiff10_xlc_v146_signal(revenue, closeadj):
    base = (np.sign(_mean(_f11_revenue_stability_score(revenue, 252), 126)) * np.sqrt(_mean(_f11_revenue_stability_score(revenue, 252), 126).abs())) * np.log1p(closeadj.abs())
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_252d_diffx126_slpct21_xmc_v147_signal(revenue, closeadj):
    base = _diff(_f11_revenue_stability_score(revenue, 252), 126) * _mean(closeadj, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revvol_21d_rmean10_sldiff10_xrr_v148_signal(revenue, closeadj):
    base = _mean(_f11_revenue_vol(revenue, 21), 10) * (revenue / _mean(revenue, 63).replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revcons_63d_ema31_slpct21_xlc_v149_signal(revenue, closeadj):
    base = _ema(_f11_revenue_consistency(revenue, 63), 31) * np.log1p(closeadj.abs())
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def drs_f11_defense_revenue_stability_revstab_126d_z63_sldiff63_xmc_v150_signal(revenue, closeadj):
    base = _z(_f11_revenue_stability_score(revenue, 126), 63) * _mean(closeadj, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    drs_f11_defense_revenue_stability_revvol_5d_rmean5_slpct5_xc_v001_signal,
    drs_f11_defense_revenue_stability_revvol_5d_rstd5_sldiff10_xlc_v002_signal,
    drs_f11_defense_revenue_stability_revvol_5d_ema5_slpct21_xmc_v003_signal,
    drs_f11_defense_revenue_stability_revvol_5d_z5_sldiff63_xrr_v004_signal,
    drs_f11_defense_revenue_stability_revvol_5d_logm5_slpct126_xc_v005_signal,
    drs_f11_defense_revenue_stability_revvol_5d_sgnsq5_sldiff252_xlc_v006_signal,
    drs_f11_defense_revenue_stability_revvol_5d_diffx5_slpct5_xmc_v007_signal,
    drs_f11_defense_revenue_stability_revvol_10d_rmean7_sldiff10_xrr_v008_signal,
    drs_f11_defense_revenue_stability_revvol_10d_rstd7_slpct21_xc_v009_signal,
    drs_f11_defense_revenue_stability_revvol_10d_ema7_sldiff63_xlc_v010_signal,
    drs_f11_defense_revenue_stability_revvol_10d_z7_slpct126_xmc_v011_signal,
    drs_f11_defense_revenue_stability_revvol_10d_logm7_sldiff252_xrr_v012_signal,
    drs_f11_defense_revenue_stability_revvol_10d_sgnsq7_slpct5_xc_v013_signal,
    drs_f11_defense_revenue_stability_revvol_10d_diffx7_sldiff10_xlc_v014_signal,
    drs_f11_defense_revenue_stability_revvol_21d_rmean10_slpct21_xmc_v015_signal,
    drs_f11_defense_revenue_stability_revvol_21d_rstd10_sldiff63_xrr_v016_signal,
    drs_f11_defense_revenue_stability_revvol_21d_ema10_slpct126_xc_v017_signal,
    drs_f11_defense_revenue_stability_revvol_21d_z10_sldiff252_xlc_v018_signal,
    drs_f11_defense_revenue_stability_revvol_21d_logm10_slpct5_xmc_v019_signal,
    drs_f11_defense_revenue_stability_revvol_21d_sgnsq10_sldiff10_xrr_v020_signal,
    drs_f11_defense_revenue_stability_revvol_21d_diffx10_slpct21_xc_v021_signal,
    drs_f11_defense_revenue_stability_revvol_42d_rmean21_sldiff63_xlc_v022_signal,
    drs_f11_defense_revenue_stability_revvol_42d_rstd21_slpct126_xmc_v023_signal,
    drs_f11_defense_revenue_stability_revvol_42d_ema21_sldiff252_xrr_v024_signal,
    drs_f11_defense_revenue_stability_revvol_42d_z21_slpct5_xc_v025_signal,
    drs_f11_defense_revenue_stability_revvol_42d_logm21_sldiff10_xlc_v026_signal,
    drs_f11_defense_revenue_stability_revvol_42d_sgnsq21_slpct21_xmc_v027_signal,
    drs_f11_defense_revenue_stability_revvol_42d_diffx21_sldiff63_xrr_v028_signal,
    drs_f11_defense_revenue_stability_revvol_63d_rmean31_slpct126_xc_v029_signal,
    drs_f11_defense_revenue_stability_revvol_63d_rstd31_sldiff252_xlc_v030_signal,
    drs_f11_defense_revenue_stability_revvol_63d_ema31_slpct5_xmc_v031_signal,
    drs_f11_defense_revenue_stability_revvol_63d_z31_sldiff10_xrr_v032_signal,
    drs_f11_defense_revenue_stability_revvol_63d_logm31_slpct21_xc_v033_signal,
    drs_f11_defense_revenue_stability_revvol_63d_sgnsq31_sldiff63_xlc_v034_signal,
    drs_f11_defense_revenue_stability_revvol_63d_diffx31_slpct126_xmc_v035_signal,
    drs_f11_defense_revenue_stability_revvol_126d_rmean63_sldiff252_xrr_v036_signal,
    drs_f11_defense_revenue_stability_revvol_126d_rstd63_slpct5_xc_v037_signal,
    drs_f11_defense_revenue_stability_revvol_126d_ema63_sldiff10_xlc_v038_signal,
    drs_f11_defense_revenue_stability_revvol_126d_z63_slpct21_xmc_v039_signal,
    drs_f11_defense_revenue_stability_revvol_126d_logm63_sldiff63_xrr_v040_signal,
    drs_f11_defense_revenue_stability_revvol_126d_sgnsq63_slpct126_xc_v041_signal,
    drs_f11_defense_revenue_stability_revvol_126d_diffx63_sldiff252_xlc_v042_signal,
    drs_f11_defense_revenue_stability_revvol_252d_rmean126_slpct5_xmc_v043_signal,
    drs_f11_defense_revenue_stability_revvol_252d_rstd126_sldiff10_xrr_v044_signal,
    drs_f11_defense_revenue_stability_revvol_252d_ema126_slpct21_xc_v045_signal,
    drs_f11_defense_revenue_stability_revvol_252d_z126_sldiff63_xlc_v046_signal,
    drs_f11_defense_revenue_stability_revvol_252d_logm126_slpct126_xmc_v047_signal,
    drs_f11_defense_revenue_stability_revvol_252d_sgnsq126_sldiff252_xrr_v048_signal,
    drs_f11_defense_revenue_stability_revvol_252d_diffx126_slpct5_xc_v049_signal,
    drs_f11_defense_revenue_stability_revcons_5d_rmean5_sldiff10_xlc_v050_signal,
    drs_f11_defense_revenue_stability_revcons_5d_rstd5_slpct21_xmc_v051_signal,
    drs_f11_defense_revenue_stability_revcons_5d_ema5_sldiff63_xrr_v052_signal,
    drs_f11_defense_revenue_stability_revcons_5d_z5_slpct126_xc_v053_signal,
    drs_f11_defense_revenue_stability_revcons_5d_logm5_sldiff252_xlc_v054_signal,
    drs_f11_defense_revenue_stability_revcons_5d_sgnsq5_slpct5_xmc_v055_signal,
    drs_f11_defense_revenue_stability_revcons_5d_diffx5_sldiff10_xrr_v056_signal,
    drs_f11_defense_revenue_stability_revcons_10d_rmean7_slpct21_xc_v057_signal,
    drs_f11_defense_revenue_stability_revcons_10d_rstd7_sldiff63_xlc_v058_signal,
    drs_f11_defense_revenue_stability_revcons_10d_ema7_slpct126_xmc_v059_signal,
    drs_f11_defense_revenue_stability_revcons_10d_z7_sldiff252_xrr_v060_signal,
    drs_f11_defense_revenue_stability_revcons_10d_logm7_slpct5_xc_v061_signal,
    drs_f11_defense_revenue_stability_revcons_10d_sgnsq7_sldiff10_xlc_v062_signal,
    drs_f11_defense_revenue_stability_revcons_10d_diffx7_slpct21_xmc_v063_signal,
    drs_f11_defense_revenue_stability_revcons_21d_rmean10_sldiff63_xrr_v064_signal,
    drs_f11_defense_revenue_stability_revcons_21d_rstd10_slpct126_xc_v065_signal,
    drs_f11_defense_revenue_stability_revcons_21d_ema10_sldiff252_xlc_v066_signal,
    drs_f11_defense_revenue_stability_revcons_21d_z10_slpct5_xmc_v067_signal,
    drs_f11_defense_revenue_stability_revcons_21d_logm10_sldiff10_xrr_v068_signal,
    drs_f11_defense_revenue_stability_revcons_21d_sgnsq10_slpct21_xc_v069_signal,
    drs_f11_defense_revenue_stability_revcons_21d_diffx10_sldiff63_xlc_v070_signal,
    drs_f11_defense_revenue_stability_revcons_42d_rmean21_slpct126_xmc_v071_signal,
    drs_f11_defense_revenue_stability_revcons_42d_rstd21_sldiff252_xrr_v072_signal,
    drs_f11_defense_revenue_stability_revcons_42d_ema21_slpct5_xc_v073_signal,
    drs_f11_defense_revenue_stability_revcons_42d_z21_sldiff10_xlc_v074_signal,
    drs_f11_defense_revenue_stability_revcons_42d_logm21_slpct21_xmc_v075_signal,
    drs_f11_defense_revenue_stability_revcons_42d_sgnsq21_sldiff63_xrr_v076_signal,
    drs_f11_defense_revenue_stability_revcons_42d_diffx21_slpct126_xc_v077_signal,
    drs_f11_defense_revenue_stability_revcons_63d_rmean31_sldiff252_xlc_v078_signal,
    drs_f11_defense_revenue_stability_revcons_63d_rstd31_slpct5_xmc_v079_signal,
    drs_f11_defense_revenue_stability_revcons_63d_ema31_sldiff10_xrr_v080_signal,
    drs_f11_defense_revenue_stability_revcons_63d_z31_slpct21_xc_v081_signal,
    drs_f11_defense_revenue_stability_revcons_63d_logm31_sldiff63_xlc_v082_signal,
    drs_f11_defense_revenue_stability_revcons_63d_sgnsq31_slpct126_xmc_v083_signal,
    drs_f11_defense_revenue_stability_revcons_63d_diffx31_sldiff252_xrr_v084_signal,
    drs_f11_defense_revenue_stability_revcons_126d_rmean63_slpct5_xc_v085_signal,
    drs_f11_defense_revenue_stability_revcons_126d_rstd63_sldiff10_xlc_v086_signal,
    drs_f11_defense_revenue_stability_revcons_126d_ema63_slpct21_xmc_v087_signal,
    drs_f11_defense_revenue_stability_revcons_126d_z63_sldiff63_xrr_v088_signal,
    drs_f11_defense_revenue_stability_revcons_126d_logm63_slpct126_xc_v089_signal,
    drs_f11_defense_revenue_stability_revcons_126d_sgnsq63_sldiff252_xlc_v090_signal,
    drs_f11_defense_revenue_stability_revcons_126d_diffx63_slpct5_xmc_v091_signal,
    drs_f11_defense_revenue_stability_revcons_252d_rmean126_sldiff10_xrr_v092_signal,
    drs_f11_defense_revenue_stability_revcons_252d_rstd126_slpct21_xc_v093_signal,
    drs_f11_defense_revenue_stability_revcons_252d_ema126_sldiff63_xlc_v094_signal,
    drs_f11_defense_revenue_stability_revcons_252d_z126_slpct126_xmc_v095_signal,
    drs_f11_defense_revenue_stability_revcons_252d_logm126_sldiff252_xrr_v096_signal,
    drs_f11_defense_revenue_stability_revcons_252d_sgnsq126_slpct5_xc_v097_signal,
    drs_f11_defense_revenue_stability_revcons_252d_diffx126_sldiff10_xlc_v098_signal,
    drs_f11_defense_revenue_stability_revstab_5d_rmean5_slpct21_xmc_v099_signal,
    drs_f11_defense_revenue_stability_revstab_5d_rstd5_sldiff63_xrr_v100_signal,
    drs_f11_defense_revenue_stability_revstab_5d_ema5_slpct126_xc_v101_signal,
    drs_f11_defense_revenue_stability_revstab_5d_z5_sldiff252_xlc_v102_signal,
    drs_f11_defense_revenue_stability_revstab_5d_logm5_slpct5_xmc_v103_signal,
    drs_f11_defense_revenue_stability_revstab_5d_sgnsq5_sldiff10_xrr_v104_signal,
    drs_f11_defense_revenue_stability_revstab_5d_diffx5_slpct21_xc_v105_signal,
    drs_f11_defense_revenue_stability_revstab_10d_rmean7_sldiff63_xlc_v106_signal,
    drs_f11_defense_revenue_stability_revstab_10d_rstd7_slpct126_xmc_v107_signal,
    drs_f11_defense_revenue_stability_revstab_10d_ema7_sldiff252_xrr_v108_signal,
    drs_f11_defense_revenue_stability_revstab_10d_z7_slpct5_xc_v109_signal,
    drs_f11_defense_revenue_stability_revstab_10d_logm7_sldiff10_xlc_v110_signal,
    drs_f11_defense_revenue_stability_revstab_10d_sgnsq7_slpct21_xmc_v111_signal,
    drs_f11_defense_revenue_stability_revstab_10d_diffx7_sldiff63_xrr_v112_signal,
    drs_f11_defense_revenue_stability_revstab_21d_rmean10_slpct126_xc_v113_signal,
    drs_f11_defense_revenue_stability_revstab_21d_rstd10_sldiff252_xlc_v114_signal,
    drs_f11_defense_revenue_stability_revstab_21d_ema10_slpct5_xmc_v115_signal,
    drs_f11_defense_revenue_stability_revstab_21d_z10_sldiff10_xrr_v116_signal,
    drs_f11_defense_revenue_stability_revstab_21d_logm10_slpct21_xc_v117_signal,
    drs_f11_defense_revenue_stability_revstab_21d_sgnsq10_sldiff63_xlc_v118_signal,
    drs_f11_defense_revenue_stability_revstab_21d_diffx10_slpct126_xmc_v119_signal,
    drs_f11_defense_revenue_stability_revstab_42d_rmean21_sldiff252_xrr_v120_signal,
    drs_f11_defense_revenue_stability_revstab_42d_rstd21_slpct5_xc_v121_signal,
    drs_f11_defense_revenue_stability_revstab_42d_ema21_sldiff10_xlc_v122_signal,
    drs_f11_defense_revenue_stability_revstab_42d_z21_slpct21_xmc_v123_signal,
    drs_f11_defense_revenue_stability_revstab_42d_logm21_sldiff63_xrr_v124_signal,
    drs_f11_defense_revenue_stability_revstab_42d_sgnsq21_slpct126_xc_v125_signal,
    drs_f11_defense_revenue_stability_revstab_42d_diffx21_sldiff252_xlc_v126_signal,
    drs_f11_defense_revenue_stability_revstab_63d_rmean31_slpct5_xmc_v127_signal,
    drs_f11_defense_revenue_stability_revstab_63d_rstd31_sldiff10_xrr_v128_signal,
    drs_f11_defense_revenue_stability_revstab_63d_ema31_slpct21_xc_v129_signal,
    drs_f11_defense_revenue_stability_revstab_63d_z31_sldiff63_xlc_v130_signal,
    drs_f11_defense_revenue_stability_revstab_63d_logm31_slpct126_xmc_v131_signal,
    drs_f11_defense_revenue_stability_revstab_63d_sgnsq31_sldiff252_xrr_v132_signal,
    drs_f11_defense_revenue_stability_revstab_63d_diffx31_slpct5_xc_v133_signal,
    drs_f11_defense_revenue_stability_revstab_126d_rmean63_sldiff10_xlc_v134_signal,
    drs_f11_defense_revenue_stability_revstab_126d_rstd63_slpct21_xmc_v135_signal,
    drs_f11_defense_revenue_stability_revstab_126d_ema63_sldiff63_xrr_v136_signal,
    drs_f11_defense_revenue_stability_revstab_126d_z63_slpct126_xc_v137_signal,
    drs_f11_defense_revenue_stability_revstab_126d_logm63_sldiff252_xlc_v138_signal,
    drs_f11_defense_revenue_stability_revstab_126d_sgnsq63_slpct5_xmc_v139_signal,
    drs_f11_defense_revenue_stability_revstab_126d_diffx63_sldiff10_xrr_v140_signal,
    drs_f11_defense_revenue_stability_revstab_252d_rmean126_slpct21_xc_v141_signal,
    drs_f11_defense_revenue_stability_revstab_252d_rstd126_sldiff63_xlc_v142_signal,
    drs_f11_defense_revenue_stability_revstab_252d_ema126_slpct126_xmc_v143_signal,
    drs_f11_defense_revenue_stability_revstab_252d_z126_sldiff252_xrr_v144_signal,
    drs_f11_defense_revenue_stability_revstab_252d_logm126_slpct5_xc_v145_signal,
    drs_f11_defense_revenue_stability_revstab_252d_sgnsq126_sldiff10_xlc_v146_signal,
    drs_f11_defense_revenue_stability_revstab_252d_diffx126_slpct21_xmc_v147_signal,
    drs_f11_defense_revenue_stability_revvol_21d_rmean10_sldiff10_xrr_v148_signal,
    drs_f11_defense_revenue_stability_revcons_63d_ema31_slpct21_xlc_v149_signal,
    drs_f11_defense_revenue_stability_revstab_126d_z63_sldiff63_xmc_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F11_DEFENSE_REVENUE_STABILITY_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")

    cols = {
        "closeadj": closeadj,
        "revenue": revenue,
        "netinc": netinc,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f11_revenue_vol", "_f11_revenue_consistency", "_f11_revenue_stability_score",)
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
    print(f"OK f11_defense_revenue_stability_2nd_derivatives_001_150_claude: {n_features} features pass")
