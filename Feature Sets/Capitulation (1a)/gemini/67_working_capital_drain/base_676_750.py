"""
67_67_working_capital_drain — Base Features 676-750
Domain: 67_working_capital_drain
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

def wcap_676_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 67 working capital drain to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(100)
    return _rank_pct(base, 5)

def wcap_677_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 67 working capital drain to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(100)
    return _rank_pct(base, 21)

def wcap_678_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 67 working capital drain to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(100)
    return _rank_pct(base, 63)

def wcap_679_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 67 working capital drain to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(100)
    return _rank_pct(base, 126)

def wcap_680_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 67 working capital drain to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(100)
    return _rank_pct(base, 252)

def wcap_681_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 67 working capital drain distribution over 5d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(100)
    return _rolling_skew(base, 5)

def wcap_682_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 67 working capital drain distribution over 21d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(100)
    return _rolling_skew(base, 21)

def wcap_683_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 67 working capital drain distribution over 63d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(100)
    return _rolling_skew(base, 63)

def wcap_684_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 67 working capital drain distribution over 126d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(100)
    return _rolling_skew(base, 126)

def wcap_685_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 67 working capital drain distribution over 252d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(100)
    return _rolling_skew(base, 252)

def wcap_686_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 67 working capital drain over 5d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(100)
    return _rolling_kurt(base, 5)

def wcap_687_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 67 working capital drain over 21d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(100)
    return _rolling_kurt(base, 21)

def wcap_688_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 67 working capital drain over 63d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(100)
    return _rolling_kurt(base, 63)

def wcap_689_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 67 working capital drain over 126d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(100)
    return _rolling_kurt(base, 126)

def wcap_690_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 67 working capital drain over 252d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(100)
    return _rolling_kurt(base, 252)

def wcap_691_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 67 working capital drain for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(100)
    return _safe_div(base, _rolling_std(base, 5))

def wcap_692_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 67 working capital drain for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(100)
    return _safe_div(base, _rolling_std(base, 21))

def wcap_693_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 67 working capital drain for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(100)
    return _safe_div(base, _rolling_std(base, 63))

def wcap_694_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 67 working capital drain for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(100)
    return _safe_div(base, _rolling_std(base, 126))

def wcap_695_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 67 working capital drain for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(100)
    return _safe_div(base, _rolling_std(base, 252))

def wcap_696_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 67 working capital drain over 5d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(100)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def wcap_697_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 67 working capital drain over 21d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(100)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def wcap_698_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 67 working capital drain over 63d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(100)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def wcap_699_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 67 working capital drain over 126d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(100)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def wcap_700_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 67 working capital drain over 252d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(100)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def wcap_701_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 67 working capital drain over a 5d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(105)
    return _rolling_mean(base, 5)

def wcap_702_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 67 working capital drain over a 21d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(105)
    return _rolling_mean(base, 21)

def wcap_703_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 67 working capital drain over a 63d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(105)
    return _rolling_mean(base, 63)

def wcap_704_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 67 working capital drain over a 126d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(105)
    return _rolling_mean(base, 126)

def wcap_705_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 67 working capital drain over a 252d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(105)
    return _rolling_mean(base, 252)

def wcap_706_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 67 working capital drain by measuring deviations from the 5d mean.
    """
    base = opinc.pct_change(105)
    return _zscore_rolling(base, 5)

def wcap_707_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 67 working capital drain by measuring deviations from the 21d mean.
    """
    base = opinc.pct_change(105)
    return _zscore_rolling(base, 21)

def wcap_708_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 67 working capital drain by measuring deviations from the 63d mean.
    """
    base = opinc.pct_change(105)
    return _zscore_rolling(base, 63)

def wcap_709_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 67 working capital drain by measuring deviations from the 126d mean.
    """
    base = opinc.pct_change(105)
    return _zscore_rolling(base, 126)

def wcap_710_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 67 working capital drain by measuring deviations from the 252d mean.
    """
    base = opinc.pct_change(105)
    return _zscore_rolling(base, 252)

def wcap_711_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 67 working capital drain to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(105)
    return _rank_pct(base, 5)

