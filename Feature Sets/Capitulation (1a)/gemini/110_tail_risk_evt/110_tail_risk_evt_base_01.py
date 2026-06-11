"""
110_tail_risk_evt — Base Features Part 1
Domain: tail_risk_evt
Asset class: Equities
Target context: Capitulation
"""
import numpy as np
import pandas as pd

# ── Utility helpers ──────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

def _safe_div(a: pd.Series, b: pd.Series) -> pd.Series:
    return a / b.replace(0, _EPS)

def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).mean()

def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).max()

def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).min()

def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).std().fillna(0)

def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div((s - m), sd)

def _rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).rank(pct=True)

# ── Feature functions ────────────────────────────────────────────────────────

def trev_001_var_95_proxy_lvl_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_001_var_95_proxy_lvl_5d
    ECONOMIC RATIONALE: 5% Value-at-Risk proxy.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05)
    return _rolling_mean(base, 5)

def trev_002_var_95_proxy_zscore_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_002_var_95_proxy_zscore_5d
    ECONOMIC RATIONALE: 5% Value-at-Risk proxy.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05)
    return _zscore_rolling(base, 5)

def trev_003_var_95_proxy_rank_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_003_var_95_proxy_rank_5d
    ECONOMIC RATIONALE: 5% Value-at-Risk proxy.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05)
    return _rank_pct(base, 5)

def trev_004_var_95_proxy_lvl_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_004_var_95_proxy_lvl_21d
    ECONOMIC RATIONALE: 5% Value-at-Risk proxy.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05)
    return _rolling_mean(base, 21)

def trev_005_var_95_proxy_zscore_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_005_var_95_proxy_zscore_21d
    ECONOMIC RATIONALE: 5% Value-at-Risk proxy.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05)
    return _zscore_rolling(base, 21)

def trev_006_var_95_proxy_rank_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_006_var_95_proxy_rank_21d
    ECONOMIC RATIONALE: 5% Value-at-Risk proxy.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05)
    return _rank_pct(base, 21)

def trev_007_var_95_proxy_lvl_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_007_var_95_proxy_lvl_63d
    ECONOMIC RATIONALE: 5% Value-at-Risk proxy.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05)
    return _rolling_mean(base, 63)

def trev_008_var_95_proxy_zscore_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_008_var_95_proxy_zscore_63d
    ECONOMIC RATIONALE: 5% Value-at-Risk proxy.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05)
    return _zscore_rolling(base, 63)

def trev_009_var_95_proxy_rank_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_009_var_95_proxy_rank_63d
    ECONOMIC RATIONALE: 5% Value-at-Risk proxy.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05)
    return _rank_pct(base, 63)

def trev_010_var_95_proxy_lvl_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_010_var_95_proxy_lvl_126d
    ECONOMIC RATIONALE: 5% Value-at-Risk proxy.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05)
    return _rolling_mean(base, 126)

def trev_011_var_95_proxy_zscore_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_011_var_95_proxy_zscore_126d
    ECONOMIC RATIONALE: 5% Value-at-Risk proxy.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05)
    return _zscore_rolling(base, 126)

def trev_012_var_95_proxy_rank_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_012_var_95_proxy_rank_126d
    ECONOMIC RATIONALE: 5% Value-at-Risk proxy.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05)
    return _rank_pct(base, 126)

def trev_013_var_95_proxy_lvl_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_013_var_95_proxy_lvl_252d
    ECONOMIC RATIONALE: 5% Value-at-Risk proxy.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05)
    return _rolling_mean(base, 252)

def trev_014_var_95_proxy_zscore_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_014_var_95_proxy_zscore_252d
    ECONOMIC RATIONALE: 5% Value-at-Risk proxy.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05)
    return _zscore_rolling(base, 252)

def trev_015_var_95_proxy_rank_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_015_var_95_proxy_rank_252d
    ECONOMIC RATIONALE: 5% Value-at-Risk proxy.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05)
    return _rank_pct(base, 252)

def trev_016_expected_shortfall_proxy_lvl_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_016_expected_shortfall_proxy_lvl_5d
    ECONOMIC RATIONALE: Average loss in the bottom 5th percentile.
    """
    base = close.pct_change(1).apply(lambda x: x[x < x.quantile(0.05)].mean() if len(x[x < x.quantile(0.05)]) > 0 else 0)
    return _rolling_mean(base, 5)

def trev_017_expected_shortfall_proxy_zscore_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_017_expected_shortfall_proxy_zscore_5d
    ECONOMIC RATIONALE: Average loss in the bottom 5th percentile.
    """
    base = close.pct_change(1).apply(lambda x: x[x < x.quantile(0.05)].mean() if len(x[x < x.quantile(0.05)]) > 0 else 0)
    return _zscore_rolling(base, 5)

def trev_018_expected_shortfall_proxy_rank_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_018_expected_shortfall_proxy_rank_5d
    ECONOMIC RATIONALE: Average loss in the bottom 5th percentile.
    """
    base = close.pct_change(1).apply(lambda x: x[x < x.quantile(0.05)].mean() if len(x[x < x.quantile(0.05)]) > 0 else 0)
    return _rank_pct(base, 5)

def trev_019_expected_shortfall_proxy_lvl_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_019_expected_shortfall_proxy_lvl_21d
    ECONOMIC RATIONALE: Average loss in the bottom 5th percentile.
    """
    base = close.pct_change(1).apply(lambda x: x[x < x.quantile(0.05)].mean() if len(x[x < x.quantile(0.05)]) > 0 else 0)
    return _rolling_mean(base, 21)

def trev_020_expected_shortfall_proxy_zscore_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_020_expected_shortfall_proxy_zscore_21d
    ECONOMIC RATIONALE: Average loss in the bottom 5th percentile.
    """
    base = close.pct_change(1).apply(lambda x: x[x < x.quantile(0.05)].mean() if len(x[x < x.quantile(0.05)]) > 0 else 0)
    return _zscore_rolling(base, 21)

def trev_021_expected_shortfall_proxy_rank_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_021_expected_shortfall_proxy_rank_21d
    ECONOMIC RATIONALE: Average loss in the bottom 5th percentile.
    """
    base = close.pct_change(1).apply(lambda x: x[x < x.quantile(0.05)].mean() if len(x[x < x.quantile(0.05)]) > 0 else 0)
    return _rank_pct(base, 21)

