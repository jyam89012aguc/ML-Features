"""
105_fractal_structure — Velocity (2nd Derivatives)
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

def frac_226_hurst_exponent_proxy_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_226_hurst_exponent_proxy_vel_5d
    ECONOMIC RATIONALE: Velocity of hurst_exponent_proxy. Simplified Hurst exponent for trend persistence.
    """
    return (np.log(high.rolling(21).max() - low.rolling(21).min()) / np.log(21)).diff(5)

def frac_227_hurst_exponent_proxy_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_227_hurst_exponent_proxy_vel_21d
    ECONOMIC RATIONALE: Velocity of hurst_exponent_proxy. Simplified Hurst exponent for trend persistence.
    """
    return (np.log(high.rolling(21).max() - low.rolling(21).min()) / np.log(21)).diff(21)

def frac_228_hurst_exponent_proxy_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_228_hurst_exponent_proxy_vel_63d
    ECONOMIC RATIONALE: Velocity of hurst_exponent_proxy. Simplified Hurst exponent for trend persistence.
    """
    return (np.log(high.rolling(21).max() - low.rolling(21).min()) / np.log(21)).diff(63)

def frac_229_hurst_exponent_proxy_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_229_hurst_exponent_proxy_vel_126d
    ECONOMIC RATIONALE: Velocity of hurst_exponent_proxy. Simplified Hurst exponent for trend persistence.
    """
    return (np.log(high.rolling(21).max() - low.rolling(21).min()) / np.log(21)).diff(126)

def frac_230_hurst_exponent_proxy_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_230_hurst_exponent_proxy_vel_252d
    ECONOMIC RATIONALE: Velocity of hurst_exponent_proxy. Simplified Hurst exponent for trend persistence.
    """
    return (np.log(high.rolling(21).max() - low.rolling(21).min()) / np.log(21)).diff(252)

def frac_231_fractal_dimension_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_231_fractal_dimension_vel_5d
    ECONOMIC RATIONALE: Velocity of fractal_dimension. Estimated fractal dimension.
    """
    return ((np.log(high.rolling(21).max() - low.rolling(21).min()) - np.log(high.rolling(5).max() - low.rolling(5).min())) / np.log(21/5)).diff(5)

def frac_232_fractal_dimension_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_232_fractal_dimension_vel_21d
    ECONOMIC RATIONALE: Velocity of fractal_dimension. Estimated fractal dimension.
    """
    return ((np.log(high.rolling(21).max() - low.rolling(21).min()) - np.log(high.rolling(5).max() - low.rolling(5).min())) / np.log(21/5)).diff(21)

def frac_233_fractal_dimension_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_233_fractal_dimension_vel_63d
    ECONOMIC RATIONALE: Velocity of fractal_dimension. Estimated fractal dimension.
    """
    return ((np.log(high.rolling(21).max() - low.rolling(21).min()) - np.log(high.rolling(5).max() - low.rolling(5).min())) / np.log(21/5)).diff(63)

def frac_234_fractal_dimension_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_234_fractal_dimension_vel_126d
    ECONOMIC RATIONALE: Velocity of fractal_dimension. Estimated fractal dimension.
    """
    return ((np.log(high.rolling(21).max() - low.rolling(21).min()) - np.log(high.rolling(5).max() - low.rolling(5).min())) / np.log(21/5)).diff(126)

def frac_235_fractal_dimension_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_235_fractal_dimension_vel_252d
    ECONOMIC RATIONALE: Velocity of fractal_dimension. Estimated fractal dimension.
    """
    return ((np.log(high.rolling(21).max() - low.rolling(21).min()) - np.log(high.rolling(5).max() - low.rolling(5).min())) / np.log(21/5)).diff(252)

def frac_236_efficiency_ratio_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_236_efficiency_ratio_vel_5d
    ECONOMIC RATIONALE: Velocity of efficiency_ratio. Kaufman's Efficiency Ratio.
    """
    return (abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)).diff(5)

def frac_237_efficiency_ratio_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_237_efficiency_ratio_vel_21d
    ECONOMIC RATIONALE: Velocity of efficiency_ratio. Kaufman's Efficiency Ratio.
    """
    return (abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)).diff(21)

def frac_238_efficiency_ratio_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_238_efficiency_ratio_vel_63d
    ECONOMIC RATIONALE: Velocity of efficiency_ratio. Kaufman's Efficiency Ratio.
    """
    return (abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)).diff(63)

