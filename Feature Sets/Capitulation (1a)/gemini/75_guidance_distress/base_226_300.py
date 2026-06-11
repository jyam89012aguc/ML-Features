"""
75_75_guidance_distress — Base Features 226-300
Domain: 75_guidance_distress
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

def guid_226_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 75 guidance distress distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(35)
    return _rolling_skew(base, 5)

def guid_227_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 75 guidance distress distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(35)
    return _rolling_skew(base, 21)

def guid_228_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 75 guidance distress distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(35)
    return _rolling_skew(base, 63)

def guid_229_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 75 guidance distress distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(35)
    return _rolling_skew(base, 126)

def guid_230_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 75 guidance distress distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(35)
    return _rolling_skew(base, 252)

def guid_231_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 75 guidance distress over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(35)
    return _rolling_kurt(base, 5)

def guid_232_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 75 guidance distress over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(35)
    return _rolling_kurt(base, 21)

def guid_233_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 75 guidance distress over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(35)
    return _rolling_kurt(base, 63)

def guid_234_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 75 guidance distress over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(35)
    return _rolling_kurt(base, 126)

def guid_235_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 75 guidance distress over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(35)
    return _rolling_kurt(base, 252)

def guid_236_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 75 guidance distress for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(35)
    return _safe_div(base, _rolling_std(base, 5))

def guid_237_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 75 guidance distress for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(35)
    return _safe_div(base, _rolling_std(base, 21))

def guid_238_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 75 guidance distress for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(35)
    return _safe_div(base, _rolling_std(base, 63))

def guid_239_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 75 guidance distress for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(35)
    return _safe_div(base, _rolling_std(base, 126))

def guid_240_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 75 guidance distress for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(35)
    return _safe_div(base, _rolling_std(base, 252))

def guid_241_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 75 guidance distress over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(35)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def guid_242_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 75 guidance distress over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(35)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def guid_243_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 75 guidance distress over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(35)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def guid_244_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 75 guidance distress over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(35)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def guid_245_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 75 guidance distress over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(35)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def guid_246_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 75 guidance distress over a 5d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(40)
    return _rolling_mean(base, 5)

def guid_247_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 75 guidance distress over a 21d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(40)
    return _rolling_mean(base, 21)

def guid_248_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 75 guidance distress over a 63d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(40)
    return _rolling_mean(base, 63)

def guid_249_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 75 guidance distress over a 126d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(40)
    return _rolling_mean(base, 126)

def guid_250_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 75 guidance distress over a 252d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(40)
    return _rolling_mean(base, 252)

def guid_251_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 75 guidance distress by measuring deviations from the 5d mean.
    """
    base = marketcap.pct_change(40)
    return _zscore_rolling(base, 5)

def guid_252_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 75 guidance distress by measuring deviations from the 21d mean.
    """
    base = marketcap.pct_change(40)
    return _zscore_rolling(base, 21)

def guid_253_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 75 guidance distress by measuring deviations from the 63d mean.
    """
    base = marketcap.pct_change(40)
    return _zscore_rolling(base, 63)

def guid_254_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 75 guidance distress by measuring deviations from the 126d mean.
    """
    base = marketcap.pct_change(40)
    return _zscore_rolling(base, 126)

def guid_255_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 75 guidance distress by measuring deviations from the 252d mean.
    """
    base = marketcap.pct_change(40)
    return _zscore_rolling(base, 252)

def guid_256_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 75 guidance distress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(40)
    return _rank_pct(base, 5)

def guid_257_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 75 guidance distress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(40)
    return _rank_pct(base, 21)

def guid_258_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 75 guidance distress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(40)
    return _rank_pct(base, 63)

def guid_259_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 75 guidance distress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(40)
    return _rank_pct(base, 126)

def guid_260_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 75 guidance distress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(40)
    return _rank_pct(base, 252)

def guid_261_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 75 guidance distress distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(40)
    return _rolling_skew(base, 5)

