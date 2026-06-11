"""
123_relative_weakness_xs — Base Features Part 1
Domain: relative_weakness_xs
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

def rwxs_001_relative_return_21d_lvl_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_001_relative_return_21d_lvl_5d
    ECONOMIC RATIONALE: Excess return over the market index.
    """
    base = close.pct_change(21) - mkt_close.pct_change(21)
    return _rolling_mean(base, 5)

def rwxs_002_relative_return_21d_zscore_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_002_relative_return_21d_zscore_5d
    ECONOMIC RATIONALE: Excess return over the market index.
    """
    base = close.pct_change(21) - mkt_close.pct_change(21)
    return _zscore_rolling(base, 5)

def rwxs_003_relative_return_21d_rank_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_003_relative_return_21d_rank_5d
    ECONOMIC RATIONALE: Excess return over the market index.
    """
    base = close.pct_change(21) - mkt_close.pct_change(21)
    return _rank_pct(base, 5)

def rwxs_004_relative_return_21d_lvl_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_004_relative_return_21d_lvl_21d
    ECONOMIC RATIONALE: Excess return over the market index.
    """
    base = close.pct_change(21) - mkt_close.pct_change(21)
    return _rolling_mean(base, 21)

def rwxs_005_relative_return_21d_zscore_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_005_relative_return_21d_zscore_21d
    ECONOMIC RATIONALE: Excess return over the market index.
    """
    base = close.pct_change(21) - mkt_close.pct_change(21)
    return _zscore_rolling(base, 21)

def rwxs_006_relative_return_21d_rank_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_006_relative_return_21d_rank_21d
    ECONOMIC RATIONALE: Excess return over the market index.
    """
    base = close.pct_change(21) - mkt_close.pct_change(21)
    return _rank_pct(base, 21)

def rwxs_007_relative_return_21d_lvl_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_007_relative_return_21d_lvl_63d
    ECONOMIC RATIONALE: Excess return over the market index.
    """
    base = close.pct_change(21) - mkt_close.pct_change(21)
    return _rolling_mean(base, 63)

def rwxs_008_relative_return_21d_zscore_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_008_relative_return_21d_zscore_63d
    ECONOMIC RATIONALE: Excess return over the market index.
    """
    base = close.pct_change(21) - mkt_close.pct_change(21)
    return _zscore_rolling(base, 63)

def rwxs_009_relative_return_21d_rank_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_009_relative_return_21d_rank_63d
    ECONOMIC RATIONALE: Excess return over the market index.
    """
    base = close.pct_change(21) - mkt_close.pct_change(21)
    return _rank_pct(base, 63)

def rwxs_010_relative_return_21d_lvl_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_010_relative_return_21d_lvl_126d
    ECONOMIC RATIONALE: Excess return over the market index.
    """
    base = close.pct_change(21) - mkt_close.pct_change(21)
    return _rolling_mean(base, 126)

def rwxs_011_relative_return_21d_zscore_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_011_relative_return_21d_zscore_126d
    ECONOMIC RATIONALE: Excess return over the market index.
    """
    base = close.pct_change(21) - mkt_close.pct_change(21)
    return _zscore_rolling(base, 126)

def rwxs_012_relative_return_21d_rank_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_012_relative_return_21d_rank_126d
    ECONOMIC RATIONALE: Excess return over the market index.
    """
    base = close.pct_change(21) - mkt_close.pct_change(21)
    return _rank_pct(base, 126)

def rwxs_013_relative_return_21d_lvl_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_013_relative_return_21d_lvl_252d
    ECONOMIC RATIONALE: Excess return over the market index.
    """
    base = close.pct_change(21) - mkt_close.pct_change(21)
    return _rolling_mean(base, 252)

def rwxs_014_relative_return_21d_zscore_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_014_relative_return_21d_zscore_252d
    ECONOMIC RATIONALE: Excess return over the market index.
    """
    base = close.pct_change(21) - mkt_close.pct_change(21)
    return _zscore_rolling(base, 252)

def rwxs_015_relative_return_21d_rank_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_015_relative_return_21d_rank_252d
    ECONOMIC RATIONALE: Excess return over the market index.
    """
    base = close.pct_change(21) - mkt_close.pct_change(21)
    return _rank_pct(base, 252)

def rwxs_016_relative_drawdown_lvl_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_016_relative_drawdown_lvl_5d
    ECONOMIC RATIONALE: Drawdown depth relative to market drawdown.
    """
    base = (close/close.rolling(252).max()) - (mkt_close/mkt_close.rolling(252).max())
    return _rolling_mean(base, 5)

def rwxs_017_relative_drawdown_zscore_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_017_relative_drawdown_zscore_5d
    ECONOMIC RATIONALE: Drawdown depth relative to market drawdown.
    """
    base = (close/close.rolling(252).max()) - (mkt_close/mkt_close.rolling(252).max())
    return _zscore_rolling(base, 5)

def rwxs_018_relative_drawdown_rank_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_018_relative_drawdown_rank_5d
    ECONOMIC RATIONALE: Drawdown depth relative to market drawdown.
    """
    base = (close/close.rolling(252).max()) - (mkt_close/mkt_close.rolling(252).max())
    return _rank_pct(base, 5)

def rwxs_019_relative_drawdown_lvl_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_019_relative_drawdown_lvl_21d
    ECONOMIC RATIONALE: Drawdown depth relative to market drawdown.
    """
    base = (close/close.rolling(252).max()) - (mkt_close/mkt_close.rolling(252).max())
    return _rolling_mean(base, 21)

def rwxs_020_relative_drawdown_zscore_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_020_relative_drawdown_zscore_21d
    ECONOMIC RATIONALE: Drawdown depth relative to market drawdown.
    """
    base = (close/close.rolling(252).max()) - (mkt_close/mkt_close.rolling(252).max())
    return _zscore_rolling(base, 21)

def rwxs_021_relative_drawdown_rank_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_021_relative_drawdown_rank_21d
    ECONOMIC RATIONALE: Drawdown depth relative to market drawdown.
    """
    base = (close/close.rolling(252).max()) - (mkt_close/mkt_close.rolling(252).max())
    return _rank_pct(base, 21)

def rwxs_022_relative_drawdown_lvl_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_022_relative_drawdown_lvl_63d
    ECONOMIC RATIONALE: Drawdown depth relative to market drawdown.
    """
    base = (close/close.rolling(252).max()) - (mkt_close/mkt_close.rolling(252).max())
    return _rolling_mean(base, 63)

def rwxs_023_relative_drawdown_zscore_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_023_relative_drawdown_zscore_63d
    ECONOMIC RATIONALE: Drawdown depth relative to market drawdown.
    """
    base = (close/close.rolling(252).max()) - (mkt_close/mkt_close.rolling(252).max())
    return _zscore_rolling(base, 63)

