"""
76_76_balance_sheet_decay — Base Features 526-600
Domain: 76_balance_sheet_decay
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

def bdec_526_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 5d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(80)
    return _rolling_mean(base, 5)

def bdec_527_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 21d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(80)
    return _rolling_mean(base, 21)

def bdec_528_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 63d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(80)
    return _rolling_mean(base, 63)

def bdec_529_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 126d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(80)
    return _rolling_mean(base, 126)

def bdec_530_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 252d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(80)
    return _rolling_mean(base, 252)

def bdec_531_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 5d mean.
    """
    base = marketcap.pct_change(80)
    return _zscore_rolling(base, 5)

def bdec_532_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 21d mean.
    """
    base = marketcap.pct_change(80)
    return _zscore_rolling(base, 21)

def bdec_533_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 63d mean.
    """
    base = marketcap.pct_change(80)
    return _zscore_rolling(base, 63)

def bdec_534_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 126d mean.
    """
    base = marketcap.pct_change(80)
    return _zscore_rolling(base, 126)

def bdec_535_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 252d mean.
    """
    base = marketcap.pct_change(80)
    return _zscore_rolling(base, 252)

def bdec_536_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 76 balance sheet decay to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(80)
    return _rank_pct(base, 5)

def bdec_537_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 76 balance sheet decay to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(80)
    return _rank_pct(base, 21)

def bdec_538_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 76 balance sheet decay to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(80)
    return _rank_pct(base, 63)

def bdec_539_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 76 balance sheet decay to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(80)
    return _rank_pct(base, 126)

def bdec_540_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 76 balance sheet decay to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(80)
    return _rank_pct(base, 252)

def bdec_541_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 76 balance sheet decay distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(80)
    return _rolling_skew(base, 5)

def bdec_542_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 76 balance sheet decay distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(80)
    return _rolling_skew(base, 21)

def bdec_543_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 76 balance sheet decay distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(80)
    return _rolling_skew(base, 63)

def bdec_544_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 76 balance sheet decay distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(80)
    return _rolling_skew(base, 126)

def bdec_545_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 76 balance sheet decay distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(80)
    return _rolling_skew(base, 252)

def bdec_546_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 76 balance sheet decay over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(80)
    return _rolling_kurt(base, 5)

def bdec_547_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 76 balance sheet decay over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(80)
    return _rolling_kurt(base, 21)

def bdec_548_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 76 balance sheet decay over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(80)
    return _rolling_kurt(base, 63)

def bdec_549_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 76 balance sheet decay over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(80)
    return _rolling_kurt(base, 126)

def bdec_550_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 76 balance sheet decay over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(80)
    return _rolling_kurt(base, 252)

def bdec_551_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(80)
    return _safe_div(base, _rolling_std(base, 5))

def bdec_552_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(80)
    return _safe_div(base, _rolling_std(base, 21))

def bdec_553_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(80)
    return _safe_div(base, _rolling_std(base, 63))

def bdec_554_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(80)
    return _safe_div(base, _rolling_std(base, 126))

def bdec_555_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(80)
    return _safe_div(base, _rolling_std(base, 252))

def bdec_556_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 76 balance sheet decay over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(80)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def bdec_557_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 76 balance sheet decay over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(80)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def bdec_558_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 76 balance sheet decay over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(80)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def bdec_559_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 76 balance sheet decay over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(80)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def bdec_560_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 76 balance sheet decay over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(80)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def bdec_561_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 5d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(85)
    return _rolling_mean(base, 5)

def bdec_562_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 21d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(85)
    return _rolling_mean(base, 21)

def bdec_563_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 63d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(85)
    return _rolling_mean(base, 63)

def bdec_564_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 126d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(85)
    return _rolling_mean(base, 126)

def bdec_565_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 252d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(85)
    return _rolling_mean(base, 252)

def bdec_566_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 5d mean.
    """
    base = marketcap.pct_change(85)
    return _zscore_rolling(base, 5)

def bdec_567_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 21d mean.
    """
    base = marketcap.pct_change(85)
    return _zscore_rolling(base, 21)

def bdec_568_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 63d mean.
    """
    base = marketcap.pct_change(85)
    return _zscore_rolling(base, 63)

def bdec_569_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 126d mean.
    """
    base = marketcap.pct_change(85)
    return _zscore_rolling(base, 126)

def bdec_570_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 252d mean.
    """
    base = marketcap.pct_change(85)
    return _zscore_rolling(base, 252)

def bdec_571_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 76 balance sheet decay to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(85)
    return _rank_pct(base, 5)

def bdec_572_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 76 balance sheet decay to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(85)
    return _rank_pct(base, 21)

def bdec_573_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 76 balance sheet decay to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(85)
    return _rank_pct(base, 63)

def bdec_574_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 76 balance sheet decay to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(85)
    return _rank_pct(base, 126)

def bdec_575_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 76 balance sheet decay to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(85)
    return _rank_pct(base, 252)

def bdec_576_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 76 balance sheet decay distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(85)
    return _rolling_skew(base, 5)

def bdec_577_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 76 balance sheet decay distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(85)
    return _rolling_skew(base, 21)

def bdec_578_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 76 balance sheet decay distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(85)
    return _rolling_skew(base, 63)

def bdec_579_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 76 balance sheet decay distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(85)
    return _rolling_skew(base, 126)

def bdec_580_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 76 balance sheet decay distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(85)
    return _rolling_skew(base, 252)

def bdec_581_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 76 balance sheet decay over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(85)
    return _rolling_kurt(base, 5)

def bdec_582_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 76 balance sheet decay over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(85)
    return _rolling_kurt(base, 21)

def bdec_583_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 76 balance sheet decay over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(85)
    return _rolling_kurt(base, 63)

def bdec_584_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 76 balance sheet decay over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(85)
    return _rolling_kurt(base, 126)

def bdec_585_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 76 balance sheet decay over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(85)
    return _rolling_kurt(base, 252)

def bdec_586_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(85)
    return _safe_div(base, _rolling_std(base, 5))

def bdec_587_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(85)
    return _safe_div(base, _rolling_std(base, 21))

def bdec_588_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(85)
    return _safe_div(base, _rolling_std(base, 63))

def bdec_589_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(85)
    return _safe_div(base, _rolling_std(base, 126))

def bdec_590_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(85)
    return _safe_div(base, _rolling_std(base, 252))

def bdec_591_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 76 balance sheet decay over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(85)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def bdec_592_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 76 balance sheet decay over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(85)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def bdec_593_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 76 balance sheet decay over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(85)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def bdec_594_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 76 balance sheet decay over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(85)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def bdec_595_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 76 balance sheet decay over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(85)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def bdec_596_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 5d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(90)
    return _rolling_mean(base, 5)

def bdec_597_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 21d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(90)
    return _rolling_mean(base, 21)

def bdec_598_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 63d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(90)
    return _rolling_mean(base, 63)

def bdec_599_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 126d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(90)
    return _rolling_mean(base, 126)

def bdec_600_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 252d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(90)
    return _rolling_mean(base, 252)
