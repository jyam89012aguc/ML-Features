"""
122_capital_access_stress — Statistical Moments
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

def cast_376_interest_burden_proxy_skew_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_376_interest_burden_proxy_skew_5d
    ECONOMIC RATIONALE: Skewness of interest_burden_proxy over 5d. Estimated interest expense relative to free cash flow.
    """
    return ((debt * 0.08) / fcf.replace(0, 1e-9)).rolling(5).skew()

def cast_377_interest_burden_proxy_kurt_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_377_interest_burden_proxy_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of interest_burden_proxy over 5d. Estimated interest expense relative to free cash flow.
    """
    return ((debt * 0.08) / fcf.replace(0, 1e-9)).rolling(5).kurt()

def cast_378_interest_burden_proxy_skew_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_378_interest_burden_proxy_skew_21d
    ECONOMIC RATIONALE: Skewness of interest_burden_proxy over 21d. Estimated interest expense relative to free cash flow.
    """
    return ((debt * 0.08) / fcf.replace(0, 1e-9)).rolling(21).skew()

def cast_379_interest_burden_proxy_kurt_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_379_interest_burden_proxy_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of interest_burden_proxy over 21d. Estimated interest expense relative to free cash flow.
    """
    return ((debt * 0.08) / fcf.replace(0, 1e-9)).rolling(21).kurt()

def cast_380_interest_burden_proxy_skew_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_380_interest_burden_proxy_skew_63d
    ECONOMIC RATIONALE: Skewness of interest_burden_proxy over 63d. Estimated interest expense relative to free cash flow.
    """
    return ((debt * 0.08) / fcf.replace(0, 1e-9)).rolling(63).skew()

def cast_381_interest_burden_proxy_kurt_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_381_interest_burden_proxy_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of interest_burden_proxy over 63d. Estimated interest expense relative to free cash flow.
    """
    return ((debt * 0.08) / fcf.replace(0, 1e-9)).rolling(63).kurt()

def cast_382_interest_burden_proxy_skew_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_382_interest_burden_proxy_skew_126d
    ECONOMIC RATIONALE: Skewness of interest_burden_proxy over 126d. Estimated interest expense relative to free cash flow.
    """
    return ((debt * 0.08) / fcf.replace(0, 1e-9)).rolling(126).skew()

def cast_383_interest_burden_proxy_kurt_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_383_interest_burden_proxy_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of interest_burden_proxy over 126d. Estimated interest expense relative to free cash flow.
    """
    return ((debt * 0.08) / fcf.replace(0, 1e-9)).rolling(126).kurt()

def cast_384_interest_burden_proxy_skew_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_384_interest_burden_proxy_skew_252d
    ECONOMIC RATIONALE: Skewness of interest_burden_proxy over 252d. Estimated interest expense relative to free cash flow.
    """
    return ((debt * 0.08) / fcf.replace(0, 1e-9)).rolling(252).skew()

def cast_385_interest_burden_proxy_kurt_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_385_interest_burden_proxy_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of interest_burden_proxy over 252d. Estimated interest expense relative to free cash flow.
    """
    return ((debt * 0.08) / fcf.replace(0, 1e-9)).rolling(252).kurt()

def cast_386_debt_to_equity_z_skew_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_386_debt_to_equity_z_skew_5d
    ECONOMIC RATIONALE: Skewness of debt_to_equity_z over 5d. Abnormality of current debt-to-equity ratio.
    """
    return (_zscore_rolling(debt / equity.replace(0, 1e-9), 252)).rolling(5).skew()

def cast_387_debt_to_equity_z_kurt_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_387_debt_to_equity_z_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of debt_to_equity_z over 5d. Abnormality of current debt-to-equity ratio.
    """
    return (_zscore_rolling(debt / equity.replace(0, 1e-9), 252)).rolling(5).kurt()

def cast_388_debt_to_equity_z_skew_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_388_debt_to_equity_z_skew_21d
    ECONOMIC RATIONALE: Skewness of debt_to_equity_z over 21d. Abnormality of current debt-to-equity ratio.
    """
    return (_zscore_rolling(debt / equity.replace(0, 1e-9), 252)).rolling(21).skew()

def cast_389_debt_to_equity_z_kurt_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_389_debt_to_equity_z_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of debt_to_equity_z over 21d. Abnormality of current debt-to-equity ratio.
    """
    return (_zscore_rolling(debt / equity.replace(0, 1e-9), 252)).rolling(21).kurt()

def cast_390_debt_to_equity_z_skew_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_390_debt_to_equity_z_skew_63d
    ECONOMIC RATIONALE: Skewness of debt_to_equity_z over 63d. Abnormality of current debt-to-equity ratio.
    """
    return (_zscore_rolling(debt / equity.replace(0, 1e-9), 252)).rolling(63).skew()

def cast_391_debt_to_equity_z_kurt_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_391_debt_to_equity_z_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of debt_to_equity_z over 63d. Abnormality of current debt-to-equity ratio.
    """
    return (_zscore_rolling(debt / equity.replace(0, 1e-9), 252)).rolling(63).kurt()

def cast_392_debt_to_equity_z_skew_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_392_debt_to_equity_z_skew_126d
    ECONOMIC RATIONALE: Skewness of debt_to_equity_z over 126d. Abnormality of current debt-to-equity ratio.
    """
    return (_zscore_rolling(debt / equity.replace(0, 1e-9), 252)).rolling(126).skew()

def cast_393_debt_to_equity_z_kurt_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_393_debt_to_equity_z_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of debt_to_equity_z over 126d. Abnormality of current debt-to-equity ratio.
    """
    return (_zscore_rolling(debt / equity.replace(0, 1e-9), 252)).rolling(126).kurt()

def cast_394_debt_to_equity_z_skew_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_394_debt_to_equity_z_skew_252d
    ECONOMIC RATIONALE: Skewness of debt_to_equity_z over 252d. Abnormality of current debt-to-equity ratio.
    """
    return (_zscore_rolling(debt / equity.replace(0, 1e-9), 252)).rolling(252).skew()

def cast_395_debt_to_equity_z_kurt_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_395_debt_to_equity_z_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of debt_to_equity_z over 252d. Abnormality of current debt-to-equity ratio.
    """
    return (_zscore_rolling(debt / equity.replace(0, 1e-9), 252)).rolling(252).kurt()

def cast_396_equity_funding_risk_skew_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_396_equity_funding_risk_skew_5d
    ECONOMIC RATIONALE: Skewness of equity_funding_risk over 5d. Capacity to raise capital via equity issuance.
    """
    return (marketcap / debt.replace(0, 1e-9)).rolling(5).skew()

def cast_397_equity_funding_risk_kurt_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_397_equity_funding_risk_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of equity_funding_risk over 5d. Capacity to raise capital via equity issuance.
    """
    return (marketcap / debt.replace(0, 1e-9)).rolling(5).kurt()

def cast_398_equity_funding_risk_skew_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_398_equity_funding_risk_skew_21d
    ECONOMIC RATIONALE: Skewness of equity_funding_risk over 21d. Capacity to raise capital via equity issuance.
    """
    return (marketcap / debt.replace(0, 1e-9)).rolling(21).skew()

def cast_399_equity_funding_risk_kurt_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_399_equity_funding_risk_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of equity_funding_risk over 21d. Capacity to raise capital via equity issuance.
    """
    return (marketcap / debt.replace(0, 1e-9)).rolling(21).kurt()

def cast_400_equity_funding_risk_skew_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_400_equity_funding_risk_skew_63d
    ECONOMIC RATIONALE: Skewness of equity_funding_risk over 63d. Capacity to raise capital via equity issuance.
    """
    return (marketcap / debt.replace(0, 1e-9)).rolling(63).skew()

