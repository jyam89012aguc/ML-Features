"""
122_capital_access_stress — Base Features Part 1
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

def cast_001_interest_burden_proxy_lvl_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_001_interest_burden_proxy_lvl_5d
    ECONOMIC RATIONALE: Estimated interest expense relative to free cash flow.
    """
    base = (debt * 0.08) / fcf.replace(0, 1e-9)
    return _rolling_mean(base, 5)

def cast_002_interest_burden_proxy_zscore_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_002_interest_burden_proxy_zscore_5d
    ECONOMIC RATIONALE: Estimated interest expense relative to free cash flow.
    """
    base = (debt * 0.08) / fcf.replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def cast_003_interest_burden_proxy_rank_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_003_interest_burden_proxy_rank_5d
    ECONOMIC RATIONALE: Estimated interest expense relative to free cash flow.
    """
    base = (debt * 0.08) / fcf.replace(0, 1e-9)
    return _rank_pct(base, 5)

def cast_004_interest_burden_proxy_lvl_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_004_interest_burden_proxy_lvl_21d
    ECONOMIC RATIONALE: Estimated interest expense relative to free cash flow.
    """
    base = (debt * 0.08) / fcf.replace(0, 1e-9)
    return _rolling_mean(base, 21)

def cast_005_interest_burden_proxy_zscore_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_005_interest_burden_proxy_zscore_21d
    ECONOMIC RATIONALE: Estimated interest expense relative to free cash flow.
    """
    base = (debt * 0.08) / fcf.replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def cast_006_interest_burden_proxy_rank_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_006_interest_burden_proxy_rank_21d
    ECONOMIC RATIONALE: Estimated interest expense relative to free cash flow.
    """
    base = (debt * 0.08) / fcf.replace(0, 1e-9)
    return _rank_pct(base, 21)

def cast_007_interest_burden_proxy_lvl_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_007_interest_burden_proxy_lvl_63d
    ECONOMIC RATIONALE: Estimated interest expense relative to free cash flow.
    """
    base = (debt * 0.08) / fcf.replace(0, 1e-9)
    return _rolling_mean(base, 63)

def cast_008_interest_burden_proxy_zscore_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_008_interest_burden_proxy_zscore_63d
    ECONOMIC RATIONALE: Estimated interest expense relative to free cash flow.
    """
    base = (debt * 0.08) / fcf.replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def cast_009_interest_burden_proxy_rank_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_009_interest_burden_proxy_rank_63d
    ECONOMIC RATIONALE: Estimated interest expense relative to free cash flow.
    """
    base = (debt * 0.08) / fcf.replace(0, 1e-9)
    return _rank_pct(base, 63)

def cast_010_interest_burden_proxy_lvl_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_010_interest_burden_proxy_lvl_126d
    ECONOMIC RATIONALE: Estimated interest expense relative to free cash flow.
    """
    base = (debt * 0.08) / fcf.replace(0, 1e-9)
    return _rolling_mean(base, 126)

def cast_011_interest_burden_proxy_zscore_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_011_interest_burden_proxy_zscore_126d
    ECONOMIC RATIONALE: Estimated interest expense relative to free cash flow.
    """
    base = (debt * 0.08) / fcf.replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def cast_012_interest_burden_proxy_rank_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_012_interest_burden_proxy_rank_126d
    ECONOMIC RATIONALE: Estimated interest expense relative to free cash flow.
    """
    base = (debt * 0.08) / fcf.replace(0, 1e-9)
    return _rank_pct(base, 126)

def cast_013_interest_burden_proxy_lvl_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_013_interest_burden_proxy_lvl_252d
    ECONOMIC RATIONALE: Estimated interest expense relative to free cash flow.
    """
    base = (debt * 0.08) / fcf.replace(0, 1e-9)
    return _rolling_mean(base, 252)

def cast_014_interest_burden_proxy_zscore_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_014_interest_burden_proxy_zscore_252d
    ECONOMIC RATIONALE: Estimated interest expense relative to free cash flow.
    """
    base = (debt * 0.08) / fcf.replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def cast_015_interest_burden_proxy_rank_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_015_interest_burden_proxy_rank_252d
    ECONOMIC RATIONALE: Estimated interest expense relative to free cash flow.
    """
    base = (debt * 0.08) / fcf.replace(0, 1e-9)
    return _rank_pct(base, 252)

def cast_016_debt_to_equity_z_lvl_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_016_debt_to_equity_z_lvl_5d
    ECONOMIC RATIONALE: Abnormality of current debt-to-equity ratio.
    """
    base = _zscore_rolling(debt / equity.replace(0, 1e-9), 252)
    return _rolling_mean(base, 5)

def cast_017_debt_to_equity_z_zscore_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_017_debt_to_equity_z_zscore_5d
    ECONOMIC RATIONALE: Abnormality of current debt-to-equity ratio.
    """
    base = _zscore_rolling(debt / equity.replace(0, 1e-9), 252)
    return _zscore_rolling(base, 5)

def cast_018_debt_to_equity_z_rank_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_018_debt_to_equity_z_rank_5d
    ECONOMIC RATIONALE: Abnormality of current debt-to-equity ratio.
    """
    base = _zscore_rolling(debt / equity.replace(0, 1e-9), 252)
    return _rank_pct(base, 5)

def cast_019_debt_to_equity_z_lvl_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_019_debt_to_equity_z_lvl_21d
    ECONOMIC RATIONALE: Abnormality of current debt-to-equity ratio.
    """
    base = _zscore_rolling(debt / equity.replace(0, 1e-9), 252)
    return _rolling_mean(base, 21)

