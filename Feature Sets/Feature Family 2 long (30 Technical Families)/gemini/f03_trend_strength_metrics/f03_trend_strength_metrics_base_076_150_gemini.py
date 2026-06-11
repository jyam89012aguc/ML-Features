# f03_trend_strength_metrics_base_076_150_gemini.py
import pandas as pd
import numpy as np

def _trend_slope(price, w):
    return (price - price.shift(w)) / price.shift(w).abs().replace(0, np.nan)
def _trend_consistency(price, w):
    return (price > price.shift(1)).astype(float).rolling(w).mean()
def _trend_efficiency(price, w):
    net_move = (price - price.shift(w)).abs()
    total_path = price.diff().abs().rolling(w).sum()
    return net_move / total_path.replace(0, np.nan)

def _sma(s, w): return s.rolling(w, min_periods=min(w, 5)).mean()
def _ema(s, w): return s.ewm(span=w, min_periods=min(w, 5), adjust=False).mean()
def _max(s, w): return s.rolling(w, min_periods=min(w, 5)).max()
def _min(s, w): return s.rolling(w, min_periods=min(w, 5)).min()
def _aroon_up(h, w): return 100 * (w - h.rolling(w+1).apply(np.argmax, raw=True)) / w
def _aroon_dn(l, w): return 100 * (w - l.rolling(w+1).apply(np.argmin, raw=True)) / w
def _linreg_slope(s, w):
    x = np.arange(w)
    x_mean = np.mean(x)
    def calc_slope(y):
        if np.any(np.isnan(y)): return np.nan
        y_mean = np.mean(y)
        return np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean)**2)
    return s.rolling(w).apply(calc_slope, raw=True)

