"""
48_debt_trajectory — Base Features 001-075
Domain: debt_trajectory
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

def _pct_change(s: pd.Series, periods: int) -> pd.Series:
    return _safe_div(s - s.shift(periods), s.shift(periods).abs())

# ── Feature functions ────────────────────────────────────────────────────────

def debt_001_debt_to_assets_lvl_5d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_001_debt_to_assets_lvl_5d"""
    base = _safe_div(debt, assets)
    return _rolling_mean(base, 5)

def debt_002_debt_to_assets_zscore_5d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_002_debt_to_assets_zscore_5d"""
    base = _safe_div(debt, assets)
    return _zscore_rolling(base, 5)

def debt_003_debt_to_assets_rank_5d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_003_debt_to_assets_rank_5d"""
    base = _safe_div(debt, assets)
    return _rank_pct(base, 5)

def debt_004_debt_to_assets_lvl_21d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_004_debt_to_assets_lvl_21d"""
    base = _safe_div(debt, assets)
    return _rolling_mean(base, 21)

def debt_005_debt_to_assets_zscore_21d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_005_debt_to_assets_zscore_21d"""
    base = _safe_div(debt, assets)
    return _zscore_rolling(base, 21)

def debt_006_debt_to_assets_rank_21d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_006_debt_to_assets_rank_21d"""
    base = _safe_div(debt, assets)
    return _rank_pct(base, 21)

def debt_007_debt_to_assets_lvl_63d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_007_debt_to_assets_lvl_63d"""
    base = _safe_div(debt, assets)
    return _rolling_mean(base, 63)

def debt_008_debt_to_assets_zscore_63d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_008_debt_to_assets_zscore_63d"""
    base = _safe_div(debt, assets)
    return _zscore_rolling(base, 63)

def debt_009_debt_to_assets_rank_63d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_009_debt_to_assets_rank_63d"""
    base = _safe_div(debt, assets)
    return _rank_pct(base, 63)

def debt_010_debt_to_assets_lvl_126d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_010_debt_to_assets_lvl_126d"""
    base = _safe_div(debt, assets)
    return _rolling_mean(base, 126)

def debt_011_debt_to_assets_zscore_126d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_011_debt_to_assets_zscore_126d"""
    base = _safe_div(debt, assets)
    return _zscore_rolling(base, 126)

def debt_012_debt_to_assets_rank_126d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_012_debt_to_assets_rank_126d"""
    base = _safe_div(debt, assets)
    return _rank_pct(base, 126)

def debt_013_debt_to_assets_lvl_252d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_013_debt_to_assets_lvl_252d"""
    base = _safe_div(debt, assets)
    return _rolling_mean(base, 252)

def debt_014_debt_to_assets_zscore_252d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_014_debt_to_assets_zscore_252d"""
    base = _safe_div(debt, assets)
    return _zscore_rolling(base, 252)

def debt_015_debt_to_assets_rank_252d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_015_debt_to_assets_rank_252d"""
    base = _safe_div(debt, assets)
    return _rank_pct(base, 252)

def debt_016_debt_to_equity_lvl_5d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_016_debt_to_equity_lvl_5d"""
    base = _safe_div(debt, equity)
    return _rolling_mean(base, 5)

def debt_017_debt_to_equity_zscore_5d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_017_debt_to_equity_zscore_5d"""
    base = _safe_div(debt, equity)
    return _zscore_rolling(base, 5)

def debt_018_debt_to_equity_rank_5d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_018_debt_to_equity_rank_5d"""
    base = _safe_div(debt, equity)
    return _rank_pct(base, 5)

def debt_019_debt_to_equity_lvl_21d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_019_debt_to_equity_lvl_21d"""
    base = _safe_div(debt, equity)
    return _rolling_mean(base, 21)

def debt_020_debt_to_equity_zscore_21d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_020_debt_to_equity_zscore_21d"""
    base = _safe_div(debt, equity)
    return _zscore_rolling(base, 21)

def debt_021_debt_to_equity_rank_21d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_021_debt_to_equity_rank_21d"""
    base = _safe_div(debt, equity)
    return _rank_pct(base, 21)

def debt_022_debt_to_equity_lvl_63d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_022_debt_to_equity_lvl_63d"""
    base = _safe_div(debt, equity)
    return _rolling_mean(base, 63)

def debt_023_debt_to_equity_zscore_63d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_023_debt_to_equity_zscore_63d"""
    base = _safe_div(debt, equity)
    return _zscore_rolling(base, 63)

