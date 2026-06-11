"""
115_115_volatility_term_structure — Base Features 226-300
Domain: 115_volatility_term_structure
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

def vts_226_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(35).std()
    return _rolling_skew(base, 5)

def vts_227_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(35).std()
    return _rolling_skew(base, 21)

def vts_228_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(35).std()
    return _rolling_skew(base, 63)

def vts_229_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(35).std()
    return _rolling_skew(base, 126)

def vts_230_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(35).std()
    return _rolling_skew(base, 252)

def vts_231_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(35).std()
    return _rolling_kurt(base, 5)

def vts_232_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(35).std()
    return _rolling_kurt(base, 21)

def vts_233_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(35).std()
    return _rolling_kurt(base, 63)

def vts_234_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(35).std()
    return _rolling_kurt(base, 126)

def vts_235_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(35).std()
    return _rolling_kurt(base, 252)

def vts_236_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(35).std()
    return _safe_div(base, _rolling_std(base, 5))

def vts_237_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(35).std()
    return _safe_div(base, _rolling_std(base, 21))

def vts_238_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(35).std()
    return _safe_div(base, _rolling_std(base, 63))

def vts_239_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(35).std()
    return _safe_div(base, _rolling_std(base, 126))

def vts_240_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(35).std()
    return _safe_div(base, _rolling_std(base, 252))

def vts_241_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(35).std()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vts_242_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(35).std()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vts_243_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(35).std()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vts_244_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(35).std()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vts_245_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(35).std()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vts_246_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(40).std()
    return _rolling_mean(base, 5)

def vts_247_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(40).std()
    return _rolling_mean(base, 21)

def vts_248_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(40).std()
    return _rolling_mean(base, 63)

def vts_249_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(40).std()
    return _rolling_mean(base, 126)

def vts_250_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(40).std()
    return _rolling_mean(base, 252)

def vts_251_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(40).std()
    return _zscore_rolling(base, 5)

def vts_252_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(40).std()
    return _zscore_rolling(base, 21)

def vts_253_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(40).std()
    return _zscore_rolling(base, 63)

def vts_254_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(40).std()
    return _zscore_rolling(base, 126)

def vts_255_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(40).std()
    return _zscore_rolling(base, 252)

def vts_256_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(40).std()
    return _rank_pct(base, 5)

def vts_257_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(40).std()
    return _rank_pct(base, 21)

def vts_258_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(40).std()
    return _rank_pct(base, 63)

def vts_259_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(40).std()
    return _rank_pct(base, 126)

def vts_260_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(40).std()
    return _rank_pct(base, 252)

def vts_261_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(40).std()
    return _rolling_skew(base, 5)

def vts_262_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(40).std()
    return _rolling_skew(base, 21)

def vts_263_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(40).std()
    return _rolling_skew(base, 63)

def vts_264_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(40).std()
    return _rolling_skew(base, 126)

def vts_265_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(40).std()
    return _rolling_skew(base, 252)

def vts_266_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(40).std()
    return _rolling_kurt(base, 5)

def vts_267_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(40).std()
    return _rolling_kurt(base, 21)

def vts_268_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(40).std()
    return _rolling_kurt(base, 63)

def vts_269_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(40).std()
    return _rolling_kurt(base, 126)

def vts_270_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(40).std()
    return _rolling_kurt(base, 252)

def vts_271_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(40).std()
    return _safe_div(base, _rolling_std(base, 5))

def vts_272_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(40).std()
    return _safe_div(base, _rolling_std(base, 21))

def vts_273_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(40).std()
    return _safe_div(base, _rolling_std(base, 63))

def vts_274_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(40).std()
    return _safe_div(base, _rolling_std(base, 126))

def vts_275_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(40).std()
    return _safe_div(base, _rolling_std(base, 252))

def vts_276_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(40).std()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vts_277_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(40).std()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vts_278_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(40).std()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vts_279_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(40).std()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vts_280_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(40).std()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vts_281_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(45).std()
    return _rolling_mean(base, 5)

def vts_282_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(45).std()
    return _rolling_mean(base, 21)

def vts_283_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(45).std()
    return _rolling_mean(base, 63)

def vts_284_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(45).std()
    return _rolling_mean(base, 126)

def vts_285_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(45).std()
    return _rolling_mean(base, 252)

def vts_286_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(45).std()
    return _zscore_rolling(base, 5)

def vts_287_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(45).std()
    return _zscore_rolling(base, 21)

def vts_288_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(45).std()
    return _zscore_rolling(base, 63)

def vts_289_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(45).std()
    return _zscore_rolling(base, 126)

def vts_290_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(45).std()
    return _zscore_rolling(base, 252)

def vts_291_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(45).std()
    return _rank_pct(base, 5)

def vts_292_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(45).std()
    return _rank_pct(base, 21)

def vts_293_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(45).std()
    return _rank_pct(base, 63)

def vts_294_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(45).std()
    return _rank_pct(base, 126)

def vts_295_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(45).std()
    return _rank_pct(base, 252)

def vts_296_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(45).std()
    return _rolling_skew(base, 5)

def vts_297_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(45).std()
    return _rolling_skew(base, 21)

def vts_298_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(45).std()
    return _rolling_skew(base, 63)

def vts_299_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(45).std()
    return _rolling_skew(base, 126)

def vts_300_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(45).std()
    return _rolling_skew(base, 252)
