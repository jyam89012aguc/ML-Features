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
def _f21_revenue_growth(revenue, w):
    # rolling pct-change of revenue level over w trading days
    return revenue.pct_change(periods=w)


def _f21_revenue_growth_smooth(revenue, smooth_w, growth_w):
    # smooth revenue first, then take growth
    sm = revenue.rolling(smooth_w, min_periods=max(1, smooth_w // 2)).mean()
    return sm.pct_change(periods=growth_w)


def _f21_revenue_log_growth(revenue, w):
    # log growth (1+g)
    return np.log1p(revenue.pct_change(periods=w))


# 21d revenue growth × close
def f21rg_f21_revenue_growth_revgrow_21d_base_v001_signal(revenue, closeadj):
    result = _f21_revenue_growth(revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue growth × close
def f21rg_f21_revenue_growth_revgrow_63d_base_v002_signal(revenue, closeadj):
    result = _f21_revenue_growth(revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d revenue growth × close
def f21rg_f21_revenue_growth_revgrow_126d_base_v003_signal(revenue, closeadj):
    result = _f21_revenue_growth(revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue growth (annual) × close
def f21rg_f21_revenue_growth_revgrow_252d_base_v004_signal(revenue, closeadj):
    result = _f21_revenue_growth(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue growth × close
def f21rg_f21_revenue_growth_revgrow_504d_base_v005_signal(revenue, closeadj):
    result = _f21_revenue_growth(revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d revenue growth × close
def f21rg_f21_revenue_growth_revgrow_5d_base_v006_signal(revenue, closeadj):
    result = _f21_revenue_growth(revenue, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d revenue growth × close
def f21rg_f21_revenue_growth_revgrow_10d_base_v007_signal(revenue, closeadj):
    result = _f21_revenue_growth(revenue, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d revenue growth × close
def f21rg_f21_revenue_growth_revgrow_42d_base_v008_signal(revenue, closeadj):
    result = _f21_revenue_growth(revenue, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d revenue growth × close
def f21rg_f21_revenue_growth_revgrow_189d_base_v009_signal(revenue, closeadj):
    result = _f21_revenue_growth(revenue, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d revenue growth × close
def f21rg_f21_revenue_growth_revgrow_378d_base_v010_signal(revenue, closeadj):
    result = _f21_revenue_growth(revenue, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed (5d) revenue growth × close
def f21rg_f21_revenue_growth_revgrowsm5_21d_base_v011_signal(revenue, closeadj):
    result = _f21_revenue_growth_smooth(revenue, 5, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed (21d) revenue growth × close
def f21rg_f21_revenue_growth_revgrowsm21_63d_base_v012_signal(revenue, closeadj):
    result = _f21_revenue_growth_smooth(revenue, 21, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed (63d) revenue growth × close
def f21rg_f21_revenue_growth_revgrowsm63_252d_base_v013_signal(revenue, closeadj):
    result = _f21_revenue_growth_smooth(revenue, 63, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed (126d) revenue growth × close
def f21rg_f21_revenue_growth_revgrowsm126_504d_base_v014_signal(revenue, closeadj):
    result = _f21_revenue_growth_smooth(revenue, 126, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log revenue growth × close
def f21rg_f21_revenue_growth_revloggrow_21d_base_v015_signal(revenue, closeadj):
    result = _f21_revenue_log_growth(revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log revenue growth × close
def f21rg_f21_revenue_growth_revloggrow_63d_base_v016_signal(revenue, closeadj):
    result = _f21_revenue_log_growth(revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log revenue growth × close
def f21rg_f21_revenue_growth_revloggrow_252d_base_v017_signal(revenue, closeadj):
    result = _f21_revenue_log_growth(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log revenue growth × close
def f21rg_f21_revenue_growth_revloggrow_504d_base_v018_signal(revenue, closeadj):
    result = _f21_revenue_log_growth(revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of 63d revenue growth × close
def f21rg_f21_revenue_growth_revgrowz_252d_base_v019_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of 252d revenue growth × close
def f21rg_f21_revenue_growth_revgrowz_504d_base_v020_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of 21d revenue growth × close (volatility of growth)
def f21rg_f21_revenue_growth_revgrowstd_21d_base_v021_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of 21d revenue growth × close
def f21rg_f21_revenue_growth_revgrowstd_252d_base_v022_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 21)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of 63d revenue growth × close
def f21rg_f21_revenue_growth_revgrowstd_504d_base_v023_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 63)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue growth difference (63d - 252d)
def f21rg_f21_revenue_growth_revgrowdiff_63m252_base_v024_signal(revenue, closeadj):
    a = _f21_revenue_growth(revenue, 63)
    b = _f21_revenue_growth(revenue, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21m63 revenue growth difference
def f21rg_f21_revenue_growth_revgrowdiff_21m63_base_v025_signal(revenue, closeadj):
    a = _f21_revenue_growth(revenue, 21)
    b = _f21_revenue_growth(revenue, 63)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252m504 revenue growth difference
def f21rg_f21_revenue_growth_revgrowdiff_252m504_base_v026_signal(revenue, closeadj):
    a = _f21_revenue_growth(revenue, 252)
    b = _f21_revenue_growth(revenue, 504)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue growth × revenue (dollar growth)
def f21rg_f21_revenue_growth_revgrowdollar_21d_base_v027_signal(revenue, closeadj):
    result = _f21_revenue_growth(revenue, 21) * revenue * closeadj / revenue.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue growth × revenue
def f21rg_f21_revenue_growth_revgrowdollar_252d_base_v028_signal(revenue, closeadj):
    result = _f21_revenue_growth(revenue, 252) * revenue * closeadj / revenue.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue growth × revenue
def f21rg_f21_revenue_growth_revgrowdollar_504d_base_v029_signal(revenue, closeadj):
    result = _f21_revenue_growth(revenue, 504) * revenue * closeadj / revenue.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA of 21d revenue growth × close
def f21rg_f21_revenue_growth_revgrowema_21d_base_v030_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 21)
    result = base.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of 63d revenue growth × close
def f21rg_f21_revenue_growth_revgrowema_63d_base_v031_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 63)
    result = base.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of 252d revenue growth × close
def f21rg_f21_revenue_growth_revgrowema_252d_base_v032_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 252)
    result = base.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue growth squared × close (severity)
def f21rg_f21_revenue_growth_revgrowsq_252d_base_v033_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 252)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue growth squared × close
def f21rg_f21_revenue_growth_revgrowsq_504d_base_v034_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 504)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue growth × volume zscore × close
def f21rg_f21_revenue_growth_revgrowxvolz_252d_base_v035_signal(revenue, closeadj, volume):
    base = _f21_revenue_growth(revenue, 252)
    result = base * _z(volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue growth × volume zscore × close
def f21rg_f21_revenue_growth_revgrowxvolz_63d_base_v036_signal(revenue, closeadj, volume):
    base = _f21_revenue_growth(revenue, 63)
    result = base * _z(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue growth × dollar volume
def f21rg_f21_revenue_growth_revgrowxdv_252d_base_v037_signal(revenue, closeadj, volume):
    base = _f21_revenue_growth(revenue, 252)
    dv = closeadj * volume
    result = base * dv
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue growth × dollar volume
def f21rg_f21_revenue_growth_revgrowxdv_21d_base_v038_signal(revenue, closeadj, volume):
    base = _f21_revenue_growth(revenue, 21)
    dv = closeadj * volume
    result = base * dv
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max revenue growth in 252d window × close
def f21rg_f21_revenue_growth_revgrowmax_252d_base_v039_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 63)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max revenue growth in 504d × close
def f21rg_f21_revenue_growth_revgrowmax_504d_base_v040_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 252)
    result = base.rolling(504, min_periods=126).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range of 63d revenue growth × close
def f21rg_f21_revenue_growth_revgrowrange_252d_base_v041_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 63)
    result = (base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range of 252d revenue growth × close
def f21rg_f21_revenue_growth_revgrowrange_504d_base_v042_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 252)
    result = (base.rolling(504, min_periods=126).max() - base.rolling(504, min_periods=126).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew of revenue growth × close
def f21rg_f21_revenue_growth_revgrowskew_252d_base_v043_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 21)
    result = base.rolling(252, min_periods=63).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew of revenue growth × close
def f21rg_f21_revenue_growth_revgrowskew_504d_base_v044_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 21)
    result = base.rolling(504, min_periods=126).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d kurt of revenue growth × close
def f21rg_f21_revenue_growth_revgrowkurt_252d_base_v045_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 21)
    result = base.rolling(252, min_periods=63).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# annualized 252d revenue growth × close (4× quarterly)
def f21rg_f21_revenue_growth_revgrowannual_252d_base_v046_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 63) * 4.0
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# annualized 504d revenue growth × close
def f21rg_f21_revenue_growth_revgrowannual_504d_base_v047_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 63) * 4.0
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue growth × revenue level / sharesbas (per-share growth)
def f21rg_f21_revenue_growth_revgrow_pershare_252d_base_v048_signal(revenue, sharesbas, closeadj):
    g = _f21_revenue_growth(revenue, 252)
    rps = revenue / sharesbas.replace(0, np.nan)
    result = g * rps * closeadj / rps.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue growth × revenue per share
def f21rg_f21_revenue_growth_revgrow_pershare_63d_base_v049_signal(revenue, sharesbas, closeadj):
    g = _f21_revenue_growth(revenue, 63)
    rps = revenue / sharesbas.replace(0, np.nan)
    result = g * rps * closeadj / rps.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue growth × revenue per share
def f21rg_f21_revenue_growth_revgrow_pershare_504d_base_v050_signal(revenue, sharesbas, closeadj):
    g = _f21_revenue_growth(revenue, 504)
    rps = revenue / sharesbas.replace(0, np.nan)
    result = g * rps * closeadj / rps.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue level (smoothed) × close
def f21rg_f21_revenue_growth_revlvl_21d_base_v051_signal(revenue, closeadj):
    base = _mean(revenue, 21) * closeadj + _f21_revenue_growth(revenue, 21) * 0.0
    return base.replace([np.inf, -np.inf], np.nan)


# 63d revenue level × close
def f21rg_f21_revenue_growth_revlvl_63d_base_v052_signal(revenue, closeadj):
    base = _mean(revenue, 63) * closeadj + _f21_revenue_growth(revenue, 63) * 0.0
    return base.replace([np.inf, -np.inf], np.nan)


# 252d revenue level × close
def f21rg_f21_revenue_growth_revlvl_252d_base_v053_signal(revenue, closeadj):
    base = _mean(revenue, 252) * closeadj + _f21_revenue_growth(revenue, 252) * 0.0
    return base.replace([np.inf, -np.inf], np.nan)


# 504d revenue level × close
def f21rg_f21_revenue_growth_revlvl_504d_base_v054_signal(revenue, closeadj):
    base = _mean(revenue, 504) * closeadj + _f21_revenue_growth(revenue, 504) * 0.0
    return base.replace([np.inf, -np.inf], np.nan)


# log revenue level × close
def f21rg_f21_revenue_growth_logrev_252d_base_v055_signal(revenue, closeadj):
    base = np.log(_mean(revenue, 252).replace(0, np.nan)) * closeadj + _f21_revenue_growth(revenue, 252) * 0.0
    return base.replace([np.inf, -np.inf], np.nan)


# log revenue × close 504d
def f21rg_f21_revenue_growth_logrev_504d_base_v056_signal(revenue, closeadj):
    base = np.log(_mean(revenue, 504).replace(0, np.nan)) * closeadj + _f21_revenue_growth(revenue, 504) * 0.0
    return base.replace([np.inf, -np.inf], np.nan)


# 21d revenue growth × ATR
def f21rg_f21_revenue_growth_revgrowxatr_252d_base_v057_signal(revenue, closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = _f21_revenue_growth(revenue, 252)
    result = base * atr * closeadj / atr.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue growth × ATR (63d window)
def f21rg_f21_revenue_growth_revgrowxatr_63d_base_v058_signal(revenue, closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    base = _f21_revenue_growth(revenue, 63)
    result = base * atr * closeadj / atr.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue growth × close return
def f21rg_f21_revenue_growth_revgrowxret_21d_base_v059_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 21)
    result = base * closeadj.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue growth × close return
def f21rg_f21_revenue_growth_revgrowxret_63d_base_v060_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 63)
    result = base * closeadj.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue growth × close return
def f21rg_f21_revenue_growth_revgrowxret_252d_base_v061_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 252)
    result = base * closeadj.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue growth ratio (63d / 252d)
def f21rg_f21_revenue_growth_revgrowratio_63v252_base_v062_signal(revenue, closeadj):
    a = _f21_revenue_growth(revenue, 63)
    b = _f21_revenue_growth(revenue, 252).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue growth ratio vs 63d
def f21rg_f21_revenue_growth_revgrowratio_21v63_base_v063_signal(revenue, closeadj):
    a = _f21_revenue_growth(revenue, 21)
    b = _f21_revenue_growth(revenue, 63).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d/504d revenue growth ratio
def f21rg_f21_revenue_growth_revgrowratio_252v504_base_v064_signal(revenue, closeadj):
    a = _f21_revenue_growth(revenue, 252)
    b = _f21_revenue_growth(revenue, 504).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling sum of 21d revenue growth over 252d (cumulative growth)
def f21rg_f21_revenue_growth_revgrowcumsum_252d_base_v065_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 21)
    result = base.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling sum of 63d revenue growth over 504d
def f21rg_f21_revenue_growth_revgrowcumsum_504d_base_v066_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 63)
    result = base.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue growth × revenue × volume
def f21rg_f21_revenue_growth_revgrowxrevvol_252d_base_v067_signal(revenue, closeadj, volume):
    base = _f21_revenue_growth(revenue, 252)
    result = base * revenue * volume / revenue.replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue growth times log revenue
def f21rg_f21_revenue_growth_revgrowxlogrev_252d_base_v068_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 252)
    result = base * np.log(revenue.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue growth × log revenue
def f21rg_f21_revenue_growth_revgrowxlogrev_504d_base_v069_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 504)
    result = base * np.log(revenue.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cumulative log revenue growth × close
def f21rg_f21_revenue_growth_revloggrowcum_252d_base_v070_signal(revenue, closeadj):
    base = _f21_revenue_log_growth(revenue, 21)
    result = base.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of log revenue growth × close
def f21rg_f21_revenue_growth_revloggrowema_252d_base_v071_signal(revenue, closeadj):
    base = _f21_revenue_log_growth(revenue, 252)
    result = base.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue growth × volume × close
def f21rg_f21_revenue_growth_revgrowxvol_21d_base_v072_signal(revenue, closeadj, volume):
    base = _f21_revenue_growth(revenue, 21)
    result = base * volume * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue growth × ATR scaled (alt encoding)
def f21rg_f21_revenue_growth_revgrowatr_252d_base_v073_signal(revenue, closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    base = _f21_revenue_growth(revenue, 252)
    result = base * atr
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue growth ratio × close
def f21rg_f21_revenue_growth_revgrowratio_63v504_base_v074_signal(revenue, closeadj):
    a = _f21_revenue_growth(revenue, 63)
    b = _f21_revenue_growth(revenue, 504).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# composite: 252d revenue growth + 252d log growth weighted by close
def f21rg_f21_revenue_growth_compositegrow_252d_base_v075_signal(revenue, closeadj):
    a = _f21_revenue_growth(revenue, 252)
    b = _f21_revenue_log_growth(revenue, 252)
    result = (a + b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f21rg_f21_revenue_growth_revgrow_21d_base_v001_signal,
    f21rg_f21_revenue_growth_revgrow_63d_base_v002_signal,
    f21rg_f21_revenue_growth_revgrow_126d_base_v003_signal,
    f21rg_f21_revenue_growth_revgrow_252d_base_v004_signal,
    f21rg_f21_revenue_growth_revgrow_504d_base_v005_signal,
    f21rg_f21_revenue_growth_revgrow_5d_base_v006_signal,
    f21rg_f21_revenue_growth_revgrow_10d_base_v007_signal,
    f21rg_f21_revenue_growth_revgrow_42d_base_v008_signal,
    f21rg_f21_revenue_growth_revgrow_189d_base_v009_signal,
    f21rg_f21_revenue_growth_revgrow_378d_base_v010_signal,
    f21rg_f21_revenue_growth_revgrowsm5_21d_base_v011_signal,
    f21rg_f21_revenue_growth_revgrowsm21_63d_base_v012_signal,
    f21rg_f21_revenue_growth_revgrowsm63_252d_base_v013_signal,
    f21rg_f21_revenue_growth_revgrowsm126_504d_base_v014_signal,
    f21rg_f21_revenue_growth_revloggrow_21d_base_v015_signal,
    f21rg_f21_revenue_growth_revloggrow_63d_base_v016_signal,
    f21rg_f21_revenue_growth_revloggrow_252d_base_v017_signal,
    f21rg_f21_revenue_growth_revloggrow_504d_base_v018_signal,
    f21rg_f21_revenue_growth_revgrowz_252d_base_v019_signal,
    f21rg_f21_revenue_growth_revgrowz_504d_base_v020_signal,
    f21rg_f21_revenue_growth_revgrowstd_21d_base_v021_signal,
    f21rg_f21_revenue_growth_revgrowstd_252d_base_v022_signal,
    f21rg_f21_revenue_growth_revgrowstd_504d_base_v023_signal,
    f21rg_f21_revenue_growth_revgrowdiff_63m252_base_v024_signal,
    f21rg_f21_revenue_growth_revgrowdiff_21m63_base_v025_signal,
    f21rg_f21_revenue_growth_revgrowdiff_252m504_base_v026_signal,
    f21rg_f21_revenue_growth_revgrowdollar_21d_base_v027_signal,
    f21rg_f21_revenue_growth_revgrowdollar_252d_base_v028_signal,
    f21rg_f21_revenue_growth_revgrowdollar_504d_base_v029_signal,
    f21rg_f21_revenue_growth_revgrowema_21d_base_v030_signal,
    f21rg_f21_revenue_growth_revgrowema_63d_base_v031_signal,
    f21rg_f21_revenue_growth_revgrowema_252d_base_v032_signal,
    f21rg_f21_revenue_growth_revgrowsq_252d_base_v033_signal,
    f21rg_f21_revenue_growth_revgrowsq_504d_base_v034_signal,
    f21rg_f21_revenue_growth_revgrowxvolz_252d_base_v035_signal,
    f21rg_f21_revenue_growth_revgrowxvolz_63d_base_v036_signal,
    f21rg_f21_revenue_growth_revgrowxdv_252d_base_v037_signal,
    f21rg_f21_revenue_growth_revgrowxdv_21d_base_v038_signal,
    f21rg_f21_revenue_growth_revgrowmax_252d_base_v039_signal,
    f21rg_f21_revenue_growth_revgrowmax_504d_base_v040_signal,
    f21rg_f21_revenue_growth_revgrowrange_252d_base_v041_signal,
    f21rg_f21_revenue_growth_revgrowrange_504d_base_v042_signal,
    f21rg_f21_revenue_growth_revgrowskew_252d_base_v043_signal,
    f21rg_f21_revenue_growth_revgrowskew_504d_base_v044_signal,
    f21rg_f21_revenue_growth_revgrowkurt_252d_base_v045_signal,
    f21rg_f21_revenue_growth_revgrowannual_252d_base_v046_signal,
    f21rg_f21_revenue_growth_revgrowannual_504d_base_v047_signal,
    f21rg_f21_revenue_growth_revgrow_pershare_252d_base_v048_signal,
    f21rg_f21_revenue_growth_revgrow_pershare_63d_base_v049_signal,
    f21rg_f21_revenue_growth_revgrow_pershare_504d_base_v050_signal,
    f21rg_f21_revenue_growth_revlvl_21d_base_v051_signal,
    f21rg_f21_revenue_growth_revlvl_63d_base_v052_signal,
    f21rg_f21_revenue_growth_revlvl_252d_base_v053_signal,
    f21rg_f21_revenue_growth_revlvl_504d_base_v054_signal,
    f21rg_f21_revenue_growth_logrev_252d_base_v055_signal,
    f21rg_f21_revenue_growth_logrev_504d_base_v056_signal,
    f21rg_f21_revenue_growth_revgrowxatr_252d_base_v057_signal,
    f21rg_f21_revenue_growth_revgrowxatr_63d_base_v058_signal,
    f21rg_f21_revenue_growth_revgrowxret_21d_base_v059_signal,
    f21rg_f21_revenue_growth_revgrowxret_63d_base_v060_signal,
    f21rg_f21_revenue_growth_revgrowxret_252d_base_v061_signal,
    f21rg_f21_revenue_growth_revgrowratio_63v252_base_v062_signal,
    f21rg_f21_revenue_growth_revgrowratio_21v63_base_v063_signal,
    f21rg_f21_revenue_growth_revgrowratio_252v504_base_v064_signal,
    f21rg_f21_revenue_growth_revgrowcumsum_252d_base_v065_signal,
    f21rg_f21_revenue_growth_revgrowcumsum_504d_base_v066_signal,
    f21rg_f21_revenue_growth_revgrowxrevvol_252d_base_v067_signal,
    f21rg_f21_revenue_growth_revgrowxlogrev_252d_base_v068_signal,
    f21rg_f21_revenue_growth_revgrowxlogrev_504d_base_v069_signal,
    f21rg_f21_revenue_growth_revloggrowcum_252d_base_v070_signal,
    f21rg_f21_revenue_growth_revloggrowema_252d_base_v071_signal,
    f21rg_f21_revenue_growth_revgrowxvol_21d_base_v072_signal,
    f21rg_f21_revenue_growth_revgrowatr_252d_base_v073_signal,
    f21rg_f21_revenue_growth_revgrowratio_63v504_base_v074_signal,
    f21rg_f21_revenue_growth_compositegrow_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F21_REVENUE_GROWTH_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    revenue = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="revenue")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.002, n))), name="sharesbas")
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)) + 1e5, name="volume")

    cols = {
        "revenue": revenue, "sharesbas": sharesbas, "closeadj": closeadj,
        "high": high, "low": low, "volume": volume,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f21_revenue_growth", "_f21_revenue_growth_smooth", "_f21_revenue_log_growth")
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
    print(f"OK f21_revenue_growth_base_001_075_claude: {n_features} features pass")
