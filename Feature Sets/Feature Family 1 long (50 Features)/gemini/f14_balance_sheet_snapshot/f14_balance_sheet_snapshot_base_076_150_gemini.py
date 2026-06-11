import pandas as pd
import numpy as np
import inspect

def _bs_ratio(num, den):
    return num / den.replace(0, np.nan)

def _bs_zscore(s, w):
    return (s - s.rolling(w, min_periods=1).mean()) / s.rolling(w, min_periods=1).std().replace(0, np.nan)

# Helper functions for core ratios 11-15 (needed for z-scores)
def _f14_balance_sheet_snapshot_wc_liab_ratio(arg_workingcapital, arg_liabilities):
    return _bs_ratio(arg_workingcapital, arg_liabilities)

def _f14_balance_sheet_snapshot_retearn_equity_ratio(arg_retearn, arg_equity):
    return _bs_ratio(arg_retearn, arg_equity)

def _f14_balance_sheet_snapshot_debt_wc_ratio(arg_debt, arg_workingcapital):
    return _bs_ratio(arg_debt, arg_workingcapital)

def _f14_balance_sheet_snapshot_assets_shares_ratio(arg_assets, arg_shareswa):
    return _bs_ratio(arg_assets, arg_shareswa)

def _f14_balance_sheet_snapshot_liab_shares_ratio(arg_liabilities, arg_shareswa):
    return _bs_ratio(arg_liabilities, arg_shareswa)

# Base 076-105: Z-scores of core ratios (Part 2)
def f14_balance_sheet_snapshot_zscore_wc_liab_63(arg_workingcapital, arg_liabilities):
    return _bs_zscore(_f14_balance_sheet_snapshot_wc_liab_ratio(arg_workingcapital, arg_liabilities), 63)

def f14_balance_sheet_snapshot_zscore_wc_liab_126(arg_workingcapital, arg_liabilities):
    return _bs_zscore(_f14_balance_sheet_snapshot_wc_liab_ratio(arg_workingcapital, arg_liabilities), 126)

def f14_balance_sheet_snapshot_zscore_wc_liab_252(arg_workingcapital, arg_liabilities):
    return _bs_zscore(_f14_balance_sheet_snapshot_wc_liab_ratio(arg_workingcapital, arg_liabilities), 252)

def f14_balance_sheet_snapshot_zscore_wc_liab_504(arg_workingcapital, arg_liabilities):
    return _bs_zscore(_f14_balance_sheet_snapshot_wc_liab_ratio(arg_workingcapital, arg_liabilities), 504)

def f14_balance_sheet_snapshot_zscore_wc_liab_756(arg_workingcapital, arg_liabilities):
    return _bs_zscore(_f14_balance_sheet_snapshot_wc_liab_ratio(arg_workingcapital, arg_liabilities), 756)

def f14_balance_sheet_snapshot_zscore_wc_liab_1260(arg_workingcapital, arg_liabilities):
    return _bs_zscore(_f14_balance_sheet_snapshot_wc_liab_ratio(arg_workingcapital, arg_liabilities), 1260)

def f14_balance_sheet_snapshot_zscore_retearn_equity_63(arg_retearn, arg_equity):
    return _bs_zscore(_f14_balance_sheet_snapshot_retearn_equity_ratio(arg_retearn, arg_equity), 63)

def f14_balance_sheet_snapshot_zscore_retearn_equity_126(arg_retearn, arg_equity):
    return _bs_zscore(_f14_balance_sheet_snapshot_retearn_equity_ratio(arg_retearn, arg_equity), 126)

def f14_balance_sheet_snapshot_zscore_retearn_equity_252(arg_retearn, arg_equity):
    return _bs_zscore(_f14_balance_sheet_snapshot_retearn_equity_ratio(arg_retearn, arg_equity), 252)

def f14_balance_sheet_snapshot_zscore_retearn_equity_504(arg_retearn, arg_equity):
    return _bs_zscore(_f14_balance_sheet_snapshot_retearn_equity_ratio(arg_retearn, arg_equity), 504)

def f14_balance_sheet_snapshot_zscore_retearn_equity_756(arg_retearn, arg_equity):
    return _bs_zscore(_f14_balance_sheet_snapshot_retearn_equity_ratio(arg_retearn, arg_equity), 756)

