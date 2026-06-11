# f19_atr_normalized_price_slope_001_150_gemini.py
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

# Feature f19anp_f19_atr_normalized_price_slope_v001_signal: Slope of normalized price (window=10, slope_window=5)
def f19anp_f19_atr_normalized_price_slope_v001_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 10)
    res = _price_atr_norm(close, _sma(close, 10), atr).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_f19_atr_normalized_price_slope_v002_signal: Slope of normalized price (window=21, slope_window=5)
def f19anp_f19_atr_normalized_price_slope_v002_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    res = _price_atr_norm(close, _sma(close, 21), atr).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_f19_atr_normalized_price_slope_v003_signal: Slope of normalized price (window=63, slope_window=21)
def f19anp_f19_atr_normalized_price_slope_v003_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 63)
    res = _price_atr_norm(closeadj, _sma(closeadj, 63), atr).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_f19_atr_normalized_price_slope_v004_signal: Slope of normalized price (window=126, slope_window=21)
def f19anp_f19_atr_normalized_price_slope_v004_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 126)
    res = _price_atr_norm(closeadj, _sma(closeadj, 126), atr).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_f19_atr_normalized_price_slope_v005_signal: Slope of normalized price (window=252, slope_window=63)
def f19anp_f19_atr_normalized_price_slope_v005_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 252)
    res = _price_atr_norm(closeadj, _sma(closeadj, 252), atr).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_f19_atr_normalized_price_slope_v006_signal: Slope of normalized price (window=504, slope_window=63)
def f19anp_f19_atr_normalized_price_slope_v006_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 504)
    res = _price_atr_norm(closeadj, _sma(closeadj, 504), atr).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_f19_atr_normalized_price_slope_v007_signal: Slope of normalized price (window=5, slope_window=5)
