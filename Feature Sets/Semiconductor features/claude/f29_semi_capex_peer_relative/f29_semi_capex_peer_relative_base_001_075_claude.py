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


def _max(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _min(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f29_daily_ffill(x, closeadj):
    return x.reindex(closeadj.index).ffill()


def _f29_ratio(a, b):
    return a / b.replace(0, np.nan)


def _f29_log_ratio(a, b):
    return np.log(a.replace(0, np.nan).abs() / b.replace(0, np.nan).abs())


# 21d mean of own capex/rev minus basket
def f29cpr_f29_semi_capex_peer_relative_cprspread_mean_21d_base_v001_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = _mean(spread, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of own capex/rev minus basket
def f29cpr_f29_semi_capex_peer_relative_cprspread_mean_63d_base_v002_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = _mean(spread, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of own capex/rev minus basket
def f29cpr_f29_semi_capex_peer_relative_cprspread_mean_126d_base_v003_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = _mean(spread, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of own capex/rev minus basket
def f29cpr_f29_semi_capex_peer_relative_cprspread_mean_252d_base_v004_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = _mean(spread, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of own capex/rev minus basket
def f29cpr_f29_semi_capex_peer_relative_cprspread_mean_504d_base_v005_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = _mean(spread, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z of own minus basket capex/rev
def f29cpr_f29_semi_capex_peer_relative_cprspread_z_21d_base_v006_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = _z(spread, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z of own minus basket capex/rev
def f29cpr_f29_semi_capex_peer_relative_cprspread_z_63d_base_v007_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = _z(spread, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z of own minus basket capex/rev
def f29cpr_f29_semi_capex_peer_relative_cprspread_z_126d_base_v008_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = _z(spread, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z of own minus basket capex/rev
def f29cpr_f29_semi_capex_peer_relative_cprspread_z_252d_base_v009_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = _z(spread, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z of own minus basket capex/rev
def f29cpr_f29_semi_capex_peer_relative_cprspread_z_504d_base_v010_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = _z(spread, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z of own minus basket
def f29cpr_f29_semi_capex_peer_relative_cprspread_rz_21d_base_v011_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    med = spread.rolling(21, min_periods=max(1, 21//2)).median()
    mad = (spread - med).abs().rolling(21, min_periods=max(1, 21//2)).median()
    result = (spread - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z of own minus basket
def f29cpr_f29_semi_capex_peer_relative_cprspread_rz_63d_base_v012_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    med = spread.rolling(63, min_periods=max(1, 63//2)).median()
    mad = (spread - med).abs().rolling(63, min_periods=max(1, 63//2)).median()
    result = (spread - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z of own minus basket
def f29cpr_f29_semi_capex_peer_relative_cprspread_rz_126d_base_v013_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    med = spread.rolling(126, min_periods=max(1, 126//2)).median()
    mad = (spread - med).abs().rolling(126, min_periods=max(1, 126//2)).median()
    result = (spread - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z of own minus basket
def f29cpr_f29_semi_capex_peer_relative_cprspread_rz_252d_base_v014_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    med = spread.rolling(252, min_periods=max(1, 252//2)).median()
    mad = (spread - med).abs().rolling(252, min_periods=max(1, 252//2)).median()
    result = (spread - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z of own minus basket
def f29cpr_f29_semi_capex_peer_relative_cprspread_rz_504d_base_v015_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    med = spread.rolling(504, min_periods=max(1, 504//2)).median()
    mad = (spread - med).abs().rolling(504, min_periods=max(1, 504//2)).median()
    result = (spread - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of own/basket capex-intensity ratio
def f29cpr_f29_semi_capex_peer_relative_cprratio_mean_21d_base_v016_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = own / bas.replace(0, np.nan)
    result = _mean(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of own/basket capex-intensity ratio
def f29cpr_f29_semi_capex_peer_relative_cprratio_mean_63d_base_v017_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = own / bas.replace(0, np.nan)
    result = _mean(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of own/basket capex-intensity ratio
def f29cpr_f29_semi_capex_peer_relative_cprratio_mean_126d_base_v018_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = own / bas.replace(0, np.nan)
    result = _mean(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of own/basket capex-intensity ratio
def f29cpr_f29_semi_capex_peer_relative_cprratio_mean_252d_base_v019_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = own / bas.replace(0, np.nan)
    result = _mean(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of own/basket capex-intensity ratio
def f29cpr_f29_semi_capex_peer_relative_cprratio_mean_504d_base_v020_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = own / bas.replace(0, np.nan)
    result = _mean(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z of own/basket capex-intensity ratio
def f29cpr_f29_semi_capex_peer_relative_cprratio_z_21d_base_v021_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = own / bas.replace(0, np.nan)
    result = _z(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z of own/basket capex-intensity ratio
def f29cpr_f29_semi_capex_peer_relative_cprratio_z_63d_base_v022_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = own / bas.replace(0, np.nan)
    result = _z(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z of own/basket capex-intensity ratio
def f29cpr_f29_semi_capex_peer_relative_cprratio_z_126d_base_v023_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = own / bas.replace(0, np.nan)
    result = _z(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z of own/basket capex-intensity ratio
def f29cpr_f29_semi_capex_peer_relative_cprratio_z_252d_base_v024_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = own / bas.replace(0, np.nan)
    result = _z(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z of own/basket capex-intensity ratio
def f29cpr_f29_semi_capex_peer_relative_cprratio_z_504d_base_v025_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = own / bas.replace(0, np.nan)
    result = _z(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of log(own/basket capex-intensity)
def f29cpr_f29_semi_capex_peer_relative_cprlogratio_mean_21d_base_v026_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = np.log(own.abs().replace(0, np.nan) / bas.abs().replace(0, np.nan))
    result = _mean(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of log(own/basket capex-intensity)
def f29cpr_f29_semi_capex_peer_relative_cprlogratio_mean_63d_base_v027_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = np.log(own.abs().replace(0, np.nan) / bas.abs().replace(0, np.nan))
    result = _mean(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of log(own/basket capex-intensity)
def f29cpr_f29_semi_capex_peer_relative_cprlogratio_mean_126d_base_v028_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = np.log(own.abs().replace(0, np.nan) / bas.abs().replace(0, np.nan))
    result = _mean(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of log(own/basket capex-intensity)
def f29cpr_f29_semi_capex_peer_relative_cprlogratio_mean_252d_base_v029_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = np.log(own.abs().replace(0, np.nan) / bas.abs().replace(0, np.nan))
    result = _mean(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of log(own/basket capex-intensity)
def f29cpr_f29_semi_capex_peer_relative_cprlogratio_mean_504d_base_v030_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = np.log(own.abs().replace(0, np.nan) / bas.abs().replace(0, np.nan))
    result = _mean(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z of log(own/basket capex-intensity)
def f29cpr_f29_semi_capex_peer_relative_cprlogratio_z_21d_base_v031_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = np.log(own.abs().replace(0, np.nan) / bas.abs().replace(0, np.nan))
    result = _z(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z of log(own/basket capex-intensity)
def f29cpr_f29_semi_capex_peer_relative_cprlogratio_z_63d_base_v032_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = np.log(own.abs().replace(0, np.nan) / bas.abs().replace(0, np.nan))
    result = _z(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z of log(own/basket capex-intensity)
def f29cpr_f29_semi_capex_peer_relative_cprlogratio_z_126d_base_v033_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = np.log(own.abs().replace(0, np.nan) / bas.abs().replace(0, np.nan))
    result = _z(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z of log(own/basket capex-intensity)
def f29cpr_f29_semi_capex_peer_relative_cprlogratio_z_252d_base_v034_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = np.log(own.abs().replace(0, np.nan) / bas.abs().replace(0, np.nan))
    result = _z(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z of log(own/basket capex-intensity)
def f29cpr_f29_semi_capex_peer_relative_cprlogratio_z_504d_base_v035_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = np.log(own.abs().replace(0, np.nan) / bas.abs().replace(0, np.nan))
    result = _z(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max of own-basket capex/rev spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_max_21d_base_v036_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = _max(spread, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max of own-basket capex/rev spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_max_63d_base_v037_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = _max(spread, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max of own-basket capex/rev spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_max_126d_base_v038_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = _max(spread, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max of own-basket capex/rev spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_max_252d_base_v039_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = _max(spread, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max of own-basket capex/rev spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_max_504d_base_v040_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = _max(spread, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min of own-basket capex/rev spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_min_21d_base_v041_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = _min(spread, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min of own-basket capex/rev spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_min_63d_base_v042_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = _min(spread, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min of own-basket capex/rev spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_min_126d_base_v043_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = _min(spread, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min of own-basket capex/rev spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_min_252d_base_v044_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = _min(spread, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min of own-basket capex/rev spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_min_504d_base_v045_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = _min(spread, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range of own-basket spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_rng_21d_base_v046_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = _max(spread, 21) - _min(spread, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range of own-basket spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_rng_63d_base_v047_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = _max(spread, 63) - _min(spread, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range of own-basket spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_rng_126d_base_v048_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = _max(spread, 126) - _min(spread, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range of own-basket spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_rng_252d_base_v049_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = _max(spread, 252) - _min(spread, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range of own-basket spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_rng_504d_base_v050_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = _max(spread, 504) - _min(spread, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pos-in-range of own-basket spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_pos_21d_base_v051_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    lo = _min(spread, 21)
    hi = _max(spread, 21)
    result = (spread - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pos-in-range of own-basket spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_pos_63d_base_v052_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    lo = _min(spread, 63)
    hi = _max(spread, 63)
    result = (spread - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d pos-in-range of own-basket spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_pos_126d_base_v053_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    lo = _min(spread, 126)
    hi = _max(spread, 126)
    result = (spread - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pos-in-range of own-basket spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_pos_252d_base_v054_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    lo = _min(spread, 252)
    hi = _max(spread, 252)
    result = (spread - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pos-in-range of own-basket spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_pos_504d_base_v055_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    lo = _min(spread, 504)
    hi = _max(spread, 504)
    result = (spread - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of own-basket spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_std_21d_base_v056_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = _std(spread, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of own-basket spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_std_63d_base_v057_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = _std(spread, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of own-basket spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_std_126d_base_v058_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = _std(spread, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of own-basket spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_std_252d_base_v059_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = _std(spread, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of own-basket spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_std_504d_base_v060_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = _std(spread, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d hit-rate own > basket capex/rev
def f29cpr_f29_semi_capex_peer_relative_cprhit_above_21d_base_v061_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    result = (own > bas).astype(float).rolling(21, min_periods=max(1, 21//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d hit-rate own > basket capex/rev
def f29cpr_f29_semi_capex_peer_relative_cprhit_above_63d_base_v062_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    result = (own > bas).astype(float).rolling(63, min_periods=max(1, 63//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d hit-rate own > basket capex/rev
def f29cpr_f29_semi_capex_peer_relative_cprhit_above_126d_base_v063_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    result = (own > bas).astype(float).rolling(126, min_periods=max(1, 126//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d hit-rate own > basket capex/rev
def f29cpr_f29_semi_capex_peer_relative_cprhit_above_252d_base_v064_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    result = (own > bas).astype(float).rolling(252, min_periods=max(1, 252//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d hit-rate own > basket capex/rev
def f29cpr_f29_semi_capex_peer_relative_cprhit_above_504d_base_v065_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    result = (own > bas).astype(float).rolling(504, min_periods=max(1, 504//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d hit-rate own < basket capex/rev
def f29cpr_f29_semi_capex_peer_relative_cprhit_below_21d_base_v066_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    result = (own < bas).astype(float).rolling(21, min_periods=max(1, 21//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d hit-rate own < basket capex/rev
def f29cpr_f29_semi_capex_peer_relative_cprhit_below_63d_base_v067_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    result = (own < bas).astype(float).rolling(63, min_periods=max(1, 63//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d hit-rate own < basket capex/rev
def f29cpr_f29_semi_capex_peer_relative_cprhit_below_126d_base_v068_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    result = (own < bas).astype(float).rolling(126, min_periods=max(1, 126//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d hit-rate own < basket capex/rev
def f29cpr_f29_semi_capex_peer_relative_cprhit_below_252d_base_v069_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    result = (own < bas).astype(float).rolling(252, min_periods=max(1, 252//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d hit-rate own < basket capex/rev
def f29cpr_f29_semi_capex_peer_relative_cprhit_below_504d_base_v070_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    result = (own < bas).astype(float).rolling(504, min_periods=max(1, 504//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown of own-basket spread vs peak
def f29cpr_f29_semi_capex_peer_relative_cprspread_dd_21d_base_v071_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = spread - _max(spread, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown of own-basket spread vs peak
def f29cpr_f29_semi_capex_peer_relative_cprspread_dd_63d_base_v072_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = spread - _max(spread, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown of own-basket spread vs peak
def f29cpr_f29_semi_capex_peer_relative_cprspread_dd_126d_base_v073_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = spread - _max(spread, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown of own-basket spread vs peak
def f29cpr_f29_semi_capex_peer_relative_cprspread_dd_252d_base_v074_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = spread - _max(spread, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown of own-basket spread vs peak
def f29cpr_f29_semi_capex_peer_relative_cprspread_dd_504d_base_v075_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = spread - _max(spread, 504)
    return result.replace([np.inf, -np.inf], np.nan)
