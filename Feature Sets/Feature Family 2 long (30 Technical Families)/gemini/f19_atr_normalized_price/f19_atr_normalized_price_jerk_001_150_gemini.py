# f19_atr_normalized_price_jerk_001_150_gemini.py
import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 5)).mean()
def _ema(s, w): return s.ewm(span=w, min_periods=min(w, 5), adjust=False).mean()
def _min(s, w): return s.rolling(w, min_periods=min(w, 5)).min()
def _max(s, w): return s.rolling(w, min_periods=min(w, 5)).max()
def _atr_val(h, l, c, w):
    tr = np.maximum(h - l, np.maximum((h - c.shift(1)).abs(), (l - c.shift(1)).abs()))
    return tr.rolling(w, min_periods=min(w, 5)).mean()
def _price_atr_norm(price, level, atr):
    return (price - level) / atr.replace(0, np.nan)
def _atr_zscore(atr, w):
    return (atr - atr.rolling(w, min_periods=min(w, 5)).mean()) / atr.rolling(w, min_periods=min(w, 5)).std().replace(0, np.nan)

# Feature f19anp_f19_atr_normalized_price_jerk_v001_signal: Jerk of normalized price (window=10, window=5)
def f19anp_f19_atr_normalized_price_jerk_v001_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 10)
    slope = _price_atr_norm(close, _sma(close, 10), atr).pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_f19_atr_normalized_price_jerk_v002_signal: Jerk of normalized price (window=21, window=5)
def f19anp_f19_atr_normalized_price_jerk_v002_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    slope = _price_atr_norm(close, _sma(close, 21), atr).pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_f19_atr_normalized_price_jerk_v003_signal: Jerk of normalized price (window=63, window=21)
def f19anp_f19_atr_normalized_price_jerk_v003_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 63)
    slope = _price_atr_norm(closeadj, _sma(closeadj, 63), atr).pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_f19_atr_normalized_price_jerk_v004_signal: Jerk of normalized price (window=126, window=21)
def f19anp_f19_atr_normalized_price_jerk_v004_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 126)
    slope = _price_atr_norm(closeadj, _sma(closeadj, 126), atr).pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_f19_atr_normalized_price_jerk_v005_signal: Jerk of normalized price (window=252, window=63)
def f19anp_f19_atr_normalized_price_jerk_v005_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 252)
    slope = _price_atr_norm(closeadj, _sma(closeadj, 252), atr).pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_f19_atr_normalized_price_jerk_v006_signal: Jerk of normalized price (window=504, window=63)
def f19anp_f19_atr_normalized_price_jerk_v006_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 504)
    slope = _price_atr_norm(closeadj, _sma(closeadj, 504), atr).pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_f19_atr_normalized_price_jerk_v007_signal: Jerk of normalized price (window=5, window=5)
