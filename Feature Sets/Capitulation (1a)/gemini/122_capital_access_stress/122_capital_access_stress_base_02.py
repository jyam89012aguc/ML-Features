"""
122_capital_access_stress — Base Features Part 2
Domain: capital_access_stress
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

def cast_121_debt_to_assets_momentum_lvl_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_121_debt_to_assets_momentum_lvl_5d
    ECONOMIC RATIONALE: Trend in the proportion of assets funded by debt.
    """
    base = (debt/assets).diff(63)
    return _rolling_mean(base, 5)

def cast_122_debt_to_assets_momentum_zscore_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_122_debt_to_assets_momentum_zscore_5d
    ECONOMIC RATIONALE: Trend in the proportion of assets funded by debt.
    """
    base = (debt/assets).diff(63)
    return _zscore_rolling(base, 5)

def cast_123_debt_to_assets_momentum_rank_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_123_debt_to_assets_momentum_rank_5d
    ECONOMIC RATIONALE: Trend in the proportion of assets funded by debt.
    """
    base = (debt/assets).diff(63)
    return _rank_pct(base, 5)

def cast_124_debt_to_assets_momentum_lvl_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_124_debt_to_assets_momentum_lvl_21d
    ECONOMIC RATIONALE: Trend in the proportion of assets funded by debt.
    """
    base = (debt/assets).diff(63)
    return _rolling_mean(base, 21)

def cast_125_debt_to_assets_momentum_zscore_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_125_debt_to_assets_momentum_zscore_21d
    ECONOMIC RATIONALE: Trend in the proportion of assets funded by debt.
    """
    base = (debt/assets).diff(63)
    return _zscore_rolling(base, 21)

def cast_126_debt_to_assets_momentum_rank_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_126_debt_to_assets_momentum_rank_21d
    ECONOMIC RATIONALE: Trend in the proportion of assets funded by debt.
    """
    base = (debt/assets).diff(63)
    return _rank_pct(base, 21)

def cast_127_debt_to_assets_momentum_lvl_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_127_debt_to_assets_momentum_lvl_63d
    ECONOMIC RATIONALE: Trend in the proportion of assets funded by debt.
    """
    base = (debt/assets).diff(63)
    return _rolling_mean(base, 63)

def cast_128_debt_to_assets_momentum_zscore_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_128_debt_to_assets_momentum_zscore_63d
    ECONOMIC RATIONALE: Trend in the proportion of assets funded by debt.
    """
    base = (debt/assets).diff(63)
    return _zscore_rolling(base, 63)

def cast_129_debt_to_assets_momentum_rank_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_129_debt_to_assets_momentum_rank_63d
    ECONOMIC RATIONALE: Trend in the proportion of assets funded by debt.
    """
    base = (debt/assets).diff(63)
    return _rank_pct(base, 63)

def cast_130_debt_to_assets_momentum_lvl_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_130_debt_to_assets_momentum_lvl_126d
    ECONOMIC RATIONALE: Trend in the proportion of assets funded by debt.
    """
    base = (debt/assets).diff(63)
    return _rolling_mean(base, 126)

def cast_131_debt_to_assets_momentum_zscore_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_131_debt_to_assets_momentum_zscore_126d
    ECONOMIC RATIONALE: Trend in the proportion of assets funded by debt.
    """
    base = (debt/assets).diff(63)
    return _zscore_rolling(base, 126)

def cast_132_debt_to_assets_momentum_rank_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_132_debt_to_assets_momentum_rank_126d
    ECONOMIC RATIONALE: Trend in the proportion of assets funded by debt.
    """
    base = (debt/assets).diff(63)
    return _rank_pct(base, 126)

def cast_133_debt_to_assets_momentum_lvl_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_133_debt_to_assets_momentum_lvl_252d
    ECONOMIC RATIONALE: Trend in the proportion of assets funded by debt.
    """
    base = (debt/assets).diff(63)
    return _rolling_mean(base, 252)

def cast_134_debt_to_assets_momentum_zscore_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_134_debt_to_assets_momentum_zscore_252d
    ECONOMIC RATIONALE: Trend in the proportion of assets funded by debt.
    """
    base = (debt/assets).diff(63)
    return _zscore_rolling(base, 252)

def cast_135_debt_to_assets_momentum_rank_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_135_debt_to_assets_momentum_rank_252d
    ECONOMIC RATIONALE: Trend in the proportion of assets funded by debt.
    """
    base = (debt/assets).diff(63)
    return _rank_pct(base, 252)

def cast_136_fcf_yield_vs_debt_lvl_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_136_fcf_yield_vs_debt_lvl_5d
    ECONOMIC RATIONALE: Cash flow yield net of debt-to-cap ratio.
    """
    base = (fcf/marketcap) - (debt/marketcap)
    return _rolling_mean(base, 5)

def cast_137_fcf_yield_vs_debt_zscore_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_137_fcf_yield_vs_debt_zscore_5d
    ECONOMIC RATIONALE: Cash flow yield net of debt-to-cap ratio.
    """
    base = (fcf/marketcap) - (debt/marketcap)
    return _zscore_rolling(base, 5)