def cast_020_debt_to_equity_z_zscore_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_020_debt_to_equity_z_zscore_21d
    ECONOMIC RATIONALE: Abnormality of current debt-to-equity ratio.
    """
    base = _zscore_rolling(debt / equity.replace(0, 1e-9), 252)
    return _zscore_rolling(base, 21)

def cast_021_debt_to_equity_z_rank_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_021_debt_to_equity_z_rank_21d
    ECONOMIC RATIONALE: Abnormality of current debt-to-equity ratio.
    """
    base = _zscore_rolling(debt / equity.replace(0, 1e-9), 252)
    return _rank_pct(base, 21)

def cast_022_debt_to_equity_z_lvl_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_022_debt_to_equity_z_lvl_63d
    ECONOMIC RATIONALE: Abnormality of current debt-to-equity ratio.
    """
    base = _zscore_rolling(debt / equity.replace(0, 1e-9), 252)
    return _rolling_mean(base, 63)

def cast_023_debt_to_equity_z_zscore_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_023_debt_to_equity_z_zscore_63d
    ECONOMIC RATIONALE: Abnormality of current debt-to-equity ratio.
    """
    base = _zscore_rolling(debt / equity.replace(0, 1e-9), 252)
    return _zscore_rolling(base, 63)

def cast_024_debt_to_equity_z_rank_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_024_debt_to_equity_z_rank_63d
    ECONOMIC RATIONALE: Abnormality of current debt-to-equity ratio.
    """
    base = _zscore_rolling(debt / equity.replace(0, 1e-9), 252)
    return _rank_pct(base, 63)

def cast_025_debt_to_equity_z_lvl_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_025_debt_to_equity_z_lvl_126d
    ECONOMIC RATIONALE: Abnormality of current debt-to-equity ratio.
    """
    base = _zscore_rolling(debt / equity.replace(0, 1e-9), 252)
    return _rolling_mean(base, 126)

def cast_026_debt_to_equity_z_zscore_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_026_debt_to_equity_z_zscore_126d
    ECONOMIC RATIONALE: Abnormality of current debt-to-equity ratio.
    """
    base = _zscore_rolling(debt / equity.replace(0, 1e-9), 252)
    return _zscore_rolling(base, 126)

def cast_027_debt_to_equity_z_rank_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_027_debt_to_equity_z_rank_126d
    ECONOMIC RATIONALE: Abnormality of current debt-to-equity ratio.
    """
    base = _zscore_rolling(debt / equity.replace(0, 1e-9), 252)
    return _rank_pct(base, 126)

def cast_028_debt_to_equity_z_lvl_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_028_debt_to_equity_z_lvl_252d
    ECONOMIC RATIONALE: Abnormality of current debt-to-equity ratio.
    """
    base = _zscore_rolling(debt / equity.replace(0, 1e-9), 252)
    return _rolling_mean(base, 252)

def cast_029_debt_to_equity_z_zscore_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_029_debt_to_equity_z_zscore_252d
    ECONOMIC RATIONALE: Abnormality of current debt-to-equity ratio.
    """
    base = _zscore_rolling(debt / equity.replace(0, 1e-9), 252)
    return _zscore_rolling(base, 252)

def cast_030_debt_to_equity_z_rank_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_030_debt_to_equity_z_rank_252d
    ECONOMIC RATIONALE: Abnormality of current debt-to-equity ratio.
    """
    base = _zscore_rolling(debt / equity.replace(0, 1e-9), 252)
    return _rank_pct(base, 252)

def cast_031_equity_funding_risk_lvl_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_031_equity_funding_risk_lvl_5d
    ECONOMIC RATIONALE: Capacity to raise capital via equity issuance.
    """
    base = marketcap / debt.replace(0, 1e-9)
    return _rolling_mean(base, 5)

def cast_032_equity_funding_risk_zscore_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_032_equity_funding_risk_zscore_5d
    ECONOMIC RATIONALE: Capacity to raise capital via equity issuance.
    """
    base = marketcap / debt.replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def cast_033_equity_funding_risk_rank_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_033_equity_funding_risk_rank_5d
    ECONOMIC RATIONALE: Capacity to raise capital via equity issuance.
    """
    base = marketcap / debt.replace(0, 1e-9)
    return _rank_pct(base, 5)

def cast_034_equity_funding_risk_lvl_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_034_equity_funding_risk_lvl_21d
    ECONOMIC RATIONALE: Capacity to raise capital via equity issuance.
    """
    base = marketcap / debt.replace(0, 1e-9)
    return _rolling_mean(base, 21)

def cast_035_equity_funding_risk_zscore_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_035_equity_funding_risk_zscore_21d
    ECONOMIC RATIONALE: Capacity to raise capital via equity issuance.
    """
    base = marketcap / debt.replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def cast_036_equity_funding_risk_rank_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_036_equity_funding_risk_rank_21d
    ECONOMIC RATIONALE: Capacity to raise capital via equity issuance.
    """
    base = marketcap / debt.replace(0, 1e-9)
    return _rank_pct(base, 21)

def cast_037_equity_funding_risk_lvl_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_037_equity_funding_risk_lvl_63d
    ECONOMIC RATIONALE: Capacity to raise capital via equity issuance.
    """
    base = marketcap / debt.replace(0, 1e-9)
    return _rolling_mean(base, 63)

def cast_038_equity_funding_risk_zscore_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_038_equity_funding_risk_zscore_63d
    ECONOMIC RATIONALE: Capacity to raise capital via equity issuance.
    """
    base = marketcap / debt.replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def cast_039_equity_funding_risk_rank_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_039_equity_funding_risk_rank_63d
    ECONOMIC RATIONALE: Capacity to raise capital via equity issuance.
    """
    base = marketcap / debt.replace(0, 1e-9)
    return _rank_pct(base, 63)

