"""
40_leverage_and_solvency — Base Features 001-075
Domain: leverage_and_solvency
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

def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).std().fillna(0)

def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div((s - m), sd)

def _rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).rank(pct=True)

# ── Feature functions ────────────────────────────────────────────────────────

def solv_001_debt_lvl_lvl_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_001_debt_lvl_lvl_5d"""
    base = debt
    return _rolling_mean(base, 5)

def solv_002_debt_lvl_zscore_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_002_debt_lvl_zscore_5d"""
    base = debt
    return _zscore_rolling(base, 5)

def solv_003_debt_lvl_rank_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_003_debt_lvl_rank_5d"""
    base = debt
    return _rank_pct(base, 5)

def solv_004_debt_lvl_lvl_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_004_debt_lvl_lvl_21d"""
    base = debt
    return _rolling_mean(base, 21)

def solv_005_debt_lvl_zscore_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_005_debt_lvl_zscore_21d"""
    base = debt
    return _zscore_rolling(base, 21)

def solv_006_debt_lvl_rank_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_006_debt_lvl_rank_21d"""
    base = debt
    return _rank_pct(base, 21)

def solv_007_debt_lvl_lvl_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_007_debt_lvl_lvl_63d"""
    base = debt
    return _rolling_mean(base, 63)

def solv_008_debt_lvl_zscore_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_008_debt_lvl_zscore_63d"""
    base = debt
    return _zscore_rolling(base, 63)

def solv_009_debt_lvl_rank_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_009_debt_lvl_rank_63d"""
    base = debt
    return _rank_pct(base, 63)

def solv_010_debt_lvl_lvl_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_010_debt_lvl_lvl_126d"""
    base = debt
    return _rolling_mean(base, 126)

def solv_011_debt_lvl_zscore_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_011_debt_lvl_zscore_126d"""
    base = debt
    return _zscore_rolling(base, 126)

def solv_012_debt_lvl_rank_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_012_debt_lvl_rank_126d"""
    base = debt
    return _rank_pct(base, 126)

def solv_013_debt_lvl_lvl_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_013_debt_lvl_lvl_252d"""
    base = debt
    return _rolling_mean(base, 252)

def solv_014_debt_lvl_zscore_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_014_debt_lvl_zscore_252d"""
    base = debt
    return _zscore_rolling(base, 252)

def solv_015_debt_lvl_rank_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_015_debt_lvl_rank_252d"""
    base = debt
    return _rank_pct(base, 252)

def solv_016_debt_assets_lvl_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_016_debt_assets_lvl_5d"""
    base = _safe_div(debt, assets)
    return _rolling_mean(base, 5)

def solv_017_debt_assets_zscore_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_017_debt_assets_zscore_5d"""
    base = _safe_div(debt, assets)
    return _zscore_rolling(base, 5)

def solv_018_debt_assets_rank_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_018_debt_assets_rank_5d"""
    base = _safe_div(debt, assets)
    return _rank_pct(base, 5)

def solv_019_debt_assets_lvl_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_019_debt_assets_lvl_21d"""
    base = _safe_div(debt, assets)
    return _rolling_mean(base, 21)

def solv_020_debt_assets_zscore_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_020_debt_assets_zscore_21d"""
    base = _safe_div(debt, assets)
    return _zscore_rolling(base, 21)

def solv_021_debt_assets_rank_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_021_debt_assets_rank_21d"""
    base = _safe_div(debt, assets)
    return _rank_pct(base, 21)

def solv_022_debt_assets_lvl_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_022_debt_assets_lvl_63d"""
    base = _safe_div(debt, assets)
    return _rolling_mean(base, 63)

def solv_023_debt_assets_zscore_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_023_debt_assets_zscore_63d"""
    base = _safe_div(debt, assets)
    return _zscore_rolling(base, 63)

def solv_024_debt_assets_rank_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_024_debt_assets_rank_63d"""
    base = _safe_div(debt, assets)
    return _rank_pct(base, 63)

def solv_025_debt_assets_lvl_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_025_debt_assets_lvl_126d"""
    base = _safe_div(debt, assets)
    return _rolling_mean(base, 126)

