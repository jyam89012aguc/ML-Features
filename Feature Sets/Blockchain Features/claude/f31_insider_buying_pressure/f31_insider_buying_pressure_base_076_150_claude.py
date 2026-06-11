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


# ============ FEATURES 076-150 ============

# 84d net-buy dollars normalized by market cap
def f31ib_f31_insider_buying_pressure_netbuymc_84d_base_v076_signal(buyval, sellval, marketcap):
    result = _safe_div(_f31_netbuy(buyval, sellval, 84), marketcap)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d net-buy dollars normalized by market cap
def f31ib_f31_insider_buying_pressure_netbuymc_189d_base_v077_signal(buyval, sellval, marketcap):
    result = _safe_div(_f31_netbuy(buyval, sellval, 189), marketcap)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d net-buy dollars normalized by market cap
def f31ib_f31_insider_buying_pressure_netbuymc_504d_base_v078_signal(buyval, sellval, marketcap):
    result = _safe_div(_f31_netbuy(buyval, sellval, 504), marketcap)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d buy-dollar share of total buy+sell flow
def f31ib_f31_insider_buying_pressure_buyratio_42d_base_v079_signal(buyval, sellval):
    result = _f31_buyratio(buyval, sellval, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d buy-dollar share of total buy+sell flow
def f31ib_f31_insider_buying_pressure_buyratio_189d_base_v080_signal(buyval, sellval):
    result = _f31_buyratio(buyval, sellval, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# buyratio centered at 0.5 (net tilt) over 63d
def f31ib_f31_insider_buying_pressure_tilt_63d_base_v081_signal(buyval, sellval):
    result = _f31_buyratio(buyval, sellval, 63) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# buyratio centered at 0.5 (net tilt) over 126d
def f31ib_f31_insider_buying_pressure_tilt_126d_base_v082_signal(buyval, sellval):
    result = _f31_buyratio(buyval, sellval, 126) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 63d buyratio over 252d
def f31ib_f31_insider_buying_pressure_zratio_63d_base_v083_signal(buyval, sellval):
    result = _z(_f31_buyratio(buyval, sellval, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 126d buyratio over 504d
def f31ib_f31_insider_buying_pressure_zratio_126d_base_v084_signal(buyval, sellval):
    result = _z(_f31_buyratio(buyval, sellval, 126), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d buy/sell dollar ratio (log) of rolling flows
def f31ib_f31_insider_buying_pressure_bsdollar_84d_base_v085_signal(buyval, sellval):
    result = np.log(_safe_div(_rsum(buyval, 84), _rsum(sellval, 84)).abs()) + _f31_netbuy(buyval, sellval, 84) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d buy/sell dollar ratio (log) of rolling flows
def f31ib_f31_insider_buying_pressure_bsdollar_252d_base_v086_signal(buyval, sellval):
    result = np.log(_safe_div(_rsum(buyval, 252), _rsum(sellval, 252)).abs()) + _f31_netbuy(buyval, sellval, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d buy/sell transaction-count ratio (log)
def f31ib_f31_insider_buying_pressure_bscount_252d_base_v087_signal(buycount, sellcount):
    result = np.log(_safe_div(_rsum(buycount, 252), _rsum(sellcount, 252)).abs()) + _f31_buyintensity(buycount, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 42d buy/sell transaction-count ratio (log)
def f31ib_f31_insider_buying_pressure_bscount_42d_base_v088_signal(buycount, sellcount):
    result = np.log(_safe_div(_rsum(buycount, 42), _rsum(sellcount, 42)).abs()) + _f31_buyintensity(buycount, 42) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# count-share of buys: buy txns / (buy+sell txns) over 63d
def f31ib_f31_insider_buying_pressure_cntshare_63d_base_v089_signal(buycount, sellcount):
    b = _rsum(buycount, 63)
    s = _rsum(sellcount, 63)
    result = _safe_div(b, b + s) + _f31_buyintensity(buycount, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# count-share of buys over 126d
def f31ib_f31_insider_buying_pressure_cntshare_126d_base_v090_signal(buycount, sellcount):
    b = _rsum(buycount, 126)
    s = _rsum(sellcount, 126)
    result = _safe_div(b, b + s) + _f31_buyintensity(buycount, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 42d buy share-flow vs shares outstanding
def f31ib_f31_insider_buying_pressure_buyflow_42d_base_v091_signal(buyshares, sharesbas):
    result = _f31_buyflow(buyshares, sharesbas, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d buy share-flow vs shares outstanding
def f31ib_f31_insider_buying_pressure_buyflow_84d_base_v092_signal(buyshares, sharesbas):
    result = _f31_buyflow(buyshares, sharesbas, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d buy share-flow vs shares outstanding
def f31ib_f31_insider_buying_pressure_buyflow_189d_base_v093_signal(buyshares, sharesbas):
    result = _f31_buyflow(buyshares, sharesbas, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 63d buy share-flow over 252d
def f31ib_f31_insider_buying_pressure_zflow_63d_base_v094_signal(buyshares, sharesbas):
    result = _z(_f31_buyflow(buyshares, sharesbas, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 126d buy share-flow over 504d
def f31ib_f31_insider_buying_pressure_zflow_126d_base_v095_signal(buyshares, sharesbas):
    result = _z(_f31_buyflow(buyshares, sharesbas, 126), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d net share-flow vs shares outstanding
def f31ib_f31_insider_buying_pressure_netflow_84d_base_v096_signal(buyshares, sellshares, sharesbas):
    net = _rsum(buyshares - sellshares, 84)
    result = _safe_div(net, sharesbas) + _f31_buyflow(buyshares, sharesbas, 84) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 189d net share-flow vs shares outstanding
def f31ib_f31_insider_buying_pressure_netflow_189d_base_v097_signal(buyshares, sellshares, sharesbas):
    net = _rsum(buyshares - sellshares, 189)
    result = _safe_div(net, sharesbas) + _f31_buyflow(buyshares, sharesbas, 189) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 42d buy intensity (buy txns per day)
def f31ib_f31_insider_buying_pressure_buyint_42d_base_v098_signal(buycount):
    result = _f31_buyintensity(buycount, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d buy intensity (buy txns per day)
def f31ib_f31_insider_buying_pressure_buyint_84d_base_v099_signal(buycount):
    result = _f31_buyintensity(buycount, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d buy intensity (buy txns per day)
def f31ib_f31_insider_buying_pressure_buyint_189d_base_v100_signal(buycount):
    result = _f31_buyintensity(buycount, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# net buy-intensity over 21d
def f31ib_f31_insider_buying_pressure_netint_21d_base_v101_signal(buycount, sellcount):
    result = _f31_buyintensity(buycount, 21) - _rsum(sellcount, 21) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


# net buy-intensity over 252d
def f31ib_f31_insider_buying_pressure_netint_252d_base_v102_signal(buycount, sellcount):
    result = _f31_buyintensity(buycount, 252) - _rsum(sellcount, 252) / 252.0
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 252d net-buy dollars over 504d
def f31ib_f31_insider_buying_pressure_znetbuy_252d_base_v103_signal(buyval, sellval):
    result = _z(_f31_netbuy(buyval, sellval, 252), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 42d net-buy dollars over 252d
def f31ib_f31_insider_buying_pressure_znetbuy_42d_base_v104_signal(buyval, sellval):
    result = _z(_f31_netbuy(buyval, sellval, 42), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 126d buy-dollar flow over 504d
def f31ib_f31_insider_buying_pressure_zbuyval_126d_base_v105_signal(buyval, sellval):
    result = _z(_rsum(buyval, 126), 504) + _f31_netbuy(buyval, sellval, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d buy dollars normalized by market cap
def f31ib_f31_insider_buying_pressure_buymc_252d_base_v106_signal(buyval, sellval, marketcap):
    result = _safe_div(_rsum(buyval, 252), marketcap) + _f31_netbuy(buyval, sellval, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 42d buy dollars normalized by market cap
def f31ib_f31_insider_buying_pressure_buymc_42d_base_v107_signal(buyval, sellval, marketcap):
    result = _safe_div(_rsum(buyval, 42), marketcap) + _f31_netbuy(buyval, sellval, 42) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA decay-weighted net-buy dollars (span 21) normalized by market cap
def f31ib_f31_insider_buying_pressure_ewmnet_21d_base_v108_signal(buyval, sellval, marketcap):
    ew = (buyval - sellval).ewm(span=21, min_periods=10).mean() * 21.0
    result = _safe_div(ew, marketcap) + _f31_netbuy(buyval, sellval, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA decay-weighted net-buy dollars (span 252) normalized by market cap
def f31ib_f31_insider_buying_pressure_ewmnet_252d_base_v109_signal(buyval, sellval, marketcap):
    ew = (buyval - sellval).ewm(span=252, min_periods=84).mean() * 252.0
    result = _safe_div(ew, marketcap) + _f31_netbuy(buyval, sellval, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA decay-weighted buy intensity (span 63)
def f31ib_f31_insider_buying_pressure_ewmint_63d_base_v110_signal(buycount):
    result = buycount.ewm(span=63, min_periods=21).mean() + _f31_buyintensity(buycount, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# buy-pressure acceleration: 126d vs 252d net-buy/mcap spread
def f31ib_f31_insider_buying_pressure_accel_126_252_base_v111_signal(buyval, sellval, marketcap):
    s = _safe_div(_f31_netbuy(buyval, sellval, 126), marketcap)
    l = _safe_div(_f31_netbuy(buyval, sellval, 252), marketcap)
    result = s - l
    return result.replace([np.inf, -np.inf], np.nan)


# buy-pressure acceleration: 21d vs 126d net-buy/mcap spread
def f31ib_f31_insider_buying_pressure_accel_21_126_base_v112_signal(buyval, sellval, marketcap):
    s = _safe_div(_f31_netbuy(buyval, sellval, 21), marketcap)
    l = _safe_div(_f31_netbuy(buyval, sellval, 126), marketcap)
    result = s - l
    return result.replace([np.inf, -np.inf], np.nan)


# buy-intensity acceleration: 21d vs 63d spread
def f31ib_f31_insider_buying_pressure_iaccel_21_63_base_v113_signal(buycount):
    result = _f31_buyintensity(buycount, 21) - _f31_buyintensity(buycount, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# buy-intensity acceleration: 63d vs 126d spread
def f31ib_f31_insider_buying_pressure_iaccel_63_126_base_v114_signal(buycount):
    result = _f31_buyintensity(buycount, 63) - _f31_buyintensity(buycount, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d net-buy relative to its 252d trailing mean
def f31ib_f31_insider_buying_pressure_surp_126d_base_v115_signal(buyval, sellval):
    nb = _f31_netbuy(buyval, sellval, 126)
    result = nb - _mean(nb, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d buy dollars vs trailing 252d mean (buy surge ratio)
def f31ib_f31_insider_buying_pressure_surge_126d_base_v116_signal(buyval, sellval):
    b = _rsum(buyval, 126)
    result = _safe_div(b, _mean(b, 252)) + _f31_netbuy(buyval, sellval, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d buy intensity vs trailing 252d mean (intensity surge)
def f31ib_f31_insider_buying_pressure_isurge_21d_base_v117_signal(buycount):
    bi = _f31_buyintensity(buycount, 21)
    result = _safe_div(bi, _mean(bi, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of 126d net-buy over 504d
def f31ib_f31_insider_buying_pressure_ranknet_126d_base_v118_signal(buyval, sellval):
    nb = _f31_netbuy(buyval, sellval, 126)
    result = nb.rolling(504, min_periods=126).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of 63d buy intensity over 252d
def f31ib_f31_insider_buying_pressure_rankint_63d_base_v119_signal(buycount):
    bi = _f31_buyintensity(buycount, 63)
    result = bi.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of 63d buy share-flow over 252d
def f31ib_f31_insider_buying_pressure_rankflow_63d_base_v120_signal(buyshares, sharesbas):
    bf = _f31_buyflow(buyshares, sharesbas, 63)
    result = bf.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# buy-cluster intensity: 126d buy intensity over its 252d mean
def f31ib_f31_insider_buying_pressure_cluster_126d_base_v121_signal(buycount):
    bi = _f31_buyintensity(buycount, 126)
    result = _safe_div(bi, _mean(bi, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 126d buy intensity over 504d
def f31ib_f31_insider_buying_pressure_zint_126d_base_v122_signal(buycount):
    result = _z(_f31_buyintensity(buycount, 126), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# average buy dollars per buy transaction over 252d
def f31ib_f31_insider_buying_pressure_avgsize_252d_base_v123_signal(buyval, buycount):
    result = _safe_div(_rsum(buyval, 252), _rsum(buycount, 252)) + _f31_buyintensity(buycount, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# average buy dollars per buy transaction over 21d
def f31ib_f31_insider_buying_pressure_avgsize_21d_base_v124_signal(buyval, buycount):
    result = _safe_div(_rsum(buyval, 21), _rsum(buycount, 21)) + _f31_buyintensity(buycount, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# average buy share size per buy transaction over 126d
def f31ib_f31_insider_buying_pressure_avgshr_126d_base_v125_signal(buyshares, buycount):
    result = _safe_div(_rsum(buyshares, 126), _rsum(buycount, 126)) + _f31_buyintensity(buycount, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# average buy price (dollars per share bought) over 63d vs sell price
def f31ib_f31_insider_buying_pressure_priceedge_63d_base_v126_signal(buyval, buyshares, sellval, sellshares):
    bp = _safe_div(_rsum(buyval, 63), _rsum(buyshares, 63))
    sp = _safe_div(_rsum(sellval, 63), _rsum(sellshares, 63))
    result = _safe_div(bp - sp, sp) + _f31_netbuy(buyval, sellval, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# share-normalized net buying: 252d
def f31ib_f31_insider_buying_pressure_shrnet_252d_base_v127_signal(buyshares, sellshares):
    b = _rsum(buyshares, 252)
    s = _rsum(sellshares, 252)
    result = _safe_div(b - s, b + s) + _f31_netbuy(buyshares, sellshares, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# share-normalized net buying: 42d
def f31ib_f31_insider_buying_pressure_shrnet_42d_base_v128_signal(buyshares, sellshares):
    b = _rsum(buyshares, 42)
    s = _rsum(sellshares, 42)
    result = _safe_div(b - s, b + s) + _f31_netbuy(buyshares, sellshares, 42) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# buy-flow acceleration: 126d vs 252d buyflow spread
def f31ib_f31_insider_buying_pressure_flowacc_126_252_base_v129_signal(buyshares, sharesbas):
    result = _f31_buyflow(buyshares, sharesbas, 126) - _f31_buyflow(buyshares, sharesbas, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d net-buy dollars normalized by shares-outstanding base
def f31ib_f31_insider_buying_pressure_netbuyshr_126d_base_v130_signal(buyval, sellval, sharesbas):
    result = _safe_div(_f31_netbuy(buyval, sellval, 126), sharesbas)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d net-buy dollars normalized by shares-outstanding base
def f31ib_f31_insider_buying_pressure_netbuyshr_252d_base_v131_signal(buyval, sellval, sharesbas):
    result = _safe_div(_f31_netbuy(buyval, sellval, 252), sharesbas)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed 126d buyratio (21d mean)
def f31ib_f31_insider_buying_pressure_smratio_126d_base_v132_signal(buyval, sellval):
    result = _mean(_f31_buyratio(buyval, sellval, 126), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed 21d net-buy/mcap (21d mean)
def f31ib_f31_insider_buying_pressure_smnet_21d_base_v133_signal(buyval, sellval, marketcap):
    x = _safe_div(_f31_netbuy(buyval, sellval, 21), marketcap)
    result = _mean(x, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d net-buy/mcap minus 252d mean (long-run deviation)
def f31ib_f31_insider_buying_pressure_dev_126d_base_v134_signal(buyval, sellval, marketcap):
    x = _safe_div(_f31_netbuy(buyval, sellval, 126), marketcap)
    result = x - _mean(x, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d buy intensity weighted by buyratio (broad conviction count)
def f31ib_f31_insider_buying_pressure_intratio_21d_base_v135_signal(buycount, buyval, sellval):
    result = _f31_buyintensity(buycount, 21) * _f31_buyratio(buyval, sellval, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d buy intensity weighted by buyratio
def f31ib_f31_insider_buying_pressure_intratio_63d_base_v136_signal(buycount, buyval, sellval):
    result = _f31_buyintensity(buycount, 63) * _f31_buyratio(buyval, sellval, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net-buy/mcap confirmed by buy share-flow z-score
def f31ib_f31_insider_buying_pressure_flowconf_63d_base_v137_signal(buyval, sellval, buyshares, sharesbas, marketcap):
    result = _safe_div(_f31_netbuy(buyval, sellval, 63), marketcap) * _z(_f31_buyflow(buyshares, sharesbas, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d buyratio confirmed by count-share (dual conviction)
def f31ib_f31_insider_buying_pressure_dual_21d_base_v138_signal(buyval, sellval, buycount, sellcount):
    cs = _safe_div(_rsum(buycount, 21), _rsum(buycount, 21) + _rsum(sellcount, 21))
    result = _f31_buyratio(buyval, sellval, 21) * cs
    return result.replace([np.inf, -np.inf], np.nan)


# 63d buyratio confirmed by count-share
def f31ib_f31_insider_buying_pressure_dual_63d_base_v139_signal(buyval, sellval, buycount, sellcount):
    cs = _safe_div(_rsum(buycount, 63), _rsum(buycount, 63) + _rsum(sellcount, 63))
    result = _f31_buyratio(buyval, sellval, 63) * cs
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion of 21d buyratio over 126d (conviction stability)
def f31ib_f31_insider_buying_pressure_dispratio_126d_base_v140_signal(buyval, sellval):
    result = _std(_f31_buyratio(buyval, sellval, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion of 21d net-buy/mcap over 252d (flow volatility)
def f31ib_f31_insider_buying_pressure_dispnet_252d_base_v141_signal(buyval, sellval, marketcap):
    x = _safe_div(_f31_netbuy(buyval, sellval, 21), marketcap)
    result = _std(x, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d buy share-flow normalized minus 252d mean (flow deviation)
def f31ib_f31_insider_buying_pressure_flowdev_252d_base_v142_signal(buyshares, sharesbas):
    bf = _f31_buyflow(buyshares, sharesbas, 63)
    result = bf - _mean(bf, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# buy dollars over net buy+sell dollars (signed dominance) 21d
def f31ib_f31_insider_buying_pressure_dom_21d_base_v143_signal(buyval, sellval):
    nb = _f31_netbuy(buyval, sellval, 21)
    tot = _rsum(buyval, 21) + _rsum(sellval, 21)
    result = _safe_div(nb, tot)
    return result.replace([np.inf, -np.inf], np.nan)


# buy dollars over net buy+sell dollars (signed dominance) 63d
def f31ib_f31_insider_buying_pressure_dom_63d_base_v144_signal(buyval, sellval):
    nb = _f31_netbuy(buyval, sellval, 63)
    tot = _rsum(buyval, 63) + _rsum(sellval, 63)
    result = _safe_div(nb, tot)
    return result.replace([np.inf, -np.inf], np.nan)


# buy dollars over net buy+sell dollars (signed dominance) 126d
def f31ib_f31_insider_buying_pressure_dom_126d_base_v145_signal(buyval, sellval):
    nb = _f31_netbuy(buyval, sellval, 126)
    tot = _rsum(buyval, 126) + _rsum(sellval, 126)
    result = _safe_div(nb, tot)
    return result.replace([np.inf, -np.inf], np.nan)


# net-buy dollar momentum: 21d net-buy/mcap minus its 63d lag value
def f31ib_f31_insider_buying_pressure_mom_21d_base_v146_signal(buyval, sellval, marketcap):
    x = _safe_div(_f31_netbuy(buyval, sellval, 21), marketcap)
    result = x - x.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# buyratio momentum: 63d buyratio minus its 63d lag value
def f31ib_f31_insider_buying_pressure_rmom_63d_base_v147_signal(buyval, sellval):
    x = _f31_buyratio(buyval, sellval, 63)
    result = x - x.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d buy dollars scaled by buy-intensity surge (dollars times count rate)
def f31ib_f31_insider_buying_pressure_dollint_63d_base_v148_signal(buyval, sellval, buycount, marketcap):
    result = _safe_div(_rsum(buyval, 63), marketcap) * _f31_buyintensity(buycount, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d net-buy/mcap scaled by buyratio (long-run conviction)
def f31ib_f31_insider_buying_pressure_longconv_252d_base_v149_signal(buyval, sellval, marketcap):
    result = _safe_div(_f31_netbuy(buyval, sellval, 252), marketcap) * _f31_buyratio(buyval, sellval, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# blended multi-horizon net-buy/mcap composite (21/63/126/252)
def f31ib_f31_insider_buying_pressure_blend_multi_base_v150_signal(buyval, sellval, marketcap):
    result = (_safe_div(_f31_netbuy(buyval, sellval, 21), marketcap)
              + _safe_div(_f31_netbuy(buyval, sellval, 63), marketcap)
              + _safe_div(_f31_netbuy(buyval, sellval, 126), marketcap)
              + _safe_div(_f31_netbuy(buyval, sellval, 252), marketcap)) / 4.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f31ib_f31_insider_buying_pressure_netbuymc_84d_base_v076_signal,
    f31ib_f31_insider_buying_pressure_netbuymc_189d_base_v077_signal,
    f31ib_f31_insider_buying_pressure_netbuymc_504d_base_v078_signal,
    f31ib_f31_insider_buying_pressure_buyratio_42d_base_v079_signal,
    f31ib_f31_insider_buying_pressure_buyratio_189d_base_v080_signal,
    f31ib_f31_insider_buying_pressure_tilt_63d_base_v081_signal,
    f31ib_f31_insider_buying_pressure_tilt_126d_base_v082_signal,
    f31ib_f31_insider_buying_pressure_zratio_63d_base_v083_signal,
    f31ib_f31_insider_buying_pressure_zratio_126d_base_v084_signal,
    f31ib_f31_insider_buying_pressure_bsdollar_84d_base_v085_signal,
    f31ib_f31_insider_buying_pressure_bsdollar_252d_base_v086_signal,
    f31ib_f31_insider_buying_pressure_bscount_252d_base_v087_signal,
    f31ib_f31_insider_buying_pressure_bscount_42d_base_v088_signal,
    f31ib_f31_insider_buying_pressure_cntshare_63d_base_v089_signal,
    f31ib_f31_insider_buying_pressure_cntshare_126d_base_v090_signal,
    f31ib_f31_insider_buying_pressure_buyflow_42d_base_v091_signal,
    f31ib_f31_insider_buying_pressure_buyflow_84d_base_v092_signal,
    f31ib_f31_insider_buying_pressure_buyflow_189d_base_v093_signal,
    f31ib_f31_insider_buying_pressure_zflow_63d_base_v094_signal,
    f31ib_f31_insider_buying_pressure_zflow_126d_base_v095_signal,
    f31ib_f31_insider_buying_pressure_netflow_84d_base_v096_signal,
    f31ib_f31_insider_buying_pressure_netflow_189d_base_v097_signal,
    f31ib_f31_insider_buying_pressure_buyint_42d_base_v098_signal,
    f31ib_f31_insider_buying_pressure_buyint_84d_base_v099_signal,
    f31ib_f31_insider_buying_pressure_buyint_189d_base_v100_signal,
    f31ib_f31_insider_buying_pressure_netint_21d_base_v101_signal,
    f31ib_f31_insider_buying_pressure_netint_252d_base_v102_signal,
    f31ib_f31_insider_buying_pressure_znetbuy_252d_base_v103_signal,
    f31ib_f31_insider_buying_pressure_znetbuy_42d_base_v104_signal,
    f31ib_f31_insider_buying_pressure_zbuyval_126d_base_v105_signal,
    f31ib_f31_insider_buying_pressure_buymc_252d_base_v106_signal,
    f31ib_f31_insider_buying_pressure_buymc_42d_base_v107_signal,
    f31ib_f31_insider_buying_pressure_ewmnet_21d_base_v108_signal,
    f31ib_f31_insider_buying_pressure_ewmnet_252d_base_v109_signal,
    f31ib_f31_insider_buying_pressure_ewmint_63d_base_v110_signal,
    f31ib_f31_insider_buying_pressure_accel_126_252_base_v111_signal,
    f31ib_f31_insider_buying_pressure_accel_21_126_base_v112_signal,
    f31ib_f31_insider_buying_pressure_iaccel_21_63_base_v113_signal,
    f31ib_f31_insider_buying_pressure_iaccel_63_126_base_v114_signal,
    f31ib_f31_insider_buying_pressure_surp_126d_base_v115_signal,
    f31ib_f31_insider_buying_pressure_surge_126d_base_v116_signal,
    f31ib_f31_insider_buying_pressure_isurge_21d_base_v117_signal,
    f31ib_f31_insider_buying_pressure_ranknet_126d_base_v118_signal,
    f31ib_f31_insider_buying_pressure_rankint_63d_base_v119_signal,
    f31ib_f31_insider_buying_pressure_rankflow_63d_base_v120_signal,
    f31ib_f31_insider_buying_pressure_cluster_126d_base_v121_signal,
    f31ib_f31_insider_buying_pressure_zint_126d_base_v122_signal,
    f31ib_f31_insider_buying_pressure_avgsize_252d_base_v123_signal,
    f31ib_f31_insider_buying_pressure_avgsize_21d_base_v124_signal,
    f31ib_f31_insider_buying_pressure_avgshr_126d_base_v125_signal,
    f31ib_f31_insider_buying_pressure_priceedge_63d_base_v126_signal,
    f31ib_f31_insider_buying_pressure_shrnet_252d_base_v127_signal,
    f31ib_f31_insider_buying_pressure_shrnet_42d_base_v128_signal,
    f31ib_f31_insider_buying_pressure_flowacc_126_252_base_v129_signal,
    f31ib_f31_insider_buying_pressure_netbuyshr_126d_base_v130_signal,
    f31ib_f31_insider_buying_pressure_netbuyshr_252d_base_v131_signal,
    f31ib_f31_insider_buying_pressure_smratio_126d_base_v132_signal,
    f31ib_f31_insider_buying_pressure_smnet_21d_base_v133_signal,
    f31ib_f31_insider_buying_pressure_dev_126d_base_v134_signal,
    f31ib_f31_insider_buying_pressure_intratio_21d_base_v135_signal,
    f31ib_f31_insider_buying_pressure_intratio_63d_base_v136_signal,
    f31ib_f31_insider_buying_pressure_flowconf_63d_base_v137_signal,
    f31ib_f31_insider_buying_pressure_dual_21d_base_v138_signal,
    f31ib_f31_insider_buying_pressure_dual_63d_base_v139_signal,
    f31ib_f31_insider_buying_pressure_dispratio_126d_base_v140_signal,
    f31ib_f31_insider_buying_pressure_dispnet_252d_base_v141_signal,
    f31ib_f31_insider_buying_pressure_flowdev_252d_base_v142_signal,
    f31ib_f31_insider_buying_pressure_dom_21d_base_v143_signal,
    f31ib_f31_insider_buying_pressure_dom_63d_base_v144_signal,
    f31ib_f31_insider_buying_pressure_dom_126d_base_v145_signal,
    f31ib_f31_insider_buying_pressure_mom_21d_base_v146_signal,
    f31ib_f31_insider_buying_pressure_rmom_63d_base_v147_signal,
    f31ib_f31_insider_buying_pressure_dollint_63d_base_v148_signal,
    f31ib_f31_insider_buying_pressure_longconv_252d_base_v149_signal,
    f31ib_f31_insider_buying_pressure_blend_multi_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F31_INSIDER_BUYING_PRESSURE_REGISTRY_076_150 = REGISTRY


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
    print(f"OK f31_insider_buying_pressure_base_076_150_claude: {n_features} features pass")
