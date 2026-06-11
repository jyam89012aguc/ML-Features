"""
121_distress_score_ensemble — Base Features Part 2
Domain: distress_score_ensemble
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

def dsen_121_ensemble_zscore_lvl_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_121_ensemble_zscore_lvl_5d
    ECONOMIC RATIONALE: Integrated balance sheet and income statement distress.
    """
    base = _zscore_rolling(liabs/assets.replace(0, 1e-9) - ocf/assets.replace(0, 1e-9), 252)
    return _rolling_mean(base, 5)

def dsen_122_ensemble_zscore_zscore_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_122_ensemble_zscore_zscore_5d
    ECONOMIC RATIONALE: Integrated balance sheet and income statement distress.
    """
    base = _zscore_rolling(liabs/assets.replace(0, 1e-9) - ocf/assets.replace(0, 1e-9), 252)
    return _zscore_rolling(base, 5)

def dsen_123_ensemble_zscore_rank_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_123_ensemble_zscore_rank_5d
    ECONOMIC RATIONALE: Integrated balance sheet and income statement distress.
    """
    base = _zscore_rolling(liabs/assets.replace(0, 1e-9) - ocf/assets.replace(0, 1e-9), 252)
    return _rank_pct(base, 5)

def dsen_124_ensemble_zscore_lvl_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_124_ensemble_zscore_lvl_21d
    ECONOMIC RATIONALE: Integrated balance sheet and income statement distress.
    """
    base = _zscore_rolling(liabs/assets.replace(0, 1e-9) - ocf/assets.replace(0, 1e-9), 252)
    return _rolling_mean(base, 21)

def dsen_125_ensemble_zscore_zscore_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_125_ensemble_zscore_zscore_21d
    ECONOMIC RATIONALE: Integrated balance sheet and income statement distress.
    """
    base = _zscore_rolling(liabs/assets.replace(0, 1e-9) - ocf/assets.replace(0, 1e-9), 252)
    return _zscore_rolling(base, 21)

def dsen_126_ensemble_zscore_rank_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_126_ensemble_zscore_rank_21d
    ECONOMIC RATIONALE: Integrated balance sheet and income statement distress.
    """
    base = _zscore_rolling(liabs/assets.replace(0, 1e-9) - ocf/assets.replace(0, 1e-9), 252)
    return _rank_pct(base, 21)

def dsen_127_ensemble_zscore_lvl_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_127_ensemble_zscore_lvl_63d
    ECONOMIC RATIONALE: Integrated balance sheet and income statement distress.
    """
    base = _zscore_rolling(liabs/assets.replace(0, 1e-9) - ocf/assets.replace(0, 1e-9), 252)
    return _rolling_mean(base, 63)

def dsen_128_ensemble_zscore_zscore_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_128_ensemble_zscore_zscore_63d
    ECONOMIC RATIONALE: Integrated balance sheet and income statement distress.
    """
    base = _zscore_rolling(liabs/assets.replace(0, 1e-9) - ocf/assets.replace(0, 1e-9), 252)
    return _zscore_rolling(base, 63)

def dsen_129_ensemble_zscore_rank_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_129_ensemble_zscore_rank_63d
    ECONOMIC RATIONALE: Integrated balance sheet and income statement distress.
    """
    base = _zscore_rolling(liabs/assets.replace(0, 1e-9) - ocf/assets.replace(0, 1e-9), 252)
    return _rank_pct(base, 63)

def dsen_130_ensemble_zscore_lvl_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_130_ensemble_zscore_lvl_126d
    ECONOMIC RATIONALE: Integrated balance sheet and income statement distress.
    """
    base = _zscore_rolling(liabs/assets.replace(0, 1e-9) - ocf/assets.replace(0, 1e-9), 252)
    return _rolling_mean(base, 126)

def dsen_131_ensemble_zscore_zscore_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_131_ensemble_zscore_zscore_126d
    ECONOMIC RATIONALE: Integrated balance sheet and income statement distress.
    """
    base = _zscore_rolling(liabs/assets.replace(0, 1e-9) - ocf/assets.replace(0, 1e-9), 252)
    return _zscore_rolling(base, 126)

def dsen_132_ensemble_zscore_rank_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_132_ensemble_zscore_rank_126d
    ECONOMIC RATIONALE: Integrated balance sheet and income statement distress.
    """
    base = _zscore_rolling(liabs/assets.replace(0, 1e-9) - ocf/assets.replace(0, 1e-9), 252)
    return _rank_pct(base, 126)

def dsen_133_ensemble_zscore_lvl_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_133_ensemble_zscore_lvl_252d
    ECONOMIC RATIONALE: Integrated balance sheet and income statement distress.
    """
    base = _zscore_rolling(liabs/assets.replace(0, 1e-9) - ocf/assets.replace(0, 1e-9), 252)
    return _rolling_mean(base, 252)

def dsen_134_ensemble_zscore_zscore_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_134_ensemble_zscore_zscore_252d
    ECONOMIC RATIONALE: Integrated balance sheet and income statement distress.
    """
    base = _zscore_rolling(liabs/assets.replace(0, 1e-9) - ocf/assets.replace(0, 1e-9), 252)
    return _zscore_rolling(base, 252)

def dsen_135_ensemble_zscore_rank_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_135_ensemble_zscore_rank_252d
    ECONOMIC RATIONALE: Integrated balance sheet and income statement distress.
    """
    base = _zscore_rolling(liabs/assets.replace(0, 1e-9) - ocf/assets.replace(0, 1e-9), 252)
    return _rank_pct(base, 252)

