"""
108_108_drawdown_history_rank — Base Features 226-300
Domain: 108_drawdown_history_rank
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

def dhrk_226_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(140).max() - 1)
    return _rolling_skew(base, 5)

def dhrk_227_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(140).max() - 1)
    return _rolling_skew(base, 21)

def dhrk_228_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(140).max() - 1)
    return _rolling_skew(base, 63)

def dhrk_229_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(140).max() - 1)
    return _rolling_skew(base, 126)

def dhrk_230_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(140).max() - 1)
    return _rolling_skew(base, 252)

def dhrk_231_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 108 drawdown history rank over 5d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(140).max() - 1)
    return _rolling_kurt(base, 5)

def dhrk_232_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 108 drawdown history rank over 21d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(140).max() - 1)
    return _rolling_kurt(base, 21)

def dhrk_233_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 108 drawdown history rank over 63d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(140).max() - 1)
    return _rolling_kurt(base, 63)

def dhrk_234_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 108 drawdown history rank over 126d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(140).max() - 1)
    return _rolling_kurt(base, 126)

def dhrk_235_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 108 drawdown history rank over 252d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(140).max() - 1)
    return _rolling_kurt(base, 252)

def dhrk_236_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 108 drawdown history rank for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(140).max() - 1)
    return _safe_div(base, _rolling_std(base, 5))

def dhrk_237_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 108 drawdown history rank for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(140).max() - 1)
    return _safe_div(base, _rolling_std(base, 21))

def dhrk_238_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 108 drawdown history rank for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(140).max() - 1)
    return _safe_div(base, _rolling_std(base, 63))

def dhrk_239_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 108 drawdown history rank for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(140).max() - 1)
    return _safe_div(base, _rolling_std(base, 126))

def dhrk_240_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 108 drawdown history rank for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(140).max() - 1)
    return _safe_div(base, _rolling_std(base, 252))

def dhrk_241_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(140).max() - 1)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dhrk_242_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(140).max() - 1)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dhrk_243_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(140).max() - 1)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dhrk_244_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(140).max() - 1)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dhrk_245_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(140).max() - 1)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dhrk_246_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 108 drawdown history rank over a 5d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(160).max() - 1)
    return _rolling_mean(base, 5)

def dhrk_247_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 108 drawdown history rank over a 21d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(160).max() - 1)
    return _rolling_mean(base, 21)

def dhrk_248_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 108 drawdown history rank over a 63d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(160).max() - 1)
    return _rolling_mean(base, 63)

def dhrk_249_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 108 drawdown history rank over a 126d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(160).max() - 1)
    return _rolling_mean(base, 126)

def dhrk_250_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 108 drawdown history rank over a 252d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(160).max() - 1)
    return _rolling_mean(base, 252)

def dhrk_251_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 5d mean.
    """
    base = (close / close.rolling(160).max() - 1)
    return _zscore_rolling(base, 5)

def dhrk_252_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 21d mean.
    """
    base = (close / close.rolling(160).max() - 1)
    return _zscore_rolling(base, 21)

def dhrk_253_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 63d mean.
    """
    base = (close / close.rolling(160).max() - 1)
    return _zscore_rolling(base, 63)

def dhrk_254_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 126d mean.
    """
    base = (close / close.rolling(160).max() - 1)
    return _zscore_rolling(base, 126)

def dhrk_255_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 252d mean.
    """
    base = (close / close.rolling(160).max() - 1)
    return _zscore_rolling(base, 252)

def dhrk_256_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(160).max() - 1)
    return _rank_pct(base, 5)

def dhrk_257_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(160).max() - 1)
    return _rank_pct(base, 21)

def dhrk_258_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(160).max() - 1)
    return _rank_pct(base, 63)

def dhrk_259_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(160).max() - 1)
    return _rank_pct(base, 126)

def dhrk_260_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(160).max() - 1)
    return _rank_pct(base, 252)

def dhrk_261_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(160).max() - 1)
    return _rolling_skew(base, 5)

def dhrk_262_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(160).max() - 1)
    return _rolling_skew(base, 21)

