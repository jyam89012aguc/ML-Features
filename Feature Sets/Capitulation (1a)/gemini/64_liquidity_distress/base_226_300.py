"""
64_64_liquidity_distress — Base Features 226-300
Domain: 64_liquidity_distress
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

def ldis_226_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 5d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(35)
    return _rolling_skew(base, 5)

def ldis_227_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 21d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(35)
    return _rolling_skew(base, 21)

def ldis_228_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 63d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(35)
    return _rolling_skew(base, 63)

def ldis_229_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 126d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(35)
    return _rolling_skew(base, 126)

def ldis_230_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 252d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(35)
    return _rolling_skew(base, 252)

def ldis_231_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 64 liquidity distress over 5d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(35)
    return _rolling_kurt(base, 5)

def ldis_232_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 64 liquidity distress over 21d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(35)
    return _rolling_kurt(base, 21)

def ldis_233_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 64 liquidity distress over 63d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(35)
    return _rolling_kurt(base, 63)

def ldis_234_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 64 liquidity distress over 126d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(35)
    return _rolling_kurt(base, 126)

def ldis_235_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 64 liquidity distress over 252d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(35)
    return _rolling_kurt(base, 252)

def ldis_236_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(35)
    return _safe_div(base, _rolling_std(base, 5))

def ldis_237_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(35)
    return _safe_div(base, _rolling_std(base, 21))

def ldis_238_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(35)
    return _safe_div(base, _rolling_std(base, 63))

def ldis_239_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(35)
    return _safe_div(base, _rolling_std(base, 126))

def ldis_240_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(35)
    return _safe_div(base, _rolling_std(base, 252))

def ldis_241_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 5d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(35)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ldis_242_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 21d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(35)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ldis_243_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 63d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(35)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ldis_244_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 126d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(35)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ldis_245_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 252d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(35)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ldis_246_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 64 liquidity distress over a 5d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(40)
    return _rolling_mean(base, 5)

def ldis_247_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 64 liquidity distress over a 21d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(40)
    return _rolling_mean(base, 21)

def ldis_248_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 64 liquidity distress over a 63d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(40)
    return _rolling_mean(base, 63)

def ldis_249_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 64 liquidity distress over a 126d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(40)
    return _rolling_mean(base, 126)

def ldis_250_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 64 liquidity distress over a 252d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(40)
    return _rolling_mean(base, 252)

def ldis_251_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 64 liquidity distress by measuring deviations from the 5d mean.
    """
    base = revenue.pct_change(40)
    return _zscore_rolling(base, 5)

def ldis_252_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 64 liquidity distress by measuring deviations from the 21d mean.
    """
    base = revenue.pct_change(40)
    return _zscore_rolling(base, 21)

def ldis_253_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 64 liquidity distress by measuring deviations from the 63d mean.
    """
    base = revenue.pct_change(40)
    return _zscore_rolling(base, 63)

def ldis_254_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 64 liquidity distress by measuring deviations from the 126d mean.
    """
    base = revenue.pct_change(40)
    return _zscore_rolling(base, 126)

def ldis_255_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 64 liquidity distress by measuring deviations from the 252d mean.
    """
    base = revenue.pct_change(40)
    return _zscore_rolling(base, 252)

def ldis_256_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(40)
    return _rank_pct(base, 5)

def ldis_257_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(40)
    return _rank_pct(base, 21)

def ldis_258_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(40)
    return _rank_pct(base, 63)

def ldis_259_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(40)
    return _rank_pct(base, 126)

def ldis_260_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(40)
    return _rank_pct(base, 252)

def ldis_261_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 5d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(40)
    return _rolling_skew(base, 5)

def ldis_262_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 21d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(40)
    return _rolling_skew(base, 21)

def ldis_263_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 63d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(40)
    return _rolling_skew(base, 63)

def ldis_264_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 126d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(40)
    return _rolling_skew(base, 126)

def ldis_265_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 252d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(40)
    return _rolling_skew(base, 252)

def ldis_266_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 64 liquidity distress over 5d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(40)
    return _rolling_kurt(base, 5)

def ldis_267_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 64 liquidity distress over 21d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(40)
    return _rolling_kurt(base, 21)

def ldis_268_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 64 liquidity distress over 63d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(40)
    return _rolling_kurt(base, 63)

def ldis_269_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 64 liquidity distress over 126d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(40)
    return _rolling_kurt(base, 126)

def ldis_270_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 64 liquidity distress over 252d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(40)
    return _rolling_kurt(base, 252)

def ldis_271_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(40)
    return _safe_div(base, _rolling_std(base, 5))

def ldis_272_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(40)
    return _safe_div(base, _rolling_std(base, 21))

def ldis_273_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(40)
    return _safe_div(base, _rolling_std(base, 63))

def ldis_274_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(40)
    return _safe_div(base, _rolling_std(base, 126))

def ldis_275_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(40)
    return _safe_div(base, _rolling_std(base, 252))

def ldis_276_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 5d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(40)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ldis_277_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 21d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(40)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ldis_278_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 63d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(40)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ldis_279_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 126d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(40)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ldis_280_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 252d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(40)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ldis_281_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 64 liquidity distress over a 5d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(45)
    return _rolling_mean(base, 5)

def ldis_282_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 64 liquidity distress over a 21d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(45)
    return _rolling_mean(base, 21)

def ldis_283_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 64 liquidity distress over a 63d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(45)
    return _rolling_mean(base, 63)

def ldis_284_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 64 liquidity distress over a 126d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(45)
    return _rolling_mean(base, 126)

def ldis_285_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 64 liquidity distress over a 252d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(45)
    return _rolling_mean(base, 252)

def ldis_286_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 64 liquidity distress by measuring deviations from the 5d mean.
    """
    base = revenue.pct_change(45)
    return _zscore_rolling(base, 5)

def ldis_287_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 64 liquidity distress by measuring deviations from the 21d mean.
    """
    base = revenue.pct_change(45)
    return _zscore_rolling(base, 21)

def ldis_288_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 64 liquidity distress by measuring deviations from the 63d mean.
    """
    base = revenue.pct_change(45)
    return _zscore_rolling(base, 63)

def ldis_289_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 64 liquidity distress by measuring deviations from the 126d mean.
    """
    base = revenue.pct_change(45)
    return _zscore_rolling(base, 126)

def ldis_290_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 64 liquidity distress by measuring deviations from the 252d mean.
    """
    base = revenue.pct_change(45)
    return _zscore_rolling(base, 252)

def ldis_291_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(45)
    return _rank_pct(base, 5)

def ldis_292_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(45)
    return _rank_pct(base, 21)

def ldis_293_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(45)
    return _rank_pct(base, 63)

def ldis_294_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(45)
    return _rank_pct(base, 126)

def ldis_295_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(45)
    return _rank_pct(base, 252)

def ldis_296_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 5d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(45)
    return _rolling_skew(base, 5)

def ldis_297_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 21d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(45)
    return _rolling_skew(base, 21)

def ldis_298_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 63d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(45)
    return _rolling_skew(base, 63)

def ldis_299_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 126d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(45)
    return _rolling_skew(base, 126)

def ldis_300_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 252d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(45)
    return _rolling_skew(base, 252)
