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
def _f06_ret(s):
    return s.pct_change()


def _f06_logret(s):
    return np.log(s / s.shift(1))


def _f06_realvol(r, w):
    return r.rolling(w, min_periods=max(2, w // 2)).std() * np.sqrt(252)

# 5d / 21d vol ratio
def f06vr_f06_semi_volatility_regime_volratio_5v21_base_v076_signal(closeadj):
    r = _f06_ret(closeadj)
    vs = _f06_realvol(r, 5)
    vl = _f06_realvol(r, 21)
    result = vs / vl.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d / 63d vol ratio
def f06vr_f06_semi_volatility_regime_volratio_21v63_base_v077_signal(closeadj):
    r = _f06_ret(closeadj)
    vs = _f06_realvol(r, 21)
    vl = _f06_realvol(r, 63)
    result = vs / vl.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d / 126d vol ratio
def f06vr_f06_semi_volatility_regime_volratio_63v126_base_v078_signal(closeadj):
    r = _f06_ret(closeadj)
    vs = _f06_realvol(r, 63)
    vl = _f06_realvol(r, 126)
    result = vs / vl.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d / 252d vol ratio
def f06vr_f06_semi_volatility_regime_volratio_126v252_base_v079_signal(closeadj):
    r = _f06_ret(closeadj)
    vs = _f06_realvol(r, 126)
    vl = _f06_realvol(r, 252)
    result = vs / vl.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d / 504d vol ratio
def f06vr_f06_semi_volatility_regime_volratio_252v504_base_v080_signal(closeadj):
    r = _f06_ret(closeadj)
    vs = _f06_realvol(r, 252)
    vl = _f06_realvol(r, 504)
    result = vs / vl.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d - 21d vol spread
def f06vr_f06_semi_volatility_regime_volspread_5v21_base_v081_signal(closeadj):
    r = _f06_ret(closeadj)
    vs = _f06_realvol(r, 5)
    vl = _f06_realvol(r, 21)
    result = vs - vl
    return result.replace([np.inf, -np.inf], np.nan)


# 21d - 63d vol spread
def f06vr_f06_semi_volatility_regime_volspread_21v63_base_v082_signal(closeadj):
    r = _f06_ret(closeadj)
    vs = _f06_realvol(r, 21)
    vl = _f06_realvol(r, 63)
    result = vs - vl
    return result.replace([np.inf, -np.inf], np.nan)


# 63d - 126d vol spread
def f06vr_f06_semi_volatility_regime_volspread_63v126_base_v083_signal(closeadj):
    r = _f06_ret(closeadj)
    vs = _f06_realvol(r, 63)
    vl = _f06_realvol(r, 126)
    result = vs - vl
    return result.replace([np.inf, -np.inf], np.nan)


# 126d - 252d vol spread
def f06vr_f06_semi_volatility_regime_volspread_126v252_base_v084_signal(closeadj):
    r = _f06_ret(closeadj)
    vs = _f06_realvol(r, 126)
    vl = _f06_realvol(r, 252)
    result = vs - vl
    return result.replace([np.inf, -np.inf], np.nan)


# 252d - 504d vol spread
def f06vr_f06_semi_volatility_regime_volspread_252v504_base_v085_signal(closeadj):
    r = _f06_ret(closeadj)
    vs = _f06_realvol(r, 252)
    vl = _f06_realvol(r, 504)
    result = vs - vl
    return result.replace([np.inf, -np.inf], np.nan)


# 21d downside vol (std of negative returns)
def f06vr_f06_semi_volatility_regime_downvol_21d_base_v086_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    result = _std(neg, 21) * np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d downside vol (std of negative returns)
def f06vr_f06_semi_volatility_regime_downvol_63d_base_v087_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    result = _std(neg, 63) * np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d downside vol (std of negative returns)
def f06vr_f06_semi_volatility_regime_downvol_126d_base_v088_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    result = _std(neg, 126) * np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d downside vol (std of negative returns)
def f06vr_f06_semi_volatility_regime_downvol_252d_base_v089_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    result = _std(neg, 252) * np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d downside vol (std of negative returns)
def f06vr_f06_semi_volatility_regime_downvol_504d_base_v090_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    result = _std(neg, 504) * np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d upside vol
def f06vr_f06_semi_volatility_regime_upvol_21d_base_v091_signal(closeadj):
    r = _f06_ret(closeadj)
    pos = r.where(r > 0)
    result = _std(pos, 21) * np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d upside vol
def f06vr_f06_semi_volatility_regime_upvol_63d_base_v092_signal(closeadj):
    r = _f06_ret(closeadj)
    pos = r.where(r > 0)
    result = _std(pos, 63) * np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d upside vol
def f06vr_f06_semi_volatility_regime_upvol_126d_base_v093_signal(closeadj):
    r = _f06_ret(closeadj)
    pos = r.where(r > 0)
    result = _std(pos, 126) * np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d upside vol
def f06vr_f06_semi_volatility_regime_upvol_252d_base_v094_signal(closeadj):
    r = _f06_ret(closeadj)
    pos = r.where(r > 0)
    result = _std(pos, 252) * np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d upside vol
def f06vr_f06_semi_volatility_regime_upvol_504d_base_v095_signal(closeadj):
    r = _f06_ret(closeadj)
    pos = r.where(r > 0)
    result = _std(pos, 504) * np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol asymmetry (downside vol - upside vol)
def f06vr_f06_semi_volatility_regime_volasym_21d_base_v096_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 21) * np.sqrt(252)
    uv = _std(r.where(r > 0), 21) * np.sqrt(252)
    result = dv - uv
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol asymmetry (downside vol - upside vol)
def f06vr_f06_semi_volatility_regime_volasym_63d_base_v097_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 63) * np.sqrt(252)
    uv = _std(r.where(r > 0), 63) * np.sqrt(252)
    result = dv - uv
    return result.replace([np.inf, -np.inf], np.nan)


