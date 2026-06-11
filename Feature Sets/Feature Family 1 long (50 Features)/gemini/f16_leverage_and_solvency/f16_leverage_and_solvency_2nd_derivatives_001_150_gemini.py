import pandas as pd
import numpy as np
import inspect

def _solv_ratio(num, den):
    return num / den.replace(0, np.nan)

def _solv_zscore(s, w):
    return (s - s.rolling(w, min_periods=1).mean()) / s.rolling(w, min_periods=1).std().replace(0, np.nan)

def _solv_slope(s):
    return s.diff()

# Slope Features 001-150 (1st derivative of base features)

# 1. Debt to Equity
def f16_leverage_and_solvency_slope_debt_equity_ratio(arg_debt, arg_equity):
    return _solv_slope(_solv_ratio(arg_debt, arg_equity))

def f16_leverage_and_solvency_slope_zscore_debt_equity_63(arg_debt, arg_equity):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_debt, arg_equity), 63))

def f16_leverage_and_solvency_slope_zscore_debt_equity_126(arg_debt, arg_equity):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_debt, arg_equity), 126))

def f16_leverage_and_solvency_slope_zscore_debt_equity_252(arg_debt, arg_equity):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_debt, arg_equity), 252))

def f16_leverage_and_solvency_slope_zscore_debt_equity_504(arg_debt, arg_equity):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_debt, arg_equity), 504))

def f16_leverage_and_solvency_slope_zscore_debt_equity_756(arg_debt, arg_equity):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_debt, arg_equity), 756))

def f16_leverage_and_solvency_slope_zscore_debt_equity_1260(arg_debt, arg_equity):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_debt, arg_equity), 1260))

# 2. Debt to EBITDA
def f16_leverage_and_solvency_slope_debt_ebitda_ratio(arg_debt, arg_ebitda):
    return _solv_slope(_solv_ratio(arg_debt, arg_ebitda))

def f16_leverage_and_solvency_slope_zscore_debt_ebitda_63(arg_debt, arg_ebitda):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_debt, arg_ebitda), 63))

def f16_leverage_and_solvency_slope_zscore_debt_ebitda_126(arg_debt, arg_ebitda):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_debt, arg_ebitda), 126))

def f16_leverage_and_solvency_slope_zscore_debt_ebitda_252(arg_debt, arg_ebitda):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_debt, arg_ebitda), 252))

def f16_leverage_and_solvency_slope_zscore_debt_ebitda_504(arg_debt, arg_ebitda):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_debt, arg_ebitda), 504))

def f16_leverage_and_solvency_slope_zscore_debt_ebitda_756(arg_debt, arg_ebitda):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_debt, arg_ebitda), 756))

def f16_leverage_and_solvency_slope_zscore_debt_ebitda_1260(arg_debt, arg_ebitda):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_debt, arg_ebitda), 1260))

# 3. Interest Coverage
def f16_leverage_and_solvency_slope_interest_coverage_ratio(arg_opinc, arg_intexp):
    return _solv_slope(_solv_ratio(arg_opinc, arg_intexp))

def f16_leverage_and_solvency_slope_zscore_interest_coverage_63(arg_opinc, arg_intexp):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_opinc, arg_intexp), 63))

def f16_leverage_and_solvency_slope_zscore_interest_coverage_126(arg_opinc, arg_intexp):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_opinc, arg_intexp), 126))

def f16_leverage_and_solvency_slope_zscore_interest_coverage_252(arg_opinc, arg_intexp):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_opinc, arg_intexp), 252))

def f16_leverage_and_solvency_slope_zscore_interest_coverage_504(arg_opinc, arg_intexp):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_opinc, arg_intexp), 504))

def f16_leverage_and_solvency_slope_zscore_interest_coverage_756(arg_opinc, arg_intexp):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_opinc, arg_intexp), 756))

def f16_leverage_and_solvency_slope_zscore_interest_coverage_1260(arg_opinc, arg_intexp):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_opinc, arg_intexp), 1260))

# 4. Debt to Assets
def f16_leverage_and_solvency_slope_debt_assets_ratio(arg_debt, arg_assets):
    return _solv_slope(_solv_ratio(arg_debt, arg_assets))

def f16_leverage_and_solvency_slope_zscore_debt_assets_63(arg_debt, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_debt, arg_assets), 63))

def f16_leverage_and_solvency_slope_zscore_debt_assets_126(arg_debt, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_debt, arg_assets), 126))

