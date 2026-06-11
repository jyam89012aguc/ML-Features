"""f08_relative_strength_rotation math-derivative features.

Each feature computes a relative-strength / trend-persistence base quantity
(efficiency ratio, Hurst-like R/S, return autocorrelation, run-length, self-
relative momentum, risk-adjusted RS, trend slope/monotonicity) on `closeadj`,
then takes a discrete math derivative: slope = 1st difference (ROC) of the base,
jerk = 2nd difference. ROC window is matched to the base window per the build
spec. Every function is fully expanded inline (no factories/exec/importlib).
"""
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
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _efficiency_ratio(close, w):
    net = (close - close.shift(w)).abs()
    path = close.diff().abs().rolling(w, min_periods=max(2, w // 2)).sum()
    return net / path.replace(0, np.nan)


def _autocorr(logret, w, lag):
    def _ac(a):
        a = a[~np.isnan(a)]
        if len(a) < lag + 5:
            return np.nan
        x = a[:-lag]
        y = a[lag:]
        if x.std() <= 0 or y.std() <= 0:
            return np.nan
        return np.corrcoef(x, y)[0, 1]
    return logret.rolling(w, min_periods=max(lag + 5, w // 2)).apply(_ac, raw=True)


def _rs_exponent(logret, w):
    def _rs(a):
        a = a[~np.isnan(a)]
        m = len(a)
        if m < 8:
            return np.nan
        mean = a.mean()
        dev = np.cumsum(a - mean)
        R = dev.max() - dev.min()
        S = a.std()
        if S <= 0 or R <= 0:
            return np.nan
        return np.log(R / S) / np.log(m)
    return logret.rolling(w, min_periods=max(8, w // 2)).apply(_rs, raw=True)


def _trend_slope(logprice, w):
    def _slp(a):
        if np.isnan(a).any():
            return np.nan
        xc = np.arange(len(a), dtype=float)
        xc = xc - xc.mean()
        denom = (xc ** 2).sum()
        if denom <= 0:
            return np.nan
        return float(np.dot(xc, a - a.mean()) / denom)
    return logprice.rolling(w, min_periods=max(8, w // 2)).apply(_slp, raw=True)



def f08rs_f08_relative_strength_rotation_effr_21d_jerk_v001_signal(closeadj):
    base = _efficiency_ratio(closeadj, 21)
    result = base.diff(5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_effr_42d_jerk_v002_signal(closeadj):
    base = _efficiency_ratio(closeadj, 42)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_effr_63d_jerk_v003_signal(closeadj):
    base = _efficiency_ratio(closeadj, 63)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_effr_84d_jerk_v004_signal(closeadj):
    base = _efficiency_ratio(closeadj, 84)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_effr_126d_jerk_v005_signal(closeadj):
    base = _efficiency_ratio(closeadj, 126)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_effr_189d_jerk_v006_signal(closeadj):
    base = _efficiency_ratio(closeadj, 189)
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_effr_252d_jerk_v007_signal(closeadj):
    base = _efficiency_ratio(closeadj, 252)
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_effr_504d_jerk_v008_signal(closeadj):
    base = _efficiency_ratio(closeadj, 504)
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_effrsgn_42d_jerk_v009_signal(closeadj):
    base = _efficiency_ratio(closeadj, 42) * np.sign(closeadj - closeadj.shift(42))
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_effrsgn_63d_jerk_v010_signal(closeadj):
    base = _efficiency_ratio(closeadj, 63) * np.sign(closeadj - closeadj.shift(63))
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_effrsgn_84d_jerk_v011_signal(closeadj):
    base = _efficiency_ratio(closeadj, 84) * np.sign(closeadj - closeadj.shift(84))
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_effrsgn_126d_jerk_v012_signal(closeadj):
    base = _efficiency_ratio(closeadj, 126) * np.sign(closeadj - closeadj.shift(126))
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_effrsgn_189d_jerk_v013_signal(closeadj):
    base = _efficiency_ratio(closeadj, 189) * np.sign(closeadj - closeadj.shift(189))
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_effrsgn_252d_jerk_v014_signal(closeadj):
    base = _efficiency_ratio(closeadj, 252) * np.sign(closeadj - closeadj.shift(252))
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_effrsgn_504d_jerk_v015_signal(closeadj):
    base = _efficiency_ratio(closeadj, 504) * np.sign(closeadj - closeadj.shift(504))
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_hurst_42d_jerk_v016_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = _rs_exponent(lr, 42)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_hurst_63d_jerk_v017_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = _rs_exponent(lr, 63)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_hurst_84d_jerk_v018_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = _rs_exponent(lr, 84)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_hurst_105d_jerk_v019_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = _rs_exponent(lr, 105)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_hurst_126d_jerk_v020_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = _rs_exponent(lr, 126)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_hurst_189d_jerk_v021_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = _rs_exponent(lr, 189)
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_hurst_252d_jerk_v022_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = _rs_exponent(lr, 252)
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_hurst_504d_jerk_v023_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = _rs_exponent(lr, 504)
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_acf1_42d_jerk_v024_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = _autocorr(lr, 42, 1)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_acf1_63d_jerk_v025_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = _autocorr(lr, 63, 1)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_acf1_84d_jerk_v026_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = _autocorr(lr, 84, 1)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_acf1_105d_jerk_v027_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = _autocorr(lr, 105, 1)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_acf1_126d_jerk_v028_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = _autocorr(lr, 126, 1)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_acf1_189d_jerk_v029_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = _autocorr(lr, 189, 1)
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_acf1_252d_jerk_v030_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = _autocorr(lr, 252, 1)
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_acf5_84d_jerk_v031_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = _autocorr(lr, 84, 5)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_acf5_105d_jerk_v032_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = _autocorr(lr, 105, 5)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_acf5_126d_jerk_v033_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = _autocorr(lr, 126, 5)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_acf5_189d_jerk_v034_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = _autocorr(lr, 189, 5)
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_acf5_252d_jerk_v035_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = _autocorr(lr, 252, 5)
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_acf5_504d_jerk_v036_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = _autocorr(lr, 504, 5)
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_varratio_84d_jerk_v037_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    v1 = lr.rolling(84, min_periods=max(2,84//2)).var()
    v5 = lr.rolling(5).sum().rolling(84, min_periods=max(2,84//2)).var()
    base = v5 / (5.0 * v1).replace(0, np.nan) - 1.0
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_varratio_105d_jerk_v038_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    v1 = lr.rolling(105, min_periods=max(2,105//2)).var()
    v5 = lr.rolling(5).sum().rolling(105, min_periods=max(2,105//2)).var()
    base = v5 / (5.0 * v1).replace(0, np.nan) - 1.0
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_varratio_126d_jerk_v039_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    v1 = lr.rolling(126, min_periods=max(2,126//2)).var()
    v5 = lr.rolling(5).sum().rolling(126, min_periods=max(2,126//2)).var()
    base = v5 / (5.0 * v1).replace(0, np.nan) - 1.0
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_varratio_189d_jerk_v040_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    v1 = lr.rolling(189, min_periods=max(2,189//2)).var()
    v5 = lr.rolling(5).sum().rolling(189, min_periods=max(2,189//2)).var()
    base = v5 / (5.0 * v1).replace(0, np.nan) - 1.0
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_varratio_252d_jerk_v041_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    v1 = lr.rolling(252, min_periods=max(2,252//2)).var()
    v5 = lr.rolling(5).sum().rolling(252, min_periods=max(2,252//2)).var()
    base = v5 / (5.0 * v1).replace(0, np.nan) - 1.0
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_varratio_504d_jerk_v042_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    v1 = lr.rolling(504, min_periods=max(2,504//2)).var()
    v5 = lr.rolling(5).sum().rolling(504, min_periods=max(2,504//2)).var()
    base = v5 / (5.0 * v1).replace(0, np.nan) - 1.0
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_selfmom_42d_jerk_v043_signal(closeadj):
    m = closeadj.shift(21) / closeadj.shift(42) - 1.0
    base = _z(m, min(4*42, 1260))
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_selfmom_63d_jerk_v044_signal(closeadj):
    m = closeadj.shift(21) / closeadj.shift(63) - 1.0
    base = _z(m, min(4*63, 1260))
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_selfmom_84d_jerk_v045_signal(closeadj):
    m = closeadj.shift(21) / closeadj.shift(84) - 1.0
    base = _z(m, min(4*84, 1260))
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_selfmom_126d_jerk_v046_signal(closeadj):
    m = closeadj.shift(21) / closeadj.shift(126) - 1.0
    base = _z(m, min(4*126, 1260))
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_selfmom_252d_jerk_v047_signal(closeadj):
    m = closeadj.shift(21) / closeadj.shift(252) - 1.0
    base = _z(m, min(4*252, 1260))
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_selfmom_504d_jerk_v048_signal(closeadj):
    m = closeadj.shift(21) / closeadj.shift(504) - 1.0
    base = _z(m, min(4*504, 1260))
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_radjmom_42d_jerk_v049_signal(closeadj):
    r = closeadj / closeadj.shift(42) - 1.0
    vol = closeadj.pct_change().rolling(42, min_periods=max(2,42//2)).std()
    base = r / vol.replace(0, np.nan)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_radjmom_63d_jerk_v050_signal(closeadj):
    r = closeadj / closeadj.shift(63) - 1.0
    vol = closeadj.pct_change().rolling(63, min_periods=max(2,63//2)).std()
    base = r / vol.replace(0, np.nan)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_radjmom_84d_jerk_v051_signal(closeadj):
    r = closeadj / closeadj.shift(84) - 1.0
    vol = closeadj.pct_change().rolling(84, min_periods=max(2,84//2)).std()
    base = r / vol.replace(0, np.nan)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_radjmom_126d_jerk_v052_signal(closeadj):
    r = closeadj / closeadj.shift(126) - 1.0
    vol = closeadj.pct_change().rolling(126, min_periods=max(2,126//2)).std()
    base = r / vol.replace(0, np.nan)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_radjmom_252d_jerk_v053_signal(closeadj):
    r = closeadj / closeadj.shift(252) - 1.0
    vol = closeadj.pct_change().rolling(252, min_periods=max(2,252//2)).std()
    base = r / vol.replace(0, np.nan)
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_radjmom_504d_jerk_v054_signal(closeadj):
    r = closeadj / closeadj.shift(504) - 1.0
    vol = closeadj.pct_change().rolling(504, min_periods=max(2,504//2)).std()
    base = r / vol.replace(0, np.nan)
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_rsrank_42d_jerk_v055_signal(closeadj):
    r = (closeadj / closeadj.shift(42) - 1.0)
    vol = closeadj.pct_change().rolling(42, min_periods=max(2,42//2)).std()
    ratio = r / vol.replace(0, np.nan)
    base = _rank(ratio, min(4*42, 1008))
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_rsrank_63d_jerk_v056_signal(closeadj):
    r = (closeadj / closeadj.shift(63) - 1.0)
    vol = closeadj.pct_change().rolling(63, min_periods=max(2,63//2)).std()
    ratio = r / vol.replace(0, np.nan)
    base = _rank(ratio, min(4*63, 1008))
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_rsrank_126d_jerk_v057_signal(closeadj):
    r = (closeadj / closeadj.shift(126) - 1.0)
    vol = closeadj.pct_change().rolling(126, min_periods=max(2,126//2)).std()
    ratio = r / vol.replace(0, np.nan)
    base = _rank(ratio, min(4*126, 1008))
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_rsrank_189d_jerk_v058_signal(closeadj):
    r = (closeadj / closeadj.shift(189) - 1.0)
    vol = closeadj.pct_change().rolling(189, min_periods=max(2,189//2)).std()
    ratio = r / vol.replace(0, np.nan)
    base = _rank(ratio, min(4*189, 1008))
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_rsrank_252d_jerk_v059_signal(closeadj):
    r = (closeadj / closeadj.shift(252) - 1.0)
    vol = closeadj.pct_change().rolling(252, min_periods=max(2,252//2)).std()
    ratio = r / vol.replace(0, np.nan)
    base = _rank(ratio, min(4*252, 1008))
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_rsrank_504d_jerk_v060_signal(closeadj):
    r = (closeadj / closeadj.shift(504) - 1.0)
    vol = closeadj.pct_change().rolling(504, min_periods=max(2,504//2)).std()
    ratio = r / vol.replace(0, np.nan)
    base = _rank(ratio, min(4*504, 1008))
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_volclust_42d_jerk_v061_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    av = lr.abs()
    base = av.rolling(42, min_periods=max(2,42//2)).std() / av.rolling(42, min_periods=max(2,42//2)).mean().replace(0, np.nan)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_volclust_63d_jerk_v062_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    av = lr.abs()
    base = av.rolling(63, min_periods=max(2,63//2)).std() / av.rolling(63, min_periods=max(2,63//2)).mean().replace(0, np.nan)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_volclust_105d_jerk_v063_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    av = lr.abs()
    base = av.rolling(105, min_periods=max(2,105//2)).std() / av.rolling(105, min_periods=max(2,105//2)).mean().replace(0, np.nan)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_volclust_126d_jerk_v064_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    av = lr.abs()
    base = av.rolling(126, min_periods=max(2,126//2)).std() / av.rolling(126, min_periods=max(2,126//2)).mean().replace(0, np.nan)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_volclust_189d_jerk_v065_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    av = lr.abs()
    base = av.rolling(189, min_periods=max(2,189//2)).std() / av.rolling(189, min_periods=max(2,189//2)).mean().replace(0, np.nan)
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_volclust_252d_jerk_v066_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    av = lr.abs()
    base = av.rolling(252, min_periods=max(2,252//2)).std() / av.rolling(252, min_periods=max(2,252//2)).mean().replace(0, np.nan)
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_trslope_42d_jerk_v067_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    slope = _trend_slope(lp, 42)
    vol = lp.diff().rolling(42, min_periods=max(2,42//2)).std()
    base = slope / vol.replace(0, np.nan)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_trslope_63d_jerk_v068_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    slope = _trend_slope(lp, 63)
    vol = lp.diff().rolling(63, min_periods=max(2,63//2)).std()
    base = slope / vol.replace(0, np.nan)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_trslope_84d_jerk_v069_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    slope = _trend_slope(lp, 84)
    vol = lp.diff().rolling(84, min_periods=max(2,84//2)).std()
    base = slope / vol.replace(0, np.nan)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_trslope_105d_jerk_v070_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    slope = _trend_slope(lp, 105)
    vol = lp.diff().rolling(105, min_periods=max(2,105//2)).std()
    base = slope / vol.replace(0, np.nan)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_trslope_126d_jerk_v071_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    slope = _trend_slope(lp, 126)
    vol = lp.diff().rolling(126, min_periods=max(2,126//2)).std()
    base = slope / vol.replace(0, np.nan)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_trslope_189d_jerk_v072_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    slope = _trend_slope(lp, 189)
    vol = lp.diff().rolling(189, min_periods=max(2,189//2)).std()
    base = slope / vol.replace(0, np.nan)
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_trslope_252d_jerk_v073_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    slope = _trend_slope(lp, 252)
    vol = lp.diff().rolling(252, min_periods=max(2,252//2)).std()
    base = slope / vol.replace(0, np.nan)
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_trslope_504d_jerk_v074_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    slope = _trend_slope(lp, 504)
    vol = lp.diff().rolling(504, min_periods=max(2,504//2)).std()
    base = slope / vol.replace(0, np.nan)
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_patheff_105d_jerk_v075_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    net = lp - lp.shift(105)
    path = lp.diff().abs().rolling(105, min_periods=max(2,105//2)).sum()
    base = net / path.replace(0, np.nan)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_patheff_126d_jerk_v076_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    net = lp - lp.shift(126)
    path = lp.diff().abs().rolling(126, min_periods=max(2,126//2)).sum()
    base = net / path.replace(0, np.nan)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_patheff_168d_jerk_v077_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    net = lp - lp.shift(168)
    path = lp.diff().abs().rolling(168, min_periods=max(2,168//2)).sum()
    base = net / path.replace(0, np.nan)
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_patheff_189d_jerk_v078_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    net = lp - lp.shift(189)
    path = lp.diff().abs().rolling(189, min_periods=max(2,189//2)).sum()
    base = net / path.replace(0, np.nan)
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_patheff_252d_jerk_v079_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    net = lp - lp.shift(252)
    path = lp.diff().abs().rolling(252, min_periods=max(2,252//2)).sum()
    base = net / path.replace(0, np.nan)
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_patheff_504d_jerk_v080_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    net = lp - lp.shift(504)
    path = lp.diff().abs().rolling(504, min_periods=max(2,504//2)).sum()
    base = net / path.replace(0, np.nan)
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_acf2_42d_jerk_v081_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = _autocorr(lr, 42, 2)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_acf2_63d_jerk_v082_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = _autocorr(lr, 63, 2)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_acf2_84d_jerk_v083_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = _autocorr(lr, 84, 2)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_acf2_105d_jerk_v084_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = _autocorr(lr, 105, 2)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_acf2_126d_jerk_v085_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = _autocorr(lr, 126, 2)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_acf2_189d_jerk_v086_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = _autocorr(lr, 189, 2)
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_acf2_252d_jerk_v087_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = _autocorr(lr, 252, 2)
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_vrslope_126d_jerk_v088_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    v1 = lr.rolling(126, min_periods=max(2,126//2)).var()
    v5 = lr.rolling(5).sum().rolling(126, min_periods=max(2,126//2)).var()
    v21 = lr.rolling(21).sum().rolling(126, min_periods=max(2,126//2)).var()
    y5 = np.log((v5 + 1e-12) / (v1 + 1e-12))
    y21 = np.log((v21 + 1e-12) / (v1 + 1e-12))
    base = (y21 - y5) / (np.log(21.0) - np.log(5.0)) / 2.0
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_vrslope_168d_jerk_v089_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    v1 = lr.rolling(168, min_periods=max(2,168//2)).var()
    v5 = lr.rolling(5).sum().rolling(168, min_periods=max(2,168//2)).var()
    v21 = lr.rolling(21).sum().rolling(168, min_periods=max(2,168//2)).var()
    y5 = np.log((v5 + 1e-12) / (v1 + 1e-12))
    y21 = np.log((v21 + 1e-12) / (v1 + 1e-12))
    base = (y21 - y5) / (np.log(21.0) - np.log(5.0)) / 2.0
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_vrslope_189d_jerk_v090_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    v1 = lr.rolling(189, min_periods=max(2,189//2)).var()
    v5 = lr.rolling(5).sum().rolling(189, min_periods=max(2,189//2)).var()
    v21 = lr.rolling(21).sum().rolling(189, min_periods=max(2,189//2)).var()
    y5 = np.log((v5 + 1e-12) / (v1 + 1e-12))
    y21 = np.log((v21 + 1e-12) / (v1 + 1e-12))
    base = (y21 - y5) / (np.log(21.0) - np.log(5.0)) / 2.0
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_vrslope_252d_jerk_v091_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    v1 = lr.rolling(252, min_periods=max(2,252//2)).var()
    v5 = lr.rolling(5).sum().rolling(252, min_periods=max(2,252//2)).var()
    v21 = lr.rolling(21).sum().rolling(252, min_periods=max(2,252//2)).var()
    y5 = np.log((v5 + 1e-12) / (v1 + 1e-12))
    y21 = np.log((v21 + 1e-12) / (v1 + 1e-12))
    base = (y21 - y5) / (np.log(21.0) - np.log(5.0)) / 2.0
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_vrslope_504d_jerk_v092_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    v1 = lr.rolling(504, min_periods=max(2,504//2)).var()
    v5 = lr.rolling(5).sum().rolling(504, min_periods=max(2,504//2)).var()
    v21 = lr.rolling(21).sum().rolling(504, min_periods=max(2,504//2)).var()
    y5 = np.log((v5 + 1e-12) / (v1 + 1e-12))
    y21 = np.log((v21 + 1e-12) / (v1 + 1e-12))
    base = (y21 - y5) / (np.log(21.0) - np.log(5.0)) / 2.0
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_updnasym_84d_jerk_v093_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    uv = (lr.clip(lower=0.0)**2).rolling(84, min_periods=max(2,84//2)).mean()
    dv = (lr.clip(upper=0.0)**2).rolling(84, min_periods=max(2,84//2)).mean()
    base = np.log((uv + 1e-12) / (dv + 1e-12))
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_updnasym_126d_jerk_v094_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    uv = (lr.clip(lower=0.0)**2).rolling(126, min_periods=max(2,126//2)).mean()
    dv = (lr.clip(upper=0.0)**2).rolling(126, min_periods=max(2,126//2)).mean()
    base = np.log((uv + 1e-12) / (dv + 1e-12))
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_updnasym_168d_jerk_v095_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    uv = (lr.clip(lower=0.0)**2).rolling(168, min_periods=max(2,168//2)).mean()
    dv = (lr.clip(upper=0.0)**2).rolling(168, min_periods=max(2,168//2)).mean()
    base = np.log((uv + 1e-12) / (dv + 1e-12))
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_updnasym_189d_jerk_v096_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    uv = (lr.clip(lower=0.0)**2).rolling(189, min_periods=max(2,189//2)).mean()
    dv = (lr.clip(upper=0.0)**2).rolling(189, min_periods=max(2,189//2)).mean()
    base = np.log((uv + 1e-12) / (dv + 1e-12))
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_updnasym_252d_jerk_v097_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    uv = (lr.clip(lower=0.0)**2).rolling(252, min_periods=max(2,252//2)).mean()
    dv = (lr.clip(upper=0.0)**2).rolling(252, min_periods=max(2,252//2)).mean()
    base = np.log((uv + 1e-12) / (dv + 1e-12))
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_updnasym_504d_jerk_v098_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    uv = (lr.clip(lower=0.0)**2).rolling(504, min_periods=max(2,504//2)).mean()
    dv = (lr.clip(upper=0.0)**2).rolling(504, min_periods=max(2,504//2)).mean()
    base = np.log((uv + 1e-12) / (dv + 1e-12))
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_runbal_21d_jerk_v099_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    sgn = np.sign(lr)
    wsum = (sgn * lr.abs().pow(0.5)).rolling(21, min_periods=max(2,21//2)).sum()
    sc = lr.abs().pow(0.5).rolling(21, min_periods=max(2,21//2)).sum()
    base = wsum / sc.replace(0, np.nan)
    result = base.diff(5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_runbal_42d_jerk_v100_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    sgn = np.sign(lr)
    wsum = (sgn * lr.abs().pow(0.5)).rolling(42, min_periods=max(2,42//2)).sum()
    sc = lr.abs().pow(0.5).rolling(42, min_periods=max(2,42//2)).sum()
    base = wsum / sc.replace(0, np.nan)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_runbal_63d_jerk_v101_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    sgn = np.sign(lr)
    wsum = (sgn * lr.abs().pow(0.5)).rolling(63, min_periods=max(2,63//2)).sum()
    sc = lr.abs().pow(0.5).rolling(63, min_periods=max(2,63//2)).sum()
    base = wsum / sc.replace(0, np.nan)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_runbal_105d_jerk_v102_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    sgn = np.sign(lr)
    wsum = (sgn * lr.abs().pow(0.5)).rolling(105, min_periods=max(2,105//2)).sum()
    sc = lr.abs().pow(0.5).rolling(105, min_periods=max(2,105//2)).sum()
    base = wsum / sc.replace(0, np.nan)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_runbal_126d_jerk_v103_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    sgn = np.sign(lr)
    wsum = (sgn * lr.abs().pow(0.5)).rolling(126, min_periods=max(2,126//2)).sum()
    sc = lr.abs().pow(0.5).rolling(126, min_periods=max(2,126//2)).sum()
    base = wsum / sc.replace(0, np.nan)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_upfrac_42d_jerk_v104_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    up = (lr > 0).astype(float).rolling(42, min_periods=max(2,42//2)).mean() - 0.5
    tilt = np.tanh(40.0 * lr).rolling(42, min_periods=max(2,42//2)).mean()
    base = up + 0.3 * tilt
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_upfrac_63d_jerk_v105_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    up = (lr > 0).astype(float).rolling(63, min_periods=max(2,63//2)).mean() - 0.5
    tilt = np.tanh(40.0 * lr).rolling(63, min_periods=max(2,63//2)).mean()
    base = up + 0.3 * tilt
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_upfrac_105d_jerk_v106_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    up = (lr > 0).astype(float).rolling(105, min_periods=max(2,105//2)).mean() - 0.5
    tilt = np.tanh(40.0 * lr).rolling(105, min_periods=max(2,105//2)).mean()
    base = up + 0.3 * tilt
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_upfrac_126d_jerk_v107_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    up = (lr > 0).astype(float).rolling(126, min_periods=max(2,126//2)).mean() - 0.5
    tilt = np.tanh(40.0 * lr).rolling(126, min_periods=max(2,126//2)).mean()
    base = up + 0.3 * tilt
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_upfrac_189d_jerk_v108_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    up = (lr > 0).astype(float).rolling(189, min_periods=max(2,189//2)).mean() - 0.5
    tilt = np.tanh(40.0 * lr).rolling(189, min_periods=max(2,189//2)).mean()
    base = up + 0.3 * tilt
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_upfrac_252d_jerk_v109_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    up = (lr > 0).astype(float).rolling(252, min_periods=max(2,252//2)).mean() - 0.5
    tilt = np.tanh(40.0 * lr).rolling(252, min_periods=max(2,252//2)).mean()
    base = up + 0.3 * tilt
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_skew_63d_jerk_v110_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = lr.rolling(63, min_periods=max(2,63//2)).skew()
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_skew_105d_jerk_v111_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = lr.rolling(105, min_periods=max(2,105//2)).skew()
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_skew_126d_jerk_v112_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = lr.rolling(126, min_periods=max(2,126//2)).skew()
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_skew_189d_jerk_v113_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = lr.rolling(189, min_periods=max(2,189//2)).skew()
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_skew_252d_jerk_v114_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = lr.rolling(252, min_periods=max(2,252//2)).skew()
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_madist_42d_jerk_v115_signal(closeadj):
    ma = _mean(closeadj, 42)
    dist = closeadj / ma.replace(0, np.nan) - 1.0
    vol = closeadj.pct_change().rolling(max(21,42//2), min_periods=11).std()
    base = dist / vol.replace(0, np.nan)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_madist_126d_jerk_v116_signal(closeadj):
    ma = _mean(closeadj, 126)
    dist = closeadj / ma.replace(0, np.nan) - 1.0
    vol = closeadj.pct_change().rolling(max(21,126//2), min_periods=11).std()
    base = dist / vol.replace(0, np.nan)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_madist_378d_jerk_v117_signal(closeadj):
    ma = _mean(closeadj, 378)
    dist = closeadj / ma.replace(0, np.nan) - 1.0
    vol = closeadj.pct_change().rolling(max(21,378//2), min_periods=11).std()
    base = dist / vol.replace(0, np.nan)
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_calmar_126d_jerk_v118_signal(closeadj):
    ret = closeadj / closeadj.shift(126) - 1.0
    peak = closeadj.rolling(126, min_periods=max(2,126//2)).max()
    dd = (closeadj / peak.replace(0, np.nan) - 1.0).rolling(126, min_periods=max(2,126//2)).min().abs()
    base = ret / dd.replace(0, np.nan)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_calmar_168d_jerk_v119_signal(closeadj):
    ret = closeadj / closeadj.shift(168) - 1.0
    peak = closeadj.rolling(168, min_periods=max(2,168//2)).max()
    dd = (closeadj / peak.replace(0, np.nan) - 1.0).rolling(168, min_periods=max(2,168//2)).min().abs()
    base = ret / dd.replace(0, np.nan)
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_calmar_189d_jerk_v120_signal(closeadj):
    ret = closeadj / closeadj.shift(189) - 1.0
    peak = closeadj.rolling(189, min_periods=max(2,189//2)).max()
    dd = (closeadj / peak.replace(0, np.nan) - 1.0).rolling(189, min_periods=max(2,189//2)).min().abs()
    base = ret / dd.replace(0, np.nan)
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_calmar_252d_jerk_v121_signal(closeadj):
    ret = closeadj / closeadj.shift(252) - 1.0
    peak = closeadj.rolling(252, min_periods=max(2,252//2)).max()
    dd = (closeadj / peak.replace(0, np.nan) - 1.0).rolling(252, min_periods=max(2,252//2)).min().abs()
    base = ret / dd.replace(0, np.nan)
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_calmar_504d_jerk_v122_signal(closeadj):
    ret = closeadj / closeadj.shift(504) - 1.0
    peak = closeadj.rolling(504, min_periods=max(2,504//2)).max()
    dd = (closeadj / peak.replace(0, np.nan) - 1.0).rolling(504, min_periods=max(2,504//2)).min().abs()
    base = ret / dd.replace(0, np.nan)
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_tau_63d_jerk_v123_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    def _tau(a):
        if np.isnan(a).any():
            return np.nan
        mm = len(a)
        rk = np.argsort(np.argsort(a)).astype(float)
        t = np.arange(mm, dtype=float)
        rkc = rk - rk.mean(); tc = t - t.mean()
        dn = np.sqrt((rkc**2).sum() * (tc**2).sum())
        if dn <= 0:
            return np.nan
        return float(np.dot(rkc, tc) / dn)
    base = lp.rolling(63, min_periods=max(8,63//2)).apply(_tau, raw=True)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_tau_84d_jerk_v124_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    def _tau(a):
        if np.isnan(a).any():
            return np.nan
        mm = len(a)
        rk = np.argsort(np.argsort(a)).astype(float)
        t = np.arange(mm, dtype=float)
        rkc = rk - rk.mean(); tc = t - t.mean()
        dn = np.sqrt((rkc**2).sum() * (tc**2).sum())
        if dn <= 0:
            return np.nan
        return float(np.dot(rkc, tc) / dn)
    base = lp.rolling(84, min_periods=max(8,84//2)).apply(_tau, raw=True)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_tau_105d_jerk_v125_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    def _tau(a):
        if np.isnan(a).any():
            return np.nan
        mm = len(a)
        rk = np.argsort(np.argsort(a)).astype(float)
        t = np.arange(mm, dtype=float)
        rkc = rk - rk.mean(); tc = t - t.mean()
        dn = np.sqrt((rkc**2).sum() * (tc**2).sum())
        if dn <= 0:
            return np.nan
        return float(np.dot(rkc, tc) / dn)
    base = lp.rolling(105, min_periods=max(8,105//2)).apply(_tau, raw=True)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_tau_126d_jerk_v126_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    def _tau(a):
        if np.isnan(a).any():
            return np.nan
        mm = len(a)
        rk = np.argsort(np.argsort(a)).astype(float)
        t = np.arange(mm, dtype=float)
        rkc = rk - rk.mean(); tc = t - t.mean()
        dn = np.sqrt((rkc**2).sum() * (tc**2).sum())
        if dn <= 0:
            return np.nan
        return float(np.dot(rkc, tc) / dn)
    base = lp.rolling(126, min_periods=max(8,126//2)).apply(_tau, raw=True)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_tau_189d_jerk_v127_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    def _tau(a):
        if np.isnan(a).any():
            return np.nan
        mm = len(a)
        rk = np.argsort(np.argsort(a)).astype(float)
        t = np.arange(mm, dtype=float)
        rkc = rk - rk.mean(); tc = t - t.mean()
        dn = np.sqrt((rkc**2).sum() * (tc**2).sum())
        if dn <= 0:
            return np.nan
        return float(np.dot(rkc, tc) / dn)
    base = lp.rolling(189, min_periods=max(8,189//2)).apply(_tau, raw=True)
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_tau_252d_jerk_v128_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    def _tau(a):
        if np.isnan(a).any():
            return np.nan
        mm = len(a)
        rk = np.argsort(np.argsort(a)).astype(float)
        t = np.arange(mm, dtype=float)
        rkc = rk - rk.mean(); tc = t - t.mean()
        dn = np.sqrt((rkc**2).sum() * (tc**2).sum())
        if dn <= 0:
            return np.nan
        return float(np.dot(rkc, tc) / dn)
    base = lp.rolling(252, min_periods=max(8,252//2)).apply(_tau, raw=True)
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_acfabs_63d_jerk_v129_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = _autocorr(lr.abs(), 63, 1)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_acfabs_105d_jerk_v130_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = _autocorr(lr.abs(), 105, 1)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_acfabs_126d_jerk_v131_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = _autocorr(lr.abs(), 126, 1)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_acfabs_189d_jerk_v132_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = _autocorr(lr.abs(), 189, 1)
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_acfabs_252d_jerk_v133_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = _autocorr(lr.abs(), 252, 1)
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_trendshare_126d_jerk_v134_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    tv = lp.rolling(21, min_periods=10).mean().rolling(126, min_periods=max(2,126//2)).var()
    totv = lp.rolling(126, min_periods=max(2,126//2)).var()
    base = tv / totv.replace(0, np.nan)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_trendshare_168d_jerk_v135_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    tv = lp.rolling(21, min_periods=10).mean().rolling(168, min_periods=max(2,168//2)).var()
    totv = lp.rolling(168, min_periods=max(2,168//2)).var()
    base = tv / totv.replace(0, np.nan)
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_trendshare_189d_jerk_v136_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    tv = lp.rolling(21, min_periods=10).mean().rolling(189, min_periods=max(2,189//2)).var()
    totv = lp.rolling(189, min_periods=max(2,189//2)).var()
    base = tv / totv.replace(0, np.nan)
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_trendshare_252d_jerk_v137_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    tv = lp.rolling(21, min_periods=10).mean().rolling(252, min_periods=max(2,252//2)).var()
    totv = lp.rolling(252, min_periods=max(2,252//2)).var()
    base = tv / totv.replace(0, np.nan)
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_trendshare_504d_jerk_v138_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    tv = lp.rolling(21, min_periods=10).mean().rolling(504, min_periods=max(2,504//2)).var()
    totv = lp.rolling(504, min_periods=max(2,504//2)).var()
    base = tv / totv.replace(0, np.nan)
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_dnconc_126d_jerk_v139_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    chg = lp.diff(21)
    worst = chg.rolling(126, min_periods=max(2,126//2)).min()
    net = (lp - lp.shift(126)).abs()
    base = worst / net.replace(0, np.nan)
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_dnconc_168d_jerk_v140_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    chg = lp.diff(21)
    worst = chg.rolling(168, min_periods=max(2,168//2)).min()
    net = (lp - lp.shift(168)).abs()
    base = worst / net.replace(0, np.nan)
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_dnconc_189d_jerk_v141_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    chg = lp.diff(21)
    worst = chg.rolling(189, min_periods=max(2,189//2)).min()
    net = (lp - lp.shift(189)).abs()
    base = worst / net.replace(0, np.nan)
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_dnconc_252d_jerk_v142_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    chg = lp.diff(21)
    worst = chg.rolling(252, min_periods=max(2,252//2)).min()
    net = (lp - lp.shift(252)).abs()
    base = worst / net.replace(0, np.nan)
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_dnconc_504d_jerk_v143_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    chg = lp.diff(21)
    worst = chg.rolling(504, min_periods=max(2,504//2)).min()
    net = (lp - lp.shift(504)).abs()
    base = worst / net.replace(0, np.nan)
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_kurt_63d_jerk_v144_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = lr.rolling(63, min_periods=max(2,63//2)).kurt()
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_kurt_105d_jerk_v145_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = lr.rolling(105, min_periods=max(2,105//2)).kurt()
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_kurt_126d_jerk_v146_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = lr.rolling(126, min_periods=max(2,126//2)).kurt()
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_kurt_189d_jerk_v147_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = lr.rolling(189, min_periods=max(2,189//2)).kurt()
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_kurt_252d_jerk_v148_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    base = lr.rolling(252, min_periods=max(2,252//2)).kurt()
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_aboveMA_126d_jerk_v149_signal(closeadj):
    ma = _mean(closeadj, max(21, 126//2))
    above = (closeadj > ma).astype(float).rolling(126, min_periods=max(2,126//2)).mean() - 0.5
    tilt = np.tanh(3.0 * (closeadj / ma.replace(0, np.nan) - 1.0))
    base = above + 0.15 * tilt.rolling(126, min_periods=max(2,126//2)).mean()
    result = base.diff(21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)
def f08rs_f08_relative_strength_rotation_aboveMA_252d_jerk_v150_signal(closeadj):
    ma = _mean(closeadj, max(21, 252//2))
    above = (closeadj > ma).astype(float).rolling(252, min_periods=max(2,252//2)).mean() - 0.5
    tilt = np.tanh(3.0 * (closeadj / ma.replace(0, np.nan) - 1.0))
    base = above + 0.15 * tilt.rolling(252, min_periods=max(2,252//2)).mean()
    result = base.diff(63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f08rs_f08_relative_strength_rotation_effr_21d_jerk_v001_signal,
    f08rs_f08_relative_strength_rotation_effr_42d_jerk_v002_signal,
    f08rs_f08_relative_strength_rotation_effr_63d_jerk_v003_signal,
    f08rs_f08_relative_strength_rotation_effr_84d_jerk_v004_signal,
    f08rs_f08_relative_strength_rotation_effr_126d_jerk_v005_signal,
    f08rs_f08_relative_strength_rotation_effr_189d_jerk_v006_signal,
    f08rs_f08_relative_strength_rotation_effr_252d_jerk_v007_signal,
    f08rs_f08_relative_strength_rotation_effr_504d_jerk_v008_signal,
    f08rs_f08_relative_strength_rotation_effrsgn_42d_jerk_v009_signal,
    f08rs_f08_relative_strength_rotation_effrsgn_63d_jerk_v010_signal,
    f08rs_f08_relative_strength_rotation_effrsgn_84d_jerk_v011_signal,
    f08rs_f08_relative_strength_rotation_effrsgn_126d_jerk_v012_signal,
    f08rs_f08_relative_strength_rotation_effrsgn_189d_jerk_v013_signal,
    f08rs_f08_relative_strength_rotation_effrsgn_252d_jerk_v014_signal,
    f08rs_f08_relative_strength_rotation_effrsgn_504d_jerk_v015_signal,
    f08rs_f08_relative_strength_rotation_hurst_42d_jerk_v016_signal,
    f08rs_f08_relative_strength_rotation_hurst_63d_jerk_v017_signal,
    f08rs_f08_relative_strength_rotation_hurst_84d_jerk_v018_signal,
    f08rs_f08_relative_strength_rotation_hurst_105d_jerk_v019_signal,
    f08rs_f08_relative_strength_rotation_hurst_126d_jerk_v020_signal,
    f08rs_f08_relative_strength_rotation_hurst_189d_jerk_v021_signal,
    f08rs_f08_relative_strength_rotation_hurst_252d_jerk_v022_signal,
    f08rs_f08_relative_strength_rotation_hurst_504d_jerk_v023_signal,
    f08rs_f08_relative_strength_rotation_acf1_42d_jerk_v024_signal,
    f08rs_f08_relative_strength_rotation_acf1_63d_jerk_v025_signal,
    f08rs_f08_relative_strength_rotation_acf1_84d_jerk_v026_signal,
    f08rs_f08_relative_strength_rotation_acf1_105d_jerk_v027_signal,
    f08rs_f08_relative_strength_rotation_acf1_126d_jerk_v028_signal,
    f08rs_f08_relative_strength_rotation_acf1_189d_jerk_v029_signal,
    f08rs_f08_relative_strength_rotation_acf1_252d_jerk_v030_signal,
    f08rs_f08_relative_strength_rotation_acf5_84d_jerk_v031_signal,
    f08rs_f08_relative_strength_rotation_acf5_105d_jerk_v032_signal,
    f08rs_f08_relative_strength_rotation_acf5_126d_jerk_v033_signal,
    f08rs_f08_relative_strength_rotation_acf5_189d_jerk_v034_signal,
    f08rs_f08_relative_strength_rotation_acf5_252d_jerk_v035_signal,
    f08rs_f08_relative_strength_rotation_acf5_504d_jerk_v036_signal,
    f08rs_f08_relative_strength_rotation_varratio_84d_jerk_v037_signal,
    f08rs_f08_relative_strength_rotation_varratio_105d_jerk_v038_signal,
    f08rs_f08_relative_strength_rotation_varratio_126d_jerk_v039_signal,
    f08rs_f08_relative_strength_rotation_varratio_189d_jerk_v040_signal,
    f08rs_f08_relative_strength_rotation_varratio_252d_jerk_v041_signal,
    f08rs_f08_relative_strength_rotation_varratio_504d_jerk_v042_signal,
    f08rs_f08_relative_strength_rotation_selfmom_42d_jerk_v043_signal,
    f08rs_f08_relative_strength_rotation_selfmom_63d_jerk_v044_signal,
    f08rs_f08_relative_strength_rotation_selfmom_84d_jerk_v045_signal,
    f08rs_f08_relative_strength_rotation_selfmom_126d_jerk_v046_signal,
    f08rs_f08_relative_strength_rotation_selfmom_252d_jerk_v047_signal,
    f08rs_f08_relative_strength_rotation_selfmom_504d_jerk_v048_signal,
    f08rs_f08_relative_strength_rotation_radjmom_42d_jerk_v049_signal,
    f08rs_f08_relative_strength_rotation_radjmom_63d_jerk_v050_signal,
    f08rs_f08_relative_strength_rotation_radjmom_84d_jerk_v051_signal,
    f08rs_f08_relative_strength_rotation_radjmom_126d_jerk_v052_signal,
    f08rs_f08_relative_strength_rotation_radjmom_252d_jerk_v053_signal,
    f08rs_f08_relative_strength_rotation_radjmom_504d_jerk_v054_signal,
    f08rs_f08_relative_strength_rotation_rsrank_42d_jerk_v055_signal,
    f08rs_f08_relative_strength_rotation_rsrank_63d_jerk_v056_signal,
    f08rs_f08_relative_strength_rotation_rsrank_126d_jerk_v057_signal,
    f08rs_f08_relative_strength_rotation_rsrank_189d_jerk_v058_signal,
    f08rs_f08_relative_strength_rotation_rsrank_252d_jerk_v059_signal,
    f08rs_f08_relative_strength_rotation_rsrank_504d_jerk_v060_signal,
    f08rs_f08_relative_strength_rotation_volclust_42d_jerk_v061_signal,
    f08rs_f08_relative_strength_rotation_volclust_63d_jerk_v062_signal,
    f08rs_f08_relative_strength_rotation_volclust_105d_jerk_v063_signal,
    f08rs_f08_relative_strength_rotation_volclust_126d_jerk_v064_signal,
    f08rs_f08_relative_strength_rotation_volclust_189d_jerk_v065_signal,
    f08rs_f08_relative_strength_rotation_volclust_252d_jerk_v066_signal,
    f08rs_f08_relative_strength_rotation_trslope_42d_jerk_v067_signal,
    f08rs_f08_relative_strength_rotation_trslope_63d_jerk_v068_signal,
    f08rs_f08_relative_strength_rotation_trslope_84d_jerk_v069_signal,
    f08rs_f08_relative_strength_rotation_trslope_105d_jerk_v070_signal,
    f08rs_f08_relative_strength_rotation_trslope_126d_jerk_v071_signal,
    f08rs_f08_relative_strength_rotation_trslope_189d_jerk_v072_signal,
    f08rs_f08_relative_strength_rotation_trslope_252d_jerk_v073_signal,
    f08rs_f08_relative_strength_rotation_trslope_504d_jerk_v074_signal,
    f08rs_f08_relative_strength_rotation_patheff_105d_jerk_v075_signal,
    f08rs_f08_relative_strength_rotation_patheff_126d_jerk_v076_signal,
    f08rs_f08_relative_strength_rotation_patheff_168d_jerk_v077_signal,
    f08rs_f08_relative_strength_rotation_patheff_189d_jerk_v078_signal,
    f08rs_f08_relative_strength_rotation_patheff_252d_jerk_v079_signal,
    f08rs_f08_relative_strength_rotation_patheff_504d_jerk_v080_signal,
    f08rs_f08_relative_strength_rotation_acf2_42d_jerk_v081_signal,
    f08rs_f08_relative_strength_rotation_acf2_63d_jerk_v082_signal,
    f08rs_f08_relative_strength_rotation_acf2_84d_jerk_v083_signal,
    f08rs_f08_relative_strength_rotation_acf2_105d_jerk_v084_signal,
    f08rs_f08_relative_strength_rotation_acf2_126d_jerk_v085_signal,
    f08rs_f08_relative_strength_rotation_acf2_189d_jerk_v086_signal,
    f08rs_f08_relative_strength_rotation_acf2_252d_jerk_v087_signal,
    f08rs_f08_relative_strength_rotation_vrslope_126d_jerk_v088_signal,
    f08rs_f08_relative_strength_rotation_vrslope_168d_jerk_v089_signal,
    f08rs_f08_relative_strength_rotation_vrslope_189d_jerk_v090_signal,
    f08rs_f08_relative_strength_rotation_vrslope_252d_jerk_v091_signal,
    f08rs_f08_relative_strength_rotation_vrslope_504d_jerk_v092_signal,
    f08rs_f08_relative_strength_rotation_updnasym_84d_jerk_v093_signal,
    f08rs_f08_relative_strength_rotation_updnasym_126d_jerk_v094_signal,
    f08rs_f08_relative_strength_rotation_updnasym_168d_jerk_v095_signal,
    f08rs_f08_relative_strength_rotation_updnasym_189d_jerk_v096_signal,
    f08rs_f08_relative_strength_rotation_updnasym_252d_jerk_v097_signal,
    f08rs_f08_relative_strength_rotation_updnasym_504d_jerk_v098_signal,
    f08rs_f08_relative_strength_rotation_runbal_21d_jerk_v099_signal,
    f08rs_f08_relative_strength_rotation_runbal_42d_jerk_v100_signal,
    f08rs_f08_relative_strength_rotation_runbal_63d_jerk_v101_signal,
    f08rs_f08_relative_strength_rotation_runbal_105d_jerk_v102_signal,
    f08rs_f08_relative_strength_rotation_runbal_126d_jerk_v103_signal,
    f08rs_f08_relative_strength_rotation_upfrac_42d_jerk_v104_signal,
    f08rs_f08_relative_strength_rotation_upfrac_63d_jerk_v105_signal,
    f08rs_f08_relative_strength_rotation_upfrac_105d_jerk_v106_signal,
    f08rs_f08_relative_strength_rotation_upfrac_126d_jerk_v107_signal,
    f08rs_f08_relative_strength_rotation_upfrac_189d_jerk_v108_signal,
    f08rs_f08_relative_strength_rotation_upfrac_252d_jerk_v109_signal,
    f08rs_f08_relative_strength_rotation_skew_63d_jerk_v110_signal,
    f08rs_f08_relative_strength_rotation_skew_105d_jerk_v111_signal,
    f08rs_f08_relative_strength_rotation_skew_126d_jerk_v112_signal,
    f08rs_f08_relative_strength_rotation_skew_189d_jerk_v113_signal,
    f08rs_f08_relative_strength_rotation_skew_252d_jerk_v114_signal,
    f08rs_f08_relative_strength_rotation_madist_42d_jerk_v115_signal,
    f08rs_f08_relative_strength_rotation_madist_126d_jerk_v116_signal,
    f08rs_f08_relative_strength_rotation_madist_378d_jerk_v117_signal,
    f08rs_f08_relative_strength_rotation_calmar_126d_jerk_v118_signal,
    f08rs_f08_relative_strength_rotation_calmar_168d_jerk_v119_signal,
    f08rs_f08_relative_strength_rotation_calmar_189d_jerk_v120_signal,
    f08rs_f08_relative_strength_rotation_calmar_252d_jerk_v121_signal,
    f08rs_f08_relative_strength_rotation_calmar_504d_jerk_v122_signal,
    f08rs_f08_relative_strength_rotation_tau_63d_jerk_v123_signal,
    f08rs_f08_relative_strength_rotation_tau_84d_jerk_v124_signal,
    f08rs_f08_relative_strength_rotation_tau_105d_jerk_v125_signal,
    f08rs_f08_relative_strength_rotation_tau_126d_jerk_v126_signal,
    f08rs_f08_relative_strength_rotation_tau_189d_jerk_v127_signal,
    f08rs_f08_relative_strength_rotation_tau_252d_jerk_v128_signal,
    f08rs_f08_relative_strength_rotation_acfabs_63d_jerk_v129_signal,
    f08rs_f08_relative_strength_rotation_acfabs_105d_jerk_v130_signal,
    f08rs_f08_relative_strength_rotation_acfabs_126d_jerk_v131_signal,
    f08rs_f08_relative_strength_rotation_acfabs_189d_jerk_v132_signal,
    f08rs_f08_relative_strength_rotation_acfabs_252d_jerk_v133_signal,
    f08rs_f08_relative_strength_rotation_trendshare_126d_jerk_v134_signal,
    f08rs_f08_relative_strength_rotation_trendshare_168d_jerk_v135_signal,
    f08rs_f08_relative_strength_rotation_trendshare_189d_jerk_v136_signal,
    f08rs_f08_relative_strength_rotation_trendshare_252d_jerk_v137_signal,
    f08rs_f08_relative_strength_rotation_trendshare_504d_jerk_v138_signal,
    f08rs_f08_relative_strength_rotation_dnconc_126d_jerk_v139_signal,
    f08rs_f08_relative_strength_rotation_dnconc_168d_jerk_v140_signal,
    f08rs_f08_relative_strength_rotation_dnconc_189d_jerk_v141_signal,
    f08rs_f08_relative_strength_rotation_dnconc_252d_jerk_v142_signal,
    f08rs_f08_relative_strength_rotation_dnconc_504d_jerk_v143_signal,
    f08rs_f08_relative_strength_rotation_kurt_63d_jerk_v144_signal,
    f08rs_f08_relative_strength_rotation_kurt_105d_jerk_v145_signal,
    f08rs_f08_relative_strength_rotation_kurt_126d_jerk_v146_signal,
    f08rs_f08_relative_strength_rotation_kurt_189d_jerk_v147_signal,
    f08rs_f08_relative_strength_rotation_kurt_252d_jerk_v148_signal,
    f08rs_f08_relative_strength_rotation_aboveMA_126d_jerk_v149_signal,
    f08rs_f08_relative_strength_rotation_aboveMA_252d_jerk_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F08_RELATIVE_STRENGTH_ROTATION_REGISTRY_3RD_001_150 = REGISTRY


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

    print("OK f08_relative_strength_rotation_3rd_derivatives_001_150_claude.py: %d features pass" % n_features)
