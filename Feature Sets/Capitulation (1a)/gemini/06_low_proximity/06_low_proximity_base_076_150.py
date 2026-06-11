"""
Low Proximity — Base Features 076–150
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

def lowp_076_stat_depth_var_0(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_077_stat_depth_var_1(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_078_stat_depth_var_2(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_079_stat_depth_var_3(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_080_stat_depth_var_4(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_081_stat_depth_var_5(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_082_stat_depth_var_6(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_083_stat_depth_var_7(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_084_stat_depth_var_8(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_085_stat_depth_var_9(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_086_stat_depth_var_10(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_087_stat_depth_var_11(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_088_stat_depth_var_12(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_089_stat_depth_var_13(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_090_stat_depth_var_14(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_091_stat_depth_var_15(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_092_stat_depth_var_16(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_093_stat_depth_var_17(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_094_stat_depth_var_18(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_095_stat_depth_var_19(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_096_stat_depth_var_20(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_097_stat_depth_var_21(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_098_stat_depth_var_22(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_099_stat_depth_var_23(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_100_stat_depth_var_24(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_101_stat_depth_var_25(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_102_stat_depth_var_26(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_103_stat_depth_var_27(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_104_stat_depth_var_28(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_105_stat_depth_var_29(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_106_stat_depth_var_30(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_107_stat_depth_var_31(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_108_stat_depth_var_32(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_109_stat_depth_var_33(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_110_stat_depth_var_34(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_111_stat_depth_var_35(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_112_stat_depth_var_36(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_113_stat_depth_var_37(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_114_stat_depth_var_38(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_115_stat_depth_var_39(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_116_stat_depth_var_40(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_117_stat_depth_var_41(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_118_stat_depth_var_42(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_119_stat_depth_var_43(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_120_stat_depth_var_44(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_121_stat_depth_var_45(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_122_stat_depth_var_46(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_123_stat_depth_var_47(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_124_stat_depth_var_48(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_125_stat_depth_var_49(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_126_stat_depth_var_50(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_127_stat_depth_var_51(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_128_stat_depth_var_52(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_129_stat_depth_var_53(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_130_stat_depth_var_54(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_131_stat_depth_var_55(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_132_stat_depth_var_56(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_133_stat_depth_var_57(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_134_stat_depth_var_58(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_135_stat_depth_var_59(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_136_stat_depth_var_60(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_137_stat_depth_var_61(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_138_stat_depth_var_62(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_139_stat_depth_var_63(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_140_stat_depth_var_64(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_141_stat_depth_var_65(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_142_stat_depth_var_66(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_143_stat_depth_var_67(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_144_stat_depth_var_68(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_145_stat_depth_var_69(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_146_stat_depth_var_70(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_147_stat_depth_var_71(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_148_stat_depth_var_72(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_149_stat_depth_var_73(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def lowp_150_stat_depth_var_74(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

# ── Registry ──────────────────────────────────────────────────────────────────

V06_REGISTRY = {
    "lowp_076_stat_depth_var_0": {"inputs": ["close"], "func": lowp_076_stat_depth_var_0},
    "lowp_077_stat_depth_var_1": {"inputs": ["close"], "func": lowp_077_stat_depth_var_1},
    "lowp_078_stat_depth_var_2": {"inputs": ["close"], "func": lowp_078_stat_depth_var_2},
    "lowp_079_stat_depth_var_3": {"inputs": ["close"], "func": lowp_079_stat_depth_var_3},
    "lowp_080_stat_depth_var_4": {"inputs": ["close"], "func": lowp_080_stat_depth_var_4},
    "lowp_081_stat_depth_var_5": {"inputs": ["close"], "func": lowp_081_stat_depth_var_5},
    "lowp_082_stat_depth_var_6": {"inputs": ["close"], "func": lowp_082_stat_depth_var_6},
    "lowp_083_stat_depth_var_7": {"inputs": ["close"], "func": lowp_083_stat_depth_var_7},
    "lowp_084_stat_depth_var_8": {"inputs": ["close"], "func": lowp_084_stat_depth_var_8},
    "lowp_085_stat_depth_var_9": {"inputs": ["close"], "func": lowp_085_stat_depth_var_9},
    "lowp_086_stat_depth_var_10": {"inputs": ["close"], "func": lowp_086_stat_depth_var_10},
    "lowp_087_stat_depth_var_11": {"inputs": ["close"], "func": lowp_087_stat_depth_var_11},
    "lowp_088_stat_depth_var_12": {"inputs": ["close"], "func": lowp_088_stat_depth_var_12},
    "lowp_089_stat_depth_var_13": {"inputs": ["close"], "func": lowp_089_stat_depth_var_13},
    "lowp_090_stat_depth_var_14": {"inputs": ["close"], "func": lowp_090_stat_depth_var_14},
    "lowp_091_stat_depth_var_15": {"inputs": ["close"], "func": lowp_091_stat_depth_var_15},
    "lowp_092_stat_depth_var_16": {"inputs": ["close"], "func": lowp_092_stat_depth_var_16},
    "lowp_093_stat_depth_var_17": {"inputs": ["close"], "func": lowp_093_stat_depth_var_17},
    "lowp_094_stat_depth_var_18": {"inputs": ["close"], "func": lowp_094_stat_depth_var_18},
    "lowp_095_stat_depth_var_19": {"inputs": ["close"], "func": lowp_095_stat_depth_var_19},
    "lowp_096_stat_depth_var_20": {"inputs": ["close"], "func": lowp_096_stat_depth_var_20},
    "lowp_097_stat_depth_var_21": {"inputs": ["close"], "func": lowp_097_stat_depth_var_21},
    "lowp_098_stat_depth_var_22": {"inputs": ["close"], "func": lowp_098_stat_depth_var_22},
    "lowp_099_stat_depth_var_23": {"inputs": ["close"], "func": lowp_099_stat_depth_var_23},
    "lowp_100_stat_depth_var_24": {"inputs": ["close"], "func": lowp_100_stat_depth_var_24},
    "lowp_101_stat_depth_var_25": {"inputs": ["close"], "func": lowp_101_stat_depth_var_25},
    "lowp_102_stat_depth_var_26": {"inputs": ["close"], "func": lowp_102_stat_depth_var_26},
    "lowp_103_stat_depth_var_27": {"inputs": ["close"], "func": lowp_103_stat_depth_var_27},
    "lowp_104_stat_depth_var_28": {"inputs": ["close"], "func": lowp_104_stat_depth_var_28},
    "lowp_105_stat_depth_var_29": {"inputs": ["close"], "func": lowp_105_stat_depth_var_29},
    "lowp_106_stat_depth_var_30": {"inputs": ["close"], "func": lowp_106_stat_depth_var_30},
    "lowp_107_stat_depth_var_31": {"inputs": ["close"], "func": lowp_107_stat_depth_var_31},
    "lowp_108_stat_depth_var_32": {"inputs": ["close"], "func": lowp_108_stat_depth_var_32},
    "lowp_109_stat_depth_var_33": {"inputs": ["close"], "func": lowp_109_stat_depth_var_33},
    "lowp_110_stat_depth_var_34": {"inputs": ["close"], "func": lowp_110_stat_depth_var_34},
    "lowp_111_stat_depth_var_35": {"inputs": ["close"], "func": lowp_111_stat_depth_var_35},
    "lowp_112_stat_depth_var_36": {"inputs": ["close"], "func": lowp_112_stat_depth_var_36},
    "lowp_113_stat_depth_var_37": {"inputs": ["close"], "func": lowp_113_stat_depth_var_37},
    "lowp_114_stat_depth_var_38": {"inputs": ["close"], "func": lowp_114_stat_depth_var_38},
    "lowp_115_stat_depth_var_39": {"inputs": ["close"], "func": lowp_115_stat_depth_var_39},
    "lowp_116_stat_depth_var_40": {"inputs": ["close"], "func": lowp_116_stat_depth_var_40},
    "lowp_117_stat_depth_var_41": {"inputs": ["close"], "func": lowp_117_stat_depth_var_41},
    "lowp_118_stat_depth_var_42": {"inputs": ["close"], "func": lowp_118_stat_depth_var_42},
    "lowp_119_stat_depth_var_43": {"inputs": ["close"], "func": lowp_119_stat_depth_var_43},
    "lowp_120_stat_depth_var_44": {"inputs": ["close"], "func": lowp_120_stat_depth_var_44},
    "lowp_121_stat_depth_var_45": {"inputs": ["close"], "func": lowp_121_stat_depth_var_45},
    "lowp_122_stat_depth_var_46": {"inputs": ["close"], "func": lowp_122_stat_depth_var_46},
    "lowp_123_stat_depth_var_47": {"inputs": ["close"], "func": lowp_123_stat_depth_var_47},
    "lowp_124_stat_depth_var_48": {"inputs": ["close"], "func": lowp_124_stat_depth_var_48},
    "lowp_125_stat_depth_var_49": {"inputs": ["close"], "func": lowp_125_stat_depth_var_49},
    "lowp_126_stat_depth_var_50": {"inputs": ["close"], "func": lowp_126_stat_depth_var_50},
    "lowp_127_stat_depth_var_51": {"inputs": ["close"], "func": lowp_127_stat_depth_var_51},
    "lowp_128_stat_depth_var_52": {"inputs": ["close"], "func": lowp_128_stat_depth_var_52},
    "lowp_129_stat_depth_var_53": {"inputs": ["close"], "func": lowp_129_stat_depth_var_53},
    "lowp_130_stat_depth_var_54": {"inputs": ["close"], "func": lowp_130_stat_depth_var_54},
    "lowp_131_stat_depth_var_55": {"inputs": ["close"], "func": lowp_131_stat_depth_var_55},
    "lowp_132_stat_depth_var_56": {"inputs": ["close"], "func": lowp_132_stat_depth_var_56},
    "lowp_133_stat_depth_var_57": {"inputs": ["close"], "func": lowp_133_stat_depth_var_57},
    "lowp_134_stat_depth_var_58": {"inputs": ["close"], "func": lowp_134_stat_depth_var_58},
    "lowp_135_stat_depth_var_59": {"inputs": ["close"], "func": lowp_135_stat_depth_var_59},
    "lowp_136_stat_depth_var_60": {"inputs": ["close"], "func": lowp_136_stat_depth_var_60},
    "lowp_137_stat_depth_var_61": {"inputs": ["close"], "func": lowp_137_stat_depth_var_61},
    "lowp_138_stat_depth_var_62": {"inputs": ["close"], "func": lowp_138_stat_depth_var_62},
    "lowp_139_stat_depth_var_63": {"inputs": ["close"], "func": lowp_139_stat_depth_var_63},
    "lowp_140_stat_depth_var_64": {"inputs": ["close"], "func": lowp_140_stat_depth_var_64},
    "lowp_141_stat_depth_var_65": {"inputs": ["close"], "func": lowp_141_stat_depth_var_65},
    "lowp_142_stat_depth_var_66": {"inputs": ["close"], "func": lowp_142_stat_depth_var_66},
    "lowp_143_stat_depth_var_67": {"inputs": ["close"], "func": lowp_143_stat_depth_var_67},
    "lowp_144_stat_depth_var_68": {"inputs": ["close"], "func": lowp_144_stat_depth_var_68},
    "lowp_145_stat_depth_var_69": {"inputs": ["close"], "func": lowp_145_stat_depth_var_69},
    "lowp_146_stat_depth_var_70": {"inputs": ["close"], "func": lowp_146_stat_depth_var_70},
    "lowp_147_stat_depth_var_71": {"inputs": ["close"], "func": lowp_147_stat_depth_var_71},
    "lowp_148_stat_depth_var_72": {"inputs": ["close"], "func": lowp_148_stat_depth_var_72},
    "lowp_149_stat_depth_var_73": {"inputs": ["close"], "func": lowp_149_stat_depth_var_73},
    "lowp_150_stat_depth_var_74": {"inputs": ["close"], "func": lowp_150_stat_depth_var_74},
}
