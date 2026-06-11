"""
123_123_relative_weakness_xs — Base Features 226-300
Domain: 123_relative_weakness_xs
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

def rwxs_226_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change(140)
    return _rolling_skew(base, 5)

def rwxs_227_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change(140)
    return _rolling_skew(base, 21)

def rwxs_228_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change(140)
    return _rolling_skew(base, 63)

def rwxs_229_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change(140)
    return _rolling_skew(base, 126)

def rwxs_230_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change(140)
    return _rolling_skew(base, 252)

def rwxs_231_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(140)
    return _rolling_kurt(base, 5)

def rwxs_232_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(140)
    return _rolling_kurt(base, 21)

def rwxs_233_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(140)
    return _rolling_kurt(base, 63)

def rwxs_234_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(140)
    return _rolling_kurt(base, 126)

def rwxs_235_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(140)
    return _rolling_kurt(base, 252)

def rwxs_236_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(140)
    return _safe_div(base, _rolling_std(base, 5))

def rwxs_237_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(140)
    return _safe_div(base, _rolling_std(base, 21))

def rwxs_238_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(140)
    return _safe_div(base, _rolling_std(base, 63))

def rwxs_239_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(140)
    return _safe_div(base, _rolling_std(base, 126))

def rwxs_240_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(140)
    return _safe_div(base, _rolling_std(base, 252))

def rwxs_241_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(140)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def rwxs_242_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(140)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def rwxs_243_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(140)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def rwxs_244_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(140)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def rwxs_245_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(140)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def rwxs_246_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change(160)
    return _rolling_mean(base, 5)

def rwxs_247_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change(160)
    return _rolling_mean(base, 21)

def rwxs_248_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change(160)
    return _rolling_mean(base, 63)

def rwxs_249_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change(160)
    return _rolling_mean(base, 126)

def rwxs_250_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change(160)
    return _rolling_mean(base, 252)

def rwxs_251_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 5d mean.
    """
    base = close.pct_change(160)
    return _zscore_rolling(base, 5)

def rwxs_252_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 21d mean.
    """
    base = close.pct_change(160)
    return _zscore_rolling(base, 21)

def rwxs_253_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 63d mean.
    """
    base = close.pct_change(160)
    return _zscore_rolling(base, 63)

def rwxs_254_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 126d mean.
    """
    base = close.pct_change(160)
    return _zscore_rolling(base, 126)

def rwxs_255_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 252d mean.
    """
    base = close.pct_change(160)
    return _zscore_rolling(base, 252)

def rwxs_256_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change(160)
    return _rank_pct(base, 5)

def rwxs_257_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change(160)
    return _rank_pct(base, 21)

def rwxs_258_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change(160)
    return _rank_pct(base, 63)

def rwxs_259_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change(160)
    return _rank_pct(base, 126)

def rwxs_260_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change(160)
    return _rank_pct(base, 252)

def rwxs_261_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change(160)
    return _rolling_skew(base, 5)

def rwxs_262_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change(160)
    return _rolling_skew(base, 21)

def rwxs_263_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change(160)
    return _rolling_skew(base, 63)

def rwxs_264_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change(160)
    return _rolling_skew(base, 126)

def rwxs_265_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change(160)
    return _rolling_skew(base, 252)

def rwxs_266_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(160)
    return _rolling_kurt(base, 5)

def rwxs_267_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(160)
    return _rolling_kurt(base, 21)

def rwxs_268_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(160)
    return _rolling_kurt(base, 63)

def rwxs_269_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(160)
    return _rolling_kurt(base, 126)

def rwxs_270_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(160)
    return _rolling_kurt(base, 252)

def rwxs_271_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(160)
    return _safe_div(base, _rolling_std(base, 5))

def rwxs_272_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(160)
    return _safe_div(base, _rolling_std(base, 21))

def rwxs_273_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(160)
    return _safe_div(base, _rolling_std(base, 63))

def rwxs_274_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(160)
    return _safe_div(base, _rolling_std(base, 126))

def rwxs_275_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(160)
    return _safe_div(base, _rolling_std(base, 252))

def rwxs_276_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(160)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def rwxs_277_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(160)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def rwxs_278_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(160)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def rwxs_279_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(160)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def rwxs_280_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(160)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def rwxs_281_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change(180)
    return _rolling_mean(base, 5)

def rwxs_282_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change(180)
    return _rolling_mean(base, 21)

def rwxs_283_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change(180)
    return _rolling_mean(base, 63)

def rwxs_284_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change(180)
    return _rolling_mean(base, 126)

def rwxs_285_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change(180)
    return _rolling_mean(base, 252)

def rwxs_286_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 5d mean.
    """
    base = close.pct_change(180)
    return _zscore_rolling(base, 5)

def rwxs_287_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 21d mean.
    """
    base = close.pct_change(180)
    return _zscore_rolling(base, 21)

def rwxs_288_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 63d mean.
    """
    base = close.pct_change(180)
    return _zscore_rolling(base, 63)

def rwxs_289_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 126d mean.
    """
    base = close.pct_change(180)
    return _zscore_rolling(base, 126)

def rwxs_290_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 252d mean.
    """
    base = close.pct_change(180)
    return _zscore_rolling(base, 252)

def rwxs_291_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change(180)
    return _rank_pct(base, 5)

def rwxs_292_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change(180)
    return _rank_pct(base, 21)

def rwxs_293_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change(180)
    return _rank_pct(base, 63)

def rwxs_294_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change(180)
    return _rank_pct(base, 126)

def rwxs_295_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change(180)
    return _rank_pct(base, 252)

def rwxs_296_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change(180)
    return _rolling_skew(base, 5)

def rwxs_297_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change(180)
    return _rolling_skew(base, 21)

def rwxs_298_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change(180)
    return _rolling_skew(base, 63)

def rwxs_299_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change(180)
    return _rolling_skew(base, 126)

def rwxs_300_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change(180)
    return _rolling_skew(base, 252)
