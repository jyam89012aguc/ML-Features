
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
    market_cap = df['marketcap']
    at = df['assets']
    re = df['retearn']
    iv_proxy = (ni / 0.1) / market_cap.replace(0, np.nan)
    f = {}
    f['f42_intrinsic_value_margin_of_safety_001'] = _z(_roc(iv_proxy, 63), 63)
    f['f42_intrinsic_value_margin_of_safety_002'] = _z(iv_proxy.diff(126), 252)
    f['f42_intrinsic_value_margin_of_safety_003'] = _z(iv_proxy / _std(iv_proxy, 252).replace(0, 1), 252)
    f['f42_intrinsic_value_margin_of_safety_004'] = _z(_ema(iv_proxy, 504) - _ema(iv_proxy, 1008), 1512)
    f['f42_intrinsic_value_margin_of_safety_005'] = _z(iv_proxy, 21)
    f['f42_intrinsic_value_margin_of_safety_006'] = _z(_roc(iv_proxy, 63), 63)
    f['f42_intrinsic_value_margin_of_safety_007'] = _z(iv_proxy.diff(126), 252)
    f['f42_intrinsic_value_margin_of_safety_008'] = _z(iv_proxy / _std(iv_proxy, 252).replace(0, 1), 252)
    f['f42_intrinsic_value_margin_of_safety_009'] = _z(_ema(iv_proxy, 504) - _ema(iv_proxy, 1008), 1512)
    f['f42_intrinsic_value_margin_of_safety_010'] = _z(iv_proxy, 21)
    f['f42_intrinsic_value_margin_of_safety_011'] = _z(_roc(iv_proxy, 63), 63)
    f['f42_intrinsic_value_margin_of_safety_012'] = _z(iv_proxy.diff(126), 252)
    f['f42_intrinsic_value_margin_of_safety_013'] = _z(iv_proxy / _std(iv_proxy, 252).replace(0, 1), 252)
    f['f42_intrinsic_value_margin_of_safety_014'] = _z(_ema(iv_proxy, 504) - _ema(iv_proxy, 1008), 1512)
    f['f42_intrinsic_value_margin_of_safety_015'] = _z(iv_proxy, 21)
    f['f42_intrinsic_value_margin_of_safety_016'] = _z(_roc(iv_proxy, 63), 63)
    f['f42_intrinsic_value_margin_of_safety_017'] = _z(iv_proxy.diff(126), 252)
    f['f42_intrinsic_value_margin_of_safety_018'] = _z(iv_proxy / _std(iv_proxy, 252).replace(0, 1), 252)
    f['f42_intrinsic_value_margin_of_safety_019'] = _z(_ema(iv_proxy, 504) - _ema(iv_proxy, 1008), 1512)
    f['f42_intrinsic_value_margin_of_safety_020'] = _z(iv_proxy, 21)
    f['f42_intrinsic_value_margin_of_safety_021'] = _z(_roc(iv_proxy, 63), 63)
    f['f42_intrinsic_value_margin_of_safety_022'] = _z(iv_proxy.diff(126), 252)
    f['f42_intrinsic_value_margin_of_safety_023'] = _z(iv_proxy / _std(iv_proxy, 252).replace(0, 1), 252)
    f['f42_intrinsic_value_margin_of_safety_024'] = _z(_ema(iv_proxy, 504) - _ema(iv_proxy, 1008), 1512)
    f['f42_intrinsic_value_margin_of_safety_025'] = _z(iv_proxy, 21)
    f['f42_intrinsic_value_margin_of_safety_026'] = _z(_roc(iv_proxy, 63), 63)
    f['f42_intrinsic_value_margin_of_safety_027'] = _z(iv_proxy.diff(126), 252)
    f['f42_intrinsic_value_margin_of_safety_028'] = _z(iv_proxy / _std(iv_proxy, 252).replace(0, 1), 252)
    f['f42_intrinsic_value_margin_of_safety_029'] = _z(_ema(iv_proxy, 504) - _ema(iv_proxy, 1008), 1512)
    f['f42_intrinsic_value_margin_of_safety_030'] = _z(iv_proxy, 21)
    f['f42_intrinsic_value_margin_of_safety_031'] = _z(_roc(iv_proxy, 63), 63)
    f['f42_intrinsic_value_margin_of_safety_032'] = _z(iv_proxy.diff(126), 252)
    f['f42_intrinsic_value_margin_of_safety_033'] = _z(iv_proxy / _std(iv_proxy, 252).replace(0, 1), 252)
    f['f42_intrinsic_value_margin_of_safety_034'] = _z(_ema(iv_proxy, 504) - _ema(iv_proxy, 1008), 1512)
    f['f42_intrinsic_value_margin_of_safety_035'] = _z(iv_proxy, 21)
    f['f42_intrinsic_value_margin_of_safety_036'] = _z(_roc(iv_proxy, 63), 63)
    f['f42_intrinsic_value_margin_of_safety_037'] = _z(iv_proxy.diff(126), 252)
    f['f42_intrinsic_value_margin_of_safety_038'] = _z(iv_proxy / _std(iv_proxy, 252).replace(0, 1), 252)
    f['f42_intrinsic_value_margin_of_safety_039'] = _z(_ema(iv_proxy, 504) - _ema(iv_proxy, 1008), 1512)
    f['f42_intrinsic_value_margin_of_safety_040'] = _z(iv_proxy, 21)
    f['f42_intrinsic_value_margin_of_safety_041'] = _z(_roc(iv_proxy, 63), 63)
    f['f42_intrinsic_value_margin_of_safety_042'] = _z(iv_proxy.diff(126), 252)
    f['f42_intrinsic_value_margin_of_safety_043'] = _z(iv_proxy / _std(iv_proxy, 252).replace(0, 1), 252)
    f['f42_intrinsic_value_margin_of_safety_044'] = _z(_ema(iv_proxy, 504) - _ema(iv_proxy, 1008), 1512)
    f['f42_intrinsic_value_margin_of_safety_045'] = _z(iv_proxy, 21)
    f['f42_intrinsic_value_margin_of_safety_046'] = _z(_roc(iv_proxy, 63), 63)
    f['f42_intrinsic_value_margin_of_safety_047'] = _z(iv_proxy.diff(126), 252)
    f['f42_intrinsic_value_margin_of_safety_048'] = _z(iv_proxy / _std(iv_proxy, 252).replace(0, 1), 252)
    f['f42_intrinsic_value_margin_of_safety_049'] = _z(_ema(iv_proxy, 504) - _ema(iv_proxy, 1008), 1512)
    f['f42_intrinsic_value_margin_of_safety_050'] = _z(iv_proxy, 21)
    f['f42_intrinsic_value_margin_of_safety_051'] = _z(_roc(iv_proxy, 63), 63)
    f['f42_intrinsic_value_margin_of_safety_052'] = _z(iv_proxy.diff(126), 252)
    f['f42_intrinsic_value_margin_of_safety_053'] = _z(iv_proxy / _std(iv_proxy, 252).replace(0, 1), 252)
    f['f42_intrinsic_value_margin_of_safety_054'] = _z(_ema(iv_proxy, 504) - _ema(iv_proxy, 1008), 1512)
    f['f42_intrinsic_value_margin_of_safety_055'] = _z(iv_proxy, 21)
    f['f42_intrinsic_value_margin_of_safety_056'] = _z(_roc(iv_proxy, 63), 63)
    f['f42_intrinsic_value_margin_of_safety_057'] = _z(iv_proxy.diff(126), 252)
    f['f42_intrinsic_value_margin_of_safety_058'] = _z(iv_proxy / _std(iv_proxy, 252).replace(0, 1), 252)
    f['f42_intrinsic_value_margin_of_safety_059'] = _z(_ema(iv_proxy, 504) - _ema(iv_proxy, 1008), 1512)
    f['f42_intrinsic_value_margin_of_safety_060'] = _z(iv_proxy, 21)
    f['f42_intrinsic_value_margin_of_safety_061'] = _z(_roc(iv_proxy, 63), 63)
    f['f42_intrinsic_value_margin_of_safety_062'] = _z(iv_proxy.diff(126), 252)
    f['f42_intrinsic_value_margin_of_safety_063'] = _z(iv_proxy / _std(iv_proxy, 252).replace(0, 1), 252)
    f['f42_intrinsic_value_margin_of_safety_064'] = _z(_ema(iv_proxy, 504) - _ema(iv_proxy, 1008), 1512)
    f['f42_intrinsic_value_margin_of_safety_065'] = _z(iv_proxy, 21)
    f['f42_intrinsic_value_margin_of_safety_066'] = _z(_roc(iv_proxy, 63), 63)
    f['f42_intrinsic_value_margin_of_safety_067'] = _z(iv_proxy.diff(126), 252)
    f['f42_intrinsic_value_margin_of_safety_068'] = _z(iv_proxy / _std(iv_proxy, 252).replace(0, 1), 252)
    f['f42_intrinsic_value_margin_of_safety_069'] = _z(_ema(iv_proxy, 504) - _ema(iv_proxy, 1008), 1512)
    f['f42_intrinsic_value_margin_of_safety_070'] = _z(iv_proxy, 21)
    f['f42_intrinsic_value_margin_of_safety_071'] = _z(_roc(iv_proxy, 63), 63)
    f['f42_intrinsic_value_margin_of_safety_072'] = _z(iv_proxy.diff(126), 252)
    f['f42_intrinsic_value_margin_of_safety_073'] = _z(iv_proxy / _std(iv_proxy, 252).replace(0, 1), 252)
    f['f42_intrinsic_value_margin_of_safety_074'] = _z(_ema(iv_proxy, 504) - _ema(iv_proxy, 1008), 1512)
    f['f42_intrinsic_value_margin_of_safety_075'] = _z(iv_proxy, 21)
    return pd.DataFrame(f)