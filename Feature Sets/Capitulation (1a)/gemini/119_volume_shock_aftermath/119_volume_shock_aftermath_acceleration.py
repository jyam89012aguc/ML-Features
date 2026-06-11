"""
119_volume_shock_aftermath — Acceleration (3rd Derivatives)
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

def vsha_301_volume_shock_mag_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_301_volume_shock_mag_accel_5d
    ECONOMIC RATIONALE: Acceleration of volume_shock_mag. Magnitude of the current volume shock.
    """
    return (volume / volume.rolling(63).mean()).diff(5).diff(_TD_MON)

def vsha_302_volume_shock_mag_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_302_volume_shock_mag_accel_21d
    ECONOMIC RATIONALE: Acceleration of volume_shock_mag. Magnitude of the current volume shock.
    """
    return (volume / volume.rolling(63).mean()).diff(21).diff(_TD_MON)

def vsha_303_volume_shock_mag_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_303_volume_shock_mag_accel_63d
    ECONOMIC RATIONALE: Acceleration of volume_shock_mag. Magnitude of the current volume shock.
    """
    return (volume / volume.rolling(63).mean()).diff(63).diff(_TD_MON)

def vsha_304_volume_shock_mag_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_304_volume_shock_mag_accel_126d
    ECONOMIC RATIONALE: Acceleration of volume_shock_mag. Magnitude of the current volume shock.
    """
    return (volume / volume.rolling(63).mean()).diff(126).diff(_TD_MON)

def vsha_305_volume_shock_mag_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_305_volume_shock_mag_accel_252d
    ECONOMIC RATIONALE: Acceleration of volume_shock_mag. Magnitude of the current volume shock.
    """
    return (volume / volume.rolling(63).mean()).diff(252).diff(_TD_MON)

def vsha_306_post_shock_drift_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_306_post_shock_drift_accel_5d
    ECONOMIC RATIONALE: Acceleration of post_shock_drift. Price drift following major volume shocks.
    """
    return (close.pct_change(21) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*2).astype(float)).diff(5).diff(_TD_MON)

def vsha_307_post_shock_drift_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_307_post_shock_drift_accel_21d
    ECONOMIC RATIONALE: Acceleration of post_shock_drift. Price drift following major volume shocks.
    """
    return (close.pct_change(21) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*2).astype(float)).diff(21).diff(_TD_MON)

def vsha_308_post_shock_drift_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_308_post_shock_drift_accel_63d
    ECONOMIC RATIONALE: Acceleration of post_shock_drift. Price drift following major volume shocks.
    """
    return (close.pct_change(21) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*2).astype(float)).diff(63).diff(_TD_MON)

def vsha_309_post_shock_drift_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_309_post_shock_drift_accel_126d
    ECONOMIC RATIONALE: Acceleration of post_shock_drift. Price drift following major volume shocks.
    """
    return (close.pct_change(21) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*2).astype(float)).diff(126).diff(_TD_MON)

def vsha_310_post_shock_drift_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_310_post_shock_drift_accel_252d
    ECONOMIC RATIONALE: Acceleration of post_shock_drift. Price drift following major volume shocks.
    """
    return (close.pct_change(21) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*2).astype(float)).diff(252).diff(_TD_MON)

def vsha_311_shock_volatility_expansion_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_311_shock_volatility_expansion_accel_5d
    ECONOMIC RATIONALE: Acceleration of shock_volatility_expansion. Volatility expansion associated with volume shocks.
    """
    return (close.rolling(21).std() / close.rolling(252).std() * (volume > volume.rolling(63).mean()*2).astype(float)).diff(5).diff(_TD_MON)

def vsha_312_shock_volatility_expansion_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_312_shock_volatility_expansion_accel_21d
    ECONOMIC RATIONALE: Acceleration of shock_volatility_expansion. Volatility expansion associated with volume shocks.
    """
    return (close.rolling(21).std() / close.rolling(252).std() * (volume > volume.rolling(63).mean()*2).astype(float)).diff(21).diff(_TD_MON)

def vsha_313_shock_volatility_expansion_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_313_shock_volatility_expansion_accel_63d
    ECONOMIC RATIONALE: Acceleration of shock_volatility_expansion. Volatility expansion associated with volume shocks.
    """
    return (close.rolling(21).std() / close.rolling(252).std() * (volume > volume.rolling(63).mean()*2).astype(float)).diff(63).diff(_TD_MON)

