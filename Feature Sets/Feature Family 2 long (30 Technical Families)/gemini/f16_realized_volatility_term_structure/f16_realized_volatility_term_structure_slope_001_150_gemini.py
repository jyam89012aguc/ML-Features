# f16_realized_volatility_term_structure_slope_001_150_gemini.py
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

# f16rvts_f16_realized_volatility_term_structure_slope_v001_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v001_signal(close: pd.Series) -> pd.Series:
    res = (_rv(close, 5)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v002_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v002_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vspread(_rv(closeadj, 21), _rv(closeadj, 252))).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v003_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v003_signal(close: pd.Series) -> pd.Series:
    res = (_vz(_rv(close, 21), 63)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v004_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v004_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vov(_rv(closeadj, 42), 126)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v005_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v005_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vrank(_rv(closeadj, 63), 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v006_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v006_signal(closeadj: pd.Series) -> pd.Series:
    res = (_rv(closeadj, 126)).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v007_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v007_signal(close: pd.Series) -> pd.Series:
    res = (_vspread(_rv(close, 5), _rv(close, 21))).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v008_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v008_signal(close: pd.Series) -> pd.Series:
    res = (_vz(_rv(close, 5), 63)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v009_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v009_signal(close: pd.Series) -> pd.Series:
    res = (_vov(_rv(close, 10), 126)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v010_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v010_signal(close: pd.Series) -> pd.Series:
    res = (_vrank(_rv(close, 21), 252)).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v011_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v011_signal(closeadj: pd.Series) -> pd.Series:
    res = (_rv(closeadj, 42)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v012_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v012_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vspread(_rv(closeadj, 21), _rv(closeadj, 252))).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v013_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v013_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vz(_rv(closeadj, 126), 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v014_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v014_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vov(_rv(closeadj, 252), 126)).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v015_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v015_signal(close: pd.Series) -> pd.Series:
    res = (_vrank(_rv(close, 5), 252)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v016_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v016_signal(close: pd.Series) -> pd.Series:
    res = (_rv(close, 10)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v017_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v017_signal(close: pd.Series) -> pd.Series:
    res = (_vspread(_rv(close, 5), _rv(close, 21))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v018_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v018_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vz(_rv(closeadj, 42), 252)).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v019_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v019_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vov(_rv(closeadj, 63), 126)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v020_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v020_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vrank(_rv(closeadj, 126), 252)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v021_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v021_signal(closeadj: pd.Series) -> pd.Series:
    res = (_rv(closeadj, 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v022_signal: slope of base feature

# f16rvts_f16_realized_volatility_term_structure_slope_v023_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v023_signal(close: pd.Series) -> pd.Series:
    res = (_vz(_rv(close, 10), 63)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v024_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v024_signal(close: pd.Series) -> pd.Series:
    res = (_vov(_rv(close, 21), 126)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v025_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v025_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vrank(_rv(closeadj, 42), 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v026_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v026_signal(closeadj: pd.Series) -> pd.Series:
    res = (_rv(closeadj, 63)).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v027_signal: slope of base feature

# f16rvts_f16_realized_volatility_term_structure_slope_v028_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v028_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vz(_rv(closeadj, 252), 252)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v029_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v029_signal(close: pd.Series) -> pd.Series:
    res = (_vov(_rv(close, 5), 126)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v030_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v030_signal(close: pd.Series) -> pd.Series:
    res = (_vrank(_rv(close, 10), 252)).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v031_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v031_signal(close: pd.Series) -> pd.Series:
    res = (_rv(close, 21)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v032_signal: slope of base feature

# f16rvts_f16_realized_volatility_term_structure_slope_v033_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v033_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vz(_rv(closeadj, 63), 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v034_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v034_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vov(_rv(closeadj, 126), 126)).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v035_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v035_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vrank(_rv(closeadj, 252), 252)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v036_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v036_signal(close: pd.Series) -> pd.Series:
    res = (_rv(close, 5)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v037_signal: slope of base feature

# f16rvts_f16_realized_volatility_term_structure_slope_v038_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v038_signal(close: pd.Series) -> pd.Series:
    res = (_vz(_rv(close, 21), 63)).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v039_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v039_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vov(_rv(closeadj, 42), 126)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v040_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v040_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vrank(_rv(closeadj, 63), 252)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v041_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v041_signal(closeadj: pd.Series) -> pd.Series:
    res = (_rv(closeadj, 126)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v042_signal: slope of base feature

# f16rvts_f16_realized_volatility_term_structure_slope_v043_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v043_signal(close: pd.Series) -> pd.Series:
    res = (_vz(_rv(close, 5), 63)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v044_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v044_signal(close: pd.Series) -> pd.Series:
    res = (_vov(_rv(close, 10), 126)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v045_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v045_signal(close: pd.Series) -> pd.Series:
    res = (_vrank(_rv(close, 21), 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v046_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v046_signal(closeadj: pd.Series) -> pd.Series:
    res = (_rv(closeadj, 42)).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v047_signal: slope of base feature

# f16rvts_f16_realized_volatility_term_structure_slope_v048_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v048_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vz(_rv(closeadj, 126), 252)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v049_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v049_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vov(_rv(closeadj, 252), 126)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v050_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v050_signal(close: pd.Series) -> pd.Series:
    res = (_vrank(_rv(close, 5), 252)).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v051_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v051_signal(close: pd.Series) -> pd.Series:
    res = (_rv(close, 10)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v052_signal: slope of base feature

# f16rvts_f16_realized_volatility_term_structure_slope_v053_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v053_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vz(_rv(closeadj, 42), 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v054_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v054_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vov(_rv(closeadj, 63), 126)).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v055_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v055_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vrank(_rv(closeadj, 126), 252)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v056_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v056_signal(closeadj: pd.Series) -> pd.Series:
    res = (_rv(closeadj, 252)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v057_signal: slope of base feature

# f16rvts_f16_realized_volatility_term_structure_slope_v058_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v058_signal(close: pd.Series) -> pd.Series:
    res = (_vz(_rv(close, 10), 63)).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v059_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v059_signal(close: pd.Series) -> pd.Series:
    res = (_vov(_rv(close, 21), 126)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v060_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v060_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vrank(_rv(closeadj, 42), 252)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v061_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v061_signal(closeadj: pd.Series) -> pd.Series:
    res = (_rv(closeadj, 63)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v062_signal: slope of base feature

# f16rvts_f16_realized_volatility_term_structure_slope_v063_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v063_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vz(_rv(closeadj, 252), 252)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v064_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v064_signal(close: pd.Series) -> pd.Series:
    res = (_vov(_rv(close, 5), 126)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v065_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v065_signal(close: pd.Series) -> pd.Series:
    res = (_vrank(_rv(close, 10), 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v066_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v066_signal(close: pd.Series) -> pd.Series:
    res = (_rv(close, 21)).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v067_signal: slope of base feature

# f16rvts_f16_realized_volatility_term_structure_slope_v068_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v068_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vz(_rv(closeadj, 63), 252)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v069_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v069_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vov(_rv(closeadj, 126), 126)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v070_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v070_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vrank(_rv(closeadj, 252), 252)).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v071_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v071_signal(close: pd.Series) -> pd.Series:
    res = (_rv(close, 5)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v072_signal: slope of base feature

# f16rvts_f16_realized_volatility_term_structure_slope_v073_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v073_signal(close: pd.Series) -> pd.Series:
    res = (_vz(_rv(close, 21), 63)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v074_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v074_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vov(_rv(closeadj, 42), 126)).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v075_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v075_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vrank(_rv(closeadj, 63), 252)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v076_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v076_signal(closeadj: pd.Series) -> pd.Series:
    res = (_rv(closeadj, 126)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v077_signal: slope of base feature

# f16rvts_f16_realized_volatility_term_structure_slope_v078_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v078_signal(close: pd.Series) -> pd.Series:
    res = (_vz(_rv(close, 5), 63)).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v079_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v079_signal(close: pd.Series) -> pd.Series:
    res = (_vov(_rv(close, 10), 126)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v080_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v080_signal(close: pd.Series) -> pd.Series:
    res = (_vrank(_rv(close, 21), 252)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v081_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v081_signal(closeadj: pd.Series) -> pd.Series:
    res = (_rv(closeadj, 42)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v082_signal: slope of base feature

# f16rvts_f16_realized_volatility_term_structure_slope_v083_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v083_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vz(_rv(closeadj, 126), 252)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v084_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v084_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vov(_rv(closeadj, 252), 126)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v085_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v085_signal(close: pd.Series) -> pd.Series:
    res = (_vrank(_rv(close, 5), 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v086_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v086_signal(close: pd.Series) -> pd.Series:
    res = (_rv(close, 10)).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v087_signal: slope of base feature

# f16rvts_f16_realized_volatility_term_structure_slope_v088_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v088_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vz(_rv(closeadj, 42), 252)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v089_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v089_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vov(_rv(closeadj, 63), 126)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v090_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v090_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vrank(_rv(closeadj, 126), 252)).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v091_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v091_signal(closeadj: pd.Series) -> pd.Series:
    res = (_rv(closeadj, 252)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v092_signal: slope of base feature

# f16rvts_f16_realized_volatility_term_structure_slope_v093_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v093_signal(close: pd.Series) -> pd.Series:
    res = (_vz(_rv(close, 10), 63)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v094_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v094_signal(close: pd.Series) -> pd.Series:
    res = (_vov(_rv(close, 21), 126)).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v095_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v095_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vrank(_rv(closeadj, 42), 252)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v096_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v096_signal(closeadj: pd.Series) -> pd.Series:
    res = (_rv(closeadj, 63)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v097_signal: slope of base feature

# f16rvts_f16_realized_volatility_term_structure_slope_v098_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v098_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vz(_rv(closeadj, 252), 252)).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v099_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v099_signal(close: pd.Series) -> pd.Series:
    res = (_vov(_rv(close, 5), 126)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v100_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v100_signal(close: pd.Series) -> pd.Series:
    res = (_vrank(_rv(close, 10), 252)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v101_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v101_signal(close: pd.Series) -> pd.Series:
    res = (_rv(close, 21)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v102_signal: slope of base feature

# f16rvts_f16_realized_volatility_term_structure_slope_v103_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v103_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vz(_rv(closeadj, 63), 252)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v104_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v104_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vov(_rv(closeadj, 126), 126)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v105_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v105_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vrank(_rv(closeadj, 252), 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v106_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v106_signal(close: pd.Series) -> pd.Series:
    res = (_rv(close, 5)).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v107_signal: slope of base feature

# f16rvts_f16_realized_volatility_term_structure_slope_v108_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v108_signal(close: pd.Series) -> pd.Series:
    res = (_vz(_rv(close, 21), 63)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v109_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v109_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vov(_rv(closeadj, 42), 126)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v110_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v110_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vrank(_rv(closeadj, 63), 252)).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v111_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v111_signal(closeadj: pd.Series) -> pd.Series:
    res = (_rv(closeadj, 126)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v112_signal: slope of base feature

# f16rvts_f16_realized_volatility_term_structure_slope_v113_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v113_signal(close: pd.Series) -> pd.Series:
    res = (_vz(_rv(close, 5), 63)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v114_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v114_signal(close: pd.Series) -> pd.Series:
    res = (_vov(_rv(close, 10), 126)).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v115_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v115_signal(close: pd.Series) -> pd.Series:
    res = (_vrank(_rv(close, 21), 252)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v116_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v116_signal(closeadj: pd.Series) -> pd.Series:
    res = (_rv(closeadj, 42)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v117_signal: slope of base feature

# f16rvts_f16_realized_volatility_term_structure_slope_v118_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v118_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vz(_rv(closeadj, 126), 252)).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v119_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v119_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vov(_rv(closeadj, 252), 126)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v120_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v120_signal(close: pd.Series) -> pd.Series:
    res = (_vrank(_rv(close, 5), 252)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v121_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v121_signal(close: pd.Series) -> pd.Series:
    res = (_rv(close, 10)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v122_signal: slope of base feature

# f16rvts_f16_realized_volatility_term_structure_slope_v123_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v123_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vz(_rv(closeadj, 42), 252)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v124_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v124_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vov(_rv(closeadj, 63), 126)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v125_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v125_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vrank(_rv(closeadj, 126), 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v126_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v126_signal(closeadj: pd.Series) -> pd.Series:
    res = (_rv(closeadj, 252)).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v127_signal: slope of base feature

# f16rvts_f16_realized_volatility_term_structure_slope_v128_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v128_signal(close: pd.Series) -> pd.Series:
    res = (_vz(_rv(close, 10), 63)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v129_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v129_signal(close: pd.Series) -> pd.Series:
    res = (_vov(_rv(close, 21), 126)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v130_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v130_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vrank(_rv(closeadj, 42), 252)).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v131_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v131_signal(closeadj: pd.Series) -> pd.Series:
    res = (_rv(closeadj, 63)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v132_signal: slope of base feature

# f16rvts_f16_realized_volatility_term_structure_slope_v133_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v133_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vz(_rv(closeadj, 252), 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v134_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v134_signal(close: pd.Series) -> pd.Series:
    res = (_vov(_rv(close, 5), 126)).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v135_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v135_signal(close: pd.Series) -> pd.Series:
    res = (_vrank(_rv(close, 10), 252)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v136_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v136_signal(close: pd.Series) -> pd.Series:
    res = (_rv(close, 21)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v137_signal: slope of base feature

# f16rvts_f16_realized_volatility_term_structure_slope_v138_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v138_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vz(_rv(closeadj, 63), 252)).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v139_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v139_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vov(_rv(closeadj, 126), 126)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v140_signal: slope of base feature
def f16rvts_f16_realized_volatility_term_structure_slope_v140_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vrank(_rv(closeadj, 252), 252)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_slope_v141_signal: slope of base feature

# f16rvts_f16_realized_volatility_term_structure_slope_v142_signal: slope of base feature

# f16rvts_f16_realized_volatility_term_structure_slope_v143_signal: slope of base feature

# f16rvts_f16_realized_volatility_term_structure_slope_v144_signal: slope of base feature

# f16rvts_f16_realized_volatility_term_structure_slope_v145_signal: slope of base feature

# f16rvts_f16_realized_volatility_term_structure_slope_v146_signal: slope of base feature

# f16rvts_f16_realized_volatility_term_structure_slope_v147_signal: slope of base feature

# f16rvts_f16_realized_volatility_term_structure_slope_v148_signal: slope of base feature

# f16rvts_f16_realized_volatility_term_structure_slope_v149_signal: slope of base feature

# f16rvts_f16_realized_volatility_term_structure_slope_v150_signal: slope of base feature

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj"]}
FEAT_NAMES = [f for f in globals() if f.startswith("f16rvts_") and f.endswith("_signal")]
F16_REALIZED_VOLATILITY_TERM_STRUCTURE_SLOPE_REGISTRY_001_150 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(FEAT_NAMES)
}

if __name__ == "__main__":
    sz = 1000; d = pd.DataFrame({"close": np.random.randn(sz).cumsum()+100, "closeadj": np.random.randn(sz).cumsum()+100, "ticker": ["T"]*sz, "date": pd.date_range("2020-01-01", periods=sz)})
    for n, c in F16_REALIZED_VOLATILITY_TERM_STRUCTURE_SLOPE_REGISTRY_001_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("OK")