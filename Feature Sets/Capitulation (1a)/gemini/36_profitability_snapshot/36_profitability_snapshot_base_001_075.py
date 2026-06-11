"""
36_profitability_snapshot — Base Features 001-075
Domain: profitability_snapshot
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

def prof_001_net_margin_lvl_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_001_net_margin_lvl_5d"""
    base = _safe_div(netinc, revenue)
    return _rolling_mean(base, 5)

def prof_002_net_margin_zscore_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_002_net_margin_zscore_5d"""
    base = _safe_div(netinc, revenue)
    return _zscore_rolling(base, 5)

def prof_003_net_margin_rank_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_003_net_margin_rank_5d"""
    base = _safe_div(netinc, revenue)
    return _rank_pct(base, 5)

def prof_004_net_margin_lvl_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_004_net_margin_lvl_21d"""
    base = _safe_div(netinc, revenue)
    return _rolling_mean(base, 21)

def prof_005_net_margin_zscore_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_005_net_margin_zscore_21d"""
    base = _safe_div(netinc, revenue)
    return _zscore_rolling(base, 21)

def prof_006_net_margin_rank_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_006_net_margin_rank_21d"""
    base = _safe_div(netinc, revenue)
    return _rank_pct(base, 21)

def prof_007_net_margin_lvl_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_007_net_margin_lvl_63d"""
    base = _safe_div(netinc, revenue)
    return _rolling_mean(base, 63)

def prof_008_net_margin_zscore_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_008_net_margin_zscore_63d"""
    base = _safe_div(netinc, revenue)
    return _zscore_rolling(base, 63)

def prof_009_net_margin_rank_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_009_net_margin_rank_63d"""
    base = _safe_div(netinc, revenue)
    return _rank_pct(base, 63)

def prof_010_net_margin_lvl_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_010_net_margin_lvl_126d"""
    base = _safe_div(netinc, revenue)
    return _rolling_mean(base, 126)

def prof_011_net_margin_zscore_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_011_net_margin_zscore_126d"""
    base = _safe_div(netinc, revenue)
    return _zscore_rolling(base, 126)

def prof_012_net_margin_rank_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_012_net_margin_rank_126d"""
    base = _safe_div(netinc, revenue)
    return _rank_pct(base, 126)

def prof_013_net_margin_lvl_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_013_net_margin_lvl_252d"""
    base = _safe_div(netinc, revenue)
    return _rolling_mean(base, 252)

def prof_014_net_margin_zscore_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_014_net_margin_zscore_252d"""
    base = _safe_div(netinc, revenue)
    return _zscore_rolling(base, 252)

def prof_015_net_margin_rank_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_015_net_margin_rank_252d"""
    base = _safe_div(netinc, revenue)
    return _rank_pct(base, 252)

def prof_016_op_margin_lvl_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_016_op_margin_lvl_5d"""
    base = _safe_div(opinc, revenue)
    return _rolling_mean(base, 5)

def prof_017_op_margin_zscore_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_017_op_margin_zscore_5d"""
    base = _safe_div(opinc, revenue)
    return _zscore_rolling(base, 5)

def prof_018_op_margin_rank_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_018_op_margin_rank_5d"""
    base = _safe_div(opinc, revenue)
    return _rank_pct(base, 5)

def prof_019_op_margin_lvl_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_019_op_margin_lvl_21d"""
    base = _safe_div(opinc, revenue)
    return _rolling_mean(base, 21)

def prof_020_op_margin_zscore_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_020_op_margin_zscore_21d"""
    base = _safe_div(opinc, revenue)
    return _zscore_rolling(base, 21)

def prof_021_op_margin_rank_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_021_op_margin_rank_21d"""
    base = _safe_div(opinc, revenue)
    return _rank_pct(base, 21)

def prof_022_op_margin_lvl_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_022_op_margin_lvl_63d"""
    base = _safe_div(opinc, revenue)
    return _rolling_mean(base, 63)

def prof_023_op_margin_zscore_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_023_op_margin_zscore_63d"""
    base = _safe_div(opinc, revenue)
    return _zscore_rolling(base, 63)

def prof_024_op_margin_rank_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_024_op_margin_rank_63d"""
    base = _safe_div(opinc, revenue)
    return _rank_pct(base, 63)

def prof_025_op_margin_lvl_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_025_op_margin_lvl_126d"""
    base = _safe_div(opinc, revenue)
    return _rolling_mean(base, 126)

def prof_026_op_margin_zscore_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_026_op_margin_zscore_126d"""
    base = _safe_div(opinc, revenue)
    return _zscore_rolling(base, 126)

def prof_027_op_margin_rank_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_027_op_margin_rank_126d"""
    base = _safe_div(opinc, revenue)
    return _rank_pct(base, 126)