def rwxs_024_relative_drawdown_rank_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_024_relative_drawdown_rank_63d
    ECONOMIC RATIONALE: Drawdown depth relative to market drawdown.
    """
    base = (close/close.rolling(252).max()) - (mkt_close/mkt_close.rolling(252).max())
    return _rank_pct(base, 63)

def rwxs_025_relative_drawdown_lvl_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_025_relative_drawdown_lvl_126d
    ECONOMIC RATIONALE: Drawdown depth relative to market drawdown.
    """
    base = (close/close.rolling(252).max()) - (mkt_close/mkt_close.rolling(252).max())
    return _rolling_mean(base, 126)

def rwxs_026_relative_drawdown_zscore_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_026_relative_drawdown_zscore_126d
    ECONOMIC RATIONALE: Drawdown depth relative to market drawdown.
    """
    base = (close/close.rolling(252).max()) - (mkt_close/mkt_close.rolling(252).max())
    return _zscore_rolling(base, 126)

def rwxs_027_relative_drawdown_rank_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_027_relative_drawdown_rank_126d
    ECONOMIC RATIONALE: Drawdown depth relative to market drawdown.
    """
    base = (close/close.rolling(252).max()) - (mkt_close/mkt_close.rolling(252).max())
    return _rank_pct(base, 126)

def rwxs_028_relative_drawdown_lvl_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_028_relative_drawdown_lvl_252d
    ECONOMIC RATIONALE: Drawdown depth relative to market drawdown.
    """
    base = (close/close.rolling(252).max()) - (mkt_close/mkt_close.rolling(252).max())
    return _rolling_mean(base, 252)

def rwxs_029_relative_drawdown_zscore_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_029_relative_drawdown_zscore_252d
    ECONOMIC RATIONALE: Drawdown depth relative to market drawdown.
    """
    base = (close/close.rolling(252).max()) - (mkt_close/mkt_close.rolling(252).max())
    return _zscore_rolling(base, 252)

def rwxs_030_relative_drawdown_rank_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_030_relative_drawdown_rank_252d
    ECONOMIC RATIONALE: Drawdown depth relative to market drawdown.
    """
    base = (close/close.rolling(252).max()) - (mkt_close/mkt_close.rolling(252).max())
    return _rank_pct(base, 252)

def rwxs_031_beta_adjusted_alpha_lvl_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_031_beta_adjusted_alpha_lvl_5d
    ECONOMIC RATIONALE: 21-day alpha adjusted for rolling beta.
    """
    base = close.pct_change(21) - (close.pct_change(1).rolling(252).corr(mkt_close.pct_change(1)) * (close.rolling(252).std()/mkt_close.rolling(252).std()) * mkt_close.pct_change(21))
    return _rolling_mean(base, 5)

def rwxs_032_beta_adjusted_alpha_zscore_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_032_beta_adjusted_alpha_zscore_5d
    ECONOMIC RATIONALE: 21-day alpha adjusted for rolling beta.
    """
    base = close.pct_change(21) - (close.pct_change(1).rolling(252).corr(mkt_close.pct_change(1)) * (close.rolling(252).std()/mkt_close.rolling(252).std()) * mkt_close.pct_change(21))
    return _zscore_rolling(base, 5)

def rwxs_033_beta_adjusted_alpha_rank_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_033_beta_adjusted_alpha_rank_5d
    ECONOMIC RATIONALE: 21-day alpha adjusted for rolling beta.
    """
    base = close.pct_change(21) - (close.pct_change(1).rolling(252).corr(mkt_close.pct_change(1)) * (close.rolling(252).std()/mkt_close.rolling(252).std()) * mkt_close.pct_change(21))
    return _rank_pct(base, 5)

def rwxs_034_beta_adjusted_alpha_lvl_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_034_beta_adjusted_alpha_lvl_21d
    ECONOMIC RATIONALE: 21-day alpha adjusted for rolling beta.
    """
    base = close.pct_change(21) - (close.pct_change(1).rolling(252).corr(mkt_close.pct_change(1)) * (close.rolling(252).std()/mkt_close.rolling(252).std()) * mkt_close.pct_change(21))
    return _rolling_mean(base, 21)

def rwxs_035_beta_adjusted_alpha_zscore_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_035_beta_adjusted_alpha_zscore_21d
    ECONOMIC RATIONALE: 21-day alpha adjusted for rolling beta.
    """
    base = close.pct_change(21) - (close.pct_change(1).rolling(252).corr(mkt_close.pct_change(1)) * (close.rolling(252).std()/mkt_close.rolling(252).std()) * mkt_close.pct_change(21))
    return _zscore_rolling(base, 21)

def rwxs_036_beta_adjusted_alpha_rank_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_036_beta_adjusted_alpha_rank_21d
    ECONOMIC RATIONALE: 21-day alpha adjusted for rolling beta.
    """
    base = close.pct_change(21) - (close.pct_change(1).rolling(252).corr(mkt_close.pct_change(1)) * (close.rolling(252).std()/mkt_close.rolling(252).std()) * mkt_close.pct_change(21))
    return _rank_pct(base, 21)

def rwxs_037_beta_adjusted_alpha_lvl_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_037_beta_adjusted_alpha_lvl_63d
    ECONOMIC RATIONALE: 21-day alpha adjusted for rolling beta.
    """
    base = close.pct_change(21) - (close.pct_change(1).rolling(252).corr(mkt_close.pct_change(1)) * (close.rolling(252).std()/mkt_close.rolling(252).std()) * mkt_close.pct_change(21))
    return _rolling_mean(base, 63)

def rwxs_038_beta_adjusted_alpha_zscore_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_038_beta_adjusted_alpha_zscore_63d
    ECONOMIC RATIONALE: 21-day alpha adjusted for rolling beta.
    """
    base = close.pct_change(21) - (close.pct_change(1).rolling(252).corr(mkt_close.pct_change(1)) * (close.rolling(252).std()/mkt_close.rolling(252).std()) * mkt_close.pct_change(21))
    return _zscore_rolling(base, 63)

def rwxs_039_beta_adjusted_alpha_rank_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_039_beta_adjusted_alpha_rank_63d
    ECONOMIC RATIONALE: 21-day alpha adjusted for rolling beta.
    """
    base = close.pct_change(21) - (close.pct_change(1).rolling(252).corr(mkt_close.pct_change(1)) * (close.rolling(252).std()/mkt_close.rolling(252).std()) * mkt_close.pct_change(21))
    return _rank_pct(base, 63)

