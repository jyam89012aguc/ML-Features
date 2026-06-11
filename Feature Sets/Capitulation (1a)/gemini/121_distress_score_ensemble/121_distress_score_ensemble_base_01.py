"""
121_distress_score_ensemble — Base Features Part 1
Domain: distress_score_ensemble
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

def dsen_001_composite_distress_z_lvl_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_001_composite_distress_z_lvl_5d
    ECONOMIC RATIONALE: Combined leverage and cash flow distress.
    """
    base = _zscore_rolling(liabs/equity.replace(0, 1e-9) + (ocf < 0).astype(float), 252)
    return _rolling_mean(base, 5)

def dsen_002_composite_distress_z_zscore_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_002_composite_distress_z_zscore_5d
    ECONOMIC RATIONALE: Combined leverage and cash flow distress.
    """
    base = _zscore_rolling(liabs/equity.replace(0, 1e-9) + (ocf < 0).astype(float), 252)
    return _zscore_rolling(base, 5)

def dsen_003_composite_distress_z_rank_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_003_composite_distress_z_rank_5d
    ECONOMIC RATIONALE: Combined leverage and cash flow distress.
    """
    base = _zscore_rolling(liabs/equity.replace(0, 1e-9) + (ocf < 0).astype(float), 252)
    return _rank_pct(base, 5)

def dsen_004_composite_distress_z_lvl_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_004_composite_distress_z_lvl_21d
    ECONOMIC RATIONALE: Combined leverage and cash flow distress.
    """
    base = _zscore_rolling(liabs/equity.replace(0, 1e-9) + (ocf < 0).astype(float), 252)
    return _rolling_mean(base, 21)

def dsen_005_composite_distress_z_zscore_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_005_composite_distress_z_zscore_21d
    ECONOMIC RATIONALE: Combined leverage and cash flow distress.
    """
    base = _zscore_rolling(liabs/equity.replace(0, 1e-9) + (ocf < 0).astype(float), 252)
    return _zscore_rolling(base, 21)

def dsen_006_composite_distress_z_rank_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_006_composite_distress_z_rank_21d
    ECONOMIC RATIONALE: Combined leverage and cash flow distress.
    """
    base = _zscore_rolling(liabs/equity.replace(0, 1e-9) + (ocf < 0).astype(float), 252)
    return _rank_pct(base, 21)

def dsen_007_composite_distress_z_lvl_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_007_composite_distress_z_lvl_63d
    ECONOMIC RATIONALE: Combined leverage and cash flow distress.
    """
    base = _zscore_rolling(liabs/equity.replace(0, 1e-9) + (ocf < 0).astype(float), 252)
    return _rolling_mean(base, 63)

def dsen_008_composite_distress_z_zscore_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_008_composite_distress_z_zscore_63d
    ECONOMIC RATIONALE: Combined leverage and cash flow distress.
    """
    base = _zscore_rolling(liabs/equity.replace(0, 1e-9) + (ocf < 0).astype(float), 252)
    return _zscore_rolling(base, 63)

def dsen_009_composite_distress_z_rank_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_009_composite_distress_z_rank_63d
    ECONOMIC RATIONALE: Combined leverage and cash flow distress.
    """
    base = _zscore_rolling(liabs/equity.replace(0, 1e-9) + (ocf < 0).astype(float), 252)
    return _rank_pct(base, 63)

def dsen_010_composite_distress_z_lvl_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_010_composite_distress_z_lvl_126d
    ECONOMIC RATIONALE: Combined leverage and cash flow distress.
    """
    base = _zscore_rolling(liabs/equity.replace(0, 1e-9) + (ocf < 0).astype(float), 252)
    return _rolling_mean(base, 126)

def dsen_011_composite_distress_z_zscore_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_011_composite_distress_z_zscore_126d
    ECONOMIC RATIONALE: Combined leverage and cash flow distress.
    """
    base = _zscore_rolling(liabs/equity.replace(0, 1e-9) + (ocf < 0).astype(float), 252)
    return _zscore_rolling(base, 126)

def dsen_012_composite_distress_z_rank_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_012_composite_distress_z_rank_126d
    ECONOMIC RATIONALE: Combined leverage and cash flow distress.
    """
    base = _zscore_rolling(liabs/equity.replace(0, 1e-9) + (ocf < 0).astype(float), 252)
    return _rank_pct(base, 126)

def dsen_013_composite_distress_z_lvl_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_013_composite_distress_z_lvl_252d
    ECONOMIC RATIONALE: Combined leverage and cash flow distress.
    """
    base = _zscore_rolling(liabs/equity.replace(0, 1e-9) + (ocf < 0).astype(float), 252)
    return _rolling_mean(base, 252)

def dsen_014_composite_distress_z_zscore_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_014_composite_distress_z_zscore_252d
    ECONOMIC RATIONALE: Combined leverage and cash flow distress.
    """
    base = _zscore_rolling(liabs/equity.replace(0, 1e-9) + (ocf < 0).astype(float), 252)
    return _zscore_rolling(base, 252)

def dsen_015_composite_distress_z_rank_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_015_composite_distress_z_rank_252d
    ECONOMIC RATIONALE: Combined leverage and cash flow distress.
    """
    base = _zscore_rolling(liabs/equity.replace(0, 1e-9) + (ocf < 0).astype(float), 252)
    return _rank_pct(base, 252)

def dsen_016_valuation_solvency_blend_lvl_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_016_valuation_solvency_blend_lvl_5d
    ECONOMIC RATIONALE: Valuation drawdown weighted by solvency.
    """
    base = (close/close.rolling(252).max()) * (equity/liabs.replace(0, 1e-9))
    return _rolling_mean(base, 5)

def dsen_017_valuation_solvency_blend_zscore_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_017_valuation_solvency_blend_zscore_5d
    ECONOMIC RATIONALE: Valuation drawdown weighted by solvency.
    """
    base = (close/close.rolling(252).max()) * (equity/liabs.replace(0, 1e-9))
    return _zscore_rolling(base, 5)

def dsen_018_valuation_solvency_blend_rank_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_018_valuation_solvency_blend_rank_5d
    ECONOMIC RATIONALE: Valuation drawdown weighted by solvency.
    """
    base = (close/close.rolling(252).max()) * (equity/liabs.replace(0, 1e-9))
    return _rank_pct(base, 5)

def dsen_019_valuation_solvency_blend_lvl_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_019_valuation_solvency_blend_lvl_21d
    ECONOMIC RATIONALE: Valuation drawdown weighted by solvency.
    """
    base = (close/close.rolling(252).max()) * (equity/liabs.replace(0, 1e-9))
    return _rolling_mean(base, 21)

