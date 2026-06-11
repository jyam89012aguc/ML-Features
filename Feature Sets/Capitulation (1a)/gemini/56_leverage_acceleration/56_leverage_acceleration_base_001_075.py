"""
56_leverage_acceleration — Base Features 001-075
Domain: leverage_acceleration
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

def leva_001_debt_equity_lvl_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_001_debt_equity_lvl_5d"""
    base = _safe_div(debt, equity)
    return _rolling_mean(base, 5)

def leva_002_debt_equity_zscore_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_002_debt_equity_zscore_5d"""
    base = _safe_div(debt, equity)
    return _zscore_rolling(base, 5)

def leva_003_debt_equity_rank_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_003_debt_equity_rank_5d"""
    base = _safe_div(debt, equity)
    return _rank_pct(base, 5)

def leva_004_debt_equity_lvl_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_004_debt_equity_lvl_21d"""
    base = _safe_div(debt, equity)
    return _rolling_mean(base, 21)

def leva_005_debt_equity_zscore_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_005_debt_equity_zscore_21d"""
    base = _safe_div(debt, equity)
    return _zscore_rolling(base, 21)

def leva_006_debt_equity_rank_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_006_debt_equity_rank_21d"""
    base = _safe_div(debt, equity)
    return _rank_pct(base, 21)

def leva_007_debt_equity_lvl_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_007_debt_equity_lvl_63d"""
    base = _safe_div(debt, equity)
    return _rolling_mean(base, 63)

def leva_008_debt_equity_zscore_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_008_debt_equity_zscore_63d"""
    base = _safe_div(debt, equity)
    return _zscore_rolling(base, 63)

def leva_009_debt_equity_rank_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_009_debt_equity_rank_63d"""
    base = _safe_div(debt, equity)
    return _rank_pct(base, 63)

def leva_010_debt_equity_lvl_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_010_debt_equity_lvl_126d"""
    base = _safe_div(debt, equity)
    return _rolling_mean(base, 126)

def leva_011_debt_equity_zscore_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_011_debt_equity_zscore_126d"""
    base = _safe_div(debt, equity)
    return _zscore_rolling(base, 126)

def leva_012_debt_equity_rank_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_012_debt_equity_rank_126d"""
    base = _safe_div(debt, equity)
    return _rank_pct(base, 126)

def leva_013_debt_equity_lvl_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_013_debt_equity_lvl_252d"""
    base = _safe_div(debt, equity)
    return _rolling_mean(base, 252)

def leva_014_debt_equity_zscore_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_014_debt_equity_zscore_252d"""
    base = _safe_div(debt, equity)
    return _zscore_rolling(base, 252)

def leva_015_debt_equity_rank_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_015_debt_equity_rank_252d"""
    base = _safe_div(debt, equity)
    return _rank_pct(base, 252)

def leva_016_debt_assets_lvl_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_016_debt_assets_lvl_5d"""
    base = _safe_div(debt, assets)
    return _rolling_mean(base, 5)

def leva_017_debt_assets_zscore_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_017_debt_assets_zscore_5d"""
    base = _safe_div(debt, assets)
    return _zscore_rolling(base, 5)

def leva_018_debt_assets_rank_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_018_debt_assets_rank_5d"""
    base = _safe_div(debt, assets)
    return _rank_pct(base, 5)

def leva_019_debt_assets_lvl_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_019_debt_assets_lvl_21d"""
    base = _safe_div(debt, assets)
    return _rolling_mean(base, 21)

def leva_020_debt_assets_zscore_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_020_debt_assets_zscore_21d"""
    base = _safe_div(debt, assets)
    return _zscore_rolling(base, 21)

def leva_021_debt_assets_rank_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_021_debt_assets_rank_21d"""
    base = _safe_div(debt, assets)
    return _rank_pct(base, 21)

def leva_022_debt_assets_lvl_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_022_debt_assets_lvl_63d"""
    base = _safe_div(debt, assets)
    return _rolling_mean(base, 63)

def leva_023_debt_assets_zscore_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_023_debt_assets_zscore_63d"""
    base = _safe_div(debt, assets)
    return _zscore_rolling(base, 63)

