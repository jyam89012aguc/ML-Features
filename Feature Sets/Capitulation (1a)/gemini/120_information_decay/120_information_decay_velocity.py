"""
120_information_decay — Velocity (2nd Derivatives)
Domain: information_decay
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

def idec_226_price_impact_decay_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_226_price_impact_decay_vel_5d
    ECONOMIC RATIONALE: Velocity of price_impact_decay. Decaying magnitude of recent price impacts.
    """
    return (close.diff(1).abs().ewm(halflife=5).mean()).diff(5)

def idec_227_price_impact_decay_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_227_price_impact_decay_vel_21d
    ECONOMIC RATIONALE: Velocity of price_impact_decay. Decaying magnitude of recent price impacts.
    """
    return (close.diff(1).abs().ewm(halflife=5).mean()).diff(21)

def idec_228_price_impact_decay_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_228_price_impact_decay_vel_63d
    ECONOMIC RATIONALE: Velocity of price_impact_decay. Decaying magnitude of recent price impacts.
    """
    return (close.diff(1).abs().ewm(halflife=5).mean()).diff(63)

def idec_229_price_impact_decay_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_229_price_impact_decay_vel_126d
    ECONOMIC RATIONALE: Velocity of price_impact_decay. Decaying magnitude of recent price impacts.
    """
    return (close.diff(1).abs().ewm(halflife=5).mean()).diff(126)

def idec_230_price_impact_decay_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_230_price_impact_decay_vel_252d
    ECONOMIC RATIONALE: Velocity of price_impact_decay. Decaying magnitude of recent price impacts.
    """
    return (close.diff(1).abs().ewm(halflife=5).mean()).diff(252)

def idec_231_volume_impact_decay_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_231_volume_impact_decay_vel_5d
    ECONOMIC RATIONALE: Velocity of volume_impact_decay. Decaying intensity of recent volume spikes.
    """
    return (volume.ewm(halflife=5).mean() / volume.rolling(63).mean()).diff(5)

def idec_232_volume_impact_decay_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_232_volume_impact_decay_vel_21d
    ECONOMIC RATIONALE: Velocity of volume_impact_decay. Decaying intensity of recent volume spikes.
    """
    return (volume.ewm(halflife=5).mean() / volume.rolling(63).mean()).diff(21)

def idec_233_volume_impact_decay_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_233_volume_impact_decay_vel_63d
    ECONOMIC RATIONALE: Velocity of volume_impact_decay. Decaying intensity of recent volume spikes.
    """
    return (volume.ewm(halflife=5).mean() / volume.rolling(63).mean()).diff(63)

def idec_234_volume_impact_decay_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_234_volume_impact_decay_vel_126d
    ECONOMIC RATIONALE: Velocity of volume_impact_decay. Decaying intensity of recent volume spikes.
    """
    return (volume.ewm(halflife=5).mean() / volume.rolling(63).mean()).diff(126)

def idec_235_volume_impact_decay_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_235_volume_impact_decay_vel_252d
    ECONOMIC RATIONALE: Velocity of volume_impact_decay. Decaying intensity of recent volume spikes.
    """
    return (volume.ewm(halflife=5).mean() / volume.rolling(63).mean()).diff(252)

def idec_236_information_horizon_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_236_information_horizon_vel_5d
    ECONOMIC RATIONALE: Velocity of information_horizon. Long-term memory of price levels.
    """
    return (close.rolling(21).corr(close.shift(21))).diff(5)

def idec_237_information_horizon_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_237_information_horizon_vel_21d
    ECONOMIC RATIONALE: Velocity of information_horizon. Long-term memory of price levels.
    """
    return (close.rolling(21).corr(close.shift(21))).diff(21)

def idec_238_information_horizon_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_238_information_horizon_vel_63d
    ECONOMIC RATIONALE: Velocity of information_horizon. Long-term memory of price levels.
    """
    return (close.rolling(21).corr(close.shift(21))).diff(63)

