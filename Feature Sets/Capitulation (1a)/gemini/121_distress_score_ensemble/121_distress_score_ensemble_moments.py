"""
121_distress_score_ensemble — Statistical Moments
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

def dsen_376_composite_distress_z_skew_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_376_composite_distress_z_skew_5d
    ECONOMIC RATIONALE: Skewness of composite_distress_z over 5d. Combined leverage and cash flow distress.
    """
    return (_zscore_rolling(liabs/equity.replace(0, 1e-9) + (ocf < 0).astype(float), 252)).rolling(5).skew()

def dsen_377_composite_distress_z_kurt_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_377_composite_distress_z_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of composite_distress_z over 5d. Combined leverage and cash flow distress.
    """
    return (_zscore_rolling(liabs/equity.replace(0, 1e-9) + (ocf < 0).astype(float), 252)).rolling(5).kurt()

def dsen_378_composite_distress_z_skew_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_378_composite_distress_z_skew_21d
    ECONOMIC RATIONALE: Skewness of composite_distress_z over 21d. Combined leverage and cash flow distress.
    """
    return (_zscore_rolling(liabs/equity.replace(0, 1e-9) + (ocf < 0).astype(float), 252)).rolling(21).skew()

def dsen_379_composite_distress_z_kurt_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_379_composite_distress_z_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of composite_distress_z over 21d. Combined leverage and cash flow distress.
    """
    return (_zscore_rolling(liabs/equity.replace(0, 1e-9) + (ocf < 0).astype(float), 252)).rolling(21).kurt()

def dsen_380_composite_distress_z_skew_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_380_composite_distress_z_skew_63d
    ECONOMIC RATIONALE: Skewness of composite_distress_z over 63d. Combined leverage and cash flow distress.
    """
    return (_zscore_rolling(liabs/equity.replace(0, 1e-9) + (ocf < 0).astype(float), 252)).rolling(63).skew()

def dsen_381_composite_distress_z_kurt_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_381_composite_distress_z_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of composite_distress_z over 63d. Combined leverage and cash flow distress.
    """
    return (_zscore_rolling(liabs/equity.replace(0, 1e-9) + (ocf < 0).astype(float), 252)).rolling(63).kurt()

def dsen_382_composite_distress_z_skew_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_382_composite_distress_z_skew_126d
    ECONOMIC RATIONALE: Skewness of composite_distress_z over 126d. Combined leverage and cash flow distress.
    """
    return (_zscore_rolling(liabs/equity.replace(0, 1e-9) + (ocf < 0).astype(float), 252)).rolling(126).skew()

def dsen_383_composite_distress_z_kurt_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_383_composite_distress_z_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of composite_distress_z over 126d. Combined leverage and cash flow distress.
    """
    return (_zscore_rolling(liabs/equity.replace(0, 1e-9) + (ocf < 0).astype(float), 252)).rolling(126).kurt()

def dsen_384_composite_distress_z_skew_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_384_composite_distress_z_skew_252d
    ECONOMIC RATIONALE: Skewness of composite_distress_z over 252d. Combined leverage and cash flow distress.
    """
    return (_zscore_rolling(liabs/equity.replace(0, 1e-9) + (ocf < 0).astype(float), 252)).rolling(252).skew()

def dsen_385_composite_distress_z_kurt_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_385_composite_distress_z_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of composite_distress_z over 252d. Combined leverage and cash flow distress.
    """
    return (_zscore_rolling(liabs/equity.replace(0, 1e-9) + (ocf < 0).astype(float), 252)).rolling(252).kurt()

def dsen_386_valuation_solvency_blend_skew_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_386_valuation_solvency_blend_skew_5d
    ECONOMIC RATIONALE: Skewness of valuation_solvency_blend over 5d. Valuation drawdown weighted by solvency.
    """
    return ((close/close.rolling(252).max()) * (equity/liabs.replace(0, 1e-9))).rolling(5).skew()

def dsen_387_valuation_solvency_blend_kurt_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_387_valuation_solvency_blend_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of valuation_solvency_blend over 5d. Valuation drawdown weighted by solvency.
    """
    return ((close/close.rolling(252).max()) * (equity/liabs.replace(0, 1e-9))).rolling(5).kurt()

def dsen_388_valuation_solvency_blend_skew_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_388_valuation_solvency_blend_skew_21d
    ECONOMIC RATIONALE: Skewness of valuation_solvency_blend over 21d. Valuation drawdown weighted by solvency.
    """
    return ((close/close.rolling(252).max()) * (equity/liabs.replace(0, 1e-9))).rolling(21).skew()

def dsen_389_valuation_solvency_blend_kurt_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_389_valuation_solvency_blend_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of valuation_solvency_blend over 21d. Valuation drawdown weighted by solvency.
    """
    return ((close/close.rolling(252).max()) * (equity/liabs.replace(0, 1e-9))).rolling(21).kurt()

def dsen_390_valuation_solvency_blend_skew_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_390_valuation_solvency_blend_skew_63d
    ECONOMIC RATIONALE: Skewness of valuation_solvency_blend over 63d. Valuation drawdown weighted by solvency.
    """
    return ((close/close.rolling(252).max()) * (equity/liabs.replace(0, 1e-9))).rolling(63).skew()

def dsen_391_valuation_solvency_blend_kurt_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_391_valuation_solvency_blend_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of valuation_solvency_blend over 63d. Valuation drawdown weighted by solvency.
    """
    return ((close/close.rolling(252).max()) * (equity/liabs.replace(0, 1e-9))).rolling(63).kurt()

def dsen_392_valuation_solvency_blend_skew_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_392_valuation_solvency_blend_skew_126d
    ECONOMIC RATIONALE: Skewness of valuation_solvency_blend over 126d. Valuation drawdown weighted by solvency.
    """
    return ((close/close.rolling(252).max()) * (equity/liabs.replace(0, 1e-9))).rolling(126).skew()

def dsen_393_valuation_solvency_blend_kurt_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_393_valuation_solvency_blend_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of valuation_solvency_blend over 126d. Valuation drawdown weighted by solvency.
    """
    return ((close/close.rolling(252).max()) * (equity/liabs.replace(0, 1e-9))).rolling(126).kurt()

def dsen_394_valuation_solvency_blend_skew_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_394_valuation_solvency_blend_skew_252d
    ECONOMIC RATIONALE: Skewness of valuation_solvency_blend over 252d. Valuation drawdown weighted by solvency.
    """
    return ((close/close.rolling(252).max()) * (equity/liabs.replace(0, 1e-9))).rolling(252).skew()

def dsen_395_valuation_solvency_blend_kurt_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_395_valuation_solvency_blend_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of valuation_solvency_blend over 252d. Valuation drawdown weighted by solvency.
    """
    return ((close/close.rolling(252).max()) * (equity/liabs.replace(0, 1e-9))).rolling(252).kurt()

def dsen_396_liquidity_momentum_ensemble_skew_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_396_liquidity_momentum_ensemble_skew_5d
    ECONOMIC RATIONALE: Skewness of liquidity_momentum_ensemble over 5d. Combined fundamental and price momentum.
    """
    return (ocf.pct_change(63) + close.pct_change(63)).rolling(5).skew()

def dsen_397_liquidity_momentum_ensemble_kurt_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_397_liquidity_momentum_ensemble_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of liquidity_momentum_ensemble over 5d. Combined fundamental and price momentum.
    """
    return (ocf.pct_change(63) + close.pct_change(63)).rolling(5).kurt()

def dsen_398_liquidity_momentum_ensemble_skew_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_398_liquidity_momentum_ensemble_skew_21d
    ECONOMIC RATIONALE: Skewness of liquidity_momentum_ensemble over 21d. Combined fundamental and price momentum.
    """
    return (ocf.pct_change(63) + close.pct_change(63)).rolling(21).skew()

def dsen_399_liquidity_momentum_ensemble_kurt_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_399_liquidity_momentum_ensemble_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of liquidity_momentum_ensemble over 21d. Combined fundamental and price momentum.
    """
    return (ocf.pct_change(63) + close.pct_change(63)).rolling(21).kurt()

def dsen_400_liquidity_momentum_ensemble_skew_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_400_liquidity_momentum_ensemble_skew_63d
    ECONOMIC RATIONALE: Skewness of liquidity_momentum_ensemble over 63d. Combined fundamental and price momentum.
    """
    return (ocf.pct_change(63) + close.pct_change(63)).rolling(63).skew()