def solv_026_debt_assets_zscore_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_026_debt_assets_zscore_126d"""
    base = _safe_div(debt, assets)
    return _zscore_rolling(base, 126)

def solv_027_debt_assets_rank_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_027_debt_assets_rank_126d"""
    base = _safe_div(debt, assets)
    return _rank_pct(base, 126)

def solv_028_debt_assets_lvl_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_028_debt_assets_lvl_252d"""
    base = _safe_div(debt, assets)
    return _rolling_mean(base, 252)

def solv_029_debt_assets_zscore_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_029_debt_assets_zscore_252d"""
    base = _safe_div(debt, assets)
    return _zscore_rolling(base, 252)

def solv_030_debt_assets_rank_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_030_debt_assets_rank_252d"""
    base = _safe_div(debt, assets)
    return _rank_pct(base, 252)

def solv_031_int_cov_lvl_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_031_int_cov_lvl_5d"""
    base = _safe_div(opinc, debt)
    return _rolling_mean(base, 5)

def solv_032_int_cov_zscore_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_032_int_cov_zscore_5d"""
    base = _safe_div(opinc, debt)
    return _zscore_rolling(base, 5)

def solv_033_int_cov_rank_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_033_int_cov_rank_5d"""
    base = _safe_div(opinc, debt)
    return _rank_pct(base, 5)

def solv_034_int_cov_lvl_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_034_int_cov_lvl_21d"""
    base = _safe_div(opinc, debt)
    return _rolling_mean(base, 21)

def solv_035_int_cov_zscore_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_035_int_cov_zscore_21d"""
    base = _safe_div(opinc, debt)
    return _zscore_rolling(base, 21)

def solv_036_int_cov_rank_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_036_int_cov_rank_21d"""
    base = _safe_div(opinc, debt)
    return _rank_pct(base, 21)

def solv_037_int_cov_lvl_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_037_int_cov_lvl_63d"""
    base = _safe_div(opinc, debt)
    return _rolling_mean(base, 63)

def solv_038_int_cov_zscore_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_038_int_cov_zscore_63d"""
    base = _safe_div(opinc, debt)
    return _zscore_rolling(base, 63)

def solv_039_int_cov_rank_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_039_int_cov_rank_63d"""
    base = _safe_div(opinc, debt)
    return _rank_pct(base, 63)

def solv_040_int_cov_lvl_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_040_int_cov_lvl_126d"""
    base = _safe_div(opinc, debt)
    return _rolling_mean(base, 126)

def solv_041_int_cov_zscore_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_041_int_cov_zscore_126d"""
    base = _safe_div(opinc, debt)
    return _zscore_rolling(base, 126)

def solv_042_int_cov_rank_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_042_int_cov_rank_126d"""
    base = _safe_div(opinc, debt)
    return _rank_pct(base, 126)

def solv_043_int_cov_lvl_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_043_int_cov_lvl_252d"""
    base = _safe_div(opinc, debt)
    return _rolling_mean(base, 252)

def solv_044_int_cov_zscore_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_044_int_cov_zscore_252d"""
    base = _safe_div(opinc, debt)
    return _zscore_rolling(base, 252)

def solv_045_int_cov_rank_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_045_int_cov_rank_252d"""
    base = _safe_div(opinc, debt)
    return _rank_pct(base, 252)

def solv_046_debt_eq_lvl_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_046_debt_eq_lvl_5d"""
    base = _safe_div(debt, equity)
    return _rolling_mean(base, 5)

def solv_047_debt_eq_zscore_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_047_debt_eq_zscore_5d"""
    base = _safe_div(debt, equity)
    return _zscore_rolling(base, 5)

def solv_048_debt_eq_rank_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_048_debt_eq_rank_5d"""
    base = _safe_div(debt, equity)
    return _rank_pct(base, 5)

def solv_049_debt_eq_lvl_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_049_debt_eq_lvl_21d"""
    base = _safe_div(debt, equity)
    return _rolling_mean(base, 21)

