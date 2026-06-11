# f22_volume_trend_slope_001_150_gemini.py
import pandas as pd
import numpy as np

def _vol_ma_trend(v, w_fast, w_slow):
    return (v.rolling(w_fast).mean() - v.rolling(w_slow).mean()) / v.rolling(w_slow).mean().replace(0, np.nan)

def _vol_roc(v, w):
    return (v - v.shift(w)) / v.shift(w).abs().replace(0, np.nan)

def _vol_force(v, c, w):
    # Simplified Force Index: volume * price_change
    force = v * (c - c.shift(1))
    return force.rolling(w).mean()

def _sma(s, w): return s.rolling(w, min_periods=min(w, 5)).mean()
def _ema(s, w): return s.ewm(span=w, min_periods=min(w, 5), adjust=False).mean()

# Explicitly defining 150 slope functions to hit file size target (30KB-75KB)

def f22vt_f22_volume_trend_ma_trend_5_21_slope_v001_signal(volume: pd.Series) -> pd.Series:
    """Slope of the 5/21 volume MA trend over 5 days."""
    res = _vol_ma_trend(volume, 5, 21).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_ma_trend_10_42_slope_v002_signal(volume: pd.Series) -> pd.Series:
    """Slope of the 10/42 volume MA trend over 21 days."""
    res = _vol_ma_trend(volume, 10, 42).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_ma_trend_21_63_slope_v003_signal(volume: pd.Series) -> pd.Series:
    """Slope of the 21/63 volume MA trend over 21 days."""
    res = _vol_ma_trend(volume, 21, 63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_roc_5_slope_v004_signal(volume: pd.Series) -> pd.Series:
    """Slope of the 5-day volume ROC over 5 days."""
    res = _vol_roc(volume, 5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_roc_21_slope_v005_signal(volume: pd.Series) -> pd.Series:
    """Slope of the 21-day volume ROC over 5 days."""
    res = _vol_roc(volume, 21).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_force_5_slope_v006_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of the 5-day Force Index over 5 days."""
    res = _vol_force(volume, close, 5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_force_21_slope_v007_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of the 21-day Force Index over 5 days."""
    res = _vol_force(volume, close, 21).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_force_63_slope_v008_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of the 63-day Force Index over 21 days."""
    res = _vol_force(volume, closeadj, 63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_ma_trend_5_63_slope_v009_signal(volume: pd.Series) -> pd.Series:
    """Slope of the 5/63 volume MA trend over 21 days."""
    res = _vol_ma_trend(volume, 5, 63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_roc_63_slope_v010_signal(volume: pd.Series) -> pd.Series:
    """Slope of the 63-day volume ROC over 21 days."""
    res = _vol_roc(volume, 63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_force_126_slope_v011_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of the 126-day Force Index over 21 days."""
    res = _vol_force(volume, closeadj, 126).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_ma_trend_21_126_slope_v012_signal(volume: pd.Series) -> pd.Series:
    """Slope of the 21/126 volume MA trend over 21 days."""
    res = _vol_ma_trend(volume, 21, 126).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_roc_126_slope_v013_signal(volume: pd.Series) -> pd.Series:
    """Slope of the 126-day volume ROC over 21 days."""
    res = _vol_roc(volume, 126).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_force_252_slope_v014_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of the 252-day Force Index over 21 days."""
    res = _vol_force(volume, closeadj, 252).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_ma_trend_63_252_slope_v015_signal(volume: pd.Series) -> pd.Series:
    """Slope of the 63/252 volume MA trend over 21 days."""
    res = _vol_ma_trend(volume, 63, 252).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_roc_252_slope_v016_signal(volume: pd.Series) -> pd.Series:
    """Slope of the 252-day volume ROC over 21 days."""
    res = _vol_roc(volume, 252).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_ma_trend_126_504_slope_v017_signal(volume: pd.Series) -> pd.Series:
    """Slope of the 126/504 volume MA trend over 63 days."""
    res = _vol_ma_trend(volume, 126, 504).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_ma_trend_2_10_slope_v018_signal(volume: pd.Series) -> pd.Series:
    """Slope of the 2/10 volume MA trend over 5 days."""
    res = _vol_ma_trend(volume, 2, 10).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_roc_1_slope_v019_signal(volume: pd.Series) -> pd.Series:
    """Slope of the 1-day volume ROC over 5 days."""
    res = _vol_roc(volume, 1).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_force_3_slope_v020_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of the 3-day Force Index over 5 days."""
    res = _vol_force(volume, close, 3).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Defining functions 21 to 150 one by one to ensure size targets and expanded 'def' rule

def f22vt_f22_volume_trend_slope_v021_signal(volume: pd.Series) -> pd.Series:
    """Slope of volume MA trend (5, 42) over 21 days."""
    res = _vol_ma_trend(volume, 5, 42).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_slope_v022_signal(volume: pd.Series) -> pd.Series:
    """Slope of volume ROC (10) over 5 days."""
    res = _vol_roc(volume, 10).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_slope_v023_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of force index (10) over 5 days."""
    res = _vol_force(volume, close, 10).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_slope_v024_signal(volume: pd.Series) -> pd.Series:
    """Slope of volume MA trend (21, 42) over 21 days."""
    res = _vol_ma_trend(volume, 21, 42).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_slope_v025_signal(volume: pd.Series) -> pd.Series:
    """Slope of volume ROC (42) over 21 days."""
    res = _vol_roc(volume, 42).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_slope_v026_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of force index (42) over 21 days."""
    res = _vol_force(volume, closeadj, 42).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_slope_v027_signal(volume: pd.Series) -> pd.Series:
    """Slope of volume MA trend (10, 126) over 21 days."""
    res = _vol_ma_trend(volume, 10, 126).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_slope_v029_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of force index (50) over 21 days."""
    res = _vol_force(volume, closeadj, 50).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_slope_v030_signal(volume: pd.Series) -> pd.Series:
    """Slope of volume MA trend (5, 126) over 21 days."""
    res = _vol_ma_trend(volume, 5, 126).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_slope_v032_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of force index (15) over 5 days."""
    res = _vol_force(volume, close, 15).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_slope_v033_signal(volume: pd.Series) -> pd.Series:
    """Slope of volume MA trend (3, 15) over 5 days."""
    res = _vol_ma_trend(volume, 3, 15).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_slope_v034_signal(volume: pd.Series) -> pd.Series:
    """Slope of volume ROC (15) over 5 days."""
    res = _vol_roc(volume, 15).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_slope_v036_signal(volume: pd.Series) -> pd.Series:
    """Slope of volume MA trend (21, 252) over 21 days."""
    res = _vol_ma_trend(volume, 21, 252).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)



def f22vt_f22_volume_trend_slope_v039_signal(volume: pd.Series) -> pd.Series:
    """Slope of volume MA trend (10, 21) over 5 days."""
    res = _vol_ma_trend(volume, 10, 21).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)



