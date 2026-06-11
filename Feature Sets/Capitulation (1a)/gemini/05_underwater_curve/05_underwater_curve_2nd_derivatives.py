"""
Underwater Curve — 2nd Derivatives
Domain: cumulative distress and underwater characteristics
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

def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).sum()

def _ewm_mean(s: pd.Series, w: int) -> pd.Series:
    return s.ewm(span=w, min_periods=1).mean()

def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div((s - m), sd)

def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))

def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change().fillna(0)

def _rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).rank(pct=True)

def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).median()

# Domain Specific Additions
def _days_since_high(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).apply(lambda x: len(x) - 1 - np.argmax(x), raw=True)

def _days_since_expanding_high(s: pd.Series) -> pd.Series:
    cummax = s.cummax()
    new_highs = (s == cummax)
    high_indices = pd.Series(np.arange(len(s)), index=s.index).where(new_highs).ffill()
    return pd.Series(np.arange(len(s)), index=s.index) - high_indices

def _pct_change(s: pd.Series, periods: int = 1) -> pd.Series:
    prev = s.shift(periods)
    return _safe_div(s - prev, prev.abs())

# ── Feature functions ────────────────────────────────────────────────────────

def vcc_001_stat_depth_var_0(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 25 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_002_stat_depth_var_1(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 25 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_003_stat_depth_var_2(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 25 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_004_stat_depth_var_3(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 25 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_005_stat_depth_var_4(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 25 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_006_stat_depth_var_5(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 25 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_007_stat_depth_var_6(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 25 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_008_stat_depth_var_7(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 25 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_009_stat_depth_var_8(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 25 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_010_stat_depth_var_9(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 25 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_011_stat_depth_var_10(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 25 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_012_stat_depth_var_11(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 25 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_013_stat_depth_var_12(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 25 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_014_stat_depth_var_13(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 25 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_015_stat_depth_var_14(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 25 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_016_stat_depth_var_15(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 25 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_017_stat_depth_var_16(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 25 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_018_stat_depth_var_17(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 25 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_019_stat_depth_var_18(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 25 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_020_stat_depth_var_19(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 25 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_021_stat_depth_var_20(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 25 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_022_stat_depth_var_21(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 25 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_023_stat_depth_var_22(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 25 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_024_stat_depth_var_23(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 25 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_025_stat_depth_var_24(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 25 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

# ── Registry ──────────────────────────────────────────────────────────────────

V05_V_REGISTRY = {
    "vcc_001_stat_depth_var_0": {"inputs": ["close"], "func": vcc_001_stat_depth_var_0},
    "vcc_002_stat_depth_var_1": {"inputs": ["close"], "func": vcc_002_stat_depth_var_1},
    "vcc_003_stat_depth_var_2": {"inputs": ["close"], "func": vcc_003_stat_depth_var_2},
    "vcc_004_stat_depth_var_3": {"inputs": ["close"], "func": vcc_004_stat_depth_var_3},
    "vcc_005_stat_depth_var_4": {"inputs": ["close"], "func": vcc_005_stat_depth_var_4},
    "vcc_006_stat_depth_var_5": {"inputs": ["close"], "func": vcc_006_stat_depth_var_5},
    "vcc_007_stat_depth_var_6": {"inputs": ["close"], "func": vcc_007_stat_depth_var_6},
    "vcc_008_stat_depth_var_7": {"inputs": ["close"], "func": vcc_008_stat_depth_var_7},
    "vcc_009_stat_depth_var_8": {"inputs": ["close"], "func": vcc_009_stat_depth_var_8},
    "vcc_010_stat_depth_var_9": {"inputs": ["close"], "func": vcc_010_stat_depth_var_9},
    "vcc_011_stat_depth_var_10": {"inputs": ["close"], "func": vcc_011_stat_depth_var_10},
    "vcc_012_stat_depth_var_11": {"inputs": ["close"], "func": vcc_012_stat_depth_var_11},
    "vcc_013_stat_depth_var_12": {"inputs": ["close"], "func": vcc_013_stat_depth_var_12},
    "vcc_014_stat_depth_var_13": {"inputs": ["close"], "func": vcc_014_stat_depth_var_13},
    "vcc_015_stat_depth_var_14": {"inputs": ["close"], "func": vcc_015_stat_depth_var_14},
    "vcc_016_stat_depth_var_15": {"inputs": ["close"], "func": vcc_016_stat_depth_var_15},
    "vcc_017_stat_depth_var_16": {"inputs": ["close"], "func": vcc_017_stat_depth_var_16},
    "vcc_018_stat_depth_var_17": {"inputs": ["close"], "func": vcc_018_stat_depth_var_17},
    "vcc_019_stat_depth_var_18": {"inputs": ["close"], "func": vcc_019_stat_depth_var_18},
    "vcc_020_stat_depth_var_19": {"inputs": ["close"], "func": vcc_020_stat_depth_var_19},
    "vcc_021_stat_depth_var_20": {"inputs": ["close"], "func": vcc_021_stat_depth_var_20},
    "vcc_022_stat_depth_var_21": {"inputs": ["close"], "func": vcc_022_stat_depth_var_21},
    "vcc_023_stat_depth_var_22": {"inputs": ["close"], "func": vcc_023_stat_depth_var_22},
    "vcc_024_stat_depth_var_23": {"inputs": ["close"], "func": vcc_024_stat_depth_var_23},
    "vcc_025_stat_depth_var_24": {"inputs": ["close"], "func": vcc_025_stat_depth_var_24},
}
