"""
105_fractal_structure — Acceleration (3rd Derivatives)
Domain: fractal_structure
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

def frac_301_hurst_exponent_proxy_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_301_hurst_exponent_proxy_accel_5d
    ECONOMIC RATIONALE: Acceleration of hurst_exponent_proxy. Simplified Hurst exponent for trend persistence.
    """
    return (np.log(high.rolling(21).max() - low.rolling(21).min()) / np.log(21)).diff(5).diff(_TD_MON)

def frac_302_hurst_exponent_proxy_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_302_hurst_exponent_proxy_accel_21d
    ECONOMIC RATIONALE: Acceleration of hurst_exponent_proxy. Simplified Hurst exponent for trend persistence.
    """
    return (np.log(high.rolling(21).max() - low.rolling(21).min()) / np.log(21)).diff(21).diff(_TD_MON)

def frac_303_hurst_exponent_proxy_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_303_hurst_exponent_proxy_accel_63d
    ECONOMIC RATIONALE: Acceleration of hurst_exponent_proxy. Simplified Hurst exponent for trend persistence.
    """
    return (np.log(high.rolling(21).max() - low.rolling(21).min()) / np.log(21)).diff(63).diff(_TD_MON)

def frac_304_hurst_exponent_proxy_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_304_hurst_exponent_proxy_accel_126d
    ECONOMIC RATIONALE: Acceleration of hurst_exponent_proxy. Simplified Hurst exponent for trend persistence.
    """
    return (np.log(high.rolling(21).max() - low.rolling(21).min()) / np.log(21)).diff(126).diff(_TD_MON)

def frac_305_hurst_exponent_proxy_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_305_hurst_exponent_proxy_accel_252d
    ECONOMIC RATIONALE: Acceleration of hurst_exponent_proxy. Simplified Hurst exponent for trend persistence.
    """
    return (np.log(high.rolling(21).max() - low.rolling(21).min()) / np.log(21)).diff(252).diff(_TD_MON)

def frac_306_fractal_dimension_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_306_fractal_dimension_accel_5d
    ECONOMIC RATIONALE: Acceleration of fractal_dimension. Estimated fractal dimension.
    """
    return ((np.log(high.rolling(21).max() - low.rolling(21).min()) - np.log(high.rolling(5).max() - low.rolling(5).min())) / np.log(21/5)).diff(5).diff(_TD_MON)

def frac_307_fractal_dimension_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_307_fractal_dimension_accel_21d
    ECONOMIC RATIONALE: Acceleration of fractal_dimension. Estimated fractal dimension.
    """
    return ((np.log(high.rolling(21).max() - low.rolling(21).min()) - np.log(high.rolling(5).max() - low.rolling(5).min())) / np.log(21/5)).diff(21).diff(_TD_MON)

def frac_308_fractal_dimension_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_308_fractal_dimension_accel_63d
    ECONOMIC RATIONALE: Acceleration of fractal_dimension. Estimated fractal dimension.
    """
    return ((np.log(high.rolling(21).max() - low.rolling(21).min()) - np.log(high.rolling(5).max() - low.rolling(5).min())) / np.log(21/5)).diff(63).diff(_TD_MON)

def frac_309_fractal_dimension_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_309_fractal_dimension_accel_126d
    ECONOMIC RATIONALE: Acceleration of fractal_dimension. Estimated fractal dimension.
    """
    return ((np.log(high.rolling(21).max() - low.rolling(21).min()) - np.log(high.rolling(5).max() - low.rolling(5).min())) / np.log(21/5)).diff(126).diff(_TD_MON)

def frac_310_fractal_dimension_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_310_fractal_dimension_accel_252d
    ECONOMIC RATIONALE: Acceleration of fractal_dimension. Estimated fractal dimension.
    """
    return ((np.log(high.rolling(21).max() - low.rolling(21).min()) - np.log(high.rolling(5).max() - low.rolling(5).min())) / np.log(21/5)).diff(252).diff(_TD_MON)

def frac_311_efficiency_ratio_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_311_efficiency_ratio_accel_5d
    ECONOMIC RATIONALE: Acceleration of efficiency_ratio. Kaufman's Efficiency Ratio.
    """
    return (abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)).diff(5).diff(_TD_MON)

def frac_312_efficiency_ratio_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_312_efficiency_ratio_accel_21d
    ECONOMIC RATIONALE: Acceleration of efficiency_ratio. Kaufman's Efficiency Ratio.
    """
    return (abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)).diff(21).diff(_TD_MON)

def frac_313_efficiency_ratio_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_313_efficiency_ratio_accel_63d
    ECONOMIC RATIONALE: Acceleration of efficiency_ratio. Kaufman's Efficiency Ratio.
    """
    return (abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)).diff(63).diff(_TD_MON)