def f19anp_f19_atr_normalized_price_slope_v007_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 5)
    res = _price_atr_norm(close, _sma(close, 5), atr).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_f19_atr_normalized_price_slope_v008_signal: Slope of normalized price (window=10, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v009_signal: Slope of normalized price (window=21, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v010_signal: Slope of normalized price (window=63, slope_window=21)

# Feature f19anp_f19_atr_normalized_price_slope_v011_signal: Slope of normalized price (window=126, slope_window=21)

# Feature f19anp_f19_atr_normalized_price_slope_v012_signal: Slope of normalized price (window=252, slope_window=63)

# Feature f19anp_f19_atr_normalized_price_slope_v013_signal: Slope of normalized price (window=504, slope_window=63)

# Feature f19anp_f19_atr_normalized_price_slope_v014_signal: Slope of normalized price (window=5, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v015_signal: Slope of normalized price (window=10, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v016_signal: Slope of normalized price (window=21, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v017_signal: Slope of normalized price (window=63, slope_window=21)

# Feature f19anp_f19_atr_normalized_price_slope_v018_signal: Slope of normalized price (window=126, slope_window=21)

# Feature f19anp_f19_atr_normalized_price_slope_v019_signal: Slope of normalized price (window=252, slope_window=63)

# Feature f19anp_f19_atr_normalized_price_slope_v020_signal: Slope of normalized price (window=504, slope_window=63)

# Feature f19anp_f19_atr_normalized_price_slope_v021_signal: Slope of normalized price (window=5, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v022_signal: Slope of normalized price (window=10, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v023_signal: Slope of normalized price (window=21, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v024_signal: Slope of normalized price (window=63, slope_window=21)

# Feature f19anp_f19_atr_normalized_price_slope_v025_signal: Slope of normalized price (window=126, slope_window=21)

# Feature f19anp_f19_atr_normalized_price_slope_v026_signal: Slope of normalized price (window=252, slope_window=63)

# Feature f19anp_f19_atr_normalized_price_slope_v027_signal: Slope of normalized price (window=504, slope_window=63)

# Feature f19anp_f19_atr_normalized_price_slope_v028_signal: Slope of normalized price (window=5, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v029_signal: Slope of normalized price (window=10, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v030_signal: Slope of normalized price (window=21, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v031_signal: Slope of normalized price (window=63, slope_window=21)

# Feature f19anp_f19_atr_normalized_price_slope_v032_signal: Slope of normalized price (window=126, slope_window=21)

# Feature f19anp_f19_atr_normalized_price_slope_v033_signal: Slope of normalized price (window=252, slope_window=63)

# Feature f19anp_f19_atr_normalized_price_slope_v034_signal: Slope of normalized price (window=504, slope_window=63)

# Feature f19anp_f19_atr_normalized_price_slope_v035_signal: Slope of normalized price (window=5, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v036_signal: Slope of normalized price (window=10, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v037_signal: Slope of normalized price (window=21, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v038_signal: Slope of normalized price (window=63, slope_window=21)

# Feature f19anp_f19_atr_normalized_price_slope_v039_signal: Slope of normalized price (window=126, slope_window=21)

# Feature f19anp_f19_atr_normalized_price_slope_v040_signal: Slope of normalized price (window=252, slope_window=63)

# Feature f19anp_f19_atr_normalized_price_slope_v041_signal: Slope of normalized price (window=504, slope_window=63)

# Feature f19anp_f19_atr_normalized_price_slope_v042_signal: Slope of normalized price (window=5, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v043_signal: Slope of normalized price (window=10, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v044_signal: Slope of normalized price (window=21, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v045_signal: Slope of normalized price (window=63, slope_window=21)

# Feature f19anp_f19_atr_normalized_price_slope_v046_signal: Slope of normalized price (window=126, slope_window=21)

# Feature f19anp_f19_atr_normalized_price_slope_v047_signal: Slope of normalized price (window=252, slope_window=63)

# Feature f19anp_f19_atr_normalized_price_slope_v048_signal: Slope of normalized price (window=504, slope_window=63)

# Feature f19anp_f19_atr_normalized_price_slope_v049_signal: Slope of normalized price (window=5, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v050_signal: Slope of normalized price (window=10, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v051_signal: Slope of normalized price (window=21, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v052_signal: Slope of normalized price (window=63, slope_window=21)

# Feature f19anp_f19_atr_normalized_price_slope_v053_signal: Slope of normalized price (window=126, slope_window=21)

# Feature f19anp_f19_atr_normalized_price_slope_v054_signal: Slope of normalized price (window=252, slope_window=63)

# Feature f19anp_f19_atr_normalized_price_slope_v055_signal: Slope of normalized price (window=504, slope_window=63)

# Feature f19anp_f19_atr_normalized_price_slope_v056_signal: Slope of normalized price (window=5, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v057_signal: Slope of normalized price (window=10, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v058_signal: Slope of normalized price (window=21, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v059_signal: Slope of normalized price (window=63, slope_window=21)

# Feature f19anp_f19_atr_normalized_price_slope_v060_signal: Slope of normalized price (window=126, slope_window=21)

# Feature f19anp_f19_atr_normalized_price_slope_v061_signal: Slope of normalized price (window=252, slope_window=63)

# Feature f19anp_f19_atr_normalized_price_slope_v062_signal: Slope of normalized price (window=504, slope_window=63)

# Feature f19anp_f19_atr_normalized_price_slope_v063_signal: Slope of normalized price (window=5, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v064_signal: Slope of normalized price (window=10, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v065_signal: Slope of normalized price (window=21, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v066_signal: Slope of normalized price (window=63, slope_window=21)

# Feature f19anp_f19_atr_normalized_price_slope_v067_signal: Slope of normalized price (window=126, slope_window=21)

# Feature f19anp_f19_atr_normalized_price_slope_v068_signal: Slope of normalized price (window=252, slope_window=63)

# Feature f19anp_f19_atr_normalized_price_slope_v069_signal: Slope of normalized price (window=504, slope_window=63)

# Feature f19anp_f19_atr_normalized_price_slope_v070_signal: Slope of normalized price (window=5, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v071_signal: Slope of normalized price (window=10, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v072_signal: Slope of normalized price (window=21, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v073_signal: Slope of normalized price (window=63, slope_window=21)

# Feature f19anp_f19_atr_normalized_price_slope_v074_signal: Slope of normalized price (window=126, slope_window=21)

# Feature f19anp_f19_atr_normalized_price_slope_v075_signal: Slope of normalized price (window=252, slope_window=63)

# Feature f19anp_f19_atr_normalized_price_slope_v076_signal: Slope of normalized price (window=504, slope_window=63)

# Feature f19anp_f19_atr_normalized_price_slope_v077_signal: Slope of normalized price (window=5, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v078_signal: Slope of normalized price (window=10, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v079_signal: Slope of normalized price (window=21, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v080_signal: Slope of normalized price (window=63, slope_window=21)

# Feature f19anp_f19_atr_normalized_price_slope_v081_signal: Slope of normalized price (window=126, slope_window=21)

# Feature f19anp_f19_atr_normalized_price_slope_v082_signal: Slope of normalized price (window=252, slope_window=63)

# Feature f19anp_f19_atr_normalized_price_slope_v083_signal: Slope of normalized price (window=504, slope_window=63)

# Feature f19anp_f19_atr_normalized_price_slope_v084_signal: Slope of normalized price (window=5, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v085_signal: Slope of normalized price (window=10, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v086_signal: Slope of normalized price (window=21, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v087_signal: Slope of normalized price (window=63, slope_window=21)

# Feature f19anp_f19_atr_normalized_price_slope_v088_signal: Slope of normalized price (window=126, slope_window=21)

# Feature f19anp_f19_atr_normalized_price_slope_v089_signal: Slope of normalized price (window=252, slope_window=63)

# Feature f19anp_f19_atr_normalized_price_slope_v090_signal: Slope of normalized price (window=504, slope_window=63)

# Feature f19anp_f19_atr_normalized_price_slope_v091_signal: Slope of normalized price (window=5, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v092_signal: Slope of normalized price (window=10, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v093_signal: Slope of normalized price (window=21, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v094_signal: Slope of normalized price (window=63, slope_window=21)

# Feature f19anp_f19_atr_normalized_price_slope_v095_signal: Slope of normalized price (window=126, slope_window=21)

# Feature f19anp_f19_atr_normalized_price_slope_v096_signal: Slope of normalized price (window=252, slope_window=63)

# Feature f19anp_f19_atr_normalized_price_slope_v097_signal: Slope of normalized price (window=504, slope_window=63)

# Feature f19anp_f19_atr_normalized_price_slope_v098_signal: Slope of normalized price (window=5, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v099_signal: Slope of normalized price (window=10, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v100_signal: Slope of normalized price (window=21, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v101_signal: Slope of normalized price (window=63, slope_window=21)

# Feature f19anp_f19_atr_normalized_price_slope_v102_signal: Slope of normalized price (window=126, slope_window=21)

# Feature f19anp_f19_atr_normalized_price_slope_v103_signal: Slope of normalized price (window=252, slope_window=63)

# Feature f19anp_f19_atr_normalized_price_slope_v104_signal: Slope of normalized price (window=504, slope_window=63)

# Feature f19anp_f19_atr_normalized_price_slope_v105_signal: Slope of normalized price (window=5, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v106_signal: Slope of normalized price (window=10, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v107_signal: Slope of normalized price (window=21, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v108_signal: Slope of normalized price (window=63, slope_window=21)

# Feature f19anp_f19_atr_normalized_price_slope_v109_signal: Slope of normalized price (window=126, slope_window=21)

# Feature f19anp_f19_atr_normalized_price_slope_v110_signal: Slope of normalized price (window=252, slope_window=63)

# Feature f19anp_f19_atr_normalized_price_slope_v111_signal: Slope of normalized price (window=504, slope_window=63)

# Feature f19anp_f19_atr_normalized_price_slope_v112_signal: Slope of normalized price (window=5, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v113_signal: Slope of normalized price (window=10, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v114_signal: Slope of normalized price (window=21, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v115_signal: Slope of normalized price (window=63, slope_window=21)

# Feature f19anp_f19_atr_normalized_price_slope_v116_signal: Slope of normalized price (window=126, slope_window=21)

# Feature f19anp_f19_atr_normalized_price_slope_v117_signal: Slope of normalized price (window=252, slope_window=63)

# Feature f19anp_f19_atr_normalized_price_slope_v118_signal: Slope of normalized price (window=504, slope_window=63)

# Feature f19anp_f19_atr_normalized_price_slope_v119_signal: Slope of normalized price (window=5, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v120_signal: Slope of normalized price (window=10, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v121_signal: Slope of normalized price (window=21, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v122_signal: Slope of normalized price (window=63, slope_window=21)

# Feature f19anp_f19_atr_normalized_price_slope_v123_signal: Slope of normalized price (window=126, slope_window=21)

# Feature f19anp_f19_atr_normalized_price_slope_v124_signal: Slope of normalized price (window=252, slope_window=63)

# Feature f19anp_f19_atr_normalized_price_slope_v125_signal: Slope of normalized price (window=504, slope_window=63)

# Feature f19anp_f19_atr_normalized_price_slope_v126_signal: Slope of normalized price (window=5, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v127_signal: Slope of normalized price (window=10, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v128_signal: Slope of normalized price (window=21, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v129_signal: Slope of normalized price (window=63, slope_window=21)

# Feature f19anp_f19_atr_normalized_price_slope_v130_signal: Slope of normalized price (window=126, slope_window=21)

# Feature f19anp_f19_atr_normalized_price_slope_v131_signal: Slope of normalized price (window=252, slope_window=63)

# Feature f19anp_f19_atr_normalized_price_slope_v132_signal: Slope of normalized price (window=504, slope_window=63)

# Feature f19anp_f19_atr_normalized_price_slope_v133_signal: Slope of normalized price (window=5, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v134_signal: Slope of normalized price (window=10, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v135_signal: Slope of normalized price (window=21, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v136_signal: Slope of normalized price (window=63, slope_window=21)

# Feature f19anp_f19_atr_normalized_price_slope_v137_signal: Slope of normalized price (window=126, slope_window=21)

# Feature f19anp_f19_atr_normalized_price_slope_v138_signal: Slope of normalized price (window=252, slope_window=63)

# Feature f19anp_f19_atr_normalized_price_slope_v139_signal: Slope of normalized price (window=504, slope_window=63)

# Feature f19anp_f19_atr_normalized_price_slope_v140_signal: Slope of normalized price (window=5, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v141_signal: Slope of normalized price (window=10, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v142_signal: Slope of normalized price (window=21, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v143_signal: Slope of normalized price (window=63, slope_window=21)

# Feature f19anp_f19_atr_normalized_price_slope_v144_signal: Slope of normalized price (window=126, slope_window=21)

# Feature f19anp_f19_atr_normalized_price_slope_v145_signal: Slope of normalized price (window=252, slope_window=63)

# Feature f19anp_f19_atr_normalized_price_slope_v146_signal: Slope of normalized price (window=504, slope_window=63)

# Feature f19anp_f19_atr_normalized_price_slope_v147_signal: Slope of normalized price (window=5, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v148_signal: Slope of normalized price (window=10, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v149_signal: Slope of normalized price (window=21, slope_window=5)

# Feature f19anp_f19_atr_normalized_price_slope_v150_signal: Slope of normalized price (window=63, slope_window=21)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = 'read_only', 'sep', 'ticker', 'date'
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f'sep.{c}' for c in ['close', 'closeadj', 'high', 'low']}

SLOPE_NAMES = [f for f in globals() if f.startswith('f19anp_') and f.endswith('_signal')]

REGISTRY = {
    n: {
        'inputs': (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        'source_table': SOURCE_TABLE,
        'source_columns': {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        'entity_column': ENTITY_COLUMN, 'date_column': DATE_COLUMN,
        'order_by': ORDER_BY, 'no_forward_looking': NO_FORWARD_LOOKING, 'func': globals()[n]
    } for n in sorted(SLOPE_NAMES)
}

if __name__ == '__main__':
    sz = 1000; d = pd.DataFrame({'close': np.random.randn(sz).cumsum()+100, 'closeadj': np.random.randn(sz).cumsum()+100, 'high': np.random.randn(sz).cumsum()+110, 'low': np.random.randn(sz).cumsum()+90, 'ticker': ['T']*sz, 'date': pd.date_range('2020-01-01', periods=sz)})
    for n, c in REGISTRY.items():
        r = c['func'](**{i: d[i] for i in c['inputs']})
        assert isinstance(r, pd.Series)
    print('SLOPE OK')
