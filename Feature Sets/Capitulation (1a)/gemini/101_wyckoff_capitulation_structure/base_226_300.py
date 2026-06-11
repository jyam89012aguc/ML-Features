"""
101_101_wyckoff_capitulation_structure — Base Features 226-300
Domain: 101_wyckoff_capitulation_structure
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

def wyck_226_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 101 wyckoff capitulation structure distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change(7)
    return _rolling_skew(base, 5)

def wyck_227_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 101 wyckoff capitulation structure distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change(7)
    return _rolling_skew(base, 21)

def wyck_228_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 101 wyckoff capitulation structure distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change(7)
    return _rolling_skew(base, 63)

def wyck_229_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 101 wyckoff capitulation structure distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change(7)
    return _rolling_skew(base, 126)

def wyck_230_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 101 wyckoff capitulation structure distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change(7)
    return _rolling_skew(base, 252)

def wyck_231_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 101 wyckoff capitulation structure over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(7)
    return _rolling_kurt(base, 5)

def wyck_232_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 101 wyckoff capitulation structure over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(7)
    return _rolling_kurt(base, 21)

def wyck_233_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 101 wyckoff capitulation structure over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(7)
    return _rolling_kurt(base, 63)

def wyck_234_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 101 wyckoff capitulation structure over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(7)
    return _rolling_kurt(base, 126)

def wyck_235_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 101 wyckoff capitulation structure over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(7)
    return _rolling_kurt(base, 252)

def wyck_236_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 101 wyckoff capitulation structure for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(7)
    return _safe_div(base, _rolling_std(base, 5))

def wyck_237_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 101 wyckoff capitulation structure for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(7)
    return _safe_div(base, _rolling_std(base, 21))

def wyck_238_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 101 wyckoff capitulation structure for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(7)
    return _safe_div(base, _rolling_std(base, 63))

def wyck_239_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 101 wyckoff capitulation structure for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(7)
    return _safe_div(base, _rolling_std(base, 126))

def wyck_240_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 101 wyckoff capitulation structure for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(7)
    return _safe_div(base, _rolling_std(base, 252))

def wyck_241_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 101 wyckoff capitulation structure over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(7)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def wyck_242_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 101 wyckoff capitulation structure over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(7)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def wyck_243_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 101 wyckoff capitulation structure over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(7)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def wyck_244_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 101 wyckoff capitulation structure over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(7)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def wyck_245_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 101 wyckoff capitulation structure over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(7)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def wyck_246_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 101 wyckoff capitulation structure over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change(8)
    return _rolling_mean(base, 5)

def wyck_247_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 101 wyckoff capitulation structure over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change(8)
    return _rolling_mean(base, 21)

def wyck_248_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 101 wyckoff capitulation structure over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change(8)
    return _rolling_mean(base, 63)

def wyck_249_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 101 wyckoff capitulation structure over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change(8)
    return _rolling_mean(base, 126)

def wyck_250_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 101 wyckoff capitulation structure over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change(8)
    return _rolling_mean(base, 252)

def wyck_251_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 101 wyckoff capitulation structure by measuring deviations from the 5d mean.
    """
    base = close.pct_change(8)
    return _zscore_rolling(base, 5)

def wyck_252_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 101 wyckoff capitulation structure by measuring deviations from the 21d mean.
    """
    base = close.pct_change(8)
    return _zscore_rolling(base, 21)

def wyck_253_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 101 wyckoff capitulation structure by measuring deviations from the 63d mean.
    """
    base = close.pct_change(8)
    return _zscore_rolling(base, 63)

def wyck_254_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 101 wyckoff capitulation structure by measuring deviations from the 126d mean.
    """
    base = close.pct_change(8)
    return _zscore_rolling(base, 126)

def wyck_255_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 101 wyckoff capitulation structure by measuring deviations from the 252d mean.
    """
    base = close.pct_change(8)
    return _zscore_rolling(base, 252)

def wyck_256_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 101 wyckoff capitulation structure to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change(8)
    return _rank_pct(base, 5)

def wyck_257_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 101 wyckoff capitulation structure to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change(8)
    return _rank_pct(base, 21)

def wyck_258_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 101 wyckoff capitulation structure to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change(8)
    return _rank_pct(base, 63)

def wyck_259_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 101 wyckoff capitulation structure to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change(8)
    return _rank_pct(base, 126)

def wyck_260_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 101 wyckoff capitulation structure to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change(8)
    return _rank_pct(base, 252)

def wyck_261_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 101 wyckoff capitulation structure distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change(8)
    return _rolling_skew(base, 5)

