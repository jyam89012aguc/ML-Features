# f02_crash_speed_base_001_075_gemini.py
import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 5)).mean()
def _ema(s, w): return s.ewm(span=w, min_periods=min(w, 5), adjust=False).mean()
def _min(s, w): return s.rolling(w, min_periods=min(w, 5)).min()
def _max(s, w): return s.rolling(w, min_periods=min(w, 5)).max()
def _std(s, w): return s.rolling(w, min_periods=min(w, 5)).std()

def _crash_speed_v(c, w): return c.pct_change(w).clip(upper=0).abs().add(1e-9) / w
def _crash_speed_fastest(c, w, n=1): return c.pct_change(n).rolling(w).min().abs().add(1e-9)
def _crash_speed_accel(c, w): return _crash_speed_v(c, w).diff(1)

def _get_price(open, high, low, close, closeadj, w):
    if w <= 5:
        return (open + high + low + close) / 4
    elif w <= 21:
        return close
    else:
        return closeadj

# --- Family 1: Velocity (001-007) ---
def f02_crash_speed_v_5d_base_v001_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (open + high + low + close) / 4
    return _crash_speed_v(p, 5).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_10d_base_v002_signal(close: pd.Series) -> pd.Series:
    return _crash_speed_v(close, 10).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_21d_base_v003_signal(close: pd.Series) -> pd.Series:
    return _crash_speed_v(close, 21).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_42d_base_v004_signal(closeadj: pd.Series) -> pd.Series:
    return _crash_speed_v(closeadj, 42).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_63d_base_v005_signal(closeadj: pd.Series) -> pd.Series:
    return _crash_speed_v(closeadj, 63).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_126d_base_v006_signal(closeadj: pd.Series) -> pd.Series:
    return _crash_speed_v(closeadj, 126).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_252d_base_v007_signal(closeadj: pd.Series) -> pd.Series:
    return _crash_speed_v(closeadj, 252).replace([np.inf, -np.inf], np.nan)

# --- Family 2: Fastest Crash n=1 (008-014) ---
def f02_crash_speed_fastest_5d_n1_base_v008_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (open + high + low + close) / 4
    return _crash_speed_fastest(p, 5, 1).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_fastest_10d_n1_base_v009_signal(close: pd.Series) -> pd.Series:
    return _crash_speed_fastest(close, 10, 1).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_fastest_21d_n1_base_v010_signal(close: pd.Series) -> pd.Series:
    return _crash_speed_fastest(close, 21, 1).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_fastest_42d_n1_base_v011_signal(closeadj: pd.Series) -> pd.Series:
    return _crash_speed_fastest(closeadj, 42, 1).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_fastest_63d_n1_base_v012_signal(closeadj: pd.Series) -> pd.Series:
    return _crash_speed_fastest(closeadj, 63, 1).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_fastest_126d_n1_base_v013_signal(closeadj: pd.Series) -> pd.Series:
    return _crash_speed_fastest(closeadj, 126, 1).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_fastest_252d_n1_base_v014_signal(closeadj: pd.Series) -> pd.Series:
    return _crash_speed_fastest(closeadj, 252, 1).replace([np.inf, -np.inf], np.nan)

# --- Family 3: Fastest Crash n=3 (015-021) ---
def f02_crash_speed_fastest_5d_n3_base_v015_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (open + high + low + close) / 4
    return _crash_speed_fastest(p, 5, 3).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_fastest_10d_n3_base_v016_signal(close: pd.Series) -> pd.Series:
    return _crash_speed_fastest(close, 10, 3).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_fastest_21d_n3_base_v017_signal(close: pd.Series) -> pd.Series:
    return _crash_speed_fastest(close, 21, 3).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_fastest_42d_n3_base_v018_signal(closeadj: pd.Series) -> pd.Series:
    return _crash_speed_fastest(closeadj, 42, 3).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_fastest_63d_n3_base_v019_signal(closeadj: pd.Series) -> pd.Series:
    return _crash_speed_fastest(closeadj, 63, 3).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_fastest_126d_n3_base_v020_signal(closeadj: pd.Series) -> pd.Series:
    return _crash_speed_fastest(closeadj, 126, 3).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_fastest_252d_n3_base_v021_signal(closeadj: pd.Series) -> pd.Series:
    return _crash_speed_fastest(closeadj, 252, 3).replace([np.inf, -np.inf], np.nan)

# --- Family 4: Fastest Crash n=5 (022-028) ---
def f02_crash_speed_fastest_5d_n5_base_v022_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (open + high + low + close) / 4
    return _crash_speed_fastest(p, 5, 5).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_fastest_10d_n5_base_v023_signal(close: pd.Series) -> pd.Series:
    return _crash_speed_fastest(close, 10, 5).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_fastest_21d_n5_base_v024_signal(close: pd.Series) -> pd.Series:
    return _crash_speed_fastest(close, 21, 5).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_fastest_42d_n5_base_v025_signal(closeadj: pd.Series) -> pd.Series:
    return _crash_speed_fastest(closeadj, 42, 5).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_fastest_63d_n5_base_v026_signal(closeadj: pd.Series) -> pd.Series:
    return _crash_speed_fastest(closeadj, 63, 5).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_fastest_126d_n5_base_v027_signal(closeadj: pd.Series) -> pd.Series:
    return _crash_speed_fastest(closeadj, 126, 5).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_fastest_252d_n5_base_v028_signal(closeadj: pd.Series) -> pd.Series:
    return _crash_speed_fastest(closeadj, 252, 5).replace([np.inf, -np.inf], np.nan)