def trev_022_expected_shortfall_proxy_lvl_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_022_expected_shortfall_proxy_lvl_63d
    ECONOMIC RATIONALE: Average loss in the bottom 5th percentile.
    """
    base = close.pct_change(1).apply(lambda x: x[x < x.quantile(0.05)].mean() if len(x[x < x.quantile(0.05)]) > 0 else 0)
    return _rolling_mean(base, 63)

def trev_023_expected_shortfall_proxy_zscore_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_023_expected_shortfall_proxy_zscore_63d
    ECONOMIC RATIONALE: Average loss in the bottom 5th percentile.
    """
    base = close.pct_change(1).apply(lambda x: x[x < x.quantile(0.05)].mean() if len(x[x < x.quantile(0.05)]) > 0 else 0)
    return _zscore_rolling(base, 63)

def trev_024_expected_shortfall_proxy_rank_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_024_expected_shortfall_proxy_rank_63d
    ECONOMIC RATIONALE: Average loss in the bottom 5th percentile.
    """
    base = close.pct_change(1).apply(lambda x: x[x < x.quantile(0.05)].mean() if len(x[x < x.quantile(0.05)]) > 0 else 0)
    return _rank_pct(base, 63)

def trev_025_expected_shortfall_proxy_lvl_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_025_expected_shortfall_proxy_lvl_126d
    ECONOMIC RATIONALE: Average loss in the bottom 5th percentile.
    """
    base = close.pct_change(1).apply(lambda x: x[x < x.quantile(0.05)].mean() if len(x[x < x.quantile(0.05)]) > 0 else 0)
    return _rolling_mean(base, 126)

def trev_026_expected_shortfall_proxy_zscore_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_026_expected_shortfall_proxy_zscore_126d
    ECONOMIC RATIONALE: Average loss in the bottom 5th percentile.
    """
    base = close.pct_change(1).apply(lambda x: x[x < x.quantile(0.05)].mean() if len(x[x < x.quantile(0.05)]) > 0 else 0)
    return _zscore_rolling(base, 126)

def trev_027_expected_shortfall_proxy_rank_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_027_expected_shortfall_proxy_rank_126d
    ECONOMIC RATIONALE: Average loss in the bottom 5th percentile.
    """
    base = close.pct_change(1).apply(lambda x: x[x < x.quantile(0.05)].mean() if len(x[x < x.quantile(0.05)]) > 0 else 0)
    return _rank_pct(base, 126)

def trev_028_expected_shortfall_proxy_lvl_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_028_expected_shortfall_proxy_lvl_252d
    ECONOMIC RATIONALE: Average loss in the bottom 5th percentile.
    """
    base = close.pct_change(1).apply(lambda x: x[x < x.quantile(0.05)].mean() if len(x[x < x.quantile(0.05)]) > 0 else 0)
    return _rolling_mean(base, 252)

def trev_029_expected_shortfall_proxy_zscore_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_029_expected_shortfall_proxy_zscore_252d
    ECONOMIC RATIONALE: Average loss in the bottom 5th percentile.
    """
    base = close.pct_change(1).apply(lambda x: x[x < x.quantile(0.05)].mean() if len(x[x < x.quantile(0.05)]) > 0 else 0)
    return _zscore_rolling(base, 252)