def cast_138_fcf_yield_vs_debt_rank_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_138_fcf_yield_vs_debt_rank_5d
    ECONOMIC RATIONALE: Cash flow yield net of debt-to-cap ratio.
    """
    base = (fcf/marketcap) - (debt/marketcap)
    return _rank_pct(base, 5)

def cast_139_fcf_yield_vs_debt_lvl_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_139_fcf_yield_vs_debt_lvl_21d
    ECONOMIC RATIONALE: Cash flow yield net of debt-to-cap ratio.
    """
    base = (fcf/marketcap) - (debt/marketcap)
    return _rolling_mean(base, 21)

def cast_140_fcf_yield_vs_debt_zscore_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_140_fcf_yield_vs_debt_zscore_21d
    ECONOMIC RATIONALE: Cash flow yield net of debt-to-cap ratio.
    """
    base = (fcf/marketcap) - (debt/marketcap)
    return _zscore_rolling(base, 21)

def cast_141_fcf_yield_vs_debt_rank_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_141_fcf_yield_vs_debt_rank_21d
    ECONOMIC RATIONALE: Cash flow yield net of debt-to-cap ratio.
    """
    base = (fcf/marketcap) - (debt/marketcap)
    return _rank_pct(base, 21)

def cast_142_fcf_yield_vs_debt_lvl_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_142_fcf_yield_vs_debt_lvl_63d
    ECONOMIC RATIONALE: Cash flow yield net of debt-to-cap ratio.
    """
    base = (fcf/marketcap) - (debt/marketcap)
    return _rolling_mean(base, 63)

def cast_143_fcf_yield_vs_debt_zscore_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_143_fcf_yield_vs_debt_zscore_63d
    ECONOMIC RATIONALE: Cash flow yield net of debt-to-cap ratio.
    """
    base = (fcf/marketcap) - (debt/marketcap)
    return _zscore_rolling(base, 63)

def cast_144_fcf_yield_vs_debt_rank_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_144_fcf_yield_vs_debt_rank_63d
    ECONOMIC RATIONALE: Cash flow yield net of debt-to-cap ratio.
    """
    base = (fcf/marketcap) - (debt/marketcap)
    return _rank_pct(base, 63)

def cast_145_fcf_yield_vs_debt_lvl_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_145_fcf_yield_vs_debt_lvl_126d
    ECONOMIC RATIONALE: Cash flow yield net of debt-to-cap ratio.
    """
    base = (fcf/marketcap) - (debt/marketcap)
    return _rolling_mean(base, 126)

def cast_146_fcf_yield_vs_debt_zscore_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_146_fcf_yield_vs_debt_zscore_126d
    ECONOMIC RATIONALE: Cash flow yield net of debt-to-cap ratio.
    """
    base = (fcf/marketcap) - (debt/marketcap)
    return _zscore_rolling(base, 126)

def cast_147_fcf_yield_vs_debt_rank_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_147_fcf_yield_vs_debt_rank_126d
    ECONOMIC RATIONALE: Cash flow yield net of debt-to-cap ratio.
    """
    base = (fcf/marketcap) - (debt/marketcap)
    return _rank_pct(base, 126)

def cast_148_fcf_yield_vs_debt_lvl_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_148_fcf_yield_vs_debt_lvl_252d
    ECONOMIC RATIONALE: Cash flow yield net of debt-to-cap ratio.
    """
    base = (fcf/marketcap) - (debt/marketcap)
    return _rolling_mean(base, 252)

def cast_149_fcf_yield_vs_debt_zscore_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_149_fcf_yield_vs_debt_zscore_252d
    ECONOMIC RATIONALE: Cash flow yield net of debt-to-cap ratio.
    """
    base = (fcf/marketcap) - (debt/marketcap)
    return _zscore_rolling(base, 252)

def cast_150_fcf_yield_vs_debt_rank_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_150_fcf_yield_vs_debt_rank_252d
    ECONOMIC RATIONALE: Cash flow yield net of debt-to-cap ratio.
    """
    base = (fcf/marketcap) - (debt/marketcap)
    return _rank_pct(base, 252)

def cast_151_capital_structure_z_lvl_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_151_capital_structure_z_lvl_5d
    ECONOMIC RATIONALE: Z-score of debt within the capital structure.
    """
    base = _zscore_rolling(debt/(debt+equity).replace(0, 1e-9), 252)
    return _rolling_mean(base, 5)

def cast_152_capital_structure_z_zscore_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_152_capital_structure_z_zscore_5d
    ECONOMIC RATIONALE: Z-score of debt within the capital structure.
    """
    base = _zscore_rolling(debt/(debt+equity).replace(0, 1e-9), 252)
    return _zscore_rolling(base, 5)

def cast_153_capital_structure_z_rank_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_153_capital_structure_z_rank_5d
    ECONOMIC RATIONALE: Z-score of debt within the capital structure.
    """
    base = _zscore_rolling(debt/(debt+equity).replace(0, 1e-9), 252)
    return _rank_pct(base, 5)