def cast_040_equity_funding_risk_lvl_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_040_equity_funding_risk_lvl_126d
    ECONOMIC RATIONALE: Capacity to raise capital via equity issuance.
    """
    base = marketcap / debt.replace(0, 1e-9)
    return _rolling_mean(base, 126)

def cast_041_equity_funding_risk_zscore_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_041_equity_funding_risk_zscore_126d
    ECONOMIC RATIONALE: Capacity to raise capital via equity issuance.
    """
    base = marketcap / debt.replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def cast_042_equity_funding_risk_rank_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_042_equity_funding_risk_rank_126d
    ECONOMIC RATIONALE: Capacity to raise capital via equity issuance.
    """
    base = marketcap / debt.replace(0, 1e-9)
    return _rank_pct(base, 126)

def cast_043_equity_funding_risk_lvl_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_043_equity_funding_risk_lvl_252d
    ECONOMIC RATIONALE: Capacity to raise capital via equity issuance.
    """
    base = marketcap / debt.replace(0, 1e-9)
    return _rolling_mean(base, 252)

def cast_044_equity_funding_risk_zscore_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_044_equity_funding_risk_zscore_252d
    ECONOMIC RATIONALE: Capacity to raise capital via equity issuance.
    """
    base = marketcap / debt.replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def cast_045_equity_funding_risk_rank_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_045_equity_funding_risk_rank_252d
    ECONOMIC RATIONALE: Capacity to raise capital via equity issuance.
    """
    base = marketcap / debt.replace(0, 1e-9)
    return _rank_pct(base, 252)

def cast_046_debt_acceleration_lvl_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_046_debt_acceleration_lvl_5d
    ECONOMIC RATIONALE: Speed of new debt accumulation.
    """
    base = debt.pct_change(63)
    return _rolling_mean(base, 5)

def cast_047_debt_acceleration_zscore_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_047_debt_acceleration_zscore_5d
    ECONOMIC RATIONALE: Speed of new debt accumulation.
    """
    base = debt.pct_change(63)
    return _zscore_rolling(base, 5)

def cast_048_debt_acceleration_rank_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_048_debt_acceleration_rank_5d
    ECONOMIC RATIONALE: Speed of new debt accumulation.
    """
    base = debt.pct_change(63)
    return _rank_pct(base, 5)

def cast_049_debt_acceleration_lvl_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_049_debt_acceleration_lvl_21d
    ECONOMIC RATIONALE: Speed of new debt accumulation.
    """
    base = debt.pct_change(63)
    return _rolling_mean(base, 21)

def cast_050_debt_acceleration_zscore_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_050_debt_acceleration_zscore_21d
    ECONOMIC RATIONALE: Speed of new debt accumulation.
    """
    base = debt.pct_change(63)
    return _zscore_rolling(base, 21)

def cast_051_debt_acceleration_rank_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_051_debt_acceleration_rank_21d
    ECONOMIC RATIONALE: Speed of new debt accumulation.
    """
    base = debt.pct_change(63)
    return _rank_pct(base, 21)

def cast_052_debt_acceleration_lvl_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_052_debt_acceleration_lvl_63d
    ECONOMIC RATIONALE: Speed of new debt accumulation.
    """
    base = debt.pct_change(63)
    return _rolling_mean(base, 63)

def cast_053_debt_acceleration_zscore_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_053_debt_acceleration_zscore_63d
    ECONOMIC RATIONALE: Speed of new debt accumulation.
    """
    base = debt.pct_change(63)
    return _zscore_rolling(base, 63)

def cast_054_debt_acceleration_rank_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_054_debt_acceleration_rank_63d
    ECONOMIC RATIONALE: Speed of new debt accumulation.
    """
    base = debt.pct_change(63)
    return _rank_pct(base, 63)

def cast_055_debt_acceleration_lvl_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_055_debt_acceleration_lvl_126d
    ECONOMIC RATIONALE: Speed of new debt accumulation.
    """
    base = debt.pct_change(63)
    return _rolling_mean(base, 126)

def cast_056_debt_acceleration_zscore_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_056_debt_acceleration_zscore_126d
    ECONOMIC RATIONALE: Speed of new debt accumulation.
    """
    base = debt.pct_change(63)
    return _zscore_rolling(base, 126)

def cast_057_debt_acceleration_rank_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_057_debt_acceleration_rank_126d
    ECONOMIC RATIONALE: Speed of new debt accumulation.
    """
    base = debt.pct_change(63)
    return _rank_pct(base, 126)

def cast_058_debt_acceleration_lvl_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_058_debt_acceleration_lvl_252d
    ECONOMIC RATIONALE: Speed of new debt accumulation.
    """
    base = debt.pct_change(63)
    return _rolling_mean(base, 252)

def cast_059_debt_acceleration_zscore_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_059_debt_acceleration_zscore_252d
    ECONOMIC RATIONALE: Speed of new debt accumulation.
    """
    base = debt.pct_change(63)
    return _zscore_rolling(base, 252)

def cast_060_debt_acceleration_rank_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_060_debt_acceleration_rank_252d
    ECONOMIC RATIONALE: Speed of new debt accumulation.
    """
    base = debt.pct_change(63)
    return _rank_pct(base, 252)

def cast_061_fcf_debt_service_lvl_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_061_fcf_debt_service_lvl_5d
    ECONOMIC RATIONALE: Ability to amortize debt from cash flow.
    """
    base = fcf / debt.replace(0, 1e-9)
    return _rolling_mean(base, 5)

def cast_062_fcf_debt_service_zscore_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_062_fcf_debt_service_zscore_5d
    ECONOMIC RATIONALE: Ability to amortize debt from cash flow.
    """
    base = fcf / debt.replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def cast_063_fcf_debt_service_rank_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_063_fcf_debt_service_rank_5d
    ECONOMIC RATIONALE: Ability to amortize debt from cash flow.
    """
    base = fcf / debt.replace(0, 1e-9)
    return _rank_pct(base, 5)