def frac_314_efficiency_ratio_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_314_efficiency_ratio_accel_126d
    ECONOMIC RATIONALE: Acceleration of efficiency_ratio. Kaufman's Efficiency Ratio.
    """
    return (abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)).diff(126).diff(_TD_MON)

def frac_315_efficiency_ratio_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_315_efficiency_ratio_accel_252d
    ECONOMIC RATIONALE: Acceleration of efficiency_ratio. Kaufman's Efficiency Ratio.
    """
    return (abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)).diff(252).diff(_TD_MON)

def frac_316_fractal_volatility_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_316_fractal_volatility_accel_5d
    ECONOMIC RATIONALE: Acceleration of fractal_volatility. Complexity of price path relative to range.
    """
    return (close.diff(1).abs().rolling(63).sum() / (high.rolling(63).max() - low.rolling(63).min()).replace(0, 1e-9)).diff(5).diff(_TD_MON)

def frac_317_fractal_volatility_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_317_fractal_volatility_accel_21d
    ECONOMIC RATIONALE: Acceleration of fractal_volatility. Complexity of price path relative to range.
    """
    return (close.diff(1).abs().rolling(63).sum() / (high.rolling(63).max() - low.rolling(63).min()).replace(0, 1e-9)).diff(21).diff(_TD_MON)

def frac_318_fractal_volatility_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_318_fractal_volatility_accel_63d
    ECONOMIC RATIONALE: Acceleration of fractal_volatility. Complexity of price path relative to range.
    """
    return (close.diff(1).abs().rolling(63).sum() / (high.rolling(63).max() - low.rolling(63).min()).replace(0, 1e-9)).diff(63).diff(_TD_MON)

def frac_319_fractal_volatility_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_319_fractal_volatility_accel_126d
    ECONOMIC RATIONALE: Acceleration of fractal_volatility. Complexity of price path relative to range.
    """
    return (close.diff(1).abs().rolling(63).sum() / (high.rolling(63).max() - low.rolling(63).min()).replace(0, 1e-9)).diff(126).diff(_TD_MON)

def frac_320_fractal_volatility_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_320_fractal_volatility_accel_252d
    ECONOMIC RATIONALE: Acceleration of fractal_volatility. Complexity of price path relative to range.
    """
    return (close.diff(1).abs().rolling(63).sum() / (high.rolling(63).max() - low.rolling(63).min()).replace(0, 1e-9)).diff(252).diff(_TD_MON)

def frac_321_self_similarity_score_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_321_self_similarity_score_accel_5d
    ECONOMIC RATIONALE: Acceleration of self_similarity_score. Correlation of returns with lagged returns.
    """
    return (close.pct_change(5).rolling(21).corr(close.pct_change(5).shift(5))).diff(5).diff(_TD_MON)

def frac_322_self_similarity_score_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_322_self_similarity_score_accel_21d
    ECONOMIC RATIONALE: Acceleration of self_similarity_score. Correlation of returns with lagged returns.
    """
    return (close.pct_change(5).rolling(21).corr(close.pct_change(5).shift(5))).diff(21).diff(_TD_MON)

def frac_323_self_similarity_score_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_323_self_similarity_score_accel_63d
    ECONOMIC RATIONALE: Acceleration of self_similarity_score. Correlation of returns with lagged returns.
    """
    return (close.pct_change(5).rolling(21).corr(close.pct_change(5).shift(5))).diff(63).diff(_TD_MON)

def frac_324_self_similarity_score_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_324_self_similarity_score_accel_126d
    ECONOMIC RATIONALE: Acceleration of self_similarity_score. Correlation of returns with lagged returns.
    """
    return (close.pct_change(5).rolling(21).corr(close.pct_change(5).shift(5))).diff(126).diff(_TD_MON)

def frac_325_self_similarity_score_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_325_self_similarity_score_accel_252d
    ECONOMIC RATIONALE: Acceleration of self_similarity_score. Correlation of returns with lagged returns.
    """
    return (close.pct_change(5).rolling(21).corr(close.pct_change(5).shift(5))).diff(252).diff(_TD_MON)

def frac_326_fractal_breakout_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_326_fractal_breakout_accel_5d
    ECONOMIC RATIONALE: Acceleration of fractal_breakout. Breakout of local fractal peaks.
    """
    return ((high > high.rolling(20).max().shift(1)).astype(float)).diff(5).diff(_TD_MON)

def frac_327_fractal_breakout_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_327_fractal_breakout_accel_21d
    ECONOMIC RATIONALE: Acceleration of fractal_breakout. Breakout of local fractal peaks.
    """
    return ((high > high.rolling(20).max().shift(1)).astype(float)).diff(21).diff(_TD_MON)

