"""
38_balance_sheet_snapshot — Base Features 001-075
Domain: balance_sheet_snapshot
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

def bals_001_assets_lvl_lvl_5d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_001_assets_lvl_lvl_5d"""
    base = assets
    return _rolling_mean(base, 5)

def bals_002_assets_lvl_zscore_5d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_002_assets_lvl_zscore_5d"""
    base = assets
    return _zscore_rolling(base, 5)

def bals_003_assets_lvl_rank_5d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_003_assets_lvl_rank_5d"""
    base = assets
    return _rank_pct(base, 5)

def bals_004_assets_lvl_lvl_21d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_004_assets_lvl_lvl_21d"""
    base = assets
    return _rolling_mean(base, 21)

def bals_005_assets_lvl_zscore_21d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_005_assets_lvl_zscore_21d"""
    base = assets
    return _zscore_rolling(base, 21)

def bals_006_assets_lvl_rank_21d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_006_assets_lvl_rank_21d"""
    base = assets
    return _rank_pct(base, 21)

def bals_007_assets_lvl_lvl_63d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_007_assets_lvl_lvl_63d"""
    base = assets
    return _rolling_mean(base, 63)

def bals_008_assets_lvl_zscore_63d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_008_assets_lvl_zscore_63d"""
    base = assets
    return _zscore_rolling(base, 63)

def bals_009_assets_lvl_rank_63d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_009_assets_lvl_rank_63d"""
    base = assets
    return _rank_pct(base, 63)

def bals_010_assets_lvl_lvl_126d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_010_assets_lvl_lvl_126d"""
    base = assets
    return _rolling_mean(base, 126)

def bals_011_assets_lvl_zscore_126d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_011_assets_lvl_zscore_126d"""
    base = assets
    return _zscore_rolling(base, 126)

def bals_012_assets_lvl_rank_126d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_012_assets_lvl_rank_126d"""
    base = assets
    return _rank_pct(base, 126)

def bals_013_assets_lvl_lvl_252d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_013_assets_lvl_lvl_252d"""
    base = assets
    return _rolling_mean(base, 252)

def bals_014_assets_lvl_zscore_252d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_014_assets_lvl_zscore_252d"""
    base = assets
    return _zscore_rolling(base, 252)

def bals_015_assets_lvl_rank_252d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_015_assets_lvl_rank_252d"""
    base = assets
    return _rank_pct(base, 252)

def bals_016_debt_eq_lvl_5d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_016_debt_eq_lvl_5d"""
    base = _safe_div(debt, equity)
    return _rolling_mean(base, 5)

def bals_017_debt_eq_zscore_5d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_017_debt_eq_zscore_5d"""
    base = _safe_div(debt, equity)
    return _zscore_rolling(base, 5)

def bals_018_debt_eq_rank_5d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_018_debt_eq_rank_5d"""
    base = _safe_div(debt, equity)
    return _rank_pct(base, 5)

def bals_019_debt_eq_lvl_21d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_019_debt_eq_lvl_21d"""
    base = _safe_div(debt, equity)
    return _rolling_mean(base, 21)

def bals_020_debt_eq_zscore_21d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_020_debt_eq_zscore_21d"""
    base = _safe_div(debt, equity)
    return _zscore_rolling(base, 21)

def bals_021_debt_eq_rank_21d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_021_debt_eq_rank_21d"""
    base = _safe_div(debt, equity)
    return _rank_pct(base, 21)

def bals_022_debt_eq_lvl_63d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_022_debt_eq_lvl_63d"""
    base = _safe_div(debt, equity)
    return _rolling_mean(base, 63)

def bals_023_debt_eq_zscore_63d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_023_debt_eq_zscore_63d"""
    base = _safe_div(debt, equity)
    return _zscore_rolling(base, 63)

def bals_024_debt_eq_rank_63d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_024_debt_eq_rank_63d"""
    base = _safe_div(debt, equity)
    return _rank_pct(base, 63)

def bals_025_debt_eq_lvl_126d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_025_debt_eq_lvl_126d"""
    base = _safe_div(debt, equity)
    return _rolling_mean(base, 126)