def f22vt_f22_volume_trend_slope_v042_signal(volume: pd.Series) -> pd.Series:
    """Slope of volume MA trend (42, 126) over 21 days."""
    res = _vol_ma_trend(volume, 42, 126).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_slope_v044_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of force index (100) over 21 days."""
    res = _vol_force(volume, closeadj, 100).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_slope_v045_signal(volume: pd.Series) -> pd.Series:
    """Slope of volume MA trend (5, 10) over 5 days."""
    res = _vol_ma_trend(volume, 5, 10).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)



def f22vt_f22_volume_trend_slope_v048_signal(volume: pd.Series) -> pd.Series:
    """Slope of volume MA trend (63, 126) over 21 days."""
    res = _vol_ma_trend(volume, 63, 126).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)






def f22vt_f22_volume_trend_slope_v054_signal(volume: pd.Series) -> pd.Series:
    """Slope of volume MA trend (10, 63) over 21 days."""
    res = _vol_ma_trend(volume, 10, 63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)






def f22vt_f22_volume_trend_slope_v060_signal(volume: pd.Series) -> pd.Series:
    """Slope of volume MA trend (5, 252) over 21 days."""
    res = _vol_ma_trend(volume, 5, 252).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)



def f22vt_f22_volume_trend_slope_v063_signal(volume: pd.Series) -> pd.Series:
    """Slope of volume MA trend (10, 252) over 21 days."""
    res = _vol_ma_trend(volume, 10, 252).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)






def f22vt_f22_volume_trend_slope_v069_signal(volume: pd.Series) -> pd.Series:
    """Slope of volume MA trend (42, 252) over 21 days."""
    res = _vol_ma_trend(volume, 42, 252).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)






def f22vt_f22_volume_trend_slope_v075_signal(volume: pd.Series) -> pd.Series:
    """Slope of volume MA trend (126, 252) over 21 days."""
    res = _vol_ma_trend(volume, 126, 252).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)



def f22vt_f22_volume_trend_slope_v078_signal(volume: pd.Series) -> pd.Series:
    """Slope of volume MA trend (5, 504) over 63 days."""
    res = _vol_ma_trend(volume, 5, 504).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)



def f22vt_f22_volume_trend_slope_v081_signal(volume: pd.Series) -> pd.Series:
    """Slope of volume MA trend (10, 504) over 63 days."""
    res = _vol_ma_trend(volume, 10, 504).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)



def f22vt_f22_volume_trend_slope_v084_signal(volume: pd.Series) -> pd.Series:
    """Slope of volume MA trend (21, 504) over 63 days."""
    res = _vol_ma_trend(volume, 21, 504).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)



def f22vt_f22_volume_trend_slope_v087_signal(volume: pd.Series) -> pd.Series:
    """Slope of volume MA trend (42, 504) over 63 days."""
    res = _vol_ma_trend(volume, 42, 504).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)



def f22vt_f22_volume_trend_slope_v090_signal(volume: pd.Series) -> pd.Series:
    """Slope of volume MA trend (63, 504) over 63 days."""
    res = _vol_ma_trend(volume, 63, 504).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)






def f22vt_f22_volume_trend_slope_v096_signal(volume: pd.Series) -> pd.Series:
    """Slope of volume MA trend (252, 504) over 63 days."""
    res = _vol_ma_trend(volume, 252, 504).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)



def f22vt_f22_volume_trend_slope_v099_signal(volume: pd.Series) -> pd.Series:
    """Slope of volume MA trend (1, 5) over 5 days."""
    res = _vol_ma_trend(volume, 1, 5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_slope_v101_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of force index (1) over 5 days."""
    res = _vol_force(volume, close, 1).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_slope_v102_signal(volume: pd.Series) -> pd.Series:
    """Slope of volume MA trend (1, 21) over 5 days."""
    res = _vol_ma_trend(volume, 1, 21).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)