def frac_328_fractal_breakout_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_328_fractal_breakout_accel_63d
    ECONOMIC RATIONALE: Acceleration of fractal_breakout. Breakout of local fractal peaks.
    """
    return ((high > high.rolling(20).max().shift(1)).astype(float)).diff(63).diff(_TD_MON)

def frac_329_fractal_breakout_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_329_fractal_breakout_accel_126d
    ECONOMIC RATIONALE: Acceleration of fractal_breakout. Breakout of local fractal peaks.
    """
    return ((high > high.rolling(20).max().shift(1)).astype(float)).diff(126).diff(_TD_MON)

def frac_330_fractal_breakout_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_330_fractal_breakout_accel_252d
    ECONOMIC RATIONALE: Acceleration of fractal_breakout. Breakout of local fractal peaks.
    """
    return ((high > high.rolling(20).max().shift(1)).astype(float)).diff(252).diff(_TD_MON)

def frac_331_fractal_support_violation_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_331_fractal_support_violation_accel_5d
    ECONOMIC RATIONALE: Acceleration of fractal_support_violation. Breakdown of local fractal troughs.
    """
    return ((low < low.rolling(20).min().shift(1)).astype(float)).diff(5).diff(_TD_MON)

def frac_332_fractal_support_violation_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_332_fractal_support_violation_accel_21d
    ECONOMIC RATIONALE: Acceleration of fractal_support_violation. Breakdown of local fractal troughs.
    """
    return ((low < low.rolling(20).min().shift(1)).astype(float)).diff(21).diff(_TD_MON)

def frac_333_fractal_support_violation_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_333_fractal_support_violation_accel_63d
    ECONOMIC RATIONALE: Acceleration of fractal_support_violation. Breakdown of local fractal troughs.
    """
    return ((low < low.rolling(20).min().shift(1)).astype(float)).diff(63).diff(_TD_MON)

def frac_334_fractal_support_violation_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_334_fractal_support_violation_accel_126d
    ECONOMIC RATIONALE: Acceleration of fractal_support_violation. Breakdown of local fractal troughs.
    """
    return ((low < low.rolling(20).min().shift(1)).astype(float)).diff(126).diff(_TD_MON)

def frac_335_fractal_support_violation_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_335_fractal_support_violation_accel_252d
    ECONOMIC RATIONALE: Acceleration of fractal_support_violation. Breakdown of local fractal troughs.
    """
    return ((low < low.rolling(20).min().shift(1)).astype(float)).diff(252).diff(_TD_MON)

def frac_336_chaos_theory_osc_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_336_chaos_theory_osc_accel_5d
    ECONOMIC RATIONALE: Acceleration of chaos_theory_osc. Noise-adjusted short-term momentum.
    """
    return (close.pct_change(1) / close.pct_change(5).rolling(21).std()).diff(5).diff(_TD_MON)

def frac_337_chaos_theory_osc_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_337_chaos_theory_osc_accel_21d
    ECONOMIC RATIONALE: Acceleration of chaos_theory_osc. Noise-adjusted short-term momentum.
    """
    return (close.pct_change(1) / close.pct_change(5).rolling(21).std()).diff(21).diff(_TD_MON)

def frac_338_chaos_theory_osc_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_338_chaos_theory_osc_accel_63d
    ECONOMIC RATIONALE: Acceleration of chaos_theory_osc. Noise-adjusted short-term momentum.
    """
    return (close.pct_change(1) / close.pct_change(5).rolling(21).std()).diff(63).diff(_TD_MON)

def frac_339_chaos_theory_osc_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_339_chaos_theory_osc_accel_126d
    ECONOMIC RATIONALE: Acceleration of chaos_theory_osc. Noise-adjusted short-term momentum.
    """
    return (close.pct_change(1) / close.pct_change(5).rolling(21).std()).diff(126).diff(_TD_MON)

def frac_340_chaos_theory_osc_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_340_chaos_theory_osc_accel_252d
    ECONOMIC RATIONALE: Acceleration of chaos_theory_osc. Noise-adjusted short-term momentum.
    """
    return (close.pct_change(1) / close.pct_change(5).rolling(21).std()).diff(252).diff(_TD_MON)

def frac_341_entropy_proxy_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_341_entropy_proxy_accel_5d
    ECONOMIC RATIONALE: Acceleration of entropy_proxy. Approximate entropy of price distribution.
    """
    return (close.rolling(21).apply(lambda x: -np.sum(np.histogram(x, bins=10, density=True)[0] * np.log(np.histogram(x, bins=10, density=True)[0] + 1e-9)))).diff(5).diff(_TD_MON)