def vsha_314_shock_volatility_expansion_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_314_shock_volatility_expansion_accel_126d
    ECONOMIC RATIONALE: Acceleration of shock_volatility_expansion. Volatility expansion associated with volume shocks.
    """
    return (close.rolling(21).std() / close.rolling(252).std() * (volume > volume.rolling(63).mean()*2).astype(float)).diff(126).diff(_TD_MON)

def vsha_315_shock_volatility_expansion_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_315_shock_volatility_expansion_accel_252d
    ECONOMIC RATIONALE: Acceleration of shock_volatility_expansion. Volatility expansion associated with volume shocks.
    """
    return (close.rolling(21).std() / close.rolling(252).std() * (volume > volume.rolling(63).mean()*2).astype(float)).diff(252).diff(_TD_MON)

def vsha_316_volume_shock_reversal_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_316_volume_shock_reversal_accel_5d
    ECONOMIC RATIONALE: Acceleration of volume_shock_reversal. Reversal of price direction after a volume shock.
    """
    return ((close.diff(5) * close.diff(5).shift(5) < 0) * (volume > volume.rolling(63).mean()*2).astype(float)).diff(5).diff(_TD_MON)

def vsha_317_volume_shock_reversal_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_317_volume_shock_reversal_accel_21d
    ECONOMIC RATIONALE: Acceleration of volume_shock_reversal. Reversal of price direction after a volume shock.
    """
    return ((close.diff(5) * close.diff(5).shift(5) < 0) * (volume > volume.rolling(63).mean()*2).astype(float)).diff(21).diff(_TD_MON)

def vsha_318_volume_shock_reversal_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_318_volume_shock_reversal_accel_63d
    ECONOMIC RATIONALE: Acceleration of volume_shock_reversal. Reversal of price direction after a volume shock.
    """
    return ((close.diff(5) * close.diff(5).shift(5) < 0) * (volume > volume.rolling(63).mean()*2).astype(float)).diff(63).diff(_TD_MON)

def vsha_319_volume_shock_reversal_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_319_volume_shock_reversal_accel_126d
    ECONOMIC RATIONALE: Acceleration of volume_shock_reversal. Reversal of price direction after a volume shock.
    """
    return ((close.diff(5) * close.diff(5).shift(5) < 0) * (volume > volume.rolling(63).mean()*2).astype(float)).diff(126).diff(_TD_MON)

def vsha_320_volume_shock_reversal_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_320_volume_shock_reversal_accel_252d
    ECONOMIC RATIONALE: Acceleration of volume_shock_reversal. Reversal of price direction after a volume shock.
    """
    return ((close.diff(5) * close.diff(5).shift(5) < 0) * (volume > volume.rolling(63).mean()*2).astype(float)).diff(252).diff(_TD_MON)

def vsha_321_shock_persistence_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_321_shock_persistence_accel_5d
    ECONOMIC RATIONALE: Acceleration of shock_persistence. Duration of a high-volume regime.
    """
    return ((volume > volume.rolling(63).mean()*2).rolling(10).sum()).diff(5).diff(_TD_MON)

def vsha_322_shock_persistence_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_322_shock_persistence_accel_21d
    ECONOMIC RATIONALE: Acceleration of shock_persistence. Duration of a high-volume regime.
    """
    return ((volume > volume.rolling(63).mean()*2).rolling(10).sum()).diff(21).diff(_TD_MON)

def vsha_323_shock_persistence_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_323_shock_persistence_accel_63d
    ECONOMIC RATIONALE: Acceleration of shock_persistence. Duration of a high-volume regime.
    """
    return ((volume > volume.rolling(63).mean()*2).rolling(10).sum()).diff(63).diff(_TD_MON)

def vsha_324_shock_persistence_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_324_shock_persistence_accel_126d
    ECONOMIC RATIONALE: Acceleration of shock_persistence. Duration of a high-volume regime.
    """
    return ((volume > volume.rolling(63).mean()*2).rolling(10).sum()).diff(126).diff(_TD_MON)

def vsha_325_shock_persistence_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_325_shock_persistence_accel_252d
    ECONOMIC RATIONALE: Acceleration of shock_persistence. Duration of a high-volume regime.
    """
    return ((volume > volume.rolling(63).mean()*2).rolling(10).sum()).diff(252).diff(_TD_MON)

def vsha_326_volume_shock_z_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_326_volume_shock_z_accel_5d
    ECONOMIC RATIONALE: Acceleration of volume_shock_z. Z-score of volume relative to annual history.
    """
    return (_zscore_rolling(volume, 252)).diff(5).diff(_TD_MON)

def vsha_327_volume_shock_z_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_327_volume_shock_z_accel_21d
    ECONOMIC RATIONALE: Acceleration of volume_shock_z. Z-score of volume relative to annual history.
    """
    return (_zscore_rolling(volume, 252)).diff(21).diff(_TD_MON)

