"""
69_network_growth_engine — Base Features 001-075
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

def nwge_001_dummy_0_5d(revenue: pd.Series) -> pd.Series:
    """nwge_001_dummy_0_5d"""
    return (revenue.pct_change(252)).shift(5)

def nwge_002_dummy_0_21d(revenue: pd.Series) -> pd.Series:
    """nwge_002_dummy_0_21d"""
    return (revenue.pct_change(252)).shift(21)

def nwge_003_dummy_0_63d(revenue: pd.Series) -> pd.Series:
    """nwge_003_dummy_0_63d"""
    return (revenue.pct_change(252)).shift(63)

def nwge_004_dummy_0_126d(revenue: pd.Series) -> pd.Series:
    """nwge_004_dummy_0_126d"""
    return (revenue.pct_change(252)).shift(126)

def nwge_005_dummy_0_252d(revenue: pd.Series) -> pd.Series:
    """nwge_005_dummy_0_252d"""
    return (revenue.pct_change(252)).shift(252)

def nwge_006_dummy_1_5d(revenue: pd.Series) -> pd.Series:
    """nwge_006_dummy_1_5d"""
    return (revenue.pct_change(252)).shift(5)

def nwge_007_dummy_1_21d(revenue: pd.Series) -> pd.Series:
    """nwge_007_dummy_1_21d"""
    return (revenue.pct_change(252)).shift(21)

def nwge_008_dummy_1_63d(revenue: pd.Series) -> pd.Series:
    """nwge_008_dummy_1_63d"""
    return (revenue.pct_change(252)).shift(63)

def nwge_009_dummy_1_126d(revenue: pd.Series) -> pd.Series:
    """nwge_009_dummy_1_126d"""
    return (revenue.pct_change(252)).shift(126)

def nwge_010_dummy_1_252d(revenue: pd.Series) -> pd.Series:
    """nwge_010_dummy_1_252d"""
    return (revenue.pct_change(252)).shift(252)

def nwge_011_dummy_2_5d(revenue: pd.Series) -> pd.Series:
    """nwge_011_dummy_2_5d"""
    return (revenue.pct_change(252)).shift(5)

def nwge_012_dummy_2_21d(revenue: pd.Series) -> pd.Series:
    """nwge_012_dummy_2_21d"""
    return (revenue.pct_change(252)).shift(21)

def nwge_013_dummy_2_63d(revenue: pd.Series) -> pd.Series:
    """nwge_013_dummy_2_63d"""
    return (revenue.pct_change(252)).shift(63)

def nwge_014_dummy_2_126d(revenue: pd.Series) -> pd.Series:
    """nwge_014_dummy_2_126d"""
    return (revenue.pct_change(252)).shift(126)

def nwge_015_dummy_2_252d(revenue: pd.Series) -> pd.Series:
    """nwge_015_dummy_2_252d"""
    return (revenue.pct_change(252)).shift(252)

def nwge_016_dummy_3_5d(revenue: pd.Series) -> pd.Series:
    """nwge_016_dummy_3_5d"""
    return (revenue.pct_change(252)).shift(5)

def nwge_017_dummy_3_21d(revenue: pd.Series) -> pd.Series:
    """nwge_017_dummy_3_21d"""
    return (revenue.pct_change(252)).shift(21)

def nwge_018_dummy_3_63d(revenue: pd.Series) -> pd.Series:
    """nwge_018_dummy_3_63d"""
    return (revenue.pct_change(252)).shift(63)

def nwge_019_dummy_3_126d(revenue: pd.Series) -> pd.Series:
    """nwge_019_dummy_3_126d"""
    return (revenue.pct_change(252)).shift(126)

def nwge_020_dummy_3_252d(revenue: pd.Series) -> pd.Series:
    """nwge_020_dummy_3_252d"""
    return (revenue.pct_change(252)).shift(252)

def nwge_021_dummy_4_5d(revenue: pd.Series) -> pd.Series:
    """nwge_021_dummy_4_5d"""
    return (revenue.pct_change(252)).shift(5)

def nwge_022_dummy_4_21d(revenue: pd.Series) -> pd.Series:
    """nwge_022_dummy_4_21d"""
    return (revenue.pct_change(252)).shift(21)

def nwge_023_dummy_4_63d(revenue: pd.Series) -> pd.Series:
    """nwge_023_dummy_4_63d"""
    return (revenue.pct_change(252)).shift(63)

def nwge_024_dummy_4_126d(revenue: pd.Series) -> pd.Series:
    """nwge_024_dummy_4_126d"""
    return (revenue.pct_change(252)).shift(126)

def nwge_025_dummy_4_252d(revenue: pd.Series) -> pd.Series:
    """nwge_025_dummy_4_252d"""
    return (revenue.pct_change(252)).shift(252)

def nwge_026_dummy_5_5d(revenue: pd.Series) -> pd.Series:
    """nwge_026_dummy_5_5d"""
    return (revenue.pct_change(252)).shift(5)

def nwge_027_dummy_5_21d(revenue: pd.Series) -> pd.Series:
    """nwge_027_dummy_5_21d"""
    return (revenue.pct_change(252)).shift(21)

def nwge_028_dummy_5_63d(revenue: pd.Series) -> pd.Series:
    """nwge_028_dummy_5_63d"""
    return (revenue.pct_change(252)).shift(63)

def nwge_029_dummy_5_126d(revenue: pd.Series) -> pd.Series:
    """nwge_029_dummy_5_126d"""
    return (revenue.pct_change(252)).shift(126)

def nwge_030_dummy_5_252d(revenue: pd.Series) -> pd.Series:
    """nwge_030_dummy_5_252d"""
    return (revenue.pct_change(252)).shift(252)

def nwge_031_dummy_6_5d(revenue: pd.Series) -> pd.Series:
    """nwge_031_dummy_6_5d"""
    return (revenue.pct_change(252)).shift(5)

def nwge_032_dummy_6_21d(revenue: pd.Series) -> pd.Series:
    """nwge_032_dummy_6_21d"""
    return (revenue.pct_change(252)).shift(21)

def nwge_033_dummy_6_63d(revenue: pd.Series) -> pd.Series:
    """nwge_033_dummy_6_63d"""
    return (revenue.pct_change(252)).shift(63)

def nwge_034_dummy_6_126d(revenue: pd.Series) -> pd.Series:
    """nwge_034_dummy_6_126d"""
    return (revenue.pct_change(252)).shift(126)

def nwge_035_dummy_6_252d(revenue: pd.Series) -> pd.Series:
    """nwge_035_dummy_6_252d"""
    return (revenue.pct_change(252)).shift(252)

def nwge_036_dummy_7_5d(revenue: pd.Series) -> pd.Series:
    """nwge_036_dummy_7_5d"""
    return (revenue.pct_change(252)).shift(5)

def nwge_037_dummy_7_21d(revenue: pd.Series) -> pd.Series:
    """nwge_037_dummy_7_21d"""
    return (revenue.pct_change(252)).shift(21)

def nwge_038_dummy_7_63d(revenue: pd.Series) -> pd.Series:
    """nwge_038_dummy_7_63d"""
    return (revenue.pct_change(252)).shift(63)

def nwge_039_dummy_7_126d(revenue: pd.Series) -> pd.Series:
    """nwge_039_dummy_7_126d"""
    return (revenue.pct_change(252)).shift(126)

def nwge_040_dummy_7_252d(revenue: pd.Series) -> pd.Series:
    """nwge_040_dummy_7_252d"""
    return (revenue.pct_change(252)).shift(252)

def nwge_041_dummy_8_5d(revenue: pd.Series) -> pd.Series:
    """nwge_041_dummy_8_5d"""
    return (revenue.pct_change(252)).shift(5)

def nwge_042_dummy_8_21d(revenue: pd.Series) -> pd.Series:
    """nwge_042_dummy_8_21d"""
    return (revenue.pct_change(252)).shift(21)

def nwge_043_dummy_8_63d(revenue: pd.Series) -> pd.Series:
    """nwge_043_dummy_8_63d"""
    return (revenue.pct_change(252)).shift(63)

def nwge_044_dummy_8_126d(revenue: pd.Series) -> pd.Series:
    """nwge_044_dummy_8_126d"""
    return (revenue.pct_change(252)).shift(126)

def nwge_045_dummy_8_252d(revenue: pd.Series) -> pd.Series:
    """nwge_045_dummy_8_252d"""
    return (revenue.pct_change(252)).shift(252)

def nwge_046_dummy_9_5d(revenue: pd.Series) -> pd.Series:
    """nwge_046_dummy_9_5d"""
    return (revenue.pct_change(252)).shift(5)

def nwge_047_dummy_9_21d(revenue: pd.Series) -> pd.Series:
    """nwge_047_dummy_9_21d"""
    return (revenue.pct_change(252)).shift(21)

def nwge_048_dummy_9_63d(revenue: pd.Series) -> pd.Series:
    """nwge_048_dummy_9_63d"""
    return (revenue.pct_change(252)).shift(63)

def nwge_049_dummy_9_126d(revenue: pd.Series) -> pd.Series:
    """nwge_049_dummy_9_126d"""
    return (revenue.pct_change(252)).shift(126)

def nwge_050_dummy_9_252d(revenue: pd.Series) -> pd.Series:
    """nwge_050_dummy_9_252d"""
    return (revenue.pct_change(252)).shift(252)

def nwge_051_dummy_10_5d(revenue: pd.Series) -> pd.Series:
    """nwge_051_dummy_10_5d"""
    return (revenue.pct_change(252)).shift(5)

def nwge_052_dummy_10_21d(revenue: pd.Series) -> pd.Series:
    """nwge_052_dummy_10_21d"""
    return (revenue.pct_change(252)).shift(21)

def nwge_053_dummy_10_63d(revenue: pd.Series) -> pd.Series:
    """nwge_053_dummy_10_63d"""
    return (revenue.pct_change(252)).shift(63)

def nwge_054_dummy_10_126d(revenue: pd.Series) -> pd.Series:
    """nwge_054_dummy_10_126d"""
    return (revenue.pct_change(252)).shift(126)

def nwge_055_dummy_10_252d(revenue: pd.Series) -> pd.Series:
    """nwge_055_dummy_10_252d"""
    return (revenue.pct_change(252)).shift(252)

def nwge_056_dummy_11_5d(revenue: pd.Series) -> pd.Series:
    """nwge_056_dummy_11_5d"""
    return (revenue.pct_change(252)).shift(5)

def nwge_057_dummy_11_21d(revenue: pd.Series) -> pd.Series:
    """nwge_057_dummy_11_21d"""
    return (revenue.pct_change(252)).shift(21)

def nwge_058_dummy_11_63d(revenue: pd.Series) -> pd.Series:
    """nwge_058_dummy_11_63d"""
    return (revenue.pct_change(252)).shift(63)

def nwge_059_dummy_11_126d(revenue: pd.Series) -> pd.Series:
    """nwge_059_dummy_11_126d"""
    return (revenue.pct_change(252)).shift(126)

def nwge_060_dummy_11_252d(revenue: pd.Series) -> pd.Series:
    """nwge_060_dummy_11_252d"""
    return (revenue.pct_change(252)).shift(252)

def nwge_061_dummy_12_5d(revenue: pd.Series) -> pd.Series:
    """nwge_061_dummy_12_5d"""
    return (revenue.pct_change(252)).shift(5)

def nwge_062_dummy_12_21d(revenue: pd.Series) -> pd.Series:
    """nwge_062_dummy_12_21d"""
    return (revenue.pct_change(252)).shift(21)

def nwge_063_dummy_12_63d(revenue: pd.Series) -> pd.Series:
    """nwge_063_dummy_12_63d"""
    return (revenue.pct_change(252)).shift(63)

def nwge_064_dummy_12_126d(revenue: pd.Series) -> pd.Series:
    """nwge_064_dummy_12_126d"""
    return (revenue.pct_change(252)).shift(126)

def nwge_065_dummy_12_252d(revenue: pd.Series) -> pd.Series:
    """nwge_065_dummy_12_252d"""
    return (revenue.pct_change(252)).shift(252)

def nwge_066_dummy_13_5d(revenue: pd.Series) -> pd.Series:
    """nwge_066_dummy_13_5d"""
    return (revenue.pct_change(252)).shift(5)

def nwge_067_dummy_13_21d(revenue: pd.Series) -> pd.Series:
    """nwge_067_dummy_13_21d"""
    return (revenue.pct_change(252)).shift(21)

def nwge_068_dummy_13_63d(revenue: pd.Series) -> pd.Series:
    """nwge_068_dummy_13_63d"""
    return (revenue.pct_change(252)).shift(63)

def nwge_069_dummy_13_126d(revenue: pd.Series) -> pd.Series:
    """nwge_069_dummy_13_126d"""
    return (revenue.pct_change(252)).shift(126)

def nwge_070_dummy_13_252d(revenue: pd.Series) -> pd.Series:
    """nwge_070_dummy_13_252d"""
    return (revenue.pct_change(252)).shift(252)

def nwge_071_dummy_14_5d(revenue: pd.Series) -> pd.Series:
    """nwge_071_dummy_14_5d"""
    return (revenue.pct_change(252)).shift(5)

def nwge_072_dummy_14_21d(revenue: pd.Series) -> pd.Series:
    """nwge_072_dummy_14_21d"""
    return (revenue.pct_change(252)).shift(21)

def nwge_073_dummy_14_63d(revenue: pd.Series) -> pd.Series:
    """nwge_073_dummy_14_63d"""
    return (revenue.pct_change(252)).shift(63)

def nwge_074_dummy_14_126d(revenue: pd.Series) -> pd.Series:
    """nwge_074_dummy_14_126d"""
    return (revenue.pct_change(252)).shift(126)

def nwge_075_dummy_14_252d(revenue: pd.Series) -> pd.Series:
    """nwge_075_dummy_14_252d"""
    return (revenue.pct_change(252)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V69_REGISTRY = {
    "nwge_001_dummy_0_5d": {"inputs": ['revenue'], "func": nwge_001_dummy_0_5d},
    "nwge_002_dummy_0_21d": {"inputs": ['revenue'], "func": nwge_002_dummy_0_21d},
    "nwge_003_dummy_0_63d": {"inputs": ['revenue'], "func": nwge_003_dummy_0_63d},
    "nwge_004_dummy_0_126d": {"inputs": ['revenue'], "func": nwge_004_dummy_0_126d},
    "nwge_005_dummy_0_252d": {"inputs": ['revenue'], "func": nwge_005_dummy_0_252d},
    "nwge_006_dummy_1_5d": {"inputs": ['revenue'], "func": nwge_006_dummy_1_5d},
    "nwge_007_dummy_1_21d": {"inputs": ['revenue'], "func": nwge_007_dummy_1_21d},
    "nwge_008_dummy_1_63d": {"inputs": ['revenue'], "func": nwge_008_dummy_1_63d},
    "nwge_009_dummy_1_126d": {"inputs": ['revenue'], "func": nwge_009_dummy_1_126d},
    "nwge_010_dummy_1_252d": {"inputs": ['revenue'], "func": nwge_010_dummy_1_252d},
    "nwge_011_dummy_2_5d": {"inputs": ['revenue'], "func": nwge_011_dummy_2_5d},
    "nwge_012_dummy_2_21d": {"inputs": ['revenue'], "func": nwge_012_dummy_2_21d},
    "nwge_013_dummy_2_63d": {"inputs": ['revenue'], "func": nwge_013_dummy_2_63d},
    "nwge_014_dummy_2_126d": {"inputs": ['revenue'], "func": nwge_014_dummy_2_126d},
    "nwge_015_dummy_2_252d": {"inputs": ['revenue'], "func": nwge_015_dummy_2_252d},
    "nwge_016_dummy_3_5d": {"inputs": ['revenue'], "func": nwge_016_dummy_3_5d},
    "nwge_017_dummy_3_21d": {"inputs": ['revenue'], "func": nwge_017_dummy_3_21d},
    "nwge_018_dummy_3_63d": {"inputs": ['revenue'], "func": nwge_018_dummy_3_63d},
    "nwge_019_dummy_3_126d": {"inputs": ['revenue'], "func": nwge_019_dummy_3_126d},
    "nwge_020_dummy_3_252d": {"inputs": ['revenue'], "func": nwge_020_dummy_3_252d},
    "nwge_021_dummy_4_5d": {"inputs": ['revenue'], "func": nwge_021_dummy_4_5d},
    "nwge_022_dummy_4_21d": {"inputs": ['revenue'], "func": nwge_022_dummy_4_21d},
    "nwge_023_dummy_4_63d": {"inputs": ['revenue'], "func": nwge_023_dummy_4_63d},
    "nwge_024_dummy_4_126d": {"inputs": ['revenue'], "func": nwge_024_dummy_4_126d},
    "nwge_025_dummy_4_252d": {"inputs": ['revenue'], "func": nwge_025_dummy_4_252d},
    "nwge_026_dummy_5_5d": {"inputs": ['revenue'], "func": nwge_026_dummy_5_5d},
    "nwge_027_dummy_5_21d": {"inputs": ['revenue'], "func": nwge_027_dummy_5_21d},
    "nwge_028_dummy_5_63d": {"inputs": ['revenue'], "func": nwge_028_dummy_5_63d},
    "nwge_029_dummy_5_126d": {"inputs": ['revenue'], "func": nwge_029_dummy_5_126d},
    "nwge_030_dummy_5_252d": {"inputs": ['revenue'], "func": nwge_030_dummy_5_252d},
    "nwge_031_dummy_6_5d": {"inputs": ['revenue'], "func": nwge_031_dummy_6_5d},
    "nwge_032_dummy_6_21d": {"inputs": ['revenue'], "func": nwge_032_dummy_6_21d},
    "nwge_033_dummy_6_63d": {"inputs": ['revenue'], "func": nwge_033_dummy_6_63d},
    "nwge_034_dummy_6_126d": {"inputs": ['revenue'], "func": nwge_034_dummy_6_126d},
    "nwge_035_dummy_6_252d": {"inputs": ['revenue'], "func": nwge_035_dummy_6_252d},
    "nwge_036_dummy_7_5d": {"inputs": ['revenue'], "func": nwge_036_dummy_7_5d},
    "nwge_037_dummy_7_21d": {"inputs": ['revenue'], "func": nwge_037_dummy_7_21d},
    "nwge_038_dummy_7_63d": {"inputs": ['revenue'], "func": nwge_038_dummy_7_63d},
    "nwge_039_dummy_7_126d": {"inputs": ['revenue'], "func": nwge_039_dummy_7_126d},
    "nwge_040_dummy_7_252d": {"inputs": ['revenue'], "func": nwge_040_dummy_7_252d},
    "nwge_041_dummy_8_5d": {"inputs": ['revenue'], "func": nwge_041_dummy_8_5d},
    "nwge_042_dummy_8_21d": {"inputs": ['revenue'], "func": nwge_042_dummy_8_21d},
    "nwge_043_dummy_8_63d": {"inputs": ['revenue'], "func": nwge_043_dummy_8_63d},
    "nwge_044_dummy_8_126d": {"inputs": ['revenue'], "func": nwge_044_dummy_8_126d},
    "nwge_045_dummy_8_252d": {"inputs": ['revenue'], "func": nwge_045_dummy_8_252d},
    "nwge_046_dummy_9_5d": {"inputs": ['revenue'], "func": nwge_046_dummy_9_5d},
    "nwge_047_dummy_9_21d": {"inputs": ['revenue'], "func": nwge_047_dummy_9_21d},
    "nwge_048_dummy_9_63d": {"inputs": ['revenue'], "func": nwge_048_dummy_9_63d},
    "nwge_049_dummy_9_126d": {"inputs": ['revenue'], "func": nwge_049_dummy_9_126d},
    "nwge_050_dummy_9_252d": {"inputs": ['revenue'], "func": nwge_050_dummy_9_252d},
    "nwge_051_dummy_10_5d": {"inputs": ['revenue'], "func": nwge_051_dummy_10_5d},
    "nwge_052_dummy_10_21d": {"inputs": ['revenue'], "func": nwge_052_dummy_10_21d},
    "nwge_053_dummy_10_63d": {"inputs": ['revenue'], "func": nwge_053_dummy_10_63d},
    "nwge_054_dummy_10_126d": {"inputs": ['revenue'], "func": nwge_054_dummy_10_126d},
    "nwge_055_dummy_10_252d": {"inputs": ['revenue'], "func": nwge_055_dummy_10_252d},
    "nwge_056_dummy_11_5d": {"inputs": ['revenue'], "func": nwge_056_dummy_11_5d},
    "nwge_057_dummy_11_21d": {"inputs": ['revenue'], "func": nwge_057_dummy_11_21d},
    "nwge_058_dummy_11_63d": {"inputs": ['revenue'], "func": nwge_058_dummy_11_63d},
    "nwge_059_dummy_11_126d": {"inputs": ['revenue'], "func": nwge_059_dummy_11_126d},
    "nwge_060_dummy_11_252d": {"inputs": ['revenue'], "func": nwge_060_dummy_11_252d},
    "nwge_061_dummy_12_5d": {"inputs": ['revenue'], "func": nwge_061_dummy_12_5d},
    "nwge_062_dummy_12_21d": {"inputs": ['revenue'], "func": nwge_062_dummy_12_21d},
    "nwge_063_dummy_12_63d": {"inputs": ['revenue'], "func": nwge_063_dummy_12_63d},
    "nwge_064_dummy_12_126d": {"inputs": ['revenue'], "func": nwge_064_dummy_12_126d},
    "nwge_065_dummy_12_252d": {"inputs": ['revenue'], "func": nwge_065_dummy_12_252d},
    "nwge_066_dummy_13_5d": {"inputs": ['revenue'], "func": nwge_066_dummy_13_5d},
    "nwge_067_dummy_13_21d": {"inputs": ['revenue'], "func": nwge_067_dummy_13_21d},
    "nwge_068_dummy_13_63d": {"inputs": ['revenue'], "func": nwge_068_dummy_13_63d},
    "nwge_069_dummy_13_126d": {"inputs": ['revenue'], "func": nwge_069_dummy_13_126d},
    "nwge_070_dummy_13_252d": {"inputs": ['revenue'], "func": nwge_070_dummy_13_252d},
    "nwge_071_dummy_14_5d": {"inputs": ['revenue'], "func": nwge_071_dummy_14_5d},
    "nwge_072_dummy_14_21d": {"inputs": ['revenue'], "func": nwge_072_dummy_14_21d},
    "nwge_073_dummy_14_63d": {"inputs": ['revenue'], "func": nwge_073_dummy_14_63d},
    "nwge_074_dummy_14_126d": {"inputs": ['revenue'], "func": nwge_074_dummy_14_126d},
    "nwge_075_dummy_14_252d": {"inputs": ['revenue'], "func": nwge_075_dummy_14_252d},
}
