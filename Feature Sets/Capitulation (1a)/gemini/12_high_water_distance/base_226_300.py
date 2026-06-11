"""
12_12_high_water_distance — Base Features 226-300
Domain: 12_high_water_distance
Asset class: Equities
Target context: Capitulation
"""
import numpy as np
import pandas as pd

# ── Utility helpers ──────────────────────────────────────────────────────────
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

def _rolling_skew(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).skew().fillna(0)

def _rolling_kurt(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).kurt().fillna(0)

# ── Feature functions ────────────────────────────────────────────────────────

def hwd_226_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 12 high water distance distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_skew(base, 5)

def hwd_227_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 12 high water distance distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_skew(base, 21)

def hwd_228_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 12 high water distance distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_skew(base, 63)

def hwd_229_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 12 high water distance distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_skew(base, 126)

def hwd_230_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 12 high water distance distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_skew(base, 252)

def hwd_231_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 12 high water distance over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_kurt(base, 5)

def hwd_232_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 12 high water distance over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_kurt(base, 21)

def hwd_233_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 12 high water distance over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_kurt(base, 63)

def hwd_234_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 12 high water distance over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_kurt(base, 126)

def hwd_235_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 12 high water distance over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_kurt(base, 252)

def hwd_236_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 12 high water distance for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _safe_div(base, _rolling_std(base, 5))

def hwd_237_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 12 high water distance for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _safe_div(base, _rolling_std(base, 21))

def hwd_238_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 12 high water distance for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _safe_div(base, _rolling_std(base, 63))

def hwd_239_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 12 high water distance for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _safe_div(base, _rolling_std(base, 126))

def hwd_240_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 12 high water distance for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _safe_div(base, _rolling_std(base, 252))

def hwd_241_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 12 high water distance over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def hwd_242_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 12 high water distance over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def hwd_243_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 12 high water distance over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def hwd_244_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 12 high water distance over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def hwd_245_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 12 high water distance over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def hwd_246_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 12 high water distance over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_mean(base, 5)

def hwd_247_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 12 high water distance over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_mean(base, 21)

def hwd_248_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 12 high water distance over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_mean(base, 63)

def hwd_249_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 12 high water distance over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_mean(base, 126)

def hwd_250_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 12 high water distance over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_mean(base, 252)

def hwd_251_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 12 high water distance by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _zscore_rolling(base, 5)

def hwd_252_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 12 high water distance by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _zscore_rolling(base, 21)

def hwd_253_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 12 high water distance by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _zscore_rolling(base, 63)

def hwd_254_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 12 high water distance by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _zscore_rolling(base, 126)

def hwd_255_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 12 high water distance by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _zscore_rolling(base, 252)

def hwd_256_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 12 high water distance to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rank_pct(base, 5)

def hwd_257_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 12 high water distance to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rank_pct(base, 21)

def hwd_258_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 12 high water distance to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rank_pct(base, 63)

def hwd_259_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 12 high water distance to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rank_pct(base, 126)

def hwd_260_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 12 high water distance to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rank_pct(base, 252)

def hwd_261_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 12 high water distance distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_skew(base, 5)

def hwd_262_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 12 high water distance distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_skew(base, 21)

def hwd_263_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 12 high water distance distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_skew(base, 63)

def hwd_264_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 12 high water distance distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_skew(base, 126)

def hwd_265_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 12 high water distance distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_skew(base, 252)

def hwd_266_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 12 high water distance over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_kurt(base, 5)

def hwd_267_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 12 high water distance over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_kurt(base, 21)

def hwd_268_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 12 high water distance over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_kurt(base, 63)

def hwd_269_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 12 high water distance over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_kurt(base, 126)

def hwd_270_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 12 high water distance over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_kurt(base, 252)

def hwd_271_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 12 high water distance for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _safe_div(base, _rolling_std(base, 5))

def hwd_272_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 12 high water distance for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _safe_div(base, _rolling_std(base, 21))

def hwd_273_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 12 high water distance for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _safe_div(base, _rolling_std(base, 63))

def hwd_274_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 12 high water distance for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _safe_div(base, _rolling_std(base, 126))

def hwd_275_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 12 high water distance for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _safe_div(base, _rolling_std(base, 252))

def hwd_276_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 12 high water distance over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def hwd_277_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 12 high water distance over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def hwd_278_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 12 high water distance over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def hwd_279_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 12 high water distance over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def hwd_280_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 12 high water distance over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def hwd_281_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 12 high water distance over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_mean(base, 5)

def hwd_282_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 12 high water distance over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_mean(base, 21)

def hwd_283_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 12 high water distance over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_mean(base, 63)

def hwd_284_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 12 high water distance over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_mean(base, 126)

def hwd_285_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 12 high water distance over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_mean(base, 252)

def hwd_286_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 12 high water distance by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _zscore_rolling(base, 5)

def hwd_287_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 12 high water distance by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _zscore_rolling(base, 21)

def hwd_288_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 12 high water distance by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _zscore_rolling(base, 63)

def hwd_289_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 12 high water distance by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _zscore_rolling(base, 126)

def hwd_290_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 12 high water distance by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _zscore_rolling(base, 252)

def hwd_291_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 12 high water distance to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rank_pct(base, 5)

def hwd_292_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 12 high water distance to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rank_pct(base, 21)

def hwd_293_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 12 high water distance to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rank_pct(base, 63)

def hwd_294_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 12 high water distance to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rank_pct(base, 126)

def hwd_295_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 12 high water distance to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rank_pct(base, 252)

def hwd_296_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 12 high water distance distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_skew(base, 5)

def hwd_297_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 12 high water distance distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_skew(base, 21)

def hwd_298_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 12 high water distance distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_skew(base, 63)

def hwd_299_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 12 high water distance distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_skew(base, 126)

def hwd_300_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 12 high water distance distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_skew(base, 252)
