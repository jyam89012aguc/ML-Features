"""
47_47_gap_down_clustering — Base Features 226-300
Domain: 47_gap_down_clustering
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

def gapc_226_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 5d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _rolling_skew(base, 5)

def gapc_227_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 21d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _rolling_skew(base, 21)

def gapc_228_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 63d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _rolling_skew(base, 63)

def gapc_229_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 126d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _rolling_skew(base, 126)

def gapc_230_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 252d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _rolling_skew(base, 252)

def gapc_231_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 5d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _rolling_kurt(base, 5)

def gapc_232_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 21d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _rolling_kurt(base, 21)

def gapc_233_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 63d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _rolling_kurt(base, 63)

def gapc_234_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 126d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _rolling_kurt(base, 126)

def gapc_235_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 252d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _rolling_kurt(base, 252)

def gapc_236_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _safe_div(base, _rolling_std(base, 5))

def gapc_237_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _safe_div(base, _rolling_std(base, 21))

def gapc_238_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _safe_div(base, _rolling_std(base, 63))

def gapc_239_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _safe_div(base, _rolling_std(base, 126))

def gapc_240_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _safe_div(base, _rolling_std(base, 252))

def gapc_241_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 5d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(35).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def gapc_242_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 21d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(35).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def gapc_243_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 63d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(35).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def gapc_244_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 126d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(35).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def gapc_245_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 252d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(35).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def gapc_246_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 5d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(40).mean())
    return _rolling_mean(base, 5)

def gapc_247_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 21d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(40).mean())
    return _rolling_mean(base, 21)

def gapc_248_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 63d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(40).mean())
    return _rolling_mean(base, 63)

def gapc_249_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 126d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(40).mean())
    return _rolling_mean(base, 126)

def gapc_250_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 252d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(40).mean())
    return _rolling_mean(base, 252)

def gapc_251_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 5d mean.
    """
    base = ((close - open).abs().rolling(40).mean())
    return _zscore_rolling(base, 5)

def gapc_252_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 21d mean.
    """
    base = ((close - open).abs().rolling(40).mean())
    return _zscore_rolling(base, 21)

def gapc_253_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 63d mean.
    """
    base = ((close - open).abs().rolling(40).mean())
    return _zscore_rolling(base, 63)

def gapc_254_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 126d mean.
    """
    base = ((close - open).abs().rolling(40).mean())
    return _zscore_rolling(base, 126)

def gapc_255_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 252d mean.
    """
    base = ((close - open).abs().rolling(40).mean())
    return _zscore_rolling(base, 252)

def gapc_256_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(40).mean())
    return _rank_pct(base, 5)

def gapc_257_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(40).mean())
    return _rank_pct(base, 21)

def gapc_258_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(40).mean())
    return _rank_pct(base, 63)

def gapc_259_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(40).mean())
    return _rank_pct(base, 126)

def gapc_260_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(40).mean())
    return _rank_pct(base, 252)

def gapc_261_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 5d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(40).mean())
    return _rolling_skew(base, 5)

def gapc_262_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 21d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(40).mean())
    return _rolling_skew(base, 21)

def gapc_263_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 63d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(40).mean())
    return _rolling_skew(base, 63)

def gapc_264_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 126d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(40).mean())
    return _rolling_skew(base, 126)

def gapc_265_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 252d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(40).mean())
    return _rolling_skew(base, 252)

def gapc_266_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 5d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(40).mean())
    return _rolling_kurt(base, 5)

def gapc_267_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 21d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(40).mean())
    return _rolling_kurt(base, 21)

def gapc_268_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 63d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(40).mean())
    return _rolling_kurt(base, 63)

def gapc_269_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 126d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(40).mean())
    return _rolling_kurt(base, 126)

def gapc_270_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 252d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(40).mean())
    return _rolling_kurt(base, 252)

def gapc_271_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(40).mean())
    return _safe_div(base, _rolling_std(base, 5))

def gapc_272_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(40).mean())
    return _safe_div(base, _rolling_std(base, 21))

def gapc_273_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(40).mean())
    return _safe_div(base, _rolling_std(base, 63))

def gapc_274_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(40).mean())
    return _safe_div(base, _rolling_std(base, 126))

def gapc_275_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(40).mean())
    return _safe_div(base, _rolling_std(base, 252))

def gapc_276_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 5d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(40).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def gapc_277_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 21d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(40).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def gapc_278_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 63d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(40).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def gapc_279_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 126d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(40).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def gapc_280_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 252d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(40).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def gapc_281_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 5d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _rolling_mean(base, 5)

def gapc_282_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 21d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _rolling_mean(base, 21)

def gapc_283_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 63d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _rolling_mean(base, 63)

def gapc_284_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 126d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _rolling_mean(base, 126)

def gapc_285_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 252d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _rolling_mean(base, 252)

def gapc_286_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 5d mean.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _zscore_rolling(base, 5)

def gapc_287_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 21d mean.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _zscore_rolling(base, 21)

def gapc_288_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 63d mean.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _zscore_rolling(base, 63)

def gapc_289_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 126d mean.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _zscore_rolling(base, 126)

def gapc_290_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 252d mean.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _zscore_rolling(base, 252)

def gapc_291_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _rank_pct(base, 5)

def gapc_292_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _rank_pct(base, 21)

def gapc_293_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _rank_pct(base, 63)

def gapc_294_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _rank_pct(base, 126)

def gapc_295_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _rank_pct(base, 252)

def gapc_296_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 5d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _rolling_skew(base, 5)

def gapc_297_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 21d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _rolling_skew(base, 21)

def gapc_298_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 63d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _rolling_skew(base, 63)

def gapc_299_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 126d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _rolling_skew(base, 126)

def gapc_300_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 252d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _rolling_skew(base, 252)