def prof_028_op_margin_lvl_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_028_op_margin_lvl_252d"""
    base = _safe_div(opinc, revenue)
    return _rolling_mean(base, 252)

def prof_029_op_margin_zscore_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_029_op_margin_zscore_252d"""
    base = _safe_div(opinc, revenue)
    return _zscore_rolling(base, 252)

def prof_030_op_margin_rank_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_030_op_margin_rank_252d"""
    base = _safe_div(opinc, revenue)
    return _rank_pct(base, 252)

def prof_031_netinc_lvl_lvl_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_031_netinc_lvl_lvl_5d"""
    base = netinc
    return _rolling_mean(base, 5)

def prof_032_netinc_lvl_zscore_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_032_netinc_lvl_zscore_5d"""
    base = netinc
    return _zscore_rolling(base, 5)

def prof_033_netinc_lvl_rank_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_033_netinc_lvl_rank_5d"""
    base = netinc
    return _rank_pct(base, 5)

def prof_034_netinc_lvl_lvl_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_034_netinc_lvl_lvl_21d"""
    base = netinc
    return _rolling_mean(base, 21)

def prof_035_netinc_lvl_zscore_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_035_netinc_lvl_zscore_21d"""
    base = netinc
    return _zscore_rolling(base, 21)

def prof_036_netinc_lvl_rank_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_036_netinc_lvl_rank_21d"""
    base = netinc
    return _rank_pct(base, 21)

def prof_037_netinc_lvl_lvl_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_037_netinc_lvl_lvl_63d"""
    base = netinc
    return _rolling_mean(base, 63)

def prof_038_netinc_lvl_zscore_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_038_netinc_lvl_zscore_63d"""
    base = netinc
    return _zscore_rolling(base, 63)

def prof_039_netinc_lvl_rank_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_039_netinc_lvl_rank_63d"""
    base = netinc
    return _rank_pct(base, 63)

def prof_040_netinc_lvl_lvl_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_040_netinc_lvl_lvl_126d"""
    base = netinc
    return _rolling_mean(base, 126)

def prof_041_netinc_lvl_zscore_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_041_netinc_lvl_zscore_126d"""
    base = netinc
    return _zscore_rolling(base, 126)

def prof_042_netinc_lvl_rank_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_042_netinc_lvl_rank_126d"""
    base = netinc
    return _rank_pct(base, 126)

def prof_043_netinc_lvl_lvl_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_043_netinc_lvl_lvl_252d"""
    base = netinc
    return _rolling_mean(base, 252)

def prof_044_netinc_lvl_zscore_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_044_netinc_lvl_zscore_252d"""
    base = netinc
    return _zscore_rolling(base, 252)

def prof_045_netinc_lvl_rank_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_045_netinc_lvl_rank_252d"""
    base = netinc
    return _rank_pct(base, 252)

def prof_046_roe_lvl_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_046_roe_lvl_5d"""
    base = _safe_div(netinc, equity)
    return _rolling_mean(base, 5)

def prof_047_roe_zscore_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_047_roe_zscore_5d"""
    base = _safe_div(netinc, equity)
    return _zscore_rolling(base, 5)

def prof_048_roe_rank_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_048_roe_rank_5d"""
    base = _safe_div(netinc, equity)
    return _rank_pct(base, 5)

def prof_049_roe_lvl_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_049_roe_lvl_21d"""
    base = _safe_div(netinc, equity)
    return _rolling_mean(base, 21)

def prof_050_roe_zscore_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_050_roe_zscore_21d"""
    base = _safe_div(netinc, equity)
    return _zscore_rolling(base, 21)

def prof_051_roe_rank_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_051_roe_rank_21d"""
    base = _safe_div(netinc, equity)
    return _rank_pct(base, 21)

def prof_052_roe_lvl_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_052_roe_lvl_63d"""
    base = _safe_div(netinc, equity)
    return _rolling_mean(base, 63)

def prof_053_roe_zscore_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_053_roe_zscore_63d"""
    base = _safe_div(netinc, equity)
    return _zscore_rolling(base, 63)

def prof_054_roe_rank_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_054_roe_rank_63d"""
    base = _safe_div(netinc, equity)
    return _rank_pct(base, 63)

def prof_055_roe_lvl_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_055_roe_lvl_126d"""
    base = _safe_div(netinc, equity)
    return _rolling_mean(base, 126)

def prof_056_roe_zscore_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_056_roe_zscore_126d"""
    base = _safe_div(netinc, equity)
    return _zscore_rolling(base, 126)

def prof_057_roe_rank_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_057_roe_rank_126d"""
    base = _safe_div(netinc, equity)
    return _rank_pct(base, 126)

