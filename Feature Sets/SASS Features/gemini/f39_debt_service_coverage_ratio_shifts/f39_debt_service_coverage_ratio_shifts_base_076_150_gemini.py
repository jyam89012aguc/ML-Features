
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
    f['f39_debt_service_coverage_ratio_shifts_076'] = _z(_roc(dscr, 63), 63)
    f['f39_debt_service_coverage_ratio_shifts_077'] = _z(dscr.diff(126), 252)
    f['f39_debt_service_coverage_ratio_shifts_078'] = _z(dscr / _std(dscr, 252).replace(0, 1), 252)
    f['f39_debt_service_coverage_ratio_shifts_079'] = _z(_ema(dscr, 504) - _ema(dscr, 1008), 1512)
    f['f39_debt_service_coverage_ratio_shifts_080'] = _z(dscr, 21)
    f['f39_debt_service_coverage_ratio_shifts_081'] = _z(_roc(dscr, 63), 63)
    f['f39_debt_service_coverage_ratio_shifts_082'] = _z(dscr.diff(126), 252)
    f['f39_debt_service_coverage_ratio_shifts_083'] = _z(dscr / _std(dscr, 252).replace(0, 1), 252)
    f['f39_debt_service_coverage_ratio_shifts_084'] = _z(_ema(dscr, 504) - _ema(dscr, 1008), 1512)
    f['f39_debt_service_coverage_ratio_shifts_085'] = _z(dscr, 21)
    f['f39_debt_service_coverage_ratio_shifts_086'] = _z(_roc(dscr, 63), 63)
    f['f39_debt_service_coverage_ratio_shifts_087'] = _z(dscr.diff(126), 252)
    f['f39_debt_service_coverage_ratio_shifts_088'] = _z(dscr / _std(dscr, 252).replace(0, 1), 252)
    f['f39_debt_service_coverage_ratio_shifts_089'] = _z(_ema(dscr, 504) - _ema(dscr, 1008), 1512)
    f['f39_debt_service_coverage_ratio_shifts_090'] = _z(dscr, 21)
    f['f39_debt_service_coverage_ratio_shifts_091'] = _z(_roc(dscr, 63), 63)
    f['f39_debt_service_coverage_ratio_shifts_092'] = _z(dscr.diff(126), 252)
    f['f39_debt_service_coverage_ratio_shifts_093'] = _z(dscr / _std(dscr, 252).replace(0, 1), 252)
    f['f39_debt_service_coverage_ratio_shifts_094'] = _z(_ema(dscr, 504) - _ema(dscr, 1008), 1512)
    f['f39_debt_service_coverage_ratio_shifts_095'] = _z(dscr, 21)
    f['f39_debt_service_coverage_ratio_shifts_096'] = _z(_roc(dscr, 63), 63)
    f['f39_debt_service_coverage_ratio_shifts_097'] = _z(dscr.diff(126), 252)
    f['f39_debt_service_coverage_ratio_shifts_098'] = _z(dscr / _std(dscr, 252).replace(0, 1), 252)
    f['f39_debt_service_coverage_ratio_shifts_099'] = _z(_ema(dscr, 504) - _ema(dscr, 1008), 1512)
    f['f39_debt_service_coverage_ratio_shifts_100'] = _z(dscr, 21)
    f['f39_debt_service_coverage_ratio_shifts_101'] = _z(_roc(dscr, 63), 63)
    f['f39_debt_service_coverage_ratio_shifts_102'] = _z(dscr.diff(126), 252)
    f['f39_debt_service_coverage_ratio_shifts_103'] = _z(dscr / _std(dscr, 252).replace(0, 1), 252)
    f['f39_debt_service_coverage_ratio_shifts_104'] = _z(_ema(dscr, 504) - _ema(dscr, 1008), 1512)
    f['f39_debt_service_coverage_ratio_shifts_105'] = _z(dscr, 21)
    f['f39_debt_service_coverage_ratio_shifts_106'] = _z(_roc(dscr, 63), 63)
    f['f39_debt_service_coverage_ratio_shifts_107'] = _z(dscr.diff(126), 252)
    f['f39_debt_service_coverage_ratio_shifts_108'] = _z(dscr / _std(dscr, 252).replace(0, 1), 252)
    f['f39_debt_service_coverage_ratio_shifts_109'] = _z(_ema(dscr, 504) - _ema(dscr, 1008), 1512)
    f['f39_debt_service_coverage_ratio_shifts_110'] = _z(dscr, 21)
    f['f39_debt_service_coverage_ratio_shifts_111'] = _z(_roc(dscr, 63), 63)
    f['f39_debt_service_coverage_ratio_shifts_112'] = _z(dscr.diff(126), 252)
    f['f39_debt_service_coverage_ratio_shifts_113'] = _z(dscr / _std(dscr, 252).replace(0, 1), 252)
    f['f39_debt_service_coverage_ratio_shifts_114'] = _z(_ema(dscr, 504) - _ema(dscr, 1008), 1512)
    f['f39_debt_service_coverage_ratio_shifts_115'] = _z(dscr, 21)
    f['f39_debt_service_coverage_ratio_shifts_116'] = _z(_roc(dscr, 63), 63)
    f['f39_debt_service_coverage_ratio_shifts_117'] = _z(dscr.diff(126), 252)
    f['f39_debt_service_coverage_ratio_shifts_118'] = _z(dscr / _std(dscr, 252).replace(0, 1), 252)
    f['f39_debt_service_coverage_ratio_shifts_119'] = _z(_ema(dscr, 504) - _ema(dscr, 1008), 1512)
    f['f39_debt_service_coverage_ratio_shifts_120'] = _z(dscr, 21)
    f['f39_debt_service_coverage_ratio_shifts_121'] = _z(_roc(dscr, 63), 63)
    f['f39_debt_service_coverage_ratio_shifts_122'] = _z(dscr.diff(126), 252)
    f['f39_debt_service_coverage_ratio_shifts_123'] = _z(dscr / _std(dscr, 252).replace(0, 1), 252)
    f['f39_debt_service_coverage_ratio_shifts_124'] = _z(_ema(dscr, 504) - _ema(dscr, 1008), 1512)
    f['f39_debt_service_coverage_ratio_shifts_125'] = _z(dscr, 21)
    f['f39_debt_service_coverage_ratio_shifts_126'] = _z(_roc(dscr, 63), 63)
    f['f39_debt_service_coverage_ratio_shifts_127'] = _z(dscr.diff(126), 252)
    f['f39_debt_service_coverage_ratio_shifts_128'] = _z(dscr / _std(dscr, 252).replace(0, 1), 252)
    f['f39_debt_service_coverage_ratio_shifts_129'] = _z(_ema(dscr, 504) - _ema(dscr, 1008), 1512)
    f['f39_debt_service_coverage_ratio_shifts_130'] = _z(dscr, 21)
    f['f39_debt_service_coverage_ratio_shifts_131'] = _z(_roc(dscr, 63), 63)
    f['f39_debt_service_coverage_ratio_shifts_132'] = _z(dscr.diff(126), 252)
    f['f39_debt_service_coverage_ratio_shifts_133'] = _z(dscr / _std(dscr, 252).replace(0, 1), 252)
    f['f39_debt_service_coverage_ratio_shifts_134'] = _z(_ema(dscr, 504) - _ema(dscr, 1008), 1512)
    f['f39_debt_service_coverage_ratio_shifts_135'] = _z(dscr, 21)
    f['f39_debt_service_coverage_ratio_shifts_136'] = _z(_roc(dscr, 63), 63)
    f['f39_debt_service_coverage_ratio_shifts_137'] = _z(dscr.diff(126), 252)
    f['f39_debt_service_coverage_ratio_shifts_138'] = _z(dscr / _std(dscr, 252).replace(0, 1), 252)
    f['f39_debt_service_coverage_ratio_shifts_139'] = _z(_ema(dscr, 504) - _ema(dscr, 1008), 1512)
    f['f39_debt_service_coverage_ratio_shifts_140'] = _z(dscr, 21)
    f['f39_debt_service_coverage_ratio_shifts_141'] = _z(_roc(dscr, 63), 63)
    f['f39_debt_service_coverage_ratio_shifts_142'] = _z(dscr.diff(126), 252)
    f['f39_debt_service_coverage_ratio_shifts_143'] = _z(dscr / _std(dscr, 252).replace(0, 1), 252)
    f['f39_debt_service_coverage_ratio_shifts_144'] = _z(_ema(dscr, 504) - _ema(dscr, 1008), 1512)
    f['f39_debt_service_coverage_ratio_shifts_145'] = _z(dscr, 21)
    f['f39_debt_service_coverage_ratio_shifts_146'] = _z(_roc(dscr, 63), 63)
    f['f39_debt_service_coverage_ratio_shifts_147'] = _z(dscr.diff(126), 252)
    f['f39_debt_service_coverage_ratio_shifts_148'] = _z(dscr / _std(dscr, 252).replace(0, 1), 252)
    f['f39_debt_service_coverage_ratio_shifts_149'] = _z(_ema(dscr, 504) - _ema(dscr, 1008), 1512)
    f['f39_debt_service_coverage_ratio_shifts_150'] = _z(dscr, 21)
    return pd.DataFrame(f)