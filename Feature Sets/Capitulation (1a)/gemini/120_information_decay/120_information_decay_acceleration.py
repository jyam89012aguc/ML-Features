"""
120_information_decay — Acceleration (3rd Derivatives)
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

def idec_301_price_impact_decay_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_301_price_impact_decay_accel_5d
    ECONOMIC RATIONALE: Acceleration of price_impact_decay. Decaying magnitude of recent price impacts.
    """
    return (close.diff(1).abs().ewm(halflife=5).mean()).diff(5).diff(_TD_MON)

def idec_302_price_impact_decay_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_302_price_impact_decay_accel_21d
    ECONOMIC RATIONALE: Acceleration of price_impact_decay. Decaying magnitude of recent price impacts.
    """
    return (close.diff(1).abs().ewm(halflife=5).mean()).diff(21).diff(_TD_MON)

def idec_303_price_impact_decay_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_303_price_impact_decay_accel_63d
    ECONOMIC RATIONALE: Acceleration of price_impact_decay. Decaying magnitude of recent price impacts.
    """
    return (close.diff(1).abs().ewm(halflife=5).mean()).diff(63).diff(_TD_MON)

def idec_304_price_impact_decay_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_304_price_impact_decay_accel_126d
    ECONOMIC RATIONALE: Acceleration of price_impact_decay. Decaying magnitude of recent price impacts.
    """
    return (close.diff(1).abs().ewm(halflife=5).mean()).diff(126).diff(_TD_MON)

def idec_305_price_impact_decay_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_305_price_impact_decay_accel_252d
    ECONOMIC RATIONALE: Acceleration of price_impact_decay. Decaying magnitude of recent price impacts.
    """
    return (close.diff(1).abs().ewm(halflife=5).mean()).diff(252).diff(_TD_MON)

def idec_306_volume_impact_decay_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_306_volume_impact_decay_accel_5d
    ECONOMIC RATIONALE: Acceleration of volume_impact_decay. Decaying intensity of recent volume spikes.
    """
    return (volume.ewm(halflife=5).mean() / volume.rolling(63).mean()).diff(5).diff(_TD_MON)

def idec_307_volume_impact_decay_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_307_volume_impact_decay_accel_21d
    ECONOMIC RATIONALE: Acceleration of volume_impact_decay. Decaying intensity of recent volume spikes.
    """
    return (volume.ewm(halflife=5).mean() / volume.rolling(63).mean()).diff(21).diff(_TD_MON)

def idec_308_volume_impact_decay_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_308_volume_impact_decay_accel_63d
    ECONOMIC RATIONALE: Acceleration of volume_impact_decay. Decaying intensity of recent volume spikes.
    """
    return (volume.ewm(halflife=5).mean() / volume.rolling(63).mean()).diff(63).diff(_TD_MON)

def idec_309_volume_impact_decay_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_309_volume_impact_decay_accel_126d
    ECONOMIC RATIONALE: Acceleration of volume_impact_decay. Decaying intensity of recent volume spikes.
    """
    return (volume.ewm(halflife=5).mean() / volume.rolling(63).mean()).diff(126).diff(_TD_MON)

def idec_310_volume_impact_decay_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_310_volume_impact_decay_accel_252d
    ECONOMIC RATIONALE: Acceleration of volume_impact_decay. Decaying intensity of recent volume spikes.
    """
    return (volume.ewm(halflife=5).mean() / volume.rolling(63).mean()).diff(252).diff(_TD_MON)

def idec_311_information_horizon_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_311_information_horizon_accel_5d
    ECONOMIC RATIONALE: Acceleration of information_horizon. Long-term memory of price levels.
    """
    return (close.rolling(21).corr(close.shift(21))).diff(5).diff(_TD_MON)

def idec_312_information_horizon_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_312_information_horizon_accel_21d
    ECONOMIC RATIONALE: Acceleration of information_horizon. Long-term memory of price levels.
    """
    return (close.rolling(21).corr(close.shift(21))).diff(21).diff(_TD_MON)

def idec_313_information_horizon_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_313_information_horizon_accel_63d
    ECONOMIC RATIONALE: Acceleration of information_horizon. Long-term memory of price levels.
    """
    return (close.rolling(21).corr(close.shift(21))).diff(63).diff(_TD_MON)

