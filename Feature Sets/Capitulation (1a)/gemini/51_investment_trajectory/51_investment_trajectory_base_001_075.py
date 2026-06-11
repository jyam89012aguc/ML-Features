"""
51_investment_trajectory — Base Features 001-075
Domain: investment_trajectory
Asset class: Equities
Target context: Capitulation
"""
import numpy as np
import pandas as pd

# ── Utility helpers ──────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

def _safe_div(a: pd.Series, b: pd.Series) -> pd.Series:
    return a / b.replace(0, _EPS)

def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).mean()

def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).max()

def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).min()

def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).std().fillna(0)

def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div((s - m), sd)

def _rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).rank(pct=True)

# ── Feature functions ────────────────────────────────────────────────────────

def invt_001_capex_abs_lvl_5d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_001_capex_abs_lvl_5d"""
    base = capex.abs()
    return _rolling_mean(base, 5)

def invt_002_capex_abs_zscore_5d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_002_capex_abs_zscore_5d"""
    base = capex.abs()
    return _zscore_rolling(base, 5)

def invt_003_capex_abs_rank_5d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_003_capex_abs_rank_5d"""
    base = capex.abs()
    return _rank_pct(base, 5)

def invt_004_capex_abs_lvl_21d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_004_capex_abs_lvl_21d"""
    base = capex.abs()
    return _rolling_mean(base, 21)

def invt_005_capex_abs_zscore_21d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_005_capex_abs_zscore_21d"""
    base = capex.abs()
    return _zscore_rolling(base, 21)

def invt_006_capex_abs_rank_21d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_006_capex_abs_rank_21d"""
    base = capex.abs()
    return _rank_pct(base, 21)

def invt_007_capex_abs_lvl_63d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_007_capex_abs_lvl_63d"""
    base = capex.abs()
    return _rolling_mean(base, 63)

def invt_008_capex_abs_zscore_63d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_008_capex_abs_zscore_63d"""
    base = capex.abs()
    return _zscore_rolling(base, 63)

def invt_009_capex_abs_rank_63d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_009_capex_abs_rank_63d"""
    base = capex.abs()
    return _rank_pct(base, 63)

def invt_010_capex_abs_lvl_126d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_010_capex_abs_lvl_126d"""
    base = capex.abs()
    return _rolling_mean(base, 126)

def invt_011_capex_abs_zscore_126d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_011_capex_abs_zscore_126d"""
    base = capex.abs()
    return _zscore_rolling(base, 126)

def invt_012_capex_abs_rank_126d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_012_capex_abs_rank_126d"""
    base = capex.abs()
    return _rank_pct(base, 126)

def invt_013_capex_abs_lvl_252d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_013_capex_abs_lvl_252d"""
    base = capex.abs()
    return _rolling_mean(base, 252)

def invt_014_capex_abs_zscore_252d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_014_capex_abs_zscore_252d"""
    base = capex.abs()
    return _zscore_rolling(base, 252)

def invt_015_capex_abs_rank_252d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_015_capex_abs_rank_252d"""
    base = capex.abs()
    return _rank_pct(base, 252)

def invt_016_ncfi_abs_lvl_5d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_016_ncfi_abs_lvl_5d"""
    base = ncfi.abs()
    return _rolling_mean(base, 5)

def invt_017_ncfi_abs_zscore_5d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_017_ncfi_abs_zscore_5d"""
    base = ncfi.abs()
    return _zscore_rolling(base, 5)

def invt_018_ncfi_abs_rank_5d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_018_ncfi_abs_rank_5d"""
    base = ncfi.abs()
    return _rank_pct(base, 5)

def invt_019_ncfi_abs_lvl_21d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_019_ncfi_abs_lvl_21d"""
    base = ncfi.abs()
    return _rolling_mean(base, 21)

def invt_020_ncfi_abs_zscore_21d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_020_ncfi_abs_zscore_21d"""
    base = ncfi.abs()
    return _zscore_rolling(base, 21)

def invt_021_ncfi_abs_rank_21d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_021_ncfi_abs_rank_21d"""
    base = ncfi.abs()
    return _rank_pct(base, 21)

def invt_022_ncfi_abs_lvl_63d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_022_ncfi_abs_lvl_63d"""
    base = ncfi.abs()
    return _rolling_mean(base, 63)