def dsen_020_valuation_solvency_blend_zscore_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_020_valuation_solvency_blend_zscore_21d
    ECONOMIC RATIONALE: Valuation drawdown weighted by solvency.
    """
    base = (close/close.rolling(252).max()) * (equity/liabs.replace(0, 1e-9))
    return _zscore_rolling(base, 21)

def dsen_021_valuation_solvency_blend_rank_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_021_valuation_solvency_blend_rank_21d
    ECONOMIC RATIONALE: Valuation drawdown weighted by solvency.
    """
    base = (close/close.rolling(252).max()) * (equity/liabs.replace(0, 1e-9))
    return _rank_pct(base, 21)

def dsen_022_valuation_solvency_blend_lvl_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_022_valuation_solvency_blend_lvl_63d
    ECONOMIC RATIONALE: Valuation drawdown weighted by solvency.
    """
    base = (close/close.rolling(252).max()) * (equity/liabs.replace(0, 1e-9))
    return _rolling_mean(base, 63)

def dsen_023_valuation_solvency_blend_zscore_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_023_valuation_solvency_blend_zscore_63d
    ECONOMIC RATIONALE: Valuation drawdown weighted by solvency.
    """
    base = (close/close.rolling(252).max()) * (equity/liabs.replace(0, 1e-9))
    return _zscore_rolling(base, 63)

def dsen_024_valuation_solvency_blend_rank_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_024_valuation_solvency_blend_rank_63d
    ECONOMIC RATIONALE: Valuation drawdown weighted by solvency.
    """
    base = (close/close.rolling(252).max()) * (equity/liabs.replace(0, 1e-9))
    return _rank_pct(base, 63)

def dsen_025_valuation_solvency_blend_lvl_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_025_valuation_solvency_blend_lvl_126d
    ECONOMIC RATIONALE: Valuation drawdown weighted by solvency.
    """
    base = (close/close.rolling(252).max()) * (equity/liabs.replace(0, 1e-9))
    return _rolling_mean(base, 126)

def dsen_026_valuation_solvency_blend_zscore_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_026_valuation_solvency_blend_zscore_126d
    ECONOMIC RATIONALE: Valuation drawdown weighted by solvency.
    """
    base = (close/close.rolling(252).max()) * (equity/liabs.replace(0, 1e-9))
    return _zscore_rolling(base, 126)

def dsen_027_valuation_solvency_blend_rank_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_027_valuation_solvency_blend_rank_126d
    ECONOMIC RATIONALE: Valuation drawdown weighted by solvency.
    """
    base = (close/close.rolling(252).max()) * (equity/liabs.replace(0, 1e-9))
    return _rank_pct(base, 126)

def dsen_028_valuation_solvency_blend_lvl_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_028_valuation_solvency_blend_lvl_252d
    ECONOMIC RATIONALE: Valuation drawdown weighted by solvency.
    """
    base = (close/close.rolling(252).max()) * (equity/liabs.replace(0, 1e-9))
    return _rolling_mean(base, 252)

def dsen_029_valuation_solvency_blend_zscore_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_029_valuation_solvency_blend_zscore_252d
    ECONOMIC RATIONALE: Valuation drawdown weighted by solvency.
    """
    base = (close/close.rolling(252).max()) * (equity/liabs.replace(0, 1e-9))
    return _zscore_rolling(base, 252)

def dsen_030_valuation_solvency_blend_rank_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_030_valuation_solvency_blend_rank_252d
    ECONOMIC RATIONALE: Valuation drawdown weighted by solvency.
    """
    base = (close/close.rolling(252).max()) * (equity/liabs.replace(0, 1e-9))
    return _rank_pct(base, 252)

def dsen_031_liquidity_momentum_ensemble_lvl_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_031_liquidity_momentum_ensemble_lvl_5d
    ECONOMIC RATIONALE: Combined fundamental and price momentum.
    """
    base = ocf.pct_change(63) + close.pct_change(63)
    return _rolling_mean(base, 5)

def dsen_032_liquidity_momentum_ensemble_zscore_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_032_liquidity_momentum_ensemble_zscore_5d
    ECONOMIC RATIONALE: Combined fundamental and price momentum.
    """
    base = ocf.pct_change(63) + close.pct_change(63)
    return _zscore_rolling(base, 5)

def dsen_033_liquidity_momentum_ensemble_rank_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_033_liquidity_momentum_ensemble_rank_5d
    ECONOMIC RATIONALE: Combined fundamental and price momentum.
    """
    base = ocf.pct_change(63) + close.pct_change(63)
    return _rank_pct(base, 5)

def dsen_034_liquidity_momentum_ensemble_lvl_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_034_liquidity_momentum_ensemble_lvl_21d
    ECONOMIC RATIONALE: Combined fundamental and price momentum.
    """
    base = ocf.pct_change(63) + close.pct_change(63)
    return _rolling_mean(base, 21)

def dsen_035_liquidity_momentum_ensemble_zscore_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_035_liquidity_momentum_ensemble_zscore_21d
    ECONOMIC RATIONALE: Combined fundamental and price momentum.
    """
    base = ocf.pct_change(63) + close.pct_change(63)
    return _zscore_rolling(base, 21)

def dsen_036_liquidity_momentum_ensemble_rank_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_036_liquidity_momentum_ensemble_rank_21d
    ECONOMIC RATIONALE: Combined fundamental and price momentum.
    """
    base = ocf.pct_change(63) + close.pct_change(63)
    return _rank_pct(base, 21)

def dsen_037_liquidity_momentum_ensemble_lvl_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_037_liquidity_momentum_ensemble_lvl_63d
    ECONOMIC RATIONALE: Combined fundamental and price momentum.
    """
    base = ocf.pct_change(63) + close.pct_change(63)
    return _rolling_mean(base, 63)

def dsen_038_liquidity_momentum_ensemble_zscore_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_038_liquidity_momentum_ensemble_zscore_63d
    ECONOMIC RATIONALE: Combined fundamental and price momentum.
    """
    base = ocf.pct_change(63) + close.pct_change(63)
    return _zscore_rolling(base, 63)

def dsen_039_liquidity_momentum_ensemble_rank_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_039_liquidity_momentum_ensemble_rank_63d
    ECONOMIC RATIONALE: Combined fundamental and price momentum.
    """
    base = ocf.pct_change(63) + close.pct_change(63)
    return _rank_pct(base, 63)