def frac_239_efficiency_ratio_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_239_efficiency_ratio_vel_126d
    ECONOMIC RATIONALE: Velocity of efficiency_ratio. Kaufman's Efficiency Ratio.
    """
    return (abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)).diff(126)

def frac_240_efficiency_ratio_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_240_efficiency_ratio_vel_252d
    ECONOMIC RATIONALE: Velocity of efficiency_ratio. Kaufman's Efficiency Ratio.
    """
    return (abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)).diff(252)

def frac_241_fractal_volatility_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_241_fractal_volatility_vel_5d
    ECONOMIC RATIONALE: Velocity of fractal_volatility. Complexity of price path relative to range.
    """
    return (close.diff(1).abs().rolling(63).sum() / (high.rolling(63).max() - low.rolling(63).min()).replace(0, 1e-9)).diff(5)

def frac_242_fractal_volatility_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_242_fractal_volatility_vel_21d
    ECONOMIC RATIONALE: Velocity of fractal_volatility. Complexity of price path relative to range.
    """
    return (close.diff(1).abs().rolling(63).sum() / (high.rolling(63).max() - low.rolling(63).min()).replace(0, 1e-9)).diff(21)

def frac_243_fractal_volatility_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_243_fractal_volatility_vel_63d
    ECONOMIC RATIONALE: Velocity of fractal_volatility. Complexity of price path relative to range.
    """
    return (close.diff(1).abs().rolling(63).sum() / (high.rolling(63).max() - low.rolling(63).min()).replace(0, 1e-9)).diff(63)

def frac_244_fractal_volatility_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_244_fractal_volatility_vel_126d
    ECONOMIC RATIONALE: Velocity of fractal_volatility. Complexity of price path relative to range.
    """
    return (close.diff(1).abs().rolling(63).sum() / (high.rolling(63).max() - low.rolling(63).min()).replace(0, 1e-9)).diff(126)

def frac_245_fractal_volatility_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_245_fractal_volatility_vel_252d
    ECONOMIC RATIONALE: Velocity of fractal_volatility. Complexity of price path relative to range.
    """
    return (close.diff(1).abs().rolling(63).sum() / (high.rolling(63).max() - low.rolling(63).min()).replace(0, 1e-9)).diff(252)

def frac_246_self_similarity_score_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_246_self_similarity_score_vel_5d
    ECONOMIC RATIONALE: Velocity of self_similarity_score. Correlation of returns with lagged returns.
    """
    return (close.pct_change(5).rolling(21).corr(close.pct_change(5).shift(5))).diff(5)

def frac_247_self_similarity_score_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_247_self_similarity_score_vel_21d
    ECONOMIC RATIONALE: Velocity of self_similarity_score. Correlation of returns with lagged returns.
    """
    return (close.pct_change(5).rolling(21).corr(close.pct_change(5).shift(5))).diff(21)

def frac_248_self_similarity_score_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_248_self_similarity_score_vel_63d
    ECONOMIC RATIONALE: Velocity of self_similarity_score. Correlation of returns with lagged returns.
    """
    return (close.pct_change(5).rolling(21).corr(close.pct_change(5).shift(5))).diff(63)

def frac_249_self_similarity_score_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_249_self_similarity_score_vel_126d
    ECONOMIC RATIONALE: Velocity of self_similarity_score. Correlation of returns with lagged returns.
    """
    return (close.pct_change(5).rolling(21).corr(close.pct_change(5).shift(5))).diff(126)

def frac_250_self_similarity_score_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_250_self_similarity_score_vel_252d
    ECONOMIC RATIONALE: Velocity of self_similarity_score. Correlation of returns with lagged returns.
    """
    return (close.pct_change(5).rolling(21).corr(close.pct_change(5).shift(5))).diff(252)

def frac_251_fractal_breakout_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_251_fractal_breakout_vel_5d
    ECONOMIC RATIONALE: Velocity of fractal_breakout. Breakout of local fractal peaks.
    """
    return ((high > high.rolling(20).max().shift(1)).astype(float)).diff(5)

def frac_252_fractal_breakout_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_252_fractal_breakout_vel_21d
    ECONOMIC RATIONALE: Velocity of fractal_breakout. Breakout of local fractal peaks.
    """
    return ((high > high.rolling(20).max().shift(1)).astype(float)).diff(21)

