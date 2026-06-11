"""
56_leverage_acceleration — Base Features 076-150
Domain: leverage_acceleration
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

def leva_076_leverage_accel_lvl_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_076_leverage_accel_lvl_5d"""
    base = _safe_div(assets, equity).diff(252)
    return _rolling_mean(base, 5)

def leva_077_leverage_accel_zscore_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_077_leverage_accel_zscore_5d"""
    base = _safe_div(assets, equity).diff(252)
    return _zscore_rolling(base, 5)

def leva_078_leverage_accel_rank_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_078_leverage_accel_rank_5d"""
    base = _safe_div(assets, equity).diff(252)
    return _rank_pct(base, 5)

def leva_079_leverage_accel_lvl_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_079_leverage_accel_lvl_21d"""
    base = _safe_div(assets, equity).diff(252)
    return _rolling_mean(base, 21)

def leva_080_leverage_accel_zscore_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_080_leverage_accel_zscore_21d"""
    base = _safe_div(assets, equity).diff(252)
    return _zscore_rolling(base, 21)

def leva_081_leverage_accel_rank_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_081_leverage_accel_rank_21d"""
    base = _safe_div(assets, equity).diff(252)
    return _rank_pct(base, 21)

def leva_082_leverage_accel_lvl_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_082_leverage_accel_lvl_63d"""
    base = _safe_div(assets, equity).diff(252)
    return _rolling_mean(base, 63)

def leva_083_leverage_accel_zscore_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_083_leverage_accel_zscore_63d"""
    base = _safe_div(assets, equity).diff(252)
    return _zscore_rolling(base, 63)

def leva_084_leverage_accel_rank_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_084_leverage_accel_rank_63d"""
    base = _safe_div(assets, equity).diff(252)
    return _rank_pct(base, 63)

def leva_085_leverage_accel_lvl_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_085_leverage_accel_lvl_126d"""
    base = _safe_div(assets, equity).diff(252)
    return _rolling_mean(base, 126)

def leva_086_leverage_accel_zscore_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_086_leverage_accel_zscore_126d"""
    base = _safe_div(assets, equity).diff(252)
    return _zscore_rolling(base, 126)

def leva_087_leverage_accel_rank_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_087_leverage_accel_rank_126d"""
    base = _safe_div(assets, equity).diff(252)
    return _rank_pct(base, 126)

def leva_088_leverage_accel_lvl_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_088_leverage_accel_lvl_252d"""
    base = _safe_div(assets, equity).diff(252)
    return _rolling_mean(base, 252)

def leva_089_leverage_accel_zscore_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_089_leverage_accel_zscore_252d"""
    base = _safe_div(assets, equity).diff(252)
    return _zscore_rolling(base, 252)

def leva_090_leverage_accel_rank_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_090_leverage_accel_rank_252d"""
    base = _safe_div(assets, equity).diff(252)
    return _rank_pct(base, 252)

def leva_091_debt_equity_chg_lvl_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_091_debt_equity_chg_lvl_5d"""
    base = _safe_div(debt, equity).diff(252)
    return _rolling_mean(base, 5)

def leva_092_debt_equity_chg_zscore_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_092_debt_equity_chg_zscore_5d"""
    base = _safe_div(debt, equity).diff(252)
    return _zscore_rolling(base, 5)

def leva_093_debt_equity_chg_rank_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_093_debt_equity_chg_rank_5d"""
    base = _safe_div(debt, equity).diff(252)
    return _rank_pct(base, 5)

def leva_094_debt_equity_chg_lvl_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_094_debt_equity_chg_lvl_21d"""
    base = _safe_div(debt, equity).diff(252)
    return _rolling_mean(base, 21)

def leva_095_debt_equity_chg_zscore_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_095_debt_equity_chg_zscore_21d"""
    base = _safe_div(debt, equity).diff(252)
    return _zscore_rolling(base, 21)

def leva_096_debt_equity_chg_rank_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_096_debt_equity_chg_rank_21d"""
    base = _safe_div(debt, equity).diff(252)
    return _rank_pct(base, 21)

def leva_097_debt_equity_chg_lvl_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_097_debt_equity_chg_lvl_63d"""
    base = _safe_div(debt, equity).diff(252)
    return _rolling_mean(base, 63)

def leva_098_debt_equity_chg_zscore_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_098_debt_equity_chg_zscore_63d"""
    base = _safe_div(debt, equity).diff(252)
    return _zscore_rolling(base, 63)