def cast_064_fcf_debt_service_lvl_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_064_fcf_debt_service_lvl_21d
    ECONOMIC RATIONALE: Ability to amortize debt from cash flow.
    """
    base = fcf / debt.replace(0, 1e-9)
    return _rolling_mean(base, 21)

def cast_065_fcf_debt_service_zscore_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_065_fcf_debt_service_zscore_21d
    ECONOMIC RATIONALE: Ability to amortize debt from cash flow.
    """
    base = fcf / debt.replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def cast_066_fcf_debt_service_rank_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_066_fcf_debt_service_rank_21d
    ECONOMIC RATIONALE: Ability to amortize debt from cash flow.
    """
    base = fcf / debt.replace(0, 1e-9)
    return _rank_pct(base, 21)

def cast_067_fcf_debt_service_lvl_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_067_fcf_debt_service_lvl_63d
    ECONOMIC RATIONALE: Ability to amortize debt from cash flow.
    """
    base = fcf / debt.replace(0, 1e-9)
    return _rolling_mean(base, 63)

def cast_068_fcf_debt_service_zscore_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_068_fcf_debt_service_zscore_63d
    ECONOMIC RATIONALE: Ability to amortize debt from cash flow.
    """
    base = fcf / debt.replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def cast_069_fcf_debt_service_rank_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_069_fcf_debt_service_rank_63d
    ECONOMIC RATIONALE: Ability to amortize debt from cash flow.
    """
    base = fcf / debt.replace(0, 1e-9)
    return _rank_pct(base, 63)

def cast_070_fcf_debt_service_lvl_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_070_fcf_debt_service_lvl_126d
    ECONOMIC RATIONALE: Ability to amortize debt from cash flow.
    """
    base = fcf / debt.replace(0, 1e-9)
    return _rolling_mean(base, 126)

def cast_071_fcf_debt_service_zscore_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_071_fcf_debt_service_zscore_126d
    ECONOMIC RATIONALE: Ability to amortize debt from cash flow.
    """
    base = fcf / debt.replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def cast_072_fcf_debt_service_rank_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_072_fcf_debt_service_rank_126d
    ECONOMIC RATIONALE: Ability to amortize debt from cash flow.
    """
    base = fcf / debt.replace(0, 1e-9)
    return _rank_pct(base, 126)

def cast_073_fcf_debt_service_lvl_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_073_fcf_debt_service_lvl_252d
    ECONOMIC RATIONALE: Ability to amortize debt from cash flow.
    """
    base = fcf / debt.replace(0, 1e-9)
    return _rolling_mean(base, 252)

def cast_074_fcf_debt_service_zscore_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_074_fcf_debt_service_zscore_252d
    ECONOMIC RATIONALE: Ability to amortize debt from cash flow.
    """
    base = fcf / debt.replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def cast_075_fcf_debt_service_rank_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_075_fcf_debt_service_rank_252d
    ECONOMIC RATIONALE: Ability to amortize debt from cash flow.
    """
    base = fcf / debt.replace(0, 1e-9)
    return _rank_pct(base, 252)

def cast_076_capital_access_score_lvl_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_076_capital_access_score_lvl_5d
    ECONOMIC RATIONALE: Divergence between market valuation and debt growth.
    """
    base = marketcap.pct_change(63) - debt.pct_change(63)
    return _rolling_mean(base, 5)

def cast_077_capital_access_score_zscore_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_077_capital_access_score_zscore_5d
    ECONOMIC RATIONALE: Divergence between market valuation and debt growth.
    """
    base = marketcap.pct_change(63) - debt.pct_change(63)
    return _zscore_rolling(base, 5)

def cast_078_capital_access_score_rank_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_078_capital_access_score_rank_5d
    ECONOMIC RATIONALE: Divergence between market valuation and debt growth.
    """
    base = marketcap.pct_change(63) - debt.pct_change(63)
    return _rank_pct(base, 5)

def cast_079_capital_access_score_lvl_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_079_capital_access_score_lvl_21d
    ECONOMIC RATIONALE: Divergence between market valuation and debt growth.
    """
    base = marketcap.pct_change(63) - debt.pct_change(63)
    return _rolling_mean(base, 21)

def cast_080_capital_access_score_zscore_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_080_capital_access_score_zscore_21d
    ECONOMIC RATIONALE: Divergence between market valuation and debt growth.
    """
    base = marketcap.pct_change(63) - debt.pct_change(63)
    return _zscore_rolling(base, 21)

def cast_081_capital_access_score_rank_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_081_capital_access_score_rank_21d
    ECONOMIC RATIONALE: Divergence between market valuation and debt growth.
    """
    base = marketcap.pct_change(63) - debt.pct_change(63)
    return _rank_pct(base, 21)

def cast_082_capital_access_score_lvl_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_082_capital_access_score_lvl_63d
    ECONOMIC RATIONALE: Divergence between market valuation and debt growth.
    """
    base = marketcap.pct_change(63) - debt.pct_change(63)
    return _rolling_mean(base, 63)

def cast_083_capital_access_score_zscore_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_083_capital_access_score_zscore_63d
    ECONOMIC RATIONALE: Divergence between market valuation and debt growth.
    """
    base = marketcap.pct_change(63) - debt.pct_change(63)
    return _zscore_rolling(base, 63)

def cast_084_capital_access_score_rank_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_084_capital_access_score_rank_63d
    ECONOMIC RATIONALE: Divergence between market valuation and debt growth.
    """
    base = marketcap.pct_change(63) - debt.pct_change(63)
    return _rank_pct(base, 63)

def cast_085_capital_access_score_lvl_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_085_capital_access_score_lvl_126d
    ECONOMIC RATIONALE: Divergence between market valuation and debt growth.
    """
    base = marketcap.pct_change(63) - debt.pct_change(63)
    return _rolling_mean(base, 126)

