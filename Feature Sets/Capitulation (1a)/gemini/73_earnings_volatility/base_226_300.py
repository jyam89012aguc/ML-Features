"""
73_73_earnings_volatility — Base Features 226-300
Domain: 73_earnings_volatility
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

def evolt_226_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 73 earnings volatility distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(35)
    return _rolling_skew(base, 5)

def evolt_227_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 73 earnings volatility distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(35)
    return _rolling_skew(base, 21)

def evolt_228_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 73 earnings volatility distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(35)
    return _rolling_skew(base, 63)

def evolt_229_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 73 earnings volatility distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(35)
    return _rolling_skew(base, 126)

def evolt_230_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 73 earnings volatility distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(35)
    return _rolling_skew(base, 252)

def evolt_231_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 73 earnings volatility over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(35)
    return _rolling_kurt(base, 5)

def evolt_232_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 73 earnings volatility over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(35)
    return _rolling_kurt(base, 21)

def evolt_233_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 73 earnings volatility over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(35)
    return _rolling_kurt(base, 63)

def evolt_234_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 73 earnings volatility over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(35)
    return _rolling_kurt(base, 126)

def evolt_235_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 73 earnings volatility over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(35)
    return _rolling_kurt(base, 252)

def evolt_236_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 73 earnings volatility for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(35)
    return _safe_div(base, _rolling_std(base, 5))

def evolt_237_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 73 earnings volatility for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(35)
    return _safe_div(base, _rolling_std(base, 21))

def evolt_238_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 73 earnings volatility for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(35)
    return _safe_div(base, _rolling_std(base, 63))

def evolt_239_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 73 earnings volatility for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(35)
    return _safe_div(base, _rolling_std(base, 126))

def evolt_240_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 73 earnings volatility for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(35)
    return _safe_div(base, _rolling_std(base, 252))

def evolt_241_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 73 earnings volatility over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(35)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def evolt_242_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 73 earnings volatility over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(35)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def evolt_243_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 73 earnings volatility over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(35)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def evolt_244_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 73 earnings volatility over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(35)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def evolt_245_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 73 earnings volatility over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(35)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def evolt_246_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 73 earnings volatility over a 5d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(40)
    return _rolling_mean(base, 5)

def evolt_247_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 73 earnings volatility over a 21d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(40)
    return _rolling_mean(base, 21)

def evolt_248_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 73 earnings volatility over a 63d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(40)
    return _rolling_mean(base, 63)

def evolt_249_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 73 earnings volatility over a 126d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(40)
    return _rolling_mean(base, 126)

def evolt_250_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 73 earnings volatility over a 252d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(40)
    return _rolling_mean(base, 252)

def evolt_251_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 73 earnings volatility by measuring deviations from the 5d mean.
    """
    base = marketcap.pct_change(40)
    return _zscore_rolling(base, 5)

def evolt_252_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 73 earnings volatility by measuring deviations from the 21d mean.
    """
    base = marketcap.pct_change(40)
    return _zscore_rolling(base, 21)

def evolt_253_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 73 earnings volatility by measuring deviations from the 63d mean.
    """
    base = marketcap.pct_change(40)
    return _zscore_rolling(base, 63)

def evolt_254_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 73 earnings volatility by measuring deviations from the 126d mean.
    """
    base = marketcap.pct_change(40)
    return _zscore_rolling(base, 126)

def evolt_255_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 73 earnings volatility by measuring deviations from the 252d mean.
    """
    base = marketcap.pct_change(40)
    return _zscore_rolling(base, 252)

def evolt_256_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 73 earnings volatility to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(40)
    return _rank_pct(base, 5)

def evolt_257_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 73 earnings volatility to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(40)
    return _rank_pct(base, 21)

def evolt_258_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 73 earnings volatility to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(40)
    return _rank_pct(base, 63)

def evolt_259_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 73 earnings volatility to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(40)
    return _rank_pct(base, 126)

def evolt_260_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 73 earnings volatility to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(40)
    return _rank_pct(base, 252)

def evolt_261_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 73 earnings volatility distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(40)
    return _rolling_skew(base, 5)