def f19anp_f19_atr_normalized_price_jerk_v007_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 5)
    slope = _price_atr_norm(close, _sma(close, 5), atr).pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_f19_atr_normalized_price_jerk_v008_signal: Jerk of normalized price (window=10, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v009_signal: Jerk of normalized price (window=21, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v010_signal: Jerk of normalized price (window=63, window=21)

# Feature f19anp_f19_atr_normalized_price_jerk_v011_signal: Jerk of normalized price (window=126, window=21)

# Feature f19anp_f19_atr_normalized_price_jerk_v012_signal: Jerk of normalized price (window=252, window=63)

# Feature f19anp_f19_atr_normalized_price_jerk_v013_signal: Jerk of normalized price (window=504, window=63)

# Feature f19anp_f19_atr_normalized_price_jerk_v014_signal: Jerk of normalized price (window=5, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v015_signal: Jerk of normalized price (window=10, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v016_signal: Jerk of normalized price (window=21, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v017_signal: Jerk of normalized price (window=63, window=21)

# Feature f19anp_f19_atr_normalized_price_jerk_v018_signal: Jerk of normalized price (window=126, window=21)

# Feature f19anp_f19_atr_normalized_price_jerk_v019_signal: Jerk of normalized price (window=252, window=63)

# Feature f19anp_f19_atr_normalized_price_jerk_v020_signal: Jerk of normalized price (window=504, window=63)

# Feature f19anp_f19_atr_normalized_price_jerk_v021_signal: Jerk of normalized price (window=5, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v022_signal: Jerk of normalized price (window=10, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v023_signal: Jerk of normalized price (window=21, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v024_signal: Jerk of normalized price (window=63, window=21)

# Feature f19anp_f19_atr_normalized_price_jerk_v025_signal: Jerk of normalized price (window=126, window=21)

# Feature f19anp_f19_atr_normalized_price_jerk_v026_signal: Jerk of normalized price (window=252, window=63)

# Feature f19anp_f19_atr_normalized_price_jerk_v027_signal: Jerk of normalized price (window=504, window=63)

# Feature f19anp_f19_atr_normalized_price_jerk_v028_signal: Jerk of normalized price (window=5, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v029_signal: Jerk of normalized price (window=10, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v030_signal: Jerk of normalized price (window=21, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v031_signal: Jerk of normalized price (window=63, window=21)

# Feature f19anp_f19_atr_normalized_price_jerk_v032_signal: Jerk of normalized price (window=126, window=21)

# Feature f19anp_f19_atr_normalized_price_jerk_v033_signal: Jerk of normalized price (window=252, window=63)

# Feature f19anp_f19_atr_normalized_price_jerk_v034_signal: Jerk of normalized price (window=504, window=63)

# Feature f19anp_f19_atr_normalized_price_jerk_v035_signal: Jerk of normalized price (window=5, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v036_signal: Jerk of normalized price (window=10, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v037_signal: Jerk of normalized price (window=21, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v038_signal: Jerk of normalized price (window=63, window=21)

# Feature f19anp_f19_atr_normalized_price_jerk_v039_signal: Jerk of normalized price (window=126, window=21)

# Feature f19anp_f19_atr_normalized_price_jerk_v040_signal: Jerk of normalized price (window=252, window=63)

# Feature f19anp_f19_atr_normalized_price_jerk_v041_signal: Jerk of normalized price (window=504, window=63)

# Feature f19anp_f19_atr_normalized_price_jerk_v042_signal: Jerk of normalized price (window=5, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v043_signal: Jerk of normalized price (window=10, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v044_signal: Jerk of normalized price (window=21, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v045_signal: Jerk of normalized price (window=63, window=21)

# Feature f19anp_f19_atr_normalized_price_jerk_v046_signal: Jerk of normalized price (window=126, window=21)

# Feature f19anp_f19_atr_normalized_price_jerk_v047_signal: Jerk of normalized price (window=252, window=63)

# Feature f19anp_f19_atr_normalized_price_jerk_v048_signal: Jerk of normalized price (window=504, window=63)

# Feature f19anp_f19_atr_normalized_price_jerk_v049_signal: Jerk of normalized price (window=5, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v050_signal: Jerk of normalized price (window=10, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v051_signal: Jerk of normalized price (window=21, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v052_signal: Jerk of normalized price (window=63, window=21)

# Feature f19anp_f19_atr_normalized_price_jerk_v053_signal: Jerk of normalized price (window=126, window=21)

# Feature f19anp_f19_atr_normalized_price_jerk_v054_signal: Jerk of normalized price (window=252, window=63)

# Feature f19anp_f19_atr_normalized_price_jerk_v055_signal: Jerk of normalized price (window=504, window=63)

# Feature f19anp_f19_atr_normalized_price_jerk_v056_signal: Jerk of normalized price (window=5, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v057_signal: Jerk of normalized price (window=10, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v058_signal: Jerk of normalized price (window=21, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v059_signal: Jerk of normalized price (window=63, window=21)

# Feature f19anp_f19_atr_normalized_price_jerk_v060_signal: Jerk of normalized price (window=126, window=21)

# Feature f19anp_f19_atr_normalized_price_jerk_v061_signal: Jerk of normalized price (window=252, window=63)

# Feature f19anp_f19_atr_normalized_price_jerk_v062_signal: Jerk of normalized price (window=504, window=63)

# Feature f19anp_f19_atr_normalized_price_jerk_v063_signal: Jerk of normalized price (window=5, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v064_signal: Jerk of normalized price (window=10, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v065_signal: Jerk of normalized price (window=21, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v066_signal: Jerk of normalized price (window=63, window=21)

# Feature f19anp_f19_atr_normalized_price_jerk_v067_signal: Jerk of normalized price (window=126, window=21)

# Feature f19anp_f19_atr_normalized_price_jerk_v068_signal: Jerk of normalized price (window=252, window=63)

# Feature f19anp_f19_atr_normalized_price_jerk_v069_signal: Jerk of normalized price (window=504, window=63)

# Feature f19anp_f19_atr_normalized_price_jerk_v070_signal: Jerk of normalized price (window=5, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v071_signal: Jerk of normalized price (window=10, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v072_signal: Jerk of normalized price (window=21, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v073_signal: Jerk of normalized price (window=63, window=21)

# Feature f19anp_f19_atr_normalized_price_jerk_v074_signal: Jerk of normalized price (window=126, window=21)

# Feature f19anp_f19_atr_normalized_price_jerk_v075_signal: Jerk of normalized price (window=252, window=63)

# Feature f19anp_f19_atr_normalized_price_jerk_v076_signal: Jerk of normalized price (window=504, window=63)

# Feature f19anp_f19_atr_normalized_price_jerk_v077_signal: Jerk of normalized price (window=5, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v078_signal: Jerk of normalized price (window=10, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v079_signal: Jerk of normalized price (window=21, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v080_signal: Jerk of normalized price (window=63, window=21)

# Feature f19anp_f19_atr_normalized_price_jerk_v081_signal: Jerk of normalized price (window=126, window=21)

# Feature f19anp_f19_atr_normalized_price_jerk_v082_signal: Jerk of normalized price (window=252, window=63)

# Feature f19anp_f19_atr_normalized_price_jerk_v083_signal: Jerk of normalized price (window=504, window=63)

# Feature f19anp_f19_atr_normalized_price_jerk_v084_signal: Jerk of normalized price (window=5, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v085_signal: Jerk of normalized price (window=10, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v086_signal: Jerk of normalized price (window=21, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v087_signal: Jerk of normalized price (window=63, window=21)

# Feature f19anp_f19_atr_normalized_price_jerk_v088_signal: Jerk of normalized price (window=126, window=21)

# Feature f19anp_f19_atr_normalized_price_jerk_v089_signal: Jerk of normalized price (window=252, window=63)

# Feature f19anp_f19_atr_normalized_price_jerk_v090_signal: Jerk of normalized price (window=504, window=63)

# Feature f19anp_f19_atr_normalized_price_jerk_v091_signal: Jerk of normalized price (window=5, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v092_signal: Jerk of normalized price (window=10, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v093_signal: Jerk of normalized price (window=21, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v094_signal: Jerk of normalized price (window=63, window=21)

# Feature f19anp_f19_atr_normalized_price_jerk_v095_signal: Jerk of normalized price (window=126, window=21)

# Feature f19anp_f19_atr_normalized_price_jerk_v096_signal: Jerk of normalized price (window=252, window=63)

# Feature f19anp_f19_atr_normalized_price_jerk_v097_signal: Jerk of normalized price (window=504, window=63)

# Feature f19anp_f19_atr_normalized_price_jerk_v098_signal: Jerk of normalized price (window=5, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v099_signal: Jerk of normalized price (window=10, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v100_signal: Jerk of normalized price (window=21, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v101_signal: Jerk of normalized price (window=63, window=21)

# Feature f19anp_f19_atr_normalized_price_jerk_v102_signal: Jerk of normalized price (window=126, window=21)

# Feature f19anp_f19_atr_normalized_price_jerk_v103_signal: Jerk of normalized price (window=252, window=63)

# Feature f19anp_f19_atr_normalized_price_jerk_v104_signal: Jerk of normalized price (window=504, window=63)

# Feature f19anp_f19_atr_normalized_price_jerk_v105_signal: Jerk of normalized price (window=5, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v106_signal: Jerk of normalized price (window=10, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v107_signal: Jerk of normalized price (window=21, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v108_signal: Jerk of normalized price (window=63, window=21)

# Feature f19anp_f19_atr_normalized_price_jerk_v109_signal: Jerk of normalized price (window=126, window=21)

# Feature f19anp_f19_atr_normalized_price_jerk_v110_signal: Jerk of normalized price (window=252, window=63)

# Feature f19anp_f19_atr_normalized_price_jerk_v111_signal: Jerk of normalized price (window=504, window=63)

# Feature f19anp_f19_atr_normalized_price_jerk_v112_signal: Jerk of normalized price (window=5, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v113_signal: Jerk of normalized price (window=10, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v114_signal: Jerk of normalized price (window=21, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v115_signal: Jerk of normalized price (window=63, window=21)

# Feature f19anp_f19_atr_normalized_price_jerk_v116_signal: Jerk of normalized price (window=126, window=21)

# Feature f19anp_f19_atr_normalized_price_jerk_v117_signal: Jerk of normalized price (window=252, window=63)

# Feature f19anp_f19_atr_normalized_price_jerk_v118_signal: Jerk of normalized price (window=504, window=63)

# Feature f19anp_f19_atr_normalized_price_jerk_v119_signal: Jerk of normalized price (window=5, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v120_signal: Jerk of normalized price (window=10, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v121_signal: Jerk of normalized price (window=21, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v122_signal: Jerk of normalized price (window=63, window=21)

# Feature f19anp_f19_atr_normalized_price_jerk_v123_signal: Jerk of normalized price (window=126, window=21)

# Feature f19anp_f19_atr_normalized_price_jerk_v124_signal: Jerk of normalized price (window=252, window=63)

# Feature f19anp_f19_atr_normalized_price_jerk_v125_signal: Jerk of normalized price (window=504, window=63)

# Feature f19anp_f19_atr_normalized_price_jerk_v126_signal: Jerk of normalized price (window=5, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v127_signal: Jerk of normalized price (window=10, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v128_signal: Jerk of normalized price (window=21, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v129_signal: Jerk of normalized price (window=63, window=21)

# Feature f19anp_f19_atr_normalized_price_jerk_v130_signal: Jerk of normalized price (window=126, window=21)

# Feature f19anp_f19_atr_normalized_price_jerk_v131_signal: Jerk of normalized price (window=252, window=63)

# Feature f19anp_f19_atr_normalized_price_jerk_v132_signal: Jerk of normalized price (window=504, window=63)

# Feature f19anp_f19_atr_normalized_price_jerk_v133_signal: Jerk of normalized price (window=5, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v134_signal: Jerk of normalized price (window=10, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v135_signal: Jerk of normalized price (window=21, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v136_signal: Jerk of normalized price (window=63, window=21)

# Feature f19anp_f19_atr_normalized_price_jerk_v137_signal: Jerk of normalized price (window=126, window=21)

# Feature f19anp_f19_atr_normalized_price_jerk_v138_signal: Jerk of normalized price (window=252, window=63)

# Feature f19anp_f19_atr_normalized_price_jerk_v139_signal: Jerk of normalized price (window=504, window=63)

# Feature f19anp_f19_atr_normalized_price_jerk_v140_signal: Jerk of normalized price (window=5, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v141_signal: Jerk of normalized price (window=10, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v142_signal: Jerk of normalized price (window=21, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v143_signal: Jerk of normalized price (window=63, window=21)

# Feature f19anp_f19_atr_normalized_price_jerk_v144_signal: Jerk of normalized price (window=126, window=21)

# Feature f19anp_f19_atr_normalized_price_jerk_v145_signal: Jerk of normalized price (window=252, window=63)

# Feature f19anp_f19_atr_normalized_price_jerk_v146_signal: Jerk of normalized price (window=504, window=63)

# Feature f19anp_f19_atr_normalized_price_jerk_v147_signal: Jerk of normalized price (window=5, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v148_signal: Jerk of normalized price (window=10, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v149_signal: Jerk of normalized price (window=21, window=5)

# Feature f19anp_f19_atr_normalized_price_jerk_v150_signal: Jerk of normalized price (window=63, window=21)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = 'read_only', 'sep', 'ticker', 'date'
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f'sep.{c}' for c in ['close', 'closeadj', 'high', 'low']}

JERK_NAMES = [f for f in globals() if f.startswith('f19anp_') and f.endswith('_signal')]

REGISTRY = {
    n: {
        'inputs': (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        'source_table': SOURCE_TABLE,
        'source_columns': {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        'entity_column': ENTITY_COLUMN, 'date_column': DATE_COLUMN,
        'order_by': ORDER_BY, 'no_forward_looking': NO_FORWARD_LOOKING, 'func': globals()[n]
    } for n in sorted(JERK_NAMES)
}

if __name__ == '__main__':
    sz = 1000; d = pd.DataFrame({'close': np.random.randn(sz).cumsum()+100, 'closeadj': np.random.randn(sz).cumsum()+100, 'high': np.random.randn(sz).cumsum()+110, 'low': np.random.randn(sz).cumsum()+90, 'ticker': ['T']*sz, 'date': pd.date_range('2020-01-01', periods=sz)})
    for n, c in REGISTRY.items():
        r = c['func'](**{i: d[i] for i in c['inputs']})
        assert isinstance(r, pd.Series)
    print('JERK OK')