def rwxs_040_beta_adjusted_alpha_lvl_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_040_beta_adjusted_alpha_lvl_126d
    ECONOMIC RATIONALE: 21-day alpha adjusted for rolling beta.
    """
    base = close.pct_change(21) - (close.pct_change(1).rolling(252).corr(mkt_close.pct_change(1)) * (close.rolling(252).std()/mkt_close.rolling(252).std()) * mkt_close.pct_change(21))
    return _rolling_mean(base, 126)

def rwxs_041_beta_adjusted_alpha_zscore_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_041_beta_adjusted_alpha_zscore_126d
    ECONOMIC RATIONALE: 21-day alpha adjusted for rolling beta.
    """
    base = close.pct_change(21) - (close.pct_change(1).rolling(252).corr(mkt_close.pct_change(1)) * (close.rolling(252).std()/mkt_close.rolling(252).std()) * mkt_close.pct_change(21))
    return _zscore_rolling(base, 126)

def rwxs_042_beta_adjusted_alpha_rank_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_042_beta_adjusted_alpha_rank_126d
    ECONOMIC RATIONALE: 21-day alpha adjusted for rolling beta.
    """
    base = close.pct_change(21) - (close.pct_change(1).rolling(252).corr(mkt_close.pct_change(1)) * (close.rolling(252).std()/mkt_close.rolling(252).std()) * mkt_close.pct_change(21))
    return _rank_pct(base, 126)

def rwxs_043_beta_adjusted_alpha_lvl_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_043_beta_adjusted_alpha_lvl_252d
    ECONOMIC RATIONALE: 21-day alpha adjusted for rolling beta.
    """
    base = close.pct_change(21) - (close.pct_change(1).rolling(252).corr(mkt_close.pct_change(1)) * (close.rolling(252).std()/mkt_close.rolling(252).std()) * mkt_close.pct_change(21))
    return _rolling_mean(base, 252)

def rwxs_044_beta_adjusted_alpha_zscore_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_044_beta_adjusted_alpha_zscore_252d
    ECONOMIC RATIONALE: 21-day alpha adjusted for rolling beta.
    """
    base = close.pct_change(21) - (close.pct_change(1).rolling(252).corr(mkt_close.pct_change(1)) * (close.rolling(252).std()/mkt_close.rolling(252).std()) * mkt_close.pct_change(21))
    return _zscore_rolling(base, 252)

def rwxs_045_beta_adjusted_alpha_rank_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_045_beta_adjusted_alpha_rank_252d
    ECONOMIC RATIONALE: 21-day alpha adjusted for rolling beta.
    """
    base = close.pct_change(21) - (close.pct_change(1).rolling(252).corr(mkt_close.pct_change(1)) * (close.rolling(252).std()/mkt_close.rolling(252).std()) * mkt_close.pct_change(21))
    return _rank_pct(base, 252)

def rwxs_046_relative_weakness_z_lvl_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_046_relative_weakness_z_lvl_5d
    ECONOMIC RATIONALE: Z-score of relative performance.
    """
    base = _zscore_rolling(close.pct_change(21) - mkt_close.pct_change(21), 252)
    return _rolling_mean(base, 5)

def rwxs_047_relative_weakness_z_zscore_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_047_relative_weakness_z_zscore_5d
    ECONOMIC RATIONALE: Z-score of relative performance.
    """
    base = _zscore_rolling(close.pct_change(21) - mkt_close.pct_change(21), 252)
    return _zscore_rolling(base, 5)

def rwxs_048_relative_weakness_z_rank_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_048_relative_weakness_z_rank_5d
    ECONOMIC RATIONALE: Z-score of relative performance.
    """
    base = _zscore_rolling(close.pct_change(21) - mkt_close.pct_change(21), 252)
    return _rank_pct(base, 5)

def rwxs_049_relative_weakness_z_lvl_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_049_relative_weakness_z_lvl_21d
    ECONOMIC RATIONALE: Z-score of relative performance.
    """
    base = _zscore_rolling(close.pct_change(21) - mkt_close.pct_change(21), 252)
    return _rolling_mean(base, 21)

def rwxs_050_relative_weakness_z_zscore_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_050_relative_weakness_z_zscore_21d
    ECONOMIC RATIONALE: Z-score of relative performance.
    """
    base = _zscore_rolling(close.pct_change(21) - mkt_close.pct_change(21), 252)
    return _zscore_rolling(base, 21)

def rwxs_051_relative_weakness_z_rank_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_051_relative_weakness_z_rank_21d
    ECONOMIC RATIONALE: Z-score of relative performance.
    """
    base = _zscore_rolling(close.pct_change(21) - mkt_close.pct_change(21), 252)
    return _rank_pct(base, 21)

def rwxs_052_relative_weakness_z_lvl_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_052_relative_weakness_z_lvl_63d
    ECONOMIC RATIONALE: Z-score of relative performance.
    """
    base = _zscore_rolling(close.pct_change(21) - mkt_close.pct_change(21), 252)
    return _rolling_mean(base, 63)

def rwxs_053_relative_weakness_z_zscore_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_053_relative_weakness_z_zscore_63d
    ECONOMIC RATIONALE: Z-score of relative performance.
    """
    base = _zscore_rolling(close.pct_change(21) - mkt_close.pct_change(21), 252)
    return _zscore_rolling(base, 63)

def rwxs_054_relative_weakness_z_rank_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_054_relative_weakness_z_rank_63d
    ECONOMIC RATIONALE: Z-score of relative performance.
    """
    base = _zscore_rolling(close.pct_change(21) - mkt_close.pct_change(21), 252)
    return _rank_pct(base, 63)

def rwxs_055_relative_weakness_z_lvl_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_055_relative_weakness_z_lvl_126d
    ECONOMIC RATIONALE: Z-score of relative performance.
    """
    base = _zscore_rolling(close.pct_change(21) - mkt_close.pct_change(21), 252)
    return _rolling_mean(base, 126)