# --- Family 5: Acceleration (029-035) ---
def f02_crash_speed_accel_5d_base_v029_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (open + high + low + close) / 4
    return _crash_speed_accel(p, 5).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_accel_10d_base_v030_signal(close: pd.Series) -> pd.Series:
    return _crash_speed_accel(close, 10).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_accel_21d_base_v031_signal(close: pd.Series) -> pd.Series:
    return _crash_speed_accel(close, 21).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_accel_42d_base_v032_signal(closeadj: pd.Series) -> pd.Series:
    return _crash_speed_accel(closeadj, 42).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_accel_63d_base_v033_signal(closeadj: pd.Series) -> pd.Series:
    return _crash_speed_accel(closeadj, 63).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_accel_126d_base_v034_signal(closeadj: pd.Series) -> pd.Series:
    return _crash_speed_accel(closeadj, 126).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_accel_252d_base_v035_signal(closeadj: pd.Series) -> pd.Series:
    return _crash_speed_accel(closeadj, 252).replace([np.inf, -np.inf], np.nan)

# --- Family 6: Acceleration 5-day diff (036-042) ---
def f02_crash_speed_accel_5d_diff5_base_v036_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (open + high + low + close) / 4
    return _crash_speed_v(p, 5).diff(5).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_accel_10d_diff5_base_v037_signal(close: pd.Series) -> pd.Series:
    return _crash_speed_v(close, 10).diff(5).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_accel_21d_diff5_base_v038_signal(close: pd.Series) -> pd.Series:
    return _crash_speed_v(close, 21).diff(5).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_accel_42d_diff5_base_v039_signal(closeadj: pd.Series) -> pd.Series:
    return _crash_speed_v(closeadj, 42).diff(5).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_accel_63d_diff5_base_v040_signal(closeadj: pd.Series) -> pd.Series:
    return _crash_speed_v(closeadj, 63).diff(5).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_accel_126d_diff5_base_v041_signal(closeadj: pd.Series) -> pd.Series:
    return _crash_speed_v(closeadj, 126).diff(5).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_accel_252d_diff5_base_v042_signal(closeadj: pd.Series) -> pd.Series:
    return _crash_speed_v(closeadj, 252).diff(5).replace([np.inf, -np.inf], np.nan)

# --- Family 7: Mean Velocity (043-049) ---
def f02_crash_speed_v_mean_5d_base_v043_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (open + high + low + close) / 4
    return _sma(_crash_speed_v(p, 5), 10).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_mean_10d_base_v044_signal(close: pd.Series) -> pd.Series:
    return _sma(_crash_speed_v(close, 10), 20).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_mean_21d_base_v045_signal(close: pd.Series) -> pd.Series:
    return _sma(_crash_speed_v(close, 21), 42).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_mean_42d_base_v046_signal(closeadj: pd.Series) -> pd.Series:
    return _sma(_crash_speed_v(closeadj, 42), 84).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_mean_63d_base_v047_signal(closeadj: pd.Series) -> pd.Series:
    return _sma(_crash_speed_v(closeadj, 63), 126).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_mean_126d_base_v048_signal(closeadj: pd.Series) -> pd.Series:
    return _sma(_crash_speed_v(closeadj, 126), 252).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_mean_252d_base_v049_signal(closeadj: pd.Series) -> pd.Series:
    return _sma(_crash_speed_v(closeadj, 252), 504).replace([np.inf, -np.inf], np.nan)

# --- Family 8: Velocity Std (050-056) ---
def f02_crash_speed_v_std_5d_base_v050_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (open + high + low + close) / 4
    return _std(_crash_speed_v(p, 5), 10).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_std_10d_base_v051_signal(close: pd.Series) -> pd.Series:
    return _std(_crash_speed_v(close, 10), 20).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_std_21d_base_v052_signal(close: pd.Series) -> pd.Series:
    return _std(_crash_speed_v(close, 21), 42).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_std_42d_base_v053_signal(closeadj: pd.Series) -> pd.Series:
    return _std(_crash_speed_v(closeadj, 42), 84).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_std_63d_base_v054_signal(closeadj: pd.Series) -> pd.Series:
    return _std(_crash_speed_v(closeadj, 63), 126).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_std_126d_base_v055_signal(closeadj: pd.Series) -> pd.Series:
    return _std(_crash_speed_v(closeadj, 126), 252).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_std_252d_base_v056_signal(closeadj: pd.Series) -> pd.Series:
    return _std(_crash_speed_v(closeadj, 252), 504).replace([np.inf, -np.inf], np.nan)