def frac_253_fractal_breakout_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_253_fractal_breakout_vel_63d
    ECONOMIC RATIONALE: Velocity of fractal_breakout. Breakout of local fractal peaks.
    """
    return ((high > high.rolling(20).max().shift(1)).astype(float)).diff(63)

def frac_254_fractal_breakout_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_254_fractal_breakout_vel_126d
    ECONOMIC RATIONALE: Velocity of fractal_breakout. Breakout of local fractal peaks.
    """
    return ((high > high.rolling(20).max().shift(1)).astype(float)).diff(126)

def frac_255_fractal_breakout_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_255_fractal_breakout_vel_252d
    ECONOMIC RATIONALE: Velocity of fractal_breakout. Breakout of local fractal peaks.
    """
    return ((high > high.rolling(20).max().shift(1)).astype(float)).diff(252)

def frac_256_fractal_support_violation_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_256_fractal_support_violation_vel_5d
    ECONOMIC RATIONALE: Velocity of fractal_support_violation. Breakdown of local fractal troughs.
    """
    return ((low < low.rolling(20).min().shift(1)).astype(float)).diff(5)

def frac_257_fractal_support_violation_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_257_fractal_support_violation_vel_21d
    ECONOMIC RATIONALE: Velocity of fractal_support_violation. Breakdown of local fractal troughs.
    """
    return ((low < low.rolling(20).min().shift(1)).astype(float)).diff(21)

def frac_258_fractal_support_violation_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_258_fractal_support_violation_vel_63d
    ECONOMIC RATIONALE: Velocity of fractal_support_violation. Breakdown of local fractal troughs.
    """
    return ((low < low.rolling(20).min().shift(1)).astype(float)).diff(63)

def frac_259_fractal_support_violation_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_259_fractal_support_violation_vel_126d
    ECONOMIC RATIONALE: Velocity of fractal_support_violation. Breakdown of local fractal troughs.
    """
    return ((low < low.rolling(20).min().shift(1)).astype(float)).diff(126)

def frac_260_fractal_support_violation_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_260_fractal_support_violation_vel_252d
    ECONOMIC RATIONALE: Velocity of fractal_support_violation. Breakdown of local fractal troughs.
    """
    return ((low < low.rolling(20).min().shift(1)).astype(float)).diff(252)

def frac_261_chaos_theory_osc_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_261_chaos_theory_osc_vel_5d
    ECONOMIC RATIONALE: Velocity of chaos_theory_osc. Noise-adjusted short-term momentum.
    """
    return (close.pct_change(1) / close.pct_change(5).rolling(21).std()).diff(5)

def frac_262_chaos_theory_osc_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_262_chaos_theory_osc_vel_21d
    ECONOMIC RATIONALE: Velocity of chaos_theory_osc. Noise-adjusted short-term momentum.
    """
    return (close.pct_change(1) / close.pct_change(5).rolling(21).std()).diff(21)

def frac_263_chaos_theory_osc_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_263_chaos_theory_osc_vel_63d
    ECONOMIC RATIONALE: Velocity of chaos_theory_osc. Noise-adjusted short-term momentum.
    """
    return (close.pct_change(1) / close.pct_change(5).rolling(21).std()).diff(63)

def frac_264_chaos_theory_osc_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_264_chaos_theory_osc_vel_126d
    ECONOMIC RATIONALE: Velocity of chaos_theory_osc. Noise-adjusted short-term momentum.
    """
    return (close.pct_change(1) / close.pct_change(5).rolling(21).std()).diff(126)

def frac_265_chaos_theory_osc_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_265_chaos_theory_osc_vel_252d
    ECONOMIC RATIONALE: Velocity of chaos_theory_osc. Noise-adjusted short-term momentum.
    """
    return (close.pct_change(1) / close.pct_change(5).rolling(21).std()).diff(252)

def frac_266_entropy_proxy_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_266_entropy_proxy_vel_5d
    ECONOMIC RATIONALE: Velocity of entropy_proxy. Approximate entropy of price distribution.
    """
    return (close.rolling(21).apply(lambda x: -np.sum(np.histogram(x, bins=10, density=True)[0] * np.log(np.histogram(x, bins=10, density=True)[0] + 1e-9)))).diff(5)

