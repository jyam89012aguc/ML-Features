"""
107_107_change_point_detection — Base Features 226-300
Domain: 107_change_point_detection
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

def cpdt_226_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(35).std().diff()
    return _rolling_skew(base, 5)

def cpdt_227_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(35).std().diff()
    return _rolling_skew(base, 21)

def cpdt_228_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(35).std().diff()
    return _rolling_skew(base, 63)

def cpdt_229_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(35).std().diff()
    return _rolling_skew(base, 126)

def cpdt_230_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(35).std().diff()
    return _rolling_skew(base, 252)

def cpdt_231_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 107 change point detection over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(35).std().diff()
    return _rolling_kurt(base, 5)

def cpdt_232_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 107 change point detection over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(35).std().diff()
    return _rolling_kurt(base, 21)

def cpdt_233_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 107 change point detection over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(35).std().diff()
    return _rolling_kurt(base, 63)

def cpdt_234_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 107 change point detection over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(35).std().diff()
    return _rolling_kurt(base, 126)

def cpdt_235_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 107 change point detection over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(35).std().diff()
    return _rolling_kurt(base, 252)

def cpdt_236_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 107 change point detection for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(35).std().diff()
    return _safe_div(base, _rolling_std(base, 5))

def cpdt_237_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 107 change point detection for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(35).std().diff()
    return _safe_div(base, _rolling_std(base, 21))

def cpdt_238_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 107 change point detection for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(35).std().diff()
    return _safe_div(base, _rolling_std(base, 63))

def cpdt_239_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 107 change point detection for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(35).std().diff()
    return _safe_div(base, _rolling_std(base, 126))

def cpdt_240_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 107 change point detection for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(35).std().diff()
    return _safe_div(base, _rolling_std(base, 252))

def cpdt_241_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(35).std().diff()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def cpdt_242_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(35).std().diff()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def cpdt_243_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(35).std().diff()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def cpdt_244_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(35).std().diff()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def cpdt_245_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(35).std().diff()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def cpdt_246_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(40).std().diff()
    return _rolling_mean(base, 5)

def cpdt_247_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(40).std().diff()
    return _rolling_mean(base, 21)

def cpdt_248_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(40).std().diff()
    return _rolling_mean(base, 63)

def cpdt_249_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(40).std().diff()
    return _rolling_mean(base, 126)

def cpdt_250_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(40).std().diff()
    return _rolling_mean(base, 252)

def cpdt_251_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 107 change point detection by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(40).std().diff()
    return _zscore_rolling(base, 5)

def cpdt_252_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 107 change point detection by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(40).std().diff()
    return _zscore_rolling(base, 21)

def cpdt_253_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 107 change point detection by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(40).std().diff()
    return _zscore_rolling(base, 63)

def cpdt_254_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 107 change point detection by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(40).std().diff()
    return _zscore_rolling(base, 126)

def cpdt_255_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 107 change point detection by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(40).std().diff()
    return _zscore_rolling(base, 252)

def cpdt_256_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(40).std().diff()
    return _rank_pct(base, 5)

def cpdt_257_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(40).std().diff()
    return _rank_pct(base, 21)

def cpdt_258_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(40).std().diff()
    return _rank_pct(base, 63)

def cpdt_259_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(40).std().diff()
    return _rank_pct(base, 126)

def cpdt_260_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(40).std().diff()
    return _rank_pct(base, 252)

def cpdt_261_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(40).std().diff()
    return _rolling_skew(base, 5)

def cpdt_262_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(40).std().diff()
    return _rolling_skew(base, 21)

def cpdt_263_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(40).std().diff()
    return _rolling_skew(base, 63)

def cpdt_264_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(40).std().diff()
    return _rolling_skew(base, 126)

def cpdt_265_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(40).std().diff()
    return _rolling_skew(base, 252)

def cpdt_266_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 107 change point detection over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(40).std().diff()
    return _rolling_kurt(base, 5)

def cpdt_267_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 107 change point detection over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(40).std().diff()
    return _rolling_kurt(base, 21)

def cpdt_268_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 107 change point detection over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(40).std().diff()
    return _rolling_kurt(base, 63)

def cpdt_269_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 107 change point detection over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(40).std().diff()
    return _rolling_kurt(base, 126)

def cpdt_270_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 107 change point detection over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(40).std().diff()
    return _rolling_kurt(base, 252)

def cpdt_271_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 107 change point detection for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(40).std().diff()
    return _safe_div(base, _rolling_std(base, 5))

def cpdt_272_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 107 change point detection for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(40).std().diff()
    return _safe_div(base, _rolling_std(base, 21))

def cpdt_273_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 107 change point detection for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(40).std().diff()
    return _safe_div(base, _rolling_std(base, 63))

def cpdt_274_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 107 change point detection for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(40).std().diff()
    return _safe_div(base, _rolling_std(base, 126))

def cpdt_275_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 107 change point detection for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(40).std().diff()
    return _safe_div(base, _rolling_std(base, 252))

def cpdt_276_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(40).std().diff()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def cpdt_277_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(40).std().diff()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def cpdt_278_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(40).std().diff()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def cpdt_279_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(40).std().diff()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def cpdt_280_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(40).std().diff()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def cpdt_281_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(45).std().diff()
    return _rolling_mean(base, 5)

def cpdt_282_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(45).std().diff()
    return _rolling_mean(base, 21)

def cpdt_283_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(45).std().diff()
    return _rolling_mean(base, 63)

def cpdt_284_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(45).std().diff()
    return _rolling_mean(base, 126)

def cpdt_285_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(45).std().diff()
    return _rolling_mean(base, 252)

def cpdt_286_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 107 change point detection by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(45).std().diff()
    return _zscore_rolling(base, 5)

def cpdt_287_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 107 change point detection by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(45).std().diff()
    return _zscore_rolling(base, 21)

def cpdt_288_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 107 change point detection by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(45).std().diff()
    return _zscore_rolling(base, 63)

def cpdt_289_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 107 change point detection by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(45).std().diff()
    return _zscore_rolling(base, 126)

def cpdt_290_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 107 change point detection by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(45).std().diff()
    return _zscore_rolling(base, 252)

def cpdt_291_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(45).std().diff()
    return _rank_pct(base, 5)

def cpdt_292_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(45).std().diff()
    return _rank_pct(base, 21)

def cpdt_293_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(45).std().diff()
    return _rank_pct(base, 63)

def cpdt_294_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(45).std().diff()
    return _rank_pct(base, 126)

def cpdt_295_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(45).std().diff()
    return _rank_pct(base, 252)

def cpdt_296_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(45).std().diff()
    return _rolling_skew(base, 5)

def cpdt_297_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(45).std().diff()
    return _rolling_skew(base, 21)

def cpdt_298_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(45).std().diff()
    return _rolling_skew(base, 63)

def cpdt_299_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(45).std().diff()
    return _rolling_skew(base, 126)

def cpdt_300_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(45).std().diff()
    return _rolling_skew(base, 252)