def cast_154_capital_structure_z_lvl_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_154_capital_structure_z_lvl_21d
    ECONOMIC RATIONALE: Z-score of debt within the capital structure.
    """
    base = _zscore_rolling(debt/(debt+equity).replace(0, 1e-9), 252)
    return _rolling_mean(base, 21)

def cast_155_capital_structure_z_zscore_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_155_capital_structure_z_zscore_21d
    ECONOMIC RATIONALE: Z-score of debt within the capital structure.
    """
    base = _zscore_rolling(debt/(debt+equity).replace(0, 1e-9), 252)
    return _zscore_rolling(base, 21)

def cast_156_capital_structure_z_rank_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_156_capital_structure_z_rank_21d
    ECONOMIC RATIONALE: Z-score of debt within the capital structure.
    """
    base = _zscore_rolling(debt/(debt+equity).replace(0, 1e-9), 252)
    return _rank_pct(base, 21)

def cast_157_capital_structure_z_lvl_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_157_capital_structure_z_lvl_63d
    ECONOMIC RATIONALE: Z-score of debt within the capital structure.
    """
    base = _zscore_rolling(debt/(debt+equity).replace(0, 1e-9), 252)
    return _rolling_mean(base, 63)

def cast_158_capital_structure_z_zscore_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_158_capital_structure_z_zscore_63d
    ECONOMIC RATIONALE: Z-score of debt within the capital structure.
    """
    base = _zscore_rolling(debt/(debt+equity).replace(0, 1e-9), 252)
    return _zscore_rolling(base, 63)

def cast_159_capital_structure_z_rank_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_159_capital_structure_z_rank_63d
    ECONOMIC RATIONALE: Z-score of debt within the capital structure.
    """
    base = _zscore_rolling(debt/(debt+equity).replace(0, 1e-9), 252)
    return _rank_pct(base, 63)

def cast_160_capital_structure_z_lvl_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_160_capital_structure_z_lvl_126d
    ECONOMIC RATIONALE: Z-score of debt within the capital structure.
    """
    base = _zscore_rolling(debt/(debt+equity).replace(0, 1e-9), 252)
    return _rolling_mean(base, 126)

def cast_161_capital_structure_z_zscore_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_161_capital_structure_z_zscore_126d
    ECONOMIC RATIONALE: Z-score of debt within the capital structure.
    """
    base = _zscore_rolling(debt/(debt+equity).replace(0, 1e-9), 252)
    return _zscore_rolling(base, 126)

def cast_162_capital_structure_z_rank_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_162_capital_structure_z_rank_126d
    ECONOMIC RATIONALE: Z-score of debt within the capital structure.
    """
    base = _zscore_rolling(debt/(debt+equity).replace(0, 1e-9), 252)
    return _rank_pct(base, 126)

def cast_163_capital_structure_z_lvl_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_163_capital_structure_z_lvl_252d
    ECONOMIC RATIONALE: Z-score of debt within the capital structure.
    """
    base = _zscore_rolling(debt/(debt+equity).replace(0, 1e-9), 252)
    return _rolling_mean(base, 252)

def cast_164_capital_structure_z_zscore_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_164_capital_structure_z_zscore_252d
    ECONOMIC RATIONALE: Z-score of debt within the capital structure.
    """
    base = _zscore_rolling(debt/(debt+equity).replace(0, 1e-9), 252)
    return _zscore_rolling(base, 252)

def cast_165_capital_structure_z_rank_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_165_capital_structure_z_rank_252d
    ECONOMIC RATIONALE: Z-score of debt within the capital structure.
    """
    base = _zscore_rolling(debt/(debt+equity).replace(0, 1e-9), 252)
    return _rank_pct(base, 252)

def cast_166_equity_value_erosion_lvl_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_166_equity_value_erosion_lvl_5d
    ECONOMIC RATIONALE: Destruction of book value relative to market price.
    """
    base = equity.diff(252) / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 5)

def cast_167_equity_value_erosion_zscore_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_167_equity_value_erosion_zscore_5d
    ECONOMIC RATIONALE: Destruction of book value relative to market price.
    """
    base = equity.diff(252) / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def cast_168_equity_value_erosion_rank_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_168_equity_value_erosion_rank_5d
    ECONOMIC RATIONALE: Destruction of book value relative to market price.
    """
    base = equity.diff(252) / marketcap.replace(0, 1e-9)
    return _rank_pct(base, 5)

def cast_169_equity_value_erosion_lvl_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_169_equity_value_erosion_lvl_21d
    ECONOMIC RATIONALE: Destruction of book value relative to market price.
    """
    base = equity.diff(252) / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 21)

def cast_170_equity_value_erosion_zscore_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_170_equity_value_erosion_zscore_21d
    ECONOMIC RATIONALE: Destruction of book value relative to market price.
    """
    base = equity.diff(252) / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def cast_171_equity_value_erosion_rank_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_171_equity_value_erosion_rank_21d
    ECONOMIC RATIONALE: Destruction of book value relative to market price.
    """
    base = equity.diff(252) / marketcap.replace(0, 1e-9)
    return _rank_pct(base, 21)

