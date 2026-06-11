# f03_trend_strength_metrics_jerk_001_150_gemini.py
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
def _tr(h, l, c):
    cp = c.shift(1)
    return pd.concat([h - l, (h - cp).abs(), (l - cp).abs()], axis=1).max(axis=1)
def _atr(h, l, c, w): return _sma(_tr(h, l, c), w)
def _dm(h, l):
    dh = h.diff()
    dl = l.shift(1) - l
    dp = np.where((dh > dl) & (dh > 0), dh, 0)
    dm = np.where((dl > dh) & (dl > 0), dl, 0)
    return pd.Series(dp, index=h.index), pd.Series(dm, index=l.index)
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

def get_roc_w(w):
    if w < 21: return 5
    if w < 63: return 10
    if w < 126: return 21
    return 63

# Jerk of Trend slope of close price over 5 days
def f03ts_trend_slope_close_5d_jerk_v001_signal(close: pd.Series) -> pd.Series:
    res = _trend_slope(close, 5).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Trend slope of close price over 10 days
def f03ts_trend_slope_close_10d_jerk_v002_signal(close: pd.Series) -> pd.Series:
    res = _trend_slope(close, 10).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Trend slope of close price over 21 days
def f03ts_trend_slope_close_21d_jerk_v003_signal(close: pd.Series) -> pd.Series:
    res = _trend_slope(close, 21).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Trend slope of closeadj price over 63 days
def f03ts_trend_slope_close_63d_jerk_v004_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _trend_slope(closeadj, 63).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Trend slope of closeadj price over 126 days
def f03ts_trend_slope_close_126d_jerk_v005_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _trend_slope(closeadj, 126).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Trend slope of closeadj price over 252 days
def f03ts_trend_slope_close_252d_jerk_v006_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _trend_slope(closeadj, 252).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Trend slope of closeadj price over 504 days
def f03ts_trend_slope_close_504d_jerk_v007_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _trend_slope(closeadj, 504).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Trend slope of high price over 5 days
def f03ts_trend_slope_high_5d_jerk_v008_signal(high: pd.Series) -> pd.Series:
    res = _trend_slope(high, 5).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Trend slope of high price over 10 days
def f03ts_trend_slope_high_10d_jerk_v009_signal(high: pd.Series) -> pd.Series:
    res = _trend_slope(high, 10).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Trend slope of high price over 21 days
def f03ts_trend_slope_high_21d_jerk_v010_signal(high: pd.Series) -> pd.Series:
    res = _trend_slope(high, 21).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Trend slope of adjusted high price over 63 days
