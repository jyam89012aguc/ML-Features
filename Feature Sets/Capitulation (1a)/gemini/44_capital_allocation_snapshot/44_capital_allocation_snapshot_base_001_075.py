"""
44_capital_allocation_snapshot — Base Features 001-075
Domain: capital_allocation_snapshot
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

def call_001_div_yield_proxy_lvl_5d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_001_div_yield_proxy_lvl_5d"""
    base = _safe_div(dividends, revenue)
    return _rolling_mean(base, 5)

def call_002_div_yield_proxy_zscore_5d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_002_div_yield_proxy_zscore_5d"""
    base = _safe_div(dividends, revenue)
    return _zscore_rolling(base, 5)

def call_003_div_yield_proxy_rank_5d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_003_div_yield_proxy_rank_5d"""
    base = _safe_div(dividends, revenue)
    return _rank_pct(base, 5)

def call_004_div_yield_proxy_lvl_21d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_004_div_yield_proxy_lvl_21d"""
    base = _safe_div(dividends, revenue)
    return _rolling_mean(base, 21)

def call_005_div_yield_proxy_zscore_21d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_005_div_yield_proxy_zscore_21d"""
    base = _safe_div(dividends, revenue)
    return _zscore_rolling(base, 21)

def call_006_div_yield_proxy_rank_21d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_006_div_yield_proxy_rank_21d"""
    base = _safe_div(dividends, revenue)
    return _rank_pct(base, 21)

def call_007_div_yield_proxy_lvl_63d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_007_div_yield_proxy_lvl_63d"""
    base = _safe_div(dividends, revenue)
    return _rolling_mean(base, 63)

def call_008_div_yield_proxy_zscore_63d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_008_div_yield_proxy_zscore_63d"""
    base = _safe_div(dividends, revenue)
    return _zscore_rolling(base, 63)

def call_009_div_yield_proxy_rank_63d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_009_div_yield_proxy_rank_63d"""
    base = _safe_div(dividends, revenue)
    return _rank_pct(base, 63)

def call_010_div_yield_proxy_lvl_126d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_010_div_yield_proxy_lvl_126d"""
    base = _safe_div(dividends, revenue)
    return _rolling_mean(base, 126)

def call_011_div_yield_proxy_zscore_126d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_011_div_yield_proxy_zscore_126d"""
    base = _safe_div(dividends, revenue)
    return _zscore_rolling(base, 126)

def call_012_div_yield_proxy_rank_126d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_012_div_yield_proxy_rank_126d"""
    base = _safe_div(dividends, revenue)
    return _rank_pct(base, 126)

def call_013_div_yield_proxy_lvl_252d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_013_div_yield_proxy_lvl_252d"""
    base = _safe_div(dividends, revenue)
    return _rolling_mean(base, 252)

def call_014_div_yield_proxy_zscore_252d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_014_div_yield_proxy_zscore_252d"""
    base = _safe_div(dividends, revenue)
    return _zscore_rolling(base, 252)

def call_015_div_yield_proxy_rank_252d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_015_div_yield_proxy_rank_252d"""
    base = _safe_div(dividends, revenue)
    return _rank_pct(base, 252)

def call_016_div_to_assets_lvl_5d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_016_div_to_assets_lvl_5d"""
    base = _safe_div(dividends, assets)
    return _rolling_mean(base, 5)

def call_017_div_to_assets_zscore_5d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_017_div_to_assets_zscore_5d"""
    base = _safe_div(dividends, assets)
    return _zscore_rolling(base, 5)

def call_018_div_to_assets_rank_5d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_018_div_to_assets_rank_5d"""
    base = _safe_div(dividends, assets)
    return _rank_pct(base, 5)

def call_019_div_to_assets_lvl_21d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_019_div_to_assets_lvl_21d"""
    base = _safe_div(dividends, assets)
    return _rolling_mean(base, 21)

def call_020_div_to_assets_zscore_21d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_020_div_to_assets_zscore_21d"""
    base = _safe_div(dividends, assets)
    return _zscore_rolling(base, 21)

def call_021_div_to_assets_rank_21d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_021_div_to_assets_rank_21d"""
    base = _safe_div(dividends, assets)
    return _rank_pct(base, 21)

def call_022_div_to_assets_lvl_63d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_022_div_to_assets_lvl_63d"""
    base = _safe_div(dividends, assets)
    return _rolling_mean(base, 63)

def call_023_div_to_assets_zscore_63d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_023_div_to_assets_zscore_63d"""
    base = _safe_div(dividends, assets)
    return _zscore_rolling(base, 63)