def idec_239_information_horizon_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_239_information_horizon_vel_126d
    ECONOMIC RATIONALE: Velocity of information_horizon. Long-term memory of price levels.
    """
    return (close.rolling(21).corr(close.shift(21))).diff(126)

def idec_240_information_horizon_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_240_information_horizon_vel_252d
    ECONOMIC RATIONALE: Velocity of information_horizon. Long-term memory of price levels.
    """
    return (close.rolling(21).corr(close.shift(21))).diff(252)

def idec_241_news_response_decay_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_241_news_response_decay_vel_5d
    ECONOMIC RATIONALE: Velocity of news_response_decay. Recent daily change relative to cumulative monthly change.
    """
    return (close.pct_change(1).abs() / close.pct_change(21).abs().shift(1).replace(0, 1e-9)).diff(5)

def idec_242_news_response_decay_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_242_news_response_decay_vel_21d
    ECONOMIC RATIONALE: Velocity of news_response_decay. Recent daily change relative to cumulative monthly change.
    """
    return (close.pct_change(1).abs() / close.pct_change(21).abs().shift(1).replace(0, 1e-9)).diff(21)

def idec_243_news_response_decay_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_243_news_response_decay_vel_63d
    ECONOMIC RATIONALE: Velocity of news_response_decay. Recent daily change relative to cumulative monthly change.
    """
    return (close.pct_change(1).abs() / close.pct_change(21).abs().shift(1).replace(0, 1e-9)).diff(63)

def idec_244_news_response_decay_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_244_news_response_decay_vel_126d
    ECONOMIC RATIONALE: Velocity of news_response_decay. Recent daily change relative to cumulative monthly change.
    """
    return (close.pct_change(1).abs() / close.pct_change(21).abs().shift(1).replace(0, 1e-9)).diff(126)

def idec_245_news_response_decay_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_245_news_response_decay_vel_252d
    ECONOMIC RATIONALE: Velocity of news_response_decay. Recent daily change relative to cumulative monthly change.
    """
    return (close.pct_change(1).abs() / close.pct_change(21).abs().shift(1).replace(0, 1e-9)).diff(252)

def idec_246_autocorr_decay_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_246_autocorr_decay_vel_5d
    ECONOMIC RATIONALE: Velocity of autocorr_decay. Decay in serial correlation across timeframes.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) / close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1)).replace(0, 1e-9)).diff(5)

def idec_247_autocorr_decay_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_247_autocorr_decay_vel_21d
    ECONOMIC RATIONALE: Velocity of autocorr_decay. Decay in serial correlation across timeframes.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) / close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1)).replace(0, 1e-9)).diff(21)

def idec_248_autocorr_decay_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_248_autocorr_decay_vel_63d
    ECONOMIC RATIONALE: Velocity of autocorr_decay. Decay in serial correlation across timeframes.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) / close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1)).replace(0, 1e-9)).diff(63)

def idec_249_autocorr_decay_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_249_autocorr_decay_vel_126d
    ECONOMIC RATIONALE: Velocity of autocorr_decay. Decay in serial correlation across timeframes.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) / close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1)).replace(0, 1e-9)).diff(126)

def idec_250_autocorr_decay_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_250_autocorr_decay_vel_252d
    ECONOMIC RATIONALE: Velocity of autocorr_decay. Decay in serial correlation across timeframes.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) / close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1)).replace(0, 1e-9)).diff(252)

def idec_251_volatility_mean_reversion_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_251_volatility_mean_reversion_vel_5d
    ECONOMIC RATIONALE: Velocity of volatility_mean_reversion. Rate at which short-term vol returns to the long-term mean.
    """
    return (close.rolling(21).std() / close.rolling(252).std()).diff(5)

def idec_252_volatility_mean_reversion_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_252_volatility_mean_reversion_vel_21d
    ECONOMIC RATIONALE: Velocity of volatility_mean_reversion. Rate at which short-term vol returns to the long-term mean.
    """
    return (close.rolling(21).std() / close.rolling(252).std()).diff(21)

def idec_253_volatility_mean_reversion_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_253_volatility_mean_reversion_vel_63d
    ECONOMIC RATIONALE: Velocity of volatility_mean_reversion. Rate at which short-term vol returns to the long-term mean.
    """
    return (close.rolling(21).std() / close.rolling(252).std()).diff(63)

