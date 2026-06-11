
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
    div = df['ncfdiv']
    buyback = df['ncfcommon']
    debt_red = df['ncfdebt']
    market_cap = df['marketcap']
    sh_yield = (div + buyback + debt_red) / market_cap.replace(0, np.nan)
    f = {}
    f['f41_shareholder_yield_intensity_001'] = _z(_roc(sh_yield, 63), 63)
    f['f41_shareholder_yield_intensity_002'] = _z(sh_yield.diff(126), 252)
    f['f41_shareholder_yield_intensity_003'] = _z(sh_yield / _std(sh_yield, 252).replace(0, 1), 252)
    f['f41_shareholder_yield_intensity_004'] = _z(_ema(sh_yield, 504) - _ema(sh_yield, 1008), 1512)
    f['f41_shareholder_yield_intensity_005'] = _z(sh_yield, 21)
    f['f41_shareholder_yield_intensity_006'] = _z(_roc(sh_yield, 63), 63)
    f['f41_shareholder_yield_intensity_007'] = _z(sh_yield.diff(126), 252)
    f['f41_shareholder_yield_intensity_008'] = _z(sh_yield / _std(sh_yield, 252).replace(0, 1), 252)
    f['f41_shareholder_yield_intensity_009'] = _z(_ema(sh_yield, 504) - _ema(sh_yield, 1008), 1512)
    f['f41_shareholder_yield_intensity_010'] = _z(sh_yield, 21)
    f['f41_shareholder_yield_intensity_011'] = _z(_roc(sh_yield, 63), 63)
    f['f41_shareholder_yield_intensity_012'] = _z(sh_yield.diff(126), 252)
    f['f41_shareholder_yield_intensity_013'] = _z(sh_yield / _std(sh_yield, 252).replace(0, 1), 252)
    f['f41_shareholder_yield_intensity_014'] = _z(_ema(sh_yield, 504) - _ema(sh_yield, 1008), 1512)
    f['f41_shareholder_yield_intensity_015'] = _z(sh_yield, 21)
    f['f41_shareholder_yield_intensity_016'] = _z(_roc(sh_yield, 63), 63)
    f['f41_shareholder_yield_intensity_017'] = _z(sh_yield.diff(126), 252)
    f['f41_shareholder_yield_intensity_018'] = _z(sh_yield / _std(sh_yield, 252).replace(0, 1), 252)
    f['f41_shareholder_yield_intensity_019'] = _z(_ema(sh_yield, 504) - _ema(sh_yield, 1008), 1512)
    f['f41_shareholder_yield_intensity_020'] = _z(sh_yield, 21)
    f['f41_shareholder_yield_intensity_021'] = _z(_roc(sh_yield, 63), 63)
    f['f41_shareholder_yield_intensity_022'] = _z(sh_yield.diff(126), 252)
    f['f41_shareholder_yield_intensity_023'] = _z(sh_yield / _std(sh_yield, 252).replace(0, 1), 252)
    f['f41_shareholder_yield_intensity_024'] = _z(_ema(sh_yield, 504) - _ema(sh_yield, 1008), 1512)
    f['f41_shareholder_yield_intensity_025'] = _z(sh_yield, 21)
    f['f41_shareholder_yield_intensity_026'] = _z(_roc(sh_yield, 63), 63)
    f['f41_shareholder_yield_intensity_027'] = _z(sh_yield.diff(126), 252)
    f['f41_shareholder_yield_intensity_028'] = _z(sh_yield / _std(sh_yield, 252).replace(0, 1), 252)
    f['f41_shareholder_yield_intensity_029'] = _z(_ema(sh_yield, 504) - _ema(sh_yield, 1008), 1512)
    f['f41_shareholder_yield_intensity_030'] = _z(sh_yield, 21)
    f['f41_shareholder_yield_intensity_031'] = _z(_roc(sh_yield, 63), 63)
    f['f41_shareholder_yield_intensity_032'] = _z(sh_yield.diff(126), 252)
    f['f41_shareholder_yield_intensity_033'] = _z(sh_yield / _std(sh_yield, 252).replace(0, 1), 252)
    f['f41_shareholder_yield_intensity_034'] = _z(_ema(sh_yield, 504) - _ema(sh_yield, 1008), 1512)
    f['f41_shareholder_yield_intensity_035'] = _z(sh_yield, 21)
    f['f41_shareholder_yield_intensity_036'] = _z(_roc(sh_yield, 63), 63)
    f['f41_shareholder_yield_intensity_037'] = _z(sh_yield.diff(126), 252)
    f['f41_shareholder_yield_intensity_038'] = _z(sh_yield / _std(sh_yield, 252).replace(0, 1), 252)
    f['f41_shareholder_yield_intensity_039'] = _z(_ema(sh_yield, 504) - _ema(sh_yield, 1008), 1512)
    f['f41_shareholder_yield_intensity_040'] = _z(sh_yield, 21)
    f['f41_shareholder_yield_intensity_041'] = _z(_roc(sh_yield, 63), 63)
    f['f41_shareholder_yield_intensity_042'] = _z(sh_yield.diff(126), 252)
    f['f41_shareholder_yield_intensity_043'] = _z(sh_yield / _std(sh_yield, 252).replace(0, 1), 252)
    f['f41_shareholder_yield_intensity_044'] = _z(_ema(sh_yield, 504) - _ema(sh_yield, 1008), 1512)
    f['f41_shareholder_yield_intensity_045'] = _z(sh_yield, 21)
    f['f41_shareholder_yield_intensity_046'] = _z(_roc(sh_yield, 63), 63)
    f['f41_shareholder_yield_intensity_047'] = _z(sh_yield.diff(126), 252)
    f['f41_shareholder_yield_intensity_048'] = _z(sh_yield / _std(sh_yield, 252).replace(0, 1), 252)
    f['f41_shareholder_yield_intensity_049'] = _z(_ema(sh_yield, 504) - _ema(sh_yield, 1008), 1512)
    f['f41_shareholder_yield_intensity_050'] = _z(sh_yield, 21)
    f['f41_shareholder_yield_intensity_051'] = _z(_roc(sh_yield, 63), 63)
    f['f41_shareholder_yield_intensity_052'] = _z(sh_yield.diff(126), 252)
    f['f41_shareholder_yield_intensity_053'] = _z(sh_yield / _std(sh_yield, 252).replace(0, 1), 252)
    f['f41_shareholder_yield_intensity_054'] = _z(_ema(sh_yield, 504) - _ema(sh_yield, 1008), 1512)
    f['f41_shareholder_yield_intensity_055'] = _z(sh_yield, 21)
    f['f41_shareholder_yield_intensity_056'] = _z(_roc(sh_yield, 63), 63)
    f['f41_shareholder_yield_intensity_057'] = _z(sh_yield.diff(126), 252)
    f['f41_shareholder_yield_intensity_058'] = _z(sh_yield / _std(sh_yield, 252).replace(0, 1), 252)
    f['f41_shareholder_yield_intensity_059'] = _z(_ema(sh_yield, 504) - _ema(sh_yield, 1008), 1512)
    f['f41_shareholder_yield_intensity_060'] = _z(sh_yield, 21)
    f['f41_shareholder_yield_intensity_061'] = _z(_roc(sh_yield, 63), 63)
    f['f41_shareholder_yield_intensity_062'] = _z(sh_yield.diff(126), 252)
    f['f41_shareholder_yield_intensity_063'] = _z(sh_yield / _std(sh_yield, 252).replace(0, 1), 252)
    f['f41_shareholder_yield_intensity_064'] = _z(_ema(sh_yield, 504) - _ema(sh_yield, 1008), 1512)
    f['f41_shareholder_yield_intensity_065'] = _z(sh_yield, 21)
    f['f41_shareholder_yield_intensity_066'] = _z(_roc(sh_yield, 63), 63)
    f['f41_shareholder_yield_intensity_067'] = _z(sh_yield.diff(126), 252)
    f['f41_shareholder_yield_intensity_068'] = _z(sh_yield / _std(sh_yield, 252).replace(0, 1), 252)
    f['f41_shareholder_yield_intensity_069'] = _z(_ema(sh_yield, 504) - _ema(sh_yield, 1008), 1512)
    f['f41_shareholder_yield_intensity_070'] = _z(sh_yield, 21)
    f['f41_shareholder_yield_intensity_071'] = _z(_roc(sh_yield, 63), 63)
    f['f41_shareholder_yield_intensity_072'] = _z(sh_yield.diff(126), 252)
    f['f41_shareholder_yield_intensity_073'] = _z(sh_yield / _std(sh_yield, 252).replace(0, 1), 252)
    f['f41_shareholder_yield_intensity_074'] = _z(_ema(sh_yield, 504) - _ema(sh_yield, 1008), 1512)
    f['f41_shareholder_yield_intensity_075'] = _z(sh_yield, 21)
    return pd.DataFrame(f)