def dsen_040_liquidity_momentum_ensemble_lvl_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_040_liquidity_momentum_ensemble_lvl_126d
    ECONOMIC RATIONALE: Combined fundamental and price momentum.
    """
    base = ocf.pct_change(63) + close.pct_change(63)
    return _rolling_mean(base, 126)

def dsen_041_liquidity_momentum_ensemble_zscore_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_041_liquidity_momentum_ensemble_zscore_126d
    ECONOMIC RATIONALE: Combined fundamental and price momentum.
    """
    base = ocf.pct_change(63) + close.pct_change(63)
    return _zscore_rolling(base, 126)

def dsen_042_liquidity_momentum_ensemble_rank_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_042_liquidity_momentum_ensemble_rank_126d
    ECONOMIC RATIONALE: Combined fundamental and price momentum.
    """
    base = ocf.pct_change(63) + close.pct_change(63)
    return _rank_pct(base, 126)

def dsen_043_liquidity_momentum_ensemble_lvl_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_043_liquidity_momentum_ensemble_lvl_252d
    ECONOMIC RATIONALE: Combined fundamental and price momentum.
    """
    base = ocf.pct_change(63) + close.pct_change(63)
    return _rolling_mean(base, 252)

def dsen_044_liquidity_momentum_ensemble_zscore_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_044_liquidity_momentum_ensemble_zscore_252d
    ECONOMIC RATIONALE: Combined fundamental and price momentum.
    """
    base = ocf.pct_change(63) + close.pct_change(63)
    return _zscore_rolling(base, 252)

def dsen_045_liquidity_momentum_ensemble_rank_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_045_liquidity_momentum_ensemble_rank_252d
    ECONOMIC RATIONALE: Combined fundamental and price momentum.
    """
    base = ocf.pct_change(63) + close.pct_change(63)
    return _rank_pct(base, 252)

def dsen_046_distress_regime_indicator_lvl_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_046_distress_regime_indicator_lvl_5d
    ECONOMIC RATIONALE: Binary flag for structural distress.
    """
    base = ((liabs > assets) | (ocf < 0)).astype(float)
    return _rolling_mean(base, 5)

def dsen_047_distress_regime_indicator_zscore_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_047_distress_regime_indicator_zscore_5d
    ECONOMIC RATIONALE: Binary flag for structural distress.
    """
    base = ((liabs > assets) | (ocf < 0)).astype(float)
    return _zscore_rolling(base, 5)

def dsen_048_distress_regime_indicator_rank_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_048_distress_regime_indicator_rank_5d
    ECONOMIC RATIONALE: Binary flag for structural distress.
    """
    base = ((liabs > assets) | (ocf < 0)).astype(float)
    return _rank_pct(base, 5)

def dsen_049_distress_regime_indicator_lvl_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_049_distress_regime_indicator_lvl_21d
    ECONOMIC RATIONALE: Binary flag for structural distress.
    """
    base = ((liabs > assets) | (ocf < 0)).astype(float)
    return _rolling_mean(base, 21)

def dsen_050_distress_regime_indicator_zscore_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_050_distress_regime_indicator_zscore_21d
    ECONOMIC RATIONALE: Binary flag for structural distress.
    """
    base = ((liabs > assets) | (ocf < 0)).astype(float)
    return _zscore_rolling(base, 21)

def dsen_051_distress_regime_indicator_rank_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_051_distress_regime_indicator_rank_21d
    ECONOMIC RATIONALE: Binary flag for structural distress.
    """
    base = ((liabs > assets) | (ocf < 0)).astype(float)
    return _rank_pct(base, 21)

def dsen_052_distress_regime_indicator_lvl_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_052_distress_regime_indicator_lvl_63d
    ECONOMIC RATIONALE: Binary flag for structural distress.
    """
    base = ((liabs > assets) | (ocf < 0)).astype(float)
    return _rolling_mean(base, 63)

def dsen_053_distress_regime_indicator_zscore_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_053_distress_regime_indicator_zscore_63d
    ECONOMIC RATIONALE: Binary flag for structural distress.
    """
    base = ((liabs > assets) | (ocf < 0)).astype(float)
    return _zscore_rolling(base, 63)

def dsen_054_distress_regime_indicator_rank_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_054_distress_regime_indicator_rank_63d
    ECONOMIC RATIONALE: Binary flag for structural distress.
    """
    base = ((liabs > assets) | (ocf < 0)).astype(float)
    return _rank_pct(base, 63)

def dsen_055_distress_regime_indicator_lvl_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_055_distress_regime_indicator_lvl_126d
    ECONOMIC RATIONALE: Binary flag for structural distress.
    """
    base = ((liabs > assets) | (ocf < 0)).astype(float)
    return _rolling_mean(base, 126)

def dsen_056_distress_regime_indicator_zscore_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_056_distress_regime_indicator_zscore_126d
    ECONOMIC RATIONALE: Binary flag for structural distress.
    """
    base = ((liabs > assets) | (ocf < 0)).astype(float)
    return _zscore_rolling(base, 126)

def dsen_057_distress_regime_indicator_rank_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_057_distress_regime_indicator_rank_126d
    ECONOMIC RATIONALE: Binary flag for structural distress.
    """
    base = ((liabs > assets) | (ocf < 0)).astype(float)
    return _rank_pct(base, 126)

def dsen_058_distress_regime_indicator_lvl_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_058_distress_regime_indicator_lvl_252d
    ECONOMIC RATIONALE: Binary flag for structural distress.
    """
    base = ((liabs > assets) | (ocf < 0)).astype(float)
    return _rolling_mean(base, 252)

def dsen_059_distress_regime_indicator_zscore_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_059_distress_regime_indicator_zscore_252d
    ECONOMIC RATIONALE: Binary flag for structural distress.
    """
    base = ((liabs > assets) | (ocf < 0)).astype(float)
    return _zscore_rolling(base, 252)

def dsen_060_distress_regime_indicator_rank_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_060_distress_regime_indicator_rank_252d
    ECONOMIC RATIONALE: Binary flag for structural distress.
    """
    base = ((liabs > assets) | (ocf < 0)).astype(float)
    return _rank_pct(base, 252)

def dsen_061_ensemble_vol_risk_lvl_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_061_ensemble_vol_risk_lvl_5d
    ECONOMIC RATIONALE: Volatility amplified by financial leverage.
    """
    base = close.rolling(21).std() * (liabs/equity.replace(0, 1e-9))
    return _rolling_mean(base, 5)