def cast_086_capital_access_score_zscore_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_086_capital_access_score_zscore_126d
    ECONOMIC RATIONALE: Divergence between market valuation and debt growth.
    """
    base = marketcap.pct_change(63) - debt.pct_change(63)
    return _zscore_rolling(base, 126)

def cast_087_capital_access_score_rank_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_087_capital_access_score_rank_126d
    ECONOMIC RATIONALE: Divergence between market valuation and debt growth.
    """
    base = marketcap.pct_change(63) - debt.pct_change(63)
    return _rank_pct(base, 126)

def cast_088_capital_access_score_lvl_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_088_capital_access_score_lvl_252d
    ECONOMIC RATIONALE: Divergence between market valuation and debt growth.
    """
    base = marketcap.pct_change(63) - debt.pct_change(63)
    return _rolling_mean(base, 252)

def cast_089_capital_access_score_zscore_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_089_capital_access_score_zscore_252d
    ECONOMIC RATIONALE: Divergence between market valuation and debt growth.
    """
    base = marketcap.pct_change(63) - debt.pct_change(63)
    return _zscore_rolling(base, 252)

def cast_090_capital_access_score_rank_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_090_capital_access_score_rank_252d
    ECONOMIC RATIONALE: Divergence between market valuation and debt growth.
    """
    base = marketcap.pct_change(63) - debt.pct_change(63)
    return _rank_pct(base, 252)

def cast_091_debt_drawdown_impact_lvl_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_091_debt_drawdown_impact_lvl_5d
    ECONOMIC RATIONALE: Debt load relative to peak firm value.
    """
    base = debt / marketcap.rolling(252).max().replace(0, 1e-9)
    return _rolling_mean(base, 5)

def cast_092_debt_drawdown_impact_zscore_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_092_debt_drawdown_impact_zscore_5d
    ECONOMIC RATIONALE: Debt load relative to peak firm value.
    """
    base = debt / marketcap.rolling(252).max().replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def cast_093_debt_drawdown_impact_rank_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_093_debt_drawdown_impact_rank_5d
    ECONOMIC RATIONALE: Debt load relative to peak firm value.
    """
    base = debt / marketcap.rolling(252).max().replace(0, 1e-9)
    return _rank_pct(base, 5)

def cast_094_debt_drawdown_impact_lvl_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_094_debt_drawdown_impact_lvl_21d
    ECONOMIC RATIONALE: Debt load relative to peak firm value.
    """
    base = debt / marketcap.rolling(252).max().replace(0, 1e-9)
    return _rolling_mean(base, 21)

def cast_095_debt_drawdown_impact_zscore_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_095_debt_drawdown_impact_zscore_21d
    ECONOMIC RATIONALE: Debt load relative to peak firm value.
    """
    base = debt / marketcap.rolling(252).max().replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def cast_096_debt_drawdown_impact_rank_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_096_debt_drawdown_impact_rank_21d
    ECONOMIC RATIONALE: Debt load relative to peak firm value.
    """
    base = debt / marketcap.rolling(252).max().replace(0, 1e-9)
    return _rank_pct(base, 21)

def cast_097_debt_drawdown_impact_lvl_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_097_debt_drawdown_impact_lvl_63d
    ECONOMIC RATIONALE: Debt load relative to peak firm value.
    """
    base = debt / marketcap.rolling(252).max().replace(0, 1e-9)
    return _rolling_mean(base, 63)

def cast_098_debt_drawdown_impact_zscore_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_098_debt_drawdown_impact_zscore_63d
    ECONOMIC RATIONALE: Debt load relative to peak firm value.
    """
    base = debt / marketcap.rolling(252).max().replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def cast_099_debt_drawdown_impact_rank_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_099_debt_drawdown_impact_rank_63d
    ECONOMIC RATIONALE: Debt load relative to peak firm value.
    """
    base = debt / marketcap.rolling(252).max().replace(0, 1e-9)
    return _rank_pct(base, 63)

def cast_100_debt_drawdown_impact_lvl_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_100_debt_drawdown_impact_lvl_126d
    ECONOMIC RATIONALE: Debt load relative to peak firm value.
    """
    base = debt / marketcap.rolling(252).max().replace(0, 1e-9)
    return _rolling_mean(base, 126)

def cast_101_debt_drawdown_impact_zscore_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_101_debt_drawdown_impact_zscore_126d
    ECONOMIC RATIONALE: Debt load relative to peak firm value.
    """
    base = debt / marketcap.rolling(252).max().replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def cast_102_debt_drawdown_impact_rank_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_102_debt_drawdown_impact_rank_126d
    ECONOMIC RATIONALE: Debt load relative to peak firm value.
    """
    base = debt / marketcap.rolling(252).max().replace(0, 1e-9)
    return _rank_pct(base, 126)

def cast_103_debt_drawdown_impact_lvl_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_103_debt_drawdown_impact_lvl_252d
    ECONOMIC RATIONALE: Debt load relative to peak firm value.
    """
    base = debt / marketcap.rolling(252).max().replace(0, 1e-9)
    return _rolling_mean(base, 252)

def cast_104_debt_drawdown_impact_zscore_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_104_debt_drawdown_impact_zscore_252d
    ECONOMIC RATIONALE: Debt load relative to peak firm value.
    """
    base = debt / marketcap.rolling(252).max().replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def cast_105_debt_drawdown_impact_rank_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_105_debt_drawdown_impact_rank_252d
    ECONOMIC RATIONALE: Debt load relative to peak firm value.
    """
    base = debt / marketcap.rolling(252).max().replace(0, 1e-9)
    return _rank_pct(base, 252)

