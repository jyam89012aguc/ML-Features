"""
36_profitability_snapshot — Base Features 076-150
Domain: profitability_snapshot
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

def prof_076_opinc_lvl_lvl_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_076_opinc_lvl_lvl_5d"""
    base = opinc
    return _rolling_mean(base, 5)

def prof_077_opinc_lvl_zscore_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_077_opinc_lvl_zscore_5d"""
    base = opinc
    return _zscore_rolling(base, 5)

def prof_078_opinc_lvl_rank_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_078_opinc_lvl_rank_5d"""
    base = opinc
    return _rank_pct(base, 5)

def prof_079_opinc_lvl_lvl_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_079_opinc_lvl_lvl_21d"""
    base = opinc
    return _rolling_mean(base, 21)

def prof_080_opinc_lvl_zscore_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_080_opinc_lvl_zscore_21d"""
    base = opinc
    return _zscore_rolling(base, 21)

def prof_081_opinc_lvl_rank_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_081_opinc_lvl_rank_21d"""
    base = opinc
    return _rank_pct(base, 21)

def prof_082_opinc_lvl_lvl_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_082_opinc_lvl_lvl_63d"""
    base = opinc
    return _rolling_mean(base, 63)

def prof_083_opinc_lvl_zscore_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_083_opinc_lvl_zscore_63d"""
    base = opinc
    return _zscore_rolling(base, 63)

def prof_084_opinc_lvl_rank_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_084_opinc_lvl_rank_63d"""
    base = opinc
    return _rank_pct(base, 63)

def prof_085_opinc_lvl_lvl_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_085_opinc_lvl_lvl_126d"""
    base = opinc
    return _rolling_mean(base, 126)

def prof_086_opinc_lvl_zscore_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_086_opinc_lvl_zscore_126d"""
    base = opinc
    return _zscore_rolling(base, 126)

def prof_087_opinc_lvl_rank_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_087_opinc_lvl_rank_126d"""
    base = opinc
    return _rank_pct(base, 126)

def prof_088_opinc_lvl_lvl_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_088_opinc_lvl_lvl_252d"""
    base = opinc
    return _rolling_mean(base, 252)

def prof_089_opinc_lvl_zscore_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_089_opinc_lvl_zscore_252d"""
    base = opinc
    return _zscore_rolling(base, 252)

def prof_090_opinc_lvl_rank_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_090_opinc_lvl_rank_252d"""
    base = opinc
    return _rank_pct(base, 252)

def prof_091_op_roe_lvl_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_091_op_roe_lvl_5d"""
    base = _safe_div(opinc, equity)
    return _rolling_mean(base, 5)

def prof_092_op_roe_zscore_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_092_op_roe_zscore_5d"""
    base = _safe_div(opinc, equity)
    return _zscore_rolling(base, 5)

def prof_093_op_roe_rank_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_093_op_roe_rank_5d"""
    base = _safe_div(opinc, equity)
    return _rank_pct(base, 5)

def prof_094_op_roe_lvl_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_094_op_roe_lvl_21d"""
    base = _safe_div(opinc, equity)
    return _rolling_mean(base, 21)

def prof_095_op_roe_zscore_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_095_op_roe_zscore_21d"""
    base = _safe_div(opinc, equity)
    return _zscore_rolling(base, 21)

def prof_096_op_roe_rank_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_096_op_roe_rank_21d"""
    base = _safe_div(opinc, equity)
    return _rank_pct(base, 21)

def prof_097_op_roe_lvl_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_097_op_roe_lvl_63d"""
    base = _safe_div(opinc, equity)
    return _rolling_mean(base, 63)

def prof_098_op_roe_zscore_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_098_op_roe_zscore_63d"""
    base = _safe_div(opinc, equity)
    return _zscore_rolling(base, 63)

def prof_099_op_roe_rank_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_099_op_roe_rank_63d"""
    base = _safe_div(opinc, equity)
    return _rank_pct(base, 63)

def prof_100_op_roe_lvl_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_100_op_roe_lvl_126d"""
    base = _safe_div(opinc, equity)
    return _rolling_mean(base, 126)

