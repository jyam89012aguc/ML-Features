"""
119_119_volume_shock_aftermath — Base Features 226-300
Domain: 119_volume_shock_aftermath
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

def vsha_226_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 5d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 70)
    return _rolling_skew(base, 5)

def vsha_227_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 21d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 70)
    return _rolling_skew(base, 21)

def vsha_228_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 63d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 70)
    return _rolling_skew(base, 63)

def vsha_229_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 126d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 70)
    return _rolling_skew(base, 126)

def vsha_230_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 252d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 70)
    return _rolling_skew(base, 252)

def vsha_231_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 5d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 70)
    return _rolling_kurt(base, 5)

def vsha_232_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 21d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 70)
    return _rolling_kurt(base, 21)

def vsha_233_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 63d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 70)
    return _rolling_kurt(base, 63)

def vsha_234_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 126d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 70)
    return _rolling_kurt(base, 126)

def vsha_235_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 252d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 70)
    return _rolling_kurt(base, 252)

def vsha_236_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 70)
    return _safe_div(base, _rolling_std(base, 5))

def vsha_237_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 70)
    return _safe_div(base, _rolling_std(base, 21))

def vsha_238_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 70)
    return _safe_div(base, _rolling_std(base, 63))

def vsha_239_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 70)
    return _safe_div(base, _rolling_std(base, 126))

def vsha_240_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 70)
    return _safe_div(base, _rolling_std(base, 252))

def vsha_241_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 5d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 70)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vsha_242_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 21d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 70)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vsha_243_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 63d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 70)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vsha_244_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 126d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 70)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vsha_245_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 252d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 70)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vsha_246_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 5d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 80)
    return _rolling_mean(base, 5)

def vsha_247_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 21d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 80)
    return _rolling_mean(base, 21)

def vsha_248_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 63d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 80)
    return _rolling_mean(base, 63)

def vsha_249_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 126d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 80)
    return _rolling_mean(base, 126)

def vsha_250_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 252d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 80)
    return _rolling_mean(base, 252)

def vsha_251_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 5d mean.
    """
    base = volume / _rolling_mean(volume, 80)
    return _zscore_rolling(base, 5)

def vsha_252_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 21d mean.
    """
    base = volume / _rolling_mean(volume, 80)
    return _zscore_rolling(base, 21)

def vsha_253_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 63d mean.
    """
    base = volume / _rolling_mean(volume, 80)
    return _zscore_rolling(base, 63)

def vsha_254_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 126d mean.
    """
    base = volume / _rolling_mean(volume, 80)
    return _zscore_rolling(base, 126)

def vsha_255_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 252d mean.
    """
    base = volume / _rolling_mean(volume, 80)
    return _zscore_rolling(base, 252)

def vsha_256_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 80)
    return _rank_pct(base, 5)

def vsha_257_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 80)
    return _rank_pct(base, 21)

def vsha_258_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 80)
    return _rank_pct(base, 63)

def vsha_259_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 80)
    return _rank_pct(base, 126)

def vsha_260_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 80)
    return _rank_pct(base, 252)

def vsha_261_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 5d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 80)
    return _rolling_skew(base, 5)

def vsha_262_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 21d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 80)
    return _rolling_skew(base, 21)

def vsha_263_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 63d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 80)
    return _rolling_skew(base, 63)

def vsha_264_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 126d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 80)
    return _rolling_skew(base, 126)

def vsha_265_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 252d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 80)
    return _rolling_skew(base, 252)

def vsha_266_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 5d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 80)
    return _rolling_kurt(base, 5)

def vsha_267_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 21d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 80)
    return _rolling_kurt(base, 21)

def vsha_268_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 63d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 80)
    return _rolling_kurt(base, 63)

def vsha_269_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 126d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 80)
    return _rolling_kurt(base, 126)

def vsha_270_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 252d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 80)
    return _rolling_kurt(base, 252)

def vsha_271_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 80)
    return _safe_div(base, _rolling_std(base, 5))

def vsha_272_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 80)
    return _safe_div(base, _rolling_std(base, 21))

def vsha_273_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 80)
    return _safe_div(base, _rolling_std(base, 63))

def vsha_274_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 80)
    return _safe_div(base, _rolling_std(base, 126))

def vsha_275_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 80)
    return _safe_div(base, _rolling_std(base, 252))

def vsha_276_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 5d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 80)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vsha_277_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 21d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 80)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vsha_278_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 63d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 80)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vsha_279_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 126d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 80)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vsha_280_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 252d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 80)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vsha_281_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 5d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 90)
    return _rolling_mean(base, 5)

def vsha_282_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 21d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 90)
    return _rolling_mean(base, 21)

def vsha_283_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 63d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 90)
    return _rolling_mean(base, 63)

def vsha_284_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 126d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 90)
    return _rolling_mean(base, 126)

def vsha_285_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 252d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 90)
    return _rolling_mean(base, 252)

def vsha_286_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 5d mean.
    """
    base = volume / _rolling_mean(volume, 90)
    return _zscore_rolling(base, 5)

def vsha_287_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 21d mean.
    """
    base = volume / _rolling_mean(volume, 90)
    return _zscore_rolling(base, 21)

def vsha_288_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 63d mean.
    """
    base = volume / _rolling_mean(volume, 90)
    return _zscore_rolling(base, 63)

def vsha_289_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 126d mean.
    """
    base = volume / _rolling_mean(volume, 90)
    return _zscore_rolling(base, 126)

def vsha_290_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 252d mean.
    """
    base = volume / _rolling_mean(volume, 90)
    return _zscore_rolling(base, 252)

def vsha_291_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 90)
    return _rank_pct(base, 5)

def vsha_292_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 90)
    return _rank_pct(base, 21)

def vsha_293_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 90)
    return _rank_pct(base, 63)

def vsha_294_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 90)
    return _rank_pct(base, 126)

def vsha_295_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 90)
    return _rank_pct(base, 252)

def vsha_296_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 5d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 90)
    return _rolling_skew(base, 5)

def vsha_297_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 21d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 90)
    return _rolling_skew(base, 21)

def vsha_298_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 63d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 90)
    return _rolling_skew(base, 63)

def vsha_299_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 126d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 90)
    return _rolling_skew(base, 126)

def vsha_300_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 252d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 90)
    return _rolling_skew(base, 252)