def dsen_401_liquidity_momentum_ensemble_kurt_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_401_liquidity_momentum_ensemble_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of liquidity_momentum_ensemble over 63d. Combined fundamental and price momentum.
    """
    return (ocf.pct_change(63) + close.pct_change(63)).rolling(63).kurt()

def dsen_402_liquidity_momentum_ensemble_skew_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_402_liquidity_momentum_ensemble_skew_126d
    ECONOMIC RATIONALE: Skewness of liquidity_momentum_ensemble over 126d. Combined fundamental and price momentum.
    """
    return (ocf.pct_change(63) + close.pct_change(63)).rolling(126).skew()

def dsen_403_liquidity_momentum_ensemble_kurt_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_403_liquidity_momentum_ensemble_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of liquidity_momentum_ensemble over 126d. Combined fundamental and price momentum.
    """
    return (ocf.pct_change(63) + close.pct_change(63)).rolling(126).kurt()

def dsen_404_liquidity_momentum_ensemble_skew_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_404_liquidity_momentum_ensemble_skew_252d
    ECONOMIC RATIONALE: Skewness of liquidity_momentum_ensemble over 252d. Combined fundamental and price momentum.
    """
    return (ocf.pct_change(63) + close.pct_change(63)).rolling(252).skew()

def dsen_405_liquidity_momentum_ensemble_kurt_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_405_liquidity_momentum_ensemble_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of liquidity_momentum_ensemble over 252d. Combined fundamental and price momentum.
    """
    return (ocf.pct_change(63) + close.pct_change(63)).rolling(252).kurt()

def dsen_406_distress_regime_indicator_skew_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_406_distress_regime_indicator_skew_5d
    ECONOMIC RATIONALE: Skewness of distress_regime_indicator over 5d. Binary flag for structural distress.
    """
    return (((liabs > assets) | (ocf < 0)).astype(float)).rolling(5).skew()

def dsen_407_distress_regime_indicator_kurt_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_407_distress_regime_indicator_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of distress_regime_indicator over 5d. Binary flag for structural distress.
    """
    return (((liabs > assets) | (ocf < 0)).astype(float)).rolling(5).kurt()

def dsen_408_distress_regime_indicator_skew_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_408_distress_regime_indicator_skew_21d
    ECONOMIC RATIONALE: Skewness of distress_regime_indicator over 21d. Binary flag for structural distress.
    """
    return (((liabs > assets) | (ocf < 0)).astype(float)).rolling(21).skew()

def dsen_409_distress_regime_indicator_kurt_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_409_distress_regime_indicator_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of distress_regime_indicator over 21d. Binary flag for structural distress.
    """
    return (((liabs > assets) | (ocf < 0)).astype(float)).rolling(21).kurt()

def dsen_410_distress_regime_indicator_skew_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_410_distress_regime_indicator_skew_63d
    ECONOMIC RATIONALE: Skewness of distress_regime_indicator over 63d. Binary flag for structural distress.
    """
    return (((liabs > assets) | (ocf < 0)).astype(float)).rolling(63).skew()

def dsen_411_distress_regime_indicator_kurt_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_411_distress_regime_indicator_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of distress_regime_indicator over 63d. Binary flag for structural distress.
    """
    return (((liabs > assets) | (ocf < 0)).astype(float)).rolling(63).kurt()

def dsen_412_distress_regime_indicator_skew_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_412_distress_regime_indicator_skew_126d
    ECONOMIC RATIONALE: Skewness of distress_regime_indicator over 126d. Binary flag for structural distress.
    """
    return (((liabs > assets) | (ocf < 0)).astype(float)).rolling(126).skew()

def dsen_413_distress_regime_indicator_kurt_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_413_distress_regime_indicator_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of distress_regime_indicator over 126d. Binary flag for structural distress.
    """
    return (((liabs > assets) | (ocf < 0)).astype(float)).rolling(126).kurt()

def dsen_414_distress_regime_indicator_skew_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_414_distress_regime_indicator_skew_252d
    ECONOMIC RATIONALE: Skewness of distress_regime_indicator over 252d. Binary flag for structural distress.
    """
    return (((liabs > assets) | (ocf < 0)).astype(float)).rolling(252).skew()

def dsen_415_distress_regime_indicator_kurt_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_415_distress_regime_indicator_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of distress_regime_indicator over 252d. Binary flag for structural distress.
    """
    return (((liabs > assets) | (ocf < 0)).astype(float)).rolling(252).kurt()

def dsen_416_ensemble_vol_risk_skew_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_416_ensemble_vol_risk_skew_5d
    ECONOMIC RATIONALE: Skewness of ensemble_vol_risk over 5d. Volatility amplified by financial leverage.
    """
    return (close.rolling(21).std() * (liabs/equity.replace(0, 1e-9))).rolling(5).skew()

def dsen_417_ensemble_vol_risk_kurt_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_417_ensemble_vol_risk_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of ensemble_vol_risk over 5d. Volatility amplified by financial leverage.
    """
    return (close.rolling(21).std() * (liabs/equity.replace(0, 1e-9))).rolling(5).kurt()

def dsen_418_ensemble_vol_risk_skew_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_418_ensemble_vol_risk_skew_21d
    ECONOMIC RATIONALE: Skewness of ensemble_vol_risk over 21d. Volatility amplified by financial leverage.
    """
    return (close.rolling(21).std() * (liabs/equity.replace(0, 1e-9))).rolling(21).skew()

def dsen_419_ensemble_vol_risk_kurt_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_419_ensemble_vol_risk_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of ensemble_vol_risk over 21d. Volatility amplified by financial leverage.
    """
    return (close.rolling(21).std() * (liabs/equity.replace(0, 1e-9))).rolling(21).kurt()

def dsen_420_ensemble_vol_risk_skew_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_420_ensemble_vol_risk_skew_63d
    ECONOMIC RATIONALE: Skewness of ensemble_vol_risk over 63d. Volatility amplified by financial leverage.
    """
    return (close.rolling(21).std() * (liabs/equity.replace(0, 1e-9))).rolling(63).skew()

def dsen_421_ensemble_vol_risk_kurt_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_421_ensemble_vol_risk_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of ensemble_vol_risk over 63d. Volatility amplified by financial leverage.
    """
    return (close.rolling(21).std() * (liabs/equity.replace(0, 1e-9))).rolling(63).kurt()

def dsen_422_ensemble_vol_risk_skew_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_422_ensemble_vol_risk_skew_126d
    ECONOMIC RATIONALE: Skewness of ensemble_vol_risk over 126d. Volatility amplified by financial leverage.
    """
    return (close.rolling(21).std() * (liabs/equity.replace(0, 1e-9))).rolling(126).skew()

def dsen_423_ensemble_vol_risk_kurt_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_423_ensemble_vol_risk_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of ensemble_vol_risk over 126d. Volatility amplified by financial leverage.
    """
    return (close.rolling(21).std() * (liabs/equity.replace(0, 1e-9))).rolling(126).kurt()

def dsen_424_ensemble_vol_risk_skew_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_424_ensemble_vol_risk_skew_252d
    ECONOMIC RATIONALE: Skewness of ensemble_vol_risk over 252d. Volatility amplified by financial leverage.
    """
    return (close.rolling(21).std() * (liabs/equity.replace(0, 1e-9))).rolling(252).skew()

def dsen_425_ensemble_vol_risk_kurt_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_425_ensemble_vol_risk_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of ensemble_vol_risk over 252d. Volatility amplified by financial leverage.
    """
    return (close.rolling(21).std() * (liabs/equity.replace(0, 1e-9))).rolling(252).kurt()

def dsen_426_multi_factor_drawdown_skew_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_426_multi_factor_drawdown_skew_5d
    ECONOMIC RATIONALE: Skewness of multi_factor_drawdown over 5d. Combined price and equity drawdown.
    """
    return ((close/close.rolling(252).max() - 1) + (equity/equity.rolling(252).max() - 1)).rolling(5).skew()

