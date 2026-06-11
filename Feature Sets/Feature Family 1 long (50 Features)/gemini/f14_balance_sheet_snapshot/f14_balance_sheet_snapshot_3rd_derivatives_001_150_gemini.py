import pandas as pd
import numpy as np
import inspect

def _bs_ratio(num, den):
    return num / den.replace(0, np.nan)

def _bs_zscore(s, w):
    return (s - s.rolling(w, min_periods=1).mean()) / s.rolling(w, min_periods=1).std().replace(0, np.nan)

def _bs_jerk(s):
    return s.diff().diff()

# Jerk 001-015: 2nd derivative of Core Ratios
def f14_balance_sheet_snapshot_jerk_debt_equity_ratio(arg_debt, arg_equity):
    return _bs_jerk(_bs_ratio(arg_debt, arg_equity))

def f14_balance_sheet_snapshot_jerk_debt_assets_ratio(arg_debt, arg_assets):
    return _bs_jerk(_bs_ratio(arg_debt, arg_assets))

def f14_balance_sheet_snapshot_jerk_equity_assets_ratio(arg_equity, arg_assets):
    return _bs_jerk(_bs_ratio(arg_equity, arg_assets))

def f14_balance_sheet_snapshot_jerk_retearn_assets_ratio(arg_retearn, arg_assets):
    return _bs_jerk(_bs_ratio(arg_retearn, arg_assets))

def f14_balance_sheet_snapshot_jerk_wc_assets_ratio(arg_workingcapital, arg_assets):
    return _bs_jerk(_bs_ratio(arg_workingcapital, arg_assets))

def f14_balance_sheet_snapshot_jerk_bvps(arg_equity, arg_shareswa):
    return _bs_jerk(_bs_ratio(arg_equity, arg_shareswa))

def f14_balance_sheet_snapshot_jerk_liab_assets_ratio(arg_liabilities, arg_assets):
    return _bs_jerk(_bs_ratio(arg_liabilities, arg_assets))

def f14_balance_sheet_snapshot_jerk_debt_liab_ratio(arg_debt, arg_liabilities):
    return _bs_jerk(_bs_ratio(arg_debt, arg_liabilities))

def f14_balance_sheet_snapshot_jerk_wc_equity_ratio(arg_workingcapital, arg_equity):
    return _bs_jerk(_bs_ratio(arg_workingcapital, arg_equity))

def f14_balance_sheet_snapshot_jerk_equity_liab_ratio(arg_equity, arg_liabilities):
    return _bs_jerk(_bs_ratio(arg_equity, arg_liabilities))

def f14_balance_sheet_snapshot_jerk_wc_liab_ratio(arg_workingcapital, arg_liabilities):
    return _bs_jerk(_bs_ratio(arg_workingcapital, arg_liabilities))

def f14_balance_sheet_snapshot_jerk_retearn_equity_ratio(arg_retearn, arg_equity):
    return _bs_jerk(_bs_ratio(arg_retearn, arg_equity))

def f14_balance_sheet_snapshot_jerk_debt_wc_ratio(arg_debt, arg_workingcapital):
    return _bs_jerk(_bs_ratio(arg_debt, arg_workingcapital))

def f14_balance_sheet_snapshot_jerk_assets_shares_ratio(arg_assets, arg_shareswa):
    return _bs_jerk(_bs_ratio(arg_assets, arg_shareswa))

def f14_balance_sheet_snapshot_jerk_liab_shares_ratio(arg_liabilities, arg_shareswa):
    return _bs_jerk(_bs_ratio(arg_liabilities, arg_shareswa))