def vsha_328_volume_shock_z_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_328_volume_shock_z_accel_63d
    ECONOMIC RATIONALE: Acceleration of volume_shock_z. Z-score of volume relative to annual history.
    """
    return (_zscore_rolling(volume, 252)).diff(63).diff(_TD_MON)

def vsha_329_volume_shock_z_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_329_volume_shock_z_accel_126d
    ECONOMIC RATIONALE: Acceleration of volume_shock_z. Z-score of volume relative to annual history.
    """
    return (_zscore_rolling(volume, 252)).diff(126).diff(_TD_MON)

def vsha_330_volume_shock_z_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_330_volume_shock_z_accel_252d
    ECONOMIC RATIONALE: Acceleration of volume_shock_z. Z-score of volume relative to annual history.
    """
    return (_zscore_rolling(volume, 252)).diff(252).diff(_TD_MON)

def vsha_331_shock_price_impact_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_331_shock_price_impact_accel_5d
    ECONOMIC RATIONALE: Acceleration of shock_price_impact. Price change weighted by the volume shock magnitude.
    """
    return (close.diff(1) * (volume / volume.rolling(63).mean())).diff(5).diff(_TD_MON)

def vsha_332_shock_price_impact_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_332_shock_price_impact_accel_21d
    ECONOMIC RATIONALE: Acceleration of shock_price_impact. Price change weighted by the volume shock magnitude.
    """
    return (close.diff(1) * (volume / volume.rolling(63).mean())).diff(21).diff(_TD_MON)

def vsha_333_shock_price_impact_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_333_shock_price_impact_accel_63d
    ECONOMIC RATIONALE: Acceleration of shock_price_impact. Price change weighted by the volume shock magnitude.
    """
    return (close.diff(1) * (volume / volume.rolling(63).mean())).diff(63).diff(_TD_MON)

def vsha_334_shock_price_impact_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_334_shock_price_impact_accel_126d
    ECONOMIC RATIONALE: Acceleration of shock_price_impact. Price change weighted by the volume shock magnitude.
    """
    return (close.diff(1) * (volume / volume.rolling(63).mean())).diff(126).diff(_TD_MON)

def vsha_335_shock_price_impact_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_335_shock_price_impact_accel_252d
    ECONOMIC RATIONALE: Acceleration of shock_price_impact. Price change weighted by the volume shock magnitude.
    """
    return (close.diff(1) * (volume / volume.rolling(63).mean())).diff(252).diff(_TD_MON)

def vsha_336_post_shock_liquidity_drain_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_336_post_shock_liquidity_drain_accel_5d
    ECONOMIC RATIONALE: Acceleration of post_shock_liquidity_drain. Liquidity dry-up following a massive shock.
    """
    return ((volume.rolling(5).mean() / volume.rolling(63).mean()) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*3).astype(float)).diff(5).diff(_TD_MON)

def vsha_337_post_shock_liquidity_drain_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_337_post_shock_liquidity_drain_accel_21d
    ECONOMIC RATIONALE: Acceleration of post_shock_liquidity_drain. Liquidity dry-up following a massive shock.
    """
    return ((volume.rolling(5).mean() / volume.rolling(63).mean()) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*3).astype(float)).diff(21).diff(_TD_MON)

def vsha_338_post_shock_liquidity_drain_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_338_post_shock_liquidity_drain_accel_63d
    ECONOMIC RATIONALE: Acceleration of post_shock_liquidity_drain. Liquidity dry-up following a massive shock.
    """
    return ((volume.rolling(5).mean() / volume.rolling(63).mean()) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*3).astype(float)).diff(63).diff(_TD_MON)

def vsha_339_post_shock_liquidity_drain_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_339_post_shock_liquidity_drain_accel_126d
    ECONOMIC RATIONALE: Acceleration of post_shock_liquidity_drain. Liquidity dry-up following a massive shock.
    """
    return ((volume.rolling(5).mean() / volume.rolling(63).mean()) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*3).astype(float)).diff(126).diff(_TD_MON)

def vsha_340_post_shock_liquidity_drain_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_340_post_shock_liquidity_drain_accel_252d
    ECONOMIC RATIONALE: Acceleration of post_shock_liquidity_drain. Liquidity dry-up following a massive shock.
    """
    return ((volume.rolling(5).mean() / volume.rolling(63).mean()) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*3).astype(float)).diff(252).diff(_TD_MON)

def vsha_341_shock_clustering_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_341_shock_clustering_accel_5d
    ECONOMIC RATIONALE: Acceleration of shock_clustering. Frequency of volume shocks in the last quarter.
    """
    return ((volume > volume.rolling(63).mean()*2).rolling(63).sum()).diff(5).diff(_TD_MON)