def invt_023_ncfi_abs_zscore_63d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_023_ncfi_abs_zscore_63d"""
    base = ncfi.abs()
    return _zscore_rolling(base, 63)

def invt_024_ncfi_abs_rank_63d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_024_ncfi_abs_rank_63d"""
    base = ncfi.abs()
    return _rank_pct(base, 63)

def invt_025_ncfi_abs_lvl_126d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_025_ncfi_abs_lvl_126d"""
    base = ncfi.abs()
    return _rolling_mean(base, 126)

def invt_026_ncfi_abs_zscore_126d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_026_ncfi_abs_zscore_126d"""
    base = ncfi.abs()
    return _zscore_rolling(base, 126)

def invt_027_ncfi_abs_rank_126d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_027_ncfi_abs_rank_126d"""
    base = ncfi.abs()
    return _rank_pct(base, 126)

def invt_028_ncfi_abs_lvl_252d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_028_ncfi_abs_lvl_252d"""
    base = ncfi.abs()
    return _rolling_mean(base, 252)

def invt_029_ncfi_abs_zscore_252d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_029_ncfi_abs_zscore_252d"""
    base = ncfi.abs()
    return _zscore_rolling(base, 252)

def invt_030_ncfi_abs_rank_252d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_030_ncfi_abs_rank_252d"""
    base = ncfi.abs()
    return _rank_pct(base, 252)

def invt_031_rnd_lvl_lvl_5d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_031_rnd_lvl_lvl_5d"""
    base = rnd.fillna(0)
    return _rolling_mean(base, 5)

def invt_032_rnd_lvl_zscore_5d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_032_rnd_lvl_zscore_5d"""
    base = rnd.fillna(0)
    return _zscore_rolling(base, 5)

def invt_033_rnd_lvl_rank_5d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_033_rnd_lvl_rank_5d"""
    base = rnd.fillna(0)
    return _rank_pct(base, 5)

def invt_034_rnd_lvl_lvl_21d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_034_rnd_lvl_lvl_21d"""
    base = rnd.fillna(0)
    return _rolling_mean(base, 21)

def invt_035_rnd_lvl_zscore_21d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_035_rnd_lvl_zscore_21d"""
    base = rnd.fillna(0)
    return _zscore_rolling(base, 21)

def invt_036_rnd_lvl_rank_21d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_036_rnd_lvl_rank_21d"""
    base = rnd.fillna(0)
    return _rank_pct(base, 21)

def invt_037_rnd_lvl_lvl_63d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_037_rnd_lvl_lvl_63d"""
    base = rnd.fillna(0)
    return _rolling_mean(base, 63)

def invt_038_rnd_lvl_zscore_63d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_038_rnd_lvl_zscore_63d"""
    base = rnd.fillna(0)
    return _zscore_rolling(base, 63)

def invt_039_rnd_lvl_rank_63d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_039_rnd_lvl_rank_63d"""
    base = rnd.fillna(0)
    return _rank_pct(base, 63)

def invt_040_rnd_lvl_lvl_126d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_040_rnd_lvl_lvl_126d"""
    base = rnd.fillna(0)
    return _rolling_mean(base, 126)

def invt_041_rnd_lvl_zscore_126d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_041_rnd_lvl_zscore_126d"""
    base = rnd.fillna(0)
    return _zscore_rolling(base, 126)

def invt_042_rnd_lvl_rank_126d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_042_rnd_lvl_rank_126d"""
    base = rnd.fillna(0)
    return _rank_pct(base, 126)

def invt_043_rnd_lvl_lvl_252d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_043_rnd_lvl_lvl_252d"""
    base = rnd.fillna(0)
    return _rolling_mean(base, 252)

def invt_044_rnd_lvl_zscore_252d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_044_rnd_lvl_zscore_252d"""
    base = rnd.fillna(0)
    return _zscore_rolling(base, 252)

def invt_045_rnd_lvl_rank_252d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_045_rnd_lvl_rank_252d"""
    base = rnd.fillna(0)
    return _rank_pct(base, 252)

def invt_046_total_inv_lvl_5d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_046_total_inv_lvl_5d"""
    base = capex.abs().fillna(0) + rnd.fillna(0)
    return _rolling_mean(base, 5)

def invt_047_total_inv_zscore_5d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_047_total_inv_zscore_5d"""
    base = capex.abs().fillna(0) + rnd.fillna(0)
    return _zscore_rolling(base, 5)

def invt_048_total_inv_rank_5d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_048_total_inv_rank_5d"""
    base = capex.abs().fillna(0) + rnd.fillna(0)
    return _rank_pct(base, 5)

