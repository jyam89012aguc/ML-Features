"""
114_114_overnight_intraday_split — Base Features 226-300
Domain: 114_overnight_intraday_split
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

def onid_226_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 5d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(7) - 1)
    return _rolling_skew(base, 5)

def onid_227_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 21d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(7) - 1)
    return _rolling_skew(base, 21)

def onid_228_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 63d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(7) - 1)
    return _rolling_skew(base, 63)

def onid_229_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 126d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(7) - 1)
    return _rolling_skew(base, 126)

def onid_230_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 252d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(7) - 1)
    return _rolling_skew(base, 252)

def onid_231_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 5d to capture explosive breakdown or reversal points.
    """
    base = (open / close.shift(7) - 1)
    return _rolling_kurt(base, 5)

def onid_232_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 21d to capture explosive breakdown or reversal points.
    """
    base = (open / close.shift(7) - 1)
    return _rolling_kurt(base, 21)

def onid_233_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 63d to capture explosive breakdown or reversal points.
    """
    base = (open / close.shift(7) - 1)
    return _rolling_kurt(base, 63)

def onid_234_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 126d to capture explosive breakdown or reversal points.
    """
    base = (open / close.shift(7) - 1)
    return _rolling_kurt(base, 126)

def onid_235_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 252d to capture explosive breakdown or reversal points.
    """
    base = (open / close.shift(7) - 1)
    return _rolling_kurt(base, 252)

def onid_236_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (open / close.shift(7) - 1)
    return _safe_div(base, _rolling_std(base, 5))

def onid_237_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (open / close.shift(7) - 1)
    return _safe_div(base, _rolling_std(base, 21))

def onid_238_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (open / close.shift(7) - 1)
    return _safe_div(base, _rolling_std(base, 63))

def onid_239_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (open / close.shift(7) - 1)
    return _safe_div(base, _rolling_std(base, 126))

def onid_240_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (open / close.shift(7) - 1)
    return _safe_div(base, _rolling_std(base, 252))

def onid_241_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 5d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(7) - 1)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def onid_242_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 21d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(7) - 1)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def onid_243_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 63d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(7) - 1)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def onid_244_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 126d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(7) - 1)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def onid_245_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 252d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(7) - 1)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def onid_246_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 5d horizon to identify extreme regimes.
    """
    base = (open / close.shift(8) - 1)
    return _rolling_mean(base, 5)

def onid_247_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 21d horizon to identify extreme regimes.
    """
    base = (open / close.shift(8) - 1)
    return _rolling_mean(base, 21)

def onid_248_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 63d horizon to identify extreme regimes.
    """
    base = (open / close.shift(8) - 1)
    return _rolling_mean(base, 63)

def onid_249_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 126d horizon to identify extreme regimes.
    """
    base = (open / close.shift(8) - 1)
    return _rolling_mean(base, 126)

def onid_250_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 252d horizon to identify extreme regimes.
    """
    base = (open / close.shift(8) - 1)
    return _rolling_mean(base, 252)

def onid_251_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 5d mean.
    """
    base = (open / close.shift(8) - 1)
    return _zscore_rolling(base, 5)

def onid_252_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 21d mean.
    """
    base = (open / close.shift(8) - 1)
    return _zscore_rolling(base, 21)

def onid_253_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 63d mean.
    """
    base = (open / close.shift(8) - 1)
    return _zscore_rolling(base, 63)

def onid_254_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 126d mean.
    """
    base = (open / close.shift(8) - 1)
    return _zscore_rolling(base, 126)

def onid_255_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 252d mean.
    """
    base = (open / close.shift(8) - 1)
    return _zscore_rolling(base, 252)

def onid_256_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (open / close.shift(8) - 1)
    return _rank_pct(base, 5)

def onid_257_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (open / close.shift(8) - 1)
    return _rank_pct(base, 21)

def onid_258_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (open / close.shift(8) - 1)
    return _rank_pct(base, 63)

def onid_259_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (open / close.shift(8) - 1)
    return _rank_pct(base, 126)

def onid_260_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (open / close.shift(8) - 1)
    return _rank_pct(base, 252)

def onid_261_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 5d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(8) - 1)
    return _rolling_skew(base, 5)

def onid_262_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 21d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(8) - 1)
    return _rolling_skew(base, 21)

