"""
119_volume_shock_aftermath — Velocity (2nd Derivatives)
Domain: volume_shock_aftermath
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

def vsha_226_volume_shock_mag_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_226_volume_shock_mag_vel_5d
    ECONOMIC RATIONALE: Velocity of volume_shock_mag. Magnitude of the current volume shock.
    """
    return (volume / volume.rolling(63).mean()).diff(5)

def vsha_227_volume_shock_mag_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_227_volume_shock_mag_vel_21d
    ECONOMIC RATIONALE: Velocity of volume_shock_mag. Magnitude of the current volume shock.
    """
    return (volume / volume.rolling(63).mean()).diff(21)

def vsha_228_volume_shock_mag_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_228_volume_shock_mag_vel_63d
    ECONOMIC RATIONALE: Velocity of volume_shock_mag. Magnitude of the current volume shock.
    """
    return (volume / volume.rolling(63).mean()).diff(63)

def vsha_229_volume_shock_mag_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_229_volume_shock_mag_vel_126d
    ECONOMIC RATIONALE: Velocity of volume_shock_mag. Magnitude of the current volume shock.
    """
    return (volume / volume.rolling(63).mean()).diff(126)

def vsha_230_volume_shock_mag_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_230_volume_shock_mag_vel_252d
    ECONOMIC RATIONALE: Velocity of volume_shock_mag. Magnitude of the current volume shock.
    """
    return (volume / volume.rolling(63).mean()).diff(252)

def vsha_231_post_shock_drift_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_231_post_shock_drift_vel_5d
    ECONOMIC RATIONALE: Velocity of post_shock_drift. Price drift following major volume shocks.
    """
    return (close.pct_change(21) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*2).astype(float)).diff(5)

def vsha_232_post_shock_drift_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_232_post_shock_drift_vel_21d
    ECONOMIC RATIONALE: Velocity of post_shock_drift. Price drift following major volume shocks.
    """
    return (close.pct_change(21) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*2).astype(float)).diff(21)

def vsha_233_post_shock_drift_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_233_post_shock_drift_vel_63d
    ECONOMIC RATIONALE: Velocity of post_shock_drift. Price drift following major volume shocks.
    """
    return (close.pct_change(21) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*2).astype(float)).diff(63)

def vsha_234_post_shock_drift_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_234_post_shock_drift_vel_126d
    ECONOMIC RATIONALE: Velocity of post_shock_drift. Price drift following major volume shocks.
    """
    return (close.pct_change(21) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*2).astype(float)).diff(126)

def vsha_235_post_shock_drift_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_235_post_shock_drift_vel_252d
    ECONOMIC RATIONALE: Velocity of post_shock_drift. Price drift following major volume shocks.
    """
    return (close.pct_change(21) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*2).astype(float)).diff(252)

def vsha_236_shock_volatility_expansion_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_236_shock_volatility_expansion_vel_5d
    ECONOMIC RATIONALE: Velocity of shock_volatility_expansion. Volatility expansion associated with volume shocks.
    """
    return (close.rolling(21).std() / close.rolling(252).std() * (volume > volume.rolling(63).mean()*2).astype(float)).diff(5)

def vsha_237_shock_volatility_expansion_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_237_shock_volatility_expansion_vel_21d
    ECONOMIC RATIONALE: Velocity of shock_volatility_expansion. Volatility expansion associated with volume shocks.
    """
    return (close.rolling(21).std() / close.rolling(252).std() * (volume > volume.rolling(63).mean()*2).astype(float)).diff(21)

def vsha_238_shock_volatility_expansion_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_238_shock_volatility_expansion_vel_63d
    ECONOMIC RATIONALE: Velocity of shock_volatility_expansion. Volatility expansion associated with volume shocks.
    """
    return (close.rolling(21).std() / close.rolling(252).std() * (volume > volume.rolling(63).mean()*2).astype(float)).diff(63)

def vsha_239_shock_volatility_expansion_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_239_shock_volatility_expansion_vel_126d
    ECONOMIC RATIONALE: Velocity of shock_volatility_expansion. Volatility expansion associated with volume shocks.
    """
    return (close.rolling(21).std() / close.rolling(252).std() * (volume > volume.rolling(63).mean()*2).astype(float)).diff(126)

def vsha_240_shock_volatility_expansion_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_240_shock_volatility_expansion_vel_252d
    ECONOMIC RATIONALE: Velocity of shock_volatility_expansion. Volatility expansion associated with volume shocks.
    """
    return (close.rolling(21).std() / close.rolling(252).std() * (volume > volume.rolling(63).mean()*2).astype(float)).diff(252)