def wyck_262_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 101 wyckoff capitulation structure distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change(8)
    return _rolling_skew(base, 21)

def wyck_263_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 101 wyckoff capitulation structure distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change(8)
    return _rolling_skew(base, 63)

def wyck_264_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 101 wyckoff capitulation structure distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change(8)
    return _rolling_skew(base, 126)

def wyck_265_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 101 wyckoff capitulation structure distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change(8)
    return _rolling_skew(base, 252)

def wyck_266_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 101 wyckoff capitulation structure over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(8)
    return _rolling_kurt(base, 5)

def wyck_267_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 101 wyckoff capitulation structure over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(8)
    return _rolling_kurt(base, 21)

def wyck_268_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 101 wyckoff capitulation structure over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(8)
    return _rolling_kurt(base, 63)

def wyck_269_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 101 wyckoff capitulation structure over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(8)
    return _rolling_kurt(base, 126)

def wyck_270_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 101 wyckoff capitulation structure over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(8)
    return _rolling_kurt(base, 252)

def wyck_271_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 101 wyckoff capitulation structure for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(8)
    return _safe_div(base, _rolling_std(base, 5))

def wyck_272_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 101 wyckoff capitulation structure for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(8)
    return _safe_div(base, _rolling_std(base, 21))

def wyck_273_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 101 wyckoff capitulation structure for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(8)
    return _safe_div(base, _rolling_std(base, 63))

def wyck_274_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 101 wyckoff capitulation structure for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(8)
    return _safe_div(base, _rolling_std(base, 126))

def wyck_275_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 101 wyckoff capitulation structure for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(8)
    return _safe_div(base, _rolling_std(base, 252))

def wyck_276_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 101 wyckoff capitulation structure over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(8)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def wyck_277_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 101 wyckoff capitulation structure over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(8)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def wyck_278_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 101 wyckoff capitulation structure over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(8)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def wyck_279_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 101 wyckoff capitulation structure over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(8)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def wyck_280_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 101 wyckoff capitulation structure over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(8)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def wyck_281_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 101 wyckoff capitulation structure over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change(9)
    return _rolling_mean(base, 5)

def wyck_282_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 101 wyckoff capitulation structure over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change(9)
    return _rolling_mean(base, 21)

def wyck_283_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 101 wyckoff capitulation structure over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change(9)
    return _rolling_mean(base, 63)

def wyck_284_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 101 wyckoff capitulation structure over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change(9)
    return _rolling_mean(base, 126)

def wyck_285_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 101 wyckoff capitulation structure over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change(9)
    return _rolling_mean(base, 252)

def wyck_286_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 101 wyckoff capitulation structure by measuring deviations from the 5d mean.
    """
    base = close.pct_change(9)
    return _zscore_rolling(base, 5)

def wyck_287_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 101 wyckoff capitulation structure by measuring deviations from the 21d mean.
    """
    base = close.pct_change(9)
    return _zscore_rolling(base, 21)

def wyck_288_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 101 wyckoff capitulation structure by measuring deviations from the 63d mean.
    """
    base = close.pct_change(9)
    return _zscore_rolling(base, 63)

def wyck_289_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 101 wyckoff capitulation structure by measuring deviations from the 126d mean.
    """
    base = close.pct_change(9)
    return _zscore_rolling(base, 126)

def wyck_290_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 101 wyckoff capitulation structure by measuring deviations from the 252d mean.
    """
    base = close.pct_change(9)
    return _zscore_rolling(base, 252)

def wyck_291_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 101 wyckoff capitulation structure to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change(9)
    return _rank_pct(base, 5)

def wyck_292_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 101 wyckoff capitulation structure to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change(9)
    return _rank_pct(base, 21)

def wyck_293_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 101 wyckoff capitulation structure to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change(9)
    return _rank_pct(base, 63)

def wyck_294_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 101 wyckoff capitulation structure to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change(9)
    return _rank_pct(base, 126)

def wyck_295_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 101 wyckoff capitulation structure to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change(9)
    return _rank_pct(base, 252)

def wyck_296_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 101 wyckoff capitulation structure distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change(9)
    return _rolling_skew(base, 5)

def wyck_297_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 101 wyckoff capitulation structure distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change(9)
    return _rolling_skew(base, 21)

def wyck_298_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 101 wyckoff capitulation structure distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change(9)
    return _rolling_skew(base, 63)

def wyck_299_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 101 wyckoff capitulation structure distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change(9)
    return _rolling_skew(base, 126)

def wyck_300_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 101 wyckoff capitulation structure distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change(9)
    return _rolling_skew(base, 252)
