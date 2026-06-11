"""
57_57_spread_proxy — Base Features 226-300
Domain: 57_spread_proxy
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

def sprd_226_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 57 spread proxy distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_skew(base, 5)

def sprd_227_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 57 spread proxy distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_skew(base, 21)

def sprd_228_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 57 spread proxy distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_skew(base, 63)

def sprd_229_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 57 spread proxy distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_skew(base, 126)

def sprd_230_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 57 spread proxy distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_skew(base, 252)

def sprd_231_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 57 spread proxy over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_kurt(base, 5)

def sprd_232_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 57 spread proxy over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_kurt(base, 21)

def sprd_233_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 57 spread proxy over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_kurt(base, 63)

def sprd_234_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 57 spread proxy over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_kurt(base, 126)

def sprd_235_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 57 spread proxy over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_kurt(base, 252)

def sprd_236_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 57 spread proxy for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _safe_div(base, _rolling_std(base, 5))

def sprd_237_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 57 spread proxy for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _safe_div(base, _rolling_std(base, 21))

def sprd_238_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 57 spread proxy for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _safe_div(base, _rolling_std(base, 63))

def sprd_239_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 57 spread proxy for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _safe_div(base, _rolling_std(base, 126))

def sprd_240_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 57 spread proxy for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _safe_div(base, _rolling_std(base, 252))

def sprd_241_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 57 spread proxy over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def sprd_242_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 57 spread proxy over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def sprd_243_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 57 spread proxy over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def sprd_244_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 57 spread proxy over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def sprd_245_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 57 spread proxy over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def sprd_246_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 57 spread proxy over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_mean(base, 5)

def sprd_247_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 57 spread proxy over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_mean(base, 21)

def sprd_248_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 57 spread proxy over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_mean(base, 63)

def sprd_249_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 57 spread proxy over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_mean(base, 126)

def sprd_250_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 57 spread proxy over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_mean(base, 252)

def sprd_251_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 57 spread proxy by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _zscore_rolling(base, 5)

def sprd_252_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 57 spread proxy by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _zscore_rolling(base, 21)

def sprd_253_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 57 spread proxy by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _zscore_rolling(base, 63)

def sprd_254_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 57 spread proxy by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _zscore_rolling(base, 126)

def sprd_255_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 57 spread proxy by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _zscore_rolling(base, 252)

def sprd_256_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 57 spread proxy to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rank_pct(base, 5)

def sprd_257_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 57 spread proxy to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rank_pct(base, 21)

def sprd_258_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 57 spread proxy to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rank_pct(base, 63)

def sprd_259_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 57 spread proxy to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rank_pct(base, 126)

def sprd_260_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 57 spread proxy to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rank_pct(base, 252)

def sprd_261_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 57 spread proxy distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_skew(base, 5)

def sprd_262_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 57 spread proxy distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_skew(base, 21)

def sprd_263_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 57 spread proxy distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_skew(base, 63)

def sprd_264_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 57 spread proxy distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_skew(base, 126)

def sprd_265_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 57 spread proxy distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_skew(base, 252)

def sprd_266_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 57 spread proxy over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_kurt(base, 5)

def sprd_267_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 57 spread proxy over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_kurt(base, 21)

def sprd_268_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 57 spread proxy over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_kurt(base, 63)

def sprd_269_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 57 spread proxy over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_kurt(base, 126)

def sprd_270_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 57 spread proxy over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_kurt(base, 252)

def sprd_271_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 57 spread proxy for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _safe_div(base, _rolling_std(base, 5))

def sprd_272_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 57 spread proxy for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _safe_div(base, _rolling_std(base, 21))

def sprd_273_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 57 spread proxy for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _safe_div(base, _rolling_std(base, 63))

def sprd_274_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 57 spread proxy for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _safe_div(base, _rolling_std(base, 126))

def sprd_275_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 57 spread proxy for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _safe_div(base, _rolling_std(base, 252))

def sprd_276_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 57 spread proxy over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def sprd_277_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 57 spread proxy over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def sprd_278_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 57 spread proxy over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def sprd_279_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 57 spread proxy over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def sprd_280_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 57 spread proxy over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def sprd_281_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 57 spread proxy over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_mean(base, 5)

def sprd_282_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 57 spread proxy over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_mean(base, 21)

def sprd_283_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 57 spread proxy over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_mean(base, 63)

def sprd_284_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 57 spread proxy over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_mean(base, 126)

def sprd_285_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 57 spread proxy over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_mean(base, 252)

def sprd_286_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 57 spread proxy by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _zscore_rolling(base, 5)

def sprd_287_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 57 spread proxy by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _zscore_rolling(base, 21)

def sprd_288_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 57 spread proxy by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _zscore_rolling(base, 63)

def sprd_289_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 57 spread proxy by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _zscore_rolling(base, 126)

def sprd_290_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 57 spread proxy by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _zscore_rolling(base, 252)

def sprd_291_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 57 spread proxy to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rank_pct(base, 5)

def sprd_292_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 57 spread proxy to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rank_pct(base, 21)

def sprd_293_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 57 spread proxy to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rank_pct(base, 63)

def sprd_294_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 57 spread proxy to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rank_pct(base, 126)

def sprd_295_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 57 spread proxy to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rank_pct(base, 252)

def sprd_296_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 57 spread proxy distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_skew(base, 5)

def sprd_297_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 57 spread proxy distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_skew(base, 21)

def sprd_298_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 57 spread proxy distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_skew(base, 63)

def sprd_299_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 57 spread proxy distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_skew(base, 126)

def sprd_300_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 57 spread proxy distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_skew(base, 252)