def frac_267_entropy_proxy_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_267_entropy_proxy_vel_21d
    ECONOMIC RATIONALE: Velocity of entropy_proxy. Approximate entropy of price distribution.
    """
    return (close.rolling(21).apply(lambda x: -np.sum(np.histogram(x, bins=10, density=True)[0] * np.log(np.histogram(x, bins=10, density=True)[0] + 1e-9)))).diff(21)

def frac_268_entropy_proxy_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_268_entropy_proxy_vel_63d
    ECONOMIC RATIONALE: Velocity of entropy_proxy. Approximate entropy of price distribution.
    """
    return (close.rolling(21).apply(lambda x: -np.sum(np.histogram(x, bins=10, density=True)[0] * np.log(np.histogram(x, bins=10, density=True)[0] + 1e-9)))).diff(63)

def frac_269_entropy_proxy_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_269_entropy_proxy_vel_126d
    ECONOMIC RATIONALE: Velocity of entropy_proxy. Approximate entropy of price distribution.
    """
    return (close.rolling(21).apply(lambda x: -np.sum(np.histogram(x, bins=10, density=True)[0] * np.log(np.histogram(x, bins=10, density=True)[0] + 1e-9)))).diff(126)

def frac_270_entropy_proxy_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_270_entropy_proxy_vel_252d
    ECONOMIC RATIONALE: Velocity of entropy_proxy. Approximate entropy of price distribution.
    """
    return (close.rolling(21).apply(lambda x: -np.sum(np.histogram(x, bins=10, density=True)[0] * np.log(np.histogram(x, bins=10, density=True)[0] + 1e-9)))).diff(252)

def frac_271_fractal_energy_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_271_fractal_energy_vel_5d
    ECONOMIC RATIONALE: Velocity of fractal_energy. Energy dissipated in price movement.
    """
    return (close.diff(1).pow(2).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min()).pow(2)).diff(5)

def frac_272_fractal_energy_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_272_fractal_energy_vel_21d
    ECONOMIC RATIONALE: Velocity of fractal_energy. Energy dissipated in price movement.
    """
    return (close.diff(1).pow(2).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min()).pow(2)).diff(21)

def frac_273_fractal_energy_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_273_fractal_energy_vel_63d
    ECONOMIC RATIONALE: Velocity of fractal_energy. Energy dissipated in price movement.
    """
    return (close.diff(1).pow(2).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min()).pow(2)).diff(63)

def frac_274_fractal_energy_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_274_fractal_energy_vel_126d
    ECONOMIC RATIONALE: Velocity of fractal_energy. Energy dissipated in price movement.
    """
    return (close.diff(1).pow(2).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min()).pow(2)).diff(126)

def frac_275_fractal_energy_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_275_fractal_energy_vel_252d
    ECONOMIC RATIONALE: Velocity of fractal_energy. Energy dissipated in price movement.
    """
    return (close.diff(1).pow(2).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min()).pow(2)).diff(252)

def frac_276_multi_scale_vol_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_276_multi_scale_vol_vel_5d
    ECONOMIC RATIONALE: Velocity of multi_scale_vol. Ratio of short-term to long-term volatility structure.
    """
    return (close.rolling(5).std() / close.rolling(63).std()).diff(5)

def frac_277_multi_scale_vol_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_277_multi_scale_vol_vel_21d
    ECONOMIC RATIONALE: Velocity of multi_scale_vol. Ratio of short-term to long-term volatility structure.
    """
    return (close.rolling(5).std() / close.rolling(63).std()).diff(21)

def frac_278_multi_scale_vol_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_278_multi_scale_vol_vel_63d
    ECONOMIC RATIONALE: Velocity of multi_scale_vol. Ratio of short-term to long-term volatility structure.
    """
    return (close.rolling(5).std() / close.rolling(63).std()).diff(63)

def frac_279_multi_scale_vol_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_279_multi_scale_vol_vel_126d
    ECONOMIC RATIONALE: Velocity of multi_scale_vol. Ratio of short-term to long-term volatility structure.
    """
    return (close.rolling(5).std() / close.rolling(63).std()).diff(126)

def frac_280_multi_scale_vol_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_280_multi_scale_vol_vel_252d
    ECONOMIC RATIONALE: Velocity of multi_scale_vol. Ratio of short-term to long-term volatility structure.
    """
    return (close.rolling(5).std() / close.rolling(63).std()).diff(252)

def frac_281_fractal_regime_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_281_fractal_regime_vel_5d
    ECONOMIC RATIONALE: Velocity of fractal_regime. Fractal trend of moving average changes.
    """
    return (close.rolling(21).mean().diff(5).rolling(63).mean()).diff(5)

def frac_282_fractal_regime_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_282_fractal_regime_vel_21d
    ECONOMIC RATIONALE: Velocity of fractal_regime. Fractal trend of moving average changes.
    """
    return (close.rolling(21).mean().diff(5).rolling(63).mean()).diff(21)