def dsen_136_market_distress_beta_lvl_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_136_market_distress_beta_lvl_5d
    ECONOMIC RATIONALE: Market sensitivity weighted by financial risk.
    """
    base = close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)) * (liabs/equity.replace(0, 1e-9))
    return _rolling_mean(base, 5)

def dsen_137_market_distress_beta_zscore_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_137_market_distress_beta_zscore_5d
    ECONOMIC RATIONALE: Market sensitivity weighted by financial risk.
    """
    base = close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)) * (liabs/equity.replace(0, 1e-9))
    return _zscore_rolling(base, 5)

def dsen_138_market_distress_beta_rank_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_138_market_distress_beta_rank_5d
    ECONOMIC RATIONALE: Market sensitivity weighted by financial risk.
    """
    base = close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)) * (liabs/equity.replace(0, 1e-9))
    return _rank_pct(base, 5)

def dsen_139_market_distress_beta_lvl_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_139_market_distress_beta_lvl_21d
    ECONOMIC RATIONALE: Market sensitivity weighted by financial risk.
    """
    base = close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)) * (liabs/equity.replace(0, 1e-9))
    return _rolling_mean(base, 21)

def dsen_140_market_distress_beta_zscore_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_140_market_distress_beta_zscore_21d
    ECONOMIC RATIONALE: Market sensitivity weighted by financial risk.
    """
    base = close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)) * (liabs/equity.replace(0, 1e-9))
    return _zscore_rolling(base, 21)

def dsen_141_market_distress_beta_rank_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_141_market_distress_beta_rank_21d
    ECONOMIC RATIONALE: Market sensitivity weighted by financial risk.
    """
    base = close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)) * (liabs/equity.replace(0, 1e-9))
    return _rank_pct(base, 21)

def dsen_142_market_distress_beta_lvl_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_142_market_distress_beta_lvl_63d
    ECONOMIC RATIONALE: Market sensitivity weighted by financial risk.
    """
    base = close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)) * (liabs/equity.replace(0, 1e-9))
    return _rolling_mean(base, 63)

def dsen_143_market_distress_beta_zscore_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_143_market_distress_beta_zscore_63d
    ECONOMIC RATIONALE: Market sensitivity weighted by financial risk.
    """
    base = close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)) * (liabs/equity.replace(0, 1e-9))
    return _zscore_rolling(base, 63)

def dsen_144_market_distress_beta_rank_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_144_market_distress_beta_rank_63d
    ECONOMIC RATIONALE: Market sensitivity weighted by financial risk.
    """
    base = close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)) * (liabs/equity.replace(0, 1e-9))
    return _rank_pct(base, 63)

def dsen_145_market_distress_beta_lvl_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_145_market_distress_beta_lvl_126d
    ECONOMIC RATIONALE: Market sensitivity weighted by financial risk.
    """
    base = close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)) * (liabs/equity.replace(0, 1e-9))
    return _rolling_mean(base, 126)

def dsen_146_market_distress_beta_zscore_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_146_market_distress_beta_zscore_126d
    ECONOMIC RATIONALE: Market sensitivity weighted by financial risk.
    """
    base = close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)) * (liabs/equity.replace(0, 1e-9))
    return _zscore_rolling(base, 126)

def dsen_147_market_distress_beta_rank_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_147_market_distress_beta_rank_126d
    ECONOMIC RATIONALE: Market sensitivity weighted by financial risk.
    """
    base = close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)) * (liabs/equity.replace(0, 1e-9))
    return _rank_pct(base, 126)

def dsen_148_market_distress_beta_lvl_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_148_market_distress_beta_lvl_252d
    ECONOMIC RATIONALE: Market sensitivity weighted by financial risk.
    """
    base = close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)) * (liabs/equity.replace(0, 1e-9))
    return _rolling_mean(base, 252)

def dsen_149_market_distress_beta_zscore_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_149_market_distress_beta_zscore_252d
    ECONOMIC RATIONALE: Market sensitivity weighted by financial risk.
    """
    base = close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)) * (liabs/equity.replace(0, 1e-9))
    return _zscore_rolling(base, 252)

def dsen_150_market_distress_beta_rank_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_150_market_distress_beta_rank_252d
    ECONOMIC RATIONALE: Market sensitivity weighted by financial risk.
    """
    base = close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)) * (liabs/equity.replace(0, 1e-9))
    return _rank_pct(base, 252)

def dsen_151_ensemble_drawdown_rank_lvl_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_151_ensemble_drawdown_rank_lvl_5d
    ECONOMIC RATIONALE: Rank of combined price and leverage stress.
    """
    base = _rank_pct(close/close.rolling(252).max() + liabs/assets.replace(0, 1e-9), 252)
    return _rolling_mean(base, 5)

def dsen_152_ensemble_drawdown_rank_zscore_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_152_ensemble_drawdown_rank_zscore_5d
    ECONOMIC RATIONALE: Rank of combined price and leverage stress.
    """
    base = _rank_pct(close/close.rolling(252).max() + liabs/assets.replace(0, 1e-9), 252)
    return _zscore_rolling(base, 5)

def dsen_153_ensemble_drawdown_rank_rank_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_153_ensemble_drawdown_rank_rank_5d
    ECONOMIC RATIONALE: Rank of combined price and leverage stress.
    """
    base = _rank_pct(close/close.rolling(252).max() + liabs/assets.replace(0, 1e-9), 252)
    return _rank_pct(base, 5)

def dsen_154_ensemble_drawdown_rank_lvl_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_154_ensemble_drawdown_rank_lvl_21d
    ECONOMIC RATIONALE: Rank of combined price and leverage stress.
    """
    base = _rank_pct(close/close.rolling(252).max() + liabs/assets.replace(0, 1e-9), 252)
    return _rolling_mean(base, 21)

def dsen_155_ensemble_drawdown_rank_zscore_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_155_ensemble_drawdown_rank_zscore_21d
    ECONOMIC RATIONALE: Rank of combined price and leverage stress.
    """
    base = _rank_pct(close/close.rolling(252).max() + liabs/assets.replace(0, 1e-9), 252)
    return _zscore_rolling(base, 21)