def cast_172_equity_value_erosion_lvl_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_172_equity_value_erosion_lvl_63d
    ECONOMIC RATIONALE: Destruction of book value relative to market price.
    """
    base = equity.diff(252) / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 63)

def cast_173_equity_value_erosion_zscore_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_173_equity_value_erosion_zscore_63d
    ECONOMIC RATIONALE: Destruction of book value relative to market price.
    """
    base = equity.diff(252) / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def cast_174_equity_value_erosion_rank_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_174_equity_value_erosion_rank_63d
    ECONOMIC RATIONALE: Destruction of book value relative to market price.
    """
    base = equity.diff(252) / marketcap.replace(0, 1e-9)
    return _rank_pct(base, 63)

def cast_175_equity_value_erosion_lvl_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_175_equity_value_erosion_lvl_126d
    ECONOMIC RATIONALE: Destruction of book value relative to market price.
    """
    base = equity.diff(252) / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 126)

def cast_176_equity_value_erosion_zscore_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_176_equity_value_erosion_zscore_126d
    ECONOMIC RATIONALE: Destruction of book value relative to market price.
    """
    base = equity.diff(252) / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def cast_177_equity_value_erosion_rank_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_177_equity_value_erosion_rank_126d
    ECONOMIC RATIONALE: Destruction of book value relative to market price.
    """
    base = equity.diff(252) / marketcap.replace(0, 1e-9)
    return _rank_pct(base, 126)

def cast_178_equity_value_erosion_lvl_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_178_equity_value_erosion_lvl_252d
    ECONOMIC RATIONALE: Destruction of book value relative to market price.
    """
    base = equity.diff(252) / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 252)

def cast_179_equity_value_erosion_zscore_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_179_equity_value_erosion_zscore_252d
    ECONOMIC RATIONALE: Destruction of book value relative to market price.
    """
    base = equity.diff(252) / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def cast_180_equity_value_erosion_rank_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_180_equity_value_erosion_rank_252d
    ECONOMIC RATIONALE: Destruction of book value relative to market price.
    """
    base = equity.diff(252) / marketcap.replace(0, 1e-9)
    return _rank_pct(base, 252)

def cast_181_debt_burden_vol_lvl_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_181_debt_burden_vol_lvl_5d
    ECONOMIC RATIONALE: Price volatility amplified by debt-to-market-cap ratio.
    """
    base = close.rolling(21).std() * (debt/marketcap.replace(0, 1e-9))
    return _rolling_mean(base, 5)

def cast_182_debt_burden_vol_zscore_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_182_debt_burden_vol_zscore_5d
    ECONOMIC RATIONALE: Price volatility amplified by debt-to-market-cap ratio.
    """
    base = close.rolling(21).std() * (debt/marketcap.replace(0, 1e-9))
    return _zscore_rolling(base, 5)

def cast_183_debt_burden_vol_rank_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_183_debt_burden_vol_rank_5d
    ECONOMIC RATIONALE: Price volatility amplified by debt-to-market-cap ratio.
    """
    base = close.rolling(21).std() * (debt/marketcap.replace(0, 1e-9))
    return _rank_pct(base, 5)

def cast_184_debt_burden_vol_lvl_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_184_debt_burden_vol_lvl_21d
    ECONOMIC RATIONALE: Price volatility amplified by debt-to-market-cap ratio.
    """
    base = close.rolling(21).std() * (debt/marketcap.replace(0, 1e-9))
    return _rolling_mean(base, 21)

def cast_185_debt_burden_vol_zscore_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_185_debt_burden_vol_zscore_21d
    ECONOMIC RATIONALE: Price volatility amplified by debt-to-market-cap ratio.
    """
    base = close.rolling(21).std() * (debt/marketcap.replace(0, 1e-9))
    return _zscore_rolling(base, 21)

def cast_186_debt_burden_vol_rank_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_186_debt_burden_vol_rank_21d
    ECONOMIC RATIONALE: Price volatility amplified by debt-to-market-cap ratio.
    """
    base = close.rolling(21).std() * (debt/marketcap.replace(0, 1e-9))
    return _rank_pct(base, 21)

def cast_187_debt_burden_vol_lvl_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_187_debt_burden_vol_lvl_63d
    ECONOMIC RATIONALE: Price volatility amplified by debt-to-market-cap ratio.
    """
    base = close.rolling(21).std() * (debt/marketcap.replace(0, 1e-9))
    return _rolling_mean(base, 63)

def cast_188_debt_burden_vol_zscore_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_188_debt_burden_vol_zscore_63d
    ECONOMIC RATIONALE: Price volatility amplified by debt-to-market-cap ratio.
    """
    base = close.rolling(21).std() * (debt/marketcap.replace(0, 1e-9))
    return _zscore_rolling(base, 63)

def cast_189_debt_burden_vol_rank_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_189_debt_burden_vol_rank_63d
    ECONOMIC RATIONALE: Price volatility amplified by debt-to-market-cap ratio.
    """
    base = close.rolling(21).std() * (debt/marketcap.replace(0, 1e-9))
    return _rank_pct(base, 63)

def cast_190_debt_burden_vol_lvl_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_190_debt_burden_vol_lvl_126d
    ECONOMIC RATIONALE: Price volatility amplified by debt-to-market-cap ratio.
    """
    base = close.rolling(21).std() * (debt/marketcap.replace(0, 1e-9))
    return _rolling_mean(base, 126)

def cast_191_debt_burden_vol_zscore_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_191_debt_burden_vol_zscore_126d
    ECONOMIC RATIONALE: Price volatility amplified by debt-to-market-cap ratio.
    """
    base = close.rolling(21).std() * (debt/marketcap.replace(0, 1e-9))
    return _zscore_rolling(base, 126)