def leva_024_debt_assets_rank_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_024_debt_assets_rank_63d"""
    base = _safe_div(debt, assets)
    return _rank_pct(base, 63)

def leva_025_debt_assets_lvl_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_025_debt_assets_lvl_126d"""
    base = _safe_div(debt, assets)
    return _rolling_mean(base, 126)

def leva_026_debt_assets_zscore_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_026_debt_assets_zscore_126d"""
    base = _safe_div(debt, assets)
    return _zscore_rolling(base, 126)

def leva_027_debt_assets_rank_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_027_debt_assets_rank_126d"""
    base = _safe_div(debt, assets)
    return _rank_pct(base, 126)

def leva_028_debt_assets_lvl_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_028_debt_assets_lvl_252d"""
    base = _safe_div(debt, assets)
    return _rolling_mean(base, 252)

def leva_029_debt_assets_zscore_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_029_debt_assets_zscore_252d"""
    base = _safe_div(debt, assets)
    return _zscore_rolling(base, 252)

def leva_030_debt_assets_rank_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_030_debt_assets_rank_252d"""
    base = _safe_div(debt, assets)
    return _rank_pct(base, 252)

def leva_031_leverage_ratio_lvl_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_031_leverage_ratio_lvl_5d"""
    base = _safe_div(assets, equity)
    return _rolling_mean(base, 5)

def leva_032_leverage_ratio_zscore_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_032_leverage_ratio_zscore_5d"""
    base = _safe_div(assets, equity)
    return _zscore_rolling(base, 5)

def leva_033_leverage_ratio_rank_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_033_leverage_ratio_rank_5d"""
    base = _safe_div(assets, equity)
    return _rank_pct(base, 5)

def leva_034_leverage_ratio_lvl_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_034_leverage_ratio_lvl_21d"""
    base = _safe_div(assets, equity)
    return _rolling_mean(base, 21)

def leva_035_leverage_ratio_zscore_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_035_leverage_ratio_zscore_21d"""
    base = _safe_div(assets, equity)
    return _zscore_rolling(base, 21)

def leva_036_leverage_ratio_rank_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_036_leverage_ratio_rank_21d"""
    base = _safe_div(assets, equity)
    return _rank_pct(base, 21)

def leva_037_leverage_ratio_lvl_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_037_leverage_ratio_lvl_63d"""
    base = _safe_div(assets, equity)
    return _rolling_mean(base, 63)

def leva_038_leverage_ratio_zscore_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_038_leverage_ratio_zscore_63d"""
    base = _safe_div(assets, equity)
    return _zscore_rolling(base, 63)

def leva_039_leverage_ratio_rank_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_039_leverage_ratio_rank_63d"""
    base = _safe_div(assets, equity)
    return _rank_pct(base, 63)

def leva_040_leverage_ratio_lvl_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_040_leverage_ratio_lvl_126d"""
    base = _safe_div(assets, equity)
    return _rolling_mean(base, 126)

def leva_041_leverage_ratio_zscore_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_041_leverage_ratio_zscore_126d"""
    base = _safe_div(assets, equity)
    return _zscore_rolling(base, 126)

def leva_042_leverage_ratio_rank_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_042_leverage_ratio_rank_126d"""
    base = _safe_div(assets, equity)
    return _rank_pct(base, 126)

def leva_043_leverage_ratio_lvl_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_043_leverage_ratio_lvl_252d"""
    base = _safe_div(assets, equity)
    return _rolling_mean(base, 252)

def leva_044_leverage_ratio_zscore_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_044_leverage_ratio_zscore_252d"""
    base = _safe_div(assets, equity)
    return _zscore_rolling(base, 252)

def leva_045_leverage_ratio_rank_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_045_leverage_ratio_rank_252d"""
    base = _safe_div(assets, equity)
    return _rank_pct(base, 252)

def leva_046_debt_ebitda_lvl_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_046_debt_ebitda_lvl_5d"""
    base = _safe_div(debt, ebitda)
    return _rolling_mean(base, 5)

def leva_047_debt_ebitda_zscore_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_047_debt_ebitda_zscore_5d"""
    base = _safe_div(debt, ebitda)
    return _zscore_rolling(base, 5)