def idec_254_volatility_mean_reversion_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_254_volatility_mean_reversion_vel_126d
    ECONOMIC RATIONALE: Velocity of volatility_mean_reversion. Rate at which short-term vol returns to the long-term mean.
    """
    return (close.rolling(21).std() / close.rolling(252).std()).diff(126)

def idec_255_volatility_mean_reversion_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_255_volatility_mean_reversion_vel_252d
    ECONOMIC RATIONALE: Velocity of volatility_mean_reversion. Rate at which short-term vol returns to the long-term mean.
    """
    return (close.rolling(21).std() / close.rolling(252).std()).diff(252)

def idec_256_information_efficiency_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_256_information_efficiency_vel_5d
    ECONOMIC RATIONALE: Velocity of information_efficiency. Rate of information incorporation into price.
    """
    return (abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)).diff(5)

def idec_257_information_efficiency_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_257_information_efficiency_vel_21d
    ECONOMIC RATIONALE: Velocity of information_efficiency. Rate of information incorporation into price.
    """
    return (abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)).diff(21)

def idec_258_information_efficiency_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_258_information_efficiency_vel_63d
    ECONOMIC RATIONALE: Velocity of information_efficiency. Rate of information incorporation into price.
    """
    return (abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)).diff(63)

def idec_259_information_efficiency_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_259_information_efficiency_vel_126d
    ECONOMIC RATIONALE: Velocity of information_efficiency. Rate of information incorporation into price.
    """
    return (abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)).diff(126)

def idec_260_information_efficiency_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_260_information_efficiency_vel_252d
    ECONOMIC RATIONALE: Velocity of information_efficiency. Rate of information incorporation into price.
    """
    return (abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)).diff(252)

def idec_261_signal_noise_decay_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_261_signal_noise_decay_vel_5d
    ECONOMIC RATIONALE: Velocity of signal_noise_decay. Decay of signal strength relative to noise.
    """
    return (close.rolling(21).mean().diff(5).abs() / close.rolling(21).std().replace(0, 1e-9)).diff(5)

def idec_262_signal_noise_decay_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_262_signal_noise_decay_vel_21d
    ECONOMIC RATIONALE: Velocity of signal_noise_decay. Decay of signal strength relative to noise.
    """
    return (close.rolling(21).mean().diff(5).abs() / close.rolling(21).std().replace(0, 1e-9)).diff(21)

def idec_263_signal_noise_decay_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_263_signal_noise_decay_vel_63d
    ECONOMIC RATIONALE: Velocity of signal_noise_decay. Decay of signal strength relative to noise.
    """
    return (close.rolling(21).mean().diff(5).abs() / close.rolling(21).std().replace(0, 1e-9)).diff(63)

def idec_264_signal_noise_decay_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_264_signal_noise_decay_vel_126d
    ECONOMIC RATIONALE: Velocity of signal_noise_decay. Decay of signal strength relative to noise.
    """
    return (close.rolling(21).mean().diff(5).abs() / close.rolling(21).std().replace(0, 1e-9)).diff(126)

def idec_265_signal_noise_decay_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_265_signal_noise_decay_vel_252d
    ECONOMIC RATIONALE: Velocity of signal_noise_decay. Decay of signal strength relative to noise.
    """
    return (close.rolling(21).mean().diff(5).abs() / close.rolling(21).std().replace(0, 1e-9)).diff(252)

def idec_266_memory_length_proxy_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_266_memory_length_proxy_vel_5d
    ECONOMIC RATIONALE: Velocity of memory_length_proxy. Estimated length of price memory.
    """
    return (close.rolling(252).apply(lambda x: np.argmax(np.correlate(x-np.mean(x), x-np.mean(x), mode='full')[len(x):]))).diff(5)

def idec_267_memory_length_proxy_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_267_memory_length_proxy_vel_21d
    ECONOMIC RATIONALE: Velocity of memory_length_proxy. Estimated length of price memory.
    """
    return (close.rolling(252).apply(lambda x: np.argmax(np.correlate(x-np.mean(x), x-np.mean(x), mode='full')[len(x):]))).diff(21)

