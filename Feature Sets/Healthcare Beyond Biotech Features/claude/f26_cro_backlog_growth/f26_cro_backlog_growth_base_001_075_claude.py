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
def _f26_backlog_growth(deferredrev, w):
    return deferredrev.pct_change(periods=w)


def _f26_backlog_to_revenue(deferredrev, revenue):
    return deferredrev / revenue.replace(0, np.nan)


def _f26_backlog_acceleration(deferredrev, w):
    g1 = deferredrev.pct_change(periods=w)
    g2 = deferredrev.pct_change(periods=w).shift(w)
    return g1 - g2


# 5d backlog growth x close
def f26cbg_f26_cro_backlog_growth_backloggrowth_5d_base_v001_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 5)
    result = g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 10d backlog growth x close
def f26cbg_f26_cro_backlog_growth_backloggrowth_10d_base_v002_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 10)
    result = g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d backlog growth x close
def f26cbg_f26_cro_backlog_growth_backloggrowth_21d_base_v003_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 21)
    result = g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 42d backlog growth x close
def f26cbg_f26_cro_backlog_growth_backloggrowth_42d_base_v004_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 42)
    result = g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d backlog growth x close
def f26cbg_f26_cro_backlog_growth_backloggrowth_63d_base_v005_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 63)
    result = g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d backlog growth x close
def f26cbg_f26_cro_backlog_growth_backloggrowth_126d_base_v006_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 126)
    result = g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 189d backlog growth x close
def f26cbg_f26_cro_backlog_growth_backloggrowth_189d_base_v007_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 189)
    result = g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d backlog growth x close
def f26cbg_f26_cro_backlog_growth_backloggrowth_252d_base_v008_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 252)
    result = g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 378d backlog growth x close
def f26cbg_f26_cro_backlog_growth_backloggrowth_378d_base_v009_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 378)
    result = g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d backlog growth x close
def f26cbg_f26_cro_backlog_growth_backloggrowth_504d_base_v010_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 504)
    result = g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 5d backlog-to-revenue x close
