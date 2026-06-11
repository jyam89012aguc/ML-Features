# f16_realized_volatility_term_structure_jerk_001_150_gemini.py
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

# f16rvts_f16_realized_volatility_term_structure_jerk_v001_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v001_signal(close: pd.Series) -> pd.Series:
    res = (_rv(close, 5)).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v002_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v002_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vspread(_rv(closeadj, 21), _rv(closeadj, 252))).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v003_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v003_signal(close: pd.Series) -> pd.Series:
    res = (_vz(_rv(close, 21), 63)).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v004_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v004_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vov(_rv(closeadj, 42), 126)).pct_change(31).pct_change(31)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v005_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v005_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vrank(_rv(closeadj, 63), 252)).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v006_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v006_signal(closeadj: pd.Series) -> pd.Series:
    res = (_rv(closeadj, 126)).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v007_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v007_signal(close: pd.Series) -> pd.Series:
    res = (_vspread(_rv(close, 5), _rv(close, 21))).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v008_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v008_signal(close: pd.Series) -> pd.Series:
    res = (_vz(_rv(close, 5), 63)).pct_change(31).pct_change(31)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v009_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v009_signal(close: pd.Series) -> pd.Series:
    res = (_vov(_rv(close, 10), 126)).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v010_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v010_signal(close: pd.Series) -> pd.Series:
    res = (_vrank(_rv(close, 21), 252)).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v011_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v011_signal(closeadj: pd.Series) -> pd.Series:
    res = (_rv(closeadj, 42)).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v012_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v012_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vspread(_rv(closeadj, 21), _rv(closeadj, 252))).pct_change(31).pct_change(31)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v013_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v013_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vz(_rv(closeadj, 126), 252)).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v014_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v014_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vov(_rv(closeadj, 252), 126)).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v015_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v015_signal(close: pd.Series) -> pd.Series:
    res = (_vrank(_rv(close, 5), 252)).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v016_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v016_signal(close: pd.Series) -> pd.Series:
    res = (_rv(close, 10)).pct_change(31).pct_change(31)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v017_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v017_signal(close: pd.Series) -> pd.Series:
    res = (_vspread(_rv(close, 5), _rv(close, 21))).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v018_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v018_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vz(_rv(closeadj, 42), 252)).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v019_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v019_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vov(_rv(closeadj, 63), 126)).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v020_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v020_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vrank(_rv(closeadj, 126), 252)).pct_change(31).pct_change(31)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v021_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v021_signal(closeadj: pd.Series) -> pd.Series:
    res = (_rv(closeadj, 252)).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v022_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v023_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v023_signal(close: pd.Series) -> pd.Series:
    res = (_vz(_rv(close, 10), 63)).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v024_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v024_signal(close: pd.Series) -> pd.Series:
    res = (_vov(_rv(close, 21), 126)).pct_change(31).pct_change(31)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v025_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v025_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vrank(_rv(closeadj, 42), 252)).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v026_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v026_signal(closeadj: pd.Series) -> pd.Series:
    res = (_rv(closeadj, 63)).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v027_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v028_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v028_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vz(_rv(closeadj, 252), 252)).pct_change(31).pct_change(31)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v029_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v029_signal(close: pd.Series) -> pd.Series:
    res = (_vov(_rv(close, 5), 126)).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v030_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v030_signal(close: pd.Series) -> pd.Series:
    res = (_vrank(_rv(close, 10), 252)).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v031_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v031_signal(close: pd.Series) -> pd.Series:
    res = (_rv(close, 21)).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v032_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v033_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v033_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vz(_rv(closeadj, 63), 252)).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v034_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v034_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vov(_rv(closeadj, 126), 126)).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v035_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v035_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vrank(_rv(closeadj, 252), 252)).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v036_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v036_signal(close: pd.Series) -> pd.Series:
    res = (_rv(close, 5)).pct_change(31).pct_change(31)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v037_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v038_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v038_signal(close: pd.Series) -> pd.Series:
    res = (_vz(_rv(close, 21), 63)).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v039_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v039_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vov(_rv(closeadj, 42), 126)).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v040_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v040_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vrank(_rv(closeadj, 63), 252)).pct_change(31).pct_change(31)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v041_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v042_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v043_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v043_signal(close: pd.Series) -> pd.Series:
    res = (_vz(_rv(close, 5), 63)).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v044_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v044_signal(close: pd.Series) -> pd.Series:
    res = (_vov(_rv(close, 10), 126)).pct_change(31).pct_change(31)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v045_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v046_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v046_signal(closeadj: pd.Series) -> pd.Series:
    res = (_rv(closeadj, 42)).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v047_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v048_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v048_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vz(_rv(closeadj, 126), 252)).pct_change(31).pct_change(31)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v049_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v050_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v050_signal(close: pd.Series) -> pd.Series:
    res = (_vrank(_rv(close, 5), 252)).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v051_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v051_signal(close: pd.Series) -> pd.Series:
    res = (_rv(close, 10)).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v052_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v053_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v054_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v054_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vov(_rv(closeadj, 63), 126)).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v055_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v055_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vrank(_rv(closeadj, 126), 252)).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v056_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v056_signal(closeadj: pd.Series) -> pd.Series:
    res = (_rv(closeadj, 252)).pct_change(31).pct_change(31)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v057_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v058_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v058_signal(close: pd.Series) -> pd.Series:
    res = (_vz(_rv(close, 10), 63)).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v059_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v059_signal(close: pd.Series) -> pd.Series:
    res = (_vov(_rv(close, 21), 126)).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v060_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v060_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vrank(_rv(closeadj, 42), 252)).pct_change(31).pct_change(31)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v061_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v062_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v063_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v063_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vz(_rv(closeadj, 252), 252)).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v064_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v064_signal(close: pd.Series) -> pd.Series:
    res = (_vov(_rv(close, 5), 126)).pct_change(31).pct_change(31)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v065_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v066_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v066_signal(close: pd.Series) -> pd.Series:
    res = (_rv(close, 21)).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v067_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v068_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v068_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vz(_rv(closeadj, 63), 252)).pct_change(31).pct_change(31)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v069_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v070_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v070_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vrank(_rv(closeadj, 252), 252)).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v071_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v071_signal(close: pd.Series) -> pd.Series:
    res = (_rv(close, 5)).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v072_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v073_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v074_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v074_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vov(_rv(closeadj, 42), 126)).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v075_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v075_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vrank(_rv(closeadj, 63), 252)).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v076_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v076_signal(closeadj: pd.Series) -> pd.Series:
    res = (_rv(closeadj, 126)).pct_change(31).pct_change(31)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v077_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v078_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v078_signal(close: pd.Series) -> pd.Series:
    res = (_vz(_rv(close, 5), 63)).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v079_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v079_signal(close: pd.Series) -> pd.Series:
    res = (_vov(_rv(close, 10), 126)).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v080_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v080_signal(close: pd.Series) -> pd.Series:
    res = (_vrank(_rv(close, 21), 252)).pct_change(31).pct_change(31)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v081_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v082_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v083_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v083_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vz(_rv(closeadj, 126), 252)).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v084_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v084_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vov(_rv(closeadj, 252), 126)).pct_change(31).pct_change(31)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v085_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v086_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v086_signal(close: pd.Series) -> pd.Series:
    res = (_rv(close, 10)).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v087_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v088_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v088_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vz(_rv(closeadj, 42), 252)).pct_change(31).pct_change(31)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v089_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v090_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v090_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vrank(_rv(closeadj, 126), 252)).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v091_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v091_signal(closeadj: pd.Series) -> pd.Series:
    res = (_rv(closeadj, 252)).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v092_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v093_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v094_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v094_signal(close: pd.Series) -> pd.Series:
    res = (_vov(_rv(close, 21), 126)).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v095_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v095_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vrank(_rv(closeadj, 42), 252)).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v096_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v096_signal(closeadj: pd.Series) -> pd.Series:
    res = (_rv(closeadj, 63)).pct_change(31).pct_change(31)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v097_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v098_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v098_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vz(_rv(closeadj, 252), 252)).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v099_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v099_signal(close: pd.Series) -> pd.Series:
    res = (_vov(_rv(close, 5), 126)).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v100_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v100_signal(close: pd.Series) -> pd.Series:
    res = (_vrank(_rv(close, 10), 252)).pct_change(31).pct_change(31)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v101_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v102_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v103_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v103_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vz(_rv(closeadj, 63), 252)).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v104_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v104_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vov(_rv(closeadj, 126), 126)).pct_change(31).pct_change(31)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v105_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v106_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v107_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v108_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v108_signal(close: pd.Series) -> pd.Series:
    res = (_vz(_rv(close, 21), 63)).pct_change(31).pct_change(31)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v109_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v110_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v111_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v111_signal(closeadj: pd.Series) -> pd.Series:
    res = (_rv(closeadj, 126)).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v112_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v113_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v114_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v115_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v115_signal(close: pd.Series) -> pd.Series:
    res = (_vrank(_rv(close, 21), 252)).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v116_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v116_signal(closeadj: pd.Series) -> pd.Series:
    res = (_rv(closeadj, 42)).pct_change(31).pct_change(31)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v117_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v118_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v119_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v119_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vov(_rv(closeadj, 252), 126)).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v120_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v120_signal(close: pd.Series) -> pd.Series:
    res = (_vrank(_rv(close, 5), 252)).pct_change(31).pct_change(31)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v121_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v122_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v123_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v123_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vz(_rv(closeadj, 42), 252)).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v124_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v124_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vov(_rv(closeadj, 63), 126)).pct_change(31).pct_change(31)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v125_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v126_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v127_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v128_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v128_signal(close: pd.Series) -> pd.Series:
    res = (_vz(_rv(close, 10), 63)).pct_change(31).pct_change(31)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v129_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v130_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v131_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v131_signal(closeadj: pd.Series) -> pd.Series:
    res = (_rv(closeadj, 63)).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v132_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v133_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v134_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v135_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v135_signal(close: pd.Series) -> pd.Series:
    res = (_vrank(_rv(close, 10), 252)).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v136_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v136_signal(close: pd.Series) -> pd.Series:
    res = (_rv(close, 21)).pct_change(31).pct_change(31)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v137_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v138_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v139_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v139_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vov(_rv(closeadj, 126), 126)).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v140_signal: jerk of base feature
def f16rvts_f16_realized_volatility_term_structure_jerk_v140_signal(closeadj: pd.Series) -> pd.Series:
    res = (_vrank(_rv(closeadj, 252), 252)).pct_change(31).pct_change(31)
    return res.replace([np.inf, -np.inf], np.nan)

# f16rvts_f16_realized_volatility_term_structure_jerk_v141_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v142_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v143_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v144_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v145_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v146_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v147_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v148_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v149_signal: jerk of base feature

# f16rvts_f16_realized_volatility_term_structure_jerk_v150_signal: jerk of base feature

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj"]}
FEAT_NAMES = [f for f in globals() if f.startswith("f16rvts_") and f.endswith("_signal")]
F16_REALIZED_VOLATILITY_TERM_STRUCTURE_JERK_REGISTRY_001_150 = {
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
    for n, c in F16_REALIZED_VOLATILITY_TERM_STRUCTURE_JERK_REGISTRY_001_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("OK")