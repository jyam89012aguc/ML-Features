"""
38_balance_sheet_snapshot — Base Features 076-150
Domain: balance_sheet_snapshot
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

def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).std().fillna(0)

def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div((s - m), sd)

def _rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).rank(pct=True)

# ── Feature functions ────────────────────────────────────────────────────────

def bals_076_liabs_lvl_lvl_5d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_076_liabs_lvl_lvl_5d"""
    base = liabs
    return _rolling_mean(base, 5)

def bals_077_liabs_lvl_zscore_5d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_077_liabs_lvl_zscore_5d"""
    base = liabs
    return _zscore_rolling(base, 5)

def bals_078_liabs_lvl_rank_5d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_078_liabs_lvl_rank_5d"""
    base = liabs
    return _rank_pct(base, 5)

def bals_079_liabs_lvl_lvl_21d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_079_liabs_lvl_lvl_21d"""
    base = liabs
    return _rolling_mean(base, 21)

def bals_080_liabs_lvl_zscore_21d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_080_liabs_lvl_zscore_21d"""
    base = liabs
    return _zscore_rolling(base, 21)

def bals_081_liabs_lvl_rank_21d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_081_liabs_lvl_rank_21d"""
    base = liabs
    return _rank_pct(base, 21)

def bals_082_liabs_lvl_lvl_63d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_082_liabs_lvl_lvl_63d"""
    base = liabs
    return _rolling_mean(base, 63)

def bals_083_liabs_lvl_zscore_63d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_083_liabs_lvl_zscore_63d"""
    base = liabs
    return _zscore_rolling(base, 63)

def bals_084_liabs_lvl_rank_63d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_084_liabs_lvl_rank_63d"""
    base = liabs
    return _rank_pct(base, 63)

def bals_085_liabs_lvl_lvl_126d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_085_liabs_lvl_lvl_126d"""
    base = liabs
    return _rolling_mean(base, 126)

def bals_086_liabs_lvl_zscore_126d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_086_liabs_lvl_zscore_126d"""
    base = liabs
    return _zscore_rolling(base, 126)

def bals_087_liabs_lvl_rank_126d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_087_liabs_lvl_rank_126d"""
    base = liabs
    return _rank_pct(base, 126)

def bals_088_liabs_lvl_lvl_252d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_088_liabs_lvl_lvl_252d"""
    base = liabs
    return _rolling_mean(base, 252)

def bals_089_liabs_lvl_zscore_252d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_089_liabs_lvl_zscore_252d"""
    base = liabs
    return _zscore_rolling(base, 252)

def bals_090_liabs_lvl_rank_252d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_090_liabs_lvl_rank_252d"""
    base = liabs
    return _rank_pct(base, 252)

def bals_091_equity_lvl_lvl_5d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_091_equity_lvl_lvl_5d"""
    base = equity
    return _rolling_mean(base, 5)

def bals_092_equity_lvl_zscore_5d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_092_equity_lvl_zscore_5d"""
    base = equity
    return _zscore_rolling(base, 5)

def bals_093_equity_lvl_rank_5d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_093_equity_lvl_rank_5d"""
    base = equity
    return _rank_pct(base, 5)

def bals_094_equity_lvl_lvl_21d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_094_equity_lvl_lvl_21d"""
    base = equity
    return _rolling_mean(base, 21)

def bals_095_equity_lvl_zscore_21d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_095_equity_lvl_zscore_21d"""
    base = equity
    return _zscore_rolling(base, 21)

def bals_096_equity_lvl_rank_21d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_096_equity_lvl_rank_21d"""
    base = equity
    return _rank_pct(base, 21)

def bals_097_equity_lvl_lvl_63d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_097_equity_lvl_lvl_63d"""
    base = equity
    return _rolling_mean(base, 63)

def bals_098_equity_lvl_zscore_63d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_098_equity_lvl_zscore_63d"""
    base = equity
    return _zscore_rolling(base, 63)