def call_024_div_to_assets_rank_63d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_024_div_to_assets_rank_63d"""
    base = _safe_div(dividends, assets)
    return _rank_pct(base, 63)

def call_025_div_to_assets_lvl_126d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_025_div_to_assets_lvl_126d"""
    base = _safe_div(dividends, assets)
    return _rolling_mean(base, 126)

def call_026_div_to_assets_zscore_126d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_026_div_to_assets_zscore_126d"""
    base = _safe_div(dividends, assets)
    return _zscore_rolling(base, 126)

def call_027_div_to_assets_rank_126d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_027_div_to_assets_rank_126d"""
    base = _safe_div(dividends, assets)
    return _rank_pct(base, 126)

def call_028_div_to_assets_lvl_252d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_028_div_to_assets_lvl_252d"""
    base = _safe_div(dividends, assets)
    return _rolling_mean(base, 252)

def call_029_div_to_assets_zscore_252d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_029_div_to_assets_zscore_252d"""
    base = _safe_div(dividends, assets)
    return _zscore_rolling(base, 252)

def call_030_div_to_assets_rank_252d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_030_div_to_assets_rank_252d"""
    base = _safe_div(dividends, assets)
    return _rank_pct(base, 252)

def call_031_current_asset_intensity_lvl_5d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_031_current_asset_intensity_lvl_5d"""
    base = _safe_div(assetsc, assets)
    return _rolling_mean(base, 5)

def call_032_current_asset_intensity_zscore_5d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_032_current_asset_intensity_zscore_5d"""
    base = _safe_div(assetsc, assets)
    return _zscore_rolling(base, 5)

def call_033_current_asset_intensity_rank_5d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_033_current_asset_intensity_rank_5d"""
    base = _safe_div(assetsc, assets)
    return _rank_pct(base, 5)

def call_034_current_asset_intensity_lvl_21d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_034_current_asset_intensity_lvl_21d"""
    base = _safe_div(assetsc, assets)
    return _rolling_mean(base, 21)

def call_035_current_asset_intensity_zscore_21d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_035_current_asset_intensity_zscore_21d"""
    base = _safe_div(assetsc, assets)
    return _zscore_rolling(base, 21)

def call_036_current_asset_intensity_rank_21d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_036_current_asset_intensity_rank_21d"""
    base = _safe_div(assetsc, assets)
    return _rank_pct(base, 21)

def call_037_current_asset_intensity_lvl_63d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_037_current_asset_intensity_lvl_63d"""
    base = _safe_div(assetsc, assets)
    return _rolling_mean(base, 63)

def call_038_current_asset_intensity_zscore_63d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_038_current_asset_intensity_zscore_63d"""
    base = _safe_div(assetsc, assets)
    return _zscore_rolling(base, 63)

def call_039_current_asset_intensity_rank_63d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_039_current_asset_intensity_rank_63d"""
    base = _safe_div(assetsc, assets)
    return _rank_pct(base, 63)

def call_040_current_asset_intensity_lvl_126d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_040_current_asset_intensity_lvl_126d"""
    base = _safe_div(assetsc, assets)
    return _rolling_mean(base, 126)

def call_041_current_asset_intensity_zscore_126d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_041_current_asset_intensity_zscore_126d"""
    base = _safe_div(assetsc, assets)
    return _zscore_rolling(base, 126)

def call_042_current_asset_intensity_rank_126d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_042_current_asset_intensity_rank_126d"""
    base = _safe_div(assetsc, assets)
    return _rank_pct(base, 126)

def call_043_current_asset_intensity_lvl_252d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_043_current_asset_intensity_lvl_252d"""
    base = _safe_div(assetsc, assets)
    return _rolling_mean(base, 252)

def call_044_current_asset_intensity_zscore_252d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_044_current_asset_intensity_zscore_252d"""
    base = _safe_div(assetsc, assets)
    return _zscore_rolling(base, 252)

def call_045_current_asset_intensity_rank_252d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_045_current_asset_intensity_rank_252d"""
    base = _safe_div(assetsc, assets)
    return _rank_pct(base, 252)

def call_046_payout_proxy_lvl_5d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_046_payout_proxy_lvl_5d"""
    base = _safe_div(dividends, netinc)
    return _rolling_mean(base, 5)

def call_047_payout_proxy_zscore_5d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_047_payout_proxy_zscore_5d"""
    base = _safe_div(dividends, netinc)
    return _zscore_rolling(base, 5)