def trev_030_expected_shortfall_proxy_rank_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_030_expected_shortfall_proxy_rank_252d
    ECONOMIC RATIONALE: Average loss in the bottom 5th percentile.
    """
    base = close.pct_change(1).apply(lambda x: x[x < x.quantile(0.05)].mean() if len(x[x < x.quantile(0.05)]) > 0 else 0)
    return _rank_pct(base, 252)

def trev_031_tail_event_density_lvl_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_031_tail_event_density_lvl_5d
    ECONOMIC RATIONALE: Frequency of 5% tail events.
    """
    base = (close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(63).sum()
    return _rolling_mean(base, 5)

def trev_032_tail_event_density_zscore_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_032_tail_event_density_zscore_5d
    ECONOMIC RATIONALE: Frequency of 5% tail events.
    """
    base = (close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(63).sum()
    return _zscore_rolling(base, 5)

def trev_033_tail_event_density_rank_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_033_tail_event_density_rank_5d
    ECONOMIC RATIONALE: Frequency of 5% tail events.
    """
    base = (close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(63).sum()
    return _rank_pct(base, 5)

def trev_034_tail_event_density_lvl_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_034_tail_event_density_lvl_21d
    ECONOMIC RATIONALE: Frequency of 5% tail events.
    """
    base = (close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(63).sum()
    return _rolling_mean(base, 21)

def trev_035_tail_event_density_zscore_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_035_tail_event_density_zscore_21d
    ECONOMIC RATIONALE: Frequency of 5% tail events.
    """
    base = (close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(63).sum()
    return _zscore_rolling(base, 21)

def trev_036_tail_event_density_rank_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_036_tail_event_density_rank_21d
    ECONOMIC RATIONALE: Frequency of 5% tail events.
    """
    base = (close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(63).sum()
    return _rank_pct(base, 21)

def trev_037_tail_event_density_lvl_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_037_tail_event_density_lvl_63d
    ECONOMIC RATIONALE: Frequency of 5% tail events.
    """
    base = (close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(63).sum()
    return _rolling_mean(base, 63)

def trev_038_tail_event_density_zscore_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_038_tail_event_density_zscore_63d
    ECONOMIC RATIONALE: Frequency of 5% tail events.
    """
    base = (close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(63).sum()
    return _zscore_rolling(base, 63)

def trev_039_tail_event_density_rank_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_039_tail_event_density_rank_63d
    ECONOMIC RATIONALE: Frequency of 5% tail events.
    """
    base = (close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(63).sum()
    return _rank_pct(base, 63)

def trev_040_tail_event_density_lvl_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_040_tail_event_density_lvl_126d
    ECONOMIC RATIONALE: Frequency of 5% tail events.
    """
    base = (close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(63).sum()
    return _rolling_mean(base, 126)

def trev_041_tail_event_density_zscore_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_041_tail_event_density_zscore_126d
    ECONOMIC RATIONALE: Frequency of 5% tail events.
    """
    base = (close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(63).sum()
    return _zscore_rolling(base, 126)

def trev_042_tail_event_density_rank_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_042_tail_event_density_rank_126d
    ECONOMIC RATIONALE: Frequency of 5% tail events.
    """
    base = (close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(63).sum()
    return _rank_pct(base, 126)

def trev_043_tail_event_density_lvl_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_043_tail_event_density_lvl_252d
    ECONOMIC RATIONALE: Frequency of 5% tail events.
    """
    base = (close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(63).sum()
    return _rolling_mean(base, 252)

def trev_044_tail_event_density_zscore_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_044_tail_event_density_zscore_252d
    ECONOMIC RATIONALE: Frequency of 5% tail events.
    """
    base = (close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(63).sum()
    return _zscore_rolling(base, 252)

def trev_045_tail_event_density_rank_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_045_tail_event_density_rank_252d
    ECONOMIC RATIONALE: Frequency of 5% tail events.
    """
    base = (close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(63).sum()
    return _rank_pct(base, 252)

def trev_046_skewness_252d_lvl_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_046_skewness_252d_lvl_5d
    ECONOMIC RATIONALE: Asymmetry of return distribution (negative = tail risk).
    """
    base = close.pct_change(1).rolling(252).skew()
    return _rolling_mean(base, 5)

def trev_047_skewness_252d_zscore_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_047_skewness_252d_zscore_5d
    ECONOMIC RATIONALE: Asymmetry of return distribution (negative = tail risk).
    """
    base = close.pct_change(1).rolling(252).skew()
    return _zscore_rolling(base, 5)

def trev_048_skewness_252d_rank_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_048_skewness_252d_rank_5d
    ECONOMIC RATIONALE: Asymmetry of return distribution (negative = tail risk).
    """
    base = close.pct_change(1).rolling(252).skew()
    return _rank_pct(base, 5)

def trev_049_skewness_252d_lvl_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_049_skewness_252d_lvl_21d
    ECONOMIC RATIONALE: Asymmetry of return distribution (negative = tail risk).
    """
    base = close.pct_change(1).rolling(252).skew()
    return _rolling_mean(base, 21)

def trev_050_skewness_252d_zscore_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_050_skewness_252d_zscore_21d
    ECONOMIC RATIONALE: Asymmetry of return distribution (negative = tail risk).
    """
    base = close.pct_change(1).rolling(252).skew()
    return _zscore_rolling(base, 21)

def trev_051_skewness_252d_rank_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_051_skewness_252d_rank_21d
    ECONOMIC RATIONALE: Asymmetry of return distribution (negative = tail risk).
    """
    base = close.pct_change(1).rolling(252).skew()
    return _rank_pct(base, 21)

def trev_052_skewness_252d_lvl_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_052_skewness_252d_lvl_63d
    ECONOMIC RATIONALE: Asymmetry of return distribution (negative = tail risk).
    """
    base = close.pct_change(1).rolling(252).skew()
    return _rolling_mean(base, 63)

def trev_053_skewness_252d_zscore_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_053_skewness_252d_zscore_63d
    ECONOMIC RATIONALE: Asymmetry of return distribution (negative = tail risk).
    """
    base = close.pct_change(1).rolling(252).skew()
    return _zscore_rolling(base, 63)

def trev_054_skewness_252d_rank_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_054_skewness_252d_rank_63d
    ECONOMIC RATIONALE: Asymmetry of return distribution (negative = tail risk).
    """
    base = close.pct_change(1).rolling(252).skew()
    return _rank_pct(base, 63)

def trev_055_skewness_252d_lvl_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_055_skewness_252d_lvl_126d
    ECONOMIC RATIONALE: Asymmetry of return distribution (negative = tail risk).
    """
    base = close.pct_change(1).rolling(252).skew()
    return _rolling_mean(base, 126)

def trev_056_skewness_252d_zscore_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_056_skewness_252d_zscore_126d
    ECONOMIC RATIONALE: Asymmetry of return distribution (negative = tail risk).
    """
    base = close.pct_change(1).rolling(252).skew()
    return _zscore_rolling(base, 126)

def trev_057_skewness_252d_rank_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_057_skewness_252d_rank_126d
    ECONOMIC RATIONALE: Asymmetry of return distribution (negative = tail risk).
    """
    base = close.pct_change(1).rolling(252).skew()
    return _rank_pct(base, 126)

def trev_058_skewness_252d_lvl_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_058_skewness_252d_lvl_252d
    ECONOMIC RATIONALE: Asymmetry of return distribution (negative = tail risk).
    """
    base = close.pct_change(1).rolling(252).skew()
    return _rolling_mean(base, 252)

def trev_059_skewness_252d_zscore_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_059_skewness_252d_zscore_252d
    ECONOMIC RATIONALE: Asymmetry of return distribution (negative = tail risk).
    """
    base = close.pct_change(1).rolling(252).skew()
    return _zscore_rolling(base, 252)

def trev_060_skewness_252d_rank_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_060_skewness_252d_rank_252d
    ECONOMIC RATIONALE: Asymmetry of return distribution (negative = tail risk).
    """
    base = close.pct_change(1).rolling(252).skew()
    return _rank_pct(base, 252)

def trev_061_kurtosis_252d_lvl_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_061_kurtosis_252d_lvl_5d
    ECONOMIC RATIONALE: Fatness of tails in the return distribution.
    """
    base = close.pct_change(1).rolling(252).kurt()
    return _rolling_mean(base, 5)

def trev_062_kurtosis_252d_zscore_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_062_kurtosis_252d_zscore_5d
    ECONOMIC RATIONALE: Fatness of tails in the return distribution.
    """
    base = close.pct_change(1).rolling(252).kurt()
    return _zscore_rolling(base, 5)

def trev_063_kurtosis_252d_rank_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_063_kurtosis_252d_rank_5d
    ECONOMIC RATIONALE: Fatness of tails in the return distribution.
    """
    base = close.pct_change(1).rolling(252).kurt()
    return _rank_pct(base, 5)

def trev_064_kurtosis_252d_lvl_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_064_kurtosis_252d_lvl_21d
    ECONOMIC RATIONALE: Fatness of tails in the return distribution.
    """
    base = close.pct_change(1).rolling(252).kurt()
    return _rolling_mean(base, 21)

def trev_065_kurtosis_252d_zscore_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_065_kurtosis_252d_zscore_21d
    ECONOMIC RATIONALE: Fatness of tails in the return distribution.
    """
    base = close.pct_change(1).rolling(252).kurt()
    return _zscore_rolling(base, 21)

def trev_066_kurtosis_252d_rank_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_066_kurtosis_252d_rank_21d
    ECONOMIC RATIONALE: Fatness of tails in the return distribution.
    """
    base = close.pct_change(1).rolling(252).kurt()
    return _rank_pct(base, 21)

def trev_067_kurtosis_252d_lvl_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_067_kurtosis_252d_lvl_63d
    ECONOMIC RATIONALE: Fatness of tails in the return distribution.
    """
    base = close.pct_change(1).rolling(252).kurt()
    return _rolling_mean(base, 63)

def trev_068_kurtosis_252d_zscore_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_068_kurtosis_252d_zscore_63d
    ECONOMIC RATIONALE: Fatness of tails in the return distribution.
    """
    base = close.pct_change(1).rolling(252).kurt()
    return _zscore_rolling(base, 63)

def trev_069_kurtosis_252d_rank_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_069_kurtosis_252d_rank_63d
    ECONOMIC RATIONALE: Fatness of tails in the return distribution.
    """
    base = close.pct_change(1).rolling(252).kurt()
    return _rank_pct(base, 63)

def trev_070_kurtosis_252d_lvl_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_070_kurtosis_252d_lvl_126d
    ECONOMIC RATIONALE: Fatness of tails in the return distribution.
    """
    base = close.pct_change(1).rolling(252).kurt()
    return _rolling_mean(base, 126)

def trev_071_kurtosis_252d_zscore_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_071_kurtosis_252d_zscore_126d
    ECONOMIC RATIONALE: Fatness of tails in the return distribution.
    """
    base = close.pct_change(1).rolling(252).kurt()
    return _zscore_rolling(base, 126)

def trev_072_kurtosis_252d_rank_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_072_kurtosis_252d_rank_126d
    ECONOMIC RATIONALE: Fatness of tails in the return distribution.
    """
    base = close.pct_change(1).rolling(252).kurt()
    return _rank_pct(base, 126)

def trev_073_kurtosis_252d_lvl_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_073_kurtosis_252d_lvl_252d
    ECONOMIC RATIONALE: Fatness of tails in the return distribution.
    """
    base = close.pct_change(1).rolling(252).kurt()
    return _rolling_mean(base, 252)

def trev_074_kurtosis_252d_zscore_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_074_kurtosis_252d_zscore_252d
    ECONOMIC RATIONALE: Fatness of tails in the return distribution.
    """
    base = close.pct_change(1).rolling(252).kurt()
    return _zscore_rolling(base, 252)

def trev_075_kurtosis_252d_rank_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_075_kurtosis_252d_rank_252d
    ECONOMIC RATIONALE: Fatness of tails in the return distribution.
    """
    base = close.pct_change(1).rolling(252).kurt()
    return _rank_pct(base, 252)

def trev_076_tail_ratio_lvl_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_076_tail_ratio_lvl_5d
    ECONOMIC RATIONALE: Ratio of upside to downside tail risk.
    """
    base = abs(close.pct_change(1).rolling(252).quantile(0.95) / close.pct_change(1).rolling(252).quantile(0.05).replace(0, 1e-9))
    return _rolling_mean(base, 5)

def trev_077_tail_ratio_zscore_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_077_tail_ratio_zscore_5d
    ECONOMIC RATIONALE: Ratio of upside to downside tail risk.
    """
    base = abs(close.pct_change(1).rolling(252).quantile(0.95) / close.pct_change(1).rolling(252).quantile(0.05).replace(0, 1e-9))
    return _zscore_rolling(base, 5)

def trev_078_tail_ratio_rank_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_078_tail_ratio_rank_5d
    ECONOMIC RATIONALE: Ratio of upside to downside tail risk.
    """
    base = abs(close.pct_change(1).rolling(252).quantile(0.95) / close.pct_change(1).rolling(252).quantile(0.05).replace(0, 1e-9))
    return _rank_pct(base, 5)

def trev_079_tail_ratio_lvl_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_079_tail_ratio_lvl_21d
    ECONOMIC RATIONALE: Ratio of upside to downside tail risk.
    """
    base = abs(close.pct_change(1).rolling(252).quantile(0.95) / close.pct_change(1).rolling(252).quantile(0.05).replace(0, 1e-9))
    return _rolling_mean(base, 21)

def trev_080_tail_ratio_zscore_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_080_tail_ratio_zscore_21d
    ECONOMIC RATIONALE: Ratio of upside to downside tail risk.
    """
    base = abs(close.pct_change(1).rolling(252).quantile(0.95) / close.pct_change(1).rolling(252).quantile(0.05).replace(0, 1e-9))
    return _zscore_rolling(base, 21)

def trev_081_tail_ratio_rank_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_081_tail_ratio_rank_21d
    ECONOMIC RATIONALE: Ratio of upside to downside tail risk.
    """
    base = abs(close.pct_change(1).rolling(252).quantile(0.95) / close.pct_change(1).rolling(252).quantile(0.05).replace(0, 1e-9))
    return _rank_pct(base, 21)

def trev_082_tail_ratio_lvl_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_082_tail_ratio_lvl_63d
    ECONOMIC RATIONALE: Ratio of upside to downside tail risk.
    """
    base = abs(close.pct_change(1).rolling(252).quantile(0.95) / close.pct_change(1).rolling(252).quantile(0.05).replace(0, 1e-9))
    return _rolling_mean(base, 63)

def trev_083_tail_ratio_zscore_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_083_tail_ratio_zscore_63d
    ECONOMIC RATIONALE: Ratio of upside to downside tail risk.
    """
    base = abs(close.pct_change(1).rolling(252).quantile(0.95) / close.pct_change(1).rolling(252).quantile(0.05).replace(0, 1e-9))
    return _zscore_rolling(base, 63)

def trev_084_tail_ratio_rank_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_084_tail_ratio_rank_63d
    ECONOMIC RATIONALE: Ratio of upside to downside tail risk.
    """
    base = abs(close.pct_change(1).rolling(252).quantile(0.95) / close.pct_change(1).rolling(252).quantile(0.05).replace(0, 1e-9))
    return _rank_pct(base, 63)

def trev_085_tail_ratio_lvl_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_085_tail_ratio_lvl_126d
    ECONOMIC RATIONALE: Ratio of upside to downside tail risk.
    """
    base = abs(close.pct_change(1).rolling(252).quantile(0.95) / close.pct_change(1).rolling(252).quantile(0.05).replace(0, 1e-9))
    return _rolling_mean(base, 126)

def trev_086_tail_ratio_zscore_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_086_tail_ratio_zscore_126d
    ECONOMIC RATIONALE: Ratio of upside to downside tail risk.
    """
    base = abs(close.pct_change(1).rolling(252).quantile(0.95) / close.pct_change(1).rolling(252).quantile(0.05).replace(0, 1e-9))
    return _zscore_rolling(base, 126)

def trev_087_tail_ratio_rank_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_087_tail_ratio_rank_126d
    ECONOMIC RATIONALE: Ratio of upside to downside tail risk.
    """
    base = abs(close.pct_change(1).rolling(252).quantile(0.95) / close.pct_change(1).rolling(252).quantile(0.05).replace(0, 1e-9))
    return _rank_pct(base, 126)

def trev_088_tail_ratio_lvl_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_088_tail_ratio_lvl_252d
    ECONOMIC RATIONALE: Ratio of upside to downside tail risk.
    """
    base = abs(close.pct_change(1).rolling(252).quantile(0.95) / close.pct_change(1).rolling(252).quantile(0.05).replace(0, 1e-9))
    return _rolling_mean(base, 252)

def trev_089_tail_ratio_zscore_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_089_tail_ratio_zscore_252d
    ECONOMIC RATIONALE: Ratio of upside to downside tail risk.
    """
    base = abs(close.pct_change(1).rolling(252).quantile(0.95) / close.pct_change(1).rolling(252).quantile(0.05).replace(0, 1e-9))
    return _zscore_rolling(base, 252)

def trev_090_tail_ratio_rank_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_090_tail_ratio_rank_252d
    ECONOMIC RATIONALE: Ratio of upside to downside tail risk.
    """
    base = abs(close.pct_change(1).rolling(252).quantile(0.95) / close.pct_change(1).rolling(252).quantile(0.05).replace(0, 1e-9))
    return _rank_pct(base, 252)

def trev_091_extreme_low_z_lvl_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_091_extreme_low_z_lvl_5d
    ECONOMIC RATIONALE: Low price deviation from annual mean.
    """
    base = _zscore_rolling(low, 252)
    return _rolling_mean(base, 5)

def trev_092_extreme_low_z_zscore_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_092_extreme_low_z_zscore_5d
    ECONOMIC RATIONALE: Low price deviation from annual mean.
    """
    base = _zscore_rolling(low, 252)
    return _zscore_rolling(base, 5)

def trev_093_extreme_low_z_rank_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_093_extreme_low_z_rank_5d
    ECONOMIC RATIONALE: Low price deviation from annual mean.
    """
    base = _zscore_rolling(low, 252)
    return _rank_pct(base, 5)

def trev_094_extreme_low_z_lvl_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_094_extreme_low_z_lvl_21d
    ECONOMIC RATIONALE: Low price deviation from annual mean.
    """
    base = _zscore_rolling(low, 252)
    return _rolling_mean(base, 21)

def trev_095_extreme_low_z_zscore_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_095_extreme_low_z_zscore_21d
    ECONOMIC RATIONALE: Low price deviation from annual mean.
    """
    base = _zscore_rolling(low, 252)
    return _zscore_rolling(base, 21)

def trev_096_extreme_low_z_rank_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_096_extreme_low_z_rank_21d
    ECONOMIC RATIONALE: Low price deviation from annual mean.
    """
    base = _zscore_rolling(low, 252)
    return _rank_pct(base, 21)

def trev_097_extreme_low_z_lvl_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_097_extreme_low_z_lvl_63d
    ECONOMIC RATIONALE: Low price deviation from annual mean.
    """
    base = _zscore_rolling(low, 252)
    return _rolling_mean(base, 63)

def trev_098_extreme_low_z_zscore_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_098_extreme_low_z_zscore_63d
    ECONOMIC RATIONALE: Low price deviation from annual mean.
    """
    base = _zscore_rolling(low, 252)
    return _zscore_rolling(base, 63)

def trev_099_extreme_low_z_rank_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_099_extreme_low_z_rank_63d
    ECONOMIC RATIONALE: Low price deviation from annual mean.
    """
    base = _zscore_rolling(low, 252)
    return _rank_pct(base, 63)

def trev_100_extreme_low_z_lvl_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_100_extreme_low_z_lvl_126d
    ECONOMIC RATIONALE: Low price deviation from annual mean.
    """
    base = _zscore_rolling(low, 252)
    return _rolling_mean(base, 126)

def trev_101_extreme_low_z_zscore_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_101_extreme_low_z_zscore_126d
    ECONOMIC RATIONALE: Low price deviation from annual mean.
    """
    base = _zscore_rolling(low, 252)
    return _zscore_rolling(base, 126)

def trev_102_extreme_low_z_rank_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_102_extreme_low_z_rank_126d
    ECONOMIC RATIONALE: Low price deviation from annual mean.
    """
    base = _zscore_rolling(low, 252)
    return _rank_pct(base, 126)

def trev_103_extreme_low_z_lvl_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_103_extreme_low_z_lvl_252d
    ECONOMIC RATIONALE: Low price deviation from annual mean.
    """
    base = _zscore_rolling(low, 252)
    return _rolling_mean(base, 252)

def trev_104_extreme_low_z_zscore_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_104_extreme_low_z_zscore_252d
    ECONOMIC RATIONALE: Low price deviation from annual mean.
    """
    base = _zscore_rolling(low, 252)
    return _zscore_rolling(base, 252)

def trev_105_extreme_low_z_rank_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_105_extreme_low_z_rank_252d
    ECONOMIC RATIONALE: Low price deviation from annual mean.
    """
    base = _zscore_rolling(low, 252)
    return _rank_pct(base, 252)

def trev_106_tail_risk_momentum_lvl_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_106_tail_risk_momentum_lvl_5d
    ECONOMIC RATIONALE: Trend in the severity of tail risk.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05).diff(21)
    return _rolling_mean(base, 5)

def trev_107_tail_risk_momentum_zscore_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_107_tail_risk_momentum_zscore_5d
    ECONOMIC RATIONALE: Trend in the severity of tail risk.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05).diff(21)
    return _zscore_rolling(base, 5)

def trev_108_tail_risk_momentum_rank_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_108_tail_risk_momentum_rank_5d
    ECONOMIC RATIONALE: Trend in the severity of tail risk.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05).diff(21)
    return _rank_pct(base, 5)

def trev_109_tail_risk_momentum_lvl_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_109_tail_risk_momentum_lvl_21d
    ECONOMIC RATIONALE: Trend in the severity of tail risk.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05).diff(21)
    return _rolling_mean(base, 21)

def trev_110_tail_risk_momentum_zscore_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_110_tail_risk_momentum_zscore_21d
    ECONOMIC RATIONALE: Trend in the severity of tail risk.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05).diff(21)
    return _zscore_rolling(base, 21)

def trev_111_tail_risk_momentum_rank_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_111_tail_risk_momentum_rank_21d
    ECONOMIC RATIONALE: Trend in the severity of tail risk.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05).diff(21)
    return _rank_pct(base, 21)

def trev_112_tail_risk_momentum_lvl_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_112_tail_risk_momentum_lvl_63d
    ECONOMIC RATIONALE: Trend in the severity of tail risk.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05).diff(21)
    return _rolling_mean(base, 63)

def trev_113_tail_risk_momentum_zscore_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_113_tail_risk_momentum_zscore_63d
    ECONOMIC RATIONALE: Trend in the severity of tail risk.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05).diff(21)
    return _zscore_rolling(base, 63)

