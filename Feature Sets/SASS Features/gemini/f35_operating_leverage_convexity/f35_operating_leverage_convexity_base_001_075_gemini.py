
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
    ebit = df['ebit']
    rev = df['revenue']
    op_lev = ebit.pct_change(63) / rev.pct_change(63).replace(0, np.nan)
    f = {}
    f['f35_operating_leverage_convexity_001'] = _z(_roc(op_lev, 63), 63)
    f['f35_operating_leverage_convexity_002'] = _z(op_lev.diff(126), 252)
    f['f35_operating_leverage_convexity_003'] = _z(op_lev / _std(op_lev, 252).replace(0, 1), 252)
    f['f35_operating_leverage_convexity_004'] = _z(_ema(op_lev, 504) - _ema(op_lev, 1008), 1512)
    f['f35_operating_leverage_convexity_005'] = _z(op_lev, 21)
    f['f35_operating_leverage_convexity_006'] = _z(_roc(op_lev, 63), 63)
    f['f35_operating_leverage_convexity_007'] = _z(op_lev.diff(126), 252)
    f['f35_operating_leverage_convexity_008'] = _z(op_lev / _std(op_lev, 252).replace(0, 1), 252)
    f['f35_operating_leverage_convexity_009'] = _z(_ema(op_lev, 504) - _ema(op_lev, 1008), 1512)
    f['f35_operating_leverage_convexity_010'] = _z(op_lev, 21)
    f['f35_operating_leverage_convexity_011'] = _z(_roc(op_lev, 63), 63)
    f['f35_operating_leverage_convexity_012'] = _z(op_lev.diff(126), 252)
    f['f35_operating_leverage_convexity_013'] = _z(op_lev / _std(op_lev, 252).replace(0, 1), 252)
    f['f35_operating_leverage_convexity_014'] = _z(_ema(op_lev, 504) - _ema(op_lev, 1008), 1512)
    f['f35_operating_leverage_convexity_015'] = _z(op_lev, 21)
    f['f35_operating_leverage_convexity_016'] = _z(_roc(op_lev, 63), 63)
    f['f35_operating_leverage_convexity_017'] = _z(op_lev.diff(126), 252)
    f['f35_operating_leverage_convexity_018'] = _z(op_lev / _std(op_lev, 252).replace(0, 1), 252)
    f['f35_operating_leverage_convexity_019'] = _z(_ema(op_lev, 504) - _ema(op_lev, 1008), 1512)
    f['f35_operating_leverage_convexity_020'] = _z(op_lev, 21)
    f['f35_operating_leverage_convexity_021'] = _z(_roc(op_lev, 63), 63)
    f['f35_operating_leverage_convexity_022'] = _z(op_lev.diff(126), 252)
    f['f35_operating_leverage_convexity_023'] = _z(op_lev / _std(op_lev, 252).replace(0, 1), 252)
    f['f35_operating_leverage_convexity_024'] = _z(_ema(op_lev, 504) - _ema(op_lev, 1008), 1512)
    f['f35_operating_leverage_convexity_025'] = _z(op_lev, 21)
    f['f35_operating_leverage_convexity_026'] = _z(_roc(op_lev, 63), 63)
    f['f35_operating_leverage_convexity_027'] = _z(op_lev.diff(126), 252)
    f['f35_operating_leverage_convexity_028'] = _z(op_lev / _std(op_lev, 252).replace(0, 1), 252)
    f['f35_operating_leverage_convexity_029'] = _z(_ema(op_lev, 504) - _ema(op_lev, 1008), 1512)
    f['f35_operating_leverage_convexity_030'] = _z(op_lev, 21)
    f['f35_operating_leverage_convexity_031'] = _z(_roc(op_lev, 63), 63)
    f['f35_operating_leverage_convexity_032'] = _z(op_lev.diff(126), 252)
    f['f35_operating_leverage_convexity_033'] = _z(op_lev / _std(op_lev, 252).replace(0, 1), 252)
    f['f35_operating_leverage_convexity_034'] = _z(_ema(op_lev, 504) - _ema(op_lev, 1008), 1512)
    f['f35_operating_leverage_convexity_035'] = _z(op_lev, 21)
    f['f35_operating_leverage_convexity_036'] = _z(_roc(op_lev, 63), 63)
    f['f35_operating_leverage_convexity_037'] = _z(op_lev.diff(126), 252)
    f['f35_operating_leverage_convexity_038'] = _z(op_lev / _std(op_lev, 252).replace(0, 1), 252)
    f['f35_operating_leverage_convexity_039'] = _z(_ema(op_lev, 504) - _ema(op_lev, 1008), 1512)
    f['f35_operating_leverage_convexity_040'] = _z(op_lev, 21)
    f['f35_operating_leverage_convexity_041'] = _z(_roc(op_lev, 63), 63)
    f['f35_operating_leverage_convexity_042'] = _z(op_lev.diff(126), 252)
    f['f35_operating_leverage_convexity_043'] = _z(op_lev / _std(op_lev, 252).replace(0, 1), 252)
    f['f35_operating_leverage_convexity_044'] = _z(_ema(op_lev, 504) - _ema(op_lev, 1008), 1512)
    f['f35_operating_leverage_convexity_045'] = _z(op_lev, 21)
    f['f35_operating_leverage_convexity_046'] = _z(_roc(op_lev, 63), 63)
    f['f35_operating_leverage_convexity_047'] = _z(op_lev.diff(126), 252)
    f['f35_operating_leverage_convexity_048'] = _z(op_lev / _std(op_lev, 252).replace(0, 1), 252)
    f['f35_operating_leverage_convexity_049'] = _z(_ema(op_lev, 504) - _ema(op_lev, 1008), 1512)
    f['f35_operating_leverage_convexity_050'] = _z(op_lev, 21)
    f['f35_operating_leverage_convexity_051'] = _z(_roc(op_lev, 63), 63)
    f['f35_operating_leverage_convexity_052'] = _z(op_lev.diff(126), 252)
    f['f35_operating_leverage_convexity_053'] = _z(op_lev / _std(op_lev, 252).replace(0, 1), 252)
    f['f35_operating_leverage_convexity_054'] = _z(_ema(op_lev, 504) - _ema(op_lev, 1008), 1512)
    f['f35_operating_leverage_convexity_055'] = _z(op_lev, 21)
    f['f35_operating_leverage_convexity_056'] = _z(_roc(op_lev, 63), 63)
    f['f35_operating_leverage_convexity_057'] = _z(op_lev.diff(126), 252)
    f['f35_operating_leverage_convexity_058'] = _z(op_lev / _std(op_lev, 252).replace(0, 1), 252)
    f['f35_operating_leverage_convexity_059'] = _z(_ema(op_lev, 504) - _ema(op_lev, 1008), 1512)
    f['f35_operating_leverage_convexity_060'] = _z(op_lev, 21)
    f['f35_operating_leverage_convexity_061'] = _z(_roc(op_lev, 63), 63)
    f['f35_operating_leverage_convexity_062'] = _z(op_lev.diff(126), 252)
    f['f35_operating_leverage_convexity_063'] = _z(op_lev / _std(op_lev, 252).replace(0, 1), 252)
    f['f35_operating_leverage_convexity_064'] = _z(_ema(op_lev, 504) - _ema(op_lev, 1008), 1512)
    f['f35_operating_leverage_convexity_065'] = _z(op_lev, 21)
    f['f35_operating_leverage_convexity_066'] = _z(_roc(op_lev, 63), 63)
    f['f35_operating_leverage_convexity_067'] = _z(op_lev.diff(126), 252)
    f['f35_operating_leverage_convexity_068'] = _z(op_lev / _std(op_lev, 252).replace(0, 1), 252)
    f['f35_operating_leverage_convexity_069'] = _z(_ema(op_lev, 504) - _ema(op_lev, 1008), 1512)
    f['f35_operating_leverage_convexity_070'] = _z(op_lev, 21)
    f['f35_operating_leverage_convexity_071'] = _z(_roc(op_lev, 63), 63)
    f['f35_operating_leverage_convexity_072'] = _z(op_lev.diff(126), 252)
    f['f35_operating_leverage_convexity_073'] = _z(op_lev / _std(op_lev, 252).replace(0, 1), 252)
    f['f35_operating_leverage_convexity_074'] = _z(_ema(op_lev, 504) - _ema(op_lev, 1008), 1512)
    f['f35_operating_leverage_convexity_075'] = _z(op_lev, 21)
    return pd.DataFrame(f)