def idec_314_information_horizon_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_314_information_horizon_accel_126d
    ECONOMIC RATIONALE: Acceleration of information_horizon. Long-term memory of price levels.
    """
    return (close.rolling(21).corr(close.shift(21))).diff(126).diff(_TD_MON)

def idec_315_information_horizon_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_315_information_horizon_accel_252d
    ECONOMIC RATIONALE: Acceleration of information_horizon. Long-term memory of price levels.
    """
    return (close.rolling(21).corr(close.shift(21))).diff(252).diff(_TD_MON)

def idec_316_news_response_decay_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_316_news_response_decay_accel_5d
    ECONOMIC RATIONALE: Acceleration of news_response_decay. Recent daily change relative to cumulative monthly change.
    """
    return (close.pct_change(1).abs() / close.pct_change(21).abs().shift(1).replace(0, 1e-9)).diff(5).diff(_TD_MON)

def idec_317_news_response_decay_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_317_news_response_decay_accel_21d
    ECONOMIC RATIONALE: Acceleration of news_response_decay. Recent daily change relative to cumulative monthly change.
    """
    return (close.pct_change(1).abs() / close.pct_change(21).abs().shift(1).replace(0, 1e-9)).diff(21).diff(_TD_MON)

def idec_318_news_response_decay_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_318_news_response_decay_accel_63d
    ECONOMIC RATIONALE: Acceleration of news_response_decay. Recent daily change relative to cumulative monthly change.
    """
    return (close.pct_change(1).abs() / close.pct_change(21).abs().shift(1).replace(0, 1e-9)).diff(63).diff(_TD_MON)

def idec_319_news_response_decay_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_319_news_response_decay_accel_126d
    ECONOMIC RATIONALE: Acceleration of news_response_decay. Recent daily change relative to cumulative monthly change.
    """
    return (close.pct_change(1).abs() / close.pct_change(21).abs().shift(1).replace(0, 1e-9)).diff(126).diff(_TD_MON)

def idec_320_news_response_decay_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_320_news_response_decay_accel_252d
    ECONOMIC RATIONALE: Acceleration of news_response_decay. Recent daily change relative to cumulative monthly change.
    """
    return (close.pct_change(1).abs() / close.pct_change(21).abs().shift(1).replace(0, 1e-9)).diff(252).diff(_TD_MON)

def idec_321_autocorr_decay_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_321_autocorr_decay_accel_5d
    ECONOMIC RATIONALE: Acceleration of autocorr_decay. Decay in serial correlation across timeframes.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) / close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1)).replace(0, 1e-9)).diff(5).diff(_TD_MON)

def idec_322_autocorr_decay_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_322_autocorr_decay_accel_21d
    ECONOMIC RATIONALE: Acceleration of autocorr_decay. Decay in serial correlation across timeframes.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) / close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1)).replace(0, 1e-9)).diff(21).diff(_TD_MON)

def idec_323_autocorr_decay_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_323_autocorr_decay_accel_63d
    ECONOMIC RATIONALE: Acceleration of autocorr_decay. Decay in serial correlation across timeframes.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) / close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1)).replace(0, 1e-9)).diff(63).diff(_TD_MON)

def idec_324_autocorr_decay_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_324_autocorr_decay_accel_126d
    ECONOMIC RATIONALE: Acceleration of autocorr_decay. Decay in serial correlation across timeframes.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) / close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1)).replace(0, 1e-9)).diff(126).diff(_TD_MON)

def idec_325_autocorr_decay_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_325_autocorr_decay_accel_252d
    ECONOMIC RATIONALE: Acceleration of autocorr_decay. Decay in serial correlation across timeframes.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) / close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1)).replace(0, 1e-9)).diff(252).diff(_TD_MON)

def idec_326_volatility_mean_reversion_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_326_volatility_mean_reversion_accel_5d
    ECONOMIC RATIONALE: Acceleration of volatility_mean_reversion. Rate at which short-term vol returns to the long-term mean.
    """
    return (close.rolling(21).std() / close.rolling(252).std()).diff(5).diff(_TD_MON)

def idec_327_volatility_mean_reversion_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_327_volatility_mean_reversion_accel_21d
    ECONOMIC RATIONALE: Acceleration of volatility_mean_reversion. Rate at which short-term vol returns to the long-term mean.
    """
    return (close.rolling(21).std() / close.rolling(252).std()).diff(21).diff(_TD_MON)

def idec_328_volatility_mean_reversion_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_328_volatility_mean_reversion_accel_63d
    ECONOMIC RATIONALE: Acceleration of volatility_mean_reversion. Rate at which short-term vol returns to the long-term mean.
    """
    return (close.rolling(21).std() / close.rolling(252).std()).diff(63).diff(_TD_MON)

