import pandas as pd
import numpy as np
import inspect

def _bs_ratio(num, den):
    return num / den.replace(0, np.nan)

def _bs_zscore(s, w):
    return (s - s.rolling(w, min_periods=1).mean()) / s.rolling(w, min_periods=1).std().replace(0, np.nan)

# Base 001-015: Core Ratios
def f14_balance_sheet_snapshot_debt_equity_ratio(arg_debt, arg_equity):
    return _bs_ratio(arg_debt, arg_equity)

def f14_balance_sheet_snapshot_debt_assets_ratio(arg_debt, arg_assets):
    return _bs_ratio(arg_debt, arg_assets)

def f14_balance_sheet_snapshot_equity_assets_ratio(arg_equity, arg_assets):
    return _bs_ratio(arg_equity, arg_assets)

def f14_balance_sheet_snapshot_retearn_assets_ratio(arg_retearn, arg_assets):
    return _bs_ratio(arg_retearn, arg_assets)

def f14_balance_sheet_snapshot_wc_assets_ratio(arg_workingcapital, arg_assets):
    return _bs_ratio(arg_workingcapital, arg_assets)

def f14_balance_sheet_snapshot_bvps(arg_equity, arg_shareswa):
    return _bs_ratio(arg_equity, arg_shareswa)

def f14_balance_sheet_snapshot_liab_assets_ratio(arg_liabilities, arg_assets):
    return _bs_ratio(arg_liabilities, arg_assets)

def f14_balance_sheet_snapshot_debt_liab_ratio(arg_debt, arg_liabilities):
    return _bs_ratio(arg_debt, arg_liabilities)

def f14_balance_sheet_snapshot_wc_equity_ratio(arg_workingcapital, arg_equity):
    return _bs_ratio(arg_workingcapital, arg_equity)

def f14_balance_sheet_snapshot_equity_liab_ratio(arg_equity, arg_liabilities):
    return _bs_ratio(arg_equity, arg_liabilities)

def f14_balance_sheet_snapshot_wc_liab_ratio(arg_workingcapital, arg_liabilities):
    return _bs_ratio(arg_workingcapital, arg_liabilities)

def f14_balance_sheet_snapshot_retearn_equity_ratio(arg_retearn, arg_equity):
    return _bs_ratio(arg_retearn, arg_equity)

def f14_balance_sheet_snapshot_debt_wc_ratio(arg_debt, arg_workingcapital):
    return _bs_ratio(arg_debt, arg_workingcapital)

def f14_balance_sheet_snapshot_assets_shares_ratio(arg_assets, arg_shareswa):
    return _bs_ratio(arg_assets, arg_shareswa)

def f14_balance_sheet_snapshot_liab_shares_ratio(arg_liabilities, arg_shareswa):
    return _bs_ratio(arg_liabilities, arg_shareswa)

# Base 016-075: Z-scores of core ratios (Part 1)
# Ratios 1-10 across 6 windows = 60 features
WINDOWS = [63, 126, 252, 504, 756, 1260]

def f14_balance_sheet_snapshot_zscore_debt_equity_63(arg_debt, arg_equity):
    return _bs_zscore(f14_balance_sheet_snapshot_debt_equity_ratio(arg_debt, arg_equity), 63)

def f14_balance_sheet_snapshot_zscore_debt_equity_126(arg_debt, arg_equity):
    return _bs_zscore(f14_balance_sheet_snapshot_debt_equity_ratio(arg_debt, arg_equity), 126)

def f14_balance_sheet_snapshot_zscore_debt_equity_252(arg_debt, arg_equity):
    return _bs_zscore(f14_balance_sheet_snapshot_debt_equity_ratio(arg_debt, arg_equity), 252)

def f14_balance_sheet_snapshot_zscore_debt_equity_504(arg_debt, arg_equity):
    return _bs_zscore(f14_balance_sheet_snapshot_debt_equity_ratio(arg_debt, arg_equity), 504)

def f14_balance_sheet_snapshot_zscore_debt_equity_756(arg_debt, arg_equity):
    return _bs_zscore(f14_balance_sheet_snapshot_debt_equity_ratio(arg_debt, arg_equity), 756)

def f14_balance_sheet_snapshot_zscore_debt_equity_1260(arg_debt, arg_equity):
    return _bs_zscore(f14_balance_sheet_snapshot_debt_equity_ratio(arg_debt, arg_equity), 1260)

