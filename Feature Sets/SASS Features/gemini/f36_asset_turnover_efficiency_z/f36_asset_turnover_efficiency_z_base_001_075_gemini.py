
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
    rev = df['revenue']
    at = df['assets']
    aturn = rev / at
    f = {}
    f['f36_asset_turnover_efficiency_z_001'] = _z(_roc(aturn, 63), 63)
    f['f36_asset_turnover_efficiency_z_002'] = _z(aturn.diff(126), 252)
    f['f36_asset_turnover_efficiency_z_003'] = _z(aturn / _std(aturn, 252).replace(0, 1), 252)
    f['f36_asset_turnover_efficiency_z_004'] = _z(_ema(aturn, 504) - _ema(aturn, 1008), 1512)
    f['f36_asset_turnover_efficiency_z_005'] = _z(aturn, 21)
    f['f36_asset_turnover_efficiency_z_006'] = _z(_roc(aturn, 63), 63)
    f['f36_asset_turnover_efficiency_z_007'] = _z(aturn.diff(126), 252)
    f['f36_asset_turnover_efficiency_z_008'] = _z(aturn / _std(aturn, 252).replace(0, 1), 252)
    f['f36_asset_turnover_efficiency_z_009'] = _z(_ema(aturn, 504) - _ema(aturn, 1008), 1512)
    f['f36_asset_turnover_efficiency_z_010'] = _z(aturn, 21)
    f['f36_asset_turnover_efficiency_z_011'] = _z(_roc(aturn, 63), 63)
    f['f36_asset_turnover_efficiency_z_012'] = _z(aturn.diff(126), 252)
    f['f36_asset_turnover_efficiency_z_013'] = _z(aturn / _std(aturn, 252).replace(0, 1), 252)
    f['f36_asset_turnover_efficiency_z_014'] = _z(_ema(aturn, 504) - _ema(aturn, 1008), 1512)
    f['f36_asset_turnover_efficiency_z_015'] = _z(aturn, 21)
    f['f36_asset_turnover_efficiency_z_016'] = _z(_roc(aturn, 63), 63)
    f['f36_asset_turnover_efficiency_z_017'] = _z(aturn.diff(126), 252)
    f['f36_asset_turnover_efficiency_z_018'] = _z(aturn / _std(aturn, 252).replace(0, 1), 252)
    f['f36_asset_turnover_efficiency_z_019'] = _z(_ema(aturn, 504) - _ema(aturn, 1008), 1512)
    f['f36_asset_turnover_efficiency_z_020'] = _z(aturn, 21)
    f['f36_asset_turnover_efficiency_z_021'] = _z(_roc(aturn, 63), 63)
    f['f36_asset_turnover_efficiency_z_022'] = _z(aturn.diff(126), 252)
    f['f36_asset_turnover_efficiency_z_023'] = _z(aturn / _std(aturn, 252).replace(0, 1), 252)
    f['f36_asset_turnover_efficiency_z_024'] = _z(_ema(aturn, 504) - _ema(aturn, 1008), 1512)
    f['f36_asset_turnover_efficiency_z_025'] = _z(aturn, 21)
    f['f36_asset_turnover_efficiency_z_026'] = _z(_roc(aturn, 63), 63)
    f['f36_asset_turnover_efficiency_z_027'] = _z(aturn.diff(126), 252)
    f['f36_asset_turnover_efficiency_z_028'] = _z(aturn / _std(aturn, 252).replace(0, 1), 252)
    f['f36_asset_turnover_efficiency_z_029'] = _z(_ema(aturn, 504) - _ema(aturn, 1008), 1512)
    f['f36_asset_turnover_efficiency_z_030'] = _z(aturn, 21)
    f['f36_asset_turnover_efficiency_z_031'] = _z(_roc(aturn, 63), 63)
    f['f36_asset_turnover_efficiency_z_032'] = _z(aturn.diff(126), 252)
    f['f36_asset_turnover_efficiency_z_033'] = _z(aturn / _std(aturn, 252).replace(0, 1), 252)
    f['f36_asset_turnover_efficiency_z_034'] = _z(_ema(aturn, 504) - _ema(aturn, 1008), 1512)
    f['f36_asset_turnover_efficiency_z_035'] = _z(aturn, 21)
    f['f36_asset_turnover_efficiency_z_036'] = _z(_roc(aturn, 63), 63)
    f['f36_asset_turnover_efficiency_z_037'] = _z(aturn.diff(126), 252)
    f['f36_asset_turnover_efficiency_z_038'] = _z(aturn / _std(aturn, 252).replace(0, 1), 252)
    f['f36_asset_turnover_efficiency_z_039'] = _z(_ema(aturn, 504) - _ema(aturn, 1008), 1512)
    f['f36_asset_turnover_efficiency_z_040'] = _z(aturn, 21)
    f['f36_asset_turnover_efficiency_z_041'] = _z(_roc(aturn, 63), 63)
    f['f36_asset_turnover_efficiency_z_042'] = _z(aturn.diff(126), 252)
    f['f36_asset_turnover_efficiency_z_043'] = _z(aturn / _std(aturn, 252).replace(0, 1), 252)
    f['f36_asset_turnover_efficiency_z_044'] = _z(_ema(aturn, 504) - _ema(aturn, 1008), 1512)
    f['f36_asset_turnover_efficiency_z_045'] = _z(aturn, 21)
    f['f36_asset_turnover_efficiency_z_046'] = _z(_roc(aturn, 63), 63)
    f['f36_asset_turnover_efficiency_z_047'] = _z(aturn.diff(126), 252)
    f['f36_asset_turnover_efficiency_z_048'] = _z(aturn / _std(aturn, 252).replace(0, 1), 252)
    f['f36_asset_turnover_efficiency_z_049'] = _z(_ema(aturn, 504) - _ema(aturn, 1008), 1512)
    f['f36_asset_turnover_efficiency_z_050'] = _z(aturn, 21)
    f['f36_asset_turnover_efficiency_z_051'] = _z(_roc(aturn, 63), 63)
    f['f36_asset_turnover_efficiency_z_052'] = _z(aturn.diff(126), 252)
    f['f36_asset_turnover_efficiency_z_053'] = _z(aturn / _std(aturn, 252).replace(0, 1), 252)
    f['f36_asset_turnover_efficiency_z_054'] = _z(_ema(aturn, 504) - _ema(aturn, 1008), 1512)
    f['f36_asset_turnover_efficiency_z_055'] = _z(aturn, 21)
    f['f36_asset_turnover_efficiency_z_056'] = _z(_roc(aturn, 63), 63)
    f['f36_asset_turnover_efficiency_z_057'] = _z(aturn.diff(126), 252)
    f['f36_asset_turnover_efficiency_z_058'] = _z(aturn / _std(aturn, 252).replace(0, 1), 252)
    f['f36_asset_turnover_efficiency_z_059'] = _z(_ema(aturn, 504) - _ema(aturn, 1008), 1512)
    f['f36_asset_turnover_efficiency_z_060'] = _z(aturn, 21)
    f['f36_asset_turnover_efficiency_z_061'] = _z(_roc(aturn, 63), 63)
    f['f36_asset_turnover_efficiency_z_062'] = _z(aturn.diff(126), 252)
    f['f36_asset_turnover_efficiency_z_063'] = _z(aturn / _std(aturn, 252).replace(0, 1), 252)
    f['f36_asset_turnover_efficiency_z_064'] = _z(_ema(aturn, 504) - _ema(aturn, 1008), 1512)
    f['f36_asset_turnover_efficiency_z_065'] = _z(aturn, 21)
    f['f36_asset_turnover_efficiency_z_066'] = _z(_roc(aturn, 63), 63)
    f['f36_asset_turnover_efficiency_z_067'] = _z(aturn.diff(126), 252)
    f['f36_asset_turnover_efficiency_z_068'] = _z(aturn / _std(aturn, 252).replace(0, 1), 252)
    f['f36_asset_turnover_efficiency_z_069'] = _z(_ema(aturn, 504) - _ema(aturn, 1008), 1512)
    f['f36_asset_turnover_efficiency_z_070'] = _z(aturn, 21)
    f['f36_asset_turnover_efficiency_z_071'] = _z(_roc(aturn, 63), 63)
    f['f36_asset_turnover_efficiency_z_072'] = _z(aturn.diff(126), 252)
    f['f36_asset_turnover_efficiency_z_073'] = _z(aturn / _std(aturn, 252).replace(0, 1), 252)
    f['f36_asset_turnover_efficiency_z_074'] = _z(_ema(aturn, 504) - _ema(aturn, 1008), 1512)
    f['f36_asset_turnover_efficiency_z_075'] = _z(aturn, 21)
    return pd.DataFrame(f)