def dsen_427_multi_factor_drawdown_kurt_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_427_multi_factor_drawdown_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of multi_factor_drawdown over 5d. Combined price and equity drawdown.
    """
    return ((close/close.rolling(252).max() - 1) + (equity/equity.rolling(252).max() - 1)).rolling(5).kurt()

def dsen_428_multi_factor_drawdown_skew_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_428_multi_factor_drawdown_skew_21d
    ECONOMIC RATIONALE: Skewness of multi_factor_drawdown over 21d. Combined price and equity drawdown.
    """
    return ((close/close.rolling(252).max() - 1) + (equity/equity.rolling(252).max() - 1)).rolling(21).skew()

def dsen_429_multi_factor_drawdown_kurt_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_429_multi_factor_drawdown_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of multi_factor_drawdown over 21d. Combined price and equity drawdown.
    """
    return ((close/close.rolling(252).max() - 1) + (equity/equity.rolling(252).max() - 1)).rolling(21).kurt()

def dsen_430_multi_factor_drawdown_skew_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_430_multi_factor_drawdown_skew_63d
    ECONOMIC RATIONALE: Skewness of multi_factor_drawdown over 63d. Combined price and equity drawdown.
    """
    return ((close/close.rolling(252).max() - 1) + (equity/equity.rolling(252).max() - 1)).rolling(63).skew()

def dsen_431_multi_factor_drawdown_kurt_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_431_multi_factor_drawdown_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of multi_factor_drawdown over 63d. Combined price and equity drawdown.
    """
    return ((close/close.rolling(252).max() - 1) + (equity/equity.rolling(252).max() - 1)).rolling(63).kurt()

def dsen_432_multi_factor_drawdown_skew_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_432_multi_factor_drawdown_skew_126d
    ECONOMIC RATIONALE: Skewness of multi_factor_drawdown over 126d. Combined price and equity drawdown.
    """
    return ((close/close.rolling(252).max() - 1) + (equity/equity.rolling(252).max() - 1)).rolling(126).skew()

def dsen_433_multi_factor_drawdown_kurt_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_433_multi_factor_drawdown_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of multi_factor_drawdown over 126d. Combined price and equity drawdown.
    """
    return ((close/close.rolling(252).max() - 1) + (equity/equity.rolling(252).max() - 1)).rolling(126).kurt()

def dsen_434_multi_factor_drawdown_skew_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_434_multi_factor_drawdown_skew_252d
    ECONOMIC RATIONALE: Skewness of multi_factor_drawdown over 252d. Combined price and equity drawdown.
    """
    return ((close/close.rolling(252).max() - 1) + (equity/equity.rolling(252).max() - 1)).rolling(252).skew()

def dsen_435_multi_factor_drawdown_kurt_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_435_multi_factor_drawdown_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of multi_factor_drawdown over 252d. Combined price and equity drawdown.
    """
    return ((close/close.rolling(252).max() - 1) + (equity/equity.rolling(252).max() - 1)).rolling(252).kurt()

def dsen_436_distress_acceleration_skew_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_436_distress_acceleration_skew_5d
    ECONOMIC RATIONALE: Skewness of distress_acceleration over 5d. Acceleration of leverage combined with price decline.
    """
    return ((liabs/equity.replace(0, 1e-9)).diff(63) + close.pct_change(63)).rolling(5).skew()

def dsen_437_distress_acceleration_kurt_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_437_distress_acceleration_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of distress_acceleration over 5d. Acceleration of leverage combined with price decline.
    """
    return ((liabs/equity.replace(0, 1e-9)).diff(63) + close.pct_change(63)).rolling(5).kurt()

def dsen_438_distress_acceleration_skew_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_438_distress_acceleration_skew_21d
    ECONOMIC RATIONALE: Skewness of distress_acceleration over 21d. Acceleration of leverage combined with price decline.
    """
    return ((liabs/equity.replace(0, 1e-9)).diff(63) + close.pct_change(63)).rolling(21).skew()

def dsen_439_distress_acceleration_kurt_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_439_distress_acceleration_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of distress_acceleration over 21d. Acceleration of leverage combined with price decline.
    """
    return ((liabs/equity.replace(0, 1e-9)).diff(63) + close.pct_change(63)).rolling(21).kurt()

def dsen_440_distress_acceleration_skew_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_440_distress_acceleration_skew_63d
    ECONOMIC RATIONALE: Skewness of distress_acceleration over 63d. Acceleration of leverage combined with price decline.
    """
    return ((liabs/equity.replace(0, 1e-9)).diff(63) + close.pct_change(63)).rolling(63).skew()

def dsen_441_distress_acceleration_kurt_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_441_distress_acceleration_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of distress_acceleration over 63d. Acceleration of leverage combined with price decline.
    """
    return ((liabs/equity.replace(0, 1e-9)).diff(63) + close.pct_change(63)).rolling(63).kurt()

def dsen_442_distress_acceleration_skew_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_442_distress_acceleration_skew_126d
    ECONOMIC RATIONALE: Skewness of distress_acceleration over 126d. Acceleration of leverage combined with price decline.
    """
    return ((liabs/equity.replace(0, 1e-9)).diff(63) + close.pct_change(63)).rolling(126).skew()

def dsen_443_distress_acceleration_kurt_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_443_distress_acceleration_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of distress_acceleration over 126d. Acceleration of leverage combined with price decline.
    """
    return ((liabs/equity.replace(0, 1e-9)).diff(63) + close.pct_change(63)).rolling(126).kurt()

def dsen_444_distress_acceleration_skew_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_444_distress_acceleration_skew_252d
    ECONOMIC RATIONALE: Skewness of distress_acceleration over 252d. Acceleration of leverage combined with price decline.
    """
    return ((liabs/equity.replace(0, 1e-9)).diff(63) + close.pct_change(63)).rolling(252).skew()

def dsen_445_distress_acceleration_kurt_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_445_distress_acceleration_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of distress_acceleration over 252d. Acceleration of leverage combined with price decline.
    """
    return ((liabs/equity.replace(0, 1e-9)).diff(63) + close.pct_change(63)).rolling(252).kurt()

def dsen_446_solvency_quality_score_skew_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_446_solvency_quality_score_skew_5d
    ECONOMIC RATIONALE: Skewness of solvency_quality_score over 5d. Cash flow coverage of debt adjusted by equity status.
    """
    return (ocf / liabs.replace(0, 1e-9) * (equity > 0).astype(float)).rolling(5).skew()

def dsen_447_solvency_quality_score_kurt_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_447_solvency_quality_score_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of solvency_quality_score over 5d. Cash flow coverage of debt adjusted by equity status.
    """
    return (ocf / liabs.replace(0, 1e-9) * (equity > 0).astype(float)).rolling(5).kurt()

def dsen_448_solvency_quality_score_skew_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_448_solvency_quality_score_skew_21d
    ECONOMIC RATIONALE: Skewness of solvency_quality_score over 21d. Cash flow coverage of debt adjusted by equity status.
    """
    return (ocf / liabs.replace(0, 1e-9) * (equity > 0).astype(float)).rolling(21).skew()

def dsen_449_solvency_quality_score_kurt_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_449_solvency_quality_score_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of solvency_quality_score over 21d. Cash flow coverage of debt adjusted by equity status.
    """
    return (ocf / liabs.replace(0, 1e-9) * (equity > 0).astype(float)).rolling(21).kurt()

def dsen_450_solvency_quality_score_skew_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_450_solvency_quality_score_skew_63d
    ECONOMIC RATIONALE: Skewness of solvency_quality_score over 63d. Cash flow coverage of debt adjusted by equity status.
    """
    return (ocf / liabs.replace(0, 1e-9) * (equity > 0).astype(float)).rolling(63).skew()