def f14_balance_sheet_snapshot_zscore_retearn_equity_1260(arg_retearn, arg_equity):
    return _bs_zscore(_f14_balance_sheet_snapshot_retearn_equity_ratio(arg_retearn, arg_equity), 1260)

def f14_balance_sheet_snapshot_zscore_debt_wc_63(arg_debt, arg_workingcapital):
    return _bs_zscore(_f14_balance_sheet_snapshot_debt_wc_ratio(arg_debt, arg_workingcapital), 63)

def f14_balance_sheet_snapshot_zscore_debt_wc_126(arg_debt, arg_workingcapital):
    return _bs_zscore(_f14_balance_sheet_snapshot_debt_wc_ratio(arg_debt, arg_workingcapital), 126)

def f14_balance_sheet_snapshot_zscore_debt_wc_252(arg_debt, arg_workingcapital):
    return _bs_zscore(_f14_balance_sheet_snapshot_debt_wc_ratio(arg_debt, arg_workingcapital), 252)

def f14_balance_sheet_snapshot_zscore_debt_wc_504(arg_debt, arg_workingcapital):
    return _bs_zscore(_f14_balance_sheet_snapshot_debt_wc_ratio(arg_debt, arg_workingcapital), 504)

def f14_balance_sheet_snapshot_zscore_debt_wc_756(arg_debt, arg_workingcapital):
    return _bs_zscore(_f14_balance_sheet_snapshot_debt_wc_ratio(arg_debt, arg_workingcapital), 756)

def f14_balance_sheet_snapshot_zscore_debt_wc_1260(arg_debt, arg_workingcapital):
    return _bs_zscore(_f14_balance_sheet_snapshot_debt_wc_ratio(arg_debt, arg_workingcapital), 1260)

def f14_balance_sheet_snapshot_zscore_assets_shares_63(arg_assets, arg_shareswa):
    return _bs_zscore(_f14_balance_sheet_snapshot_assets_shares_ratio(arg_assets, arg_shareswa), 63)

def f14_balance_sheet_snapshot_zscore_assets_shares_126(arg_assets, arg_shareswa):
    return _bs_zscore(_f14_balance_sheet_snapshot_assets_shares_ratio(arg_assets, arg_shareswa), 126)

def f14_balance_sheet_snapshot_zscore_assets_shares_252(arg_assets, arg_shareswa):
    return _bs_zscore(_f14_balance_sheet_snapshot_assets_shares_ratio(arg_assets, arg_shareswa), 252)

def f14_balance_sheet_snapshot_zscore_assets_shares_504(arg_assets, arg_shareswa):
    return _bs_zscore(_f14_balance_sheet_snapshot_assets_shares_ratio(arg_assets, arg_shareswa), 504)

def f14_balance_sheet_snapshot_zscore_assets_shares_756(arg_assets, arg_shareswa):
    return _bs_zscore(_f14_balance_sheet_snapshot_assets_shares_ratio(arg_assets, arg_shareswa), 756)

def f14_balance_sheet_snapshot_zscore_assets_shares_1260(arg_assets, arg_shareswa):
    return _bs_zscore(_f14_balance_sheet_snapshot_assets_shares_ratio(arg_assets, arg_shareswa), 1260)

def f14_balance_sheet_snapshot_zscore_liab_shares_63(arg_liabilities, arg_shareswa):
    return _bs_zscore(_f14_balance_sheet_snapshot_liab_shares_ratio(arg_liabilities, arg_shareswa), 63)

def f14_balance_sheet_snapshot_zscore_liab_shares_126(arg_liabilities, arg_shareswa):
    return _bs_zscore(_f14_balance_sheet_snapshot_liab_shares_ratio(arg_liabilities, arg_shareswa), 126)

def f14_balance_sheet_snapshot_zscore_liab_shares_252(arg_liabilities, arg_shareswa):
    return _bs_zscore(_f14_balance_sheet_snapshot_liab_shares_ratio(arg_liabilities, arg_shareswa), 252)

