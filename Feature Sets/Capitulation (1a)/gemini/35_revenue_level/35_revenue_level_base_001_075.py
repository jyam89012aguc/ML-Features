"""
35_revenue_level — Base Features 001-075
Domain: revenue_level
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

def revl_001_level_lvl_5d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_001_level_lvl_5d"""
    base = revenue
    return _rolling_mean(base, 5)

def revl_002_level_zscore_5d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_002_level_zscore_5d"""
    base = revenue
    return _zscore_rolling(base, 5)

def revl_003_level_rank_5d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_003_level_rank_5d"""
    base = revenue
    return _rank_pct(base, 5)

def revl_004_level_lvl_21d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_004_level_lvl_21d"""
    base = revenue
    return _rolling_mean(base, 21)

def revl_005_level_zscore_21d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_005_level_zscore_21d"""
    base = revenue
    return _zscore_rolling(base, 21)

def revl_006_level_rank_21d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_006_level_rank_21d"""
    base = revenue
    return _rank_pct(base, 21)

def revl_007_level_lvl_63d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_007_level_lvl_63d"""
    base = revenue
    return _rolling_mean(base, 63)

def revl_008_level_zscore_63d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_008_level_zscore_63d"""
    base = revenue
    return _zscore_rolling(base, 63)

def revl_009_level_rank_63d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_009_level_rank_63d"""
    base = revenue
    return _rank_pct(base, 63)

def revl_010_level_lvl_126d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_010_level_lvl_126d"""
    base = revenue
    return _rolling_mean(base, 126)

def revl_011_level_zscore_126d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_011_level_zscore_126d"""
    base = revenue
    return _zscore_rolling(base, 126)

def revl_012_level_rank_126d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_012_level_rank_126d"""
    base = revenue
    return _rank_pct(base, 126)

def revl_013_level_lvl_252d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_013_level_lvl_252d"""
    base = revenue
    return _rolling_mean(base, 252)

def revl_014_level_zscore_252d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_014_level_zscore_252d"""
    base = revenue
    return _zscore_rolling(base, 252)

def revl_015_level_rank_252d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_015_level_rank_252d"""
    base = revenue
    return _rank_pct(base, 252)

def revl_016_ps_lvl_5d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_016_ps_lvl_5d"""
    base = _safe_div(revenue, sharesbas)
    return _rolling_mean(base, 5)

def revl_017_ps_zscore_5d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_017_ps_zscore_5d"""
    base = _safe_div(revenue, sharesbas)
    return _zscore_rolling(base, 5)

def revl_018_ps_rank_5d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_018_ps_rank_5d"""
    base = _safe_div(revenue, sharesbas)
    return _rank_pct(base, 5)

def revl_019_ps_lvl_21d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_019_ps_lvl_21d"""
    base = _safe_div(revenue, sharesbas)
    return _rolling_mean(base, 21)

def revl_020_ps_zscore_21d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_020_ps_zscore_21d"""
    base = _safe_div(revenue, sharesbas)
    return _zscore_rolling(base, 21)

def revl_021_ps_rank_21d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_021_ps_rank_21d"""
    base = _safe_div(revenue, sharesbas)
    return _rank_pct(base, 21)

def revl_022_ps_lvl_63d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_022_ps_lvl_63d"""
    base = _safe_div(revenue, sharesbas)
    return _rolling_mean(base, 63)

def revl_023_ps_zscore_63d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_023_ps_zscore_63d"""
    base = _safe_div(revenue, sharesbas)
    return _zscore_rolling(base, 63)

def revl_024_ps_rank_63d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_024_ps_rank_63d"""
    base = _safe_div(revenue, sharesbas)
    return _rank_pct(base, 63)

def revl_025_ps_lvl_126d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_025_ps_lvl_126d"""
    base = _safe_div(revenue, sharesbas)
    return _rolling_mean(base, 126)

def revl_026_ps_zscore_126d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_026_ps_zscore_126d"""
    base = _safe_div(revenue, sharesbas)
    return _zscore_rolling(base, 126)

def revl_027_ps_rank_126d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_027_ps_rank_126d"""
    base = _safe_div(revenue, sharesbas)
    return _rank_pct(base, 126)

def revl_028_ps_lvl_252d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_028_ps_lvl_252d"""
    base = _safe_div(revenue, sharesbas)
    return _rolling_mean(base, 252)

def revl_029_ps_zscore_252d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_029_ps_zscore_252d"""
    base = _safe_div(revenue, sharesbas)
    return _zscore_rolling(base, 252)