def cast_401_equity_funding_risk_kurt_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_401_equity_funding_risk_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of equity_funding_risk over 63d. Capacity to raise capital via equity issuance.
    """
    return (marketcap / debt.replace(0, 1e-9)).rolling(63).kurt()

def cast_402_equity_funding_risk_skew_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_402_equity_funding_risk_skew_126d
    ECONOMIC RATIONALE: Skewness of equity_funding_risk over 126d. Capacity to raise capital via equity issuance.
    """
    return (marketcap / debt.replace(0, 1e-9)).rolling(126).skew()

def cast_403_equity_funding_risk_kurt_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_403_equity_funding_risk_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of equity_funding_risk over 126d. Capacity to raise capital via equity issuance.
    """
    return (marketcap / debt.replace(0, 1e-9)).rolling(126).kurt()

def cast_404_equity_funding_risk_skew_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_404_equity_funding_risk_skew_252d
    ECONOMIC RATIONALE: Skewness of equity_funding_risk over 252d. Capacity to raise capital via equity issuance.
    """
    return (marketcap / debt.replace(0, 1e-9)).rolling(252).skew()

def cast_405_equity_funding_risk_kurt_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_405_equity_funding_risk_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of equity_funding_risk over 252d. Capacity to raise capital via equity issuance.
    """
    return (marketcap / debt.replace(0, 1e-9)).rolling(252).kurt()

def cast_406_debt_acceleration_skew_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_406_debt_acceleration_skew_5d
    ECONOMIC RATIONALE: Skewness of debt_acceleration over 5d. Speed of new debt accumulation.
    """
    return (debt.pct_change(63)).rolling(5).skew()

def cast_407_debt_acceleration_kurt_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_407_debt_acceleration_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of debt_acceleration over 5d. Speed of new debt accumulation.
    """
    return (debt.pct_change(63)).rolling(5).kurt()

def cast_408_debt_acceleration_skew_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_408_debt_acceleration_skew_21d
    ECONOMIC RATIONALE: Skewness of debt_acceleration over 21d. Speed of new debt accumulation.
    """
    return (debt.pct_change(63)).rolling(21).skew()

def cast_409_debt_acceleration_kurt_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_409_debt_acceleration_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of debt_acceleration over 21d. Speed of new debt accumulation.
    """
    return (debt.pct_change(63)).rolling(21).kurt()

def cast_410_debt_acceleration_skew_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_410_debt_acceleration_skew_63d
    ECONOMIC RATIONALE: Skewness of debt_acceleration over 63d. Speed of new debt accumulation.
    """
    return (debt.pct_change(63)).rolling(63).skew()

def cast_411_debt_acceleration_kurt_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_411_debt_acceleration_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of debt_acceleration over 63d. Speed of new debt accumulation.
    """
    return (debt.pct_change(63)).rolling(63).kurt()

def cast_412_debt_acceleration_skew_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_412_debt_acceleration_skew_126d
    ECONOMIC RATIONALE: Skewness of debt_acceleration over 126d. Speed of new debt accumulation.
    """
    return (debt.pct_change(63)).rolling(126).skew()

def cast_413_debt_acceleration_kurt_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_413_debt_acceleration_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of debt_acceleration over 126d. Speed of new debt accumulation.
    """
    return (debt.pct_change(63)).rolling(126).kurt()

def cast_414_debt_acceleration_skew_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_414_debt_acceleration_skew_252d
    ECONOMIC RATIONALE: Skewness of debt_acceleration over 252d. Speed of new debt accumulation.
    """
    return (debt.pct_change(63)).rolling(252).skew()

def cast_415_debt_acceleration_kurt_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_415_debt_acceleration_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of debt_acceleration over 252d. Speed of new debt accumulation.
    """
    return (debt.pct_change(63)).rolling(252).kurt()

def cast_416_fcf_debt_service_skew_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_416_fcf_debt_service_skew_5d
    ECONOMIC RATIONALE: Skewness of fcf_debt_service over 5d. Ability to amortize debt from cash flow.
    """
    return (fcf / debt.replace(0, 1e-9)).rolling(5).skew()

def cast_417_fcf_debt_service_kurt_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_417_fcf_debt_service_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of fcf_debt_service over 5d. Ability to amortize debt from cash flow.
    """
    return (fcf / debt.replace(0, 1e-9)).rolling(5).kurt()

def cast_418_fcf_debt_service_skew_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_418_fcf_debt_service_skew_21d
    ECONOMIC RATIONALE: Skewness of fcf_debt_service over 21d. Ability to amortize debt from cash flow.
    """
    return (fcf / debt.replace(0, 1e-9)).rolling(21).skew()

def cast_419_fcf_debt_service_kurt_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_419_fcf_debt_service_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of fcf_debt_service over 21d. Ability to amortize debt from cash flow.
    """
    return (fcf / debt.replace(0, 1e-9)).rolling(21).kurt()

def cast_420_fcf_debt_service_skew_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_420_fcf_debt_service_skew_63d
    ECONOMIC RATIONALE: Skewness of fcf_debt_service over 63d. Ability to amortize debt from cash flow.
    """
    return (fcf / debt.replace(0, 1e-9)).rolling(63).skew()

def cast_421_fcf_debt_service_kurt_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_421_fcf_debt_service_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of fcf_debt_service over 63d. Ability to amortize debt from cash flow.
    """
    return (fcf / debt.replace(0, 1e-9)).rolling(63).kurt()

def cast_422_fcf_debt_service_skew_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_422_fcf_debt_service_skew_126d
    ECONOMIC RATIONALE: Skewness of fcf_debt_service over 126d. Ability to amortize debt from cash flow.
    """
    return (fcf / debt.replace(0, 1e-9)).rolling(126).skew()

def cast_423_fcf_debt_service_kurt_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_423_fcf_debt_service_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of fcf_debt_service over 126d. Ability to amortize debt from cash flow.
    """
    return (fcf / debt.replace(0, 1e-9)).rolling(126).kurt()

def cast_424_fcf_debt_service_skew_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_424_fcf_debt_service_skew_252d
    ECONOMIC RATIONALE: Skewness of fcf_debt_service over 252d. Ability to amortize debt from cash flow.
    """
    return (fcf / debt.replace(0, 1e-9)).rolling(252).skew()

def cast_425_fcf_debt_service_kurt_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_425_fcf_debt_service_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of fcf_debt_service over 252d. Ability to amortize debt from cash flow.
    """
    return (fcf / debt.replace(0, 1e-9)).rolling(252).kurt()

def cast_426_capital_access_score_skew_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_426_capital_access_score_skew_5d
    ECONOMIC RATIONALE: Skewness of capital_access_score over 5d. Divergence between market valuation and debt growth.
    """
    return (marketcap.pct_change(63) - debt.pct_change(63)).rolling(5).skew()

def cast_427_capital_access_score_kurt_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_427_capital_access_score_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of capital_access_score over 5d. Divergence between market valuation and debt growth.
    """
    return (marketcap.pct_change(63) - debt.pct_change(63)).rolling(5).kurt()

def cast_428_capital_access_score_skew_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_428_capital_access_score_skew_21d
    ECONOMIC RATIONALE: Skewness of capital_access_score over 21d. Divergence between market valuation and debt growth.
    """
    return (marketcap.pct_change(63) - debt.pct_change(63)).rolling(21).skew()