def leva_099_debt_equity_chg_rank_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_099_debt_equity_chg_rank_63d"""
    base = _safe_div(debt, equity).diff(252)
    return _rank_pct(base, 63)

def leva_100_debt_equity_chg_lvl_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_100_debt_equity_chg_lvl_126d"""
    base = _safe_div(debt, equity).diff(252)
    return _rolling_mean(base, 126)

def leva_101_debt_equity_chg_zscore_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_101_debt_equity_chg_zscore_126d"""
    base = _safe_div(debt, equity).diff(252)
    return _zscore_rolling(base, 126)

def leva_102_debt_equity_chg_rank_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_102_debt_equity_chg_rank_126d"""
    base = _safe_div(debt, equity).diff(252)
    return _rank_pct(base, 126)

def leva_103_debt_equity_chg_lvl_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_103_debt_equity_chg_lvl_252d"""
    base = _safe_div(debt, equity).diff(252)
    return _rolling_mean(base, 252)

def leva_104_debt_equity_chg_zscore_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_104_debt_equity_chg_zscore_252d"""
    base = _safe_div(debt, equity).diff(252)
    return _zscore_rolling(base, 252)

def leva_105_debt_equity_chg_rank_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_105_debt_equity_chg_rank_252d"""
    base = _safe_div(debt, equity).diff(252)
    return _rank_pct(base, 252)

def leva_106_leverage_z_lvl_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_106_leverage_z_lvl_5d"""
    base = _zscore_rolling(_safe_div(assets, equity), 252)
    return _rolling_mean(base, 5)

def leva_107_leverage_z_zscore_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_107_leverage_z_zscore_5d"""
    base = _zscore_rolling(_safe_div(assets, equity), 252)
    return _zscore_rolling(base, 5)

def leva_108_leverage_z_rank_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_108_leverage_z_rank_5d"""
    base = _zscore_rolling(_safe_div(assets, equity), 252)
    return _rank_pct(base, 5)

def leva_109_leverage_z_lvl_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_109_leverage_z_lvl_21d"""
    base = _zscore_rolling(_safe_div(assets, equity), 252)
    return _rolling_mean(base, 21)

def leva_110_leverage_z_zscore_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_110_leverage_z_zscore_21d"""
    base = _zscore_rolling(_safe_div(assets, equity), 252)
    return _zscore_rolling(base, 21)

def leva_111_leverage_z_rank_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_111_leverage_z_rank_21d"""
    base = _zscore_rolling(_safe_div(assets, equity), 252)
    return _rank_pct(base, 21)

def leva_112_leverage_z_lvl_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_112_leverage_z_lvl_63d"""
    base = _zscore_rolling(_safe_div(assets, equity), 252)
    return _rolling_mean(base, 63)

def leva_113_leverage_z_zscore_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_113_leverage_z_zscore_63d"""
    base = _zscore_rolling(_safe_div(assets, equity), 252)
    return _zscore_rolling(base, 63)

def leva_114_leverage_z_rank_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_114_leverage_z_rank_63d"""
    base = _zscore_rolling(_safe_div(assets, equity), 252)
    return _rank_pct(base, 63)

def leva_115_leverage_z_lvl_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_115_leverage_z_lvl_126d"""
    base = _zscore_rolling(_safe_div(assets, equity), 252)
    return _rolling_mean(base, 126)

def leva_116_leverage_z_zscore_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_116_leverage_z_zscore_126d"""
    base = _zscore_rolling(_safe_div(assets, equity), 252)
    return _zscore_rolling(base, 126)

def leva_117_leverage_z_rank_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_117_leverage_z_rank_126d"""
    base = _zscore_rolling(_safe_div(assets, equity), 252)
    return _rank_pct(base, 126)

def leva_118_leverage_z_lvl_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_118_leverage_z_lvl_252d"""
    base = _zscore_rolling(_safe_div(assets, equity), 252)
    return _rolling_mean(base, 252)

def leva_119_leverage_z_zscore_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_119_leverage_z_zscore_252d"""
    base = _zscore_rolling(_safe_div(assets, equity), 252)
    return _zscore_rolling(base, 252)

def leva_120_leverage_z_rank_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_120_leverage_z_rank_252d"""
    base = _zscore_rolling(_safe_div(assets, equity), 252)
    return _rank_pct(base, 252)