def dsen_156_ensemble_drawdown_rank_rank_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_156_ensemble_drawdown_rank_rank_21d
    ECONOMIC RATIONALE: Rank of combined price and leverage stress.
    """
    base = _rank_pct(close/close.rolling(252).max() + liabs/assets.replace(0, 1e-9), 252)
    return _rank_pct(base, 21)

def dsen_157_ensemble_drawdown_rank_lvl_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_157_ensemble_drawdown_rank_lvl_63d
    ECONOMIC RATIONALE: Rank of combined price and leverage stress.
    """
    base = _rank_pct(close/close.rolling(252).max() + liabs/assets.replace(0, 1e-9), 252)
    return _rolling_mean(base, 63)

def dsen_158_ensemble_drawdown_rank_zscore_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_158_ensemble_drawdown_rank_zscore_63d
    ECONOMIC RATIONALE: Rank of combined price and leverage stress.
    """
    base = _rank_pct(close/close.rolling(252).max() + liabs/assets.replace(0, 1e-9), 252)
    return _zscore_rolling(base, 63)

def dsen_159_ensemble_drawdown_rank_rank_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_159_ensemble_drawdown_rank_rank_63d
    ECONOMIC RATIONALE: Rank of combined price and leverage stress.
    """
    base = _rank_pct(close/close.rolling(252).max() + liabs/assets.replace(0, 1e-9), 252)
    return _rank_pct(base, 63)

def dsen_160_ensemble_drawdown_rank_lvl_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_160_ensemble_drawdown_rank_lvl_126d
    ECONOMIC RATIONALE: Rank of combined price and leverage stress.
    """
    base = _rank_pct(close/close.rolling(252).max() + liabs/assets.replace(0, 1e-9), 252)
    return _rolling_mean(base, 126)

def dsen_161_ensemble_drawdown_rank_zscore_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_161_ensemble_drawdown_rank_zscore_126d
    ECONOMIC RATIONALE: Rank of combined price and leverage stress.
    """
    base = _rank_pct(close/close.rolling(252).max() + liabs/assets.replace(0, 1e-9), 252)
    return _zscore_rolling(base, 126)

def dsen_162_ensemble_drawdown_rank_rank_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_162_ensemble_drawdown_rank_rank_126d
    ECONOMIC RATIONALE: Rank of combined price and leverage stress.
    """
    base = _rank_pct(close/close.rolling(252).max() + liabs/assets.replace(0, 1e-9), 252)
    return _rank_pct(base, 126)

def dsen_163_ensemble_drawdown_rank_lvl_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_163_ensemble_drawdown_rank_lvl_252d
    ECONOMIC RATIONALE: Rank of combined price and leverage stress.
    """
    base = _rank_pct(close/close.rolling(252).max() + liabs/assets.replace(0, 1e-9), 252)
    return _rolling_mean(base, 252)

def dsen_164_ensemble_drawdown_rank_zscore_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_164_ensemble_drawdown_rank_zscore_252d
    ECONOMIC RATIONALE: Rank of combined price and leverage stress.
    """
    base = _rank_pct(close/close.rolling(252).max() + liabs/assets.replace(0, 1e-9), 252)
    return _zscore_rolling(base, 252)

def dsen_165_ensemble_drawdown_rank_rank_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_165_ensemble_drawdown_rank_rank_252d
    ECONOMIC RATIONALE: Rank of combined price and leverage stress.
    """
    base = _rank_pct(close/close.rolling(252).max() + liabs/assets.replace(0, 1e-9), 252)
    return _rank_pct(base, 252)

def dsen_166_distress_reversal_potential_lvl_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_166_distress_reversal_potential_lvl_5d
    ECONOMIC RATIONALE: Reversal potential for highly levered distressed firms.
    """
    base = close.pct_change(5) * (liabs/equity.replace(0, 1e-9) > 2).astype(float)
    return _rolling_mean(base, 5)

def dsen_167_distress_reversal_potential_zscore_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_167_distress_reversal_potential_zscore_5d
    ECONOMIC RATIONALE: Reversal potential for highly levered distressed firms.
    """
    base = close.pct_change(5) * (liabs/equity.replace(0, 1e-9) > 2).astype(float)
    return _zscore_rolling(base, 5)

def dsen_168_distress_reversal_potential_rank_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_168_distress_reversal_potential_rank_5d
    ECONOMIC RATIONALE: Reversal potential for highly levered distressed firms.
    """
    base = close.pct_change(5) * (liabs/equity.replace(0, 1e-9) > 2).astype(float)
    return _rank_pct(base, 5)

def dsen_169_distress_reversal_potential_lvl_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_169_distress_reversal_potential_lvl_21d
    ECONOMIC RATIONALE: Reversal potential for highly levered distressed firms.
    """
    base = close.pct_change(5) * (liabs/equity.replace(0, 1e-9) > 2).astype(float)
    return _rolling_mean(base, 21)

def dsen_170_distress_reversal_potential_zscore_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_170_distress_reversal_potential_zscore_21d
    ECONOMIC RATIONALE: Reversal potential for highly levered distressed firms.
    """
    base = close.pct_change(5) * (liabs/equity.replace(0, 1e-9) > 2).astype(float)
    return _zscore_rolling(base, 21)

def dsen_171_distress_reversal_potential_rank_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_171_distress_reversal_potential_rank_21d
    ECONOMIC RATIONALE: Reversal potential for highly levered distressed firms.
    """
    base = close.pct_change(5) * (liabs/equity.replace(0, 1e-9) > 2).astype(float)
    return _rank_pct(base, 21)