def f16_leverage_and_solvency_slope_zscore_debt_assets_252(arg_debt, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_debt, arg_assets), 252))

def f16_leverage_and_solvency_slope_zscore_debt_assets_504(arg_debt, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_debt, arg_assets), 504))

def f16_leverage_and_solvency_slope_zscore_debt_assets_756(arg_debt, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_debt, arg_assets), 756))

def f16_leverage_and_solvency_slope_zscore_debt_assets_1260(arg_debt, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_debt, arg_assets), 1260))

# 5. Equity to Assets
def f16_leverage_and_solvency_slope_equity_assets_ratio(arg_equity, arg_assets):
    return _solv_slope(_solv_ratio(arg_equity, arg_assets))

def f16_leverage_and_solvency_slope_zscore_equity_assets_63(arg_equity, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_equity, arg_assets), 63))

def f16_leverage_and_solvency_slope_zscore_equity_assets_126(arg_equity, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_equity, arg_assets), 126))

def f16_leverage_and_solvency_slope_zscore_equity_assets_252(arg_equity, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_equity, arg_assets), 252))

def f16_leverage_and_solvency_slope_zscore_equity_assets_504(arg_equity, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_equity, arg_assets), 504))

def f16_leverage_and_solvency_slope_zscore_equity_assets_756(arg_equity, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_equity, arg_assets), 756))

def f16_leverage_and_solvency_slope_zscore_equity_assets_1260(arg_equity, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_equity, arg_assets), 1260))

# 6. Liabilities to Assets
def f16_leverage_and_solvency_slope_liabilities_assets_ratio(arg_liabilities, arg_assets):
    return _solv_slope(_solv_ratio(arg_liabilities, arg_assets))

def f16_leverage_and_solvency_slope_zscore_liabilities_assets_63(arg_liabilities, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_liabilities, arg_assets), 63))

def f16_leverage_and_solvency_slope_zscore_liabilities_assets_126(arg_liabilities, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_liabilities, arg_assets), 126))

def f16_leverage_and_solvency_slope_zscore_liabilities_assets_252(arg_liabilities, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_liabilities, arg_assets), 252))

def f16_leverage_and_solvency_slope_zscore_liabilities_assets_504(arg_liabilities, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_liabilities, arg_assets), 504))

def f16_leverage_and_solvency_slope_zscore_liabilities_assets_756(arg_liabilities, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_liabilities, arg_assets), 756))

def f16_leverage_and_solvency_slope_zscore_liabilities_assets_1260(arg_liabilities, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_liabilities, arg_assets), 1260))

# 7. Working Capital to Debt
def f16_leverage_and_solvency_slope_wc_debt_ratio(arg_workingcapital, arg_debt):
    return _solv_slope(_solv_ratio(arg_workingcapital, arg_debt))

def f16_leverage_and_solvency_slope_zscore_wc_debt_63(arg_workingcapital, arg_debt):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_workingcapital, arg_debt), 63))

def f16_leverage_and_solvency_slope_zscore_wc_debt_126(arg_workingcapital, arg_debt):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_workingcapital, arg_debt), 126))

def f16_leverage_and_solvency_slope_zscore_wc_debt_252(arg_workingcapital, arg_debt):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_workingcapital, arg_debt), 252))

def f16_leverage_and_solvency_slope_zscore_wc_debt_504(arg_workingcapital, arg_debt):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_workingcapital, arg_debt), 504))

def f16_leverage_and_solvency_slope_zscore_wc_debt_756(arg_workingcapital, arg_debt):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_workingcapital, arg_debt), 756))

def f16_leverage_and_solvency_slope_zscore_wc_debt_1260(arg_workingcapital, arg_debt):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_workingcapital, arg_debt), 1260))

# 8. Debt to Cap
def f16_leverage_and_solvency_slope_debt_cap_ratio(arg_debt, arg_equity):
    return _solv_slope(_solv_ratio(arg_debt, arg_debt + arg_equity))

def f16_leverage_and_solvency_slope_zscore_debt_cap_63(arg_debt, arg_equity):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_debt, arg_debt + arg_equity), 63))

def f16_leverage_and_solvency_slope_zscore_debt_cap_126(arg_debt, arg_equity):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_debt, arg_debt + arg_equity), 126))

def f16_leverage_and_solvency_slope_zscore_debt_cap_252(arg_debt, arg_equity):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_debt, arg_debt + arg_equity), 252))