def f14_balance_sheet_snapshot_zscore_debt_assets_63(arg_debt, arg_assets):
    return _bs_zscore(f14_balance_sheet_snapshot_debt_assets_ratio(arg_debt, arg_assets), 63)

def f14_balance_sheet_snapshot_zscore_debt_assets_126(arg_debt, arg_assets):
    return _bs_zscore(f14_balance_sheet_snapshot_debt_assets_ratio(arg_debt, arg_assets), 126)

def f14_balance_sheet_snapshot_zscore_debt_assets_252(arg_debt, arg_assets):
    return _bs_zscore(f14_balance_sheet_snapshot_debt_assets_ratio(arg_debt, arg_assets), 252)

def f14_balance_sheet_snapshot_zscore_debt_assets_504(arg_debt, arg_assets):
    return _bs_zscore(f14_balance_sheet_snapshot_debt_assets_ratio(arg_debt, arg_assets), 504)

def f14_balance_sheet_snapshot_zscore_debt_assets_756(arg_debt, arg_assets):
    return _bs_zscore(f14_balance_sheet_snapshot_debt_assets_ratio(arg_debt, arg_assets), 756)

def f14_balance_sheet_snapshot_zscore_debt_assets_1260(arg_debt, arg_assets):
    return _bs_zscore(f14_balance_sheet_snapshot_debt_assets_ratio(arg_debt, arg_assets), 1260)

def f14_balance_sheet_snapshot_zscore_equity_assets_63(arg_equity, arg_assets):
    return _bs_zscore(f14_balance_sheet_snapshot_equity_assets_ratio(arg_equity, arg_assets), 63)

def f14_balance_sheet_snapshot_zscore_equity_assets_126(arg_equity, arg_assets):
    return _bs_zscore(f14_balance_sheet_snapshot_equity_assets_ratio(arg_equity, arg_assets), 126)

def f14_balance_sheet_snapshot_zscore_equity_assets_252(arg_equity, arg_assets):
    return _bs_zscore(f14_balance_sheet_snapshot_equity_assets_ratio(arg_equity, arg_assets), 252)

def f14_balance_sheet_snapshot_zscore_equity_assets_504(arg_equity, arg_assets):
    return _bs_zscore(f14_balance_sheet_snapshot_equity_assets_ratio(arg_equity, arg_assets), 504)

def f14_balance_sheet_snapshot_zscore_equity_assets_756(arg_equity, arg_assets):
    return _bs_zscore(f14_balance_sheet_snapshot_equity_assets_ratio(arg_equity, arg_assets), 756)

def f14_balance_sheet_snapshot_zscore_equity_assets_1260(arg_equity, arg_assets):
    return _bs_zscore(f14_balance_sheet_snapshot_equity_assets_ratio(arg_equity, arg_assets), 1260)

def f14_balance_sheet_snapshot_zscore_retearn_assets_63(arg_retearn, arg_assets):
    return _bs_zscore(f14_balance_sheet_snapshot_retearn_assets_ratio(arg_retearn, arg_assets), 63)

def f14_balance_sheet_snapshot_zscore_retearn_assets_126(arg_retearn, arg_assets):
    return _bs_zscore(f14_balance_sheet_snapshot_retearn_assets_ratio(arg_retearn, arg_assets), 126)

def f14_balance_sheet_snapshot_zscore_retearn_assets_252(arg_retearn, arg_assets):
    return _bs_zscore(f14_balance_sheet_snapshot_retearn_assets_ratio(arg_retearn, arg_assets), 252)

def f14_balance_sheet_snapshot_zscore_retearn_assets_504(arg_retearn, arg_assets):
    return _bs_zscore(f14_balance_sheet_snapshot_retearn_assets_ratio(arg_retearn, arg_assets), 504)

def f14_balance_sheet_snapshot_zscore_retearn_assets_756(arg_retearn, arg_assets):
    return _bs_zscore(f14_balance_sheet_snapshot_retearn_assets_ratio(arg_retearn, arg_assets), 756)

def f14_balance_sheet_snapshot_zscore_retearn_assets_1260(arg_retearn, arg_assets):
    return _bs_zscore(f14_balance_sheet_snapshot_retearn_assets_ratio(arg_retearn, arg_assets), 1260)