def dsen_062_ensemble_vol_risk_zscore_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_062_ensemble_vol_risk_zscore_5d
    ECONOMIC RATIONALE: Volatility amplified by financial leverage.
    """
    base = close.rolling(21).std() * (liabs/equity.replace(0, 1e-9))
    return _zscore_rolling(base, 5)

def dsen_063_ensemble_vol_risk_rank_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_063_ensemble_vol_risk_rank_5d
    ECONOMIC RATIONALE: Volatility amplified by financial leverage.
    """
    base = close.rolling(21).std() * (liabs/equity.replace(0, 1e-9))
    return _rank_pct(base, 5)

def dsen_064_ensemble_vol_risk_lvl_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_064_ensemble_vol_risk_lvl_21d
    ECONOMIC RATIONALE: Volatility amplified by financial leverage.
    """
    base = close.rolling(21).std() * (liabs/equity.replace(0, 1e-9))
    return _rolling_mean(base, 21)

def dsen_065_ensemble_vol_risk_zscore_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_065_ensemble_vol_risk_zscore_21d
    ECONOMIC RATIONALE: Volatility amplified by financial leverage.
    """
    base = close.rolling(21).std() * (liabs/equity.replace(0, 1e-9))
    return _zscore_rolling(base, 21)

def dsen_066_ensemble_vol_risk_rank_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_066_ensemble_vol_risk_rank_21d
    ECONOMIC RATIONALE: Volatility amplified by financial leverage.
    """
    base = close.rolling(21).std() * (liabs/equity.replace(0, 1e-9))
    return _rank_pct(base, 21)

def dsen_067_ensemble_vol_risk_lvl_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_067_ensemble_vol_risk_lvl_63d
    ECONOMIC RATIONALE: Volatility amplified by financial leverage.
    """
    base = close.rolling(21).std() * (liabs/equity.replace(0, 1e-9))
    return _rolling_mean(base, 63)

def dsen_068_ensemble_vol_risk_zscore_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_068_ensemble_vol_risk_zscore_63d
    ECONOMIC RATIONALE: Volatility amplified by financial leverage.
    """
    base = close.rolling(21).std() * (liabs/equity.replace(0, 1e-9))
    return _zscore_rolling(base, 63)

def dsen_069_ensemble_vol_risk_rank_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_069_ensemble_vol_risk_rank_63d
    ECONOMIC RATIONALE: Volatility amplified by financial leverage.
    """
    base = close.rolling(21).std() * (liabs/equity.replace(0, 1e-9))
    return _rank_pct(base, 63)

def dsen_070_ensemble_vol_risk_lvl_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_070_ensemble_vol_risk_lvl_126d
    ECONOMIC RATIONALE: Volatility amplified by financial leverage.
    """
    base = close.rolling(21).std() * (liabs/equity.replace(0, 1e-9))
    return _rolling_mean(base, 126)

def dsen_071_ensemble_vol_risk_zscore_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_071_ensemble_vol_risk_zscore_126d
    ECONOMIC RATIONALE: Volatility amplified by financial leverage.
    """
    base = close.rolling(21).std() * (liabs/equity.replace(0, 1e-9))
    return _zscore_rolling(base, 126)

def dsen_072_ensemble_vol_risk_rank_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_072_ensemble_vol_risk_rank_126d
    ECONOMIC RATIONALE: Volatility amplified by financial leverage.
    """
    base = close.rolling(21).std() * (liabs/equity.replace(0, 1e-9))
    return _rank_pct(base, 126)

def dsen_073_ensemble_vol_risk_lvl_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_073_ensemble_vol_risk_lvl_252d
    ECONOMIC RATIONALE: Volatility amplified by financial leverage.
    """
    base = close.rolling(21).std() * (liabs/equity.replace(0, 1e-9))
    return _rolling_mean(base, 252)

def dsen_074_ensemble_vol_risk_zscore_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_074_ensemble_vol_risk_zscore_252d
    ECONOMIC RATIONALE: Volatility amplified by financial leverage.
    """
    base = close.rolling(21).std() * (liabs/equity.replace(0, 1e-9))
    return _zscore_rolling(base, 252)

def dsen_075_ensemble_vol_risk_rank_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_075_ensemble_vol_risk_rank_252d
    ECONOMIC RATIONALE: Volatility amplified by financial leverage.
    """
    base = close.rolling(21).std() * (liabs/equity.replace(0, 1e-9))
    return _rank_pct(base, 252)

def dsen_076_multi_factor_drawdown_lvl_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_076_multi_factor_drawdown_lvl_5d
    ECONOMIC RATIONALE: Combined price and equity drawdown.
    """
    base = (close/close.rolling(252).max() - 1) + (equity/equity.rolling(252).max() - 1)
    return _rolling_mean(base, 5)

def dsen_077_multi_factor_drawdown_zscore_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_077_multi_factor_drawdown_zscore_5d
    ECONOMIC RATIONALE: Combined price and equity drawdown.
    """
    base = (close/close.rolling(252).max() - 1) + (equity/equity.rolling(252).max() - 1)
    return _zscore_rolling(base, 5)

def dsen_078_multi_factor_drawdown_rank_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_078_multi_factor_drawdown_rank_5d
    ECONOMIC RATIONALE: Combined price and equity drawdown.
    """
    base = (close/close.rolling(252).max() - 1) + (equity/equity.rolling(252).max() - 1)
    return _rank_pct(base, 5)

def dsen_079_multi_factor_drawdown_lvl_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_079_multi_factor_drawdown_lvl_21d
    ECONOMIC RATIONALE: Combined price and equity drawdown.
    """
    base = (close/close.rolling(252).max() - 1) + (equity/equity.rolling(252).max() - 1)
    return _rolling_mean(base, 21)

def dsen_080_multi_factor_drawdown_zscore_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_080_multi_factor_drawdown_zscore_21d
    ECONOMIC RATIONALE: Combined price and equity drawdown.
    """
    base = (close/close.rolling(252).max() - 1) + (equity/equity.rolling(252).max() - 1)
    return _zscore_rolling(base, 21)

def dsen_081_multi_factor_drawdown_rank_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_081_multi_factor_drawdown_rank_21d
    ECONOMIC RATIONALE: Combined price and equity drawdown.
    """
    base = (close/close.rolling(252).max() - 1) + (equity/equity.rolling(252).max() - 1)
    return _rank_pct(base, 21)

