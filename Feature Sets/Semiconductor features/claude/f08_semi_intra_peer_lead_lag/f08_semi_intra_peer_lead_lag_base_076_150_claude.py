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
def _f08_ret(s):
    return s.pct_change()


def _f08_lag_corr(own_r, bas_r, w, lag):
    return own_r.rolling(w, min_periods=max(2, w // 2)).corr(bas_r.shift(-lag))


def _f08_lead_corr(own_r, bas_r, w, lead):
    return own_r.rolling(w, min_periods=max(2, w // 2)).corr(bas_r.shift(lead))

# 21d z-score of own-lead 1d corr
def f08ll_f08_semi_intra_peer_lead_lag_ownlead1z_21d_base_v076_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    c = _f08_lag_corr(o, b, 21, 1)
    result = _z(c, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of own-lead 1d corr
def f08ll_f08_semi_intra_peer_lead_lag_ownlead1z_63d_base_v077_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    c = _f08_lag_corr(o, b, 63, 1)
    result = _z(c, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of own-lead 1d corr
def f08ll_f08_semi_intra_peer_lead_lag_ownlead1z_126d_base_v078_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    c = _f08_lag_corr(o, b, 126, 1)
    result = _z(c, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of own-lead 1d corr
def f08ll_f08_semi_intra_peer_lead_lag_ownlead1z_252d_base_v079_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    c = _f08_lag_corr(o, b, 252, 1)
    result = _z(c, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of own-lead 1d corr
def f08ll_f08_semi_intra_peer_lead_lag_ownlead1z_504d_base_v080_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    c = _f08_lag_corr(o, b, 504, 1)
    result = _z(c, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of basket-lead 1d corr
def f08ll_f08_semi_intra_peer_lead_lag_basketlead1z_21d_base_v081_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    c = _f08_lead_corr(o, b, 21, 1)
    result = _z(c, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of basket-lead 1d corr
def f08ll_f08_semi_intra_peer_lead_lag_basketlead1z_63d_base_v082_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    c = _f08_lead_corr(o, b, 63, 1)
    result = _z(c, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of basket-lead 1d corr
def f08ll_f08_semi_intra_peer_lead_lag_basketlead1z_126d_base_v083_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    c = _f08_lead_corr(o, b, 126, 1)
    result = _z(c, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of basket-lead 1d corr
def f08ll_f08_semi_intra_peer_lead_lag_basketlead1z_252d_base_v084_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    c = _f08_lead_corr(o, b, 252, 1)
    result = _z(c, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of basket-lead 1d corr
def f08ll_f08_semi_intra_peer_lead_lag_basketlead1z_504d_base_v085_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    c = _f08_lead_corr(o, b, 504, 1)
    result = _z(c, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d beta of basket vs own lagged 1d (own leads basket beta)
def f08ll_f08_semi_intra_peer_lead_lag_ownleadbeta_21d_base_v086_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    ol = o.shift(1)
    cov = b.rolling(21, min_periods=max(2, 21 // 2)).cov(ol)
    var = ol.rolling(21, min_periods=max(2, 21 // 2)).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d beta of basket vs own lagged 1d (own leads basket beta)
def f08ll_f08_semi_intra_peer_lead_lag_ownleadbeta_63d_base_v087_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    ol = o.shift(1)
    cov = b.rolling(63, min_periods=max(2, 63 // 2)).cov(ol)
    var = ol.rolling(63, min_periods=max(2, 63 // 2)).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d beta of basket vs own lagged 1d (own leads basket beta)
def f08ll_f08_semi_intra_peer_lead_lag_ownleadbeta_126d_base_v088_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    ol = o.shift(1)
    cov = b.rolling(126, min_periods=max(2, 126 // 2)).cov(ol)
    var = ol.rolling(126, min_periods=max(2, 126 // 2)).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d beta of basket vs own lagged 1d (own leads basket beta)
def f08ll_f08_semi_intra_peer_lead_lag_ownleadbeta_252d_base_v089_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    ol = o.shift(1)
    cov = b.rolling(252, min_periods=max(2, 252 // 2)).cov(ol)
    var = ol.rolling(252, min_periods=max(2, 252 // 2)).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d beta of basket vs own lagged 1d (own leads basket beta)
def f08ll_f08_semi_intra_peer_lead_lag_ownleadbeta_504d_base_v090_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    ol = o.shift(1)
    cov = b.rolling(504, min_periods=max(2, 504 // 2)).cov(ol)
    var = ol.rolling(504, min_periods=max(2, 504 // 2)).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d beta of own vs basket lagged 1d (basket leads own beta)
def f08ll_f08_semi_intra_peer_lead_lag_basketleadbeta_21d_base_v091_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    bl = b.shift(1)
    cov = o.rolling(21, min_periods=max(2, 21 // 2)).cov(bl)
    var = bl.rolling(21, min_periods=max(2, 21 // 2)).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d beta of own vs basket lagged 1d (basket leads own beta)
def f08ll_f08_semi_intra_peer_lead_lag_basketleadbeta_63d_base_v092_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    bl = b.shift(1)
    cov = o.rolling(63, min_periods=max(2, 63 // 2)).cov(bl)
    var = bl.rolling(63, min_periods=max(2, 63 // 2)).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d beta of own vs basket lagged 1d (basket leads own beta)
def f08ll_f08_semi_intra_peer_lead_lag_basketleadbeta_126d_base_v093_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    bl = b.shift(1)
    cov = o.rolling(126, min_periods=max(2, 126 // 2)).cov(bl)
    var = bl.rolling(126, min_periods=max(2, 126 // 2)).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d beta of own vs basket lagged 1d (basket leads own beta)
def f08ll_f08_semi_intra_peer_lead_lag_basketleadbeta_252d_base_v094_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    bl = b.shift(1)
    cov = o.rolling(252, min_periods=max(2, 252 // 2)).cov(bl)
    var = bl.rolling(252, min_periods=max(2, 252 // 2)).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d beta of own vs basket lagged 1d (basket leads own beta)
def f08ll_f08_semi_intra_peer_lead_lag_basketleadbeta_504d_base_v095_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    bl = b.shift(1)
    cov = o.rolling(504, min_periods=max(2, 504 // 2)).cov(bl)
    var = bl.rolling(504, min_periods=max(2, 504 // 2)).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lead-beta asymmetry (own-leads-basket beta - basket-leads-own beta)
def f08ll_f08_semi_intra_peer_lead_lag_leadbetasym_21d_base_v096_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    ol, bl = o.shift(1), b.shift(1)
    vbl = bl.rolling(21, min_periods=max(2, 21 // 2)).var()
    vol = ol.rolling(21, min_periods=max(2, 21 // 2)).var()
    ob = b.rolling(21, min_periods=max(2, 21 // 2)).cov(ol) / vol.replace(0, np.nan)
    bo = o.rolling(21, min_periods=max(2, 21 // 2)).cov(bl) / vbl.replace(0, np.nan)
    result = ob - bo
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lead-beta asymmetry (own-leads-basket beta - basket-leads-own beta)
def f08ll_f08_semi_intra_peer_lead_lag_leadbetasym_63d_base_v097_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    ol, bl = o.shift(1), b.shift(1)
    vbl = bl.rolling(63, min_periods=max(2, 63 // 2)).var()
    vol = ol.rolling(63, min_periods=max(2, 63 // 2)).var()
    ob = b.rolling(63, min_periods=max(2, 63 // 2)).cov(ol) / vol.replace(0, np.nan)
    bo = o.rolling(63, min_periods=max(2, 63 // 2)).cov(bl) / vbl.replace(0, np.nan)
    result = ob - bo
    return result.replace([np.inf, -np.inf], np.nan)


# 126d lead-beta asymmetry (own-leads-basket beta - basket-leads-own beta)
def f08ll_f08_semi_intra_peer_lead_lag_leadbetasym_126d_base_v098_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    ol, bl = o.shift(1), b.shift(1)
    vbl = bl.rolling(126, min_periods=max(2, 126 // 2)).var()
    vol = ol.rolling(126, min_periods=max(2, 126 // 2)).var()
    ob = b.rolling(126, min_periods=max(2, 126 // 2)).cov(ol) / vol.replace(0, np.nan)
    bo = o.rolling(126, min_periods=max(2, 126 // 2)).cov(bl) / vbl.replace(0, np.nan)
    result = ob - bo
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lead-beta asymmetry (own-leads-basket beta - basket-leads-own beta)
def f08ll_f08_semi_intra_peer_lead_lag_leadbetasym_252d_base_v099_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    ol, bl = o.shift(1), b.shift(1)
    vbl = bl.rolling(252, min_periods=max(2, 252 // 2)).var()
    vol = ol.rolling(252, min_periods=max(2, 252 // 2)).var()
    ob = b.rolling(252, min_periods=max(2, 252 // 2)).cov(ol) / vol.replace(0, np.nan)
    bo = o.rolling(252, min_periods=max(2, 252 // 2)).cov(bl) / vbl.replace(0, np.nan)
    result = ob - bo
    return result.replace([np.inf, -np.inf], np.nan)


# 504d lead-beta asymmetry (own-leads-basket beta - basket-leads-own beta)
def f08ll_f08_semi_intra_peer_lead_lag_leadbetasym_504d_base_v100_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    ol, bl = o.shift(1), b.shift(1)
    vbl = bl.rolling(504, min_periods=max(2, 504 // 2)).var()
    vol = ol.rolling(504, min_periods=max(2, 504 // 2)).var()
    ob = b.rolling(504, min_periods=max(2, 504 // 2)).cov(ol) / vol.replace(0, np.nan)
    bo = o.rolling(504, min_periods=max(2, 504 // 2)).cov(bl) / vbl.replace(0, np.nan)
    result = ob - bo
    return result.replace([np.inf, -np.inf], np.nan)


# 21d argmax of corr across lags -21..21 step 3
def f08ll_f08_semi_intra_peer_lead_lag_argmaxlag21_21d_base_v101_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    lags = list(range(-21, 22, 3))
    cors = []
    for L in lags:
        cors.append(o.rolling(21, min_periods=max(2, 21 // 2)).corr(b.shift(-L)))
    df = pd.concat(cors, axis=1)
    df.columns = lags
    mask = df.notna().any(axis=1)
    result = pd.Series(np.nan, index=df.index)
    result.loc[mask] = df.loc[mask].idxmax(axis=1)
    result = result.astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d argmax of corr across lags -21..21 step 3
def f08ll_f08_semi_intra_peer_lead_lag_argmaxlag21_63d_base_v102_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    lags = list(range(-21, 22, 3))
    cors = []
    for L in lags:
        cors.append(o.rolling(63, min_periods=max(2, 63 // 2)).corr(b.shift(-L)))
    df = pd.concat(cors, axis=1)
    df.columns = lags
    mask = df.notna().any(axis=1)
    result = pd.Series(np.nan, index=df.index)
    result.loc[mask] = df.loc[mask].idxmax(axis=1)
    result = result.astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d argmax of corr across lags -21..21 step 3
def f08ll_f08_semi_intra_peer_lead_lag_argmaxlag21_126d_base_v103_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    lags = list(range(-21, 22, 3))
    cors = []
    for L in lags:
        cors.append(o.rolling(126, min_periods=max(2, 126 // 2)).corr(b.shift(-L)))
    df = pd.concat(cors, axis=1)
    df.columns = lags
    mask = df.notna().any(axis=1)
    result = pd.Series(np.nan, index=df.index)
    result.loc[mask] = df.loc[mask].idxmax(axis=1)
    result = result.astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d argmax of corr across lags -21..21 step 3
def f08ll_f08_semi_intra_peer_lead_lag_argmaxlag21_252d_base_v104_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    lags = list(range(-21, 22, 3))
    cors = []
    for L in lags:
        cors.append(o.rolling(252, min_periods=max(2, 252 // 2)).corr(b.shift(-L)))
    df = pd.concat(cors, axis=1)
    df.columns = lags
    mask = df.notna().any(axis=1)
    result = pd.Series(np.nan, index=df.index)
    result.loc[mask] = df.loc[mask].idxmax(axis=1)
    result = result.astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d argmax of corr across lags -21..21 step 3
def f08ll_f08_semi_intra_peer_lead_lag_argmaxlag21_504d_base_v105_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    lags = list(range(-21, 22, 3))
    cors = []
    for L in lags:
        cors.append(o.rolling(504, min_periods=max(2, 504 // 2)).corr(b.shift(-L)))
    df = pd.concat(cors, axis=1)
    df.columns = lags
    mask = df.notna().any(axis=1)
    result = pd.Series(np.nan, index=df.index)
    result.loc[mask] = df.loc[mask].idxmax(axis=1)
    result = result.astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max corr across lags -21..21 step 3
def f08ll_f08_semi_intra_peer_lead_lag_maxlagcorr21_21d_base_v106_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    lags = list(range(-21, 22, 3))
    cors = []
    for L in lags:
        cors.append(o.rolling(21, min_periods=max(2, 21 // 2)).corr(b.shift(-L)))
    df = pd.concat(cors, axis=1)
    result = df.max(axis=1)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max corr across lags -21..21 step 3
def f08ll_f08_semi_intra_peer_lead_lag_maxlagcorr21_63d_base_v107_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    lags = list(range(-21, 22, 3))
    cors = []
    for L in lags:
        cors.append(o.rolling(63, min_periods=max(2, 63 // 2)).corr(b.shift(-L)))
    df = pd.concat(cors, axis=1)
    result = df.max(axis=1)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max corr across lags -21..21 step 3
def f08ll_f08_semi_intra_peer_lead_lag_maxlagcorr21_126d_base_v108_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    lags = list(range(-21, 22, 3))
    cors = []
    for L in lags:
        cors.append(o.rolling(126, min_periods=max(2, 126 // 2)).corr(b.shift(-L)))
    df = pd.concat(cors, axis=1)
    result = df.max(axis=1)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max corr across lags -21..21 step 3
def f08ll_f08_semi_intra_peer_lead_lag_maxlagcorr21_252d_base_v109_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    lags = list(range(-21, 22, 3))
    cors = []
    for L in lags:
        cors.append(o.rolling(252, min_periods=max(2, 252 // 2)).corr(b.shift(-L)))
    df = pd.concat(cors, axis=1)
    result = df.max(axis=1)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max corr across lags -21..21 step 3
def f08ll_f08_semi_intra_peer_lead_lag_maxlagcorr21_504d_base_v110_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    lags = list(range(-21, 22, 3))
    cors = []
    for L in lags:
        cors.append(o.rolling(504, min_periods=max(2, 504 // 2)).corr(b.shift(-L)))
    df = pd.concat(cors, axis=1)
    result = df.max(axis=1)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cumulative spread own_ret(t-5) - basket_ret(t)
def f08ll_f08_semi_intra_peer_lead_lag_leadspread5_21d_base_v111_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    d = o.shift(5) - b
    result = d.rolling(21, min_periods=max(1, 21 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cumulative spread own_ret(t-5) - basket_ret(t)
def f08ll_f08_semi_intra_peer_lead_lag_leadspread5_63d_base_v112_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    d = o.shift(5) - b
    result = d.rolling(63, min_periods=max(1, 63 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cumulative spread own_ret(t-5) - basket_ret(t)
def f08ll_f08_semi_intra_peer_lead_lag_leadspread5_126d_base_v113_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    d = o.shift(5) - b
    result = d.rolling(126, min_periods=max(1, 126 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumulative spread own_ret(t-5) - basket_ret(t)
def f08ll_f08_semi_intra_peer_lead_lag_leadspread5_252d_base_v114_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    d = o.shift(5) - b
    result = d.rolling(252, min_periods=max(1, 252 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumulative spread own_ret(t-5) - basket_ret(t)
def f08ll_f08_semi_intra_peer_lead_lag_leadspread5_504d_base_v115_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    d = o.shift(5) - b
    result = d.rolling(504, min_periods=max(1, 504 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cumulative spread own_ret(t) - basket_ret(t-5)
def f08ll_f08_semi_intra_peer_lead_lag_lagspread5_21d_base_v116_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    d = o - b.shift(5)
    result = d.rolling(21, min_periods=max(1, 21 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cumulative spread own_ret(t) - basket_ret(t-5)
def f08ll_f08_semi_intra_peer_lead_lag_lagspread5_63d_base_v117_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    d = o - b.shift(5)
    result = d.rolling(63, min_periods=max(1, 63 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cumulative spread own_ret(t) - basket_ret(t-5)
def f08ll_f08_semi_intra_peer_lead_lag_lagspread5_126d_base_v118_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    d = o - b.shift(5)
    result = d.rolling(126, min_periods=max(1, 126 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumulative spread own_ret(t) - basket_ret(t-5)
def f08ll_f08_semi_intra_peer_lead_lag_lagspread5_252d_base_v119_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    d = o - b.shift(5)
    result = d.rolling(252, min_periods=max(1, 252 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumulative spread own_ret(t) - basket_ret(t-5)
def f08ll_f08_semi_intra_peer_lead_lag_lagspread5_504d_base_v120_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    d = o - b.shift(5)
    result = d.rolling(504, min_periods=max(1, 504 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d absolute lead-lag asymmetry at 1d (lead-lag strength)
def f08ll_f08_semi_intra_peer_lead_lag_absllasym1_21d_base_v121_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    a = _f08_lag_corr(o, b, 21, 1) - _f08_lead_corr(o, b, 21, 1)
    result = a.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d absolute lead-lag asymmetry at 1d (lead-lag strength)
def f08ll_f08_semi_intra_peer_lead_lag_absllasym1_63d_base_v122_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    a = _f08_lag_corr(o, b, 63, 1) - _f08_lead_corr(o, b, 63, 1)
    result = a.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d absolute lead-lag asymmetry at 1d (lead-lag strength)
def f08ll_f08_semi_intra_peer_lead_lag_absllasym1_126d_base_v123_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    a = _f08_lag_corr(o, b, 126, 1) - _f08_lead_corr(o, b, 126, 1)
    result = a.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d absolute lead-lag asymmetry at 1d (lead-lag strength)
def f08ll_f08_semi_intra_peer_lead_lag_absllasym1_252d_base_v124_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    a = _f08_lag_corr(o, b, 252, 1) - _f08_lead_corr(o, b, 252, 1)
    result = a.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d absolute lead-lag asymmetry at 1d (lead-lag strength)
def f08ll_f08_semi_intra_peer_lead_lag_absllasym1_504d_base_v125_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    a = _f08_lag_corr(o, b, 504, 1) - _f08_lead_corr(o, b, 504, 1)
    result = a.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sum of own-lead corrs (1,2,5) minus basket-lead corrs
def f08ll_f08_semi_intra_peer_lead_lag_sumllasym_21d_base_v126_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    ol = _f08_lag_corr(o, b, 21, 1) + _f08_lag_corr(o, b, 21, 2) + _f08_lag_corr(o, b, 21, 5)
    bl = _f08_lead_corr(o, b, 21, 1) + _f08_lead_corr(o, b, 21, 2) + _f08_lead_corr(o, b, 21, 5)
    result = ol - bl
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of own-lead corrs (1,2,5) minus basket-lead corrs
def f08ll_f08_semi_intra_peer_lead_lag_sumllasym_63d_base_v127_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    ol = _f08_lag_corr(o, b, 63, 1) + _f08_lag_corr(o, b, 63, 2) + _f08_lag_corr(o, b, 63, 5)
    bl = _f08_lead_corr(o, b, 63, 1) + _f08_lead_corr(o, b, 63, 2) + _f08_lead_corr(o, b, 63, 5)
    result = ol - bl
    return result.replace([np.inf, -np.inf], np.nan)


# 126d sum of own-lead corrs (1,2,5) minus basket-lead corrs
def f08ll_f08_semi_intra_peer_lead_lag_sumllasym_126d_base_v128_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    ol = _f08_lag_corr(o, b, 126, 1) + _f08_lag_corr(o, b, 126, 2) + _f08_lag_corr(o, b, 126, 5)
    bl = _f08_lead_corr(o, b, 126, 1) + _f08_lead_corr(o, b, 126, 2) + _f08_lead_corr(o, b, 126, 5)
    result = ol - bl
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of own-lead corrs (1,2,5) minus basket-lead corrs
def f08ll_f08_semi_intra_peer_lead_lag_sumllasym_252d_base_v129_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    ol = _f08_lag_corr(o, b, 252, 1) + _f08_lag_corr(o, b, 252, 2) + _f08_lag_corr(o, b, 252, 5)
    bl = _f08_lead_corr(o, b, 252, 1) + _f08_lead_corr(o, b, 252, 2) + _f08_lead_corr(o, b, 252, 5)
    result = ol - bl
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of own-lead corrs (1,2,5) minus basket-lead corrs
def f08ll_f08_semi_intra_peer_lead_lag_sumllasym_504d_base_v130_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    ol = _f08_lag_corr(o, b, 504, 1) + _f08_lag_corr(o, b, 504, 2) + _f08_lag_corr(o, b, 504, 5)
    bl = _f08_lead_corr(o, b, 504, 1) + _f08_lead_corr(o, b, 504, 2) + _f08_lead_corr(o, b, 504, 5)
    result = ol - bl
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lead-lag asymmetry at 1d normalized by lag-0 corr
def f08ll_f08_semi_intra_peer_lead_lag_llnorm_21d_base_v131_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    c0 = o.rolling(21, min_periods=max(2, 21 // 2)).corr(b)
    asym = _f08_lag_corr(o, b, 21, 1) - _f08_lead_corr(o, b, 21, 1)
    result = asym / c0.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lead-lag asymmetry at 1d normalized by lag-0 corr
def f08ll_f08_semi_intra_peer_lead_lag_llnorm_63d_base_v132_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    c0 = o.rolling(63, min_periods=max(2, 63 // 2)).corr(b)
    asym = _f08_lag_corr(o, b, 63, 1) - _f08_lead_corr(o, b, 63, 1)
    result = asym / c0.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d lead-lag asymmetry at 1d normalized by lag-0 corr
def f08ll_f08_semi_intra_peer_lead_lag_llnorm_126d_base_v133_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    c0 = o.rolling(126, min_periods=max(2, 126 // 2)).corr(b)
    asym = _f08_lag_corr(o, b, 126, 1) - _f08_lead_corr(o, b, 126, 1)
    result = asym / c0.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lead-lag asymmetry at 1d normalized by lag-0 corr
def f08ll_f08_semi_intra_peer_lead_lag_llnorm_252d_base_v134_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    c0 = o.rolling(252, min_periods=max(2, 252 // 2)).corr(b)
    asym = _f08_lag_corr(o, b, 252, 1) - _f08_lead_corr(o, b, 252, 1)
    result = asym / c0.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d lead-lag asymmetry at 1d normalized by lag-0 corr
def f08ll_f08_semi_intra_peer_lead_lag_llnorm_504d_base_v135_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    c0 = o.rolling(504, min_periods=max(2, 504 // 2)).corr(b)
    asym = _f08_lag_corr(o, b, 504, 1) - _f08_lead_corr(o, b, 504, 1)
    result = asym / c0.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lead decay (own-lead1 corr minus own-lead2 corr)
def f08ll_f08_semi_intra_peer_lead_lag_leaddecay_21d_base_v136_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lag_corr(o, b, 21, 1) - _f08_lag_corr(o, b, 21, 2)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lead decay (own-lead1 corr minus own-lead2 corr)
def f08ll_f08_semi_intra_peer_lead_lag_leaddecay_63d_base_v137_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lag_corr(o, b, 63, 1) - _f08_lag_corr(o, b, 63, 2)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d lead decay (own-lead1 corr minus own-lead2 corr)
def f08ll_f08_semi_intra_peer_lead_lag_leaddecay_126d_base_v138_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lag_corr(o, b, 126, 1) - _f08_lag_corr(o, b, 126, 2)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lead decay (own-lead1 corr minus own-lead2 corr)
def f08ll_f08_semi_intra_peer_lead_lag_leaddecay_252d_base_v139_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lag_corr(o, b, 252, 1) - _f08_lag_corr(o, b, 252, 2)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d lead decay (own-lead1 corr minus own-lead2 corr)
def f08ll_f08_semi_intra_peer_lead_lag_leaddecay_504d_base_v140_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lag_corr(o, b, 504, 1) - _f08_lag_corr(o, b, 504, 2)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lead decay (own-lead1 corr minus own-lead5 corr)
def f08ll_f08_semi_intra_peer_lead_lag_leaddecay5_21d_base_v141_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lag_corr(o, b, 21, 1) - _f08_lag_corr(o, b, 21, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lead decay (own-lead1 corr minus own-lead5 corr)
def f08ll_f08_semi_intra_peer_lead_lag_leaddecay5_63d_base_v142_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lag_corr(o, b, 63, 1) - _f08_lag_corr(o, b, 63, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d lead decay (own-lead1 corr minus own-lead5 corr)
def f08ll_f08_semi_intra_peer_lead_lag_leaddecay5_126d_base_v143_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lag_corr(o, b, 126, 1) - _f08_lag_corr(o, b, 126, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lead decay (own-lead1 corr minus own-lead5 corr)
def f08ll_f08_semi_intra_peer_lead_lag_leaddecay5_252d_base_v144_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lag_corr(o, b, 252, 1) - _f08_lag_corr(o, b, 252, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d lead decay (own-lead1 corr minus own-lead5 corr)
def f08ll_f08_semi_intra_peer_lead_lag_leaddecay5_504d_base_v145_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lag_corr(o, b, 504, 1) - _f08_lag_corr(o, b, 504, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# short composite: 21z + 63z + 126z of own-lead1 asymmetry
def f08ll_f08_semi_intra_peer_lead_lag_llcomposite_short_base_v146_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    a21 = _f08_lag_corr(o, b, 21, 1) - _f08_lead_corr(o, b, 21, 1)
    a63 = _f08_lag_corr(o, b, 63, 1) - _f08_lead_corr(o, b, 63, 1)
    a126 = _f08_lag_corr(o, b, 126, 1) - _f08_lead_corr(o, b, 126, 1)
    result = _z(a21, 63) + _z(a63, 126) + _z(a126, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# long composite: 63z + 126z + 252z of own-lead1 asymmetry
def f08ll_f08_semi_intra_peer_lead_lag_llcomposite_long_base_v147_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    a63 = _f08_lag_corr(o, b, 63, 1) - _f08_lead_corr(o, b, 63, 1)
    a126 = _f08_lag_corr(o, b, 126, 1) - _f08_lead_corr(o, b, 126, 1)
    a252 = _f08_lag_corr(o, b, 252, 1) - _f08_lead_corr(o, b, 252, 1)
    result = _z(a63, 126) + _z(a126, 252) + _z(a252, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# lead-lag regime divergence (short-long EMA cross sign of own-lead1 corr)
def f08ll_f08_semi_intra_peer_lead_lag_llregime_divergence_base_v148_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    c = _f08_lag_corr(o, b, 63, 1)
    short = np.sign(c.ewm(span=21, adjust=False).mean() - c.ewm(span=63, adjust=False).mean())
    long = np.sign(c.ewm(span=126, adjust=False).mean() - c.ewm(span=252, adjust=False).mean())
    result = pd.Series(short - long, index=c.index)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lead-lag quality: asymmetry / std-of-asymmetry
def f08ll_f08_semi_intra_peer_lead_lag_llquality_63d_base_v149_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    a = _f08_lag_corr(o, b, 63, 1) - _f08_lead_corr(o, b, 63, 1)
    result = a / _std(a, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lead-lag quality: asymmetry / std-of-asymmetry
def f08ll_f08_semi_intra_peer_lead_lag_llquality_252d_base_v150_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    a = _f08_lag_corr(o, b, 252, 1) - _f08_lead_corr(o, b, 252, 1)
    result = a / _std(a, 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