def f16_leverage_and_solvency_slope_zscore_debt_cap_504(arg_debt, arg_equity):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_debt, arg_debt + arg_equity), 504))

def f16_leverage_and_solvency_slope_zscore_debt_cap_756(arg_debt, arg_equity):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_debt, arg_debt + arg_equity), 756))

def f16_leverage_and_solvency_slope_zscore_debt_cap_1260(arg_debt, arg_equity):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_debt, arg_debt + arg_equity), 1260))

# 9. EBITDA Coverage
def f16_leverage_and_solvency_slope_ebitda_coverage_ratio(arg_ebitda, arg_intexp):
    return _solv_slope(_solv_ratio(arg_ebitda, arg_intexp))

def f16_leverage_and_solvency_slope_zscore_ebitda_coverage_63(arg_ebitda, arg_intexp):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_ebitda, arg_intexp), 63))

def f16_leverage_and_solvency_slope_zscore_ebitda_coverage_126(arg_ebitda, arg_intexp):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_ebitda, arg_intexp), 126))

def f16_leverage_and_solvency_slope_zscore_ebitda_coverage_252(arg_ebitda, arg_intexp):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_ebitda, arg_intexp), 252))

def f16_leverage_and_solvency_slope_zscore_ebitda_coverage_504(arg_ebitda, arg_intexp):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_ebitda, arg_intexp), 504))

def f16_leverage_and_solvency_slope_zscore_ebitda_coverage_756(arg_ebitda, arg_intexp):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_ebitda, arg_intexp), 756))

def f16_leverage_and_solvency_slope_zscore_ebitda_coverage_1260(arg_ebitda, arg_intexp):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_ebitda, arg_intexp), 1260))

# 10. Equity Multiplier
def f16_leverage_and_solvency_slope_equity_multiplier_ratio(arg_assets, arg_equity):
    return _solv_slope(_solv_ratio(arg_assets, arg_equity))

def f16_leverage_and_solvency_slope_zscore_equity_multiplier_63(arg_assets, arg_equity):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_assets, arg_equity), 63))

def f16_leverage_and_solvency_slope_zscore_equity_multiplier_126(arg_assets, arg_equity):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_assets, arg_equity), 126))

def f16_leverage_and_solvency_slope_zscore_equity_multiplier_252(arg_assets, arg_equity):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_assets, arg_equity), 252))

def f16_leverage_and_solvency_slope_zscore_equity_multiplier_504(arg_assets, arg_equity):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_assets, arg_equity), 504))

def f16_leverage_and_solvency_slope_zscore_equity_multiplier_756(arg_assets, arg_equity):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_assets, arg_equity), 756))

def f16_leverage_and_solvency_slope_zscore_equity_multiplier_1260(arg_assets, arg_equity):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_assets, arg_equity), 1260))

# 11. WC to Assets
def f16_leverage_and_solvency_slope_wc_assets_ratio(arg_workingcapital, arg_assets):
    return _solv_slope(_solv_ratio(arg_workingcapital, arg_assets))

def f16_leverage_and_solvency_slope_zscore_wc_assets_63(arg_workingcapital, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_workingcapital, arg_assets), 63))

def f16_leverage_and_solvency_slope_zscore_wc_assets_126(arg_workingcapital, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_workingcapital, arg_assets), 126))

def f16_leverage_and_solvency_slope_zscore_wc_assets_252(arg_workingcapital, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_workingcapital, arg_assets), 252))

def f16_leverage_and_solvency_slope_zscore_wc_assets_504(arg_workingcapital, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_workingcapital, arg_assets), 504))

def f16_leverage_and_solvency_slope_zscore_wc_assets_756(arg_workingcapital, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_workingcapital, arg_assets), 756))

def f16_leverage_and_solvency_slope_zscore_wc_assets_1260(arg_workingcapital, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_workingcapital, arg_assets), 1260))

# 12. Liabilities to Equity
def f16_leverage_and_solvency_slope_liabilities_equity_ratio(arg_liabilities, arg_equity):
    return _solv_slope(_solv_ratio(arg_liabilities, arg_equity))

def f16_leverage_and_solvency_slope_zscore_liabilities_equity_63(arg_liabilities, arg_equity):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_liabilities, arg_equity), 63))

def f16_leverage_and_solvency_slope_zscore_liabilities_equity_126(arg_liabilities, arg_equity):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_liabilities, arg_equity), 126))

def f16_leverage_and_solvency_slope_zscore_liabilities_equity_252(arg_liabilities, arg_equity):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_liabilities, arg_equity), 252))

