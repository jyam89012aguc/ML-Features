import sys, numpy as np, pandas as pd, importlib.util, traceback

base = r'C:\Users\jyama\Desktop\need to move\capitulation 1a claude\114_overnight_intraday_split'
N = 300

np.random.seed(42)
close = pd.Series(50.0 + np.cumsum(np.random.randn(N) * 0.5), name='close')
close = close.clip(lower=1.0)
open_ = close.shift(1).fillna(close.iloc[0]) * (1 + np.random.randn(N) * 0.005)
open_ = open_.clip(lower=0.5)
high = pd.concat([close, open_], axis=1).max(axis=1) * (1 + np.abs(np.random.randn(N) * 0.003))
low  = pd.concat([close, open_], axis=1).min(axis=1) * (1 - np.abs(np.random.randn(N) * 0.003))
low  = low.clip(lower=0.1)
volume = pd.Series(np.abs(np.random.randn(N) * 1e6) + 1e5)

data = {'close': close, 'open': open_, 'high': high, 'low': low, 'volume': volume}

files = [
    ('114_overnight_intraday_split_base_001_075.py', 'OVERNIGHT_INTRADAY_SPLIT_REGISTRY_001_075', 75),
    ('114_overnight_intraday_split_base_076_150.py', 'OVERNIGHT_INTRADAY_SPLIT_REGISTRY_076_150', 75),
    ('114_overnight_intraday_split_2nd_derivatives.py', 'OVERNIGHT_INTRADAY_SPLIT_REGISTRY_2ND_DERIVATIVES', 25),
    ('114_overnight_intraday_split_3rd_derivatives.py', 'OVERNIGHT_INTRADAY_SPLIT_REGISTRY_3RD_DERIVATIVES', 25),
    ('114_overnight_intraday_split_extended_001_075.py', 'OVERNIGHT_INTRADAY_SPLIT_EXTENDED_REGISTRY_001_075', 75),
]

all_ok = True
for fname, reg_name, expected_count in files:
    fpath = base + '\\' + fname
    spec = importlib.util.spec_from_file_location('mod_' + fname[:10], fpath)
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except Exception as e:
        print(f'IMPORT FAIL {fname}: {e}')
        all_ok = False
        continue
    registry = getattr(mod, reg_name, None)
    if registry is None:
        print(f'REGISTRY NOT FOUND: {reg_name} in {fname}')
        all_ok = False
        continue
    count = len(registry)
    errors = []
    for feat_name, meta in registry.items():
        func = meta['func']
        inputs = meta['inputs']
        args = [data[k] for k in inputs]
        try:
            result = func(*args)
            if not isinstance(result, pd.Series):
                errors.append(f'{feat_name}: returned {type(result).__name__}, not Series')
        except Exception as e:
            errors.append(f'{feat_name}: {type(e).__name__}: {e}')
    status = 'SMOKE_OK' if not errors else f'SMOKE_ERRORS({len(errors)})'
    count_ok = 'COUNT_OK' if count == expected_count else f'COUNT_WRONG({count}!={expected_count})'
    print(f'{fname}: {count_ok} {status}')
    for err in errors:
        print('  ERROR:', err)
    if errors or count != expected_count:
        all_ok = False

print()
print('ALL CLEAN' if all_ok else 'ISSUES FOUND')