def leva_048_debt_ebitda_rank_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_048_debt_ebitda_rank_5d"""
    base = _safe_div(debt, ebitda)
    return _rank_pct(base, 5)

def leva_049_debt_ebitda_lvl_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_049_debt_ebitda_lvl_21d"""
    base = _safe_div(debt, ebitda)
    return _rolling_mean(base, 21)

def leva_050_debt_ebitda_zscore_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_050_debt_ebitda_zscore_21d"""
    base = _safe_div(debt, ebitda)
    return _zscore_rolling(base, 21)

def leva_051_debt_ebitda_rank_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_051_debt_ebitda_rank_21d"""
    base = _safe_div(debt, ebitda)
    return _rank_pct(base, 21)

def leva_052_debt_ebitda_lvl_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_052_debt_ebitda_lvl_63d"""
    base = _safe_div(debt, ebitda)
    return _rolling_mean(base, 63)

def leva_053_debt_ebitda_zscore_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_053_debt_ebitda_zscore_63d"""
    base = _safe_div(debt, ebitda)
    return _zscore_rolling(base, 63)

def leva_054_debt_ebitda_rank_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_054_debt_ebitda_rank_63d"""
    base = _safe_div(debt, ebitda)
    return _rank_pct(base, 63)

def leva_055_debt_ebitda_lvl_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_055_debt_ebitda_lvl_126d"""
    base = _safe_div(debt, ebitda)
    return _rolling_mean(base, 126)

def leva_056_debt_ebitda_zscore_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_056_debt_ebitda_zscore_126d"""
    base = _safe_div(debt, ebitda)
    return _zscore_rolling(base, 126)

def leva_057_debt_ebitda_rank_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_057_debt_ebitda_rank_126d"""
    base = _safe_div(debt, ebitda)
    return _rank_pct(base, 126)

def leva_058_debt_ebitda_lvl_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_058_debt_ebitda_lvl_252d"""
    base = _safe_div(debt, ebitda)
    return _rolling_mean(base, 252)

def leva_059_debt_ebitda_zscore_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_059_debt_ebitda_zscore_252d"""
    base = _safe_div(debt, ebitda)
    return _zscore_rolling(base, 252)

def leva_060_debt_ebitda_rank_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_060_debt_ebitda_rank_252d"""
    base = _safe_div(debt, ebitda)
    return _rank_pct(base, 252)

def leva_061_debt_chg_yoy_lvl_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_061_debt_chg_yoy_lvl_5d"""
    base = debt.pct_change(252)
    return _rolling_mean(base, 5)

def leva_062_debt_chg_yoy_zscore_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_062_debt_chg_yoy_zscore_5d"""
    base = debt.pct_change(252)
    return _zscore_rolling(base, 5)

def leva_063_debt_chg_yoy_rank_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_063_debt_chg_yoy_rank_5d"""
    base = debt.pct_change(252)
    return _rank_pct(base, 5)

def leva_064_debt_chg_yoy_lvl_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_064_debt_chg_yoy_lvl_21d"""
    base = debt.pct_change(252)
    return _rolling_mean(base, 21)

def leva_065_debt_chg_yoy_zscore_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_065_debt_chg_yoy_zscore_21d"""
    base = debt.pct_change(252)
    return _zscore_rolling(base, 21)

def leva_066_debt_chg_yoy_rank_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_066_debt_chg_yoy_rank_21d"""
    base = debt.pct_change(252)
    return _rank_pct(base, 21)

def leva_067_debt_chg_yoy_lvl_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_067_debt_chg_yoy_lvl_63d"""
    base = debt.pct_change(252)
    return _rolling_mean(base, 63)

def leva_068_debt_chg_yoy_zscore_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_068_debt_chg_yoy_zscore_63d"""
    base = debt.pct_change(252)
    return _zscore_rolling(base, 63)

def leva_069_debt_chg_yoy_rank_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_069_debt_chg_yoy_rank_63d"""
    base = debt.pct_change(252)
    return _rank_pct(base, 63)

def leva_070_debt_chg_yoy_lvl_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_070_debt_chg_yoy_lvl_126d"""
    base = debt.pct_change(252)
    return _rolling_mean(base, 126)

def leva_071_debt_chg_yoy_zscore_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_071_debt_chg_yoy_zscore_126d"""
    base = debt.pct_change(252)
    return _zscore_rolling(base, 126)

