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

# 21d corr at lag 0 (contemporaneous)
def f08ll_f08_semi_intra_peer_lead_lag_corr0_21d_base_v001_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = o.rolling(21, min_periods=max(2, 21 // 2)).corr(b)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d corr at lag 0 (contemporaneous)
def f08ll_f08_semi_intra_peer_lead_lag_corr0_63d_base_v002_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = o.rolling(63, min_periods=max(2, 63 // 2)).corr(b)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d corr at lag 0 (contemporaneous)
def f08ll_f08_semi_intra_peer_lead_lag_corr0_126d_base_v003_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = o.rolling(126, min_periods=max(2, 126 // 2)).corr(b)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d corr at lag 0 (contemporaneous)
def f08ll_f08_semi_intra_peer_lead_lag_corr0_252d_base_v004_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = o.rolling(252, min_periods=max(2, 252 // 2)).corr(b)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d corr at lag 0 (contemporaneous)
def f08ll_f08_semi_intra_peer_lead_lag_corr0_504d_base_v005_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = o.rolling(504, min_periods=max(2, 504 // 2)).corr(b)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d corr own vs basket shifted +1d (basket leads own)
def f08ll_f08_semi_intra_peer_lead_lag_basketlead1_21d_base_v006_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lead_corr(o, b, 21, 1)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d corr own vs basket shifted +1d (basket leads own)
def f08ll_f08_semi_intra_peer_lead_lag_basketlead1_63d_base_v007_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lead_corr(o, b, 63, 1)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d corr own vs basket shifted +1d (basket leads own)
def f08ll_f08_semi_intra_peer_lead_lag_basketlead1_126d_base_v008_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lead_corr(o, b, 126, 1)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d corr own vs basket shifted +1d (basket leads own)
def f08ll_f08_semi_intra_peer_lead_lag_basketlead1_252d_base_v009_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lead_corr(o, b, 252, 1)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d corr own vs basket shifted +1d (basket leads own)
def f08ll_f08_semi_intra_peer_lead_lag_basketlead1_504d_base_v010_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lead_corr(o, b, 504, 1)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d corr own vs basket shifted +2d
def f08ll_f08_semi_intra_peer_lead_lag_basketlead2_21d_base_v011_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lead_corr(o, b, 21, 2)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d corr own vs basket shifted +2d
def f08ll_f08_semi_intra_peer_lead_lag_basketlead2_63d_base_v012_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lead_corr(o, b, 63, 2)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d corr own vs basket shifted +2d
def f08ll_f08_semi_intra_peer_lead_lag_basketlead2_126d_base_v013_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lead_corr(o, b, 126, 2)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d corr own vs basket shifted +2d
def f08ll_f08_semi_intra_peer_lead_lag_basketlead2_252d_base_v014_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lead_corr(o, b, 252, 2)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d corr own vs basket shifted +2d
def f08ll_f08_semi_intra_peer_lead_lag_basketlead2_504d_base_v015_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lead_corr(o, b, 504, 2)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d corr own vs basket shifted +5d
def f08ll_f08_semi_intra_peer_lead_lag_basketlead5_21d_base_v016_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lead_corr(o, b, 21, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d corr own vs basket shifted +5d
def f08ll_f08_semi_intra_peer_lead_lag_basketlead5_63d_base_v017_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lead_corr(o, b, 63, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d corr own vs basket shifted +5d
def f08ll_f08_semi_intra_peer_lead_lag_basketlead5_126d_base_v018_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lead_corr(o, b, 126, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d corr own vs basket shifted +5d
def f08ll_f08_semi_intra_peer_lead_lag_basketlead5_252d_base_v019_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lead_corr(o, b, 252, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d corr own vs basket shifted +5d
def f08ll_f08_semi_intra_peer_lead_lag_basketlead5_504d_base_v020_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lead_corr(o, b, 504, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d corr own vs basket shifted -1d (own leads)
def f08ll_f08_semi_intra_peer_lead_lag_ownlead1_21d_base_v021_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lag_corr(o, b, 21, 1)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d corr own vs basket shifted -1d (own leads)
def f08ll_f08_semi_intra_peer_lead_lag_ownlead1_63d_base_v022_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lag_corr(o, b, 63, 1)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d corr own vs basket shifted -1d (own leads)
def f08ll_f08_semi_intra_peer_lead_lag_ownlead1_126d_base_v023_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lag_corr(o, b, 126, 1)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d corr own vs basket shifted -1d (own leads)
def f08ll_f08_semi_intra_peer_lead_lag_ownlead1_252d_base_v024_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lag_corr(o, b, 252, 1)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d corr own vs basket shifted -1d (own leads)
def f08ll_f08_semi_intra_peer_lead_lag_ownlead1_504d_base_v025_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lag_corr(o, b, 504, 1)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d corr own vs basket shifted -2d
def f08ll_f08_semi_intra_peer_lead_lag_ownlead2_21d_base_v026_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lag_corr(o, b, 21, 2)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d corr own vs basket shifted -2d
def f08ll_f08_semi_intra_peer_lead_lag_ownlead2_63d_base_v027_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lag_corr(o, b, 63, 2)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d corr own vs basket shifted -2d
def f08ll_f08_semi_intra_peer_lead_lag_ownlead2_126d_base_v028_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lag_corr(o, b, 126, 2)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d corr own vs basket shifted -2d
def f08ll_f08_semi_intra_peer_lead_lag_ownlead2_252d_base_v029_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lag_corr(o, b, 252, 2)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d corr own vs basket shifted -2d
def f08ll_f08_semi_intra_peer_lead_lag_ownlead2_504d_base_v030_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lag_corr(o, b, 504, 2)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d corr own vs basket shifted -5d
def f08ll_f08_semi_intra_peer_lead_lag_ownlead5_21d_base_v031_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lag_corr(o, b, 21, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d corr own vs basket shifted -5d
def f08ll_f08_semi_intra_peer_lead_lag_ownlead5_63d_base_v032_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lag_corr(o, b, 63, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d corr own vs basket shifted -5d
def f08ll_f08_semi_intra_peer_lead_lag_ownlead5_126d_base_v033_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lag_corr(o, b, 126, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d corr own vs basket shifted -5d
def f08ll_f08_semi_intra_peer_lead_lag_ownlead5_252d_base_v034_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lag_corr(o, b, 252, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d corr own vs basket shifted -5d
def f08ll_f08_semi_intra_peer_lead_lag_ownlead5_504d_base_v035_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lag_corr(o, b, 504, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lead-lag asymmetry at 1d (own-lead minus basket-lead)
def f08ll_f08_semi_intra_peer_lead_lag_llasym1_21d_base_v036_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    olead = _f08_lag_corr(o, b, 21, 1)
    blead = _f08_lead_corr(o, b, 21, 1)
    result = olead - blead
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lead-lag asymmetry at 1d (own-lead minus basket-lead)
def f08ll_f08_semi_intra_peer_lead_lag_llasym1_63d_base_v037_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    olead = _f08_lag_corr(o, b, 63, 1)
    blead = _f08_lead_corr(o, b, 63, 1)
    result = olead - blead
    return result.replace([np.inf, -np.inf], np.nan)


# 126d lead-lag asymmetry at 1d (own-lead minus basket-lead)
def f08ll_f08_semi_intra_peer_lead_lag_llasym1_126d_base_v038_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    olead = _f08_lag_corr(o, b, 126, 1)
    blead = _f08_lead_corr(o, b, 126, 1)
    result = olead - blead
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lead-lag asymmetry at 1d (own-lead minus basket-lead)
def f08ll_f08_semi_intra_peer_lead_lag_llasym1_252d_base_v039_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    olead = _f08_lag_corr(o, b, 252, 1)
    blead = _f08_lead_corr(o, b, 252, 1)
    result = olead - blead
    return result.replace([np.inf, -np.inf], np.nan)


# 504d lead-lag asymmetry at 1d (own-lead minus basket-lead)
def f08ll_f08_semi_intra_peer_lead_lag_llasym1_504d_base_v040_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    olead = _f08_lag_corr(o, b, 504, 1)
    blead = _f08_lead_corr(o, b, 504, 1)
    result = olead - blead
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lead-lag asymmetry at 2d
def f08ll_f08_semi_intra_peer_lead_lag_llasym2_21d_base_v041_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    olead = _f08_lag_corr(o, b, 21, 2)
    blead = _f08_lead_corr(o, b, 21, 2)
    result = olead - blead
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lead-lag asymmetry at 2d
def f08ll_f08_semi_intra_peer_lead_lag_llasym2_63d_base_v042_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    olead = _f08_lag_corr(o, b, 63, 2)
    blead = _f08_lead_corr(o, b, 63, 2)
    result = olead - blead
    return result.replace([np.inf, -np.inf], np.nan)


# 126d lead-lag asymmetry at 2d
def f08ll_f08_semi_intra_peer_lead_lag_llasym2_126d_base_v043_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    olead = _f08_lag_corr(o, b, 126, 2)
    blead = _f08_lead_corr(o, b, 126, 2)
    result = olead - blead
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lead-lag asymmetry at 2d
def f08ll_f08_semi_intra_peer_lead_lag_llasym2_252d_base_v044_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    olead = _f08_lag_corr(o, b, 252, 2)
    blead = _f08_lead_corr(o, b, 252, 2)
    result = olead - blead
    return result.replace([np.inf, -np.inf], np.nan)


# 504d lead-lag asymmetry at 2d
def f08ll_f08_semi_intra_peer_lead_lag_llasym2_504d_base_v045_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    olead = _f08_lag_corr(o, b, 504, 2)
    blead = _f08_lead_corr(o, b, 504, 2)
    result = olead - blead
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lead-lag asymmetry at 5d
def f08ll_f08_semi_intra_peer_lead_lag_llasym5_21d_base_v046_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    olead = _f08_lag_corr(o, b, 21, 5)
    blead = _f08_lead_corr(o, b, 21, 5)
    result = olead - blead
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lead-lag asymmetry at 5d
def f08ll_f08_semi_intra_peer_lead_lag_llasym5_63d_base_v047_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    olead = _f08_lag_corr(o, b, 63, 5)
    blead = _f08_lead_corr(o, b, 63, 5)
    result = olead - blead
    return result.replace([np.inf, -np.inf], np.nan)


# 126d lead-lag asymmetry at 5d
def f08ll_f08_semi_intra_peer_lead_lag_llasym5_126d_base_v048_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    olead = _f08_lag_corr(o, b, 126, 5)
    blead = _f08_lead_corr(o, b, 126, 5)
    result = olead - blead
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lead-lag asymmetry at 5d
def f08ll_f08_semi_intra_peer_lead_lag_llasym5_252d_base_v049_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    olead = _f08_lag_corr(o, b, 252, 5)
    blead = _f08_lead_corr(o, b, 252, 5)
    result = olead - blead
    return result.replace([np.inf, -np.inf], np.nan)


# 504d lead-lag asymmetry at 5d
def f08ll_f08_semi_intra_peer_lead_lag_llasym5_504d_base_v050_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    olead = _f08_lag_corr(o, b, 504, 5)
    blead = _f08_lead_corr(o, b, 504, 5)
    result = olead - blead
    return result.replace([np.inf, -np.inf], np.nan)


# 21d argmax of corr across lags -5..5 (positive means own leads)
def f08ll_f08_semi_intra_peer_lead_lag_argmaxlag_21d_base_v051_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    lags = list(range(-5, 6))
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


# 63d argmax of corr across lags -5..5 (positive means own leads)
def f08ll_f08_semi_intra_peer_lead_lag_argmaxlag_63d_base_v052_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    lags = list(range(-5, 6))
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


# 126d argmax of corr across lags -5..5 (positive means own leads)
def f08ll_f08_semi_intra_peer_lead_lag_argmaxlag_126d_base_v053_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    lags = list(range(-5, 6))
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


# 252d argmax of corr across lags -5..5 (positive means own leads)
def f08ll_f08_semi_intra_peer_lead_lag_argmaxlag_252d_base_v054_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    lags = list(range(-5, 6))
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


# 504d argmax of corr across lags -5..5 (positive means own leads)
def f08ll_f08_semi_intra_peer_lead_lag_argmaxlag_504d_base_v055_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    lags = list(range(-5, 6))
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


# 21d max corr across lags -5..5
def f08ll_f08_semi_intra_peer_lead_lag_maxlagcorr_21d_base_v056_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    lags = list(range(-5, 6))
    cors = []
    for L in lags:
        cors.append(o.rolling(21, min_periods=max(2, 21 // 2)).corr(b.shift(-L)))
    df = pd.concat(cors, axis=1)
    result = df.max(axis=1)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max corr across lags -5..5
def f08ll_f08_semi_intra_peer_lead_lag_maxlagcorr_63d_base_v057_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    lags = list(range(-5, 6))
    cors = []
    for L in lags:
        cors.append(o.rolling(63, min_periods=max(2, 63 // 2)).corr(b.shift(-L)))
    df = pd.concat(cors, axis=1)
    result = df.max(axis=1)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max corr across lags -5..5
def f08ll_f08_semi_intra_peer_lead_lag_maxlagcorr_126d_base_v058_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    lags = list(range(-5, 6))
    cors = []
    for L in lags:
        cors.append(o.rolling(126, min_periods=max(2, 126 // 2)).corr(b.shift(-L)))
    df = pd.concat(cors, axis=1)
    result = df.max(axis=1)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max corr across lags -5..5
def f08ll_f08_semi_intra_peer_lead_lag_maxlagcorr_252d_base_v059_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    lags = list(range(-5, 6))
    cors = []
    for L in lags:
        cors.append(o.rolling(252, min_periods=max(2, 252 // 2)).corr(b.shift(-L)))
    df = pd.concat(cors, axis=1)
    result = df.max(axis=1)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max corr across lags -5..5
def f08ll_f08_semi_intra_peer_lead_lag_maxlagcorr_504d_base_v060_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    lags = list(range(-5, 6))
    cors = []
    for L in lags:
        cors.append(o.rolling(504, min_periods=max(2, 504 // 2)).corr(b.shift(-L)))
    df = pd.concat(cors, axis=1)
    result = df.max(axis=1)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d corr own vs basket shifted +21d
def f08ll_f08_semi_intra_peer_lead_lag_basketlead21_21d_base_v061_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lead_corr(o, b, 21, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d corr own vs basket shifted +21d
def f08ll_f08_semi_intra_peer_lead_lag_basketlead21_63d_base_v062_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lead_corr(o, b, 63, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d corr own vs basket shifted +21d
def f08ll_f08_semi_intra_peer_lead_lag_basketlead21_126d_base_v063_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lead_corr(o, b, 126, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d corr own vs basket shifted +21d
def f08ll_f08_semi_intra_peer_lead_lag_basketlead21_252d_base_v064_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lead_corr(o, b, 252, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d corr own vs basket shifted +21d
def f08ll_f08_semi_intra_peer_lead_lag_basketlead21_504d_base_v065_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lead_corr(o, b, 504, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d corr own vs basket shifted -21d (own leads by 21d)
def f08ll_f08_semi_intra_peer_lead_lag_ownlead21_21d_base_v066_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lag_corr(o, b, 21, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d corr own vs basket shifted -21d (own leads by 21d)
def f08ll_f08_semi_intra_peer_lead_lag_ownlead21_63d_base_v067_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lag_corr(o, b, 63, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d corr own vs basket shifted -21d (own leads by 21d)
def f08ll_f08_semi_intra_peer_lead_lag_ownlead21_126d_base_v068_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lag_corr(o, b, 126, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d corr own vs basket shifted -21d (own leads by 21d)
def f08ll_f08_semi_intra_peer_lead_lag_ownlead21_252d_base_v069_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lag_corr(o, b, 252, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d corr own vs basket shifted -21d (own leads by 21d)
def f08ll_f08_semi_intra_peer_lead_lag_ownlead21_504d_base_v070_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    result = _f08_lag_corr(o, b, 504, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lead-lag asymmetry at 21d
def f08ll_f08_semi_intra_peer_lead_lag_llasym21_21d_base_v071_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    olead = _f08_lag_corr(o, b, 21, 21)
    blead = _f08_lead_corr(o, b, 21, 21)
    result = olead - blead
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lead-lag asymmetry at 21d
def f08ll_f08_semi_intra_peer_lead_lag_llasym21_63d_base_v072_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    olead = _f08_lag_corr(o, b, 63, 21)
    blead = _f08_lead_corr(o, b, 63, 21)
    result = olead - blead
    return result.replace([np.inf, -np.inf], np.nan)


# 126d lead-lag asymmetry at 21d
def f08ll_f08_semi_intra_peer_lead_lag_llasym21_126d_base_v073_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    olead = _f08_lag_corr(o, b, 126, 21)
    blead = _f08_lead_corr(o, b, 126, 21)
    result = olead - blead
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lead-lag asymmetry at 21d
def f08ll_f08_semi_intra_peer_lead_lag_llasym21_252d_base_v074_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    olead = _f08_lag_corr(o, b, 252, 21)
    blead = _f08_lead_corr(o, b, 252, 21)
    result = olead - blead
    return result.replace([np.inf, -np.inf], np.nan)


# 504d lead-lag asymmetry at 21d
def f08ll_f08_semi_intra_peer_lead_lag_llasym21_504d_base_v075_signal(closeadj, semi_basket_closeadj):
    o, b = _f08_ret(closeadj), _f08_ret(semi_basket_closeadj)
    olead = _f08_lag_corr(o, b, 504, 21)
    blead = _f08_lead_corr(o, b, 504, 21)
    result = olead - blead
    return result.replace([np.inf, -np.inf], np.nan)