def debt_024_debt_to_equity_rank_63d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_024_debt_to_equity_rank_63d"""
    base = _safe_div(debt, equity)
    return _rank_pct(base, 63)

def debt_025_debt_to_equity_lvl_126d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_025_debt_to_equity_lvl_126d"""
    base = _safe_div(debt, equity)
    return _rolling_mean(base, 126)

def debt_026_debt_to_equity_zscore_126d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_026_debt_to_equity_zscore_126d"""
    base = _safe_div(debt, equity)
    return _zscore_rolling(base, 126)

def debt_027_debt_to_equity_rank_126d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_027_debt_to_equity_rank_126d"""
    base = _safe_div(debt, equity)
    return _rank_pct(base, 126)

def debt_028_debt_to_equity_lvl_252d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_028_debt_to_equity_lvl_252d"""
    base = _safe_div(debt, equity)
    return _rolling_mean(base, 252)

def debt_029_debt_to_equity_zscore_252d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_029_debt_to_equity_zscore_252d"""
    base = _safe_div(debt, equity)
    return _zscore_rolling(base, 252)

def debt_030_debt_to_equity_rank_252d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_030_debt_to_equity_rank_252d"""
    base = _safe_div(debt, equity)
    return _rank_pct(base, 252)

def debt_031_debt_to_ebitda_lvl_5d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_031_debt_to_ebitda_lvl_5d"""
    base = _safe_div(debt, ebitda)
    return _rolling_mean(base, 5)

def debt_032_debt_to_ebitda_zscore_5d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_032_debt_to_ebitda_zscore_5d"""
    base = _safe_div(debt, ebitda)
    return _zscore_rolling(base, 5)

def debt_033_debt_to_ebitda_rank_5d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_033_debt_to_ebitda_rank_5d"""
    base = _safe_div(debt, ebitda)
    return _rank_pct(base, 5)

def debt_034_debt_to_ebitda_lvl_21d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_034_debt_to_ebitda_lvl_21d"""
    base = _safe_div(debt, ebitda)
    return _rolling_mean(base, 21)

def debt_035_debt_to_ebitda_zscore_21d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_035_debt_to_ebitda_zscore_21d"""
    base = _safe_div(debt, ebitda)
    return _zscore_rolling(base, 21)

def debt_036_debt_to_ebitda_rank_21d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_036_debt_to_ebitda_rank_21d"""
    base = _safe_div(debt, ebitda)
    return _rank_pct(base, 21)

def debt_037_debt_to_ebitda_lvl_63d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_037_debt_to_ebitda_lvl_63d"""
    base = _safe_div(debt, ebitda)
    return _rolling_mean(base, 63)

def debt_038_debt_to_ebitda_zscore_63d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_038_debt_to_ebitda_zscore_63d"""
    base = _safe_div(debt, ebitda)
    return _zscore_rolling(base, 63)

def debt_039_debt_to_ebitda_rank_63d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_039_debt_to_ebitda_rank_63d"""
    base = _safe_div(debt, ebitda)
    return _rank_pct(base, 63)

def debt_040_debt_to_ebitda_lvl_126d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_040_debt_to_ebitda_lvl_126d"""
    base = _safe_div(debt, ebitda)
    return _rolling_mean(base, 126)

def debt_041_debt_to_ebitda_zscore_126d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_041_debt_to_ebitda_zscore_126d"""
    base = _safe_div(debt, ebitda)
    return _zscore_rolling(base, 126)

def debt_042_debt_to_ebitda_rank_126d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_042_debt_to_ebitda_rank_126d"""
    base = _safe_div(debt, ebitda)
    return _rank_pct(base, 126)

def debt_043_debt_to_ebitda_lvl_252d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_043_debt_to_ebitda_lvl_252d"""
    base = _safe_div(debt, ebitda)
    return _rolling_mean(base, 252)

def debt_044_debt_to_ebitda_zscore_252d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_044_debt_to_ebitda_zscore_252d"""
    base = _safe_div(debt, ebitda)
    return _zscore_rolling(base, 252)

def debt_045_debt_to_ebitda_rank_252d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_045_debt_to_ebitda_rank_252d"""
    base = _safe_div(debt, ebitda)
    return _rank_pct(base, 252)