def idec_329_volatility_mean_reversion_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_329_volatility_mean_reversion_accel_126d
    ECONOMIC RATIONALE: Acceleration of volatility_mean_reversion. Rate at which short-term vol returns to the long-term mean.
    """
    return (close.rolling(21).std() / close.rolling(252).std()).diff(126).diff(_TD_MON)

def idec_330_volatility_mean_reversion_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_330_volatility_mean_reversion_accel_252d
    ECONOMIC RATIONALE: Acceleration of volatility_mean_reversion. Rate at which short-term vol returns to the long-term mean.
    """
    return (close.rolling(21).std() / close.rolling(252).std()).diff(252).diff(_TD_MON)

def idec_331_information_efficiency_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_331_information_efficiency_accel_5d
    ECONOMIC RATIONALE: Acceleration of information_efficiency. Rate of information incorporation into price.
    """
    return (abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)).diff(5).diff(_TD_MON)

def idec_332_information_efficiency_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_332_information_efficiency_accel_21d
    ECONOMIC RATIONALE: Acceleration of information_efficiency. Rate of information incorporation into price.
    """
    return (abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)).diff(21).diff(_TD_MON)

def idec_333_information_efficiency_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_333_information_efficiency_accel_63d
    ECONOMIC RATIONALE: Acceleration of information_efficiency. Rate of information incorporation into price.
    """
    return (abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)).diff(63).diff(_TD_MON)

def idec_334_information_efficiency_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_334_information_efficiency_accel_126d
    ECONOMIC RATIONALE: Acceleration of information_efficiency. Rate of information incorporation into price.
    """
    return (abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)).diff(126).diff(_TD_MON)

def idec_335_information_efficiency_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_335_information_efficiency_accel_252d
    ECONOMIC RATIONALE: Acceleration of information_efficiency. Rate of information incorporation into price.
    """
    return (abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)).diff(252).diff(_TD_MON)

def idec_336_signal_noise_decay_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_336_signal_noise_decay_accel_5d
    ECONOMIC RATIONALE: Acceleration of signal_noise_decay. Decay of signal strength relative to noise.
    """
    return (close.rolling(21).mean().diff(5).abs() / close.rolling(21).std().replace(0, 1e-9)).diff(5).diff(_TD_MON)

def idec_337_signal_noise_decay_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_337_signal_noise_decay_accel_21d
    ECONOMIC RATIONALE: Acceleration of signal_noise_decay. Decay of signal strength relative to noise.
    """
    return (close.rolling(21).mean().diff(5).abs() / close.rolling(21).std().replace(0, 1e-9)).diff(21).diff(_TD_MON)

def idec_338_signal_noise_decay_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_338_signal_noise_decay_accel_63d
    ECONOMIC RATIONALE: Acceleration of signal_noise_decay. Decay of signal strength relative to noise.
    """
    return (close.rolling(21).mean().diff(5).abs() / close.rolling(21).std().replace(0, 1e-9)).diff(63).diff(_TD_MON)

def idec_339_signal_noise_decay_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_339_signal_noise_decay_accel_126d
    ECONOMIC RATIONALE: Acceleration of signal_noise_decay. Decay of signal strength relative to noise.
    """
    return (close.rolling(21).mean().diff(5).abs() / close.rolling(21).std().replace(0, 1e-9)).diff(126).diff(_TD_MON)

def idec_340_signal_noise_decay_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_340_signal_noise_decay_accel_252d
    ECONOMIC RATIONALE: Acceleration of signal_noise_decay. Decay of signal strength relative to noise.
    """
    return (close.rolling(21).mean().diff(5).abs() / close.rolling(21).std().replace(0, 1e-9)).diff(252).diff(_TD_MON)

def idec_341_memory_length_proxy_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_341_memory_length_proxy_accel_5d
    ECONOMIC RATIONALE: Acceleration of memory_length_proxy. Estimated length of price memory.
    """
    return (close.rolling(252).apply(lambda x: np.argmax(np.correlate(x-np.mean(x), x-np.mean(x), mode='full')[len(x):]))).diff(5).diff(_TD_MON)

def idec_342_memory_length_proxy_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_342_memory_length_proxy_accel_21d
    ECONOMIC RATIONALE: Acceleration of memory_length_proxy. Estimated length of price memory.
    """
    return (close.rolling(252).apply(lambda x: np.argmax(np.correlate(x-np.mean(x), x-np.mean(x), mode='full')[len(x):]))).diff(21).diff(_TD_MON)

