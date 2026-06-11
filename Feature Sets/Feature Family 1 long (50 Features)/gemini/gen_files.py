
import os
import pandas as pd
import numpy as np
import inspect

def generate_base_file(folder, feature_name, prefix, inputs, start_v, end_v, file_name):
    header = f'''import pandas as pd
import numpy as np
import inspect

def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()

def _{prefix}_ratio(num, den):
    return num / den.replace(0, np.nan)

def _{prefix}_diff(a, b):
    return a - b

def _{prefix}_zscore(s, w):
    sma = _sma(s, w)
    std = _std(s, w)
    return (s - sma) / std.replace(0, np.nan)

'''
    functions = []
    windows = [63, 126, 252, 504, 756, 1260]
    
    count = start_v
    while count <= end_v:
        for i1 in range(len(inputs)):
            for i2 in range(len(inputs)):
                if count > end_v: break
                inp1 = inputs[i1]
                inp2 = inputs[i2]
                w = windows[count % len(windows)]
                
                if inp1 == inp2:
                    func_name = f'{prefix}_{feature_name}_{inp1}_w{w}_v{count:03d}_base_signal'
                    body = f'''# Base feature: {inp1} smoothed by {w}d
def {func_name}({inp1}) -> pd.Series:
    """Calculates the smoothed {inp1} over {w} days."""
    res = _sma({inp1}, {w})
    return res.replace([np.inf, -np.inf], np.nan)

'''
                else:
                    func_name = f'{prefix}_{feature_name}_{inp1}_{inp2}_ratio_w{w}_v{count:03d}_base_signal'
                    body = f'''# Base feature: ratio of {inp1} to {inp2} smoothed by {w}d
def {func_name}({inp1}, {inp2}) -> pd.Series:
    """Calculates the ratio of {inp1} to {inp2} smoothed over {w} days."""
    ratio = _{prefix}_ratio({inp1}, {inp2})
    res = _sma(ratio, {w})
    return res.replace([np.inf, -np.inf], np.nan)

'''
                functions.append(body)
                count += 1

    display_path = file_name.replace('\\', '/')
    footer = f'''
if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 2000
    df = pd.DataFrame({{col: np.random.normal(100, 20, n) for col in {inputs}}})
    for col in {inputs}:
        df[col] = df[col].abs() + 1
            
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('{prefix}_'))]
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        y1 = func(*args)
        assert isinstance(y1, pd.Series), f"{{func.__name__}} did not return a Series"
        assert not y1.isna().all(), f"{{func.__name__}} is all NaNs"
    print(f"All {{len(funcs)}} tests passed for {display_path}!")

REGISTRY = {{fn.__name__: {{"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn}} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('{prefix}_'))]}}
{feature_name.upper()}_REGISTRY_BASE = REGISTRY
'''
    content = header + ''.join(functions) + footer
    with open(file_name, 'w') as f:
        f.write(content)