def rwxs_056_relative_weakness_z_zscore_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_056_relative_weakness_z_zscore_126d
    ECONOMIC RATIONALE: Z-score of relative performance.
    """
    base = _zscore_rolling(close.pct_change(21) - mkt_close.pct_change(21), 252)
    return _zscore_rolling(base, 126)

def rwxs_057_relative_weakness_z_rank_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_057_relative_weakness_z_rank_126d
    ECONOMIC RATIONALE: Z-score of relative performance.
    """
    base = _zscore_rolling(close.pct_change(21) - mkt_close.pct_change(21), 252)
    return _rank_pct(base, 126)

def rwxs_058_relative_weakness_z_lvl_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_058_relative_weakness_z_lvl_252d
    ECONOMIC RATIONALE: Z-score of relative performance.
    """
    base = _zscore_rolling(close.pct_change(21) - mkt_close.pct_change(21), 252)
    return _rolling_mean(base, 252)

def rwxs_059_relative_weakness_z_zscore_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_059_relative_weakness_z_zscore_252d
    ECONOMIC RATIONALE: Z-score of relative performance.
    """
    base = _zscore_rolling(close.pct_change(21) - mkt_close.pct_change(21), 252)
    return _zscore_rolling(base, 252)

def rwxs_060_relative_weakness_z_rank_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_060_relative_weakness_z_rank_252d
    ECONOMIC RATIONALE: Z-score of relative performance.
    """
    base = _zscore_rolling(close.pct_change(21) - mkt_close.pct_change(21), 252)
    return _rank_pct(base, 252)

def rwxs_061_underperformance_persistence_lvl_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_061_underperformance_persistence_lvl_5d
    ECONOMIC RATIONALE: Frequency of days underperforming the market.
    """
    base = ((close.pct_change(1) < mkt_close.pct_change(1)).rolling(21).sum())
    return _rolling_mean(base, 5)

def rwxs_062_underperformance_persistence_zscore_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_062_underperformance_persistence_zscore_5d
    ECONOMIC RATIONALE: Frequency of days underperforming the market.
    """
    base = ((close.pct_change(1) < mkt_close.pct_change(1)).rolling(21).sum())
    return _zscore_rolling(base, 5)

def rwxs_063_underperformance_persistence_rank_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_063_underperformance_persistence_rank_5d
    ECONOMIC RATIONALE: Frequency of days underperforming the market.
    """
    base = ((close.pct_change(1) < mkt_close.pct_change(1)).rolling(21).sum())
    return _rank_pct(base, 5)

def rwxs_064_underperformance_persistence_lvl_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_064_underperformance_persistence_lvl_21d
    ECONOMIC RATIONALE: Frequency of days underperforming the market.
    """
    base = ((close.pct_change(1) < mkt_close.pct_change(1)).rolling(21).sum())
    return _rolling_mean(base, 21)

def rwxs_065_underperformance_persistence_zscore_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_065_underperformance_persistence_zscore_21d
    ECONOMIC RATIONALE: Frequency of days underperforming the market.
    """
    base = ((close.pct_change(1) < mkt_close.pct_change(1)).rolling(21).sum())
    return _zscore_rolling(base, 21)

def rwxs_066_underperformance_persistence_rank_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_066_underperformance_persistence_rank_21d
    ECONOMIC RATIONALE: Frequency of days underperforming the market.
    """
    base = ((close.pct_change(1) < mkt_close.pct_change(1)).rolling(21).sum())
    return _rank_pct(base, 21)

def rwxs_067_underperformance_persistence_lvl_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_067_underperformance_persistence_lvl_63d
    ECONOMIC RATIONALE: Frequency of days underperforming the market.
    """
    base = ((close.pct_change(1) < mkt_close.pct_change(1)).rolling(21).sum())
    return _rolling_mean(base, 63)

def rwxs_068_underperformance_persistence_zscore_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_068_underperformance_persistence_zscore_63d
    ECONOMIC RATIONALE: Frequency of days underperforming the market.
    """
    base = ((close.pct_change(1) < mkt_close.pct_change(1)).rolling(21).sum())
    return _zscore_rolling(base, 63)

def rwxs_069_underperformance_persistence_rank_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_069_underperformance_persistence_rank_63d
    ECONOMIC RATIONALE: Frequency of days underperforming the market.
    """
    base = ((close.pct_change(1) < mkt_close.pct_change(1)).rolling(21).sum())
    return _rank_pct(base, 63)

def rwxs_070_underperformance_persistence_lvl_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_070_underperformance_persistence_lvl_126d
    ECONOMIC RATIONALE: Frequency of days underperforming the market.
    """
    base = ((close.pct_change(1) < mkt_close.pct_change(1)).rolling(21).sum())
    return _rolling_mean(base, 126)

def rwxs_071_underperformance_persistence_zscore_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_071_underperformance_persistence_zscore_126d
    ECONOMIC RATIONALE: Frequency of days underperforming the market.
    """
    base = ((close.pct_change(1) < mkt_close.pct_change(1)).rolling(21).sum())
    return _zscore_rolling(base, 126)

def rwxs_072_underperformance_persistence_rank_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_072_underperformance_persistence_rank_126d
    ECONOMIC RATIONALE: Frequency of days underperforming the market.
    """
    base = ((close.pct_change(1) < mkt_close.pct_change(1)).rolling(21).sum())
    return _rank_pct(base, 126)

def rwxs_073_underperformance_persistence_lvl_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_073_underperformance_persistence_lvl_252d
    ECONOMIC RATIONALE: Frequency of days underperforming the market.
    """
    base = ((close.pct_change(1) < mkt_close.pct_change(1)).rolling(21).sum())
    return _rolling_mean(base, 252)

def rwxs_074_underperformance_persistence_zscore_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_074_underperformance_persistence_zscore_252d
    ECONOMIC RATIONALE: Frequency of days underperforming the market.
    """
    base = ((close.pct_change(1) < mkt_close.pct_change(1)).rolling(21).sum())
    return _zscore_rolling(base, 252)

def rwxs_075_underperformance_persistence_rank_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_075_underperformance_persistence_rank_252d
    ECONOMIC RATIONALE: Frequency of days underperforming the market.
    """
    base = ((close.pct_change(1) < mkt_close.pct_change(1)).rolling(21).sum())
    return _rank_pct(base, 252)