def dsen_172_distress_reversal_potential_lvl_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_172_distress_reversal_potential_lvl_63d
    ECONOMIC RATIONALE: Reversal potential for highly levered distressed firms.
    """
    base = close.pct_change(5) * (liabs/equity.replace(0, 1e-9) > 2).astype(float)
    return _rolling_mean(base, 63)

def dsen_173_distress_reversal_potential_zscore_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_173_distress_reversal_potential_zscore_63d
    ECONOMIC RATIONALE: Reversal potential for highly levered distressed firms.
    """
    base = close.pct_change(5) * (liabs/equity.replace(0, 1e-9) > 2).astype(float)
    return _zscore_rolling(base, 63)

def dsen_174_distress_reversal_potential_rank_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_174_distress_reversal_potential_rank_63d
    ECONOMIC RATIONALE: Reversal potential for highly levered distressed firms.
    """
    base = close.pct_change(5) * (liabs/equity.replace(0, 1e-9) > 2).astype(float)
    return _rank_pct(base, 63)

def dsen_175_distress_reversal_potential_lvl_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_175_distress_reversal_potential_lvl_126d
    ECONOMIC RATIONALE: Reversal potential for highly levered distressed firms.
    """
    base = close.pct_change(5) * (liabs/equity.replace(0, 1e-9) > 2).astype(float)
    return _rolling_mean(base, 126)

def dsen_176_distress_reversal_potential_zscore_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_176_distress_reversal_potential_zscore_126d
    ECONOMIC RATIONALE: Reversal potential for highly levered distressed firms.
    """
    base = close.pct_change(5) * (liabs/equity.replace(0, 1e-9) > 2).astype(float)
    return _zscore_rolling(base, 126)

def dsen_177_distress_reversal_potential_rank_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_177_distress_reversal_potential_rank_126d
    ECONOMIC RATIONALE: Reversal potential for highly levered distressed firms.
    """
    base = close.pct_change(5) * (liabs/equity.replace(0, 1e-9) > 2).astype(float)
    return _rank_pct(base, 126)

def dsen_178_distress_reversal_potential_lvl_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_178_distress_reversal_potential_lvl_252d
    ECONOMIC RATIONALE: Reversal potential for highly levered distressed firms.
    """
    base = close.pct_change(5) * (liabs/equity.replace(0, 1e-9) > 2).astype(float)
    return _rolling_mean(base, 252)

def dsen_179_distress_reversal_potential_zscore_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_179_distress_reversal_potential_zscore_252d
    ECONOMIC RATIONALE: Reversal potential for highly levered distressed firms.
    """
    base = close.pct_change(5) * (liabs/equity.replace(0, 1e-9) > 2).astype(float)
    return _zscore_rolling(base, 252)

def dsen_180_distress_reversal_potential_rank_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_180_distress_reversal_potential_rank_252d
    ECONOMIC RATIONALE: Reversal potential for highly levered distressed firms.
    """
    base = close.pct_change(5) * (liabs/equity.replace(0, 1e-9) > 2).astype(float)
    return _rank_pct(base, 252)

def dsen_181_ensemble_liquidity_gap_lvl_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_181_ensemble_liquidity_gap_lvl_5d
    ECONOMIC RATIONALE: Net cash flow after change in liabilities.
    """
    base = ocf - liabs.diff(63)
    return _rolling_mean(base, 5)

def dsen_182_ensemble_liquidity_gap_zscore_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_182_ensemble_liquidity_gap_zscore_5d
    ECONOMIC RATIONALE: Net cash flow after change in liabilities.
    """
    base = ocf - liabs.diff(63)
    return _zscore_rolling(base, 5)

def dsen_183_ensemble_liquidity_gap_rank_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_183_ensemble_liquidity_gap_rank_5d
    ECONOMIC RATIONALE: Net cash flow after change in liabilities.
    """
    base = ocf - liabs.diff(63)
    return _rank_pct(base, 5)

def dsen_184_ensemble_liquidity_gap_lvl_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_184_ensemble_liquidity_gap_lvl_21d
    ECONOMIC RATIONALE: Net cash flow after change in liabilities.
    """
    base = ocf - liabs.diff(63)
    return _rolling_mean(base, 21)

def dsen_185_ensemble_liquidity_gap_zscore_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_185_ensemble_liquidity_gap_zscore_21d
    ECONOMIC RATIONALE: Net cash flow after change in liabilities.
    """
    base = ocf - liabs.diff(63)
    return _zscore_rolling(base, 21)

def dsen_186_ensemble_liquidity_gap_rank_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_186_ensemble_liquidity_gap_rank_21d
    ECONOMIC RATIONALE: Net cash flow after change in liabilities.
    """
    base = ocf - liabs.diff(63)
    return _rank_pct(base, 21)

def dsen_187_ensemble_liquidity_gap_lvl_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_187_ensemble_liquidity_gap_lvl_63d
    ECONOMIC RATIONALE: Net cash flow after change in liabilities.
    """
    base = ocf - liabs.diff(63)
    return _rolling_mean(base, 63)

def dsen_188_ensemble_liquidity_gap_zscore_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_188_ensemble_liquidity_gap_zscore_63d
    ECONOMIC RATIONALE: Net cash flow after change in liabilities.
    """
    base = ocf - liabs.diff(63)
    return _zscore_rolling(base, 63)

def dsen_189_ensemble_liquidity_gap_rank_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_189_ensemble_liquidity_gap_rank_63d
    ECONOMIC RATIONALE: Net cash flow after change in liabilities.
    """
    base = ocf - liabs.diff(63)
    return _rank_pct(base, 63)