# --- Family 9: Velocity Z-score (057-063) ---
def f02_crash_speed_v_z_5d_base_v057_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (open + high + low + close) / 4
    v = _crash_speed_v(p, 5)
    return ((v - _sma(v, 21)) / _std(v, 21).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_z_10d_base_v058_signal(close: pd.Series) -> pd.Series:
    v = _crash_speed_v(close, 10)
    return ((v - _sma(v, 42)) / _std(v, 42).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_z_21d_base_v059_signal(close: pd.Series) -> pd.Series:
    v = _crash_speed_v(close, 21)
    return ((v - _sma(v, 63)) / _std(v, 63).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_z_42d_base_v060_signal(closeadj: pd.Series) -> pd.Series:
    v = _crash_speed_v(closeadj, 42)
    return ((v - _sma(v, 84)) / _std(v, 84).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_z_63d_base_v061_signal(closeadj: pd.Series) -> pd.Series:
    v = _crash_speed_v(closeadj, 63)
    return ((v - _sma(v, 126)) / _std(v, 126).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_z_126d_base_v062_signal(closeadj: pd.Series) -> pd.Series:
    v = _crash_speed_v(closeadj, 126)
    return ((v - _sma(v, 252)) / _std(v, 252).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_z_252d_base_v063_signal(closeadj: pd.Series) -> pd.Series:
    v = _crash_speed_v(closeadj, 252)
    return ((v - _sma(v, 504)) / _std(v, 504).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

# --- Family 10: Velocity relative to Max (064-070) ---
def f02_crash_speed_v_rel_max_5d_base_v064_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (open + high + low + close) / 4
    v = _crash_speed_v(p, 5)
    return (v / _max(v, 252).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_rel_max_10d_base_v065_signal(close: pd.Series) -> pd.Series:
    v = _crash_speed_v(close, 10)
    return (v / _max(v, 252).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_rel_max_21d_base_v066_signal(close: pd.Series) -> pd.Series:
    v = _crash_speed_v(close, 21)
    return (v / _max(v, 252).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_rel_max_42d_base_v067_signal(closeadj: pd.Series) -> pd.Series:
    v = _crash_speed_v(closeadj, 42)
    return (v / _max(v, 252).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_rel_max_63d_base_v068_signal(closeadj: pd.Series) -> pd.Series:
    v = _crash_speed_v(closeadj, 63)
    return (v / _max(v, 252).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_rel_max_126d_base_v069_signal(closeadj: pd.Series) -> pd.Series:
    v = _crash_speed_v(closeadj, 126)
    return (v / _max(v, 252).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_rel_max_252d_base_v070_signal(closeadj: pd.Series) -> pd.Series:
    v = _crash_speed_v(closeadj, 252)
    return (v / _max(v, 252).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

# --- Family 11: Velocity relative to Mean (071-075) ---
def f02_crash_speed_v_rel_mean_5d_base_v071_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (open + high + low + close) / 4
    v = _crash_speed_v(p, 5)
    return (v / _sma(v, 252).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_rel_mean_10d_base_v072_signal(close: pd.Series) -> pd.Series:
    v = _crash_speed_v(close, 10)
    return (v / _sma(v, 252).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_rel_mean_21d_base_v073_signal(close: pd.Series) -> pd.Series:
    v = _crash_speed_v(close, 21)
    return (v / _sma(v, 252).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_rel_mean_42d_base_v074_signal(closeadj: pd.Series) -> pd.Series:
    v = _crash_speed_v(closeadj, 42)
    return (v / _sma(v, 252).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_rel_mean_63d_base_v075_signal(closeadj: pd.Series) -> pd.Series:
    v = _crash_speed_v(closeadj, 63)
    return (v / _sma(v, 252).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low", "open"]}

BASE_NAMES = [f for f in globals() if f.startswith("f02_crash_speed_") and f.endswith("_signal")]

F02_CRASH_SPEED_BASE_REGISTRY_001_075 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(BASE_NAMES)
}

if __name__ == "__main__":
    import pandas as pd; import numpy as np
    np.random.seed(42)
    n = 2500
    close = pd.Series(np.exp(np.random.normal(-0.02, 0.1, n).cumsum()) * 100)
    d = pd.DataFrame({
        'close': close, 'closeadj': close,
        'open': close.shift(1) * np.exp(np.random.normal(0, 0.02, n)),
        'high': close * np.exp(np.random.uniform(0, 0.05, n)),
        'low': close * np.exp(np.random.uniform(-0.05, 0, n)),
        'volume': np.random.randint(1000, 1000000, n).astype(float),
        'ticker': ['T'] * n,
        'date': pd.date_range('2020-01-01', periods=n)
    }).fillna(method='bfill')
    
    for n, c in F02_CRASH_SPEED_BASE_REGISTRY_001_075.items():
        q = c["func"](**{i: d[i] for i in c["inputs"]})
        assert len(q) > 0
        assert q.nunique() > 2
        assert q.std() > 0
    print("base 001-075 OK")