def dsen_082_multi_factor_drawdown_lvl_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_082_multi_factor_drawdown_lvl_63d
    ECONOMIC RATIONALE: Combined price and equity drawdown.
    """
    base = (close/close.rolling(252).max() - 1) + (equity/equity.rolling(252).max() - 1)
    return _rolling_mean(base, 63)

def dsen_083_multi_factor_drawdown_zscore_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_083_multi_factor_drawdown_zscore_63d
    ECONOMIC RATIONALE: Combined price and equity drawdown.
    """
    base = (close/close.rolling(252).max() - 1) + (equity/equity.rolling(252).max() - 1)
    return _zscore_rolling(base, 63)

def dsen_084_multi_factor_drawdown_rank_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_084_multi_factor_drawdown_rank_63d
    ECONOMIC RATIONALE: Combined price and equity drawdown.
    """
    base = (close/close.rolling(252).max() - 1) + (equity/equity.rolling(252).max() - 1)
    return _rank_pct(base, 63)

def dsen_085_multi_factor_drawdown_lvl_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_085_multi_factor_drawdown_lvl_126d
    ECONOMIC RATIONALE: Combined price and equity drawdown.
    """
    base = (close/close.rolling(252).max() - 1) + (equity/equity.rolling(252).max() - 1)
    return _rolling_mean(base, 126)

def dsen_086_multi_factor_drawdown_zscore_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_086_multi_factor_drawdown_zscore_126d
    ECONOMIC RATIONALE: Combined price and equity drawdown.
    """
    base = (close/close.rolling(252).max() - 1) + (equity/equity.rolling(252).max() - 1)
    return _zscore_rolling(base, 126)

def dsen_087_multi_factor_drawdown_rank_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_087_multi_factor_drawdown_rank_126d
    ECONOMIC RATIONALE: Combined price and equity drawdown.
    """
    base = (close/close.rolling(252).max() - 1) + (equity/equity.rolling(252).max() - 1)
    return _rank_pct(base, 126)

def dsen_088_multi_factor_drawdown_lvl_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_088_multi_factor_drawdown_lvl_252d
    ECONOMIC RATIONALE: Combined price and equity drawdown.
    """
    base = (close/close.rolling(252).max() - 1) + (equity/equity.rolling(252).max() - 1)
    return _rolling_mean(base, 252)

def dsen_089_multi_factor_drawdown_zscore_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_089_multi_factor_drawdown_zscore_252d
    ECONOMIC RATIONALE: Combined price and equity drawdown.
    """
    base = (close/close.rolling(252).max() - 1) + (equity/equity.rolling(252).max() - 1)
    return _zscore_rolling(base, 252)

def dsen_090_multi_factor_drawdown_rank_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_090_multi_factor_drawdown_rank_252d
    ECONOMIC RATIONALE: Combined price and equity drawdown.
    """
    base = (close/close.rolling(252).max() - 1) + (equity/equity.rolling(252).max() - 1)
    return _rank_pct(base, 252)

def dsen_091_distress_acceleration_lvl_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_091_distress_acceleration_lvl_5d
    ECONOMIC RATIONALE: Acceleration of leverage combined with price decline.
    """
    base = (liabs/equity.replace(0, 1e-9)).diff(63) + close.pct_change(63)
    return _rolling_mean(base, 5)

def dsen_092_distress_acceleration_zscore_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_092_distress_acceleration_zscore_5d
    ECONOMIC RATIONALE: Acceleration of leverage combined with price decline.
    """
    base = (liabs/equity.replace(0, 1e-9)).diff(63) + close.pct_change(63)
    return _zscore_rolling(base, 5)

def dsen_093_distress_acceleration_rank_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_093_distress_acceleration_rank_5d
    ECONOMIC RATIONALE: Acceleration of leverage combined with price decline.
    """
    base = (liabs/equity.replace(0, 1e-9)).diff(63) + close.pct_change(63)
    return _rank_pct(base, 5)

def dsen_094_distress_acceleration_lvl_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_094_distress_acceleration_lvl_21d
    ECONOMIC RATIONALE: Acceleration of leverage combined with price decline.
    """
    base = (liabs/equity.replace(0, 1e-9)).diff(63) + close.pct_change(63)
    return _rolling_mean(base, 21)

def dsen_095_distress_acceleration_zscore_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_095_distress_acceleration_zscore_21d
    ECONOMIC RATIONALE: Acceleration of leverage combined with price decline.
    """
    base = (liabs/equity.replace(0, 1e-9)).diff(63) + close.pct_change(63)
    return _zscore_rolling(base, 21)

def dsen_096_distress_acceleration_rank_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_096_distress_acceleration_rank_21d
    ECONOMIC RATIONALE: Acceleration of leverage combined with price decline.
    """
    base = (liabs/equity.replace(0, 1e-9)).diff(63) + close.pct_change(63)
    return _rank_pct(base, 21)

def dsen_097_distress_acceleration_lvl_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_097_distress_acceleration_lvl_63d
    ECONOMIC RATIONALE: Acceleration of leverage combined with price decline.
    """
    base = (liabs/equity.replace(0, 1e-9)).diff(63) + close.pct_change(63)
    return _rolling_mean(base, 63)

def dsen_098_distress_acceleration_zscore_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_098_distress_acceleration_zscore_63d
    ECONOMIC RATIONALE: Acceleration of leverage combined with price decline.
    """
    base = (liabs/equity.replace(0, 1e-9)).diff(63) + close.pct_change(63)
    return _zscore_rolling(base, 63)

def dsen_099_distress_acceleration_rank_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_099_distress_acceleration_rank_63d
    ECONOMIC RATIONALE: Acceleration of leverage combined with price decline.
    """
    base = (liabs/equity.replace(0, 1e-9)).diff(63) + close.pct_change(63)
    return _rank_pct(base, 63)

def dsen_100_distress_acceleration_lvl_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_100_distress_acceleration_lvl_126d
    ECONOMIC RATIONALE: Acceleration of leverage combined with price decline.
    """
    base = (liabs/equity.replace(0, 1e-9)).diff(63) + close.pct_change(63)
    return _rolling_mean(base, 126)

def dsen_101_distress_acceleration_zscore_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_101_distress_acceleration_zscore_126d
    ECONOMIC RATIONALE: Acceleration of leverage combined with price decline.
    """
    base = (liabs/equity.replace(0, 1e-9)).diff(63) + close.pct_change(63)
    return _zscore_rolling(base, 126)

