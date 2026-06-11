"""
62_62_margin_compression — Base Features 526-600
Domain: 62_margin_compression
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

def mcmp_526_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 62 margin compression over a 5d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(80)
    return _rolling_mean(base, 5)

def mcmp_527_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 62 margin compression over a 21d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(80)
    return _rolling_mean(base, 21)

def mcmp_528_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 62 margin compression over a 63d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(80)
    return _rolling_mean(base, 63)

def mcmp_529_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 62 margin compression over a 126d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(80)
    return _rolling_mean(base, 126)

def mcmp_530_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 62 margin compression over a 252d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(80)
    return _rolling_mean(base, 252)

def mcmp_531_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 62 margin compression by measuring deviations from the 5d mean.
    """
    base = revenue.pct_change(80)
    return _zscore_rolling(base, 5)

def mcmp_532_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 62 margin compression by measuring deviations from the 21d mean.
    """
    base = revenue.pct_change(80)
    return _zscore_rolling(base, 21)

def mcmp_533_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 62 margin compression by measuring deviations from the 63d mean.
    """
    base = revenue.pct_change(80)
    return _zscore_rolling(base, 63)

def mcmp_534_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 62 margin compression by measuring deviations from the 126d mean.
    """
    base = revenue.pct_change(80)
    return _zscore_rolling(base, 126)

def mcmp_535_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 62 margin compression by measuring deviations from the 252d mean.
    """
    base = revenue.pct_change(80)
    return _zscore_rolling(base, 252)

def mcmp_536_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 62 margin compression to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(80)
    return _rank_pct(base, 5)

def mcmp_537_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 62 margin compression to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(80)
    return _rank_pct(base, 21)

def mcmp_538_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 62 margin compression to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(80)
    return _rank_pct(base, 63)

def mcmp_539_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 62 margin compression to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(80)
    return _rank_pct(base, 126)

def mcmp_540_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 62 margin compression to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(80)
    return _rank_pct(base, 252)

def mcmp_541_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 62 margin compression distribution over 5d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(80)
    return _rolling_skew(base, 5)

def mcmp_542_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 62 margin compression distribution over 21d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(80)
    return _rolling_skew(base, 21)

def mcmp_543_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 62 margin compression distribution over 63d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(80)
    return _rolling_skew(base, 63)

def mcmp_544_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 62 margin compression distribution over 126d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(80)
    return _rolling_skew(base, 126)

def mcmp_545_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 62 margin compression distribution over 252d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(80)
    return _rolling_skew(base, 252)

def mcmp_546_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 62 margin compression over 5d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(80)
    return _rolling_kurt(base, 5)

def mcmp_547_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 62 margin compression over 21d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(80)
    return _rolling_kurt(base, 21)

def mcmp_548_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 62 margin compression over 63d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(80)
    return _rolling_kurt(base, 63)

def mcmp_549_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 62 margin compression over 126d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(80)
    return _rolling_kurt(base, 126)

def mcmp_550_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 62 margin compression over 252d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(80)
    return _rolling_kurt(base, 252)

def mcmp_551_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 62 margin compression for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(80)
    return _safe_div(base, _rolling_std(base, 5))

def mcmp_552_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 62 margin compression for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(80)
    return _safe_div(base, _rolling_std(base, 21))

def mcmp_553_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 62 margin compression for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(80)
    return _safe_div(base, _rolling_std(base, 63))

def mcmp_554_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 62 margin compression for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(80)
    return _safe_div(base, _rolling_std(base, 126))

def mcmp_555_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 62 margin compression for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(80)
    return _safe_div(base, _rolling_std(base, 252))

def mcmp_556_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 62 margin compression over 5d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(80)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def mcmp_557_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 62 margin compression over 21d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(80)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def mcmp_558_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 62 margin compression over 63d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(80)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def mcmp_559_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 62 margin compression over 126d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(80)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def mcmp_560_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 62 margin compression over 252d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(80)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def mcmp_561_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 62 margin compression over a 5d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(85)
    return _rolling_mean(base, 5)

def mcmp_562_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 62 margin compression over a 21d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(85)
    return _rolling_mean(base, 21)