def vsha_241_volume_shock_reversal_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_241_volume_shock_reversal_vel_5d
    ECONOMIC RATIONALE: Velocity of volume_shock_reversal. Reversal of price direction after a volume shock.
    """
    return ((close.diff(5) * close.diff(5).shift(5) < 0) * (volume > volume.rolling(63).mean()*2).astype(float)).diff(5)

def vsha_242_volume_shock_reversal_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_242_volume_shock_reversal_vel_21d
    ECONOMIC RATIONALE: Velocity of volume_shock_reversal. Reversal of price direction after a volume shock.
    """
    return ((close.diff(5) * close.diff(5).shift(5) < 0) * (volume > volume.rolling(63).mean()*2).astype(float)).diff(21)

def vsha_243_volume_shock_reversal_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_243_volume_shock_reversal_vel_63d
    ECONOMIC RATIONALE: Velocity of volume_shock_reversal. Reversal of price direction after a volume shock.
    """
    return ((close.diff(5) * close.diff(5).shift(5) < 0) * (volume > volume.rolling(63).mean()*2).astype(float)).diff(63)

def vsha_244_volume_shock_reversal_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_244_volume_shock_reversal_vel_126d
    ECONOMIC RATIONALE: Velocity of volume_shock_reversal. Reversal of price direction after a volume shock.
    """
    return ((close.diff(5) * close.diff(5).shift(5) < 0) * (volume > volume.rolling(63).mean()*2).astype(float)).diff(126)

def vsha_245_volume_shock_reversal_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_245_volume_shock_reversal_vel_252d
    ECONOMIC RATIONALE: Velocity of volume_shock_reversal. Reversal of price direction after a volume shock.
    """
    return ((close.diff(5) * close.diff(5).shift(5) < 0) * (volume > volume.rolling(63).mean()*2).astype(float)).diff(252)

def vsha_246_shock_persistence_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_246_shock_persistence_vel_5d
    ECONOMIC RATIONALE: Velocity of shock_persistence. Duration of a high-volume regime.
    """
    return ((volume > volume.rolling(63).mean()*2).rolling(10).sum()).diff(5)

def vsha_247_shock_persistence_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_247_shock_persistence_vel_21d
    ECONOMIC RATIONALE: Velocity of shock_persistence. Duration of a high-volume regime.
    """
    return ((volume > volume.rolling(63).mean()*2).rolling(10).sum()).diff(21)

def vsha_248_shock_persistence_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_248_shock_persistence_vel_63d
    ECONOMIC RATIONALE: Velocity of shock_persistence. Duration of a high-volume regime.
    """
    return ((volume > volume.rolling(63).mean()*2).rolling(10).sum()).diff(63)

def vsha_249_shock_persistence_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_249_shock_persistence_vel_126d
    ECONOMIC RATIONALE: Velocity of shock_persistence. Duration of a high-volume regime.
    """
    return ((volume > volume.rolling(63).mean()*2).rolling(10).sum()).diff(126)

def vsha_250_shock_persistence_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_250_shock_persistence_vel_252d
    ECONOMIC RATIONALE: Velocity of shock_persistence. Duration of a high-volume regime.
    """
    return ((volume > volume.rolling(63).mean()*2).rolling(10).sum()).diff(252)

def vsha_251_volume_shock_z_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_251_volume_shock_z_vel_5d
    ECONOMIC RATIONALE: Velocity of volume_shock_z. Z-score of volume relative to annual history.
    """
    return (_zscore_rolling(volume, 252)).diff(5)

def vsha_252_volume_shock_z_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_252_volume_shock_z_vel_21d
    ECONOMIC RATIONALE: Velocity of volume_shock_z. Z-score of volume relative to annual history.
    """
    return (_zscore_rolling(volume, 252)).diff(21)

def vsha_253_volume_shock_z_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_253_volume_shock_z_vel_63d
    ECONOMIC RATIONALE: Velocity of volume_shock_z. Z-score of volume relative to annual history.
    """
    return (_zscore_rolling(volume, 252)).diff(63)

def vsha_254_volume_shock_z_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_254_volume_shock_z_vel_126d
    ECONOMIC RATIONALE: Velocity of volume_shock_z. Z-score of volume relative to annual history.
    """
    return (_zscore_rolling(volume, 252)).diff(126)

