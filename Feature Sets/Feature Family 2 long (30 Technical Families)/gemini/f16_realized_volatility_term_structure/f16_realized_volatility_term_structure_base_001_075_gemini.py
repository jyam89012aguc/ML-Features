# f16_realized_volatility_term_structure_base_001_075_gemini.py
import pandas as pd
import numpy as np

def _sma(s, w):
    return s.rolling(w, min_periods=min(w, 5)).mean()

def _std(s, w):
    return s.rolling(w, min_periods=min(w, 5)).std()

def _rv(p, w):
    returns = np.log(p / p.shift(1).replace(0, np.nan))
    return returns.rolling(w, min_periods=min(w, 5)).std() * np.sqrt(252)

def _vspread(vs, vl):
    return (vs - vl) / vl.abs().replace(0, np.nan)

def _vz(v, w):
    return (v - _sma(v, w)) / _std(v, w).replace(0, np.nan)

def _vrank(v, w):
    return v.rolling(w, min_periods=min(w, 5)).rank(pct=True)

def _vov(v, w):
    return _std(v, w)

# f16rvts_f16_realized_volatility_term_structure_v001_signal: 5d realized vol close
def f16rvts_f16_realized_volatility_term_structure_v001_signal(close: pd.Series) -> pd.Series:
    res = _rv(close, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_v002_signal: 10d vs 42d vol spread closeadj
def f16rvts_f16_realized_volatility_term_structure_v002_signal(closeadj: pd.Series) -> pd.Series:
    res = _vspread(_rv(closeadj, 10), _rv(closeadj, 42))
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_v003_signal: 63d z-scored 21d vol close
def f16rvts_f16_realized_volatility_term_structure_v003_signal(close: pd.Series) -> pd.Series:
    res = _vz(_rv(close, 21), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_v004_signal: 126d volatility of 42d vol closeadj
def f16rvts_f16_realized_volatility_term_structure_v004_signal(closeadj: pd.Series) -> pd.Series:
    res = _vov(_rv(closeadj, 42), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_v005_signal: 252d percentile rank of 63d vol closeadj
def f16rvts_f16_realized_volatility_term_structure_v005_signal(closeadj: pd.Series) -> pd.Series:
    res = _vrank(_rv(closeadj, 63), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_v006_signal: 126d realized vol closeadj
def f16rvts_f16_realized_volatility_term_structure_v006_signal(closeadj: pd.Series) -> pd.Series:
    res = _rv(closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_v007_signal: 10d vs 252d vol spread closeadj
def f16rvts_f16_realized_volatility_term_structure_v007_signal(closeadj: pd.Series) -> pd.Series:
    res = _vspread(_rv(closeadj, 10), _rv(closeadj, 252))
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_v008_signal: 21d z-scored 5d vol close
def f16rvts_f16_realized_volatility_term_structure_v008_signal(close: pd.Series) -> pd.Series:
    res = _vz(_rv(close, 5), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_v009_signal: 42d volatility of 10d vol close
def f16rvts_f16_realized_volatility_term_structure_v009_signal(close: pd.Series) -> pd.Series:
    res = _vov(_rv(close, 10), 42)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_v010_signal: 63d percentile rank of 21d vol close
def f16rvts_f16_realized_volatility_term_structure_v010_signal(close: pd.Series) -> pd.Series:
    res = _vrank(_rv(close, 21), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_v011_signal: 42d realized vol closeadj
def f16rvts_f16_realized_volatility_term_structure_v011_signal(closeadj: pd.Series) -> pd.Series:
    res = _rv(closeadj, 42)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_v012_signal: 63d vs 252d vol spread closeadj
def f16rvts_f16_realized_volatility_term_structure_v012_signal(closeadj: pd.Series) -> pd.Series:
    res = _vspread(_rv(closeadj, 63), _rv(closeadj, 252))
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_v013_signal: 5d z-scored 126d vol closeadj
def f16rvts_f16_realized_volatility_term_structure_v013_signal(closeadj: pd.Series) -> pd.Series:
    res = _vz(_rv(closeadj, 126), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_v014_signal: 10d volatility of 252d vol closeadj
def f16rvts_f16_realized_volatility_term_structure_v014_signal(closeadj: pd.Series) -> pd.Series:
    res = _vov(_rv(closeadj, 252), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_v015_signal: 21d percentile rank of 5d vol close
def f16rvts_f16_realized_volatility_term_structure_v015_signal(close: pd.Series) -> pd.Series:
    res = _vrank(_rv(close, 5), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_v016_signal: 10d realized vol close
def f16rvts_f16_realized_volatility_term_structure_v016_signal(close: pd.Series) -> pd.Series:
    res = _rv(close, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_v017_signal: 21d vs 63d vol spread closeadj
def f16rvts_f16_realized_volatility_term_structure_v017_signal(closeadj: pd.Series) -> pd.Series:
    res = _vspread(_rv(closeadj, 21), _rv(closeadj, 63))
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_v018_signal: 126d z-scored 42d vol closeadj
def f16rvts_f16_realized_volatility_term_structure_v018_signal(closeadj: pd.Series) -> pd.Series:
    res = _vz(_rv(closeadj, 42), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_v019_signal: 252d volatility of 63d vol closeadj
def f16rvts_f16_realized_volatility_term_structure_v019_signal(closeadj: pd.Series) -> pd.Series:
    res = _vov(_rv(closeadj, 63), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_v020_signal: 5d percentile rank of 126d vol closeadj
def f16rvts_f16_realized_volatility_term_structure_v020_signal(closeadj: pd.Series) -> pd.Series:
    res = _vrank(_rv(closeadj, 126), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_v021_signal: 252d realized vol closeadj
def f16rvts_f16_realized_volatility_term_structure_v021_signal(closeadj: pd.Series) -> pd.Series:
    res = _rv(closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_v022_signal: 5d vs 21d vol spread close
def f16rvts_f16_realized_volatility_term_structure_v022_signal(close: pd.Series) -> pd.Series:
    res = _vspread(_rv(close, 5), _rv(close, 21))
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_v023_signal: 42d z-scored 10d vol close
def f16rvts_f16_realized_volatility_term_structure_v023_signal(close: pd.Series) -> pd.Series:
    res = _vz(_rv(close, 10), 42)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_v024_signal: 63d volatility of 21d vol close
def f16rvts_f16_realized_volatility_term_structure_v024_signal(close: pd.Series) -> pd.Series:
    res = _vov(_rv(close, 21), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_v025_signal: 126d percentile rank of 42d vol closeadj
def f16rvts_f16_realized_volatility_term_structure_v025_signal(closeadj: pd.Series) -> pd.Series:
    res = _vrank(_rv(closeadj, 42), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_v026_signal: 63d realized vol closeadj
def f16rvts_f16_realized_volatility_term_structure_v026_signal(closeadj: pd.Series) -> pd.Series:
    res = _rv(closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_v027_signal: 5d vs 126d vol spread closeadj
def f16rvts_f16_realized_volatility_term_structure_v027_signal(closeadj: pd.Series) -> pd.Series:
    res = _vspread(_rv(closeadj, 5), _rv(closeadj, 126))
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_v028_signal: 10d z-scored 252d vol closeadj
def f16rvts_f16_realized_volatility_term_structure_v028_signal(closeadj: pd.Series) -> pd.Series:
    res = _vz(_rv(closeadj, 252), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_v029_signal: 21d volatility of 5d vol close
def f16rvts_f16_realized_volatility_term_structure_v029_signal(close: pd.Series) -> pd.Series:
    res = _vov(_rv(close, 5), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_v030_signal: 42d percentile rank of 10d vol close
def f16rvts_f16_realized_volatility_term_structure_v030_signal(close: pd.Series) -> pd.Series:
    res = _vrank(_rv(close, 10), 42)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_v031_signal: 21d realized vol close
def f16rvts_f16_realized_volatility_term_structure_v031_signal(close: pd.Series) -> pd.Series:
    res = _rv(close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_v032_signal: 42d vs 126d vol spread closeadj
def f16rvts_f16_realized_volatility_term_structure_v032_signal(closeadj: pd.Series) -> pd.Series:
    res = _vspread(_rv(closeadj, 42), _rv(closeadj, 126))
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_v033_signal: 252d z-scored 63d vol closeadj
def f16rvts_f16_realized_volatility_term_structure_v033_signal(closeadj: pd.Series) -> pd.Series:
    res = _vz(_rv(closeadj, 63), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_v034_signal: 5d volatility of 126d vol closeadj
def f16rvts_f16_realized_volatility_term_structure_v034_signal(closeadj: pd.Series) -> pd.Series:
    res = _vov(_rv(closeadj, 126), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_v035_signal: 10d percentile rank of 252d vol closeadj
def f16rvts_f16_realized_volatility_term_structure_v035_signal(closeadj: pd.Series) -> pd.Series:
    res = _vrank(_rv(closeadj, 252), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_v036_signal: 5d realized vol close

# f16rvts_f16_realized_volatility_term_structure_v037_signal: 10d vs 42d vol spread closeadj

# f16rvts_f16_realized_volatility_term_structure_v038_signal: 63d z-scored 21d vol close

# f16rvts_f16_realized_volatility_term_structure_v039_signal: 126d volatility of 42d vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v040_signal: 252d percentile rank of 63d vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v041_signal: 126d realized vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v042_signal: 10d vs 252d vol spread closeadj

# f16rvts_f16_realized_volatility_term_structure_v043_signal: 21d z-scored 5d vol close

# f16rvts_f16_realized_volatility_term_structure_v044_signal: 42d volatility of 10d vol close

# f16rvts_f16_realized_volatility_term_structure_v045_signal: 63d percentile rank of 21d vol close

# f16rvts_f16_realized_volatility_term_structure_v046_signal: 42d realized vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v047_signal: 63d vs 252d vol spread closeadj

# f16rvts_f16_realized_volatility_term_structure_v048_signal: 5d z-scored 126d vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v049_signal: 10d volatility of 252d vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v050_signal: 21d percentile rank of 5d vol close

# f16rvts_f16_realized_volatility_term_structure_v051_signal: 10d realized vol close

# f16rvts_f16_realized_volatility_term_structure_v052_signal: 21d vs 63d vol spread closeadj

# f16rvts_f16_realized_volatility_term_structure_v053_signal: 126d z-scored 42d vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v054_signal: 252d volatility of 63d vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v055_signal: 5d percentile rank of 126d vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v056_signal: 252d realized vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v057_signal: 5d vs 21d vol spread close

# f16rvts_f16_realized_volatility_term_structure_v058_signal: 42d z-scored 10d vol close

# f16rvts_f16_realized_volatility_term_structure_v059_signal: 63d volatility of 21d vol close

# f16rvts_f16_realized_volatility_term_structure_v060_signal: 126d percentile rank of 42d vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v061_signal: 63d realized vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v062_signal: 5d vs 126d vol spread closeadj

# f16rvts_f16_realized_volatility_term_structure_v063_signal: 10d z-scored 252d vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v064_signal: 21d volatility of 5d vol close

# f16rvts_f16_realized_volatility_term_structure_v065_signal: 42d percentile rank of 10d vol close

# f16rvts_f16_realized_volatility_term_structure_v066_signal: 21d realized vol close

# f16rvts_f16_realized_volatility_term_structure_v067_signal: 42d vs 126d vol spread closeadj

# f16rvts_f16_realized_volatility_term_structure_v068_signal: 252d z-scored 63d vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v069_signal: 5d volatility of 126d vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v070_signal: 10d percentile rank of 252d vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v071_signal: 5d realized vol close

# f16rvts_f16_realized_volatility_term_structure_v072_signal: 10d vs 42d vol spread closeadj

# f16rvts_f16_realized_volatility_term_structure_v073_signal: 63d z-scored 21d vol close

# f16rvts_f16_realized_volatility_term_structure_v074_signal: 126d volatility of 42d vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v075_signal: 252d percentile rank of 63d vol closeadj

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj"]}
BASE_NAMES = [f for f in globals() if f.startswith("f16rvts_") and f.endswith("_signal")]
F16_REALIZED_VOLATILITY_TERM_STRUCTURE_BASE_REGISTRY_001_075 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(BASE_NAMES)
}

if __name__ == "__main__":
    sz = 500; d = pd.DataFrame({"close": np.random.randn(sz).cumsum()+100, "closeadj": np.random.randn(sz).cumsum()+100, "ticker": ["T"]*sz, "date": pd.date_range("2020-01-01", periods=sz)})
    for n, c in F16_REALIZED_VOLATILITY_TERM_STRUCTURE_BASE_REGISTRY_001_075.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("OK")