def vsha_342_shock_clustering_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_342_shock_clustering_accel_21d
    ECONOMIC RATIONALE: Acceleration of shock_clustering. Frequency of volume shocks in the last quarter.
    """
    return ((volume > volume.rolling(63).mean()*2).rolling(63).sum()).diff(21).diff(_TD_MON)

def vsha_343_shock_clustering_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_343_shock_clustering_accel_63d
    ECONOMIC RATIONALE: Acceleration of shock_clustering. Frequency of volume shocks in the last quarter.
    """
    return ((volume > volume.rolling(63).mean()*2).rolling(63).sum()).diff(63).diff(_TD_MON)

def vsha_344_shock_clustering_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_344_shock_clustering_accel_126d
    ECONOMIC RATIONALE: Acceleration of shock_clustering. Frequency of volume shocks in the last quarter.
    """
    return ((volume > volume.rolling(63).mean()*2).rolling(63).sum()).diff(126).diff(_TD_MON)

def vsha_345_shock_clustering_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_345_shock_clustering_accel_252d
    ECONOMIC RATIONALE: Acceleration of shock_clustering. Frequency of volume shocks in the last quarter.
    """
    return ((volume > volume.rolling(63).mean()*2).rolling(63).sum()).diff(252).diff(_TD_MON)

def vsha_346_volume_shock_entropy_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_346_volume_shock_entropy_accel_5d
    ECONOMIC RATIONALE: Acceleration of volume_shock_entropy. Unpredictability of volume during shocks.
    """
    return (volume.rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))).diff(5).diff(_TD_MON)

def vsha_347_volume_shock_entropy_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_347_volume_shock_entropy_accel_21d
    ECONOMIC RATIONALE: Acceleration of volume_shock_entropy. Unpredictability of volume during shocks.
    """
    return (volume.rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))).diff(21).diff(_TD_MON)

def vsha_348_volume_shock_entropy_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_348_volume_shock_entropy_accel_63d
    ECONOMIC RATIONALE: Acceleration of volume_shock_entropy. Unpredictability of volume during shocks.
    """
    return (volume.rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))).diff(63).diff(_TD_MON)

def vsha_349_volume_shock_entropy_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_349_volume_shock_entropy_accel_126d
    ECONOMIC RATIONALE: Acceleration of volume_shock_entropy. Unpredictability of volume during shocks.
    """
    return (volume.rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))).diff(126).diff(_TD_MON)

def vsha_350_volume_shock_entropy_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_350_volume_shock_entropy_accel_252d
    ECONOMIC RATIONALE: Acceleration of volume_shock_entropy. Unpredictability of volume during shocks.
    """
    return (volume.rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))).diff(252).diff(_TD_MON)

def vsha_351_shock_exhaustion_proxy_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_351_shock_exhaustion_proxy_accel_5d
    ECONOMIC RATIONALE: Acceleration of shock_exhaustion_proxy. Large volume shock with minimal price impact.
    """
    return ((volume > volume.rolling(63).mean()*3) & (close.diff(1).abs() < close.rolling(21).std()*0.5)).diff(5).diff(_TD_MON)

def vsha_352_shock_exhaustion_proxy_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_352_shock_exhaustion_proxy_accel_21d
    ECONOMIC RATIONALE: Acceleration of shock_exhaustion_proxy. Large volume shock with minimal price impact.
    """
    return ((volume > volume.rolling(63).mean()*3) & (close.diff(1).abs() < close.rolling(21).std()*0.5)).diff(21).diff(_TD_MON)

def vsha_353_shock_exhaustion_proxy_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_353_shock_exhaustion_proxy_accel_63d
    ECONOMIC RATIONALE: Acceleration of shock_exhaustion_proxy. Large volume shock with minimal price impact.
    """
    return ((volume > volume.rolling(63).mean()*3) & (close.diff(1).abs() < close.rolling(21).std()*0.5)).diff(63).diff(_TD_MON)

def vsha_354_shock_exhaustion_proxy_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_354_shock_exhaustion_proxy_accel_126d
    ECONOMIC RATIONALE: Acceleration of shock_exhaustion_proxy. Large volume shock with minimal price impact.
    """
    return ((volume > volume.rolling(63).mean()*3) & (close.diff(1).abs() < close.rolling(21).std()*0.5)).diff(126).diff(_TD_MON)

def vsha_355_shock_exhaustion_proxy_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_355_shock_exhaustion_proxy_accel_252d
    ECONOMIC RATIONALE: Acceleration of shock_exhaustion_proxy. Large volume shock with minimal price impact.
    """
    return ((volume > volume.rolling(63).mean()*3) & (close.diff(1).abs() < close.rolling(21).std()*0.5)).diff(252).diff(_TD_MON)