def invt_049_total_inv_lvl_21d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_049_total_inv_lvl_21d"""
    base = capex.abs().fillna(0) + rnd.fillna(0)
    return _rolling_mean(base, 21)

def invt_050_total_inv_zscore_21d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_050_total_inv_zscore_21d"""
    base = capex.abs().fillna(0) + rnd.fillna(0)
    return _zscore_rolling(base, 21)

def invt_051_total_inv_rank_21d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_051_total_inv_rank_21d"""
    base = capex.abs().fillna(0) + rnd.fillna(0)
    return _rank_pct(base, 21)

def invt_052_total_inv_lvl_63d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_052_total_inv_lvl_63d"""
    base = capex.abs().fillna(0) + rnd.fillna(0)
    return _rolling_mean(base, 63)

def invt_053_total_inv_zscore_63d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_053_total_inv_zscore_63d"""
    base = capex.abs().fillna(0) + rnd.fillna(0)
    return _zscore_rolling(base, 63)

def invt_054_total_inv_rank_63d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_054_total_inv_rank_63d"""
    base = capex.abs().fillna(0) + rnd.fillna(0)
    return _rank_pct(base, 63)

def invt_055_total_inv_lvl_126d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_055_total_inv_lvl_126d"""
    base = capex.abs().fillna(0) + rnd.fillna(0)
    return _rolling_mean(base, 126)

def invt_056_total_inv_zscore_126d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_056_total_inv_zscore_126d"""
    base = capex.abs().fillna(0) + rnd.fillna(0)
    return _zscore_rolling(base, 126)

def invt_057_total_inv_rank_126d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_057_total_inv_rank_126d"""
    base = capex.abs().fillna(0) + rnd.fillna(0)
    return _rank_pct(base, 126)

def invt_058_total_inv_lvl_252d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_058_total_inv_lvl_252d"""
    base = capex.abs().fillna(0) + rnd.fillna(0)
    return _rolling_mean(base, 252)

def invt_059_total_inv_zscore_252d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_059_total_inv_zscore_252d"""
    base = capex.abs().fillna(0) + rnd.fillna(0)
    return _zscore_rolling(base, 252)

def invt_060_total_inv_rank_252d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_060_total_inv_rank_252d"""
    base = capex.abs().fillna(0) + rnd.fillna(0)
    return _rank_pct(base, 252)

def invt_061_inv_intensity_lvl_5d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_061_inv_intensity_lvl_5d"""
    base = _safe_div(capex.abs().fillna(0) + rnd.fillna(0), revenue)
    return _rolling_mean(base, 5)

def invt_062_inv_intensity_zscore_5d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_062_inv_intensity_zscore_5d"""
    base = _safe_div(capex.abs().fillna(0) + rnd.fillna(0), revenue)
    return _zscore_rolling(base, 5)

def invt_063_inv_intensity_rank_5d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_063_inv_intensity_rank_5d"""
    base = _safe_div(capex.abs().fillna(0) + rnd.fillna(0), revenue)
    return _rank_pct(base, 5)

def invt_064_inv_intensity_lvl_21d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_064_inv_intensity_lvl_21d"""
    base = _safe_div(capex.abs().fillna(0) + rnd.fillna(0), revenue)
    return _rolling_mean(base, 21)

def invt_065_inv_intensity_zscore_21d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_065_inv_intensity_zscore_21d"""
    base = _safe_div(capex.abs().fillna(0) + rnd.fillna(0), revenue)
    return _zscore_rolling(base, 21)

def invt_066_inv_intensity_rank_21d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_066_inv_intensity_rank_21d"""
    base = _safe_div(capex.abs().fillna(0) + rnd.fillna(0), revenue)
    return _rank_pct(base, 21)

def invt_067_inv_intensity_lvl_63d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_067_inv_intensity_lvl_63d"""
    base = _safe_div(capex.abs().fillna(0) + rnd.fillna(0), revenue)
    return _rolling_mean(base, 63)

def invt_068_inv_intensity_zscore_63d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_068_inv_intensity_zscore_63d"""
    base = _safe_div(capex.abs().fillna(0) + rnd.fillna(0), revenue)
    return _zscore_rolling(base, 63)