def idec_343_memory_length_proxy_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_343_memory_length_proxy_accel_63d
    ECONOMIC RATIONALE: Acceleration of memory_length_proxy. Estimated length of price memory.
    """
    return (close.rolling(252).apply(lambda x: np.argmax(np.correlate(x-np.mean(x), x-np.mean(x), mode='full')[len(x):]))).diff(63).diff(_TD_MON)

def idec_344_memory_length_proxy_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_344_memory_length_proxy_accel_126d
    ECONOMIC RATIONALE: Acceleration of memory_length_proxy. Estimated length of price memory.
    """
    return (close.rolling(252).apply(lambda x: np.argmax(np.correlate(x-np.mean(x), x-np.mean(x), mode='full')[len(x):]))).diff(126).diff(_TD_MON)

def idec_345_memory_length_proxy_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_345_memory_length_proxy_accel_252d
    ECONOMIC RATIONALE: Acceleration of memory_length_proxy. Estimated length of price memory.
    """
    return (close.rolling(252).apply(lambda x: np.argmax(np.correlate(x-np.mean(x), x-np.mean(x), mode='full')[len(x):]))).diff(252).diff(_TD_MON)

def idec_346_information_shock_persistence_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_346_information_shock_persistence_accel_5d
    ECONOMIC RATIONALE: Acceleration of information_shock_persistence. Persistence of information-driven price volatility.
    """
    return (close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()).diff(5).diff(_TD_MON)

def idec_347_information_shock_persistence_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_347_information_shock_persistence_accel_21d
    ECONOMIC RATIONALE: Acceleration of information_shock_persistence. Persistence of information-driven price volatility.
    """
    return (close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()).diff(21).diff(_TD_MON)

def idec_348_information_shock_persistence_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_348_information_shock_persistence_accel_63d
    ECONOMIC RATIONALE: Acceleration of information_shock_persistence. Persistence of information-driven price volatility.
    """
    return (close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()).diff(63).diff(_TD_MON)

def idec_349_information_shock_persistence_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_349_information_shock_persistence_accel_126d
    ECONOMIC RATIONALE: Acceleration of information_shock_persistence. Persistence of information-driven price volatility.
    """
    return (close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()).diff(126).diff(_TD_MON)

def idec_350_information_shock_persistence_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_350_information_shock_persistence_accel_252d
    ECONOMIC RATIONALE: Acceleration of information_shock_persistence. Persistence of information-driven price volatility.
    """
    return (close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()).diff(252).diff(_TD_MON)

def idec_351_drift_decay_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_351_drift_decay_accel_5d
    ECONOMIC RATIONALE: Acceleration of drift_decay. Decay of short-term drift relative to quarterly trend.
    """
    return (close.pct_change(5).abs() / close.pct_change(63).abs().replace(0, 1e-9)).diff(5).diff(_TD_MON)

def idec_352_drift_decay_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_352_drift_decay_accel_21d
    ECONOMIC RATIONALE: Acceleration of drift_decay. Decay of short-term drift relative to quarterly trend.
    """
    return (close.pct_change(5).abs() / close.pct_change(63).abs().replace(0, 1e-9)).diff(21).diff(_TD_MON)

def idec_353_drift_decay_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_353_drift_decay_accel_63d
    ECONOMIC RATIONALE: Acceleration of drift_decay. Decay of short-term drift relative to quarterly trend.
    """
    return (close.pct_change(5).abs() / close.pct_change(63).abs().replace(0, 1e-9)).diff(63).diff(_TD_MON)

def idec_354_drift_decay_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_354_drift_decay_accel_126d
    ECONOMIC RATIONALE: Acceleration of drift_decay. Decay of short-term drift relative to quarterly trend.
    """
    return (close.pct_change(5).abs() / close.pct_change(63).abs().replace(0, 1e-9)).diff(126).diff(_TD_MON)