def f14_balance_sheet_snapshot_zscore_wc_assets_63(arg_workingcapital, arg_assets):
    return _bs_zscore(f14_balance_sheet_snapshot_wc_assets_ratio(arg_workingcapital, arg_assets), 63)

def f14_balance_sheet_snapshot_zscore_wc_assets_126(arg_workingcapital, arg_assets):
    return _bs_zscore(f14_balance_sheet_snapshot_wc_assets_ratio(arg_workingcapital, arg_assets), 126)

def f14_balance_sheet_snapshot_zscore_wc_assets_252(arg_workingcapital, arg_assets):
    return _bs_zscore(f14_balance_sheet_snapshot_wc_assets_ratio(arg_workingcapital, arg_assets), 252)

def f14_balance_sheet_snapshot_zscore_wc_assets_504(arg_workingcapital, arg_assets):
    return _bs_zscore(f14_balance_sheet_snapshot_wc_assets_ratio(arg_workingcapital, arg_assets), 504)

def f14_balance_sheet_snapshot_zscore_wc_assets_756(arg_workingcapital, arg_assets):
    return _bs_zscore(f14_balance_sheet_snapshot_wc_assets_ratio(arg_workingcapital, arg_assets), 756)

def f14_balance_sheet_snapshot_zscore_wc_assets_1260(arg_workingcapital, arg_assets):
    return _bs_zscore(f14_balance_sheet_snapshot_wc_assets_ratio(arg_workingcapital, arg_assets), 1260)

def f14_balance_sheet_snapshot_zscore_bvps_63(arg_equity, arg_shareswa):
    return _bs_zscore(f14_balance_sheet_snapshot_bvps(arg_equity, arg_shareswa), 63)

def f14_balance_sheet_snapshot_zscore_bvps_126(arg_equity, arg_shareswa):
    return _bs_zscore(f14_balance_sheet_snapshot_bvps(arg_equity, arg_shareswa), 126)

def f14_balance_sheet_snapshot_zscore_bvps_252(arg_equity, arg_shareswa):
    return _bs_zscore(f14_balance_sheet_snapshot_bvps(arg_equity, arg_shareswa), 252)

def f14_balance_sheet_snapshot_zscore_bvps_504(arg_equity, arg_shareswa):
    return _bs_zscore(f14_balance_sheet_snapshot_bvps(arg_equity, arg_shareswa), 504)

def f14_balance_sheet_snapshot_zscore_bvps_756(arg_equity, arg_shareswa):
    return _bs_zscore(f14_balance_sheet_snapshot_bvps(arg_equity, arg_shareswa), 756)

def f14_balance_sheet_snapshot_zscore_bvps_1260(arg_equity, arg_shareswa):
    return _bs_zscore(f14_balance_sheet_snapshot_bvps(arg_equity, arg_shareswa), 1260)

def f14_balance_sheet_snapshot_zscore_liab_assets_63(arg_liabilities, arg_assets):
    return _bs_zscore(f14_balance_sheet_snapshot_liab_assets_ratio(arg_liabilities, arg_assets), 63)

def f14_balance_sheet_snapshot_zscore_liab_assets_126(arg_liabilities, arg_assets):
    return _bs_zscore(f14_balance_sheet_snapshot_liab_assets_ratio(arg_liabilities, arg_assets), 126)

def f14_balance_sheet_snapshot_zscore_liab_assets_252(arg_liabilities, arg_assets):
    return _bs_zscore(f14_balance_sheet_snapshot_liab_assets_ratio(arg_liabilities, arg_assets), 252)

def f14_balance_sheet_snapshot_zscore_liab_assets_504(arg_liabilities, arg_assets):
    return _bs_zscore(f14_balance_sheet_snapshot_liab_assets_ratio(arg_liabilities, arg_assets), 504)

def f14_balance_sheet_snapshot_zscore_liab_assets_756(arg_liabilities, arg_assets):
    return _bs_zscore(f14_balance_sheet_snapshot_liab_assets_ratio(arg_liabilities, arg_assets), 756)

def f14_balance_sheet_snapshot_zscore_liab_assets_1260(arg_liabilities, arg_assets):
    return _bs_zscore(f14_balance_sheet_snapshot_liab_assets_ratio(arg_liabilities, arg_assets), 1260)