def generate_slope_file(folder, feature_name, prefix, inputs, file_name):
    header = f'''import pandas as pd
import numpy as np
import inspect

def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()

def _{prefix}_ratio(num, den):
    return num / den.replace(0, np.nan)

def _{prefix}_diff(a, b):
    return a - b

def _{prefix}_slope(s, w):
    return s.diff(w) / s.abs().replace(0, np.nan)

def _{prefix}_zscore(s, w):
    sma = _sma(s, w)
    std = _std(s, w)
    return (s - sma) / std.replace(0, np.nan)

'''
    functions = []
    windows = [63, 126, 252, 504]
    slope_windows = [5, 21, 63]
    
    count = 1
    while count <= 150:
        for i1 in range(len(inputs)):
            for i2 in range(len(inputs)):
                if count > 150: break
                inp1 = inputs[i1]
                inp2 = inputs[i2]
                w = windows[count % len(windows)]
                sw = slope_windows[count % len(slope_windows)]
                
                if inp1 == inp2:
                    func_name = f'{prefix}_{feature_name}_{inp1}_w{w}_sw{sw}_v{count:03d}_slope_signal'
                    body = f'''# Slope feature: {inp1} smoothed by {w}d, slope over {sw}d
def {func_name}({inp1}) -> pd.Series:
    """Calculates the slope of smoothed {inp1} over {sw} days."""
    base = _sma({inp1}, {w})
    res = _{prefix}_slope(base, {sw})
    return res.replace([np.inf, -np.inf], np.nan)

'''
                else:
                    func_name = f'{prefix}_{feature_name}_{inp1}_{inp2}_ratio_w{w}_sw{sw}_v{count:03d}_slope_signal'
                    body = f'''# Slope feature: ratio of {inp1} to {inp2} smoothed by {w}d, slope over {sw}d
def {func_name}({inp1}, {inp2}) -> pd.Series:
    """Calculates the slope of the ratio of {inp1} to {inp2} smoothed over {sw} days."""
    ratio = _{prefix}_ratio({inp1}, {inp2})
    base = _sma(ratio, {w})
    res = _{prefix}_slope(base, {sw})
    return res.replace([np.inf, -np.inf], np.nan)

'''
                functions.append(body)
                count += 1

    display_path = file_name.replace('\\', '/')
    footer = f'''
if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 2000
    df = pd.DataFrame({{col: np.random.normal(100, 20, n) for col in {inputs}}})
    for col in {inputs}:
        df[col] = df[col].abs() + 1
            
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('{prefix}_'))]
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        y1 = func(*args)
        assert isinstance(y1, pd.Series), f"{{func.__name__}} did not return a Series"
        assert not y1.isna().all(), f"{{func.__name__}} is all NaNs"
    print(f"All {{len(funcs)}} tests passed for {display_path}!")

REGISTRY = {{fn.__name__: {{"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn}} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('{prefix}_'))]}}
{feature_name.upper()}_REGISTRY_SLOPE = REGISTRY
'''
    content = header + ''.join(functions) + footer
    with open(file_name, 'w') as f:
        f.write(content)

def generate_jerk_file(folder, feature_name, prefix, inputs, file_name):
    header = f'''import pandas as pd
import numpy as np
import inspect

def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()

def _{prefix}_ratio(num, den):
    return num / den.replace(0, np.nan)

def _{prefix}_diff(a, b):
    return a - b

def _{prefix}_slope(s, w):
    return s.diff(w) / s.abs().replace(0, np.nan)

def _{prefix}_jerk(s, jw):
    return s.diff(jw)

def _{prefix}_zscore(s, w):
    sma = _sma(s, w)
    std = _std(s, w)
    return (s - sma) / std.replace(0, np.nan)

'''
    functions = []
    windows = [63, 126, 252]
    slope_windows = [21, 63]
    jerk_windows = [5, 21]
    
    count = 1
    while count <= 150:
        for i1 in range(len(inputs)):
            for i2 in range(len(inputs)):
                if count > 150: break
                inp1 = inputs[i1]
                inp2 = inputs[i2]
                w = windows[count % len(windows)]
                sw = slope_windows[count % len(slope_windows)]
                jw = jerk_windows[count % len(jerk_windows)]
                
                if inp1 == inp2:
                    func_name = f'{prefix}_{feature_name}_{inp1}_w{w}_sw{sw}_jw{jw}_v{count:03d}_jerk_signal'
                    body = f'''# Jerk feature: {inp1} smoothed by {w}d, slope {sw}d, jerk {jw}d
def {func_name}({inp1}) -> pd.Series:
    """Calculates the jerk of smoothed {inp1}."""
    base = _sma({inp1}, {w})
    slope = _{prefix}_slope(base, {sw})
    res = _{prefix}_jerk(slope, {jw})
    return res.replace([np.inf, -np.inf], np.nan)

'''
                else:
                    func_name = f'{prefix}_{feature_name}_{inp1}_{inp2}_ratio_w{w}_sw{sw}_jw{jw}_v{count:03d}_jerk_signal'
                    body = f'''# Jerk feature: ratio of {inp1} to {inp2} smoothed by {w}d, slope {sw}d, jerk {jw}d
def {func_name}({inp1}, {inp2}) -> pd.Series:
    """Calculates the jerk of the ratio of {inp1} to {inp2} smoothed."""
    ratio = _{prefix}_ratio({inp1}, {inp2})
    base = _sma(ratio, {w})
    slope = _{prefix}_slope(base, {sw})
    res = _{prefix}_jerk(slope, {jw})
    return res.replace([np.inf, -np.inf], np.nan)

'''
                functions.append(body)
                count += 1

    display_path = file_name.replace('\\', '/')
    footer = f'''
if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 2000
    df = pd.DataFrame({{col: np.random.normal(100, 20, n) for col in {inputs}}})
    for col in {inputs}:
        df[col] = df[col].abs() + 1
            
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('{prefix}_'))]
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        y1 = func(*args)
        assert isinstance(y1, pd.Series), f"{{func.__name__}} did not return a Series"
        assert not y1.isna().all(), f"{{func.__name__}} is all NaNs"
    print(f"All {{len(funcs)}} tests passed for {display_path}!")

REGISTRY = {{fn.__name__: {{"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn}} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('{prefix}_'))]}}
{feature_name.upper()}_REGISTRY_JERK = REGISTRY
'''
    content = header + ''.join(functions) + footer
    with open(file_name, 'w') as f:
        f.write(content)

