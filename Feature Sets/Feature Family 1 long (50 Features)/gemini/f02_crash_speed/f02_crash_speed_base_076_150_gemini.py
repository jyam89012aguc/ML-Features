# f02_crash_speed_base_076_150_gemini.py
import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 5)).mean()
def _ema(s, w): return s.ewm(span=w, min_periods=min(w, 5), adjust=False).mean()
def _min(s, w): return s.rolling(w, min_periods=min(w, 5)).min()
def _max(s, w): return s.rolling(w, min_periods=min(w, 5)).max()
def _std(s, w): return s.rolling(w, min_periods=min(w, 5)).std()
def _skew(s, w): return s.rolling(w, min_periods=min(w, 10)).skew()
def _kurt(s, w): return s.rolling(w, min_periods=min(w, 10)).kurt()
def _rank(s, w): return s.rolling(w, min_periods=min(w, 20)).rank(pct=True)

def _crash_speed_v(c, w): return c.pct_change(w).clip(upper=0).abs().add(1e-9) / w
def _crash_speed_fastest(c, w, n=1): return c.pct_change(n).rolling(w).min().abs().add(1e-9)
def _crash_speed_accel(c, w): return _crash_speed_v(c, w).diff(1)

# --- Family 11 (cont): Velocity relative to Mean (076-077) ---
def f02_crash_speed_v_rel_mean_126d_base_v076_signal(closeadj: pd.Series) -> pd.Series:
    v = _crash_speed_v(closeadj, 126)
    return (v / _sma(v, 252).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_rel_mean_252d_base_v077_signal(closeadj: pd.Series) -> pd.Series:
    v = _crash_speed_v(closeadj, 252)
    return (v / _sma(v, 252).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

# --- Family 12: Velocity Skewness (078-084) ---
def f02_crash_speed_v_skew_5d_base_v078_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (open + high + low + close) / 4
    return _skew(_crash_speed_v(p, 5), 25).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_skew_10d_base_v079_signal(close: pd.Series) -> pd.Series:
    return _skew(_crash_speed_v(close, 10), 50).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_skew_21d_base_v080_signal(close: pd.Series) -> pd.Series:
    return _skew(_crash_speed_v(close, 21), 105).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_skew_42d_base_v081_signal(closeadj: pd.Series) -> pd.Series:
    return _skew(_crash_speed_v(closeadj, 42), 210).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_skew_63d_base_v082_signal(closeadj: pd.Series) -> pd.Series:
    return _skew(_crash_speed_v(closeadj, 63), 252).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_skew_126d_base_v083_signal(closeadj: pd.Series) -> pd.Series:
    return _skew(_crash_speed_v(closeadj, 126), 252).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_skew_252d_base_v084_signal(closeadj: pd.Series) -> pd.Series:
    return _skew(_crash_speed_v(closeadj, 252), 504).replace([np.inf, -np.inf], np.nan)

# --- Family 13: Velocity Kurtosis (085-091) ---
def f02_crash_speed_v_kurt_5d_base_v085_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (open + high + low + close) / 4
    return _kurt(_crash_speed_v(p, 5), 25).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_kurt_10d_base_v086_signal(close: pd.Series) -> pd.Series:
    return _kurt(_crash_speed_v(close, 10), 50).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_kurt_21d_base_v087_signal(close: pd.Series) -> pd.Series:
    return _kurt(_crash_speed_v(close, 21), 105).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_kurt_42d_base_v088_signal(closeadj: pd.Series) -> pd.Series:
    return _kurt(_crash_speed_v(closeadj, 42), 210).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_kurt_63d_base_v089_signal(closeadj: pd.Series) -> pd.Series:
    return _kurt(_crash_speed_v(closeadj, 63), 252).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_kurt_126d_base_v090_signal(closeadj: pd.Series) -> pd.Series:
    return _kurt(_crash_speed_v(closeadj, 126), 252).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_kurt_252d_base_v091_signal(closeadj: pd.Series) -> pd.Series:
    return _kurt(_crash_speed_v(closeadj, 252), 504).replace([np.inf, -np.inf], np.nan)

# --- Family 14: Velocity rolling rank (092-098) ---
def f02_crash_speed_v_rank_5d_base_v092_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (open + high + low + close) / 4
    return _rank(_crash_speed_v(p, 5), 252).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_rank_10d_base_v093_signal(close: pd.Series) -> pd.Series:
    return _rank(_crash_speed_v(close, 10), 252).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_rank_21d_base_v094_signal(close: pd.Series) -> pd.Series:
    return _rank(_crash_speed_v(close, 21), 252).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_rank_42d_base_v095_signal(closeadj: pd.Series) -> pd.Series:
    return _rank(_crash_speed_v(closeadj, 42), 252).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_rank_63d_base_v096_signal(closeadj: pd.Series) -> pd.Series:
    return _rank(_crash_speed_v(closeadj, 63), 252).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_rank_126d_base_v097_signal(closeadj: pd.Series) -> pd.Series:
    return _rank(_crash_speed_v(closeadj, 126), 252).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_rank_252d_base_v098_signal(closeadj: pd.Series) -> pd.Series:
    return _rank(_crash_speed_v(closeadj, 252), 252).replace([np.inf, -np.inf], np.nan)

# --- Family 15: Velocity / Fastest (n=1) ratio (099-105) ---
def f02_crash_speed_v_fast_n1_ratio_5d_base_v099_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (open + high + low + close) / 4
    return (_crash_speed_v(p, 5) / _crash_speed_fastest(p, 5, 1).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_fast_n1_ratio_10d_base_v100_signal(close: pd.Series) -> pd.Series:
    return (_crash_speed_v(close, 10) / _crash_speed_fastest(close, 10, 1).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_fast_n1_ratio_21d_base_v101_signal(close: pd.Series) -> pd.Series:
    return (_crash_speed_v(close, 21) / _crash_speed_fastest(close, 21, 1).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_fast_n1_ratio_42d_base_v102_signal(closeadj: pd.Series) -> pd.Series:
    return (_crash_speed_v(closeadj, 42) / _crash_speed_fastest(closeadj, 42, 1).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_fast_n1_ratio_63d_base_v103_signal(closeadj: pd.Series) -> pd.Series:
    return (_crash_speed_v(closeadj, 63) / _crash_speed_fastest(closeadj, 63, 1).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_fast_n1_ratio_126d_base_v104_signal(closeadj: pd.Series) -> pd.Series:
    return (_crash_speed_v(closeadj, 126) / _crash_speed_fastest(closeadj, 126, 1).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_fast_n1_ratio_252d_base_v105_signal(closeadj: pd.Series) -> pd.Series:
    return (_crash_speed_v(closeadj, 252) / _crash_speed_fastest(closeadj, 252, 1).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

# --- Family 16: Velocity / Fastest (n=5) ratio (106-112) ---
def f02_crash_speed_v_fast_n5_ratio_5d_base_v106_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (open + high + low + close) / 4
    return (_crash_speed_v(p, 5) / _crash_speed_fastest(p, 5, 5).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_fast_n5_ratio_10d_base_v107_signal(close: pd.Series) -> pd.Series:
    return (_crash_speed_v(close, 10) / _crash_speed_fastest(close, 10, 5).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_fast_n5_ratio_21d_base_v108_signal(close: pd.Series) -> pd.Series:
    return (_crash_speed_v(close, 21) / _crash_speed_fastest(close, 21, 5).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_fast_n5_ratio_42d_base_v109_signal(closeadj: pd.Series) -> pd.Series:
    return (_crash_speed_v(closeadj, 42) / _crash_speed_fastest(closeadj, 42, 5).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_fast_n5_ratio_63d_base_v110_signal(closeadj: pd.Series) -> pd.Series:
    return (_crash_speed_v(closeadj, 63) / _crash_speed_fastest(closeadj, 63, 5).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_fast_n5_ratio_126d_base_v111_signal(closeadj: pd.Series) -> pd.Series:
    return (_crash_speed_v(closeadj, 126) / _crash_speed_fastest(closeadj, 126, 5).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_fast_n5_ratio_252d_base_v112_signal(closeadj: pd.Series) -> pd.Series:
    return (_crash_speed_v(closeadj, 252) / _crash_speed_fastest(closeadj, 252, 5).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

# --- Family 17: Acceleration / Velocity ratio (113-119) ---
def f02_crash_speed_accel_v_ratio_5d_base_v113_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (open + high + low + close) / 4
    return (_crash_speed_accel(p, 5) / _crash_speed_v(p, 5).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_accel_v_ratio_10d_base_v114_signal(close: pd.Series) -> pd.Series:
    return (_crash_speed_accel(close, 10) / _crash_speed_v(close, 10).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_accel_v_ratio_21d_base_v115_signal(close: pd.Series) -> pd.Series:
    return (_crash_speed_accel(close, 21) / _crash_speed_v(close, 21).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_accel_v_ratio_42d_base_v116_signal(closeadj: pd.Series) -> pd.Series:
    return (_crash_speed_accel(closeadj, 42) / _crash_speed_v(closeadj, 42).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_accel_v_ratio_63d_base_v117_signal(closeadj: pd.Series) -> pd.Series:
    return (_crash_speed_accel(closeadj, 63) / _crash_speed_v(closeadj, 63).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_accel_v_ratio_126d_base_v118_signal(closeadj: pd.Series) -> pd.Series:
    return (_crash_speed_accel(closeadj, 126) / _crash_speed_v(closeadj, 126).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_accel_v_ratio_252d_base_v119_signal(closeadj: pd.Series) -> pd.Series:
    return (_crash_speed_accel(closeadj, 252) / _crash_speed_v(closeadj, 252).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

# --- Family 18: Acceleration Std (120-126) ---
def f02_crash_speed_accel_std_5d_base_v120_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (open + high + low + close) / 4
    return _std(_crash_speed_accel(p, 5), 21).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_accel_std_10d_base_v121_signal(close: pd.Series) -> pd.Series:
    return _std(_crash_speed_accel(close, 10), 42).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_accel_std_21d_base_v122_signal(close: pd.Series) -> pd.Series:
    return _std(_crash_speed_accel(close, 21), 63).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_accel_std_42d_base_v123_signal(closeadj: pd.Series) -> pd.Series:
    return _std(_crash_speed_accel(closeadj, 42), 84).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_accel_std_63d_base_v124_signal(closeadj: pd.Series) -> pd.Series:
    return _std(_crash_speed_accel(closeadj, 63), 126).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_accel_std_126d_base_v125_signal(closeadj: pd.Series) -> pd.Series:
    return _std(_crash_speed_accel(closeadj, 126), 252).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_accel_std_252d_base_v126_signal(closeadj: pd.Series) -> pd.Series:
    return _std(_crash_speed_accel(closeadj, 252), 504).replace([np.inf, -np.inf], np.nan)

# --- Family 19: Acceleration Z-score (127-133) ---
def f02_crash_speed_accel_z_5d_base_v127_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (open + high + low + close) / 4
    a = _crash_speed_accel(p, 5)
    return ((a - _sma(a, 21)) / _std(a, 21).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_accel_z_10d_base_v128_signal(close: pd.Series) -> pd.Series:
    a = _crash_speed_accel(close, 10)
    return ((a - _sma(a, 42)) / _std(a, 42).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_accel_z_21d_base_v129_signal(close: pd.Series) -> pd.Series:
    a = _crash_speed_accel(close, 21)
    return ((a - _sma(a, 63)) / _std(a, 63).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_accel_z_42d_base_v130_signal(closeadj: pd.Series) -> pd.Series:
    a = _crash_speed_accel(closeadj, 42)
    return ((a - _sma(a, 84)) / _std(a, 84).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_accel_z_63d_base_v131_signal(closeadj: pd.Series) -> pd.Series:
    a = _crash_speed_accel(closeadj, 63)
    return ((a - _sma(a, 126)) / _std(a, 126).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_accel_z_126d_base_v132_signal(closeadj: pd.Series) -> pd.Series:
    a = _crash_speed_accel(closeadj, 126)
    return ((a - _sma(a, 252)) / _std(a, 252).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_accel_z_252d_base_v133_signal(closeadj: pd.Series) -> pd.Series:
    a = _crash_speed_accel(closeadj, 252)
    return ((a - _sma(a, 504)) / _std(a, 504).replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

# --- Family 20: Velocity EMA (134-140) ---
def f02_crash_speed_v_ema_5d_base_v134_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (open + high + low + close) / 4
    return _ema(_crash_speed_v(p, 5), 5).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_ema_10d_base_v135_signal(close: pd.Series) -> pd.Series:
    return _ema(_crash_speed_v(close, 10), 10).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_ema_21d_base_v136_signal(close: pd.Series) -> pd.Series:
    return _ema(_crash_speed_v(close, 21), 21).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_ema_42d_base_v137_signal(closeadj: pd.Series) -> pd.Series:
    return _ema(_crash_speed_v(closeadj, 42), 42).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_ema_63d_base_v138_signal(closeadj: pd.Series) -> pd.Series:
    return _ema(_crash_speed_v(closeadj, 63), 63).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_ema_126d_base_v139_signal(closeadj: pd.Series) -> pd.Series:
    return _ema(_crash_speed_v(closeadj, 126), 126).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_ema_252d_base_v140_signal(closeadj: pd.Series) -> pd.Series:
    return _ema(_crash_speed_v(closeadj, 252), 252).replace([np.inf, -np.inf], np.nan)

# --- Family 21: Velocity EMA Distance (141-147) ---
def f02_crash_speed_v_ema_dist_5d_base_v141_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (open + high + low + close) / 4
    v = _crash_speed_v(p, 5)
    e = _ema(v, 5)
    return ((v - e) / e.replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_ema_dist_10d_base_v142_signal(close: pd.Series) -> pd.Series:
    v = _crash_speed_v(close, 10)
    e = _ema(v, 10)
    return ((v - e) / e.replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_ema_dist_21d_base_v143_signal(close: pd.Series) -> pd.Series:
    v = _crash_speed_v(close, 21)
    e = _ema(v, 21)
    return ((v - e) / e.replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_ema_dist_42d_base_v144_signal(closeadj: pd.Series) -> pd.Series:
    v = _crash_speed_v(closeadj, 42)
    e = _ema(v, 42)
    return ((v - e) / e.replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_ema_dist_63d_base_v145_signal(closeadj: pd.Series) -> pd.Series:
    v = _crash_speed_v(closeadj, 63)
    e = _ema(v, 63)
    return ((v - e) / e.replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_ema_dist_126d_base_v146_signal(closeadj: pd.Series) -> pd.Series:
    v = _crash_speed_v(closeadj, 126)
    e = _ema(v, 126)
    return ((v - e) / e.replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_ema_dist_252d_base_v147_signal(closeadj: pd.Series) -> pd.Series:
    v = _crash_speed_v(closeadj, 252)
    e = _ema(v, 252)
    return ((v - e) / e.replace(0, np.nan)).replace([np.inf, -np.inf], np.nan)

# --- Family 22: Velocity mean (window 504) (148-150) ---
def f02_crash_speed_v_mean504_5d_base_v148_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (open + high + low + close) / 4
    return _sma(_crash_speed_v(p, 5), 504).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_mean504_10d_base_v149_signal(close: pd.Series) -> pd.Series:
    return _sma(_crash_speed_v(close, 10), 504).replace([np.inf, -np.inf], np.nan)

def f02_crash_speed_v_mean504_21d_base_v150_signal(close: pd.Series) -> pd.Series:
    return _sma(_crash_speed_v(close, 21), 504).replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low", "open"]}

BASE_NAMES = [f for f in globals() if f.startswith("f02_crash_speed_") and f.endswith("_signal")]

F02_CRASH_SPEED_BASE_REGISTRY_076_150 = {
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
    
    for n, c in F02_CRASH_SPEED_BASE_REGISTRY_076_150.items():
        q = c["func"](**{i: d[i] for i in c["inputs"]})
        assert len(q) > 0
        assert q.nunique() > 2
        assert q.std() > 0
    print("base 076-150 OK")