def guid_262_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 75 guidance distress distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(40)
    return _rolling_skew(base, 21)

def guid_263_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 75 guidance distress distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(40)
    return _rolling_skew(base, 63)

def guid_264_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 75 guidance distress distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(40)
    return _rolling_skew(base, 126)

def guid_265_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 75 guidance distress distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(40)
    return _rolling_skew(base, 252)

def guid_266_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 75 guidance distress over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(40)
    return _rolling_kurt(base, 5)

def guid_267_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 75 guidance distress over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(40)
    return _rolling_kurt(base, 21)

def guid_268_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 75 guidance distress over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(40)
    return _rolling_kurt(base, 63)

def guid_269_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 75 guidance distress over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(40)
    return _rolling_kurt(base, 126)

def guid_270_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 75 guidance distress over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(40)
    return _rolling_kurt(base, 252)

def guid_271_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 75 guidance distress for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(40)
    return _safe_div(base, _rolling_std(base, 5))

def guid_272_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 75 guidance distress for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(40)
    return _safe_div(base, _rolling_std(base, 21))

def guid_273_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 75 guidance distress for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(40)
    return _safe_div(base, _rolling_std(base, 63))

def guid_274_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 75 guidance distress for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(40)
    return _safe_div(base, _rolling_std(base, 126))

def guid_275_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 75 guidance distress for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(40)
    return _safe_div(base, _rolling_std(base, 252))

def guid_276_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 75 guidance distress over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(40)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def guid_277_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 75 guidance distress over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(40)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def guid_278_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 75 guidance distress over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(40)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def guid_279_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 75 guidance distress over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(40)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def guid_280_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 75 guidance distress over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(40)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def guid_281_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 75 guidance distress over a 5d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(45)
    return _rolling_mean(base, 5)

def guid_282_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 75 guidance distress over a 21d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(45)
    return _rolling_mean(base, 21)

def guid_283_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 75 guidance distress over a 63d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(45)
    return _rolling_mean(base, 63)

def guid_284_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 75 guidance distress over a 126d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(45)
    return _rolling_mean(base, 126)

def guid_285_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 75 guidance distress over a 252d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(45)
    return _rolling_mean(base, 252)

def guid_286_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 75 guidance distress by measuring deviations from the 5d mean.
    """
    base = marketcap.pct_change(45)
    return _zscore_rolling(base, 5)

def guid_287_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 75 guidance distress by measuring deviations from the 21d mean.
    """
    base = marketcap.pct_change(45)
    return _zscore_rolling(base, 21)

def guid_288_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 75 guidance distress by measuring deviations from the 63d mean.
    """
    base = marketcap.pct_change(45)
    return _zscore_rolling(base, 63)

def guid_289_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 75 guidance distress by measuring deviations from the 126d mean.
    """
    base = marketcap.pct_change(45)
    return _zscore_rolling(base, 126)

def guid_290_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 75 guidance distress by measuring deviations from the 252d mean.
    """
    base = marketcap.pct_change(45)
    return _zscore_rolling(base, 252)

def guid_291_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 75 guidance distress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(45)
    return _rank_pct(base, 5)

def guid_292_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 75 guidance distress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(45)
    return _rank_pct(base, 21)

def guid_293_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 75 guidance distress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(45)
    return _rank_pct(base, 63)

def guid_294_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 75 guidance distress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(45)
    return _rank_pct(base, 126)

def guid_295_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 75 guidance distress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(45)
    return _rank_pct(base, 252)

def guid_296_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 75 guidance distress distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(45)
    return _rolling_skew(base, 5)

def guid_297_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 75 guidance distress distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(45)
    return _rolling_skew(base, 21)

def guid_298_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 75 guidance distress distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(45)
    return _rolling_skew(base, 63)

def guid_299_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 75 guidance distress distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(45)
    return _rolling_skew(base, 126)

def guid_300_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 75 guidance distress distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(45)
    return _rolling_skew(base, 252)