def revl_030_ps_rank_252d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_030_ps_rank_252d"""
    base = _safe_div(revenue, sharesbas)
    return _rank_pct(base, 252)

def revl_031_pa_lvl_5d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_031_pa_lvl_5d"""
    base = _safe_div(revenue, assets)
    return _rolling_mean(base, 5)

def revl_032_pa_zscore_5d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_032_pa_zscore_5d"""
    base = _safe_div(revenue, assets)
    return _zscore_rolling(base, 5)

def revl_033_pa_rank_5d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_033_pa_rank_5d"""
    base = _safe_div(revenue, assets)
    return _rank_pct(base, 5)

def revl_034_pa_lvl_21d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_034_pa_lvl_21d"""
    base = _safe_div(revenue, assets)
    return _rolling_mean(base, 21)

def revl_035_pa_zscore_21d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_035_pa_zscore_21d"""
    base = _safe_div(revenue, assets)
    return _zscore_rolling(base, 21)

def revl_036_pa_rank_21d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_036_pa_rank_21d"""
    base = _safe_div(revenue, assets)
    return _rank_pct(base, 21)

def revl_037_pa_lvl_63d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_037_pa_lvl_63d"""
    base = _safe_div(revenue, assets)
    return _rolling_mean(base, 63)

def revl_038_pa_zscore_63d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_038_pa_zscore_63d"""
    base = _safe_div(revenue, assets)
    return _zscore_rolling(base, 63)

def revl_039_pa_rank_63d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_039_pa_rank_63d"""
    base = _safe_div(revenue, assets)
    return _rank_pct(base, 63)

def revl_040_pa_lvl_126d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_040_pa_lvl_126d"""
    base = _safe_div(revenue, assets)
    return _rolling_mean(base, 126)

def revl_041_pa_zscore_126d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_041_pa_zscore_126d"""
    base = _safe_div(revenue, assets)
    return _zscore_rolling(base, 126)

def revl_042_pa_rank_126d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_042_pa_rank_126d"""
    base = _safe_div(revenue, assets)
    return _rank_pct(base, 126)

def revl_043_pa_lvl_252d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_043_pa_lvl_252d"""
    base = _safe_div(revenue, assets)
    return _rolling_mean(base, 252)

def revl_044_pa_zscore_252d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_044_pa_zscore_252d"""
    base = _safe_div(revenue, assets)
    return _zscore_rolling(base, 252)

def revl_045_pa_rank_252d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_045_pa_rank_252d"""
    base = _safe_div(revenue, assets)
    return _rank_pct(base, 252)

def revl_046_log_lvl_5d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_046_log_lvl_5d"""
    base = np.log(revenue.clip(lower=_EPS))
    return _rolling_mean(base, 5)

def revl_047_log_zscore_5d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_047_log_zscore_5d"""
    base = np.log(revenue.clip(lower=_EPS))
    return _zscore_rolling(base, 5)

def revl_048_log_rank_5d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_048_log_rank_5d"""
    base = np.log(revenue.clip(lower=_EPS))
    return _rank_pct(base, 5)

def revl_049_log_lvl_21d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_049_log_lvl_21d"""
    base = np.log(revenue.clip(lower=_EPS))
    return _rolling_mean(base, 21)

def revl_050_log_zscore_21d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_050_log_zscore_21d"""
    base = np.log(revenue.clip(lower=_EPS))
    return _zscore_rolling(base, 21)

def revl_051_log_rank_21d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_051_log_rank_21d"""
    base = np.log(revenue.clip(lower=_EPS))
    return _rank_pct(base, 21)

def revl_052_log_lvl_63d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_052_log_lvl_63d"""
    base = np.log(revenue.clip(lower=_EPS))
    return _rolling_mean(base, 63)

def revl_053_log_zscore_63d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_053_log_zscore_63d"""
    base = np.log(revenue.clip(lower=_EPS))
    return _zscore_rolling(base, 63)

def revl_054_log_rank_63d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_054_log_rank_63d"""
    base = np.log(revenue.clip(lower=_EPS))
    return _rank_pct(base, 63)

def revl_055_log_lvl_126d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_055_log_lvl_126d"""
    base = np.log(revenue.clip(lower=_EPS))
    return _rolling_mean(base, 126)