def f16_leverage_and_solvency_slope_zscore_liabilities_equity_504(arg_liabilities, arg_equity):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_liabilities, arg_equity), 504))

def f16_leverage_and_solvency_slope_zscore_liabilities_equity_756(arg_liabilities, arg_equity):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_liabilities, arg_equity), 756))

def f16_leverage_and_solvency_slope_zscore_liabilities_equity_1260(arg_liabilities, arg_equity):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_liabilities, arg_equity), 1260))

# 13. OpInc to Debt
def f16_leverage_and_solvency_slope_opinc_debt_ratio(arg_opinc, arg_debt):
    return _solv_slope(_solv_ratio(arg_opinc, arg_debt))

def f16_leverage_and_solvency_slope_zscore_opinc_debt_63(arg_opinc, arg_debt):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_opinc, arg_debt), 63))

def f16_leverage_and_solvency_slope_zscore_opinc_debt_126(arg_opinc, arg_debt):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_opinc, arg_debt), 126))

def f16_leverage_and_solvency_slope_zscore_opinc_debt_252(arg_opinc, arg_debt):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_opinc, arg_debt), 252))

def f16_leverage_and_solvency_slope_zscore_opinc_debt_504(arg_opinc, arg_debt):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_opinc, arg_debt), 504))

def f16_leverage_and_solvency_slope_zscore_opinc_debt_756(arg_opinc, arg_debt):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_opinc, arg_debt), 756))

def f16_leverage_and_solvency_slope_zscore_opinc_debt_1260(arg_opinc, arg_debt):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_opinc, arg_debt), 1260))

# 14. EBITDA to Debt
def f16_leverage_and_solvency_slope_ebitda_debt_ratio(arg_ebitda, arg_debt):
    return _solv_slope(_solv_ratio(arg_ebitda, arg_debt))

def f16_leverage_and_solvency_slope_zscore_ebitda_debt_63(arg_ebitda, arg_debt):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_ebitda, arg_debt), 63))

def f16_leverage_and_solvency_slope_zscore_ebitda_debt_126(arg_ebitda, arg_debt):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_ebitda, arg_debt), 126))

def f16_leverage_and_solvency_slope_zscore_ebitda_debt_252(arg_ebitda, arg_debt):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_ebitda, arg_debt), 252))

def f16_leverage_and_solvency_slope_zscore_ebitda_debt_504(arg_ebitda, arg_debt):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_ebitda, arg_debt), 504))

def f16_leverage_and_solvency_slope_zscore_ebitda_debt_756(arg_ebitda, arg_debt):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_ebitda, arg_debt), 756))

def f16_leverage_and_solvency_slope_zscore_ebitda_debt_1260(arg_ebitda, arg_debt):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_ebitda, arg_debt), 1260))

# 15. Debt to (Debt + Assets)
def f16_leverage_and_solvency_slope_debt_to_assets_plus_debt_ratio(arg_debt, arg_assets):
    return _solv_slope(_solv_ratio(arg_debt, arg_debt + arg_assets))

def f16_leverage_and_solvency_slope_zscore_debt_to_assets_plus_debt_63(arg_debt, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_debt, arg_debt + arg_assets), 63))

def f16_leverage_and_solvency_slope_zscore_debt_to_assets_plus_debt_126(arg_debt, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_debt, arg_debt + arg_assets), 126))

def f16_leverage_and_solvency_slope_zscore_debt_to_assets_plus_debt_252(arg_debt, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_debt, arg_debt + arg_assets), 252))

def f16_leverage_and_solvency_slope_zscore_debt_to_assets_plus_debt_504(arg_debt, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_debt, arg_debt + arg_assets), 504))

def f16_leverage_and_solvency_slope_zscore_debt_to_assets_plus_debt_756(arg_debt, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_debt, arg_debt + arg_assets), 756))

def f16_leverage_and_solvency_slope_zscore_debt_to_assets_plus_debt_1260(arg_debt, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_debt, arg_debt + arg_assets), 1260))

# 16. Equity Total Cap
def f16_leverage_and_solvency_slope_equity_total_cap_ratio(arg_equity, arg_debt):
    return _solv_slope(_solv_ratio(arg_equity, arg_debt + arg_equity))

def f16_leverage_and_solvency_slope_zscore_equity_total_cap_63(arg_equity, arg_debt):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_equity, arg_debt + arg_equity), 63))