def idec_355_drift_decay_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_355_drift_decay_accel_252d
    ECONOMIC RATIONALE: Acceleration of drift_decay. Decay of short-term drift relative to quarterly trend.
    """
    return (close.pct_change(5).abs() / close.pct_change(63).abs().replace(0, 1e-9)).diff(252).diff(_TD_MON)

def idec_356_information_entropy_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_356_information_entropy_accel_5d
    ECONOMIC RATIONALE: Acceleration of information_entropy. Uncertainty or decay of information in price returns.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))).diff(5).diff(_TD_MON)

def idec_357_information_entropy_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_357_information_entropy_accel_21d
    ECONOMIC RATIONALE: Acceleration of information_entropy. Uncertainty or decay of information in price returns.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))).diff(21).diff(_TD_MON)

def idec_358_information_entropy_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_358_information_entropy_accel_63d
    ECONOMIC RATIONALE: Acceleration of information_entropy. Uncertainty or decay of information in price returns.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))).diff(63).diff(_TD_MON)

def idec_359_information_entropy_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_359_information_entropy_accel_126d
    ECONOMIC RATIONALE: Acceleration of information_entropy. Uncertainty or decay of information in price returns.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))).diff(126).diff(_TD_MON)

def idec_360_information_entropy_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_360_information_entropy_accel_252d
    ECONOMIC RATIONALE: Acceleration of information_entropy. Uncertainty or decay of information in price returns.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))).diff(252).diff(_TD_MON)

def idec_361_volume_memory_decay_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_361_volume_memory_decay_accel_5d
    ECONOMIC RATIONALE: Acceleration of volume_memory_decay. Persistence of volume regimes.
    """
    return (volume.rolling(21).corr(volume.shift(21))).diff(5).diff(_TD_MON)

def idec_362_volume_memory_decay_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_362_volume_memory_decay_accel_21d
    ECONOMIC RATIONALE: Acceleration of volume_memory_decay. Persistence of volume regimes.
    """
    return (volume.rolling(21).corr(volume.shift(21))).diff(21).diff(_TD_MON)

def idec_363_volume_memory_decay_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_363_volume_memory_decay_accel_63d
    ECONOMIC RATIONALE: Acceleration of volume_memory_decay. Persistence of volume regimes.
    """
    return (volume.rolling(21).corr(volume.shift(21))).diff(63).diff(_TD_MON)

def idec_364_volume_memory_decay_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_364_volume_memory_decay_accel_126d
    ECONOMIC RATIONALE: Acceleration of volume_memory_decay. Persistence of volume regimes.
    """
    return (volume.rolling(21).corr(volume.shift(21))).diff(126).diff(_TD_MON)

def idec_365_volume_memory_decay_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_365_volume_memory_decay_accel_252d
    ECONOMIC RATIONALE: Acceleration of volume_memory_decay. Persistence of volume regimes.
    """
    return (volume.rolling(21).corr(volume.shift(21))).diff(252).diff(_TD_MON)

def idec_366_price_stickiness_decay_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_366_price_stickiness_decay_accel_5d
    ECONOMIC RATIONALE: Acceleration of price_stickiness_decay. Change in the rate of price stagnation.
    """
    return ((close.diff(1).abs() < 0.01).rolling(21).mean().diff(21)).diff(5).diff(_TD_MON)

def idec_367_price_stickiness_decay_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_367_price_stickiness_decay_accel_21d
    ECONOMIC RATIONALE: Acceleration of price_stickiness_decay. Change in the rate of price stagnation.
    """
    return ((close.diff(1).abs() < 0.01).rolling(21).mean().diff(21)).diff(21).diff(_TD_MON)

def idec_368_price_stickiness_decay_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_368_price_stickiness_decay_accel_63d
    ECONOMIC RATIONALE: Acceleration of price_stickiness_decay. Change in the rate of price stagnation.
    """
    return ((close.diff(1).abs() < 0.01).rolling(21).mean().diff(21)).diff(63).diff(_TD_MON)

def idec_369_price_stickiness_decay_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_369_price_stickiness_decay_accel_126d
    ECONOMIC RATIONALE: Acceleration of price_stickiness_decay. Change in the rate of price stagnation.
    """
    return ((close.diff(1).abs() < 0.01).rolling(21).mean().diff(21)).diff(126).diff(_TD_MON)