def cast_192_debt_burden_vol_rank_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_192_debt_burden_vol_rank_126d
    ECONOMIC RATIONALE: Price volatility amplified by debt-to-market-cap ratio.
    """
    base = close.rolling(21).std() * (debt/marketcap.replace(0, 1e-9))
    return _rank_pct(base, 126)

def cast_193_debt_burden_vol_lvl_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_193_debt_burden_vol_lvl_252d
    ECONOMIC RATIONALE: Price volatility amplified by debt-to-market-cap ratio.
    """
    base = close.rolling(21).std() * (debt/marketcap.replace(0, 1e-9))
    return _rolling_mean(base, 252)

def cast_194_debt_burden_vol_zscore_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_194_debt_burden_vol_zscore_252d
    ECONOMIC RATIONALE: Price volatility amplified by debt-to-market-cap ratio.
    """
    base = close.rolling(21).std() * (debt/marketcap.replace(0, 1e-9))
    return _zscore_rolling(base, 252)

def cast_195_debt_burden_vol_rank_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_195_debt_burden_vol_rank_252d
    ECONOMIC RATIONALE: Price volatility amplified by debt-to-market-cap ratio.
    """
    base = close.rolling(21).std() * (debt/marketcap.replace(0, 1e-9))
    return _rank_pct(base, 252)

def cast_196_capital_stress_index_lvl_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_196_capital_stress_index_lvl_5d
    ECONOMIC RATIONALE: Debt growth relative to cash flow capacity.
    """
    base = debt.pct_change(21) / fcf.rolling(63).mean().abs().replace(0, 1e-9)
    return _rolling_mean(base, 5)

def cast_197_capital_stress_index_zscore_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_197_capital_stress_index_zscore_5d
    ECONOMIC RATIONALE: Debt growth relative to cash flow capacity.
    """
    base = debt.pct_change(21) / fcf.rolling(63).mean().abs().replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def cast_198_capital_stress_index_rank_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_198_capital_stress_index_rank_5d
    ECONOMIC RATIONALE: Debt growth relative to cash flow capacity.
    """
    base = debt.pct_change(21) / fcf.rolling(63).mean().abs().replace(0, 1e-9)
    return _rank_pct(base, 5)

def cast_199_capital_stress_index_lvl_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_199_capital_stress_index_lvl_21d
    ECONOMIC RATIONALE: Debt growth relative to cash flow capacity.
    """
    base = debt.pct_change(21) / fcf.rolling(63).mean().abs().replace(0, 1e-9)
    return _rolling_mean(base, 21)

def cast_200_capital_stress_index_zscore_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_200_capital_stress_index_zscore_21d
    ECONOMIC RATIONALE: Debt growth relative to cash flow capacity.
    """
    base = debt.pct_change(21) / fcf.rolling(63).mean().abs().replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def cast_201_capital_stress_index_rank_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_201_capital_stress_index_rank_21d
    ECONOMIC RATIONALE: Debt growth relative to cash flow capacity.
    """
    base = debt.pct_change(21) / fcf.rolling(63).mean().abs().replace(0, 1e-9)
    return _rank_pct(base, 21)

def cast_202_capital_stress_index_lvl_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_202_capital_stress_index_lvl_63d
    ECONOMIC RATIONALE: Debt growth relative to cash flow capacity.
    """
    base = debt.pct_change(21) / fcf.rolling(63).mean().abs().replace(0, 1e-9)
    return _rolling_mean(base, 63)

def cast_203_capital_stress_index_zscore_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_203_capital_stress_index_zscore_63d
    ECONOMIC RATIONALE: Debt growth relative to cash flow capacity.
    """
    base = debt.pct_change(21) / fcf.rolling(63).mean().abs().replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def cast_204_capital_stress_index_rank_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_204_capital_stress_index_rank_63d
    ECONOMIC RATIONALE: Debt growth relative to cash flow capacity.
    """
    base = debt.pct_change(21) / fcf.rolling(63).mean().abs().replace(0, 1e-9)
    return _rank_pct(base, 63)

def cast_205_capital_stress_index_lvl_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_205_capital_stress_index_lvl_126d
    ECONOMIC RATIONALE: Debt growth relative to cash flow capacity.
    """
    base = debt.pct_change(21) / fcf.rolling(63).mean().abs().replace(0, 1e-9)
    return _rolling_mean(base, 126)

def cast_206_capital_stress_index_zscore_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_206_capital_stress_index_zscore_126d
    ECONOMIC RATIONALE: Debt growth relative to cash flow capacity.
    """
    base = debt.pct_change(21) / fcf.rolling(63).mean().abs().replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def cast_207_capital_stress_index_rank_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_207_capital_stress_index_rank_126d
    ECONOMIC RATIONALE: Debt growth relative to cash flow capacity.
    """
    base = debt.pct_change(21) / fcf.rolling(63).mean().abs().replace(0, 1e-9)
    return _rank_pct(base, 126)