def f16_leverage_and_solvency_slope_zscore_equity_total_cap_126(arg_equity, arg_debt):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_equity, arg_debt + arg_equity), 126))

def f16_leverage_and_solvency_slope_zscore_equity_total_cap_252(arg_equity, arg_debt):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_equity, arg_debt + arg_equity), 252))

def f16_leverage_and_solvency_slope_zscore_equity_total_cap_504(arg_equity, arg_debt):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_equity, arg_debt + arg_equity), 504))

def f16_leverage_and_solvency_slope_zscore_equity_total_cap_756(arg_equity, arg_debt):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_equity, arg_debt + arg_equity), 756))

def f16_leverage_and_solvency_slope_zscore_equity_total_cap_1260(arg_equity, arg_debt):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_equity, arg_debt + arg_equity), 1260))

# 17. Liabilities to (Debt + Assets)
def f16_leverage_and_solvency_slope_liabilities_to_assets_plus_debt_ratio(arg_liabilities, arg_debt, arg_assets):
    return _solv_slope(_solv_ratio(arg_liabilities, arg_debt + arg_assets))

def f16_leverage_and_solvency_slope_zscore_liabilities_to_assets_plus_debt_63(arg_liabilities, arg_debt, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_liabilities, arg_debt + arg_assets), 63))

def f16_leverage_and_solvency_slope_zscore_liabilities_to_assets_plus_debt_126(arg_liabilities, arg_debt, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_liabilities, arg_debt + arg_assets), 126))

def f16_leverage_and_solvency_slope_zscore_liabilities_to_assets_plus_debt_252(arg_liabilities, arg_debt, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_liabilities, arg_debt + arg_assets), 252))

def f16_leverage_and_solvency_slope_zscore_liabilities_to_assets_plus_debt_504(arg_liabilities, arg_debt, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_liabilities, arg_debt + arg_assets), 504))

def f16_leverage_and_solvency_slope_zscore_liabilities_to_assets_plus_debt_756(arg_liabilities, arg_debt, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_liabilities, arg_debt + arg_assets), 756))

def f16_leverage_and_solvency_slope_zscore_liabilities_to_assets_plus_debt_1260(arg_liabilities, arg_debt, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_liabilities, arg_debt + arg_assets), 1260))

# 18. OpInc to Assets
def f16_leverage_and_solvency_slope_opinc_assets_ratio(arg_opinc, arg_assets):
    return _solv_slope(_solv_ratio(arg_opinc, arg_assets))

def f16_leverage_and_solvency_slope_zscore_opinc_assets_63(arg_opinc, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_opinc, arg_assets), 63))

def f16_leverage_and_solvency_slope_zscore_opinc_assets_126(arg_opinc, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_opinc, arg_assets), 126))

def f16_leverage_and_solvency_slope_zscore_opinc_assets_252(arg_opinc, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_opinc, arg_assets), 252))

def f16_leverage_and_solvency_slope_zscore_opinc_assets_504(arg_opinc, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_opinc, arg_assets), 504))

def f16_leverage_and_solvency_slope_zscore_opinc_assets_756(arg_opinc, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_opinc, arg_assets), 756))

def f16_leverage_and_solvency_slope_zscore_opinc_assets_1260(arg_opinc, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_opinc, arg_assets), 1260))

# 19. EBITDA to Assets
def f16_leverage_and_solvency_slope_ebitda_assets_ratio(arg_ebitda, arg_assets):
    return _solv_slope(_solv_ratio(arg_ebitda, arg_assets))

def f16_leverage_and_solvency_slope_zscore_ebitda_assets_63(arg_ebitda, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_ebitda, arg_assets), 63))

def f16_leverage_and_solvency_slope_zscore_ebitda_assets_126(arg_ebitda, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_ebitda, arg_assets), 126))

def f16_leverage_and_solvency_slope_zscore_ebitda_assets_252(arg_ebitda, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_ebitda, arg_assets), 252))

def f16_leverage_and_solvency_slope_zscore_ebitda_assets_504(arg_ebitda, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_ebitda, arg_assets), 504))

def f16_leverage_and_solvency_slope_zscore_ebitda_assets_756(arg_ebitda, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_ebitda, arg_assets), 756))

def f16_leverage_and_solvency_slope_zscore_ebitda_assets_1260(arg_ebitda, arg_assets):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_ebitda, arg_assets), 1260))