def trev_114_tail_risk_momentum_rank_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_114_tail_risk_momentum_rank_63d
    ECONOMIC RATIONALE: Trend in the severity of tail risk.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05).diff(21)
    return _rank_pct(base, 63)

def trev_115_tail_risk_momentum_lvl_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_115_tail_risk_momentum_lvl_126d
    ECONOMIC RATIONALE: Trend in the severity of tail risk.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05).diff(21)
    return _rolling_mean(base, 126)

def trev_116_tail_risk_momentum_zscore_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_116_tail_risk_momentum_zscore_126d
    ECONOMIC RATIONALE: Trend in the severity of tail risk.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05).diff(21)
    return _zscore_rolling(base, 126)

def trev_117_tail_risk_momentum_rank_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_117_tail_risk_momentum_rank_126d
    ECONOMIC RATIONALE: Trend in the severity of tail risk.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05).diff(21)
    return _rank_pct(base, 126)

def trev_118_tail_risk_momentum_lvl_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_118_tail_risk_momentum_lvl_252d
    ECONOMIC RATIONALE: Trend in the severity of tail risk.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05).diff(21)
    return _rolling_mean(base, 252)

def trev_119_tail_risk_momentum_zscore_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_119_tail_risk_momentum_zscore_252d
    ECONOMIC RATIONALE: Trend in the severity of tail risk.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05).diff(21)
    return _zscore_rolling(base, 252)

