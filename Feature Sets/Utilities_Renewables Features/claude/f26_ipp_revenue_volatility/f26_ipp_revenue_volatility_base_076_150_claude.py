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
def _f26_revenue_cv(revenue, w):
    m = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = revenue.rolling(w, min_periods=max(1, w // 2)).std()
    return sd / m.replace(0, np.nan).abs()


def _f26_revenue_vol(revenue, w):
    r = revenue.pct_change()
    return r.rolling(w, min_periods=max(1, w // 2)).std()


def _f26_volatility_score(revenue, ebitda, w):
    rcv = revenue.rolling(w, min_periods=max(1, w // 2)).std() / revenue.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan).abs()
    ecv = ebitda.rolling(w, min_periods=max(1, w // 2)).std() / ebitda.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan).abs()
    return rcv + ecv



# ===== features =====

# w=189 tr=8 sc=2 iw=126 prim=_f26_revenue_vol
def f26irv_f26_ipp_revenue_volatility_revenue_vol_189d_t8s2i126_base_v076_signal(closeadj, revenue):
    base = _f26_revenue_vol(revenue, 189)
    val = base * base.abs()
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=252 tr=0 sc=2 iw=126 prim=_f26_revenue_vol
def f26irv_f26_ipp_revenue_volatility_revenue_vol_252d_t0s2i126_base_v077_signal(closeadj, revenue):
    base = _f26_revenue_vol(revenue, 252)
    val = base
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=252 tr=2 sc=2 iw=126 prim=_f26_revenue_vol
def f26irv_f26_ipp_revenue_volatility_revenue_vol_252d_t2s2i126_base_v078_signal(closeadj, revenue):
    base = _f26_revenue_vol(revenue, 252)
    val = _std(base, 126)
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=252 tr=4 sc=2 iw=126 prim=_f26_revenue_vol
def f26irv_f26_ipp_revenue_volatility_revenue_vol_252d_t4s2i126_base_v079_signal(closeadj, revenue):
    base = _f26_revenue_vol(revenue, 252)
    val = base * closeadj
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=252 tr=6 sc=2 iw=126 prim=_f26_revenue_vol
def f26irv_f26_ipp_revenue_volatility_revenue_vol_252d_t6s2i126_base_v080_signal(closeadj, revenue):
    base = _f26_revenue_vol(revenue, 252)
    val = base + _mean(base, 126)
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=252 tr=8 sc=2 iw=126 prim=_f26_revenue_vol
def f26irv_f26_ipp_revenue_volatility_revenue_vol_252d_t8s2i126_base_v081_signal(closeadj, revenue):
    base = _f26_revenue_vol(revenue, 252)
    val = base * base.abs()
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=378 tr=0 sc=2 iw=126 prim=_f26_revenue_vol
def f26irv_f26_ipp_revenue_volatility_revenue_vol_378d_t0s2i126_base_v082_signal(closeadj, revenue):
    base = _f26_revenue_vol(revenue, 378)
    val = base
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=378 tr=2 sc=2 iw=126 prim=_f26_revenue_vol
def f26irv_f26_ipp_revenue_volatility_revenue_vol_378d_t2s2i126_base_v083_signal(closeadj, revenue):
    base = _f26_revenue_vol(revenue, 378)
    val = _std(base, 126)
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=378 tr=4 sc=2 iw=126 prim=_f26_revenue_vol
def f26irv_f26_ipp_revenue_volatility_revenue_vol_378d_t4s2i126_base_v084_signal(closeadj, revenue):
    base = _f26_revenue_vol(revenue, 378)
    val = base * closeadj
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=378 tr=6 sc=2 iw=126 prim=_f26_revenue_vol
def f26irv_f26_ipp_revenue_volatility_revenue_vol_378d_t6s2i126_base_v085_signal(closeadj, revenue):
    base = _f26_revenue_vol(revenue, 378)
    val = base + _mean(base, 126)
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=378 tr=8 sc=2 iw=126 prim=_f26_revenue_vol
def f26irv_f26_ipp_revenue_volatility_revenue_vol_378d_t8s2i126_base_v086_signal(closeadj, revenue):
    base = _f26_revenue_vol(revenue, 378)
    val = base * base.abs()
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=504 tr=0 sc=2 iw=126 prim=_f26_revenue_vol
def f26irv_f26_ipp_revenue_volatility_revenue_vol_504d_t0s2i126_base_v087_signal(closeadj, revenue):
    base = _f26_revenue_vol(revenue, 504)
    val = base
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=504 tr=2 sc=2 iw=126 prim=_f26_revenue_vol
def f26irv_f26_ipp_revenue_volatility_revenue_vol_504d_t2s2i126_base_v088_signal(closeadj, revenue):
    base = _f26_revenue_vol(revenue, 504)
    val = _std(base, 126)
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=504 tr=4 sc=2 iw=126 prim=_f26_revenue_vol
def f26irv_f26_ipp_revenue_volatility_revenue_vol_504d_t4s2i126_base_v089_signal(closeadj, revenue):
    base = _f26_revenue_vol(revenue, 504)
    val = base * closeadj
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=504 tr=6 sc=2 iw=126 prim=_f26_revenue_vol
def f26irv_f26_ipp_revenue_volatility_revenue_vol_504d_t6s2i126_base_v090_signal(closeadj, revenue):
    base = _f26_revenue_vol(revenue, 504)
    val = base + _mean(base, 126)
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=504 tr=8 sc=2 iw=126 prim=_f26_revenue_vol
def f26irv_f26_ipp_revenue_volatility_revenue_vol_504d_t8s2i126_base_v091_signal(closeadj, revenue):
    base = _f26_revenue_vol(revenue, 504)
    val = base * base.abs()
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=5 tr=0 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_5d_t0s2i126_base_v092_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 5)
    val = base
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=5 tr=2 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_5d_t2s2i126_base_v093_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 5)
    val = _std(base, 126)
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=5 tr=4 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_5d_t4s2i126_base_v094_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 5)
    val = base * closeadj
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=5 tr=6 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_5d_t6s2i126_base_v095_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 5)
    val = base + _mean(base, 126)
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=5 tr=8 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_5d_t8s2i126_base_v096_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 5)
    val = base * base.abs()
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=10 tr=0 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_10d_t0s2i126_base_v097_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 10)
    val = base
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=10 tr=2 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_10d_t2s2i126_base_v098_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 10)
    val = _std(base, 126)
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=10 tr=4 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_10d_t4s2i126_base_v099_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 10)
    val = base * closeadj
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=10 tr=6 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_10d_t6s2i126_base_v100_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 10)
    val = base + _mean(base, 126)
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=10 tr=8 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_10d_t8s2i126_base_v101_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 10)
    val = base * base.abs()
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=21 tr=0 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_21d_t0s2i126_base_v102_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 21)
    val = base
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=21 tr=2 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_21d_t2s2i126_base_v103_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 21)
    val = _std(base, 126)
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=21 tr=4 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_21d_t4s2i126_base_v104_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 21)
    val = base * closeadj
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=21 tr=6 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_21d_t6s2i126_base_v105_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 21)
    val = base + _mean(base, 126)
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=21 tr=8 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_21d_t8s2i126_base_v106_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 21)
    val = base * base.abs()
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=42 tr=0 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_42d_t0s2i126_base_v107_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 42)
    val = base
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=42 tr=2 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_42d_t2s2i126_base_v108_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 42)
    val = _std(base, 126)
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=42 tr=4 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_42d_t4s2i126_base_v109_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 42)
    val = base * closeadj
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=42 tr=6 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_42d_t6s2i126_base_v110_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 42)
    val = base + _mean(base, 126)
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=42 tr=8 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_42d_t8s2i126_base_v111_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 42)
    val = base * base.abs()
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=63 tr=0 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_63d_t0s2i126_base_v112_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 63)
    val = base
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=63 tr=2 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_63d_t2s2i126_base_v113_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 63)
    val = _std(base, 126)
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=63 tr=4 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_63d_t4s2i126_base_v114_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 63)
    val = base * closeadj
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=63 tr=6 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_63d_t6s2i126_base_v115_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 63)
    val = base + _mean(base, 126)
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=63 tr=8 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_63d_t8s2i126_base_v116_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 63)
    val = base * base.abs()
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=126 tr=0 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_126d_t0s2i126_base_v117_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 126)
    val = base
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=126 tr=2 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_126d_t2s2i126_base_v118_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 126)
    val = _std(base, 126)
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=126 tr=4 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_126d_t4s2i126_base_v119_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 126)
    val = base * closeadj
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=126 tr=6 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_126d_t6s2i126_base_v120_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 126)
    val = base + _mean(base, 126)
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=126 tr=8 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_126d_t8s2i126_base_v121_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 126)
    val = base * base.abs()
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=189 tr=0 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_189d_t0s2i126_base_v122_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 189)
    val = base
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=189 tr=2 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_189d_t2s2i126_base_v123_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 189)
    val = _std(base, 126)
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=189 tr=4 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_189d_t4s2i126_base_v124_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 189)
    val = base * closeadj
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=189 tr=6 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_189d_t6s2i126_base_v125_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 189)
    val = base + _mean(base, 126)
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=189 tr=8 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_189d_t8s2i126_base_v126_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 189)
    val = base * base.abs()
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=252 tr=0 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_252d_t0s2i126_base_v127_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 252)
    val = base
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=252 tr=2 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_252d_t2s2i126_base_v128_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 252)
    val = _std(base, 126)
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=252 tr=4 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_252d_t4s2i126_base_v129_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 252)
    val = base * closeadj
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=252 tr=6 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_252d_t6s2i126_base_v130_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 252)
    val = base + _mean(base, 126)
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=252 tr=8 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_252d_t8s2i126_base_v131_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 252)
    val = base * base.abs()
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=378 tr=0 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_378d_t0s2i126_base_v132_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 378)
    val = base
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=378 tr=2 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_378d_t2s2i126_base_v133_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 378)
    val = _std(base, 126)
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=378 tr=4 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_378d_t4s2i126_base_v134_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 378)
    val = base * closeadj
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=378 tr=6 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_378d_t6s2i126_base_v135_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 378)
    val = base + _mean(base, 126)
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=378 tr=8 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_378d_t8s2i126_base_v136_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 378)
    val = base * base.abs()
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=504 tr=0 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_504d_t0s2i126_base_v137_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 504)
    val = base
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=504 tr=2 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_504d_t2s2i126_base_v138_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 504)
    val = _std(base, 126)
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=504 tr=4 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_504d_t4s2i126_base_v139_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 504)
    val = base * closeadj
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=504 tr=6 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_504d_t6s2i126_base_v140_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 504)
    val = base + _mean(base, 126)
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=504 tr=8 sc=2 iw=126 prim=_f26_volatility_score
def f26irv_f26_ipp_revenue_volatility_volatility_score_504d_t8s2i126_base_v141_signal(closeadj, ebitda, revenue):
    base = _f26_volatility_score(revenue, ebitda, 504)
    val = base * base.abs()
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=5 tr=0 sc=2 iw=126 prim=_f26_revenue_cv
def f26irv_f26_ipp_revenue_volatility_revenue_cv_5d_t0s2i126_base_v142_signal(closeadj, revenue):
    base = _f26_revenue_cv(revenue, 5)
    val = base
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=5 tr=2 sc=2 iw=126 prim=_f26_revenue_cv
def f26irv_f26_ipp_revenue_volatility_revenue_cv_5d_t2s2i126_base_v143_signal(closeadj, revenue):
    base = _f26_revenue_cv(revenue, 5)
    val = _std(base, 126)
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=5 tr=4 sc=2 iw=126 prim=_f26_revenue_cv
def f26irv_f26_ipp_revenue_volatility_revenue_cv_5d_t4s2i126_base_v144_signal(closeadj, revenue):
    base = _f26_revenue_cv(revenue, 5)
    val = base * closeadj
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=5 tr=6 sc=2 iw=126 prim=_f26_revenue_cv
def f26irv_f26_ipp_revenue_volatility_revenue_cv_5d_t6s2i126_base_v145_signal(closeadj, revenue):
    base = _f26_revenue_cv(revenue, 5)
    val = base + _mean(base, 126)
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=5 tr=8 sc=2 iw=126 prim=_f26_revenue_cv
def f26irv_f26_ipp_revenue_volatility_revenue_cv_5d_t8s2i126_base_v146_signal(closeadj, revenue):
    base = _f26_revenue_cv(revenue, 5)
    val = base * base.abs()
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=10 tr=0 sc=2 iw=126 prim=_f26_revenue_cv
def f26irv_f26_ipp_revenue_volatility_revenue_cv_10d_t0s2i126_base_v147_signal(closeadj, revenue):
    base = _f26_revenue_cv(revenue, 10)
    val = base
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=10 tr=2 sc=2 iw=126 prim=_f26_revenue_cv
def f26irv_f26_ipp_revenue_volatility_revenue_cv_10d_t2s2i126_base_v148_signal(closeadj, revenue):
    base = _f26_revenue_cv(revenue, 10)
    val = _std(base, 126)
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=10 tr=4 sc=2 iw=126 prim=_f26_revenue_cv
def f26irv_f26_ipp_revenue_volatility_revenue_cv_10d_t4s2i126_base_v149_signal(closeadj, revenue):
    base = _f26_revenue_cv(revenue, 10)
    val = base * closeadj
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=10 tr=6 sc=2 iw=126 prim=_f26_revenue_cv
def f26irv_f26_ipp_revenue_volatility_revenue_cv_10d_t6s2i126_base_v150_signal(closeadj, revenue):
    base = _f26_revenue_cv(revenue, 10)
    val = base + _mean(base, 126)
    result = val * np.log(closeadj.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f26irv_f26_ipp_revenue_volatility_revenue_vol_189d_t8s2i126_base_v076_signal,
    f26irv_f26_ipp_revenue_volatility_revenue_vol_252d_t0s2i126_base_v077_signal,
    f26irv_f26_ipp_revenue_volatility_revenue_vol_252d_t2s2i126_base_v078_signal,
    f26irv_f26_ipp_revenue_volatility_revenue_vol_252d_t4s2i126_base_v079_signal,
    f26irv_f26_ipp_revenue_volatility_revenue_vol_252d_t6s2i126_base_v080_signal,
    f26irv_f26_ipp_revenue_volatility_revenue_vol_252d_t8s2i126_base_v081_signal,
    f26irv_f26_ipp_revenue_volatility_revenue_vol_378d_t0s2i126_base_v082_signal,
    f26irv_f26_ipp_revenue_volatility_revenue_vol_378d_t2s2i126_base_v083_signal,
    f26irv_f26_ipp_revenue_volatility_revenue_vol_378d_t4s2i126_base_v084_signal,
    f26irv_f26_ipp_revenue_volatility_revenue_vol_378d_t6s2i126_base_v085_signal,
    f26irv_f26_ipp_revenue_volatility_revenue_vol_378d_t8s2i126_base_v086_signal,
    f26irv_f26_ipp_revenue_volatility_revenue_vol_504d_t0s2i126_base_v087_signal,
    f26irv_f26_ipp_revenue_volatility_revenue_vol_504d_t2s2i126_base_v088_signal,
    f26irv_f26_ipp_revenue_volatility_revenue_vol_504d_t4s2i126_base_v089_signal,
    f26irv_f26_ipp_revenue_volatility_revenue_vol_504d_t6s2i126_base_v090_signal,
    f26irv_f26_ipp_revenue_volatility_revenue_vol_504d_t8s2i126_base_v091_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_5d_t0s2i126_base_v092_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_5d_t2s2i126_base_v093_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_5d_t4s2i126_base_v094_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_5d_t6s2i126_base_v095_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_5d_t8s2i126_base_v096_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_10d_t0s2i126_base_v097_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_10d_t2s2i126_base_v098_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_10d_t4s2i126_base_v099_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_10d_t6s2i126_base_v100_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_10d_t8s2i126_base_v101_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_21d_t0s2i126_base_v102_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_21d_t2s2i126_base_v103_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_21d_t4s2i126_base_v104_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_21d_t6s2i126_base_v105_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_21d_t8s2i126_base_v106_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_42d_t0s2i126_base_v107_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_42d_t2s2i126_base_v108_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_42d_t4s2i126_base_v109_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_42d_t6s2i126_base_v110_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_42d_t8s2i126_base_v111_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_63d_t0s2i126_base_v112_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_63d_t2s2i126_base_v113_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_63d_t4s2i126_base_v114_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_63d_t6s2i126_base_v115_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_63d_t8s2i126_base_v116_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_126d_t0s2i126_base_v117_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_126d_t2s2i126_base_v118_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_126d_t4s2i126_base_v119_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_126d_t6s2i126_base_v120_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_126d_t8s2i126_base_v121_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_189d_t0s2i126_base_v122_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_189d_t2s2i126_base_v123_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_189d_t4s2i126_base_v124_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_189d_t6s2i126_base_v125_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_189d_t8s2i126_base_v126_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_252d_t0s2i126_base_v127_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_252d_t2s2i126_base_v128_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_252d_t4s2i126_base_v129_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_252d_t6s2i126_base_v130_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_252d_t8s2i126_base_v131_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_378d_t0s2i126_base_v132_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_378d_t2s2i126_base_v133_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_378d_t4s2i126_base_v134_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_378d_t6s2i126_base_v135_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_378d_t8s2i126_base_v136_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_504d_t0s2i126_base_v137_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_504d_t2s2i126_base_v138_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_504d_t4s2i126_base_v139_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_504d_t6s2i126_base_v140_signal,
    f26irv_f26_ipp_revenue_volatility_volatility_score_504d_t8s2i126_base_v141_signal,
    f26irv_f26_ipp_revenue_volatility_revenue_cv_5d_t0s2i126_base_v142_signal,
    f26irv_f26_ipp_revenue_volatility_revenue_cv_5d_t2s2i126_base_v143_signal,
    f26irv_f26_ipp_revenue_volatility_revenue_cv_5d_t4s2i126_base_v144_signal,
    f26irv_f26_ipp_revenue_volatility_revenue_cv_5d_t6s2i126_base_v145_signal,
    f26irv_f26_ipp_revenue_volatility_revenue_cv_5d_t8s2i126_base_v146_signal,
    f26irv_f26_ipp_revenue_volatility_revenue_cv_10d_t0s2i126_base_v147_signal,
    f26irv_f26_ipp_revenue_volatility_revenue_cv_10d_t2s2i126_base_v148_signal,
    f26irv_f26_ipp_revenue_volatility_revenue_cv_10d_t4s2i126_base_v149_signal,
    f26irv_f26_ipp_revenue_volatility_revenue_cv_10d_t6s2i126_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F26_IPP_REVENUE_VOLATILITY_REGISTRY_076_150 = REGISTRY


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
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    assetsc      = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsc")
    assetsnc     = pd.Series(1.2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsnc")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    liabilitiesc = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesc")
    liabilitiesnc= pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesnc")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    equityusd    = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equityusd")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    debtc        = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtc")
    debtnc       = pd.Series(4.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtnc")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    intangibles  = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    tangibles    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="tangibles")
    invcap       = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")
    retearn      = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="retearn")
    sbcomp       = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="sbcomp")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    shareswadil  = pd.Series(1.02e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswadil")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    epsdil       = pd.Series(0.98 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="epsdil")
    bvps         = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="bvps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    sps          = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="sps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    pe           = pd.Series(closeadj / eps.replace(0, np.nan).abs(), name="pe")
    pb           = pd.Series(closeadj / bvps.replace(0, np.nan).abs(), name="pb")
    ps           = pd.Series(closeadj / sps.replace(0, np.nan).abs(), name="ps")
    evebit       = pd.Series(ev / ebit.replace(0, np.nan).abs(), name="evebit")
    evebitda     = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ros          = pd.Series(0.08 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ros")
    currentratio = pd.Series(1.5 + 0.3*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="currentratio")
    de           = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    divyield     = pd.Series(0.02 + 0.005*np.sin(np.arange(n)/250.0) + 0.001*np.random.randn(n), name="divyield")
    assetturnover= pd.Series(0.7 + 0.15*np.sin(np.arange(n)/250.0) + 0.02*np.random.randn(n), name="assetturnover")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "assets": assets, "assetsc": assetsc, "assetsnc": assetsnc,
        "liabilities": liabilities, "liabilitiesc": liabilitiesc, "liabilitiesnc": liabilitiesnc,
        "equity": equity, "equityusd": equityusd,
        "debt": debt, "debtc": debtc, "debtnc": debtnc, "cashneq": cashneq,
        "inventory": inventory, "receivables": receivables, "payables": payables,
        "deferredrev": deferredrev, "workingcapital": workingcapital,
        "ppnenet": ppnenet, "intangibles": intangibles, "tangibles": tangibles,
        "invcap": invcap, "retearn": retearn, "sbcomp": sbcomp,
        "sharesbas": sharesbas, "shareswa": shareswa, "shareswadil": shareswadil,
        "eps": eps, "epsdil": epsdil, "bvps": bvps, "fcfps": fcfps, "sps": sps, "dps": dps,
        "marketcap": marketcap, "ev": ev,
        "pe": pe, "pb": pb, "ps": ps, "evebit": evebit, "evebitda": evebitda,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
        "roa": roa, "roe": roe, "roic": roic, "ros": ros,
        "currentratio": currentratio, "de": de,
        "payoutratio": payoutratio, "divyield": divyield, "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f26_revenue_cv', '_f26_revenue_vol', '_f26_volatility_score')
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
    print(f"OK f26_ipp_revenue_volatility_base_076_150_claude: {n_features} features pass")