def dsen_451_solvency_quality_score_kurt_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_451_solvency_quality_score_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of solvency_quality_score over 63d. Cash flow coverage of debt adjusted by equity status.
    """
    return (ocf / liabs.replace(0, 1e-9) * (equity > 0).astype(float)).rolling(63).kurt()

def dsen_452_solvency_quality_score_skew_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_452_solvency_quality_score_skew_126d
    ECONOMIC RATIONALE: Skewness of solvency_quality_score over 126d. Cash flow coverage of debt adjusted by equity status.
    """
    return (ocf / liabs.replace(0, 1e-9) * (equity > 0).astype(float)).rolling(126).skew()

def dsen_453_solvency_quality_score_kurt_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_453_solvency_quality_score_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of solvency_quality_score over 126d. Cash flow coverage of debt adjusted by equity status.
    """
    return (ocf / liabs.replace(0, 1e-9) * (equity > 0).astype(float)).rolling(126).kurt()

def dsen_454_solvency_quality_score_skew_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_454_solvency_quality_score_skew_252d
    ECONOMIC RATIONALE: Skewness of solvency_quality_score over 252d. Cash flow coverage of debt adjusted by equity status.
    """
    return (ocf / liabs.replace(0, 1e-9) * (equity > 0).astype(float)).rolling(252).skew()

def dsen_455_solvency_quality_score_kurt_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_455_solvency_quality_score_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of solvency_quality_score over 252d. Cash flow coverage of debt adjusted by equity status.
    """
    return (ocf / liabs.replace(0, 1e-9) * (equity > 0).astype(float)).rolling(252).kurt()

def dsen_456_ensemble_zscore_skew_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_456_ensemble_zscore_skew_5d
    ECONOMIC RATIONALE: Skewness of ensemble_zscore over 5d. Integrated balance sheet and income statement distress.
    """
    return (_zscore_rolling(liabs/assets.replace(0, 1e-9) - ocf/assets.replace(0, 1e-9), 252)).rolling(5).skew()

def dsen_457_ensemble_zscore_kurt_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_457_ensemble_zscore_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of ensemble_zscore over 5d. Integrated balance sheet and income statement distress.
    """
    return (_zscore_rolling(liabs/assets.replace(0, 1e-9) - ocf/assets.replace(0, 1e-9), 252)).rolling(5).kurt()

def dsen_458_ensemble_zscore_skew_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_458_ensemble_zscore_skew_21d
    ECONOMIC RATIONALE: Skewness of ensemble_zscore over 21d. Integrated balance sheet and income statement distress.
    """
    return (_zscore_rolling(liabs/assets.replace(0, 1e-9) - ocf/assets.replace(0, 1e-9), 252)).rolling(21).skew()

def dsen_459_ensemble_zscore_kurt_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_459_ensemble_zscore_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of ensemble_zscore over 21d. Integrated balance sheet and income statement distress.
    """
    return (_zscore_rolling(liabs/assets.replace(0, 1e-9) - ocf/assets.replace(0, 1e-9), 252)).rolling(21).kurt()

def dsen_460_ensemble_zscore_skew_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_460_ensemble_zscore_skew_63d
    ECONOMIC RATIONALE: Skewness of ensemble_zscore over 63d. Integrated balance sheet and income statement distress.
    """
    return (_zscore_rolling(liabs/assets.replace(0, 1e-9) - ocf/assets.replace(0, 1e-9), 252)).rolling(63).skew()

def dsen_461_ensemble_zscore_kurt_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_461_ensemble_zscore_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of ensemble_zscore over 63d. Integrated balance sheet and income statement distress.
    """
    return (_zscore_rolling(liabs/assets.replace(0, 1e-9) - ocf/assets.replace(0, 1e-9), 252)).rolling(63).kurt()

def dsen_462_ensemble_zscore_skew_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_462_ensemble_zscore_skew_126d
    ECONOMIC RATIONALE: Skewness of ensemble_zscore over 126d. Integrated balance sheet and income statement distress.
    """
    return (_zscore_rolling(liabs/assets.replace(0, 1e-9) - ocf/assets.replace(0, 1e-9), 252)).rolling(126).skew()

def dsen_463_ensemble_zscore_kurt_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_463_ensemble_zscore_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of ensemble_zscore over 126d. Integrated balance sheet and income statement distress.
    """
    return (_zscore_rolling(liabs/assets.replace(0, 1e-9) - ocf/assets.replace(0, 1e-9), 252)).rolling(126).kurt()

def dsen_464_ensemble_zscore_skew_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_464_ensemble_zscore_skew_252d
    ECONOMIC RATIONALE: Skewness of ensemble_zscore over 252d. Integrated balance sheet and income statement distress.
    """
    return (_zscore_rolling(liabs/assets.replace(0, 1e-9) - ocf/assets.replace(0, 1e-9), 252)).rolling(252).skew()

def dsen_465_ensemble_zscore_kurt_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_465_ensemble_zscore_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of ensemble_zscore over 252d. Integrated balance sheet and income statement distress.
    """
    return (_zscore_rolling(liabs/assets.replace(0, 1e-9) - ocf/assets.replace(0, 1e-9), 252)).rolling(252).kurt()

def dsen_466_market_distress_beta_skew_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_466_market_distress_beta_skew_5d
    ECONOMIC RATIONALE: Skewness of market_distress_beta over 5d. Market sensitivity weighted by financial risk.
    """
    return (close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)) * (liabs/equity.replace(0, 1e-9))).rolling(5).skew()

def dsen_467_market_distress_beta_kurt_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_467_market_distress_beta_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of market_distress_beta over 5d. Market sensitivity weighted by financial risk.
    """
    return (close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)) * (liabs/equity.replace(0, 1e-9))).rolling(5).kurt()

def dsen_468_market_distress_beta_skew_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_468_market_distress_beta_skew_21d
    ECONOMIC RATIONALE: Skewness of market_distress_beta over 21d. Market sensitivity weighted by financial risk.
    """
    return (close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)) * (liabs/equity.replace(0, 1e-9))).rolling(21).skew()

def dsen_469_market_distress_beta_kurt_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_469_market_distress_beta_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of market_distress_beta over 21d. Market sensitivity weighted by financial risk.
    """
    return (close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)) * (liabs/equity.replace(0, 1e-9))).rolling(21).kurt()

def dsen_470_market_distress_beta_skew_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_470_market_distress_beta_skew_63d
    ECONOMIC RATIONALE: Skewness of market_distress_beta over 63d. Market sensitivity weighted by financial risk.
    """
    return (close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)) * (liabs/equity.replace(0, 1e-9))).rolling(63).skew()

def dsen_471_market_distress_beta_kurt_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_471_market_distress_beta_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of market_distress_beta over 63d. Market sensitivity weighted by financial risk.
    """
    return (close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)) * (liabs/equity.replace(0, 1e-9))).rolling(63).kurt()

def dsen_472_market_distress_beta_skew_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_472_market_distress_beta_skew_126d
    ECONOMIC RATIONALE: Skewness of market_distress_beta over 126d. Market sensitivity weighted by financial risk.
    """
    return (close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)) * (liabs/equity.replace(0, 1e-9))).rolling(126).skew()

def dsen_473_market_distress_beta_kurt_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_473_market_distress_beta_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of market_distress_beta over 126d. Market sensitivity weighted by financial risk.
    """
    return (close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)) * (liabs/equity.replace(0, 1e-9))).rolling(126).kurt()

def dsen_474_market_distress_beta_skew_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_474_market_distress_beta_skew_252d
    ECONOMIC RATIONALE: Skewness of market_distress_beta over 252d. Market sensitivity weighted by financial risk.
    """
    return (close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)) * (liabs/equity.replace(0, 1e-9))).rolling(252).skew()

def dsen_475_market_distress_beta_kurt_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_475_market_distress_beta_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of market_distress_beta over 252d. Market sensitivity weighted by financial risk.
    """
    return (close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)) * (liabs/equity.replace(0, 1e-9))).rolling(252).kurt()

def dsen_476_ensemble_drawdown_rank_skew_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_476_ensemble_drawdown_rank_skew_5d
    ECONOMIC RATIONALE: Skewness of ensemble_drawdown_rank over 5d. Rank of combined price and leverage stress.
    """
    return (_rank_pct(close/close.rolling(252).max() + liabs/assets.replace(0, 1e-9), 252)).rolling(5).skew()