def bals_026_debt_eq_zscore_126d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_026_debt_eq_zscore_126d"""
    base = _safe_div(debt, equity)
    return _zscore_rolling(base, 126)

def bals_027_debt_eq_rank_126d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_027_debt_eq_rank_126d"""
    base = _safe_div(debt, equity)
    return _rank_pct(base, 126)

def bals_028_debt_eq_lvl_252d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_028_debt_eq_lvl_252d"""
    base = _safe_div(debt, equity)
    return _rolling_mean(base, 252)

def bals_029_debt_eq_zscore_252d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_029_debt_eq_zscore_252d"""
    base = _safe_div(debt, equity)
    return _zscore_rolling(base, 252)

def bals_030_debt_eq_rank_252d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_030_debt_eq_rank_252d"""
    base = _safe_div(debt, equity)
    return _rank_pct(base, 252)

def bals_031_curr_rat_lvl_5d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_031_curr_rat_lvl_5d"""
    base = _safe_div(assets, liabs)
    return _rolling_mean(base, 5)

def bals_032_curr_rat_zscore_5d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_032_curr_rat_zscore_5d"""
    base = _safe_div(assets, liabs)
    return _zscore_rolling(base, 5)

def bals_033_curr_rat_rank_5d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_033_curr_rat_rank_5d"""
    base = _safe_div(assets, liabs)
    return _rank_pct(base, 5)

def bals_034_curr_rat_lvl_21d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_034_curr_rat_lvl_21d"""
    base = _safe_div(assets, liabs)
    return _rolling_mean(base, 21)

def bals_035_curr_rat_zscore_21d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_035_curr_rat_zscore_21d"""
    base = _safe_div(assets, liabs)
    return _zscore_rolling(base, 21)

def bals_036_curr_rat_rank_21d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_036_curr_rat_rank_21d"""
    base = _safe_div(assets, liabs)
    return _rank_pct(base, 21)

def bals_037_curr_rat_lvl_63d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_037_curr_rat_lvl_63d"""
    base = _safe_div(assets, liabs)
    return _rolling_mean(base, 63)

def bals_038_curr_rat_zscore_63d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_038_curr_rat_zscore_63d"""
    base = _safe_div(assets, liabs)
    return _zscore_rolling(base, 63)

def bals_039_curr_rat_rank_63d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_039_curr_rat_rank_63d"""
    base = _safe_div(assets, liabs)
    return _rank_pct(base, 63)

def bals_040_curr_rat_lvl_126d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_040_curr_rat_lvl_126d"""
    base = _safe_div(assets, liabs)
    return _rolling_mean(base, 126)

def bals_041_curr_rat_zscore_126d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_041_curr_rat_zscore_126d"""
    base = _safe_div(assets, liabs)
    return _zscore_rolling(base, 126)

def bals_042_curr_rat_rank_126d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_042_curr_rat_rank_126d"""
    base = _safe_div(assets, liabs)
    return _rank_pct(base, 126)

def bals_043_curr_rat_lvl_252d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_043_curr_rat_lvl_252d"""
    base = _safe_div(assets, liabs)
    return _rolling_mean(base, 252)

def bals_044_curr_rat_zscore_252d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_044_curr_rat_zscore_252d"""
    base = _safe_div(assets, liabs)
    return _zscore_rolling(base, 252)

def bals_045_curr_rat_rank_252d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_045_curr_rat_rank_252d"""
    base = _safe_div(assets, liabs)
    return _rank_pct(base, 252)

def bals_046_cash_assets_lvl_5d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_046_cash_assets_lvl_5d"""
    base = _safe_div(cashnequiv, assets)
    return _rolling_mean(base, 5)

def bals_047_cash_assets_zscore_5d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_047_cash_assets_zscore_5d"""
    base = _safe_div(cashnequiv, assets)
    return _zscore_rolling(base, 5)