def idec_268_memory_length_proxy_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_268_memory_length_proxy_vel_63d
    ECONOMIC RATIONALE: Velocity of memory_length_proxy. Estimated length of price memory.
    """
    return (close.rolling(252).apply(lambda x: np.argmax(np.correlate(x-np.mean(x), x-np.mean(x), mode='full')[len(x):]))).diff(63)

def idec_269_memory_length_proxy_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_269_memory_length_proxy_vel_126d
    ECONOMIC RATIONALE: Velocity of memory_length_proxy. Estimated length of price memory.
    """
    return (close.rolling(252).apply(lambda x: np.argmax(np.correlate(x-np.mean(x), x-np.mean(x), mode='full')[len(x):]))).diff(126)

def idec_270_memory_length_proxy_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_270_memory_length_proxy_vel_252d
    ECONOMIC RATIONALE: Velocity of memory_length_proxy. Estimated length of price memory.
    """
    return (close.rolling(252).apply(lambda x: np.argmax(np.correlate(x-np.mean(x), x-np.mean(x), mode='full')[len(x):]))).diff(252)

def idec_271_information_shock_persistence_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_271_information_shock_persistence_vel_5d
    ECONOMIC RATIONALE: Velocity of information_shock_persistence. Persistence of information-driven price volatility.
    """
    return (close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()).diff(5)

def idec_272_information_shock_persistence_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_272_information_shock_persistence_vel_21d
    ECONOMIC RATIONALE: Velocity of information_shock_persistence. Persistence of information-driven price volatility.
    """
    return (close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()).diff(21)

def idec_273_information_shock_persistence_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_273_information_shock_persistence_vel_63d
    ECONOMIC RATIONALE: Velocity of information_shock_persistence. Persistence of information-driven price volatility.
    """
    return (close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()).diff(63)

def idec_274_information_shock_persistence_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_274_information_shock_persistence_vel_126d
    ECONOMIC RATIONALE: Velocity of information_shock_persistence. Persistence of information-driven price volatility.
    """
    return (close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()).diff(126)

def idec_275_information_shock_persistence_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_275_information_shock_persistence_vel_252d
    ECONOMIC RATIONALE: Velocity of information_shock_persistence. Persistence of information-driven price volatility.
    """
    return (close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()).diff(252)

def idec_276_drift_decay_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_276_drift_decay_vel_5d
    ECONOMIC RATIONALE: Velocity of drift_decay. Decay of short-term drift relative to quarterly trend.
    """
    return (close.pct_change(5).abs() / close.pct_change(63).abs().replace(0, 1e-9)).diff(5)

def idec_277_drift_decay_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_277_drift_decay_vel_21d
    ECONOMIC RATIONALE: Velocity of drift_decay. Decay of short-term drift relative to quarterly trend.
    """
    return (close.pct_change(5).abs() / close.pct_change(63).abs().replace(0, 1e-9)).diff(21)

def idec_278_drift_decay_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_278_drift_decay_vel_63d
    ECONOMIC RATIONALE: Velocity of drift_decay. Decay of short-term drift relative to quarterly trend.
    """
    return (close.pct_change(5).abs() / close.pct_change(63).abs().replace(0, 1e-9)).diff(63)

def idec_279_drift_decay_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_279_drift_decay_vel_126d
    ECONOMIC RATIONALE: Velocity of drift_decay. Decay of short-term drift relative to quarterly trend.
    """
    return (close.pct_change(5).abs() / close.pct_change(63).abs().replace(0, 1e-9)).diff(126)