def prof_058_roe_lvl_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_058_roe_lvl_252d"""
    base = _safe_div(netinc, equity)
    return _rolling_mean(base, 252)

def prof_059_roe_zscore_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_059_roe_zscore_252d"""
    base = _safe_div(netinc, equity)
    return _zscore_rolling(base, 252)

def prof_060_roe_rank_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_060_roe_rank_252d"""
    base = _safe_div(netinc, equity)
    return _rank_pct(base, 252)

def prof_061_roa_lvl_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_061_roa_lvl_5d"""
    base = _safe_div(netinc, assets)
    return _rolling_mean(base, 5)

def prof_062_roa_zscore_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_062_roa_zscore_5d"""
    base = _safe_div(netinc, assets)
    return _zscore_rolling(base, 5)

def prof_063_roa_rank_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_063_roa_rank_5d"""
    base = _safe_div(netinc, assets)
    return _rank_pct(base, 5)

def prof_064_roa_lvl_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_064_roa_lvl_21d"""
    base = _safe_div(netinc, assets)
    return _rolling_mean(base, 21)

def prof_065_roa_zscore_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_065_roa_zscore_21d"""
    base = _safe_div(netinc, assets)
    return _zscore_rolling(base, 21)

def prof_066_roa_rank_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_066_roa_rank_21d"""
    base = _safe_div(netinc, assets)
    return _rank_pct(base, 21)

def prof_067_roa_lvl_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_067_roa_lvl_63d"""
    base = _safe_div(netinc, assets)
    return _rolling_mean(base, 63)

def prof_068_roa_zscore_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_068_roa_zscore_63d"""
    base = _safe_div(netinc, assets)
    return _zscore_rolling(base, 63)

def prof_069_roa_rank_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_069_roa_rank_63d"""
    base = _safe_div(netinc, assets)
    return _rank_pct(base, 63)

def prof_070_roa_lvl_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_070_roa_lvl_126d"""
    base = _safe_div(netinc, assets)
    return _rolling_mean(base, 126)

def prof_071_roa_zscore_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_071_roa_zscore_126d"""
    base = _safe_div(netinc, assets)
    return _zscore_rolling(base, 126)

def prof_072_roa_rank_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_072_roa_rank_126d"""
    base = _safe_div(netinc, assets)
    return _rank_pct(base, 126)

def prof_073_roa_lvl_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_073_roa_lvl_252d"""
    base = _safe_div(netinc, assets)
    return _rolling_mean(base, 252)