# Trend slope of Aroon Up over 5 days
def f03ts_trend_slope_aroon_up_5d_v076_signal(high: pd.Series) -> pd.Series:
    res = _trend_slope(_aroon_up(high, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend slope of Aroon Up over 10 days
def f03ts_trend_slope_aroon_up_10d_v077_signal(high: pd.Series) -> pd.Series:
    res = _trend_slope(_aroon_up(high, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend slope of Aroon Up over 21 days
def f03ts_trend_slope_aroon_up_21d_v078_signal(high: pd.Series) -> pd.Series:
    res = _trend_slope(_aroon_up(high, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend slope of Aroon Up over 63 days (adjusted)
def f03ts_trend_slope_aroon_up_63d_v079_signal(high: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _trend_slope(_aroon_up(high * adj, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend slope of Aroon Up over 126 days (adjusted)
def f03ts_trend_slope_aroon_up_126d_v080_signal(high: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _trend_slope(_aroon_up(high * adj, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend slope of Aroon Up over 252 days (adjusted)
def f03ts_trend_slope_aroon_up_252d_v081_signal(high: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _trend_slope(_aroon_up(high * adj, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend slope of Aroon Up over 504 days (adjusted)
def f03ts_trend_slope_aroon_up_504d_v082_signal(high: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _trend_slope(_aroon_up(high * adj, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of Aroon Down over 5 days
def f03ts_trend_consistency_aroon_dn_5d_v083_signal(low: pd.Series) -> pd.Series:
    res = _trend_consistency(_aroon_dn(low, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of Aroon Down over 10 days
def f03ts_trend_consistency_aroon_dn_10d_v084_signal(low: pd.Series) -> pd.Series:
    res = _trend_consistency(_aroon_dn(low, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of Aroon Down over 21 days
def f03ts_trend_consistency_aroon_dn_21d_v085_signal(low: pd.Series) -> pd.Series:
    res = _trend_consistency(_aroon_dn(low, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of Aroon Down over 63 days (adjusted)
def f03ts_trend_consistency_aroon_dn_63d_v086_signal(low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _trend_consistency(_aroon_dn(low * adj, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of Aroon Down over 126 days (adjusted)
def f03ts_trend_consistency_aroon_dn_126d_v087_signal(low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _trend_consistency(_aroon_dn(low * adj, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of Aroon Down over 252 days (adjusted)
def f03ts_trend_consistency_aroon_dn_252d_v088_signal(low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _trend_consistency(_aroon_dn(low * adj, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of Aroon Down over 504 days (adjusted)
def f03ts_trend_consistency_aroon_dn_504d_v089_signal(low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _trend_consistency(_aroon_dn(low * adj, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of Aroon Up over 5 days
def f03ts_trend_efficiency_aroon_up_5d_v090_signal(high: pd.Series) -> pd.Series:
    res = _trend_efficiency(_aroon_up(high, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of Aroon Up over 10 days
def f03ts_trend_efficiency_aroon_up_10d_v091_signal(high: pd.Series) -> pd.Series:
    res = _trend_efficiency(_aroon_up(high, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of Aroon Up over 21 days
def f03ts_trend_efficiency_aroon_up_21d_v092_signal(high: pd.Series) -> pd.Series:
    res = _trend_efficiency(_aroon_up(high, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of Aroon Up over 63 days (adjusted)
def f03ts_trend_efficiency_aroon_up_63d_v093_signal(high: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _trend_efficiency(_aroon_up(high * adj, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of Aroon Up over 126 days (adjusted)
def f03ts_trend_efficiency_aroon_up_126d_v094_signal(high: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _trend_efficiency(_aroon_up(high * adj, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of Aroon Up over 252 days (adjusted)
def f03ts_trend_efficiency_aroon_up_252d_v095_signal(high: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _trend_efficiency(_aroon_up(high * adj, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of Aroon Up over 504 days (adjusted)
def f03ts_trend_efficiency_aroon_up_504d_v096_signal(high: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _trend_efficiency(_aroon_up(high * adj, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of Linreg Slope over 5 days
def f03ts_trend_consistency_linreg_slope_5d_v097_signal(close: pd.Series) -> pd.Series:
    res = _trend_consistency(_linreg_slope(close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of Linreg Slope over 10 days
def f03ts_trend_consistency_linreg_slope_10d_v098_signal(close: pd.Series) -> pd.Series:
    res = _trend_consistency(_linreg_slope(close, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of Linreg Slope over 21 days
def f03ts_trend_consistency_linreg_slope_21d_v099_signal(close: pd.Series) -> pd.Series:
    res = _trend_consistency(_linreg_slope(close, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of Linreg Slope over 63 days (adjusted)
def f03ts_trend_consistency_linreg_slope_63d_v100_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_consistency(_linreg_slope(closeadj, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of Linreg Slope over 126 days (adjusted)
def f03ts_trend_consistency_linreg_slope_126d_v101_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_consistency(_linreg_slope(closeadj, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of Linreg Slope over 252 days (adjusted)
def f03ts_trend_consistency_linreg_slope_252d_v102_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_consistency(_linreg_slope(closeadj, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of Linreg Slope over 504 days (adjusted)
def f03ts_trend_consistency_linreg_slope_504d_v103_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_consistency(_linreg_slope(closeadj, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of Linreg Slope over 5 days
def f03ts_trend_efficiency_linreg_slope_5d_v104_signal(close: pd.Series) -> pd.Series:
    res = _trend_efficiency(_linreg_slope(close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of Linreg Slope over 10 days
def f03ts_trend_efficiency_linreg_slope_10d_v105_signal(close: pd.Series) -> pd.Series:
    res = _trend_efficiency(_linreg_slope(close, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of Linreg Slope over 21 days
def f03ts_trend_efficiency_linreg_slope_21d_v106_signal(close: pd.Series) -> pd.Series:
    res = _trend_efficiency(_linreg_slope(close, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of Linreg Slope over 63 days (adjusted)
def f03ts_trend_efficiency_linreg_slope_63d_v107_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_efficiency(_linreg_slope(closeadj, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of Linreg Slope over 126 days (adjusted)
def f03ts_trend_efficiency_linreg_slope_126d_v108_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_efficiency(_linreg_slope(closeadj, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of Linreg Slope over 252 days (adjusted)
def f03ts_trend_efficiency_linreg_slope_252d_v109_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_efficiency(_linreg_slope(closeadj, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of Linreg Slope over 504 days (adjusted)
def f03ts_trend_efficiency_linreg_slope_504d_v110_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_efficiency(_linreg_slope(closeadj, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend slope of Linreg Slope over 5 days
def f03ts_trend_slope_linreg_slope_5d_v111_signal(close: pd.Series) -> pd.Series:
    res = _trend_slope(_linreg_slope(close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend slope of Linreg Slope over 10 days
def f03ts_trend_slope_linreg_slope_10d_v112_signal(close: pd.Series) -> pd.Series:
    res = _trend_slope(_linreg_slope(close, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend slope of Linreg Slope over 21 days
def f03ts_trend_slope_linreg_slope_21d_v113_signal(close: pd.Series) -> pd.Series:
    res = _trend_slope(_linreg_slope(close, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend slope of Linreg Slope over 63 days (adjusted)
def f03ts_trend_slope_linreg_slope_63d_v114_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_slope(_linreg_slope(closeadj, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend slope of Linreg Slope over 126 days (adjusted)
def f03ts_trend_slope_linreg_slope_126d_v115_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_slope(_linreg_slope(closeadj, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend slope of Linreg Slope over 252 days (adjusted)
def f03ts_trend_slope_linreg_slope_252d_v116_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_slope(_linreg_slope(closeadj, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend slope of Linreg Slope over 504 days (adjusted)
def f03ts_trend_slope_linreg_slope_504d_v117_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_slope(_linreg_slope(closeadj, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of Trend Consistency over 5 days
def f03ts_trend_persistence_consistency_5d_v118_signal(close: pd.Series) -> pd.Series:
    res = _trend_consistency(_trend_consistency(close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of Trend Consistency over 10 days
def f03ts_trend_persistence_consistency_10d_v119_signal(close: pd.Series) -> pd.Series:
    res = _trend_consistency(_trend_consistency(close, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of Trend Consistency over 21 days
def f03ts_trend_persistence_consistency_21d_v120_signal(close: pd.Series) -> pd.Series:
    res = _trend_consistency(_trend_consistency(close, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of Trend Consistency over 63 days (adjusted)
def f03ts_trend_persistence_consistency_63d_v121_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_consistency(_trend_consistency(closeadj, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of Trend Consistency over 126 days (adjusted)
def f03ts_trend_persistence_consistency_126d_v122_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_consistency(_trend_consistency(closeadj, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of Trend Consistency over 252 days (adjusted)
def f03ts_trend_persistence_consistency_252d_v123_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_consistency(_trend_consistency(closeadj, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of Trend Consistency over 504 days (adjusted)
def f03ts_trend_persistence_consistency_504d_v124_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_consistency(_trend_consistency(closeadj, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of Trend Efficiency over 5 days
def f03ts_trend_persistence_efficiency_5d_v125_signal(close: pd.Series) -> pd.Series:
    res = _trend_consistency(_trend_efficiency(close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of Trend Efficiency over 10 days
def f03ts_trend_persistence_efficiency_10d_v126_signal(close: pd.Series) -> pd.Series:
    res = _trend_consistency(_trend_efficiency(close, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of Trend Efficiency over 21 days
def f03ts_trend_persistence_efficiency_21d_v127_signal(close: pd.Series) -> pd.Series:
    res = _trend_consistency(_trend_efficiency(close, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of Trend Efficiency over 63 days (adjusted)
def f03ts_trend_persistence_efficiency_63d_v128_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_consistency(_trend_efficiency(closeadj, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of Trend Efficiency over 126 days (adjusted)
def f03ts_trend_persistence_efficiency_126d_v129_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_consistency(_trend_efficiency(closeadj, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of Trend Efficiency over 252 days (adjusted)
def f03ts_trend_persistence_efficiency_252d_v130_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_consistency(_trend_efficiency(closeadj, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of Trend Efficiency over 504 days (adjusted)
def f03ts_trend_persistence_efficiency_504d_v131_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_consistency(_trend_efficiency(closeadj, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend slope of High-Low range over 10 days
def f03ts_trend_slope_hl_range_10d_v132_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    res = _trend_slope(high - low, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend slope of High-Low range over 21 days
def f03ts_trend_slope_hl_range_21d_v133_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    res = _trend_slope(high - low, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend slope of High-Low range over 63 days (adjusted)
def f03ts_trend_slope_hl_range_63d_v134_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _trend_slope((high - low) * adj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend slope of High-Low range over 126 days (adjusted)
def f03ts_trend_slope_hl_range_126d_v135_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _trend_slope((high - low) * adj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend slope of High-Low range over 252 days (adjusted)
def f03ts_trend_slope_hl_range_252d_v136_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _trend_slope((high - low) * adj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of close price variation v137

# Trend efficiency of close price variation v138

# Trend efficiency of close price variation v139

# Trend efficiency of close price variation v140
def f03ts_trend_efficiency_var_140_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_efficiency(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of close price variation v141
def f03ts_trend_efficiency_var_141_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_efficiency(closeadj, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of close price variation v142
def f03ts_trend_efficiency_var_142_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_efficiency(closeadj, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of close price variation v143

# Trend efficiency of close price variation v144

# Trend efficiency of close price variation v145

# Trend efficiency of close price variation v146

# Trend efficiency of close price variation v147

# Trend efficiency of close price variation v148

# Trend efficiency of close price variation v149

# Trend efficiency of close price variation v150

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low"]}

BASE_NAMES = [f for f in globals() if f.startswith("f03ts_") and f.endswith("_signal")]

F03_TREND_STRENGTH_METRICS_BASE_REGISTRY_076_150 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(BASE_NAMES)
}

if __name__ == "__main__":
    import pandas as pd; import numpy as np
    sz = 500; d = pd.DataFrame({"close": np.random.randn(sz).cumsum()+100, "closeadj": np.random.randn(sz).cumsum()+100, "high": np.random.randn(sz).cumsum()+110, "low": np.random.randn(sz).cumsum()+90, "ticker": ["T"]*sz, "date": pd.date_range("2020-01-01", periods=sz)})
    for n, c in F03_TREND_STRENGTH_METRICS_BASE_REGISTRY_076_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 076-150 OK")