def f14_balance_sheet_snapshot_zscore_liab_shares_504(arg_liabilities, arg_shareswa):
    return _bs_zscore(_f14_balance_sheet_snapshot_liab_shares_ratio(arg_liabilities, arg_shareswa), 504)

def f14_balance_sheet_snapshot_zscore_liab_shares_756(arg_liabilities, arg_shareswa):
    return _bs_zscore(_f14_balance_sheet_snapshot_liab_shares_ratio(arg_liabilities, arg_shareswa), 756)

def f14_balance_sheet_snapshot_zscore_liab_shares_1260(arg_liabilities, arg_shareswa):
    return _bs_zscore(_f14_balance_sheet_snapshot_liab_shares_ratio(arg_liabilities, arg_shareswa), 1260)

# Base 106-150: Z-scores of raw inputs
def f14_balance_sheet_snapshot_zscore_equity_63(arg_equity):
    return _bs_zscore(arg_equity, 63)

def f14_balance_sheet_snapshot_zscore_equity_126(arg_equity):
    return _bs_zscore(arg_equity, 126)

def f14_balance_sheet_snapshot_zscore_equity_252(arg_equity):
    return _bs_zscore(arg_equity, 252)

def f14_balance_sheet_snapshot_zscore_equity_504(arg_equity):
    return _bs_zscore(arg_equity, 504)

def f14_balance_sheet_snapshot_zscore_equity_756(arg_equity):
    return _bs_zscore(arg_equity, 756)

def f14_balance_sheet_snapshot_zscore_equity_1260(arg_equity):
    return _bs_zscore(arg_equity, 1260)

def f14_balance_sheet_snapshot_zscore_debt_63(arg_debt):
    return _bs_zscore(arg_debt, 63)

def f14_balance_sheet_snapshot_zscore_debt_126(arg_debt):
    return _bs_zscore(arg_debt, 126)

def f14_balance_sheet_snapshot_zscore_debt_252(arg_debt):
    return _bs_zscore(arg_debt, 252)

def f14_balance_sheet_snapshot_zscore_debt_504(arg_debt):
    return _bs_zscore(arg_debt, 504)

def f14_balance_sheet_snapshot_zscore_debt_756(arg_debt):
    return _bs_zscore(arg_debt, 756)

def f14_balance_sheet_snapshot_zscore_debt_1260(arg_debt):
    return _bs_zscore(arg_debt, 1260)

def f14_balance_sheet_snapshot_zscore_assets_63(arg_assets):
    return _bs_zscore(arg_assets, 63)

def f14_balance_sheet_snapshot_zscore_assets_126(arg_assets):
    return _bs_zscore(arg_assets, 126)

def f14_balance_sheet_snapshot_zscore_assets_252(arg_assets):
    return _bs_zscore(arg_assets, 252)

def f14_balance_sheet_snapshot_zscore_assets_504(arg_assets):
    return _bs_zscore(arg_assets, 504)

def f14_balance_sheet_snapshot_zscore_assets_756(arg_assets):
    return _bs_zscore(arg_assets, 756)

def f14_balance_sheet_snapshot_zscore_assets_1260(arg_assets):
    return _bs_zscore(arg_assets, 1260)

def f14_balance_sheet_snapshot_zscore_liabilities_63(arg_liabilities):
    return _bs_zscore(arg_liabilities, 63)

def f14_balance_sheet_snapshot_zscore_liabilities_126(arg_liabilities):
    return _bs_zscore(arg_liabilities, 126)

def f14_balance_sheet_snapshot_zscore_liabilities_252(arg_liabilities):
    return _bs_zscore(arg_liabilities, 252)

def f14_balance_sheet_snapshot_zscore_liabilities_504(arg_liabilities):
    return _bs_zscore(arg_liabilities, 504)

def f14_balance_sheet_snapshot_zscore_liabilities_756(arg_liabilities):
    return _bs_zscore(arg_liabilities, 756)

def f14_balance_sheet_snapshot_zscore_liabilities_1260(arg_liabilities):
    return _bs_zscore(arg_liabilities, 1260)

def f14_balance_sheet_snapshot_zscore_workingcapital_63(arg_workingcapital):
    return _bs_zscore(arg_workingcapital, 63)