def frac_342_entropy_proxy_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_342_entropy_proxy_accel_21d
    ECONOMIC RATIONALE: Acceleration of entropy_proxy. Approximate entropy of price distribution.
    """
    return (close.rolling(21).apply(lambda x: -np.sum(np.histogram(x, bins=10, density=True)[0] * np.log(np.histogram(x, bins=10, density=True)[0] + 1e-9)))).diff(21).diff(_TD_MON)

def frac_343_entropy_proxy_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_343_entropy_proxy_accel_63d
    ECONOMIC RATIONALE: Acceleration of entropy_proxy. Approximate entropy of price distribution.
    """
    return (close.rolling(21).apply(lambda x: -np.sum(np.histogram(x, bins=10, density=True)[0] * np.log(np.histogram(x, bins=10, density=True)[0] + 1e-9)))).diff(63).diff(_TD_MON)

def frac_344_entropy_proxy_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_344_entropy_proxy_accel_126d
    ECONOMIC RATIONALE: Acceleration of entropy_proxy. Approximate entropy of price distribution.
    """
    return (close.rolling(21).apply(lambda x: -np.sum(np.histogram(x, bins=10, density=True)[0] * np.log(np.histogram(x, bins=10, density=True)[0] + 1e-9)))).diff(126).diff(_TD_MON)

def frac_345_entropy_proxy_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_345_entropy_proxy_accel_252d
    ECONOMIC RATIONALE: Acceleration of entropy_proxy. Approximate entropy of price distribution.
    """
    return (close.rolling(21).apply(lambda x: -np.sum(np.histogram(x, bins=10, density=True)[0] * np.log(np.histogram(x, bins=10, density=True)[0] + 1e-9)))).diff(252).diff(_TD_MON)

def frac_346_fractal_energy_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_346_fractal_energy_accel_5d
    ECONOMIC RATIONALE: Acceleration of fractal_energy. Energy dissipated in price movement.
    """
    return (close.diff(1).pow(2).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min()).pow(2)).diff(5).diff(_TD_MON)

def frac_347_fractal_energy_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_347_fractal_energy_accel_21d
    ECONOMIC RATIONALE: Acceleration of fractal_energy. Energy dissipated in price movement.
    """
    return (close.diff(1).pow(2).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min()).pow(2)).diff(21).diff(_TD_MON)

def frac_348_fractal_energy_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_348_fractal_energy_accel_63d
    ECONOMIC RATIONALE: Acceleration of fractal_energy. Energy dissipated in price movement.
    """
    return (close.diff(1).pow(2).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min()).pow(2)).diff(63).diff(_TD_MON)

def frac_349_fractal_energy_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_349_fractal_energy_accel_126d
    ECONOMIC RATIONALE: Acceleration of fractal_energy. Energy dissipated in price movement.
    """
    return (close.diff(1).pow(2).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min()).pow(2)).diff(126).diff(_TD_MON)

def frac_350_fractal_energy_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_350_fractal_energy_accel_252d
    ECONOMIC RATIONALE: Acceleration of fractal_energy. Energy dissipated in price movement.
    """
    return (close.diff(1).pow(2).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min()).pow(2)).diff(252).diff(_TD_MON)

def frac_351_multi_scale_vol_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_351_multi_scale_vol_accel_5d
    ECONOMIC RATIONALE: Acceleration of multi_scale_vol. Ratio of short-term to long-term volatility structure.
    """
    return (close.rolling(5).std() / close.rolling(63).std()).diff(5).diff(_TD_MON)

def frac_352_multi_scale_vol_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_352_multi_scale_vol_accel_21d
    ECONOMIC RATIONALE: Acceleration of multi_scale_vol. Ratio of short-term to long-term volatility structure.
    """
    return (close.rolling(5).std() / close.rolling(63).std()).diff(21).diff(_TD_MON)

def frac_353_multi_scale_vol_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_353_multi_scale_vol_accel_63d
    ECONOMIC RATIONALE: Acceleration of multi_scale_vol. Ratio of short-term to long-term volatility structure.
    """
    return (close.rolling(5).std() / close.rolling(63).std()).diff(63).diff(_TD_MON)

def frac_354_multi_scale_vol_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_354_multi_scale_vol_accel_126d
    ECONOMIC RATIONALE: Acceleration of multi_scale_vol. Ratio of short-term to long-term volatility structure.
    """
    return (close.rolling(5).std() / close.rolling(63).std()).diff(126).diff(_TD_MON)

def frac_355_multi_scale_vol_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_355_multi_scale_vol_accel_252d
    ECONOMIC RATIONALE: Acceleration of multi_scale_vol. Ratio of short-term to long-term volatility structure.
    """
    return (close.rolling(5).std() / close.rolling(63).std()).diff(252).diff(_TD_MON)