def dsen_190_ensemble_liquidity_gap_lvl_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_190_ensemble_liquidity_gap_lvl_126d
    ECONOMIC RATIONALE: Net cash flow after change in liabilities.
    """
    base = ocf - liabs.diff(63)
    return _rolling_mean(base, 126)

def dsen_191_ensemble_liquidity_gap_zscore_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_191_ensemble_liquidity_gap_zscore_126d
    ECONOMIC RATIONALE: Net cash flow after change in liabilities.
    """
    base = ocf - liabs.diff(63)
    return _zscore_rolling(base, 126)

def dsen_192_ensemble_liquidity_gap_rank_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_192_ensemble_liquidity_gap_rank_126d
    ECONOMIC RATIONALE: Net cash flow after change in liabilities.
    """
    base = ocf - liabs.diff(63)
    return _rank_pct(base, 126)

def dsen_193_ensemble_liquidity_gap_lvl_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_193_ensemble_liquidity_gap_lvl_252d
    ECONOMIC RATIONALE: Net cash flow after change in liabilities.
    """
    base = ocf - liabs.diff(63)
    return _rolling_mean(base, 252)

def dsen_194_ensemble_liquidity_gap_zscore_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_194_ensemble_liquidity_gap_zscore_252d
    ECONOMIC RATIONALE: Net cash flow after change in liabilities.
    """
    base = ocf - liabs.diff(63)
    return _zscore_rolling(base, 252)

def dsen_195_ensemble_liquidity_gap_rank_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_195_ensemble_liquidity_gap_rank_252d
    ECONOMIC RATIONALE: Net cash flow after change in liabilities.
    """
    base = ocf - liabs.diff(63)
    return _rank_pct(base, 252)

def dsen_196_structural_fragility_index_lvl_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_196_structural_fragility_index_lvl_5d
    ECONOMIC RATIONALE: Financial leverage relative to price stability.
    """
    base = (liabs/equity.replace(0, 1e-9)) / close.rolling(252).std().replace(0, 1e-9)
    return _rolling_mean(base, 5)

def dsen_197_structural_fragility_index_zscore_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_197_structural_fragility_index_zscore_5d
    ECONOMIC RATIONALE: Financial leverage relative to price stability.
    """
    base = (liabs/equity.replace(0, 1e-9)) / close.rolling(252).std().replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def dsen_198_structural_fragility_index_rank_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_198_structural_fragility_index_rank_5d
    ECONOMIC RATIONALE: Financial leverage relative to price stability.
    """
    base = (liabs/equity.replace(0, 1e-9)) / close.rolling(252).std().replace(0, 1e-9)
    return _rank_pct(base, 5)

def dsen_199_structural_fragility_index_lvl_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_199_structural_fragility_index_lvl_21d
    ECONOMIC RATIONALE: Financial leverage relative to price stability.
    """
    base = (liabs/equity.replace(0, 1e-9)) / close.rolling(252).std().replace(0, 1e-9)
    return _rolling_mean(base, 21)

def dsen_200_structural_fragility_index_zscore_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_200_structural_fragility_index_zscore_21d
    ECONOMIC RATIONALE: Financial leverage relative to price stability.
    """
    base = (liabs/equity.replace(0, 1e-9)) / close.rolling(252).std().replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def dsen_201_structural_fragility_index_rank_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_201_structural_fragility_index_rank_21d
    ECONOMIC RATIONALE: Financial leverage relative to price stability.
    """
    base = (liabs/equity.replace(0, 1e-9)) / close.rolling(252).std().replace(0, 1e-9)
    return _rank_pct(base, 21)

def dsen_202_structural_fragility_index_lvl_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_202_structural_fragility_index_lvl_63d
    ECONOMIC RATIONALE: Financial leverage relative to price stability.
    """
    base = (liabs/equity.replace(0, 1e-9)) / close.rolling(252).std().replace(0, 1e-9)
    return _rolling_mean(base, 63)

def dsen_203_structural_fragility_index_zscore_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_203_structural_fragility_index_zscore_63d
    ECONOMIC RATIONALE: Financial leverage relative to price stability.
    """
    base = (liabs/equity.replace(0, 1e-9)) / close.rolling(252).std().replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def dsen_204_structural_fragility_index_rank_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_204_structural_fragility_index_rank_63d
    ECONOMIC RATIONALE: Financial leverage relative to price stability.
    """
    base = (liabs/equity.replace(0, 1e-9)) / close.rolling(252).std().replace(0, 1e-9)
    return _rank_pct(base, 63)

def dsen_205_structural_fragility_index_lvl_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_205_structural_fragility_index_lvl_126d
    ECONOMIC RATIONALE: Financial leverage relative to price stability.
    """
    base = (liabs/equity.replace(0, 1e-9)) / close.rolling(252).std().replace(0, 1e-9)
    return _rolling_mean(base, 126)

def dsen_206_structural_fragility_index_zscore_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_206_structural_fragility_index_zscore_126d
    ECONOMIC RATIONALE: Financial leverage relative to price stability.
    """
    base = (liabs/equity.replace(0, 1e-9)) / close.rolling(252).std().replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def dsen_207_structural_fragility_index_rank_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_207_structural_fragility_index_rank_126d
    ECONOMIC RATIONALE: Financial leverage relative to price stability.
    """
    base = (liabs/equity.replace(0, 1e-9)) / close.rolling(252).std().replace(0, 1e-9)
    return _rank_pct(base, 126)