def idec_280_drift_decay_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_280_drift_decay_vel_252d
    ECONOMIC RATIONALE: Velocity of drift_decay. Decay of short-term drift relative to quarterly trend.
    """
    return (close.pct_change(5).abs() / close.pct_change(63).abs().replace(0, 1e-9)).diff(252)

def idec_281_information_entropy_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_281_information_entropy_vel_5d
    ECONOMIC RATIONALE: Velocity of information_entropy. Uncertainty or decay of information in price returns.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))).diff(5)

def idec_282_information_entropy_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_282_information_entropy_vel_21d
    ECONOMIC RATIONALE: Velocity of information_entropy. Uncertainty or decay of information in price returns.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))).diff(21)

def idec_283_information_entropy_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_283_information_entropy_vel_63d
    ECONOMIC RATIONALE: Velocity of information_entropy. Uncertainty or decay of information in price returns.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))).diff(63)

def idec_284_information_entropy_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_284_information_entropy_vel_126d
    ECONOMIC RATIONALE: Velocity of information_entropy. Uncertainty or decay of information in price returns.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))).diff(126)

def idec_285_information_entropy_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_285_information_entropy_vel_252d
    ECONOMIC RATIONALE: Velocity of information_entropy. Uncertainty or decay of information in price returns.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))).diff(252)

def idec_286_volume_memory_decay_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_286_volume_memory_decay_vel_5d
    ECONOMIC RATIONALE: Velocity of volume_memory_decay. Persistence of volume regimes.
    """
    return (volume.rolling(21).corr(volume.shift(21))).diff(5)

def idec_287_volume_memory_decay_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_287_volume_memory_decay_vel_21d
    ECONOMIC RATIONALE: Velocity of volume_memory_decay. Persistence of volume regimes.
    """
    return (volume.rolling(21).corr(volume.shift(21))).diff(21)

def idec_288_volume_memory_decay_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_288_volume_memory_decay_vel_63d
    ECONOMIC RATIONALE: Velocity of volume_memory_decay. Persistence of volume regimes.
    """
    return (volume.rolling(21).corr(volume.shift(21))).diff(63)

def idec_289_volume_memory_decay_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_289_volume_memory_decay_vel_126d
    ECONOMIC RATIONALE: Velocity of volume_memory_decay. Persistence of volume regimes.
    """
    return (volume.rolling(21).corr(volume.shift(21))).diff(126)

def idec_290_volume_memory_decay_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_290_volume_memory_decay_vel_252d
    ECONOMIC RATIONALE: Velocity of volume_memory_decay. Persistence of volume regimes.
    """
    return (volume.rolling(21).corr(volume.shift(21))).diff(252)

def idec_291_price_stickiness_decay_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_291_price_stickiness_decay_vel_5d
    ECONOMIC RATIONALE: Velocity of price_stickiness_decay. Change in the rate of price stagnation.
    """
    return ((close.diff(1).abs() < 0.01).rolling(21).mean().diff(21)).diff(5)

def idec_292_price_stickiness_decay_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_292_price_stickiness_decay_vel_21d
    ECONOMIC RATIONALE: Velocity of price_stickiness_decay. Change in the rate of price stagnation.
    """
    return ((close.diff(1).abs() < 0.01).rolling(21).mean().diff(21)).diff(21)

def idec_293_price_stickiness_decay_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_293_price_stickiness_decay_vel_63d
    ECONOMIC RATIONALE: Velocity of price_stickiness_decay. Change in the rate of price stagnation.
    """
    return ((close.diff(1).abs() < 0.01).rolling(21).mean().diff(21)).diff(63)

def idec_294_price_stickiness_decay_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_294_price_stickiness_decay_vel_126d
    ECONOMIC RATIONALE: Velocity of price_stickiness_decay. Change in the rate of price stagnation.
    """
    return ((close.diff(1).abs() < 0.01).rolling(21).mean().diff(21)).diff(126)

def idec_295_price_stickiness_decay_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_295_price_stickiness_decay_vel_252d
    ECONOMIC RATIONALE: Velocity of price_stickiness_decay. Change in the rate of price stagnation.
    """
    return ((close.diff(1).abs() < 0.01).rolling(21).mean().diff(21)).diff(252)

def idec_296_information_flow_acceleration_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_296_information_flow_acceleration_vel_5d
    ECONOMIC RATIONALE: Velocity of information_flow_acceleration. Acceleration of information flow into price.
    """
    return (close.diff(1).abs().ewm(span=5).mean() / close.diff(1).abs().ewm(span=63).mean()).diff(5)