def bals_099_equity_lvl_rank_63d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_099_equity_lvl_rank_63d"""
    base = equity
    return _rank_pct(base, 63)

def bals_100_equity_lvl_lvl_126d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_100_equity_lvl_lvl_126d"""
    base = equity
    return _rolling_mean(base, 126)

def bals_101_equity_lvl_zscore_126d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_101_equity_lvl_zscore_126d"""
    base = equity
    return _zscore_rolling(base, 126)

def bals_102_equity_lvl_rank_126d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_102_equity_lvl_rank_126d"""
    base = equity
    return _rank_pct(base, 126)

def bals_103_equity_lvl_lvl_252d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_103_equity_lvl_lvl_252d"""
    base = equity
    return _rolling_mean(base, 252)

def bals_104_equity_lvl_zscore_252d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_104_equity_lvl_zscore_252d"""
    base = equity
    return _zscore_rolling(base, 252)

def bals_105_equity_lvl_rank_252d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_105_equity_lvl_rank_252d"""
    base = equity
    return _rank_pct(base, 252)

def bals_106_debt_assets_lvl_5d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_106_debt_assets_lvl_5d"""
    base = _safe_div(debt, assets)
    return _rolling_mean(base, 5)

def bals_107_debt_assets_zscore_5d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_107_debt_assets_zscore_5d"""
    base = _safe_div(debt, assets)
    return _zscore_rolling(base, 5)

def bals_108_debt_assets_rank_5d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_108_debt_assets_rank_5d"""
    base = _safe_div(debt, assets)
    return _rank_pct(base, 5)

def bals_109_debt_assets_lvl_21d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_109_debt_assets_lvl_21d"""
    base = _safe_div(debt, assets)
    return _rolling_mean(base, 21)

def bals_110_debt_assets_zscore_21d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_110_debt_assets_zscore_21d"""
    base = _safe_div(debt, assets)
    return _zscore_rolling(base, 21)

def bals_111_debt_assets_rank_21d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_111_debt_assets_rank_21d"""
    base = _safe_div(debt, assets)
    return _rank_pct(base, 21)

def bals_112_debt_assets_lvl_63d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_112_debt_assets_lvl_63d"""
    base = _safe_div(debt, assets)
    return _rolling_mean(base, 63)

def bals_113_debt_assets_zscore_63d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_113_debt_assets_zscore_63d"""
    base = _safe_div(debt, assets)
    return _zscore_rolling(base, 63)

def bals_114_debt_assets_rank_63d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_114_debt_assets_rank_63d"""
    base = _safe_div(debt, assets)
    return _rank_pct(base, 63)

def bals_115_debt_assets_lvl_126d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_115_debt_assets_lvl_126d"""
    base = _safe_div(debt, assets)
    return _rolling_mean(base, 126)

def bals_116_debt_assets_zscore_126d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_116_debt_assets_zscore_126d"""
    base = _safe_div(debt, assets)
    return _zscore_rolling(base, 126)

def bals_117_debt_assets_rank_126d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_117_debt_assets_rank_126d"""
    base = _safe_div(debt, assets)
    return _rank_pct(base, 126)

def bals_118_debt_assets_lvl_252d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_118_debt_assets_lvl_252d"""
    base = _safe_div(debt, assets)
    return _rolling_mean(base, 252)

def bals_119_debt_assets_zscore_252d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_119_debt_assets_zscore_252d"""
    base = _safe_div(debt, assets)
    return _zscore_rolling(base, 252)

def bals_120_debt_assets_rank_252d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_120_debt_assets_rank_252d"""
    base = _safe_div(debt, assets)
    return _rank_pct(base, 252)

def bals_121_cash_debt_lvl_5d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_121_cash_debt_lvl_5d"""
    base = _safe_div(cashnequiv, debt)
    return _rolling_mean(base, 5)

def bals_122_cash_debt_zscore_5d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_122_cash_debt_zscore_5d"""
    base = _safe_div(cashnequiv, debt)
    return _zscore_rolling(base, 5)

