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


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f088_disthigh(close, w):
    hi = close.rolling(w, min_periods=max(1, w//2)).max()
    return (close - hi) / hi.replace(0, np.nan).abs()


# 63d z-score of disthigh_252d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_z_63d_base_v076_signal(closeadj):
    base = _f088_disthigh(closeadj, 252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of disthigh_252d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_z_126d_base_v077_signal(closeadj):
    base = _f088_disthigh(closeadj, 252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of disthigh_252d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_z_252d_base_v078_signal(closeadj):
    base = _f088_disthigh(closeadj, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of disthigh_252d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_z_504d_base_v079_signal(closeadj):
    base = _f088_disthigh(closeadj, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of disthigh_504d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_z_63d_base_v080_signal(closeadj):
    base = _f088_disthigh(closeadj, 504)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of disthigh_504d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_z_126d_base_v081_signal(closeadj):
    base = _f088_disthigh(closeadj, 504)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of disthigh_504d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_z_252d_base_v082_signal(closeadj):
    base = _f088_disthigh(closeadj, 504)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of disthigh_504d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_z_504d_base_v083_signal(closeadj):
    base = _f088_disthigh(closeadj, 504)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of disthigh_756d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_z_63d_base_v084_signal(closeadj):
    base = _f088_disthigh(closeadj, 756)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of disthigh_756d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_z_126d_base_v085_signal(closeadj):
    base = _f088_disthigh(closeadj, 756)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of disthigh_756d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_z_252d_base_v086_signal(closeadj):
    base = _f088_disthigh(closeadj, 756)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of disthigh_756d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_z_504d_base_v087_signal(closeadj):
    base = _f088_disthigh(closeadj, 756)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of disthigh_1260d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_z_63d_base_v088_signal(closeadj):
    base = _f088_disthigh(closeadj, 1260)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of disthigh_1260d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_z_126d_base_v089_signal(closeadj):
    base = _f088_disthigh(closeadj, 1260)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of disthigh_1260d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_z_252d_base_v090_signal(closeadj):
    base = _f088_disthigh(closeadj, 1260)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of disthigh_1260d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_z_504d_base_v091_signal(closeadj):
    base = _f088_disthigh(closeadj, 1260)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of new_high_252_flag
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_z_63d_base_v092_signal(closeadj):
    base = (closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of new_high_252_flag
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_z_126d_base_v093_signal(closeadj):
    base = (closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of new_high_252_flag
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_z_252d_base_v094_signal(closeadj):
    base = (closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of new_high_252_flag
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_z_504d_base_v095_signal(closeadj):
    base = (closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of high_pctile_504
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_z_63d_base_v096_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of high_pctile_504
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_z_126d_base_v097_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of high_pctile_504
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_z_252d_base_v098_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of high_pctile_504
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_z_504d_base_v099_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of days_since_252high
def f088hi_f088_ohlcv_multi_year_highs_days_since_252high_z_63d_base_v100_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmax(), raw=False))
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of days_since_252high
def f088hi_f088_ohlcv_multi_year_highs_days_since_252high_z_126d_base_v101_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmax(), raw=False))
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of days_since_252high
def f088hi_f088_ohlcv_multi_year_highs_days_since_252high_z_252d_base_v102_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmax(), raw=False))
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of days_since_252high
def f088hi_f088_ohlcv_multi_year_highs_days_since_252high_z_504d_base_v103_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmax(), raw=False))
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of disthigh_252d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_distmax_252d_base_v104_signal(closeadj):
    base = _f088_disthigh(closeadj, 252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of disthigh_252d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_distmax_504d_base_v105_signal(closeadj):
    base = _f088_disthigh(closeadj, 252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of disthigh_504d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_distmax_252d_base_v106_signal(closeadj):
    base = _f088_disthigh(closeadj, 504)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of disthigh_504d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_distmax_504d_base_v107_signal(closeadj):
    base = _f088_disthigh(closeadj, 504)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of disthigh_756d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_distmax_252d_base_v108_signal(closeadj):
    base = _f088_disthigh(closeadj, 756)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of disthigh_756d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_distmax_504d_base_v109_signal(closeadj):
    base = _f088_disthigh(closeadj, 756)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of disthigh_1260d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_distmax_252d_base_v110_signal(closeadj):
    base = _f088_disthigh(closeadj, 1260)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of disthigh_1260d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_distmax_504d_base_v111_signal(closeadj):
    base = _f088_disthigh(closeadj, 1260)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of new_high_252_flag
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_distmax_252d_base_v112_signal(closeadj):
    base = (closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of new_high_252_flag
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_distmax_504d_base_v113_signal(closeadj):
    base = (closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of high_pctile_504
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_distmax_252d_base_v114_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of high_pctile_504
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_distmax_504d_base_v115_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of days_since_252high
def f088hi_f088_ohlcv_multi_year_highs_days_since_252high_distmax_252d_base_v116_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmax(), raw=False))
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of days_since_252high
def f088hi_f088_ohlcv_multi_year_highs_days_since_252high_distmax_504d_base_v117_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmax(), raw=False))
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of disthigh_252d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_distmed_126d_base_v118_signal(closeadj):
    base = _f088_disthigh(closeadj, 252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of disthigh_252d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_distmed_252d_base_v119_signal(closeadj):
    base = _f088_disthigh(closeadj, 252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of disthigh_252d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_distmed_504d_base_v120_signal(closeadj):
    base = _f088_disthigh(closeadj, 252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of disthigh_504d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_distmed_126d_base_v121_signal(closeadj):
    base = _f088_disthigh(closeadj, 504)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of disthigh_504d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_distmed_252d_base_v122_signal(closeadj):
    base = _f088_disthigh(closeadj, 504)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of disthigh_504d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_distmed_504d_base_v123_signal(closeadj):
    base = _f088_disthigh(closeadj, 504)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of disthigh_756d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_distmed_126d_base_v124_signal(closeadj):
    base = _f088_disthigh(closeadj, 756)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of disthigh_756d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_distmed_252d_base_v125_signal(closeadj):
    base = _f088_disthigh(closeadj, 756)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of disthigh_756d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_distmed_504d_base_v126_signal(closeadj):
    base = _f088_disthigh(closeadj, 756)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of disthigh_1260d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_distmed_126d_base_v127_signal(closeadj):
    base = _f088_disthigh(closeadj, 1260)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of disthigh_1260d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_distmed_252d_base_v128_signal(closeadj):
    base = _f088_disthigh(closeadj, 1260)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of disthigh_1260d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_distmed_504d_base_v129_signal(closeadj):
    base = _f088_disthigh(closeadj, 1260)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of new_high_252_flag
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_distmed_126d_base_v130_signal(closeadj):
    base = (closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of new_high_252_flag
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_distmed_252d_base_v131_signal(closeadj):
    base = (closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of new_high_252_flag
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_distmed_504d_base_v132_signal(closeadj):
    base = (closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of high_pctile_504
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_distmed_126d_base_v133_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of high_pctile_504
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_distmed_252d_base_v134_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of high_pctile_504
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_distmed_504d_base_v135_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of days_since_252high
def f088hi_f088_ohlcv_multi_year_highs_days_since_252high_distmed_126d_base_v136_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmax(), raw=False))
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of days_since_252high
def f088hi_f088_ohlcv_multi_year_highs_days_since_252high_distmed_252d_base_v137_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmax(), raw=False))
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of days_since_252high
def f088hi_f088_ohlcv_multi_year_highs_days_since_252high_distmed_504d_base_v138_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmax(), raw=False))
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in disthigh_252d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_chg_63d_base_v139_signal(closeadj):
    base = _f088_disthigh(closeadj, 252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in disthigh_252d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_chg_252d_base_v140_signal(closeadj):
    base = _f088_disthigh(closeadj, 252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in disthigh_504d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_chg_63d_base_v141_signal(closeadj):
    base = _f088_disthigh(closeadj, 504)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in disthigh_504d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_chg_252d_base_v142_signal(closeadj):
    base = _f088_disthigh(closeadj, 504)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in disthigh_756d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_chg_63d_base_v143_signal(closeadj):
    base = _f088_disthigh(closeadj, 756)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in disthigh_756d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_chg_252d_base_v144_signal(closeadj):
    base = _f088_disthigh(closeadj, 756)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in disthigh_1260d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_chg_63d_base_v145_signal(closeadj):
    base = _f088_disthigh(closeadj, 1260)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in disthigh_1260d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_chg_252d_base_v146_signal(closeadj):
    base = _f088_disthigh(closeadj, 1260)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in new_high_252_flag
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_chg_63d_base_v147_signal(closeadj):
    base = (closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in new_high_252_flag
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_chg_252d_base_v148_signal(closeadj):
    base = (closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in high_pctile_504
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_chg_63d_base_v149_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in high_pctile_504
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_chg_252d_base_v150_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