def mcmp_563_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 62 margin compression over a 63d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(85)
    return _rolling_mean(base, 63)

def mcmp_564_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 62 margin compression over a 126d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(85)
    return _rolling_mean(base, 126)

def mcmp_565_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 62 margin compression over a 252d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(85)
    return _rolling_mean(base, 252)

def mcmp_566_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 62 margin compression by measuring deviations from the 5d mean.
    """
    base = revenue.pct_change(85)
    return _zscore_rolling(base, 5)

def mcmp_567_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 62 margin compression by measuring deviations from the 21d mean.
    """
    base = revenue.pct_change(85)
    return _zscore_rolling(base, 21)

def mcmp_568_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 62 margin compression by measuring deviations from the 63d mean.
    """
    base = revenue.pct_change(85)
    return _zscore_rolling(base, 63)

def mcmp_569_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 62 margin compression by measuring deviations from the 126d mean.
    """
    base = revenue.pct_change(85)
    return _zscore_rolling(base, 126)

def mcmp_570_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 62 margin compression by measuring deviations from the 252d mean.
    """
    base = revenue.pct_change(85)
    return _zscore_rolling(base, 252)

def mcmp_571_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 62 margin compression to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(85)
    return _rank_pct(base, 5)

def mcmp_572_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 62 margin compression to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(85)
    return _rank_pct(base, 21)

def mcmp_573_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 62 margin compression to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(85)
    return _rank_pct(base, 63)

def mcmp_574_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 62 margin compression to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(85)
    return _rank_pct(base, 126)

def mcmp_575_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 62 margin compression to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(85)
    return _rank_pct(base, 252)

def mcmp_576_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 62 margin compression distribution over 5d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(85)
    return _rolling_skew(base, 5)

def mcmp_577_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 62 margin compression distribution over 21d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(85)
    return _rolling_skew(base, 21)

def mcmp_578_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 62 margin compression distribution over 63d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(85)
    return _rolling_skew(base, 63)

def mcmp_579_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 62 margin compression distribution over 126d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(85)
    return _rolling_skew(base, 126)

def mcmp_580_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 62 margin compression distribution over 252d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(85)
    return _rolling_skew(base, 252)

def mcmp_581_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 62 margin compression over 5d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(85)
    return _rolling_kurt(base, 5)

def mcmp_582_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 62 margin compression over 21d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(85)
    return _rolling_kurt(base, 21)

def mcmp_583_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 62 margin compression over 63d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(85)
    return _rolling_kurt(base, 63)

def mcmp_584_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 62 margin compression over 126d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(85)
    return _rolling_kurt(base, 126)

def mcmp_585_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 62 margin compression over 252d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(85)
    return _rolling_kurt(base, 252)

def mcmp_586_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 62 margin compression for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(85)
    return _safe_div(base, _rolling_std(base, 5))

def mcmp_587_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 62 margin compression for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(85)
    return _safe_div(base, _rolling_std(base, 21))

def mcmp_588_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 62 margin compression for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(85)
    return _safe_div(base, _rolling_std(base, 63))

def mcmp_589_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 62 margin compression for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(85)
    return _safe_div(base, _rolling_std(base, 126))

def mcmp_590_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 62 margin compression for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(85)
    return _safe_div(base, _rolling_std(base, 252))

def mcmp_591_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 62 margin compression over 5d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(85)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def mcmp_592_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 62 margin compression over 21d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(85)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def mcmp_593_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 62 margin compression over 63d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(85)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def mcmp_594_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 62 margin compression over 126d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(85)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def mcmp_595_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 62 margin compression over 252d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(85)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def mcmp_596_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 62 margin compression over a 5d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(90)
    return _rolling_mean(base, 5)

def mcmp_597_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 62 margin compression over a 21d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(90)
    return _rolling_mean(base, 21)

def mcmp_598_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 62 margin compression over a 63d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(90)
    return _rolling_mean(base, 63)

def mcmp_599_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 62 margin compression over a 126d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(90)
    return _rolling_mean(base, 126)

def mcmp_600_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 62 margin compression over a 252d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(90)
    return _rolling_mean(base, 252)