def vsha_255_volume_shock_z_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_255_volume_shock_z_vel_252d
    ECONOMIC RATIONALE: Velocity of volume_shock_z. Z-score of volume relative to annual history.
    """
    return (_zscore_rolling(volume, 252)).diff(252)

def vsha_256_shock_price_impact_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_256_shock_price_impact_vel_5d
    ECONOMIC RATIONALE: Velocity of shock_price_impact. Price change weighted by the volume shock magnitude.
    """
    return (close.diff(1) * (volume / volume.rolling(63).mean())).diff(5)

def vsha_257_shock_price_impact_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_257_shock_price_impact_vel_21d
    ECONOMIC RATIONALE: Velocity of shock_price_impact. Price change weighted by the volume shock magnitude.
    """
    return (close.diff(1) * (volume / volume.rolling(63).mean())).diff(21)

def vsha_258_shock_price_impact_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_258_shock_price_impact_vel_63d
    ECONOMIC RATIONALE: Velocity of shock_price_impact. Price change weighted by the volume shock magnitude.
    """
    return (close.diff(1) * (volume / volume.rolling(63).mean())).diff(63)

def vsha_259_shock_price_impact_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_259_shock_price_impact_vel_126d
    ECONOMIC RATIONALE: Velocity of shock_price_impact. Price change weighted by the volume shock magnitude.
    """
    return (close.diff(1) * (volume / volume.rolling(63).mean())).diff(126)

def vsha_260_shock_price_impact_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_260_shock_price_impact_vel_252d
    ECONOMIC RATIONALE: Velocity of shock_price_impact. Price change weighted by the volume shock magnitude.
    """
    return (close.diff(1) * (volume / volume.rolling(63).mean())).diff(252)

def vsha_261_post_shock_liquidity_drain_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_261_post_shock_liquidity_drain_vel_5d
    ECONOMIC RATIONALE: Velocity of post_shock_liquidity_drain. Liquidity dry-up following a massive shock.
    """
    return ((volume.rolling(5).mean() / volume.rolling(63).mean()) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*3).astype(float)).diff(5)

def vsha_262_post_shock_liquidity_drain_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_262_post_shock_liquidity_drain_vel_21d
    ECONOMIC RATIONALE: Velocity of post_shock_liquidity_drain. Liquidity dry-up following a massive shock.
    """
    return ((volume.rolling(5).mean() / volume.rolling(63).mean()) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*3).astype(float)).diff(21)

def vsha_263_post_shock_liquidity_drain_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_263_post_shock_liquidity_drain_vel_63d
    ECONOMIC RATIONALE: Velocity of post_shock_liquidity_drain. Liquidity dry-up following a massive shock.
    """
    return ((volume.rolling(5).mean() / volume.rolling(63).mean()) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*3).astype(float)).diff(63)

def vsha_264_post_shock_liquidity_drain_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_264_post_shock_liquidity_drain_vel_126d
    ECONOMIC RATIONALE: Velocity of post_shock_liquidity_drain. Liquidity dry-up following a massive shock.
    """
    return ((volume.rolling(5).mean() / volume.rolling(63).mean()) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*3).astype(float)).diff(126)

def vsha_265_post_shock_liquidity_drain_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_265_post_shock_liquidity_drain_vel_252d
    ECONOMIC RATIONALE: Velocity of post_shock_liquidity_drain. Liquidity dry-up following a massive shock.
    """
    return ((volume.rolling(5).mean() / volume.rolling(63).mean()) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*3).astype(float)).diff(252)

def vsha_266_shock_clustering_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_266_shock_clustering_vel_5d
    ECONOMIC RATIONALE: Velocity of shock_clustering. Frequency of volume shocks in the last quarter.
    """
    return ((volume > volume.rolling(63).mean()*2).rolling(63).sum()).diff(5)

def vsha_267_shock_clustering_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_267_shock_clustering_vel_21d
    ECONOMIC RATIONALE: Velocity of shock_clustering. Frequency of volume shocks in the last quarter.
    """
    return ((volume > volume.rolling(63).mean()*2).rolling(63).sum()).diff(21)

def vsha_268_shock_clustering_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_268_shock_clustering_vel_63d
    ECONOMIC RATIONALE: Velocity of shock_clustering. Frequency of volume shocks in the last quarter.
    """
    return ((volume > volume.rolling(63).mean()*2).rolling(63).sum()).diff(63)

