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


# 21d skew of own-basket spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_skew_21d_base_v001_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = spread.rolling(21, min_periods=max(1, 21//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d skew of own-basket spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_skew_63d_base_v002_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = spread.rolling(63, min_periods=max(1, 63//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d skew of own-basket spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_skew_126d_base_v003_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = spread.rolling(126, min_periods=max(1, 126//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew of own-basket spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_skew_252d_base_v004_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = spread.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew of own-basket spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_skew_504d_base_v005_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = spread.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d kurt of own-basket spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_kurt_21d_base_v006_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = spread.rolling(21, min_periods=max(1, 21//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d kurt of own-basket spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_kurt_63d_base_v007_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = spread.rolling(63, min_periods=max(1, 63//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d kurt of own-basket spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_kurt_126d_base_v008_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = spread.rolling(126, min_periods=max(1, 126//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d kurt of own-basket spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_kurt_252d_base_v009_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = spread.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d kurt of own-basket spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_kurt_504d_base_v010_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = spread.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d run-up of own-basket spread from trough
def f29cpr_f29_semi_capex_peer_relative_cprspread_runup_21d_base_v011_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = spread - _min(spread, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d run-up of own-basket spread from trough
def f29cpr_f29_semi_capex_peer_relative_cprspread_runup_63d_base_v012_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = spread - _min(spread, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d run-up of own-basket spread from trough
def f29cpr_f29_semi_capex_peer_relative_cprspread_runup_126d_base_v013_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = spread - _min(spread, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d run-up of own-basket spread from trough
def f29cpr_f29_semi_capex_peer_relative_cprspread_runup_252d_base_v014_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = spread - _min(spread, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d run-up of own-basket spread from trough
def f29cpr_f29_semi_capex_peer_relative_cprspread_runup_504d_base_v015_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = spread - _min(spread, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d signed cum of own>basket innovations
def f29cpr_f29_semi_capex_peer_relative_cprspread_signcum_21d_base_v016_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = pd.Series(np.sign(spread.diff()), index=spread.index).rolling(21, min_periods=max(1, 21//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signed cum of own>basket innovations
def f29cpr_f29_semi_capex_peer_relative_cprspread_signcum_63d_base_v017_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = pd.Series(np.sign(spread.diff()), index=spread.index).rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d signed cum of own>basket innovations
def f29cpr_f29_semi_capex_peer_relative_cprspread_signcum_126d_base_v018_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = pd.Series(np.sign(spread.diff()), index=spread.index).rolling(126, min_periods=max(1, 126//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signed cum of own>basket innovations
def f29cpr_f29_semi_capex_peer_relative_cprspread_signcum_252d_base_v019_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = pd.Series(np.sign(spread.diff()), index=spread.index).rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d signed cum of own>basket innovations
def f29cpr_f29_semi_capex_peer_relative_cprspread_signcum_504d_base_v020_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = pd.Series(np.sign(spread.diff()), index=spread.index).rolling(504, min_periods=max(1, 504//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ema(5)-ema(21) of own-basket spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_ema_21d_base_v021_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = spread.ewm(span=5, adjust=False).mean() - spread.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ema(5)-ema(63) of own-basket spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_ema_63d_base_v022_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = spread.ewm(span=5, adjust=False).mean() - spread.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ema(5)-ema(126) of own-basket spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_ema_126d_base_v023_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = spread.ewm(span=5, adjust=False).mean() - spread.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ema(5)-ema(252) of own-basket spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_ema_252d_base_v024_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = spread.ewm(span=5, adjust=False).mean() - spread.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ema(5)-ema(504) of own-basket spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_ema_504d_base_v025_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = spread.ewm(span=5, adjust=False).mean() - spread.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d deviation of spread from rolling median
def f29cpr_f29_semi_capex_peer_relative_cprspread_devmed_21d_base_v026_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    med = spread.rolling(21, min_periods=max(1, 21//2)).median()
    result = spread - med
    return result.replace([np.inf, -np.inf], np.nan)


# 63d deviation of spread from rolling median
def f29cpr_f29_semi_capex_peer_relative_cprspread_devmed_63d_base_v027_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    med = spread.rolling(63, min_periods=max(1, 63//2)).median()
    result = spread - med
    return result.replace([np.inf, -np.inf], np.nan)


# 126d deviation of spread from rolling median
def f29cpr_f29_semi_capex_peer_relative_cprspread_devmed_126d_base_v028_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    med = spread.rolling(126, min_periods=max(1, 126//2)).median()
    result = spread - med
    return result.replace([np.inf, -np.inf], np.nan)


# 252d deviation of spread from rolling median
def f29cpr_f29_semi_capex_peer_relative_cprspread_devmed_252d_base_v029_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    med = spread.rolling(252, min_periods=max(1, 252//2)).median()
    result = spread - med
    return result.replace([np.inf, -np.inf], np.nan)


# 504d deviation of spread from rolling median
def f29cpr_f29_semi_capex_peer_relative_cprspread_devmed_504d_base_v030_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    med = spread.rolling(504, min_periods=max(1, 504//2)).median()
    result = spread - med
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z log own/basket
def f29cpr_f29_semi_capex_peer_relative_cprlogratio_rz_21d_base_v031_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = np.log(own.abs().replace(0, np.nan) / bas.abs().replace(0, np.nan))
    med = r.rolling(21, min_periods=max(1, 21//2)).median()
    mad = (r - med).abs().rolling(21, min_periods=max(1, 21//2)).median()
    result = (r - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z log own/basket
def f29cpr_f29_semi_capex_peer_relative_cprlogratio_rz_63d_base_v032_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = np.log(own.abs().replace(0, np.nan) / bas.abs().replace(0, np.nan))
    med = r.rolling(63, min_periods=max(1, 63//2)).median()
    mad = (r - med).abs().rolling(63, min_periods=max(1, 63//2)).median()
    result = (r - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z log own/basket
def f29cpr_f29_semi_capex_peer_relative_cprlogratio_rz_126d_base_v033_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = np.log(own.abs().replace(0, np.nan) / bas.abs().replace(0, np.nan))
    med = r.rolling(126, min_periods=max(1, 126//2)).median()
    mad = (r - med).abs().rolling(126, min_periods=max(1, 126//2)).median()
    result = (r - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z log own/basket
def f29cpr_f29_semi_capex_peer_relative_cprlogratio_rz_252d_base_v034_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = np.log(own.abs().replace(0, np.nan) / bas.abs().replace(0, np.nan))
    med = r.rolling(252, min_periods=max(1, 252//2)).median()
    mad = (r - med).abs().rolling(252, min_periods=max(1, 252//2)).median()
    result = (r - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z log own/basket
def f29cpr_f29_semi_capex_peer_relative_cprlogratio_rz_504d_base_v035_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = np.log(own.abs().replace(0, np.nan) / bas.abs().replace(0, np.nan))
    med = r.rolling(504, min_periods=max(1, 504//2)).median()
    mad = (r - med).abs().rolling(504, min_periods=max(1, 504//2)).median()
    result = (r - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown of own/basket ratio vs peak
def f29cpr_f29_semi_capex_peer_relative_cprratio_dd_21d_base_v036_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = own / bas.replace(0, np.nan)
    result = r - _max(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown of own/basket ratio vs peak
def f29cpr_f29_semi_capex_peer_relative_cprratio_dd_63d_base_v037_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = own / bas.replace(0, np.nan)
    result = r - _max(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown of own/basket ratio vs peak
def f29cpr_f29_semi_capex_peer_relative_cprratio_dd_126d_base_v038_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = own / bas.replace(0, np.nan)
    result = r - _max(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown of own/basket ratio vs peak
def f29cpr_f29_semi_capex_peer_relative_cprratio_dd_252d_base_v039_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = own / bas.replace(0, np.nan)
    result = r - _max(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown of own/basket ratio vs peak
def f29cpr_f29_semi_capex_peer_relative_cprratio_dd_504d_base_v040_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = own / bas.replace(0, np.nan)
    result = r - _max(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z of basket capex/rev alone
def f29cpr_f29_semi_capex_peer_relative_cprbas_z_21d_base_v041_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    result = _z(bas, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z of basket capex/rev alone
def f29cpr_f29_semi_capex_peer_relative_cprbas_z_63d_base_v042_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    result = _z(bas, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z of basket capex/rev alone
def f29cpr_f29_semi_capex_peer_relative_cprbas_z_126d_base_v043_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    result = _z(bas, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z of basket capex/rev alone
def f29cpr_f29_semi_capex_peer_relative_cprbas_z_252d_base_v044_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    result = _z(bas, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z of basket capex/rev alone
def f29cpr_f29_semi_capex_peer_relative_cprbas_z_504d_base_v045_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    result = _z(bas, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of basket capex/rev alone
def f29cpr_f29_semi_capex_peer_relative_cprbas_mean_21d_base_v046_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    result = _mean(bas, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of basket capex/rev alone
def f29cpr_f29_semi_capex_peer_relative_cprbas_mean_63d_base_v047_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    result = _mean(bas, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of basket capex/rev alone
def f29cpr_f29_semi_capex_peer_relative_cprbas_mean_126d_base_v048_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    result = _mean(bas, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of basket capex/rev alone
def f29cpr_f29_semi_capex_peer_relative_cprbas_mean_252d_base_v049_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    result = _mean(bas, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of basket capex/rev alone
def f29cpr_f29_semi_capex_peer_relative_cprbas_mean_504d_base_v050_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    result = _mean(bas, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d quartile rank of own-basket spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_quart_21d_base_v051_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = spread.rolling(21, min_periods=max(1, 21//2)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d quartile rank of own-basket spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_quart_63d_base_v052_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = spread.rolling(63, min_periods=max(1, 63//2)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d quartile rank of own-basket spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_quart_126d_base_v053_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = spread.rolling(126, min_periods=max(1, 126//2)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d quartile rank of own-basket spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_quart_252d_base_v054_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = spread.rolling(252, min_periods=max(1, 252//2)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d quartile rank of own-basket spread
def f29cpr_f29_semi_capex_peer_relative_cprspread_quart_504d_base_v055_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    result = spread.rolling(504, min_periods=max(1, 504//2)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d corr own vs basket capex/rev
def f29cpr_f29_semi_capex_peer_relative_cprlead_corr_21d_base_v056_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    result = own.rolling(21, min_periods=max(2, 21//2)).corr(bas)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d corr own vs basket capex/rev
def f29cpr_f29_semi_capex_peer_relative_cprlead_corr_63d_base_v057_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    result = own.rolling(63, min_periods=max(2, 63//2)).corr(bas)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d corr own vs basket capex/rev
def f29cpr_f29_semi_capex_peer_relative_cprlead_corr_126d_base_v058_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    result = own.rolling(126, min_periods=max(2, 126//2)).corr(bas)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d corr own vs basket capex/rev
def f29cpr_f29_semi_capex_peer_relative_cprlead_corr_252d_base_v059_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    result = own.rolling(252, min_periods=max(2, 252//2)).corr(bas)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d corr own vs basket capex/rev
def f29cpr_f29_semi_capex_peer_relative_cprlead_corr_504d_base_v060_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    result = own.rolling(504, min_periods=max(2, 504//2)).corr(bas)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d beta own vs basket capex/rev
def f29cpr_f29_semi_capex_peer_relative_cprlead_beta_21d_base_v061_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    cov = own.rolling(21, min_periods=max(2, 21//2)).cov(bas)
    var = bas.rolling(21, min_periods=max(2, 21//2)).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d beta own vs basket capex/rev
def f29cpr_f29_semi_capex_peer_relative_cprlead_beta_63d_base_v062_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    cov = own.rolling(63, min_periods=max(2, 63//2)).cov(bas)
    var = bas.rolling(63, min_periods=max(2, 63//2)).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d beta own vs basket capex/rev
def f29cpr_f29_semi_capex_peer_relative_cprlead_beta_126d_base_v063_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    cov = own.rolling(126, min_periods=max(2, 126//2)).cov(bas)
    var = bas.rolling(126, min_periods=max(2, 126//2)).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d beta own vs basket capex/rev
def f29cpr_f29_semi_capex_peer_relative_cprlead_beta_252d_base_v064_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    cov = own.rolling(252, min_periods=max(2, 252//2)).cov(bas)
    var = bas.rolling(252, min_periods=max(2, 252//2)).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d beta own vs basket capex/rev
def f29cpr_f29_semi_capex_peer_relative_cprlead_beta_504d_base_v065_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    cov = own.rolling(504, min_periods=max(2, 504//2)).cov(bas)
    var = bas.rolling(504, min_periods=max(2, 504//2)).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d hit-rate spread above its rolling std band
def f29cpr_f29_semi_capex_peer_relative_cprspread_above_std_21d_base_v066_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    sd = _std(spread, 21)
    result = (spread > sd).astype(float).rolling(21, min_periods=max(1, 21//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d hit-rate spread above its rolling std band
def f29cpr_f29_semi_capex_peer_relative_cprspread_above_std_63d_base_v067_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    sd = _std(spread, 63)
    result = (spread > sd).astype(float).rolling(63, min_periods=max(1, 63//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d hit-rate spread above its rolling std band
def f29cpr_f29_semi_capex_peer_relative_cprspread_above_std_126d_base_v068_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    sd = _std(spread, 126)
    result = (spread > sd).astype(float).rolling(126, min_periods=max(1, 126//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d hit-rate spread above its rolling std band
def f29cpr_f29_semi_capex_peer_relative_cprspread_above_std_252d_base_v069_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    sd = _std(spread, 252)
    result = (spread > sd).astype(float).rolling(252, min_periods=max(1, 252//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d hit-rate spread above its rolling std band
def f29cpr_f29_semi_capex_peer_relative_cprspread_above_std_504d_base_v070_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    spread = own - bas
    sd = _std(spread, 504)
    result = (spread > sd).astype(float).rolling(504, min_periods=max(1, 504//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d composite z: own/bas ratio + spread z
def f29cpr_f29_semi_capex_peer_relative_cprcompos_z_21d_base_v071_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = own / bas.replace(0, np.nan)
    spread = own - bas
    result = _z(r, 21) + _z(spread, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite z: own/bas ratio + spread z
def f29cpr_f29_semi_capex_peer_relative_cprcompos_z_63d_base_v072_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = own / bas.replace(0, np.nan)
    spread = own - bas
    result = _z(r, 63) + _z(spread, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d composite z: own/bas ratio + spread z
def f29cpr_f29_semi_capex_peer_relative_cprcompos_z_126d_base_v073_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = own / bas.replace(0, np.nan)
    spread = own - bas
    result = _z(r, 126) + _z(spread, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite z: own/bas ratio + spread z
def f29cpr_f29_semi_capex_peer_relative_cprcompos_z_252d_base_v074_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = own / bas.replace(0, np.nan)
    spread = own - bas
    result = _z(r, 252) + _z(spread, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d composite z: own/bas ratio + spread z
def f29cpr_f29_semi_capex_peer_relative_cprcompos_z_504d_base_v075_signal(capex, revenue, semi_basket_capex_revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    own = cx / rv.replace(0, np.nan)
    bas = semi_basket_capex_revenue.reindex(closeadj.index).ffill()
    r = own / bas.replace(0, np.nan)
    spread = own - bas
    result = _z(r, 504) + _z(spread, 504)
    return result.replace([np.inf, -np.inf], np.nan)