def leva_121_leverage_rank_lvl_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_121_leverage_rank_lvl_5d"""
    base = _rank_pct(_safe_div(assets, equity), 252)
    return _rolling_mean(base, 5)

def leva_122_leverage_rank_zscore_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_122_leverage_rank_zscore_5d"""
    base = _rank_pct(_safe_div(assets, equity), 252)
    return _zscore_rolling(base, 5)

def leva_123_leverage_rank_rank_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_123_leverage_rank_rank_5d"""
    base = _rank_pct(_safe_div(assets, equity), 252)
    return _rank_pct(base, 5)

def leva_124_leverage_rank_lvl_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_124_leverage_rank_lvl_21d"""
    base = _rank_pct(_safe_div(assets, equity), 252)
    return _rolling_mean(base, 21)

def leva_125_leverage_rank_zscore_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_125_leverage_rank_zscore_21d"""
    base = _rank_pct(_safe_div(assets, equity), 252)
    return _zscore_rolling(base, 21)

def leva_126_leverage_rank_rank_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_126_leverage_rank_rank_21d"""
    base = _rank_pct(_safe_div(assets, equity), 252)
    return _rank_pct(base, 21)

def leva_127_leverage_rank_lvl_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_127_leverage_rank_lvl_63d"""
    base = _rank_pct(_safe_div(assets, equity), 252)
    return _rolling_mean(base, 63)

def leva_128_leverage_rank_zscore_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_128_leverage_rank_zscore_63d"""
    base = _rank_pct(_safe_div(assets, equity), 252)
    return _zscore_rolling(base, 63)

def leva_129_leverage_rank_rank_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_129_leverage_rank_rank_63d"""
    base = _rank_pct(_safe_div(assets, equity), 252)
    return _rank_pct(base, 63)

def leva_130_leverage_rank_lvl_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_130_leverage_rank_lvl_126d"""
    base = _rank_pct(_safe_div(assets, equity), 252)
    return _rolling_mean(base, 126)

def leva_131_leverage_rank_zscore_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_131_leverage_rank_zscore_126d"""
    base = _rank_pct(_safe_div(assets, equity), 252)
    return _zscore_rolling(base, 126)

def leva_132_leverage_rank_rank_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_132_leverage_rank_rank_126d"""
    base = _rank_pct(_safe_div(assets, equity), 252)
    return _rank_pct(base, 126)

def leva_133_leverage_rank_lvl_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_133_leverage_rank_lvl_252d"""
    base = _rank_pct(_safe_div(assets, equity), 252)
    return _rolling_mean(base, 252)

def leva_134_leverage_rank_zscore_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_134_leverage_rank_zscore_252d"""
    base = _rank_pct(_safe_div(assets, equity), 252)
    return _zscore_rolling(base, 252)

def leva_135_leverage_rank_rank_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_135_leverage_rank_rank_252d"""
    base = _rank_pct(_safe_div(assets, equity), 252)
    return _rank_pct(base, 252)

def leva_136_leverage_vol_lvl_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_136_leverage_vol_lvl_5d"""
    base = _rolling_std(_safe_div(assets, equity), 63)
    return _rolling_mean(base, 5)

def leva_137_leverage_vol_zscore_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_137_leverage_vol_zscore_5d"""
    base = _rolling_std(_safe_div(assets, equity), 63)
    return _zscore_rolling(base, 5)

def leva_138_leverage_vol_rank_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_138_leverage_vol_rank_5d"""
    base = _rolling_std(_safe_div(assets, equity), 63)
    return _rank_pct(base, 5)

def leva_139_leverage_vol_lvl_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_139_leverage_vol_lvl_21d"""
    base = _rolling_std(_safe_div(assets, equity), 63)
    return _rolling_mean(base, 21)

def leva_140_leverage_vol_zscore_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_140_leverage_vol_zscore_21d"""
    base = _rolling_std(_safe_div(assets, equity), 63)
    return _zscore_rolling(base, 21)

def leva_141_leverage_vol_rank_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_141_leverage_vol_rank_21d"""
    base = _rolling_std(_safe_div(assets, equity), 63)
    return _rank_pct(base, 21)

def leva_142_leverage_vol_lvl_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_142_leverage_vol_lvl_63d"""
    base = _rolling_std(_safe_div(assets, equity), 63)
    return _rolling_mean(base, 63)