def cast_429_capital_access_score_kurt_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_429_capital_access_score_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of capital_access_score over 21d. Divergence between market valuation and debt growth.
    """
    return (marketcap.pct_change(63) - debt.pct_change(63)).rolling(21).kurt()

def cast_430_capital_access_score_skew_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_430_capital_access_score_skew_63d
    ECONOMIC RATIONALE: Skewness of capital_access_score over 63d. Divergence between market valuation and debt growth.
    """
    return (marketcap.pct_change(63) - debt.pct_change(63)).rolling(63).skew()

def cast_431_capital_access_score_kurt_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_431_capital_access_score_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of capital_access_score over 63d. Divergence between market valuation and debt growth.
    """
    return (marketcap.pct_change(63) - debt.pct_change(63)).rolling(63).kurt()

def cast_432_capital_access_score_skew_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_432_capital_access_score_skew_126d
    ECONOMIC RATIONALE: Skewness of capital_access_score over 126d. Divergence between market valuation and debt growth.
    """
    return (marketcap.pct_change(63) - debt.pct_change(63)).rolling(126).skew()

def cast_433_capital_access_score_kurt_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_433_capital_access_score_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of capital_access_score over 126d. Divergence between market valuation and debt growth.
    """
    return (marketcap.pct_change(63) - debt.pct_change(63)).rolling(126).kurt()

def cast_434_capital_access_score_skew_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_434_capital_access_score_skew_252d
    ECONOMIC RATIONALE: Skewness of capital_access_score over 252d. Divergence between market valuation and debt growth.
    """
    return (marketcap.pct_change(63) - debt.pct_change(63)).rolling(252).skew()

def cast_435_capital_access_score_kurt_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_435_capital_access_score_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of capital_access_score over 252d. Divergence between market valuation and debt growth.
    """
    return (marketcap.pct_change(63) - debt.pct_change(63)).rolling(252).kurt()

def cast_436_debt_drawdown_impact_skew_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_436_debt_drawdown_impact_skew_5d
    ECONOMIC RATIONALE: Skewness of debt_drawdown_impact over 5d. Debt load relative to peak firm value.
    """
    return (debt / marketcap.rolling(252).max().replace(0, 1e-9)).rolling(5).skew()

def cast_437_debt_drawdown_impact_kurt_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_437_debt_drawdown_impact_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of debt_drawdown_impact over 5d. Debt load relative to peak firm value.
    """
    return (debt / marketcap.rolling(252).max().replace(0, 1e-9)).rolling(5).kurt()

def cast_438_debt_drawdown_impact_skew_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_438_debt_drawdown_impact_skew_21d
    ECONOMIC RATIONALE: Skewness of debt_drawdown_impact over 21d. Debt load relative to peak firm value.
    """
    return (debt / marketcap.rolling(252).max().replace(0, 1e-9)).rolling(21).skew()

def cast_439_debt_drawdown_impact_kurt_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_439_debt_drawdown_impact_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of debt_drawdown_impact over 21d. Debt load relative to peak firm value.
    """
    return (debt / marketcap.rolling(252).max().replace(0, 1e-9)).rolling(21).kurt()

def cast_440_debt_drawdown_impact_skew_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_440_debt_drawdown_impact_skew_63d
    ECONOMIC RATIONALE: Skewness of debt_drawdown_impact over 63d. Debt load relative to peak firm value.
    """
    return (debt / marketcap.rolling(252).max().replace(0, 1e-9)).rolling(63).skew()

def cast_441_debt_drawdown_impact_kurt_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_441_debt_drawdown_impact_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of debt_drawdown_impact over 63d. Debt load relative to peak firm value.
    """
    return (debt / marketcap.rolling(252).max().replace(0, 1e-9)).rolling(63).kurt()

def cast_442_debt_drawdown_impact_skew_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_442_debt_drawdown_impact_skew_126d
    ECONOMIC RATIONALE: Skewness of debt_drawdown_impact over 126d. Debt load relative to peak firm value.
    """
    return (debt / marketcap.rolling(252).max().replace(0, 1e-9)).rolling(126).skew()

def cast_443_debt_drawdown_impact_kurt_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_443_debt_drawdown_impact_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of debt_drawdown_impact over 126d. Debt load relative to peak firm value.
    """
    return (debt / marketcap.rolling(252).max().replace(0, 1e-9)).rolling(126).kurt()

def cast_444_debt_drawdown_impact_skew_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_444_debt_drawdown_impact_skew_252d
    ECONOMIC RATIONALE: Skewness of debt_drawdown_impact over 252d. Debt load relative to peak firm value.
    """
    return (debt / marketcap.rolling(252).max().replace(0, 1e-9)).rolling(252).skew()

def cast_445_debt_drawdown_impact_kurt_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_445_debt_drawdown_impact_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of debt_drawdown_impact over 252d. Debt load relative to peak firm value.
    """
    return (debt / marketcap.rolling(252).max().replace(0, 1e-9)).rolling(252).kurt()

def cast_446_refinancing_risk_proxy_skew_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_446_refinancing_risk_proxy_skew_5d
    ECONOMIC RATIONALE: Skewness of refinancing_risk_proxy over 5d. High risk of inability to refinance maturing debt.
    """
    return ((debt > equity).astype(float) * (marketcap < 100e6).astype(float)).rolling(5).skew()

def cast_447_refinancing_risk_proxy_kurt_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_447_refinancing_risk_proxy_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of refinancing_risk_proxy over 5d. High risk of inability to refinance maturing debt.
    """
    return ((debt > equity).astype(float) * (marketcap < 100e6).astype(float)).rolling(5).kurt()

def cast_448_refinancing_risk_proxy_skew_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_448_refinancing_risk_proxy_skew_21d
    ECONOMIC RATIONALE: Skewness of refinancing_risk_proxy over 21d. High risk of inability to refinance maturing debt.
    """
    return ((debt > equity).astype(float) * (marketcap < 100e6).astype(float)).rolling(21).skew()

def cast_449_refinancing_risk_proxy_kurt_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_449_refinancing_risk_proxy_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of refinancing_risk_proxy over 21d. High risk of inability to refinance maturing debt.
    """
    return ((debt > equity).astype(float) * (marketcap < 100e6).astype(float)).rolling(21).kurt()

def cast_450_refinancing_risk_proxy_skew_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_450_refinancing_risk_proxy_skew_63d
    ECONOMIC RATIONALE: Skewness of refinancing_risk_proxy over 63d. High risk of inability to refinance maturing debt.
    """
    return ((debt > equity).astype(float) * (marketcap < 100e6).astype(float)).rolling(63).skew()

def cast_451_refinancing_risk_proxy_kurt_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_451_refinancing_risk_proxy_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of refinancing_risk_proxy over 63d. High risk of inability to refinance maturing debt.
    """
    return ((debt > equity).astype(float) * (marketcap < 100e6).astype(float)).rolling(63).kurt()

def cast_452_refinancing_risk_proxy_skew_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_452_refinancing_risk_proxy_skew_126d
    ECONOMIC RATIONALE: Skewness of refinancing_risk_proxy over 126d. High risk of inability to refinance maturing debt.
    """
    return ((debt > equity).astype(float) * (marketcap < 100e6).astype(float)).rolling(126).skew()