def dsen_477_ensemble_drawdown_rank_kurt_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_477_ensemble_drawdown_rank_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of ensemble_drawdown_rank over 5d. Rank of combined price and leverage stress.
    """
    return (_rank_pct(close/close.rolling(252).max() + liabs/assets.replace(0, 1e-9), 252)).rolling(5).kurt()

def dsen_478_ensemble_drawdown_rank_skew_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_478_ensemble_drawdown_rank_skew_21d
    ECONOMIC RATIONALE: Skewness of ensemble_drawdown_rank over 21d. Rank of combined price and leverage stress.
    """
    return (_rank_pct(close/close.rolling(252).max() + liabs/assets.replace(0, 1e-9), 252)).rolling(21).skew()

def dsen_479_ensemble_drawdown_rank_kurt_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_479_ensemble_drawdown_rank_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of ensemble_drawdown_rank over 21d. Rank of combined price and leverage stress.
    """
    return (_rank_pct(close/close.rolling(252).max() + liabs/assets.replace(0, 1e-9), 252)).rolling(21).kurt()

def dsen_480_ensemble_drawdown_rank_skew_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_480_ensemble_drawdown_rank_skew_63d
    ECONOMIC RATIONALE: Skewness of ensemble_drawdown_rank over 63d. Rank of combined price and leverage stress.
    """
    return (_rank_pct(close/close.rolling(252).max() + liabs/assets.replace(0, 1e-9), 252)).rolling(63).skew()

def dsen_481_ensemble_drawdown_rank_kurt_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_481_ensemble_drawdown_rank_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of ensemble_drawdown_rank over 63d. Rank of combined price and leverage stress.
    """
    return (_rank_pct(close/close.rolling(252).max() + liabs/assets.replace(0, 1e-9), 252)).rolling(63).kurt()

def dsen_482_ensemble_drawdown_rank_skew_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_482_ensemble_drawdown_rank_skew_126d
    ECONOMIC RATIONALE: Skewness of ensemble_drawdown_rank over 126d. Rank of combined price and leverage stress.
    """
    return (_rank_pct(close/close.rolling(252).max() + liabs/assets.replace(0, 1e-9), 252)).rolling(126).skew()

def dsen_483_ensemble_drawdown_rank_kurt_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_483_ensemble_drawdown_rank_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of ensemble_drawdown_rank over 126d. Rank of combined price and leverage stress.
    """
    return (_rank_pct(close/close.rolling(252).max() + liabs/assets.replace(0, 1e-9), 252)).rolling(126).kurt()

def dsen_484_ensemble_drawdown_rank_skew_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_484_ensemble_drawdown_rank_skew_252d
    ECONOMIC RATIONALE: Skewness of ensemble_drawdown_rank over 252d. Rank of combined price and leverage stress.
    """
    return (_rank_pct(close/close.rolling(252).max() + liabs/assets.replace(0, 1e-9), 252)).rolling(252).skew()

def dsen_485_ensemble_drawdown_rank_kurt_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_485_ensemble_drawdown_rank_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of ensemble_drawdown_rank over 252d. Rank of combined price and leverage stress.
    """
    return (_rank_pct(close/close.rolling(252).max() + liabs/assets.replace(0, 1e-9), 252)).rolling(252).kurt()

def dsen_486_distress_reversal_potential_skew_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_486_distress_reversal_potential_skew_5d
    ECONOMIC RATIONALE: Skewness of distress_reversal_potential over 5d. Reversal potential for highly levered distressed firms.
    """
    return (close.pct_change(5) * (liabs/equity.replace(0, 1e-9) > 2).astype(float)).rolling(5).skew()

def dsen_487_distress_reversal_potential_kurt_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_487_distress_reversal_potential_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of distress_reversal_potential over 5d. Reversal potential for highly levered distressed firms.
    """
    return (close.pct_change(5) * (liabs/equity.replace(0, 1e-9) > 2).astype(float)).rolling(5).kurt()

def dsen_488_distress_reversal_potential_skew_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_488_distress_reversal_potential_skew_21d
    ECONOMIC RATIONALE: Skewness of distress_reversal_potential over 21d. Reversal potential for highly levered distressed firms.
    """
    return (close.pct_change(5) * (liabs/equity.replace(0, 1e-9) > 2).astype(float)).rolling(21).skew()

def dsen_489_distress_reversal_potential_kurt_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_489_distress_reversal_potential_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of distress_reversal_potential over 21d. Reversal potential for highly levered distressed firms.
    """
    return (close.pct_change(5) * (liabs/equity.replace(0, 1e-9) > 2).astype(float)).rolling(21).kurt()

def dsen_490_distress_reversal_potential_skew_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_490_distress_reversal_potential_skew_63d
    ECONOMIC RATIONALE: Skewness of distress_reversal_potential over 63d. Reversal potential for highly levered distressed firms.
    """
    return (close.pct_change(5) * (liabs/equity.replace(0, 1e-9) > 2).astype(float)).rolling(63).skew()

def dsen_491_distress_reversal_potential_kurt_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_491_distress_reversal_potential_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of distress_reversal_potential over 63d. Reversal potential for highly levered distressed firms.
    """
    return (close.pct_change(5) * (liabs/equity.replace(0, 1e-9) > 2).astype(float)).rolling(63).kurt()

def dsen_492_distress_reversal_potential_skew_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_492_distress_reversal_potential_skew_126d
    ECONOMIC RATIONALE: Skewness of distress_reversal_potential over 126d. Reversal potential for highly levered distressed firms.
    """
    return (close.pct_change(5) * (liabs/equity.replace(0, 1e-9) > 2).astype(float)).rolling(126).skew()

def dsen_493_distress_reversal_potential_kurt_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_493_distress_reversal_potential_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of distress_reversal_potential over 126d. Reversal potential for highly levered distressed firms.
    """
    return (close.pct_change(5) * (liabs/equity.replace(0, 1e-9) > 2).astype(float)).rolling(126).kurt()

def dsen_494_distress_reversal_potential_skew_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_494_distress_reversal_potential_skew_252d
    ECONOMIC RATIONALE: Skewness of distress_reversal_potential over 252d. Reversal potential for highly levered distressed firms.
    """
    return (close.pct_change(5) * (liabs/equity.replace(0, 1e-9) > 2).astype(float)).rolling(252).skew()

def dsen_495_distress_reversal_potential_kurt_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_495_distress_reversal_potential_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of distress_reversal_potential over 252d. Reversal potential for highly levered distressed firms.
    """
    return (close.pct_change(5) * (liabs/equity.replace(0, 1e-9) > 2).astype(float)).rolling(252).kurt()

def dsen_496_ensemble_liquidity_gap_skew_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_496_ensemble_liquidity_gap_skew_5d
    ECONOMIC RATIONALE: Skewness of ensemble_liquidity_gap over 5d. Net cash flow after change in liabilities.
    """
    return (ocf - liabs.diff(63)).rolling(5).skew()

def dsen_497_ensemble_liquidity_gap_kurt_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_497_ensemble_liquidity_gap_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of ensemble_liquidity_gap over 5d. Net cash flow after change in liabilities.
    """
    return (ocf - liabs.diff(63)).rolling(5).kurt()

def dsen_498_ensemble_liquidity_gap_skew_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_498_ensemble_liquidity_gap_skew_21d
    ECONOMIC RATIONALE: Skewness of ensemble_liquidity_gap over 21d. Net cash flow after change in liabilities.
    """
    return (ocf - liabs.diff(63)).rolling(21).skew()

def dsen_499_ensemble_liquidity_gap_kurt_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_499_ensemble_liquidity_gap_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of ensemble_liquidity_gap over 21d. Net cash flow after change in liabilities.
    """
    return (ocf - liabs.diff(63)).rolling(21).kurt()

def dsen_500_ensemble_liquidity_gap_skew_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_500_ensemble_liquidity_gap_skew_63d
    ECONOMIC RATIONALE: Skewness of ensemble_liquidity_gap over 63d. Net cash flow after change in liabilities.
    """
    return (ocf - liabs.diff(63)).rolling(63).skew()