def dhrk_263_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(160).max() - 1)
    return _rolling_skew(base, 63)

def dhrk_264_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(160).max() - 1)
    return _rolling_skew(base, 126)

def dhrk_265_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(160).max() - 1)
    return _rolling_skew(base, 252)

def dhrk_266_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 108 drawdown history rank over 5d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(160).max() - 1)
    return _rolling_kurt(base, 5)

def dhrk_267_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 108 drawdown history rank over 21d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(160).max() - 1)
    return _rolling_kurt(base, 21)

def dhrk_268_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 108 drawdown history rank over 63d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(160).max() - 1)
    return _rolling_kurt(base, 63)

def dhrk_269_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 108 drawdown history rank over 126d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(160).max() - 1)
    return _rolling_kurt(base, 126)

def dhrk_270_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 108 drawdown history rank over 252d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(160).max() - 1)
    return _rolling_kurt(base, 252)

def dhrk_271_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 108 drawdown history rank for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(160).max() - 1)
    return _safe_div(base, _rolling_std(base, 5))

def dhrk_272_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 108 drawdown history rank for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(160).max() - 1)
    return _safe_div(base, _rolling_std(base, 21))

def dhrk_273_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 108 drawdown history rank for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(160).max() - 1)
    return _safe_div(base, _rolling_std(base, 63))

def dhrk_274_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 108 drawdown history rank for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(160).max() - 1)
    return _safe_div(base, _rolling_std(base, 126))

def dhrk_275_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 108 drawdown history rank for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(160).max() - 1)
    return _safe_div(base, _rolling_std(base, 252))

def dhrk_276_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(160).max() - 1)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dhrk_277_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(160).max() - 1)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dhrk_278_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(160).max() - 1)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dhrk_279_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(160).max() - 1)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dhrk_280_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(160).max() - 1)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dhrk_281_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 108 drawdown history rank over a 5d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(180).max() - 1)
    return _rolling_mean(base, 5)

def dhrk_282_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 108 drawdown history rank over a 21d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(180).max() - 1)
    return _rolling_mean(base, 21)

def dhrk_283_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 108 drawdown history rank over a 63d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(180).max() - 1)
    return _rolling_mean(base, 63)

def dhrk_284_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 108 drawdown history rank over a 126d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(180).max() - 1)
    return _rolling_mean(base, 126)

def dhrk_285_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 108 drawdown history rank over a 252d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(180).max() - 1)
    return _rolling_mean(base, 252)

def dhrk_286_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 5d mean.
    """
    base = (close / close.rolling(180).max() - 1)
    return _zscore_rolling(base, 5)

def dhrk_287_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 21d mean.
    """
    base = (close / close.rolling(180).max() - 1)
    return _zscore_rolling(base, 21)

def dhrk_288_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 63d mean.
    """
    base = (close / close.rolling(180).max() - 1)
    return _zscore_rolling(base, 63)

def dhrk_289_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 126d mean.
    """
    base = (close / close.rolling(180).max() - 1)
    return _zscore_rolling(base, 126)

def dhrk_290_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 252d mean.
    """
    base = (close / close.rolling(180).max() - 1)
    return _zscore_rolling(base, 252)

def dhrk_291_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(180).max() - 1)
    return _rank_pct(base, 5)

def dhrk_292_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(180).max() - 1)
    return _rank_pct(base, 21)

def dhrk_293_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(180).max() - 1)
    return _rank_pct(base, 63)

def dhrk_294_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(180).max() - 1)
    return _rank_pct(base, 126)

def dhrk_295_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(180).max() - 1)
    return _rank_pct(base, 252)

def dhrk_296_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(180).max() - 1)
    return _rolling_skew(base, 5)

def dhrk_297_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(180).max() - 1)
    return _rolling_skew(base, 21)

def dhrk_298_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(180).max() - 1)
    return _rolling_skew(base, 63)

def dhrk_299_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(180).max() - 1)
    return _rolling_skew(base, 126)

def dhrk_300_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(180).max() - 1)
    return _rolling_skew(base, 252)