def revl_056_log_zscore_126d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_056_log_zscore_126d"""
    base = np.log(revenue.clip(lower=_EPS))
    return _zscore_rolling(base, 126)

def revl_057_log_rank_126d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_057_log_rank_126d"""
    base = np.log(revenue.clip(lower=_EPS))
    return _rank_pct(base, 126)

def revl_058_log_lvl_252d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_058_log_lvl_252d"""
    base = np.log(revenue.clip(lower=_EPS))
    return _rolling_mean(base, 252)

def revl_059_log_zscore_252d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_059_log_zscore_252d"""
    base = np.log(revenue.clip(lower=_EPS))
    return _zscore_rolling(base, 252)

def revl_060_log_rank_252d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_060_log_rank_252d"""
    base = np.log(revenue.clip(lower=_EPS))
    return _rank_pct(base, 252)

def revl_061_yield_lvl_5d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_061_yield_lvl_5d"""
    base = _safe_div(revenue, marketcap)
    return _rolling_mean(base, 5)

def revl_062_yield_zscore_5d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_062_yield_zscore_5d"""
    base = _safe_div(revenue, marketcap)
    return _zscore_rolling(base, 5)

def revl_063_yield_rank_5d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_063_yield_rank_5d"""
    base = _safe_div(revenue, marketcap)
    return _rank_pct(base, 5)

def revl_064_yield_lvl_21d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_064_yield_lvl_21d"""
    base = _safe_div(revenue, marketcap)
    return _rolling_mean(base, 21)

def revl_065_yield_zscore_21d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_065_yield_zscore_21d"""
    base = _safe_div(revenue, marketcap)
    return _zscore_rolling(base, 21)

def revl_066_yield_rank_21d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_066_yield_rank_21d"""
    base = _safe_div(revenue, marketcap)
    return _rank_pct(base, 21)

def revl_067_yield_lvl_63d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_067_yield_lvl_63d"""
    base = _safe_div(revenue, marketcap)
    return _rolling_mean(base, 63)

def revl_068_yield_zscore_63d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_068_yield_zscore_63d"""
    base = _safe_div(revenue, marketcap)
    return _zscore_rolling(base, 63)

def revl_069_yield_rank_63d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_069_yield_rank_63d"""
    base = _safe_div(revenue, marketcap)
    return _rank_pct(base, 63)

def revl_070_yield_lvl_126d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_070_yield_lvl_126d"""
    base = _safe_div(revenue, marketcap)
    return _rolling_mean(base, 126)

def revl_071_yield_zscore_126d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_071_yield_zscore_126d"""
    base = _safe_div(revenue, marketcap)
    return _zscore_rolling(base, 126)

def revl_072_yield_rank_126d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_072_yield_rank_126d"""
    base = _safe_div(revenue, marketcap)
    return _rank_pct(base, 126)

def revl_073_yield_lvl_252d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_073_yield_lvl_252d"""
    base = _safe_div(revenue, marketcap)
    return _rolling_mean(base, 252)