def trev_120_tail_risk_momentum_rank_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_120_tail_risk_momentum_rank_252d
    ECONOMIC RATIONALE: Trend in the severity of tail risk.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05).diff(21)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V110_REGISTRY_1 = {
    "trev_001_var_95_proxy_lvl_5d": {"inputs": ["close", "low", "open"], "func": trev_001_var_95_proxy_lvl_5d},
    "trev_002_var_95_proxy_zscore_5d": {"inputs": ["close", "low", "open"], "func": trev_002_var_95_proxy_zscore_5d},
    "trev_003_var_95_proxy_rank_5d": {"inputs": ["close", "low", "open"], "func": trev_003_var_95_proxy_rank_5d},
    "trev_004_var_95_proxy_lvl_21d": {"inputs": ["close", "low", "open"], "func": trev_004_var_95_proxy_lvl_21d},
    "trev_005_var_95_proxy_zscore_21d": {"inputs": ["close", "low", "open"], "func": trev_005_var_95_proxy_zscore_21d},
    "trev_006_var_95_proxy_rank_21d": {"inputs": ["close", "low", "open"], "func": trev_006_var_95_proxy_rank_21d},
    "trev_007_var_95_proxy_lvl_63d": {"inputs": ["close", "low", "open"], "func": trev_007_var_95_proxy_lvl_63d},
    "trev_008_var_95_proxy_zscore_63d": {"inputs": ["close", "low", "open"], "func": trev_008_var_95_proxy_zscore_63d},
    "trev_009_var_95_proxy_rank_63d": {"inputs": ["close", "low", "open"], "func": trev_009_var_95_proxy_rank_63d},
    "trev_010_var_95_proxy_lvl_126d": {"inputs": ["close", "low", "open"], "func": trev_010_var_95_proxy_lvl_126d},
    "trev_011_var_95_proxy_zscore_126d": {"inputs": ["close", "low", "open"], "func": trev_011_var_95_proxy_zscore_126d},
    "trev_012_var_95_proxy_rank_126d": {"inputs": ["close", "low", "open"], "func": trev_012_var_95_proxy_rank_126d},
    "trev_013_var_95_proxy_lvl_252d": {"inputs": ["close", "low", "open"], "func": trev_013_var_95_proxy_lvl_252d},
    "trev_014_var_95_proxy_zscore_252d": {"inputs": ["close", "low", "open"], "func": trev_014_var_95_proxy_zscore_252d},
    "trev_015_var_95_proxy_rank_252d": {"inputs": ["close", "low", "open"], "func": trev_015_var_95_proxy_rank_252d},
    "trev_016_expected_shortfall_proxy_lvl_5d": {"inputs": ["close", "low", "open"], "func": trev_016_expected_shortfall_proxy_lvl_5d},
    "trev_017_expected_shortfall_proxy_zscore_5d": {"inputs": ["close", "low", "open"], "func": trev_017_expected_shortfall_proxy_zscore_5d},
    "trev_018_expected_shortfall_proxy_rank_5d": {"inputs": ["close", "low", "open"], "func": trev_018_expected_shortfall_proxy_rank_5d},
    "trev_019_expected_shortfall_proxy_lvl_21d": {"inputs": ["close", "low", "open"], "func": trev_019_expected_shortfall_proxy_lvl_21d},
    "trev_020_expected_shortfall_proxy_zscore_21d": {"inputs": ["close", "low", "open"], "func": trev_020_expected_shortfall_proxy_zscore_21d},
    "trev_021_expected_shortfall_proxy_rank_21d": {"inputs": ["close", "low", "open"], "func": trev_021_expected_shortfall_proxy_rank_21d},
    "trev_022_expected_shortfall_proxy_lvl_63d": {"inputs": ["close", "low", "open"], "func": trev_022_expected_shortfall_proxy_lvl_63d},
    "trev_023_expected_shortfall_proxy_zscore_63d": {"inputs": ["close", "low", "open"], "func": trev_023_expected_shortfall_proxy_zscore_63d},
    "trev_024_expected_shortfall_proxy_rank_63d": {"inputs": ["close", "low", "open"], "func": trev_024_expected_shortfall_proxy_rank_63d},
    "trev_025_expected_shortfall_proxy_lvl_126d": {"inputs": ["close", "low", "open"], "func": trev_025_expected_shortfall_proxy_lvl_126d},
    "trev_026_expected_shortfall_proxy_zscore_126d": {"inputs": ["close", "low", "open"], "func": trev_026_expected_shortfall_proxy_zscore_126d},
    "trev_027_expected_shortfall_proxy_rank_126d": {"inputs": ["close", "low", "open"], "func": trev_027_expected_shortfall_proxy_rank_126d},
    "trev_028_expected_shortfall_proxy_lvl_252d": {"inputs": ["close", "low", "open"], "func": trev_028_expected_shortfall_proxy_lvl_252d},
    "trev_029_expected_shortfall_proxy_zscore_252d": {"inputs": ["close", "low", "open"], "func": trev_029_expected_shortfall_proxy_zscore_252d},
    "trev_030_expected_shortfall_proxy_rank_252d": {"inputs": ["close", "low", "open"], "func": trev_030_expected_shortfall_proxy_rank_252d},
    "trev_031_tail_event_density_lvl_5d": {"inputs": ["close", "low", "open"], "func": trev_031_tail_event_density_lvl_5d},
    "trev_032_tail_event_density_zscore_5d": {"inputs": ["close", "low", "open"], "func": trev_032_tail_event_density_zscore_5d},
    "trev_033_tail_event_density_rank_5d": {"inputs": ["close", "low", "open"], "func": trev_033_tail_event_density_rank_5d},
    "trev_034_tail_event_density_lvl_21d": {"inputs": ["close", "low", "open"], "func": trev_034_tail_event_density_lvl_21d},
    "trev_035_tail_event_density_zscore_21d": {"inputs": ["close", "low", "open"], "func": trev_035_tail_event_density_zscore_21d},
    "trev_036_tail_event_density_rank_21d": {"inputs": ["close", "low", "open"], "func": trev_036_tail_event_density_rank_21d},
    "trev_037_tail_event_density_lvl_63d": {"inputs": ["close", "low", "open"], "func": trev_037_tail_event_density_lvl_63d},
    "trev_038_tail_event_density_zscore_63d": {"inputs": ["close", "low", "open"], "func": trev_038_tail_event_density_zscore_63d},
    "trev_039_tail_event_density_rank_63d": {"inputs": ["close", "low", "open"], "func": trev_039_tail_event_density_rank_63d},
    "trev_040_tail_event_density_lvl_126d": {"inputs": ["close", "low", "open"], "func": trev_040_tail_event_density_lvl_126d},
    "trev_041_tail_event_density_zscore_126d": {"inputs": ["close", "low", "open"], "func": trev_041_tail_event_density_zscore_126d},
    "trev_042_tail_event_density_rank_126d": {"inputs": ["close", "low", "open"], "func": trev_042_tail_event_density_rank_126d},
    "trev_043_tail_event_density_lvl_252d": {"inputs": ["close", "low", "open"], "func": trev_043_tail_event_density_lvl_252d},
    "trev_044_tail_event_density_zscore_252d": {"inputs": ["close", "low", "open"], "func": trev_044_tail_event_density_zscore_252d},
    "trev_045_tail_event_density_rank_252d": {"inputs": ["close", "low", "open"], "func": trev_045_tail_event_density_rank_252d},
    "trev_046_skewness_252d_lvl_5d": {"inputs": ["close", "low", "open"], "func": trev_046_skewness_252d_lvl_5d},
    "trev_047_skewness_252d_zscore_5d": {"inputs": ["close", "low", "open"], "func": trev_047_skewness_252d_zscore_5d},
    "trev_048_skewness_252d_rank_5d": {"inputs": ["close", "low", "open"], "func": trev_048_skewness_252d_rank_5d},
    "trev_049_skewness_252d_lvl_21d": {"inputs": ["close", "low", "open"], "func": trev_049_skewness_252d_lvl_21d},
    "trev_050_skewness_252d_zscore_21d": {"inputs": ["close", "low", "open"], "func": trev_050_skewness_252d_zscore_21d},
    "trev_051_skewness_252d_rank_21d": {"inputs": ["close", "low", "open"], "func": trev_051_skewness_252d_rank_21d},
    "trev_052_skewness_252d_lvl_63d": {"inputs": ["close", "low", "open"], "func": trev_052_skewness_252d_lvl_63d},
    "trev_053_skewness_252d_zscore_63d": {"inputs": ["close", "low", "open"], "func": trev_053_skewness_252d_zscore_63d},
    "trev_054_skewness_252d_rank_63d": {"inputs": ["close", "low", "open"], "func": trev_054_skewness_252d_rank_63d},
    "trev_055_skewness_252d_lvl_126d": {"inputs": ["close", "low", "open"], "func": trev_055_skewness_252d_lvl_126d},
    "trev_056_skewness_252d_zscore_126d": {"inputs": ["close", "low", "open"], "func": trev_056_skewness_252d_zscore_126d},
    "trev_057_skewness_252d_rank_126d": {"inputs": ["close", "low", "open"], "func": trev_057_skewness_252d_rank_126d},
    "trev_058_skewness_252d_lvl_252d": {"inputs": ["close", "low", "open"], "func": trev_058_skewness_252d_lvl_252d},
    "trev_059_skewness_252d_zscore_252d": {"inputs": ["close", "low", "open"], "func": trev_059_skewness_252d_zscore_252d},
    "trev_060_skewness_252d_rank_252d": {"inputs": ["close", "low", "open"], "func": trev_060_skewness_252d_rank_252d},
    "trev_061_kurtosis_252d_lvl_5d": {"inputs": ["close", "low", "open"], "func": trev_061_kurtosis_252d_lvl_5d},
    "trev_062_kurtosis_252d_zscore_5d": {"inputs": ["close", "low", "open"], "func": trev_062_kurtosis_252d_zscore_5d},
    "trev_063_kurtosis_252d_rank_5d": {"inputs": ["close", "low", "open"], "func": trev_063_kurtosis_252d_rank_5d},
    "trev_064_kurtosis_252d_lvl_21d": {"inputs": ["close", "low", "open"], "func": trev_064_kurtosis_252d_lvl_21d},
    "trev_065_kurtosis_252d_zscore_21d": {"inputs": ["close", "low", "open"], "func": trev_065_kurtosis_252d_zscore_21d},
    "trev_066_kurtosis_252d_rank_21d": {"inputs": ["close", "low", "open"], "func": trev_066_kurtosis_252d_rank_21d},
    "trev_067_kurtosis_252d_lvl_63d": {"inputs": ["close", "low", "open"], "func": trev_067_kurtosis_252d_lvl_63d},
    "trev_068_kurtosis_252d_zscore_63d": {"inputs": ["close", "low", "open"], "func": trev_068_kurtosis_252d_zscore_63d},
    "trev_069_kurtosis_252d_rank_63d": {"inputs": ["close", "low", "open"], "func": trev_069_kurtosis_252d_rank_63d},
    "trev_070_kurtosis_252d_lvl_126d": {"inputs": ["close", "low", "open"], "func": trev_070_kurtosis_252d_lvl_126d},
    "trev_071_kurtosis_252d_zscore_126d": {"inputs": ["close", "low", "open"], "func": trev_071_kurtosis_252d_zscore_126d},
    "trev_072_kurtosis_252d_rank_126d": {"inputs": ["close", "low", "open"], "func": trev_072_kurtosis_252d_rank_126d},
    "trev_073_kurtosis_252d_lvl_252d": {"inputs": ["close", "low", "open"], "func": trev_073_kurtosis_252d_lvl_252d},
    "trev_074_kurtosis_252d_zscore_252d": {"inputs": ["close", "low", "open"], "func": trev_074_kurtosis_252d_zscore_252d},
    "trev_075_kurtosis_252d_rank_252d": {"inputs": ["close", "low", "open"], "func": trev_075_kurtosis_252d_rank_252d},
    "trev_076_tail_ratio_lvl_5d": {"inputs": ["close", "low", "open"], "func": trev_076_tail_ratio_lvl_5d},
    "trev_077_tail_ratio_zscore_5d": {"inputs": ["close", "low", "open"], "func": trev_077_tail_ratio_zscore_5d},
    "trev_078_tail_ratio_rank_5d": {"inputs": ["close", "low", "open"], "func": trev_078_tail_ratio_rank_5d},
    "trev_079_tail_ratio_lvl_21d": {"inputs": ["close", "low", "open"], "func": trev_079_tail_ratio_lvl_21d},
    "trev_080_tail_ratio_zscore_21d": {"inputs": ["close", "low", "open"], "func": trev_080_tail_ratio_zscore_21d},
    "trev_081_tail_ratio_rank_21d": {"inputs": ["close", "low", "open"], "func": trev_081_tail_ratio_rank_21d},
    "trev_082_tail_ratio_lvl_63d": {"inputs": ["close", "low", "open"], "func": trev_082_tail_ratio_lvl_63d},
    "trev_083_tail_ratio_zscore_63d": {"inputs": ["close", "low", "open"], "func": trev_083_tail_ratio_zscore_63d},
    "trev_084_tail_ratio_rank_63d": {"inputs": ["close", "low", "open"], "func": trev_084_tail_ratio_rank_63d},
    "trev_085_tail_ratio_lvl_126d": {"inputs": ["close", "low", "open"], "func": trev_085_tail_ratio_lvl_126d},
    "trev_086_tail_ratio_zscore_126d": {"inputs": ["close", "low", "open"], "func": trev_086_tail_ratio_zscore_126d},
    "trev_087_tail_ratio_rank_126d": {"inputs": ["close", "low", "open"], "func": trev_087_tail_ratio_rank_126d},
    "trev_088_tail_ratio_lvl_252d": {"inputs": ["close", "low", "open"], "func": trev_088_tail_ratio_lvl_252d},
    "trev_089_tail_ratio_zscore_252d": {"inputs": ["close", "low", "open"], "func": trev_089_tail_ratio_zscore_252d},
    "trev_090_tail_ratio_rank_252d": {"inputs": ["close", "low", "open"], "func": trev_090_tail_ratio_rank_252d},
    "trev_091_extreme_low_z_lvl_5d": {"inputs": ["close", "low", "open"], "func": trev_091_extreme_low_z_lvl_5d},
    "trev_092_extreme_low_z_zscore_5d": {"inputs": ["close", "low", "open"], "func": trev_092_extreme_low_z_zscore_5d},
    "trev_093_extreme_low_z_rank_5d": {"inputs": ["close", "low", "open"], "func": trev_093_extreme_low_z_rank_5d},
    "trev_094_extreme_low_z_lvl_21d": {"inputs": ["close", "low", "open"], "func": trev_094_extreme_low_z_lvl_21d},
    "trev_095_extreme_low_z_zscore_21d": {"inputs": ["close", "low", "open"], "func": trev_095_extreme_low_z_zscore_21d},
    "trev_096_extreme_low_z_rank_21d": {"inputs": ["close", "low", "open"], "func": trev_096_extreme_low_z_rank_21d},
    "trev_097_extreme_low_z_lvl_63d": {"inputs": ["close", "low", "open"], "func": trev_097_extreme_low_z_lvl_63d},
    "trev_098_extreme_low_z_zscore_63d": {"inputs": ["close", "low", "open"], "func": trev_098_extreme_low_z_zscore_63d},
    "trev_099_extreme_low_z_rank_63d": {"inputs": ["close", "low", "open"], "func": trev_099_extreme_low_z_rank_63d},
    "trev_100_extreme_low_z_lvl_126d": {"inputs": ["close", "low", "open"], "func": trev_100_extreme_low_z_lvl_126d},
    "trev_101_extreme_low_z_zscore_126d": {"inputs": ["close", "low", "open"], "func": trev_101_extreme_low_z_zscore_126d},
    "trev_102_extreme_low_z_rank_126d": {"inputs": ["close", "low", "open"], "func": trev_102_extreme_low_z_rank_126d},
    "trev_103_extreme_low_z_lvl_252d": {"inputs": ["close", "low", "open"], "func": trev_103_extreme_low_z_lvl_252d},
    "trev_104_extreme_low_z_zscore_252d": {"inputs": ["close", "low", "open"], "func": trev_104_extreme_low_z_zscore_252d},
    "trev_105_extreme_low_z_rank_252d": {"inputs": ["close", "low", "open"], "func": trev_105_extreme_low_z_rank_252d},
    "trev_106_tail_risk_momentum_lvl_5d": {"inputs": ["close", "low", "open"], "func": trev_106_tail_risk_momentum_lvl_5d},
    "trev_107_tail_risk_momentum_zscore_5d": {"inputs": ["close", "low", "open"], "func": trev_107_tail_risk_momentum_zscore_5d},
    "trev_108_tail_risk_momentum_rank_5d": {"inputs": ["close", "low", "open"], "func": trev_108_tail_risk_momentum_rank_5d},
    "trev_109_tail_risk_momentum_lvl_21d": {"inputs": ["close", "low", "open"], "func": trev_109_tail_risk_momentum_lvl_21d},
    "trev_110_tail_risk_momentum_zscore_21d": {"inputs": ["close", "low", "open"], "func": trev_110_tail_risk_momentum_zscore_21d},
    "trev_111_tail_risk_momentum_rank_21d": {"inputs": ["close", "low", "open"], "func": trev_111_tail_risk_momentum_rank_21d},
    "trev_112_tail_risk_momentum_lvl_63d": {"inputs": ["close", "low", "open"], "func": trev_112_tail_risk_momentum_lvl_63d},
    "trev_113_tail_risk_momentum_zscore_63d": {"inputs": ["close", "low", "open"], "func": trev_113_tail_risk_momentum_zscore_63d},
    "trev_114_tail_risk_momentum_rank_63d": {"inputs": ["close", "low", "open"], "func": trev_114_tail_risk_momentum_rank_63d},
    "trev_115_tail_risk_momentum_lvl_126d": {"inputs": ["close", "low", "open"], "func": trev_115_tail_risk_momentum_lvl_126d},
    "trev_116_tail_risk_momentum_zscore_126d": {"inputs": ["close", "low", "open"], "func": trev_116_tail_risk_momentum_zscore_126d},
    "trev_117_tail_risk_momentum_rank_126d": {"inputs": ["close", "low", "open"], "func": trev_117_tail_risk_momentum_rank_126d},
    "trev_118_tail_risk_momentum_lvl_252d": {"inputs": ["close", "low", "open"], "func": trev_118_tail_risk_momentum_lvl_252d},
    "trev_119_tail_risk_momentum_zscore_252d": {"inputs": ["close", "low", "open"], "func": trev_119_tail_risk_momentum_zscore_252d},
    "trev_120_tail_risk_momentum_rank_252d": {"inputs": ["close", "low", "open"], "func": trev_120_tail_risk_momentum_rank_252d},
}