def cast_106_refinancing_risk_proxy_lvl_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_106_refinancing_risk_proxy_lvl_5d
    ECONOMIC RATIONALE: High risk of inability to refinance maturing debt.
    """
    base = (debt > equity).astype(float) * (marketcap < 100e6).astype(float)
    return _rolling_mean(base, 5)

def cast_107_refinancing_risk_proxy_zscore_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_107_refinancing_risk_proxy_zscore_5d
    ECONOMIC RATIONALE: High risk of inability to refinance maturing debt.
    """
    base = (debt > equity).astype(float) * (marketcap < 100e6).astype(float)
    return _zscore_rolling(base, 5)

def cast_108_refinancing_risk_proxy_rank_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_108_refinancing_risk_proxy_rank_5d
    ECONOMIC RATIONALE: High risk of inability to refinance maturing debt.
    """
    base = (debt > equity).astype(float) * (marketcap < 100e6).astype(float)
    return _rank_pct(base, 5)

def cast_109_refinancing_risk_proxy_lvl_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_109_refinancing_risk_proxy_lvl_21d
    ECONOMIC RATIONALE: High risk of inability to refinance maturing debt.
    """
    base = (debt > equity).astype(float) * (marketcap < 100e6).astype(float)
    return _rolling_mean(base, 21)

def cast_110_refinancing_risk_proxy_zscore_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_110_refinancing_risk_proxy_zscore_21d
    ECONOMIC RATIONALE: High risk of inability to refinance maturing debt.
    """
    base = (debt > equity).astype(float) * (marketcap < 100e6).astype(float)
    return _zscore_rolling(base, 21)

def cast_111_refinancing_risk_proxy_rank_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_111_refinancing_risk_proxy_rank_21d
    ECONOMIC RATIONALE: High risk of inability to refinance maturing debt.
    """
    base = (debt > equity).astype(float) * (marketcap < 100e6).astype(float)
    return _rank_pct(base, 21)

def cast_112_refinancing_risk_proxy_lvl_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_112_refinancing_risk_proxy_lvl_63d
    ECONOMIC RATIONALE: High risk of inability to refinance maturing debt.
    """
    base = (debt > equity).astype(float) * (marketcap < 100e6).astype(float)
    return _rolling_mean(base, 63)

def cast_113_refinancing_risk_proxy_zscore_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_113_refinancing_risk_proxy_zscore_63d
    ECONOMIC RATIONALE: High risk of inability to refinance maturing debt.
    """
    base = (debt > equity).astype(float) * (marketcap < 100e6).astype(float)
    return _zscore_rolling(base, 63)

def cast_114_refinancing_risk_proxy_rank_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_114_refinancing_risk_proxy_rank_63d
    ECONOMIC RATIONALE: High risk of inability to refinance maturing debt.
    """
    base = (debt > equity).astype(float) * (marketcap < 100e6).astype(float)
    return _rank_pct(base, 63)

def cast_115_refinancing_risk_proxy_lvl_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_115_refinancing_risk_proxy_lvl_126d
    ECONOMIC RATIONALE: High risk of inability to refinance maturing debt.
    """
    base = (debt > equity).astype(float) * (marketcap < 100e6).astype(float)
    return _rolling_mean(base, 126)

def cast_116_refinancing_risk_proxy_zscore_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_116_refinancing_risk_proxy_zscore_126d
    ECONOMIC RATIONALE: High risk of inability to refinance maturing debt.
    """
    base = (debt > equity).astype(float) * (marketcap < 100e6).astype(float)
    return _zscore_rolling(base, 126)

def cast_117_refinancing_risk_proxy_rank_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_117_refinancing_risk_proxy_rank_126d
    ECONOMIC RATIONALE: High risk of inability to refinance maturing debt.
    """
    base = (debt > equity).astype(float) * (marketcap < 100e6).astype(float)
    return _rank_pct(base, 126)

def cast_118_refinancing_risk_proxy_lvl_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_118_refinancing_risk_proxy_lvl_252d
    ECONOMIC RATIONALE: High risk of inability to refinance maturing debt.
    """
    base = (debt > equity).astype(float) * (marketcap < 100e6).astype(float)
    return _rolling_mean(base, 252)

def cast_119_refinancing_risk_proxy_zscore_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_119_refinancing_risk_proxy_zscore_252d
    ECONOMIC RATIONALE: High risk of inability to refinance maturing debt.
    """
    base = (debt > equity).astype(float) * (marketcap < 100e6).astype(float)
    return _zscore_rolling(base, 252)