def f14_balance_sheet_snapshot_zscore_debt_liab_63(arg_debt, arg_liabilities):
    return _bs_zscore(f14_balance_sheet_snapshot_debt_liab_ratio(arg_debt, arg_liabilities), 63)

def f14_balance_sheet_snapshot_zscore_debt_liab_126(arg_debt, arg_liabilities):
    return _bs_zscore(f14_balance_sheet_snapshot_debt_liab_ratio(arg_debt, arg_liabilities), 126)

def f14_balance_sheet_snapshot_zscore_debt_liab_252(arg_debt, arg_liabilities):
    return _bs_zscore(f14_balance_sheet_snapshot_debt_liab_ratio(arg_debt, arg_liabilities), 252)

def f14_balance_sheet_snapshot_zscore_debt_liab_504(arg_debt, arg_liabilities):
    return _bs_zscore(f14_balance_sheet_snapshot_debt_liab_ratio(arg_debt, arg_liabilities), 504)

def f14_balance_sheet_snapshot_zscore_debt_liab_756(arg_debt, arg_liabilities):
    return _bs_zscore(f14_balance_sheet_snapshot_debt_liab_ratio(arg_debt, arg_liabilities), 756)

def f14_balance_sheet_snapshot_zscore_debt_liab_1260(arg_debt, arg_liabilities):
    return _bs_zscore(f14_balance_sheet_snapshot_debt_liab_ratio(arg_debt, arg_liabilities), 1260)

def f14_balance_sheet_snapshot_zscore_wc_equity_63(arg_workingcapital, arg_equity):
    return _bs_zscore(f14_balance_sheet_snapshot_wc_equity_ratio(arg_workingcapital, arg_equity), 63)

def f14_balance_sheet_snapshot_zscore_wc_equity_126(arg_workingcapital, arg_equity):
    return _bs_zscore(f14_balance_sheet_snapshot_wc_equity_ratio(arg_workingcapital, arg_equity), 126)

def f14_balance_sheet_snapshot_zscore_wc_equity_252(arg_workingcapital, arg_equity):
    return _bs_zscore(f14_balance_sheet_snapshot_wc_equity_ratio(arg_workingcapital, arg_equity), 252)

def f14_balance_sheet_snapshot_zscore_wc_equity_504(arg_workingcapital, arg_equity):
    return _bs_zscore(f14_balance_sheet_snapshot_wc_equity_ratio(arg_workingcapital, arg_equity), 504)

def f14_balance_sheet_snapshot_zscore_wc_equity_756(arg_workingcapital, arg_equity):
    return _bs_zscore(f14_balance_sheet_snapshot_wc_equity_ratio(arg_workingcapital, arg_equity), 756)

def f14_balance_sheet_snapshot_zscore_wc_equity_1260(arg_workingcapital, arg_equity):
    return _bs_zscore(f14_balance_sheet_snapshot_wc_equity_ratio(arg_workingcapital, arg_equity), 1260)

def f14_balance_sheet_snapshot_zscore_equity_liab_63(arg_equity, arg_liabilities):
    return _bs_zscore(f14_balance_sheet_snapshot_equity_liab_ratio(arg_equity, arg_liabilities), 63)

def f14_balance_sheet_snapshot_zscore_equity_liab_126(arg_equity, arg_liabilities):
    return _bs_zscore(f14_balance_sheet_snapshot_equity_liab_ratio(arg_equity, arg_liabilities), 126)

def f14_balance_sheet_snapshot_zscore_equity_liab_252(arg_equity, arg_liabilities):
    return _bs_zscore(f14_balance_sheet_snapshot_equity_liab_ratio(arg_equity, arg_liabilities), 252)

def f14_balance_sheet_snapshot_zscore_equity_liab_504(arg_equity, arg_liabilities):
    return _bs_zscore(f14_balance_sheet_snapshot_equity_liab_ratio(arg_equity, arg_liabilities), 504)

def f14_balance_sheet_snapshot_zscore_equity_liab_756(arg_equity, arg_liabilities):
    return _bs_zscore(f14_balance_sheet_snapshot_equity_liab_ratio(arg_equity, arg_liabilities), 756)

def f14_balance_sheet_snapshot_zscore_equity_liab_1260(arg_equity, arg_liabilities):
    return _bs_zscore(f14_balance_sheet_snapshot_equity_liab_ratio(arg_equity, arg_liabilities), 1260)

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
