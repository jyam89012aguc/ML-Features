import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_FIVEYEAR = 1260
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
def _z(s, w):
    m = s.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(2, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _rvol(closeadj, w):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    return r.rolling(w, min_periods=max(2, w // 2)).std()


def _hret(closeadj, h):
    return np.log(closeadj.replace(0, np.nan) / closeadj.shift(h).replace(0, np.nan))


def _dnsemi(closeadj, w):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    neg = r.where(r < 0, 0.0)
    return np.sqrt((neg ** 2).rolling(w, min_periods=max(2, w // 2)).mean())


def _upsemi(closeadj, w):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    pos = r.where(r > 0, 0.0)
    return np.sqrt((pos ** 2).rolling(w, min_periods=max(2, w // 2)).mean())


def _ewmavol(closeadj, span):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    return np.sqrt((r ** 2).ewm(span=span, min_periods=max(2, span // 2)).mean())


def _cone(closeadj, w, hist):
    v = _rvol(closeadj, w)
    return v.rolling(hist, min_periods=max(2, hist // 4)).rank(pct=True) - 0.5


# ============================================================
# jerk of base[5d vol]: ROC=5d
def f10rv_f10_realized_volatility_term_rvol_5d_jerk_v001_signal(closeadj):
    base = _rvol(closeadj, 5)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[10d vol]: ROC=10d
def f10rv_f10_realized_volatility_term_rvol_10d_jerk_v002_signal(closeadj):
    base = _rvol(closeadj, 10)
    d1 = base - base.shift(10)
    d2 = d1 - d1.shift(10)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[21d vol]: ROC=21d
def f10rv_f10_realized_volatility_term_rvol_21d_jerk_v003_signal(closeadj):
    base = _rvol(closeadj, 21)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[42d vol]: ROC=42d
def f10rv_f10_realized_volatility_term_rvol_42d_jerk_v004_signal(closeadj):
    base = _rvol(closeadj, 42)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[63d vol (wk roc)]: ROC=5d
def f10rv_f10_realized_volatility_term_rvol_63d_jerk_v005_signal(closeadj):
    base = _rvol(closeadj, 63)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[126d vol]: ROC=63d
def f10rv_f10_realized_volatility_term_rvol_126d_jerk_v006_signal(closeadj):
    base = _rvol(closeadj, 126)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[189d vol (mo roc)]: ROC=21d
def f10rv_f10_realized_volatility_term_rvol_189d_jerk_v007_signal(closeadj):
    base = _rvol(closeadj, 189)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[252d vol]: ROC=126d
def f10rv_f10_realized_volatility_term_rvol_252d_jerk_v008_signal(closeadj):
    base = _rvol(closeadj, 252)
    d1 = base - base.shift(126)
    d2 = d1 - d1.shift(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[21d vol (qtr roc)]: ROC=63d
def f10rv_f10_realized_volatility_term_rvolq_21d_jerk_v009_signal(closeadj):
    base = _rvol(closeadj, 21)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[63d vol (qtr roc)]: ROC=63d
def f10rv_f10_realized_volatility_term_rvolq_63d_jerk_v010_signal(closeadj):
    base = _rvol(closeadj, 63)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[126d vol (mo roc)]: ROC=21d
def f10rv_f10_realized_volatility_term_rvolq_126d_jerk_v011_signal(closeadj):
    base = _rvol(closeadj, 126)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[252d vol (mo roc)]: ROC=21d
def f10rv_f10_realized_volatility_term_rvolq_252d_jerk_v012_signal(closeadj):
    base = _rvol(closeadj, 252)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[vol of 5d ret]: ROC=21d
def f10rv_f10_realized_volatility_term_rvh5_63d_jerk_v013_signal(closeadj):
    base = _hret(closeadj, 5).rolling(63, min_periods=21).std() / np.sqrt(5.0)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[vol of 10d ret]: ROC=21d
def f10rv_f10_realized_volatility_term_rvh10_63d_jerk_v014_signal(closeadj):
    base = _hret(closeadj, 10).rolling(63, min_periods=21).std() / np.sqrt(10.0)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[vol of 21d ret]: ROC=21d
def f10rv_f10_realized_volatility_term_rvh21_126d_jerk_v015_signal(closeadj):
    base = _hret(closeadj, 21).rolling(126, min_periods=42).std() / np.sqrt(21.0)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[vol of 2d ret]: ROC=21d
def f10rv_f10_realized_volatility_term_rvh2_63d_jerk_v016_signal(closeadj):
    base = _hret(closeadj, 2).rolling(63, min_periods=21).std() / np.sqrt(2.0)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[ts 5/21]: ROC=21d
def f10rv_f10_realized_volatility_term_tsr5v21_21d_jerk_v017_signal(closeadj):
    base = _rvol(closeadj, 5) / _rvol(closeadj, 21).replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[ts 5/63]: ROC=21d
def f10rv_f10_realized_volatility_term_tsr5v63_63d_jerk_v018_signal(closeadj):
    base = _rvol(closeadj, 5) / _rvol(closeadj, 63).replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[ts 10/42]: ROC=21d
def f10rv_f10_realized_volatility_term_tsr10v42_42d_jerk_v019_signal(closeadj):
    base = _rvol(closeadj, 10) / _rvol(closeadj, 42).replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[ts 21/63]: ROC=21d
def f10rv_f10_realized_volatility_term_tsr21v63_63d_jerk_v020_signal(closeadj):
    base = _rvol(closeadj, 21) / _rvol(closeadj, 63).replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[ts 21/126]: ROC=5d
def f10rv_f10_realized_volatility_term_tsr21v126_126d_jerk_v021_signal(closeadj):
    base = _rvol(closeadj, 21) / _rvol(closeadj, 126).replace(0, np.nan)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[ts 42/189]: ROC=63d
def f10rv_f10_realized_volatility_term_tsr42v189_189d_jerk_v022_signal(closeadj):
    base = _rvol(closeadj, 42) / _rvol(closeadj, 189).replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[ts 63/252]: ROC=126d
def f10rv_f10_realized_volatility_term_tsr63v252_252d_jerk_v023_signal(closeadj):
    base = _rvol(closeadj, 63) / _rvol(closeadj, 252).replace(0, np.nan)
    d1 = base - base.shift(126)
    d2 = d1 - d1.shift(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[ts 126/252]: ROC=63d
def f10rv_f10_realized_volatility_term_tsr126v252_252d_jerk_v024_signal(closeadj):
    base = _rvol(closeadj, 126) / _rvol(closeadj, 252).replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[ts 10/252]: ROC=21d
def f10rv_f10_realized_volatility_term_tsr10v252_252d_jerk_v025_signal(closeadj):
    base = _rvol(closeadj, 10) / _rvol(closeadj, 252).replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[slope 5->63]: ROC=63d
def f10rv_f10_realized_volatility_term_vslope5_63_63d_jerk_v026_signal(closeadj):
    base = _rvol(closeadj, 63) - _rvol(closeadj, 5)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[slope 21->126]: ROC=126d
def f10rv_f10_realized_volatility_term_vslope21_126_126d_jerk_v027_signal(closeadj):
    base = _rvol(closeadj, 126) - _rvol(closeadj, 21)
    d1 = base - base.shift(126)
    d2 = d1 - d1.shift(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[slope 21->252]: ROC=126d
def f10rv_f10_realized_volatility_term_vslope21_252_252d_jerk_v028_signal(closeadj):
    base = _rvol(closeadj, 252) - _rvol(closeadj, 21)
    d1 = base - base.shift(126)
    d2 = d1 - d1.shift(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[efficiency ratio 63 (trend/vol path)]: ROC=21d
def f10rv_f10_realized_volatility_term_effratio63_63d_jerk_v029_signal(closeadj):
    net = (closeadj - closeadj.shift(63)).abs()
    path = closeadj.diff().abs().rolling(63, min_periods=21).sum()
    base = net / path.replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[bfly 21/63/252]: ROC=63d
def f10rv_f10_realized_volatility_term_curvA_252d_jerk_v030_signal(closeadj):
    base = (_rvol(closeadj, 21) + _rvol(closeadj, 252)) / 2.0 - _rvol(closeadj, 63)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[bfly 5/21/63]: ROC=21d
def f10rv_f10_realized_volatility_term_curvB_63d_jerk_v031_signal(closeadj):
    base = (_rvol(closeadj, 5) + _rvol(closeadj, 63)) / 2.0 - _rvol(closeadj, 21)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[bfly 21/126/252]: ROC=63d
def f10rv_f10_realized_volatility_term_curvC_252d_jerk_v032_signal(closeadj):
    base = (_rvol(closeadj, 21) + _rvol(closeadj, 252)) / 2.0 - _rvol(closeadj, 126)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[log-bfly 21/63/126/252]: ROC=63d
def f10rv_f10_realized_volatility_term_curvlog_252d_jerk_v033_signal(closeadj):
    v21 = np.log(_rvol(closeadj, 21).replace(0, np.nan)); v63 = np.log(_rvol(closeadj, 63).replace(0, np.nan))
    v126 = np.log(_rvol(closeadj, 126).replace(0, np.nan)); v252 = np.log(_rvol(closeadj, 252).replace(0, np.nan))
    base = (v252 - 2.0 * v126 + v63) - (v126 - 2.0 * v63 + v21)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[dn semi 21]: ROC=21d
def f10rv_f10_realized_volatility_term_dnsemi_21d_jerk_v034_signal(closeadj):
    base = _dnsemi(closeadj, 21)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[dn semi 63]: ROC=21d
def f10rv_f10_realized_volatility_term_dnsemi_63d_jerk_v035_signal(closeadj):
    base = _dnsemi(closeadj, 63)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[dn semi 126]: ROC=63d
def f10rv_f10_realized_volatility_term_dnsemi_126d_jerk_v036_signal(closeadj):
    base = _dnsemi(closeadj, 126)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[up semi 21]: ROC=21d
def f10rv_f10_realized_volatility_term_upsemi_21d_jerk_v037_signal(closeadj):
    base = _upsemi(closeadj, 21)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[up semi 63]: ROC=21d
def f10rv_f10_realized_volatility_term_upsemi_63d_jerk_v038_signal(closeadj):
    base = _upsemi(closeadj, 63)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[up semi 126]: ROC=63d
def f10rv_f10_realized_volatility_term_upsemi_126d_jerk_v039_signal(closeadj):
    base = _upsemi(closeadj, 126)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[semi spread 63]: ROC=21d
def f10rv_f10_realized_volatility_term_semispr63_63d_jerk_v040_signal(closeadj):
    base = _dnsemi(closeadj, 63) - _upsemi(closeadj, 63)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[semi spread 126]: ROC=63d
def f10rv_f10_realized_volatility_term_semispr126_126d_jerk_v041_signal(closeadj):
    base = _dnsemi(closeadj, 126) - _upsemi(closeadj, 126)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[semi balance 63]: ROC=63d
def f10rv_f10_realized_volatility_term_semibal63_63d_jerk_v042_signal(closeadj):
    dn = _dnsemi(closeadj, 63); up = _upsemi(closeadj, 63)
    base = (dn - up) / (dn + up).replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[semi balance 252]: ROC=63d
def f10rv_f10_realized_volatility_term_semibal252_252d_jerk_v043_signal(closeadj):
    dn = _dnsemi(closeadj, 252); up = _upsemi(closeadj, 252)
    base = (dn - up) / (dn + up).replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[semi ratio 21]: ROC=21d
def f10rv_f10_realized_volatility_term_semiratio21_21d_jerk_v044_signal(closeadj):
    base = _dnsemi(closeadj, 21) / _upsemi(closeadj, 21).replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[dn semi ts 21/126]: ROC=63d
def f10rv_f10_realized_volatility_term_dnsemits_126d_jerk_v045_signal(closeadj):
    base = _dnsemi(closeadj, 21) / _dnsemi(closeadj, 126).replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[up semi ts 21/126]: ROC=63d
def f10rv_f10_realized_volatility_term_upsemits_126d_jerk_v046_signal(closeadj):
    base = _upsemi(closeadj, 21) / _upsemi(closeadj, 126).replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[dn semi slope 21->126]: ROC=126d
def f10rv_f10_realized_volatility_term_dnsemislope_126d_jerk_v047_signal(closeadj):
    base = _dnsemi(closeadj, 126) - _dnsemi(closeadj, 21)
    d1 = base - base.shift(126)
    d2 = d1 - d1.shift(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[cone 21/252]: ROC=126d
def f10rv_f10_realized_volatility_term_cone21_252_252d_jerk_v048_signal(closeadj):
    base = _cone(closeadj, 21, 252)
    d1 = base - base.shift(126)
    d2 = d1 - d1.shift(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[cone 63/504]: ROC=63d
def f10rv_f10_realized_volatility_term_cone63_504_504d_jerk_v049_signal(closeadj):
    base = _cone(closeadj, 63, 504)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[cone 10/252]: ROC=21d
def f10rv_f10_realized_volatility_term_cone10_252_252d_jerk_v050_signal(closeadj):
    base = _cone(closeadj, 10, 252)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[cone 126/1260]: ROC=126d
def f10rv_f10_realized_volatility_term_cone126_1260_1260d_jerk_v051_signal(closeadj):
    base = _cone(closeadj, 126, 1260)
    d1 = base - base.shift(126)
    d2 = d1 - d1.shift(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[cone 42/504]: ROC=42d
def f10rv_f10_realized_volatility_term_cone42_504_504d_jerk_v052_signal(closeadj):
    base = _cone(closeadj, 42, 504)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[vol skew via |r| mean/median 63]: ROC=21d
def f10rv_f10_realized_volatility_term_rvskewabs_63d_jerk_v053_signal(closeadj):
    ar = np.log(closeadj.replace(0, np.nan)).diff().abs()
    base = ar.rolling(63, min_periods=21).mean() / ar.rolling(63, min_periods=21).median().replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[vol z 63/504]: ROC=126d
def f10rv_f10_realized_volatility_term_conez63_504_504d_jerk_v054_signal(closeadj):
    base = _z(_rvol(closeadj, 63), 504)
    d1 = base - base.shift(126)
    d2 = d1 - d1.shift(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[dn semi cone 63/504]: ROC=63d
def f10rv_f10_realized_volatility_term_dnsemicone_504d_jerk_v055_signal(closeadj):
    dn = _dnsemi(closeadj, 63)
    base = dn.rolling(504, min_periods=126).rank(pct=True) - 0.5
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[vol-adj ret 21]: ROC=21d
def f10rv_f10_realized_volatility_term_vadjret21_21d_jerk_v056_signal(closeadj):
    base = _hret(closeadj, 21) / _rvol(closeadj, 21).replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[vol-adj ret 63]: ROC=21d
def f10rv_f10_realized_volatility_term_vadjret63_63d_jerk_v057_signal(closeadj):
    base = _hret(closeadj, 63) / _rvol(closeadj, 63).replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[vol-adj ret 126]: ROC=63d
def f10rv_f10_realized_volatility_term_vadjret126_126d_jerk_v058_signal(closeadj):
    base = _hret(closeadj, 126) / _rvol(closeadj, 126).replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[vol-adj ret 252]: ROC=63d
def f10rv_f10_realized_volatility_term_vadjret252_252d_jerk_v059_signal(closeadj):
    base = _hret(closeadj, 252) / _rvol(closeadj, 252).replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[sortino 63]: ROC=63d
def f10rv_f10_realized_volatility_term_sortino63_63d_jerk_v060_signal(closeadj):
    base = _hret(closeadj, 63) / (_dnsemi(closeadj, 63) * np.sqrt(63.0)).replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[sortino 21]: ROC=21d
def f10rv_f10_realized_volatility_term_sortino21_21d_jerk_v061_signal(closeadj):
    base = _hret(closeadj, 21) / (_dnsemi(closeadj, 21) * np.sqrt(21.0)).replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[vol-adj ret slope 21-126]: ROC=21d
def f10rv_f10_realized_volatility_term_vadjslope_126d_jerk_v062_signal(closeadj):
    s = _hret(closeadj, 21) / _rvol(closeadj, 21).replace(0, np.nan)
    l = _hret(closeadj, 126) / _rvol(closeadj, 126).replace(0, np.nan)
    base = s - l
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[vov 21/63]: ROC=21d
def f10rv_f10_realized_volatility_term_vov21_63_63d_jerk_v063_signal(closeadj):
    v = _rvol(closeadj, 21)
    base = v.rolling(63, min_periods=21).std()
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[vov 63/252]: ROC=63d
def f10rv_f10_realized_volatility_term_vov63_252_252d_jerk_v064_signal(closeadj):
    v = _rvol(closeadj, 63)
    base = v.rolling(252, min_periods=63).std()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[vov 5/63]: ROC=21d
def f10rv_f10_realized_volatility_term_vov5_63_63d_jerk_v065_signal(closeadj):
    v = _rvol(closeadj, 5)
    base = v.rolling(63, min_periods=21).std()
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[vol cv 21/252]: ROC=63d
def f10rv_f10_realized_volatility_term_volcv21_252d_jerk_v066_signal(closeadj):
    v = _rvol(closeadj, 21)
    base = v.rolling(252, min_periods=63).std() / v.rolling(252, min_periods=63).mean().replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[vol cv 63/504]: ROC=63d
def f10rv_f10_realized_volatility_term_volcv63_504d_jerk_v067_signal(closeadj):
    v = _rvol(closeadj, 63)
    base = v.rolling(504, min_periods=126).std() / v.rolling(504, min_periods=126).mean().replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[micro vov 5/21]: ROC=5d
def f10rv_f10_realized_volatility_term_microvov_21d_jerk_v068_signal(closeadj):
    v = _rvol(closeadj, 5)
    base = v.rolling(21, min_periods=10).std() / v.rolling(21, min_periods=10).mean().replace(0, np.nan)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[log-vov 21/252]: ROC=126d
def f10rv_f10_realized_volatility_term_logvov_252d_jerk_v069_signal(closeadj):
    lv = np.log(_rvol(closeadj, 21).replace(0, np.nan))
    base = lv.rolling(252, min_periods=63).std()
    d1 = base - base.shift(126)
    d2 = d1 - d1.shift(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[abs-return autocorr 63]: ROC=21d
def f10rv_f10_realized_volatility_term_retabsac_63d_jerk_v070_signal(closeadj):
    ar = np.log(closeadj.replace(0, np.nan)).diff().abs()
    base = ar.rolling(63, min_periods=21).corr(ar.shift(1))
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[vol revert 63]: ROC=63d
def f10rv_f10_realized_volatility_term_volrevert63_504d_jerk_v071_signal(closeadj):
    v = _rvol(closeadj, 63)
    ew = v.ewm(span=252, min_periods=63).mean()
    base = (v - ew) / v.rolling(504, min_periods=126).std().replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[vol drawdown 21/252]: ROC=42d
def f10rv_f10_realized_volatility_term_voldd21_252d_jerk_v072_signal(closeadj):
    v = _rvol(closeadj, 21)
    base = v / v.rolling(252, min_periods=63).max().replace(0, np.nan) - 1.0
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[vol exp streak]: ROC=21d
def f10rv_f10_realized_volatility_term_volexp_63d_jerk_v073_signal(closeadj):
    v = _rvol(closeadj, 21)
    above = (v > v.rolling(63, min_periods=21).mean()).astype(float)
    base = above.rolling(63, min_periods=21).mean() - 0.5
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[ewma vol 21]: ROC=21d
def f10rv_f10_realized_volatility_term_ewmavol21_21d_jerk_v074_signal(closeadj):
    base = _ewmavol(closeadj, 21)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[ewma vol 63]: ROC=21d
def f10rv_f10_realized_volatility_term_ewmavol63_63d_jerk_v075_signal(closeadj):
    base = _ewmavol(closeadj, 63)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[ewma ts 10/63]: ROC=21d
def f10rv_f10_realized_volatility_term_ewts10v63_63d_jerk_v076_signal(closeadj):
    base = _ewmavol(closeadj, 10) / _ewmavol(closeadj, 63).replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[ewma ts 21/126]: ROC=63d
def f10rv_f10_realized_volatility_term_ewts21v126_126d_jerk_v077_signal(closeadj):
    base = _ewmavol(closeadj, 21) / _ewmavol(closeadj, 126).replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[ewma-simple gap 63]: ROC=21d
def f10rv_f10_realized_volatility_term_ewmagap_63d_jerk_v078_signal(closeadj):
    ew = _ewmavol(closeadj, 63)
    base = ew / _rvol(closeadj, 126).replace(0, np.nan) - 1.0
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[jump dominance 63]: ROC=21d
def f10rv_f10_realized_volatility_term_jumpdom_63d_jerk_v079_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    base = r.abs().rolling(63, min_periods=21).max() / r.rolling(63, min_periods=21).std().replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[bipower jump 63]: ROC=21d
def f10rv_f10_realized_volatility_term_bipower_63d_jerk_v080_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    bp = (r.abs() * r.shift(1).abs()).rolling(63, min_periods=21).mean() * (np.pi / 2.0)
    rv = (r ** 2).rolling(63, min_periods=21).mean()
    base = 1.0 - bp / rv.replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[rv concentration 21]: ROC=21d
def f10rv_f10_realized_volatility_term_rvconc21_21d_jerk_v081_signal(closeadj):
    r2 = np.log(closeadj.replace(0, np.nan)).diff() ** 2
    base = r2.rolling(21, min_periods=10).max() / r2.rolling(21, min_periods=10).sum().replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[rv concentration 63]: ROC=63d
def f10rv_f10_realized_volatility_term_rvconc63_63d_jerk_v082_signal(closeadj):
    r2 = np.log(closeadj.replace(0, np.nan)).diff() ** 2
    base = r2.rolling(63, min_periods=21).max() / r2.rolling(63, min_periods=21).sum().replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[rv herfindahl 63]: ROC=21d
def f10rv_f10_realized_volatility_term_rvherf_63d_jerk_v083_signal(closeadj):
    r2 = np.log(closeadj.replace(0, np.nan)).diff() ** 2
    base = (r2 ** 2).rolling(63, min_periods=21).sum() / (r2.rolling(63, min_periods=21).sum() ** 2).replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[l1/l2 vol 21]: ROC=21d
def f10rv_f10_realized_volatility_term_l1l2_21_21d_jerk_v084_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    base = r.abs().rolling(21, min_periods=10).mean() / r.rolling(21, min_periods=10).std().replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[l1/l2 vol 63]: ROC=21d
def f10rv_f10_realized_volatility_term_l1l2_63_63d_jerk_v085_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    base = r.abs().rolling(63, min_periods=21).mean() / r.rolling(63, min_periods=21).std().replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[kurtosis 63]: ROC=21d
def f10rv_f10_realized_volatility_term_kurt63_63d_jerk_v086_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    base = r.rolling(63, min_periods=21).kurt()
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[kurtosis 126]: ROC=63d
def f10rv_f10_realized_volatility_term_kurt126_126d_jerk_v087_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    base = r.rolling(126, min_periods=42).kurt()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[skew 63]: ROC=21d
def f10rv_f10_realized_volatility_term_skew63_63d_jerk_v088_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    base = r.rolling(63, min_periods=21).skew()
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[skew 126]: ROC=63d
def f10rv_f10_realized_volatility_term_skew126_126d_jerk_v089_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    base = r.rolling(126, min_periods=42).skew()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[med/std 63]: ROC=21d
def f10rv_f10_realized_volatility_term_medmad_63d_jerk_v090_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    base = r.abs().rolling(63, min_periods=21).median() / r.rolling(63, min_periods=21).std().replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[iqr/std 126]: ROC=63d
def f10rv_f10_realized_volatility_term_iqrstd_126d_jerk_v091_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    q75 = r.rolling(126, min_periods=42).quantile(0.75); q25 = r.rolling(126, min_periods=42).quantile(0.25)
    base = (q75 - q25) / r.rolling(126, min_periods=42).std().replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[vol persistence 63]: ROC=21d
def f10rv_f10_realized_volatility_term_volpersist63_63d_jerk_v092_signal(closeadj):
    r2 = np.log(closeadj.replace(0, np.nan)).diff() ** 2
    base = r2.rolling(63, min_periods=21).corr(r2.shift(1))
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[vol persistence 126]: ROC=63d
def f10rv_f10_realized_volatility_term_volpersist126_126d_jerk_v093_signal(closeadj):
    r2 = np.log(closeadj.replace(0, np.nan)).diff() ** 2
    base = r2.rolling(126, min_periods=42).corr(r2.shift(1))
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[return ac1 63]: ROC=21d
def f10rv_f10_realized_volatility_term_retac1_63d_jerk_v094_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    base = r.rolling(63, min_periods=21).corr(r.shift(1))
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[leverage corr 126]: ROC=63d
def f10rv_f10_realized_volatility_term_leverage_126d_jerk_v095_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    base = r.rolling(126, min_periods=42).corr((r.shift(-1)) ** 2)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[vol ar1 126]: ROC=21d
def f10rv_f10_realized_volatility_term_volar1_126d_jerk_v096_signal(closeadj):
    lv = np.log(_rvol(closeadj, 21).replace(0, np.nan))
    base = lv.rolling(126, min_periods=42).corr(lv.shift(5))
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[variance ratio 5d]: ROC=21d
def f10rv_f10_realized_volatility_term_vr5_126d_jerk_v097_signal(closeadj):
    r1 = np.log(closeadj.replace(0, np.nan)).diff()
    base = (_hret(closeadj, 5) ** 2).rolling(126, min_periods=42).mean() / (5.0 * (r1 ** 2).rolling(126, min_periods=42).mean()).replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[variance ratio 21d]: ROC=63d
def f10rv_f10_realized_volatility_term_vr21_252d_jerk_v098_signal(closeadj):
    r1 = np.log(closeadj.replace(0, np.nan)).diff()
    base = (_hret(closeadj, 21) ** 2).rolling(252, min_periods=84).mean() / (21.0 * (r1 ** 2).rolling(252, min_periods=84).mean()).replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[mad vol 21]: ROC=21d
def f10rv_f10_realized_volatility_term_madvol21_21d_jerk_v099_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    base = r.abs().rolling(21, min_periods=10).mean()
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[mad ts 21/126]: ROC=63d
def f10rv_f10_realized_volatility_term_madts_126d_jerk_v100_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    base = r.abs().rolling(21, min_periods=10).mean() / r.abs().rolling(126, min_periods=42).mean().replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[cone width 21/252]: ROC=63d
def f10rv_f10_realized_volatility_term_conewidth_252d_jerk_v101_signal(closeadj):
    v = _rvol(closeadj, 21)
    hi = v.rolling(252, min_periods=63).quantile(0.9); lo = v.rolling(252, min_periods=63).quantile(0.1)
    base = (hi - lo) / v.rolling(252, min_periods=63).median().replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[cone floor dist 21/252]: ROC=126d
def f10rv_f10_realized_volatility_term_conefloor_252d_jerk_v102_signal(closeadj):
    v = _rvol(closeadj, 21)
    lo = v.rolling(252, min_periods=63).min()
    base = (v - lo) / lo.replace(0, np.nan)
    d1 = base - base.shift(126)
    d2 = d1 - d1.shift(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[cone amplitude 63/1260]: ROC=63d
def f10rv_f10_realized_volatility_term_coneamp_1260d_jerk_v103_signal(closeadj):
    v = _rvol(closeadj, 63)
    base = (v.rolling(1260, min_periods=252).max() - v.rolling(1260, min_periods=252).min()) / v.rolling(1260, min_periods=252).mean().replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[vol mom 21 (wk)]: ROC=21d
def f10rv_f10_realized_volatility_term_volmom21_21d_jerk_v104_signal(closeadj):
    v = _rvol(closeadj, 21)
    base = np.log(v.replace(0, np.nan) / v.shift(5).replace(0, np.nan))
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[vol mom 126 (qtr)]: ROC=63d
def f10rv_f10_realized_volatility_term_volmom126_126d_jerk_v105_signal(closeadj):
    v = _rvol(closeadj, 126)
    base = np.log(v.replace(0, np.nan) / v.shift(63).replace(0, np.nan))
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[vol trend 63]: ROC=63d
def f10rv_f10_realized_volatility_term_voltrend63_63d_jerk_v106_signal(closeadj):
    v = _rvol(closeadj, 63)
    base = np.log(v.replace(0, np.nan) / v.shift(63).replace(0, np.nan))
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[vol accel 21]: ROC=5d
def f10rv_f10_realized_volatility_term_volaccel21_21d_jerk_v107_signal(closeadj):
    v = _rvol(closeadj, 21)
    base = v - 2.0 * v.shift(5) + v.shift(10)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[ts dispersion]: ROC=63d
def f10rv_f10_realized_volatility_term_tsdisp_252d_jerk_v108_signal(closeadj):
    stk = pd.concat([_rvol(closeadj,5),_rvol(closeadj,21),_rvol(closeadj,63),_rvol(closeadj,126),_rvol(closeadj,252)], axis=1)
    base = stk.std(axis=1) / stk.mean(axis=1).replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[ts rolldown]: ROC=63d
def f10rv_f10_realized_volatility_term_rolldown_252d_jerk_v109_signal(closeadj):
    v63 = _rvol(closeadj, 63); v126 = _rvol(closeadj, 126); v252 = _rvol(closeadj, 252)
    base = (v63 - (2.0 * v126 - v252)) / v126.replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[curve-center distance]: ROC=63d
def f10rv_f10_realized_volatility_term_curvecenter_252d_jerk_v110_signal(closeadj):
    center = (_rvol(closeadj,21)+_rvol(closeadj,63)+_rvol(closeadj,126)+_rvol(closeadj,252)) / 4.0
    base = _rvol(closeadj, 21) / center.replace(0, np.nan) - 1.0
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[curve twist]: ROC=63d
def f10rv_f10_realized_volatility_term_tstwist_252d_jerk_v111_signal(closeadj):
    near = _rvol(closeadj, 21) / _rvol(closeadj, 63).replace(0, np.nan)
    far = _rvol(closeadj, 126) / _rvol(closeadj, 252).replace(0, np.nan)
    base = near - far
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[vol curve center-of-mass]: ROC=63d
def f10rv_f10_realized_volatility_term_volcom_252d_jerk_v112_signal(closeadj):
    w = np.array([5.0, 21.0, 63.0, 126.0, 252.0])
    stk = pd.concat([_rvol(closeadj,5),_rvol(closeadj,21),_rvol(closeadj,63),_rvol(closeadj,126),_rvol(closeadj,252)], axis=1)
    base = np.log(((stk * w).sum(axis=1) / stk.sum(axis=1).replace(0, np.nan)).replace(0, np.nan))
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[31d vol]: ROC=21d
def f10rv_f10_realized_volatility_term_rvol_31d_jerk_v113_signal(closeadj):
    base = _rvol(closeadj, 31)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[84d vol]: ROC=21d
def f10rv_f10_realized_volatility_term_rvol_84d_jerk_v114_signal(closeadj):
    base = _rvol(closeadj, 84)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[168d vol]: ROC=63d
def f10rv_f10_realized_volatility_term_rvol_168d_jerk_v115_signal(closeadj):
    base = _rvol(closeadj, 168)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[504d vol]: ROC=63d
def f10rv_f10_realized_volatility_term_rvol_504d_jerk_v116_signal(closeadj):
    base = _rvol(closeadj, 504)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[ts 31/126]: ROC=63d
def f10rv_f10_realized_volatility_term_tsr31v126_126d_jerk_v117_signal(closeadj):
    base = _rvol(closeadj, 31) / _rvol(closeadj, 126).replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[ts 84/252]: ROC=63d
def f10rv_f10_realized_volatility_term_tsr84v252_252d_jerk_v118_signal(closeadj):
    base = _rvol(closeadj, 84) / _rvol(closeadj, 252).replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[dn semi 168]: ROC=63d
def f10rv_f10_realized_volatility_term_dnsemi168_168d_jerk_v119_signal(closeadj):
    base = _dnsemi(closeadj, 168)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[up semi 168]: ROC=63d
def f10rv_f10_realized_volatility_term_upsemi168_168d_jerk_v120_signal(closeadj):
    base = _upsemi(closeadj, 168)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[vol of 3d ret]: ROC=21d
def f10rv_f10_realized_volatility_term_rvh3_63d_jerk_v121_signal(closeadj):
    base = _hret(closeadj, 3).rolling(63, min_periods=21).std() / np.sqrt(3.0)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[vol of 42d ret]: ROC=63d
def f10rv_f10_realized_volatility_term_rvh42_252d_jerk_v122_signal(closeadj):
    base = _hret(closeadj, 42).rolling(252, min_periods=84).std() / np.sqrt(42.0)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[efficiency ratio 21 (trend/vol path)]: ROC=21d
def f10rv_f10_realized_volatility_term_effratio21_21d_jerk_v123_signal(closeadj):
    net = (closeadj - closeadj.shift(21)).abs()
    path = closeadj.diff().abs().rolling(21, min_periods=10).sum()
    base = net / path.replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[gain/pain vol ratio 63]: ROC=21d
def f10rv_f10_realized_volatility_term_gainpainvol_63d_jerk_v124_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    gain = r.where(r > 0, 0.0).rolling(63, min_periods=21).sum()
    pain = (-r.where(r < 0, 0.0)).rolling(63, min_periods=21).sum()
    base = gain / pain.replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[realized variance 21]: ROC=21d
def f10rv_f10_realized_volatility_term_rvar21_21d_jerk_v125_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    base = (r ** 2).rolling(21, min_periods=10).sum()
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[realized variance 63]: ROC=21d
def f10rv_f10_realized_volatility_term_rvar63_63d_jerk_v126_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    base = (r ** 2).rolling(63, min_periods=21).sum()
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[cc-ewma estimator gap 21]: ROC=21d
def f10rv_f10_realized_volatility_term_estgap_21d_jerk_v127_signal(closeadj):
    cc = _rvol(closeadj, 21); ew = _ewmavol(closeadj, 21)
    base = (cc - ew) / ((cc + ew) / 2.0).replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[vol of 7d ret]: ROC=21d
def f10rv_f10_realized_volatility_term_rvh7_63d_jerk_v128_signal(closeadj):
    base = _hret(closeadj, 7).rolling(63, min_periods=21).std() / np.sqrt(7.0)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[dn semi cone 21/252]: ROC=21d
def f10rv_f10_realized_volatility_term_dnsemicone21_252d_jerk_v129_signal(closeadj):
    dn = _dnsemi(closeadj, 21)
    base = dn.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[up semi cone 21/252]: ROC=63d
def f10rv_f10_realized_volatility_term_upsemicone21_252d_jerk_v130_signal(closeadj):
    up = _upsemi(closeadj, 21)
    base = up.rolling(252, min_periods=63).rank(pct=True) - 0.5
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[vol swing 63]: ROC=21d
def f10rv_f10_realized_volatility_term_volswing_63d_jerk_v131_signal(closeadj):
    v = _rvol(closeadj, 21)
    base = (v.rolling(63, min_periods=21).max() - v.rolling(63, min_periods=21).min()) / v.rolling(63, min_periods=21).mean().replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[vol series skew]: ROC=63d
def f10rv_f10_realized_volatility_term_volseriesskew_252d_jerk_v132_signal(closeadj):
    v = _rvol(closeadj, 21)
    base = v.rolling(252, min_periods=63).skew()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[log-range realized vol proxy 63]: ROC=21d
def f10rv_f10_realized_volatility_term_rangevol63_63d_jerk_v133_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    hi = lr.rolling(63, min_periods=21).max(); lo = lr.rolling(63, min_periods=21).min()
    base = (hi - lo) / lr.rolling(63, min_periods=21).std().replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[ts 5/126]: ROC=126d
def f10rv_f10_realized_volatility_term_tsr5v126_126d_jerk_v134_signal(closeadj):
    base = _rvol(closeadj, 5) / _rvol(closeadj, 126).replace(0, np.nan)
    d1 = base - base.shift(126)
    d2 = d1 - d1.shift(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[cone spread 21 vs 126]: ROC=21d
def f10rv_f10_realized_volatility_term_conespread21v126_252d_jerk_v135_signal(closeadj):
    c21 = _cone(closeadj, 21, 252); c126 = _cone(closeadj, 126, 504)
    base = c21 - c126
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[slope 10->63]: ROC=5d
def f10rv_f10_realized_volatility_term_vslope10_63_63d_jerk_v136_signal(closeadj):
    base = _rvol(closeadj, 63) - _rvol(closeadj, 10)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[slope 42->252]: ROC=63d
def f10rv_f10_realized_volatility_term_vslope42_252_252d_jerk_v137_signal(closeadj):
    base = _rvol(closeadj, 252) - _rvol(closeadj, 42)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[vov 126/504]: ROC=63d
def f10rv_f10_realized_volatility_term_vov126_504_504d_jerk_v138_signal(closeadj):
    v = _rvol(closeadj, 126)
    base = v.rolling(504, min_periods=126).std()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[cone mom 63/504]: ROC=63d
def f10rv_f10_realized_volatility_term_conemom_504d_jerk_v139_signal(closeadj):
    cp = _cone(closeadj, 63, 504)
    base = cp - cp.shift(21)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[cone slope 21v126]: ROC=63d
def f10rv_f10_realized_volatility_term_coneslope_252d_jerk_v140_signal(closeadj):
    c21 = _rvol(closeadj, 21).rolling(252, min_periods=63).rank(pct=True)
    c126 = _rvol(closeadj, 126).rolling(252, min_periods=63).rank(pct=True)
    base = c21 - c126
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[vol z gap 21-126]: ROC=21d
def f10rv_f10_realized_volatility_term_volzgap_252d_jerk_v141_signal(closeadj):
    base = _z(_rvol(closeadj, 21), 252) - _z(_rvol(closeadj, 126), 252)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[extreme intensity 63]: ROC=21d
def f10rv_f10_realized_volatility_term_extremeint_63d_jerk_v142_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    sd = r.rolling(63, min_periods=21).std()
    base = (r.abs() / (2.0 * sd).replace(0, np.nan) - 1.0).clip(lower=0).rolling(63, min_periods=21).mean()
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[tail asymmetry 63]: ROC=21d
def f10rv_f10_realized_volatility_term_tailasym_63d_jerk_v143_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    sd = r.rolling(63, min_periods=21).std()
    dn = (-r - 1.5 * sd).clip(lower=0).rolling(63, min_periods=21).mean()
    up = (r - 1.5 * sd).clip(lower=0).rolling(63, min_periods=21).mean()
    base = (dn - up) / sd.replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[vol elasticity 21]: ROC=21d
def f10rv_f10_realized_volatility_term_volelast_21d_jerk_v144_signal(closeadj):
    v = _rvol(closeadj, 21)
    dvol = np.log(v.replace(0, np.nan) / v.shift(21).replace(0, np.nan))
    base = dvol * np.sign(_hret(closeadj, 21))
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[vol after down 126]: ROC=63d
def f10rv_f10_realized_volatility_term_volafterdown_126d_jerk_v145_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff(); r2 = r ** 2
    vd = r2.where(r.shift(1) < 0).rolling(126, min_periods=30).mean()
    vu = r2.where(r.shift(1) > 0).rolling(126, min_periods=30).mean()
    base = np.sqrt(vd) - np.sqrt(vu)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[risk-adj-ret vol 126]: ROC=63d
def f10rv_f10_realized_volatility_term_riskadjvol_126d_jerk_v146_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    ra = r / r.rolling(21, min_periods=10).std().replace(0, np.nan)
    base = ra.rolling(126, min_periods=42).std()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[rv entropy 63]: ROC=21d
def f10rv_f10_realized_volatility_term_rventropy_63d_jerk_v147_signal(closeadj):
    r2 = np.log(closeadj.replace(0, np.nan)).diff() ** 2
    def _ent(a):
        s = a.sum()
        if s <= 0:
            return np.nan
        p = a / s; p = p[p > 0]
        return -(p * np.log(p)).sum() / np.log(len(a))
    base = r2.rolling(63, min_periods=21).apply(_ent, raw=True)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[curvature rank]: ROC=63d
def f10rv_f10_realized_volatility_term_curvrank_252d_jerk_v148_signal(closeadj):
    v21 = _rvol(closeadj, 21); v63 = _rvol(closeadj, 63); v252 = _rvol(closeadj, 252)
    bf = ((v21 + v252) / 2.0 - v63) / v63.replace(0, np.nan)
    base = bf.rolling(504, min_periods=126).rank(pct=True) - 0.5
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[compression run 21/252]: ROC=21d
def f10rv_f10_realized_volatility_term_compressrun_63d_jerk_v149_signal(closeadj):
    v = _rvol(closeadj, 21)
    q25 = v.rolling(252, min_periods=63).quantile(0.25)
    base = (v <= q25).astype(float).rolling(63, min_periods=21).mean() - 0.3
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of base[bipower jump 21]: ROC=21d
def f10rv_f10_realized_volatility_term_bipower21_21d_jerk_v150_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    bp = (r.abs() * r.shift(1).abs()).rolling(21, min_periods=10).mean() * (np.pi / 2.0)
    rv = (r ** 2).rolling(21, min_periods=10).mean()
    base = 1.0 - bp / rv.replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f10rv_f10_realized_volatility_term_rvol_5d_jerk_v001_signal,
    f10rv_f10_realized_volatility_term_rvol_10d_jerk_v002_signal,
    f10rv_f10_realized_volatility_term_rvol_21d_jerk_v003_signal,
    f10rv_f10_realized_volatility_term_rvol_42d_jerk_v004_signal,
    f10rv_f10_realized_volatility_term_rvol_63d_jerk_v005_signal,
    f10rv_f10_realized_volatility_term_rvol_126d_jerk_v006_signal,
    f10rv_f10_realized_volatility_term_rvol_189d_jerk_v007_signal,
    f10rv_f10_realized_volatility_term_rvol_252d_jerk_v008_signal,
    f10rv_f10_realized_volatility_term_rvolq_21d_jerk_v009_signal,
    f10rv_f10_realized_volatility_term_rvolq_63d_jerk_v010_signal,
    f10rv_f10_realized_volatility_term_rvolq_126d_jerk_v011_signal,
    f10rv_f10_realized_volatility_term_rvolq_252d_jerk_v012_signal,
    f10rv_f10_realized_volatility_term_rvh5_63d_jerk_v013_signal,
    f10rv_f10_realized_volatility_term_rvh10_63d_jerk_v014_signal,
    f10rv_f10_realized_volatility_term_rvh21_126d_jerk_v015_signal,
    f10rv_f10_realized_volatility_term_rvh2_63d_jerk_v016_signal,
    f10rv_f10_realized_volatility_term_tsr5v21_21d_jerk_v017_signal,
    f10rv_f10_realized_volatility_term_tsr5v63_63d_jerk_v018_signal,
    f10rv_f10_realized_volatility_term_tsr10v42_42d_jerk_v019_signal,
    f10rv_f10_realized_volatility_term_tsr21v63_63d_jerk_v020_signal,
    f10rv_f10_realized_volatility_term_tsr21v126_126d_jerk_v021_signal,
    f10rv_f10_realized_volatility_term_tsr42v189_189d_jerk_v022_signal,
    f10rv_f10_realized_volatility_term_tsr63v252_252d_jerk_v023_signal,
    f10rv_f10_realized_volatility_term_tsr126v252_252d_jerk_v024_signal,
    f10rv_f10_realized_volatility_term_tsr10v252_252d_jerk_v025_signal,
    f10rv_f10_realized_volatility_term_vslope5_63_63d_jerk_v026_signal,
    f10rv_f10_realized_volatility_term_vslope21_126_126d_jerk_v027_signal,
    f10rv_f10_realized_volatility_term_vslope21_252_252d_jerk_v028_signal,
    f10rv_f10_realized_volatility_term_effratio63_63d_jerk_v029_signal,
    f10rv_f10_realized_volatility_term_curvA_252d_jerk_v030_signal,
    f10rv_f10_realized_volatility_term_curvB_63d_jerk_v031_signal,
    f10rv_f10_realized_volatility_term_curvC_252d_jerk_v032_signal,
    f10rv_f10_realized_volatility_term_curvlog_252d_jerk_v033_signal,
    f10rv_f10_realized_volatility_term_dnsemi_21d_jerk_v034_signal,
    f10rv_f10_realized_volatility_term_dnsemi_63d_jerk_v035_signal,
    f10rv_f10_realized_volatility_term_dnsemi_126d_jerk_v036_signal,
    f10rv_f10_realized_volatility_term_upsemi_21d_jerk_v037_signal,
    f10rv_f10_realized_volatility_term_upsemi_63d_jerk_v038_signal,
    f10rv_f10_realized_volatility_term_upsemi_126d_jerk_v039_signal,
    f10rv_f10_realized_volatility_term_semispr63_63d_jerk_v040_signal,
    f10rv_f10_realized_volatility_term_semispr126_126d_jerk_v041_signal,
    f10rv_f10_realized_volatility_term_semibal63_63d_jerk_v042_signal,
    f10rv_f10_realized_volatility_term_semibal252_252d_jerk_v043_signal,
    f10rv_f10_realized_volatility_term_semiratio21_21d_jerk_v044_signal,
    f10rv_f10_realized_volatility_term_dnsemits_126d_jerk_v045_signal,
    f10rv_f10_realized_volatility_term_upsemits_126d_jerk_v046_signal,
    f10rv_f10_realized_volatility_term_dnsemislope_126d_jerk_v047_signal,
    f10rv_f10_realized_volatility_term_cone21_252_252d_jerk_v048_signal,
    f10rv_f10_realized_volatility_term_cone63_504_504d_jerk_v049_signal,
    f10rv_f10_realized_volatility_term_cone10_252_252d_jerk_v050_signal,
    f10rv_f10_realized_volatility_term_cone126_1260_1260d_jerk_v051_signal,
    f10rv_f10_realized_volatility_term_cone42_504_504d_jerk_v052_signal,
    f10rv_f10_realized_volatility_term_rvskewabs_63d_jerk_v053_signal,
    f10rv_f10_realized_volatility_term_conez63_504_504d_jerk_v054_signal,
    f10rv_f10_realized_volatility_term_dnsemicone_504d_jerk_v055_signal,
    f10rv_f10_realized_volatility_term_vadjret21_21d_jerk_v056_signal,
    f10rv_f10_realized_volatility_term_vadjret63_63d_jerk_v057_signal,
    f10rv_f10_realized_volatility_term_vadjret126_126d_jerk_v058_signal,
    f10rv_f10_realized_volatility_term_vadjret252_252d_jerk_v059_signal,
    f10rv_f10_realized_volatility_term_sortino63_63d_jerk_v060_signal,
    f10rv_f10_realized_volatility_term_sortino21_21d_jerk_v061_signal,
    f10rv_f10_realized_volatility_term_vadjslope_126d_jerk_v062_signal,
    f10rv_f10_realized_volatility_term_vov21_63_63d_jerk_v063_signal,
    f10rv_f10_realized_volatility_term_vov63_252_252d_jerk_v064_signal,
    f10rv_f10_realized_volatility_term_vov5_63_63d_jerk_v065_signal,
    f10rv_f10_realized_volatility_term_volcv21_252d_jerk_v066_signal,
    f10rv_f10_realized_volatility_term_volcv63_504d_jerk_v067_signal,
    f10rv_f10_realized_volatility_term_microvov_21d_jerk_v068_signal,
    f10rv_f10_realized_volatility_term_logvov_252d_jerk_v069_signal,
    f10rv_f10_realized_volatility_term_retabsac_63d_jerk_v070_signal,
    f10rv_f10_realized_volatility_term_volrevert63_504d_jerk_v071_signal,
    f10rv_f10_realized_volatility_term_voldd21_252d_jerk_v072_signal,
    f10rv_f10_realized_volatility_term_volexp_63d_jerk_v073_signal,
    f10rv_f10_realized_volatility_term_ewmavol21_21d_jerk_v074_signal,
    f10rv_f10_realized_volatility_term_ewmavol63_63d_jerk_v075_signal,
    f10rv_f10_realized_volatility_term_ewts10v63_63d_jerk_v076_signal,
    f10rv_f10_realized_volatility_term_ewts21v126_126d_jerk_v077_signal,
    f10rv_f10_realized_volatility_term_ewmagap_63d_jerk_v078_signal,
    f10rv_f10_realized_volatility_term_jumpdom_63d_jerk_v079_signal,
    f10rv_f10_realized_volatility_term_bipower_63d_jerk_v080_signal,
    f10rv_f10_realized_volatility_term_rvconc21_21d_jerk_v081_signal,
    f10rv_f10_realized_volatility_term_rvconc63_63d_jerk_v082_signal,
    f10rv_f10_realized_volatility_term_rvherf_63d_jerk_v083_signal,
    f10rv_f10_realized_volatility_term_l1l2_21_21d_jerk_v084_signal,
    f10rv_f10_realized_volatility_term_l1l2_63_63d_jerk_v085_signal,
    f10rv_f10_realized_volatility_term_kurt63_63d_jerk_v086_signal,
    f10rv_f10_realized_volatility_term_kurt126_126d_jerk_v087_signal,
    f10rv_f10_realized_volatility_term_skew63_63d_jerk_v088_signal,
    f10rv_f10_realized_volatility_term_skew126_126d_jerk_v089_signal,
    f10rv_f10_realized_volatility_term_medmad_63d_jerk_v090_signal,
    f10rv_f10_realized_volatility_term_iqrstd_126d_jerk_v091_signal,
    f10rv_f10_realized_volatility_term_volpersist63_63d_jerk_v092_signal,
    f10rv_f10_realized_volatility_term_volpersist126_126d_jerk_v093_signal,
    f10rv_f10_realized_volatility_term_retac1_63d_jerk_v094_signal,
    f10rv_f10_realized_volatility_term_leverage_126d_jerk_v095_signal,
    f10rv_f10_realized_volatility_term_volar1_126d_jerk_v096_signal,
    f10rv_f10_realized_volatility_term_vr5_126d_jerk_v097_signal,
    f10rv_f10_realized_volatility_term_vr21_252d_jerk_v098_signal,
    f10rv_f10_realized_volatility_term_madvol21_21d_jerk_v099_signal,
    f10rv_f10_realized_volatility_term_madts_126d_jerk_v100_signal,
    f10rv_f10_realized_volatility_term_conewidth_252d_jerk_v101_signal,
    f10rv_f10_realized_volatility_term_conefloor_252d_jerk_v102_signal,
    f10rv_f10_realized_volatility_term_coneamp_1260d_jerk_v103_signal,
    f10rv_f10_realized_volatility_term_volmom21_21d_jerk_v104_signal,
    f10rv_f10_realized_volatility_term_volmom126_126d_jerk_v105_signal,
    f10rv_f10_realized_volatility_term_voltrend63_63d_jerk_v106_signal,
    f10rv_f10_realized_volatility_term_volaccel21_21d_jerk_v107_signal,
    f10rv_f10_realized_volatility_term_tsdisp_252d_jerk_v108_signal,
    f10rv_f10_realized_volatility_term_rolldown_252d_jerk_v109_signal,
    f10rv_f10_realized_volatility_term_curvecenter_252d_jerk_v110_signal,
    f10rv_f10_realized_volatility_term_tstwist_252d_jerk_v111_signal,
    f10rv_f10_realized_volatility_term_volcom_252d_jerk_v112_signal,
    f10rv_f10_realized_volatility_term_rvol_31d_jerk_v113_signal,
    f10rv_f10_realized_volatility_term_rvol_84d_jerk_v114_signal,
    f10rv_f10_realized_volatility_term_rvol_168d_jerk_v115_signal,
    f10rv_f10_realized_volatility_term_rvol_504d_jerk_v116_signal,
    f10rv_f10_realized_volatility_term_tsr31v126_126d_jerk_v117_signal,
    f10rv_f10_realized_volatility_term_tsr84v252_252d_jerk_v118_signal,
    f10rv_f10_realized_volatility_term_dnsemi168_168d_jerk_v119_signal,
    f10rv_f10_realized_volatility_term_upsemi168_168d_jerk_v120_signal,
    f10rv_f10_realized_volatility_term_rvh3_63d_jerk_v121_signal,
    f10rv_f10_realized_volatility_term_rvh42_252d_jerk_v122_signal,
    f10rv_f10_realized_volatility_term_effratio21_21d_jerk_v123_signal,
    f10rv_f10_realized_volatility_term_gainpainvol_63d_jerk_v124_signal,
    f10rv_f10_realized_volatility_term_rvar21_21d_jerk_v125_signal,
    f10rv_f10_realized_volatility_term_rvar63_63d_jerk_v126_signal,
    f10rv_f10_realized_volatility_term_estgap_21d_jerk_v127_signal,
    f10rv_f10_realized_volatility_term_rvh7_63d_jerk_v128_signal,
    f10rv_f10_realized_volatility_term_dnsemicone21_252d_jerk_v129_signal,
    f10rv_f10_realized_volatility_term_upsemicone21_252d_jerk_v130_signal,
    f10rv_f10_realized_volatility_term_volswing_63d_jerk_v131_signal,
    f10rv_f10_realized_volatility_term_volseriesskew_252d_jerk_v132_signal,
    f10rv_f10_realized_volatility_term_rangevol63_63d_jerk_v133_signal,
    f10rv_f10_realized_volatility_term_tsr5v126_126d_jerk_v134_signal,
    f10rv_f10_realized_volatility_term_conespread21v126_252d_jerk_v135_signal,
    f10rv_f10_realized_volatility_term_vslope10_63_63d_jerk_v136_signal,
    f10rv_f10_realized_volatility_term_vslope42_252_252d_jerk_v137_signal,
    f10rv_f10_realized_volatility_term_vov126_504_504d_jerk_v138_signal,
    f10rv_f10_realized_volatility_term_conemom_504d_jerk_v139_signal,
    f10rv_f10_realized_volatility_term_coneslope_252d_jerk_v140_signal,
    f10rv_f10_realized_volatility_term_volzgap_252d_jerk_v141_signal,
    f10rv_f10_realized_volatility_term_extremeint_63d_jerk_v142_signal,
    f10rv_f10_realized_volatility_term_tailasym_63d_jerk_v143_signal,
    f10rv_f10_realized_volatility_term_volelast_21d_jerk_v144_signal,
    f10rv_f10_realized_volatility_term_volafterdown_126d_jerk_v145_signal,
    f10rv_f10_realized_volatility_term_riskadjvol_126d_jerk_v146_signal,
    f10rv_f10_realized_volatility_term_rventropy_63d_jerk_v147_signal,
    f10rv_f10_realized_volatility_term_curvrank_252d_jerk_v148_signal,
    f10rv_f10_realized_volatility_term_compressrun_63d_jerk_v149_signal,
    f10rv_f10_realized_volatility_term_bipower21_21d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F10_REALIZED_VOLATILITY_TERM_REGISTRY_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0003, 0.035, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")

    cols = {"closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 20, "%s nunique=%d" % (name, q.nunique())
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        results[name] = y1.iloc[504:]
        n_features += 1

    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), "nan_ok=%d/%d" % (nan_ok, n_features)

    items = list(results.items())
    for i in range(len(items)):
        ni, si = items[i]
        ai = si.dropna()
        for j in range(i + 1, len(items)):
            nj, sj = items[j]
            aj = sj.dropna()
            idx = ai.index.intersection(aj.index)
            if len(idx) < 30:
                continue
            c = ai.loc[idx].corr(aj.loc[idx])
            if c is None or np.isnan(c):
                continue
            assert abs(c) <= 0.97, "CORR %s vs %s = %.4f" % (ni, nj, c)

    print("OK f10_realized_volatility_term_3rd_derivatives_001_150_claude: %d features pass" % n_features)