def debt_046_debt_to_revenue_lvl_5d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_046_debt_to_revenue_lvl_5d"""
    base = _safe_div(debt, revenue)
    return _rolling_mean(base, 5)

def debt_047_debt_to_revenue_zscore_5d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_047_debt_to_revenue_zscore_5d"""
    base = _safe_div(debt, revenue)
    return _zscore_rolling(base, 5)

def debt_048_debt_to_revenue_rank_5d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_048_debt_to_revenue_rank_5d"""
    base = _safe_div(debt, revenue)
    return _rank_pct(base, 5)

def debt_049_debt_to_revenue_lvl_21d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_049_debt_to_revenue_lvl_21d"""
    base = _safe_div(debt, revenue)
    return _rolling_mean(base, 21)

def debt_050_debt_to_revenue_zscore_21d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_050_debt_to_revenue_zscore_21d"""
    base = _safe_div(debt, revenue)
    return _zscore_rolling(base, 21)

def debt_051_debt_to_revenue_rank_21d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_051_debt_to_revenue_rank_21d"""
    base = _safe_div(debt, revenue)
    return _rank_pct(base, 21)

def debt_052_debt_to_revenue_lvl_63d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_052_debt_to_revenue_lvl_63d"""
    base = _safe_div(debt, revenue)
    return _rolling_mean(base, 63)

def debt_053_debt_to_revenue_zscore_63d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_053_debt_to_revenue_zscore_63d"""
    base = _safe_div(debt, revenue)
    return _zscore_rolling(base, 63)

def debt_054_debt_to_revenue_rank_63d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_054_debt_to_revenue_rank_63d"""
    base = _safe_div(debt, revenue)
    return _rank_pct(base, 63)

def debt_055_debt_to_revenue_lvl_126d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_055_debt_to_revenue_lvl_126d"""
    base = _safe_div(debt, revenue)
    return _rolling_mean(base, 126)

def debt_056_debt_to_revenue_zscore_126d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_056_debt_to_revenue_zscore_126d"""
    base = _safe_div(debt, revenue)
    return _zscore_rolling(base, 126)

def debt_057_debt_to_revenue_rank_126d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_057_debt_to_revenue_rank_126d"""
    base = _safe_div(debt, revenue)
    return _rank_pct(base, 126)

def debt_058_debt_to_revenue_lvl_252d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_058_debt_to_revenue_lvl_252d"""
    base = _safe_div(debt, revenue)
    return _rolling_mean(base, 252)

def debt_059_debt_to_revenue_zscore_252d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_059_debt_to_revenue_zscore_252d"""
    base = _safe_div(debt, revenue)
    return _zscore_rolling(base, 252)

def debt_060_debt_to_revenue_rank_252d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_060_debt_to_revenue_rank_252d"""
    base = _safe_div(debt, revenue)
    return _rank_pct(base, 252)

def debt_061_leverage_lvl_5d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_061_leverage_lvl_5d"""
    base = _safe_div(assets, equity)
    return _rolling_mean(base, 5)

def debt_062_leverage_zscore_5d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_062_leverage_zscore_5d"""
    base = _safe_div(assets, equity)
    return _zscore_rolling(base, 5)

def debt_063_leverage_rank_5d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_063_leverage_rank_5d"""
    base = _safe_div(assets, equity)
    return _rank_pct(base, 5)

def debt_064_leverage_lvl_21d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_064_leverage_lvl_21d"""
    base = _safe_div(assets, equity)
    return _rolling_mean(base, 21)

def debt_065_leverage_zscore_21d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_065_leverage_zscore_21d"""
    base = _safe_div(assets, equity)
    return _zscore_rolling(base, 21)

def debt_066_leverage_rank_21d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_066_leverage_rank_21d"""
    base = _safe_div(assets, equity)
    return _rank_pct(base, 21)

def debt_067_leverage_lvl_63d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_067_leverage_lvl_63d"""
    base = _safe_div(assets, equity)
    return _rolling_mean(base, 63)

def debt_068_leverage_zscore_63d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_068_leverage_zscore_63d"""
    base = _safe_div(assets, equity)
    return _zscore_rolling(base, 63)

def debt_069_leverage_rank_63d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_069_leverage_rank_63d"""
    base = _safe_div(assets, equity)
    return _rank_pct(base, 63)

