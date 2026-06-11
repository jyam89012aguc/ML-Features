
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
    ebitda = df['ebitda']
    interest = df['intexp']
    debt_repay = df['ncfdebt']
    dscr = ebitda / (interest + debt_repay).replace(0, np.nan)
    f = {}
    f['f39_debt_service_coverage_ratio_shifts_001'] = _z(_roc(dscr, 63), 63)
    f['f39_debt_service_coverage_ratio_shifts_002'] = _z(dscr.diff(126), 252)
    f['f39_debt_service_coverage_ratio_shifts_003'] = _z(dscr / _std(dscr, 252).replace(0, 1), 252)
    f['f39_debt_service_coverage_ratio_shifts_004'] = _z(_ema(dscr, 504) - _ema(dscr, 1008), 1512)
    f['f39_debt_service_coverage_ratio_shifts_005'] = _z(dscr, 21)
    f['f39_debt_service_coverage_ratio_shifts_006'] = _z(_roc(dscr, 63), 63)
    f['f39_debt_service_coverage_ratio_shifts_007'] = _z(dscr.diff(126), 252)
    f['f39_debt_service_coverage_ratio_shifts_008'] = _z(dscr / _std(dscr, 252).replace(0, 1), 252)
    f['f39_debt_service_coverage_ratio_shifts_009'] = _z(_ema(dscr, 504) - _ema(dscr, 1008), 1512)
    f['f39_debt_service_coverage_ratio_shifts_010'] = _z(dscr, 21)
    f['f39_debt_service_coverage_ratio_shifts_011'] = _z(_roc(dscr, 63), 63)
    f['f39_debt_service_coverage_ratio_shifts_012'] = _z(dscr.diff(126), 252)
    f['f39_debt_service_coverage_ratio_shifts_013'] = _z(dscr / _std(dscr, 252).replace(0, 1), 252)
    f['f39_debt_service_coverage_ratio_shifts_014'] = _z(_ema(dscr, 504) - _ema(dscr, 1008), 1512)
    f['f39_debt_service_coverage_ratio_shifts_015'] = _z(dscr, 21)
    f['f39_debt_service_coverage_ratio_shifts_016'] = _z(_roc(dscr, 63), 63)
    f['f39_debt_service_coverage_ratio_shifts_017'] = _z(dscr.diff(126), 252)
    f['f39_debt_service_coverage_ratio_shifts_018'] = _z(dscr / _std(dscr, 252).replace(0, 1), 252)
    f['f39_debt_service_coverage_ratio_shifts_019'] = _z(_ema(dscr, 504) - _ema(dscr, 1008), 1512)
    f['f39_debt_service_coverage_ratio_shifts_020'] = _z(dscr, 21)
    f['f39_debt_service_coverage_ratio_shifts_021'] = _z(_roc(dscr, 63), 63)
    f['f39_debt_service_coverage_ratio_shifts_022'] = _z(dscr.diff(126), 252)
    f['f39_debt_service_coverage_ratio_shifts_023'] = _z(dscr / _std(dscr, 252).replace(0, 1), 252)
    f['f39_debt_service_coverage_ratio_shifts_024'] = _z(_ema(dscr, 504) - _ema(dscr, 1008), 1512)
    f['f39_debt_service_coverage_ratio_shifts_025'] = _z(dscr, 21)
    f['f39_debt_service_coverage_ratio_shifts_026'] = _z(_roc(dscr, 63), 63)
    f['f39_debt_service_coverage_ratio_shifts_027'] = _z(dscr.diff(126), 252)
    f['f39_debt_service_coverage_ratio_shifts_028'] = _z(dscr / _std(dscr, 252).replace(0, 1), 252)
    f['f39_debt_service_coverage_ratio_shifts_029'] = _z(_ema(dscr, 504) - _ema(dscr, 1008), 1512)
    f['f39_debt_service_coverage_ratio_shifts_030'] = _z(dscr, 21)
    f['f39_debt_service_coverage_ratio_shifts_031'] = _z(_roc(dscr, 63), 63)
    f['f39_debt_service_coverage_ratio_shifts_032'] = _z(dscr.diff(126), 252)
    f['f39_debt_service_coverage_ratio_shifts_033'] = _z(dscr / _std(dscr, 252).replace(0, 1), 252)
    f['f39_debt_service_coverage_ratio_shifts_034'] = _z(_ema(dscr, 504) - _ema(dscr, 1008), 1512)
    f['f39_debt_service_coverage_ratio_shifts_035'] = _z(dscr, 21)
    f['f39_debt_service_coverage_ratio_shifts_036'] = _z(_roc(dscr, 63), 63)
    f['f39_debt_service_coverage_ratio_shifts_037'] = _z(dscr.diff(126), 252)
    f['f39_debt_service_coverage_ratio_shifts_038'] = _z(dscr / _std(dscr, 252).replace(0, 1), 252)
    f['f39_debt_service_coverage_ratio_shifts_039'] = _z(_ema(dscr, 504) - _ema(dscr, 1008), 1512)
    f['f39_debt_service_coverage_ratio_shifts_040'] = _z(dscr, 21)
    f['f39_debt_service_coverage_ratio_shifts_041'] = _z(_roc(dscr, 63), 63)
    f['f39_debt_service_coverage_ratio_shifts_042'] = _z(dscr.diff(126), 252)
    f['f39_debt_service_coverage_ratio_shifts_043'] = _z(dscr / _std(dscr, 252).replace(0, 1), 252)
    f['f39_debt_service_coverage_ratio_shifts_044'] = _z(_ema(dscr, 504) - _ema(dscr, 1008), 1512)
    f['f39_debt_service_coverage_ratio_shifts_045'] = _z(dscr, 21)
    f['f39_debt_service_coverage_ratio_shifts_046'] = _z(_roc(dscr, 63), 63)
    f['f39_debt_service_coverage_ratio_shifts_047'] = _z(dscr.diff(126), 252)
    f['f39_debt_service_coverage_ratio_shifts_048'] = _z(dscr / _std(dscr, 252).replace(0, 1), 252)
    f['f39_debt_service_coverage_ratio_shifts_049'] = _z(_ema(dscr, 504) - _ema(dscr, 1008), 1512)
    f['f39_debt_service_coverage_ratio_shifts_050'] = _z(dscr, 21)
    f['f39_debt_service_coverage_ratio_shifts_051'] = _z(_roc(dscr, 63), 63)
    f['f39_debt_service_coverage_ratio_shifts_052'] = _z(dscr.diff(126), 252)
    f['f39_debt_service_coverage_ratio_shifts_053'] = _z(dscr / _std(dscr, 252).replace(0, 1), 252)
    f['f39_debt_service_coverage_ratio_shifts_054'] = _z(_ema(dscr, 504) - _ema(dscr, 1008), 1512)
    f['f39_debt_service_coverage_ratio_shifts_055'] = _z(dscr, 21)
    f['f39_debt_service_coverage_ratio_shifts_056'] = _z(_roc(dscr, 63), 63)
    f['f39_debt_service_coverage_ratio_shifts_057'] = _z(dscr.diff(126), 252)
    f['f39_debt_service_coverage_ratio_shifts_058'] = _z(dscr / _std(dscr, 252).replace(0, 1), 252)
    f['f39_debt_service_coverage_ratio_shifts_059'] = _z(_ema(dscr, 504) - _ema(dscr, 1008), 1512)
    f['f39_debt_service_coverage_ratio_shifts_060'] = _z(dscr, 21)
    f['f39_debt_service_coverage_ratio_shifts_061'] = _z(_roc(dscr, 63), 63)
    f['f39_debt_service_coverage_ratio_shifts_062'] = _z(dscr.diff(126), 252)
    f['f39_debt_service_coverage_ratio_shifts_063'] = _z(dscr / _std(dscr, 252).replace(0, 1), 252)
    f['f39_debt_service_coverage_ratio_shifts_064'] = _z(_ema(dscr, 504) - _ema(dscr, 1008), 1512)
    f['f39_debt_service_coverage_ratio_shifts_065'] = _z(dscr, 21)
    f['f39_debt_service_coverage_ratio_shifts_066'] = _z(_roc(dscr, 63), 63)
    f['f39_debt_service_coverage_ratio_shifts_067'] = _z(dscr.diff(126), 252)
    f['f39_debt_service_coverage_ratio_shifts_068'] = _z(dscr / _std(dscr, 252).replace(0, 1), 252)
    f['f39_debt_service_coverage_ratio_shifts_069'] = _z(_ema(dscr, 504) - _ema(dscr, 1008), 1512)
    f['f39_debt_service_coverage_ratio_shifts_070'] = _z(dscr, 21)
    f['f39_debt_service_coverage_ratio_shifts_071'] = _z(_roc(dscr, 63), 63)
    f['f39_debt_service_coverage_ratio_shifts_072'] = _z(dscr.diff(126), 252)
    f['f39_debt_service_coverage_ratio_shifts_073'] = _z(dscr / _std(dscr, 252).replace(0, 1), 252)
    f['f39_debt_service_coverage_ratio_shifts_074'] = _z(_ema(dscr, 504) - _ema(dscr, 1008), 1512)
    f['f39_debt_service_coverage_ratio_shifts_075'] = _z(dscr, 21)
    return pd.DataFrame(f)