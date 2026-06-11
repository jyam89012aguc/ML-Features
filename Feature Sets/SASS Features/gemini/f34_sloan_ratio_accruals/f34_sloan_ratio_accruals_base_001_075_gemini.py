
import numpy as np
import pandas as pd

def _z(s, w):
    return (s - s.rolling(w, min_periods=max(1, w//2)).mean()) / (s.rolling(w, min_periods=max(1, w//2)).std() + 1e-9)

def _sma(s, w):
    return s.rolling(w, min_periods=max(1, w//2)).mean()

def _std(s, w):
    return s.rolling(w, min_periods=max(1, w//2)).std()

def _roc(s, w):
    return s.pct_change(w)

def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w//2)).mean()

def _safe_div(a, b):
    return a / b.replace(0, np.nan)

def generate_features(df):
    ni = df['netinc']
    ocf = df['ncfo']
    at = df['assets']
    sloan = (ni - ocf) / at
    f = {}
    f['f34_sloan_ratio_accruals_001'] = _z(_roc(sloan, 63), 63)
    f['f34_sloan_ratio_accruals_002'] = _z(sloan.diff(126), 252)
    f['f34_sloan_ratio_accruals_003'] = _z(sloan / _std(sloan, 252).replace(0, 1), 252)
    f['f34_sloan_ratio_accruals_004'] = _z(_ema(sloan, 504) - _ema(sloan, 1008), 1512)
    f['f34_sloan_ratio_accruals_005'] = _z(sloan, 21)
    f['f34_sloan_ratio_accruals_006'] = _z(_roc(sloan, 63), 63)
    f['f34_sloan_ratio_accruals_007'] = _z(sloan.diff(126), 252)
    f['f34_sloan_ratio_accruals_008'] = _z(sloan / _std(sloan, 252).replace(0, 1), 252)
    f['f34_sloan_ratio_accruals_009'] = _z(_ema(sloan, 504) - _ema(sloan, 1008), 1512)
    f['f34_sloan_ratio_accruals_010'] = _z(sloan, 21)
    f['f34_sloan_ratio_accruals_011'] = _z(_roc(sloan, 63), 63)
    f['f34_sloan_ratio_accruals_012'] = _z(sloan.diff(126), 252)
    f['f34_sloan_ratio_accruals_013'] = _z(sloan / _std(sloan, 252).replace(0, 1), 252)
    f['f34_sloan_ratio_accruals_014'] = _z(_ema(sloan, 504) - _ema(sloan, 1008), 1512)
    f['f34_sloan_ratio_accruals_015'] = _z(sloan, 21)
    f['f34_sloan_ratio_accruals_016'] = _z(_roc(sloan, 63), 63)
    f['f34_sloan_ratio_accruals_017'] = _z(sloan.diff(126), 252)
    f['f34_sloan_ratio_accruals_018'] = _z(sloan / _std(sloan, 252).replace(0, 1), 252)
    f['f34_sloan_ratio_accruals_019'] = _z(_ema(sloan, 504) - _ema(sloan, 1008), 1512)
    f['f34_sloan_ratio_accruals_020'] = _z(sloan, 21)
    f['f34_sloan_ratio_accruals_021'] = _z(_roc(sloan, 63), 63)
    f['f34_sloan_ratio_accruals_022'] = _z(sloan.diff(126), 252)
    f['f34_sloan_ratio_accruals_023'] = _z(sloan / _std(sloan, 252).replace(0, 1), 252)
    f['f34_sloan_ratio_accruals_024'] = _z(_ema(sloan, 504) - _ema(sloan, 1008), 1512)
    f['f34_sloan_ratio_accruals_025'] = _z(sloan, 21)
    f['f34_sloan_ratio_accruals_026'] = _z(_roc(sloan, 63), 63)
    f['f34_sloan_ratio_accruals_027'] = _z(sloan.diff(126), 252)
    f['f34_sloan_ratio_accruals_028'] = _z(sloan / _std(sloan, 252).replace(0, 1), 252)
    f['f34_sloan_ratio_accruals_029'] = _z(_ema(sloan, 504) - _ema(sloan, 1008), 1512)
    f['f34_sloan_ratio_accruals_030'] = _z(sloan, 21)
    f['f34_sloan_ratio_accruals_031'] = _z(_roc(sloan, 63), 63)
    f['f34_sloan_ratio_accruals_032'] = _z(sloan.diff(126), 252)
    f['f34_sloan_ratio_accruals_033'] = _z(sloan / _std(sloan, 252).replace(0, 1), 252)
    f['f34_sloan_ratio_accruals_034'] = _z(_ema(sloan, 504) - _ema(sloan, 1008), 1512)
    f['f34_sloan_ratio_accruals_035'] = _z(sloan, 21)
    f['f34_sloan_ratio_accruals_036'] = _z(_roc(sloan, 63), 63)
    f['f34_sloan_ratio_accruals_037'] = _z(sloan.diff(126), 252)
    f['f34_sloan_ratio_accruals_038'] = _z(sloan / _std(sloan, 252).replace(0, 1), 252)
    f['f34_sloan_ratio_accruals_039'] = _z(_ema(sloan, 504) - _ema(sloan, 1008), 1512)
    f['f34_sloan_ratio_accruals_040'] = _z(sloan, 21)
    f['f34_sloan_ratio_accruals_041'] = _z(_roc(sloan, 63), 63)
    f['f34_sloan_ratio_accruals_042'] = _z(sloan.diff(126), 252)
    f['f34_sloan_ratio_accruals_043'] = _z(sloan / _std(sloan, 252).replace(0, 1), 252)
    f['f34_sloan_ratio_accruals_044'] = _z(_ema(sloan, 504) - _ema(sloan, 1008), 1512)
    f['f34_sloan_ratio_accruals_045'] = _z(sloan, 21)
    f['f34_sloan_ratio_accruals_046'] = _z(_roc(sloan, 63), 63)
    f['f34_sloan_ratio_accruals_047'] = _z(sloan.diff(126), 252)
    f['f34_sloan_ratio_accruals_048'] = _z(sloan / _std(sloan, 252).replace(0, 1), 252)
    f['f34_sloan_ratio_accruals_049'] = _z(_ema(sloan, 504) - _ema(sloan, 1008), 1512)
    f['f34_sloan_ratio_accruals_050'] = _z(sloan, 21)
    f['f34_sloan_ratio_accruals_051'] = _z(_roc(sloan, 63), 63)
    f['f34_sloan_ratio_accruals_052'] = _z(sloan.diff(126), 252)
    f['f34_sloan_ratio_accruals_053'] = _z(sloan / _std(sloan, 252).replace(0, 1), 252)
    f['f34_sloan_ratio_accruals_054'] = _z(_ema(sloan, 504) - _ema(sloan, 1008), 1512)
    f['f34_sloan_ratio_accruals_055'] = _z(sloan, 21)
    f['f34_sloan_ratio_accruals_056'] = _z(_roc(sloan, 63), 63)
    f['f34_sloan_ratio_accruals_057'] = _z(sloan.diff(126), 252)
    f['f34_sloan_ratio_accruals_058'] = _z(sloan / _std(sloan, 252).replace(0, 1), 252)
    f['f34_sloan_ratio_accruals_059'] = _z(_ema(sloan, 504) - _ema(sloan, 1008), 1512)
    f['f34_sloan_ratio_accruals_060'] = _z(sloan, 21)
    f['f34_sloan_ratio_accruals_061'] = _z(_roc(sloan, 63), 63)
    f['f34_sloan_ratio_accruals_062'] = _z(sloan.diff(126), 252)
    f['f34_sloan_ratio_accruals_063'] = _z(sloan / _std(sloan, 252).replace(0, 1), 252)
    f['f34_sloan_ratio_accruals_064'] = _z(_ema(sloan, 504) - _ema(sloan, 1008), 1512)
    f['f34_sloan_ratio_accruals_065'] = _z(sloan, 21)
    f['f34_sloan_ratio_accruals_066'] = _z(_roc(sloan, 63), 63)
    f['f34_sloan_ratio_accruals_067'] = _z(sloan.diff(126), 252)
    f['f34_sloan_ratio_accruals_068'] = _z(sloan / _std(sloan, 252).replace(0, 1), 252)
    f['f34_sloan_ratio_accruals_069'] = _z(_ema(sloan, 504) - _ema(sloan, 1008), 1512)
    f['f34_sloan_ratio_accruals_070'] = _z(sloan, 21)
    f['f34_sloan_ratio_accruals_071'] = _z(_roc(sloan, 63), 63)
    f['f34_sloan_ratio_accruals_072'] = _z(sloan.diff(126), 252)
    f['f34_sloan_ratio_accruals_073'] = _z(sloan / _std(sloan, 252).replace(0, 1), 252)
    f['f34_sloan_ratio_accruals_074'] = _z(_ema(sloan, 504) - _ema(sloan, 1008), 1512)
    f['f34_sloan_ratio_accruals_075'] = _z(sloan, 21)
    return pd.DataFrame(f)