def bals_123_cash_debt_rank_5d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_123_cash_debt_rank_5d"""
    base = _safe_div(cashnequiv, debt)
    return _rank_pct(base, 5)

def bals_124_cash_debt_lvl_21d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_124_cash_debt_lvl_21d"""
    base = _safe_div(cashnequiv, debt)
    return _rolling_mean(base, 21)

def bals_125_cash_debt_zscore_21d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_125_cash_debt_zscore_21d"""
    base = _safe_div(cashnequiv, debt)
    return _zscore_rolling(base, 21)

def bals_126_cash_debt_rank_21d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_126_cash_debt_rank_21d"""
    base = _safe_div(cashnequiv, debt)
    return _rank_pct(base, 21)

def bals_127_cash_debt_lvl_63d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_127_cash_debt_lvl_63d"""
    base = _safe_div(cashnequiv, debt)
    return _rolling_mean(base, 63)

def bals_128_cash_debt_zscore_63d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_128_cash_debt_zscore_63d"""
    base = _safe_div(cashnequiv, debt)
    return _zscore_rolling(base, 63)

def bals_129_cash_debt_rank_63d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_129_cash_debt_rank_63d"""
    base = _safe_div(cashnequiv, debt)
    return _rank_pct(base, 63)

def bals_130_cash_debt_lvl_126d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_130_cash_debt_lvl_126d"""
    base = _safe_div(cashnequiv, debt)
    return _rolling_mean(base, 126)

def bals_131_cash_debt_zscore_126d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_131_cash_debt_zscore_126d"""
    base = _safe_div(cashnequiv, debt)
    return _zscore_rolling(base, 126)

def bals_132_cash_debt_rank_126d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_132_cash_debt_rank_126d"""
    base = _safe_div(cashnequiv, debt)
    return _rank_pct(base, 126)

def bals_133_cash_debt_lvl_252d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_133_cash_debt_lvl_252d"""
    base = _safe_div(cashnequiv, debt)
    return _rolling_mean(base, 252)

def bals_134_cash_debt_zscore_252d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_134_cash_debt_zscore_252d"""
    base = _safe_div(cashnequiv, debt)
    return _zscore_rolling(base, 252)

def bals_135_cash_debt_rank_252d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_135_cash_debt_rank_252d"""
    base = _safe_div(cashnequiv, debt)
    return _rank_pct(base, 252)

def bals_136_net_debt_lvl_5d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_136_net_debt_lvl_5d"""
    base = debt - cashnequiv
    return _rolling_mean(base, 5)

def bals_137_net_debt_zscore_5d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_137_net_debt_zscore_5d"""
    base = debt - cashnequiv
    return _zscore_rolling(base, 5)

def bals_138_net_debt_rank_5d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_138_net_debt_rank_5d"""
    base = debt - cashnequiv
    return _rank_pct(base, 5)

def bals_139_net_debt_lvl_21d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_139_net_debt_lvl_21d"""
    base = debt - cashnequiv
    return _rolling_mean(base, 21)

def bals_140_net_debt_zscore_21d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_140_net_debt_zscore_21d"""
    base = debt - cashnequiv
    return _zscore_rolling(base, 21)

def bals_141_net_debt_rank_21d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_141_net_debt_rank_21d"""
    base = debt - cashnequiv
    return _rank_pct(base, 21)

def bals_142_net_debt_lvl_63d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_142_net_debt_lvl_63d"""
    base = debt - cashnequiv
    return _rolling_mean(base, 63)

def bals_143_net_debt_zscore_63d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_143_net_debt_zscore_63d"""
    base = debt - cashnequiv
    return _zscore_rolling(base, 63)

def bals_144_net_debt_rank_63d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_144_net_debt_rank_63d"""
    base = debt - cashnequiv
    return _rank_pct(base, 63)