def idec_370_price_stickiness_decay_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_370_price_stickiness_decay_accel_252d
    ECONOMIC RATIONALE: Acceleration of price_stickiness_decay. Change in the rate of price stagnation.
    """
    return ((close.diff(1).abs() < 0.01).rolling(21).mean().diff(21)).diff(252).diff(_TD_MON)

def idec_371_information_flow_acceleration_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_371_information_flow_acceleration_accel_5d
    ECONOMIC RATIONALE: Acceleration of information_flow_acceleration. Acceleration of information flow into price.
    """
    return (close.diff(1).abs().ewm(span=5).mean() / close.diff(1).abs().ewm(span=63).mean()).diff(5).diff(_TD_MON)

def idec_372_information_flow_acceleration_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_372_information_flow_acceleration_accel_21d
    ECONOMIC RATIONALE: Acceleration of information_flow_acceleration. Acceleration of information flow into price.
    """
    return (close.diff(1).abs().ewm(span=5).mean() / close.diff(1).abs().ewm(span=63).mean()).diff(21).diff(_TD_MON)

def idec_373_information_flow_acceleration_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_373_information_flow_acceleration_accel_63d
    ECONOMIC RATIONALE: Acceleration of information_flow_acceleration. Acceleration of information flow into price.
    """
    return (close.diff(1).abs().ewm(span=5).mean() / close.diff(1).abs().ewm(span=63).mean()).diff(63).diff(_TD_MON)

def idec_374_information_flow_acceleration_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_374_information_flow_acceleration_accel_126d
    ECONOMIC RATIONALE: Acceleration of information_flow_acceleration. Acceleration of information flow into price.
    """
    return (close.diff(1).abs().ewm(span=5).mean() / close.diff(1).abs().ewm(span=63).mean()).diff(126).diff(_TD_MON)

def idec_375_information_flow_acceleration_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_375_information_flow_acceleration_accel_252d
    ECONOMIC RATIONALE: Acceleration of information_flow_acceleration. Acceleration of information flow into price.
    """
    return (close.diff(1).abs().ewm(span=5).mean() / close.diff(1).abs().ewm(span=63).mean()).diff(252).diff(_TD_MON)