def call_048_payout_proxy_rank_5d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_048_payout_proxy_rank_5d"""
    base = _safe_div(dividends, netinc)
    return _rank_pct(base, 5)

def call_049_payout_proxy_lvl_21d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_049_payout_proxy_lvl_21d"""
    base = _safe_div(dividends, netinc)
    return _rolling_mean(base, 21)

def call_050_payout_proxy_zscore_21d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_050_payout_proxy_zscore_21d"""
    base = _safe_div(dividends, netinc)
    return _zscore_rolling(base, 21)

def call_051_payout_proxy_rank_21d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_051_payout_proxy_rank_21d"""
    base = _safe_div(dividends, netinc)
    return _rank_pct(base, 21)

def call_052_payout_proxy_lvl_63d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_052_payout_proxy_lvl_63d"""
    base = _safe_div(dividends, netinc)
    return _rolling_mean(base, 63)

def call_053_payout_proxy_zscore_63d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_053_payout_proxy_zscore_63d"""
    base = _safe_div(dividends, netinc)
    return _zscore_rolling(base, 63)

def call_054_payout_proxy_rank_63d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_054_payout_proxy_rank_63d"""
    base = _safe_div(dividends, netinc)
    return _rank_pct(base, 63)

def call_055_payout_proxy_lvl_126d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_055_payout_proxy_lvl_126d"""
    base = _safe_div(dividends, netinc)
    return _rolling_mean(base, 126)

def call_056_payout_proxy_zscore_126d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_056_payout_proxy_zscore_126d"""
    base = _safe_div(dividends, netinc)
    return _zscore_rolling(base, 126)

def call_057_payout_proxy_rank_126d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_057_payout_proxy_rank_126d"""
    base = _safe_div(dividends, netinc)
    return _rank_pct(base, 126)

def call_058_payout_proxy_lvl_252d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_058_payout_proxy_lvl_252d"""
    base = _safe_div(dividends, netinc)
    return _rolling_mean(base, 252)

def call_059_payout_proxy_zscore_252d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_059_payout_proxy_zscore_252d"""
    base = _safe_div(dividends, netinc)
    return _zscore_rolling(base, 252)

def call_060_payout_proxy_rank_252d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_060_payout_proxy_rank_252d"""
    base = _safe_div(dividends, netinc)
    return _rank_pct(base, 252)

def call_061_current_asset_to_revenue_lvl_5d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_061_current_asset_to_revenue_lvl_5d"""
    base = _safe_div(assetsc, revenue)
    return _rolling_mean(base, 5)

def call_062_current_asset_to_revenue_zscore_5d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_062_current_asset_to_revenue_zscore_5d"""
    base = _safe_div(assetsc, revenue)
    return _zscore_rolling(base, 5)

def call_063_current_asset_to_revenue_rank_5d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_063_current_asset_to_revenue_rank_5d"""
    base = _safe_div(assetsc, revenue)
    return _rank_pct(base, 5)

def call_064_current_asset_to_revenue_lvl_21d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_064_current_asset_to_revenue_lvl_21d"""
    base = _safe_div(assetsc, revenue)
    return _rolling_mean(base, 21)

def call_065_current_asset_to_revenue_zscore_21d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_065_current_asset_to_revenue_zscore_21d"""
    base = _safe_div(assetsc, revenue)
    return _zscore_rolling(base, 21)

def call_066_current_asset_to_revenue_rank_21d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_066_current_asset_to_revenue_rank_21d"""
    base = _safe_div(assetsc, revenue)
    return _rank_pct(base, 21)

def call_067_current_asset_to_revenue_lvl_63d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_067_current_asset_to_revenue_lvl_63d"""
    base = _safe_div(assetsc, revenue)
    return _rolling_mean(base, 63)

def call_068_current_asset_to_revenue_zscore_63d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_068_current_asset_to_revenue_zscore_63d"""
    base = _safe_div(assetsc, revenue)
    return _zscore_rolling(base, 63)

def call_069_current_asset_to_revenue_rank_63d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_069_current_asset_to_revenue_rank_63d"""
    base = _safe_div(assetsc, revenue)
    return _rank_pct(base, 63)

