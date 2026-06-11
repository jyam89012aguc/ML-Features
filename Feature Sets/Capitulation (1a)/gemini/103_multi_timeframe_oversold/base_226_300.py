"""
103_103_multi_timeframe_oversold — Base Features 226-300
Domain: 103_multi_timeframe_oversold
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

def mtfo_226_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 5d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 65)
    return _rolling_skew(base, 5)

def mtfo_227_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 21d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 65)
    return _rolling_skew(base, 21)

def mtfo_228_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 63d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 65)
    return _rolling_skew(base, 63)

def mtfo_229_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 126d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 65)
    return _rolling_skew(base, 126)

def mtfo_230_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 252d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 65)
    return _rolling_skew(base, 252)

def mtfo_231_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 5d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 65)
    return _rolling_kurt(base, 5)

def mtfo_232_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 21d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 65)
    return _rolling_kurt(base, 21)

def mtfo_233_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 63d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 65)
    return _rolling_kurt(base, 63)

def mtfo_234_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 126d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 65)
    return _rolling_kurt(base, 126)

def mtfo_235_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 252d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 65)
    return _rolling_kurt(base, 252)

def mtfo_236_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 65)
    return _safe_div(base, _rolling_std(base, 5))

def mtfo_237_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 65)
    return _safe_div(base, _rolling_std(base, 21))

def mtfo_238_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 65)
    return _safe_div(base, _rolling_std(base, 63))

def mtfo_239_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 65)
    return _safe_div(base, _rolling_std(base, 126))

def mtfo_240_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 65)
    return _safe_div(base, _rolling_std(base, 252))

def mtfo_241_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 5d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 65)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def mtfo_242_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 21d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 65)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def mtfo_243_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 63d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 65)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def mtfo_244_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 126d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 65)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def mtfo_245_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 252d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 65)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def mtfo_246_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 5d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 75)
    return _rolling_mean(base, 5)

def mtfo_247_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 21d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 75)
    return _rolling_mean(base, 21)

def mtfo_248_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 63d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 75)
    return _rolling_mean(base, 63)

def mtfo_249_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 126d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 75)
    return _rolling_mean(base, 126)

def mtfo_250_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 252d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 75)
    return _rolling_mean(base, 252)

def mtfo_251_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 5d mean.
    """
    base = _zscore_rolling(close, 75)
    return _zscore_rolling(base, 5)

def mtfo_252_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 21d mean.
    """
    base = _zscore_rolling(close, 75)
    return _zscore_rolling(base, 21)

def mtfo_253_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 63d mean.
    """
    base = _zscore_rolling(close, 75)
    return _zscore_rolling(base, 63)

def mtfo_254_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 126d mean.
    """
    base = _zscore_rolling(close, 75)
    return _zscore_rolling(base, 126)

def mtfo_255_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 252d mean.
    """
    base = _zscore_rolling(close, 75)
    return _zscore_rolling(base, 252)

def mtfo_256_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 75)
    return _rank_pct(base, 5)

def mtfo_257_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 75)
    return _rank_pct(base, 21)

def mtfo_258_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 75)
    return _rank_pct(base, 63)

def mtfo_259_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 75)
    return _rank_pct(base, 126)

def mtfo_260_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 75)
    return _rank_pct(base, 252)

def mtfo_261_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 5d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 75)
    return _rolling_skew(base, 5)

def mtfo_262_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 21d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 75)
    return _rolling_skew(base, 21)

def mtfo_263_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 63d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 75)
    return _rolling_skew(base, 63)

def mtfo_264_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 126d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 75)
    return _rolling_skew(base, 126)

def mtfo_265_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 252d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 75)
    return _rolling_skew(base, 252)

def mtfo_266_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 5d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 75)
    return _rolling_kurt(base, 5)

def mtfo_267_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 21d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 75)
    return _rolling_kurt(base, 21)

def mtfo_268_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 63d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 75)
    return _rolling_kurt(base, 63)

def mtfo_269_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 126d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 75)
    return _rolling_kurt(base, 126)

def mtfo_270_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 252d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 75)
    return _rolling_kurt(base, 252)

def mtfo_271_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 75)
    return _safe_div(base, _rolling_std(base, 5))

def mtfo_272_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 75)
    return _safe_div(base, _rolling_std(base, 21))

def mtfo_273_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 75)
    return _safe_div(base, _rolling_std(base, 63))

def mtfo_274_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 75)
    return _safe_div(base, _rolling_std(base, 126))

def mtfo_275_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 75)
    return _safe_div(base, _rolling_std(base, 252))

def mtfo_276_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 5d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 75)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def mtfo_277_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 21d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 75)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def mtfo_278_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 63d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 75)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def mtfo_279_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 126d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 75)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def mtfo_280_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 252d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 75)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def mtfo_281_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 5d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 85)
    return _rolling_mean(base, 5)

def mtfo_282_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 21d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 85)
    return _rolling_mean(base, 21)

def mtfo_283_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 63d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 85)
    return _rolling_mean(base, 63)

def mtfo_284_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 126d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 85)
    return _rolling_mean(base, 126)

def mtfo_285_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 252d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 85)
    return _rolling_mean(base, 252)

def mtfo_286_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 5d mean.
    """
    base = _zscore_rolling(close, 85)
    return _zscore_rolling(base, 5)

def mtfo_287_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 21d mean.
    """
    base = _zscore_rolling(close, 85)
    return _zscore_rolling(base, 21)

def mtfo_288_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 63d mean.
    """
    base = _zscore_rolling(close, 85)
    return _zscore_rolling(base, 63)

def mtfo_289_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 126d mean.
    """
    base = _zscore_rolling(close, 85)
    return _zscore_rolling(base, 126)

def mtfo_290_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 252d mean.
    """
    base = _zscore_rolling(close, 85)
    return _zscore_rolling(base, 252)

def mtfo_291_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 85)
    return _rank_pct(base, 5)

def mtfo_292_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 85)
    return _rank_pct(base, 21)

def mtfo_293_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 85)
    return _rank_pct(base, 63)

def mtfo_294_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 85)
    return _rank_pct(base, 126)

def mtfo_295_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 85)
    return _rank_pct(base, 252)

def mtfo_296_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 5d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 85)
    return _rolling_skew(base, 5)

def mtfo_297_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 21d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 85)
    return _rolling_skew(base, 21)

def mtfo_298_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 63d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 85)
    return _rolling_skew(base, 63)

def mtfo_299_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 126d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 85)
    return _rolling_skew(base, 126)

def mtfo_300_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 252d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 85)
    return _rolling_skew(base, 252)
