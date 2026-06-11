"""
08_08_decline_streaks — Base Features 226-300
Domain: 08_decline_streaks
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

def dstk_226_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 08 decline streaks distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_skew(base, 5)

def dstk_227_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 08 decline streaks distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_skew(base, 21)

def dstk_228_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 08 decline streaks distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_skew(base, 63)

def dstk_229_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 08 decline streaks distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_skew(base, 126)

def dstk_230_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 08 decline streaks distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_skew(base, 252)

def dstk_231_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 08 decline streaks over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_kurt(base, 5)

def dstk_232_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 08 decline streaks over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_kurt(base, 21)

def dstk_233_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 08 decline streaks over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_kurt(base, 63)

def dstk_234_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 08 decline streaks over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_kurt(base, 126)

def dstk_235_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 08 decline streaks over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_kurt(base, 252)

def dstk_236_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 08 decline streaks for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _safe_div(base, _rolling_std(base, 5))

def dstk_237_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 08 decline streaks for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _safe_div(base, _rolling_std(base, 21))

def dstk_238_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 08 decline streaks for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _safe_div(base, _rolling_std(base, 63))

def dstk_239_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 08 decline streaks for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _safe_div(base, _rolling_std(base, 126))

def dstk_240_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 08 decline streaks for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _safe_div(base, _rolling_std(base, 252))

def dstk_241_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 08 decline streaks over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dstk_242_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 08 decline streaks over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dstk_243_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 08 decline streaks over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dstk_244_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 08 decline streaks over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dstk_245_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 08 decline streaks over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dstk_246_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 08 decline streaks over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_mean(base, 5)

def dstk_247_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 08 decline streaks over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_mean(base, 21)

def dstk_248_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 08 decline streaks over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_mean(base, 63)

def dstk_249_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 08 decline streaks over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_mean(base, 126)

def dstk_250_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 08 decline streaks over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_mean(base, 252)

def dstk_251_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 08 decline streaks by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _zscore_rolling(base, 5)

def dstk_252_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 08 decline streaks by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _zscore_rolling(base, 21)

def dstk_253_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 08 decline streaks by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _zscore_rolling(base, 63)

def dstk_254_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 08 decline streaks by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _zscore_rolling(base, 126)

def dstk_255_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 08 decline streaks by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _zscore_rolling(base, 252)

def dstk_256_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 08 decline streaks to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rank_pct(base, 5)

def dstk_257_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 08 decline streaks to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rank_pct(base, 21)

def dstk_258_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 08 decline streaks to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rank_pct(base, 63)

def dstk_259_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 08 decline streaks to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rank_pct(base, 126)

def dstk_260_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 08 decline streaks to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rank_pct(base, 252)

def dstk_261_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 08 decline streaks distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_skew(base, 5)

def dstk_262_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 08 decline streaks distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_skew(base, 21)

def dstk_263_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 08 decline streaks distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_skew(base, 63)

def dstk_264_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 08 decline streaks distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_skew(base, 126)

def dstk_265_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 08 decline streaks distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_skew(base, 252)

def dstk_266_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 08 decline streaks over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_kurt(base, 5)

def dstk_267_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 08 decline streaks over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_kurt(base, 21)

def dstk_268_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 08 decline streaks over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_kurt(base, 63)

def dstk_269_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 08 decline streaks over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_kurt(base, 126)

def dstk_270_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 08 decline streaks over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _rolling_kurt(base, 252)

def dstk_271_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 08 decline streaks for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _safe_div(base, _rolling_std(base, 5))

def dstk_272_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 08 decline streaks for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _safe_div(base, _rolling_std(base, 21))

def dstk_273_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 08 decline streaks for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _safe_div(base, _rolling_std(base, 63))

def dstk_274_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 08 decline streaks for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _safe_div(base, _rolling_std(base, 126))

def dstk_275_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 08 decline streaks for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return _safe_div(base, _rolling_std(base, 252))

def dstk_276_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 08 decline streaks over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dstk_277_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 08 decline streaks over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dstk_278_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 08 decline streaks over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dstk_279_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 08 decline streaks over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dstk_280_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 08 decline streaks over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(8).rolling(40).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dstk_281_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 08 decline streaks over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_mean(base, 5)

def dstk_282_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 08 decline streaks over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_mean(base, 21)

def dstk_283_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 08 decline streaks over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_mean(base, 63)

def dstk_284_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 08 decline streaks over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_mean(base, 126)

def dstk_285_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 08 decline streaks over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_mean(base, 252)

def dstk_286_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 08 decline streaks by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _zscore_rolling(base, 5)

def dstk_287_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 08 decline streaks by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _zscore_rolling(base, 21)

def dstk_288_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 08 decline streaks by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _zscore_rolling(base, 63)

def dstk_289_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 08 decline streaks by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _zscore_rolling(base, 126)

def dstk_290_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 08 decline streaks by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _zscore_rolling(base, 252)

def dstk_291_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 08 decline streaks to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rank_pct(base, 5)

def dstk_292_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 08 decline streaks to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rank_pct(base, 21)

def dstk_293_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 08 decline streaks to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rank_pct(base, 63)

def dstk_294_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 08 decline streaks to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rank_pct(base, 126)

def dstk_295_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 08 decline streaks to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rank_pct(base, 252)

def dstk_296_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 08 decline streaks distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_skew(base, 5)

def dstk_297_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 08 decline streaks distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_skew(base, 21)

def dstk_298_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 08 decline streaks distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_skew(base, 63)

def dstk_299_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 08 decline streaks distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_skew(base, 126)

def dstk_300_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 08 decline streaks distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_skew(base, 252)