# Define configurations for each folder
configs = [
    {
        'folder': 'f25_growth_vs_cost',
        'feature_name': 'f25_growth_vs_cost',
        'prefix': 'f25gvc',
        'inputs': ['revenue', 'capex', 'assets', 'opinc', 'ebitda', 'netinc']
    },
    {
        'folder': 'f26_dilution_rate',
        'feature_name': 'f26_dilution_rate',
        'prefix': 'f26dr',
        'inputs': ['sharesbas', 'revenue', 'netinc', 'assets', 'equity', 'fcf']
    },
    {
        'folder': 'f27_investment_trajectory',
        'feature_name': 'f27_investment_trajectory',
        'prefix': 'f27it',
        'inputs': ['investments', 'capex', 'revenue', 'assets', 'cash', 'debt']
    },
    {
        'folder': 'f28_valuation_trajectory',
        'feature_name': 'f28_valuation_trajectory',
        'prefix': 'f28vt',
        'inputs': ['marketcap', 'ev', 'revenue', 'ebitda', 'netinc', 'assets']
    },
    {
        'folder': 'f29_revenue_acceleration',
        'feature_name': 'f29_revenue_acceleration',
        'prefix': 'f29ra',
        'inputs': ['revenue', 'gp', 'opinc', 'ebitda', 'netinc', 'assets']
    }
]

base_path = r'C:\Users\jyama\Desktop\active_non audited features per AI\gemini\PENDING_20260511_152500 (50 feature family)'

for cfg in configs:
    folder_path = os.path.join(base_path, cfg['folder'])
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Base 001-075
    generate_base_file(cfg['folder'], cfg['feature_name'], cfg['prefix'], cfg['inputs'], 1, 75, os.path.join(folder_path, f"{cfg['feature_name']}_base_001_075_gemini.py"))
    # Base 076-150
    generate_base_file(cfg['folder'], cfg['feature_name'], cfg['prefix'], cfg['inputs'], 76, 150, os.path.join(folder_path, f"{cfg['feature_name']}_base_076_150_gemini.py"))
    # Slope 001-150
    generate_slope_file(cfg['folder'], cfg['feature_name'], cfg['prefix'], cfg['inputs'], os.path.join(folder_path, f"{cfg['feature_name']}_slope_001_150_gemini.py"))
    # Jerk 001-150
    generate_jerk_file(cfg['folder'], cfg['feature_name'], cfg['prefix'], cfg['inputs'], os.path.join(folder_path, f"{cfg['feature_name']}_jerk_001_150_gemini.py"))

