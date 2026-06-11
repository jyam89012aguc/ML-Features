"""
74_74_fundamental_momentum — Base Features 676-750
Domain: 74_fundamental_momentum
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

def fmom_676_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(100)
    return _rank_pct(base, 5)

def fmom_677_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(100)
    return _rank_pct(base, 21)

def fmom_678_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(100)
    return _rank_pct(base, 63)

def fmom_679_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(100)
    return _rank_pct(base, 126)

def fmom_680_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(100)
    return _rank_pct(base, 252)

def fmom_681_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 74 fundamental momentum distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(100)
    return _rolling_skew(base, 5)

def fmom_682_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 74 fundamental momentum distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(100)
    return _rolling_skew(base, 21)

def fmom_683_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 74 fundamental momentum distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(100)
    return _rolling_skew(base, 63)

def fmom_684_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 74 fundamental momentum distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(100)
    return _rolling_skew(base, 126)

def fmom_685_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 74 fundamental momentum distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(100)
    return _rolling_skew(base, 252)

def fmom_686_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 74 fundamental momentum over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(100)
    return _rolling_kurt(base, 5)

def fmom_687_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 74 fundamental momentum over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(100)
    return _rolling_kurt(base, 21)

def fmom_688_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 74 fundamental momentum over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(100)
    return _rolling_kurt(base, 63)

def fmom_689_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 74 fundamental momentum over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(100)
    return _rolling_kurt(base, 126)

def fmom_690_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 74 fundamental momentum over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(100)
    return _rolling_kurt(base, 252)

def fmom_691_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(100)
    return _safe_div(base, _rolling_std(base, 5))

def fmom_692_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(100)
    return _safe_div(base, _rolling_std(base, 21))

def fmom_693_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(100)
    return _safe_div(base, _rolling_std(base, 63))

def fmom_694_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(100)
    return _safe_div(base, _rolling_std(base, 126))

def fmom_695_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(100)
    return _safe_div(base, _rolling_std(base, 252))

def fmom_696_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 74 fundamental momentum over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(100)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def fmom_697_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 74 fundamental momentum over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(100)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def fmom_698_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 74 fundamental momentum over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(100)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def fmom_699_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 74 fundamental momentum over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(100)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def fmom_700_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 74 fundamental momentum over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(100)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def fmom_701_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 74 fundamental momentum over a 5d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(105)
    return _rolling_mean(base, 5)

def fmom_702_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 74 fundamental momentum over a 21d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(105)
    return _rolling_mean(base, 21)

def fmom_703_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 74 fundamental momentum over a 63d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(105)
    return _rolling_mean(base, 63)

def fmom_704_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 74 fundamental momentum over a 126d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(105)
    return _rolling_mean(base, 126)

def fmom_705_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 74 fundamental momentum over a 252d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(105)
    return _rolling_mean(base, 252)

def fmom_706_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 5d mean.
    """
    base = marketcap.pct_change(105)
    return _zscore_rolling(base, 5)

def fmom_707_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 21d mean.
    """
    base = marketcap.pct_change(105)
    return _zscore_rolling(base, 21)

def fmom_708_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 63d mean.
    """
    base = marketcap.pct_change(105)
    return _zscore_rolling(base, 63)

def fmom_709_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 126d mean.
    """
    base = marketcap.pct_change(105)
    return _zscore_rolling(base, 126)

def fmom_710_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 252d mean.
    """
    base = marketcap.pct_change(105)
    return _zscore_rolling(base, 252)

def fmom_711_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(105)
    return _rank_pct(base, 5)

def fmom_712_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(105)
    return _rank_pct(base, 21)

def fmom_713_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(105)
    return _rank_pct(base, 63)

def fmom_714_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(105)
    return _rank_pct(base, 126)

def fmom_715_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(105)
    return _rank_pct(base, 252)

def fmom_716_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 74 fundamental momentum distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(105)
    return _rolling_skew(base, 5)

def fmom_717_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 74 fundamental momentum distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(105)
    return _rolling_skew(base, 21)

def fmom_718_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 74 fundamental momentum distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(105)
    return _rolling_skew(base, 63)

def fmom_719_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 74 fundamental momentum distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(105)
    return _rolling_skew(base, 126)

def fmom_720_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 74 fundamental momentum distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(105)
    return _rolling_skew(base, 252)

def fmom_721_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 74 fundamental momentum over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(105)
    return _rolling_kurt(base, 5)

def fmom_722_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 74 fundamental momentum over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(105)
    return _rolling_kurt(base, 21)

def fmom_723_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 74 fundamental momentum over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(105)
    return _rolling_kurt(base, 63)

def fmom_724_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 74 fundamental momentum over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(105)
    return _rolling_kurt(base, 126)

def fmom_725_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 74 fundamental momentum over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(105)
    return _rolling_kurt(base, 252)

def fmom_726_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(105)
    return _safe_div(base, _rolling_std(base, 5))

def fmom_727_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(105)
    return _safe_div(base, _rolling_std(base, 21))

def fmom_728_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(105)
    return _safe_div(base, _rolling_std(base, 63))

def fmom_729_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(105)
    return _safe_div(base, _rolling_std(base, 126))

def fmom_730_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(105)
    return _safe_div(base, _rolling_std(base, 252))

def fmom_731_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 74 fundamental momentum over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(105)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def fmom_732_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 74 fundamental momentum over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(105)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def fmom_733_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 74 fundamental momentum over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(105)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def fmom_734_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 74 fundamental momentum over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(105)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def fmom_735_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 74 fundamental momentum over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(105)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def fmom_736_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 74 fundamental momentum over a 5d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(110)
    return _rolling_mean(base, 5)

def fmom_737_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 74 fundamental momentum over a 21d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(110)
    return _rolling_mean(base, 21)

def fmom_738_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 74 fundamental momentum over a 63d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(110)
    return _rolling_mean(base, 63)

def fmom_739_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 74 fundamental momentum over a 126d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(110)
    return _rolling_mean(base, 126)

def fmom_740_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 74 fundamental momentum over a 252d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(110)
    return _rolling_mean(base, 252)

def fmom_741_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 5d mean.
    """
    base = marketcap.pct_change(110)
    return _zscore_rolling(base, 5)

def fmom_742_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 21d mean.
    """
    base = marketcap.pct_change(110)
    return _zscore_rolling(base, 21)

def fmom_743_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 63d mean.
    """
    base = marketcap.pct_change(110)
    return _zscore_rolling(base, 63)

def fmom_744_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 126d mean.
    """
    base = marketcap.pct_change(110)
    return _zscore_rolling(base, 126)

def fmom_745_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 252d mean.
    """
    base = marketcap.pct_change(110)
    return _zscore_rolling(base, 252)

def fmom_746_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(110)
    return _rank_pct(base, 5)

def fmom_747_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(110)
    return _rank_pct(base, 21)

def fmom_748_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(110)
    return _rank_pct(base, 63)

def fmom_749_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(110)
    return _rank_pct(base, 126)

def fmom_750_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(110)
    return _rank_pct(base, 252)
