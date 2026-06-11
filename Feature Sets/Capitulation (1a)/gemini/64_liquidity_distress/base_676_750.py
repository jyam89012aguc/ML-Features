"""
64_64_liquidity_distress — Base Features 676-750
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

def ldis_676_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(100)
    return _rank_pct(base, 5)

def ldis_677_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(100)
    return _rank_pct(base, 21)

def ldis_678_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(100)
    return _rank_pct(base, 63)

def ldis_679_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(100)
    return _rank_pct(base, 126)

def ldis_680_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(100)
    return _rank_pct(base, 252)

def ldis_681_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 5d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(100)
    return _rolling_skew(base, 5)

def ldis_682_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 21d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(100)
    return _rolling_skew(base, 21)

def ldis_683_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 63d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(100)
    return _rolling_skew(base, 63)

def ldis_684_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 126d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(100)
    return _rolling_skew(base, 126)

def ldis_685_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 252d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(100)
    return _rolling_skew(base, 252)

def ldis_686_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 64 liquidity distress over 5d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(100)
    return _rolling_kurt(base, 5)

def ldis_687_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 64 liquidity distress over 21d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(100)
    return _rolling_kurt(base, 21)

def ldis_688_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 64 liquidity distress over 63d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(100)
    return _rolling_kurt(base, 63)

def ldis_689_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 64 liquidity distress over 126d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(100)
    return _rolling_kurt(base, 126)

def ldis_690_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 64 liquidity distress over 252d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(100)
    return _rolling_kurt(base, 252)

def ldis_691_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(100)
    return _safe_div(base, _rolling_std(base, 5))

def ldis_692_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(100)
    return _safe_div(base, _rolling_std(base, 21))

def ldis_693_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(100)
    return _safe_div(base, _rolling_std(base, 63))

def ldis_694_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(100)
    return _safe_div(base, _rolling_std(base, 126))

def ldis_695_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(100)
    return _safe_div(base, _rolling_std(base, 252))

def ldis_696_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 5d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(100)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ldis_697_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 21d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(100)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ldis_698_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 63d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(100)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ldis_699_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 126d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(100)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ldis_700_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 252d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(100)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ldis_701_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 64 liquidity distress over a 5d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(105)
    return _rolling_mean(base, 5)

def ldis_702_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 64 liquidity distress over a 21d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(105)
    return _rolling_mean(base, 21)

def ldis_703_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 64 liquidity distress over a 63d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(105)
    return _rolling_mean(base, 63)

def ldis_704_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 64 liquidity distress over a 126d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(105)
    return _rolling_mean(base, 126)

def ldis_705_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 64 liquidity distress over a 252d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(105)
    return _rolling_mean(base, 252)

def ldis_706_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 64 liquidity distress by measuring deviations from the 5d mean.
    """
    base = revenue.pct_change(105)
    return _zscore_rolling(base, 5)

def ldis_707_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 64 liquidity distress by measuring deviations from the 21d mean.
    """
    base = revenue.pct_change(105)
    return _zscore_rolling(base, 21)

def ldis_708_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 64 liquidity distress by measuring deviations from the 63d mean.
    """
    base = revenue.pct_change(105)
    return _zscore_rolling(base, 63)

def ldis_709_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 64 liquidity distress by measuring deviations from the 126d mean.
    """
    base = revenue.pct_change(105)
    return _zscore_rolling(base, 126)

def ldis_710_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 64 liquidity distress by measuring deviations from the 252d mean.
    """
    base = revenue.pct_change(105)
    return _zscore_rolling(base, 252)

def ldis_711_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(105)
    return _rank_pct(base, 5)

def ldis_712_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(105)
    return _rank_pct(base, 21)

def ldis_713_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(105)
    return _rank_pct(base, 63)

def ldis_714_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(105)
    return _rank_pct(base, 126)

def ldis_715_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(105)
    return _rank_pct(base, 252)

def ldis_716_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 5d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(105)
    return _rolling_skew(base, 5)

def ldis_717_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 21d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(105)
    return _rolling_skew(base, 21)

def ldis_718_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 63d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(105)
    return _rolling_skew(base, 63)

def ldis_719_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 126d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(105)
    return _rolling_skew(base, 126)

def ldis_720_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 252d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(105)
    return _rolling_skew(base, 252)

def ldis_721_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 64 liquidity distress over 5d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(105)
    return _rolling_kurt(base, 5)

def ldis_722_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 64 liquidity distress over 21d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(105)
    return _rolling_kurt(base, 21)

def ldis_723_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 64 liquidity distress over 63d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(105)
    return _rolling_kurt(base, 63)

def ldis_724_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 64 liquidity distress over 126d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(105)
    return _rolling_kurt(base, 126)

def ldis_725_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 64 liquidity distress over 252d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(105)
    return _rolling_kurt(base, 252)

def ldis_726_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(105)
    return _safe_div(base, _rolling_std(base, 5))

def ldis_727_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(105)
    return _safe_div(base, _rolling_std(base, 21))

def ldis_728_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(105)
    return _safe_div(base, _rolling_std(base, 63))

def ldis_729_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(105)
    return _safe_div(base, _rolling_std(base, 126))

def ldis_730_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(105)
    return _safe_div(base, _rolling_std(base, 252))

def ldis_731_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 5d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(105)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ldis_732_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 21d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(105)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ldis_733_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 63d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(105)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ldis_734_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 126d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(105)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ldis_735_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 252d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(105)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ldis_736_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 64 liquidity distress over a 5d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(110)
    return _rolling_mean(base, 5)

def ldis_737_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 64 liquidity distress over a 21d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(110)
    return _rolling_mean(base, 21)

def ldis_738_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 64 liquidity distress over a 63d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(110)
    return _rolling_mean(base, 63)

def ldis_739_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 64 liquidity distress over a 126d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(110)
    return _rolling_mean(base, 126)

def ldis_740_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 64 liquidity distress over a 252d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(110)
    return _rolling_mean(base, 252)

def ldis_741_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 64 liquidity distress by measuring deviations from the 5d mean.
    """
    base = revenue.pct_change(110)
    return _zscore_rolling(base, 5)

def ldis_742_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 64 liquidity distress by measuring deviations from the 21d mean.
    """
    base = revenue.pct_change(110)
    return _zscore_rolling(base, 21)

def ldis_743_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 64 liquidity distress by measuring deviations from the 63d mean.
    """
    base = revenue.pct_change(110)
    return _zscore_rolling(base, 63)

def ldis_744_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 64 liquidity distress by measuring deviations from the 126d mean.
    """
    base = revenue.pct_change(110)
    return _zscore_rolling(base, 126)

def ldis_745_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 64 liquidity distress by measuring deviations from the 252d mean.
    """
    base = revenue.pct_change(110)
    return _zscore_rolling(base, 252)

def ldis_746_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(110)
    return _rank_pct(base, 5)

def ldis_747_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(110)
    return _rank_pct(base, 21)

def ldis_748_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(110)
    return _rank_pct(base, 63)

def ldis_749_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(110)
    return _rank_pct(base, 126)

def ldis_750_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(110)
    return _rank_pct(base, 252)