def cast_453_refinancing_risk_proxy_kurt_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_453_refinancing_risk_proxy_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of refinancing_risk_proxy over 126d. High risk of inability to refinance maturing debt.
    """
    return ((debt > equity).astype(float) * (marketcap < 100e6).astype(float)).rolling(126).kurt()

def cast_454_refinancing_risk_proxy_skew_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_454_refinancing_risk_proxy_skew_252d
    ECONOMIC RATIONALE: Skewness of refinancing_risk_proxy over 252d. High risk of inability to refinance maturing debt.
    """
    return ((debt > equity).astype(float) * (marketcap < 100e6).astype(float)).rolling(252).skew()

def cast_455_refinancing_risk_proxy_kurt_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_455_refinancing_risk_proxy_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of refinancing_risk_proxy over 252d. High risk of inability to refinance maturing debt.
    """
    return ((debt > equity).astype(float) * (marketcap < 100e6).astype(float)).rolling(252).kurt()

def cast_456_debt_to_assets_momentum_skew_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_456_debt_to_assets_momentum_skew_5d
    ECONOMIC RATIONALE: Skewness of debt_to_assets_momentum over 5d. Trend in the proportion of assets funded by debt.
    """
    return ((debt/assets).diff(63)).rolling(5).skew()

def cast_457_debt_to_assets_momentum_kurt_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_457_debt_to_assets_momentum_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of debt_to_assets_momentum over 5d. Trend in the proportion of assets funded by debt.
    """
    return ((debt/assets).diff(63)).rolling(5).kurt()

def cast_458_debt_to_assets_momentum_skew_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_458_debt_to_assets_momentum_skew_21d
    ECONOMIC RATIONALE: Skewness of debt_to_assets_momentum over 21d. Trend in the proportion of assets funded by debt.
    """
    return ((debt/assets).diff(63)).rolling(21).skew()

def cast_459_debt_to_assets_momentum_kurt_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_459_debt_to_assets_momentum_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of debt_to_assets_momentum over 21d. Trend in the proportion of assets funded by debt.
    """
    return ((debt/assets).diff(63)).rolling(21).kurt()

def cast_460_debt_to_assets_momentum_skew_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_460_debt_to_assets_momentum_skew_63d
    ECONOMIC RATIONALE: Skewness of debt_to_assets_momentum over 63d. Trend in the proportion of assets funded by debt.
    """
    return ((debt/assets).diff(63)).rolling(63).skew()

def cast_461_debt_to_assets_momentum_kurt_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_461_debt_to_assets_momentum_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of debt_to_assets_momentum over 63d. Trend in the proportion of assets funded by debt.
    """
    return ((debt/assets).diff(63)).rolling(63).kurt()

def cast_462_debt_to_assets_momentum_skew_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_462_debt_to_assets_momentum_skew_126d
    ECONOMIC RATIONALE: Skewness of debt_to_assets_momentum over 126d. Trend in the proportion of assets funded by debt.
    """
    return ((debt/assets).diff(63)).rolling(126).skew()

def cast_463_debt_to_assets_momentum_kurt_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_463_debt_to_assets_momentum_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of debt_to_assets_momentum over 126d. Trend in the proportion of assets funded by debt.
    """
    return ((debt/assets).diff(63)).rolling(126).kurt()

def cast_464_debt_to_assets_momentum_skew_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_464_debt_to_assets_momentum_skew_252d
    ECONOMIC RATIONALE: Skewness of debt_to_assets_momentum over 252d. Trend in the proportion of assets funded by debt.
    """
    return ((debt/assets).diff(63)).rolling(252).skew()

def cast_465_debt_to_assets_momentum_kurt_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_465_debt_to_assets_momentum_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of debt_to_assets_momentum over 252d. Trend in the proportion of assets funded by debt.
    """
    return ((debt/assets).diff(63)).rolling(252).kurt()

def cast_466_fcf_yield_vs_debt_skew_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_466_fcf_yield_vs_debt_skew_5d
    ECONOMIC RATIONALE: Skewness of fcf_yield_vs_debt over 5d. Cash flow yield net of debt-to-cap ratio.
    """
    return ((fcf/marketcap) - (debt/marketcap)).rolling(5).skew()

def cast_467_fcf_yield_vs_debt_kurt_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_467_fcf_yield_vs_debt_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of fcf_yield_vs_debt over 5d. Cash flow yield net of debt-to-cap ratio.
    """
    return ((fcf/marketcap) - (debt/marketcap)).rolling(5).kurt()

def cast_468_fcf_yield_vs_debt_skew_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_468_fcf_yield_vs_debt_skew_21d
    ECONOMIC RATIONALE: Skewness of fcf_yield_vs_debt over 21d. Cash flow yield net of debt-to-cap ratio.
    """
    return ((fcf/marketcap) - (debt/marketcap)).rolling(21).skew()

def cast_469_fcf_yield_vs_debt_kurt_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_469_fcf_yield_vs_debt_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of fcf_yield_vs_debt over 21d. Cash flow yield net of debt-to-cap ratio.
    """
    return ((fcf/marketcap) - (debt/marketcap)).rolling(21).kurt()

def cast_470_fcf_yield_vs_debt_skew_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_470_fcf_yield_vs_debt_skew_63d
    ECONOMIC RATIONALE: Skewness of fcf_yield_vs_debt over 63d. Cash flow yield net of debt-to-cap ratio.
    """
    return ((fcf/marketcap) - (debt/marketcap)).rolling(63).skew()

def cast_471_fcf_yield_vs_debt_kurt_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_471_fcf_yield_vs_debt_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of fcf_yield_vs_debt over 63d. Cash flow yield net of debt-to-cap ratio.
    """
    return ((fcf/marketcap) - (debt/marketcap)).rolling(63).kurt()

def cast_472_fcf_yield_vs_debt_skew_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_472_fcf_yield_vs_debt_skew_126d
    ECONOMIC RATIONALE: Skewness of fcf_yield_vs_debt over 126d. Cash flow yield net of debt-to-cap ratio.
    """
    return ((fcf/marketcap) - (debt/marketcap)).rolling(126).skew()

def cast_473_fcf_yield_vs_debt_kurt_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_473_fcf_yield_vs_debt_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of fcf_yield_vs_debt over 126d. Cash flow yield net of debt-to-cap ratio.
    """
    return ((fcf/marketcap) - (debt/marketcap)).rolling(126).kurt()

def cast_474_fcf_yield_vs_debt_skew_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_474_fcf_yield_vs_debt_skew_252d
    ECONOMIC RATIONALE: Skewness of fcf_yield_vs_debt over 252d. Cash flow yield net of debt-to-cap ratio.
    """
    return ((fcf/marketcap) - (debt/marketcap)).rolling(252).skew()

def cast_475_fcf_yield_vs_debt_kurt_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_475_fcf_yield_vs_debt_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of fcf_yield_vs_debt over 252d. Cash flow yield net of debt-to-cap ratio.
    """
    return ((fcf/marketcap) - (debt/marketcap)).rolling(252).kurt()

def cast_476_capital_structure_z_skew_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_476_capital_structure_z_skew_5d
    ECONOMIC RATIONALE: Skewness of capital_structure_z over 5d. Z-score of debt within the capital structure.
    """
    return (_zscore_rolling(debt/(debt+equity).replace(0, 1e-9), 252)).rolling(5).skew()