def wcap_712_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 67 working capital drain to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(105)
    return _rank_pct(base, 21)

def wcap_713_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 67 working capital drain to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(105)
    return _rank_pct(base, 63)

def wcap_714_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 67 working capital drain to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(105)
    return _rank_pct(base, 126)

def wcap_715_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 67 working capital drain to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(105)
    return _rank_pct(base, 252)

def wcap_716_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 67 working capital drain distribution over 5d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(105)
    return _rolling_skew(base, 5)

def wcap_717_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 67 working capital drain distribution over 21d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(105)
    return _rolling_skew(base, 21)

def wcap_718_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 67 working capital drain distribution over 63d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(105)
    return _rolling_skew(base, 63)

def wcap_719_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 67 working capital drain distribution over 126d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(105)
    return _rolling_skew(base, 126)

def wcap_720_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 67 working capital drain distribution over 252d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(105)
    return _rolling_skew(base, 252)

def wcap_721_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 67 working capital drain over 5d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(105)
    return _rolling_kurt(base, 5)

def wcap_722_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 67 working capital drain over 21d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(105)
    return _rolling_kurt(base, 21)

def wcap_723_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 67 working capital drain over 63d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(105)
    return _rolling_kurt(base, 63)

def wcap_724_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 67 working capital drain over 126d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(105)
    return _rolling_kurt(base, 126)

def wcap_725_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 67 working capital drain over 252d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(105)
    return _rolling_kurt(base, 252)

def wcap_726_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 67 working capital drain for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(105)
    return _safe_div(base, _rolling_std(base, 5))

def wcap_727_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 67 working capital drain for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(105)
    return _safe_div(base, _rolling_std(base, 21))

def wcap_728_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 67 working capital drain for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(105)
    return _safe_div(base, _rolling_std(base, 63))

def wcap_729_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 67 working capital drain for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(105)
    return _safe_div(base, _rolling_std(base, 126))

def wcap_730_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 67 working capital drain for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(105)
    return _safe_div(base, _rolling_std(base, 252))

def wcap_731_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 67 working capital drain over 5d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(105)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def wcap_732_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 67 working capital drain over 21d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(105)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def wcap_733_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 67 working capital drain over 63d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(105)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def wcap_734_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 67 working capital drain over 126d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(105)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def wcap_735_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 67 working capital drain over 252d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(105)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def wcap_736_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 67 working capital drain over a 5d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(110)
    return _rolling_mean(base, 5)

def wcap_737_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 67 working capital drain over a 21d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(110)
    return _rolling_mean(base, 21)

def wcap_738_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 67 working capital drain over a 63d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(110)
    return _rolling_mean(base, 63)

def wcap_739_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 67 working capital drain over a 126d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(110)
    return _rolling_mean(base, 126)

def wcap_740_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 67 working capital drain over a 252d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(110)
    return _rolling_mean(base, 252)

def wcap_741_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 67 working capital drain by measuring deviations from the 5d mean.
    """
    base = opinc.pct_change(110)
    return _zscore_rolling(base, 5)

def wcap_742_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 67 working capital drain by measuring deviations from the 21d mean.
    """
    base = opinc.pct_change(110)
    return _zscore_rolling(base, 21)

def wcap_743_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 67 working capital drain by measuring deviations from the 63d mean.
    """
    base = opinc.pct_change(110)
    return _zscore_rolling(base, 63)

def wcap_744_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 67 working capital drain by measuring deviations from the 126d mean.
    """
    base = opinc.pct_change(110)
    return _zscore_rolling(base, 126)

def wcap_745_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 67 working capital drain by measuring deviations from the 252d mean.
    """
    base = opinc.pct_change(110)
    return _zscore_rolling(base, 252)

def wcap_746_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 67 working capital drain to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(110)
    return _rank_pct(base, 5)

def wcap_747_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 67 working capital drain to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(110)
    return _rank_pct(base, 21)

def wcap_748_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 67 working capital drain to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(110)
    return _rank_pct(base, 63)

def wcap_749_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 67 working capital drain to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(110)
    return _rank_pct(base, 126)

def wcap_750_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 67 working capital drain to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(110)
    return _rank_pct(base, 252)