def cast_208_capital_stress_index_lvl_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_208_capital_stress_index_lvl_252d
    ECONOMIC RATIONALE: Debt growth relative to cash flow capacity.
    """
    base = debt.pct_change(21) / fcf.rolling(63).mean().abs().replace(0, 1e-9)
    return _rolling_mean(base, 252)

def cast_209_capital_stress_index_zscore_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_209_capital_stress_index_zscore_252d
    ECONOMIC RATIONALE: Debt growth relative to cash flow capacity.
    """
    base = debt.pct_change(21) / fcf.rolling(63).mean().abs().replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def cast_210_capital_stress_index_rank_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_210_capital_stress_index_rank_252d
    ECONOMIC RATIONALE: Debt growth relative to cash flow capacity.
    """
    base = debt.pct_change(21) / fcf.rolling(63).mean().abs().replace(0, 1e-9)
    return _rank_pct(base, 252)

def cast_211_solvency_cushion_lvl_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_211_solvency_cushion_lvl_5d
    ECONOMIC RATIONALE: Proportion of assets funded by shareholders.
    """
    base = equity / assets.replace(0, 1e-9)
    return _rolling_mean(base, 5)

def cast_212_solvency_cushion_zscore_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_212_solvency_cushion_zscore_5d
    ECONOMIC RATIONALE: Proportion of assets funded by shareholders.
    """
    base = equity / assets.replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def cast_213_solvency_cushion_rank_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_213_solvency_cushion_rank_5d
    ECONOMIC RATIONALE: Proportion of assets funded by shareholders.
    """
    base = equity / assets.replace(0, 1e-9)
    return _rank_pct(base, 5)

def cast_214_solvency_cushion_lvl_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_214_solvency_cushion_lvl_21d
    ECONOMIC RATIONALE: Proportion of assets funded by shareholders.
    """
    base = equity / assets.replace(0, 1e-9)
    return _rolling_mean(base, 21)

def cast_215_solvency_cushion_zscore_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_215_solvency_cushion_zscore_21d
    ECONOMIC RATIONALE: Proportion of assets funded by shareholders.
    """
    base = equity / assets.replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def cast_216_solvency_cushion_rank_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_216_solvency_cushion_rank_21d
    ECONOMIC RATIONALE: Proportion of assets funded by shareholders.
    """
    base = equity / assets.replace(0, 1e-9)
    return _rank_pct(base, 21)

def cast_217_solvency_cushion_lvl_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_217_solvency_cushion_lvl_63d
    ECONOMIC RATIONALE: Proportion of assets funded by shareholders.
    """
    base = equity / assets.replace(0, 1e-9)
    return _rolling_mean(base, 63)

def cast_218_solvency_cushion_zscore_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_218_solvency_cushion_zscore_63d
    ECONOMIC RATIONALE: Proportion of assets funded by shareholders.
    """
    base = equity / assets.replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def cast_219_solvency_cushion_rank_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_219_solvency_cushion_rank_63d
    ECONOMIC RATIONALE: Proportion of assets funded by shareholders.
    """
    base = equity / assets.replace(0, 1e-9)
    return _rank_pct(base, 63)

def cast_220_solvency_cushion_lvl_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_220_solvency_cushion_lvl_126d
    ECONOMIC RATIONALE: Proportion of assets funded by shareholders.
    """
    base = equity / assets.replace(0, 1e-9)
    return _rolling_mean(base, 126)

def cast_221_solvency_cushion_zscore_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_221_solvency_cushion_zscore_126d
    ECONOMIC RATIONALE: Proportion of assets funded by shareholders.
    """
    base = equity / assets.replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def cast_222_solvency_cushion_rank_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_222_solvency_cushion_rank_126d
    ECONOMIC RATIONALE: Proportion of assets funded by shareholders.
    """
    base = equity / assets.replace(0, 1e-9)
    return _rank_pct(base, 126)

def cast_223_solvency_cushion_lvl_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_223_solvency_cushion_lvl_252d
    ECONOMIC RATIONALE: Proportion of assets funded by shareholders.
    """
    base = equity / assets.replace(0, 1e-9)
    return _rolling_mean(base, 252)