def dsen_102_distress_acceleration_rank_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_102_distress_acceleration_rank_126d
    ECONOMIC RATIONALE: Acceleration of leverage combined with price decline.
    """
    base = (liabs/equity.replace(0, 1e-9)).diff(63) + close.pct_change(63)
    return _rank_pct(base, 126)

def dsen_103_distress_acceleration_lvl_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_103_distress_acceleration_lvl_252d
    ECONOMIC RATIONALE: Acceleration of leverage combined with price decline.
    """
    base = (liabs/equity.replace(0, 1e-9)).diff(63) + close.pct_change(63)
    return _rolling_mean(base, 252)

def dsen_104_distress_acceleration_zscore_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_104_distress_acceleration_zscore_252d
    ECONOMIC RATIONALE: Acceleration of leverage combined with price decline.
    """
    base = (liabs/equity.replace(0, 1e-9)).diff(63) + close.pct_change(63)
    return _zscore_rolling(base, 252)

def dsen_105_distress_acceleration_rank_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_105_distress_acceleration_rank_252d
    ECONOMIC RATIONALE: Acceleration of leverage combined with price decline.
    """
    base = (liabs/equity.replace(0, 1e-9)).diff(63) + close.pct_change(63)
    return _rank_pct(base, 252)

def dsen_106_solvency_quality_score_lvl_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_106_solvency_quality_score_lvl_5d
    ECONOMIC RATIONALE: Cash flow coverage of debt adjusted by equity status.
    """
    base = ocf / liabs.replace(0, 1e-9) * (equity > 0).astype(float)
    return _rolling_mean(base, 5)

def dsen_107_solvency_quality_score_zscore_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_107_solvency_quality_score_zscore_5d
    ECONOMIC RATIONALE: Cash flow coverage of debt adjusted by equity status.
    """
    base = ocf / liabs.replace(0, 1e-9) * (equity > 0).astype(float)
    return _zscore_rolling(base, 5)

def dsen_108_solvency_quality_score_rank_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_108_solvency_quality_score_rank_5d
    ECONOMIC RATIONALE: Cash flow coverage of debt adjusted by equity status.
    """
    base = ocf / liabs.replace(0, 1e-9) * (equity > 0).astype(float)
    return _rank_pct(base, 5)

def dsen_109_solvency_quality_score_lvl_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_109_solvency_quality_score_lvl_21d
    ECONOMIC RATIONALE: Cash flow coverage of debt adjusted by equity status.
    """
    base = ocf / liabs.replace(0, 1e-9) * (equity > 0).astype(float)
    return _rolling_mean(base, 21)

def dsen_110_solvency_quality_score_zscore_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_110_solvency_quality_score_zscore_21d
    ECONOMIC RATIONALE: Cash flow coverage of debt adjusted by equity status.
    """
    base = ocf / liabs.replace(0, 1e-9) * (equity > 0).astype(float)
    return _zscore_rolling(base, 21)

def dsen_111_solvency_quality_score_rank_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_111_solvency_quality_score_rank_21d
    ECONOMIC RATIONALE: Cash flow coverage of debt adjusted by equity status.
    """
    base = ocf / liabs.replace(0, 1e-9) * (equity > 0).astype(float)
    return _rank_pct(base, 21)

def dsen_112_solvency_quality_score_lvl_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_112_solvency_quality_score_lvl_63d
    ECONOMIC RATIONALE: Cash flow coverage of debt adjusted by equity status.
    """
    base = ocf / liabs.replace(0, 1e-9) * (equity > 0).astype(float)
    return _rolling_mean(base, 63)

def dsen_113_solvency_quality_score_zscore_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_113_solvency_quality_score_zscore_63d
    ECONOMIC RATIONALE: Cash flow coverage of debt adjusted by equity status.
    """
    base = ocf / liabs.replace(0, 1e-9) * (equity > 0).astype(float)
    return _zscore_rolling(base, 63)

def dsen_114_solvency_quality_score_rank_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_114_solvency_quality_score_rank_63d
    ECONOMIC RATIONALE: Cash flow coverage of debt adjusted by equity status.
    """
    base = ocf / liabs.replace(0, 1e-9) * (equity > 0).astype(float)
    return _rank_pct(base, 63)

def dsen_115_solvency_quality_score_lvl_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_115_solvency_quality_score_lvl_126d
    ECONOMIC RATIONALE: Cash flow coverage of debt adjusted by equity status.
    """
    base = ocf / liabs.replace(0, 1e-9) * (equity > 0).astype(float)
    return _rolling_mean(base, 126)

def dsen_116_solvency_quality_score_zscore_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_116_solvency_quality_score_zscore_126d
    ECONOMIC RATIONALE: Cash flow coverage of debt adjusted by equity status.
    """
    base = ocf / liabs.replace(0, 1e-9) * (equity > 0).astype(float)
    return _zscore_rolling(base, 126)

def dsen_117_solvency_quality_score_rank_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_117_solvency_quality_score_rank_126d
    ECONOMIC RATIONALE: Cash flow coverage of debt adjusted by equity status.
    """
    base = ocf / liabs.replace(0, 1e-9) * (equity > 0).astype(float)
    return _rank_pct(base, 126)

def dsen_118_solvency_quality_score_lvl_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_118_solvency_quality_score_lvl_252d
    ECONOMIC RATIONALE: Cash flow coverage of debt adjusted by equity status.
    """
    base = ocf / liabs.replace(0, 1e-9) * (equity > 0).astype(float)
    return _rolling_mean(base, 252)

def dsen_119_solvency_quality_score_zscore_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_119_solvency_quality_score_zscore_252d
    ECONOMIC RATIONALE: Cash flow coverage of debt adjusted by equity status.
    """
    base = ocf / liabs.replace(0, 1e-9) * (equity > 0).astype(float)
    return _zscore_rolling(base, 252)

