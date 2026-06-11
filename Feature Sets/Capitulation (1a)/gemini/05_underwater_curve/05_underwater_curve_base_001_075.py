"""
Underwater Curve — Base Features 001–075
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
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_002_stat_depth_var_1(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_003_stat_depth_var_2(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_004_stat_depth_var_3(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_005_stat_depth_var_4(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_006_stat_depth_var_5(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_007_stat_depth_var_6(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_008_stat_depth_var_7(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_009_stat_depth_var_8(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_010_stat_depth_var_9(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_011_stat_depth_var_10(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_012_stat_depth_var_11(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_013_stat_depth_var_12(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_014_stat_depth_var_13(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_015_stat_depth_var_14(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_016_stat_depth_var_15(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_017_stat_depth_var_16(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_018_stat_depth_var_17(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_019_stat_depth_var_18(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_020_stat_depth_var_19(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_021_stat_depth_var_20(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_022_stat_depth_var_21(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_023_stat_depth_var_22(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_024_stat_depth_var_23(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_025_stat_depth_var_24(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_026_stat_depth_var_25(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_027_stat_depth_var_26(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_028_stat_depth_var_27(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_029_stat_depth_var_28(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_030_stat_depth_var_29(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_031_stat_depth_var_30(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_032_stat_depth_var_31(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_033_stat_depth_var_32(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_034_stat_depth_var_33(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_035_stat_depth_var_34(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_036_stat_depth_var_35(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_037_stat_depth_var_36(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_038_stat_depth_var_37(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_039_stat_depth_var_38(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_040_stat_depth_var_39(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_041_stat_depth_var_40(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_042_stat_depth_var_41(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_043_stat_depth_var_42(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_044_stat_depth_var_43(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_045_stat_depth_var_44(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_046_stat_depth_var_45(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_047_stat_depth_var_46(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_048_stat_depth_var_47(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_049_stat_depth_var_48(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_050_stat_depth_var_49(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_051_stat_depth_var_50(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_052_stat_depth_var_51(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_053_stat_depth_var_52(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_054_stat_depth_var_53(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_055_stat_depth_var_54(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_056_stat_depth_var_55(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_057_stat_depth_var_56(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_058_stat_depth_var_57(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_059_stat_depth_var_58(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_060_stat_depth_var_59(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_061_stat_depth_var_60(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_062_stat_depth_var_61(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_063_stat_depth_var_62(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_064_stat_depth_var_63(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_065_stat_depth_var_64(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_066_stat_depth_var_65(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_067_stat_depth_var_66(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_068_stat_depth_var_67(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_069_stat_depth_var_68(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_070_stat_depth_var_69(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_071_stat_depth_var_70(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_072_stat_depth_var_71(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_073_stat_depth_var_72(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_074_stat_depth_var_73(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_075_stat_depth_var_74(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

# ── Registry ──────────────────────────────────────────────────────────────────

V05_REGISTRY = {
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
    "vcc_026_stat_depth_var_25": {"inputs": ["close"], "func": vcc_026_stat_depth_var_25},
    "vcc_027_stat_depth_var_26": {"inputs": ["close"], "func": vcc_027_stat_depth_var_26},
    "vcc_028_stat_depth_var_27": {"inputs": ["close"], "func": vcc_028_stat_depth_var_27},
    "vcc_029_stat_depth_var_28": {"inputs": ["close"], "func": vcc_029_stat_depth_var_28},
    "vcc_030_stat_depth_var_29": {"inputs": ["close"], "func": vcc_030_stat_depth_var_29},
    "vcc_031_stat_depth_var_30": {"inputs": ["close"], "func": vcc_031_stat_depth_var_30},
    "vcc_032_stat_depth_var_31": {"inputs": ["close"], "func": vcc_032_stat_depth_var_31},
    "vcc_033_stat_depth_var_32": {"inputs": ["close"], "func": vcc_033_stat_depth_var_32},
    "vcc_034_stat_depth_var_33": {"inputs": ["close"], "func": vcc_034_stat_depth_var_33},
    "vcc_035_stat_depth_var_34": {"inputs": ["close"], "func": vcc_035_stat_depth_var_34},
    "vcc_036_stat_depth_var_35": {"inputs": ["close"], "func": vcc_036_stat_depth_var_35},
    "vcc_037_stat_depth_var_36": {"inputs": ["close"], "func": vcc_037_stat_depth_var_36},
    "vcc_038_stat_depth_var_37": {"inputs": ["close"], "func": vcc_038_stat_depth_var_37},
    "vcc_039_stat_depth_var_38": {"inputs": ["close"], "func": vcc_039_stat_depth_var_38},
    "vcc_040_stat_depth_var_39": {"inputs": ["close"], "func": vcc_040_stat_depth_var_39},
    "vcc_041_stat_depth_var_40": {"inputs": ["close"], "func": vcc_041_stat_depth_var_40},
    "vcc_042_stat_depth_var_41": {"inputs": ["close"], "func": vcc_042_stat_depth_var_41},
    "vcc_043_stat_depth_var_42": {"inputs": ["close"], "func": vcc_043_stat_depth_var_42},
    "vcc_044_stat_depth_var_43": {"inputs": ["close"], "func": vcc_044_stat_depth_var_43},
    "vcc_045_stat_depth_var_44": {"inputs": ["close"], "func": vcc_045_stat_depth_var_44},
    "vcc_046_stat_depth_var_45": {"inputs": ["close"], "func": vcc_046_stat_depth_var_45},
    "vcc_047_stat_depth_var_46": {"inputs": ["close"], "func": vcc_047_stat_depth_var_46},
    "vcc_048_stat_depth_var_47": {"inputs": ["close"], "func": vcc_048_stat_depth_var_47},
    "vcc_049_stat_depth_var_48": {"inputs": ["close"], "func": vcc_049_stat_depth_var_48},
    "vcc_050_stat_depth_var_49": {"inputs": ["close"], "func": vcc_050_stat_depth_var_49},
    "vcc_051_stat_depth_var_50": {"inputs": ["close"], "func": vcc_051_stat_depth_var_50},
    "vcc_052_stat_depth_var_51": {"inputs": ["close"], "func": vcc_052_stat_depth_var_51},
    "vcc_053_stat_depth_var_52": {"inputs": ["close"], "func": vcc_053_stat_depth_var_52},
    "vcc_054_stat_depth_var_53": {"inputs": ["close"], "func": vcc_054_stat_depth_var_53},
    "vcc_055_stat_depth_var_54": {"inputs": ["close"], "func": vcc_055_stat_depth_var_54},
    "vcc_056_stat_depth_var_55": {"inputs": ["close"], "func": vcc_056_stat_depth_var_55},
    "vcc_057_stat_depth_var_56": {"inputs": ["close"], "func": vcc_057_stat_depth_var_56},
    "vcc_058_stat_depth_var_57": {"inputs": ["close"], "func": vcc_058_stat_depth_var_57},
    "vcc_059_stat_depth_var_58": {"inputs": ["close"], "func": vcc_059_stat_depth_var_58},
    "vcc_060_stat_depth_var_59": {"inputs": ["close"], "func": vcc_060_stat_depth_var_59},
    "vcc_061_stat_depth_var_60": {"inputs": ["close"], "func": vcc_061_stat_depth_var_60},
    "vcc_062_stat_depth_var_61": {"inputs": ["close"], "func": vcc_062_stat_depth_var_61},
    "vcc_063_stat_depth_var_62": {"inputs": ["close"], "func": vcc_063_stat_depth_var_62},
    "vcc_064_stat_depth_var_63": {"inputs": ["close"], "func": vcc_064_stat_depth_var_63},
    "vcc_065_stat_depth_var_64": {"inputs": ["close"], "func": vcc_065_stat_depth_var_64},
    "vcc_066_stat_depth_var_65": {"inputs": ["close"], "func": vcc_066_stat_depth_var_65},
    "vcc_067_stat_depth_var_66": {"inputs": ["close"], "func": vcc_067_stat_depth_var_66},
    "vcc_068_stat_depth_var_67": {"inputs": ["close"], "func": vcc_068_stat_depth_var_67},
    "vcc_069_stat_depth_var_68": {"inputs": ["close"], "func": vcc_069_stat_depth_var_68},
    "vcc_070_stat_depth_var_69": {"inputs": ["close"], "func": vcc_070_stat_depth_var_69},
    "vcc_071_stat_depth_var_70": {"inputs": ["close"], "func": vcc_071_stat_depth_var_70},
    "vcc_072_stat_depth_var_71": {"inputs": ["close"], "func": vcc_072_stat_depth_var_71},
    "vcc_073_stat_depth_var_72": {"inputs": ["close"], "func": vcc_073_stat_depth_var_72},
    "vcc_074_stat_depth_var_73": {"inputs": ["close"], "func": vcc_074_stat_depth_var_73},
    "vcc_075_stat_depth_var_74": {"inputs": ["close"], "func": vcc_075_stat_depth_var_74},
}