def f26cbg_f26_cro_backlog_growth_blgtorev_5d_base_v011_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    result = br.rolling(5, min_periods=max(1, 5 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 10d backlog-to-revenue x close
def f26cbg_f26_cro_backlog_growth_blgtorev_10d_base_v012_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    result = br.rolling(10, min_periods=max(1, 10 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d backlog-to-revenue x close
def f26cbg_f26_cro_backlog_growth_blgtorev_21d_base_v013_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    result = br.rolling(21, min_periods=max(1, 21 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 42d backlog-to-revenue x close
def f26cbg_f26_cro_backlog_growth_blgtorev_42d_base_v014_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    result = br.rolling(42, min_periods=max(1, 42 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d backlog-to-revenue x close
def f26cbg_f26_cro_backlog_growth_blgtorev_63d_base_v015_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    result = br.rolling(63, min_periods=max(1, 63 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d backlog-to-revenue x close
def f26cbg_f26_cro_backlog_growth_blgtorev_126d_base_v016_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    result = br.rolling(126, min_periods=max(1, 126 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 189d backlog-to-revenue x close
def f26cbg_f26_cro_backlog_growth_blgtorev_189d_base_v017_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    result = br.rolling(189, min_periods=max(1, 189 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d backlog-to-revenue x close
def f26cbg_f26_cro_backlog_growth_blgtorev_252d_base_v018_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    result = br.rolling(252, min_periods=max(1, 252 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 378d backlog-to-revenue x close
def f26cbg_f26_cro_backlog_growth_blgtorev_378d_base_v019_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    result = br.rolling(378, min_periods=max(1, 378 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d backlog-to-revenue x close
def f26cbg_f26_cro_backlog_growth_blgtorev_504d_base_v020_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    result = br.rolling(504, min_periods=max(1, 504 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 5d backlog acceleration x close
def f26cbg_f26_cro_backlog_growth_blgaccel_5d_base_v021_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 5)
    result = a * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 10d backlog acceleration x close
def f26cbg_f26_cro_backlog_growth_blgaccel_10d_base_v022_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 10)
    result = a * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d backlog acceleration x close
def f26cbg_f26_cro_backlog_growth_blgaccel_21d_base_v023_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 21)
    result = a * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 42d backlog acceleration x close
def f26cbg_f26_cro_backlog_growth_blgaccel_42d_base_v024_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 42)
    result = a * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d backlog acceleration x close
def f26cbg_f26_cro_backlog_growth_blgaccel_63d_base_v025_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 63)
    result = a * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d backlog acceleration x close
def f26cbg_f26_cro_backlog_growth_blgaccel_126d_base_v026_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 126)
    result = a * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 189d backlog acceleration x close
def f26cbg_f26_cro_backlog_growth_blgaccel_189d_base_v027_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 189)
    result = a * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d backlog acceleration x close
def f26cbg_f26_cro_backlog_growth_blgaccel_252d_base_v028_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 252)
    result = a * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 378d backlog acceleration x close
def f26cbg_f26_cro_backlog_growth_blgaccel_378d_base_v029_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 378)
    result = a * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d backlog acceleration x close
def f26cbg_f26_cro_backlog_growth_blgaccel_504d_base_v030_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 504)
    result = a * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 5d backlog growth zscore x close
def f26cbg_f26_cro_backlog_growth_blggrowthz_5d_base_v031_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 5)
    result = _z(g, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 10d backlog growth zscore x close
def f26cbg_f26_cro_backlog_growth_blggrowthz_10d_base_v032_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 10)
    result = _z(g, 20) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d backlog growth zscore x close
def f26cbg_f26_cro_backlog_growth_blggrowthz_21d_base_v033_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 21)
    result = _z(g, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 42d backlog growth zscore x close
def f26cbg_f26_cro_backlog_growth_blggrowthz_42d_base_v034_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 42)
    result = _z(g, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d backlog growth zscore x close
def f26cbg_f26_cro_backlog_growth_blggrowthz_63d_base_v035_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 63)
    result = _z(g, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d backlog growth zscore x close
def f26cbg_f26_cro_backlog_growth_blggrowthz_126d_base_v036_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 126)
    result = _z(g, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 189d backlog growth zscore x close
def f26cbg_f26_cro_backlog_growth_blggrowthz_189d_base_v037_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 189)
    result = _z(g, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d backlog growth zscore x close
def f26cbg_f26_cro_backlog_growth_blggrowthz_252d_base_v038_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 252)
    result = _z(g, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 378d backlog growth zscore x close
def f26cbg_f26_cro_backlog_growth_blggrowthz_378d_base_v039_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 378)
    result = _z(g, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d backlog growth zscore x close
def f26cbg_f26_cro_backlog_growth_blggrowthz_504d_base_v040_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 504)
    result = _z(g, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 5d backlog/rev zscore x close
def f26cbg_f26_cro_backlog_growth_blgtorevz_5d_base_v041_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    result = _z(br, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 10d backlog/rev zscore x close
def f26cbg_f26_cro_backlog_growth_blgtorevz_10d_base_v042_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    result = _z(br, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d backlog/rev zscore x close
def f26cbg_f26_cro_backlog_growth_blgtorevz_21d_base_v043_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    result = _z(br, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 42d backlog/rev zscore x close
def f26cbg_f26_cro_backlog_growth_blgtorevz_42d_base_v044_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    result = _z(br, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d backlog/rev zscore x close
def f26cbg_f26_cro_backlog_growth_blgtorevz_63d_base_v045_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    result = _z(br, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d backlog/rev zscore x close
def f26cbg_f26_cro_backlog_growth_blgtorevz_126d_base_v046_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    result = _z(br, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 189d backlog/rev zscore x close
def f26cbg_f26_cro_backlog_growth_blgtorevz_189d_base_v047_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    result = _z(br, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d backlog/rev zscore x close
def f26cbg_f26_cro_backlog_growth_blgtorevz_252d_base_v048_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    result = _z(br, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 378d backlog/rev zscore x close
def f26cbg_f26_cro_backlog_growth_blgtorevz_378d_base_v049_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    result = _z(br, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d backlog/rev zscore x close
def f26cbg_f26_cro_backlog_growth_blgtorevz_504d_base_v050_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    result = _z(br, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 5d backlog growth x revenue mean
def f26cbg_f26_cro_backlog_growth_blggrowthxrev_5d_base_v051_signal(deferredrev, revenue):
    g = _f26_backlog_growth(deferredrev, 5)
    rm = revenue.rolling(5, min_periods=max(1, 5 // 2)).mean()
    result = g * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 10d backlog growth x revenue mean
def f26cbg_f26_cro_backlog_growth_blggrowthxrev_10d_base_v052_signal(deferredrev, revenue):
    g = _f26_backlog_growth(deferredrev, 10)
    rm = revenue.rolling(10, min_periods=max(1, 10 // 2)).mean()
    result = g * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 21d backlog growth x revenue mean
def f26cbg_f26_cro_backlog_growth_blggrowthxrev_21d_base_v053_signal(deferredrev, revenue):
    g = _f26_backlog_growth(deferredrev, 21)
    rm = revenue.rolling(21, min_periods=max(1, 21 // 2)).mean()
    result = g * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 42d backlog growth x revenue mean
def f26cbg_f26_cro_backlog_growth_blggrowthxrev_42d_base_v054_signal(deferredrev, revenue):
    g = _f26_backlog_growth(deferredrev, 42)
    rm = revenue.rolling(42, min_periods=max(1, 42 // 2)).mean()
    result = g * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 63d backlog growth x revenue mean
def f26cbg_f26_cro_backlog_growth_blggrowthxrev_63d_base_v055_signal(deferredrev, revenue):
    g = _f26_backlog_growth(deferredrev, 63)
    rm = revenue.rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = g * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 126d backlog growth x revenue mean
def f26cbg_f26_cro_backlog_growth_blggrowthxrev_126d_base_v056_signal(deferredrev, revenue):
    g = _f26_backlog_growth(deferredrev, 126)
    rm = revenue.rolling(126, min_periods=max(1, 126 // 2)).mean()
    result = g * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 189d backlog growth x revenue mean
def f26cbg_f26_cro_backlog_growth_blggrowthxrev_189d_base_v057_signal(deferredrev, revenue):
    g = _f26_backlog_growth(deferredrev, 189)
    rm = revenue.rolling(189, min_periods=max(1, 189 // 2)).mean()
    result = g * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 252d backlog growth x revenue mean
def f26cbg_f26_cro_backlog_growth_blggrowthxrev_252d_base_v058_signal(deferredrev, revenue):
    g = _f26_backlog_growth(deferredrev, 252)
    rm = revenue.rolling(252, min_periods=max(1, 252 // 2)).mean()
    result = g * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 378d backlog growth x revenue mean
def f26cbg_f26_cro_backlog_growth_blggrowthxrev_378d_base_v059_signal(deferredrev, revenue):
    g = _f26_backlog_growth(deferredrev, 378)
    rm = revenue.rolling(378, min_periods=max(1, 378 // 2)).mean()
    result = g * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 504d backlog growth x revenue mean
def f26cbg_f26_cro_backlog_growth_blggrowthxrev_504d_base_v060_signal(deferredrev, revenue):
    g = _f26_backlog_growth(deferredrev, 504)
    rm = revenue.rolling(504, min_periods=max(1, 504 // 2)).mean()
    result = g * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 5d backlog accel x revenue mean
def f26cbg_f26_cro_backlog_growth_blgaccelxrev_5d_base_v061_signal(deferredrev, revenue):
    a = _f26_backlog_acceleration(deferredrev, 5)
    rm = revenue.rolling(5, min_periods=max(1, 5 // 2)).mean()
    result = a * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 10d backlog accel x revenue mean
def f26cbg_f26_cro_backlog_growth_blgaccelxrev_10d_base_v062_signal(deferredrev, revenue):
    a = _f26_backlog_acceleration(deferredrev, 10)
    rm = revenue.rolling(10, min_periods=max(1, 10 // 2)).mean()
    result = a * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 21d backlog accel x revenue mean
def f26cbg_f26_cro_backlog_growth_blgaccelxrev_21d_base_v063_signal(deferredrev, revenue):
    a = _f26_backlog_acceleration(deferredrev, 21)
    rm = revenue.rolling(21, min_periods=max(1, 21 // 2)).mean()
    result = a * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 42d backlog accel x revenue mean
def f26cbg_f26_cro_backlog_growth_blgaccelxrev_42d_base_v064_signal(deferredrev, revenue):
    a = _f26_backlog_acceleration(deferredrev, 42)
    rm = revenue.rolling(42, min_periods=max(1, 42 // 2)).mean()
    result = a * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 63d backlog accel x revenue mean
def f26cbg_f26_cro_backlog_growth_blgaccelxrev_63d_base_v065_signal(deferredrev, revenue):
    a = _f26_backlog_acceleration(deferredrev, 63)
    rm = revenue.rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = a * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 5d backlog/rev std x close
def f26cbg_f26_cro_backlog_growth_blgtorevstd_5d_base_v066_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    result = br.rolling(5, min_periods=max(1, 5 // 2)).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 10d backlog/rev std x close
def f26cbg_f26_cro_backlog_growth_blgtorevstd_10d_base_v067_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    result = br.rolling(10, min_periods=max(1, 10 // 2)).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d backlog/rev std x close
def f26cbg_f26_cro_backlog_growth_blgtorevstd_21d_base_v068_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    result = br.rolling(21, min_periods=max(1, 21 // 2)).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 42d backlog/rev std x close
def f26cbg_f26_cro_backlog_growth_blgtorevstd_42d_base_v069_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    result = br.rolling(42, min_periods=max(1, 42 // 2)).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d backlog/rev std x close
def f26cbg_f26_cro_backlog_growth_blgtorevstd_63d_base_v070_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    result = br.rolling(63, min_periods=max(1, 63 // 2)).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 5d backlog growth std x close
def f26cbg_f26_cro_backlog_growth_blggrowthstd_5d_base_v071_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 5)
    result = g.rolling(5, min_periods=max(1, 5 // 2)).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 10d backlog growth std x close
def f26cbg_f26_cro_backlog_growth_blggrowthstd_10d_base_v072_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 10)
    result = g.rolling(10, min_periods=max(1, 10 // 2)).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d backlog growth std x close
def f26cbg_f26_cro_backlog_growth_blggrowthstd_21d_base_v073_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 21)
    result = g.rolling(21, min_periods=max(1, 21 // 2)).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 42d backlog growth std x close
def f26cbg_f26_cro_backlog_growth_blggrowthstd_42d_base_v074_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 42)
    result = g.rolling(42, min_periods=max(1, 42 // 2)).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d backlog growth std x close
def f26cbg_f26_cro_backlog_growth_blggrowthstd_63d_base_v075_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 63)
    result = g.rolling(63, min_periods=max(1, 63 // 2)).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f26cbg_f26_cro_backlog_growth_backloggrowth_5d_base_v001_signal,
    f26cbg_f26_cro_backlog_growth_backloggrowth_10d_base_v002_signal,
    f26cbg_f26_cro_backlog_growth_backloggrowth_21d_base_v003_signal,
    f26cbg_f26_cro_backlog_growth_backloggrowth_42d_base_v004_signal,
    f26cbg_f26_cro_backlog_growth_backloggrowth_63d_base_v005_signal,
    f26cbg_f26_cro_backlog_growth_backloggrowth_126d_base_v006_signal,
    f26cbg_f26_cro_backlog_growth_backloggrowth_189d_base_v007_signal,
    f26cbg_f26_cro_backlog_growth_backloggrowth_252d_base_v008_signal,
    f26cbg_f26_cro_backlog_growth_backloggrowth_378d_base_v009_signal,
    f26cbg_f26_cro_backlog_growth_backloggrowth_504d_base_v010_signal,
    f26cbg_f26_cro_backlog_growth_blgtorev_5d_base_v011_signal,
    f26cbg_f26_cro_backlog_growth_blgtorev_10d_base_v012_signal,
    f26cbg_f26_cro_backlog_growth_blgtorev_21d_base_v013_signal,
    f26cbg_f26_cro_backlog_growth_blgtorev_42d_base_v014_signal,
    f26cbg_f26_cro_backlog_growth_blgtorev_63d_base_v015_signal,
    f26cbg_f26_cro_backlog_growth_blgtorev_126d_base_v016_signal,
    f26cbg_f26_cro_backlog_growth_blgtorev_189d_base_v017_signal,
    f26cbg_f26_cro_backlog_growth_blgtorev_252d_base_v018_signal,
    f26cbg_f26_cro_backlog_growth_blgtorev_378d_base_v019_signal,
    f26cbg_f26_cro_backlog_growth_blgtorev_504d_base_v020_signal,
    f26cbg_f26_cro_backlog_growth_blgaccel_5d_base_v021_signal,
    f26cbg_f26_cro_backlog_growth_blgaccel_10d_base_v022_signal,
    f26cbg_f26_cro_backlog_growth_blgaccel_21d_base_v023_signal,
    f26cbg_f26_cro_backlog_growth_blgaccel_42d_base_v024_signal,
    f26cbg_f26_cro_backlog_growth_blgaccel_63d_base_v025_signal,
    f26cbg_f26_cro_backlog_growth_blgaccel_126d_base_v026_signal,
    f26cbg_f26_cro_backlog_growth_blgaccel_189d_base_v027_signal,
    f26cbg_f26_cro_backlog_growth_blgaccel_252d_base_v028_signal,
    f26cbg_f26_cro_backlog_growth_blgaccel_378d_base_v029_signal,
    f26cbg_f26_cro_backlog_growth_blgaccel_504d_base_v030_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthz_5d_base_v031_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthz_10d_base_v032_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthz_21d_base_v033_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthz_42d_base_v034_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthz_63d_base_v035_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthz_126d_base_v036_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthz_189d_base_v037_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthz_252d_base_v038_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthz_378d_base_v039_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthz_504d_base_v040_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevz_5d_base_v041_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevz_10d_base_v042_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevz_21d_base_v043_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevz_42d_base_v044_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevz_63d_base_v045_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevz_126d_base_v046_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevz_189d_base_v047_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevz_252d_base_v048_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevz_378d_base_v049_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevz_504d_base_v050_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxrev_5d_base_v051_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxrev_10d_base_v052_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxrev_21d_base_v053_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxrev_42d_base_v054_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxrev_63d_base_v055_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxrev_126d_base_v056_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxrev_189d_base_v057_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxrev_252d_base_v058_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxrev_378d_base_v059_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxrev_504d_base_v060_signal,
    f26cbg_f26_cro_backlog_growth_blgaccelxrev_5d_base_v061_signal,
    f26cbg_f26_cro_backlog_growth_blgaccelxrev_10d_base_v062_signal,
    f26cbg_f26_cro_backlog_growth_blgaccelxrev_21d_base_v063_signal,
    f26cbg_f26_cro_backlog_growth_blgaccelxrev_42d_base_v064_signal,
    f26cbg_f26_cro_backlog_growth_blgaccelxrev_63d_base_v065_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevstd_5d_base_v066_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevstd_10d_base_v067_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevstd_21d_base_v068_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevstd_42d_base_v069_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevstd_63d_base_v070_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthstd_5d_base_v071_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthstd_10d_base_v072_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthstd_21d_base_v073_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthstd_42d_base_v074_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthstd_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F26_CRO_BACKLOG_GROWTH_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "fcf": fcf, "capex": capex,
        "deferredrev": deferredrev,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f26_backlog_growth", "_f26_backlog_to_revenue", "_f26_backlog_acceleration",)
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
    print(f"OK f26_cro_backlog_growth_base_001_075_claude: {n_features} features pass")
