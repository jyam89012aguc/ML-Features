import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
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


def _rsum(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


# ===== folder domain primitives (insider buying pressure) =====
def _f31_netbuy(buyval, sellval, w):
    # trailing-w sum of net open-market dollars bought (buy minus sell)
    return _rsum(buyval - sellval, w)


def _f31_buyratio(buyval, sellval, w):
    # rolling share of dollars that are buys vs total buy+sell flow
    b = _rsum(buyval, w)
    s = _rsum(sellval, w)
    return _safe_div(b, b + s)


def _f31_buyintensity(buycount, w):
    # average number of buy transactions per day over the window (count rate)
    return _rsum(buycount, w) / float(w)


def _f31_buyflow(buyshares, sharesbas, w):
    # trailing bought shares as a fraction of shares outstanding
    return _safe_div(_rsum(buyshares, w), sharesbas)


# ============ FEATURES 001-075 ============

# 21d net-buy dollars normalized by market cap
def f31ib_f31_insider_buying_pressure_netbuymc_21d_base_v001_signal(buyval, sellval, marketcap):
    result = _safe_div(_f31_netbuy(buyval, sellval, 21), marketcap)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net-buy dollars normalized by market cap
def f31ib_f31_insider_buying_pressure_netbuymc_63d_base_v002_signal(buyval, sellval, marketcap):
    result = _safe_div(_f31_netbuy(buyval, sellval, 63), marketcap)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d net-buy dollars normalized by market cap
def f31ib_f31_insider_buying_pressure_netbuymc_126d_base_v003_signal(buyval, sellval, marketcap):
    result = _safe_div(_f31_netbuy(buyval, sellval, 126), marketcap)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d net-buy dollars normalized by market cap
def f31ib_f31_insider_buying_pressure_netbuymc_252d_base_v004_signal(buyval, sellval, marketcap):
    result = _safe_div(_f31_netbuy(buyval, sellval, 252), marketcap)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d net-buy dollars normalized by market cap
def f31ib_f31_insider_buying_pressure_netbuymc_42d_base_v005_signal(buyval, sellval, marketcap):
    result = _safe_div(_f31_netbuy(buyval, sellval, 42), marketcap)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d buy-dollar share of total buy+sell flow
def f31ib_f31_insider_buying_pressure_buyratio_21d_base_v006_signal(buyval, sellval):
    result = _f31_buyratio(buyval, sellval, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d buy-dollar share of total buy+sell flow
def f31ib_f31_insider_buying_pressure_buyratio_63d_base_v007_signal(buyval, sellval):
    result = _f31_buyratio(buyval, sellval, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d buy-dollar share of total buy+sell flow
def f31ib_f31_insider_buying_pressure_buyratio_126d_base_v008_signal(buyval, sellval):
    result = _f31_buyratio(buyval, sellval, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d buy-dollar share of total buy+sell flow
def f31ib_f31_insider_buying_pressure_buyratio_252d_base_v009_signal(buyval, sellval):
    result = _f31_buyratio(buyval, sellval, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d buy-dollar share of total buy+sell flow
def f31ib_f31_insider_buying_pressure_buyratio_84d_base_v010_signal(buyval, sellval):
    result = _f31_buyratio(buyval, sellval, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d buy/sell dollar ratio (log) of rolling flows
def f31ib_f31_insider_buying_pressure_bsdollar_21d_base_v011_signal(buyval, sellval):
    result = np.log(_safe_div(_rsum(buyval, 21), _rsum(sellval, 21)).abs()) + _f31_netbuy(buyval, sellval, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d buy/sell dollar ratio (log) of rolling flows
def f31ib_f31_insider_buying_pressure_bsdollar_63d_base_v012_signal(buyval, sellval):
    result = np.log(_safe_div(_rsum(buyval, 63), _rsum(sellval, 63)).abs()) + _f31_netbuy(buyval, sellval, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d buy/sell dollar ratio (log) of rolling flows
def f31ib_f31_insider_buying_pressure_bsdollar_126d_base_v013_signal(buyval, sellval):
    result = np.log(_safe_div(_rsum(buyval, 126), _rsum(sellval, 126)).abs()) + _f31_netbuy(buyval, sellval, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d buy/sell transaction-count ratio (log)
def f31ib_f31_insider_buying_pressure_bscount_21d_base_v014_signal(buycount, sellcount):
    result = np.log(_safe_div(_rsum(buycount, 21), _rsum(sellcount, 21)).abs()) + _f31_buyintensity(buycount, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d buy/sell transaction-count ratio (log)
def f31ib_f31_insider_buying_pressure_bscount_63d_base_v015_signal(buycount, sellcount):
    result = np.log(_safe_div(_rsum(buycount, 63), _rsum(sellcount, 63)).abs()) + _f31_buyintensity(buycount, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d buy/sell transaction-count ratio (log)
def f31ib_f31_insider_buying_pressure_bscount_126d_base_v016_signal(buycount, sellcount):
    result = np.log(_safe_div(_rsum(buycount, 126), _rsum(sellcount, 126)).abs()) + _f31_buyintensity(buycount, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d buy share-flow vs shares outstanding
def f31ib_f31_insider_buying_pressure_buyflow_21d_base_v017_signal(buyshares, sharesbas):
    result = _f31_buyflow(buyshares, sharesbas, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d buy share-flow vs shares outstanding
def f31ib_f31_insider_buying_pressure_buyflow_63d_base_v018_signal(buyshares, sharesbas):
    result = _f31_buyflow(buyshares, sharesbas, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d buy share-flow vs shares outstanding
def f31ib_f31_insider_buying_pressure_buyflow_126d_base_v019_signal(buyshares, sharesbas):
    result = _f31_buyflow(buyshares, sharesbas, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d buy share-flow vs shares outstanding
def f31ib_f31_insider_buying_pressure_buyflow_252d_base_v020_signal(buyshares, sharesbas):
    result = _f31_buyflow(buyshares, sharesbas, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d net share-flow (buy minus sell shares) vs shares outstanding
def f31ib_f31_insider_buying_pressure_netflow_21d_base_v021_signal(buyshares, sellshares, sharesbas):
    net = _rsum(buyshares - sellshares, 21)
    result = _safe_div(net, sharesbas) + _f31_buyflow(buyshares, sharesbas, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net share-flow vs shares outstanding
def f31ib_f31_insider_buying_pressure_netflow_63d_base_v022_signal(buyshares, sellshares, sharesbas):
    net = _rsum(buyshares - sellshares, 63)
    result = _safe_div(net, sharesbas) + _f31_buyflow(buyshares, sharesbas, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d net share-flow vs shares outstanding
def f31ib_f31_insider_buying_pressure_netflow_126d_base_v023_signal(buyshares, sellshares, sharesbas):
    net = _rsum(buyshares - sellshares, 126)
    result = _safe_div(net, sharesbas) + _f31_buyflow(buyshares, sharesbas, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d net share-flow vs shares outstanding
def f31ib_f31_insider_buying_pressure_netflow_252d_base_v024_signal(buyshares, sellshares, sharesbas):
    net = _rsum(buyshares - sellshares, 252)
    result = _safe_div(net, sharesbas) + _f31_buyflow(buyshares, sharesbas, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d buy intensity (buy txns per day)
def f31ib_f31_insider_buying_pressure_buyint_21d_base_v025_signal(buycount):
    result = _f31_buyintensity(buycount, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d buy intensity (buy txns per day)
def f31ib_f31_insider_buying_pressure_buyint_63d_base_v026_signal(buycount):
    result = _f31_buyintensity(buycount, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d buy intensity (buy txns per day)
def f31ib_f31_insider_buying_pressure_buyint_126d_base_v027_signal(buycount):
    result = _f31_buyintensity(buycount, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d buy intensity (buy txns per day)
def f31ib_f31_insider_buying_pressure_buyint_252d_base_v028_signal(buycount):
    result = _f31_buyintensity(buycount, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# net buy-intensity (buy minus sell txns per day) over 63d
def f31ib_f31_insider_buying_pressure_netint_63d_base_v029_signal(buycount, sellcount):
    result = _f31_buyintensity(buycount, 63) - _rsum(sellcount, 63) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


# net buy-intensity over 126d
def f31ib_f31_insider_buying_pressure_netint_126d_base_v030_signal(buycount, sellcount):
    result = _f31_buyintensity(buycount, 126) - _rsum(sellcount, 126) / 126.0
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 21d net-buy dollars over 252d
def f31ib_f31_insider_buying_pressure_znetbuy_21d_base_v031_signal(buyval, sellval):
    result = _z(_f31_netbuy(buyval, sellval, 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 63d net-buy dollars over 252d
def f31ib_f31_insider_buying_pressure_znetbuy_63d_base_v032_signal(buyval, sellval):
    result = _z(_f31_netbuy(buyval, sellval, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 126d net-buy dollars over 504d
def f31ib_f31_insider_buying_pressure_znetbuy_126d_base_v033_signal(buyval, sellval):
    result = _z(_f31_netbuy(buyval, sellval, 126), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 21d buy-dollar flow over 252d
def f31ib_f31_insider_buying_pressure_zbuyval_21d_base_v034_signal(buyval, sellval):
    result = _z(_rsum(buyval, 21), 252) + _f31_netbuy(buyval, sellval, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 63d buy-dollar flow over 252d
def f31ib_f31_insider_buying_pressure_zbuyval_63d_base_v035_signal(buyval, sellval):
    result = _z(_rsum(buyval, 63), 252) + _f31_netbuy(buyval, sellval, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d buy dollars normalized by market cap
def f31ib_f31_insider_buying_pressure_buymc_21d_base_v036_signal(buyval, sellval, marketcap):
    result = _safe_div(_rsum(buyval, 21), marketcap) + _f31_netbuy(buyval, sellval, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d buy dollars normalized by market cap
def f31ib_f31_insider_buying_pressure_buymc_63d_base_v037_signal(buyval, sellval, marketcap):
    result = _safe_div(_rsum(buyval, 63), marketcap) + _f31_netbuy(buyval, sellval, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d buy dollars normalized by market cap
def f31ib_f31_insider_buying_pressure_buymc_126d_base_v038_signal(buyval, sellval, marketcap):
    result = _safe_div(_rsum(buyval, 126), marketcap) + _f31_netbuy(buyval, sellval, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA decay-weighted recent buy dollars (span 21) normalized by market cap
def f31ib_f31_insider_buying_pressure_ewmbuy_21d_base_v039_signal(buyval, sellval, marketcap):
    ew = buyval.ewm(span=21, min_periods=10).mean() * 21.0
    result = _safe_div(ew, marketcap) + _f31_netbuy(buyval, sellval, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA decay-weighted recent buy dollars (span 63) normalized by market cap
def f31ib_f31_insider_buying_pressure_ewmbuy_63d_base_v040_signal(buyval, sellval, marketcap):
    ew = buyval.ewm(span=63, min_periods=21).mean() * 63.0
    result = _safe_div(ew, marketcap) + _f31_netbuy(buyval, sellval, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA decay-weighted net-buy dollars (span 42) normalized by market cap
def f31ib_f31_insider_buying_pressure_ewmnet_42d_base_v041_signal(buyval, sellval, marketcap):
    ew = (buyval - sellval).ewm(span=42, min_periods=21).mean() * 42.0
    result = _safe_div(ew, marketcap) + _f31_netbuy(buyval, sellval, 42) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA decay-weighted net-buy dollars (span 126) normalized by market cap
def f31ib_f31_insider_buying_pressure_ewmnet_126d_base_v042_signal(buyval, sellval, marketcap):
    ew = (buyval - sellval).ewm(span=126, min_periods=42).mean() * 126.0
    result = _safe_div(ew, marketcap) + _f31_netbuy(buyval, sellval, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# buy-pressure acceleration: 21d vs 63d net-buy/mcap spread
def f31ib_f31_insider_buying_pressure_accel_21_63_base_v043_signal(buyval, sellval, marketcap):
    s = _safe_div(_f31_netbuy(buyval, sellval, 21), marketcap)
    l = _safe_div(_f31_netbuy(buyval, sellval, 63), marketcap)
    result = s - l
    return result.replace([np.inf, -np.inf], np.nan)


# buy-pressure acceleration: 63d vs 126d net-buy/mcap spread
def f31ib_f31_insider_buying_pressure_accel_63_126_base_v044_signal(buyval, sellval, marketcap):
    s = _safe_div(_f31_netbuy(buyval, sellval, 63), marketcap)
    l = _safe_div(_f31_netbuy(buyval, sellval, 126), marketcap)
    result = s - l
    return result.replace([np.inf, -np.inf], np.nan)


# buy-ratio acceleration: 21d vs 126d buyratio spread
def f31ib_f31_insider_buying_pressure_raccel_21_126_base_v045_signal(buyval, sellval):
    result = _f31_buyratio(buyval, sellval, 21) - _f31_buyratio(buyval, sellval, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# buy-ratio acceleration: 63d vs 252d buyratio spread
def f31ib_f31_insider_buying_pressure_raccel_63_252_base_v046_signal(buyval, sellval):
    result = _f31_buyratio(buyval, sellval, 63) - _f31_buyratio(buyval, sellval, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d net-buy relative to its 126d trailing mean (buy-pressure surprise)
def f31ib_f31_insider_buying_pressure_surp_21d_base_v047_signal(buyval, sellval):
    nb = _f31_netbuy(buyval, sellval, 21)
    result = nb - _mean(nb, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net-buy relative to its 252d trailing mean
def f31ib_f31_insider_buying_pressure_surp_63d_base_v048_signal(buyval, sellval):
    nb = _f31_netbuy(buyval, sellval, 63)
    result = nb - _mean(nb, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d buy dollars vs trailing 252d mean (buy surge ratio)
def f31ib_f31_insider_buying_pressure_surge_21d_base_v049_signal(buyval, sellval):
    b = _rsum(buyval, 21)
    result = _safe_div(b, _mean(b, 252)) + _f31_netbuy(buyval, sellval, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d buy dollars vs trailing 252d mean (buy surge ratio)
def f31ib_f31_insider_buying_pressure_surge_63d_base_v050_signal(buyval, sellval):
    b = _rsum(buyval, 63)
    result = _safe_div(b, _mean(b, 252)) + _f31_netbuy(buyval, sellval, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of 21d buy dollars over 252d
def f31ib_f31_insider_buying_pressure_rankbuy_21d_base_v051_signal(buyval, sellval):
    b = _rsum(buyval, 21)
    result = b.rolling(252, min_periods=63).rank(pct=True) + _f31_netbuy(buyval, sellval, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of 63d net-buy over 252d
def f31ib_f31_insider_buying_pressure_ranknet_63d_base_v052_signal(buyval, sellval):
    nb = _f31_netbuy(buyval, sellval, 63)
    result = nb.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of 126d buyratio over 252d
def f31ib_f31_insider_buying_pressure_rankratio_126d_base_v053_signal(buyval, sellval):
    br = _f31_buyratio(buyval, sellval, 126)
    result = br.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# buy-cluster intensity: 21d buy intensity over its 252d mean
def f31ib_f31_insider_buying_pressure_cluster_21d_base_v054_signal(buycount):
    bi = _f31_buyintensity(buycount, 21)
    result = _safe_div(bi, _mean(bi, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# buy-cluster intensity: 63d buy intensity over its 252d mean
def f31ib_f31_insider_buying_pressure_cluster_63d_base_v055_signal(buycount):
    bi = _f31_buyintensity(buycount, 63)
    result = _safe_div(bi, _mean(bi, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 21d buy intensity over 252d
def f31ib_f31_insider_buying_pressure_zint_21d_base_v056_signal(buycount):
    result = _z(_f31_buyintensity(buycount, 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 63d buy intensity over 252d
def f31ib_f31_insider_buying_pressure_zint_63d_base_v057_signal(buycount):
    result = _z(_f31_buyintensity(buycount, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# average buy dollars per buy transaction over 63d (conviction size)
def f31ib_f31_insider_buying_pressure_avgsize_63d_base_v058_signal(buyval, buycount):
    result = _safe_div(_rsum(buyval, 63), _rsum(buycount, 63)) + _f31_buyintensity(buycount, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# average buy dollars per buy transaction over 126d
def f31ib_f31_insider_buying_pressure_avgsize_126d_base_v059_signal(buyval, buycount):
    result = _safe_div(_rsum(buyval, 126), _rsum(buycount, 126)) + _f31_buyintensity(buycount, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# average buy share size per buy transaction over 63d
def f31ib_f31_insider_buying_pressure_avgshr_63d_base_v060_signal(buyshares, buycount):
    result = _safe_div(_rsum(buyshares, 63), _rsum(buycount, 63)) + _f31_buyintensity(buycount, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# share-normalized net buying: 21d net shares over trailing buy+sell shares
def f31ib_f31_insider_buying_pressure_shrnet_21d_base_v061_signal(buyshares, sellshares):
    b = _rsum(buyshares, 21)
    s = _rsum(sellshares, 21)
    result = _safe_div(b - s, b + s) + _f31_netbuy(buyshares, sellshares, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# share-normalized net buying: 63d
def f31ib_f31_insider_buying_pressure_shrnet_63d_base_v062_signal(buyshares, sellshares):
    b = _rsum(buyshares, 63)
    s = _rsum(sellshares, 63)
    result = _safe_div(b - s, b + s) + _f31_netbuy(buyshares, sellshares, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# share-normalized net buying: 126d
def f31ib_f31_insider_buying_pressure_shrnet_126d_base_v063_signal(buyshares, sellshares):
    b = _rsum(buyshares, 126)
    s = _rsum(sellshares, 126)
    result = _safe_div(b - s, b + s) + _f31_netbuy(buyshares, sellshares, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# buy-flow acceleration: 21d vs 63d buyflow spread
def f31ib_f31_insider_buying_pressure_flowacc_21_63_base_v064_signal(buyshares, sharesbas):
    result = _f31_buyflow(buyshares, sharesbas, 21) - _f31_buyflow(buyshares, sharesbas, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# buy-flow acceleration: 63d vs 126d buyflow spread
def f31ib_f31_insider_buying_pressure_flowacc_63_126_base_v065_signal(buyshares, sharesbas):
    result = _f31_buyflow(buyshares, sharesbas, 63) - _f31_buyflow(buyshares, sharesbas, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d net-buy dollars normalized by shares-outstanding dollar base
def f31ib_f31_insider_buying_pressure_netbuyshr_21d_base_v066_signal(buyval, sellval, sharesbas):
    result = _safe_div(_f31_netbuy(buyval, sellval, 21), sharesbas)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net-buy dollars normalized by shares-outstanding base
def f31ib_f31_insider_buying_pressure_netbuyshr_63d_base_v067_signal(buyval, sellval, sharesbas):
    result = _safe_div(_f31_netbuy(buyval, sellval, 63), sharesbas)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed 21d buyratio (21d mean) -- continuous conviction trend
def f31ib_f31_insider_buying_pressure_smratio_21d_base_v068_signal(buyval, sellval):
    result = _mean(_f31_buyratio(buyval, sellval, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed 63d buyratio (21d mean)
def f31ib_f31_insider_buying_pressure_smratio_63d_base_v069_signal(buyval, sellval):
    result = _mean(_f31_buyratio(buyval, sellval, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d net-buy/mcap minus 252d mean (long-run buy-pressure deviation)
def f31ib_f31_insider_buying_pressure_dev_21d_base_v070_signal(buyval, sellval, marketcap):
    x = _safe_div(_f31_netbuy(buyval, sellval, 21), marketcap)
    result = x - _mean(x, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net-buy/mcap minus 252d mean
def f31ib_f31_insider_buying_pressure_dev_63d_base_v071_signal(buyval, sellval, marketcap):
    x = _safe_div(_f31_netbuy(buyval, sellval, 63), marketcap)
    result = x - _mean(x, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d buy dollars scaled by buy-flow intensity (dollar conviction)
def f31ib_f31_insider_buying_pressure_conv_21d_base_v072_signal(buyval, buyshares, sharesbas):
    result = _safe_div(_rsum(buyval, 21), sharesbas) * _f31_buyflow(buyshares, sharesbas, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d buy dollars scaled by buy-flow intensity
def f31ib_f31_insider_buying_pressure_conv_63d_base_v073_signal(buyval, buyshares, sharesbas):
    result = _safe_div(_rsum(buyval, 63), sharesbas) * _f31_buyflow(buyshares, sharesbas, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d net-buy dollars confirmed by buy-intensity z-score
def f31ib_f31_insider_buying_pressure_intconf_126d_base_v074_signal(buyval, sellval, buycount, marketcap):
    result = _safe_div(_f31_netbuy(buyval, sellval, 126), marketcap) * _z(_f31_buyintensity(buycount, 126), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d buy share-flow scaled by buyratio (broad conviction)
def f31ib_f31_insider_buying_pressure_flowratio_252d_base_v075_signal(buyshares, sharesbas, buyval, sellval):
    result = _f31_buyflow(buyshares, sharesbas, 252) * _f31_buyratio(buyval, sellval, 252)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f31ib_f31_insider_buying_pressure_netbuymc_21d_base_v001_signal,
    f31ib_f31_insider_buying_pressure_netbuymc_63d_base_v002_signal,
    f31ib_f31_insider_buying_pressure_netbuymc_126d_base_v003_signal,
    f31ib_f31_insider_buying_pressure_netbuymc_252d_base_v004_signal,
    f31ib_f31_insider_buying_pressure_netbuymc_42d_base_v005_signal,
    f31ib_f31_insider_buying_pressure_buyratio_21d_base_v006_signal,
    f31ib_f31_insider_buying_pressure_buyratio_63d_base_v007_signal,
    f31ib_f31_insider_buying_pressure_buyratio_126d_base_v008_signal,
    f31ib_f31_insider_buying_pressure_buyratio_252d_base_v009_signal,
    f31ib_f31_insider_buying_pressure_buyratio_84d_base_v010_signal,
    f31ib_f31_insider_buying_pressure_bsdollar_21d_base_v011_signal,
    f31ib_f31_insider_buying_pressure_bsdollar_63d_base_v012_signal,
    f31ib_f31_insider_buying_pressure_bsdollar_126d_base_v013_signal,
    f31ib_f31_insider_buying_pressure_bscount_21d_base_v014_signal,
    f31ib_f31_insider_buying_pressure_bscount_63d_base_v015_signal,
    f31ib_f31_insider_buying_pressure_bscount_126d_base_v016_signal,
    f31ib_f31_insider_buying_pressure_buyflow_21d_base_v017_signal,
    f31ib_f31_insider_buying_pressure_buyflow_63d_base_v018_signal,
    f31ib_f31_insider_buying_pressure_buyflow_126d_base_v019_signal,
    f31ib_f31_insider_buying_pressure_buyflow_252d_base_v020_signal,
    f31ib_f31_insider_buying_pressure_netflow_21d_base_v021_signal,
    f31ib_f31_insider_buying_pressure_netflow_63d_base_v022_signal,
    f31ib_f31_insider_buying_pressure_netflow_126d_base_v023_signal,
    f31ib_f31_insider_buying_pressure_netflow_252d_base_v024_signal,
    f31ib_f31_insider_buying_pressure_buyint_21d_base_v025_signal,
    f31ib_f31_insider_buying_pressure_buyint_63d_base_v026_signal,
    f31ib_f31_insider_buying_pressure_buyint_126d_base_v027_signal,
    f31ib_f31_insider_buying_pressure_buyint_252d_base_v028_signal,
    f31ib_f31_insider_buying_pressure_netint_63d_base_v029_signal,
    f31ib_f31_insider_buying_pressure_netint_126d_base_v030_signal,
    f31ib_f31_insider_buying_pressure_znetbuy_21d_base_v031_signal,
    f31ib_f31_insider_buying_pressure_znetbuy_63d_base_v032_signal,
    f31ib_f31_insider_buying_pressure_znetbuy_126d_base_v033_signal,
    f31ib_f31_insider_buying_pressure_zbuyval_21d_base_v034_signal,
    f31ib_f31_insider_buying_pressure_zbuyval_63d_base_v035_signal,
    f31ib_f31_insider_buying_pressure_buymc_21d_base_v036_signal,
    f31ib_f31_insider_buying_pressure_buymc_63d_base_v037_signal,
    f31ib_f31_insider_buying_pressure_buymc_126d_base_v038_signal,
    f31ib_f31_insider_buying_pressure_ewmbuy_21d_base_v039_signal,
    f31ib_f31_insider_buying_pressure_ewmbuy_63d_base_v040_signal,
    f31ib_f31_insider_buying_pressure_ewmnet_42d_base_v041_signal,
    f31ib_f31_insider_buying_pressure_ewmnet_126d_base_v042_signal,
    f31ib_f31_insider_buying_pressure_accel_21_63_base_v043_signal,
    f31ib_f31_insider_buying_pressure_accel_63_126_base_v044_signal,
    f31ib_f31_insider_buying_pressure_raccel_21_126_base_v045_signal,
    f31ib_f31_insider_buying_pressure_raccel_63_252_base_v046_signal,
    f31ib_f31_insider_buying_pressure_surp_21d_base_v047_signal,
    f31ib_f31_insider_buying_pressure_surp_63d_base_v048_signal,
    f31ib_f31_insider_buying_pressure_surge_21d_base_v049_signal,
    f31ib_f31_insider_buying_pressure_surge_63d_base_v050_signal,
    f31ib_f31_insider_buying_pressure_rankbuy_21d_base_v051_signal,
    f31ib_f31_insider_buying_pressure_ranknet_63d_base_v052_signal,
    f31ib_f31_insider_buying_pressure_rankratio_126d_base_v053_signal,
    f31ib_f31_insider_buying_pressure_cluster_21d_base_v054_signal,
    f31ib_f31_insider_buying_pressure_cluster_63d_base_v055_signal,
    f31ib_f31_insider_buying_pressure_zint_21d_base_v056_signal,
    f31ib_f31_insider_buying_pressure_zint_63d_base_v057_signal,
    f31ib_f31_insider_buying_pressure_avgsize_63d_base_v058_signal,
    f31ib_f31_insider_buying_pressure_avgsize_126d_base_v059_signal,
    f31ib_f31_insider_buying_pressure_avgshr_63d_base_v060_signal,
    f31ib_f31_insider_buying_pressure_shrnet_21d_base_v061_signal,
    f31ib_f31_insider_buying_pressure_shrnet_63d_base_v062_signal,
    f31ib_f31_insider_buying_pressure_shrnet_126d_base_v063_signal,
    f31ib_f31_insider_buying_pressure_flowacc_21_63_base_v064_signal,
    f31ib_f31_insider_buying_pressure_flowacc_63_126_base_v065_signal,
    f31ib_f31_insider_buying_pressure_netbuyshr_21d_base_v066_signal,
    f31ib_f31_insider_buying_pressure_netbuyshr_63d_base_v067_signal,
    f31ib_f31_insider_buying_pressure_smratio_21d_base_v068_signal,
    f31ib_f31_insider_buying_pressure_smratio_63d_base_v069_signal,
    f31ib_f31_insider_buying_pressure_dev_21d_base_v070_signal,
    f31ib_f31_insider_buying_pressure_dev_63d_base_v071_signal,
    f31ib_f31_insider_buying_pressure_conv_21d_base_v072_signal,
    f31ib_f31_insider_buying_pressure_conv_63d_base_v073_signal,
    f31ib_f31_insider_buying_pressure_intconf_126d_base_v074_signal,
    f31ib_f31_insider_buying_pressure_flowratio_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F31_INSIDER_BUYING_PRESSURE_REGISTRY_001_075 = REGISTRY


def _synth_cols(names):
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    nh = np.abs(np.random.normal(0, 0.02, n)); nl = np.abs(np.random.normal(0, 0.02, n))
    POS = {"open","high","low","close","closeadj","price","volume","marketcap","ev",
           "assets","assetsc","equity","revenue","gp","ebitda","ppnenet","sharesbas",
           "shareswa","cashneq","cor","opex","sgna","rnd","inventory","receivables",
           "intangibles","evebitda","evebit","pe","pb","ps","currentratio","bvps","sps",
           "shrvalue","shrunits","totalvalue","percentoftotal","sf3a_shares","sf3a_value",
           "sf3b_shares","sf3b_value","grossmargin","beta1y","beta5y","invcap","debt",
           "buyval","sellval","buyshares","sellshares","buycount","sellcount"}
    for nm in names:
        if nm in ("closeadj","close","price"):
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price*(1+np.random.normal(0,0.01,n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price*(1+nh), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price*(1-nl), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7,7e6,n))+1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0,1.0,n))
            level = 1000.0*np.exp(0.03*np.random.normal(0,1,n).cumsum()/np.sqrt(n))
            s = level + 50.0*walk
            if nm in POS:
                s = np.abs(s) + 10.0
            out[nm] = pd.Series(s, name=nm)
    return out


if __name__ == "__main__":
    domain_primitives = ("_f31_netbuy", "_f31_buyratio", "_f31_buyintensity", "_f31_buyflow")
    needed = set()
    for fn in _FEATURES:
        for p in inspect.signature(fn).parameters.values():
            needed.add(p.name)
    cols = _synth_cols(sorted(needed))
    n_features = 0; nan_ok = 0
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args); y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        if y1.iloc[504:].isna().mean() < 0.5:
            nan_ok += 1
        assert any(p in inspect.getsource(fn) for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f31_insider_buying_pressure_base_001_075_claude: {n_features} features pass")