def frac_356_fractal_regime_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_356_fractal_regime_accel_5d
    ECONOMIC RATIONALE: Acceleration of fractal_regime. Fractal trend of moving average changes.
    """
    return (close.rolling(21).mean().diff(5).rolling(63).mean()).diff(5).diff(_TD_MON)

def frac_357_fractal_regime_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_357_fractal_regime_accel_21d
    ECONOMIC RATIONALE: Acceleration of fractal_regime. Fractal trend of moving average changes.
    """
    return (close.rolling(21).mean().diff(5).rolling(63).mean()).diff(21).diff(_TD_MON)

def frac_358_fractal_regime_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_358_fractal_regime_accel_63d
    ECONOMIC RATIONALE: Acceleration of fractal_regime. Fractal trend of moving average changes.
    """
    return (close.rolling(21).mean().diff(5).rolling(63).mean()).diff(63).diff(_TD_MON)

def frac_359_fractal_regime_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_359_fractal_regime_accel_126d
    ECONOMIC RATIONALE: Acceleration of fractal_regime. Fractal trend of moving average changes.
    """
    return (close.rolling(21).mean().diff(5).rolling(63).mean()).diff(126).diff(_TD_MON)

def frac_360_fractal_regime_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_360_fractal_regime_accel_252d
    ECONOMIC RATIONALE: Acceleration of fractal_regime. Fractal trend of moving average changes.
    """
    return (close.rolling(21).mean().diff(5).rolling(63).mean()).diff(252).diff(_TD_MON)

def frac_361_box_counting_proxy_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_361_box_counting_proxy_accel_5d
    ECONOMIC RATIONALE: Acceleration of box_counting_proxy. Box-counting dimension approximation.
    """
    return (((high.rolling(10).max() - low.rolling(10).min()) + (high.rolling(10).max().shift(10) - low.rolling(10).min().shift(10))) / (high.rolling(20).max() - low.rolling(20).min())).diff(5).diff(_TD_MON)

def frac_362_box_counting_proxy_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_362_box_counting_proxy_accel_21d
    ECONOMIC RATIONALE: Acceleration of box_counting_proxy. Box-counting dimension approximation.
    """
    return (((high.rolling(10).max() - low.rolling(10).min()) + (high.rolling(10).max().shift(10) - low.rolling(10).min().shift(10))) / (high.rolling(20).max() - low.rolling(20).min())).diff(21).diff(_TD_MON)

def frac_363_box_counting_proxy_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_363_box_counting_proxy_accel_63d
    ECONOMIC RATIONALE: Acceleration of box_counting_proxy. Box-counting dimension approximation.
    """
    return (((high.rolling(10).max() - low.rolling(10).min()) + (high.rolling(10).max().shift(10) - low.rolling(10).min().shift(10))) / (high.rolling(20).max() - low.rolling(20).min())).diff(63).diff(_TD_MON)

def frac_364_box_counting_proxy_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_364_box_counting_proxy_accel_126d
    ECONOMIC RATIONALE: Acceleration of box_counting_proxy. Box-counting dimension approximation.
    """
    return (((high.rolling(10).max() - low.rolling(10).min()) + (high.rolling(10).max().shift(10) - low.rolling(10).min().shift(10))) / (high.rolling(20).max() - low.rolling(20).min())).diff(126).diff(_TD_MON)

def frac_365_box_counting_proxy_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_365_box_counting_proxy_accel_252d
    ECONOMIC RATIONALE: Acceleration of box_counting_proxy. Box-counting dimension approximation.
    """
    return (((high.rolling(10).max() - low.rolling(10).min()) + (high.rolling(10).max().shift(10) - low.rolling(10).min().shift(10))) / (high.rolling(20).max() - low.rolling(20).min())).diff(252).diff(_TD_MON)

def frac_366_fractal_trend_index_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_366_fractal_trend_index_accel_5d
    ECONOMIC RATIONALE: Acceleration of fractal_trend_index. Trend magnitude relative to structural range.
    """
    return (close.diff(63) / (high.rolling(63).max() - low.rolling(63).min())).diff(5).diff(_TD_MON)

def frac_367_fractal_trend_index_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_367_fractal_trend_index_accel_21d
    ECONOMIC RATIONALE: Acceleration of fractal_trend_index. Trend magnitude relative to structural range.
    """
    return (close.diff(63) / (high.rolling(63).max() - low.rolling(63).min())).diff(21).diff(_TD_MON)