def prof_101_op_roe_zscore_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_101_op_roe_zscore_126d"""
    base = _safe_div(opinc, equity)
    return _zscore_rolling(base, 126)

def prof_102_op_roe_rank_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_102_op_roe_rank_126d"""
    base = _safe_div(opinc, equity)
    return _rank_pct(base, 126)

def prof_103_op_roe_lvl_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_103_op_roe_lvl_252d"""
    base = _safe_div(opinc, equity)
    return _rolling_mean(base, 252)

def prof_104_op_roe_zscore_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_104_op_roe_zscore_252d"""
    base = _safe_div(opinc, equity)
    return _zscore_rolling(base, 252)

def prof_105_op_roe_rank_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_105_op_roe_rank_252d"""
    base = _safe_div(opinc, equity)
    return _rank_pct(base, 252)

def prof_106_op_roa_lvl_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_106_op_roa_lvl_5d"""
    base = _safe_div(opinc, assets)
    return _rolling_mean(base, 5)

def prof_107_op_roa_zscore_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_107_op_roa_zscore_5d"""
    base = _safe_div(opinc, assets)
    return _zscore_rolling(base, 5)

def prof_108_op_roa_rank_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_108_op_roa_rank_5d"""
    base = _safe_div(opinc, assets)
    return _rank_pct(base, 5)

def prof_109_op_roa_lvl_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_109_op_roa_lvl_21d"""
    base = _safe_div(opinc, assets)
    return _rolling_mean(base, 21)

def prof_110_op_roa_zscore_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_110_op_roa_zscore_21d"""
    base = _safe_div(opinc, assets)
    return _zscore_rolling(base, 21)

def prof_111_op_roa_rank_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_111_op_roa_rank_21d"""
    base = _safe_div(opinc, assets)
    return _rank_pct(base, 21)

def prof_112_op_roa_lvl_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_112_op_roa_lvl_63d"""
    base = _safe_div(opinc, assets)
    return _rolling_mean(base, 63)

def prof_113_op_roa_zscore_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_113_op_roa_zscore_63d"""
    base = _safe_div(opinc, assets)
    return _zscore_rolling(base, 63)

def prof_114_op_roa_rank_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_114_op_roa_rank_63d"""
    base = _safe_div(opinc, assets)
    return _rank_pct(base, 63)

def prof_115_op_roa_lvl_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_115_op_roa_lvl_126d"""
    base = _safe_div(opinc, assets)
    return _rolling_mean(base, 126)

def prof_116_op_roa_zscore_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_116_op_roa_zscore_126d"""
    base = _safe_div(opinc, assets)
    return _zscore_rolling(base, 126)

def prof_117_op_roa_rank_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_117_op_roa_rank_126d"""
    base = _safe_div(opinc, assets)
    return _rank_pct(base, 126)

def prof_118_op_roa_lvl_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_118_op_roa_lvl_252d"""
    base = _safe_div(opinc, assets)
    return _rolling_mean(base, 252)

def prof_119_op_roa_zscore_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_119_op_roa_zscore_252d"""
    base = _safe_div(opinc, assets)
    return _zscore_rolling(base, 252)

def prof_120_op_roa_rank_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_120_op_roa_rank_252d"""
    base = _safe_div(opinc, assets)
    return _rank_pct(base, 252)

def prof_121_roic_proxy_lvl_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_121_roic_proxy_lvl_5d"""
    base = _safe_div(opinc, assets - liabs + debt)
    return _rolling_mean(base, 5)

def prof_122_roic_proxy_zscore_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_122_roic_proxy_zscore_5d"""
    base = _safe_div(opinc, assets - liabs + debt)
    return _zscore_rolling(base, 5)

def prof_123_roic_proxy_rank_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_123_roic_proxy_rank_5d"""
    base = _safe_div(opinc, assets - liabs + debt)
    return _rank_pct(base, 5)

def prof_124_roic_proxy_lvl_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_124_roic_proxy_lvl_21d"""
    base = _safe_div(opinc, assets - liabs + debt)
    return _rolling_mean(base, 21)

