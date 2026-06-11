"""
93_93_institutional_bottom_fish — Base Features 226-300
Domain: 93_institutional_bottom_fish
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

def ibf_226_skew_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 5d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_skew(base, 5)

def ibf_227_skew_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 21d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_skew(base, 21)

def ibf_228_skew_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 63d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_skew(base, 63)

def ibf_229_skew_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 126d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_skew(base, 126)

def ibf_230_skew_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 252d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_skew(base, 252)

def ibf_231_kurt_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 5d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_kurt(base, 5)

def ibf_232_kurt_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 21d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_kurt(base, 21)

def ibf_233_kurt_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 63d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_kurt(base, 63)

def ibf_234_kurt_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 126d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_kurt(base, 126)

def ibf_235_kurt_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 252d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_kurt(base, 252)

def ibf_236_voladj_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _safe_div(base, _rolling_std(base, 5))

def ibf_237_voladj_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _safe_div(base, _rolling_std(base, 21))

def ibf_238_voladj_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _safe_div(base, _rolling_std(base, 63))

def ibf_239_voladj_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _safe_div(base, _rolling_std(base, 126))

def ibf_240_voladj_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _safe_div(base, _rolling_std(base, 252))

def ibf_241_lognorm_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 5d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ibf_242_lognorm_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 21d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ibf_243_lognorm_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 63d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ibf_244_lognorm_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 126d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ibf_245_lognorm_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 252d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ibf_246_lvl_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 5d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rolling_mean(base, 5)

def ibf_247_lvl_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 21d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rolling_mean(base, 21)

def ibf_248_lvl_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 63d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rolling_mean(base, 63)

def ibf_249_lvl_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 126d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rolling_mean(base, 126)

def ibf_250_lvl_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 252d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rolling_mean(base, 252)

def ibf_251_zscore_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 5d mean.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _zscore_rolling(base, 5)

def ibf_252_zscore_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 21d mean.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _zscore_rolling(base, 21)

def ibf_253_zscore_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 63d mean.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _zscore_rolling(base, 63)

def ibf_254_zscore_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 126d mean.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _zscore_rolling(base, 126)

def ibf_255_zscore_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 252d mean.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _zscore_rolling(base, 252)

def ibf_256_rank_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rank_pct(base, 5)

def ibf_257_rank_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rank_pct(base, 21)

def ibf_258_rank_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rank_pct(base, 63)

def ibf_259_rank_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rank_pct(base, 126)

def ibf_260_rank_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rank_pct(base, 252)

def ibf_261_skew_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 5d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rolling_skew(base, 5)

def ibf_262_skew_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 21d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rolling_skew(base, 21)

def ibf_263_skew_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 63d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rolling_skew(base, 63)

def ibf_264_skew_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 126d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rolling_skew(base, 126)

def ibf_265_skew_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 252d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rolling_skew(base, 252)

def ibf_266_kurt_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 5d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rolling_kurt(base, 5)

def ibf_267_kurt_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 21d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rolling_kurt(base, 21)

def ibf_268_kurt_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 63d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rolling_kurt(base, 63)

def ibf_269_kurt_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 126d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rolling_kurt(base, 126)

def ibf_270_kurt_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 252d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rolling_kurt(base, 252)

def ibf_271_voladj_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _safe_div(base, _rolling_std(base, 5))

def ibf_272_voladj_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _safe_div(base, _rolling_std(base, 21))

def ibf_273_voladj_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _safe_div(base, _rolling_std(base, 63))

def ibf_274_voladj_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _safe_div(base, _rolling_std(base, 126))

def ibf_275_voladj_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _safe_div(base, _rolling_std(base, 252))

def ibf_276_lognorm_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 5d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ibf_277_lognorm_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 21d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ibf_278_lognorm_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 63d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ibf_279_lognorm_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 126d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ibf_280_lognorm_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 252d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ibf_281_lvl_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 5d horizon to identify extreme regimes.
    """
    base = holder_count.diff(21).abs()
    return _rolling_mean(base, 5)

def ibf_282_lvl_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 21d horizon to identify extreme regimes.
    """
    base = holder_count.diff(21).abs()
    return _rolling_mean(base, 21)

def ibf_283_lvl_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 63d horizon to identify extreme regimes.
    """
    base = holder_count.diff(21).abs()
    return _rolling_mean(base, 63)

def ibf_284_lvl_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 126d horizon to identify extreme regimes.
    """
    base = holder_count.diff(21).abs()
    return _rolling_mean(base, 126)

def ibf_285_lvl_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 252d horizon to identify extreme regimes.
    """
    base = holder_count.diff(21).abs()
    return _rolling_mean(base, 252)

def ibf_286_zscore_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 5d mean.
    """
    base = holder_count.diff(21).abs()
    return _zscore_rolling(base, 5)

def ibf_287_zscore_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 21d mean.
    """
    base = holder_count.diff(21).abs()
    return _zscore_rolling(base, 21)

def ibf_288_zscore_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 63d mean.
    """
    base = holder_count.diff(21).abs()
    return _zscore_rolling(base, 63)

def ibf_289_zscore_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 126d mean.
    """
    base = holder_count.diff(21).abs()
    return _zscore_rolling(base, 126)

def ibf_290_zscore_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 252d mean.
    """
    base = holder_count.diff(21).abs()
    return _zscore_rolling(base, 252)

def ibf_291_rank_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = holder_count.diff(21).abs()
    return _rank_pct(base, 5)

def ibf_292_rank_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = holder_count.diff(21).abs()
    return _rank_pct(base, 21)

def ibf_293_rank_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = holder_count.diff(21).abs()
    return _rank_pct(base, 63)

def ibf_294_rank_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = holder_count.diff(21).abs()
    return _rank_pct(base, 126)

def ibf_295_rank_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = holder_count.diff(21).abs()
    return _rank_pct(base, 252)

def ibf_296_skew_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 5d to detect tail risk or exhaustion.
    """
    base = holder_count.diff(21).abs()
    return _rolling_skew(base, 5)

def ibf_297_skew_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 21d to detect tail risk or exhaustion.
    """
    base = holder_count.diff(21).abs()
    return _rolling_skew(base, 21)

def ibf_298_skew_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 63d to detect tail risk or exhaustion.
    """
    base = holder_count.diff(21).abs()
    return _rolling_skew(base, 63)

def ibf_299_skew_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 126d to detect tail risk or exhaustion.
    """
    base = holder_count.diff(21).abs()
    return _rolling_skew(base, 126)

def ibf_300_skew_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 252d to detect tail risk or exhaustion.
    """
    base = holder_count.diff(21).abs()
    return _rolling_skew(base, 252)
