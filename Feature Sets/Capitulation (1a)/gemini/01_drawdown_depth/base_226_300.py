"""
01_01_drawdown_depth — Base Features 226-300
Domain: 01_drawdown_depth
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

def dd_226_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 01 drawdown depth distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_skew(base, 5)

def dd_227_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 01 drawdown depth distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_skew(base, 21)

def dd_228_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 01 drawdown depth distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_skew(base, 63)

def dd_229_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 01 drawdown depth distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_skew(base, 126)

def dd_230_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 01 drawdown depth distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_skew(base, 252)

def dd_231_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 01 drawdown depth over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_kurt(base, 5)

def dd_232_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 01 drawdown depth over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_kurt(base, 21)

def dd_233_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 01 drawdown depth over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_kurt(base, 63)

def dd_234_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 01 drawdown depth over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_kurt(base, 126)

def dd_235_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 01 drawdown depth over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_kurt(base, 252)

def dd_236_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 01 drawdown depth for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _safe_div(base, _rolling_std(base, 5))

def dd_237_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 01 drawdown depth for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _safe_div(base, _rolling_std(base, 21))

def dd_238_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 01 drawdown depth for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _safe_div(base, _rolling_std(base, 63))

def dd_239_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 01 drawdown depth for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _safe_div(base, _rolling_std(base, 126))

def dd_240_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 01 drawdown depth for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _safe_div(base, _rolling_std(base, 252))

def dd_241_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 01 drawdown depth over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dd_242_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 01 drawdown depth over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dd_243_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 01 drawdown depth over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dd_244_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 01 drawdown depth over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dd_245_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 01 drawdown depth over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dd_246_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 01 drawdown depth over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_mean(base, 5)

def dd_247_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 01 drawdown depth over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_mean(base, 21)

def dd_248_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 01 drawdown depth over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_mean(base, 63)

def dd_249_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 01 drawdown depth over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_mean(base, 126)

def dd_250_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 01 drawdown depth over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_mean(base, 252)

def dd_251_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 01 drawdown depth by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _zscore_rolling(base, 5)

def dd_252_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 01 drawdown depth by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _zscore_rolling(base, 21)

def dd_253_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 01 drawdown depth by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _zscore_rolling(base, 63)

def dd_254_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 01 drawdown depth by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _zscore_rolling(base, 126)

def dd_255_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 01 drawdown depth by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _zscore_rolling(base, 252)

def dd_256_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 01 drawdown depth to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rank_pct(base, 5)

def dd_257_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 01 drawdown depth to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rank_pct(base, 21)

def dd_258_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 01 drawdown depth to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rank_pct(base, 63)

def dd_259_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 01 drawdown depth to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rank_pct(base, 126)

def dd_260_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 01 drawdown depth to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rank_pct(base, 252)

def dd_261_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 01 drawdown depth distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_skew(base, 5)

def dd_262_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 01 drawdown depth distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_skew(base, 21)

def dd_263_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 01 drawdown depth distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_skew(base, 63)

def dd_264_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 01 drawdown depth distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_skew(base, 126)

def dd_265_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 01 drawdown depth distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_skew(base, 252)

def dd_266_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 01 drawdown depth over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_kurt(base, 5)

def dd_267_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 01 drawdown depth over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_kurt(base, 21)

def dd_268_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 01 drawdown depth over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_kurt(base, 63)

def dd_269_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 01 drawdown depth over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_kurt(base, 126)

def dd_270_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 01 drawdown depth over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_kurt(base, 252)

def dd_271_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 01 drawdown depth for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _safe_div(base, _rolling_std(base, 5))

def dd_272_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 01 drawdown depth for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _safe_div(base, _rolling_std(base, 21))

def dd_273_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 01 drawdown depth for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _safe_div(base, _rolling_std(base, 63))

def dd_274_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 01 drawdown depth for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _safe_div(base, _rolling_std(base, 126))

def dd_275_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 01 drawdown depth for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _safe_div(base, _rolling_std(base, 252))

def dd_276_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 01 drawdown depth over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dd_277_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 01 drawdown depth over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dd_278_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 01 drawdown depth over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dd_279_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 01 drawdown depth over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dd_280_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 01 drawdown depth over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dd_281_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 01 drawdown depth over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_mean(base, 5)

def dd_282_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 01 drawdown depth over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_mean(base, 21)

def dd_283_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 01 drawdown depth over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_mean(base, 63)

def dd_284_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 01 drawdown depth over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_mean(base, 126)

def dd_285_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 01 drawdown depth over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_mean(base, 252)

def dd_286_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 01 drawdown depth by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _zscore_rolling(base, 5)

def dd_287_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 01 drawdown depth by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _zscore_rolling(base, 21)

def dd_288_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 01 drawdown depth by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _zscore_rolling(base, 63)

def dd_289_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 01 drawdown depth by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _zscore_rolling(base, 126)

def dd_290_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 01 drawdown depth by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _zscore_rolling(base, 252)

def dd_291_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 01 drawdown depth to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rank_pct(base, 5)

def dd_292_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 01 drawdown depth to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rank_pct(base, 21)

def dd_293_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 01 drawdown depth to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rank_pct(base, 63)

def dd_294_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 01 drawdown depth to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rank_pct(base, 126)

def dd_295_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 01 drawdown depth to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rank_pct(base, 252)

def dd_296_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 01 drawdown depth distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_skew(base, 5)

def dd_297_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 01 drawdown depth distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_skew(base, 21)

def dd_298_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 01 drawdown depth distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_skew(base, 63)

def dd_299_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 01 drawdown depth distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_skew(base, 126)

def dd_300_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 01 drawdown depth distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_skew(base, 252)