def prof_125_roic_proxy_zscore_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_125_roic_proxy_zscore_21d"""
    base = _safe_div(opinc, assets - liabs + debt)
    return _zscore_rolling(base, 21)

def prof_126_roic_proxy_rank_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_126_roic_proxy_rank_21d"""
    base = _safe_div(opinc, assets - liabs + debt)
    return _rank_pct(base, 21)

def prof_127_roic_proxy_lvl_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_127_roic_proxy_lvl_63d"""
    base = _safe_div(opinc, assets - liabs + debt)
    return _rolling_mean(base, 63)

def prof_128_roic_proxy_zscore_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_128_roic_proxy_zscore_63d"""
    base = _safe_div(opinc, assets - liabs + debt)
    return _zscore_rolling(base, 63)

def prof_129_roic_proxy_rank_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_129_roic_proxy_rank_63d"""
    base = _safe_div(opinc, assets - liabs + debt)
    return _rank_pct(base, 63)

def prof_130_roic_proxy_lvl_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_130_roic_proxy_lvl_126d"""
    base = _safe_div(opinc, assets - liabs + debt)
    return _rolling_mean(base, 126)

def prof_131_roic_proxy_zscore_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_131_roic_proxy_zscore_126d"""
    base = _safe_div(opinc, assets - liabs + debt)
    return _zscore_rolling(base, 126)

def prof_132_roic_proxy_rank_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_132_roic_proxy_rank_126d"""
    base = _safe_div(opinc, assets - liabs + debt)
    return _rank_pct(base, 126)

def prof_133_roic_proxy_lvl_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_133_roic_proxy_lvl_252d"""
    base = _safe_div(opinc, assets - liabs + debt)
    return _rolling_mean(base, 252)

def prof_134_roic_proxy_zscore_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_134_roic_proxy_zscore_252d"""
    base = _safe_div(opinc, assets - liabs + debt)
    return _zscore_rolling(base, 252)

def prof_135_roic_proxy_rank_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_135_roic_proxy_rank_252d"""
    base = _safe_div(opinc, assets - liabs + debt)
    return _rank_pct(base, 252)

def prof_136_net_op_rat_lvl_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_136_net_op_rat_lvl_5d"""
    base = _safe_div(netinc, opinc.abs())
    return _rolling_mean(base, 5)

def prof_137_net_op_rat_zscore_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_137_net_op_rat_zscore_5d"""
    base = _safe_div(netinc, opinc.abs())
    return _zscore_rolling(base, 5)

def prof_138_net_op_rat_rank_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_138_net_op_rat_rank_5d"""
    base = _safe_div(netinc, opinc.abs())
    return _rank_pct(base, 5)

def prof_139_net_op_rat_lvl_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_139_net_op_rat_lvl_21d"""
    base = _safe_div(netinc, opinc.abs())
    return _rolling_mean(base, 21)

def prof_140_net_op_rat_zscore_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_140_net_op_rat_zscore_21d"""
    base = _safe_div(netinc, opinc.abs())
    return _zscore_rolling(base, 21)

def prof_141_net_op_rat_rank_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_141_net_op_rat_rank_21d"""
    base = _safe_div(netinc, opinc.abs())
    return _rank_pct(base, 21)

def prof_142_net_op_rat_lvl_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_142_net_op_rat_lvl_63d"""
    base = _safe_div(netinc, opinc.abs())
    return _rolling_mean(base, 63)

def prof_143_net_op_rat_zscore_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_143_net_op_rat_zscore_63d"""
    base = _safe_div(netinc, opinc.abs())
    return _zscore_rolling(base, 63)

def prof_144_net_op_rat_rank_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_144_net_op_rat_rank_63d"""
    base = _safe_div(netinc, opinc.abs())
    return _rank_pct(base, 63)