def frac_368_fractal_trend_index_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_368_fractal_trend_index_accel_63d
    ECONOMIC RATIONALE: Acceleration of fractal_trend_index. Trend magnitude relative to structural range.
    """
    return (close.diff(63) / (high.rolling(63).max() - low.rolling(63).min())).diff(63).diff(_TD_MON)

def frac_369_fractal_trend_index_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_369_fractal_trend_index_accel_126d
    ECONOMIC RATIONALE: Acceleration of fractal_trend_index. Trend magnitude relative to structural range.
    """
    return (close.diff(63) / (high.rolling(63).max() - low.rolling(63).min())).diff(126).diff(_TD_MON)

def frac_370_fractal_trend_index_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_370_fractal_trend_index_accel_252d
    ECONOMIC RATIONALE: Acceleration of fractal_trend_index. Trend magnitude relative to structural range.
    """
    return (close.diff(63) / (high.rolling(63).max() - low.rolling(63).min())).diff(252).diff(_TD_MON)

def frac_371_fractal_noise_ratio_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_371_fractal_noise_ratio_accel_5d
    ECONOMIC RATIONALE: Acceleration of fractal_noise_ratio. Proportion of price movement attributed to noise.
    """
    return (1 - efficiency_ratio).diff(5).diff(_TD_MON)

def frac_372_fractal_noise_ratio_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_372_fractal_noise_ratio_accel_21d
    ECONOMIC RATIONALE: Acceleration of fractal_noise_ratio. Proportion of price movement attributed to noise.
    """
    return (1 - efficiency_ratio).diff(21).diff(_TD_MON)

def frac_373_fractal_noise_ratio_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_373_fractal_noise_ratio_accel_63d
    ECONOMIC RATIONALE: Acceleration of fractal_noise_ratio. Proportion of price movement attributed to noise.
    """
    return (1 - efficiency_ratio).diff(63).diff(_TD_MON)

def frac_374_fractal_noise_ratio_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_374_fractal_noise_ratio_accel_126d
    ECONOMIC RATIONALE: Acceleration of fractal_noise_ratio. Proportion of price movement attributed to noise.
    """
    return (1 - efficiency_ratio).diff(126).diff(_TD_MON)

def frac_375_fractal_noise_ratio_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_375_fractal_noise_ratio_accel_252d
    ECONOMIC RATIONALE: Acceleration of fractal_noise_ratio. Proportion of price movement attributed to noise.
    """
    return (1 - efficiency_ratio).diff(252).diff(_TD_MON)