def frac_283_fractal_regime_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_283_fractal_regime_vel_63d
    ECONOMIC RATIONALE: Velocity of fractal_regime. Fractal trend of moving average changes.
    """
    return (close.rolling(21).mean().diff(5).rolling(63).mean()).diff(63)

def frac_284_fractal_regime_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_284_fractal_regime_vel_126d
    ECONOMIC RATIONALE: Velocity of fractal_regime. Fractal trend of moving average changes.
    """
    return (close.rolling(21).mean().diff(5).rolling(63).mean()).diff(126)

def frac_285_fractal_regime_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_285_fractal_regime_vel_252d
    ECONOMIC RATIONALE: Velocity of fractal_regime. Fractal trend of moving average changes.
    """
    return (close.rolling(21).mean().diff(5).rolling(63).mean()).diff(252)

def frac_286_box_counting_proxy_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_286_box_counting_proxy_vel_5d
    ECONOMIC RATIONALE: Velocity of box_counting_proxy. Box-counting dimension approximation.
    """
    return (((high.rolling(10).max() - low.rolling(10).min()) + (high.rolling(10).max().shift(10) - low.rolling(10).min().shift(10))) / (high.rolling(20).max() - low.rolling(20).min())).diff(5)

def frac_287_box_counting_proxy_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_287_box_counting_proxy_vel_21d
    ECONOMIC RATIONALE: Velocity of box_counting_proxy. Box-counting dimension approximation.
    """
    return (((high.rolling(10).max() - low.rolling(10).min()) + (high.rolling(10).max().shift(10) - low.rolling(10).min().shift(10))) / (high.rolling(20).max() - low.rolling(20).min())).diff(21)

def frac_288_box_counting_proxy_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_288_box_counting_proxy_vel_63d
    ECONOMIC RATIONALE: Velocity of box_counting_proxy. Box-counting dimension approximation.
    """
    return (((high.rolling(10).max() - low.rolling(10).min()) + (high.rolling(10).max().shift(10) - low.rolling(10).min().shift(10))) / (high.rolling(20).max() - low.rolling(20).min())).diff(63)

def frac_289_box_counting_proxy_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_289_box_counting_proxy_vel_126d
    ECONOMIC RATIONALE: Velocity of box_counting_proxy. Box-counting dimension approximation.
    """
    return (((high.rolling(10).max() - low.rolling(10).min()) + (high.rolling(10).max().shift(10) - low.rolling(10).min().shift(10))) / (high.rolling(20).max() - low.rolling(20).min())).diff(126)

def frac_290_box_counting_proxy_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_290_box_counting_proxy_vel_252d
    ECONOMIC RATIONALE: Velocity of box_counting_proxy. Box-counting dimension approximation.
    """
    return (((high.rolling(10).max() - low.rolling(10).min()) + (high.rolling(10).max().shift(10) - low.rolling(10).min().shift(10))) / (high.rolling(20).max() - low.rolling(20).min())).diff(252)

def frac_291_fractal_trend_index_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_291_fractal_trend_index_vel_5d
    ECONOMIC RATIONALE: Velocity of fractal_trend_index. Trend magnitude relative to structural range.
    """
    return (close.diff(63) / (high.rolling(63).max() - low.rolling(63).min())).diff(5)

def frac_292_fractal_trend_index_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_292_fractal_trend_index_vel_21d
    ECONOMIC RATIONALE: Velocity of fractal_trend_index. Trend magnitude relative to structural range.
    """
    return (close.diff(63) / (high.rolling(63).max() - low.rolling(63).min())).diff(21)

def frac_293_fractal_trend_index_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_293_fractal_trend_index_vel_63d
    ECONOMIC RATIONALE: Velocity of fractal_trend_index. Trend magnitude relative to structural range.
    """
    return (close.diff(63) / (high.rolling(63).max() - low.rolling(63).min())).diff(63)

def frac_294_fractal_trend_index_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_294_fractal_trend_index_vel_126d
    ECONOMIC RATIONALE: Velocity of fractal_trend_index. Trend magnitude relative to structural range.
    """
    return (close.diff(63) / (high.rolling(63).max() - low.rolling(63).min())).diff(126)