def invt_069_inv_intensity_rank_63d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_069_inv_intensity_rank_63d"""
    base = _safe_div(capex.abs().fillna(0) + rnd.fillna(0), revenue)
    return _rank_pct(base, 63)

def invt_070_inv_intensity_lvl_126d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_070_inv_intensity_lvl_126d"""
    base = _safe_div(capex.abs().fillna(0) + rnd.fillna(0), revenue)
    return _rolling_mean(base, 126)

def invt_071_inv_intensity_zscore_126d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_071_inv_intensity_zscore_126d"""
    base = _safe_div(capex.abs().fillna(0) + rnd.fillna(0), revenue)
    return _zscore_rolling(base, 126)

def invt_072_inv_intensity_rank_126d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_072_inv_intensity_rank_126d"""
    base = _safe_div(capex.abs().fillna(0) + rnd.fillna(0), revenue)
    return _rank_pct(base, 126)

def invt_073_inv_intensity_lvl_252d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_073_inv_intensity_lvl_252d"""
    base = _safe_div(capex.abs().fillna(0) + rnd.fillna(0), revenue)
    return _rolling_mean(base, 252)

def invt_074_inv_intensity_zscore_252d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_074_inv_intensity_zscore_252d"""
    base = _safe_div(capex.abs().fillna(0) + rnd.fillna(0), revenue)
    return _zscore_rolling(base, 252)

