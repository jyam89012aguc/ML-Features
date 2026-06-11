"""
104_104_mean_reversion_potential — Base Features 226-300
Domain: 104_mean_reversion_potential
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

def mrpt_226_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 5d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 125) - 1
    return _rolling_skew(base, 5)

def mrpt_227_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 21d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 125) - 1
    return _rolling_skew(base, 21)

def mrpt_228_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 63d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 125) - 1
    return _rolling_skew(base, 63)

def mrpt_229_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 126d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 125) - 1
    return _rolling_skew(base, 126)

def mrpt_230_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 252d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 125) - 1
    return _rolling_skew(base, 252)

def mrpt_231_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 5d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 125) - 1
    return _rolling_kurt(base, 5)

def mrpt_232_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 21d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 125) - 1
    return _rolling_kurt(base, 21)

def mrpt_233_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 63d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 125) - 1
    return _rolling_kurt(base, 63)

def mrpt_234_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 126d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 125) - 1
    return _rolling_kurt(base, 126)

def mrpt_235_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 252d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 125) - 1
    return _rolling_kurt(base, 252)

def mrpt_236_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 125) - 1
    return _safe_div(base, _rolling_std(base, 5))

def mrpt_237_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 125) - 1
    return _safe_div(base, _rolling_std(base, 21))

def mrpt_238_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 125) - 1
    return _safe_div(base, _rolling_std(base, 63))

def mrpt_239_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 125) - 1
    return _safe_div(base, _rolling_std(base, 126))

def mrpt_240_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 125) - 1
    return _safe_div(base, _rolling_std(base, 252))

def mrpt_241_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 5d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 125) - 1
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def mrpt_242_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 21d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 125) - 1
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def mrpt_243_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 63d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 125) - 1
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def mrpt_244_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 126d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 125) - 1
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def mrpt_245_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 252d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 125) - 1
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def mrpt_246_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 5d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 145) - 1
    return _rolling_mean(base, 5)

def mrpt_247_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 21d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 145) - 1
    return _rolling_mean(base, 21)

def mrpt_248_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 63d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 145) - 1
    return _rolling_mean(base, 63)

def mrpt_249_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 126d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 145) - 1
    return _rolling_mean(base, 126)

def mrpt_250_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 252d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 145) - 1
    return _rolling_mean(base, 252)

def mrpt_251_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 5d mean.
    """
    base = close / _rolling_mean(close, 145) - 1
    return _zscore_rolling(base, 5)

def mrpt_252_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 21d mean.
    """
    base = close / _rolling_mean(close, 145) - 1
    return _zscore_rolling(base, 21)

def mrpt_253_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 63d mean.
    """
    base = close / _rolling_mean(close, 145) - 1
    return _zscore_rolling(base, 63)

def mrpt_254_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 126d mean.
    """
    base = close / _rolling_mean(close, 145) - 1
    return _zscore_rolling(base, 126)

def mrpt_255_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 252d mean.
    """
    base = close / _rolling_mean(close, 145) - 1
    return _zscore_rolling(base, 252)

def mrpt_256_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 145) - 1
    return _rank_pct(base, 5)

def mrpt_257_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 145) - 1
    return _rank_pct(base, 21)

def mrpt_258_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 145) - 1
    return _rank_pct(base, 63)

def mrpt_259_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 145) - 1
    return _rank_pct(base, 126)

def mrpt_260_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 145) - 1
    return _rank_pct(base, 252)

def mrpt_261_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 5d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 145) - 1
    return _rolling_skew(base, 5)

def mrpt_262_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 21d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 145) - 1
    return _rolling_skew(base, 21)

def mrpt_263_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 63d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 145) - 1
    return _rolling_skew(base, 63)

def mrpt_264_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 126d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 145) - 1
    return _rolling_skew(base, 126)

def mrpt_265_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 252d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 145) - 1
    return _rolling_skew(base, 252)

def mrpt_266_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 5d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 145) - 1
    return _rolling_kurt(base, 5)

def mrpt_267_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 21d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 145) - 1
    return _rolling_kurt(base, 21)

def mrpt_268_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 63d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 145) - 1
    return _rolling_kurt(base, 63)

def mrpt_269_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 126d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 145) - 1
    return _rolling_kurt(base, 126)

def mrpt_270_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 252d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 145) - 1
    return _rolling_kurt(base, 252)

def mrpt_271_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 145) - 1
    return _safe_div(base, _rolling_std(base, 5))

def mrpt_272_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 145) - 1
    return _safe_div(base, _rolling_std(base, 21))

def mrpt_273_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 145) - 1
    return _safe_div(base, _rolling_std(base, 63))

def mrpt_274_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 145) - 1
    return _safe_div(base, _rolling_std(base, 126))

def mrpt_275_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 145) - 1
    return _safe_div(base, _rolling_std(base, 252))

def mrpt_276_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 5d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 145) - 1
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def mrpt_277_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 21d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 145) - 1
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def mrpt_278_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 63d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 145) - 1
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def mrpt_279_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 126d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 145) - 1
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def mrpt_280_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 252d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 145) - 1
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def mrpt_281_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 5d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 165) - 1
    return _rolling_mean(base, 5)

def mrpt_282_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 21d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 165) - 1
    return _rolling_mean(base, 21)

def mrpt_283_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 63d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 165) - 1
    return _rolling_mean(base, 63)

def mrpt_284_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 126d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 165) - 1
    return _rolling_mean(base, 126)

def mrpt_285_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 252d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 165) - 1
    return _rolling_mean(base, 252)

def mrpt_286_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 5d mean.
    """
    base = close / _rolling_mean(close, 165) - 1
    return _zscore_rolling(base, 5)

def mrpt_287_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 21d mean.
    """
    base = close / _rolling_mean(close, 165) - 1
    return _zscore_rolling(base, 21)

def mrpt_288_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 63d mean.
    """
    base = close / _rolling_mean(close, 165) - 1
    return _zscore_rolling(base, 63)

def mrpt_289_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 126d mean.
    """
    base = close / _rolling_mean(close, 165) - 1
    return _zscore_rolling(base, 126)

def mrpt_290_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 252d mean.
    """
    base = close / _rolling_mean(close, 165) - 1
    return _zscore_rolling(base, 252)

def mrpt_291_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 165) - 1
    return _rank_pct(base, 5)

def mrpt_292_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 165) - 1
    return _rank_pct(base, 21)

def mrpt_293_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 165) - 1
    return _rank_pct(base, 63)

def mrpt_294_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 165) - 1
    return _rank_pct(base, 126)

def mrpt_295_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 165) - 1
    return _rank_pct(base, 252)

def mrpt_296_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 5d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 165) - 1
    return _rolling_skew(base, 5)

def mrpt_297_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 21d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 165) - 1
    return _rolling_skew(base, 21)

def mrpt_298_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 63d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 165) - 1
    return _rolling_skew(base, 63)

def mrpt_299_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 126d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 165) - 1
    return _rolling_skew(base, 126)

def mrpt_300_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 252d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 165) - 1
    return _rolling_skew(base, 252)