# 20. WC to Liabilities
def f16_leverage_and_solvency_slope_wc_liabilities_ratio(arg_workingcapital, arg_liabilities):
    return _solv_slope(_solv_ratio(arg_workingcapital, arg_liabilities))

def f16_leverage_and_solvency_slope_zscore_wc_liabilities_63(arg_workingcapital, arg_liabilities):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_workingcapital, arg_liabilities), 63))

def f16_leverage_and_solvency_slope_zscore_wc_liabilities_126(arg_workingcapital, arg_liabilities):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_workingcapital, arg_liabilities), 126))

def f16_leverage_and_solvency_slope_zscore_wc_liabilities_252(arg_workingcapital, arg_liabilities):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_workingcapital, arg_liabilities), 252))

def f16_leverage_and_solvency_slope_zscore_wc_liabilities_504(arg_workingcapital, arg_liabilities):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_workingcapital, arg_liabilities), 504))

def f16_leverage_and_solvency_slope_zscore_wc_liabilities_756(arg_workingcapital, arg_liabilities):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_workingcapital, arg_liabilities), 756))

def f16_leverage_and_solvency_slope_zscore_wc_liabilities_1260(arg_workingcapital, arg_liabilities):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_workingcapital, arg_liabilities), 1260))

# 21. Current Ratio
def f16_leverage_and_solvency_slope_current_ratio_direct(arg_currentratio):
    return _solv_slope(arg_currentratio)

def f16_leverage_and_solvency_slope_zscore_current_ratio_63(arg_currentratio):
    return _solv_slope(_solv_zscore(arg_currentratio, 63))

def f16_leverage_and_solvency_slope_zscore_current_ratio_126(arg_currentratio):
    return _solv_slope(_solv_zscore(arg_currentratio, 126))

def f16_leverage_and_solvency_slope_zscore_current_ratio_252(arg_currentratio):
    return _solv_slope(_solv_zscore(arg_currentratio, 252))

def f16_leverage_and_solvency_slope_zscore_current_ratio_504(arg_currentratio):
    return _solv_slope(_solv_zscore(arg_currentratio, 504))

def f16_leverage_and_solvency_slope_zscore_current_ratio_756(arg_currentratio):
    return _solv_slope(_solv_zscore(arg_currentratio, 756))

def f16_leverage_and_solvency_slope_zscore_current_ratio_1260(arg_currentratio):
    return _solv_slope(_solv_zscore(arg_currentratio, 1260))

# 22. Assets to Debt
def f16_leverage_and_solvency_slope_assets_debt_ratio(arg_assets, arg_debt):
    return _solv_slope(_solv_ratio(arg_assets, arg_debt))

def f16_leverage_and_solvency_slope_zscore_assets_debt_63(arg_assets, arg_debt):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_assets, arg_debt), 63))

def f16_leverage_and_solvency_slope_zscore_assets_debt_126(arg_assets, arg_debt):
    return _solv_slope(_solv_zscore(_solv_ratio(arg_assets, arg_debt), 126))

def test_features():
    n = 1500
    data = {
        'debt': pd.Series(np.random.uniform(1e6, 1e8, n)),
        'equity': pd.Series(np.random.uniform(1e6, 1e8, n)),
        'ebitda': pd.Series(np.random.uniform(1e5, 1e7, n)),
        'opinc': pd.Series(np.random.uniform(1e5, 1e7, n)),
        'intexp': pd.Series(np.random.uniform(1e4, 1e6, n)),
        'assets': pd.Series(np.random.uniform(1e7, 1e9, n)),
        'liabilities': pd.Series(np.random.uniform(1e6, 1e8, n)),
        'workingcapital': pd.Series(np.random.uniform(1e5, 1e7, n)),
        'currentratio': pd.Series(np.random.uniform(0.5, 3.0, n)),
    }
    
    functions = [obj for name, obj in globals().items()
                 if (inspect.isfunction(obj) and name.startswith('f16_leverage_and_solvency_slope_'))]
    
    for func in functions:
        sig = inspect.signature(func)
        args = {param: data[param.replace('arg_', '')] for param in sig.parameters}
        res = func(**args)
        
        assert len(res) > 0, f"Function {func.__name__} returned empty result"
        valid = res.dropna()
        if len(valid) > 10:
            assert valid.nunique() > 2, f"Function {func.__name__} has too few unique values"
            assert valid.std() > 0, f"Function {func.__name__} has zero standard deviation"

if __name__ == "__main__":
    test_features()
    print("All tests passed!")