def idec_297_information_flow_acceleration_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_297_information_flow_acceleration_vel_21d
    ECONOMIC RATIONALE: Velocity of information_flow_acceleration. Acceleration of information flow into price.
    """
    return (close.diff(1).abs().ewm(span=5).mean() / close.diff(1).abs().ewm(span=63).mean()).diff(21)

def idec_298_information_flow_acceleration_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_298_information_flow_acceleration_vel_63d
    ECONOMIC RATIONALE: Velocity of information_flow_acceleration. Acceleration of information flow into price.
    """
    return (close.diff(1).abs().ewm(span=5).mean() / close.diff(1).abs().ewm(span=63).mean()).diff(63)

def idec_299_information_flow_acceleration_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_299_information_flow_acceleration_vel_126d
    ECONOMIC RATIONALE: Velocity of information_flow_acceleration. Acceleration of information flow into price.
    """
    return (close.diff(1).abs().ewm(span=5).mean() / close.diff(1).abs().ewm(span=63).mean()).diff(126)

def idec_300_information_flow_acceleration_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_300_information_flow_acceleration_vel_252d
    ECONOMIC RATIONALE: Velocity of information_flow_acceleration. Acceleration of information flow into price.
    """
    return (close.diff(1).abs().ewm(span=5).mean() / close.diff(1).abs().ewm(span=63).mean()).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V120_REGISTRY_VEL = {
    "idec_226_price_impact_decay_vel_5d": {"inputs": ["close", "volume"], "func": idec_226_price_impact_decay_vel_5d},
    "idec_227_price_impact_decay_vel_21d": {"inputs": ["close", "volume"], "func": idec_227_price_impact_decay_vel_21d},
    "idec_228_price_impact_decay_vel_63d": {"inputs": ["close", "volume"], "func": idec_228_price_impact_decay_vel_63d},
    "idec_229_price_impact_decay_vel_126d": {"inputs": ["close", "volume"], "func": idec_229_price_impact_decay_vel_126d},
    "idec_230_price_impact_decay_vel_252d": {"inputs": ["close", "volume"], "func": idec_230_price_impact_decay_vel_252d},
    "idec_231_volume_impact_decay_vel_5d": {"inputs": ["close", "volume"], "func": idec_231_volume_impact_decay_vel_5d},
    "idec_232_volume_impact_decay_vel_21d": {"inputs": ["close", "volume"], "func": idec_232_volume_impact_decay_vel_21d},
    "idec_233_volume_impact_decay_vel_63d": {"inputs": ["close", "volume"], "func": idec_233_volume_impact_decay_vel_63d},
    "idec_234_volume_impact_decay_vel_126d": {"inputs": ["close", "volume"], "func": idec_234_volume_impact_decay_vel_126d},
    "idec_235_volume_impact_decay_vel_252d": {"inputs": ["close", "volume"], "func": idec_235_volume_impact_decay_vel_252d},
    "idec_236_information_horizon_vel_5d": {"inputs": ["close", "volume"], "func": idec_236_information_horizon_vel_5d},
    "idec_237_information_horizon_vel_21d": {"inputs": ["close", "volume"], "func": idec_237_information_horizon_vel_21d},
    "idec_238_information_horizon_vel_63d": {"inputs": ["close", "volume"], "func": idec_238_information_horizon_vel_63d},
    "idec_239_information_horizon_vel_126d": {"inputs": ["close", "volume"], "func": idec_239_information_horizon_vel_126d},
    "idec_240_information_horizon_vel_252d": {"inputs": ["close", "volume"], "func": idec_240_information_horizon_vel_252d},
    "idec_241_news_response_decay_vel_5d": {"inputs": ["close", "volume"], "func": idec_241_news_response_decay_vel_5d},
    "idec_242_news_response_decay_vel_21d": {"inputs": ["close", "volume"], "func": idec_242_news_response_decay_vel_21d},
    "idec_243_news_response_decay_vel_63d": {"inputs": ["close", "volume"], "func": idec_243_news_response_decay_vel_63d},
    "idec_244_news_response_decay_vel_126d": {"inputs": ["close", "volume"], "func": idec_244_news_response_decay_vel_126d},
    "idec_245_news_response_decay_vel_252d": {"inputs": ["close", "volume"], "func": idec_245_news_response_decay_vel_252d},
    "idec_246_autocorr_decay_vel_5d": {"inputs": ["close", "volume"], "func": idec_246_autocorr_decay_vel_5d},
    "idec_247_autocorr_decay_vel_21d": {"inputs": ["close", "volume"], "func": idec_247_autocorr_decay_vel_21d},
    "idec_248_autocorr_decay_vel_63d": {"inputs": ["close", "volume"], "func": idec_248_autocorr_decay_vel_63d},
    "idec_249_autocorr_decay_vel_126d": {"inputs": ["close", "volume"], "func": idec_249_autocorr_decay_vel_126d},
    "idec_250_autocorr_decay_vel_252d": {"inputs": ["close", "volume"], "func": idec_250_autocorr_decay_vel_252d},
    "idec_251_volatility_mean_reversion_vel_5d": {"inputs": ["close", "volume"], "func": idec_251_volatility_mean_reversion_vel_5d},
    "idec_252_volatility_mean_reversion_vel_21d": {"inputs": ["close", "volume"], "func": idec_252_volatility_mean_reversion_vel_21d},
    "idec_253_volatility_mean_reversion_vel_63d": {"inputs": ["close", "volume"], "func": idec_253_volatility_mean_reversion_vel_63d},
    "idec_254_volatility_mean_reversion_vel_126d": {"inputs": ["close", "volume"], "func": idec_254_volatility_mean_reversion_vel_126d},
    "idec_255_volatility_mean_reversion_vel_252d": {"inputs": ["close", "volume"], "func": idec_255_volatility_mean_reversion_vel_252d},
    "idec_256_information_efficiency_vel_5d": {"inputs": ["close", "volume"], "func": idec_256_information_efficiency_vel_5d},
    "idec_257_information_efficiency_vel_21d": {"inputs": ["close", "volume"], "func": idec_257_information_efficiency_vel_21d},
    "idec_258_information_efficiency_vel_63d": {"inputs": ["close", "volume"], "func": idec_258_information_efficiency_vel_63d},
    "idec_259_information_efficiency_vel_126d": {"inputs": ["close", "volume"], "func": idec_259_information_efficiency_vel_126d},
    "idec_260_information_efficiency_vel_252d": {"inputs": ["close", "volume"], "func": idec_260_information_efficiency_vel_252d},
    "idec_261_signal_noise_decay_vel_5d": {"inputs": ["close", "volume"], "func": idec_261_signal_noise_decay_vel_5d},
    "idec_262_signal_noise_decay_vel_21d": {"inputs": ["close", "volume"], "func": idec_262_signal_noise_decay_vel_21d},
    "idec_263_signal_noise_decay_vel_63d": {"inputs": ["close", "volume"], "func": idec_263_signal_noise_decay_vel_63d},
    "idec_264_signal_noise_decay_vel_126d": {"inputs": ["close", "volume"], "func": idec_264_signal_noise_decay_vel_126d},
    "idec_265_signal_noise_decay_vel_252d": {"inputs": ["close", "volume"], "func": idec_265_signal_noise_decay_vel_252d},
    "idec_266_memory_length_proxy_vel_5d": {"inputs": ["close", "volume"], "func": idec_266_memory_length_proxy_vel_5d},
    "idec_267_memory_length_proxy_vel_21d": {"inputs": ["close", "volume"], "func": idec_267_memory_length_proxy_vel_21d},
    "idec_268_memory_length_proxy_vel_63d": {"inputs": ["close", "volume"], "func": idec_268_memory_length_proxy_vel_63d},
    "idec_269_memory_length_proxy_vel_126d": {"inputs": ["close", "volume"], "func": idec_269_memory_length_proxy_vel_126d},
    "idec_270_memory_length_proxy_vel_252d": {"inputs": ["close", "volume"], "func": idec_270_memory_length_proxy_vel_252d},
    "idec_271_information_shock_persistence_vel_5d": {"inputs": ["close", "volume"], "func": idec_271_information_shock_persistence_vel_5d},
    "idec_272_information_shock_persistence_vel_21d": {"inputs": ["close", "volume"], "func": idec_272_information_shock_persistence_vel_21d},
    "idec_273_information_shock_persistence_vel_63d": {"inputs": ["close", "volume"], "func": idec_273_information_shock_persistence_vel_63d},
    "idec_274_information_shock_persistence_vel_126d": {"inputs": ["close", "volume"], "func": idec_274_information_shock_persistence_vel_126d},
    "idec_275_information_shock_persistence_vel_252d": {"inputs": ["close", "volume"], "func": idec_275_information_shock_persistence_vel_252d},
    "idec_276_drift_decay_vel_5d": {"inputs": ["close", "volume"], "func": idec_276_drift_decay_vel_5d},
    "idec_277_drift_decay_vel_21d": {"inputs": ["close", "volume"], "func": idec_277_drift_decay_vel_21d},
    "idec_278_drift_decay_vel_63d": {"inputs": ["close", "volume"], "func": idec_278_drift_decay_vel_63d},
    "idec_279_drift_decay_vel_126d": {"inputs": ["close", "volume"], "func": idec_279_drift_decay_vel_126d},
    "idec_280_drift_decay_vel_252d": {"inputs": ["close", "volume"], "func": idec_280_drift_decay_vel_252d},
    "idec_281_information_entropy_vel_5d": {"inputs": ["close", "volume"], "func": idec_281_information_entropy_vel_5d},
    "idec_282_information_entropy_vel_21d": {"inputs": ["close", "volume"], "func": idec_282_information_entropy_vel_21d},
    "idec_283_information_entropy_vel_63d": {"inputs": ["close", "volume"], "func": idec_283_information_entropy_vel_63d},
    "idec_284_information_entropy_vel_126d": {"inputs": ["close", "volume"], "func": idec_284_information_entropy_vel_126d},
    "idec_285_information_entropy_vel_252d": {"inputs": ["close", "volume"], "func": idec_285_information_entropy_vel_252d},
    "idec_286_volume_memory_decay_vel_5d": {"inputs": ["close", "volume"], "func": idec_286_volume_memory_decay_vel_5d},
    "idec_287_volume_memory_decay_vel_21d": {"inputs": ["close", "volume"], "func": idec_287_volume_memory_decay_vel_21d},
    "idec_288_volume_memory_decay_vel_63d": {"inputs": ["close", "volume"], "func": idec_288_volume_memory_decay_vel_63d},
    "idec_289_volume_memory_decay_vel_126d": {"inputs": ["close", "volume"], "func": idec_289_volume_memory_decay_vel_126d},
    "idec_290_volume_memory_decay_vel_252d": {"inputs": ["close", "volume"], "func": idec_290_volume_memory_decay_vel_252d},
    "idec_291_price_stickiness_decay_vel_5d": {"inputs": ["close", "volume"], "func": idec_291_price_stickiness_decay_vel_5d},
    "idec_292_price_stickiness_decay_vel_21d": {"inputs": ["close", "volume"], "func": idec_292_price_stickiness_decay_vel_21d},
    "idec_293_price_stickiness_decay_vel_63d": {"inputs": ["close", "volume"], "func": idec_293_price_stickiness_decay_vel_63d},
    "idec_294_price_stickiness_decay_vel_126d": {"inputs": ["close", "volume"], "func": idec_294_price_stickiness_decay_vel_126d},
    "idec_295_price_stickiness_decay_vel_252d": {"inputs": ["close", "volume"], "func": idec_295_price_stickiness_decay_vel_252d},
    "idec_296_information_flow_acceleration_vel_5d": {"inputs": ["close", "volume"], "func": idec_296_information_flow_acceleration_vel_5d},
    "idec_297_information_flow_acceleration_vel_21d": {"inputs": ["close", "volume"], "func": idec_297_information_flow_acceleration_vel_21d},
    "idec_298_information_flow_acceleration_vel_63d": {"inputs": ["close", "volume"], "func": idec_298_information_flow_acceleration_vel_63d},
    "idec_299_information_flow_acceleration_vel_126d": {"inputs": ["close", "volume"], "func": idec_299_information_flow_acceleration_vel_126d},
    "idec_300_information_flow_acceleration_vel_252d": {"inputs": ["close", "volume"], "func": idec_300_information_flow_acceleration_vel_252d},
}
