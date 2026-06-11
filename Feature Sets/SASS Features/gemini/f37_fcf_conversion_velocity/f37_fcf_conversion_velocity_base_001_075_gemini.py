
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
    fcf = df['fcf']
    ni = df['netinc']
    ebitda = df['ebitda']
    fcf_conv = fcf / ni.replace(0, np.nan)
    f = {}
    f['f37_fcf_conversion_velocity_001'] = _z(_roc(fcf_conv, 63), 63)
    f['f37_fcf_conversion_velocity_002'] = _z(fcf_conv.diff(126), 252)
    f['f37_fcf_conversion_velocity_003'] = _z(fcf_conv / _std(fcf_conv, 252).replace(0, 1), 252)
    f['f37_fcf_conversion_velocity_004'] = _z(_ema(fcf_conv, 504) - _ema(fcf_conv, 1008), 1512)
    f['f37_fcf_conversion_velocity_005'] = _z(fcf_conv, 21)
    f['f37_fcf_conversion_velocity_006'] = _z(_roc(fcf_conv, 63), 63)
    f['f37_fcf_conversion_velocity_007'] = _z(fcf_conv.diff(126), 252)
    f['f37_fcf_conversion_velocity_008'] = _z(fcf_conv / _std(fcf_conv, 252).replace(0, 1), 252)
    f['f37_fcf_conversion_velocity_009'] = _z(_ema(fcf_conv, 504) - _ema(fcf_conv, 1008), 1512)
    f['f37_fcf_conversion_velocity_010'] = _z(fcf_conv, 21)
    f['f37_fcf_conversion_velocity_011'] = _z(_roc(fcf_conv, 63), 63)
    f['f37_fcf_conversion_velocity_012'] = _z(fcf_conv.diff(126), 252)
    f['f37_fcf_conversion_velocity_013'] = _z(fcf_conv / _std(fcf_conv, 252).replace(0, 1), 252)
    f['f37_fcf_conversion_velocity_014'] = _z(_ema(fcf_conv, 504) - _ema(fcf_conv, 1008), 1512)
    f['f37_fcf_conversion_velocity_015'] = _z(fcf_conv, 21)
    f['f37_fcf_conversion_velocity_016'] = _z(_roc(fcf_conv, 63), 63)
    f['f37_fcf_conversion_velocity_017'] = _z(fcf_conv.diff(126), 252)
    f['f37_fcf_conversion_velocity_018'] = _z(fcf_conv / _std(fcf_conv, 252).replace(0, 1), 252)
    f['f37_fcf_conversion_velocity_019'] = _z(_ema(fcf_conv, 504) - _ema(fcf_conv, 1008), 1512)
    f['f37_fcf_conversion_velocity_020'] = _z(fcf_conv, 21)
    f['f37_fcf_conversion_velocity_021'] = _z(_roc(fcf_conv, 63), 63)
    f['f37_fcf_conversion_velocity_022'] = _z(fcf_conv.diff(126), 252)
    f['f37_fcf_conversion_velocity_023'] = _z(fcf_conv / _std(fcf_conv, 252).replace(0, 1), 252)
    f['f37_fcf_conversion_velocity_024'] = _z(_ema(fcf_conv, 504) - _ema(fcf_conv, 1008), 1512)
    f['f37_fcf_conversion_velocity_025'] = _z(fcf_conv, 21)
    f['f37_fcf_conversion_velocity_026'] = _z(_roc(fcf_conv, 63), 63)
    f['f37_fcf_conversion_velocity_027'] = _z(fcf_conv.diff(126), 252)
    f['f37_fcf_conversion_velocity_028'] = _z(fcf_conv / _std(fcf_conv, 252).replace(0, 1), 252)
    f['f37_fcf_conversion_velocity_029'] = _z(_ema(fcf_conv, 504) - _ema(fcf_conv, 1008), 1512)
    f['f37_fcf_conversion_velocity_030'] = _z(fcf_conv, 21)
    f['f37_fcf_conversion_velocity_031'] = _z(_roc(fcf_conv, 63), 63)
    f['f37_fcf_conversion_velocity_032'] = _z(fcf_conv.diff(126), 252)
    f['f37_fcf_conversion_velocity_033'] = _z(fcf_conv / _std(fcf_conv, 252).replace(0, 1), 252)
    f['f37_fcf_conversion_velocity_034'] = _z(_ema(fcf_conv, 504) - _ema(fcf_conv, 1008), 1512)
    f['f37_fcf_conversion_velocity_035'] = _z(fcf_conv, 21)
    f['f37_fcf_conversion_velocity_036'] = _z(_roc(fcf_conv, 63), 63)
    f['f37_fcf_conversion_velocity_037'] = _z(fcf_conv.diff(126), 252)
    f['f37_fcf_conversion_velocity_038'] = _z(fcf_conv / _std(fcf_conv, 252).replace(0, 1), 252)
    f['f37_fcf_conversion_velocity_039'] = _z(_ema(fcf_conv, 504) - _ema(fcf_conv, 1008), 1512)
    f['f37_fcf_conversion_velocity_040'] = _z(fcf_conv, 21)
    f['f37_fcf_conversion_velocity_041'] = _z(_roc(fcf_conv, 63), 63)
    f['f37_fcf_conversion_velocity_042'] = _z(fcf_conv.diff(126), 252)
    f['f37_fcf_conversion_velocity_043'] = _z(fcf_conv / _std(fcf_conv, 252).replace(0, 1), 252)
    f['f37_fcf_conversion_velocity_044'] = _z(_ema(fcf_conv, 504) - _ema(fcf_conv, 1008), 1512)
    f['f37_fcf_conversion_velocity_045'] = _z(fcf_conv, 21)
    f['f37_fcf_conversion_velocity_046'] = _z(_roc(fcf_conv, 63), 63)
    f['f37_fcf_conversion_velocity_047'] = _z(fcf_conv.diff(126), 252)
    f['f37_fcf_conversion_velocity_048'] = _z(fcf_conv / _std(fcf_conv, 252).replace(0, 1), 252)
    f['f37_fcf_conversion_velocity_049'] = _z(_ema(fcf_conv, 504) - _ema(fcf_conv, 1008), 1512)
    f['f37_fcf_conversion_velocity_050'] = _z(fcf_conv, 21)
    f['f37_fcf_conversion_velocity_051'] = _z(_roc(fcf_conv, 63), 63)
    f['f37_fcf_conversion_velocity_052'] = _z(fcf_conv.diff(126), 252)
    f['f37_fcf_conversion_velocity_053'] = _z(fcf_conv / _std(fcf_conv, 252).replace(0, 1), 252)
    f['f37_fcf_conversion_velocity_054'] = _z(_ema(fcf_conv, 504) - _ema(fcf_conv, 1008), 1512)
    f['f37_fcf_conversion_velocity_055'] = _z(fcf_conv, 21)
    f['f37_fcf_conversion_velocity_056'] = _z(_roc(fcf_conv, 63), 63)
    f['f37_fcf_conversion_velocity_057'] = _z(fcf_conv.diff(126), 252)
    f['f37_fcf_conversion_velocity_058'] = _z(fcf_conv / _std(fcf_conv, 252).replace(0, 1), 252)
    f['f37_fcf_conversion_velocity_059'] = _z(_ema(fcf_conv, 504) - _ema(fcf_conv, 1008), 1512)
    f['f37_fcf_conversion_velocity_060'] = _z(fcf_conv, 21)
    f['f37_fcf_conversion_velocity_061'] = _z(_roc(fcf_conv, 63), 63)
    f['f37_fcf_conversion_velocity_062'] = _z(fcf_conv.diff(126), 252)
    f['f37_fcf_conversion_velocity_063'] = _z(fcf_conv / _std(fcf_conv, 252).replace(0, 1), 252)
    f['f37_fcf_conversion_velocity_064'] = _z(_ema(fcf_conv, 504) - _ema(fcf_conv, 1008), 1512)
    f['f37_fcf_conversion_velocity_065'] = _z(fcf_conv, 21)
    f['f37_fcf_conversion_velocity_066'] = _z(_roc(fcf_conv, 63), 63)
    f['f37_fcf_conversion_velocity_067'] = _z(fcf_conv.diff(126), 252)
    f['f37_fcf_conversion_velocity_068'] = _z(fcf_conv / _std(fcf_conv, 252).replace(0, 1), 252)
    f['f37_fcf_conversion_velocity_069'] = _z(_ema(fcf_conv, 504) - _ema(fcf_conv, 1008), 1512)
    f['f37_fcf_conversion_velocity_070'] = _z(fcf_conv, 21)
    f['f37_fcf_conversion_velocity_071'] = _z(_roc(fcf_conv, 63), 63)
    f['f37_fcf_conversion_velocity_072'] = _z(fcf_conv.diff(126), 252)
    f['f37_fcf_conversion_velocity_073'] = _z(fcf_conv / _std(fcf_conv, 252).replace(0, 1), 252)
    f['f37_fcf_conversion_velocity_074'] = _z(_ema(fcf_conv, 504) - _ema(fcf_conv, 1008), 1512)
    f['f37_fcf_conversion_velocity_075'] = _z(fcf_conv, 21)
    return pd.DataFrame(f)