def rwxs_076_relative_momentum_div_lvl_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_076_relative_momentum_div_lvl_5d
    ECONOMIC RATIONALE: Ratio of stock momentum to market momentum.
    """
    base = close.pct_change(63) / mkt_close.pct_change(63).replace(0, 1e-9)
    return _rolling_mean(base, 5)

def rwxs_077_relative_momentum_div_zscore_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_077_relative_momentum_div_zscore_5d
    ECONOMIC RATIONALE: Ratio of stock momentum to market momentum.
    """
    base = close.pct_change(63) / mkt_close.pct_change(63).replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def rwxs_078_relative_momentum_div_rank_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_078_relative_momentum_div_rank_5d
    ECONOMIC RATIONALE: Ratio of stock momentum to market momentum.
    """
    base = close.pct_change(63) / mkt_close.pct_change(63).replace(0, 1e-9)
    return _rank_pct(base, 5)

def rwxs_079_relative_momentum_div_lvl_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_079_relative_momentum_div_lvl_21d
    ECONOMIC RATIONALE: Ratio of stock momentum to market momentum.
    """
    base = close.pct_change(63) / mkt_close.pct_change(63).replace(0, 1e-9)
    return _rolling_mean(base, 21)

def rwxs_080_relative_momentum_div_zscore_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_080_relative_momentum_div_zscore_21d
    ECONOMIC RATIONALE: Ratio of stock momentum to market momentum.
    """
    base = close.pct_change(63) / mkt_close.pct_change(63).replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def rwxs_081_relative_momentum_div_rank_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_081_relative_momentum_div_rank_21d
    ECONOMIC RATIONALE: Ratio of stock momentum to market momentum.
    """
    base = close.pct_change(63) / mkt_close.pct_change(63).replace(0, 1e-9)
    return _rank_pct(base, 21)

def rwxs_082_relative_momentum_div_lvl_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_082_relative_momentum_div_lvl_63d
    ECONOMIC RATIONALE: Ratio of stock momentum to market momentum.
    """
    base = close.pct_change(63) / mkt_close.pct_change(63).replace(0, 1e-9)
    return _rolling_mean(base, 63)

def rwxs_083_relative_momentum_div_zscore_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_083_relative_momentum_div_zscore_63d
    ECONOMIC RATIONALE: Ratio of stock momentum to market momentum.
    """
    base = close.pct_change(63) / mkt_close.pct_change(63).replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def rwxs_084_relative_momentum_div_rank_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_084_relative_momentum_div_rank_63d
    ECONOMIC RATIONALE: Ratio of stock momentum to market momentum.
    """
    base = close.pct_change(63) / mkt_close.pct_change(63).replace(0, 1e-9)
    return _rank_pct(base, 63)

def rwxs_085_relative_momentum_div_lvl_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_085_relative_momentum_div_lvl_126d
    ECONOMIC RATIONALE: Ratio of stock momentum to market momentum.
    """
    base = close.pct_change(63) / mkt_close.pct_change(63).replace(0, 1e-9)
    return _rolling_mean(base, 126)

def rwxs_086_relative_momentum_div_zscore_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_086_relative_momentum_div_zscore_126d
    ECONOMIC RATIONALE: Ratio of stock momentum to market momentum.
    """
    base = close.pct_change(63) / mkt_close.pct_change(63).replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def rwxs_087_relative_momentum_div_rank_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_087_relative_momentum_div_rank_126d
    ECONOMIC RATIONALE: Ratio of stock momentum to market momentum.
    """
    base = close.pct_change(63) / mkt_close.pct_change(63).replace(0, 1e-9)
    return _rank_pct(base, 126)

def rwxs_088_relative_momentum_div_lvl_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_088_relative_momentum_div_lvl_252d
    ECONOMIC RATIONALE: Ratio of stock momentum to market momentum.
    """
    base = close.pct_change(63) / mkt_close.pct_change(63).replace(0, 1e-9)
    return _rolling_mean(base, 252)

def rwxs_089_relative_momentum_div_zscore_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_089_relative_momentum_div_zscore_252d
    ECONOMIC RATIONALE: Ratio of stock momentum to market momentum.
    """
    base = close.pct_change(63) / mkt_close.pct_change(63).replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def rwxs_090_relative_momentum_div_rank_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_090_relative_momentum_div_rank_252d
    ECONOMIC RATIONALE: Ratio of stock momentum to market momentum.
    """
    base = close.pct_change(63) / mkt_close.pct_change(63).replace(0, 1e-9)
    return _rank_pct(base, 252)

def rwxs_091_xs_weakness_acceleration_lvl_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_091_xs_weakness_acceleration_lvl_5d
    ECONOMIC RATIONALE: Acceleration of underperformance.
    """
    base = (close.pct_change(21) - mkt_close.pct_change(21)).diff(21)
    return _rolling_mean(base, 5)

def rwxs_092_xs_weakness_acceleration_zscore_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_092_xs_weakness_acceleration_zscore_5d
    ECONOMIC RATIONALE: Acceleration of underperformance.
    """
    base = (close.pct_change(21) - mkt_close.pct_change(21)).diff(21)
    return _zscore_rolling(base, 5)

def rwxs_093_xs_weakness_acceleration_rank_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_093_xs_weakness_acceleration_rank_5d
    ECONOMIC RATIONALE: Acceleration of underperformance.
    """
    base = (close.pct_change(21) - mkt_close.pct_change(21)).diff(21)
    return _rank_pct(base, 5)

def rwxs_094_xs_weakness_acceleration_lvl_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_094_xs_weakness_acceleration_lvl_21d
    ECONOMIC RATIONALE: Acceleration of underperformance.
    """
    base = (close.pct_change(21) - mkt_close.pct_change(21)).diff(21)
    return _rolling_mean(base, 21)

def rwxs_095_xs_weakness_acceleration_zscore_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_095_xs_weakness_acceleration_zscore_21d
    ECONOMIC RATIONALE: Acceleration of underperformance.
    """
    base = (close.pct_change(21) - mkt_close.pct_change(21)).diff(21)
    return _zscore_rolling(base, 21)

def rwxs_096_xs_weakness_acceleration_rank_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_096_xs_weakness_acceleration_rank_21d
    ECONOMIC RATIONALE: Acceleration of underperformance.
    """
    base = (close.pct_change(21) - mkt_close.pct_change(21)).diff(21)
    return _rank_pct(base, 21)

def rwxs_097_xs_weakness_acceleration_lvl_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_097_xs_weakness_acceleration_lvl_63d
    ECONOMIC RATIONALE: Acceleration of underperformance.
    """
    base = (close.pct_change(21) - mkt_close.pct_change(21)).diff(21)
    return _rolling_mean(base, 63)