def cast_477_capital_structure_z_kurt_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_477_capital_structure_z_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of capital_structure_z over 5d. Z-score of debt within the capital structure.
    """
    return (_zscore_rolling(debt/(debt+equity).replace(0, 1e-9), 252)).rolling(5).kurt()

def cast_478_capital_structure_z_skew_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_478_capital_structure_z_skew_21d
    ECONOMIC RATIONALE: Skewness of capital_structure_z over 21d. Z-score of debt within the capital structure.
    """
    return (_zscore_rolling(debt/(debt+equity).replace(0, 1e-9), 252)).rolling(21).skew()

def cast_479_capital_structure_z_kurt_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_479_capital_structure_z_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of capital_structure_z over 21d. Z-score of debt within the capital structure.
    """
    return (_zscore_rolling(debt/(debt+equity).replace(0, 1e-9), 252)).rolling(21).kurt()

def cast_480_capital_structure_z_skew_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_480_capital_structure_z_skew_63d
    ECONOMIC RATIONALE: Skewness of capital_structure_z over 63d. Z-score of debt within the capital structure.
    """
    return (_zscore_rolling(debt/(debt+equity).replace(0, 1e-9), 252)).rolling(63).skew()

def cast_481_capital_structure_z_kurt_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_481_capital_structure_z_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of capital_structure_z over 63d. Z-score of debt within the capital structure.
    """
    return (_zscore_rolling(debt/(debt+equity).replace(0, 1e-9), 252)).rolling(63).kurt()

def cast_482_capital_structure_z_skew_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_482_capital_structure_z_skew_126d
    ECONOMIC RATIONALE: Skewness of capital_structure_z over 126d. Z-score of debt within the capital structure.
    """
    return (_zscore_rolling(debt/(debt+equity).replace(0, 1e-9), 252)).rolling(126).skew()

def cast_483_capital_structure_z_kurt_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_483_capital_structure_z_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of capital_structure_z over 126d. Z-score of debt within the capital structure.
    """
    return (_zscore_rolling(debt/(debt+equity).replace(0, 1e-9), 252)).rolling(126).kurt()

def cast_484_capital_structure_z_skew_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_484_capital_structure_z_skew_252d
    ECONOMIC RATIONALE: Skewness of capital_structure_z over 252d. Z-score of debt within the capital structure.
    """
    return (_zscore_rolling(debt/(debt+equity).replace(0, 1e-9), 252)).rolling(252).skew()

def cast_485_capital_structure_z_kurt_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_485_capital_structure_z_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of capital_structure_z over 252d. Z-score of debt within the capital structure.
    """
    return (_zscore_rolling(debt/(debt+equity).replace(0, 1e-9), 252)).rolling(252).kurt()

def cast_486_equity_value_erosion_skew_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_486_equity_value_erosion_skew_5d
    ECONOMIC RATIONALE: Skewness of equity_value_erosion over 5d. Destruction of book value relative to market price.
    """
    return (equity.diff(252) / marketcap.replace(0, 1e-9)).rolling(5).skew()

def cast_487_equity_value_erosion_kurt_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_487_equity_value_erosion_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of equity_value_erosion over 5d. Destruction of book value relative to market price.
    """
    return (equity.diff(252) / marketcap.replace(0, 1e-9)).rolling(5).kurt()

def cast_488_equity_value_erosion_skew_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_488_equity_value_erosion_skew_21d
    ECONOMIC RATIONALE: Skewness of equity_value_erosion over 21d. Destruction of book value relative to market price.
    """
    return (equity.diff(252) / marketcap.replace(0, 1e-9)).rolling(21).skew()

def cast_489_equity_value_erosion_kurt_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_489_equity_value_erosion_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of equity_value_erosion over 21d. Destruction of book value relative to market price.
    """
    return (equity.diff(252) / marketcap.replace(0, 1e-9)).rolling(21).kurt()

def cast_490_equity_value_erosion_skew_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_490_equity_value_erosion_skew_63d
    ECONOMIC RATIONALE: Skewness of equity_value_erosion over 63d. Destruction of book value relative to market price.
    """
    return (equity.diff(252) / marketcap.replace(0, 1e-9)).rolling(63).skew()

def cast_491_equity_value_erosion_kurt_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_491_equity_value_erosion_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of equity_value_erosion over 63d. Destruction of book value relative to market price.
    """
    return (equity.diff(252) / marketcap.replace(0, 1e-9)).rolling(63).kurt()

def cast_492_equity_value_erosion_skew_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_492_equity_value_erosion_skew_126d
    ECONOMIC RATIONALE: Skewness of equity_value_erosion over 126d. Destruction of book value relative to market price.
    """
    return (equity.diff(252) / marketcap.replace(0, 1e-9)).rolling(126).skew()

def cast_493_equity_value_erosion_kurt_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_493_equity_value_erosion_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of equity_value_erosion over 126d. Destruction of book value relative to market price.
    """
    return (equity.diff(252) / marketcap.replace(0, 1e-9)).rolling(126).kurt()

def cast_494_equity_value_erosion_skew_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_494_equity_value_erosion_skew_252d
    ECONOMIC RATIONALE: Skewness of equity_value_erosion over 252d. Destruction of book value relative to market price.
    """
    return (equity.diff(252) / marketcap.replace(0, 1e-9)).rolling(252).skew()

def cast_495_equity_value_erosion_kurt_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_495_equity_value_erosion_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of equity_value_erosion over 252d. Destruction of book value relative to market price.
    """
    return (equity.diff(252) / marketcap.replace(0, 1e-9)).rolling(252).kurt()

def cast_496_debt_burden_vol_skew_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_496_debt_burden_vol_skew_5d
    ECONOMIC RATIONALE: Skewness of debt_burden_vol over 5d. Price volatility amplified by debt-to-market-cap ratio.
    """
    return (close.rolling(21).std() * (debt/marketcap.replace(0, 1e-9))).rolling(5).skew()

def cast_497_debt_burden_vol_kurt_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_497_debt_burden_vol_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of debt_burden_vol over 5d. Price volatility amplified by debt-to-market-cap ratio.
    """
    return (close.rolling(21).std() * (debt/marketcap.replace(0, 1e-9))).rolling(5).kurt()

def cast_498_debt_burden_vol_skew_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_498_debt_burden_vol_skew_21d
    ECONOMIC RATIONALE: Skewness of debt_burden_vol over 21d. Price volatility amplified by debt-to-market-cap ratio.
    """
    return (close.rolling(21).std() * (debt/marketcap.replace(0, 1e-9))).rolling(21).skew()

def cast_499_debt_burden_vol_kurt_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_499_debt_burden_vol_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of debt_burden_vol over 21d. Price volatility amplified by debt-to-market-cap ratio.
    """
    return (close.rolling(21).std() * (debt/marketcap.replace(0, 1e-9))).rolling(21).kurt()

def cast_500_debt_burden_vol_skew_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_500_debt_burden_vol_skew_63d
    ECONOMIC RATIONALE: Skewness of debt_burden_vol over 63d. Price volatility amplified by debt-to-market-cap ratio.
    """
    return (close.rolling(21).std() * (debt/marketcap.replace(0, 1e-9))).rolling(63).skew()

def cast_501_debt_burden_vol_kurt_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_501_debt_burden_vol_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of debt_burden_vol over 63d. Price volatility amplified by debt-to-market-cap ratio.
    """
    return (close.rolling(21).std() * (debt/marketcap.replace(0, 1e-9))).rolling(63).kurt()

def cast_502_debt_burden_vol_skew_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_502_debt_burden_vol_skew_126d
    ECONOMIC RATIONALE: Skewness of debt_burden_vol over 126d. Price volatility amplified by debt-to-market-cap ratio.
    """
    return (close.rolling(21).std() * (debt/marketcap.replace(0, 1e-9))).rolling(126).skew()