def prof_145_net_op_rat_lvl_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_145_net_op_rat_lvl_126d"""
    base = _safe_div(netinc, opinc.abs())
    return _rolling_mean(base, 126)

def prof_146_net_op_rat_zscore_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_146_net_op_rat_zscore_126d"""
    base = _safe_div(netinc, opinc.abs())
    return _zscore_rolling(base, 126)

def prof_147_net_op_rat_rank_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_147_net_op_rat_rank_126d"""
    base = _safe_div(netinc, opinc.abs())
    return _rank_pct(base, 126)

def prof_148_net_op_rat_lvl_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_148_net_op_rat_lvl_252d"""
    base = _safe_div(netinc, opinc.abs())
    return _rolling_mean(base, 252)

def prof_149_net_op_rat_zscore_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_149_net_op_rat_zscore_252d"""
    base = _safe_div(netinc, opinc.abs())
    return _zscore_rolling(base, 252)

def prof_150_net_op_rat_rank_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_150_net_op_rat_rank_252d"""
    base = _safe_div(netinc, opinc.abs())
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V36_REGISTRY_2 = {
    "prof_076_opinc_lvl_lvl_5d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_076_opinc_lvl_lvl_5d},
    "prof_077_opinc_lvl_zscore_5d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_077_opinc_lvl_zscore_5d},
    "prof_078_opinc_lvl_rank_5d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_078_opinc_lvl_rank_5d},
    "prof_079_opinc_lvl_lvl_21d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_079_opinc_lvl_lvl_21d},
    "prof_080_opinc_lvl_zscore_21d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_080_opinc_lvl_zscore_21d},
    "prof_081_opinc_lvl_rank_21d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_081_opinc_lvl_rank_21d},
    "prof_082_opinc_lvl_lvl_63d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_082_opinc_lvl_lvl_63d},
    "prof_083_opinc_lvl_zscore_63d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_083_opinc_lvl_zscore_63d},
    "prof_084_opinc_lvl_rank_63d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_084_opinc_lvl_rank_63d},
    "prof_085_opinc_lvl_lvl_126d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_085_opinc_lvl_lvl_126d},
    "prof_086_opinc_lvl_zscore_126d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_086_opinc_lvl_zscore_126d},
    "prof_087_opinc_lvl_rank_126d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_087_opinc_lvl_rank_126d},
    "prof_088_opinc_lvl_lvl_252d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_088_opinc_lvl_lvl_252d},
    "prof_089_opinc_lvl_zscore_252d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_089_opinc_lvl_zscore_252d},
    "prof_090_opinc_lvl_rank_252d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_090_opinc_lvl_rank_252d},
    "prof_091_op_roe_lvl_5d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_091_op_roe_lvl_5d},
    "prof_092_op_roe_zscore_5d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_092_op_roe_zscore_5d},
    "prof_093_op_roe_rank_5d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_093_op_roe_rank_5d},
    "prof_094_op_roe_lvl_21d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_094_op_roe_lvl_21d},
    "prof_095_op_roe_zscore_21d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_095_op_roe_zscore_21d},
    "prof_096_op_roe_rank_21d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_096_op_roe_rank_21d},
    "prof_097_op_roe_lvl_63d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_097_op_roe_lvl_63d},
    "prof_098_op_roe_zscore_63d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_098_op_roe_zscore_63d},
    "prof_099_op_roe_rank_63d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_099_op_roe_rank_63d},
    "prof_100_op_roe_lvl_126d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_100_op_roe_lvl_126d},
    "prof_101_op_roe_zscore_126d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_101_op_roe_zscore_126d},
    "prof_102_op_roe_rank_126d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_102_op_roe_rank_126d},
    "prof_103_op_roe_lvl_252d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_103_op_roe_lvl_252d},
    "prof_104_op_roe_zscore_252d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_104_op_roe_zscore_252d},
    "prof_105_op_roe_rank_252d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_105_op_roe_rank_252d},
    "prof_106_op_roa_lvl_5d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_106_op_roa_lvl_5d},
    "prof_107_op_roa_zscore_5d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_107_op_roa_zscore_5d},
    "prof_108_op_roa_rank_5d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_108_op_roa_rank_5d},
    "prof_109_op_roa_lvl_21d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_109_op_roa_lvl_21d},
    "prof_110_op_roa_zscore_21d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_110_op_roa_zscore_21d},
    "prof_111_op_roa_rank_21d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_111_op_roa_rank_21d},
    "prof_112_op_roa_lvl_63d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_112_op_roa_lvl_63d},
    "prof_113_op_roa_zscore_63d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_113_op_roa_zscore_63d},
    "prof_114_op_roa_rank_63d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_114_op_roa_rank_63d},
    "prof_115_op_roa_lvl_126d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_115_op_roa_lvl_126d},
    "prof_116_op_roa_zscore_126d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_116_op_roa_zscore_126d},
    "prof_117_op_roa_rank_126d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_117_op_roa_rank_126d},
    "prof_118_op_roa_lvl_252d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_118_op_roa_lvl_252d},
    "prof_119_op_roa_zscore_252d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_119_op_roa_zscore_252d},
    "prof_120_op_roa_rank_252d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_120_op_roa_rank_252d},
    "prof_121_roic_proxy_lvl_5d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_121_roic_proxy_lvl_5d},
    "prof_122_roic_proxy_zscore_5d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_122_roic_proxy_zscore_5d},
    "prof_123_roic_proxy_rank_5d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_123_roic_proxy_rank_5d},
    "prof_124_roic_proxy_lvl_21d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_124_roic_proxy_lvl_21d},
    "prof_125_roic_proxy_zscore_21d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_125_roic_proxy_zscore_21d},
    "prof_126_roic_proxy_rank_21d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_126_roic_proxy_rank_21d},
    "prof_127_roic_proxy_lvl_63d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_127_roic_proxy_lvl_63d},
    "prof_128_roic_proxy_zscore_63d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_128_roic_proxy_zscore_63d},
    "prof_129_roic_proxy_rank_63d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_129_roic_proxy_rank_63d},
    "prof_130_roic_proxy_lvl_126d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_130_roic_proxy_lvl_126d},
    "prof_131_roic_proxy_zscore_126d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_131_roic_proxy_zscore_126d},
    "prof_132_roic_proxy_rank_126d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_132_roic_proxy_rank_126d},
    "prof_133_roic_proxy_lvl_252d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_133_roic_proxy_lvl_252d},
    "prof_134_roic_proxy_zscore_252d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_134_roic_proxy_zscore_252d},
    "prof_135_roic_proxy_rank_252d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_135_roic_proxy_rank_252d},
    "prof_136_net_op_rat_lvl_5d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_136_net_op_rat_lvl_5d},
    "prof_137_net_op_rat_zscore_5d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_137_net_op_rat_zscore_5d},
    "prof_138_net_op_rat_rank_5d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_138_net_op_rat_rank_5d},
    "prof_139_net_op_rat_lvl_21d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_139_net_op_rat_lvl_21d},
    "prof_140_net_op_rat_zscore_21d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_140_net_op_rat_zscore_21d},
    "prof_141_net_op_rat_rank_21d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_141_net_op_rat_rank_21d},
    "prof_142_net_op_rat_lvl_63d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_142_net_op_rat_lvl_63d},
    "prof_143_net_op_rat_zscore_63d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_143_net_op_rat_zscore_63d},
    "prof_144_net_op_rat_rank_63d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_144_net_op_rat_rank_63d},
    "prof_145_net_op_rat_lvl_126d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_145_net_op_rat_lvl_126d},
    "prof_146_net_op_rat_zscore_126d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_146_net_op_rat_zscore_126d},
    "prof_147_net_op_rat_rank_126d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_147_net_op_rat_rank_126d},
    "prof_148_net_op_rat_lvl_252d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_148_net_op_rat_lvl_252d},
    "prof_149_net_op_rat_zscore_252d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_149_net_op_rat_zscore_252d},
    "prof_150_net_op_rat_rank_252d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_150_net_op_rat_rank_252d},
}