def vsha_269_shock_clustering_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_269_shock_clustering_vel_126d
    ECONOMIC RATIONALE: Velocity of shock_clustering. Frequency of volume shocks in the last quarter.
    """
    return ((volume > volume.rolling(63).mean()*2).rolling(63).sum()).diff(126)

def vsha_270_shock_clustering_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_270_shock_clustering_vel_252d
    ECONOMIC RATIONALE: Velocity of shock_clustering. Frequency of volume shocks in the last quarter.
    """
    return ((volume > volume.rolling(63).mean()*2).rolling(63).sum()).diff(252)

def vsha_271_volume_shock_entropy_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_271_volume_shock_entropy_vel_5d
    ECONOMIC RATIONALE: Velocity of volume_shock_entropy. Unpredictability of volume during shocks.
    """
    return (volume.rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))).diff(5)

def vsha_272_volume_shock_entropy_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_272_volume_shock_entropy_vel_21d
    ECONOMIC RATIONALE: Velocity of volume_shock_entropy. Unpredictability of volume during shocks.
    """
    return (volume.rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))).diff(21)

def vsha_273_volume_shock_entropy_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_273_volume_shock_entropy_vel_63d
    ECONOMIC RATIONALE: Velocity of volume_shock_entropy. Unpredictability of volume during shocks.
    """
    return (volume.rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))).diff(63)

def vsha_274_volume_shock_entropy_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_274_volume_shock_entropy_vel_126d
    ECONOMIC RATIONALE: Velocity of volume_shock_entropy. Unpredictability of volume during shocks.
    """
    return (volume.rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))).diff(126)

def vsha_275_volume_shock_entropy_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_275_volume_shock_entropy_vel_252d
    ECONOMIC RATIONALE: Velocity of volume_shock_entropy. Unpredictability of volume during shocks.
    """
    return (volume.rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))).diff(252)

def vsha_276_shock_exhaustion_proxy_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_276_shock_exhaustion_proxy_vel_5d
    ECONOMIC RATIONALE: Velocity of shock_exhaustion_proxy. Large volume shock with minimal price impact.
    """
    return ((volume > volume.rolling(63).mean()*3) & (close.diff(1).abs() < close.rolling(21).std()*0.5)).diff(5)

def vsha_277_shock_exhaustion_proxy_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_277_shock_exhaustion_proxy_vel_21d
    ECONOMIC RATIONALE: Velocity of shock_exhaustion_proxy. Large volume shock with minimal price impact.
    """
    return ((volume > volume.rolling(63).mean()*3) & (close.diff(1).abs() < close.rolling(21).std()*0.5)).diff(21)

def vsha_278_shock_exhaustion_proxy_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_278_shock_exhaustion_proxy_vel_63d
    ECONOMIC RATIONALE: Velocity of shock_exhaustion_proxy. Large volume shock with minimal price impact.
    """
    return ((volume > volume.rolling(63).mean()*3) & (close.diff(1).abs() < close.rolling(21).std()*0.5)).diff(63)

def vsha_279_shock_exhaustion_proxy_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_279_shock_exhaustion_proxy_vel_126d
    ECONOMIC RATIONALE: Velocity of shock_exhaustion_proxy. Large volume shock with minimal price impact.
    """
    return ((volume > volume.rolling(63).mean()*3) & (close.diff(1).abs() < close.rolling(21).std()*0.5)).diff(126)

def vsha_280_shock_exhaustion_proxy_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_280_shock_exhaustion_proxy_vel_252d
    ECONOMIC RATIONALE: Velocity of shock_exhaustion_proxy. Large volume shock with minimal price impact.
    """
    return ((volume > volume.rolling(63).mean()*3) & (close.diff(1).abs() < close.rolling(21).std()*0.5)).diff(252)

def vsha_281_shock_recovery_rate_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_281_shock_recovery_rate_vel_5d
    ECONOMIC RATIONALE: Velocity of shock_recovery_rate. Recovery relative to the price at the last volume peak.
    """
    return (close / close.shift(volume.rolling(63).apply(lambda x: np.argmax(x)))).diff(5)

def vsha_282_shock_recovery_rate_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_282_shock_recovery_rate_vel_21d
    ECONOMIC RATIONALE: Velocity of shock_recovery_rate. Recovery relative to the price at the last volume peak.
    """
    return (close / close.shift(volume.rolling(63).apply(lambda x: np.argmax(x)))).diff(21)