def vsha_356_shock_recovery_rate_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_356_shock_recovery_rate_accel_5d
    ECONOMIC RATIONALE: Acceleration of shock_recovery_rate. Recovery relative to the price at the last volume peak.
    """
    return (close / close.shift(volume.rolling(63).apply(lambda x: np.argmax(x)))).diff(5).diff(_TD_MON)

def vsha_357_shock_recovery_rate_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_357_shock_recovery_rate_accel_21d
    ECONOMIC RATIONALE: Acceleration of shock_recovery_rate. Recovery relative to the price at the last volume peak.
    """
    return (close / close.shift(volume.rolling(63).apply(lambda x: np.argmax(x)))).diff(21).diff(_TD_MON)

def vsha_358_shock_recovery_rate_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_358_shock_recovery_rate_accel_63d
    ECONOMIC RATIONALE: Acceleration of shock_recovery_rate. Recovery relative to the price at the last volume peak.
    """
    return (close / close.shift(volume.rolling(63).apply(lambda x: np.argmax(x)))).diff(63).diff(_TD_MON)

def vsha_359_shock_recovery_rate_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_359_shock_recovery_rate_accel_126d
    ECONOMIC RATIONALE: Acceleration of shock_recovery_rate. Recovery relative to the price at the last volume peak.
    """
    return (close / close.shift(volume.rolling(63).apply(lambda x: np.argmax(x)))).diff(126).diff(_TD_MON)

def vsha_360_shock_recovery_rate_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_360_shock_recovery_rate_accel_252d
    ECONOMIC RATIONALE: Acceleration of shock_recovery_rate. Recovery relative to the price at the last volume peak.
    """
    return (close / close.shift(volume.rolling(63).apply(lambda x: np.argmax(x)))).diff(252).diff(_TD_MON)

def vsha_361_volume_shock_momentum_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_361_volume_shock_momentum_accel_5d
    ECONOMIC RATIONALE: Acceleration of volume_shock_momentum. Synchronized volume and price momentum.
    """
    return (volume.pct_change(5) * close.pct_change(5)).diff(5).diff(_TD_MON)

def vsha_362_volume_shock_momentum_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_362_volume_shock_momentum_accel_21d
    ECONOMIC RATIONALE: Acceleration of volume_shock_momentum. Synchronized volume and price momentum.
    """
    return (volume.pct_change(5) * close.pct_change(5)).diff(21).diff(_TD_MON)

def vsha_363_volume_shock_momentum_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_363_volume_shock_momentum_accel_63d
    ECONOMIC RATIONALE: Acceleration of volume_shock_momentum. Synchronized volume and price momentum.
    """
    return (volume.pct_change(5) * close.pct_change(5)).diff(63).diff(_TD_MON)

def vsha_364_volume_shock_momentum_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_364_volume_shock_momentum_accel_126d
    ECONOMIC RATIONALE: Acceleration of volume_shock_momentum. Synchronized volume and price momentum.
    """
    return (volume.pct_change(5) * close.pct_change(5)).diff(126).diff(_TD_MON)

def vsha_365_volume_shock_momentum_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_365_volume_shock_momentum_accel_252d
    ECONOMIC RATIONALE: Acceleration of volume_shock_momentum. Synchronized volume and price momentum.
    """
    return (volume.pct_change(5) * close.pct_change(5)).diff(252).diff(_TD_MON)

def vsha_366_shock_regime_shift_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_366_shock_regime_shift_accel_5d
    ECONOMIC RATIONALE: Acceleration of shock_regime_shift. Structural shift in average volume levels.
    """
    return (volume.rolling(21).mean().diff(21) / volume.rolling(252).std()).diff(5).diff(_TD_MON)

def vsha_367_shock_regime_shift_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_367_shock_regime_shift_accel_21d
    ECONOMIC RATIONALE: Acceleration of shock_regime_shift. Structural shift in average volume levels.
    """
    return (volume.rolling(21).mean().diff(21) / volume.rolling(252).std()).diff(21).diff(_TD_MON)

def vsha_368_shock_regime_shift_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_368_shock_regime_shift_accel_63d
    ECONOMIC RATIONALE: Acceleration of shock_regime_shift. Structural shift in average volume levels.
    """
    return (volume.rolling(21).mean().diff(21) / volume.rolling(252).std()).diff(63).diff(_TD_MON)

def vsha_369_shock_regime_shift_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_369_shock_regime_shift_accel_126d
    ECONOMIC RATIONALE: Acceleration of shock_regime_shift. Structural shift in average volume levels.
    """
    return (volume.rolling(21).mean().diff(21) / volume.rolling(252).std()).diff(126).diff(_TD_MON)