def solv_050_debt_eq_zscore_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_050_debt_eq_zscore_21d"""
    base = _safe_div(debt, equity)
    return _zscore_rolling(base, 21)

def solv_051_debt_eq_rank_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_051_debt_eq_rank_21d"""
    base = _safe_div(debt, equity)
    return _rank_pct(base, 21)

def solv_052_debt_eq_lvl_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_052_debt_eq_lvl_63d"""
    base = _safe_div(debt, equity)
    return _rolling_mean(base, 63)

def solv_053_debt_eq_zscore_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_053_debt_eq_zscore_63d"""
    base = _safe_div(debt, equity)
    return _zscore_rolling(base, 63)

def solv_054_debt_eq_rank_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_054_debt_eq_rank_63d"""
    base = _safe_div(debt, equity)
    return _rank_pct(base, 63)

def solv_055_debt_eq_lvl_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_055_debt_eq_lvl_126d"""
    base = _safe_div(debt, equity)
    return _rolling_mean(base, 126)

def solv_056_debt_eq_zscore_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_056_debt_eq_zscore_126d"""
    base = _safe_div(debt, equity)
    return _zscore_rolling(base, 126)

def solv_057_debt_eq_rank_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_057_debt_eq_rank_126d"""
    base = _safe_div(debt, equity)
    return _rank_pct(base, 126)

def solv_058_debt_eq_lvl_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_058_debt_eq_lvl_252d"""
    base = _safe_div(debt, equity)
    return _rolling_mean(base, 252)

def solv_059_debt_eq_zscore_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_059_debt_eq_zscore_252d"""
    base = _safe_div(debt, equity)
    return _zscore_rolling(base, 252)

def solv_060_debt_eq_rank_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_060_debt_eq_rank_252d"""
    base = _safe_div(debt, equity)
    return _rank_pct(base, 252)

def solv_061_altman_wc_ta_lvl_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_061_altman_wc_ta_lvl_5d"""
    base = _safe_div(assets - liabs, assets)
    return _rolling_mean(base, 5)

def solv_062_altman_wc_ta_zscore_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_062_altman_wc_ta_zscore_5d"""
    base = _safe_div(assets - liabs, assets)
    return _zscore_rolling(base, 5)

def solv_063_altman_wc_ta_rank_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_063_altman_wc_ta_rank_5d"""
    base = _safe_div(assets - liabs, assets)
    return _rank_pct(base, 5)

def solv_064_altman_wc_ta_lvl_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_064_altman_wc_ta_lvl_21d"""
    base = _safe_div(assets - liabs, assets)
    return _rolling_mean(base, 21)

def solv_065_altman_wc_ta_zscore_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_065_altman_wc_ta_zscore_21d"""
    base = _safe_div(assets - liabs, assets)
    return _zscore_rolling(base, 21)

def solv_066_altman_wc_ta_rank_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_066_altman_wc_ta_rank_21d"""
    base = _safe_div(assets - liabs, assets)
    return _rank_pct(base, 21)

def solv_067_altman_wc_ta_lvl_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_067_altman_wc_ta_lvl_63d"""
    base = _safe_div(assets - liabs, assets)
    return _rolling_mean(base, 63)

def solv_068_altman_wc_ta_zscore_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_068_altman_wc_ta_zscore_63d"""
    base = _safe_div(assets - liabs, assets)
    return _zscore_rolling(base, 63)

def solv_069_altman_wc_ta_rank_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_069_altman_wc_ta_rank_63d"""
    base = _safe_div(assets - liabs, assets)
    return _rank_pct(base, 63)

def solv_070_altman_wc_ta_lvl_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_070_altman_wc_ta_lvl_126d"""
    base = _safe_div(assets - liabs, assets)
    return _rolling_mean(base, 126)

def solv_071_altman_wc_ta_zscore_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_071_altman_wc_ta_zscore_126d"""
    base = _safe_div(assets - liabs, assets)
    return _zscore_rolling(base, 126)