def bals_145_net_debt_lvl_126d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_145_net_debt_lvl_126d"""
    base = debt - cashnequiv
    return _rolling_mean(base, 126)

def bals_146_net_debt_zscore_126d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_146_net_debt_zscore_126d"""
    base = debt - cashnequiv
    return _zscore_rolling(base, 126)

def bals_147_net_debt_rank_126d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_147_net_debt_rank_126d"""
    base = debt - cashnequiv
    return _rank_pct(base, 126)

def bals_148_net_debt_lvl_252d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_148_net_debt_lvl_252d"""
    base = debt - cashnequiv
    return _rolling_mean(base, 252)

def bals_149_net_debt_zscore_252d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_149_net_debt_zscore_252d"""
    base = debt - cashnequiv
    return _zscore_rolling(base, 252)

def bals_150_net_debt_rank_252d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_150_net_debt_rank_252d"""
    base = debt - cashnequiv
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V38_REGISTRY_2 = {
    "bals_076_liabs_lvl_lvl_5d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_076_liabs_lvl_lvl_5d},
    "bals_077_liabs_lvl_zscore_5d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_077_liabs_lvl_zscore_5d},
    "bals_078_liabs_lvl_rank_5d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_078_liabs_lvl_rank_5d},
    "bals_079_liabs_lvl_lvl_21d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_079_liabs_lvl_lvl_21d},
    "bals_080_liabs_lvl_zscore_21d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_080_liabs_lvl_zscore_21d},
    "bals_081_liabs_lvl_rank_21d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_081_liabs_lvl_rank_21d},
    "bals_082_liabs_lvl_lvl_63d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_082_liabs_lvl_lvl_63d},
    "bals_083_liabs_lvl_zscore_63d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_083_liabs_lvl_zscore_63d},
    "bals_084_liabs_lvl_rank_63d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_084_liabs_lvl_rank_63d},
    "bals_085_liabs_lvl_lvl_126d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_085_liabs_lvl_lvl_126d},
    "bals_086_liabs_lvl_zscore_126d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_086_liabs_lvl_zscore_126d},
    "bals_087_liabs_lvl_rank_126d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_087_liabs_lvl_rank_126d},
    "bals_088_liabs_lvl_lvl_252d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_088_liabs_lvl_lvl_252d},
    "bals_089_liabs_lvl_zscore_252d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_089_liabs_lvl_zscore_252d},
    "bals_090_liabs_lvl_rank_252d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_090_liabs_lvl_rank_252d},
    "bals_091_equity_lvl_lvl_5d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_091_equity_lvl_lvl_5d},
    "bals_092_equity_lvl_zscore_5d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_092_equity_lvl_zscore_5d},
    "bals_093_equity_lvl_rank_5d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_093_equity_lvl_rank_5d},
    "bals_094_equity_lvl_lvl_21d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_094_equity_lvl_lvl_21d},
    "bals_095_equity_lvl_zscore_21d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_095_equity_lvl_zscore_21d},
    "bals_096_equity_lvl_rank_21d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_096_equity_lvl_rank_21d},
    "bals_097_equity_lvl_lvl_63d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_097_equity_lvl_lvl_63d},
    "bals_098_equity_lvl_zscore_63d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_098_equity_lvl_zscore_63d},
    "bals_099_equity_lvl_rank_63d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_099_equity_lvl_rank_63d},
    "bals_100_equity_lvl_lvl_126d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_100_equity_lvl_lvl_126d},
    "bals_101_equity_lvl_zscore_126d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_101_equity_lvl_zscore_126d},
    "bals_102_equity_lvl_rank_126d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_102_equity_lvl_rank_126d},
    "bals_103_equity_lvl_lvl_252d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_103_equity_lvl_lvl_252d},
    "bals_104_equity_lvl_zscore_252d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_104_equity_lvl_zscore_252d},
    "bals_105_equity_lvl_rank_252d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_105_equity_lvl_rank_252d},
    "bals_106_debt_assets_lvl_5d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_106_debt_assets_lvl_5d},
    "bals_107_debt_assets_zscore_5d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_107_debt_assets_zscore_5d},
    "bals_108_debt_assets_rank_5d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_108_debt_assets_rank_5d},
    "bals_109_debt_assets_lvl_21d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_109_debt_assets_lvl_21d},
    "bals_110_debt_assets_zscore_21d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_110_debt_assets_zscore_21d},
    "bals_111_debt_assets_rank_21d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_111_debt_assets_rank_21d},
    "bals_112_debt_assets_lvl_63d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_112_debt_assets_lvl_63d},
    "bals_113_debt_assets_zscore_63d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_113_debt_assets_zscore_63d},
    "bals_114_debt_assets_rank_63d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_114_debt_assets_rank_63d},
    "bals_115_debt_assets_lvl_126d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_115_debt_assets_lvl_126d},
    "bals_116_debt_assets_zscore_126d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_116_debt_assets_zscore_126d},
    "bals_117_debt_assets_rank_126d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_117_debt_assets_rank_126d},
    "bals_118_debt_assets_lvl_252d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_118_debt_assets_lvl_252d},
    "bals_119_debt_assets_zscore_252d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_119_debt_assets_zscore_252d},
    "bals_120_debt_assets_rank_252d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_120_debt_assets_rank_252d},
    "bals_121_cash_debt_lvl_5d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_121_cash_debt_lvl_5d},
    "bals_122_cash_debt_zscore_5d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_122_cash_debt_zscore_5d},
    "bals_123_cash_debt_rank_5d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_123_cash_debt_rank_5d},
    "bals_124_cash_debt_lvl_21d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_124_cash_debt_lvl_21d},
    "bals_125_cash_debt_zscore_21d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_125_cash_debt_zscore_21d},
    "bals_126_cash_debt_rank_21d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_126_cash_debt_rank_21d},
    "bals_127_cash_debt_lvl_63d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_127_cash_debt_lvl_63d},
    "bals_128_cash_debt_zscore_63d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_128_cash_debt_zscore_63d},
    "bals_129_cash_debt_rank_63d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_129_cash_debt_rank_63d},
    "bals_130_cash_debt_lvl_126d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_130_cash_debt_lvl_126d},
    "bals_131_cash_debt_zscore_126d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_131_cash_debt_zscore_126d},
    "bals_132_cash_debt_rank_126d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_132_cash_debt_rank_126d},
    "bals_133_cash_debt_lvl_252d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_133_cash_debt_lvl_252d},
    "bals_134_cash_debt_zscore_252d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_134_cash_debt_zscore_252d},
    "bals_135_cash_debt_rank_252d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_135_cash_debt_rank_252d},
    "bals_136_net_debt_lvl_5d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_136_net_debt_lvl_5d},
    "bals_137_net_debt_zscore_5d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_137_net_debt_zscore_5d},
    "bals_138_net_debt_rank_5d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_138_net_debt_rank_5d},
    "bals_139_net_debt_lvl_21d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_139_net_debt_lvl_21d},
    "bals_140_net_debt_zscore_21d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_140_net_debt_zscore_21d},
    "bals_141_net_debt_rank_21d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_141_net_debt_rank_21d},
    "bals_142_net_debt_lvl_63d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_142_net_debt_lvl_63d},
    "bals_143_net_debt_zscore_63d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_143_net_debt_zscore_63d},
    "bals_144_net_debt_rank_63d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_144_net_debt_rank_63d},
    "bals_145_net_debt_lvl_126d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_145_net_debt_lvl_126d},
    "bals_146_net_debt_zscore_126d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_146_net_debt_zscore_126d},
    "bals_147_net_debt_rank_126d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_147_net_debt_rank_126d},
    "bals_148_net_debt_lvl_252d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_148_net_debt_lvl_252d},
    "bals_149_net_debt_zscore_252d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_149_net_debt_zscore_252d},
    "bals_150_net_debt_rank_252d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_150_net_debt_rank_252d},
}