def leva_143_leverage_vol_zscore_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_143_leverage_vol_zscore_63d"""
    base = _rolling_std(_safe_div(assets, equity), 63)
    return _zscore_rolling(base, 63)

def leva_144_leverage_vol_rank_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_144_leverage_vol_rank_63d"""
    base = _rolling_std(_safe_div(assets, equity), 63)
    return _rank_pct(base, 63)

def leva_145_leverage_vol_lvl_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_145_leverage_vol_lvl_126d"""
    base = _rolling_std(_safe_div(assets, equity), 63)
    return _rolling_mean(base, 126)

def leva_146_leverage_vol_zscore_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_146_leverage_vol_zscore_126d"""
    base = _rolling_std(_safe_div(assets, equity), 63)
    return _zscore_rolling(base, 126)

def leva_147_leverage_vol_rank_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_147_leverage_vol_rank_126d"""
    base = _rolling_std(_safe_div(assets, equity), 63)
    return _rank_pct(base, 126)

def leva_148_leverage_vol_lvl_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_148_leverage_vol_lvl_252d"""
    base = _rolling_std(_safe_div(assets, equity), 63)
    return _rolling_mean(base, 252)

def leva_149_leverage_vol_zscore_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_149_leverage_vol_zscore_252d"""
    base = _rolling_std(_safe_div(assets, equity), 63)
    return _zscore_rolling(base, 252)

def leva_150_leverage_vol_rank_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_150_leverage_vol_rank_252d"""
    base = _rolling_std(_safe_div(assets, equity), 63)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V56_REGISTRY_2 = {
    "leva_076_leverage_accel_lvl_5d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_076_leverage_accel_lvl_5d},
    "leva_077_leverage_accel_zscore_5d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_077_leverage_accel_zscore_5d},
    "leva_078_leverage_accel_rank_5d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_078_leverage_accel_rank_5d},
    "leva_079_leverage_accel_lvl_21d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_079_leverage_accel_lvl_21d},
    "leva_080_leverage_accel_zscore_21d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_080_leverage_accel_zscore_21d},
    "leva_081_leverage_accel_rank_21d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_081_leverage_accel_rank_21d},
    "leva_082_leverage_accel_lvl_63d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_082_leverage_accel_lvl_63d},
    "leva_083_leverage_accel_zscore_63d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_083_leverage_accel_zscore_63d},
    "leva_084_leverage_accel_rank_63d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_084_leverage_accel_rank_63d},
    "leva_085_leverage_accel_lvl_126d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_085_leverage_accel_lvl_126d},
    "leva_086_leverage_accel_zscore_126d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_086_leverage_accel_zscore_126d},
    "leva_087_leverage_accel_rank_126d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_087_leverage_accel_rank_126d},
    "leva_088_leverage_accel_lvl_252d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_088_leverage_accel_lvl_252d},
    "leva_089_leverage_accel_zscore_252d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_089_leverage_accel_zscore_252d},
    "leva_090_leverage_accel_rank_252d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_090_leverage_accel_rank_252d},
    "leva_091_debt_equity_chg_lvl_5d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_091_debt_equity_chg_lvl_5d},
    "leva_092_debt_equity_chg_zscore_5d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_092_debt_equity_chg_zscore_5d},
    "leva_093_debt_equity_chg_rank_5d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_093_debt_equity_chg_rank_5d},
    "leva_094_debt_equity_chg_lvl_21d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_094_debt_equity_chg_lvl_21d},
    "leva_095_debt_equity_chg_zscore_21d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_095_debt_equity_chg_zscore_21d},
    "leva_096_debt_equity_chg_rank_21d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_096_debt_equity_chg_rank_21d},
    "leva_097_debt_equity_chg_lvl_63d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_097_debt_equity_chg_lvl_63d},
    "leva_098_debt_equity_chg_zscore_63d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_098_debt_equity_chg_zscore_63d},
    "leva_099_debt_equity_chg_rank_63d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_099_debt_equity_chg_rank_63d},
    "leva_100_debt_equity_chg_lvl_126d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_100_debt_equity_chg_lvl_126d},
    "leva_101_debt_equity_chg_zscore_126d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_101_debt_equity_chg_zscore_126d},
    "leva_102_debt_equity_chg_rank_126d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_102_debt_equity_chg_rank_126d},
    "leva_103_debt_equity_chg_lvl_252d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_103_debt_equity_chg_lvl_252d},
    "leva_104_debt_equity_chg_zscore_252d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_104_debt_equity_chg_zscore_252d},
    "leva_105_debt_equity_chg_rank_252d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_105_debt_equity_chg_rank_252d},
    "leva_106_leverage_z_lvl_5d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_106_leverage_z_lvl_5d},
    "leva_107_leverage_z_zscore_5d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_107_leverage_z_zscore_5d},
    "leva_108_leverage_z_rank_5d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_108_leverage_z_rank_5d},
    "leva_109_leverage_z_lvl_21d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_109_leverage_z_lvl_21d},
    "leva_110_leverage_z_zscore_21d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_110_leverage_z_zscore_21d},
    "leva_111_leverage_z_rank_21d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_111_leverage_z_rank_21d},
    "leva_112_leverage_z_lvl_63d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_112_leverage_z_lvl_63d},
    "leva_113_leverage_z_zscore_63d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_113_leverage_z_zscore_63d},
    "leva_114_leverage_z_rank_63d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_114_leverage_z_rank_63d},
    "leva_115_leverage_z_lvl_126d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_115_leverage_z_lvl_126d},
    "leva_116_leverage_z_zscore_126d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_116_leverage_z_zscore_126d},
    "leva_117_leverage_z_rank_126d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_117_leverage_z_rank_126d},
    "leva_118_leverage_z_lvl_252d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_118_leverage_z_lvl_252d},
    "leva_119_leverage_z_zscore_252d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_119_leverage_z_zscore_252d},
    "leva_120_leverage_z_rank_252d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_120_leverage_z_rank_252d},
    "leva_121_leverage_rank_lvl_5d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_121_leverage_rank_lvl_5d},
    "leva_122_leverage_rank_zscore_5d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_122_leverage_rank_zscore_5d},
    "leva_123_leverage_rank_rank_5d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_123_leverage_rank_rank_5d},
    "leva_124_leverage_rank_lvl_21d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_124_leverage_rank_lvl_21d},
    "leva_125_leverage_rank_zscore_21d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_125_leverage_rank_zscore_21d},
    "leva_126_leverage_rank_rank_21d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_126_leverage_rank_rank_21d},
    "leva_127_leverage_rank_lvl_63d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_127_leverage_rank_lvl_63d},
    "leva_128_leverage_rank_zscore_63d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_128_leverage_rank_zscore_63d},
    "leva_129_leverage_rank_rank_63d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_129_leverage_rank_rank_63d},
    "leva_130_leverage_rank_lvl_126d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_130_leverage_rank_lvl_126d},
    "leva_131_leverage_rank_zscore_126d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_131_leverage_rank_zscore_126d},
    "leva_132_leverage_rank_rank_126d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_132_leverage_rank_rank_126d},
    "leva_133_leverage_rank_lvl_252d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_133_leverage_rank_lvl_252d},
    "leva_134_leverage_rank_zscore_252d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_134_leverage_rank_zscore_252d},
    "leva_135_leverage_rank_rank_252d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_135_leverage_rank_rank_252d},
    "leva_136_leverage_vol_lvl_5d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_136_leverage_vol_lvl_5d},
    "leva_137_leverage_vol_zscore_5d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_137_leverage_vol_zscore_5d},
    "leva_138_leverage_vol_rank_5d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_138_leverage_vol_rank_5d},
    "leva_139_leverage_vol_lvl_21d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_139_leverage_vol_lvl_21d},
    "leva_140_leverage_vol_zscore_21d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_140_leverage_vol_zscore_21d},
    "leva_141_leverage_vol_rank_21d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_141_leverage_vol_rank_21d},
    "leva_142_leverage_vol_lvl_63d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_142_leverage_vol_lvl_63d},
    "leva_143_leverage_vol_zscore_63d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_143_leverage_vol_zscore_63d},
    "leva_144_leverage_vol_rank_63d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_144_leverage_vol_rank_63d},
    "leva_145_leverage_vol_lvl_126d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_145_leverage_vol_lvl_126d},
    "leva_146_leverage_vol_zscore_126d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_146_leverage_vol_zscore_126d},
    "leva_147_leverage_vol_rank_126d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_147_leverage_vol_rank_126d},
    "leva_148_leverage_vol_lvl_252d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_148_leverage_vol_lvl_252d},
    "leva_149_leverage_vol_zscore_252d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_149_leverage_vol_zscore_252d},
    "leva_150_leverage_vol_rank_252d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_150_leverage_vol_rank_252d},
}