def f14_balance_sheet_snapshot_zscore_workingcapital_126(arg_workingcapital):
    return _bs_zscore(arg_workingcapital, 126)

def f14_balance_sheet_snapshot_zscore_workingcapital_252(arg_workingcapital):
    return _bs_zscore(arg_workingcapital, 252)

def f14_balance_sheet_snapshot_zscore_workingcapital_504(arg_workingcapital):
    return _bs_zscore(arg_workingcapital, 504)

def f14_balance_sheet_snapshot_zscore_workingcapital_756(arg_workingcapital):
    return _bs_zscore(arg_workingcapital, 756)

def f14_balance_sheet_snapshot_zscore_workingcapital_1260(arg_workingcapital):
    return _bs_zscore(arg_workingcapital, 1260)

def f14_balance_sheet_snapshot_zscore_currentratio_63(arg_currentratio):
    return _bs_zscore(arg_currentratio, 63)

def f14_balance_sheet_snapshot_zscore_currentratio_126(arg_currentratio):
    return _bs_zscore(arg_currentratio, 126)

def f14_balance_sheet_snapshot_zscore_currentratio_252(arg_currentratio):
    return _bs_zscore(arg_currentratio, 252)

def f14_balance_sheet_snapshot_zscore_currentratio_504(arg_currentratio):
    return _bs_zscore(arg_currentratio, 504)

def f14_balance_sheet_snapshot_zscore_currentratio_756(arg_currentratio):
    return _bs_zscore(arg_currentratio, 756)

def f14_balance_sheet_snapshot_zscore_currentratio_1260(arg_currentratio):
    return _bs_zscore(arg_currentratio, 1260)

def f14_balance_sheet_snapshot_zscore_retearn_63(arg_retearn):
    return _bs_zscore(arg_retearn, 63)

def f14_balance_sheet_snapshot_zscore_retearn_126(arg_retearn):
    return _bs_zscore(arg_retearn, 126)

def f14_balance_sheet_snapshot_zscore_retearn_252(arg_retearn):
    return _bs_zscore(arg_retearn, 252)

def f14_balance_sheet_snapshot_zscore_retearn_504(arg_retearn):
    return _bs_zscore(arg_retearn, 504)

def f14_balance_sheet_snapshot_zscore_retearn_756(arg_retearn):
    return _bs_zscore(arg_retearn, 756)

def f14_balance_sheet_snapshot_zscore_retearn_1260(arg_retearn):
    return _bs_zscore(arg_retearn, 1260)

def f14_balance_sheet_snapshot_zscore_shareswa_63(arg_shareswa):
    return _bs_zscore(arg_shareswa, 63)

def f14_balance_sheet_snapshot_zscore_shareswa_126(arg_shareswa):
    return _bs_zscore(arg_shareswa, 126)

def f14_balance_sheet_snapshot_zscore_shareswa_252(arg_shareswa):
    return _bs_zscore(arg_shareswa, 252)

def test_features():
    # Synthetic data
    n = 2000
    data = {
        'equity': pd.Series(np.random.uniform(100, 1000, n)),
        'debt': pd.Series(np.random.uniform(50, 500, n)),
        'assets': pd.Series(np.random.uniform(200, 2000, n)),
        'liabilities': pd.Series(np.random.uniform(100, 1000, n)),
        'workingcapital': pd.Series(np.random.uniform(-100, 500, n)),
        'currentratio': pd.Series(np.random.uniform(0.5, 3.0, n)),
        'retearn': pd.Series(np.random.uniform(10, 500, n)),
        'shareswa': pd.Series(np.random.uniform(1, 100, n)),
    }
    
    functions = [obj for name, obj in globals().items()
                 if (inspect.isfunction(obj) and name.startswith('f14_balance_sheet_snapshot_'))]
    
    for func in functions:
        sig = inspect.signature(func)
        args = {param: data[param.replace('arg_', '')] for param in sig.parameters}
        res = func(**args)
        
        assert len(res) > 0, f"Function {func.__name__} returned empty result"
        assert res.nunique() > 2, f"Function {func.__name__} has too few unique values"
        assert res.std() > 0, f"Function {func.__name__} has zero standard deviation"

if __name__ == "__main__":
    test_features()
    print("All tests passed!")