def revl_074_yield_zscore_252d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_074_yield_zscore_252d"""
    base = _safe_div(revenue, marketcap)
    return _zscore_rolling(base, 252)

def revl_075_yield_rank_252d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_075_yield_rank_252d"""
    base = _safe_div(revenue, marketcap)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V35_REGISTRY = {
    "revl_001_level_lvl_5d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_001_level_lvl_5d},
    "revl_002_level_zscore_5d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_002_level_zscore_5d},
    "revl_003_level_rank_5d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_003_level_rank_5d},
    "revl_004_level_lvl_21d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_004_level_lvl_21d},
    "revl_005_level_zscore_21d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_005_level_zscore_21d},
    "revl_006_level_rank_21d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_006_level_rank_21d},
    "revl_007_level_lvl_63d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_007_level_lvl_63d},
    "revl_008_level_zscore_63d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_008_level_zscore_63d},
    "revl_009_level_rank_63d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_009_level_rank_63d},
    "revl_010_level_lvl_126d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_010_level_lvl_126d},
    "revl_011_level_zscore_126d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_011_level_zscore_126d},
    "revl_012_level_rank_126d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_012_level_rank_126d},
    "revl_013_level_lvl_252d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_013_level_lvl_252d},
    "revl_014_level_zscore_252d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_014_level_zscore_252d},
    "revl_015_level_rank_252d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_015_level_rank_252d},
    "revl_016_ps_lvl_5d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_016_ps_lvl_5d},
    "revl_017_ps_zscore_5d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_017_ps_zscore_5d},
    "revl_018_ps_rank_5d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_018_ps_rank_5d},
    "revl_019_ps_lvl_21d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_019_ps_lvl_21d},
    "revl_020_ps_zscore_21d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_020_ps_zscore_21d},
    "revl_021_ps_rank_21d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_021_ps_rank_21d},
    "revl_022_ps_lvl_63d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_022_ps_lvl_63d},
    "revl_023_ps_zscore_63d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_023_ps_zscore_63d},
    "revl_024_ps_rank_63d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_024_ps_rank_63d},
    "revl_025_ps_lvl_126d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_025_ps_lvl_126d},
    "revl_026_ps_zscore_126d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_026_ps_zscore_126d},
    "revl_027_ps_rank_126d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_027_ps_rank_126d},
    "revl_028_ps_lvl_252d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_028_ps_lvl_252d},
    "revl_029_ps_zscore_252d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_029_ps_zscore_252d},
    "revl_030_ps_rank_252d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_030_ps_rank_252d},
    "revl_031_pa_lvl_5d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_031_pa_lvl_5d},
    "revl_032_pa_zscore_5d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_032_pa_zscore_5d},
    "revl_033_pa_rank_5d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_033_pa_rank_5d},
    "revl_034_pa_lvl_21d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_034_pa_lvl_21d},
    "revl_035_pa_zscore_21d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_035_pa_zscore_21d},
    "revl_036_pa_rank_21d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_036_pa_rank_21d},
    "revl_037_pa_lvl_63d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_037_pa_lvl_63d},
    "revl_038_pa_zscore_63d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_038_pa_zscore_63d},
    "revl_039_pa_rank_63d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_039_pa_rank_63d},
    "revl_040_pa_lvl_126d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_040_pa_lvl_126d},
    "revl_041_pa_zscore_126d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_041_pa_zscore_126d},
    "revl_042_pa_rank_126d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_042_pa_rank_126d},
    "revl_043_pa_lvl_252d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_043_pa_lvl_252d},
    "revl_044_pa_zscore_252d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_044_pa_zscore_252d},
    "revl_045_pa_rank_252d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_045_pa_rank_252d},
    "revl_046_log_lvl_5d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_046_log_lvl_5d},
    "revl_047_log_zscore_5d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_047_log_zscore_5d},
    "revl_048_log_rank_5d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_048_log_rank_5d},
    "revl_049_log_lvl_21d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_049_log_lvl_21d},
    "revl_050_log_zscore_21d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_050_log_zscore_21d},
    "revl_051_log_rank_21d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_051_log_rank_21d},
    "revl_052_log_lvl_63d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_052_log_lvl_63d},
    "revl_053_log_zscore_63d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_053_log_zscore_63d},
    "revl_054_log_rank_63d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_054_log_rank_63d},
    "revl_055_log_lvl_126d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_055_log_lvl_126d},
    "revl_056_log_zscore_126d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_056_log_zscore_126d},
    "revl_057_log_rank_126d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_057_log_rank_126d},
    "revl_058_log_lvl_252d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_058_log_lvl_252d},
    "revl_059_log_zscore_252d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_059_log_zscore_252d},
    "revl_060_log_rank_252d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_060_log_rank_252d},
    "revl_061_yield_lvl_5d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_061_yield_lvl_5d},
    "revl_062_yield_zscore_5d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_062_yield_zscore_5d},
    "revl_063_yield_rank_5d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_063_yield_rank_5d},
    "revl_064_yield_lvl_21d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_064_yield_lvl_21d},
    "revl_065_yield_zscore_21d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_065_yield_zscore_21d},
    "revl_066_yield_rank_21d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_066_yield_rank_21d},
    "revl_067_yield_lvl_63d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_067_yield_lvl_63d},
    "revl_068_yield_zscore_63d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_068_yield_zscore_63d},
    "revl_069_yield_rank_63d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_069_yield_rank_63d},
    "revl_070_yield_lvl_126d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_070_yield_lvl_126d},
    "revl_071_yield_zscore_126d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_071_yield_zscore_126d},
    "revl_072_yield_rank_126d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_072_yield_rank_126d},
    "revl_073_yield_lvl_252d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_073_yield_lvl_252d},
    "revl_074_yield_zscore_252d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_074_yield_zscore_252d},
    "revl_075_yield_rank_252d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_075_yield_rank_252d},
}