def frac_295_fractal_trend_index_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_295_fractal_trend_index_vel_252d
    ECONOMIC RATIONALE: Velocity of fractal_trend_index. Trend magnitude relative to structural range.
    """
    return (close.diff(63) / (high.rolling(63).max() - low.rolling(63).min())).diff(252)

def frac_296_fractal_noise_ratio_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_296_fractal_noise_ratio_vel_5d
    ECONOMIC RATIONALE: Velocity of fractal_noise_ratio. Proportion of price movement attributed to noise.
    """
    return (1 - efficiency_ratio).diff(5)

def frac_297_fractal_noise_ratio_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_297_fractal_noise_ratio_vel_21d
    ECONOMIC RATIONALE: Velocity of fractal_noise_ratio. Proportion of price movement attributed to noise.
    """
    return (1 - efficiency_ratio).diff(21)

def frac_298_fractal_noise_ratio_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_298_fractal_noise_ratio_vel_63d
    ECONOMIC RATIONALE: Velocity of fractal_noise_ratio. Proportion of price movement attributed to noise.
    """
    return (1 - efficiency_ratio).diff(63)

def frac_299_fractal_noise_ratio_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_299_fractal_noise_ratio_vel_126d
    ECONOMIC RATIONALE: Velocity of fractal_noise_ratio. Proportion of price movement attributed to noise.
    """
    return (1 - efficiency_ratio).diff(126)

def frac_300_fractal_noise_ratio_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_300_fractal_noise_ratio_vel_252d
    ECONOMIC RATIONALE: Velocity of fractal_noise_ratio. Proportion of price movement attributed to noise.
    """
    return (1 - efficiency_ratio).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V105_REGISTRY_VEL = {
    "frac_226_hurst_exponent_proxy_vel_5d": {"inputs": ["close", "high", "low"], "func": frac_226_hurst_exponent_proxy_vel_5d},
    "frac_227_hurst_exponent_proxy_vel_21d": {"inputs": ["close", "high", "low"], "func": frac_227_hurst_exponent_proxy_vel_21d},
    "frac_228_hurst_exponent_proxy_vel_63d": {"inputs": ["close", "high", "low"], "func": frac_228_hurst_exponent_proxy_vel_63d},
    "frac_229_hurst_exponent_proxy_vel_126d": {"inputs": ["close", "high", "low"], "func": frac_229_hurst_exponent_proxy_vel_126d},
    "frac_230_hurst_exponent_proxy_vel_252d": {"inputs": ["close", "high", "low"], "func": frac_230_hurst_exponent_proxy_vel_252d},
    "frac_231_fractal_dimension_vel_5d": {"inputs": ["close", "high", "low"], "func": frac_231_fractal_dimension_vel_5d},
    "frac_232_fractal_dimension_vel_21d": {"inputs": ["close", "high", "low"], "func": frac_232_fractal_dimension_vel_21d},
    "frac_233_fractal_dimension_vel_63d": {"inputs": ["close", "high", "low"], "func": frac_233_fractal_dimension_vel_63d},
    "frac_234_fractal_dimension_vel_126d": {"inputs": ["close", "high", "low"], "func": frac_234_fractal_dimension_vel_126d},
    "frac_235_fractal_dimension_vel_252d": {"inputs": ["close", "high", "low"], "func": frac_235_fractal_dimension_vel_252d},
    "frac_236_efficiency_ratio_vel_5d": {"inputs": ["close", "high", "low"], "func": frac_236_efficiency_ratio_vel_5d},
    "frac_237_efficiency_ratio_vel_21d": {"inputs": ["close", "high", "low"], "func": frac_237_efficiency_ratio_vel_21d},
    "frac_238_efficiency_ratio_vel_63d": {"inputs": ["close", "high", "low"], "func": frac_238_efficiency_ratio_vel_63d},
    "frac_239_efficiency_ratio_vel_126d": {"inputs": ["close", "high", "low"], "func": frac_239_efficiency_ratio_vel_126d},
    "frac_240_efficiency_ratio_vel_252d": {"inputs": ["close", "high", "low"], "func": frac_240_efficiency_ratio_vel_252d},
    "frac_241_fractal_volatility_vel_5d": {"inputs": ["close", "high", "low"], "func": frac_241_fractal_volatility_vel_5d},
    "frac_242_fractal_volatility_vel_21d": {"inputs": ["close", "high", "low"], "func": frac_242_fractal_volatility_vel_21d},
    "frac_243_fractal_volatility_vel_63d": {"inputs": ["close", "high", "low"], "func": frac_243_fractal_volatility_vel_63d},
    "frac_244_fractal_volatility_vel_126d": {"inputs": ["close", "high", "low"], "func": frac_244_fractal_volatility_vel_126d},
    "frac_245_fractal_volatility_vel_252d": {"inputs": ["close", "high", "low"], "func": frac_245_fractal_volatility_vel_252d},
    "frac_246_self_similarity_score_vel_5d": {"inputs": ["close", "high", "low"], "func": frac_246_self_similarity_score_vel_5d},
    "frac_247_self_similarity_score_vel_21d": {"inputs": ["close", "high", "low"], "func": frac_247_self_similarity_score_vel_21d},
    "frac_248_self_similarity_score_vel_63d": {"inputs": ["close", "high", "low"], "func": frac_248_self_similarity_score_vel_63d},
    "frac_249_self_similarity_score_vel_126d": {"inputs": ["close", "high", "low"], "func": frac_249_self_similarity_score_vel_126d},
    "frac_250_self_similarity_score_vel_252d": {"inputs": ["close", "high", "low"], "func": frac_250_self_similarity_score_vel_252d},
    "frac_251_fractal_breakout_vel_5d": {"inputs": ["close", "high", "low"], "func": frac_251_fractal_breakout_vel_5d},
    "frac_252_fractal_breakout_vel_21d": {"inputs": ["close", "high", "low"], "func": frac_252_fractal_breakout_vel_21d},
    "frac_253_fractal_breakout_vel_63d": {"inputs": ["close", "high", "low"], "func": frac_253_fractal_breakout_vel_63d},
    "frac_254_fractal_breakout_vel_126d": {"inputs": ["close", "high", "low"], "func": frac_254_fractal_breakout_vel_126d},
    "frac_255_fractal_breakout_vel_252d": {"inputs": ["close", "high", "low"], "func": frac_255_fractal_breakout_vel_252d},
    "frac_256_fractal_support_violation_vel_5d": {"inputs": ["close", "high", "low"], "func": frac_256_fractal_support_violation_vel_5d},
    "frac_257_fractal_support_violation_vel_21d": {"inputs": ["close", "high", "low"], "func": frac_257_fractal_support_violation_vel_21d},
    "frac_258_fractal_support_violation_vel_63d": {"inputs": ["close", "high", "low"], "func": frac_258_fractal_support_violation_vel_63d},
    "frac_259_fractal_support_violation_vel_126d": {"inputs": ["close", "high", "low"], "func": frac_259_fractal_support_violation_vel_126d},
    "frac_260_fractal_support_violation_vel_252d": {"inputs": ["close", "high", "low"], "func": frac_260_fractal_support_violation_vel_252d},
    "frac_261_chaos_theory_osc_vel_5d": {"inputs": ["close", "high", "low"], "func": frac_261_chaos_theory_osc_vel_5d},
    "frac_262_chaos_theory_osc_vel_21d": {"inputs": ["close", "high", "low"], "func": frac_262_chaos_theory_osc_vel_21d},
    "frac_263_chaos_theory_osc_vel_63d": {"inputs": ["close", "high", "low"], "func": frac_263_chaos_theory_osc_vel_63d},
    "frac_264_chaos_theory_osc_vel_126d": {"inputs": ["close", "high", "low"], "func": frac_264_chaos_theory_osc_vel_126d},
    "frac_265_chaos_theory_osc_vel_252d": {"inputs": ["close", "high", "low"], "func": frac_265_chaos_theory_osc_vel_252d},
    "frac_266_entropy_proxy_vel_5d": {"inputs": ["close", "high", "low"], "func": frac_266_entropy_proxy_vel_5d},
    "frac_267_entropy_proxy_vel_21d": {"inputs": ["close", "high", "low"], "func": frac_267_entropy_proxy_vel_21d},
    "frac_268_entropy_proxy_vel_63d": {"inputs": ["close", "high", "low"], "func": frac_268_entropy_proxy_vel_63d},
    "frac_269_entropy_proxy_vel_126d": {"inputs": ["close", "high", "low"], "func": frac_269_entropy_proxy_vel_126d},
    "frac_270_entropy_proxy_vel_252d": {"inputs": ["close", "high", "low"], "func": frac_270_entropy_proxy_vel_252d},
    "frac_271_fractal_energy_vel_5d": {"inputs": ["close", "high", "low"], "func": frac_271_fractal_energy_vel_5d},
    "frac_272_fractal_energy_vel_21d": {"inputs": ["close", "high", "low"], "func": frac_272_fractal_energy_vel_21d},
    "frac_273_fractal_energy_vel_63d": {"inputs": ["close", "high", "low"], "func": frac_273_fractal_energy_vel_63d},
    "frac_274_fractal_energy_vel_126d": {"inputs": ["close", "high", "low"], "func": frac_274_fractal_energy_vel_126d},
    "frac_275_fractal_energy_vel_252d": {"inputs": ["close", "high", "low"], "func": frac_275_fractal_energy_vel_252d},
    "frac_276_multi_scale_vol_vel_5d": {"inputs": ["close", "high", "low"], "func": frac_276_multi_scale_vol_vel_5d},
    "frac_277_multi_scale_vol_vel_21d": {"inputs": ["close", "high", "low"], "func": frac_277_multi_scale_vol_vel_21d},
    "frac_278_multi_scale_vol_vel_63d": {"inputs": ["close", "high", "low"], "func": frac_278_multi_scale_vol_vel_63d},
    "frac_279_multi_scale_vol_vel_126d": {"inputs": ["close", "high", "low"], "func": frac_279_multi_scale_vol_vel_126d},
    "frac_280_multi_scale_vol_vel_252d": {"inputs": ["close", "high", "low"], "func": frac_280_multi_scale_vol_vel_252d},
    "frac_281_fractal_regime_vel_5d": {"inputs": ["close", "high", "low"], "func": frac_281_fractal_regime_vel_5d},
    "frac_282_fractal_regime_vel_21d": {"inputs": ["close", "high", "low"], "func": frac_282_fractal_regime_vel_21d},
    "frac_283_fractal_regime_vel_63d": {"inputs": ["close", "high", "low"], "func": frac_283_fractal_regime_vel_63d},
    "frac_284_fractal_regime_vel_126d": {"inputs": ["close", "high", "low"], "func": frac_284_fractal_regime_vel_126d},
    "frac_285_fractal_regime_vel_252d": {"inputs": ["close", "high", "low"], "func": frac_285_fractal_regime_vel_252d},
    "frac_286_box_counting_proxy_vel_5d": {"inputs": ["close", "high", "low"], "func": frac_286_box_counting_proxy_vel_5d},
    "frac_287_box_counting_proxy_vel_21d": {"inputs": ["close", "high", "low"], "func": frac_287_box_counting_proxy_vel_21d},
    "frac_288_box_counting_proxy_vel_63d": {"inputs": ["close", "high", "low"], "func": frac_288_box_counting_proxy_vel_63d},
    "frac_289_box_counting_proxy_vel_126d": {"inputs": ["close", "high", "low"], "func": frac_289_box_counting_proxy_vel_126d},
    "frac_290_box_counting_proxy_vel_252d": {"inputs": ["close", "high", "low"], "func": frac_290_box_counting_proxy_vel_252d},
    "frac_291_fractal_trend_index_vel_5d": {"inputs": ["close", "high", "low"], "func": frac_291_fractal_trend_index_vel_5d},
    "frac_292_fractal_trend_index_vel_21d": {"inputs": ["close", "high", "low"], "func": frac_292_fractal_trend_index_vel_21d},
    "frac_293_fractal_trend_index_vel_63d": {"inputs": ["close", "high", "low"], "func": frac_293_fractal_trend_index_vel_63d},
    "frac_294_fractal_trend_index_vel_126d": {"inputs": ["close", "high", "low"], "func": frac_294_fractal_trend_index_vel_126d},
    "frac_295_fractal_trend_index_vel_252d": {"inputs": ["close", "high", "low"], "func": frac_295_fractal_trend_index_vel_252d},
    "frac_296_fractal_noise_ratio_vel_5d": {"inputs": ["close", "high", "low"], "func": frac_296_fractal_noise_ratio_vel_5d},
    "frac_297_fractal_noise_ratio_vel_21d": {"inputs": ["close", "high", "low"], "func": frac_297_fractal_noise_ratio_vel_21d},
    "frac_298_fractal_noise_ratio_vel_63d": {"inputs": ["close", "high", "low"], "func": frac_298_fractal_noise_ratio_vel_63d},
    "frac_299_fractal_noise_ratio_vel_126d": {"inputs": ["close", "high", "low"], "func": frac_299_fractal_noise_ratio_vel_126d},
    "frac_300_fractal_noise_ratio_vel_252d": {"inputs": ["close", "high", "low"], "func": frac_300_fractal_noise_ratio_vel_252d},
}