# Jerk 016-105: 2nd derivative of Z-scores of core ratios
WINDOWS = [63, 126, 252, 504, 756, 1260]
CORE_RATIO_FUNCS = [
    ('debt_equity', lambda d, e: _bs_ratio(d, e), ['arg_debt', 'arg_equity']),
    ('debt_assets', lambda d, a: _bs_ratio(d, a), ['arg_debt', 'arg_assets']),
    ('equity_assets', lambda e, a: _bs_ratio(e, a), ['arg_equity', 'arg_assets']),
    ('retearn_assets', lambda r, a: _bs_ratio(r, a), ['arg_retearn', 'arg_assets']),
    ('wc_assets', lambda wc, a: _bs_ratio(wc, a), ['arg_workingcapital', 'arg_assets']),
    ('bvps', lambda e, s: _bs_ratio(e, s), ['arg_equity', 'arg_shareswa']),
    ('liab_assets', lambda l, a: _bs_ratio(l, a), ['arg_liabilities', 'arg_assets']),
    ('debt_liab', lambda d, l: _bs_ratio(d, l), ['arg_debt', 'arg_liabilities']),
    ('wc_equity', lambda wc, e: _bs_ratio(wc, e), ['arg_workingcapital', 'arg_equity']),
    ('equity_liab', lambda e, l: _bs_ratio(e, l), ['arg_equity', 'arg_liabilities']),
    ('wc_liab', lambda wc, l: _bs_ratio(wc, l), ['arg_workingcapital', 'arg_liabilities']),
    ('retearn_equity', lambda r, e: _bs_ratio(r, e), ['arg_retearn', 'arg_equity']),
    ('debt_wc', lambda d, wc: _bs_ratio(d, wc), ['arg_debt', 'arg_workingcapital']),
    ('assets_shares', lambda a, s: _bs_ratio(a, s), ['arg_assets', 'arg_shareswa']),
    ('liab_shares', lambda l, s: _bs_ratio(l, s), ['arg_liabilities', 'arg_shareswa']),
]

for base_name, base_fn, ratio_args in CORE_RATIO_FUNCS:
    for w in WINDOWS:
        func_name = f"f14_balance_sheet_snapshot_jerk_zscore_{base_name}_{w}"
        def make_func(bfn, window, rargs):
            return lambda **kwargs: _bs_jerk(_bs_zscore(bfn(*[kwargs[a] for a in rargs]), window))
        globals()[func_name] = make_func(base_fn, w, ratio_args)
        # Update signature for inspect
        globals()[func_name].__signature__ = inspect.Signature([inspect.Parameter(a, inspect.Parameter.POSITIONAL_OR_KEYWORD) for a in ratio_args])

# Jerk 106-150: 2nd derivative of Z-scores of raw inputs
INPUTS = ['equity', 'debt', 'assets', 'liabilities', 'workingcapital', 'currentratio', 'retearn', 'shareswa']
for inp in INPUTS:
    for w in WINDOWS:
        if len([f for f in globals() if f.startswith('f14_balance_sheet_snapshot_jerk_')]) >= 150:
             break
        func_name = f"f14_balance_sheet_snapshot_jerk_zscore_{inp}_{w}"
        arg_name = f"arg_{inp}"
        def make_inp_func(window, aname):
            return lambda **kwargs: _bs_jerk(_bs_zscore(kwargs[aname], window))
        globals()[func_name] = make_inp_func(w, arg_name)
        globals()[func_name].__signature__ = inspect.Signature([inspect.Parameter(arg_name, inspect.Parameter.POSITIONAL_OR_KEYWORD)])

def test_features():
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
    
    functions = [obj for name, obj in globals().items() if name.startswith('f14_balance_sheet_snapshot_jerk_')]
    print(f"Testing {len(functions)} jerk features")
    
    for func in functions:
        sig = inspect.signature(func)
        args = {param: data[param.replace('arg_', '')] for param in sig.parameters}
        res = func(**args)
        
        assert len(res) > 0, f"Function {func.__name__} returned empty result"
        valid = res.dropna()
        if len(valid) > 10:
            assert valid.nunique() > 2, f"Function {func} has too few unique values"
            assert valid.std() > 0, f"Function {func} has zero standard deviation"

if __name__ == "__main__":
    test_features()
    print("All tests passed!")