# ── Registry ──────────────────────────────────────────────────────────────────
V120_REGISTRY_ACCEL = {
    "idec_301_price_impact_decay_accel_5d": {"inputs": ["close", "volume"], "func": idec_301_price_impact_decay_accel_5d},
    "idec_302_price_impact_decay_accel_21d": {"inputs": ["close", "volume"], "func": idec_302_price_impact_decay_accel_21d},
    "idec_303_price_impact_decay_accel_63d": {"inputs": ["close", "volume"], "func": idec_303_price_impact_decay_accel_63d},
    "idec_304_price_impact_decay_accel_126d": {"inputs": ["close", "volume"], "func": idec_304_price_impact_decay_accel_126d},
    "idec_305_price_impact_decay_accel_252d": {"inputs": ["close", "volume"], "func": idec_305_price_impact_decay_accel_252d},
    "idec_306_volume_impact_decay_accel_5d": {"inputs": ["close", "volume"], "func": idec_306_volume_impact_decay_accel_5d},
    "idec_307_volume_impact_decay_accel_21d": {"inputs": ["close", "volume"], "func": idec_307_volume_impact_decay_accel_21d},
    "idec_308_volume_impact_decay_accel_63d": {"inputs": ["close", "volume"], "func": idec_308_volume_impact_decay_accel_63d},
    "idec_309_volume_impact_decay_accel_126d": {"inputs": ["close", "volume"], "func": idec_309_volume_impact_decay_accel_126d},
    "idec_310_volume_impact_decay_accel_252d": {"inputs": ["close", "volume"], "func": idec_310_volume_impact_decay_accel_252d},
    "idec_311_information_horizon_accel_5d": {"inputs": ["close", "volume"], "func": idec_311_information_horizon_accel_5d},
    "idec_312_information_horizon_accel_21d": {"inputs": ["close", "volume"], "func": idec_312_information_horizon_accel_21d},
    "idec_313_information_horizon_accel_63d": {"inputs": ["close", "volume"], "func": idec_313_information_horizon_accel_63d},
    "idec_314_information_horizon_accel_126d": {"inputs": ["close", "volume"], "func": idec_314_information_horizon_accel_126d},
    "idec_315_information_horizon_accel_252d": {"inputs": ["close", "volume"], "func": idec_315_information_horizon_accel_252d},
    "idec_316_news_response_decay_accel_5d": {"inputs": ["close", "volume"], "func": idec_316_news_response_decay_accel_5d},
    "idec_317_news_response_decay_accel_21d": {"inputs": ["close", "volume"], "func": idec_317_news_response_decay_accel_21d},
    "idec_318_news_response_decay_accel_63d": {"inputs": ["close", "volume"], "func": idec_318_news_response_decay_accel_63d},
    "idec_319_news_response_decay_accel_126d": {"inputs": ["close", "volume"], "func": idec_319_news_response_decay_accel_126d},
    "idec_320_news_response_decay_accel_252d": {"inputs": ["close", "volume"], "func": idec_320_news_response_decay_accel_252d},
    "idec_321_autocorr_decay_accel_5d": {"inputs": ["close", "volume"], "func": idec_321_autocorr_decay_accel_5d},
    "idec_322_autocorr_decay_accel_21d": {"inputs": ["close", "volume"], "func": idec_322_autocorr_decay_accel_21d},
    "idec_323_autocorr_decay_accel_63d": {"inputs": ["close", "volume"], "func": idec_323_autocorr_decay_accel_63d},
    "idec_324_autocorr_decay_accel_126d": {"inputs": ["close", "volume"], "func": idec_324_autocorr_decay_accel_126d},
    "idec_325_autocorr_decay_accel_252d": {"inputs": ["close", "volume"], "func": idec_325_autocorr_decay_accel_252d},
    "idec_326_volatility_mean_reversion_accel_5d": {"inputs": ["close", "volume"], "func": idec_326_volatility_mean_reversion_accel_5d},
    "idec_327_volatility_mean_reversion_accel_21d": {"inputs": ["close", "volume"], "func": idec_327_volatility_mean_reversion_accel_21d},
    "idec_328_volatility_mean_reversion_accel_63d": {"inputs": ["close", "volume"], "func": idec_328_volatility_mean_reversion_accel_63d},
    "idec_329_volatility_mean_reversion_accel_126d": {"inputs": ["close", "volume"], "func": idec_329_volatility_mean_reversion_accel_126d},
    "idec_330_volatility_mean_reversion_accel_252d": {"inputs": ["close", "volume"], "func": idec_330_volatility_mean_reversion_accel_252d},
    "idec_331_information_efficiency_accel_5d": {"inputs": ["close", "volume"], "func": idec_331_information_efficiency_accel_5d},
    "idec_332_information_efficiency_accel_21d": {"inputs": ["close", "volume"], "func": idec_332_information_efficiency_accel_21d},
    "idec_333_information_efficiency_accel_63d": {"inputs": ["close", "volume"], "func": idec_333_information_efficiency_accel_63d},
    "idec_334_information_efficiency_accel_126d": {"inputs": ["close", "volume"], "func": idec_334_information_efficiency_accel_126d},
    "idec_335_information_efficiency_accel_252d": {"inputs": ["close", "volume"], "func": idec_335_information_efficiency_accel_252d},
    "idec_336_signal_noise_decay_accel_5d": {"inputs": ["close", "volume"], "func": idec_336_signal_noise_decay_accel_5d},
    "idec_337_signal_noise_decay_accel_21d": {"inputs": ["close", "volume"], "func": idec_337_signal_noise_decay_accel_21d},
    "idec_338_signal_noise_decay_accel_63d": {"inputs": ["close", "volume"], "func": idec_338_signal_noise_decay_accel_63d},
    "idec_339_signal_noise_decay_accel_126d": {"inputs": ["close", "volume"], "func": idec_339_signal_noise_decay_accel_126d},
    "idec_340_signal_noise_decay_accel_252d": {"inputs": ["close", "volume"], "func": idec_340_signal_noise_decay_accel_252d},
    "idec_341_memory_length_proxy_accel_5d": {"inputs": ["close", "volume"], "func": idec_341_memory_length_proxy_accel_5d},
    "idec_342_memory_length_proxy_accel_21d": {"inputs": ["close", "volume"], "func": idec_342_memory_length_proxy_accel_21d},
    "idec_343_memory_length_proxy_accel_63d": {"inputs": ["close", "volume"], "func": idec_343_memory_length_proxy_accel_63d},
    "idec_344_memory_length_proxy_accel_126d": {"inputs": ["close", "volume"], "func": idec_344_memory_length_proxy_accel_126d},
    "idec_345_memory_length_proxy_accel_252d": {"inputs": ["close", "volume"], "func": idec_345_memory_length_proxy_accel_252d},
    "idec_346_information_shock_persistence_accel_5d": {"inputs": ["close", "volume"], "func": idec_346_information_shock_persistence_accel_5d},
    "idec_347_information_shock_persistence_accel_21d": {"inputs": ["close", "volume"], "func": idec_347_information_shock_persistence_accel_21d},
    "idec_348_information_shock_persistence_accel_63d": {"inputs": ["close", "volume"], "func": idec_348_information_shock_persistence_accel_63d},
    "idec_349_information_shock_persistence_accel_126d": {"inputs": ["close", "volume"], "func": idec_349_information_shock_persistence_accel_126d},
    "idec_350_information_shock_persistence_accel_252d": {"inputs": ["close", "volume"], "func": idec_350_information_shock_persistence_accel_252d},
    "idec_351_drift_decay_accel_5d": {"inputs": ["close", "volume"], "func": idec_351_drift_decay_accel_5d},
    "idec_352_drift_decay_accel_21d": {"inputs": ["close", "volume"], "func": idec_352_drift_decay_accel_21d},
    "idec_353_drift_decay_accel_63d": {"inputs": ["close", "volume"], "func": idec_353_drift_decay_accel_63d},
    "idec_354_drift_decay_accel_126d": {"inputs": ["close", "volume"], "func": idec_354_drift_decay_accel_126d},
    "idec_355_drift_decay_accel_252d": {"inputs": ["close", "volume"], "func": idec_355_drift_decay_accel_252d},
    "idec_356_information_entropy_accel_5d": {"inputs": ["close", "volume"], "func": idec_356_information_entropy_accel_5d},
    "idec_357_information_entropy_accel_21d": {"inputs": ["close", "volume"], "func": idec_357_information_entropy_accel_21d},
    "idec_358_information_entropy_accel_63d": {"inputs": ["close", "volume"], "func": idec_358_information_entropy_accel_63d},
    "idec_359_information_entropy_accel_126d": {"inputs": ["close", "volume"], "func": idec_359_information_entropy_accel_126d},
    "idec_360_information_entropy_accel_252d": {"inputs": ["close", "volume"], "func": idec_360_information_entropy_accel_252d},
    "idec_361_volume_memory_decay_accel_5d": {"inputs": ["close", "volume"], "func": idec_361_volume_memory_decay_accel_5d},
    "idec_362_volume_memory_decay_accel_21d": {"inputs": ["close", "volume"], "func": idec_362_volume_memory_decay_accel_21d},
    "idec_363_volume_memory_decay_accel_63d": {"inputs": ["close", "volume"], "func": idec_363_volume_memory_decay_accel_63d},
    "idec_364_volume_memory_decay_accel_126d": {"inputs": ["close", "volume"], "func": idec_364_volume_memory_decay_accel_126d},
    "idec_365_volume_memory_decay_accel_252d": {"inputs": ["close", "volume"], "func": idec_365_volume_memory_decay_accel_252d},
    "idec_366_price_stickiness_decay_accel_5d": {"inputs": ["close", "volume"], "func": idec_366_price_stickiness_decay_accel_5d},
    "idec_367_price_stickiness_decay_accel_21d": {"inputs": ["close", "volume"], "func": idec_367_price_stickiness_decay_accel_21d},
    "idec_368_price_stickiness_decay_accel_63d": {"inputs": ["close", "volume"], "func": idec_368_price_stickiness_decay_accel_63d},
    "idec_369_price_stickiness_decay_accel_126d": {"inputs": ["close", "volume"], "func": idec_369_price_stickiness_decay_accel_126d},
    "idec_370_price_stickiness_decay_accel_252d": {"inputs": ["close", "volume"], "func": idec_370_price_stickiness_decay_accel_252d},
    "idec_371_information_flow_acceleration_accel_5d": {"inputs": ["close", "volume"], "func": idec_371_information_flow_acceleration_accel_5d},
    "idec_372_information_flow_acceleration_accel_21d": {"inputs": ["close", "volume"], "func": idec_372_information_flow_acceleration_accel_21d},
    "idec_373_information_flow_acceleration_accel_63d": {"inputs": ["close", "volume"], "func": idec_373_information_flow_acceleration_accel_63d},
    "idec_374_information_flow_acceleration_accel_126d": {"inputs": ["close", "volume"], "func": idec_374_information_flow_acceleration_accel_126d},
    "idec_375_information_flow_acceleration_accel_252d": {"inputs": ["close", "volume"], "func": idec_375_information_flow_acceleration_accel_252d},
}
