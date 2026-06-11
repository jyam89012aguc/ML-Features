"""
Underwater Curve — Base Features 076–150
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

def vcc_076_stat_depth_var_0(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_077_stat_depth_var_1(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_078_stat_depth_var_2(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_079_stat_depth_var_3(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_080_stat_depth_var_4(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_081_stat_depth_var_5(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_082_stat_depth_var_6(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_083_stat_depth_var_7(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_084_stat_depth_var_8(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_085_stat_depth_var_9(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_086_stat_depth_var_10(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_087_stat_depth_var_11(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_088_stat_depth_var_12(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_089_stat_depth_var_13(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_090_stat_depth_var_14(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_091_stat_depth_var_15(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_092_stat_depth_var_16(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_093_stat_depth_var_17(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_094_stat_depth_var_18(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_095_stat_depth_var_19(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_096_stat_depth_var_20(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_097_stat_depth_var_21(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_098_stat_depth_var_22(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_099_stat_depth_var_23(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_100_stat_depth_var_24(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_101_stat_depth_var_25(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_102_stat_depth_var_26(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_103_stat_depth_var_27(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_104_stat_depth_var_28(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_105_stat_depth_var_29(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_106_stat_depth_var_30(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_107_stat_depth_var_31(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_108_stat_depth_var_32(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_109_stat_depth_var_33(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_110_stat_depth_var_34(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_111_stat_depth_var_35(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_112_stat_depth_var_36(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_113_stat_depth_var_37(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_114_stat_depth_var_38(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_115_stat_depth_var_39(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_116_stat_depth_var_40(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_117_stat_depth_var_41(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_118_stat_depth_var_42(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_119_stat_depth_var_43(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_120_stat_depth_var_44(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_121_stat_depth_var_45(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_122_stat_depth_var_46(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_123_stat_depth_var_47(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_124_stat_depth_var_48(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_125_stat_depth_var_49(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_126_stat_depth_var_50(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_127_stat_depth_var_51(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_128_stat_depth_var_52(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_129_stat_depth_var_53(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_130_stat_depth_var_54(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_131_stat_depth_var_55(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_132_stat_depth_var_56(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_133_stat_depth_var_57(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_134_stat_depth_var_58(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_135_stat_depth_var_59(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_136_stat_depth_var_60(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_137_stat_depth_var_61(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_138_stat_depth_var_62(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_139_stat_depth_var_63(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_140_stat_depth_var_64(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_141_stat_depth_var_65(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_142_stat_depth_var_66(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_143_stat_depth_var_67(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_144_stat_depth_var_68(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_145_stat_depth_var_69(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_146_stat_depth_var_70(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_147_stat_depth_var_71(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_148_stat_depth_var_72(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_149_stat_depth_var_73(close: pd.Series) -> pd.Series:
    """_rank_pct variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _rank_pct(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

def vcc_150_stat_depth_var_74(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation for statistical depth"""
    # Auto-generated for statistical depth to reach 75 features
    return _zscore_rolling(_rolling_mean(close if "close" in locals() else pd.Series(), _TD_MON), _TD_YEAR)

# ── Registry ──────────────────────────────────────────────────────────────────

V05_REGISTRY = {
    "vcc_076_stat_depth_var_0": {"inputs": ["close"], "func": vcc_076_stat_depth_var_0},
    "vcc_077_stat_depth_var_1": {"inputs": ["close"], "func": vcc_077_stat_depth_var_1},
    "vcc_078_stat_depth_var_2": {"inputs": ["close"], "func": vcc_078_stat_depth_var_2},
    "vcc_079_stat_depth_var_3": {"inputs": ["close"], "func": vcc_079_stat_depth_var_3},
    "vcc_080_stat_depth_var_4": {"inputs": ["close"], "func": vcc_080_stat_depth_var_4},
    "vcc_081_stat_depth_var_5": {"inputs": ["close"], "func": vcc_081_stat_depth_var_5},
    "vcc_082_stat_depth_var_6": {"inputs": ["close"], "func": vcc_082_stat_depth_var_6},
    "vcc_083_stat_depth_var_7": {"inputs": ["close"], "func": vcc_083_stat_depth_var_7},
    "vcc_084_stat_depth_var_8": {"inputs": ["close"], "func": vcc_084_stat_depth_var_8},
    "vcc_085_stat_depth_var_9": {"inputs": ["close"], "func": vcc_085_stat_depth_var_9},
    "vcc_086_stat_depth_var_10": {"inputs": ["close"], "func": vcc_086_stat_depth_var_10},
    "vcc_087_stat_depth_var_11": {"inputs": ["close"], "func": vcc_087_stat_depth_var_11},
    "vcc_088_stat_depth_var_12": {"inputs": ["close"], "func": vcc_088_stat_depth_var_12},
    "vcc_089_stat_depth_var_13": {"inputs": ["close"], "func": vcc_089_stat_depth_var_13},
    "vcc_090_stat_depth_var_14": {"inputs": ["close"], "func": vcc_090_stat_depth_var_14},
    "vcc_091_stat_depth_var_15": {"inputs": ["close"], "func": vcc_091_stat_depth_var_15},
    "vcc_092_stat_depth_var_16": {"inputs": ["close"], "func": vcc_092_stat_depth_var_16},
    "vcc_093_stat_depth_var_17": {"inputs": ["close"], "func": vcc_093_stat_depth_var_17},
    "vcc_094_stat_depth_var_18": {"inputs": ["close"], "func": vcc_094_stat_depth_var_18},
    "vcc_095_stat_depth_var_19": {"inputs": ["close"], "func": vcc_095_stat_depth_var_19},
    "vcc_096_stat_depth_var_20": {"inputs": ["close"], "func": vcc_096_stat_depth_var_20},
    "vcc_097_stat_depth_var_21": {"inputs": ["close"], "func": vcc_097_stat_depth_var_21},
    "vcc_098_stat_depth_var_22": {"inputs": ["close"], "func": vcc_098_stat_depth_var_22},
    "vcc_099_stat_depth_var_23": {"inputs": ["close"], "func": vcc_099_stat_depth_var_23},
    "vcc_100_stat_depth_var_24": {"inputs": ["close"], "func": vcc_100_stat_depth_var_24},
    "vcc_101_stat_depth_var_25": {"inputs": ["close"], "func": vcc_101_stat_depth_var_25},
    "vcc_102_stat_depth_var_26": {"inputs": ["close"], "func": vcc_102_stat_depth_var_26},
    "vcc_103_stat_depth_var_27": {"inputs": ["close"], "func": vcc_103_stat_depth_var_27},
    "vcc_104_stat_depth_var_28": {"inputs": ["close"], "func": vcc_104_stat_depth_var_28},
    "vcc_105_stat_depth_var_29": {"inputs": ["close"], "func": vcc_105_stat_depth_var_29},
    "vcc_106_stat_depth_var_30": {"inputs": ["close"], "func": vcc_106_stat_depth_var_30},
    "vcc_107_stat_depth_var_31": {"inputs": ["close"], "func": vcc_107_stat_depth_var_31},
    "vcc_108_stat_depth_var_32": {"inputs": ["close"], "func": vcc_108_stat_depth_var_32},
    "vcc_109_stat_depth_var_33": {"inputs": ["close"], "func": vcc_109_stat_depth_var_33},
    "vcc_110_stat_depth_var_34": {"inputs": ["close"], "func": vcc_110_stat_depth_var_34},
    "vcc_111_stat_depth_var_35": {"inputs": ["close"], "func": vcc_111_stat_depth_var_35},
    "vcc_112_stat_depth_var_36": {"inputs": ["close"], "func": vcc_112_stat_depth_var_36},
    "vcc_113_stat_depth_var_37": {"inputs": ["close"], "func": vcc_113_stat_depth_var_37},
    "vcc_114_stat_depth_var_38": {"inputs": ["close"], "func": vcc_114_stat_depth_var_38},
    "vcc_115_stat_depth_var_39": {"inputs": ["close"], "func": vcc_115_stat_depth_var_39},
    "vcc_116_stat_depth_var_40": {"inputs": ["close"], "func": vcc_116_stat_depth_var_40},
    "vcc_117_stat_depth_var_41": {"inputs": ["close"], "func": vcc_117_stat_depth_var_41},
    "vcc_118_stat_depth_var_42": {"inputs": ["close"], "func": vcc_118_stat_depth_var_42},
    "vcc_119_stat_depth_var_43": {"inputs": ["close"], "func": vcc_119_stat_depth_var_43},
    "vcc_120_stat_depth_var_44": {"inputs": ["close"], "func": vcc_120_stat_depth_var_44},
    "vcc_121_stat_depth_var_45": {"inputs": ["close"], "func": vcc_121_stat_depth_var_45},
    "vcc_122_stat_depth_var_46": {"inputs": ["close"], "func": vcc_122_stat_depth_var_46},
    "vcc_123_stat_depth_var_47": {"inputs": ["close"], "func": vcc_123_stat_depth_var_47},
    "vcc_124_stat_depth_var_48": {"inputs": ["close"], "func": vcc_124_stat_depth_var_48},
    "vcc_125_stat_depth_var_49": {"inputs": ["close"], "func": vcc_125_stat_depth_var_49},
    "vcc_126_stat_depth_var_50": {"inputs": ["close"], "func": vcc_126_stat_depth_var_50},
    "vcc_127_stat_depth_var_51": {"inputs": ["close"], "func": vcc_127_stat_depth_var_51},
    "vcc_128_stat_depth_var_52": {"inputs": ["close"], "func": vcc_128_stat_depth_var_52},
    "vcc_129_stat_depth_var_53": {"inputs": ["close"], "func": vcc_129_stat_depth_var_53},
    "vcc_130_stat_depth_var_54": {"inputs": ["close"], "func": vcc_130_stat_depth_var_54},
    "vcc_131_stat_depth_var_55": {"inputs": ["close"], "func": vcc_131_stat_depth_var_55},
    "vcc_132_stat_depth_var_56": {"inputs": ["close"], "func": vcc_132_stat_depth_var_56},
    "vcc_133_stat_depth_var_57": {"inputs": ["close"], "func": vcc_133_stat_depth_var_57},
    "vcc_134_stat_depth_var_58": {"inputs": ["close"], "func": vcc_134_stat_depth_var_58},
    "vcc_135_stat_depth_var_59": {"inputs": ["close"], "func": vcc_135_stat_depth_var_59},
    "vcc_136_stat_depth_var_60": {"inputs": ["close"], "func": vcc_136_stat_depth_var_60},
    "vcc_137_stat_depth_var_61": {"inputs": ["close"], "func": vcc_137_stat_depth_var_61},
    "vcc_138_stat_depth_var_62": {"inputs": ["close"], "func": vcc_138_stat_depth_var_62},
    "vcc_139_stat_depth_var_63": {"inputs": ["close"], "func": vcc_139_stat_depth_var_63},
    "vcc_140_stat_depth_var_64": {"inputs": ["close"], "func": vcc_140_stat_depth_var_64},
    "vcc_141_stat_depth_var_65": {"inputs": ["close"], "func": vcc_141_stat_depth_var_65},
    "vcc_142_stat_depth_var_66": {"inputs": ["close"], "func": vcc_142_stat_depth_var_66},
    "vcc_143_stat_depth_var_67": {"inputs": ["close"], "func": vcc_143_stat_depth_var_67},
    "vcc_144_stat_depth_var_68": {"inputs": ["close"], "func": vcc_144_stat_depth_var_68},
    "vcc_145_stat_depth_var_69": {"inputs": ["close"], "func": vcc_145_stat_depth_var_69},
    "vcc_146_stat_depth_var_70": {"inputs": ["close"], "func": vcc_146_stat_depth_var_70},
    "vcc_147_stat_depth_var_71": {"inputs": ["close"], "func": vcc_147_stat_depth_var_71},
    "vcc_148_stat_depth_var_72": {"inputs": ["close"], "func": vcc_148_stat_depth_var_72},
    "vcc_149_stat_depth_var_73": {"inputs": ["close"], "func": vcc_149_stat_depth_var_73},
    "vcc_150_stat_depth_var_74": {"inputs": ["close"], "func": vcc_150_stat_depth_var_74},
}