def bals_048_cash_assets_rank_5d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_048_cash_assets_rank_5d"""
    base = _safe_div(cashnequiv, assets)
    return _rank_pct(base, 5)

def bals_049_cash_assets_lvl_21d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_049_cash_assets_lvl_21d"""
    base = _safe_div(cashnequiv, assets)
    return _rolling_mean(base, 21)

def bals_050_cash_assets_zscore_21d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_050_cash_assets_zscore_21d"""
    base = _safe_div(cashnequiv, assets)
    return _zscore_rolling(base, 21)

def bals_051_cash_assets_rank_21d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_051_cash_assets_rank_21d"""
    base = _safe_div(cashnequiv, assets)
    return _rank_pct(base, 21)

def bals_052_cash_assets_lvl_63d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_052_cash_assets_lvl_63d"""
    base = _safe_div(cashnequiv, assets)
    return _rolling_mean(base, 63)

def bals_053_cash_assets_zscore_63d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_053_cash_assets_zscore_63d"""
    base = _safe_div(cashnequiv, assets)
    return _zscore_rolling(base, 63)

def bals_054_cash_assets_rank_63d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_054_cash_assets_rank_63d"""
    base = _safe_div(cashnequiv, assets)
    return _rank_pct(base, 63)

def bals_055_cash_assets_lvl_126d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_055_cash_assets_lvl_126d"""
    base = _safe_div(cashnequiv, assets)
    return _rolling_mean(base, 126)

def bals_056_cash_assets_zscore_126d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_056_cash_assets_zscore_126d"""
    base = _safe_div(cashnequiv, assets)
    return _zscore_rolling(base, 126)

def bals_057_cash_assets_rank_126d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_057_cash_assets_rank_126d"""
    base = _safe_div(cashnequiv, assets)
    return _rank_pct(base, 126)

def bals_058_cash_assets_lvl_252d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_058_cash_assets_lvl_252d"""
    base = _safe_div(cashnequiv, assets)
    return _rolling_mean(base, 252)

def bals_059_cash_assets_zscore_252d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_059_cash_assets_zscore_252d"""
    base = _safe_div(cashnequiv, assets)
    return _zscore_rolling(base, 252)

def bals_060_cash_assets_rank_252d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_060_cash_assets_rank_252d"""
    base = _safe_div(cashnequiv, assets)
    return _rank_pct(base, 252)

def bals_061_equity_assets_lvl_5d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_061_equity_assets_lvl_5d"""
    base = _safe_div(equity, assets)
    return _rolling_mean(base, 5)

def bals_062_equity_assets_zscore_5d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_062_equity_assets_zscore_5d"""
    base = _safe_div(equity, assets)
    return _zscore_rolling(base, 5)

def bals_063_equity_assets_rank_5d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_063_equity_assets_rank_5d"""
    base = _safe_div(equity, assets)
    return _rank_pct(base, 5)

def bals_064_equity_assets_lvl_21d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_064_equity_assets_lvl_21d"""
    base = _safe_div(equity, assets)
    return _rolling_mean(base, 21)

def bals_065_equity_assets_zscore_21d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_065_equity_assets_zscore_21d"""
    base = _safe_div(equity, assets)
    return _zscore_rolling(base, 21)

def bals_066_equity_assets_rank_21d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_066_equity_assets_rank_21d"""
    base = _safe_div(equity, assets)
    return _rank_pct(base, 21)

def bals_067_equity_assets_lvl_63d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_067_equity_assets_lvl_63d"""
    base = _safe_div(equity, assets)
    return _rolling_mean(base, 63)

def bals_068_equity_assets_zscore_63d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_068_equity_assets_zscore_63d"""
    base = _safe_div(equity, assets)
    return _zscore_rolling(base, 63)

def bals_069_equity_assets_rank_63d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_069_equity_assets_rank_63d"""
    base = _safe_div(equity, assets)
    return _rank_pct(base, 63)