def call_070_current_asset_to_revenue_lvl_126d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_070_current_asset_to_revenue_lvl_126d"""
    base = _safe_div(assetsc, revenue)
    return _rolling_mean(base, 126)

def call_071_current_asset_to_revenue_zscore_126d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_071_current_asset_to_revenue_zscore_126d"""
    base = _safe_div(assetsc, revenue)
    return _zscore_rolling(base, 126)

def call_072_current_asset_to_revenue_rank_126d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_072_current_asset_to_revenue_rank_126d"""
    base = _safe_div(assetsc, revenue)
    return _rank_pct(base, 126)

def call_073_current_asset_to_revenue_lvl_252d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_073_current_asset_to_revenue_lvl_252d"""
    base = _safe_div(assetsc, revenue)
    return _rolling_mean(base, 252)

def call_074_current_asset_to_revenue_zscore_252d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_074_current_asset_to_revenue_zscore_252d"""
    base = _safe_div(assetsc, revenue)
    return _zscore_rolling(base, 252)

def call_075_current_asset_to_revenue_rank_252d(dividends: pd.Series, assetsc: pd.Series, assets: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """call_075_current_asset_to_revenue_rank_252d"""
    base = _safe_div(assetsc, revenue)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V44_REGISTRY = {
    "call_001_div_yield_proxy_lvl_5d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_001_div_yield_proxy_lvl_5d},
    "call_002_div_yield_proxy_zscore_5d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_002_div_yield_proxy_zscore_5d},
    "call_003_div_yield_proxy_rank_5d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_003_div_yield_proxy_rank_5d},
    "call_004_div_yield_proxy_lvl_21d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_004_div_yield_proxy_lvl_21d},
    "call_005_div_yield_proxy_zscore_21d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_005_div_yield_proxy_zscore_21d},
    "call_006_div_yield_proxy_rank_21d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_006_div_yield_proxy_rank_21d},
    "call_007_div_yield_proxy_lvl_63d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_007_div_yield_proxy_lvl_63d},
    "call_008_div_yield_proxy_zscore_63d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_008_div_yield_proxy_zscore_63d},
    "call_009_div_yield_proxy_rank_63d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_009_div_yield_proxy_rank_63d},
    "call_010_div_yield_proxy_lvl_126d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_010_div_yield_proxy_lvl_126d},
    "call_011_div_yield_proxy_zscore_126d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_011_div_yield_proxy_zscore_126d},
    "call_012_div_yield_proxy_rank_126d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_012_div_yield_proxy_rank_126d},
    "call_013_div_yield_proxy_lvl_252d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_013_div_yield_proxy_lvl_252d},
    "call_014_div_yield_proxy_zscore_252d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_014_div_yield_proxy_zscore_252d},
    "call_015_div_yield_proxy_rank_252d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_015_div_yield_proxy_rank_252d},
    "call_016_div_to_assets_lvl_5d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_016_div_to_assets_lvl_5d},
    "call_017_div_to_assets_zscore_5d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_017_div_to_assets_zscore_5d},
    "call_018_div_to_assets_rank_5d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_018_div_to_assets_rank_5d},
    "call_019_div_to_assets_lvl_21d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_019_div_to_assets_lvl_21d},
    "call_020_div_to_assets_zscore_21d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_020_div_to_assets_zscore_21d},
    "call_021_div_to_assets_rank_21d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_021_div_to_assets_rank_21d},
    "call_022_div_to_assets_lvl_63d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_022_div_to_assets_lvl_63d},
    "call_023_div_to_assets_zscore_63d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_023_div_to_assets_zscore_63d},
    "call_024_div_to_assets_rank_63d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_024_div_to_assets_rank_63d},
    "call_025_div_to_assets_lvl_126d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_025_div_to_assets_lvl_126d},
    "call_026_div_to_assets_zscore_126d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_026_div_to_assets_zscore_126d},
    "call_027_div_to_assets_rank_126d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_027_div_to_assets_rank_126d},
    "call_028_div_to_assets_lvl_252d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_028_div_to_assets_lvl_252d},
    "call_029_div_to_assets_zscore_252d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_029_div_to_assets_zscore_252d},
    "call_030_div_to_assets_rank_252d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_030_div_to_assets_rank_252d},
    "call_031_current_asset_intensity_lvl_5d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_031_current_asset_intensity_lvl_5d},
    "call_032_current_asset_intensity_zscore_5d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_032_current_asset_intensity_zscore_5d},
    "call_033_current_asset_intensity_rank_5d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_033_current_asset_intensity_rank_5d},
    "call_034_current_asset_intensity_lvl_21d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_034_current_asset_intensity_lvl_21d},
    "call_035_current_asset_intensity_zscore_21d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_035_current_asset_intensity_zscore_21d},
    "call_036_current_asset_intensity_rank_21d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_036_current_asset_intensity_rank_21d},
    "call_037_current_asset_intensity_lvl_63d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_037_current_asset_intensity_lvl_63d},
    "call_038_current_asset_intensity_zscore_63d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_038_current_asset_intensity_zscore_63d},
    "call_039_current_asset_intensity_rank_63d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_039_current_asset_intensity_rank_63d},
    "call_040_current_asset_intensity_lvl_126d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_040_current_asset_intensity_lvl_126d},
    "call_041_current_asset_intensity_zscore_126d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_041_current_asset_intensity_zscore_126d},
    "call_042_current_asset_intensity_rank_126d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_042_current_asset_intensity_rank_126d},
    "call_043_current_asset_intensity_lvl_252d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_043_current_asset_intensity_lvl_252d},
    "call_044_current_asset_intensity_zscore_252d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_044_current_asset_intensity_zscore_252d},
    "call_045_current_asset_intensity_rank_252d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_045_current_asset_intensity_rank_252d},
    "call_046_payout_proxy_lvl_5d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_046_payout_proxy_lvl_5d},
    "call_047_payout_proxy_zscore_5d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_047_payout_proxy_zscore_5d},
    "call_048_payout_proxy_rank_5d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_048_payout_proxy_rank_5d},
    "call_049_payout_proxy_lvl_21d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_049_payout_proxy_lvl_21d},
    "call_050_payout_proxy_zscore_21d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_050_payout_proxy_zscore_21d},
    "call_051_payout_proxy_rank_21d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_051_payout_proxy_rank_21d},
    "call_052_payout_proxy_lvl_63d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_052_payout_proxy_lvl_63d},
    "call_053_payout_proxy_zscore_63d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_053_payout_proxy_zscore_63d},
    "call_054_payout_proxy_rank_63d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_054_payout_proxy_rank_63d},
    "call_055_payout_proxy_lvl_126d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_055_payout_proxy_lvl_126d},
    "call_056_payout_proxy_zscore_126d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_056_payout_proxy_zscore_126d},
    "call_057_payout_proxy_rank_126d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_057_payout_proxy_rank_126d},
    "call_058_payout_proxy_lvl_252d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_058_payout_proxy_lvl_252d},
    "call_059_payout_proxy_zscore_252d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_059_payout_proxy_zscore_252d},
    "call_060_payout_proxy_rank_252d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_060_payout_proxy_rank_252d},
    "call_061_current_asset_to_revenue_lvl_5d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_061_current_asset_to_revenue_lvl_5d},
    "call_062_current_asset_to_revenue_zscore_5d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_062_current_asset_to_revenue_zscore_5d},
    "call_063_current_asset_to_revenue_rank_5d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_063_current_asset_to_revenue_rank_5d},
    "call_064_current_asset_to_revenue_lvl_21d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_064_current_asset_to_revenue_lvl_21d},
    "call_065_current_asset_to_revenue_zscore_21d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_065_current_asset_to_revenue_zscore_21d},
    "call_066_current_asset_to_revenue_rank_21d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_066_current_asset_to_revenue_rank_21d},
    "call_067_current_asset_to_revenue_lvl_63d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_067_current_asset_to_revenue_lvl_63d},
    "call_068_current_asset_to_revenue_zscore_63d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_068_current_asset_to_revenue_zscore_63d},
    "call_069_current_asset_to_revenue_rank_63d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_069_current_asset_to_revenue_rank_63d},
    "call_070_current_asset_to_revenue_lvl_126d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_070_current_asset_to_revenue_lvl_126d},
    "call_071_current_asset_to_revenue_zscore_126d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_071_current_asset_to_revenue_zscore_126d},
    "call_072_current_asset_to_revenue_rank_126d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_072_current_asset_to_revenue_rank_126d},
    "call_073_current_asset_to_revenue_lvl_252d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_073_current_asset_to_revenue_lvl_252d},
    "call_074_current_asset_to_revenue_zscore_252d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_074_current_asset_to_revenue_zscore_252d},
    "call_075_current_asset_to_revenue_rank_252d": {"inputs": ['dividends', 'assetsc', 'assets', 'revenue', 'netinc'], "func": call_075_current_asset_to_revenue_rank_252d},
}