def cast_503_debt_burden_vol_kurt_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_503_debt_burden_vol_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of debt_burden_vol over 126d. Price volatility amplified by debt-to-market-cap ratio.
    """
    return (close.rolling(21).std() * (debt/marketcap.replace(0, 1e-9))).rolling(126).kurt()

def cast_504_debt_burden_vol_skew_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_504_debt_burden_vol_skew_252d
    ECONOMIC RATIONALE: Skewness of debt_burden_vol over 252d. Price volatility amplified by debt-to-market-cap ratio.
    """
    return (close.rolling(21).std() * (debt/marketcap.replace(0, 1e-9))).rolling(252).skew()

def cast_505_debt_burden_vol_kurt_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_505_debt_burden_vol_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of debt_burden_vol over 252d. Price volatility amplified by debt-to-market-cap ratio.
    """
    return (close.rolling(21).std() * (debt/marketcap.replace(0, 1e-9))).rolling(252).kurt()

def cast_506_capital_stress_index_skew_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_506_capital_stress_index_skew_5d
    ECONOMIC RATIONALE: Skewness of capital_stress_index over 5d. Debt growth relative to cash flow capacity.
    """
    return (debt.pct_change(21) / fcf.rolling(63).mean().abs().replace(0, 1e-9)).rolling(5).skew()

def cast_507_capital_stress_index_kurt_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_507_capital_stress_index_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of capital_stress_index over 5d. Debt growth relative to cash flow capacity.
    """
    return (debt.pct_change(21) / fcf.rolling(63).mean().abs().replace(0, 1e-9)).rolling(5).kurt()

def cast_508_capital_stress_index_skew_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_508_capital_stress_index_skew_21d
    ECONOMIC RATIONALE: Skewness of capital_stress_index over 21d. Debt growth relative to cash flow capacity.
    """
    return (debt.pct_change(21) / fcf.rolling(63).mean().abs().replace(0, 1e-9)).rolling(21).skew()

def cast_509_capital_stress_index_kurt_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_509_capital_stress_index_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of capital_stress_index over 21d. Debt growth relative to cash flow capacity.
    """
    return (debt.pct_change(21) / fcf.rolling(63).mean().abs().replace(0, 1e-9)).rolling(21).kurt()

def cast_510_capital_stress_index_skew_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_510_capital_stress_index_skew_63d
    ECONOMIC RATIONALE: Skewness of capital_stress_index over 63d. Debt growth relative to cash flow capacity.
    """
    return (debt.pct_change(21) / fcf.rolling(63).mean().abs().replace(0, 1e-9)).rolling(63).skew()

def cast_511_capital_stress_index_kurt_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_511_capital_stress_index_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of capital_stress_index over 63d. Debt growth relative to cash flow capacity.
    """
    return (debt.pct_change(21) / fcf.rolling(63).mean().abs().replace(0, 1e-9)).rolling(63).kurt()

def cast_512_capital_stress_index_skew_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_512_capital_stress_index_skew_126d
    ECONOMIC RATIONALE: Skewness of capital_stress_index over 126d. Debt growth relative to cash flow capacity.
    """
    return (debt.pct_change(21) / fcf.rolling(63).mean().abs().replace(0, 1e-9)).rolling(126).skew()

def cast_513_capital_stress_index_kurt_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_513_capital_stress_index_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of capital_stress_index over 126d. Debt growth relative to cash flow capacity.
    """
    return (debt.pct_change(21) / fcf.rolling(63).mean().abs().replace(0, 1e-9)).rolling(126).kurt()

def cast_514_capital_stress_index_skew_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_514_capital_stress_index_skew_252d
    ECONOMIC RATIONALE: Skewness of capital_stress_index over 252d. Debt growth relative to cash flow capacity.
    """
    return (debt.pct_change(21) / fcf.rolling(63).mean().abs().replace(0, 1e-9)).rolling(252).skew()

def cast_515_capital_stress_index_kurt_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_515_capital_stress_index_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of capital_stress_index over 252d. Debt growth relative to cash flow capacity.
    """
    return (debt.pct_change(21) / fcf.rolling(63).mean().abs().replace(0, 1e-9)).rolling(252).kurt()

def cast_516_solvency_cushion_skew_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_516_solvency_cushion_skew_5d
    ECONOMIC RATIONALE: Skewness of solvency_cushion over 5d. Proportion of assets funded by shareholders.
    """
    return (equity / assets.replace(0, 1e-9)).rolling(5).skew()

def cast_517_solvency_cushion_kurt_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_517_solvency_cushion_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of solvency_cushion over 5d. Proportion of assets funded by shareholders.
    """
    return (equity / assets.replace(0, 1e-9)).rolling(5).kurt()

def cast_518_solvency_cushion_skew_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_518_solvency_cushion_skew_21d
    ECONOMIC RATIONALE: Skewness of solvency_cushion over 21d. Proportion of assets funded by shareholders.
    """
    return (equity / assets.replace(0, 1e-9)).rolling(21).skew()

def cast_519_solvency_cushion_kurt_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_519_solvency_cushion_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of solvency_cushion over 21d. Proportion of assets funded by shareholders.
    """
    return (equity / assets.replace(0, 1e-9)).rolling(21).kurt()

def cast_520_solvency_cushion_skew_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_520_solvency_cushion_skew_63d
    ECONOMIC RATIONALE: Skewness of solvency_cushion over 63d. Proportion of assets funded by shareholders.
    """
    return (equity / assets.replace(0, 1e-9)).rolling(63).skew()

def cast_521_solvency_cushion_kurt_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_521_solvency_cushion_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of solvency_cushion over 63d. Proportion of assets funded by shareholders.
    """
    return (equity / assets.replace(0, 1e-9)).rolling(63).kurt()

def cast_522_solvency_cushion_skew_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_522_solvency_cushion_skew_126d
    ECONOMIC RATIONALE: Skewness of solvency_cushion over 126d. Proportion of assets funded by shareholders.
    """
    return (equity / assets.replace(0, 1e-9)).rolling(126).skew()

def cast_523_solvency_cushion_kurt_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_523_solvency_cushion_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of solvency_cushion over 126d. Proportion of assets funded by shareholders.
    """
    return (equity / assets.replace(0, 1e-9)).rolling(126).kurt()

def cast_524_solvency_cushion_skew_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_524_solvency_cushion_skew_252d
    ECONOMIC RATIONALE: Skewness of solvency_cushion over 252d. Proportion of assets funded by shareholders.
    """
    return (equity / assets.replace(0, 1e-9)).rolling(252).skew()