def bals_070_equity_assets_lvl_126d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_070_equity_assets_lvl_126d"""
    base = _safe_div(equity, assets)
    return _rolling_mean(base, 126)

def bals_071_equity_assets_zscore_126d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_071_equity_assets_zscore_126d"""
    base = _safe_div(equity, assets)
    return _zscore_rolling(base, 126)

def bals_072_equity_assets_rank_126d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_072_equity_assets_rank_126d"""
    base = _safe_div(equity, assets)
    return _rank_pct(base, 126)

def bals_073_equity_assets_lvl_252d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_073_equity_assets_lvl_252d"""
    base = _safe_div(equity, assets)
    return _rolling_mean(base, 252)

def bals_074_equity_assets_zscore_252d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_074_equity_assets_zscore_252d"""
    base = _safe_div(equity, assets)
    return _zscore_rolling(base, 252)

def bals_075_equity_assets_rank_252d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_075_equity_assets_rank_252d"""
    base = _safe_div(equity, assets)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V38_REGISTRY = {
    "bals_001_assets_lvl_lvl_5d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_001_assets_lvl_lvl_5d},
    "bals_002_assets_lvl_zscore_5d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_002_assets_lvl_zscore_5d},
    "bals_003_assets_lvl_rank_5d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_003_assets_lvl_rank_5d},
    "bals_004_assets_lvl_lvl_21d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_004_assets_lvl_lvl_21d},
    "bals_005_assets_lvl_zscore_21d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_005_assets_lvl_zscore_21d},
    "bals_006_assets_lvl_rank_21d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_006_assets_lvl_rank_21d},
    "bals_007_assets_lvl_lvl_63d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_007_assets_lvl_lvl_63d},
    "bals_008_assets_lvl_zscore_63d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_008_assets_lvl_zscore_63d},
    "bals_009_assets_lvl_rank_63d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_009_assets_lvl_rank_63d},
    "bals_010_assets_lvl_lvl_126d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_010_assets_lvl_lvl_126d},
    "bals_011_assets_lvl_zscore_126d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_011_assets_lvl_zscore_126d},
    "bals_012_assets_lvl_rank_126d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_012_assets_lvl_rank_126d},
    "bals_013_assets_lvl_lvl_252d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_013_assets_lvl_lvl_252d},
    "bals_014_assets_lvl_zscore_252d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_014_assets_lvl_zscore_252d},
    "bals_015_assets_lvl_rank_252d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_015_assets_lvl_rank_252d},
    "bals_016_debt_eq_lvl_5d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_016_debt_eq_lvl_5d},
    "bals_017_debt_eq_zscore_5d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_017_debt_eq_zscore_5d},
    "bals_018_debt_eq_rank_5d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_018_debt_eq_rank_5d},
    "bals_019_debt_eq_lvl_21d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_019_debt_eq_lvl_21d},
    "bals_020_debt_eq_zscore_21d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_020_debt_eq_zscore_21d},
    "bals_021_debt_eq_rank_21d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_021_debt_eq_rank_21d},
    "bals_022_debt_eq_lvl_63d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_022_debt_eq_lvl_63d},
    "bals_023_debt_eq_zscore_63d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_023_debt_eq_zscore_63d},
    "bals_024_debt_eq_rank_63d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_024_debt_eq_rank_63d},
    "bals_025_debt_eq_lvl_126d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_025_debt_eq_lvl_126d},
    "bals_026_debt_eq_zscore_126d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_026_debt_eq_zscore_126d},
    "bals_027_debt_eq_rank_126d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_027_debt_eq_rank_126d},
    "bals_028_debt_eq_lvl_252d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_028_debt_eq_lvl_252d},
    "bals_029_debt_eq_zscore_252d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_029_debt_eq_zscore_252d},
    "bals_030_debt_eq_rank_252d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_030_debt_eq_rank_252d},
    "bals_031_curr_rat_lvl_5d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_031_curr_rat_lvl_5d},
    "bals_032_curr_rat_zscore_5d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_032_curr_rat_zscore_5d},
    "bals_033_curr_rat_rank_5d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_033_curr_rat_rank_5d},
    "bals_034_curr_rat_lvl_21d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_034_curr_rat_lvl_21d},
    "bals_035_curr_rat_zscore_21d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_035_curr_rat_zscore_21d},
    "bals_036_curr_rat_rank_21d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_036_curr_rat_rank_21d},
    "bals_037_curr_rat_lvl_63d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_037_curr_rat_lvl_63d},
    "bals_038_curr_rat_zscore_63d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_038_curr_rat_zscore_63d},
    "bals_039_curr_rat_rank_63d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_039_curr_rat_rank_63d},
    "bals_040_curr_rat_lvl_126d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_040_curr_rat_lvl_126d},
    "bals_041_curr_rat_zscore_126d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_041_curr_rat_zscore_126d},
    "bals_042_curr_rat_rank_126d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_042_curr_rat_rank_126d},
    "bals_043_curr_rat_lvl_252d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_043_curr_rat_lvl_252d},
    "bals_044_curr_rat_zscore_252d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_044_curr_rat_zscore_252d},
    "bals_045_curr_rat_rank_252d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_045_curr_rat_rank_252d},
    "bals_046_cash_assets_lvl_5d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_046_cash_assets_lvl_5d},
    "bals_047_cash_assets_zscore_5d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_047_cash_assets_zscore_5d},
    "bals_048_cash_assets_rank_5d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_048_cash_assets_rank_5d},
    "bals_049_cash_assets_lvl_21d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_049_cash_assets_lvl_21d},
    "bals_050_cash_assets_zscore_21d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_050_cash_assets_zscore_21d},
    "bals_051_cash_assets_rank_21d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_051_cash_assets_rank_21d},
    "bals_052_cash_assets_lvl_63d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_052_cash_assets_lvl_63d},
    "bals_053_cash_assets_zscore_63d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_053_cash_assets_zscore_63d},
    "bals_054_cash_assets_rank_63d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_054_cash_assets_rank_63d},
    "bals_055_cash_assets_lvl_126d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_055_cash_assets_lvl_126d},
    "bals_056_cash_assets_zscore_126d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_056_cash_assets_zscore_126d},
    "bals_057_cash_assets_rank_126d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_057_cash_assets_rank_126d},
    "bals_058_cash_assets_lvl_252d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_058_cash_assets_lvl_252d},
    "bals_059_cash_assets_zscore_252d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_059_cash_assets_zscore_252d},
    "bals_060_cash_assets_rank_252d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_060_cash_assets_rank_252d},
    "bals_061_equity_assets_lvl_5d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_061_equity_assets_lvl_5d},
    "bals_062_equity_assets_zscore_5d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_062_equity_assets_zscore_5d},
    "bals_063_equity_assets_rank_5d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_063_equity_assets_rank_5d},
    "bals_064_equity_assets_lvl_21d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_064_equity_assets_lvl_21d},
    "bals_065_equity_assets_zscore_21d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_065_equity_assets_zscore_21d},
    "bals_066_equity_assets_rank_21d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_066_equity_assets_rank_21d},
    "bals_067_equity_assets_lvl_63d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_067_equity_assets_lvl_63d},
    "bals_068_equity_assets_zscore_63d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_068_equity_assets_zscore_63d},
    "bals_069_equity_assets_rank_63d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_069_equity_assets_rank_63d},
    "bals_070_equity_assets_lvl_126d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_070_equity_assets_lvl_126d},
    "bals_071_equity_assets_zscore_126d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_071_equity_assets_zscore_126d},
    "bals_072_equity_assets_rank_126d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_072_equity_assets_rank_126d},
    "bals_073_equity_assets_lvl_252d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_073_equity_assets_lvl_252d},
    "bals_074_equity_assets_zscore_252d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_074_equity_assets_zscore_252d},
    "bals_075_equity_assets_rank_252d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_075_equity_assets_rank_252d},
}
