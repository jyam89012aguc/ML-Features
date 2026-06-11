
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
    ic = df['invcap']
    croic = fcf / ic.replace(0, np.nan)
    f = {}
    f['f38_croic_capital_efficiency_001'] = _z(_roc(croic, 63), 63)
    f['f38_croic_capital_efficiency_002'] = _z(croic.diff(126), 252)
    f['f38_croic_capital_efficiency_003'] = _z(croic / _std(croic, 252).replace(0, 1), 252)
    f['f38_croic_capital_efficiency_004'] = _z(_ema(croic, 504) - _ema(croic, 1008), 1512)
    f['f38_croic_capital_efficiency_005'] = _z(croic, 21)
    f['f38_croic_capital_efficiency_006'] = _z(_roc(croic, 63), 63)
    f['f38_croic_capital_efficiency_007'] = _z(croic.diff(126), 252)
    f['f38_croic_capital_efficiency_008'] = _z(croic / _std(croic, 252).replace(0, 1), 252)
    f['f38_croic_capital_efficiency_009'] = _z(_ema(croic, 504) - _ema(croic, 1008), 1512)
    f['f38_croic_capital_efficiency_010'] = _z(croic, 21)
    f['f38_croic_capital_efficiency_011'] = _z(_roc(croic, 63), 63)
    f['f38_croic_capital_efficiency_012'] = _z(croic.diff(126), 252)
    f['f38_croic_capital_efficiency_013'] = _z(croic / _std(croic, 252).replace(0, 1), 252)
    f['f38_croic_capital_efficiency_014'] = _z(_ema(croic, 504) - _ema(croic, 1008), 1512)
    f['f38_croic_capital_efficiency_015'] = _z(croic, 21)
    f['f38_croic_capital_efficiency_016'] = _z(_roc(croic, 63), 63)
    f['f38_croic_capital_efficiency_017'] = _z(croic.diff(126), 252)
    f['f38_croic_capital_efficiency_018'] = _z(croic / _std(croic, 252).replace(0, 1), 252)
    f['f38_croic_capital_efficiency_019'] = _z(_ema(croic, 504) - _ema(croic, 1008), 1512)
    f['f38_croic_capital_efficiency_020'] = _z(croic, 21)
    f['f38_croic_capital_efficiency_021'] = _z(_roc(croic, 63), 63)
    f['f38_croic_capital_efficiency_022'] = _z(croic.diff(126), 252)
    f['f38_croic_capital_efficiency_023'] = _z(croic / _std(croic, 252).replace(0, 1), 252)
    f['f38_croic_capital_efficiency_024'] = _z(_ema(croic, 504) - _ema(croic, 1008), 1512)
    f['f38_croic_capital_efficiency_025'] = _z(croic, 21)
    f['f38_croic_capital_efficiency_026'] = _z(_roc(croic, 63), 63)
    f['f38_croic_capital_efficiency_027'] = _z(croic.diff(126), 252)
    f['f38_croic_capital_efficiency_028'] = _z(croic / _std(croic, 252).replace(0, 1), 252)
    f['f38_croic_capital_efficiency_029'] = _z(_ema(croic, 504) - _ema(croic, 1008), 1512)
    f['f38_croic_capital_efficiency_030'] = _z(croic, 21)
    f['f38_croic_capital_efficiency_031'] = _z(_roc(croic, 63), 63)
    f['f38_croic_capital_efficiency_032'] = _z(croic.diff(126), 252)
    f['f38_croic_capital_efficiency_033'] = _z(croic / _std(croic, 252).replace(0, 1), 252)
    f['f38_croic_capital_efficiency_034'] = _z(_ema(croic, 504) - _ema(croic, 1008), 1512)
    f['f38_croic_capital_efficiency_035'] = _z(croic, 21)
    f['f38_croic_capital_efficiency_036'] = _z(_roc(croic, 63), 63)
    f['f38_croic_capital_efficiency_037'] = _z(croic.diff(126), 252)
    f['f38_croic_capital_efficiency_038'] = _z(croic / _std(croic, 252).replace(0, 1), 252)
    f['f38_croic_capital_efficiency_039'] = _z(_ema(croic, 504) - _ema(croic, 1008), 1512)
    f['f38_croic_capital_efficiency_040'] = _z(croic, 21)
    f['f38_croic_capital_efficiency_041'] = _z(_roc(croic, 63), 63)
    f['f38_croic_capital_efficiency_042'] = _z(croic.diff(126), 252)
    f['f38_croic_capital_efficiency_043'] = _z(croic / _std(croic, 252).replace(0, 1), 252)
    f['f38_croic_capital_efficiency_044'] = _z(_ema(croic, 504) - _ema(croic, 1008), 1512)
    f['f38_croic_capital_efficiency_045'] = _z(croic, 21)
    f['f38_croic_capital_efficiency_046'] = _z(_roc(croic, 63), 63)
    f['f38_croic_capital_efficiency_047'] = _z(croic.diff(126), 252)
    f['f38_croic_capital_efficiency_048'] = _z(croic / _std(croic, 252).replace(0, 1), 252)
    f['f38_croic_capital_efficiency_049'] = _z(_ema(croic, 504) - _ema(croic, 1008), 1512)
    f['f38_croic_capital_efficiency_050'] = _z(croic, 21)
    f['f38_croic_capital_efficiency_051'] = _z(_roc(croic, 63), 63)
    f['f38_croic_capital_efficiency_052'] = _z(croic.diff(126), 252)
    f['f38_croic_capital_efficiency_053'] = _z(croic / _std(croic, 252).replace(0, 1), 252)
    f['f38_croic_capital_efficiency_054'] = _z(_ema(croic, 504) - _ema(croic, 1008), 1512)
    f['f38_croic_capital_efficiency_055'] = _z(croic, 21)
    f['f38_croic_capital_efficiency_056'] = _z(_roc(croic, 63), 63)
    f['f38_croic_capital_efficiency_057'] = _z(croic.diff(126), 252)
    f['f38_croic_capital_efficiency_058'] = _z(croic / _std(croic, 252).replace(0, 1), 252)
    f['f38_croic_capital_efficiency_059'] = _z(_ema(croic, 504) - _ema(croic, 1008), 1512)
    f['f38_croic_capital_efficiency_060'] = _z(croic, 21)
    f['f38_croic_capital_efficiency_061'] = _z(_roc(croic, 63), 63)
    f['f38_croic_capital_efficiency_062'] = _z(croic.diff(126), 252)
    f['f38_croic_capital_efficiency_063'] = _z(croic / _std(croic, 252).replace(0, 1), 252)
    f['f38_croic_capital_efficiency_064'] = _z(_ema(croic, 504) - _ema(croic, 1008), 1512)
    f['f38_croic_capital_efficiency_065'] = _z(croic, 21)
    f['f38_croic_capital_efficiency_066'] = _z(_roc(croic, 63), 63)
    f['f38_croic_capital_efficiency_067'] = _z(croic.diff(126), 252)
    f['f38_croic_capital_efficiency_068'] = _z(croic / _std(croic, 252).replace(0, 1), 252)
    f['f38_croic_capital_efficiency_069'] = _z(_ema(croic, 504) - _ema(croic, 1008), 1512)
    f['f38_croic_capital_efficiency_070'] = _z(croic, 21)
    f['f38_croic_capital_efficiency_071'] = _z(_roc(croic, 63), 63)
    f['f38_croic_capital_efficiency_072'] = _z(croic.diff(126), 252)
    f['f38_croic_capital_efficiency_073'] = _z(croic / _std(croic, 252).replace(0, 1), 252)
    f['f38_croic_capital_efficiency_074'] = _z(_ema(croic, 504) - _ema(croic, 1008), 1512)
    f['f38_croic_capital_efficiency_075'] = _z(croic, 21)
    return pd.DataFrame(f)