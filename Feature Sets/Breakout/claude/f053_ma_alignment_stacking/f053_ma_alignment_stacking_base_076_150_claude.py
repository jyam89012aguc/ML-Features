import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f053_ma_fast(closeadj, w):
    return closeadj.rolling(w, min_periods=max(1, w // 2)).mean()


def _f053_ma_alignment(closeadj, w):
    w_fast = max(2, w // 4)
    w_mid = max(3, w // 2)
    w_slow = w
    fast = closeadj.rolling(w_fast, min_periods=max(1, w_fast // 2)).mean()
    mid = closeadj.rolling(w_mid, min_periods=max(1, w_mid // 2)).mean()
    slow = closeadj.rolling(w_slow, min_periods=max(1, w_slow // 2)).mean()
    return (fast - mid) / slow.replace(0, np.nan).abs() + (mid - slow) / slow.replace(0, np.nan).abs()


def _f053_stacking_score(closeadj, w):
    w_fast = max(2, w // 4)
    w_mid = max(3, w // 2)
    w_slow = w
    fast = closeadj.rolling(w_fast, min_periods=max(1, w_fast // 2)).mean()
    mid = closeadj.rolling(w_mid, min_periods=max(1, w_mid // 2)).mean()
    slow = closeadj.rolling(w_slow, min_periods=max(1, w_slow // 2)).mean()
    align = (fast - mid) / slow.replace(0, np.nan).abs() + (mid - slow) / slow.replace(0, np.nan).abs()
    return align * closeadj


def f053mas_f053_ma_alignment_stacking_ma_fast_5d_base_v076_signal(closeadj):
    result = _z(_f053_ma_fast(closeadj, 5), 5) * _z(_f053_ma_fast(closeadj, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_10d_base_v077_signal(closeadj):
    result = _mean(_f053_ma_fast(closeadj, 10), 10) * _std(_f053_ma_fast(closeadj, 10), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_21d_base_v078_signal(closeadj):
    result = _mean(_f053_ma_fast(closeadj, 21), 21) / _std(_f053_ma_fast(closeadj, 21), 21).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_42d_base_v079_signal(closeadj):
    result = ((_f053_ma_fast(closeadj, 42)).ewm(span=42, adjust=False).mean() - _mean(_f053_ma_fast(closeadj, 42), 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_63d_base_v080_signal(closeadj):
    result = ((_f053_ma_fast(closeadj, 63)).rolling(63, min_periods=max(1, 63 // 2)).max() - (_f053_ma_fast(closeadj, 63)).rolling(63, min_periods=max(1, 63 // 2)).min()) * closeadj / _mean(closeadj.abs() + 1e-9, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_126d_base_v081_signal(closeadj):
    result = _mean((_f053_ma_fast(closeadj, 126)).abs(), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_189d_base_v082_signal(closeadj):
    result = _std((_f053_ma_fast(closeadj, 189)).abs(), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_252d_base_v083_signal(closeadj):
    result = (_f053_ma_fast(closeadj, 252)).diff(max(1, 252 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_378d_base_v084_signal(closeadj):
    result = ((1.0 + (_f053_ma_fast(closeadj, 378)).pct_change().fillna(0)).rolling(378, min_periods=max(1, 378 // 2)).apply(np.prod, raw=True) - 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_504d_base_v085_signal(closeadj):
    result = (_f053_ma_fast(closeadj, 504)).rolling(504, min_periods=max(1, 504 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_5d_base_v086_signal(closeadj):
    result = ((_f053_ma_fast(closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).median() - _mean(_f053_ma_fast(closeadj, 5), 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_10d_base_v087_signal(closeadj):
    result = ((_f053_ma_fast(closeadj, 10)).rolling(10, min_periods=max(1, 10 // 2)).quantile(0.75) - (_f053_ma_fast(closeadj, 10)).rolling(10, min_periods=max(1, 10 // 2)).quantile(0.25)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_21d_base_v088_signal(closeadj):
    result = _z((_f053_ma_fast(closeadj, 21)).ewm(span=21, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_42d_base_v089_signal(closeadj):
    result = (_mean(_f053_ma_fast(closeadj, 42), 42) - _mean(_f053_ma_fast(closeadj, 42), max(2, 42 // 2))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_63d_base_v090_signal(closeadj):
    result = _mean(_f053_ma_fast(closeadj, 63), max(2, 63 // 2)) / _mean(_f053_ma_fast(closeadj, 63), 63).replace(0, np.nan).abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_126d_base_v091_signal(closeadj):
    result = np.sign(_f053_ma_fast(closeadj, 126)) * (_f053_ma_fast(closeadj, 126)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_189d_base_v092_signal(closeadj):
    result = np.tanh(_z(_f053_ma_fast(closeadj, 189), 63)) * np.log1p(_safe_div(_f053_ma_fast(closeadj, 189), _mean(closeadj, 252)).abs()) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_252d_base_v093_signal(closeadj):
    result = _std(_f053_ma_fast(closeadj, 252), 252) / _mean(_f053_ma_fast(closeadj, 252), 252).replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_378d_base_v094_signal(closeadj):
    result = ((_f053_ma_fast(closeadj, 378)).rolling(378, min_periods=max(1, 378 // 2)).max() - (_f053_ma_fast(closeadj, 378))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_504d_base_v095_signal(closeadj):
    result = ((_f053_ma_fast(closeadj, 504)) - (_f053_ma_fast(closeadj, 504)).rolling(504, min_periods=max(1, 504 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_5d_base_v096_signal(closeadj):
    result = (_f053_ma_fast(closeadj, 5)).rolling(5, min_periods=max(2, 5 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_10d_base_v097_signal(closeadj):
    result = (_f053_ma_fast(closeadj, 10)).diff(10).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_21d_base_v098_signal(closeadj):
    result = (_f053_ma_fast(closeadj, 21)).ewm(span=21, adjust=False).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_42d_base_v099_signal(closeadj):
    result = (((_f053_ma_fast(closeadj, 42)).pct_change().fillna(0)).abs() * closeadj).rolling(42, min_periods=max(1, 42 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_63d_base_v100_signal(closeadj):
    result = ((_f053_ma_fast(closeadj, 63)).ewm(span=63, adjust=False).mean() - (_f053_ma_fast(closeadj, 63)).ewm(span=max(2, 63 // 4), adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_5d_base_v101_signal(closeadj):
    result = _z(_f053_ma_alignment(closeadj, 5), 5) * _z(_f053_ma_alignment(closeadj, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_10d_base_v102_signal(closeadj):
    result = _mean(_f053_ma_alignment(closeadj, 10), 10) * _std(_f053_ma_alignment(closeadj, 10), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_21d_base_v103_signal(closeadj):
    result = _mean(_f053_ma_alignment(closeadj, 21), 21) / _std(_f053_ma_alignment(closeadj, 21), 21).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_42d_base_v104_signal(closeadj):
    result = ((_f053_ma_alignment(closeadj, 42)).ewm(span=42, adjust=False).mean() - _mean(_f053_ma_alignment(closeadj, 42), 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_63d_base_v105_signal(closeadj):
    result = ((_f053_ma_alignment(closeadj, 63)).rolling(63, min_periods=max(1, 63 // 2)).max() - (_f053_ma_alignment(closeadj, 63)).rolling(63, min_periods=max(1, 63 // 2)).min()) * closeadj / _mean(closeadj.abs() + 1e-9, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_126d_base_v106_signal(closeadj):
    result = _mean((_f053_ma_alignment(closeadj, 126)).abs(), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_189d_base_v107_signal(closeadj):
    result = _std((_f053_ma_alignment(closeadj, 189)).abs(), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_252d_base_v108_signal(closeadj):
    result = (_f053_ma_alignment(closeadj, 252)).diff(max(1, 252 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_378d_base_v109_signal(closeadj):
    result = ((1.0 + (_f053_ma_alignment(closeadj, 378)).pct_change().fillna(0)).rolling(378, min_periods=max(1, 378 // 2)).apply(np.prod, raw=True) - 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_504d_base_v110_signal(closeadj):
    result = (_f053_ma_alignment(closeadj, 504)).rolling(504, min_periods=max(1, 504 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_5d_base_v111_signal(closeadj):
    result = ((_f053_ma_alignment(closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).median() - _mean(_f053_ma_alignment(closeadj, 5), 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_10d_base_v112_signal(closeadj):
    result = ((_f053_ma_alignment(closeadj, 10)).rolling(10, min_periods=max(1, 10 // 2)).quantile(0.75) - (_f053_ma_alignment(closeadj, 10)).rolling(10, min_periods=max(1, 10 // 2)).quantile(0.25)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_21d_base_v113_signal(closeadj):
    result = _z((_f053_ma_alignment(closeadj, 21)).ewm(span=21, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_42d_base_v114_signal(closeadj):
    result = (_mean(_f053_ma_alignment(closeadj, 42), 42) - _mean(_f053_ma_alignment(closeadj, 42), max(2, 42 // 2))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_63d_base_v115_signal(closeadj):
    result = _mean(_f053_ma_alignment(closeadj, 63), max(2, 63 // 2)) / _mean(_f053_ma_alignment(closeadj, 63), 63).replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_126d_base_v116_signal(closeadj):
    result = np.sign(_f053_ma_alignment(closeadj, 126)) * (_f053_ma_alignment(closeadj, 126)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_189d_base_v117_signal(closeadj):
    result = np.sign(_f053_ma_alignment(closeadj, 189)) * np.log1p((_f053_ma_alignment(closeadj, 189)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_252d_base_v118_signal(closeadj):
    result = _std(_f053_ma_alignment(closeadj, 252), 252) / _mean(_f053_ma_alignment(closeadj, 252), 252).replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_378d_base_v119_signal(closeadj):
    result = ((_f053_ma_alignment(closeadj, 378)).rolling(378, min_periods=max(1, 378 // 2)).max() - (_f053_ma_alignment(closeadj, 378))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_504d_base_v120_signal(closeadj):
    result = ((_f053_ma_alignment(closeadj, 504)) - (_f053_ma_alignment(closeadj, 504)).rolling(504, min_periods=max(1, 504 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_5d_base_v121_signal(closeadj):
    result = (_f053_ma_alignment(closeadj, 5)).rolling(5, min_periods=max(2, 5 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_10d_base_v122_signal(closeadj):
    result = (_f053_ma_alignment(closeadj, 10)).diff(10).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_21d_base_v123_signal(closeadj):
    result = (_f053_ma_alignment(closeadj, 21)).ewm(span=21, adjust=False).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_42d_base_v124_signal(closeadj):
    result = (((_f053_ma_alignment(closeadj, 42)).pct_change().fillna(0)).abs() * closeadj).rolling(42, min_periods=max(1, 42 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_63d_base_v125_signal(closeadj):
    result = ((_f053_ma_alignment(closeadj, 63)).ewm(span=63, adjust=False).mean() - (_f053_ma_alignment(closeadj, 63)).ewm(span=max(2, 63 // 4), adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_5d_base_v126_signal(closeadj):
    result = _z(_f053_stacking_score(closeadj, 5), 5) * _z(_f053_stacking_score(closeadj, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_10d_base_v127_signal(closeadj):
    result = _mean(_f053_stacking_score(closeadj, 10), 10) * _std(_f053_stacking_score(closeadj, 10), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_21d_base_v128_signal(closeadj):
    result = _mean(_f053_stacking_score(closeadj, 21), 21) / _std(_f053_stacking_score(closeadj, 21), 21).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_42d_base_v129_signal(closeadj):
    result = ((_f053_stacking_score(closeadj, 42)).ewm(span=42, adjust=False).mean() - _mean(_f053_stacking_score(closeadj, 42), 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_63d_base_v130_signal(closeadj):
    result = ((_f053_stacking_score(closeadj, 63)).rolling(63, min_periods=max(1, 63 // 2)).max() - (_f053_stacking_score(closeadj, 63)).rolling(63, min_periods=max(1, 63 // 2)).min()) * closeadj / _mean(closeadj.abs() + 1e-9, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_126d_base_v131_signal(closeadj):
    result = _mean((_f053_stacking_score(closeadj, 126)).abs(), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_189d_base_v132_signal(closeadj):
    result = _std((_f053_stacking_score(closeadj, 189)).abs(), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_252d_base_v133_signal(closeadj):
    result = (_f053_stacking_score(closeadj, 252)).diff(max(1, 252 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_378d_base_v134_signal(closeadj):
    result = ((1.0 + (_f053_stacking_score(closeadj, 378)).pct_change().fillna(0)).rolling(378, min_periods=max(1, 378 // 2)).apply(np.prod, raw=True) - 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_504d_base_v135_signal(closeadj):
    result = (_f053_stacking_score(closeadj, 504)).rolling(504, min_periods=max(1, 504 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_5d_base_v136_signal(closeadj):
    result = ((_f053_stacking_score(closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).median() - _mean(_f053_stacking_score(closeadj, 5), 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_10d_base_v137_signal(closeadj):
    result = ((_f053_stacking_score(closeadj, 10)).rolling(10, min_periods=max(1, 10 // 2)).quantile(0.75) - (_f053_stacking_score(closeadj, 10)).rolling(10, min_periods=max(1, 10 // 2)).quantile(0.25)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_21d_base_v138_signal(closeadj):
    result = _z((_f053_stacking_score(closeadj, 21)).ewm(span=21, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_42d_base_v139_signal(closeadj):
    result = (_mean(_f053_stacking_score(closeadj, 42), 42) - _mean(_f053_stacking_score(closeadj, 42), max(2, 42 // 2))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_63d_base_v140_signal(closeadj):
    result = _mean(_f053_stacking_score(closeadj, 63), max(2, 63 // 2)) / _mean(_f053_stacking_score(closeadj, 63), 63).replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_126d_base_v141_signal(closeadj):
    result = np.sign(_f053_stacking_score(closeadj, 126)) * (_f053_stacking_score(closeadj, 126)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_189d_base_v142_signal(closeadj):
    result = np.sign(_f053_stacking_score(closeadj, 189)) * np.log1p((_f053_stacking_score(closeadj, 189)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_252d_base_v143_signal(closeadj):
    result = _std(_f053_stacking_score(closeadj, 252), 252) / _mean(_f053_stacking_score(closeadj, 252), 252).replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_378d_base_v144_signal(closeadj):
    result = ((_f053_stacking_score(closeadj, 378)).rolling(378, min_periods=max(1, 378 // 2)).max() - (_f053_stacking_score(closeadj, 378))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_504d_base_v145_signal(closeadj):
    result = ((_f053_stacking_score(closeadj, 504)) - (_f053_stacking_score(closeadj, 504)).rolling(504, min_periods=max(1, 504 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_5d_base_v146_signal(closeadj):
    result = (_f053_stacking_score(closeadj, 5)).rolling(5, min_periods=max(2, 5 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_10d_base_v147_signal(closeadj):
    result = (_f053_stacking_score(closeadj, 10)).diff(10).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_21d_base_v148_signal(closeadj):
    result = (_f053_stacking_score(closeadj, 21)).ewm(span=21, adjust=False).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_42d_base_v149_signal(closeadj):
    result = (((_f053_stacking_score(closeadj, 42)).pct_change().fillna(0)).abs() * closeadj).rolling(42, min_periods=max(1, 42 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_63d_base_v150_signal(closeadj):
    result = ((_f053_stacking_score(closeadj, 63)).ewm(span=63, adjust=False).mean() - (_f053_stacking_score(closeadj, 63)).ewm(span=max(2, 63 // 4), adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f053mas_f053_ma_alignment_stacking_ma_fast_5d_base_v076_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_10d_base_v077_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_21d_base_v078_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_42d_base_v079_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_63d_base_v080_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_126d_base_v081_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_189d_base_v082_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_252d_base_v083_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_378d_base_v084_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_504d_base_v085_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_5d_base_v086_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_10d_base_v087_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_21d_base_v088_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_42d_base_v089_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_63d_base_v090_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_126d_base_v091_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_189d_base_v092_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_252d_base_v093_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_378d_base_v094_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_504d_base_v095_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_5d_base_v096_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_10d_base_v097_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_21d_base_v098_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_42d_base_v099_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_63d_base_v100_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_5d_base_v101_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_10d_base_v102_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_21d_base_v103_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_42d_base_v104_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_63d_base_v105_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_126d_base_v106_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_189d_base_v107_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_252d_base_v108_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_378d_base_v109_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_504d_base_v110_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_5d_base_v111_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_10d_base_v112_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_21d_base_v113_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_42d_base_v114_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_63d_base_v115_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_126d_base_v116_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_189d_base_v117_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_252d_base_v118_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_378d_base_v119_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_504d_base_v120_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_5d_base_v121_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_10d_base_v122_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_21d_base_v123_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_42d_base_v124_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_63d_base_v125_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_5d_base_v126_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_10d_base_v127_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_21d_base_v128_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_42d_base_v129_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_63d_base_v130_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_126d_base_v131_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_189d_base_v132_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_252d_base_v133_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_378d_base_v134_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_504d_base_v135_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_5d_base_v136_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_10d_base_v137_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_21d_base_v138_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_42d_base_v139_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_63d_base_v140_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_126d_base_v141_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_189d_base_v142_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_252d_base_v143_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_378d_base_v144_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_504d_base_v145_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_5d_base_v146_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_10d_base_v147_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_21d_base_v148_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_42d_base_v149_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F053_MA_ALIGNMENT_STACKING_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    cols = {"closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f053_ma_fast', '_f053_ma_alignment', '_f053_stacking_score')
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f053_ma_alignment_stacking_base_076_150_claude: {n_features} features pass")