def rwxs_098_xs_weakness_acceleration_zscore_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_098_xs_weakness_acceleration_zscore_63d
    ECONOMIC RATIONALE: Acceleration of underperformance.
    """
    base = (close.pct_change(21) - mkt_close.pct_change(21)).diff(21)
    return _zscore_rolling(base, 63)

def rwxs_099_xs_weakness_acceleration_rank_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_099_xs_weakness_acceleration_rank_63d
    ECONOMIC RATIONALE: Acceleration of underperformance.
    """
    base = (close.pct_change(21) - mkt_close.pct_change(21)).diff(21)
    return _rank_pct(base, 63)

def rwxs_100_xs_weakness_acceleration_lvl_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_100_xs_weakness_acceleration_lvl_126d
    ECONOMIC RATIONALE: Acceleration of underperformance.
    """
    base = (close.pct_change(21) - mkt_close.pct_change(21)).diff(21)
    return _rolling_mean(base, 126)

def rwxs_101_xs_weakness_acceleration_zscore_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_101_xs_weakness_acceleration_zscore_126d
    ECONOMIC RATIONALE: Acceleration of underperformance.
    """
    base = (close.pct_change(21) - mkt_close.pct_change(21)).diff(21)
    return _zscore_rolling(base, 126)

def rwxs_102_xs_weakness_acceleration_rank_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_102_xs_weakness_acceleration_rank_126d
    ECONOMIC RATIONALE: Acceleration of underperformance.
    """
    base = (close.pct_change(21) - mkt_close.pct_change(21)).diff(21)
    return _rank_pct(base, 126)

def rwxs_103_xs_weakness_acceleration_lvl_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_103_xs_weakness_acceleration_lvl_252d
    ECONOMIC RATIONALE: Acceleration of underperformance.
    """
    base = (close.pct_change(21) - mkt_close.pct_change(21)).diff(21)
    return _rolling_mean(base, 252)

def rwxs_104_xs_weakness_acceleration_zscore_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_104_xs_weakness_acceleration_zscore_252d
    ECONOMIC RATIONALE: Acceleration of underperformance.
    """
    base = (close.pct_change(21) - mkt_close.pct_change(21)).diff(21)
    return _zscore_rolling(base, 252)

def rwxs_105_xs_weakness_acceleration_rank_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_105_xs_weakness_acceleration_rank_252d
    ECONOMIC RATIONALE: Acceleration of underperformance.
    """
    base = (close.pct_change(21) - mkt_close.pct_change(21)).diff(21)
    return _rank_pct(base, 252)

def rwxs_106_relative_volatility_lvl_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_106_relative_volatility_lvl_5d
    ECONOMIC RATIONALE: Stock volatility relative to market volatility.
    """
    base = close.rolling(21).std() / mkt_close.rolling(21).std()
    return _rolling_mean(base, 5)

def rwxs_107_relative_volatility_zscore_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_107_relative_volatility_zscore_5d
    ECONOMIC RATIONALE: Stock volatility relative to market volatility.
    """
    base = close.rolling(21).std() / mkt_close.rolling(21).std()
    return _zscore_rolling(base, 5)

def rwxs_108_relative_volatility_rank_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_108_relative_volatility_rank_5d
    ECONOMIC RATIONALE: Stock volatility relative to market volatility.
    """
    base = close.rolling(21).std() / mkt_close.rolling(21).std()
    return _rank_pct(base, 5)

def rwxs_109_relative_volatility_lvl_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_109_relative_volatility_lvl_21d
    ECONOMIC RATIONALE: Stock volatility relative to market volatility.
    """
    base = close.rolling(21).std() / mkt_close.rolling(21).std()
    return _rolling_mean(base, 21)

def rwxs_110_relative_volatility_zscore_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_110_relative_volatility_zscore_21d
    ECONOMIC RATIONALE: Stock volatility relative to market volatility.
    """
    base = close.rolling(21).std() / mkt_close.rolling(21).std()
    return _zscore_rolling(base, 21)

def rwxs_111_relative_volatility_rank_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_111_relative_volatility_rank_21d
    ECONOMIC RATIONALE: Stock volatility relative to market volatility.
    """
    base = close.rolling(21).std() / mkt_close.rolling(21).std()
    return _rank_pct(base, 21)

def rwxs_112_relative_volatility_lvl_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_112_relative_volatility_lvl_63d
    ECONOMIC RATIONALE: Stock volatility relative to market volatility.
    """
    base = close.rolling(21).std() / mkt_close.rolling(21).std()
    return _rolling_mean(base, 63)

def rwxs_113_relative_volatility_zscore_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_113_relative_volatility_zscore_63d
    ECONOMIC RATIONALE: Stock volatility relative to market volatility.
    """
    base = close.rolling(21).std() / mkt_close.rolling(21).std()
    return _zscore_rolling(base, 63)

def rwxs_114_relative_volatility_rank_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_114_relative_volatility_rank_63d
    ECONOMIC RATIONALE: Stock volatility relative to market volatility.
    """
    base = close.rolling(21).std() / mkt_close.rolling(21).std()
    return _rank_pct(base, 63)

def rwxs_115_relative_volatility_lvl_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_115_relative_volatility_lvl_126d
    ECONOMIC RATIONALE: Stock volatility relative to market volatility.
    """
    base = close.rolling(21).std() / mkt_close.rolling(21).std()
    return _rolling_mean(base, 126)

def rwxs_116_relative_volatility_zscore_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_116_relative_volatility_zscore_126d
    ECONOMIC RATIONALE: Stock volatility relative to market volatility.
    """
    base = close.rolling(21).std() / mkt_close.rolling(21).std()
    return _zscore_rolling(base, 126)

def rwxs_117_relative_volatility_rank_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_117_relative_volatility_rank_126d
    ECONOMIC RATIONALE: Stock volatility relative to market volatility.
    """
    base = close.rolling(21).std() / mkt_close.rolling(21).std()
    return _rank_pct(base, 126)

def rwxs_118_relative_volatility_lvl_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_118_relative_volatility_lvl_252d
    ECONOMIC RATIONALE: Stock volatility relative to market volatility.
    """
    base = close.rolling(21).std() / mkt_close.rolling(21).std()
    return _rolling_mean(base, 252)

def rwxs_119_relative_volatility_zscore_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_119_relative_volatility_zscore_252d
    ECONOMIC RATIONALE: Stock volatility relative to market volatility.
    """
    base = close.rolling(21).std() / mkt_close.rolling(21).std()
    return _zscore_rolling(base, 252)