# 126d vol asymmetry (downside vol - upside vol)
def f06vr_f06_semi_volatility_regime_volasym_126d_base_v098_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 126) * np.sqrt(252)
    uv = _std(r.where(r > 0), 126) * np.sqrt(252)
    result = dv - uv
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vol asymmetry (downside vol - upside vol)
def f06vr_f06_semi_volatility_regime_volasym_252d_base_v099_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 252) * np.sqrt(252)
    uv = _std(r.where(r > 0), 252) * np.sqrt(252)
    result = dv - uv
    return result.replace([np.inf, -np.inf], np.nan)


# 504d vol asymmetry (downside vol - upside vol)
def f06vr_f06_semi_volatility_regime_volasym_504d_base_v100_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 504) * np.sqrt(252)
    uv = _std(r.where(r > 0), 504) * np.sqrt(252)
    result = dv - uv
    return result.replace([np.inf, -np.inf], np.nan)


# 21d return skew
def f06vr_f06_semi_volatility_regime_retskew_21d_base_v101_signal(closeadj):
    r = _f06_ret(closeadj)
    result = r.rolling(21, min_periods=max(2, 21 // 2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d return skew
def f06vr_f06_semi_volatility_regime_retskew_63d_base_v102_signal(closeadj):
    r = _f06_ret(closeadj)
    result = r.rolling(63, min_periods=max(2, 63 // 2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d return skew
def f06vr_f06_semi_volatility_regime_retskew_126d_base_v103_signal(closeadj):
    r = _f06_ret(closeadj)
    result = r.rolling(126, min_periods=max(2, 126 // 2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d return skew
def f06vr_f06_semi_volatility_regime_retskew_252d_base_v104_signal(closeadj):
    r = _f06_ret(closeadj)
    result = r.rolling(252, min_periods=max(2, 252 // 2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d return skew
def f06vr_f06_semi_volatility_regime_retskew_504d_base_v105_signal(closeadj):
    r = _f06_ret(closeadj)
    result = r.rolling(504, min_periods=max(2, 504 // 2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d return kurtosis
def f06vr_f06_semi_volatility_regime_retkurt_21d_base_v106_signal(closeadj):
    r = _f06_ret(closeadj)
    result = r.rolling(21, min_periods=max(2, 21 // 2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d return kurtosis
def f06vr_f06_semi_volatility_regime_retkurt_63d_base_v107_signal(closeadj):
    r = _f06_ret(closeadj)
    result = r.rolling(63, min_periods=max(2, 63 // 2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d return kurtosis
def f06vr_f06_semi_volatility_regime_retkurt_126d_base_v108_signal(closeadj):
    r = _f06_ret(closeadj)
    result = r.rolling(126, min_periods=max(2, 126 // 2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d return kurtosis
def f06vr_f06_semi_volatility_regime_retkurt_252d_base_v109_signal(closeadj):
    r = _f06_ret(closeadj)
    result = r.rolling(252, min_periods=max(2, 252 // 2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d return kurtosis
def f06vr_f06_semi_volatility_regime_retkurt_504d_base_v110_signal(closeadj):
    r = _f06_ret(closeadj)
    result = r.rolling(504, min_periods=max(2, 504 // 2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean absolute return
def f06vr_f06_semi_volatility_regime_absretmean_21d_base_v111_signal(closeadj):
    r = _f06_ret(closeadj).abs()
    result = _mean(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean absolute return
def f06vr_f06_semi_volatility_regime_absretmean_63d_base_v112_signal(closeadj):
    r = _f06_ret(closeadj).abs()
    result = _mean(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean absolute return
def f06vr_f06_semi_volatility_regime_absretmean_126d_base_v113_signal(closeadj):
    r = _f06_ret(closeadj).abs()
    result = _mean(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean absolute return
def f06vr_f06_semi_volatility_regime_absretmean_252d_base_v114_signal(closeadj):
    r = _f06_ret(closeadj).abs()
    result = _mean(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean absolute return
def f06vr_f06_semi_volatility_regime_absretmean_504d_base_v115_signal(closeadj):
    r = _f06_ret(closeadj).abs()
    result = _mean(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean squared return
def f06vr_f06_semi_volatility_regime_squaredretmean_21d_base_v116_signal(closeadj):
    r = _f06_ret(closeadj) ** 2
    result = _mean(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean squared return
def f06vr_f06_semi_volatility_regime_squaredretmean_63d_base_v117_signal(closeadj):
    r = _f06_ret(closeadj) ** 2
    result = _mean(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean squared return
def f06vr_f06_semi_volatility_regime_squaredretmean_126d_base_v118_signal(closeadj):
    r = _f06_ret(closeadj) ** 2
    result = _mean(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean squared return
def f06vr_f06_semi_volatility_regime_squaredretmean_252d_base_v119_signal(closeadj):
    r = _f06_ret(closeadj) ** 2
    result = _mean(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean squared return
def f06vr_f06_semi_volatility_regime_squaredretmean_504d_base_v120_signal(closeadj):
    r = _f06_ret(closeadj) ** 2
    result = _mean(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol regime: vol / long-term median vol
def f06vr_f06_semi_volatility_regime_volregime_21d_base_v121_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    med = v_.rolling(504, min_periods=252).median()
    result = v_ / med.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol regime: vol / long-term median vol
def f06vr_f06_semi_volatility_regime_volregime_63d_base_v122_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    med = v_.rolling(504, min_periods=252).median()
    result = v_ / med.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d vol regime: vol / long-term median vol
def f06vr_f06_semi_volatility_regime_volregime_126d_base_v123_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    med = v_.rolling(504, min_periods=252).median()
    result = v_ / med.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vol regime: vol / long-term median vol
def f06vr_f06_semi_volatility_regime_volregime_252d_base_v124_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    med = v_.rolling(504, min_periods=252).median()
    result = v_ / med.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d vol regime: vol / long-term median vol
def f06vr_f06_semi_volatility_regime_volregime_504d_base_v125_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    med = v_.rolling(504, min_periods=252).median()
    result = v_ / med.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol percentile rank over 63d
def f06vr_f06_semi_volatility_regime_volpctrank_21d_base_v126_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    result = v_.rolling(63, min_periods=max(2, 63 // 2)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol percentile rank over 126d
def f06vr_f06_semi_volatility_regime_volpctrank_63d_base_v127_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    result = v_.rolling(126, min_periods=max(2, 126 // 2)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d vol percentile rank over 252d
def f06vr_f06_semi_volatility_regime_volpctrank_126d_base_v128_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    result = v_.rolling(252, min_periods=max(2, 252 // 2)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vol percentile rank over 504d
def f06vr_f06_semi_volatility_regime_volpctrank_252d_base_v129_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    result = v_.rolling(504, min_periods=max(2, 504 // 2)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d vol percentile rank over 756d
def f06vr_f06_semi_volatility_regime_volpctrank_504d_base_v130_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    result = v_.rolling(756, min_periods=max(2, 756 // 2)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d vol minus its value 21d ago
def f06vr_f06_semi_volatility_regime_volaccel_5v21_base_v131_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 5)
    result = v_ - v_.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol minus its value 63d ago
def f06vr_f06_semi_volatility_regime_volaccel_21v63_base_v132_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    result = v_ - v_.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol minus its value 126d ago
def f06vr_f06_semi_volatility_regime_volaccel_63v126_base_v133_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    result = v_ - v_.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d vol minus its value 252d ago
def f06vr_f06_semi_volatility_regime_volaccel_126v252_base_v134_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    result = v_ - v_.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vol minus its value 504d ago
def f06vr_f06_semi_volatility_regime_volaccel_252v504_base_v135_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    result = v_ - v_.shift(504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol clustering (autocorr of |returns|)
def f06vr_f06_semi_volatility_regime_volcluster_21d_base_v136_signal(closeadj):
    r = _f06_ret(closeadj).abs()
    result = r.rolling(21, min_periods=max(2, 21 // 2)).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol clustering (autocorr of |returns|)
def f06vr_f06_semi_volatility_regime_volcluster_63d_base_v137_signal(closeadj):
    r = _f06_ret(closeadj).abs()
    result = r.rolling(63, min_periods=max(2, 63 // 2)).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d vol clustering (autocorr of |returns|)
def f06vr_f06_semi_volatility_regime_volcluster_126d_base_v138_signal(closeadj):
    r = _f06_ret(closeadj).abs()
    result = r.rolling(126, min_periods=max(2, 126 // 2)).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vol clustering (autocorr of |returns|)
def f06vr_f06_semi_volatility_regime_volcluster_252d_base_v139_signal(closeadj):
    r = _f06_ret(closeadj).abs()
    result = r.rolling(252, min_periods=max(2, 252 // 2)).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d vol clustering (autocorr of |returns|)
def f06vr_f06_semi_volatility_regime_volcluster_504d_base_v140_signal(closeadj):
    r = _f06_ret(closeadj).abs()
    result = r.rolling(504, min_periods=max(2, 504 // 2)).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EWMA vol minus realized vol
def f06vr_f06_semi_volatility_regime_ewmavsreal_21d_base_v141_signal(closeadj):
    r = _f06_ret(closeadj)
    ewmv = r.ewm(span=21, adjust=False).std() * np.sqrt(252)
    rv = _f06_realvol(r, 21)
    result = ewmv - rv
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EWMA vol minus realized vol
def f06vr_f06_semi_volatility_regime_ewmavsreal_63d_base_v142_signal(closeadj):
    r = _f06_ret(closeadj)
    ewmv = r.ewm(span=63, adjust=False).std() * np.sqrt(252)
    rv = _f06_realvol(r, 63)
    result = ewmv - rv
    return result.replace([np.inf, -np.inf], np.nan)


# 126d EWMA vol minus realized vol
def f06vr_f06_semi_volatility_regime_ewmavsreal_126d_base_v143_signal(closeadj):
    r = _f06_ret(closeadj)
    ewmv = r.ewm(span=126, adjust=False).std() * np.sqrt(252)
    rv = _f06_realvol(r, 126)
    result = ewmv - rv
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EWMA vol minus realized vol
def f06vr_f06_semi_volatility_regime_ewmavsreal_252d_base_v144_signal(closeadj):
    r = _f06_ret(closeadj)
    ewmv = r.ewm(span=252, adjust=False).std() * np.sqrt(252)
    rv = _f06_realvol(r, 252)
    result = ewmv - rv
    return result.replace([np.inf, -np.inf], np.nan)


# 504d EWMA vol minus realized vol
def f06vr_f06_semi_volatility_regime_ewmavsreal_504d_base_v145_signal(closeadj):
    r = _f06_ret(closeadj)
    ewmv = r.ewm(span=504, adjust=False).std() * np.sqrt(252)
    rv = _f06_realvol(r, 504)
    result = ewmv - rv
    return result.replace([np.inf, -np.inf], np.nan)


# short composite: 21z + 63z + 126z of vol
def f06vr_f06_semi_volatility_regime_volcomposite_short_base_v146_signal(closeadj):
    r = _f06_ret(closeadj)
    v21 = _f06_realvol(r, 21)
    v63 = _f06_realvol(r, 63)
    v126 = _f06_realvol(r, 126)
    result = _z(v21, 63) + _z(v63, 126) + _z(v126, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# long composite: 63z + 126z + 252z of vol
def f06vr_f06_semi_volatility_regime_volcomposite_long_base_v147_signal(closeadj):
    r = _f06_ret(closeadj)
    v63 = _f06_realvol(r, 63)
    v126 = _f06_realvol(r, 126)
    v252 = _f06_realvol(r, 252)
    result = _z(v63, 126) + _z(v126, 252) + _z(v252, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime divergence: short - long EMA cross sign of vol
def f06vr_f06_semi_volatility_regime_volregime_divergence_base_v148_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    short = np.sign(v_.ewm(span=21, adjust=False).mean() - v_.ewm(span=63, adjust=False).mean())
    long = np.sign(v_.ewm(span=126, adjust=False).mean() - v_.ewm(span=252, adjust=False).mean())
    result = pd.Series(short - long, index=v_.index)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol quality: vol-of-vol / vol (instability)
def f06vr_f06_semi_volatility_regime_volquality_63d_base_v149_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    vov = _std(v_, 126)
    result = vov / v_.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vol quality: vol-of-vol / vol
def f06vr_f06_semi_volatility_regime_volquality_252d_base_v150_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    vov = _std(v_, 504)
    result = vov / v_.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