def evolt_262_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 73 earnings volatility distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(40)
    return _rolling_skew(base, 21)

def evolt_263_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 73 earnings volatility distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(40)
    return _rolling_skew(base, 63)

def evolt_264_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 73 earnings volatility distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(40)
    return _rolling_skew(base, 126)

def evolt_265_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 73 earnings volatility distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(40)
    return _rolling_skew(base, 252)

def evolt_266_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 73 earnings volatility over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(40)
    return _rolling_kurt(base, 5)

def evolt_267_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 73 earnings volatility over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(40)
    return _rolling_kurt(base, 21)

def evolt_268_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 73 earnings volatility over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(40)
    return _rolling_kurt(base, 63)

def evolt_269_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 73 earnings volatility over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(40)
    return _rolling_kurt(base, 126)

def evolt_270_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 73 earnings volatility over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(40)
    return _rolling_kurt(base, 252)

def evolt_271_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 73 earnings volatility for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(40)
    return _safe_div(base, _rolling_std(base, 5))

def evolt_272_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 73 earnings volatility for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(40)
    return _safe_div(base, _rolling_std(base, 21))

def evolt_273_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 73 earnings volatility for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(40)
    return _safe_div(base, _rolling_std(base, 63))

def evolt_274_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 73 earnings volatility for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(40)
    return _safe_div(base, _rolling_std(base, 126))

def evolt_275_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 73 earnings volatility for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(40)
    return _safe_div(base, _rolling_std(base, 252))

def evolt_276_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 73 earnings volatility over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(40)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def evolt_277_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 73 earnings volatility over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(40)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def evolt_278_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 73 earnings volatility over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(40)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def evolt_279_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 73 earnings volatility over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(40)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def evolt_280_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 73 earnings volatility over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(40)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def evolt_281_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 73 earnings volatility over a 5d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(45)
    return _rolling_mean(base, 5)

def evolt_282_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 73 earnings volatility over a 21d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(45)
    return _rolling_mean(base, 21)

def evolt_283_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 73 earnings volatility over a 63d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(45)
    return _rolling_mean(base, 63)

def evolt_284_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 73 earnings volatility over a 126d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(45)
    return _rolling_mean(base, 126)

def evolt_285_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 73 earnings volatility over a 252d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(45)
    return _rolling_mean(base, 252)

def evolt_286_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 73 earnings volatility by measuring deviations from the 5d mean.
    """
    base = marketcap.pct_change(45)
    return _zscore_rolling(base, 5)

def evolt_287_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 73 earnings volatility by measuring deviations from the 21d mean.
    """
    base = marketcap.pct_change(45)
    return _zscore_rolling(base, 21)

def evolt_288_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 73 earnings volatility by measuring deviations from the 63d mean.
    """
    base = marketcap.pct_change(45)
    return _zscore_rolling(base, 63)

def evolt_289_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 73 earnings volatility by measuring deviations from the 126d mean.
    """
    base = marketcap.pct_change(45)
    return _zscore_rolling(base, 126)

def evolt_290_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 73 earnings volatility by measuring deviations from the 252d mean.
    """
    base = marketcap.pct_change(45)
    return _zscore_rolling(base, 252)

def evolt_291_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 73 earnings volatility to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(45)
    return _rank_pct(base, 5)

def evolt_292_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 73 earnings volatility to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(45)
    return _rank_pct(base, 21)

def evolt_293_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 73 earnings volatility to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(45)
    return _rank_pct(base, 63)

def evolt_294_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 73 earnings volatility to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(45)
    return _rank_pct(base, 126)

def evolt_295_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 73 earnings volatility to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(45)
    return _rank_pct(base, 252)

def evolt_296_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 73 earnings volatility distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(45)
    return _rolling_skew(base, 5)

def evolt_297_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 73 earnings volatility distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(45)
    return _rolling_skew(base, 21)

def evolt_298_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 73 earnings volatility distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(45)
    return _rolling_skew(base, 63)

def evolt_299_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 73 earnings volatility distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(45)
    return _rolling_skew(base, 126)

def evolt_300_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 73 earnings volatility distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(45)
    return _rolling_skew(base, 252)