def vsha_283_shock_recovery_rate_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_283_shock_recovery_rate_vel_63d
    ECONOMIC RATIONALE: Velocity of shock_recovery_rate. Recovery relative to the price at the last volume peak.
    """
    return (close / close.shift(volume.rolling(63).apply(lambda x: np.argmax(x)))).diff(63)

def vsha_284_shock_recovery_rate_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_284_shock_recovery_rate_vel_126d
    ECONOMIC RATIONALE: Velocity of shock_recovery_rate. Recovery relative to the price at the last volume peak.
    """
    return (close / close.shift(volume.rolling(63).apply(lambda x: np.argmax(x)))).diff(126)

def vsha_285_shock_recovery_rate_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_285_shock_recovery_rate_vel_252d
    ECONOMIC RATIONALE: Velocity of shock_recovery_rate. Recovery relative to the price at the last volume peak.
    """
    return (close / close.shift(volume.rolling(63).apply(lambda x: np.argmax(x)))).diff(252)

def vsha_286_volume_shock_momentum_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_286_volume_shock_momentum_vel_5d
    ECONOMIC RATIONALE: Velocity of volume_shock_momentum. Synchronized volume and price momentum.
    """
    return (volume.pct_change(5) * close.pct_change(5)).diff(5)

def vsha_287_volume_shock_momentum_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_287_volume_shock_momentum_vel_21d
    ECONOMIC RATIONALE: Velocity of volume_shock_momentum. Synchronized volume and price momentum.
    """
    return (volume.pct_change(5) * close.pct_change(5)).diff(21)

def vsha_288_volume_shock_momentum_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_288_volume_shock_momentum_vel_63d
    ECONOMIC RATIONALE: Velocity of volume_shock_momentum. Synchronized volume and price momentum.
    """
    return (volume.pct_change(5) * close.pct_change(5)).diff(63)

def vsha_289_volume_shock_momentum_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_289_volume_shock_momentum_vel_126d
    ECONOMIC RATIONALE: Velocity of volume_shock_momentum. Synchronized volume and price momentum.
    """
    return (volume.pct_change(5) * close.pct_change(5)).diff(126)

def vsha_290_volume_shock_momentum_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_290_volume_shock_momentum_vel_252d
    ECONOMIC RATIONALE: Velocity of volume_shock_momentum. Synchronized volume and price momentum.
    """
    return (volume.pct_change(5) * close.pct_change(5)).diff(252)

def vsha_291_shock_regime_shift_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_291_shock_regime_shift_vel_5d
    ECONOMIC RATIONALE: Velocity of shock_regime_shift. Structural shift in average volume levels.
    """
    return (volume.rolling(21).mean().diff(21) / volume.rolling(252).std()).diff(5)

def vsha_292_shock_regime_shift_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_292_shock_regime_shift_vel_21d
    ECONOMIC RATIONALE: Velocity of shock_regime_shift. Structural shift in average volume levels.
    """
    return (volume.rolling(21).mean().diff(21) / volume.rolling(252).std()).diff(21)

def vsha_293_shock_regime_shift_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_293_shock_regime_shift_vel_63d
    ECONOMIC RATIONALE: Velocity of shock_regime_shift. Structural shift in average volume levels.
    """
    return (volume.rolling(21).mean().diff(21) / volume.rolling(252).std()).diff(63)

def vsha_294_shock_regime_shift_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_294_shock_regime_shift_vel_126d
    ECONOMIC RATIONALE: Velocity of shock_regime_shift. Structural shift in average volume levels.
    """
    return (volume.rolling(21).mean().diff(21) / volume.rolling(252).std()).diff(126)

def vsha_295_shock_regime_shift_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_295_shock_regime_shift_vel_252d
    ECONOMIC RATIONALE: Velocity of shock_regime_shift. Structural shift in average volume levels.
    """
    return (volume.rolling(21).mean().diff(21) / volume.rolling(252).std()).diff(252)

def vsha_296_volume_shock_tail_corr_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_296_volume_shock_tail_corr_vel_5d
    ECONOMIC RATIONALE: Velocity of volume_shock_tail_corr. Correlation between volume shocks and price magnitude.
    """
    return (volume.rolling(21).corr(close.pct_change(1).abs())).diff(5)