def dsen_120_solvency_quality_score_rank_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_120_solvency_quality_score_rank_252d
    ECONOMIC RATIONALE: Cash flow coverage of debt adjusted by equity status.
    """
    base = ocf / liabs.replace(0, 1e-9) * (equity > 0).astype(float)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V121_REGISTRY_1 = {
    "dsen_001_composite_distress_z_lvl_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_001_composite_distress_z_lvl_5d},
    "dsen_002_composite_distress_z_zscore_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_002_composite_distress_z_zscore_5d},
    "dsen_003_composite_distress_z_rank_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_003_composite_distress_z_rank_5d},
    "dsen_004_composite_distress_z_lvl_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_004_composite_distress_z_lvl_21d},
    "dsen_005_composite_distress_z_zscore_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_005_composite_distress_z_zscore_21d},
    "dsen_006_composite_distress_z_rank_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_006_composite_distress_z_rank_21d},
    "dsen_007_composite_distress_z_lvl_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_007_composite_distress_z_lvl_63d},
    "dsen_008_composite_distress_z_zscore_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_008_composite_distress_z_zscore_63d},
    "dsen_009_composite_distress_z_rank_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_009_composite_distress_z_rank_63d},
    "dsen_010_composite_distress_z_lvl_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_010_composite_distress_z_lvl_126d},
    "dsen_011_composite_distress_z_zscore_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_011_composite_distress_z_zscore_126d},
    "dsen_012_composite_distress_z_rank_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_012_composite_distress_z_rank_126d},
    "dsen_013_composite_distress_z_lvl_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_013_composite_distress_z_lvl_252d},
    "dsen_014_composite_distress_z_zscore_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_014_composite_distress_z_zscore_252d},
    "dsen_015_composite_distress_z_rank_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_015_composite_distress_z_rank_252d},
    "dsen_016_valuation_solvency_blend_lvl_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_016_valuation_solvency_blend_lvl_5d},
    "dsen_017_valuation_solvency_blend_zscore_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_017_valuation_solvency_blend_zscore_5d},
    "dsen_018_valuation_solvency_blend_rank_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_018_valuation_solvency_blend_rank_5d},
    "dsen_019_valuation_solvency_blend_lvl_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_019_valuation_solvency_blend_lvl_21d},
    "dsen_020_valuation_solvency_blend_zscore_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_020_valuation_solvency_blend_zscore_21d},
    "dsen_021_valuation_solvency_blend_rank_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_021_valuation_solvency_blend_rank_21d},
    "dsen_022_valuation_solvency_blend_lvl_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_022_valuation_solvency_blend_lvl_63d},
    "dsen_023_valuation_solvency_blend_zscore_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_023_valuation_solvency_blend_zscore_63d},
    "dsen_024_valuation_solvency_blend_rank_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_024_valuation_solvency_blend_rank_63d},
    "dsen_025_valuation_solvency_blend_lvl_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_025_valuation_solvency_blend_lvl_126d},
    "dsen_026_valuation_solvency_blend_zscore_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_026_valuation_solvency_blend_zscore_126d},
    "dsen_027_valuation_solvency_blend_rank_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_027_valuation_solvency_blend_rank_126d},
    "dsen_028_valuation_solvency_blend_lvl_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_028_valuation_solvency_blend_lvl_252d},
    "dsen_029_valuation_solvency_blend_zscore_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_029_valuation_solvency_blend_zscore_252d},
    "dsen_030_valuation_solvency_blend_rank_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_030_valuation_solvency_blend_rank_252d},
    "dsen_031_liquidity_momentum_ensemble_lvl_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_031_liquidity_momentum_ensemble_lvl_5d},
    "dsen_032_liquidity_momentum_ensemble_zscore_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_032_liquidity_momentum_ensemble_zscore_5d},
    "dsen_033_liquidity_momentum_ensemble_rank_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_033_liquidity_momentum_ensemble_rank_5d},
    "dsen_034_liquidity_momentum_ensemble_lvl_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_034_liquidity_momentum_ensemble_lvl_21d},
    "dsen_035_liquidity_momentum_ensemble_zscore_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_035_liquidity_momentum_ensemble_zscore_21d},
    "dsen_036_liquidity_momentum_ensemble_rank_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_036_liquidity_momentum_ensemble_rank_21d},
    "dsen_037_liquidity_momentum_ensemble_lvl_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_037_liquidity_momentum_ensemble_lvl_63d},
    "dsen_038_liquidity_momentum_ensemble_zscore_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_038_liquidity_momentum_ensemble_zscore_63d},
    "dsen_039_liquidity_momentum_ensemble_rank_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_039_liquidity_momentum_ensemble_rank_63d},
    "dsen_040_liquidity_momentum_ensemble_lvl_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_040_liquidity_momentum_ensemble_lvl_126d},
    "dsen_041_liquidity_momentum_ensemble_zscore_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_041_liquidity_momentum_ensemble_zscore_126d},
    "dsen_042_liquidity_momentum_ensemble_rank_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_042_liquidity_momentum_ensemble_rank_126d},
    "dsen_043_liquidity_momentum_ensemble_lvl_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_043_liquidity_momentum_ensemble_lvl_252d},
    "dsen_044_liquidity_momentum_ensemble_zscore_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_044_liquidity_momentum_ensemble_zscore_252d},
    "dsen_045_liquidity_momentum_ensemble_rank_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_045_liquidity_momentum_ensemble_rank_252d},
    "dsen_046_distress_regime_indicator_lvl_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_046_distress_regime_indicator_lvl_5d},
    "dsen_047_distress_regime_indicator_zscore_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_047_distress_regime_indicator_zscore_5d},
    "dsen_048_distress_regime_indicator_rank_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_048_distress_regime_indicator_rank_5d},
    "dsen_049_distress_regime_indicator_lvl_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_049_distress_regime_indicator_lvl_21d},
    "dsen_050_distress_regime_indicator_zscore_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_050_distress_regime_indicator_zscore_21d},
    "dsen_051_distress_regime_indicator_rank_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_051_distress_regime_indicator_rank_21d},
    "dsen_052_distress_regime_indicator_lvl_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_052_distress_regime_indicator_lvl_63d},
    "dsen_053_distress_regime_indicator_zscore_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_053_distress_regime_indicator_zscore_63d},
    "dsen_054_distress_regime_indicator_rank_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_054_distress_regime_indicator_rank_63d},
    "dsen_055_distress_regime_indicator_lvl_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_055_distress_regime_indicator_lvl_126d},
    "dsen_056_distress_regime_indicator_zscore_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_056_distress_regime_indicator_zscore_126d},
    "dsen_057_distress_regime_indicator_rank_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_057_distress_regime_indicator_rank_126d},
    "dsen_058_distress_regime_indicator_lvl_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_058_distress_regime_indicator_lvl_252d},
    "dsen_059_distress_regime_indicator_zscore_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_059_distress_regime_indicator_zscore_252d},
    "dsen_060_distress_regime_indicator_rank_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_060_distress_regime_indicator_rank_252d},
    "dsen_061_ensemble_vol_risk_lvl_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_061_ensemble_vol_risk_lvl_5d},
    "dsen_062_ensemble_vol_risk_zscore_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_062_ensemble_vol_risk_zscore_5d},
    "dsen_063_ensemble_vol_risk_rank_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_063_ensemble_vol_risk_rank_5d},
    "dsen_064_ensemble_vol_risk_lvl_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_064_ensemble_vol_risk_lvl_21d},
    "dsen_065_ensemble_vol_risk_zscore_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_065_ensemble_vol_risk_zscore_21d},
    "dsen_066_ensemble_vol_risk_rank_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_066_ensemble_vol_risk_rank_21d},
    "dsen_067_ensemble_vol_risk_lvl_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_067_ensemble_vol_risk_lvl_63d},
    "dsen_068_ensemble_vol_risk_zscore_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_068_ensemble_vol_risk_zscore_63d},
    "dsen_069_ensemble_vol_risk_rank_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_069_ensemble_vol_risk_rank_63d},
    "dsen_070_ensemble_vol_risk_lvl_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_070_ensemble_vol_risk_lvl_126d},
    "dsen_071_ensemble_vol_risk_zscore_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_071_ensemble_vol_risk_zscore_126d},
    "dsen_072_ensemble_vol_risk_rank_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_072_ensemble_vol_risk_rank_126d},
    "dsen_073_ensemble_vol_risk_lvl_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_073_ensemble_vol_risk_lvl_252d},
    "dsen_074_ensemble_vol_risk_zscore_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_074_ensemble_vol_risk_zscore_252d},
    "dsen_075_ensemble_vol_risk_rank_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_075_ensemble_vol_risk_rank_252d},
    "dsen_076_multi_factor_drawdown_lvl_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_076_multi_factor_drawdown_lvl_5d},
    "dsen_077_multi_factor_drawdown_zscore_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_077_multi_factor_drawdown_zscore_5d},
    "dsen_078_multi_factor_drawdown_rank_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_078_multi_factor_drawdown_rank_5d},
    "dsen_079_multi_factor_drawdown_lvl_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_079_multi_factor_drawdown_lvl_21d},
    "dsen_080_multi_factor_drawdown_zscore_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_080_multi_factor_drawdown_zscore_21d},
    "dsen_081_multi_factor_drawdown_rank_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_081_multi_factor_drawdown_rank_21d},
    "dsen_082_multi_factor_drawdown_lvl_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_082_multi_factor_drawdown_lvl_63d},
    "dsen_083_multi_factor_drawdown_zscore_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_083_multi_factor_drawdown_zscore_63d},
    "dsen_084_multi_factor_drawdown_rank_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_084_multi_factor_drawdown_rank_63d},
    "dsen_085_multi_factor_drawdown_lvl_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_085_multi_factor_drawdown_lvl_126d},
    "dsen_086_multi_factor_drawdown_zscore_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_086_multi_factor_drawdown_zscore_126d},
    "dsen_087_multi_factor_drawdown_rank_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_087_multi_factor_drawdown_rank_126d},
    "dsen_088_multi_factor_drawdown_lvl_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_088_multi_factor_drawdown_lvl_252d},
    "dsen_089_multi_factor_drawdown_zscore_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_089_multi_factor_drawdown_zscore_252d},
    "dsen_090_multi_factor_drawdown_rank_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_090_multi_factor_drawdown_rank_252d},
    "dsen_091_distress_acceleration_lvl_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_091_distress_acceleration_lvl_5d},
    "dsen_092_distress_acceleration_zscore_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_092_distress_acceleration_zscore_5d},
    "dsen_093_distress_acceleration_rank_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_093_distress_acceleration_rank_5d},
    "dsen_094_distress_acceleration_lvl_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_094_distress_acceleration_lvl_21d},
    "dsen_095_distress_acceleration_zscore_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_095_distress_acceleration_zscore_21d},
    "dsen_096_distress_acceleration_rank_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_096_distress_acceleration_rank_21d},
    "dsen_097_distress_acceleration_lvl_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_097_distress_acceleration_lvl_63d},
    "dsen_098_distress_acceleration_zscore_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_098_distress_acceleration_zscore_63d},
    "dsen_099_distress_acceleration_rank_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_099_distress_acceleration_rank_63d},
    "dsen_100_distress_acceleration_lvl_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_100_distress_acceleration_lvl_126d},
    "dsen_101_distress_acceleration_zscore_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_101_distress_acceleration_zscore_126d},
    "dsen_102_distress_acceleration_rank_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_102_distress_acceleration_rank_126d},
    "dsen_103_distress_acceleration_lvl_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_103_distress_acceleration_lvl_252d},
    "dsen_104_distress_acceleration_zscore_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_104_distress_acceleration_zscore_252d},
    "dsen_105_distress_acceleration_rank_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_105_distress_acceleration_rank_252d},
    "dsen_106_solvency_quality_score_lvl_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_106_solvency_quality_score_lvl_5d},
    "dsen_107_solvency_quality_score_zscore_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_107_solvency_quality_score_zscore_5d},
    "dsen_108_solvency_quality_score_rank_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_108_solvency_quality_score_rank_5d},
    "dsen_109_solvency_quality_score_lvl_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_109_solvency_quality_score_lvl_21d},
    "dsen_110_solvency_quality_score_zscore_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_110_solvency_quality_score_zscore_21d},
    "dsen_111_solvency_quality_score_rank_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_111_solvency_quality_score_rank_21d},
    "dsen_112_solvency_quality_score_lvl_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_112_solvency_quality_score_lvl_63d},
    "dsen_113_solvency_quality_score_zscore_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_113_solvency_quality_score_zscore_63d},
    "dsen_114_solvency_quality_score_rank_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_114_solvency_quality_score_rank_63d},
    "dsen_115_solvency_quality_score_lvl_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_115_solvency_quality_score_lvl_126d},
    "dsen_116_solvency_quality_score_zscore_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_116_solvency_quality_score_zscore_126d},
    "dsen_117_solvency_quality_score_rank_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_117_solvency_quality_score_rank_126d},
    "dsen_118_solvency_quality_score_lvl_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_118_solvency_quality_score_lvl_252d},
    "dsen_119_solvency_quality_score_zscore_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_119_solvency_quality_score_zscore_252d},
    "dsen_120_solvency_quality_score_rank_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_120_solvency_quality_score_rank_252d},
}