def debt_070_leverage_lvl_126d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_070_leverage_lvl_126d"""
    base = _safe_div(assets, equity)
    return _rolling_mean(base, 126)

def debt_071_leverage_zscore_126d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_071_leverage_zscore_126d"""
    base = _safe_div(assets, equity)
    return _zscore_rolling(base, 126)

def debt_072_leverage_rank_126d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_072_leverage_rank_126d"""
    base = _safe_div(assets, equity)
    return _rank_pct(base, 126)

def debt_073_leverage_lvl_252d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_073_leverage_lvl_252d"""
    base = _safe_div(assets, equity)
    return _rolling_mean(base, 252)

def debt_074_leverage_zscore_252d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_074_leverage_zscore_252d"""
    base = _safe_div(assets, equity)
    return _zscore_rolling(base, 252)

def debt_075_leverage_rank_252d(debt: pd.Series, assets: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """debt_075_leverage_rank_252d"""
    base = _safe_div(assets, equity)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V48_REGISTRY = {
    "debt_001_debt_to_assets_lvl_5d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_001_debt_to_assets_lvl_5d},
    "debt_002_debt_to_assets_zscore_5d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_002_debt_to_assets_zscore_5d},
    "debt_003_debt_to_assets_rank_5d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_003_debt_to_assets_rank_5d},
    "debt_004_debt_to_assets_lvl_21d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_004_debt_to_assets_lvl_21d},
    "debt_005_debt_to_assets_zscore_21d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_005_debt_to_assets_zscore_21d},
    "debt_006_debt_to_assets_rank_21d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_006_debt_to_assets_rank_21d},
    "debt_007_debt_to_assets_lvl_63d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_007_debt_to_assets_lvl_63d},
    "debt_008_debt_to_assets_zscore_63d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_008_debt_to_assets_zscore_63d},
    "debt_009_debt_to_assets_rank_63d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_009_debt_to_assets_rank_63d},
    "debt_010_debt_to_assets_lvl_126d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_010_debt_to_assets_lvl_126d},
    "debt_011_debt_to_assets_zscore_126d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_011_debt_to_assets_zscore_126d},
    "debt_012_debt_to_assets_rank_126d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_012_debt_to_assets_rank_126d},
    "debt_013_debt_to_assets_lvl_252d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_013_debt_to_assets_lvl_252d},
    "debt_014_debt_to_assets_zscore_252d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_014_debt_to_assets_zscore_252d},
    "debt_015_debt_to_assets_rank_252d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_015_debt_to_assets_rank_252d},
    "debt_016_debt_to_equity_lvl_5d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_016_debt_to_equity_lvl_5d},
    "debt_017_debt_to_equity_zscore_5d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_017_debt_to_equity_zscore_5d},
    "debt_018_debt_to_equity_rank_5d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_018_debt_to_equity_rank_5d},
    "debt_019_debt_to_equity_lvl_21d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_019_debt_to_equity_lvl_21d},
    "debt_020_debt_to_equity_zscore_21d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_020_debt_to_equity_zscore_21d},
    "debt_021_debt_to_equity_rank_21d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_021_debt_to_equity_rank_21d},
    "debt_022_debt_to_equity_lvl_63d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_022_debt_to_equity_lvl_63d},
    "debt_023_debt_to_equity_zscore_63d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_023_debt_to_equity_zscore_63d},
    "debt_024_debt_to_equity_rank_63d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_024_debt_to_equity_rank_63d},
    "debt_025_debt_to_equity_lvl_126d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_025_debt_to_equity_lvl_126d},
    "debt_026_debt_to_equity_zscore_126d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_026_debt_to_equity_zscore_126d},
    "debt_027_debt_to_equity_rank_126d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_027_debt_to_equity_rank_126d},
    "debt_028_debt_to_equity_lvl_252d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_028_debt_to_equity_lvl_252d},
    "debt_029_debt_to_equity_zscore_252d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_029_debt_to_equity_zscore_252d},
    "debt_030_debt_to_equity_rank_252d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_030_debt_to_equity_rank_252d},
    "debt_031_debt_to_ebitda_lvl_5d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_031_debt_to_ebitda_lvl_5d},
    "debt_032_debt_to_ebitda_zscore_5d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_032_debt_to_ebitda_zscore_5d},
    "debt_033_debt_to_ebitda_rank_5d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_033_debt_to_ebitda_rank_5d},
    "debt_034_debt_to_ebitda_lvl_21d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_034_debt_to_ebitda_lvl_21d},
    "debt_035_debt_to_ebitda_zscore_21d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_035_debt_to_ebitda_zscore_21d},
    "debt_036_debt_to_ebitda_rank_21d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_036_debt_to_ebitda_rank_21d},
    "debt_037_debt_to_ebitda_lvl_63d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_037_debt_to_ebitda_lvl_63d},
    "debt_038_debt_to_ebitda_zscore_63d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_038_debt_to_ebitda_zscore_63d},
    "debt_039_debt_to_ebitda_rank_63d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_039_debt_to_ebitda_rank_63d},
    "debt_040_debt_to_ebitda_lvl_126d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_040_debt_to_ebitda_lvl_126d},
    "debt_041_debt_to_ebitda_zscore_126d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_041_debt_to_ebitda_zscore_126d},
    "debt_042_debt_to_ebitda_rank_126d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_042_debt_to_ebitda_rank_126d},
    "debt_043_debt_to_ebitda_lvl_252d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_043_debt_to_ebitda_lvl_252d},
    "debt_044_debt_to_ebitda_zscore_252d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_044_debt_to_ebitda_zscore_252d},
    "debt_045_debt_to_ebitda_rank_252d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_045_debt_to_ebitda_rank_252d},
    "debt_046_debt_to_revenue_lvl_5d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_046_debt_to_revenue_lvl_5d},
    "debt_047_debt_to_revenue_zscore_5d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_047_debt_to_revenue_zscore_5d},
    "debt_048_debt_to_revenue_rank_5d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_048_debt_to_revenue_rank_5d},
    "debt_049_debt_to_revenue_lvl_21d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_049_debt_to_revenue_lvl_21d},
    "debt_050_debt_to_revenue_zscore_21d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_050_debt_to_revenue_zscore_21d},
    "debt_051_debt_to_revenue_rank_21d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_051_debt_to_revenue_rank_21d},
    "debt_052_debt_to_revenue_lvl_63d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_052_debt_to_revenue_lvl_63d},
    "debt_053_debt_to_revenue_zscore_63d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_053_debt_to_revenue_zscore_63d},
    "debt_054_debt_to_revenue_rank_63d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_054_debt_to_revenue_rank_63d},
    "debt_055_debt_to_revenue_lvl_126d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_055_debt_to_revenue_lvl_126d},
    "debt_056_debt_to_revenue_zscore_126d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_056_debt_to_revenue_zscore_126d},
    "debt_057_debt_to_revenue_rank_126d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_057_debt_to_revenue_rank_126d},
    "debt_058_debt_to_revenue_lvl_252d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_058_debt_to_revenue_lvl_252d},
    "debt_059_debt_to_revenue_zscore_252d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_059_debt_to_revenue_zscore_252d},
    "debt_060_debt_to_revenue_rank_252d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_060_debt_to_revenue_rank_252d},
    "debt_061_leverage_lvl_5d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_061_leverage_lvl_5d},
    "debt_062_leverage_zscore_5d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_062_leverage_zscore_5d},
    "debt_063_leverage_rank_5d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_063_leverage_rank_5d},
    "debt_064_leverage_lvl_21d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_064_leverage_lvl_21d},
    "debt_065_leverage_zscore_21d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_065_leverage_zscore_21d},
    "debt_066_leverage_rank_21d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_066_leverage_rank_21d},
    "debt_067_leverage_lvl_63d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_067_leverage_lvl_63d},
    "debt_068_leverage_zscore_63d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_068_leverage_zscore_63d},
    "debt_069_leverage_rank_63d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_069_leverage_rank_63d},
    "debt_070_leverage_lvl_126d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_070_leverage_lvl_126d},
    "debt_071_leverage_zscore_126d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_071_leverage_zscore_126d},
    "debt_072_leverage_rank_126d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_072_leverage_rank_126d},
    "debt_073_leverage_lvl_252d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_073_leverage_lvl_252d},
    "debt_074_leverage_zscore_252d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_074_leverage_zscore_252d},
    "debt_075_leverage_rank_252d": {"inputs": ['debt', 'assets', 'equity', 'ebitda', 'revenue'], "func": debt_075_leverage_rank_252d},
}