def vsha_370_shock_regime_shift_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_370_shock_regime_shift_accel_252d
    ECONOMIC RATIONALE: Acceleration of shock_regime_shift. Structural shift in average volume levels.
    """
    return (volume.rolling(21).mean().diff(21) / volume.rolling(252).std()).diff(252).diff(_TD_MON)

def vsha_371_volume_shock_tail_corr_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_371_volume_shock_tail_corr_accel_5d
    ECONOMIC RATIONALE: Acceleration of volume_shock_tail_corr. Correlation between volume shocks and price magnitude.
    """
    return (volume.rolling(21).corr(close.pct_change(1).abs())).diff(5).diff(_TD_MON)

def vsha_372_volume_shock_tail_corr_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_372_volume_shock_tail_corr_accel_21d
    ECONOMIC RATIONALE: Acceleration of volume_shock_tail_corr. Correlation between volume shocks and price magnitude.
    """
    return (volume.rolling(21).corr(close.pct_change(1).abs())).diff(21).diff(_TD_MON)

def vsha_373_volume_shock_tail_corr_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_373_volume_shock_tail_corr_accel_63d
    ECONOMIC RATIONALE: Acceleration of volume_shock_tail_corr. Correlation between volume shocks and price magnitude.
    """
    return (volume.rolling(21).corr(close.pct_change(1).abs())).diff(63).diff(_TD_MON)

def vsha_374_volume_shock_tail_corr_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_374_volume_shock_tail_corr_accel_126d
    ECONOMIC RATIONALE: Acceleration of volume_shock_tail_corr. Correlation between volume shocks and price magnitude.
    """
    return (volume.rolling(21).corr(close.pct_change(1).abs())).diff(126).diff(_TD_MON)

def vsha_375_volume_shock_tail_corr_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_375_volume_shock_tail_corr_accel_252d
    ECONOMIC RATIONALE: Acceleration of volume_shock_tail_corr. Correlation between volume shocks and price magnitude.
    """
    return (volume.rolling(21).corr(close.pct_change(1).abs())).diff(252).diff(_TD_MON)