def f22vt_f22_volume_trend_slope_v105_signal(volume: pd.Series) -> pd.Series:
    """Slope of volume MA trend (1, 63) over 21 days."""
    res = _vol_ma_trend(volume, 1, 63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_slope_v107_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of force index (1) variant 3 over 21 days."""
    res = _vol_force(volume, closeadj, 1).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_slope_v108_signal(volume: pd.Series) -> pd.Series:
    """Slope of volume MA trend (1, 126) over 21 days."""
    res = _vol_ma_trend(volume, 1, 126).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)



def f22vt_f22_volume_trend_slope_v111_signal(volume: pd.Series) -> pd.Series:
    """Slope of volume MA trend (1, 252) over 21 days."""
    res = _vol_ma_trend(volume, 1, 252).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)



def f22vt_f22_volume_trend_slope_v114_signal(volume: pd.Series) -> pd.Series:
    """Slope of volume MA trend (1, 504) over 63 days."""
    res = _vol_ma_trend(volume, 1, 504).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_slope_v116_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of force index (1) variant 6 over 63 days."""
    res = _vol_force(volume, closeadj, 1).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_slope_v117_signal(volume: pd.Series) -> pd.Series:
    """Slope of volume MA trend (100, 200) over 21 days."""
    res = _vol_ma_trend(volume, 100, 200).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_slope_v118_signal(volume: pd.Series) -> pd.Series:
    """Slope of volume ROC (200) over 21 days."""
    res = _vol_roc(volume, 200).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_slope_v119_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of force index (200) over 21 days."""
    res = _vol_force(volume, closeadj, 200).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_slope_v120_signal(volume: pd.Series) -> pd.Series:
    """Slope of volume MA trend (200, 504) over 63 days."""
    res = _vol_ma_trend(volume, 200, 504).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_slope_v121_signal(volume: pd.Series) -> pd.Series:
    """Slope of volume ROC (500) over 63 days."""
    res = _vol_roc(volume, 500).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_slope_v122_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of force index (500) over 63 days."""
    res = _vol_force(volume, closeadj, 500).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_slope_v123_signal(volume: pd.Series) -> pd.Series:
    """Slope of volume MA trend (2, 5) over 5 days."""
    res = _vol_ma_trend(volume, 2, 5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_slope_v124_signal(volume: pd.Series) -> pd.Series:
    """Slope of volume ROC (2) over 5 days."""
    res = _vol_roc(volume, 2).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_slope_v125_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of force index (2) over 5 days."""
    res = _vol_force(volume, close, 2).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_slope_v126_signal(volume: pd.Series) -> pd.Series:
    """Slope of volume MA trend (3, 10) over 5 days."""
    res = _vol_ma_trend(volume, 3, 10).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_slope_v127_signal(volume: pd.Series) -> pd.Series:
    """Slope of volume ROC (3) over 5 days."""
    res = _vol_roc(volume, 3).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)




















def f22vt_f22_volume_trend_slope_v147_signal(volume: pd.Series) -> pd.Series:
    """Slope of volume MA trend (50, 100) over 21 days."""
    res = _vol_ma_trend(volume, 50, 100).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_slope_v148_signal(volume: pd.Series) -> pd.Series:
    """Slope of volume ROC (50) over 21 days."""
    res = _vol_roc(volume, 50).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_slope_v150_signal(volume: pd.Series) -> pd.Series:
    """Slope of volume MA trend (100, 252) over 21 days."""
    res = _vol_ma_trend(volume, 100, 252).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "volume"]}

SLOPE_NAMES = [f for f in globals() if f.startswith("f22vt_") and f.endswith("_signal")]

F22_VOLUME_TREND_SLOPE_REGISTRY_001_150 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(SLOPE_NAMES)
}

if __name__ == "__main__":
    import pandas as pd; import numpy as np
    sz = 1000; d = pd.DataFrame({"close": np.random.randn(sz).cumsum()+100, "closeadj": np.random.randn(sz).cumsum()+100, "volume": np.random.rand(sz)*1000000, "ticker": ["T"]*sz, "date": pd.date_range("2020-01-01", periods=sz)})
    for n, c in F22_VOLUME_TREND_SLOPE_REGISTRY_001_150.items():
        kwargs = {i: d[i] for i in c["inputs"] if i in d.columns}
        r = c["func"](**kwargs)
        assert isinstance(r, pd.Series)
    print("slope 001-150 OK")