def invt_075_inv_intensity_rank_252d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_075_inv_intensity_rank_252d"""
    base = _safe_div(capex.abs().fillna(0) + rnd.fillna(0), revenue)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V51_REGISTRY = {
    "invt_001_capex_abs_lvl_5d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_001_capex_abs_lvl_5d},
    "invt_002_capex_abs_zscore_5d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_002_capex_abs_zscore_5d},
    "invt_003_capex_abs_rank_5d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_003_capex_abs_rank_5d},
    "invt_004_capex_abs_lvl_21d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_004_capex_abs_lvl_21d},
    "invt_005_capex_abs_zscore_21d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_005_capex_abs_zscore_21d},
    "invt_006_capex_abs_rank_21d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_006_capex_abs_rank_21d},
    "invt_007_capex_abs_lvl_63d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_007_capex_abs_lvl_63d},
    "invt_008_capex_abs_zscore_63d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_008_capex_abs_zscore_63d},
    "invt_009_capex_abs_rank_63d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_009_capex_abs_rank_63d},
    "invt_010_capex_abs_lvl_126d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_010_capex_abs_lvl_126d},
    "invt_011_capex_abs_zscore_126d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_011_capex_abs_zscore_126d},
    "invt_012_capex_abs_rank_126d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_012_capex_abs_rank_126d},
    "invt_013_capex_abs_lvl_252d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_013_capex_abs_lvl_252d},
    "invt_014_capex_abs_zscore_252d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_014_capex_abs_zscore_252d},
    "invt_015_capex_abs_rank_252d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_015_capex_abs_rank_252d},
    "invt_016_ncfi_abs_lvl_5d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_016_ncfi_abs_lvl_5d},
    "invt_017_ncfi_abs_zscore_5d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_017_ncfi_abs_zscore_5d},
    "invt_018_ncfi_abs_rank_5d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_018_ncfi_abs_rank_5d},
    "invt_019_ncfi_abs_lvl_21d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_019_ncfi_abs_lvl_21d},
    "invt_020_ncfi_abs_zscore_21d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_020_ncfi_abs_zscore_21d},
    "invt_021_ncfi_abs_rank_21d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_021_ncfi_abs_rank_21d},
    "invt_022_ncfi_abs_lvl_63d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_022_ncfi_abs_lvl_63d},
    "invt_023_ncfi_abs_zscore_63d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_023_ncfi_abs_zscore_63d},
    "invt_024_ncfi_abs_rank_63d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_024_ncfi_abs_rank_63d},
    "invt_025_ncfi_abs_lvl_126d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_025_ncfi_abs_lvl_126d},
    "invt_026_ncfi_abs_zscore_126d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_026_ncfi_abs_zscore_126d},
    "invt_027_ncfi_abs_rank_126d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_027_ncfi_abs_rank_126d},
    "invt_028_ncfi_abs_lvl_252d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_028_ncfi_abs_lvl_252d},
    "invt_029_ncfi_abs_zscore_252d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_029_ncfi_abs_zscore_252d},
    "invt_030_ncfi_abs_rank_252d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_030_ncfi_abs_rank_252d},
    "invt_031_rnd_lvl_lvl_5d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_031_rnd_lvl_lvl_5d},
    "invt_032_rnd_lvl_zscore_5d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_032_rnd_lvl_zscore_5d},
    "invt_033_rnd_lvl_rank_5d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_033_rnd_lvl_rank_5d},
    "invt_034_rnd_lvl_lvl_21d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_034_rnd_lvl_lvl_21d},
    "invt_035_rnd_lvl_zscore_21d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_035_rnd_lvl_zscore_21d},
    "invt_036_rnd_lvl_rank_21d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_036_rnd_lvl_rank_21d},
    "invt_037_rnd_lvl_lvl_63d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_037_rnd_lvl_lvl_63d},
    "invt_038_rnd_lvl_zscore_63d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_038_rnd_lvl_zscore_63d},
    "invt_039_rnd_lvl_rank_63d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_039_rnd_lvl_rank_63d},
    "invt_040_rnd_lvl_lvl_126d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_040_rnd_lvl_lvl_126d},
    "invt_041_rnd_lvl_zscore_126d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_041_rnd_lvl_zscore_126d},
    "invt_042_rnd_lvl_rank_126d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_042_rnd_lvl_rank_126d},
    "invt_043_rnd_lvl_lvl_252d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_043_rnd_lvl_lvl_252d},
    "invt_044_rnd_lvl_zscore_252d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_044_rnd_lvl_zscore_252d},
    "invt_045_rnd_lvl_rank_252d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_045_rnd_lvl_rank_252d},
    "invt_046_total_inv_lvl_5d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_046_total_inv_lvl_5d},
    "invt_047_total_inv_zscore_5d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_047_total_inv_zscore_5d},
    "invt_048_total_inv_rank_5d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_048_total_inv_rank_5d},
    "invt_049_total_inv_lvl_21d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_049_total_inv_lvl_21d},
    "invt_050_total_inv_zscore_21d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_050_total_inv_zscore_21d},
    "invt_051_total_inv_rank_21d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_051_total_inv_rank_21d},
    "invt_052_total_inv_lvl_63d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_052_total_inv_lvl_63d},
    "invt_053_total_inv_zscore_63d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_053_total_inv_zscore_63d},
    "invt_054_total_inv_rank_63d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_054_total_inv_rank_63d},
    "invt_055_total_inv_lvl_126d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_055_total_inv_lvl_126d},
    "invt_056_total_inv_zscore_126d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_056_total_inv_zscore_126d},
    "invt_057_total_inv_rank_126d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_057_total_inv_rank_126d},
    "invt_058_total_inv_lvl_252d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_058_total_inv_lvl_252d},
    "invt_059_total_inv_zscore_252d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_059_total_inv_zscore_252d},
    "invt_060_total_inv_rank_252d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_060_total_inv_rank_252d},
    "invt_061_inv_intensity_lvl_5d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_061_inv_intensity_lvl_5d},
    "invt_062_inv_intensity_zscore_5d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_062_inv_intensity_zscore_5d},
    "invt_063_inv_intensity_rank_5d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_063_inv_intensity_rank_5d},
    "invt_064_inv_intensity_lvl_21d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_064_inv_intensity_lvl_21d},
    "invt_065_inv_intensity_zscore_21d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_065_inv_intensity_zscore_21d},
    "invt_066_inv_intensity_rank_21d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_066_inv_intensity_rank_21d},
    "invt_067_inv_intensity_lvl_63d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_067_inv_intensity_lvl_63d},
    "invt_068_inv_intensity_zscore_63d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_068_inv_intensity_zscore_63d},
    "invt_069_inv_intensity_rank_63d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_069_inv_intensity_rank_63d},
    "invt_070_inv_intensity_lvl_126d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_070_inv_intensity_lvl_126d},
    "invt_071_inv_intensity_zscore_126d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_071_inv_intensity_zscore_126d},
    "invt_072_inv_intensity_rank_126d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_072_inv_intensity_rank_126d},
    "invt_073_inv_intensity_lvl_252d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_073_inv_intensity_lvl_252d},
    "invt_074_inv_intensity_zscore_252d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_074_inv_intensity_zscore_252d},
    "invt_075_inv_intensity_rank_252d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_075_inv_intensity_rank_252d},
}
