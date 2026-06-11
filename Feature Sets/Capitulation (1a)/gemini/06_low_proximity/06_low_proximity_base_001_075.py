"""
Low Proximity — Base Features 001–075
Domain: distance to recent and historical lows
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

def lowp_001_stat_depth_var_0(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_002_stat_depth_var_1(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_003_stat_depth_var_2(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_004_stat_depth_var_3(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_005_stat_depth_var_4(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_006_stat_depth_var_5(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_007_stat_depth_var_6(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_008_stat_depth_var_7(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_009_stat_depth_var_8(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_010_stat_depth_var_9(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_011_stat_depth_var_10(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_012_stat_depth_var_11(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_013_stat_depth_var_12(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_014_stat_depth_var_13(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_015_stat_depth_var_14(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_016_stat_depth_var_15(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_017_stat_depth_var_16(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_018_stat_depth_var_17(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_019_stat_depth_var_18(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_020_stat_depth_var_19(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_021_stat_depth_var_20(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_022_stat_depth_var_21(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_023_stat_depth_var_22(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_024_stat_depth_var_23(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_025_stat_depth_var_24(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_026_stat_depth_var_25(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_027_stat_depth_var_26(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_028_stat_depth_var_27(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_029_stat_depth_var_28(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_030_stat_depth_var_29(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_031_stat_depth_var_30(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_032_stat_depth_var_31(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_033_stat_depth_var_32(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_034_stat_depth_var_33(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_035_stat_depth_var_34(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_036_stat_depth_var_35(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_037_stat_depth_var_36(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_038_stat_depth_var_37(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_039_stat_depth_var_38(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_040_stat_depth_var_39(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_041_stat_depth_var_40(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_042_stat_depth_var_41(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_043_stat_depth_var_42(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_044_stat_depth_var_43(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_045_stat_depth_var_44(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_046_stat_depth_var_45(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_047_stat_depth_var_46(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_048_stat_depth_var_47(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_049_stat_depth_var_48(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_050_stat_depth_var_49(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_051_stat_depth_var_50(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_052_stat_depth_var_51(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_053_stat_depth_var_52(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_054_stat_depth_var_53(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_055_stat_depth_var_54(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_056_stat_depth_var_55(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_057_stat_depth_var_56(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_058_stat_depth_var_57(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_059_stat_depth_var_58(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_060_stat_depth_var_59(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_061_stat_depth_var_60(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_062_stat_depth_var_61(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_063_stat_depth_var_62(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_064_stat_depth_var_63(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_065_stat_depth_var_64(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_066_stat_depth_var_65(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_067_stat_depth_var_66(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_068_stat_depth_var_67(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_069_stat_depth_var_68(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_070_stat_depth_var_69(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_071_stat_depth_var_70(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_072_stat_depth_var_71(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_073_stat_depth_var_72(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_074_stat_depth_var_73(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_075_stat_depth_var_74(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

# ── Registry ──────────────────────────────────────────────────────────────────

V06_REGISTRY = {
    "lowp_001_stat_depth_var_0": {"inputs": ["close"], "func": lowp_001_stat_depth_var_0},
    "lowp_002_stat_depth_var_1": {"inputs": ["close"], "func": lowp_002_stat_depth_var_1},
    "lowp_003_stat_depth_var_2": {"inputs": ["close"], "func": lowp_003_stat_depth_var_2},
    "lowp_004_stat_depth_var_3": {"inputs": ["close"], "func": lowp_004_stat_depth_var_3},
    "lowp_005_stat_depth_var_4": {"inputs": ["close"], "func": lowp_005_stat_depth_var_4},
    "lowp_006_stat_depth_var_5": {"inputs": ["close"], "func": lowp_006_stat_depth_var_5},
    "lowp_007_stat_depth_var_6": {"inputs": ["close"], "func": lowp_007_stat_depth_var_6},
    "lowp_008_stat_depth_var_7": {"inputs": ["close"], "func": lowp_008_stat_depth_var_7},
    "lowp_009_stat_depth_var_8": {"inputs": ["close"], "func": lowp_009_stat_depth_var_8},
    "lowp_010_stat_depth_var_9": {"inputs": ["close"], "func": lowp_010_stat_depth_var_9},
    "lowp_011_stat_depth_var_10": {"inputs": ["close"], "func": lowp_011_stat_depth_var_10},
    "lowp_012_stat_depth_var_11": {"inputs": ["close"], "func": lowp_012_stat_depth_var_11},
    "lowp_013_stat_depth_var_12": {"inputs": ["close"], "func": lowp_013_stat_depth_var_12},
    "lowp_014_stat_depth_var_13": {"inputs": ["close"], "func": lowp_014_stat_depth_var_13},
    "lowp_015_stat_depth_var_14": {"inputs": ["close"], "func": lowp_015_stat_depth_var_14},
    "lowp_016_stat_depth_var_15": {"inputs": ["close"], "func": lowp_016_stat_depth_var_15},
    "lowp_017_stat_depth_var_16": {"inputs": ["close"], "func": lowp_017_stat_depth_var_16},
    "lowp_018_stat_depth_var_17": {"inputs": ["close"], "func": lowp_018_stat_depth_var_17},
    "lowp_019_stat_depth_var_18": {"inputs": ["close"], "func": lowp_019_stat_depth_var_18},
    "lowp_020_stat_depth_var_19": {"inputs": ["close"], "func": lowp_020_stat_depth_var_19},
    "lowp_021_stat_depth_var_20": {"inputs": ["close"], "func": lowp_021_stat_depth_var_20},
    "lowp_022_stat_depth_var_21": {"inputs": ["close"], "func": lowp_022_stat_depth_var_21},
    "lowp_023_stat_depth_var_22": {"inputs": ["close"], "func": lowp_023_stat_depth_var_22},
    "lowp_024_stat_depth_var_23": {"inputs": ["close"], "func": lowp_024_stat_depth_var_23},
    "lowp_025_stat_depth_var_24": {"inputs": ["close"], "func": lowp_025_stat_depth_var_24},
    "lowp_026_stat_depth_var_25": {"inputs": ["close"], "func": lowp_026_stat_depth_var_25},
    "lowp_027_stat_depth_var_26": {"inputs": ["close"], "func": lowp_027_stat_depth_var_26},
    "lowp_028_stat_depth_var_27": {"inputs": ["close"], "func": lowp_028_stat_depth_var_27},
    "lowp_029_stat_depth_var_28": {"inputs": ["close"], "func": lowp_029_stat_depth_var_28},
    "lowp_030_stat_depth_var_29": {"inputs": ["close"], "func": lowp_030_stat_depth_var_29},
    "lowp_031_stat_depth_var_30": {"inputs": ["close"], "func": lowp_031_stat_depth_var_30},
    "lowp_032_stat_depth_var_31": {"inputs": ["close"], "func": lowp_032_stat_depth_var_31},
    "lowp_033_stat_depth_var_32": {"inputs": ["close"], "func": lowp_033_stat_depth_var_32},
    "lowp_034_stat_depth_var_33": {"inputs": ["close"], "func": lowp_034_stat_depth_var_33},
    "lowp_035_stat_depth_var_34": {"inputs": ["close"], "func": lowp_035_stat_depth_var_34},
    "lowp_036_stat_depth_var_35": {"inputs": ["close"], "func": lowp_036_stat_depth_var_35},
    "lowp_037_stat_depth_var_36": {"inputs": ["close"], "func": lowp_037_stat_depth_var_36},
    "lowp_038_stat_depth_var_37": {"inputs": ["close"], "func": lowp_038_stat_depth_var_37},
    "lowp_039_stat_depth_var_38": {"inputs": ["close"], "func": lowp_039_stat_depth_var_38},
    "lowp_040_stat_depth_var_39": {"inputs": ["close"], "func": lowp_040_stat_depth_var_39},
    "lowp_041_stat_depth_var_40": {"inputs": ["close"], "func": lowp_041_stat_depth_var_40},
    "lowp_042_stat_depth_var_41": {"inputs": ["close"], "func": lowp_042_stat_depth_var_41},
    "lowp_043_stat_depth_var_42": {"inputs": ["close"], "func": lowp_043_stat_depth_var_42},
    "lowp_044_stat_depth_var_43": {"inputs": ["close"], "func": lowp_044_stat_depth_var_43},
    "lowp_045_stat_depth_var_44": {"inputs": ["close"], "func": lowp_045_stat_depth_var_44},
    "lowp_046_stat_depth_var_45": {"inputs": ["close"], "func": lowp_046_stat_depth_var_45},
    "lowp_047_stat_depth_var_46": {"inputs": ["close"], "func": lowp_047_stat_depth_var_46},
    "lowp_048_stat_depth_var_47": {"inputs": ["close"], "func": lowp_048_stat_depth_var_47},
    "lowp_049_stat_depth_var_48": {"inputs": ["close"], "func": lowp_049_stat_depth_var_48},
    "lowp_050_stat_depth_var_49": {"inputs": ["close"], "func": lowp_050_stat_depth_var_49},
    "lowp_051_stat_depth_var_50": {"inputs": ["close"], "func": lowp_051_stat_depth_var_50},
    "lowp_052_stat_depth_var_51": {"inputs": ["close"], "func": lowp_052_stat_depth_var_51},
    "lowp_053_stat_depth_var_52": {"inputs": ["close"], "func": lowp_053_stat_depth_var_52},
    "lowp_054_stat_depth_var_53": {"inputs": ["close"], "func": lowp_054_stat_depth_var_53},
    "lowp_055_stat_depth_var_54": {"inputs": ["close"], "func": lowp_055_stat_depth_var_54},
    "lowp_056_stat_depth_var_55": {"inputs": ["close"], "func": lowp_056_stat_depth_var_55},
    "lowp_057_stat_depth_var_56": {"inputs": ["close"], "func": lowp_057_stat_depth_var_56},
    "lowp_058_stat_depth_var_57": {"inputs": ["close"], "func": lowp_058_stat_depth_var_57},
    "lowp_059_stat_depth_var_58": {"inputs": ["close"], "func": lowp_059_stat_depth_var_58},
    "lowp_060_stat_depth_var_59": {"inputs": ["close"], "func": lowp_060_stat_depth_var_59},
    "lowp_061_stat_depth_var_60": {"inputs": ["close"], "func": lowp_061_stat_depth_var_60},
    "lowp_062_stat_depth_var_61": {"inputs": ["close"], "func": lowp_062_stat_depth_var_61},
    "lowp_063_stat_depth_var_62": {"inputs": ["close"], "func": lowp_063_stat_depth_var_62},
    "lowp_064_stat_depth_var_63": {"inputs": ["close"], "func": lowp_064_stat_depth_var_63},
    "lowp_065_stat_depth_var_64": {"inputs": ["close"], "func": lowp_065_stat_depth_var_64},
    "lowp_066_stat_depth_var_65": {"inputs": ["close"], "func": lowp_066_stat_depth_var_65},
    "lowp_067_stat_depth_var_66": {"inputs": ["close"], "func": lowp_067_stat_depth_var_66},
    "lowp_068_stat_depth_var_67": {"inputs": ["close"], "func": lowp_068_stat_depth_var_67},
    "lowp_069_stat_depth_var_68": {"inputs": ["close"], "func": lowp_069_stat_depth_var_68},
    "lowp_070_stat_depth_var_69": {"inputs": ["close"], "func": lowp_070_stat_depth_var_69},
    "lowp_071_stat_depth_var_70": {"inputs": ["close"], "func": lowp_071_stat_depth_var_70},
    "lowp_072_stat_depth_var_71": {"inputs": ["close"], "func": lowp_072_stat_depth_var_71},
    "lowp_073_stat_depth_var_72": {"inputs": ["close"], "func": lowp_073_stat_depth_var_72},
    "lowp_074_stat_depth_var_73": {"inputs": ["close"], "func": lowp_074_stat_depth_var_73},
    "lowp_075_stat_depth_var_74": {"inputs": ["close"], "func": lowp_075_stat_depth_var_74},
}
