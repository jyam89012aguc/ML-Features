import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _max(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _min(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _z(s, w):
    return (s - _mean(s, w)) / _std(s, w).replace(0, np.nan)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f29_daily_ffill(x, closeadj):
    return x.reindex(closeadj.index).ffill()


def _f29_ratio(a, b):
    return a / b.replace(0, np.nan)


def _f29_log_ratio(a, b):
    return np.log(a.replace(0, np.nan).abs() / b.replace(0, np.nan).abs())


# 5d slope of own-basket spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_level_level_slope_v001_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    base = own - bas
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of own-basket spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_level_level_slope_v002_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    base = own - bas
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of own-basket spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_level_level_slope_v003_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    base = own - bas
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of own-basket spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_level_level_slope_v004_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    base = own - bas
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of own-basket spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_level_level_slope_v005_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    base = own - bas
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_z21_21d_slope_v006_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _z(spread, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_z21_21d_slope_v007_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _z(spread, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_z21_21d_slope_v008_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _z(spread, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d z spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_z21_21d_slope_v009_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _z(spread, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d z spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_z21_21d_slope_v010_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _z(spread, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_z63_63d_slope_v011_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _z(spread, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_z63_63d_slope_v012_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _z(spread, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_z63_63d_slope_v013_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _z(spread, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d z spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_z63_63d_slope_v014_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _z(spread, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d z spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_z63_63d_slope_v015_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _z(spread, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_z126_126d_slope_v016_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _z(spread, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_z126_126d_slope_v017_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _z(spread, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_z126_126d_slope_v018_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _z(spread, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d z spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_z126_126d_slope_v019_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _z(spread, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d z spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_z126_126d_slope_v020_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _z(spread, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_z252_252d_slope_v021_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _z(spread, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_z252_252d_slope_v022_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _z(spread, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_z252_252d_slope_v023_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _z(spread, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d z spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_z252_252d_slope_v024_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _z(spread, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d z spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_z252_252d_slope_v025_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _z(spread, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of own/basket ratio
def f29cpr_f29_semi_capex_peer_relative_cprratio_level_level_slope_v026_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    base = own / bas.replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of own/basket ratio
def f29cpr_f29_semi_capex_peer_relative_cprratio_level_level_slope_v027_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    base = own / bas.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of own/basket ratio
def f29cpr_f29_semi_capex_peer_relative_cprratio_level_level_slope_v028_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    base = own / bas.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of own/basket ratio
def f29cpr_f29_semi_capex_peer_relative_cprratio_level_level_slope_v029_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    base = own / bas.replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of own/basket ratio
def f29cpr_f29_semi_capex_peer_relative_cprratio_level_level_slope_v030_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    base = own / bas.replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z own/basket
def f29cpr_f29_semi_capex_peer_relative_cprratio_z63_63d_slope_v031_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = own / bas.replace(0, np.nan)
    base = _z(r, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z own/basket
def f29cpr_f29_semi_capex_peer_relative_cprratio_z63_63d_slope_v032_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = own / bas.replace(0, np.nan)
    base = _z(r, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z own/basket
def f29cpr_f29_semi_capex_peer_relative_cprratio_z63_63d_slope_v033_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = own / bas.replace(0, np.nan)
    base = _z(r, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d z own/basket
def f29cpr_f29_semi_capex_peer_relative_cprratio_z63_63d_slope_v034_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = own / bas.replace(0, np.nan)
    base = _z(r, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d z own/basket
def f29cpr_f29_semi_capex_peer_relative_cprratio_z63_63d_slope_v035_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = own / bas.replace(0, np.nan)
    base = _z(r, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z own/basket
def f29cpr_f29_semi_capex_peer_relative_cprratio_z252_252d_slope_v036_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = own / bas.replace(0, np.nan)
    base = _z(r, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z own/basket
def f29cpr_f29_semi_capex_peer_relative_cprratio_z252_252d_slope_v037_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = own / bas.replace(0, np.nan)
    base = _z(r, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z own/basket
def f29cpr_f29_semi_capex_peer_relative_cprratio_z252_252d_slope_v038_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = own / bas.replace(0, np.nan)
    base = _z(r, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d z own/basket
def f29cpr_f29_semi_capex_peer_relative_cprratio_z252_252d_slope_v039_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = own / bas.replace(0, np.nan)
    base = _z(r, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d z own/basket
def f29cpr_f29_semi_capex_peer_relative_cprratio_z252_252d_slope_v040_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = own / bas.replace(0, np.nan)
    base = _z(r, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of log(own/basket)
def f29cpr_f29_semi_capex_peer_relative_cprlogratio_level_level_slope_v041_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    base = np.log(own.abs().replace(0, np.nan) / bas.abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of log(own/basket)
def f29cpr_f29_semi_capex_peer_relative_cprlogratio_level_level_slope_v042_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    base = np.log(own.abs().replace(0, np.nan) / bas.abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of log(own/basket)
def f29cpr_f29_semi_capex_peer_relative_cprlogratio_level_level_slope_v043_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    base = np.log(own.abs().replace(0, np.nan) / bas.abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of log(own/basket)
def f29cpr_f29_semi_capex_peer_relative_cprlogratio_level_level_slope_v044_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    base = np.log(own.abs().replace(0, np.nan) / bas.abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of log(own/basket)
def f29cpr_f29_semi_capex_peer_relative_cprlogratio_level_level_slope_v045_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    base = np.log(own.abs().replace(0, np.nan) / bas.abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z log ratio
def f29cpr_f29_semi_capex_peer_relative_cprlogratio_z63_63d_slope_v046_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = np.log(own.abs().replace(0, np.nan) / bas.abs().replace(0, np.nan))
    base = _z(r, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z log ratio
def f29cpr_f29_semi_capex_peer_relative_cprlogratio_z63_63d_slope_v047_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = np.log(own.abs().replace(0, np.nan) / bas.abs().replace(0, np.nan))
    base = _z(r, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z log ratio
def f29cpr_f29_semi_capex_peer_relative_cprlogratio_z63_63d_slope_v048_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = np.log(own.abs().replace(0, np.nan) / bas.abs().replace(0, np.nan))
    base = _z(r, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d z log ratio
def f29cpr_f29_semi_capex_peer_relative_cprlogratio_z63_63d_slope_v049_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = np.log(own.abs().replace(0, np.nan) / bas.abs().replace(0, np.nan))
    base = _z(r, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d z log ratio
def f29cpr_f29_semi_capex_peer_relative_cprlogratio_z63_63d_slope_v050_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = np.log(own.abs().replace(0, np.nan) / bas.abs().replace(0, np.nan))
    base = _z(r, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z log ratio
def f29cpr_f29_semi_capex_peer_relative_cprlogratio_z252_252d_slope_v051_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = np.log(own.abs().replace(0, np.nan) / bas.abs().replace(0, np.nan))
    base = _z(r, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z log ratio
def f29cpr_f29_semi_capex_peer_relative_cprlogratio_z252_252d_slope_v052_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = np.log(own.abs().replace(0, np.nan) / bas.abs().replace(0, np.nan))
    base = _z(r, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z log ratio
def f29cpr_f29_semi_capex_peer_relative_cprlogratio_z252_252d_slope_v053_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = np.log(own.abs().replace(0, np.nan) / bas.abs().replace(0, np.nan))
    base = _z(r, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d z log ratio
def f29cpr_f29_semi_capex_peer_relative_cprlogratio_z252_252d_slope_v054_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = np.log(own.abs().replace(0, np.nan) / bas.abs().replace(0, np.nan))
    base = _z(r, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d z log ratio
def f29cpr_f29_semi_capex_peer_relative_cprlogratio_z252_252d_slope_v055_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = np.log(own.abs().replace(0, np.nan) / bas.abs().replace(0, np.nan))
    base = _z(r, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d max spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_max63_63d_slope_v056_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _max(spread, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d max spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_max63_63d_slope_v057_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _max(spread, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d max spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_max63_63d_slope_v058_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _max(spread, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d max spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_max63_63d_slope_v059_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _max(spread, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d max spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_max63_63d_slope_v060_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _max(spread, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d min spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_min63_63d_slope_v061_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _min(spread, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d min spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_min63_63d_slope_v062_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _min(spread, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d min spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_min63_63d_slope_v063_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _min(spread, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d min spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_min63_63d_slope_v064_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _min(spread, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d min spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_min63_63d_slope_v065_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _min(spread, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d range spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_rng63_63d_slope_v066_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _max(spread, 63) - _min(spread, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d range spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_rng63_63d_slope_v067_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _max(spread, 63) - _min(spread, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d range spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_rng63_63d_slope_v068_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _max(spread, 63) - _min(spread, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d range spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_rng63_63d_slope_v069_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _max(spread, 63) - _min(spread, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d range spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_rng63_63d_slope_v070_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _max(spread, 63) - _min(spread, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pos-in-range
def f29cpr_f29_semi_capex_peer_relative_cprspread_pos63_63d_slope_v071_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    lo = _min(spread, 63)
    hi = _max(spread, 63)
    base = (spread - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pos-in-range
def f29cpr_f29_semi_capex_peer_relative_cprspread_pos63_63d_slope_v072_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    lo = _min(spread, 63)
    hi = _max(spread, 63)
    base = (spread - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pos-in-range
def f29cpr_f29_semi_capex_peer_relative_cprspread_pos63_63d_slope_v073_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    lo = _min(spread, 63)
    hi = _max(spread, 63)
    base = (spread - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d pos-in-range
def f29cpr_f29_semi_capex_peer_relative_cprspread_pos63_63d_slope_v074_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    lo = _min(spread, 63)
    hi = _max(spread, 63)
    base = (spread - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d pos-in-range
def f29cpr_f29_semi_capex_peer_relative_cprspread_pos63_63d_slope_v075_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    lo = _min(spread, 63)
    hi = _max(spread, 63)
    base = (spread - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_std63_63d_slope_v076_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _std(spread, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_std63_63d_slope_v077_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _std(spread, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_std63_63d_slope_v078_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _std(spread, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d std spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_std63_63d_slope_v079_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _std(spread, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d std spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_std63_63d_slope_v080_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _std(spread, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_std252_252d_slope_v081_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _std(spread, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_std252_252d_slope_v082_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _std(spread, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_std252_252d_slope_v083_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _std(spread, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d std spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_std252_252d_slope_v084_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _std(spread, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d std spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_std252_252d_slope_v085_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = _std(spread, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d hit-rate own>basket
def f29cpr_f29_semi_capex_peer_relative_cprhit_above63_63d_slope_v086_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    base = (own > bas).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d hit-rate own>basket
def f29cpr_f29_semi_capex_peer_relative_cprhit_above63_63d_slope_v087_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    base = (own > bas).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d hit-rate own>basket
def f29cpr_f29_semi_capex_peer_relative_cprhit_above63_63d_slope_v088_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    base = (own > bas).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d hit-rate own>basket
def f29cpr_f29_semi_capex_peer_relative_cprhit_above63_63d_slope_v089_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    base = (own > bas).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d hit-rate own>basket
def f29cpr_f29_semi_capex_peer_relative_cprhit_above63_63d_slope_v090_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    base = (own > bas).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d hit-rate own>basket
def f29cpr_f29_semi_capex_peer_relative_cprhit_above252_252d_slope_v091_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    base = (own > bas).astype(float).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d hit-rate own>basket
def f29cpr_f29_semi_capex_peer_relative_cprhit_above252_252d_slope_v092_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    base = (own > bas).astype(float).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d hit-rate own>basket
def f29cpr_f29_semi_capex_peer_relative_cprhit_above252_252d_slope_v093_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    base = (own > bas).astype(float).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d hit-rate own>basket
def f29cpr_f29_semi_capex_peer_relative_cprhit_above252_252d_slope_v094_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    base = (own > bas).astype(float).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d hit-rate own>basket
def f29cpr_f29_semi_capex_peer_relative_cprhit_above252_252d_slope_v095_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    base = (own > bas).astype(float).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d spread drawdown
def f29cpr_f29_semi_capex_peer_relative_cprspread_dd63_63d_slope_v096_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = spread - _max(spread, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d spread drawdown
def f29cpr_f29_semi_capex_peer_relative_cprspread_dd63_63d_slope_v097_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = spread - _max(spread, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d spread drawdown
def f29cpr_f29_semi_capex_peer_relative_cprspread_dd63_63d_slope_v098_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = spread - _max(spread, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d spread drawdown
def f29cpr_f29_semi_capex_peer_relative_cprspread_dd63_63d_slope_v099_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = spread - _max(spread, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d spread drawdown
def f29cpr_f29_semi_capex_peer_relative_cprspread_dd63_63d_slope_v100_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = spread - _max(spread, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d spread drawdown
def f29cpr_f29_semi_capex_peer_relative_cprspread_dd252_252d_slope_v101_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = spread - _max(spread, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d spread drawdown
def f29cpr_f29_semi_capex_peer_relative_cprspread_dd252_252d_slope_v102_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = spread - _max(spread, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d spread drawdown
def f29cpr_f29_semi_capex_peer_relative_cprspread_dd252_252d_slope_v103_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = spread - _max(spread, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d spread drawdown
def f29cpr_f29_semi_capex_peer_relative_cprspread_dd252_252d_slope_v104_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = spread - _max(spread, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d spread drawdown
def f29cpr_f29_semi_capex_peer_relative_cprspread_dd252_252d_slope_v105_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = spread - _max(spread, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d spread run-up
def f29cpr_f29_semi_capex_peer_relative_cprspread_runup63_63d_slope_v106_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = spread - _min(spread, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d spread run-up
def f29cpr_f29_semi_capex_peer_relative_cprspread_runup63_63d_slope_v107_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = spread - _min(spread, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d spread run-up
def f29cpr_f29_semi_capex_peer_relative_cprspread_runup63_63d_slope_v108_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = spread - _min(spread, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d spread run-up
def f29cpr_f29_semi_capex_peer_relative_cprspread_runup63_63d_slope_v109_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = spread - _min(spread, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d spread run-up
def f29cpr_f29_semi_capex_peer_relative_cprspread_runup63_63d_slope_v110_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = spread - _min(spread, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d spread skew
def f29cpr_f29_semi_capex_peer_relative_cprspread_skew63_63d_slope_v111_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = spread.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d spread skew
def f29cpr_f29_semi_capex_peer_relative_cprspread_skew63_63d_slope_v112_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = spread.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d spread skew
def f29cpr_f29_semi_capex_peer_relative_cprspread_skew63_63d_slope_v113_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = spread.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d spread skew
def f29cpr_f29_semi_capex_peer_relative_cprspread_skew63_63d_slope_v114_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = spread.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d spread skew
def f29cpr_f29_semi_capex_peer_relative_cprspread_skew63_63d_slope_v115_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = spread.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d spread kurt
def f29cpr_f29_semi_capex_peer_relative_cprspread_kurt63_63d_slope_v116_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = spread.rolling(63, min_periods=32).kurt()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d spread kurt
def f29cpr_f29_semi_capex_peer_relative_cprspread_kurt63_63d_slope_v117_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = spread.rolling(63, min_periods=32).kurt()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d spread kurt
def f29cpr_f29_semi_capex_peer_relative_cprspread_kurt63_63d_slope_v118_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = spread.rolling(63, min_periods=32).kurt()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d spread kurt
def f29cpr_f29_semi_capex_peer_relative_cprspread_kurt63_63d_slope_v119_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = spread.rolling(63, min_periods=32).kurt()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d spread kurt
def f29cpr_f29_semi_capex_peer_relative_cprspread_kurt63_63d_slope_v120_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = spread.rolling(63, min_periods=32).kurt()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of ema(5)-ema(63) spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_ema_5v63_slope_v121_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = spread.ewm(span=5, adjust=False).mean() - spread.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ema(5)-ema(63) spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_ema_5v63_slope_v122_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = spread.ewm(span=5, adjust=False).mean() - spread.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ema(5)-ema(63) spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_ema_5v63_slope_v123_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = spread.ewm(span=5, adjust=False).mean() - spread.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of ema(5)-ema(63) spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_ema_5v63_slope_v124_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = spread.ewm(span=5, adjust=False).mean() - spread.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of ema(5)-ema(63) spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_ema_5v63_slope_v125_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = spread.ewm(span=5, adjust=False).mean() - spread.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d quartile rank spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_quart63_63d_slope_v126_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = spread.rolling(63, min_periods=32).rank(pct=True)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d quartile rank spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_quart63_63d_slope_v127_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = spread.rolling(63, min_periods=32).rank(pct=True)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d quartile rank spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_quart63_63d_slope_v128_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = spread.rolling(63, min_periods=32).rank(pct=True)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d quartile rank spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_quart63_63d_slope_v129_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = spread.rolling(63, min_periods=32).rank(pct=True)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d quartile rank spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_quart63_63d_slope_v130_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    base = spread.rolling(63, min_periods=32).rank(pct=True)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d corr own vs basket
def f29cpr_f29_semi_capex_peer_relative_cprlead_corr63_63d_slope_v131_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    base = own.rolling(63, min_periods=32).corr(bas)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d corr own vs basket
def f29cpr_f29_semi_capex_peer_relative_cprlead_corr63_63d_slope_v132_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    base = own.rolling(63, min_periods=32).corr(bas)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d corr own vs basket
def f29cpr_f29_semi_capex_peer_relative_cprlead_corr63_63d_slope_v133_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    base = own.rolling(63, min_periods=32).corr(bas)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d corr own vs basket
def f29cpr_f29_semi_capex_peer_relative_cprlead_corr63_63d_slope_v134_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    base = own.rolling(63, min_periods=32).corr(bas)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d corr own vs basket
def f29cpr_f29_semi_capex_peer_relative_cprlead_corr63_63d_slope_v135_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    base = own.rolling(63, min_periods=32).corr(bas)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d beta own vs basket
def f29cpr_f29_semi_capex_peer_relative_cprlead_beta63_63d_slope_v136_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    cov = own.rolling(63, min_periods=32).cov(bas)
    var = bas.rolling(63, min_periods=32).var()
    base = cov / var.replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d beta own vs basket
def f29cpr_f29_semi_capex_peer_relative_cprlead_beta63_63d_slope_v137_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    cov = own.rolling(63, min_periods=32).cov(bas)
    var = bas.rolling(63, min_periods=32).var()
    base = cov / var.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d beta own vs basket
def f29cpr_f29_semi_capex_peer_relative_cprlead_beta63_63d_slope_v138_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    cov = own.rolling(63, min_periods=32).cov(bas)
    var = bas.rolling(63, min_periods=32).var()
    base = cov / var.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d beta own vs basket
def f29cpr_f29_semi_capex_peer_relative_cprlead_beta63_63d_slope_v139_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    cov = own.rolling(63, min_periods=32).cov(bas)
    var = bas.rolling(63, min_periods=32).var()
    base = cov / var.replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d beta own vs basket
def f29cpr_f29_semi_capex_peer_relative_cprlead_beta63_63d_slope_v140_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    cov = own.rolling(63, min_periods=32).cov(bas)
    var = bas.rolling(63, min_periods=32).var()
    base = cov / var.replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z basket capex/rev
def f29cpr_f29_semi_capex_peer_relative_cprbas_z63_63d_slope_v141_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    base = _z(bas, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z basket capex/rev
def f29cpr_f29_semi_capex_peer_relative_cprbas_z63_63d_slope_v142_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    base = _z(bas, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z basket capex/rev
def f29cpr_f29_semi_capex_peer_relative_cprbas_z63_63d_slope_v143_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    base = _z(bas, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d z basket capex/rev
def f29cpr_f29_semi_capex_peer_relative_cprbas_z63_63d_slope_v144_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    base = _z(bas, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d z basket capex/rev
def f29cpr_f29_semi_capex_peer_relative_cprbas_z63_63d_slope_v145_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    base = _z(bas, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z basket capex/rev
def f29cpr_f29_semi_capex_peer_relative_cprbas_z252_252d_slope_v146_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    base = _z(bas, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z basket capex/rev
def f29cpr_f29_semi_capex_peer_relative_cprbas_z252_252d_slope_v147_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    base = _z(bas, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z basket capex/rev
def f29cpr_f29_semi_capex_peer_relative_cprbas_z252_252d_slope_v148_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    base = _z(bas, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d z basket capex/rev
def f29cpr_f29_semi_capex_peer_relative_cprbas_z252_252d_slope_v149_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    base = _z(bas, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d z basket capex/rev
def f29cpr_f29_semi_capex_peer_relative_cprbas_z252_252d_slope_v150_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    base = _z(bas, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