def rwxs_120_relative_volatility_rank_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_120_relative_volatility_rank_252d
    ECONOMIC RATIONALE: Stock volatility relative to market volatility.
    """
    base = close.rolling(21).std() / mkt_close.rolling(21).std()
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V123_REGISTRY_1 = {
    "rwxs_001_relative_return_21d_lvl_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_001_relative_return_21d_lvl_5d},
    "rwxs_002_relative_return_21d_zscore_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_002_relative_return_21d_zscore_5d},
    "rwxs_003_relative_return_21d_rank_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_003_relative_return_21d_rank_5d},
    "rwxs_004_relative_return_21d_lvl_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_004_relative_return_21d_lvl_21d},
    "rwxs_005_relative_return_21d_zscore_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_005_relative_return_21d_zscore_21d},
    "rwxs_006_relative_return_21d_rank_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_006_relative_return_21d_rank_21d},
    "rwxs_007_relative_return_21d_lvl_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_007_relative_return_21d_lvl_63d},
    "rwxs_008_relative_return_21d_zscore_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_008_relative_return_21d_zscore_63d},
    "rwxs_009_relative_return_21d_rank_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_009_relative_return_21d_rank_63d},
    "rwxs_010_relative_return_21d_lvl_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_010_relative_return_21d_lvl_126d},
    "rwxs_011_relative_return_21d_zscore_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_011_relative_return_21d_zscore_126d},
    "rwxs_012_relative_return_21d_rank_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_012_relative_return_21d_rank_126d},
    "rwxs_013_relative_return_21d_lvl_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_013_relative_return_21d_lvl_252d},
    "rwxs_014_relative_return_21d_zscore_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_014_relative_return_21d_zscore_252d},
    "rwxs_015_relative_return_21d_rank_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_015_relative_return_21d_rank_252d},
    "rwxs_016_relative_drawdown_lvl_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_016_relative_drawdown_lvl_5d},
    "rwxs_017_relative_drawdown_zscore_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_017_relative_drawdown_zscore_5d},
    "rwxs_018_relative_drawdown_rank_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_018_relative_drawdown_rank_5d},
    "rwxs_019_relative_drawdown_lvl_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_019_relative_drawdown_lvl_21d},
    "rwxs_020_relative_drawdown_zscore_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_020_relative_drawdown_zscore_21d},
    "rwxs_021_relative_drawdown_rank_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_021_relative_drawdown_rank_21d},
    "rwxs_022_relative_drawdown_lvl_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_022_relative_drawdown_lvl_63d},
    "rwxs_023_relative_drawdown_zscore_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_023_relative_drawdown_zscore_63d},
    "rwxs_024_relative_drawdown_rank_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_024_relative_drawdown_rank_63d},
    "rwxs_025_relative_drawdown_lvl_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_025_relative_drawdown_lvl_126d},
    "rwxs_026_relative_drawdown_zscore_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_026_relative_drawdown_zscore_126d},
    "rwxs_027_relative_drawdown_rank_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_027_relative_drawdown_rank_126d},
    "rwxs_028_relative_drawdown_lvl_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_028_relative_drawdown_lvl_252d},
    "rwxs_029_relative_drawdown_zscore_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_029_relative_drawdown_zscore_252d},
    "rwxs_030_relative_drawdown_rank_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_030_relative_drawdown_rank_252d},
    "rwxs_031_beta_adjusted_alpha_lvl_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_031_beta_adjusted_alpha_lvl_5d},
    "rwxs_032_beta_adjusted_alpha_zscore_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_032_beta_adjusted_alpha_zscore_5d},
    "rwxs_033_beta_adjusted_alpha_rank_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_033_beta_adjusted_alpha_rank_5d},
    "rwxs_034_beta_adjusted_alpha_lvl_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_034_beta_adjusted_alpha_lvl_21d},
    "rwxs_035_beta_adjusted_alpha_zscore_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_035_beta_adjusted_alpha_zscore_21d},
    "rwxs_036_beta_adjusted_alpha_rank_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_036_beta_adjusted_alpha_rank_21d},
    "rwxs_037_beta_adjusted_alpha_lvl_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_037_beta_adjusted_alpha_lvl_63d},
    "rwxs_038_beta_adjusted_alpha_zscore_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_038_beta_adjusted_alpha_zscore_63d},
    "rwxs_039_beta_adjusted_alpha_rank_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_039_beta_adjusted_alpha_rank_63d},
    "rwxs_040_beta_adjusted_alpha_lvl_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_040_beta_adjusted_alpha_lvl_126d},
    "rwxs_041_beta_adjusted_alpha_zscore_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_041_beta_adjusted_alpha_zscore_126d},
    "rwxs_042_beta_adjusted_alpha_rank_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_042_beta_adjusted_alpha_rank_126d},
    "rwxs_043_beta_adjusted_alpha_lvl_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_043_beta_adjusted_alpha_lvl_252d},
    "rwxs_044_beta_adjusted_alpha_zscore_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_044_beta_adjusted_alpha_zscore_252d},
    "rwxs_045_beta_adjusted_alpha_rank_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_045_beta_adjusted_alpha_rank_252d},
    "rwxs_046_relative_weakness_z_lvl_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_046_relative_weakness_z_lvl_5d},
    "rwxs_047_relative_weakness_z_zscore_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_047_relative_weakness_z_zscore_5d},
    "rwxs_048_relative_weakness_z_rank_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_048_relative_weakness_z_rank_5d},
    "rwxs_049_relative_weakness_z_lvl_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_049_relative_weakness_z_lvl_21d},
    "rwxs_050_relative_weakness_z_zscore_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_050_relative_weakness_z_zscore_21d},
    "rwxs_051_relative_weakness_z_rank_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_051_relative_weakness_z_rank_21d},
    "rwxs_052_relative_weakness_z_lvl_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_052_relative_weakness_z_lvl_63d},
    "rwxs_053_relative_weakness_z_zscore_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_053_relative_weakness_z_zscore_63d},
    "rwxs_054_relative_weakness_z_rank_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_054_relative_weakness_z_rank_63d},
    "rwxs_055_relative_weakness_z_lvl_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_055_relative_weakness_z_lvl_126d},
    "rwxs_056_relative_weakness_z_zscore_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_056_relative_weakness_z_zscore_126d},
    "rwxs_057_relative_weakness_z_rank_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_057_relative_weakness_z_rank_126d},
    "rwxs_058_relative_weakness_z_lvl_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_058_relative_weakness_z_lvl_252d},
    "rwxs_059_relative_weakness_z_zscore_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_059_relative_weakness_z_zscore_252d},
    "rwxs_060_relative_weakness_z_rank_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_060_relative_weakness_z_rank_252d},
    "rwxs_061_underperformance_persistence_lvl_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_061_underperformance_persistence_lvl_5d},
    "rwxs_062_underperformance_persistence_zscore_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_062_underperformance_persistence_zscore_5d},
    "rwxs_063_underperformance_persistence_rank_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_063_underperformance_persistence_rank_5d},
    "rwxs_064_underperformance_persistence_lvl_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_064_underperformance_persistence_lvl_21d},
    "rwxs_065_underperformance_persistence_zscore_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_065_underperformance_persistence_zscore_21d},
    "rwxs_066_underperformance_persistence_rank_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_066_underperformance_persistence_rank_21d},
    "rwxs_067_underperformance_persistence_lvl_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_067_underperformance_persistence_lvl_63d},
    "rwxs_068_underperformance_persistence_zscore_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_068_underperformance_persistence_zscore_63d},
    "rwxs_069_underperformance_persistence_rank_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_069_underperformance_persistence_rank_63d},
    "rwxs_070_underperformance_persistence_lvl_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_070_underperformance_persistence_lvl_126d},
    "rwxs_071_underperformance_persistence_zscore_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_071_underperformance_persistence_zscore_126d},
    "rwxs_072_underperformance_persistence_rank_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_072_underperformance_persistence_rank_126d},
    "rwxs_073_underperformance_persistence_lvl_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_073_underperformance_persistence_lvl_252d},
    "rwxs_074_underperformance_persistence_zscore_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_074_underperformance_persistence_zscore_252d},
    "rwxs_075_underperformance_persistence_rank_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_075_underperformance_persistence_rank_252d},
    "rwxs_076_relative_momentum_div_lvl_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_076_relative_momentum_div_lvl_5d},
    "rwxs_077_relative_momentum_div_zscore_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_077_relative_momentum_div_zscore_5d},
    "rwxs_078_relative_momentum_div_rank_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_078_relative_momentum_div_rank_5d},
    "rwxs_079_relative_momentum_div_lvl_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_079_relative_momentum_div_lvl_21d},
    "rwxs_080_relative_momentum_div_zscore_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_080_relative_momentum_div_zscore_21d},
    "rwxs_081_relative_momentum_div_rank_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_081_relative_momentum_div_rank_21d},
    "rwxs_082_relative_momentum_div_lvl_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_082_relative_momentum_div_lvl_63d},
    "rwxs_083_relative_momentum_div_zscore_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_083_relative_momentum_div_zscore_63d},
    "rwxs_084_relative_momentum_div_rank_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_084_relative_momentum_div_rank_63d},
    "rwxs_085_relative_momentum_div_lvl_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_085_relative_momentum_div_lvl_126d},
    "rwxs_086_relative_momentum_div_zscore_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_086_relative_momentum_div_zscore_126d},
    "rwxs_087_relative_momentum_div_rank_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_087_relative_momentum_div_rank_126d},
    "rwxs_088_relative_momentum_div_lvl_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_088_relative_momentum_div_lvl_252d},
    "rwxs_089_relative_momentum_div_zscore_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_089_relative_momentum_div_zscore_252d},
    "rwxs_090_relative_momentum_div_rank_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_090_relative_momentum_div_rank_252d},
    "rwxs_091_xs_weakness_acceleration_lvl_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_091_xs_weakness_acceleration_lvl_5d},
    "rwxs_092_xs_weakness_acceleration_zscore_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_092_xs_weakness_acceleration_zscore_5d},
    "rwxs_093_xs_weakness_acceleration_rank_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_093_xs_weakness_acceleration_rank_5d},
    "rwxs_094_xs_weakness_acceleration_lvl_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_094_xs_weakness_acceleration_lvl_21d},
    "rwxs_095_xs_weakness_acceleration_zscore_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_095_xs_weakness_acceleration_zscore_21d},
    "rwxs_096_xs_weakness_acceleration_rank_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_096_xs_weakness_acceleration_rank_21d},
    "rwxs_097_xs_weakness_acceleration_lvl_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_097_xs_weakness_acceleration_lvl_63d},
    "rwxs_098_xs_weakness_acceleration_zscore_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_098_xs_weakness_acceleration_zscore_63d},
    "rwxs_099_xs_weakness_acceleration_rank_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_099_xs_weakness_acceleration_rank_63d},
    "rwxs_100_xs_weakness_acceleration_lvl_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_100_xs_weakness_acceleration_lvl_126d},
    "rwxs_101_xs_weakness_acceleration_zscore_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_101_xs_weakness_acceleration_zscore_126d},
    "rwxs_102_xs_weakness_acceleration_rank_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_102_xs_weakness_acceleration_rank_126d},
    "rwxs_103_xs_weakness_acceleration_lvl_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_103_xs_weakness_acceleration_lvl_252d},
    "rwxs_104_xs_weakness_acceleration_zscore_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_104_xs_weakness_acceleration_zscore_252d},
    "rwxs_105_xs_weakness_acceleration_rank_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_105_xs_weakness_acceleration_rank_252d},
    "rwxs_106_relative_volatility_lvl_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_106_relative_volatility_lvl_5d},
    "rwxs_107_relative_volatility_zscore_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_107_relative_volatility_zscore_5d},
    "rwxs_108_relative_volatility_rank_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_108_relative_volatility_rank_5d},
    "rwxs_109_relative_volatility_lvl_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_109_relative_volatility_lvl_21d},
    "rwxs_110_relative_volatility_zscore_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_110_relative_volatility_zscore_21d},
    "rwxs_111_relative_volatility_rank_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_111_relative_volatility_rank_21d},
    "rwxs_112_relative_volatility_lvl_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_112_relative_volatility_lvl_63d},
    "rwxs_113_relative_volatility_zscore_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_113_relative_volatility_zscore_63d},
    "rwxs_114_relative_volatility_rank_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_114_relative_volatility_rank_63d},
    "rwxs_115_relative_volatility_lvl_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_115_relative_volatility_lvl_126d},
    "rwxs_116_relative_volatility_zscore_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_116_relative_volatility_zscore_126d},
    "rwxs_117_relative_volatility_rank_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_117_relative_volatility_rank_126d},
    "rwxs_118_relative_volatility_lvl_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_118_relative_volatility_lvl_252d},
    "rwxs_119_relative_volatility_zscore_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_119_relative_volatility_zscore_252d},
    "rwxs_120_relative_volatility_rank_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_120_relative_volatility_rank_252d},
}