def solv_072_altman_wc_ta_rank_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_072_altman_wc_ta_rank_126d"""
    base = _safe_div(assets - liabs, assets)
    return _rank_pct(base, 126)

def solv_073_altman_wc_ta_lvl_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_073_altman_wc_ta_lvl_252d"""
    base = _safe_div(assets - liabs, assets)
    return _rolling_mean(base, 252)

def solv_074_altman_wc_ta_zscore_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_074_altman_wc_ta_zscore_252d"""
    base = _safe_div(assets - liabs, assets)
    return _zscore_rolling(base, 252)

def solv_075_altman_wc_ta_rank_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_075_altman_wc_ta_rank_252d"""
    base = _safe_div(assets - liabs, assets)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V40_REGISTRY = {
    "solv_001_debt_lvl_lvl_5d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_001_debt_lvl_lvl_5d},
    "solv_002_debt_lvl_zscore_5d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_002_debt_lvl_zscore_5d},
    "solv_003_debt_lvl_rank_5d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_003_debt_lvl_rank_5d},
    "solv_004_debt_lvl_lvl_21d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_004_debt_lvl_lvl_21d},
    "solv_005_debt_lvl_zscore_21d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_005_debt_lvl_zscore_21d},
    "solv_006_debt_lvl_rank_21d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_006_debt_lvl_rank_21d},
    "solv_007_debt_lvl_lvl_63d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_007_debt_lvl_lvl_63d},
    "solv_008_debt_lvl_zscore_63d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_008_debt_lvl_zscore_63d},
    "solv_009_debt_lvl_rank_63d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_009_debt_lvl_rank_63d},
    "solv_010_debt_lvl_lvl_126d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_010_debt_lvl_lvl_126d},
    "solv_011_debt_lvl_zscore_126d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_011_debt_lvl_zscore_126d},
    "solv_012_debt_lvl_rank_126d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_012_debt_lvl_rank_126d},
    "solv_013_debt_lvl_lvl_252d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_013_debt_lvl_lvl_252d},
    "solv_014_debt_lvl_zscore_252d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_014_debt_lvl_zscore_252d},
    "solv_015_debt_lvl_rank_252d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_015_debt_lvl_rank_252d},
    "solv_016_debt_assets_lvl_5d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_016_debt_assets_lvl_5d},
    "solv_017_debt_assets_zscore_5d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_017_debt_assets_zscore_5d},
    "solv_018_debt_assets_rank_5d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_018_debt_assets_rank_5d},
    "solv_019_debt_assets_lvl_21d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_019_debt_assets_lvl_21d},
    "solv_020_debt_assets_zscore_21d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_020_debt_assets_zscore_21d},
    "solv_021_debt_assets_rank_21d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_021_debt_assets_rank_21d},
    "solv_022_debt_assets_lvl_63d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_022_debt_assets_lvl_63d},
    "solv_023_debt_assets_zscore_63d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_023_debt_assets_zscore_63d},
    "solv_024_debt_assets_rank_63d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_024_debt_assets_rank_63d},
    "solv_025_debt_assets_lvl_126d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_025_debt_assets_lvl_126d},
    "solv_026_debt_assets_zscore_126d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_026_debt_assets_zscore_126d},
    "solv_027_debt_assets_rank_126d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_027_debt_assets_rank_126d},
    "solv_028_debt_assets_lvl_252d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_028_debt_assets_lvl_252d},
    "solv_029_debt_assets_zscore_252d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_029_debt_assets_zscore_252d},
    "solv_030_debt_assets_rank_252d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_030_debt_assets_rank_252d},
    "solv_031_int_cov_lvl_5d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_031_int_cov_lvl_5d},
    "solv_032_int_cov_zscore_5d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_032_int_cov_zscore_5d},
    "solv_033_int_cov_rank_5d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_033_int_cov_rank_5d},
    "solv_034_int_cov_lvl_21d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_034_int_cov_lvl_21d},
    "solv_035_int_cov_zscore_21d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_035_int_cov_zscore_21d},
    "solv_036_int_cov_rank_21d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_036_int_cov_rank_21d},
    "solv_037_int_cov_lvl_63d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_037_int_cov_lvl_63d},
    "solv_038_int_cov_zscore_63d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_038_int_cov_zscore_63d},
    "solv_039_int_cov_rank_63d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_039_int_cov_rank_63d},
    "solv_040_int_cov_lvl_126d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_040_int_cov_lvl_126d},
    "solv_041_int_cov_zscore_126d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_041_int_cov_zscore_126d},
    "solv_042_int_cov_rank_126d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_042_int_cov_rank_126d},
    "solv_043_int_cov_lvl_252d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_043_int_cov_lvl_252d},
    "solv_044_int_cov_zscore_252d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_044_int_cov_zscore_252d},
    "solv_045_int_cov_rank_252d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_045_int_cov_rank_252d},
    "solv_046_debt_eq_lvl_5d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_046_debt_eq_lvl_5d},
    "solv_047_debt_eq_zscore_5d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_047_debt_eq_zscore_5d},
    "solv_048_debt_eq_rank_5d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_048_debt_eq_rank_5d},
    "solv_049_debt_eq_lvl_21d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_049_debt_eq_lvl_21d},
    "solv_050_debt_eq_zscore_21d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_050_debt_eq_zscore_21d},
    "solv_051_debt_eq_rank_21d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_051_debt_eq_rank_21d},
    "solv_052_debt_eq_lvl_63d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_052_debt_eq_lvl_63d},
    "solv_053_debt_eq_zscore_63d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_053_debt_eq_zscore_63d},
    "solv_054_debt_eq_rank_63d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_054_debt_eq_rank_63d},
    "solv_055_debt_eq_lvl_126d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_055_debt_eq_lvl_126d},
    "solv_056_debt_eq_zscore_126d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_056_debt_eq_zscore_126d},
    "solv_057_debt_eq_rank_126d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_057_debt_eq_rank_126d},
    "solv_058_debt_eq_lvl_252d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_058_debt_eq_lvl_252d},
    "solv_059_debt_eq_zscore_252d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_059_debt_eq_zscore_252d},
    "solv_060_debt_eq_rank_252d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_060_debt_eq_rank_252d},
    "solv_061_altman_wc_ta_lvl_5d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_061_altman_wc_ta_lvl_5d},
    "solv_062_altman_wc_ta_zscore_5d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_062_altman_wc_ta_zscore_5d},
    "solv_063_altman_wc_ta_rank_5d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_063_altman_wc_ta_rank_5d},
    "solv_064_altman_wc_ta_lvl_21d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_064_altman_wc_ta_lvl_21d},
    "solv_065_altman_wc_ta_zscore_21d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_065_altman_wc_ta_zscore_21d},
    "solv_066_altman_wc_ta_rank_21d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_066_altman_wc_ta_rank_21d},
    "solv_067_altman_wc_ta_lvl_63d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_067_altman_wc_ta_lvl_63d},
    "solv_068_altman_wc_ta_zscore_63d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_068_altman_wc_ta_zscore_63d},
    "solv_069_altman_wc_ta_rank_63d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_069_altman_wc_ta_rank_63d},
    "solv_070_altman_wc_ta_lvl_126d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_070_altman_wc_ta_lvl_126d},
    "solv_071_altman_wc_ta_zscore_126d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_071_altman_wc_ta_zscore_126d},
    "solv_072_altman_wc_ta_rank_126d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_072_altman_wc_ta_rank_126d},
    "solv_073_altman_wc_ta_lvl_252d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_073_altman_wc_ta_lvl_252d},
    "solv_074_altman_wc_ta_zscore_252d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_074_altman_wc_ta_zscore_252d},
    "solv_075_altman_wc_ta_rank_252d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_075_altman_wc_ta_rank_252d},
}