def cast_224_solvency_cushion_zscore_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_224_solvency_cushion_zscore_252d
    ECONOMIC RATIONALE: Proportion of assets funded by shareholders.
    """
    base = equity / assets.replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def cast_225_solvency_cushion_rank_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_225_solvency_cushion_rank_252d
    ECONOMIC RATIONALE: Proportion of assets funded by shareholders.
    """
    base = equity / assets.replace(0, 1e-9)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V122_REGISTRY_2 = {
    "cast_121_debt_to_assets_momentum_lvl_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_121_debt_to_assets_momentum_lvl_5d},
    "cast_122_debt_to_assets_momentum_zscore_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_122_debt_to_assets_momentum_zscore_5d},
    "cast_123_debt_to_assets_momentum_rank_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_123_debt_to_assets_momentum_rank_5d},
    "cast_124_debt_to_assets_momentum_lvl_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_124_debt_to_assets_momentum_lvl_21d},
    "cast_125_debt_to_assets_momentum_zscore_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_125_debt_to_assets_momentum_zscore_21d},
    "cast_126_debt_to_assets_momentum_rank_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_126_debt_to_assets_momentum_rank_21d},
    "cast_127_debt_to_assets_momentum_lvl_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_127_debt_to_assets_momentum_lvl_63d},
    "cast_128_debt_to_assets_momentum_zscore_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_128_debt_to_assets_momentum_zscore_63d},
    "cast_129_debt_to_assets_momentum_rank_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_129_debt_to_assets_momentum_rank_63d},
    "cast_130_debt_to_assets_momentum_lvl_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_130_debt_to_assets_momentum_lvl_126d},
    "cast_131_debt_to_assets_momentum_zscore_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_131_debt_to_assets_momentum_zscore_126d},
    "cast_132_debt_to_assets_momentum_rank_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_132_debt_to_assets_momentum_rank_126d},
    "cast_133_debt_to_assets_momentum_lvl_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_133_debt_to_assets_momentum_lvl_252d},
    "cast_134_debt_to_assets_momentum_zscore_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_134_debt_to_assets_momentum_zscore_252d},
    "cast_135_debt_to_assets_momentum_rank_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_135_debt_to_assets_momentum_rank_252d},
    "cast_136_fcf_yield_vs_debt_lvl_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_136_fcf_yield_vs_debt_lvl_5d},
    "cast_137_fcf_yield_vs_debt_zscore_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_137_fcf_yield_vs_debt_zscore_5d},
    "cast_138_fcf_yield_vs_debt_rank_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_138_fcf_yield_vs_debt_rank_5d},
    "cast_139_fcf_yield_vs_debt_lvl_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_139_fcf_yield_vs_debt_lvl_21d},
    "cast_140_fcf_yield_vs_debt_zscore_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_140_fcf_yield_vs_debt_zscore_21d},
    "cast_141_fcf_yield_vs_debt_rank_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_141_fcf_yield_vs_debt_rank_21d},
    "cast_142_fcf_yield_vs_debt_lvl_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_142_fcf_yield_vs_debt_lvl_63d},
    "cast_143_fcf_yield_vs_debt_zscore_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_143_fcf_yield_vs_debt_zscore_63d},
    "cast_144_fcf_yield_vs_debt_rank_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_144_fcf_yield_vs_debt_rank_63d},
    "cast_145_fcf_yield_vs_debt_lvl_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_145_fcf_yield_vs_debt_lvl_126d},
    "cast_146_fcf_yield_vs_debt_zscore_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_146_fcf_yield_vs_debt_zscore_126d},
    "cast_147_fcf_yield_vs_debt_rank_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_147_fcf_yield_vs_debt_rank_126d},
    "cast_148_fcf_yield_vs_debt_lvl_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_148_fcf_yield_vs_debt_lvl_252d},
    "cast_149_fcf_yield_vs_debt_zscore_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_149_fcf_yield_vs_debt_zscore_252d},
    "cast_150_fcf_yield_vs_debt_rank_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_150_fcf_yield_vs_debt_rank_252d},
    "cast_151_capital_structure_z_lvl_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_151_capital_structure_z_lvl_5d},
    "cast_152_capital_structure_z_zscore_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_152_capital_structure_z_zscore_5d},
    "cast_153_capital_structure_z_rank_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_153_capital_structure_z_rank_5d},
    "cast_154_capital_structure_z_lvl_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_154_capital_structure_z_lvl_21d},
    "cast_155_capital_structure_z_zscore_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_155_capital_structure_z_zscore_21d},
    "cast_156_capital_structure_z_rank_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_156_capital_structure_z_rank_21d},
    "cast_157_capital_structure_z_lvl_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_157_capital_structure_z_lvl_63d},
    "cast_158_capital_structure_z_zscore_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_158_capital_structure_z_zscore_63d},
    "cast_159_capital_structure_z_rank_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_159_capital_structure_z_rank_63d},
    "cast_160_capital_structure_z_lvl_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_160_capital_structure_z_lvl_126d},
    "cast_161_capital_structure_z_zscore_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_161_capital_structure_z_zscore_126d},
    "cast_162_capital_structure_z_rank_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_162_capital_structure_z_rank_126d},
    "cast_163_capital_structure_z_lvl_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_163_capital_structure_z_lvl_252d},
    "cast_164_capital_structure_z_zscore_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_164_capital_structure_z_zscore_252d},
    "cast_165_capital_structure_z_rank_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_165_capital_structure_z_rank_252d},
    "cast_166_equity_value_erosion_lvl_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_166_equity_value_erosion_lvl_5d},
    "cast_167_equity_value_erosion_zscore_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_167_equity_value_erosion_zscore_5d},
    "cast_168_equity_value_erosion_rank_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_168_equity_value_erosion_rank_5d},
    "cast_169_equity_value_erosion_lvl_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_169_equity_value_erosion_lvl_21d},
    "cast_170_equity_value_erosion_zscore_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_170_equity_value_erosion_zscore_21d},
    "cast_171_equity_value_erosion_rank_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_171_equity_value_erosion_rank_21d},
    "cast_172_equity_value_erosion_lvl_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_172_equity_value_erosion_lvl_63d},
    "cast_173_equity_value_erosion_zscore_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_173_equity_value_erosion_zscore_63d},
    "cast_174_equity_value_erosion_rank_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_174_equity_value_erosion_rank_63d},
    "cast_175_equity_value_erosion_lvl_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_175_equity_value_erosion_lvl_126d},
    "cast_176_equity_value_erosion_zscore_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_176_equity_value_erosion_zscore_126d},
    "cast_177_equity_value_erosion_rank_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_177_equity_value_erosion_rank_126d},
    "cast_178_equity_value_erosion_lvl_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_178_equity_value_erosion_lvl_252d},
    "cast_179_equity_value_erosion_zscore_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_179_equity_value_erosion_zscore_252d},
    "cast_180_equity_value_erosion_rank_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_180_equity_value_erosion_rank_252d},
    "cast_181_debt_burden_vol_lvl_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_181_debt_burden_vol_lvl_5d},
    "cast_182_debt_burden_vol_zscore_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_182_debt_burden_vol_zscore_5d},
    "cast_183_debt_burden_vol_rank_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_183_debt_burden_vol_rank_5d},
    "cast_184_debt_burden_vol_lvl_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_184_debt_burden_vol_lvl_21d},
    "cast_185_debt_burden_vol_zscore_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_185_debt_burden_vol_zscore_21d},
    "cast_186_debt_burden_vol_rank_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_186_debt_burden_vol_rank_21d},
    "cast_187_debt_burden_vol_lvl_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_187_debt_burden_vol_lvl_63d},
    "cast_188_debt_burden_vol_zscore_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_188_debt_burden_vol_zscore_63d},
    "cast_189_debt_burden_vol_rank_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_189_debt_burden_vol_rank_63d},
    "cast_190_debt_burden_vol_lvl_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_190_debt_burden_vol_lvl_126d},
    "cast_191_debt_burden_vol_zscore_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_191_debt_burden_vol_zscore_126d},
    "cast_192_debt_burden_vol_rank_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_192_debt_burden_vol_rank_126d},
    "cast_193_debt_burden_vol_lvl_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_193_debt_burden_vol_lvl_252d},
    "cast_194_debt_burden_vol_zscore_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_194_debt_burden_vol_zscore_252d},
    "cast_195_debt_burden_vol_rank_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_195_debt_burden_vol_rank_252d},
    "cast_196_capital_stress_index_lvl_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_196_capital_stress_index_lvl_5d},
    "cast_197_capital_stress_index_zscore_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_197_capital_stress_index_zscore_5d},
    "cast_198_capital_stress_index_rank_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_198_capital_stress_index_rank_5d},
    "cast_199_capital_stress_index_lvl_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_199_capital_stress_index_lvl_21d},
    "cast_200_capital_stress_index_zscore_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_200_capital_stress_index_zscore_21d},
    "cast_201_capital_stress_index_rank_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_201_capital_stress_index_rank_21d},
    "cast_202_capital_stress_index_lvl_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_202_capital_stress_index_lvl_63d},
    "cast_203_capital_stress_index_zscore_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_203_capital_stress_index_zscore_63d},
    "cast_204_capital_stress_index_rank_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_204_capital_stress_index_rank_63d},
    "cast_205_capital_stress_index_lvl_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_205_capital_stress_index_lvl_126d},
    "cast_206_capital_stress_index_zscore_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_206_capital_stress_index_zscore_126d},
    "cast_207_capital_stress_index_rank_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_207_capital_stress_index_rank_126d},
    "cast_208_capital_stress_index_lvl_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_208_capital_stress_index_lvl_252d},
    "cast_209_capital_stress_index_zscore_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_209_capital_stress_index_zscore_252d},
    "cast_210_capital_stress_index_rank_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_210_capital_stress_index_rank_252d},
    "cast_211_solvency_cushion_lvl_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_211_solvency_cushion_lvl_5d},
    "cast_212_solvency_cushion_zscore_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_212_solvency_cushion_zscore_5d},
    "cast_213_solvency_cushion_rank_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_213_solvency_cushion_rank_5d},
    "cast_214_solvency_cushion_lvl_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_214_solvency_cushion_lvl_21d},
    "cast_215_solvency_cushion_zscore_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_215_solvency_cushion_zscore_21d},
    "cast_216_solvency_cushion_rank_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_216_solvency_cushion_rank_21d},
    "cast_217_solvency_cushion_lvl_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_217_solvency_cushion_lvl_63d},
    "cast_218_solvency_cushion_zscore_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_218_solvency_cushion_zscore_63d},
    "cast_219_solvency_cushion_rank_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_219_solvency_cushion_rank_63d},
    "cast_220_solvency_cushion_lvl_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_220_solvency_cushion_lvl_126d},
    "cast_221_solvency_cushion_zscore_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_221_solvency_cushion_zscore_126d},
    "cast_222_solvency_cushion_rank_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_222_solvency_cushion_rank_126d},
    "cast_223_solvency_cushion_lvl_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_223_solvency_cushion_lvl_252d},
    "cast_224_solvency_cushion_zscore_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_224_solvency_cushion_zscore_252d},
    "cast_225_solvency_cushion_rank_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_225_solvency_cushion_rank_252d},
}
