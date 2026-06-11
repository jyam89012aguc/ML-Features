
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
    ca = df['assetsc']
    cl = df['liabilitiesc']
    rev = df['revenue']
    wc_eff = (ca - cl) / rev.replace(0, np.nan)
    f = {}
    f['f40_working_capital_efficiency_regimes_001'] = _z(_roc(wc_eff, 63), 63)
    f['f40_working_capital_efficiency_regimes_002'] = _z(wc_eff.diff(126), 252)
    f['f40_working_capital_efficiency_regimes_003'] = _z(wc_eff / _std(wc_eff, 252).replace(0, 1), 252)
    f['f40_working_capital_efficiency_regimes_004'] = _z(_ema(wc_eff, 504) - _ema(wc_eff, 1008), 1512)
    f['f40_working_capital_efficiency_regimes_005'] = _z(wc_eff, 21)
    f['f40_working_capital_efficiency_regimes_006'] = _z(_roc(wc_eff, 63), 63)
    f['f40_working_capital_efficiency_regimes_007'] = _z(wc_eff.diff(126), 252)
    f['f40_working_capital_efficiency_regimes_008'] = _z(wc_eff / _std(wc_eff, 252).replace(0, 1), 252)
    f['f40_working_capital_efficiency_regimes_009'] = _z(_ema(wc_eff, 504) - _ema(wc_eff, 1008), 1512)
    f['f40_working_capital_efficiency_regimes_010'] = _z(wc_eff, 21)
    f['f40_working_capital_efficiency_regimes_011'] = _z(_roc(wc_eff, 63), 63)
    f['f40_working_capital_efficiency_regimes_012'] = _z(wc_eff.diff(126), 252)
    f['f40_working_capital_efficiency_regimes_013'] = _z(wc_eff / _std(wc_eff, 252).replace(0, 1), 252)
    f['f40_working_capital_efficiency_regimes_014'] = _z(_ema(wc_eff, 504) - _ema(wc_eff, 1008), 1512)
    f['f40_working_capital_efficiency_regimes_015'] = _z(wc_eff, 21)
    f['f40_working_capital_efficiency_regimes_016'] = _z(_roc(wc_eff, 63), 63)
    f['f40_working_capital_efficiency_regimes_017'] = _z(wc_eff.diff(126), 252)
    f['f40_working_capital_efficiency_regimes_018'] = _z(wc_eff / _std(wc_eff, 252).replace(0, 1), 252)
    f['f40_working_capital_efficiency_regimes_019'] = _z(_ema(wc_eff, 504) - _ema(wc_eff, 1008), 1512)
    f['f40_working_capital_efficiency_regimes_020'] = _z(wc_eff, 21)
    f['f40_working_capital_efficiency_regimes_021'] = _z(_roc(wc_eff, 63), 63)
    f['f40_working_capital_efficiency_regimes_022'] = _z(wc_eff.diff(126), 252)
    f['f40_working_capital_efficiency_regimes_023'] = _z(wc_eff / _std(wc_eff, 252).replace(0, 1), 252)
    f['f40_working_capital_efficiency_regimes_024'] = _z(_ema(wc_eff, 504) - _ema(wc_eff, 1008), 1512)
    f['f40_working_capital_efficiency_regimes_025'] = _z(wc_eff, 21)
    f['f40_working_capital_efficiency_regimes_026'] = _z(_roc(wc_eff, 63), 63)
    f['f40_working_capital_efficiency_regimes_027'] = _z(wc_eff.diff(126), 252)
    f['f40_working_capital_efficiency_regimes_028'] = _z(wc_eff / _std(wc_eff, 252).replace(0, 1), 252)
    f['f40_working_capital_efficiency_regimes_029'] = _z(_ema(wc_eff, 504) - _ema(wc_eff, 1008), 1512)
    f['f40_working_capital_efficiency_regimes_030'] = _z(wc_eff, 21)
    f['f40_working_capital_efficiency_regimes_031'] = _z(_roc(wc_eff, 63), 63)
    f['f40_working_capital_efficiency_regimes_032'] = _z(wc_eff.diff(126), 252)
    f['f40_working_capital_efficiency_regimes_033'] = _z(wc_eff / _std(wc_eff, 252).replace(0, 1), 252)
    f['f40_working_capital_efficiency_regimes_034'] = _z(_ema(wc_eff, 504) - _ema(wc_eff, 1008), 1512)
    f['f40_working_capital_efficiency_regimes_035'] = _z(wc_eff, 21)
    f['f40_working_capital_efficiency_regimes_036'] = _z(_roc(wc_eff, 63), 63)
    f['f40_working_capital_efficiency_regimes_037'] = _z(wc_eff.diff(126), 252)
    f['f40_working_capital_efficiency_regimes_038'] = _z(wc_eff / _std(wc_eff, 252).replace(0, 1), 252)
    f['f40_working_capital_efficiency_regimes_039'] = _z(_ema(wc_eff, 504) - _ema(wc_eff, 1008), 1512)
    f['f40_working_capital_efficiency_regimes_040'] = _z(wc_eff, 21)
    f['f40_working_capital_efficiency_regimes_041'] = _z(_roc(wc_eff, 63), 63)
    f['f40_working_capital_efficiency_regimes_042'] = _z(wc_eff.diff(126), 252)
    f['f40_working_capital_efficiency_regimes_043'] = _z(wc_eff / _std(wc_eff, 252).replace(0, 1), 252)
    f['f40_working_capital_efficiency_regimes_044'] = _z(_ema(wc_eff, 504) - _ema(wc_eff, 1008), 1512)
    f['f40_working_capital_efficiency_regimes_045'] = _z(wc_eff, 21)
    f['f40_working_capital_efficiency_regimes_046'] = _z(_roc(wc_eff, 63), 63)
    f['f40_working_capital_efficiency_regimes_047'] = _z(wc_eff.diff(126), 252)
    f['f40_working_capital_efficiency_regimes_048'] = _z(wc_eff / _std(wc_eff, 252).replace(0, 1), 252)
    f['f40_working_capital_efficiency_regimes_049'] = _z(_ema(wc_eff, 504) - _ema(wc_eff, 1008), 1512)
    f['f40_working_capital_efficiency_regimes_050'] = _z(wc_eff, 21)
    f['f40_working_capital_efficiency_regimes_051'] = _z(_roc(wc_eff, 63), 63)
    f['f40_working_capital_efficiency_regimes_052'] = _z(wc_eff.diff(126), 252)
    f['f40_working_capital_efficiency_regimes_053'] = _z(wc_eff / _std(wc_eff, 252).replace(0, 1), 252)
    f['f40_working_capital_efficiency_regimes_054'] = _z(_ema(wc_eff, 504) - _ema(wc_eff, 1008), 1512)
    f['f40_working_capital_efficiency_regimes_055'] = _z(wc_eff, 21)
    f['f40_working_capital_efficiency_regimes_056'] = _z(_roc(wc_eff, 63), 63)
    f['f40_working_capital_efficiency_regimes_057'] = _z(wc_eff.diff(126), 252)
    f['f40_working_capital_efficiency_regimes_058'] = _z(wc_eff / _std(wc_eff, 252).replace(0, 1), 252)
    f['f40_working_capital_efficiency_regimes_059'] = _z(_ema(wc_eff, 504) - _ema(wc_eff, 1008), 1512)
    f['f40_working_capital_efficiency_regimes_060'] = _z(wc_eff, 21)
    f['f40_working_capital_efficiency_regimes_061'] = _z(_roc(wc_eff, 63), 63)
    f['f40_working_capital_efficiency_regimes_062'] = _z(wc_eff.diff(126), 252)
    f['f40_working_capital_efficiency_regimes_063'] = _z(wc_eff / _std(wc_eff, 252).replace(0, 1), 252)
    f['f40_working_capital_efficiency_regimes_064'] = _z(_ema(wc_eff, 504) - _ema(wc_eff, 1008), 1512)
    f['f40_working_capital_efficiency_regimes_065'] = _z(wc_eff, 21)
    f['f40_working_capital_efficiency_regimes_066'] = _z(_roc(wc_eff, 63), 63)
    f['f40_working_capital_efficiency_regimes_067'] = _z(wc_eff.diff(126), 252)
    f['f40_working_capital_efficiency_regimes_068'] = _z(wc_eff / _std(wc_eff, 252).replace(0, 1), 252)
    f['f40_working_capital_efficiency_regimes_069'] = _z(_ema(wc_eff, 504) - _ema(wc_eff, 1008), 1512)
    f['f40_working_capital_efficiency_regimes_070'] = _z(wc_eff, 21)
    f['f40_working_capital_efficiency_regimes_071'] = _z(_roc(wc_eff, 63), 63)
    f['f40_working_capital_efficiency_regimes_072'] = _z(wc_eff.diff(126), 252)
    f['f40_working_capital_efficiency_regimes_073'] = _z(wc_eff / _std(wc_eff, 252).replace(0, 1), 252)
    f['f40_working_capital_efficiency_regimes_074'] = _z(_ema(wc_eff, 504) - _ema(wc_eff, 1008), 1512)
    f['f40_working_capital_efficiency_regimes_075'] = _z(wc_eff, 21)
    return pd.DataFrame(f)