def vsha_297_volume_shock_tail_corr_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_297_volume_shock_tail_corr_vel_21d
    ECONOMIC RATIONALE: Velocity of volume_shock_tail_corr. Correlation between volume shocks and price magnitude.
    """
    return (volume.rolling(21).corr(close.pct_change(1).abs())).diff(21)

def vsha_298_volume_shock_tail_corr_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_298_volume_shock_tail_corr_vel_63d
    ECONOMIC RATIONALE: Velocity of volume_shock_tail_corr. Correlation between volume shocks and price magnitude.
    """
    return (volume.rolling(21).corr(close.pct_change(1).abs())).diff(63)

def vsha_299_volume_shock_tail_corr_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_299_volume_shock_tail_corr_vel_126d
    ECONOMIC RATIONALE: Velocity of volume_shock_tail_corr. Correlation between volume shocks and price magnitude.
    """
    return (volume.rolling(21).corr(close.pct_change(1).abs())).diff(126)

def vsha_300_volume_shock_tail_corr_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_300_volume_shock_tail_corr_vel_252d
    ECONOMIC RATIONALE: Velocity of volume_shock_tail_corr. Correlation between volume shocks and price magnitude.
    """
    return (volume.rolling(21).corr(close.pct_change(1).abs())).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V119_REGISTRY_VEL = {
    "vsha_226_volume_shock_mag_vel_5d": {"inputs": ["close", "volume"], "func": vsha_226_volume_shock_mag_vel_5d},
    "vsha_227_volume_shock_mag_vel_21d": {"inputs": ["close", "volume"], "func": vsha_227_volume_shock_mag_vel_21d},
    "vsha_228_volume_shock_mag_vel_63d": {"inputs": ["close", "volume"], "func": vsha_228_volume_shock_mag_vel_63d},
    "vsha_229_volume_shock_mag_vel_126d": {"inputs": ["close", "volume"], "func": vsha_229_volume_shock_mag_vel_126d},
    "vsha_230_volume_shock_mag_vel_252d": {"inputs": ["close", "volume"], "func": vsha_230_volume_shock_mag_vel_252d},
    "vsha_231_post_shock_drift_vel_5d": {"inputs": ["close", "volume"], "func": vsha_231_post_shock_drift_vel_5d},
    "vsha_232_post_shock_drift_vel_21d": {"inputs": ["close", "volume"], "func": vsha_232_post_shock_drift_vel_21d},
    "vsha_233_post_shock_drift_vel_63d": {"inputs": ["close", "volume"], "func": vsha_233_post_shock_drift_vel_63d},
    "vsha_234_post_shock_drift_vel_126d": {"inputs": ["close", "volume"], "func": vsha_234_post_shock_drift_vel_126d},
    "vsha_235_post_shock_drift_vel_252d": {"inputs": ["close", "volume"], "func": vsha_235_post_shock_drift_vel_252d},
    "vsha_236_shock_volatility_expansion_vel_5d": {"inputs": ["close", "volume"], "func": vsha_236_shock_volatility_expansion_vel_5d},
    "vsha_237_shock_volatility_expansion_vel_21d": {"inputs": ["close", "volume"], "func": vsha_237_shock_volatility_expansion_vel_21d},
    "vsha_238_shock_volatility_expansion_vel_63d": {"inputs": ["close", "volume"], "func": vsha_238_shock_volatility_expansion_vel_63d},
    "vsha_239_shock_volatility_expansion_vel_126d": {"inputs": ["close", "volume"], "func": vsha_239_shock_volatility_expansion_vel_126d},
    "vsha_240_shock_volatility_expansion_vel_252d": {"inputs": ["close", "volume"], "func": vsha_240_shock_volatility_expansion_vel_252d},
    "vsha_241_volume_shock_reversal_vel_5d": {"inputs": ["close", "volume"], "func": vsha_241_volume_shock_reversal_vel_5d},
    "vsha_242_volume_shock_reversal_vel_21d": {"inputs": ["close", "volume"], "func": vsha_242_volume_shock_reversal_vel_21d},
    "vsha_243_volume_shock_reversal_vel_63d": {"inputs": ["close", "volume"], "func": vsha_243_volume_shock_reversal_vel_63d},
    "vsha_244_volume_shock_reversal_vel_126d": {"inputs": ["close", "volume"], "func": vsha_244_volume_shock_reversal_vel_126d},
    "vsha_245_volume_shock_reversal_vel_252d": {"inputs": ["close", "volume"], "func": vsha_245_volume_shock_reversal_vel_252d},
    "vsha_246_shock_persistence_vel_5d": {"inputs": ["close", "volume"], "func": vsha_246_shock_persistence_vel_5d},
    "vsha_247_shock_persistence_vel_21d": {"inputs": ["close", "volume"], "func": vsha_247_shock_persistence_vel_21d},
    "vsha_248_shock_persistence_vel_63d": {"inputs": ["close", "volume"], "func": vsha_248_shock_persistence_vel_63d},
    "vsha_249_shock_persistence_vel_126d": {"inputs": ["close", "volume"], "func": vsha_249_shock_persistence_vel_126d},
    "vsha_250_shock_persistence_vel_252d": {"inputs": ["close", "volume"], "func": vsha_250_shock_persistence_vel_252d},
    "vsha_251_volume_shock_z_vel_5d": {"inputs": ["close", "volume"], "func": vsha_251_volume_shock_z_vel_5d},
    "vsha_252_volume_shock_z_vel_21d": {"inputs": ["close", "volume"], "func": vsha_252_volume_shock_z_vel_21d},
    "vsha_253_volume_shock_z_vel_63d": {"inputs": ["close", "volume"], "func": vsha_253_volume_shock_z_vel_63d},
    "vsha_254_volume_shock_z_vel_126d": {"inputs": ["close", "volume"], "func": vsha_254_volume_shock_z_vel_126d},
    "vsha_255_volume_shock_z_vel_252d": {"inputs": ["close", "volume"], "func": vsha_255_volume_shock_z_vel_252d},
    "vsha_256_shock_price_impact_vel_5d": {"inputs": ["close", "volume"], "func": vsha_256_shock_price_impact_vel_5d},
    "vsha_257_shock_price_impact_vel_21d": {"inputs": ["close", "volume"], "func": vsha_257_shock_price_impact_vel_21d},
    "vsha_258_shock_price_impact_vel_63d": {"inputs": ["close", "volume"], "func": vsha_258_shock_price_impact_vel_63d},
    "vsha_259_shock_price_impact_vel_126d": {"inputs": ["close", "volume"], "func": vsha_259_shock_price_impact_vel_126d},
    "vsha_260_shock_price_impact_vel_252d": {"inputs": ["close", "volume"], "func": vsha_260_shock_price_impact_vel_252d},
    "vsha_261_post_shock_liquidity_drain_vel_5d": {"inputs": ["close", "volume"], "func": vsha_261_post_shock_liquidity_drain_vel_5d},
    "vsha_262_post_shock_liquidity_drain_vel_21d": {"inputs": ["close", "volume"], "func": vsha_262_post_shock_liquidity_drain_vel_21d},
    "vsha_263_post_shock_liquidity_drain_vel_63d": {"inputs": ["close", "volume"], "func": vsha_263_post_shock_liquidity_drain_vel_63d},
    "vsha_264_post_shock_liquidity_drain_vel_126d": {"inputs": ["close", "volume"], "func": vsha_264_post_shock_liquidity_drain_vel_126d},
    "vsha_265_post_shock_liquidity_drain_vel_252d": {"inputs": ["close", "volume"], "func": vsha_265_post_shock_liquidity_drain_vel_252d},
    "vsha_266_shock_clustering_vel_5d": {"inputs": ["close", "volume"], "func": vsha_266_shock_clustering_vel_5d},
    "vsha_267_shock_clustering_vel_21d": {"inputs": ["close", "volume"], "func": vsha_267_shock_clustering_vel_21d},
    "vsha_268_shock_clustering_vel_63d": {"inputs": ["close", "volume"], "func": vsha_268_shock_clustering_vel_63d},
    "vsha_269_shock_clustering_vel_126d": {"inputs": ["close", "volume"], "func": vsha_269_shock_clustering_vel_126d},
    "vsha_270_shock_clustering_vel_252d": {"inputs": ["close", "volume"], "func": vsha_270_shock_clustering_vel_252d},
    "vsha_271_volume_shock_entropy_vel_5d": {"inputs": ["close", "volume"], "func": vsha_271_volume_shock_entropy_vel_5d},
    "vsha_272_volume_shock_entropy_vel_21d": {"inputs": ["close", "volume"], "func": vsha_272_volume_shock_entropy_vel_21d},
    "vsha_273_volume_shock_entropy_vel_63d": {"inputs": ["close", "volume"], "func": vsha_273_volume_shock_entropy_vel_63d},
    "vsha_274_volume_shock_entropy_vel_126d": {"inputs": ["close", "volume"], "func": vsha_274_volume_shock_entropy_vel_126d},
    "vsha_275_volume_shock_entropy_vel_252d": {"inputs": ["close", "volume"], "func": vsha_275_volume_shock_entropy_vel_252d},
    "vsha_276_shock_exhaustion_proxy_vel_5d": {"inputs": ["close", "volume"], "func": vsha_276_shock_exhaustion_proxy_vel_5d},
    "vsha_277_shock_exhaustion_proxy_vel_21d": {"inputs": ["close", "volume"], "func": vsha_277_shock_exhaustion_proxy_vel_21d},
    "vsha_278_shock_exhaustion_proxy_vel_63d": {"inputs": ["close", "volume"], "func": vsha_278_shock_exhaustion_proxy_vel_63d},
    "vsha_279_shock_exhaustion_proxy_vel_126d": {"inputs": ["close", "volume"], "func": vsha_279_shock_exhaustion_proxy_vel_126d},
    "vsha_280_shock_exhaustion_proxy_vel_252d": {"inputs": ["close", "volume"], "func": vsha_280_shock_exhaustion_proxy_vel_252d},
    "vsha_281_shock_recovery_rate_vel_5d": {"inputs": ["close", "volume"], "func": vsha_281_shock_recovery_rate_vel_5d},
    "vsha_282_shock_recovery_rate_vel_21d": {"inputs": ["close", "volume"], "func": vsha_282_shock_recovery_rate_vel_21d},
    "vsha_283_shock_recovery_rate_vel_63d": {"inputs": ["close", "volume"], "func": vsha_283_shock_recovery_rate_vel_63d},
    "vsha_284_shock_recovery_rate_vel_126d": {"inputs": ["close", "volume"], "func": vsha_284_shock_recovery_rate_vel_126d},
    "vsha_285_shock_recovery_rate_vel_252d": {"inputs": ["close", "volume"], "func": vsha_285_shock_recovery_rate_vel_252d},
    "vsha_286_volume_shock_momentum_vel_5d": {"inputs": ["close", "volume"], "func": vsha_286_volume_shock_momentum_vel_5d},
    "vsha_287_volume_shock_momentum_vel_21d": {"inputs": ["close", "volume"], "func": vsha_287_volume_shock_momentum_vel_21d},
    "vsha_288_volume_shock_momentum_vel_63d": {"inputs": ["close", "volume"], "func": vsha_288_volume_shock_momentum_vel_63d},
    "vsha_289_volume_shock_momentum_vel_126d": {"inputs": ["close", "volume"], "func": vsha_289_volume_shock_momentum_vel_126d},
    "vsha_290_volume_shock_momentum_vel_252d": {"inputs": ["close", "volume"], "func": vsha_290_volume_shock_momentum_vel_252d},
    "vsha_291_shock_regime_shift_vel_5d": {"inputs": ["close", "volume"], "func": vsha_291_shock_regime_shift_vel_5d},
    "vsha_292_shock_regime_shift_vel_21d": {"inputs": ["close", "volume"], "func": vsha_292_shock_regime_shift_vel_21d},
    "vsha_293_shock_regime_shift_vel_63d": {"inputs": ["close", "volume"], "func": vsha_293_shock_regime_shift_vel_63d},
    "vsha_294_shock_regime_shift_vel_126d": {"inputs": ["close", "volume"], "func": vsha_294_shock_regime_shift_vel_126d},
    "vsha_295_shock_regime_shift_vel_252d": {"inputs": ["close", "volume"], "func": vsha_295_shock_regime_shift_vel_252d},
    "vsha_296_volume_shock_tail_corr_vel_5d": {"inputs": ["close", "volume"], "func": vsha_296_volume_shock_tail_corr_vel_5d},
    "vsha_297_volume_shock_tail_corr_vel_21d": {"inputs": ["close", "volume"], "func": vsha_297_volume_shock_tail_corr_vel_21d},
    "vsha_298_volume_shock_tail_corr_vel_63d": {"inputs": ["close", "volume"], "func": vsha_298_volume_shock_tail_corr_vel_63d},
    "vsha_299_volume_shock_tail_corr_vel_126d": {"inputs": ["close", "volume"], "func": vsha_299_volume_shock_tail_corr_vel_126d},
    "vsha_300_volume_shock_tail_corr_vel_252d": {"inputs": ["close", "volume"], "func": vsha_300_volume_shock_tail_corr_vel_252d},
}