# ── Registry ──────────────────────────────────────────────────────────────────
V119_REGISTRY_ACCEL = {
    "vsha_301_volume_shock_mag_accel_5d": {"inputs": ["close", "volume"], "func": vsha_301_volume_shock_mag_accel_5d},
    "vsha_302_volume_shock_mag_accel_21d": {"inputs": ["close", "volume"], "func": vsha_302_volume_shock_mag_accel_21d},
    "vsha_303_volume_shock_mag_accel_63d": {"inputs": ["close", "volume"], "func": vsha_303_volume_shock_mag_accel_63d},
    "vsha_304_volume_shock_mag_accel_126d": {"inputs": ["close", "volume"], "func": vsha_304_volume_shock_mag_accel_126d},
    "vsha_305_volume_shock_mag_accel_252d": {"inputs": ["close", "volume"], "func": vsha_305_volume_shock_mag_accel_252d},
    "vsha_306_post_shock_drift_accel_5d": {"inputs": ["close", "volume"], "func": vsha_306_post_shock_drift_accel_5d},
    "vsha_307_post_shock_drift_accel_21d": {"inputs": ["close", "volume"], "func": vsha_307_post_shock_drift_accel_21d},
    "vsha_308_post_shock_drift_accel_63d": {"inputs": ["close", "volume"], "func": vsha_308_post_shock_drift_accel_63d},
    "vsha_309_post_shock_drift_accel_126d": {"inputs": ["close", "volume"], "func": vsha_309_post_shock_drift_accel_126d},
    "vsha_310_post_shock_drift_accel_252d": {"inputs": ["close", "volume"], "func": vsha_310_post_shock_drift_accel_252d},
    "vsha_311_shock_volatility_expansion_accel_5d": {"inputs": ["close", "volume"], "func": vsha_311_shock_volatility_expansion_accel_5d},
    "vsha_312_shock_volatility_expansion_accel_21d": {"inputs": ["close", "volume"], "func": vsha_312_shock_volatility_expansion_accel_21d},
    "vsha_313_shock_volatility_expansion_accel_63d": {"inputs": ["close", "volume"], "func": vsha_313_shock_volatility_expansion_accel_63d},
    "vsha_314_shock_volatility_expansion_accel_126d": {"inputs": ["close", "volume"], "func": vsha_314_shock_volatility_expansion_accel_126d},
    "vsha_315_shock_volatility_expansion_accel_252d": {"inputs": ["close", "volume"], "func": vsha_315_shock_volatility_expansion_accel_252d},
    "vsha_316_volume_shock_reversal_accel_5d": {"inputs": ["close", "volume"], "func": vsha_316_volume_shock_reversal_accel_5d},
    "vsha_317_volume_shock_reversal_accel_21d": {"inputs": ["close", "volume"], "func": vsha_317_volume_shock_reversal_accel_21d},
    "vsha_318_volume_shock_reversal_accel_63d": {"inputs": ["close", "volume"], "func": vsha_318_volume_shock_reversal_accel_63d},
    "vsha_319_volume_shock_reversal_accel_126d": {"inputs": ["close", "volume"], "func": vsha_319_volume_shock_reversal_accel_126d},
    "vsha_320_volume_shock_reversal_accel_252d": {"inputs": ["close", "volume"], "func": vsha_320_volume_shock_reversal_accel_252d},
    "vsha_321_shock_persistence_accel_5d": {"inputs": ["close", "volume"], "func": vsha_321_shock_persistence_accel_5d},
    "vsha_322_shock_persistence_accel_21d": {"inputs": ["close", "volume"], "func": vsha_322_shock_persistence_accel_21d},
    "vsha_323_shock_persistence_accel_63d": {"inputs": ["close", "volume"], "func": vsha_323_shock_persistence_accel_63d},
    "vsha_324_shock_persistence_accel_126d": {"inputs": ["close", "volume"], "func": vsha_324_shock_persistence_accel_126d},
    "vsha_325_shock_persistence_accel_252d": {"inputs": ["close", "volume"], "func": vsha_325_shock_persistence_accel_252d},
    "vsha_326_volume_shock_z_accel_5d": {"inputs": ["close", "volume"], "func": vsha_326_volume_shock_z_accel_5d},
    "vsha_327_volume_shock_z_accel_21d": {"inputs": ["close", "volume"], "func": vsha_327_volume_shock_z_accel_21d},
    "vsha_328_volume_shock_z_accel_63d": {"inputs": ["close", "volume"], "func": vsha_328_volume_shock_z_accel_63d},
    "vsha_329_volume_shock_z_accel_126d": {"inputs": ["close", "volume"], "func": vsha_329_volume_shock_z_accel_126d},
    "vsha_330_volume_shock_z_accel_252d": {"inputs": ["close", "volume"], "func": vsha_330_volume_shock_z_accel_252d},
    "vsha_331_shock_price_impact_accel_5d": {"inputs": ["close", "volume"], "func": vsha_331_shock_price_impact_accel_5d},
    "vsha_332_shock_price_impact_accel_21d": {"inputs": ["close", "volume"], "func": vsha_332_shock_price_impact_accel_21d},
    "vsha_333_shock_price_impact_accel_63d": {"inputs": ["close", "volume"], "func": vsha_333_shock_price_impact_accel_63d},
    "vsha_334_shock_price_impact_accel_126d": {"inputs": ["close", "volume"], "func": vsha_334_shock_price_impact_accel_126d},
    "vsha_335_shock_price_impact_accel_252d": {"inputs": ["close", "volume"], "func": vsha_335_shock_price_impact_accel_252d},
    "vsha_336_post_shock_liquidity_drain_accel_5d": {"inputs": ["close", "volume"], "func": vsha_336_post_shock_liquidity_drain_accel_5d},
    "vsha_337_post_shock_liquidity_drain_accel_21d": {"inputs": ["close", "volume"], "func": vsha_337_post_shock_liquidity_drain_accel_21d},
    "vsha_338_post_shock_liquidity_drain_accel_63d": {"inputs": ["close", "volume"], "func": vsha_338_post_shock_liquidity_drain_accel_63d},
    "vsha_339_post_shock_liquidity_drain_accel_126d": {"inputs": ["close", "volume"], "func": vsha_339_post_shock_liquidity_drain_accel_126d},
    "vsha_340_post_shock_liquidity_drain_accel_252d": {"inputs": ["close", "volume"], "func": vsha_340_post_shock_liquidity_drain_accel_252d},
    "vsha_341_shock_clustering_accel_5d": {"inputs": ["close", "volume"], "func": vsha_341_shock_clustering_accel_5d},
    "vsha_342_shock_clustering_accel_21d": {"inputs": ["close", "volume"], "func": vsha_342_shock_clustering_accel_21d},
    "vsha_343_shock_clustering_accel_63d": {"inputs": ["close", "volume"], "func": vsha_343_shock_clustering_accel_63d},
    "vsha_344_shock_clustering_accel_126d": {"inputs": ["close", "volume"], "func": vsha_344_shock_clustering_accel_126d},
    "vsha_345_shock_clustering_accel_252d": {"inputs": ["close", "volume"], "func": vsha_345_shock_clustering_accel_252d},
    "vsha_346_volume_shock_entropy_accel_5d": {"inputs": ["close", "volume"], "func": vsha_346_volume_shock_entropy_accel_5d},
    "vsha_347_volume_shock_entropy_accel_21d": {"inputs": ["close", "volume"], "func": vsha_347_volume_shock_entropy_accel_21d},
    "vsha_348_volume_shock_entropy_accel_63d": {"inputs": ["close", "volume"], "func": vsha_348_volume_shock_entropy_accel_63d},
    "vsha_349_volume_shock_entropy_accel_126d": {"inputs": ["close", "volume"], "func": vsha_349_volume_shock_entropy_accel_126d},
    "vsha_350_volume_shock_entropy_accel_252d": {"inputs": ["close", "volume"], "func": vsha_350_volume_shock_entropy_accel_252d},
    "vsha_351_shock_exhaustion_proxy_accel_5d": {"inputs": ["close", "volume"], "func": vsha_351_shock_exhaustion_proxy_accel_5d},
    "vsha_352_shock_exhaustion_proxy_accel_21d": {"inputs": ["close", "volume"], "func": vsha_352_shock_exhaustion_proxy_accel_21d},
    "vsha_353_shock_exhaustion_proxy_accel_63d": {"inputs": ["close", "volume"], "func": vsha_353_shock_exhaustion_proxy_accel_63d},
    "vsha_354_shock_exhaustion_proxy_accel_126d": {"inputs": ["close", "volume"], "func": vsha_354_shock_exhaustion_proxy_accel_126d},
    "vsha_355_shock_exhaustion_proxy_accel_252d": {"inputs": ["close", "volume"], "func": vsha_355_shock_exhaustion_proxy_accel_252d},
    "vsha_356_shock_recovery_rate_accel_5d": {"inputs": ["close", "volume"], "func": vsha_356_shock_recovery_rate_accel_5d},
    "vsha_357_shock_recovery_rate_accel_21d": {"inputs": ["close", "volume"], "func": vsha_357_shock_recovery_rate_accel_21d},
    "vsha_358_shock_recovery_rate_accel_63d": {"inputs": ["close", "volume"], "func": vsha_358_shock_recovery_rate_accel_63d},
    "vsha_359_shock_recovery_rate_accel_126d": {"inputs": ["close", "volume"], "func": vsha_359_shock_recovery_rate_accel_126d},
    "vsha_360_shock_recovery_rate_accel_252d": {"inputs": ["close", "volume"], "func": vsha_360_shock_recovery_rate_accel_252d},
    "vsha_361_volume_shock_momentum_accel_5d": {"inputs": ["close", "volume"], "func": vsha_361_volume_shock_momentum_accel_5d},
    "vsha_362_volume_shock_momentum_accel_21d": {"inputs": ["close", "volume"], "func": vsha_362_volume_shock_momentum_accel_21d},
    "vsha_363_volume_shock_momentum_accel_63d": {"inputs": ["close", "volume"], "func": vsha_363_volume_shock_momentum_accel_63d},
    "vsha_364_volume_shock_momentum_accel_126d": {"inputs": ["close", "volume"], "func": vsha_364_volume_shock_momentum_accel_126d},
    "vsha_365_volume_shock_momentum_accel_252d": {"inputs": ["close", "volume"], "func": vsha_365_volume_shock_momentum_accel_252d},
    "vsha_366_shock_regime_shift_accel_5d": {"inputs": ["close", "volume"], "func": vsha_366_shock_regime_shift_accel_5d},
    "vsha_367_shock_regime_shift_accel_21d": {"inputs": ["close", "volume"], "func": vsha_367_shock_regime_shift_accel_21d},
    "vsha_368_shock_regime_shift_accel_63d": {"inputs": ["close", "volume"], "func": vsha_368_shock_regime_shift_accel_63d},
    "vsha_369_shock_regime_shift_accel_126d": {"inputs": ["close", "volume"], "func": vsha_369_shock_regime_shift_accel_126d},
    "vsha_370_shock_regime_shift_accel_252d": {"inputs": ["close", "volume"], "func": vsha_370_shock_regime_shift_accel_252d},
    "vsha_371_volume_shock_tail_corr_accel_5d": {"inputs": ["close", "volume"], "func": vsha_371_volume_shock_tail_corr_accel_5d},
    "vsha_372_volume_shock_tail_corr_accel_21d": {"inputs": ["close", "volume"], "func": vsha_372_volume_shock_tail_corr_accel_21d},
    "vsha_373_volume_shock_tail_corr_accel_63d": {"inputs": ["close", "volume"], "func": vsha_373_volume_shock_tail_corr_accel_63d},
    "vsha_374_volume_shock_tail_corr_accel_126d": {"inputs": ["close", "volume"], "func": vsha_374_volume_shock_tail_corr_accel_126d},
    "vsha_375_volume_shock_tail_corr_accel_252d": {"inputs": ["close", "volume"], "func": vsha_375_volume_shock_tail_corr_accel_252d},
}
