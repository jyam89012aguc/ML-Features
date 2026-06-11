"""
91_91_institutional_exit — Base Features 526-600
Domain: 91_institutional_exit
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

def iext_526_lvl_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 91 institutional exit over a 5d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_mean(base, 5)

def iext_527_lvl_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 91 institutional exit over a 21d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_mean(base, 21)

def iext_528_lvl_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 91 institutional exit over a 63d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_mean(base, 63)

def iext_529_lvl_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 91 institutional exit over a 126d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_mean(base, 126)

def iext_530_lvl_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 91 institutional exit over a 252d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_mean(base, 252)

def iext_531_zscore_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 91 institutional exit by measuring deviations from the 5d mean.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _zscore_rolling(base, 5)

def iext_532_zscore_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 91 institutional exit by measuring deviations from the 21d mean.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _zscore_rolling(base, 21)

def iext_533_zscore_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 91 institutional exit by measuring deviations from the 63d mean.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _zscore_rolling(base, 63)

def iext_534_zscore_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 91 institutional exit by measuring deviations from the 126d mean.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _zscore_rolling(base, 126)

def iext_535_zscore_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 91 institutional exit by measuring deviations from the 252d mean.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _zscore_rolling(base, 252)

def iext_536_rank_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 91 institutional exit to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rank_pct(base, 5)

def iext_537_rank_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 91 institutional exit to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rank_pct(base, 21)

def iext_538_rank_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 91 institutional exit to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rank_pct(base, 63)

def iext_539_rank_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 91 institutional exit to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rank_pct(base, 126)

def iext_540_rank_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 91 institutional exit to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rank_pct(base, 252)

def iext_541_skew_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 91 institutional exit distribution over 5d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_skew(base, 5)

def iext_542_skew_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 91 institutional exit distribution over 21d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_skew(base, 21)

def iext_543_skew_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 91 institutional exit distribution over 63d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_skew(base, 63)

def iext_544_skew_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 91 institutional exit distribution over 126d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_skew(base, 126)

def iext_545_skew_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 91 institutional exit distribution over 252d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_skew(base, 252)

def iext_546_kurt_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 91 institutional exit over 5d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_kurt(base, 5)

def iext_547_kurt_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 91 institutional exit over 21d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_kurt(base, 21)

def iext_548_kurt_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 91 institutional exit over 63d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_kurt(base, 63)

def iext_549_kurt_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 91 institutional exit over 126d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_kurt(base, 126)

def iext_550_kurt_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 91 institutional exit over 252d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_kurt(base, 252)

def iext_551_voladj_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 91 institutional exit for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _safe_div(base, _rolling_std(base, 5))

def iext_552_voladj_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 91 institutional exit for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _safe_div(base, _rolling_std(base, 21))

def iext_553_voladj_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 91 institutional exit for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _safe_div(base, _rolling_std(base, 63))

def iext_554_voladj_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 91 institutional exit for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _safe_div(base, _rolling_std(base, 126))

def iext_555_voladj_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 91 institutional exit for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _safe_div(base, _rolling_std(base, 252))

def iext_556_lognorm_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 91 institutional exit over 5d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def iext_557_lognorm_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 91 institutional exit over 21d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def iext_558_lognorm_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 91 institutional exit over 63d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def iext_559_lognorm_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 91 institutional exit over 126d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def iext_560_lognorm_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 91 institutional exit over 252d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def iext_561_lvl_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 91 institutional exit over a 5d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_mean(base, 5)

def iext_562_lvl_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 91 institutional exit over a 21d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_mean(base, 21)

def iext_563_lvl_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 91 institutional exit over a 63d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_mean(base, 63)

def iext_564_lvl_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 91 institutional exit over a 126d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_mean(base, 126)

def iext_565_lvl_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 91 institutional exit over a 252d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_mean(base, 252)

def iext_566_zscore_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 91 institutional exit by measuring deviations from the 5d mean.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _zscore_rolling(base, 5)

def iext_567_zscore_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 91 institutional exit by measuring deviations from the 21d mean.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _zscore_rolling(base, 21)

def iext_568_zscore_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 91 institutional exit by measuring deviations from the 63d mean.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _zscore_rolling(base, 63)

def iext_569_zscore_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 91 institutional exit by measuring deviations from the 126d mean.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _zscore_rolling(base, 126)

def iext_570_zscore_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 91 institutional exit by measuring deviations from the 252d mean.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _zscore_rolling(base, 252)

def iext_571_rank_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 91 institutional exit to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rank_pct(base, 5)

def iext_572_rank_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 91 institutional exit to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rank_pct(base, 21)

def iext_573_rank_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 91 institutional exit to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rank_pct(base, 63)

def iext_574_rank_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 91 institutional exit to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rank_pct(base, 126)

def iext_575_rank_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 91 institutional exit to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rank_pct(base, 252)

def iext_576_skew_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 91 institutional exit distribution over 5d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_skew(base, 5)

def iext_577_skew_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 91 institutional exit distribution over 21d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_skew(base, 21)

def iext_578_skew_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 91 institutional exit distribution over 63d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_skew(base, 63)

def iext_579_skew_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 91 institutional exit distribution over 126d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_skew(base, 126)

def iext_580_skew_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 91 institutional exit distribution over 252d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_skew(base, 252)

def iext_581_kurt_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 91 institutional exit over 5d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_kurt(base, 5)

def iext_582_kurt_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 91 institutional exit over 21d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_kurt(base, 21)

def iext_583_kurt_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 91 institutional exit over 63d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_kurt(base, 63)

def iext_584_kurt_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 91 institutional exit over 126d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_kurt(base, 126)

def iext_585_kurt_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 91 institutional exit over 252d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_kurt(base, 252)

def iext_586_voladj_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 91 institutional exit for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _safe_div(base, _rolling_std(base, 5))

def iext_587_voladj_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 91 institutional exit for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _safe_div(base, _rolling_std(base, 21))

def iext_588_voladj_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 91 institutional exit for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _safe_div(base, _rolling_std(base, 63))

def iext_589_voladj_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 91 institutional exit for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _safe_div(base, _rolling_std(base, 126))

def iext_590_voladj_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 91 institutional exit for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _safe_div(base, _rolling_std(base, 252))

def iext_591_lognorm_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 91 institutional exit over 5d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def iext_592_lognorm_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 91 institutional exit over 21d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def iext_593_lognorm_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 91 institutional exit over 63d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def iext_594_lognorm_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 91 institutional exit over 126d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def iext_595_lognorm_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 91 institutional exit over 252d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def iext_596_lvl_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 91 institutional exit over a 5d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rolling_mean(base, 5)

def iext_597_lvl_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 91 institutional exit over a 21d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rolling_mean(base, 21)

def iext_598_lvl_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 91 institutional exit over a 63d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rolling_mean(base, 63)

def iext_599_lvl_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 91 institutional exit over a 126d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rolling_mean(base, 126)

def iext_600_lvl_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 91 institutional exit over a 252d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rolling_mean(base, 252)