def dsen_501_ensemble_liquidity_gap_kurt_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_501_ensemble_liquidity_gap_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of ensemble_liquidity_gap over 63d. Net cash flow after change in liabilities.
    """
    return (ocf - liabs.diff(63)).rolling(63).kurt()

def dsen_502_ensemble_liquidity_gap_skew_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_502_ensemble_liquidity_gap_skew_126d
    ECONOMIC RATIONALE: Skewness of ensemble_liquidity_gap over 126d. Net cash flow after change in liabilities.
    """
    return (ocf - liabs.diff(63)).rolling(126).skew()

def dsen_503_ensemble_liquidity_gap_kurt_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_503_ensemble_liquidity_gap_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of ensemble_liquidity_gap over 126d. Net cash flow after change in liabilities.
    """
    return (ocf - liabs.diff(63)).rolling(126).kurt()

def dsen_504_ensemble_liquidity_gap_skew_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_504_ensemble_liquidity_gap_skew_252d
    ECONOMIC RATIONALE: Skewness of ensemble_liquidity_gap over 252d. Net cash flow after change in liabilities.
    """
    return (ocf - liabs.diff(63)).rolling(252).skew()

def dsen_505_ensemble_liquidity_gap_kurt_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_505_ensemble_liquidity_gap_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of ensemble_liquidity_gap over 252d. Net cash flow after change in liabilities.
    """
    return (ocf - liabs.diff(63)).rolling(252).kurt()

def dsen_506_structural_fragility_index_skew_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_506_structural_fragility_index_skew_5d
    ECONOMIC RATIONALE: Skewness of structural_fragility_index over 5d. Financial leverage relative to price stability.
    """
    return ((liabs/equity.replace(0, 1e-9)) / close.rolling(252).std().replace(0, 1e-9)).rolling(5).skew()

def dsen_507_structural_fragility_index_kurt_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_507_structural_fragility_index_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of structural_fragility_index over 5d. Financial leverage relative to price stability.
    """
    return ((liabs/equity.replace(0, 1e-9)) / close.rolling(252).std().replace(0, 1e-9)).rolling(5).kurt()

def dsen_508_structural_fragility_index_skew_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_508_structural_fragility_index_skew_21d
    ECONOMIC RATIONALE: Skewness of structural_fragility_index over 21d. Financial leverage relative to price stability.
    """
    return ((liabs/equity.replace(0, 1e-9)) / close.rolling(252).std().replace(0, 1e-9)).rolling(21).skew()

def dsen_509_structural_fragility_index_kurt_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_509_structural_fragility_index_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of structural_fragility_index over 21d. Financial leverage relative to price stability.
    """
    return ((liabs/equity.replace(0, 1e-9)) / close.rolling(252).std().replace(0, 1e-9)).rolling(21).kurt()

def dsen_510_structural_fragility_index_skew_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_510_structural_fragility_index_skew_63d
    ECONOMIC RATIONALE: Skewness of structural_fragility_index over 63d. Financial leverage relative to price stability.
    """
    return ((liabs/equity.replace(0, 1e-9)) / close.rolling(252).std().replace(0, 1e-9)).rolling(63).skew()

def dsen_511_structural_fragility_index_kurt_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_511_structural_fragility_index_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of structural_fragility_index over 63d. Financial leverage relative to price stability.
    """
    return ((liabs/equity.replace(0, 1e-9)) / close.rolling(252).std().replace(0, 1e-9)).rolling(63).kurt()

def dsen_512_structural_fragility_index_skew_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_512_structural_fragility_index_skew_126d
    ECONOMIC RATIONALE: Skewness of structural_fragility_index over 126d. Financial leverage relative to price stability.
    """
    return ((liabs/equity.replace(0, 1e-9)) / close.rolling(252).std().replace(0, 1e-9)).rolling(126).skew()

def dsen_513_structural_fragility_index_kurt_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_513_structural_fragility_index_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of structural_fragility_index over 126d. Financial leverage relative to price stability.
    """
    return ((liabs/equity.replace(0, 1e-9)) / close.rolling(252).std().replace(0, 1e-9)).rolling(126).kurt()

def dsen_514_structural_fragility_index_skew_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_514_structural_fragility_index_skew_252d
    ECONOMIC RATIONALE: Skewness of structural_fragility_index over 252d. Financial leverage relative to price stability.
    """
    return ((liabs/equity.replace(0, 1e-9)) / close.rolling(252).std().replace(0, 1e-9)).rolling(252).skew()

def dsen_515_structural_fragility_index_kurt_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_515_structural_fragility_index_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of structural_fragility_index over 252d. Financial leverage relative to price stability.
    """
    return ((liabs/equity.replace(0, 1e-9)) / close.rolling(252).std().replace(0, 1e-9)).rolling(252).kurt()

def dsen_516_ensemble_tail_risk_skew_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_516_ensemble_tail_risk_skew_5d
    ECONOMIC RATIONALE: Skewness of ensemble_tail_risk over 5d. Co-occurrence of price tail events and insolvency.
    """
    return (((close.pct_change(1) < -0.05) & (liabs > equity)).astype(float)).rolling(5).skew()

def dsen_517_ensemble_tail_risk_kurt_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_517_ensemble_tail_risk_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of ensemble_tail_risk over 5d. Co-occurrence of price tail events and insolvency.
    """
    return (((close.pct_change(1) < -0.05) & (liabs > equity)).astype(float)).rolling(5).kurt()

def dsen_518_ensemble_tail_risk_skew_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_518_ensemble_tail_risk_skew_21d
    ECONOMIC RATIONALE: Skewness of ensemble_tail_risk over 21d. Co-occurrence of price tail events and insolvency.
    """
    return (((close.pct_change(1) < -0.05) & (liabs > equity)).astype(float)).rolling(21).skew()

def dsen_519_ensemble_tail_risk_kurt_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_519_ensemble_tail_risk_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of ensemble_tail_risk over 21d. Co-occurrence of price tail events and insolvency.
    """
    return (((close.pct_change(1) < -0.05) & (liabs > equity)).astype(float)).rolling(21).kurt()

def dsen_520_ensemble_tail_risk_skew_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_520_ensemble_tail_risk_skew_63d
    ECONOMIC RATIONALE: Skewness of ensemble_tail_risk over 63d. Co-occurrence of price tail events and insolvency.
    """
    return (((close.pct_change(1) < -0.05) & (liabs > equity)).astype(float)).rolling(63).skew()

def dsen_521_ensemble_tail_risk_kurt_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_521_ensemble_tail_risk_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of ensemble_tail_risk over 63d. Co-occurrence of price tail events and insolvency.
    """
    return (((close.pct_change(1) < -0.05) & (liabs > equity)).astype(float)).rolling(63).kurt()

def dsen_522_ensemble_tail_risk_skew_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_522_ensemble_tail_risk_skew_126d
    ECONOMIC RATIONALE: Skewness of ensemble_tail_risk over 126d. Co-occurrence of price tail events and insolvency.
    """
    return (((close.pct_change(1) < -0.05) & (liabs > equity)).astype(float)).rolling(126).skew()

def dsen_523_ensemble_tail_risk_kurt_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_523_ensemble_tail_risk_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of ensemble_tail_risk over 126d. Co-occurrence of price tail events and insolvency.
    """
    return (((close.pct_change(1) < -0.05) & (liabs > equity)).astype(float)).rolling(126).kurt()

def dsen_524_ensemble_tail_risk_skew_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_524_ensemble_tail_risk_skew_252d
    ECONOMIC RATIONALE: Skewness of ensemble_tail_risk over 252d. Co-occurrence of price tail events and insolvency.
    """
    return (((close.pct_change(1) < -0.05) & (liabs > equity)).astype(float)).rolling(252).skew()