# ── Registry ──────────────────────────────────────────────────────────────────
V105_REGISTRY_ACCEL = {
    "frac_301_hurst_exponent_proxy_accel_5d": {"inputs": ["close", "high", "low"], "func": frac_301_hurst_exponent_proxy_accel_5d},
    "frac_302_hurst_exponent_proxy_accel_21d": {"inputs": ["close", "high", "low"], "func": frac_302_hurst_exponent_proxy_accel_21d},
    "frac_303_hurst_exponent_proxy_accel_63d": {"inputs": ["close", "high", "low"], "func": frac_303_hurst_exponent_proxy_accel_63d},
    "frac_304_hurst_exponent_proxy_accel_126d": {"inputs": ["close", "high", "low"], "func": frac_304_hurst_exponent_proxy_accel_126d},
    "frac_305_hurst_exponent_proxy_accel_252d": {"inputs": ["close", "high", "low"], "func": frac_305_hurst_exponent_proxy_accel_252d},
    "frac_306_fractal_dimension_accel_5d": {"inputs": ["close", "high", "low"], "func": frac_306_fractal_dimension_accel_5d},
    "frac_307_fractal_dimension_accel_21d": {"inputs": ["close", "high", "low"], "func": frac_307_fractal_dimension_accel_21d},
    "frac_308_fractal_dimension_accel_63d": {"inputs": ["close", "high", "low"], "func": frac_308_fractal_dimension_accel_63d},
    "frac_309_fractal_dimension_accel_126d": {"inputs": ["close", "high", "low"], "func": frac_309_fractal_dimension_accel_126d},
    "frac_310_fractal_dimension_accel_252d": {"inputs": ["close", "high", "low"], "func": frac_310_fractal_dimension_accel_252d},
    "frac_311_efficiency_ratio_accel_5d": {"inputs": ["close", "high", "low"], "func": frac_311_efficiency_ratio_accel_5d},
    "frac_312_efficiency_ratio_accel_21d": {"inputs": ["close", "high", "low"], "func": frac_312_efficiency_ratio_accel_21d},
    "frac_313_efficiency_ratio_accel_63d": {"inputs": ["close", "high", "low"], "func": frac_313_efficiency_ratio_accel_63d},
    "frac_314_efficiency_ratio_accel_126d": {"inputs": ["close", "high", "low"], "func": frac_314_efficiency_ratio_accel_126d},
    "frac_315_efficiency_ratio_accel_252d": {"inputs": ["close", "high", "low"], "func": frac_315_efficiency_ratio_accel_252d},
    "frac_316_fractal_volatility_accel_5d": {"inputs": ["close", "high", "low"], "func": frac_316_fractal_volatility_accel_5d},
    "frac_317_fractal_volatility_accel_21d": {"inputs": ["close", "high", "low"], "func": frac_317_fractal_volatility_accel_21d},
    "frac_318_fractal_volatility_accel_63d": {"inputs": ["close", "high", "low"], "func": frac_318_fractal_volatility_accel_63d},
    "frac_319_fractal_volatility_accel_126d": {"inputs": ["close", "high", "low"], "func": frac_319_fractal_volatility_accel_126d},
    "frac_320_fractal_volatility_accel_252d": {"inputs": ["close", "high", "low"], "func": frac_320_fractal_volatility_accel_252d},
    "frac_321_self_similarity_score_accel_5d": {"inputs": ["close", "high", "low"], "func": frac_321_self_similarity_score_accel_5d},
    "frac_322_self_similarity_score_accel_21d": {"inputs": ["close", "high", "low"], "func": frac_322_self_similarity_score_accel_21d},
    "frac_323_self_similarity_score_accel_63d": {"inputs": ["close", "high", "low"], "func": frac_323_self_similarity_score_accel_63d},
    "frac_324_self_similarity_score_accel_126d": {"inputs": ["close", "high", "low"], "func": frac_324_self_similarity_score_accel_126d},
    "frac_325_self_similarity_score_accel_252d": {"inputs": ["close", "high", "low"], "func": frac_325_self_similarity_score_accel_252d},
    "frac_326_fractal_breakout_accel_5d": {"inputs": ["close", "high", "low"], "func": frac_326_fractal_breakout_accel_5d},
    "frac_327_fractal_breakout_accel_21d": {"inputs": ["close", "high", "low"], "func": frac_327_fractal_breakout_accel_21d},
    "frac_328_fractal_breakout_accel_63d": {"inputs": ["close", "high", "low"], "func": frac_328_fractal_breakout_accel_63d},
    "frac_329_fractal_breakout_accel_126d": {"inputs": ["close", "high", "low"], "func": frac_329_fractal_breakout_accel_126d},
    "frac_330_fractal_breakout_accel_252d": {"inputs": ["close", "high", "low"], "func": frac_330_fractal_breakout_accel_252d},
    "frac_331_fractal_support_violation_accel_5d": {"inputs": ["close", "high", "low"], "func": frac_331_fractal_support_violation_accel_5d},
    "frac_332_fractal_support_violation_accel_21d": {"inputs": ["close", "high", "low"], "func": frac_332_fractal_support_violation_accel_21d},
    "frac_333_fractal_support_violation_accel_63d": {"inputs": ["close", "high", "low"], "func": frac_333_fractal_support_violation_accel_63d},
    "frac_334_fractal_support_violation_accel_126d": {"inputs": ["close", "high", "low"], "func": frac_334_fractal_support_violation_accel_126d},
    "frac_335_fractal_support_violation_accel_252d": {"inputs": ["close", "high", "low"], "func": frac_335_fractal_support_violation_accel_252d},
    "frac_336_chaos_theory_osc_accel_5d": {"inputs": ["close", "high", "low"], "func": frac_336_chaos_theory_osc_accel_5d},
    "frac_337_chaos_theory_osc_accel_21d": {"inputs": ["close", "high", "low"], "func": frac_337_chaos_theory_osc_accel_21d},
    "frac_338_chaos_theory_osc_accel_63d": {"inputs": ["close", "high", "low"], "func": frac_338_chaos_theory_osc_accel_63d},
    "frac_339_chaos_theory_osc_accel_126d": {"inputs": ["close", "high", "low"], "func": frac_339_chaos_theory_osc_accel_126d},
    "frac_340_chaos_theory_osc_accel_252d": {"inputs": ["close", "high", "low"], "func": frac_340_chaos_theory_osc_accel_252d},
    "frac_341_entropy_proxy_accel_5d": {"inputs": ["close", "high", "low"], "func": frac_341_entropy_proxy_accel_5d},
    "frac_342_entropy_proxy_accel_21d": {"inputs": ["close", "high", "low"], "func": frac_342_entropy_proxy_accel_21d},
    "frac_343_entropy_proxy_accel_63d": {"inputs": ["close", "high", "low"], "func": frac_343_entropy_proxy_accel_63d},
    "frac_344_entropy_proxy_accel_126d": {"inputs": ["close", "high", "low"], "func": frac_344_entropy_proxy_accel_126d},
    "frac_345_entropy_proxy_accel_252d": {"inputs": ["close", "high", "low"], "func": frac_345_entropy_proxy_accel_252d},
    "frac_346_fractal_energy_accel_5d": {"inputs": ["close", "high", "low"], "func": frac_346_fractal_energy_accel_5d},
    "frac_347_fractal_energy_accel_21d": {"inputs": ["close", "high", "low"], "func": frac_347_fractal_energy_accel_21d},
    "frac_348_fractal_energy_accel_63d": {"inputs": ["close", "high", "low"], "func": frac_348_fractal_energy_accel_63d},
    "frac_349_fractal_energy_accel_126d": {"inputs": ["close", "high", "low"], "func": frac_349_fractal_energy_accel_126d},
    "frac_350_fractal_energy_accel_252d": {"inputs": ["close", "high", "low"], "func": frac_350_fractal_energy_accel_252d},
    "frac_351_multi_scale_vol_accel_5d": {"inputs": ["close", "high", "low"], "func": frac_351_multi_scale_vol_accel_5d},
    "frac_352_multi_scale_vol_accel_21d": {"inputs": ["close", "high", "low"], "func": frac_352_multi_scale_vol_accel_21d},
    "frac_353_multi_scale_vol_accel_63d": {"inputs": ["close", "high", "low"], "func": frac_353_multi_scale_vol_accel_63d},
    "frac_354_multi_scale_vol_accel_126d": {"inputs": ["close", "high", "low"], "func": frac_354_multi_scale_vol_accel_126d},
    "frac_355_multi_scale_vol_accel_252d": {"inputs": ["close", "high", "low"], "func": frac_355_multi_scale_vol_accel_252d},
    "frac_356_fractal_regime_accel_5d": {"inputs": ["close", "high", "low"], "func": frac_356_fractal_regime_accel_5d},
    "frac_357_fractal_regime_accel_21d": {"inputs": ["close", "high", "low"], "func": frac_357_fractal_regime_accel_21d},
    "frac_358_fractal_regime_accel_63d": {"inputs": ["close", "high", "low"], "func": frac_358_fractal_regime_accel_63d},
    "frac_359_fractal_regime_accel_126d": {"inputs": ["close", "high", "low"], "func": frac_359_fractal_regime_accel_126d},
    "frac_360_fractal_regime_accel_252d": {"inputs": ["close", "high", "low"], "func": frac_360_fractal_regime_accel_252d},
    "frac_361_box_counting_proxy_accel_5d": {"inputs": ["close", "high", "low"], "func": frac_361_box_counting_proxy_accel_5d},
    "frac_362_box_counting_proxy_accel_21d": {"inputs": ["close", "high", "low"], "func": frac_362_box_counting_proxy_accel_21d},
    "frac_363_box_counting_proxy_accel_63d": {"inputs": ["close", "high", "low"], "func": frac_363_box_counting_proxy_accel_63d},
    "frac_364_box_counting_proxy_accel_126d": {"inputs": ["close", "high", "low"], "func": frac_364_box_counting_proxy_accel_126d},
    "frac_365_box_counting_proxy_accel_252d": {"inputs": ["close", "high", "low"], "func": frac_365_box_counting_proxy_accel_252d},
    "frac_366_fractal_trend_index_accel_5d": {"inputs": ["close", "high", "low"], "func": frac_366_fractal_trend_index_accel_5d},
    "frac_367_fractal_trend_index_accel_21d": {"inputs": ["close", "high", "low"], "func": frac_367_fractal_trend_index_accel_21d},
    "frac_368_fractal_trend_index_accel_63d": {"inputs": ["close", "high", "low"], "func": frac_368_fractal_trend_index_accel_63d},
    "frac_369_fractal_trend_index_accel_126d": {"inputs": ["close", "high", "low"], "func": frac_369_fractal_trend_index_accel_126d},
    "frac_370_fractal_trend_index_accel_252d": {"inputs": ["close", "high", "low"], "func": frac_370_fractal_trend_index_accel_252d},
    "frac_371_fractal_noise_ratio_accel_5d": {"inputs": ["close", "high", "low"], "func": frac_371_fractal_noise_ratio_accel_5d},
    "frac_372_fractal_noise_ratio_accel_21d": {"inputs": ["close", "high", "low"], "func": frac_372_fractal_noise_ratio_accel_21d},
    "frac_373_fractal_noise_ratio_accel_63d": {"inputs": ["close", "high", "low"], "func": frac_373_fractal_noise_ratio_accel_63d},
    "frac_374_fractal_noise_ratio_accel_126d": {"inputs": ["close", "high", "low"], "func": frac_374_fractal_noise_ratio_accel_126d},
    "frac_375_fractal_noise_ratio_accel_252d": {"inputs": ["close", "high", "low"], "func": frac_375_fractal_noise_ratio_accel_252d},
}