def cast_120_refinancing_risk_proxy_rank_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_120_refinancing_risk_proxy_rank_252d
    ECONOMIC RATIONALE: High risk of inability to refinance maturing debt.
    """
    base = (debt > equity).astype(float) * (marketcap < 100e6).astype(float)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V122_REGISTRY_1 = {
    "cast_001_interest_burden_proxy_lvl_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_001_interest_burden_proxy_lvl_5d},
    "cast_002_interest_burden_proxy_zscore_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_002_interest_burden_proxy_zscore_5d},
    "cast_003_interest_burden_proxy_rank_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_003_interest_burden_proxy_rank_5d},
    "cast_004_interest_burden_proxy_lvl_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_004_interest_burden_proxy_lvl_21d},
    "cast_005_interest_burden_proxy_zscore_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_005_interest_burden_proxy_zscore_21d},
    "cast_006_interest_burden_proxy_rank_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_006_interest_burden_proxy_rank_21d},
    "cast_007_interest_burden_proxy_lvl_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_007_interest_burden_proxy_lvl_63d},
    "cast_008_interest_burden_proxy_zscore_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_008_interest_burden_proxy_zscore_63d},
    "cast_009_interest_burden_proxy_rank_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_009_interest_burden_proxy_rank_63d},
    "cast_010_interest_burden_proxy_lvl_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_010_interest_burden_proxy_lvl_126d},
    "cast_011_interest_burden_proxy_zscore_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_011_interest_burden_proxy_zscore_126d},
    "cast_012_interest_burden_proxy_rank_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_012_interest_burden_proxy_rank_126d},
    "cast_013_interest_burden_proxy_lvl_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_013_interest_burden_proxy_lvl_252d},
    "cast_014_interest_burden_proxy_zscore_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_014_interest_burden_proxy_zscore_252d},
    "cast_015_interest_burden_proxy_rank_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_015_interest_burden_proxy_rank_252d},
    "cast_016_debt_to_equity_z_lvl_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_016_debt_to_equity_z_lvl_5d},
    "cast_017_debt_to_equity_z_zscore_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_017_debt_to_equity_z_zscore_5d},
    "cast_018_debt_to_equity_z_rank_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_018_debt_to_equity_z_rank_5d},
    "cast_019_debt_to_equity_z_lvl_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_019_debt_to_equity_z_lvl_21d},
    "cast_020_debt_to_equity_z_zscore_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_020_debt_to_equity_z_zscore_21d},
    "cast_021_debt_to_equity_z_rank_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_021_debt_to_equity_z_rank_21d},
    "cast_022_debt_to_equity_z_lvl_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_022_debt_to_equity_z_lvl_63d},
    "cast_023_debt_to_equity_z_zscore_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_023_debt_to_equity_z_zscore_63d},
    "cast_024_debt_to_equity_z_rank_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_024_debt_to_equity_z_rank_63d},
    "cast_025_debt_to_equity_z_lvl_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_025_debt_to_equity_z_lvl_126d},
    "cast_026_debt_to_equity_z_zscore_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_026_debt_to_equity_z_zscore_126d},
    "cast_027_debt_to_equity_z_rank_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_027_debt_to_equity_z_rank_126d},
    "cast_028_debt_to_equity_z_lvl_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_028_debt_to_equity_z_lvl_252d},
    "cast_029_debt_to_equity_z_zscore_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_029_debt_to_equity_z_zscore_252d},
    "cast_030_debt_to_equity_z_rank_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_030_debt_to_equity_z_rank_252d},
    "cast_031_equity_funding_risk_lvl_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_031_equity_funding_risk_lvl_5d},
    "cast_032_equity_funding_risk_zscore_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_032_equity_funding_risk_zscore_5d},
    "cast_033_equity_funding_risk_rank_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_033_equity_funding_risk_rank_5d},
    "cast_034_equity_funding_risk_lvl_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_034_equity_funding_risk_lvl_21d},
    "cast_035_equity_funding_risk_zscore_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_035_equity_funding_risk_zscore_21d},
    "cast_036_equity_funding_risk_rank_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_036_equity_funding_risk_rank_21d},
    "cast_037_equity_funding_risk_lvl_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_037_equity_funding_risk_lvl_63d},
    "cast_038_equity_funding_risk_zscore_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_038_equity_funding_risk_zscore_63d},
    "cast_039_equity_funding_risk_rank_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_039_equity_funding_risk_rank_63d},
    "cast_040_equity_funding_risk_lvl_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_040_equity_funding_risk_lvl_126d},
    "cast_041_equity_funding_risk_zscore_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_041_equity_funding_risk_zscore_126d},
    "cast_042_equity_funding_risk_rank_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_042_equity_funding_risk_rank_126d},
    "cast_043_equity_funding_risk_lvl_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_043_equity_funding_risk_lvl_252d},
    "cast_044_equity_funding_risk_zscore_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_044_equity_funding_risk_zscore_252d},
    "cast_045_equity_funding_risk_rank_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_045_equity_funding_risk_rank_252d},
    "cast_046_debt_acceleration_lvl_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_046_debt_acceleration_lvl_5d},
    "cast_047_debt_acceleration_zscore_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_047_debt_acceleration_zscore_5d},
    "cast_048_debt_acceleration_rank_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_048_debt_acceleration_rank_5d},
    "cast_049_debt_acceleration_lvl_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_049_debt_acceleration_lvl_21d},
    "cast_050_debt_acceleration_zscore_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_050_debt_acceleration_zscore_21d},
    "cast_051_debt_acceleration_rank_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_051_debt_acceleration_rank_21d},
    "cast_052_debt_acceleration_lvl_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_052_debt_acceleration_lvl_63d},
    "cast_053_debt_acceleration_zscore_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_053_debt_acceleration_zscore_63d},
    "cast_054_debt_acceleration_rank_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_054_debt_acceleration_rank_63d},
    "cast_055_debt_acceleration_lvl_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_055_debt_acceleration_lvl_126d},
    "cast_056_debt_acceleration_zscore_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_056_debt_acceleration_zscore_126d},
    "cast_057_debt_acceleration_rank_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_057_debt_acceleration_rank_126d},
    "cast_058_debt_acceleration_lvl_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_058_debt_acceleration_lvl_252d},
    "cast_059_debt_acceleration_zscore_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_059_debt_acceleration_zscore_252d},
    "cast_060_debt_acceleration_rank_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_060_debt_acceleration_rank_252d},
    "cast_061_fcf_debt_service_lvl_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_061_fcf_debt_service_lvl_5d},
    "cast_062_fcf_debt_service_zscore_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_062_fcf_debt_service_zscore_5d},
    "cast_063_fcf_debt_service_rank_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_063_fcf_debt_service_rank_5d},
    "cast_064_fcf_debt_service_lvl_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_064_fcf_debt_service_lvl_21d},
    "cast_065_fcf_debt_service_zscore_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_065_fcf_debt_service_zscore_21d},
    "cast_066_fcf_debt_service_rank_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_066_fcf_debt_service_rank_21d},
    "cast_067_fcf_debt_service_lvl_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_067_fcf_debt_service_lvl_63d},
    "cast_068_fcf_debt_service_zscore_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_068_fcf_debt_service_zscore_63d},
    "cast_069_fcf_debt_service_rank_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_069_fcf_debt_service_rank_63d},
    "cast_070_fcf_debt_service_lvl_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_070_fcf_debt_service_lvl_126d},
    "cast_071_fcf_debt_service_zscore_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_071_fcf_debt_service_zscore_126d},
    "cast_072_fcf_debt_service_rank_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_072_fcf_debt_service_rank_126d},
    "cast_073_fcf_debt_service_lvl_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_073_fcf_debt_service_lvl_252d},
    "cast_074_fcf_debt_service_zscore_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_074_fcf_debt_service_zscore_252d},
    "cast_075_fcf_debt_service_rank_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_075_fcf_debt_service_rank_252d},
    "cast_076_capital_access_score_lvl_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_076_capital_access_score_lvl_5d},
    "cast_077_capital_access_score_zscore_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_077_capital_access_score_zscore_5d},
    "cast_078_capital_access_score_rank_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_078_capital_access_score_rank_5d},
    "cast_079_capital_access_score_lvl_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_079_capital_access_score_lvl_21d},
    "cast_080_capital_access_score_zscore_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_080_capital_access_score_zscore_21d},
    "cast_081_capital_access_score_rank_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_081_capital_access_score_rank_21d},
    "cast_082_capital_access_score_lvl_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_082_capital_access_score_lvl_63d},
    "cast_083_capital_access_score_zscore_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_083_capital_access_score_zscore_63d},
    "cast_084_capital_access_score_rank_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_084_capital_access_score_rank_63d},
    "cast_085_capital_access_score_lvl_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_085_capital_access_score_lvl_126d},
    "cast_086_capital_access_score_zscore_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_086_capital_access_score_zscore_126d},
    "cast_087_capital_access_score_rank_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_087_capital_access_score_rank_126d},
    "cast_088_capital_access_score_lvl_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_088_capital_access_score_lvl_252d},
    "cast_089_capital_access_score_zscore_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_089_capital_access_score_zscore_252d},
    "cast_090_capital_access_score_rank_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_090_capital_access_score_rank_252d},
    "cast_091_debt_drawdown_impact_lvl_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_091_debt_drawdown_impact_lvl_5d},
    "cast_092_debt_drawdown_impact_zscore_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_092_debt_drawdown_impact_zscore_5d},
    "cast_093_debt_drawdown_impact_rank_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_093_debt_drawdown_impact_rank_5d},
    "cast_094_debt_drawdown_impact_lvl_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_094_debt_drawdown_impact_lvl_21d},
    "cast_095_debt_drawdown_impact_zscore_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_095_debt_drawdown_impact_zscore_21d},
    "cast_096_debt_drawdown_impact_rank_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_096_debt_drawdown_impact_rank_21d},
    "cast_097_debt_drawdown_impact_lvl_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_097_debt_drawdown_impact_lvl_63d},
    "cast_098_debt_drawdown_impact_zscore_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_098_debt_drawdown_impact_zscore_63d},
    "cast_099_debt_drawdown_impact_rank_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_099_debt_drawdown_impact_rank_63d},
    "cast_100_debt_drawdown_impact_lvl_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_100_debt_drawdown_impact_lvl_126d},
    "cast_101_debt_drawdown_impact_zscore_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_101_debt_drawdown_impact_zscore_126d},
    "cast_102_debt_drawdown_impact_rank_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_102_debt_drawdown_impact_rank_126d},
    "cast_103_debt_drawdown_impact_lvl_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_103_debt_drawdown_impact_lvl_252d},
    "cast_104_debt_drawdown_impact_zscore_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_104_debt_drawdown_impact_zscore_252d},
    "cast_105_debt_drawdown_impact_rank_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_105_debt_drawdown_impact_rank_252d},
    "cast_106_refinancing_risk_proxy_lvl_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_106_refinancing_risk_proxy_lvl_5d},
    "cast_107_refinancing_risk_proxy_zscore_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_107_refinancing_risk_proxy_zscore_5d},
    "cast_108_refinancing_risk_proxy_rank_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_108_refinancing_risk_proxy_rank_5d},
    "cast_109_refinancing_risk_proxy_lvl_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_109_refinancing_risk_proxy_lvl_21d},
    "cast_110_refinancing_risk_proxy_zscore_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_110_refinancing_risk_proxy_zscore_21d},
    "cast_111_refinancing_risk_proxy_rank_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_111_refinancing_risk_proxy_rank_21d},
    "cast_112_refinancing_risk_proxy_lvl_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_112_refinancing_risk_proxy_lvl_63d},
    "cast_113_refinancing_risk_proxy_zscore_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_113_refinancing_risk_proxy_zscore_63d},
    "cast_114_refinancing_risk_proxy_rank_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_114_refinancing_risk_proxy_rank_63d},
    "cast_115_refinancing_risk_proxy_lvl_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_115_refinancing_risk_proxy_lvl_126d},
    "cast_116_refinancing_risk_proxy_zscore_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_116_refinancing_risk_proxy_zscore_126d},
    "cast_117_refinancing_risk_proxy_rank_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_117_refinancing_risk_proxy_rank_126d},
    "cast_118_refinancing_risk_proxy_lvl_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_118_refinancing_risk_proxy_lvl_252d},
    "cast_119_refinancing_risk_proxy_zscore_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_119_refinancing_risk_proxy_zscore_252d},
    "cast_120_refinancing_risk_proxy_rank_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_120_refinancing_risk_proxy_rank_252d},
}