def dsen_208_structural_fragility_index_lvl_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_208_structural_fragility_index_lvl_252d
    ECONOMIC RATIONALE: Financial leverage relative to price stability.
    """
    base = (liabs/equity.replace(0, 1e-9)) / close.rolling(252).std().replace(0, 1e-9)
    return _rolling_mean(base, 252)

def dsen_209_structural_fragility_index_zscore_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_209_structural_fragility_index_zscore_252d
    ECONOMIC RATIONALE: Financial leverage relative to price stability.
    """
    base = (liabs/equity.replace(0, 1e-9)) / close.rolling(252).std().replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def dsen_210_structural_fragility_index_rank_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_210_structural_fragility_index_rank_252d
    ECONOMIC RATIONALE: Financial leverage relative to price stability.
    """
    base = (liabs/equity.replace(0, 1e-9)) / close.rolling(252).std().replace(0, 1e-9)
    return _rank_pct(base, 252)

def dsen_211_ensemble_tail_risk_lvl_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_211_ensemble_tail_risk_lvl_5d
    ECONOMIC RATIONALE: Co-occurrence of price tail events and insolvency.
    """
    base = ((close.pct_change(1) < -0.05) & (liabs > equity)).astype(float)
    return _rolling_mean(base, 5)

def dsen_212_ensemble_tail_risk_zscore_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_212_ensemble_tail_risk_zscore_5d
    ECONOMIC RATIONALE: Co-occurrence of price tail events and insolvency.
    """
    base = ((close.pct_change(1) < -0.05) & (liabs > equity)).astype(float)
    return _zscore_rolling(base, 5)

def dsen_213_ensemble_tail_risk_rank_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_213_ensemble_tail_risk_rank_5d
    ECONOMIC RATIONALE: Co-occurrence of price tail events and insolvency.
    """
    base = ((close.pct_change(1) < -0.05) & (liabs > equity)).astype(float)
    return _rank_pct(base, 5)

def dsen_214_ensemble_tail_risk_lvl_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_214_ensemble_tail_risk_lvl_21d
    ECONOMIC RATIONALE: Co-occurrence of price tail events and insolvency.
    """
    base = ((close.pct_change(1) < -0.05) & (liabs > equity)).astype(float)
    return _rolling_mean(base, 21)

def dsen_215_ensemble_tail_risk_zscore_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_215_ensemble_tail_risk_zscore_21d
    ECONOMIC RATIONALE: Co-occurrence of price tail events and insolvency.
    """
    base = ((close.pct_change(1) < -0.05) & (liabs > equity)).astype(float)
    return _zscore_rolling(base, 21)

def dsen_216_ensemble_tail_risk_rank_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_216_ensemble_tail_risk_rank_21d
    ECONOMIC RATIONALE: Co-occurrence of price tail events and insolvency.
    """
    base = ((close.pct_change(1) < -0.05) & (liabs > equity)).astype(float)
    return _rank_pct(base, 21)

def dsen_217_ensemble_tail_risk_lvl_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_217_ensemble_tail_risk_lvl_63d
    ECONOMIC RATIONALE: Co-occurrence of price tail events and insolvency.
    """
    base = ((close.pct_change(1) < -0.05) & (liabs > equity)).astype(float)
    return _rolling_mean(base, 63)

def dsen_218_ensemble_tail_risk_zscore_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_218_ensemble_tail_risk_zscore_63d
    ECONOMIC RATIONALE: Co-occurrence of price tail events and insolvency.
    """
    base = ((close.pct_change(1) < -0.05) & (liabs > equity)).astype(float)
    return _zscore_rolling(base, 63)

def dsen_219_ensemble_tail_risk_rank_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_219_ensemble_tail_risk_rank_63d
    ECONOMIC RATIONALE: Co-occurrence of price tail events and insolvency.
    """
    base = ((close.pct_change(1) < -0.05) & (liabs > equity)).astype(float)
    return _rank_pct(base, 63)

def dsen_220_ensemble_tail_risk_lvl_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_220_ensemble_tail_risk_lvl_126d
    ECONOMIC RATIONALE: Co-occurrence of price tail events and insolvency.
    """
    base = ((close.pct_change(1) < -0.05) & (liabs > equity)).astype(float)
    return _rolling_mean(base, 126)

def dsen_221_ensemble_tail_risk_zscore_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_221_ensemble_tail_risk_zscore_126d
    ECONOMIC RATIONALE: Co-occurrence of price tail events and insolvency.
    """
    base = ((close.pct_change(1) < -0.05) & (liabs > equity)).astype(float)
    return _zscore_rolling(base, 126)

def dsen_222_ensemble_tail_risk_rank_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_222_ensemble_tail_risk_rank_126d
    ECONOMIC RATIONALE: Co-occurrence of price tail events and insolvency.
    """
    base = ((close.pct_change(1) < -0.05) & (liabs > equity)).astype(float)
    return _rank_pct(base, 126)

def dsen_223_ensemble_tail_risk_lvl_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_223_ensemble_tail_risk_lvl_252d
    ECONOMIC RATIONALE: Co-occurrence of price tail events and insolvency.
    """
    base = ((close.pct_change(1) < -0.05) & (liabs > equity)).astype(float)
    return _rolling_mean(base, 252)