def cast_525_solvency_cushion_kurt_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_525_solvency_cushion_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of solvency_cushion over 252d. Proportion of assets funded by shareholders.
    """
    return (equity / assets.replace(0, 1e-9)).rolling(252).kurt()

# ── Registry ──────────────────────────────────────────────────────────────────
V122_REGISTRY_MOMENTS = {
    "cast_376_interest_burden_proxy_skew_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_376_interest_burden_proxy_skew_5d},
    "cast_377_interest_burden_proxy_kurt_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_377_interest_burden_proxy_kurt_5d},
    "cast_378_interest_burden_proxy_skew_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_378_interest_burden_proxy_skew_21d},
    "cast_379_interest_burden_proxy_kurt_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_379_interest_burden_proxy_kurt_21d},
    "cast_380_interest_burden_proxy_skew_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_380_interest_burden_proxy_skew_63d},
    "cast_381_interest_burden_proxy_kurt_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_381_interest_burden_proxy_kurt_63d},
    "cast_382_interest_burden_proxy_skew_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_382_interest_burden_proxy_skew_126d},
    "cast_383_interest_burden_proxy_kurt_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_383_interest_burden_proxy_kurt_126d},
    "cast_384_interest_burden_proxy_skew_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_384_interest_burden_proxy_skew_252d},
    "cast_385_interest_burden_proxy_kurt_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_385_interest_burden_proxy_kurt_252d},
    "cast_386_debt_to_equity_z_skew_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_386_debt_to_equity_z_skew_5d},
    "cast_387_debt_to_equity_z_kurt_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_387_debt_to_equity_z_kurt_5d},
    "cast_388_debt_to_equity_z_skew_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_388_debt_to_equity_z_skew_21d},
    "cast_389_debt_to_equity_z_kurt_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_389_debt_to_equity_z_kurt_21d},
    "cast_390_debt_to_equity_z_skew_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_390_debt_to_equity_z_skew_63d},
    "cast_391_debt_to_equity_z_kurt_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_391_debt_to_equity_z_kurt_63d},
    "cast_392_debt_to_equity_z_skew_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_392_debt_to_equity_z_skew_126d},
    "cast_393_debt_to_equity_z_kurt_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_393_debt_to_equity_z_kurt_126d},
    "cast_394_debt_to_equity_z_skew_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_394_debt_to_equity_z_skew_252d},
    "cast_395_debt_to_equity_z_kurt_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_395_debt_to_equity_z_kurt_252d},
    "cast_396_equity_funding_risk_skew_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_396_equity_funding_risk_skew_5d},
    "cast_397_equity_funding_risk_kurt_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_397_equity_funding_risk_kurt_5d},
    "cast_398_equity_funding_risk_skew_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_398_equity_funding_risk_skew_21d},
    "cast_399_equity_funding_risk_kurt_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_399_equity_funding_risk_kurt_21d},
    "cast_400_equity_funding_risk_skew_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_400_equity_funding_risk_skew_63d},
    "cast_401_equity_funding_risk_kurt_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_401_equity_funding_risk_kurt_63d},
    "cast_402_equity_funding_risk_skew_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_402_equity_funding_risk_skew_126d},
    "cast_403_equity_funding_risk_kurt_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_403_equity_funding_risk_kurt_126d},
    "cast_404_equity_funding_risk_skew_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_404_equity_funding_risk_skew_252d},
    "cast_405_equity_funding_risk_kurt_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_405_equity_funding_risk_kurt_252d},
    "cast_406_debt_acceleration_skew_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_406_debt_acceleration_skew_5d},
    "cast_407_debt_acceleration_kurt_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_407_debt_acceleration_kurt_5d},
    "cast_408_debt_acceleration_skew_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_408_debt_acceleration_skew_21d},
    "cast_409_debt_acceleration_kurt_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_409_debt_acceleration_kurt_21d},
    "cast_410_debt_acceleration_skew_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_410_debt_acceleration_skew_63d},
    "cast_411_debt_acceleration_kurt_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_411_debt_acceleration_kurt_63d},
    "cast_412_debt_acceleration_skew_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_412_debt_acceleration_skew_126d},
    "cast_413_debt_acceleration_kurt_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_413_debt_acceleration_kurt_126d},
    "cast_414_debt_acceleration_skew_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_414_debt_acceleration_skew_252d},
    "cast_415_debt_acceleration_kurt_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_415_debt_acceleration_kurt_252d},
    "cast_416_fcf_debt_service_skew_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_416_fcf_debt_service_skew_5d},
    "cast_417_fcf_debt_service_kurt_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_417_fcf_debt_service_kurt_5d},
    "cast_418_fcf_debt_service_skew_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_418_fcf_debt_service_skew_21d},
    "cast_419_fcf_debt_service_kurt_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_419_fcf_debt_service_kurt_21d},
    "cast_420_fcf_debt_service_skew_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_420_fcf_debt_service_skew_63d},
    "cast_421_fcf_debt_service_kurt_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_421_fcf_debt_service_kurt_63d},
    "cast_422_fcf_debt_service_skew_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_422_fcf_debt_service_skew_126d},
    "cast_423_fcf_debt_service_kurt_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_423_fcf_debt_service_kurt_126d},
    "cast_424_fcf_debt_service_skew_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_424_fcf_debt_service_skew_252d},
    "cast_425_fcf_debt_service_kurt_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_425_fcf_debt_service_kurt_252d},
    "cast_426_capital_access_score_skew_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_426_capital_access_score_skew_5d},
    "cast_427_capital_access_score_kurt_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_427_capital_access_score_kurt_5d},
    "cast_428_capital_access_score_skew_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_428_capital_access_score_skew_21d},
    "cast_429_capital_access_score_kurt_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_429_capital_access_score_kurt_21d},
    "cast_430_capital_access_score_skew_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_430_capital_access_score_skew_63d},
    "cast_431_capital_access_score_kurt_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_431_capital_access_score_kurt_63d},
    "cast_432_capital_access_score_skew_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_432_capital_access_score_skew_126d},
    "cast_433_capital_access_score_kurt_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_433_capital_access_score_kurt_126d},
    "cast_434_capital_access_score_skew_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_434_capital_access_score_skew_252d},
    "cast_435_capital_access_score_kurt_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_435_capital_access_score_kurt_252d},
    "cast_436_debt_drawdown_impact_skew_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_436_debt_drawdown_impact_skew_5d},
    "cast_437_debt_drawdown_impact_kurt_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_437_debt_drawdown_impact_kurt_5d},
    "cast_438_debt_drawdown_impact_skew_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_438_debt_drawdown_impact_skew_21d},
    "cast_439_debt_drawdown_impact_kurt_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_439_debt_drawdown_impact_kurt_21d},
    "cast_440_debt_drawdown_impact_skew_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_440_debt_drawdown_impact_skew_63d},
    "cast_441_debt_drawdown_impact_kurt_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_441_debt_drawdown_impact_kurt_63d},
    "cast_442_debt_drawdown_impact_skew_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_442_debt_drawdown_impact_skew_126d},
    "cast_443_debt_drawdown_impact_kurt_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_443_debt_drawdown_impact_kurt_126d},
    "cast_444_debt_drawdown_impact_skew_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_444_debt_drawdown_impact_skew_252d},
    "cast_445_debt_drawdown_impact_kurt_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_445_debt_drawdown_impact_kurt_252d},
    "cast_446_refinancing_risk_proxy_skew_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_446_refinancing_risk_proxy_skew_5d},
    "cast_447_refinancing_risk_proxy_kurt_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_447_refinancing_risk_proxy_kurt_5d},
    "cast_448_refinancing_risk_proxy_skew_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_448_refinancing_risk_proxy_skew_21d},
    "cast_449_refinancing_risk_proxy_kurt_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_449_refinancing_risk_proxy_kurt_21d},
    "cast_450_refinancing_risk_proxy_skew_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_450_refinancing_risk_proxy_skew_63d},
    "cast_451_refinancing_risk_proxy_kurt_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_451_refinancing_risk_proxy_kurt_63d},
    "cast_452_refinancing_risk_proxy_skew_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_452_refinancing_risk_proxy_skew_126d},
    "cast_453_refinancing_risk_proxy_kurt_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_453_refinancing_risk_proxy_kurt_126d},
    "cast_454_refinancing_risk_proxy_skew_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_454_refinancing_risk_proxy_skew_252d},
    "cast_455_refinancing_risk_proxy_kurt_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_455_refinancing_risk_proxy_kurt_252d},
    "cast_456_debt_to_assets_momentum_skew_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_456_debt_to_assets_momentum_skew_5d},
    "cast_457_debt_to_assets_momentum_kurt_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_457_debt_to_assets_momentum_kurt_5d},
    "cast_458_debt_to_assets_momentum_skew_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_458_debt_to_assets_momentum_skew_21d},
    "cast_459_debt_to_assets_momentum_kurt_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_459_debt_to_assets_momentum_kurt_21d},
    "cast_460_debt_to_assets_momentum_skew_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_460_debt_to_assets_momentum_skew_63d},
    "cast_461_debt_to_assets_momentum_kurt_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_461_debt_to_assets_momentum_kurt_63d},
    "cast_462_debt_to_assets_momentum_skew_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_462_debt_to_assets_momentum_skew_126d},
    "cast_463_debt_to_assets_momentum_kurt_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_463_debt_to_assets_momentum_kurt_126d},
    "cast_464_debt_to_assets_momentum_skew_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_464_debt_to_assets_momentum_skew_252d},
    "cast_465_debt_to_assets_momentum_kurt_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_465_debt_to_assets_momentum_kurt_252d},
    "cast_466_fcf_yield_vs_debt_skew_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_466_fcf_yield_vs_debt_skew_5d},
    "cast_467_fcf_yield_vs_debt_kurt_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_467_fcf_yield_vs_debt_kurt_5d},
    "cast_468_fcf_yield_vs_debt_skew_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_468_fcf_yield_vs_debt_skew_21d},
    "cast_469_fcf_yield_vs_debt_kurt_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_469_fcf_yield_vs_debt_kurt_21d},
    "cast_470_fcf_yield_vs_debt_skew_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_470_fcf_yield_vs_debt_skew_63d},
    "cast_471_fcf_yield_vs_debt_kurt_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_471_fcf_yield_vs_debt_kurt_63d},
    "cast_472_fcf_yield_vs_debt_skew_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_472_fcf_yield_vs_debt_skew_126d},
    "cast_473_fcf_yield_vs_debt_kurt_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_473_fcf_yield_vs_debt_kurt_126d},
    "cast_474_fcf_yield_vs_debt_skew_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_474_fcf_yield_vs_debt_skew_252d},
    "cast_475_fcf_yield_vs_debt_kurt_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_475_fcf_yield_vs_debt_kurt_252d},
    "cast_476_capital_structure_z_skew_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_476_capital_structure_z_skew_5d},
    "cast_477_capital_structure_z_kurt_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_477_capital_structure_z_kurt_5d},
    "cast_478_capital_structure_z_skew_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_478_capital_structure_z_skew_21d},
    "cast_479_capital_structure_z_kurt_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_479_capital_structure_z_kurt_21d},
    "cast_480_capital_structure_z_skew_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_480_capital_structure_z_skew_63d},
    "cast_481_capital_structure_z_kurt_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_481_capital_structure_z_kurt_63d},
    "cast_482_capital_structure_z_skew_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_482_capital_structure_z_skew_126d},
    "cast_483_capital_structure_z_kurt_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_483_capital_structure_z_kurt_126d},
    "cast_484_capital_structure_z_skew_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_484_capital_structure_z_skew_252d},
    "cast_485_capital_structure_z_kurt_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_485_capital_structure_z_kurt_252d},
    "cast_486_equity_value_erosion_skew_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_486_equity_value_erosion_skew_5d},
    "cast_487_equity_value_erosion_kurt_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_487_equity_value_erosion_kurt_5d},
    "cast_488_equity_value_erosion_skew_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_488_equity_value_erosion_skew_21d},
    "cast_489_equity_value_erosion_kurt_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_489_equity_value_erosion_kurt_21d},
    "cast_490_equity_value_erosion_skew_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_490_equity_value_erosion_skew_63d},
    "cast_491_equity_value_erosion_kurt_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_491_equity_value_erosion_kurt_63d},
    "cast_492_equity_value_erosion_skew_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_492_equity_value_erosion_skew_126d},
    "cast_493_equity_value_erosion_kurt_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_493_equity_value_erosion_kurt_126d},
    "cast_494_equity_value_erosion_skew_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_494_equity_value_erosion_skew_252d},
    "cast_495_equity_value_erosion_kurt_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_495_equity_value_erosion_kurt_252d},
    "cast_496_debt_burden_vol_skew_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_496_debt_burden_vol_skew_5d},
    "cast_497_debt_burden_vol_kurt_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_497_debt_burden_vol_kurt_5d},
    "cast_498_debt_burden_vol_skew_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_498_debt_burden_vol_skew_21d},
    "cast_499_debt_burden_vol_kurt_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_499_debt_burden_vol_kurt_21d},
    "cast_500_debt_burden_vol_skew_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_500_debt_burden_vol_skew_63d},
    "cast_501_debt_burden_vol_kurt_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_501_debt_burden_vol_kurt_63d},
    "cast_502_debt_burden_vol_skew_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_502_debt_burden_vol_skew_126d},
    "cast_503_debt_burden_vol_kurt_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_503_debt_burden_vol_kurt_126d},
    "cast_504_debt_burden_vol_skew_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_504_debt_burden_vol_skew_252d},
    "cast_505_debt_burden_vol_kurt_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_505_debt_burden_vol_kurt_252d},
    "cast_506_capital_stress_index_skew_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_506_capital_stress_index_skew_5d},
    "cast_507_capital_stress_index_kurt_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_507_capital_stress_index_kurt_5d},
    "cast_508_capital_stress_index_skew_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_508_capital_stress_index_skew_21d},
    "cast_509_capital_stress_index_kurt_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_509_capital_stress_index_kurt_21d},
    "cast_510_capital_stress_index_skew_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_510_capital_stress_index_skew_63d},
    "cast_511_capital_stress_index_kurt_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_511_capital_stress_index_kurt_63d},
    "cast_512_capital_stress_index_skew_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_512_capital_stress_index_skew_126d},
    "cast_513_capital_stress_index_kurt_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_513_capital_stress_index_kurt_126d},
    "cast_514_capital_stress_index_skew_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_514_capital_stress_index_skew_252d},
    "cast_515_capital_stress_index_kurt_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_515_capital_stress_index_kurt_252d},
    "cast_516_solvency_cushion_skew_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_516_solvency_cushion_skew_5d},
    "cast_517_solvency_cushion_kurt_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_517_solvency_cushion_kurt_5d},
    "cast_518_solvency_cushion_skew_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_518_solvency_cushion_skew_21d},
    "cast_519_solvency_cushion_kurt_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_519_solvency_cushion_kurt_21d},
    "cast_520_solvency_cushion_skew_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_520_solvency_cushion_skew_63d},
    "cast_521_solvency_cushion_kurt_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_521_solvency_cushion_kurt_63d},
    "cast_522_solvency_cushion_skew_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_522_solvency_cushion_skew_126d},
    "cast_523_solvency_cushion_kurt_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_523_solvency_cushion_kurt_126d},
    "cast_524_solvency_cushion_skew_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_524_solvency_cushion_skew_252d},
    "cast_525_solvency_cushion_kurt_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_525_solvency_cushion_kurt_252d},
}