def leva_072_debt_chg_yoy_rank_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_072_debt_chg_yoy_rank_126d"""
    base = debt.pct_change(252)
    return _rank_pct(base, 126)

def leva_073_debt_chg_yoy_lvl_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_073_debt_chg_yoy_lvl_252d"""
    base = debt.pct_change(252)
    return _rolling_mean(base, 252)

def leva_074_debt_chg_yoy_zscore_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_074_debt_chg_yoy_zscore_252d"""
    base = debt.pct_change(252)
    return _zscore_rolling(base, 252)

def leva_075_debt_chg_yoy_rank_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_075_debt_chg_yoy_rank_252d"""
    base = debt.pct_change(252)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V56_REGISTRY = {
    "leva_001_debt_equity_lvl_5d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_001_debt_equity_lvl_5d},
    "leva_002_debt_equity_zscore_5d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_002_debt_equity_zscore_5d},
    "leva_003_debt_equity_rank_5d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_003_debt_equity_rank_5d},
    "leva_004_debt_equity_lvl_21d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_004_debt_equity_lvl_21d},
    "leva_005_debt_equity_zscore_21d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_005_debt_equity_zscore_21d},
    "leva_006_debt_equity_rank_21d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_006_debt_equity_rank_21d},
    "leva_007_debt_equity_lvl_63d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_007_debt_equity_lvl_63d},
    "leva_008_debt_equity_zscore_63d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_008_debt_equity_zscore_63d},
    "leva_009_debt_equity_rank_63d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_009_debt_equity_rank_63d},
    "leva_010_debt_equity_lvl_126d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_010_debt_equity_lvl_126d},
    "leva_011_debt_equity_zscore_126d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_011_debt_equity_zscore_126d},
    "leva_012_debt_equity_rank_126d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_012_debt_equity_rank_126d},
    "leva_013_debt_equity_lvl_252d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_013_debt_equity_lvl_252d},
    "leva_014_debt_equity_zscore_252d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_014_debt_equity_zscore_252d},
    "leva_015_debt_equity_rank_252d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_015_debt_equity_rank_252d},
    "leva_016_debt_assets_lvl_5d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_016_debt_assets_lvl_5d},
    "leva_017_debt_assets_zscore_5d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_017_debt_assets_zscore_5d},
    "leva_018_debt_assets_rank_5d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_018_debt_assets_rank_5d},
    "leva_019_debt_assets_lvl_21d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_019_debt_assets_lvl_21d},
    "leva_020_debt_assets_zscore_21d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_020_debt_assets_zscore_21d},
    "leva_021_debt_assets_rank_21d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_021_debt_assets_rank_21d},
    "leva_022_debt_assets_lvl_63d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_022_debt_assets_lvl_63d},
    "leva_023_debt_assets_zscore_63d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_023_debt_assets_zscore_63d},
    "leva_024_debt_assets_rank_63d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_024_debt_assets_rank_63d},
    "leva_025_debt_assets_lvl_126d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_025_debt_assets_lvl_126d},
    "leva_026_debt_assets_zscore_126d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_026_debt_assets_zscore_126d},
    "leva_027_debt_assets_rank_126d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_027_debt_assets_rank_126d},
    "leva_028_debt_assets_lvl_252d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_028_debt_assets_lvl_252d},
    "leva_029_debt_assets_zscore_252d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_029_debt_assets_zscore_252d},
    "leva_030_debt_assets_rank_252d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_030_debt_assets_rank_252d},
    "leva_031_leverage_ratio_lvl_5d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_031_leverage_ratio_lvl_5d},
    "leva_032_leverage_ratio_zscore_5d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_032_leverage_ratio_zscore_5d},
    "leva_033_leverage_ratio_rank_5d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_033_leverage_ratio_rank_5d},
    "leva_034_leverage_ratio_lvl_21d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_034_leverage_ratio_lvl_21d},
    "leva_035_leverage_ratio_zscore_21d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_035_leverage_ratio_zscore_21d},
    "leva_036_leverage_ratio_rank_21d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_036_leverage_ratio_rank_21d},
    "leva_037_leverage_ratio_lvl_63d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_037_leverage_ratio_lvl_63d},
    "leva_038_leverage_ratio_zscore_63d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_038_leverage_ratio_zscore_63d},
    "leva_039_leverage_ratio_rank_63d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_039_leverage_ratio_rank_63d},
    "leva_040_leverage_ratio_lvl_126d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_040_leverage_ratio_lvl_126d},
    "leva_041_leverage_ratio_zscore_126d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_041_leverage_ratio_zscore_126d},
    "leva_042_leverage_ratio_rank_126d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_042_leverage_ratio_rank_126d},
    "leva_043_leverage_ratio_lvl_252d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_043_leverage_ratio_lvl_252d},
    "leva_044_leverage_ratio_zscore_252d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_044_leverage_ratio_zscore_252d},
    "leva_045_leverage_ratio_rank_252d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_045_leverage_ratio_rank_252d},
    "leva_046_debt_ebitda_lvl_5d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_046_debt_ebitda_lvl_5d},
    "leva_047_debt_ebitda_zscore_5d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_047_debt_ebitda_zscore_5d},
    "leva_048_debt_ebitda_rank_5d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_048_debt_ebitda_rank_5d},
    "leva_049_debt_ebitda_lvl_21d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_049_debt_ebitda_lvl_21d},
    "leva_050_debt_ebitda_zscore_21d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_050_debt_ebitda_zscore_21d},
    "leva_051_debt_ebitda_rank_21d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_051_debt_ebitda_rank_21d},
    "leva_052_debt_ebitda_lvl_63d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_052_debt_ebitda_lvl_63d},
    "leva_053_debt_ebitda_zscore_63d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_053_debt_ebitda_zscore_63d},
    "leva_054_debt_ebitda_rank_63d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_054_debt_ebitda_rank_63d},
    "leva_055_debt_ebitda_lvl_126d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_055_debt_ebitda_lvl_126d},
    "leva_056_debt_ebitda_zscore_126d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_056_debt_ebitda_zscore_126d},
    "leva_057_debt_ebitda_rank_126d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_057_debt_ebitda_rank_126d},
    "leva_058_debt_ebitda_lvl_252d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_058_debt_ebitda_lvl_252d},
    "leva_059_debt_ebitda_zscore_252d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_059_debt_ebitda_zscore_252d},
    "leva_060_debt_ebitda_rank_252d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_060_debt_ebitda_rank_252d},
    "leva_061_debt_chg_yoy_lvl_5d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_061_debt_chg_yoy_lvl_5d},
    "leva_062_debt_chg_yoy_zscore_5d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_062_debt_chg_yoy_zscore_5d},
    "leva_063_debt_chg_yoy_rank_5d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_063_debt_chg_yoy_rank_5d},
    "leva_064_debt_chg_yoy_lvl_21d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_064_debt_chg_yoy_lvl_21d},
    "leva_065_debt_chg_yoy_zscore_21d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_065_debt_chg_yoy_zscore_21d},
    "leva_066_debt_chg_yoy_rank_21d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_066_debt_chg_yoy_rank_21d},
    "leva_067_debt_chg_yoy_lvl_63d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_067_debt_chg_yoy_lvl_63d},
    "leva_068_debt_chg_yoy_zscore_63d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_068_debt_chg_yoy_zscore_63d},
    "leva_069_debt_chg_yoy_rank_63d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_069_debt_chg_yoy_rank_63d},
    "leva_070_debt_chg_yoy_lvl_126d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_070_debt_chg_yoy_lvl_126d},
    "leva_071_debt_chg_yoy_zscore_126d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_071_debt_chg_yoy_zscore_126d},
    "leva_072_debt_chg_yoy_rank_126d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_072_debt_chg_yoy_rank_126d},
    "leva_073_debt_chg_yoy_lvl_252d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_073_debt_chg_yoy_lvl_252d},
    "leva_074_debt_chg_yoy_zscore_252d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_074_debt_chg_yoy_zscore_252d},
    "leva_075_debt_chg_yoy_rank_252d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_075_debt_chg_yoy_rank_252d},
}