def dsen_525_ensemble_tail_risk_kurt_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_525_ensemble_tail_risk_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of ensemble_tail_risk over 252d. Co-occurrence of price tail events and insolvency.
    """
    return (((close.pct_change(1) < -0.05) & (liabs > equity)).astype(float)).rolling(252).kurt()

# ── Registry ──────────────────────────────────────────────────────────────────
V121_REGISTRY_MOMENTS = {
    "dsen_376_composite_distress_z_skew_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_376_composite_distress_z_skew_5d},
    "dsen_377_composite_distress_z_kurt_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_377_composite_distress_z_kurt_5d},
    "dsen_378_composite_distress_z_skew_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_378_composite_distress_z_skew_21d},
    "dsen_379_composite_distress_z_kurt_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_379_composite_distress_z_kurt_21d},
    "dsen_380_composite_distress_z_skew_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_380_composite_distress_z_skew_63d},
    "dsen_381_composite_distress_z_kurt_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_381_composite_distress_z_kurt_63d},
    "dsen_382_composite_distress_z_skew_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_382_composite_distress_z_skew_126d},
    "dsen_383_composite_distress_z_kurt_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_383_composite_distress_z_kurt_126d},
    "dsen_384_composite_distress_z_skew_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_384_composite_distress_z_skew_252d},
    "dsen_385_composite_distress_z_kurt_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_385_composite_distress_z_kurt_252d},
    "dsen_386_valuation_solvency_blend_skew_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_386_valuation_solvency_blend_skew_5d},
    "dsen_387_valuation_solvency_blend_kurt_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_387_valuation_solvency_blend_kurt_5d},
    "dsen_388_valuation_solvency_blend_skew_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_388_valuation_solvency_blend_skew_21d},
    "dsen_389_valuation_solvency_blend_kurt_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_389_valuation_solvency_blend_kurt_21d},
    "dsen_390_valuation_solvency_blend_skew_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_390_valuation_solvency_blend_skew_63d},
    "dsen_391_valuation_solvency_blend_kurt_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_391_valuation_solvency_blend_kurt_63d},
    "dsen_392_valuation_solvency_blend_skew_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_392_valuation_solvency_blend_skew_126d},
    "dsen_393_valuation_solvency_blend_kurt_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_393_valuation_solvency_blend_kurt_126d},
    "dsen_394_valuation_solvency_blend_skew_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_394_valuation_solvency_blend_skew_252d},
    "dsen_395_valuation_solvency_blend_kurt_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_395_valuation_solvency_blend_kurt_252d},
    "dsen_396_liquidity_momentum_ensemble_skew_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_396_liquidity_momentum_ensemble_skew_5d},
    "dsen_397_liquidity_momentum_ensemble_kurt_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_397_liquidity_momentum_ensemble_kurt_5d},
    "dsen_398_liquidity_momentum_ensemble_skew_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_398_liquidity_momentum_ensemble_skew_21d},
    "dsen_399_liquidity_momentum_ensemble_kurt_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_399_liquidity_momentum_ensemble_kurt_21d},
    "dsen_400_liquidity_momentum_ensemble_skew_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_400_liquidity_momentum_ensemble_skew_63d},
    "dsen_401_liquidity_momentum_ensemble_kurt_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_401_liquidity_momentum_ensemble_kurt_63d},
    "dsen_402_liquidity_momentum_ensemble_skew_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_402_liquidity_momentum_ensemble_skew_126d},
    "dsen_403_liquidity_momentum_ensemble_kurt_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_403_liquidity_momentum_ensemble_kurt_126d},
    "dsen_404_liquidity_momentum_ensemble_skew_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_404_liquidity_momentum_ensemble_skew_252d},
    "dsen_405_liquidity_momentum_ensemble_kurt_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_405_liquidity_momentum_ensemble_kurt_252d},
    "dsen_406_distress_regime_indicator_skew_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_406_distress_regime_indicator_skew_5d},
    "dsen_407_distress_regime_indicator_kurt_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_407_distress_regime_indicator_kurt_5d},
    "dsen_408_distress_regime_indicator_skew_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_408_distress_regime_indicator_skew_21d},
    "dsen_409_distress_regime_indicator_kurt_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_409_distress_regime_indicator_kurt_21d},
    "dsen_410_distress_regime_indicator_skew_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_410_distress_regime_indicator_skew_63d},
    "dsen_411_distress_regime_indicator_kurt_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_411_distress_regime_indicator_kurt_63d},
    "dsen_412_distress_regime_indicator_skew_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_412_distress_regime_indicator_skew_126d},
    "dsen_413_distress_regime_indicator_kurt_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_413_distress_regime_indicator_kurt_126d},
    "dsen_414_distress_regime_indicator_skew_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_414_distress_regime_indicator_skew_252d},
    "dsen_415_distress_regime_indicator_kurt_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_415_distress_regime_indicator_kurt_252d},
    "dsen_416_ensemble_vol_risk_skew_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_416_ensemble_vol_risk_skew_5d},
    "dsen_417_ensemble_vol_risk_kurt_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_417_ensemble_vol_risk_kurt_5d},
    "dsen_418_ensemble_vol_risk_skew_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_418_ensemble_vol_risk_skew_21d},
    "dsen_419_ensemble_vol_risk_kurt_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_419_ensemble_vol_risk_kurt_21d},
    "dsen_420_ensemble_vol_risk_skew_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_420_ensemble_vol_risk_skew_63d},
    "dsen_421_ensemble_vol_risk_kurt_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_421_ensemble_vol_risk_kurt_63d},
    "dsen_422_ensemble_vol_risk_skew_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_422_ensemble_vol_risk_skew_126d},
    "dsen_423_ensemble_vol_risk_kurt_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_423_ensemble_vol_risk_kurt_126d},
    "dsen_424_ensemble_vol_risk_skew_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_424_ensemble_vol_risk_skew_252d},
    "dsen_425_ensemble_vol_risk_kurt_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_425_ensemble_vol_risk_kurt_252d},
    "dsen_426_multi_factor_drawdown_skew_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_426_multi_factor_drawdown_skew_5d},
    "dsen_427_multi_factor_drawdown_kurt_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_427_multi_factor_drawdown_kurt_5d},
    "dsen_428_multi_factor_drawdown_skew_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_428_multi_factor_drawdown_skew_21d},
    "dsen_429_multi_factor_drawdown_kurt_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_429_multi_factor_drawdown_kurt_21d},
    "dsen_430_multi_factor_drawdown_skew_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_430_multi_factor_drawdown_skew_63d},
    "dsen_431_multi_factor_drawdown_kurt_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_431_multi_factor_drawdown_kurt_63d},
    "dsen_432_multi_factor_drawdown_skew_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_432_multi_factor_drawdown_skew_126d},
    "dsen_433_multi_factor_drawdown_kurt_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_433_multi_factor_drawdown_kurt_126d},
    "dsen_434_multi_factor_drawdown_skew_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_434_multi_factor_drawdown_skew_252d},
    "dsen_435_multi_factor_drawdown_kurt_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_435_multi_factor_drawdown_kurt_252d},
    "dsen_436_distress_acceleration_skew_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_436_distress_acceleration_skew_5d},
    "dsen_437_distress_acceleration_kurt_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_437_distress_acceleration_kurt_5d},
    "dsen_438_distress_acceleration_skew_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_438_distress_acceleration_skew_21d},
    "dsen_439_distress_acceleration_kurt_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_439_distress_acceleration_kurt_21d},
    "dsen_440_distress_acceleration_skew_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_440_distress_acceleration_skew_63d},
    "dsen_441_distress_acceleration_kurt_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_441_distress_acceleration_kurt_63d},
    "dsen_442_distress_acceleration_skew_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_442_distress_acceleration_skew_126d},
    "dsen_443_distress_acceleration_kurt_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_443_distress_acceleration_kurt_126d},
    "dsen_444_distress_acceleration_skew_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_444_distress_acceleration_skew_252d},
    "dsen_445_distress_acceleration_kurt_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_445_distress_acceleration_kurt_252d},
    "dsen_446_solvency_quality_score_skew_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_446_solvency_quality_score_skew_5d},
    "dsen_447_solvency_quality_score_kurt_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_447_solvency_quality_score_kurt_5d},
    "dsen_448_solvency_quality_score_skew_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_448_solvency_quality_score_skew_21d},
    "dsen_449_solvency_quality_score_kurt_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_449_solvency_quality_score_kurt_21d},
    "dsen_450_solvency_quality_score_skew_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_450_solvency_quality_score_skew_63d},
    "dsen_451_solvency_quality_score_kurt_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_451_solvency_quality_score_kurt_63d},
    "dsen_452_solvency_quality_score_skew_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_452_solvency_quality_score_skew_126d},
    "dsen_453_solvency_quality_score_kurt_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_453_solvency_quality_score_kurt_126d},
    "dsen_454_solvency_quality_score_skew_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_454_solvency_quality_score_skew_252d},
    "dsen_455_solvency_quality_score_kurt_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_455_solvency_quality_score_kurt_252d},
    "dsen_456_ensemble_zscore_skew_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_456_ensemble_zscore_skew_5d},
    "dsen_457_ensemble_zscore_kurt_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_457_ensemble_zscore_kurt_5d},
    "dsen_458_ensemble_zscore_skew_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_458_ensemble_zscore_skew_21d},
    "dsen_459_ensemble_zscore_kurt_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_459_ensemble_zscore_kurt_21d},
    "dsen_460_ensemble_zscore_skew_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_460_ensemble_zscore_skew_63d},
    "dsen_461_ensemble_zscore_kurt_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_461_ensemble_zscore_kurt_63d},
    "dsen_462_ensemble_zscore_skew_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_462_ensemble_zscore_skew_126d},
    "dsen_463_ensemble_zscore_kurt_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_463_ensemble_zscore_kurt_126d},
    "dsen_464_ensemble_zscore_skew_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_464_ensemble_zscore_skew_252d},
    "dsen_465_ensemble_zscore_kurt_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_465_ensemble_zscore_kurt_252d},
    "dsen_466_market_distress_beta_skew_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_466_market_distress_beta_skew_5d},
    "dsen_467_market_distress_beta_kurt_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_467_market_distress_beta_kurt_5d},
    "dsen_468_market_distress_beta_skew_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_468_market_distress_beta_skew_21d},
    "dsen_469_market_distress_beta_kurt_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_469_market_distress_beta_kurt_21d},
    "dsen_470_market_distress_beta_skew_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_470_market_distress_beta_skew_63d},
    "dsen_471_market_distress_beta_kurt_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_471_market_distress_beta_kurt_63d},
    "dsen_472_market_distress_beta_skew_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_472_market_distress_beta_skew_126d},
    "dsen_473_market_distress_beta_kurt_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_473_market_distress_beta_kurt_126d},
    "dsen_474_market_distress_beta_skew_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_474_market_distress_beta_skew_252d},
    "dsen_475_market_distress_beta_kurt_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_475_market_distress_beta_kurt_252d},
    "dsen_476_ensemble_drawdown_rank_skew_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_476_ensemble_drawdown_rank_skew_5d},
    "dsen_477_ensemble_drawdown_rank_kurt_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_477_ensemble_drawdown_rank_kurt_5d},
    "dsen_478_ensemble_drawdown_rank_skew_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_478_ensemble_drawdown_rank_skew_21d},
    "dsen_479_ensemble_drawdown_rank_kurt_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_479_ensemble_drawdown_rank_kurt_21d},
    "dsen_480_ensemble_drawdown_rank_skew_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_480_ensemble_drawdown_rank_skew_63d},
    "dsen_481_ensemble_drawdown_rank_kurt_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_481_ensemble_drawdown_rank_kurt_63d},
    "dsen_482_ensemble_drawdown_rank_skew_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_482_ensemble_drawdown_rank_skew_126d},
    "dsen_483_ensemble_drawdown_rank_kurt_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_483_ensemble_drawdown_rank_kurt_126d},
    "dsen_484_ensemble_drawdown_rank_skew_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_484_ensemble_drawdown_rank_skew_252d},
    "dsen_485_ensemble_drawdown_rank_kurt_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_485_ensemble_drawdown_rank_kurt_252d},
    "dsen_486_distress_reversal_potential_skew_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_486_distress_reversal_potential_skew_5d},
    "dsen_487_distress_reversal_potential_kurt_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_487_distress_reversal_potential_kurt_5d},
    "dsen_488_distress_reversal_potential_skew_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_488_distress_reversal_potential_skew_21d},
    "dsen_489_distress_reversal_potential_kurt_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_489_distress_reversal_potential_kurt_21d},
    "dsen_490_distress_reversal_potential_skew_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_490_distress_reversal_potential_skew_63d},
    "dsen_491_distress_reversal_potential_kurt_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_491_distress_reversal_potential_kurt_63d},
    "dsen_492_distress_reversal_potential_skew_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_492_distress_reversal_potential_skew_126d},
    "dsen_493_distress_reversal_potential_kurt_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_493_distress_reversal_potential_kurt_126d},
    "dsen_494_distress_reversal_potential_skew_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_494_distress_reversal_potential_skew_252d},
    "dsen_495_distress_reversal_potential_kurt_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_495_distress_reversal_potential_kurt_252d},
    "dsen_496_ensemble_liquidity_gap_skew_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_496_ensemble_liquidity_gap_skew_5d},
    "dsen_497_ensemble_liquidity_gap_kurt_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_497_ensemble_liquidity_gap_kurt_5d},
    "dsen_498_ensemble_liquidity_gap_skew_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_498_ensemble_liquidity_gap_skew_21d},
    "dsen_499_ensemble_liquidity_gap_kurt_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_499_ensemble_liquidity_gap_kurt_21d},
    "dsen_500_ensemble_liquidity_gap_skew_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_500_ensemble_liquidity_gap_skew_63d},
    "dsen_501_ensemble_liquidity_gap_kurt_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_501_ensemble_liquidity_gap_kurt_63d},
    "dsen_502_ensemble_liquidity_gap_skew_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_502_ensemble_liquidity_gap_skew_126d},
    "dsen_503_ensemble_liquidity_gap_kurt_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_503_ensemble_liquidity_gap_kurt_126d},
    "dsen_504_ensemble_liquidity_gap_skew_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_504_ensemble_liquidity_gap_skew_252d},
    "dsen_505_ensemble_liquidity_gap_kurt_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_505_ensemble_liquidity_gap_kurt_252d},
    "dsen_506_structural_fragility_index_skew_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_506_structural_fragility_index_skew_5d},
    "dsen_507_structural_fragility_index_kurt_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_507_structural_fragility_index_kurt_5d},
    "dsen_508_structural_fragility_index_skew_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_508_structural_fragility_index_skew_21d},
    "dsen_509_structural_fragility_index_kurt_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_509_structural_fragility_index_kurt_21d},
    "dsen_510_structural_fragility_index_skew_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_510_structural_fragility_index_skew_63d},
    "dsen_511_structural_fragility_index_kurt_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_511_structural_fragility_index_kurt_63d},
    "dsen_512_structural_fragility_index_skew_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_512_structural_fragility_index_skew_126d},
    "dsen_513_structural_fragility_index_kurt_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_513_structural_fragility_index_kurt_126d},
    "dsen_514_structural_fragility_index_skew_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_514_structural_fragility_index_skew_252d},
    "dsen_515_structural_fragility_index_kurt_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_515_structural_fragility_index_kurt_252d},
    "dsen_516_ensemble_tail_risk_skew_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_516_ensemble_tail_risk_skew_5d},
    "dsen_517_ensemble_tail_risk_kurt_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_517_ensemble_tail_risk_kurt_5d},
    "dsen_518_ensemble_tail_risk_skew_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_518_ensemble_tail_risk_skew_21d},
    "dsen_519_ensemble_tail_risk_kurt_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_519_ensemble_tail_risk_kurt_21d},
    "dsen_520_ensemble_tail_risk_skew_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_520_ensemble_tail_risk_skew_63d},
    "dsen_521_ensemble_tail_risk_kurt_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_521_ensemble_tail_risk_kurt_63d},
    "dsen_522_ensemble_tail_risk_skew_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_522_ensemble_tail_risk_skew_126d},
    "dsen_523_ensemble_tail_risk_kurt_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_523_ensemble_tail_risk_kurt_126d},
    "dsen_524_ensemble_tail_risk_skew_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_524_ensemble_tail_risk_skew_252d},
    "dsen_525_ensemble_tail_risk_kurt_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_525_ensemble_tail_risk_kurt_252d},
}