def dsen_224_ensemble_tail_risk_zscore_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_224_ensemble_tail_risk_zscore_252d
    ECONOMIC RATIONALE: Co-occurrence of price tail events and insolvency.
    """
    base = ((close.pct_change(1) < -0.05) & (liabs > equity)).astype(float)
    return _zscore_rolling(base, 252)

def dsen_225_ensemble_tail_risk_rank_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_225_ensemble_tail_risk_rank_252d
    ECONOMIC RATIONALE: Co-occurrence of price tail events and insolvency.
    """
    base = ((close.pct_change(1) < -0.05) & (liabs > equity)).astype(float)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V121_REGISTRY_2 = {
    "dsen_121_ensemble_zscore_lvl_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_121_ensemble_zscore_lvl_5d},
    "dsen_122_ensemble_zscore_zscore_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_122_ensemble_zscore_zscore_5d},
    "dsen_123_ensemble_zscore_rank_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_123_ensemble_zscore_rank_5d},
    "dsen_124_ensemble_zscore_lvl_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_124_ensemble_zscore_lvl_21d},
    "dsen_125_ensemble_zscore_zscore_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_125_ensemble_zscore_zscore_21d},
    "dsen_126_ensemble_zscore_rank_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_126_ensemble_zscore_rank_21d},
    "dsen_127_ensemble_zscore_lvl_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_127_ensemble_zscore_lvl_63d},
    "dsen_128_ensemble_zscore_zscore_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_128_ensemble_zscore_zscore_63d},
    "dsen_129_ensemble_zscore_rank_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_129_ensemble_zscore_rank_63d},
    "dsen_130_ensemble_zscore_lvl_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_130_ensemble_zscore_lvl_126d},
    "dsen_131_ensemble_zscore_zscore_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_131_ensemble_zscore_zscore_126d},
    "dsen_132_ensemble_zscore_rank_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_132_ensemble_zscore_rank_126d},
    "dsen_133_ensemble_zscore_lvl_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_133_ensemble_zscore_lvl_252d},
    "dsen_134_ensemble_zscore_zscore_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_134_ensemble_zscore_zscore_252d},
    "dsen_135_ensemble_zscore_rank_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_135_ensemble_zscore_rank_252d},
    "dsen_136_market_distress_beta_lvl_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_136_market_distress_beta_lvl_5d},
    "dsen_137_market_distress_beta_zscore_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_137_market_distress_beta_zscore_5d},
    "dsen_138_market_distress_beta_rank_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_138_market_distress_beta_rank_5d},
    "dsen_139_market_distress_beta_lvl_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_139_market_distress_beta_lvl_21d},
    "dsen_140_market_distress_beta_zscore_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_140_market_distress_beta_zscore_21d},
    "dsen_141_market_distress_beta_rank_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_141_market_distress_beta_rank_21d},
    "dsen_142_market_distress_beta_lvl_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_142_market_distress_beta_lvl_63d},
    "dsen_143_market_distress_beta_zscore_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_143_market_distress_beta_zscore_63d},
    "dsen_144_market_distress_beta_rank_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_144_market_distress_beta_rank_63d},
    "dsen_145_market_distress_beta_lvl_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_145_market_distress_beta_lvl_126d},
    "dsen_146_market_distress_beta_zscore_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_146_market_distress_beta_zscore_126d},
    "dsen_147_market_distress_beta_rank_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_147_market_distress_beta_rank_126d},
    "dsen_148_market_distress_beta_lvl_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_148_market_distress_beta_lvl_252d},
    "dsen_149_market_distress_beta_zscore_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_149_market_distress_beta_zscore_252d},
    "dsen_150_market_distress_beta_rank_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_150_market_distress_beta_rank_252d},
    "dsen_151_ensemble_drawdown_rank_lvl_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_151_ensemble_drawdown_rank_lvl_5d},
    "dsen_152_ensemble_drawdown_rank_zscore_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_152_ensemble_drawdown_rank_zscore_5d},
    "dsen_153_ensemble_drawdown_rank_rank_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_153_ensemble_drawdown_rank_rank_5d},
    "dsen_154_ensemble_drawdown_rank_lvl_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_154_ensemble_drawdown_rank_lvl_21d},
    "dsen_155_ensemble_drawdown_rank_zscore_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_155_ensemble_drawdown_rank_zscore_21d},
    "dsen_156_ensemble_drawdown_rank_rank_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_156_ensemble_drawdown_rank_rank_21d},
    "dsen_157_ensemble_drawdown_rank_lvl_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_157_ensemble_drawdown_rank_lvl_63d},
    "dsen_158_ensemble_drawdown_rank_zscore_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_158_ensemble_drawdown_rank_zscore_63d},
    "dsen_159_ensemble_drawdown_rank_rank_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_159_ensemble_drawdown_rank_rank_63d},
    "dsen_160_ensemble_drawdown_rank_lvl_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_160_ensemble_drawdown_rank_lvl_126d},
    "dsen_161_ensemble_drawdown_rank_zscore_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_161_ensemble_drawdown_rank_zscore_126d},
    "dsen_162_ensemble_drawdown_rank_rank_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_162_ensemble_drawdown_rank_rank_126d},
    "dsen_163_ensemble_drawdown_rank_lvl_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_163_ensemble_drawdown_rank_lvl_252d},
    "dsen_164_ensemble_drawdown_rank_zscore_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_164_ensemble_drawdown_rank_zscore_252d},
    "dsen_165_ensemble_drawdown_rank_rank_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_165_ensemble_drawdown_rank_rank_252d},
    "dsen_166_distress_reversal_potential_lvl_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_166_distress_reversal_potential_lvl_5d},
    "dsen_167_distress_reversal_potential_zscore_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_167_distress_reversal_potential_zscore_5d},
    "dsen_168_distress_reversal_potential_rank_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_168_distress_reversal_potential_rank_5d},
    "dsen_169_distress_reversal_potential_lvl_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_169_distress_reversal_potential_lvl_21d},
    "dsen_170_distress_reversal_potential_zscore_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_170_distress_reversal_potential_zscore_21d},
    "dsen_171_distress_reversal_potential_rank_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_171_distress_reversal_potential_rank_21d},
    "dsen_172_distress_reversal_potential_lvl_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_172_distress_reversal_potential_lvl_63d},
    "dsen_173_distress_reversal_potential_zscore_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_173_distress_reversal_potential_zscore_63d},
    "dsen_174_distress_reversal_potential_rank_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_174_distress_reversal_potential_rank_63d},
    "dsen_175_distress_reversal_potential_lvl_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_175_distress_reversal_potential_lvl_126d},
    "dsen_176_distress_reversal_potential_zscore_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_176_distress_reversal_potential_zscore_126d},
    "dsen_177_distress_reversal_potential_rank_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_177_distress_reversal_potential_rank_126d},
    "dsen_178_distress_reversal_potential_lvl_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_178_distress_reversal_potential_lvl_252d},
    "dsen_179_distress_reversal_potential_zscore_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_179_distress_reversal_potential_zscore_252d},
    "dsen_180_distress_reversal_potential_rank_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_180_distress_reversal_potential_rank_252d},
    "dsen_181_ensemble_liquidity_gap_lvl_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_181_ensemble_liquidity_gap_lvl_5d},
    "dsen_182_ensemble_liquidity_gap_zscore_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_182_ensemble_liquidity_gap_zscore_5d},
    "dsen_183_ensemble_liquidity_gap_rank_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_183_ensemble_liquidity_gap_rank_5d},
    "dsen_184_ensemble_liquidity_gap_lvl_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_184_ensemble_liquidity_gap_lvl_21d},
    "dsen_185_ensemble_liquidity_gap_zscore_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_185_ensemble_liquidity_gap_zscore_21d},
    "dsen_186_ensemble_liquidity_gap_rank_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_186_ensemble_liquidity_gap_rank_21d},
    "dsen_187_ensemble_liquidity_gap_lvl_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_187_ensemble_liquidity_gap_lvl_63d},
    "dsen_188_ensemble_liquidity_gap_zscore_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_188_ensemble_liquidity_gap_zscore_63d},
    "dsen_189_ensemble_liquidity_gap_rank_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_189_ensemble_liquidity_gap_rank_63d},
    "dsen_190_ensemble_liquidity_gap_lvl_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_190_ensemble_liquidity_gap_lvl_126d},
    "dsen_191_ensemble_liquidity_gap_zscore_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_191_ensemble_liquidity_gap_zscore_126d},
    "dsen_192_ensemble_liquidity_gap_rank_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_192_ensemble_liquidity_gap_rank_126d},
    "dsen_193_ensemble_liquidity_gap_lvl_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_193_ensemble_liquidity_gap_lvl_252d},
    "dsen_194_ensemble_liquidity_gap_zscore_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_194_ensemble_liquidity_gap_zscore_252d},
    "dsen_195_ensemble_liquidity_gap_rank_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_195_ensemble_liquidity_gap_rank_252d},
    "dsen_196_structural_fragility_index_lvl_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_196_structural_fragility_index_lvl_5d},
    "dsen_197_structural_fragility_index_zscore_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_197_structural_fragility_index_zscore_5d},
    "dsen_198_structural_fragility_index_rank_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_198_structural_fragility_index_rank_5d},
    "dsen_199_structural_fragility_index_lvl_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_199_structural_fragility_index_lvl_21d},
    "dsen_200_structural_fragility_index_zscore_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_200_structural_fragility_index_zscore_21d},
    "dsen_201_structural_fragility_index_rank_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_201_structural_fragility_index_rank_21d},
    "dsen_202_structural_fragility_index_lvl_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_202_structural_fragility_index_lvl_63d},
    "dsen_203_structural_fragility_index_zscore_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_203_structural_fragility_index_zscore_63d},
    "dsen_204_structural_fragility_index_rank_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_204_structural_fragility_index_rank_63d},
    "dsen_205_structural_fragility_index_lvl_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_205_structural_fragility_index_lvl_126d},
    "dsen_206_structural_fragility_index_zscore_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_206_structural_fragility_index_zscore_126d},
    "dsen_207_structural_fragility_index_rank_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_207_structural_fragility_index_rank_126d},
    "dsen_208_structural_fragility_index_lvl_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_208_structural_fragility_index_lvl_252d},
    "dsen_209_structural_fragility_index_zscore_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_209_structural_fragility_index_zscore_252d},
    "dsen_210_structural_fragility_index_rank_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_210_structural_fragility_index_rank_252d},
    "dsen_211_ensemble_tail_risk_lvl_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_211_ensemble_tail_risk_lvl_5d},
    "dsen_212_ensemble_tail_risk_zscore_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_212_ensemble_tail_risk_zscore_5d},
    "dsen_213_ensemble_tail_risk_rank_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_213_ensemble_tail_risk_rank_5d},
    "dsen_214_ensemble_tail_risk_lvl_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_214_ensemble_tail_risk_lvl_21d},
    "dsen_215_ensemble_tail_risk_zscore_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_215_ensemble_tail_risk_zscore_21d},
    "dsen_216_ensemble_tail_risk_rank_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_216_ensemble_tail_risk_rank_21d},
    "dsen_217_ensemble_tail_risk_lvl_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_217_ensemble_tail_risk_lvl_63d},
    "dsen_218_ensemble_tail_risk_zscore_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_218_ensemble_tail_risk_zscore_63d},
    "dsen_219_ensemble_tail_risk_rank_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_219_ensemble_tail_risk_rank_63d},
    "dsen_220_ensemble_tail_risk_lvl_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_220_ensemble_tail_risk_lvl_126d},
    "dsen_221_ensemble_tail_risk_zscore_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_221_ensemble_tail_risk_zscore_126d},
    "dsen_222_ensemble_tail_risk_rank_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_222_ensemble_tail_risk_rank_126d},
    "dsen_223_ensemble_tail_risk_lvl_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_223_ensemble_tail_risk_lvl_252d},
    "dsen_224_ensemble_tail_risk_zscore_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_224_ensemble_tail_risk_zscore_252d},
    "dsen_225_ensemble_tail_risk_rank_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_225_ensemble_tail_risk_rank_252d},
}