def prof_074_roa_zscore_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_074_roa_zscore_252d"""
    base = _safe_div(netinc, assets)
    return _zscore_rolling(base, 252)

def prof_075_roa_rank_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_075_roa_rank_252d"""
    base = _safe_div(netinc, assets)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V36_REGISTRY = {
    "prof_001_net_margin_lvl_5d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_001_net_margin_lvl_5d},
    "prof_002_net_margin_zscore_5d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_002_net_margin_zscore_5d},
    "prof_003_net_margin_rank_5d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_003_net_margin_rank_5d},
    "prof_004_net_margin_lvl_21d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_004_net_margin_lvl_21d},
    "prof_005_net_margin_zscore_21d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_005_net_margin_zscore_21d},
    "prof_006_net_margin_rank_21d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_006_net_margin_rank_21d},
    "prof_007_net_margin_lvl_63d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_007_net_margin_lvl_63d},
    "prof_008_net_margin_zscore_63d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_008_net_margin_zscore_63d},
    "prof_009_net_margin_rank_63d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_009_net_margin_rank_63d},
    "prof_010_net_margin_lvl_126d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_010_net_margin_lvl_126d},
    "prof_011_net_margin_zscore_126d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_011_net_margin_zscore_126d},
    "prof_012_net_margin_rank_126d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_012_net_margin_rank_126d},
    "prof_013_net_margin_lvl_252d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_013_net_margin_lvl_252d},
    "prof_014_net_margin_zscore_252d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_014_net_margin_zscore_252d},
    "prof_015_net_margin_rank_252d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_015_net_margin_rank_252d},
    "prof_016_op_margin_lvl_5d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_016_op_margin_lvl_5d},
    "prof_017_op_margin_zscore_5d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_017_op_margin_zscore_5d},
    "prof_018_op_margin_rank_5d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_018_op_margin_rank_5d},
    "prof_019_op_margin_lvl_21d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_019_op_margin_lvl_21d},
    "prof_020_op_margin_zscore_21d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_020_op_margin_zscore_21d},
    "prof_021_op_margin_rank_21d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_021_op_margin_rank_21d},
    "prof_022_op_margin_lvl_63d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_022_op_margin_lvl_63d},
    "prof_023_op_margin_zscore_63d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_023_op_margin_zscore_63d},
    "prof_024_op_margin_rank_63d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_024_op_margin_rank_63d},
    "prof_025_op_margin_lvl_126d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_025_op_margin_lvl_126d},
    "prof_026_op_margin_zscore_126d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_026_op_margin_zscore_126d},
    "prof_027_op_margin_rank_126d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_027_op_margin_rank_126d},
    "prof_028_op_margin_lvl_252d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_028_op_margin_lvl_252d},
    "prof_029_op_margin_zscore_252d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_029_op_margin_zscore_252d},
    "prof_030_op_margin_rank_252d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_030_op_margin_rank_252d},
    "prof_031_netinc_lvl_lvl_5d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_031_netinc_lvl_lvl_5d},
    "prof_032_netinc_lvl_zscore_5d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_032_netinc_lvl_zscore_5d},
    "prof_033_netinc_lvl_rank_5d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_033_netinc_lvl_rank_5d},
    "prof_034_netinc_lvl_lvl_21d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_034_netinc_lvl_lvl_21d},
    "prof_035_netinc_lvl_zscore_21d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_035_netinc_lvl_zscore_21d},
    "prof_036_netinc_lvl_rank_21d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_036_netinc_lvl_rank_21d},
    "prof_037_netinc_lvl_lvl_63d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_037_netinc_lvl_lvl_63d},
    "prof_038_netinc_lvl_zscore_63d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_038_netinc_lvl_zscore_63d},
    "prof_039_netinc_lvl_rank_63d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_039_netinc_lvl_rank_63d},
    "prof_040_netinc_lvl_lvl_126d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_040_netinc_lvl_lvl_126d},
    "prof_041_netinc_lvl_zscore_126d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_041_netinc_lvl_zscore_126d},
    "prof_042_netinc_lvl_rank_126d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_042_netinc_lvl_rank_126d},
    "prof_043_netinc_lvl_lvl_252d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_043_netinc_lvl_lvl_252d},
    "prof_044_netinc_lvl_zscore_252d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_044_netinc_lvl_zscore_252d},
    "prof_045_netinc_lvl_rank_252d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_045_netinc_lvl_rank_252d},
    "prof_046_roe_lvl_5d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_046_roe_lvl_5d},
    "prof_047_roe_zscore_5d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_047_roe_zscore_5d},
    "prof_048_roe_rank_5d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_048_roe_rank_5d},
    "prof_049_roe_lvl_21d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_049_roe_lvl_21d},
    "prof_050_roe_zscore_21d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_050_roe_zscore_21d},
    "prof_051_roe_rank_21d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_051_roe_rank_21d},
    "prof_052_roe_lvl_63d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_052_roe_lvl_63d},
    "prof_053_roe_zscore_63d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_053_roe_zscore_63d},
    "prof_054_roe_rank_63d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_054_roe_rank_63d},
    "prof_055_roe_lvl_126d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_055_roe_lvl_126d},
    "prof_056_roe_zscore_126d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_056_roe_zscore_126d},
    "prof_057_roe_rank_126d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_057_roe_rank_126d},
    "prof_058_roe_lvl_252d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_058_roe_lvl_252d},
    "prof_059_roe_zscore_252d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_059_roe_zscore_252d},
    "prof_060_roe_rank_252d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_060_roe_rank_252d},
    "prof_061_roa_lvl_5d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_061_roa_lvl_5d},
    "prof_062_roa_zscore_5d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_062_roa_zscore_5d},
    "prof_063_roa_rank_5d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_063_roa_rank_5d},
    "prof_064_roa_lvl_21d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_064_roa_lvl_21d},
    "prof_065_roa_zscore_21d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_065_roa_zscore_21d},
    "prof_066_roa_rank_21d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_066_roa_rank_21d},
    "prof_067_roa_lvl_63d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_067_roa_lvl_63d},
    "prof_068_roa_zscore_63d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_068_roa_zscore_63d},
    "prof_069_roa_rank_63d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_069_roa_rank_63d},
    "prof_070_roa_lvl_126d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_070_roa_lvl_126d},
    "prof_071_roa_zscore_126d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_071_roa_zscore_126d},
    "prof_072_roa_rank_126d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_072_roa_rank_126d},
    "prof_073_roa_lvl_252d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_073_roa_lvl_252d},
    "prof_074_roa_zscore_252d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_074_roa_zscore_252d},
    "prof_075_roa_rank_252d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_075_roa_rank_252d},
}