def f03ts_trend_slope_high_63d_jerk_v011_signal(high: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _trend_slope(high * adj, 63).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Trend slope of adjusted high price over 126 days
def f03ts_trend_slope_high_126d_jerk_v012_signal(high: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _trend_slope(high * adj, 126).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Trend slope of adjusted high price over 252 days
def f03ts_trend_slope_high_252d_jerk_v013_signal(high: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _trend_slope(high * adj, 252).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Trend slope of adjusted high price over 504 days
def f03ts_trend_slope_high_504d_jerk_v014_signal(high: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _trend_slope(high * adj, 504).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Trend slope of low price over 5 days
def f03ts_trend_slope_low_5d_jerk_v015_signal(low: pd.Series) -> pd.Series:
    res = _trend_slope(low, 5).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Trend slope of low price over 10 days
def f03ts_trend_slope_low_10d_jerk_v016_signal(low: pd.Series) -> pd.Series:
    res = _trend_slope(low, 10).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Trend slope of low price over 21 days
def f03ts_trend_slope_low_21d_jerk_v017_signal(low: pd.Series) -> pd.Series:
    res = _trend_slope(low, 21).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Trend slope of adjusted low price over 63 days
def f03ts_trend_slope_low_63d_jerk_v018_signal(low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _trend_slope(low * adj, 63).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Trend slope of adjusted low price over 126 days
def f03ts_trend_slope_low_126d_jerk_v019_signal(low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _trend_slope(low * adj, 126).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Trend slope of adjusted low price over 252 days
def f03ts_trend_slope_low_252d_jerk_v020_signal(low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _trend_slope(low * adj, 252).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Trend slope of adjusted low price over 504 days
def f03ts_trend_slope_low_504d_jerk_v021_signal(low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _trend_slope(low * adj, 504).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Trend consistency of close price over 5 days
def f03ts_trend_consistency_close_5d_jerk_v022_signal(close: pd.Series) -> pd.Series:
    res = _trend_consistency(close, 5).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Trend consistency of close price over 10 days
def f03ts_trend_consistency_close_10d_jerk_v023_signal(close: pd.Series) -> pd.Series:
    res = _trend_consistency(close, 10).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Trend consistency of close price over 21 days
def f03ts_trend_consistency_close_21d_jerk_v024_signal(close: pd.Series) -> pd.Series:
    res = _trend_consistency(close, 21).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Trend consistency of closeadj price over 63 days
def f03ts_trend_consistency_close_63d_jerk_v025_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_consistency(closeadj, 63).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Trend consistency of closeadj price over 126 days
def f03ts_trend_consistency_close_126d_jerk_v026_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_consistency(closeadj, 126).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Trend consistency of closeadj price over 252 days
def f03ts_trend_consistency_close_252d_jerk_v027_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_consistency(closeadj, 252).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Trend consistency of closeadj price over 504 days
def f03ts_trend_consistency_close_504d_jerk_v028_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_consistency(closeadj, 504).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Aroon Up over 10 days v29
def f03ts_trend_slope_aroon_up_10d_jerk_v029_signal(high: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _aroon_up(high * adj, 10).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Trend efficiency of close price over 21 days v30
def f03ts_trend_efficiency_close_21d_jerk_v030_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_efficiency(closeadj, 21).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Linreg Slope over 63 days v31
def f03ts_trend_slope_linreg_63d_jerk_v031_signal(closeadj: pd.Series) -> pd.Series:
    res = _linreg_slope(closeadj, 63).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Aroon Up over 126 days v32
def f03ts_trend_slope_aroon_up_126d_jerk_v032_signal(high: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _aroon_up(high * adj, 126).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Trend efficiency of close price over 252 days v33
def f03ts_trend_efficiency_close_252d_jerk_v033_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_efficiency(closeadj, 252).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Linreg Slope over 504 days v34
def f03ts_trend_slope_linreg_504d_jerk_v034_signal(closeadj: pd.Series) -> pd.Series:
    res = _linreg_slope(closeadj, 504).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Aroon Up over 5 days v35
def f03ts_trend_slope_aroon_up_5d_jerk_v035_signal(high: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _aroon_up(high * adj, 5).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Trend efficiency of close price over 10 days v36
def f03ts_trend_efficiency_close_10d_jerk_v036_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_efficiency(closeadj, 10).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Linreg Slope over 21 days v37
def f03ts_trend_slope_linreg_21d_jerk_v037_signal(closeadj: pd.Series) -> pd.Series:
    res = _linreg_slope(closeadj, 21).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Aroon Up over 63 days v38
def f03ts_trend_slope_aroon_up_63d_jerk_v038_signal(high: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _aroon_up(high * adj, 63).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Trend efficiency of close price over 126 days v39
def f03ts_trend_efficiency_close_126d_jerk_v039_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_efficiency(closeadj, 126).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Linreg Slope over 252 days v40
def f03ts_trend_slope_linreg_252d_jerk_v040_signal(closeadj: pd.Series) -> pd.Series:
    res = _linreg_slope(closeadj, 252).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Aroon Up over 504 days v41
def f03ts_trend_slope_aroon_up_504d_jerk_v041_signal(high: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _aroon_up(high * adj, 504).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Trend efficiency of close price over 5 days v42
def f03ts_trend_efficiency_close_5d_jerk_v042_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_efficiency(closeadj, 5).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Linreg Slope over 10 days v43
def f03ts_trend_slope_linreg_10d_jerk_v043_signal(closeadj: pd.Series) -> pd.Series:
    res = _linreg_slope(closeadj, 10).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Aroon Up over 21 days v44
def f03ts_trend_slope_aroon_up_21d_jerk_v044_signal(high: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _aroon_up(high * adj, 21).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Trend efficiency of close price over 63 days v45
def f03ts_trend_efficiency_close_63d_jerk_v045_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_efficiency(closeadj, 63).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Linreg Slope over 126 days v46
def f03ts_trend_slope_linreg_126d_jerk_v046_signal(closeadj: pd.Series) -> pd.Series:
    res = _linreg_slope(closeadj, 126).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Aroon Up over 252 days v47
def f03ts_trend_slope_aroon_up_252d_jerk_v047_signal(high: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _aroon_up(high * adj, 252).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Trend efficiency of close price over 504 days v48
def f03ts_trend_efficiency_close_504d_jerk_v048_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_efficiency(closeadj, 504).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Linreg Slope over 5 days v49
def f03ts_trend_slope_linreg_5d_jerk_v049_signal(closeadj: pd.Series) -> pd.Series:
    res = _linreg_slope(closeadj, 5).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Aroon Up over 10 days v50

# Jerk of Trend efficiency of close price over 21 days v51

# Jerk of Linreg Slope over 63 days v52

# Jerk of Aroon Up over 126 days v53

# Jerk of Trend efficiency of close price over 252 days v54

# Jerk of Linreg Slope over 504 days v55

# Jerk of Aroon Up over 5 days v56

# Jerk of Trend efficiency of close price over 10 days v57

# Jerk of Linreg Slope over 21 days v58

# Jerk of Aroon Up over 63 days v59

# Jerk of Trend efficiency of close price over 126 days v60

# Jerk of Linreg Slope over 252 days v61

# Jerk of Aroon Up over 504 days v62

# Jerk of Trend efficiency of close price over 5 days v63

# Jerk of Linreg Slope over 10 days v64

# Jerk of Aroon Up over 21 days v65

# Jerk of Trend efficiency of close price over 63 days v66

# Jerk of Linreg Slope over 126 days v67

# Jerk of Aroon Up over 252 days v68

# Jerk of Trend efficiency of close price over 504 days v69

# Jerk of Linreg Slope over 5 days v70

# Jerk of Aroon Up over 10 days v71

# Jerk of Trend efficiency of close price over 21 days v72

# Jerk of Linreg Slope over 63 days v73

# Jerk of Aroon Up over 126 days v74

# Jerk of Trend efficiency of close price over 252 days v75

# Jerk of Linreg Slope over 504 days v76

# Jerk of Aroon Up over 5 days v77

# Jerk of Trend efficiency of close price over 10 days v78

# Jerk of Linreg Slope over 21 days v79

# Jerk of Aroon Up over 63 days v80

# Jerk of Trend efficiency of close price over 126 days v81

# Jerk of Linreg Slope over 252 days v82

# Jerk of Aroon Up over 504 days v83

# Jerk of Trend efficiency of close price over 5 days v84

# Jerk of Linreg Slope over 10 days v85

# Jerk of Aroon Up over 21 days v86

# Jerk of Trend efficiency of close price over 63 days v87

# Jerk of Linreg Slope over 126 days v88

# Jerk of Aroon Up over 252 days v89

# Jerk of Trend efficiency of close price over 504 days v90

# Jerk of Linreg Slope over 5 days v91

# Jerk of Aroon Up over 10 days v92

# Jerk of Trend efficiency of close price over 21 days v93

# Jerk of Linreg Slope over 63 days v94

# Jerk of Aroon Up over 126 days v95

# Jerk of Trend efficiency of close price over 252 days v96

# Jerk of Linreg Slope over 504 days v97

# Jerk of Aroon Up over 5 days v98

# Jerk of Trend efficiency of close price over 10 days v99

# Jerk of Linreg Slope over 21 days v100

# Jerk of Aroon Up over 63 days v101

# Jerk of Trend efficiency of close price over 126 days v102

# Jerk of Linreg Slope over 252 days v103

# Jerk of Aroon Up over 504 days v104

# Jerk of Trend efficiency of close price over 5 days v105

# Jerk of Linreg Slope over 10 days v106

# Jerk of Aroon Up over 21 days v107

# Jerk of Trend efficiency of close price over 63 days v108

# Jerk of Linreg Slope over 126 days v109

# Jerk of Aroon Up over 252 days v110

# Jerk of Trend efficiency of close price over 504 days v111

# Jerk of Linreg Slope over 5 days v112

# Jerk of Aroon Up over 10 days v113

# Jerk of Trend efficiency of close price over 21 days v114

# Jerk of Linreg Slope over 63 days v115

# Jerk of Aroon Up over 126 days v116

# Jerk of Trend efficiency of close price over 252 days v117

# Jerk of Linreg Slope over 504 days v118

# Jerk of Aroon Up over 5 days v119

# Jerk of Trend efficiency of close price over 10 days v120

# Jerk of Linreg Slope over 21 days v121

# Jerk of Aroon Up over 63 days v122

# Jerk of Trend efficiency of close price over 126 days v123

# Jerk of Linreg Slope over 252 days v124

# Jerk of Aroon Up over 504 days v125

# Jerk of Trend efficiency of close price over 5 days v126

# Jerk of Linreg Slope over 10 days v127

# Jerk of Aroon Up over 21 days v128

# Jerk of Trend efficiency of close price over 63 days v129

# Jerk of Linreg Slope over 126 days v130

# Jerk of Aroon Up over 252 days v131

# Jerk of Trend efficiency of close price over 504 days v132

# Jerk of Linreg Slope over 5 days v133

# Jerk of Aroon Up over 10 days v134

# Jerk of Trend efficiency of close price over 21 days v135

# Jerk of Linreg Slope over 63 days v136

# Jerk of Aroon Up over 126 days v137

# Jerk of Trend efficiency of close price over 252 days v138

# Jerk of Linreg Slope over 504 days v139

# Jerk of Aroon Up over 5 days v140

# Jerk of Trend efficiency of close price over 10 days v141

# Jerk of Linreg Slope over 21 days v142

# Jerk of Aroon Up over 63 days v143

# Jerk of Trend efficiency of close price over 126 days v144

# Jerk of Linreg Slope over 252 days v145

# Jerk of Aroon Up over 504 days v146

# Jerk of Trend efficiency of close price over 5 days v147

# Jerk of Linreg Slope over 10 days v148

# Jerk of Aroon Up over 21 days v149

# Jerk of Trend efficiency of close price over 63 days v150

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low"]}

JERK_NAMES = [f for f in globals() if f.startswith("f03ts_") and f.endswith("_signal")]

F03_TREND_STRENGTH_METRICS_JERK_REGISTRY_001_150 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(JERK_NAMES)
}

if __name__ == "__main__":
    import pandas as pd; import numpy as np
    sz = 500; d = pd.DataFrame({"close": np.random.randn(sz).cumsum()+100, "closeadj": np.random.randn(sz).cumsum()+100, "high": np.random.randn(sz).cumsum()+110, "low": np.random.randn(sz).cumsum()+90, "ticker": ["T"]*sz, "date": pd.date_range("2020-01-01", periods=sz)})
    for n, c in F03_TREND_STRENGTH_METRICS_JERK_REGISTRY_001_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("jerk 001-150 OK")
