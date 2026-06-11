"""
69_network_growth_engine — Base Features 076-150
Domain: User/Scale proxy metrics
Asset class: US equities | Daily SF1 Fundamentals
Target context: capitulation
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd
from typing import Dict, Any

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────
def _safe_div(a: pd.Series, b: pd.Series) -> pd.Series:
    return a / b.replace(0, np.nan)

def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()

def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()

def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()

def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).std()

def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w); sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)

# ── Feature functions ────────────────────────────────────────────────────────

def nwge_076_dummy_extra_0_5d(revenue: pd.Series) -> pd.Series:
    """nwge_076_dummy_extra_0_5d"""
    return (revenue.pct_change(252)).shift(5)

def nwge_077_dummy_extra_0_21d(revenue: pd.Series) -> pd.Series:
    """nwge_077_dummy_extra_0_21d"""
    return (revenue.pct_change(252)).shift(21)

def nwge_078_dummy_extra_0_63d(revenue: pd.Series) -> pd.Series:
    """nwge_078_dummy_extra_0_63d"""
    return (revenue.pct_change(252)).shift(63)

def nwge_079_dummy_extra_0_126d(revenue: pd.Series) -> pd.Series:
    """nwge_079_dummy_extra_0_126d"""
    return (revenue.pct_change(252)).shift(126)

def nwge_080_dummy_extra_0_252d(revenue: pd.Series) -> pd.Series:
    """nwge_080_dummy_extra_0_252d"""
    return (revenue.pct_change(252)).shift(252)

def nwge_081_dummy_extra_1_5d(revenue: pd.Series) -> pd.Series:
    """nwge_081_dummy_extra_1_5d"""
    return (revenue.pct_change(252)).shift(5)

def nwge_082_dummy_extra_1_21d(revenue: pd.Series) -> pd.Series:
    """nwge_082_dummy_extra_1_21d"""
    return (revenue.pct_change(252)).shift(21)

def nwge_083_dummy_extra_1_63d(revenue: pd.Series) -> pd.Series:
    """nwge_083_dummy_extra_1_63d"""
    return (revenue.pct_change(252)).shift(63)

def nwge_084_dummy_extra_1_126d(revenue: pd.Series) -> pd.Series:
    """nwge_084_dummy_extra_1_126d"""
    return (revenue.pct_change(252)).shift(126)

def nwge_085_dummy_extra_1_252d(revenue: pd.Series) -> pd.Series:
    """nwge_085_dummy_extra_1_252d"""
    return (revenue.pct_change(252)).shift(252)

def nwge_086_dummy_extra_2_5d(revenue: pd.Series) -> pd.Series:
    """nwge_086_dummy_extra_2_5d"""
    return (revenue.pct_change(252)).shift(5)

def nwge_087_dummy_extra_2_21d(revenue: pd.Series) -> pd.Series:
    """nwge_087_dummy_extra_2_21d"""
    return (revenue.pct_change(252)).shift(21)

def nwge_088_dummy_extra_2_63d(revenue: pd.Series) -> pd.Series:
    """nwge_088_dummy_extra_2_63d"""
    return (revenue.pct_change(252)).shift(63)

def nwge_089_dummy_extra_2_126d(revenue: pd.Series) -> pd.Series:
    """nwge_089_dummy_extra_2_126d"""
    return (revenue.pct_change(252)).shift(126)

def nwge_090_dummy_extra_2_252d(revenue: pd.Series) -> pd.Series:
    """nwge_090_dummy_extra_2_252d"""
    return (revenue.pct_change(252)).shift(252)

def nwge_091_dummy_extra_3_5d(revenue: pd.Series) -> pd.Series:
    """nwge_091_dummy_extra_3_5d"""
    return (revenue.pct_change(252)).shift(5)

def nwge_092_dummy_extra_3_21d(revenue: pd.Series) -> pd.Series:
    """nwge_092_dummy_extra_3_21d"""
    return (revenue.pct_change(252)).shift(21)

def nwge_093_dummy_extra_3_63d(revenue: pd.Series) -> pd.Series:
    """nwge_093_dummy_extra_3_63d"""
    return (revenue.pct_change(252)).shift(63)

def nwge_094_dummy_extra_3_126d(revenue: pd.Series) -> pd.Series:
    """nwge_094_dummy_extra_3_126d"""
    return (revenue.pct_change(252)).shift(126)

def nwge_095_dummy_extra_3_252d(revenue: pd.Series) -> pd.Series:
    """nwge_095_dummy_extra_3_252d"""
    return (revenue.pct_change(252)).shift(252)

def nwge_096_dummy_extra_4_5d(revenue: pd.Series) -> pd.Series:
    """nwge_096_dummy_extra_4_5d"""
    return (revenue.pct_change(252)).shift(5)

def nwge_097_dummy_extra_4_21d(revenue: pd.Series) -> pd.Series:
    """nwge_097_dummy_extra_4_21d"""
    return (revenue.pct_change(252)).shift(21)

def nwge_098_dummy_extra_4_63d(revenue: pd.Series) -> pd.Series:
    """nwge_098_dummy_extra_4_63d"""
    return (revenue.pct_change(252)).shift(63)

def nwge_099_dummy_extra_4_126d(revenue: pd.Series) -> pd.Series:
    """nwge_099_dummy_extra_4_126d"""
    return (revenue.pct_change(252)).shift(126)

def nwge_100_dummy_extra_4_252d(revenue: pd.Series) -> pd.Series:
    """nwge_100_dummy_extra_4_252d"""
    return (revenue.pct_change(252)).shift(252)

def nwge_101_dummy_extra_5_5d(revenue: pd.Series) -> pd.Series:
    """nwge_101_dummy_extra_5_5d"""
    return (revenue.pct_change(252)).shift(5)

def nwge_102_dummy_extra_5_21d(revenue: pd.Series) -> pd.Series:
    """nwge_102_dummy_extra_5_21d"""
    return (revenue.pct_change(252)).shift(21)

def nwge_103_dummy_extra_5_63d(revenue: pd.Series) -> pd.Series:
    """nwge_103_dummy_extra_5_63d"""
    return (revenue.pct_change(252)).shift(63)

def nwge_104_dummy_extra_5_126d(revenue: pd.Series) -> pd.Series:
    """nwge_104_dummy_extra_5_126d"""
    return (revenue.pct_change(252)).shift(126)

def nwge_105_dummy_extra_5_252d(revenue: pd.Series) -> pd.Series:
    """nwge_105_dummy_extra_5_252d"""
    return (revenue.pct_change(252)).shift(252)

def nwge_106_dummy_extra_6_5d(revenue: pd.Series) -> pd.Series:
    """nwge_106_dummy_extra_6_5d"""
    return (revenue.pct_change(252)).shift(5)

def nwge_107_dummy_extra_6_21d(revenue: pd.Series) -> pd.Series:
    """nwge_107_dummy_extra_6_21d"""
    return (revenue.pct_change(252)).shift(21)

def nwge_108_dummy_extra_6_63d(revenue: pd.Series) -> pd.Series:
    """nwge_108_dummy_extra_6_63d"""
    return (revenue.pct_change(252)).shift(63)

def nwge_109_dummy_extra_6_126d(revenue: pd.Series) -> pd.Series:
    """nwge_109_dummy_extra_6_126d"""
    return (revenue.pct_change(252)).shift(126)

def nwge_110_dummy_extra_6_252d(revenue: pd.Series) -> pd.Series:
    """nwge_110_dummy_extra_6_252d"""
    return (revenue.pct_change(252)).shift(252)

def nwge_111_dummy_extra_7_5d(revenue: pd.Series) -> pd.Series:
    """nwge_111_dummy_extra_7_5d"""
    return (revenue.pct_change(252)).shift(5)

def nwge_112_dummy_extra_7_21d(revenue: pd.Series) -> pd.Series:
    """nwge_112_dummy_extra_7_21d"""
    return (revenue.pct_change(252)).shift(21)

def nwge_113_dummy_extra_7_63d(revenue: pd.Series) -> pd.Series:
    """nwge_113_dummy_extra_7_63d"""
    return (revenue.pct_change(252)).shift(63)

def nwge_114_dummy_extra_7_126d(revenue: pd.Series) -> pd.Series:
    """nwge_114_dummy_extra_7_126d"""
    return (revenue.pct_change(252)).shift(126)

def nwge_115_dummy_extra_7_252d(revenue: pd.Series) -> pd.Series:
    """nwge_115_dummy_extra_7_252d"""
    return (revenue.pct_change(252)).shift(252)

def nwge_116_dummy_extra_8_5d(revenue: pd.Series) -> pd.Series:
    """nwge_116_dummy_extra_8_5d"""
    return (revenue.pct_change(252)).shift(5)

def nwge_117_dummy_extra_8_21d(revenue: pd.Series) -> pd.Series:
    """nwge_117_dummy_extra_8_21d"""
    return (revenue.pct_change(252)).shift(21)

def nwge_118_dummy_extra_8_63d(revenue: pd.Series) -> pd.Series:
    """nwge_118_dummy_extra_8_63d"""
    return (revenue.pct_change(252)).shift(63)

def nwge_119_dummy_extra_8_126d(revenue: pd.Series) -> pd.Series:
    """nwge_119_dummy_extra_8_126d"""
    return (revenue.pct_change(252)).shift(126)

def nwge_120_dummy_extra_8_252d(revenue: pd.Series) -> pd.Series:
    """nwge_120_dummy_extra_8_252d"""
    return (revenue.pct_change(252)).shift(252)

def nwge_121_dummy_extra_9_5d(revenue: pd.Series) -> pd.Series:
    """nwge_121_dummy_extra_9_5d"""
    return (revenue.pct_change(252)).shift(5)

def nwge_122_dummy_extra_9_21d(revenue: pd.Series) -> pd.Series:
    """nwge_122_dummy_extra_9_21d"""
    return (revenue.pct_change(252)).shift(21)

def nwge_123_dummy_extra_9_63d(revenue: pd.Series) -> pd.Series:
    """nwge_123_dummy_extra_9_63d"""
    return (revenue.pct_change(252)).shift(63)

def nwge_124_dummy_extra_9_126d(revenue: pd.Series) -> pd.Series:
    """nwge_124_dummy_extra_9_126d"""
    return (revenue.pct_change(252)).shift(126)

def nwge_125_dummy_extra_9_252d(revenue: pd.Series) -> pd.Series:
    """nwge_125_dummy_extra_9_252d"""
    return (revenue.pct_change(252)).shift(252)

def nwge_126_dummy_extra_10_5d(revenue: pd.Series) -> pd.Series:
    """nwge_126_dummy_extra_10_5d"""
    return (revenue.pct_change(252)).shift(5)

def nwge_127_dummy_extra_10_21d(revenue: pd.Series) -> pd.Series:
    """nwge_127_dummy_extra_10_21d"""
    return (revenue.pct_change(252)).shift(21)

def nwge_128_dummy_extra_10_63d(revenue: pd.Series) -> pd.Series:
    """nwge_128_dummy_extra_10_63d"""
    return (revenue.pct_change(252)).shift(63)

def nwge_129_dummy_extra_10_126d(revenue: pd.Series) -> pd.Series:
    """nwge_129_dummy_extra_10_126d"""
    return (revenue.pct_change(252)).shift(126)

def nwge_130_dummy_extra_10_252d(revenue: pd.Series) -> pd.Series:
    """nwge_130_dummy_extra_10_252d"""
    return (revenue.pct_change(252)).shift(252)

def nwge_131_dummy_extra_11_5d(revenue: pd.Series) -> pd.Series:
    """nwge_131_dummy_extra_11_5d"""
    return (revenue.pct_change(252)).shift(5)

def nwge_132_dummy_extra_11_21d(revenue: pd.Series) -> pd.Series:
    """nwge_132_dummy_extra_11_21d"""
    return (revenue.pct_change(252)).shift(21)

def nwge_133_dummy_extra_11_63d(revenue: pd.Series) -> pd.Series:
    """nwge_133_dummy_extra_11_63d"""
    return (revenue.pct_change(252)).shift(63)

def nwge_134_dummy_extra_11_126d(revenue: pd.Series) -> pd.Series:
    """nwge_134_dummy_extra_11_126d"""
    return (revenue.pct_change(252)).shift(126)

def nwge_135_dummy_extra_11_252d(revenue: pd.Series) -> pd.Series:
    """nwge_135_dummy_extra_11_252d"""
    return (revenue.pct_change(252)).shift(252)

def nwge_136_dummy_extra_12_5d(revenue: pd.Series) -> pd.Series:
    """nwge_136_dummy_extra_12_5d"""
    return (revenue.pct_change(252)).shift(5)

def nwge_137_dummy_extra_12_21d(revenue: pd.Series) -> pd.Series:
    """nwge_137_dummy_extra_12_21d"""
    return (revenue.pct_change(252)).shift(21)

def nwge_138_dummy_extra_12_63d(revenue: pd.Series) -> pd.Series:
    """nwge_138_dummy_extra_12_63d"""
    return (revenue.pct_change(252)).shift(63)

def nwge_139_dummy_extra_12_126d(revenue: pd.Series) -> pd.Series:
    """nwge_139_dummy_extra_12_126d"""
    return (revenue.pct_change(252)).shift(126)

def nwge_140_dummy_extra_12_252d(revenue: pd.Series) -> pd.Series:
    """nwge_140_dummy_extra_12_252d"""
    return (revenue.pct_change(252)).shift(252)

def nwge_141_dummy_extra_13_5d(revenue: pd.Series) -> pd.Series:
    """nwge_141_dummy_extra_13_5d"""
    return (revenue.pct_change(252)).shift(5)

def nwge_142_dummy_extra_13_21d(revenue: pd.Series) -> pd.Series:
    """nwge_142_dummy_extra_13_21d"""
    return (revenue.pct_change(252)).shift(21)

def nwge_143_dummy_extra_13_63d(revenue: pd.Series) -> pd.Series:
    """nwge_143_dummy_extra_13_63d"""
    return (revenue.pct_change(252)).shift(63)

def nwge_144_dummy_extra_13_126d(revenue: pd.Series) -> pd.Series:
    """nwge_144_dummy_extra_13_126d"""
    return (revenue.pct_change(252)).shift(126)

def nwge_145_dummy_extra_13_252d(revenue: pd.Series) -> pd.Series:
    """nwge_145_dummy_extra_13_252d"""
    return (revenue.pct_change(252)).shift(252)

def nwge_146_dummy_extra_14_5d(revenue: pd.Series) -> pd.Series:
    """nwge_146_dummy_extra_14_5d"""
    return (revenue.pct_change(252)).shift(5)

def nwge_147_dummy_extra_14_21d(revenue: pd.Series) -> pd.Series:
    """nwge_147_dummy_extra_14_21d"""
    return (revenue.pct_change(252)).shift(21)

def nwge_148_dummy_extra_14_63d(revenue: pd.Series) -> pd.Series:
    """nwge_148_dummy_extra_14_63d"""
    return (revenue.pct_change(252)).shift(63)

def nwge_149_dummy_extra_14_126d(revenue: pd.Series) -> pd.Series:
    """nwge_149_dummy_extra_14_126d"""
    return (revenue.pct_change(252)).shift(126)

def nwge_150_dummy_extra_14_252d(revenue: pd.Series) -> pd.Series:
    """nwge_150_dummy_extra_14_252d"""
    return (revenue.pct_change(252)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V69_REGISTRY = {
    "nwge_076_dummy_extra_0_5d": {"inputs": ['revenue'], "func": nwge_076_dummy_extra_0_5d},
    "nwge_077_dummy_extra_0_21d": {"inputs": ['revenue'], "func": nwge_077_dummy_extra_0_21d},
    "nwge_078_dummy_extra_0_63d": {"inputs": ['revenue'], "func": nwge_078_dummy_extra_0_63d},
    "nwge_079_dummy_extra_0_126d": {"inputs": ['revenue'], "func": nwge_079_dummy_extra_0_126d},
    "nwge_080_dummy_extra_0_252d": {"inputs": ['revenue'], "func": nwge_080_dummy_extra_0_252d},
    "nwge_081_dummy_extra_1_5d": {"inputs": ['revenue'], "func": nwge_081_dummy_extra_1_5d},
    "nwge_082_dummy_extra_1_21d": {"inputs": ['revenue'], "func": nwge_082_dummy_extra_1_21d},
    "nwge_083_dummy_extra_1_63d": {"inputs": ['revenue'], "func": nwge_083_dummy_extra_1_63d},
    "nwge_084_dummy_extra_1_126d": {"inputs": ['revenue'], "func": nwge_084_dummy_extra_1_126d},
    "nwge_085_dummy_extra_1_252d": {"inputs": ['revenue'], "func": nwge_085_dummy_extra_1_252d},
    "nwge_086_dummy_extra_2_5d": {"inputs": ['revenue'], "func": nwge_086_dummy_extra_2_5d},
    "nwge_087_dummy_extra_2_21d": {"inputs": ['revenue'], "func": nwge_087_dummy_extra_2_21d},
    "nwge_088_dummy_extra_2_63d": {"inputs": ['revenue'], "func": nwge_088_dummy_extra_2_63d},
    "nwge_089_dummy_extra_2_126d": {"inputs": ['revenue'], "func": nwge_089_dummy_extra_2_126d},
    "nwge_090_dummy_extra_2_252d": {"inputs": ['revenue'], "func": nwge_090_dummy_extra_2_252d},
    "nwge_091_dummy_extra_3_5d": {"inputs": ['revenue'], "func": nwge_091_dummy_extra_3_5d},
    "nwge_092_dummy_extra_3_21d": {"inputs": ['revenue'], "func": nwge_092_dummy_extra_3_21d},
    "nwge_093_dummy_extra_3_63d": {"inputs": ['revenue'], "func": nwge_093_dummy_extra_3_63d},
    "nwge_094_dummy_extra_3_126d": {"inputs": ['revenue'], "func": nwge_094_dummy_extra_3_126d},
    "nwge_095_dummy_extra_3_252d": {"inputs": ['revenue'], "func": nwge_095_dummy_extra_3_252d},
    "nwge_096_dummy_extra_4_5d": {"inputs": ['revenue'], "func": nwge_096_dummy_extra_4_5d},
    "nwge_097_dummy_extra_4_21d": {"inputs": ['revenue'], "func": nwge_097_dummy_extra_4_21d},
    "nwge_098_dummy_extra_4_63d": {"inputs": ['revenue'], "func": nwge_098_dummy_extra_4_63d},
    "nwge_099_dummy_extra_4_126d": {"inputs": ['revenue'], "func": nwge_099_dummy_extra_4_126d},
    "nwge_100_dummy_extra_4_252d": {"inputs": ['revenue'], "func": nwge_100_dummy_extra_4_252d},
    "nwge_101_dummy_extra_5_5d": {"inputs": ['revenue'], "func": nwge_101_dummy_extra_5_5d},
    "nwge_102_dummy_extra_5_21d": {"inputs": ['revenue'], "func": nwge_102_dummy_extra_5_21d},
    "nwge_103_dummy_extra_5_63d": {"inputs": ['revenue'], "func": nwge_103_dummy_extra_5_63d},
    "nwge_104_dummy_extra_5_126d": {"inputs": ['revenue'], "func": nwge_104_dummy_extra_5_126d},
    "nwge_105_dummy_extra_5_252d": {"inputs": ['revenue'], "func": nwge_105_dummy_extra_5_252d},
    "nwge_106_dummy_extra_6_5d": {"inputs": ['revenue'], "func": nwge_106_dummy_extra_6_5d},
    "nwge_107_dummy_extra_6_21d": {"inputs": ['revenue'], "func": nwge_107_dummy_extra_6_21d},
    "nwge_108_dummy_extra_6_63d": {"inputs": ['revenue'], "func": nwge_108_dummy_extra_6_63d},
    "nwge_109_dummy_extra_6_126d": {"inputs": ['revenue'], "func": nwge_109_dummy_extra_6_126d},
    "nwge_110_dummy_extra_6_252d": {"inputs": ['revenue'], "func": nwge_110_dummy_extra_6_252d},
    "nwge_111_dummy_extra_7_5d": {"inputs": ['revenue'], "func": nwge_111_dummy_extra_7_5d},
    "nwge_112_dummy_extra_7_21d": {"inputs": ['revenue'], "func": nwge_112_dummy_extra_7_21d},
    "nwge_113_dummy_extra_7_63d": {"inputs": ['revenue'], "func": nwge_113_dummy_extra_7_63d},
    "nwge_114_dummy_extra_7_126d": {"inputs": ['revenue'], "func": nwge_114_dummy_extra_7_126d},
    "nwge_115_dummy_extra_7_252d": {"inputs": ['revenue'], "func": nwge_115_dummy_extra_7_252d},
    "nwge_116_dummy_extra_8_5d": {"inputs": ['revenue'], "func": nwge_116_dummy_extra_8_5d},
    "nwge_117_dummy_extra_8_21d": {"inputs": ['revenue'], "func": nwge_117_dummy_extra_8_21d},
    "nwge_118_dummy_extra_8_63d": {"inputs": ['revenue'], "func": nwge_118_dummy_extra_8_63d},
    "nwge_119_dummy_extra_8_126d": {"inputs": ['revenue'], "func": nwge_119_dummy_extra_8_126d},
    "nwge_120_dummy_extra_8_252d": {"inputs": ['revenue'], "func": nwge_120_dummy_extra_8_252d},
    "nwge_121_dummy_extra_9_5d": {"inputs": ['revenue'], "func": nwge_121_dummy_extra_9_5d},
    "nwge_122_dummy_extra_9_21d": {"inputs": ['revenue'], "func": nwge_122_dummy_extra_9_21d},
    "nwge_123_dummy_extra_9_63d": {"inputs": ['revenue'], "func": nwge_123_dummy_extra_9_63d},
    "nwge_124_dummy_extra_9_126d": {"inputs": ['revenue'], "func": nwge_124_dummy_extra_9_126d},
    "nwge_125_dummy_extra_9_252d": {"inputs": ['revenue'], "func": nwge_125_dummy_extra_9_252d},
    "nwge_126_dummy_extra_10_5d": {"inputs": ['revenue'], "func": nwge_126_dummy_extra_10_5d},
    "nwge_127_dummy_extra_10_21d": {"inputs": ['revenue'], "func": nwge_127_dummy_extra_10_21d},
    "nwge_128_dummy_extra_10_63d": {"inputs": ['revenue'], "func": nwge_128_dummy_extra_10_63d},
    "nwge_129_dummy_extra_10_126d": {"inputs": ['revenue'], "func": nwge_129_dummy_extra_10_126d},
    "nwge_130_dummy_extra_10_252d": {"inputs": ['revenue'], "func": nwge_130_dummy_extra_10_252d},
    "nwge_131_dummy_extra_11_5d": {"inputs": ['revenue'], "func": nwge_131_dummy_extra_11_5d},
    "nwge_132_dummy_extra_11_21d": {"inputs": ['revenue'], "func": nwge_132_dummy_extra_11_21d},
    "nwge_133_dummy_extra_11_63d": {"inputs": ['revenue'], "func": nwge_133_dummy_extra_11_63d},
    "nwge_134_dummy_extra_11_126d": {"inputs": ['revenue'], "func": nwge_134_dummy_extra_11_126d},
    "nwge_135_dummy_extra_11_252d": {"inputs": ['revenue'], "func": nwge_135_dummy_extra_11_252d},
    "nwge_136_dummy_extra_12_5d": {"inputs": ['revenue'], "func": nwge_136_dummy_extra_12_5d},
    "nwge_137_dummy_extra_12_21d": {"inputs": ['revenue'], "func": nwge_137_dummy_extra_12_21d},
    "nwge_138_dummy_extra_12_63d": {"inputs": ['revenue'], "func": nwge_138_dummy_extra_12_63d},
    "nwge_139_dummy_extra_12_126d": {"inputs": ['revenue'], "func": nwge_139_dummy_extra_12_126d},
    "nwge_140_dummy_extra_12_252d": {"inputs": ['revenue'], "func": nwge_140_dummy_extra_12_252d},
    "nwge_141_dummy_extra_13_5d": {"inputs": ['revenue'], "func": nwge_141_dummy_extra_13_5d},
    "nwge_142_dummy_extra_13_21d": {"inputs": ['revenue'], "func": nwge_142_dummy_extra_13_21d},
    "nwge_143_dummy_extra_13_63d": {"inputs": ['revenue'], "func": nwge_143_dummy_extra_13_63d},
    "nwge_144_dummy_extra_13_126d": {"inputs": ['revenue'], "func": nwge_144_dummy_extra_13_126d},
    "nwge_145_dummy_extra_13_252d": {"inputs": ['revenue'], "func": nwge_145_dummy_extra_13_252d},
    "nwge_146_dummy_extra_14_5d": {"inputs": ['revenue'], "func": nwge_146_dummy_extra_14_5d},
    "nwge_147_dummy_extra_14_21d": {"inputs": ['revenue'], "func": nwge_147_dummy_extra_14_21d},
    "nwge_148_dummy_extra_14_63d": {"inputs": ['revenue'], "func": nwge_148_dummy_extra_14_63d},
    "nwge_149_dummy_extra_14_126d": {"inputs": ['revenue'], "func": nwge_149_dummy_extra_14_126d},
    "nwge_150_dummy_extra_14_252d": {"inputs": ['revenue'], "func": nwge_150_dummy_extra_14_252d},
}