def onid_263_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 63d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(8) - 1)
    return _rolling_skew(base, 63)

def onid_264_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 126d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(8) - 1)
    return _rolling_skew(base, 126)

def onid_265_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 252d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(8) - 1)
    return _rolling_skew(base, 252)

def onid_266_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 5d to capture explosive breakdown or reversal points.
    """
    base = (open / close.shift(8) - 1)
    return _rolling_kurt(base, 5)

def onid_267_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 21d to capture explosive breakdown or reversal points.
    """
    base = (open / close.shift(8) - 1)
    return _rolling_kurt(base, 21)

def onid_268_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 63d to capture explosive breakdown or reversal points.
    """
    base = (open / close.shift(8) - 1)
    return _rolling_kurt(base, 63)

def onid_269_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 126d to capture explosive breakdown or reversal points.
    """
    base = (open / close.shift(8) - 1)
    return _rolling_kurt(base, 126)

def onid_270_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 252d to capture explosive breakdown or reversal points.
    """
    base = (open / close.shift(8) - 1)
    return _rolling_kurt(base, 252)

def onid_271_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (open / close.shift(8) - 1)
    return _safe_div(base, _rolling_std(base, 5))

def onid_272_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (open / close.shift(8) - 1)
    return _safe_div(base, _rolling_std(base, 21))

def onid_273_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (open / close.shift(8) - 1)
    return _safe_div(base, _rolling_std(base, 63))

def onid_274_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (open / close.shift(8) - 1)
    return _safe_div(base, _rolling_std(base, 126))

def onid_275_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (open / close.shift(8) - 1)
    return _safe_div(base, _rolling_std(base, 252))

def onid_276_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 5d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(8) - 1)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def onid_277_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 21d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(8) - 1)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def onid_278_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 63d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(8) - 1)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def onid_279_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 126d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(8) - 1)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def onid_280_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 252d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(8) - 1)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def onid_281_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 5d horizon to identify extreme regimes.
    """
    base = (open / close.shift(9) - 1)
    return _rolling_mean(base, 5)

def onid_282_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 21d horizon to identify extreme regimes.
    """
    base = (open / close.shift(9) - 1)
    return _rolling_mean(base, 21)

def onid_283_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 63d horizon to identify extreme regimes.
    """
    base = (open / close.shift(9) - 1)
    return _rolling_mean(base, 63)

def onid_284_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 126d horizon to identify extreme regimes.
    """
    base = (open / close.shift(9) - 1)
    return _rolling_mean(base, 126)

def onid_285_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 252d horizon to identify extreme regimes.
    """
    base = (open / close.shift(9) - 1)
    return _rolling_mean(base, 252)

def onid_286_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 5d mean.
    """
    base = (open / close.shift(9) - 1)
    return _zscore_rolling(base, 5)

def onid_287_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 21d mean.
    """
    base = (open / close.shift(9) - 1)
    return _zscore_rolling(base, 21)

def onid_288_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 63d mean.
    """
    base = (open / close.shift(9) - 1)
    return _zscore_rolling(base, 63)

def onid_289_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 126d mean.
    """
    base = (open / close.shift(9) - 1)
    return _zscore_rolling(base, 126)

def onid_290_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 252d mean.
    """
    base = (open / close.shift(9) - 1)
    return _zscore_rolling(base, 252)

def onid_291_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (open / close.shift(9) - 1)
    return _rank_pct(base, 5)

def onid_292_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (open / close.shift(9) - 1)
    return _rank_pct(base, 21)

def onid_293_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (open / close.shift(9) - 1)
    return _rank_pct(base, 63)

def onid_294_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (open / close.shift(9) - 1)
    return _rank_pct(base, 126)

def onid_295_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (open / close.shift(9) - 1)
    return _rank_pct(base, 252)

def onid_296_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 5d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(9) - 1)
    return _rolling_skew(base, 5)

def onid_297_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 21d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(9) - 1)
    return _rolling_skew(base, 21)

def onid_298_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 63d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(9) - 1)
    return _rolling_skew(base, 63)

def onid_299_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 126d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(9) - 1)
    return _rolling_skew(base, 126)

def onid_300_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 252d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(9) - 1)
    return _rolling_skew(base, 252)
