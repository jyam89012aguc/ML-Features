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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _jerk(base, w):
    return base.diff(w).diff(w) / base.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f09_momentum_roc(close, w):
    # rate of change (close to close) over window w
    return close.pct_change(periods=w)


def _f09_momentum_logret(close, w):
    # log return over window w
    return np.log(close / close.shift(w).replace(0, np.nan))


def _f09_momentum_riskadj(close, w, vol_w):
    # rate of change normalized by rolling stddev of returns
    r = close.pct_change(periods=w)
    s = _std(close.pct_change(), vol_w)
    return r / s.replace(0, np.nan)


# 5d jerk of 5d ROC
def f09pm_f09_price_momentum_roc_5d_jerk_v001_signal(closeadj):
    base = _f09_momentum_roc(closeadj, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d ROC
def f09pm_f09_price_momentum_roc_21d_jerk_v002_signal(closeadj):
    base = _f09_momentum_roc(closeadj, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d ROC
def f09pm_f09_price_momentum_roc_21d_jerk_v003_signal(closeadj):
    base = _f09_momentum_roc(closeadj, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d ROC
def f09pm_f09_price_momentum_roc_63d_jerk_v004_signal(closeadj):
    base = _f09_momentum_roc(closeadj, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d ROC
def f09pm_f09_price_momentum_roc_63d_jerk_v005_signal(closeadj):
    base = _f09_momentum_roc(closeadj, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 126d ROC
def f09pm_f09_price_momentum_roc_126d_jerk_v006_signal(closeadj):
    base = _f09_momentum_roc(closeadj, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 126d ROC
def f09pm_f09_price_momentum_roc_126d_jerk_v007_signal(closeadj):
    base = _f09_momentum_roc(closeadj, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d ROC
def f09pm_f09_price_momentum_roc_252d_jerk_v008_signal(closeadj):
    base = _f09_momentum_roc(closeadj, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ROC
def f09pm_f09_price_momentum_roc_252d_jerk_v009_signal(closeadj):
    base = _f09_momentum_roc(closeadj, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 252d ROC
def f09pm_f09_price_momentum_roc_252d_jerk_v010_signal(closeadj):
    base = _f09_momentum_roc(closeadj, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d ROC
def f09pm_f09_price_momentum_roc_504d_jerk_v011_signal(closeadj):
    base = _f09_momentum_roc(closeadj, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 504d ROC
def f09pm_f09_price_momentum_roc_504d_jerk_v012_signal(closeadj):
    base = _f09_momentum_roc(closeadj, 504) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 5d log ret
def f09pm_f09_price_momentum_logret_5d_jerk_v013_signal(closeadj):
    base = _f09_momentum_logret(closeadj, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d log ret
def f09pm_f09_price_momentum_logret_21d_jerk_v014_signal(closeadj):
    base = _f09_momentum_logret(closeadj, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d log ret
def f09pm_f09_price_momentum_logret_63d_jerk_v015_signal(closeadj):
    base = _f09_momentum_logret(closeadj, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d log ret
def f09pm_f09_price_momentum_logret_252d_jerk_v016_signal(closeadj):
    base = _f09_momentum_logret(closeadj, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 504d log ret
def f09pm_f09_price_momentum_logret_504d_jerk_v017_signal(closeadj):
    base = _f09_momentum_logret(closeadj, 504) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d risk-adjusted ROC
def f09pm_f09_price_momentum_riskadj_21d_jerk_v018_signal(closeadj):
    base = _f09_momentum_riskadj(closeadj, 21, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d risk-adjusted ROC
def f09pm_f09_price_momentum_riskadj_63d_jerk_v019_signal(closeadj):
    base = _f09_momentum_riskadj(closeadj, 63, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 126d risk-adjusted ROC
def f09pm_f09_price_momentum_riskadj_126d_jerk_v020_signal(closeadj):
    base = _f09_momentum_riskadj(closeadj, 126, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d risk-adjusted ROC
def f09pm_f09_price_momentum_riskadj_252d_jerk_v021_signal(closeadj):
    base = _f09_momentum_riskadj(closeadj, 252, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 504d risk-adjusted ROC
def f09pm_f09_price_momentum_riskadj_504d_jerk_v022_signal(closeadj):
    base = _f09_momentum_riskadj(closeadj, 504, 126) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d ROC z-score
def f09pm_f09_price_momentum_rocz_21d_jerk_v023_signal(closeadj):
    base = _z(_f09_momentum_roc(closeadj, 21), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d ROC z-score
def f09pm_f09_price_momentum_rocz_63d_jerk_v024_signal(closeadj):
    base = _z(_f09_momentum_roc(closeadj, 63), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ROC z-score
def f09pm_f09_price_momentum_rocz_252d_jerk_v025_signal(closeadj):
    base = _z(_f09_momentum_roc(closeadj, 252), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d ROC squared
def f09pm_f09_price_momentum_rocsq_21d_jerk_v026_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 21)
    base = r * r.abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d ROC squared
def f09pm_f09_price_momentum_rocsq_63d_jerk_v027_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 63)
    base = r * r.abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ROC squared
def f09pm_f09_price_momentum_rocsq_252d_jerk_v028_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 252)
    base = r * r.abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 5d ROC mean
def f09pm_f09_price_momentum_rocmean_5d_jerk_v029_signal(closeadj):
    base = _mean(_f09_momentum_roc(closeadj, 5), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d ROC mean
def f09pm_f09_price_momentum_rocmean_21d_jerk_v030_signal(closeadj):
    base = _mean(_f09_momentum_roc(closeadj, 21), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d ROC mean
def f09pm_f09_price_momentum_rocmean_63d_jerk_v031_signal(closeadj):
    base = _mean(_f09_momentum_roc(closeadj, 63), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ROC mean
def f09pm_f09_price_momentum_rocmean_252d_jerk_v032_signal(closeadj):
    base = _mean(_f09_momentum_roc(closeadj, 252), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d ROC std
def f09pm_f09_price_momentum_rocstd_21d_jerk_v033_signal(closeadj):
    base = _std(_f09_momentum_roc(closeadj, 21), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d ROC std
def f09pm_f09_price_momentum_rocstd_63d_jerk_v034_signal(closeadj):
    base = _std(_f09_momentum_roc(closeadj, 63), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d ROC × price
def f09pm_f09_price_momentum_rocxprice_21d_jerk_v035_signal(closeadj):
    base = _f09_momentum_roc(closeadj, 21) * closeadj * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d ROC × price
def f09pm_f09_price_momentum_rocxprice_63d_jerk_v036_signal(closeadj):
    base = _f09_momentum_roc(closeadj, 63) * closeadj * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ROC × price
def f09pm_f09_price_momentum_rocxprice_252d_jerk_v037_signal(closeadj):
    base = _f09_momentum_roc(closeadj, 252) * closeadj * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 504d ROC × price
def f09pm_f09_price_momentum_rocxprice_504d_jerk_v038_signal(closeadj):
    base = _f09_momentum_roc(closeadj, 504) * closeadj * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of (252d - 21d) momentum diff
def f09pm_f09_price_momentum_rocdiff_252m21_jerk_v039_signal(closeadj):
    a = _f09_momentum_roc(closeadj, 252)
    b = _f09_momentum_roc(closeadj, 21)
    base = (a - b) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of (63d - 21d) momentum diff
def f09pm_f09_price_momentum_rocdiff_63m21_jerk_v040_signal(closeadj):
    a = _f09_momentum_roc(closeadj, 63)
    b = _f09_momentum_roc(closeadj, 21)
    base = (a - b) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of (252d - 63d) momentum diff
def f09pm_f09_price_momentum_rocdiff_252m63_jerk_v041_signal(closeadj):
    a = _f09_momentum_roc(closeadj, 252)
    b = _f09_momentum_roc(closeadj, 63)
    base = (a - b) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of (504d - 252d) momentum diff
def f09pm_f09_price_momentum_rocdiff_504m252_jerk_v042_signal(closeadj):
    a = _f09_momentum_roc(closeadj, 504)
    b = _f09_momentum_roc(closeadj, 252)
    base = (a - b) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d ROC × volume z
def f09pm_f09_price_momentum_rocxvolz_21d_jerk_v043_signal(closeadj, volume):
    base = _f09_momentum_roc(closeadj, 21) * _z(volume, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d ROC × volume z
def f09pm_f09_price_momentum_rocxvolz_63d_jerk_v044_signal(closeadj, volume):
    base = _f09_momentum_roc(closeadj, 63) * _z(volume, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ROC × dollar volume mean
def f09pm_f09_price_momentum_rocxdv_252d_jerk_v045_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f09_momentum_roc(closeadj, 252) * _mean(dv, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 5d ROC × dollar volume
def f09pm_f09_price_momentum_rocxdv_5d_jerk_v046_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f09_momentum_roc(closeadj, 5) * dv
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d win-streak
def f09pm_f09_price_momentum_winstreak_21d_jerk_v047_signal(closeadj):
    flag = (_f09_momentum_roc(closeadj, 1) > 0).astype(float)
    grp = (flag.diff().fillna(0) != 0).cumsum()
    streak = flag.groupby(grp).cumsum() * flag
    base = streak.rolling(21, min_periods=5).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d win-streak
def f09pm_f09_price_momentum_winstreak_63d_jerk_v048_signal(closeadj):
    flag = (_f09_momentum_roc(closeadj, 1) > 0).astype(float)
    grp = (flag.diff().fillna(0) != 0).cumsum()
    streak = flag.groupby(grp).cumsum() * flag
    base = streak.rolling(63, min_periods=21).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d win-streak
def f09pm_f09_price_momentum_winstreak_252d_jerk_v049_signal(closeadj):
    flag = (_f09_momentum_roc(closeadj, 1) > 0).astype(float)
    grp = (flag.diff().fillna(0) != 0).cumsum()
    streak = flag.groupby(grp).cumsum() * flag
    base = streak.rolling(252, min_periods=63).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d loss-streak
def f09pm_f09_price_momentum_lossstreak_21d_jerk_v050_signal(closeadj):
    flag = (_f09_momentum_roc(closeadj, 1) < 0).astype(float)
    grp = (flag.diff().fillna(0) != 0).cumsum()
    streak = flag.groupby(grp).cumsum() * flag
    base = streak.rolling(21, min_periods=5).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d loss-streak
def f09pm_f09_price_momentum_lossstreak_63d_jerk_v051_signal(closeadj):
    flag = (_f09_momentum_roc(closeadj, 1) < 0).astype(float)
    grp = (flag.diff().fillna(0) != 0).cumsum()
    streak = flag.groupby(grp).cumsum() * flag
    base = streak.rolling(63, min_periods=21).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d loss-streak
def f09pm_f09_price_momentum_lossstreak_252d_jerk_v052_signal(closeadj):
    flag = (_f09_momentum_roc(closeadj, 1) < 0).astype(float)
    grp = (flag.diff().fillna(0) != 0).cumsum()
    streak = flag.groupby(grp).cumsum() * flag
    base = streak.rolling(252, min_periods=63).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d win-rate
def f09pm_f09_price_momentum_winrate_21d_jerk_v053_signal(closeadj):
    flag = (_f09_momentum_roc(closeadj, 1) > 0).astype(float)
    base = flag.rolling(21, min_periods=5).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d win-rate
def f09pm_f09_price_momentum_winrate_63d_jerk_v054_signal(closeadj):
    flag = (_f09_momentum_roc(closeadj, 1) > 0).astype(float)
    base = flag.rolling(63, min_periods=21).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d win-rate
def f09pm_f09_price_momentum_winrate_252d_jerk_v055_signal(closeadj):
    flag = (_f09_momentum_roc(closeadj, 1) > 0).astype(float)
    base = flag.rolling(252, min_periods=63).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 504d win-rate
def f09pm_f09_price_momentum_winrate_504d_jerk_v056_signal(closeadj):
    flag = (_f09_momentum_roc(closeadj, 1) > 0).astype(float)
    base = flag.rolling(504, min_periods=126).mean() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of avg up-day ret (21d)
def f09pm_f09_price_momentum_avgupret_21d_jerk_v057_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 1)
    pos = r.where(r > 0, 0.0)
    base = pos.rolling(21, min_periods=5).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of avg up-day ret (63d)
def f09pm_f09_price_momentum_avgupret_63d_jerk_v058_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 1)
    pos = r.where(r > 0, 0.0)
    base = pos.rolling(63, min_periods=21).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of avg up-day ret (252d)
def f09pm_f09_price_momentum_avgupret_252d_jerk_v059_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 1)
    pos = r.where(r > 0, 0.0)
    base = pos.rolling(252, min_periods=63).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of avg down-day ret (21d)
def f09pm_f09_price_momentum_avgdownret_21d_jerk_v060_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 1)
    neg = r.where(r < 0, 0.0)
    base = neg.rolling(21, min_periods=5).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of avg down-day ret (63d)
def f09pm_f09_price_momentum_avgdownret_63d_jerk_v061_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 1)
    neg = r.where(r < 0, 0.0)
    base = neg.rolling(63, min_periods=21).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of avg down-day ret (252d)
def f09pm_f09_price_momentum_avgdownret_252d_jerk_v062_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 1)
    neg = r.where(r < 0, 0.0)
    base = neg.rolling(252, min_periods=63).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d Sharpe
def f09pm_f09_price_momentum_sharpe_21d_jerk_v063_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 1)
    m = _mean(r, 21)
    s = _std(r, 21)
    base = (m / s.replace(0, np.nan)) * np.sqrt(252) * closeadj + _f09_momentum_roc(closeadj, 21) * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d Sharpe
def f09pm_f09_price_momentum_sharpe_63d_jerk_v064_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 1)
    m = _mean(r, 63)
    s = _std(r, 63)
    base = (m / s.replace(0, np.nan)) * np.sqrt(252) * closeadj + _f09_momentum_roc(closeadj, 63) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d Sharpe
def f09pm_f09_price_momentum_sharpe_252d_jerk_v065_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 1)
    m = _mean(r, 252)
    s = _std(r, 252)
    base = (m / s.replace(0, np.nan)) * np.sqrt(252) * closeadj + _f09_momentum_roc(closeadj, 252) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 504d Sharpe
def f09pm_f09_price_momentum_sharpe_504d_jerk_v066_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 1)
    m = _mean(r, 504)
    s = _std(r, 504)
    base = (m / s.replace(0, np.nan)) * np.sqrt(252) * closeadj + _f09_momentum_roc(closeadj, 504) * 0.0
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d ROC autocorr
def f09pm_f09_price_momentum_rocautocorr_21d_jerk_v067_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 21)
    base = r * r.shift(21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d ROC autocorr
def f09pm_f09_price_momentum_rocautocorr_63d_jerk_v068_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 63)
    base = r * r.shift(63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ROC autocorr
def f09pm_f09_price_momentum_rocautocorr_252d_jerk_v069_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 252)
    base = r * r.shift(252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of monthly 21d ROC mean
def f09pm_f09_price_momentum_monthlyroc_21d_jerk_v070_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 21)
    base = _mean(r, 5) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d ROC monthly mean
def f09pm_f09_price_momentum_monthlyroc_63d_jerk_v071_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 63)
    base = _mean(r, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ROC quarterly mean
def f09pm_f09_price_momentum_quarterlyroc_252d_jerk_v072_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 252)
    base = _mean(r, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 12m-1m momentum
def f09pm_f09_price_momentum_mom12m1m_jerk_v073_signal(closeadj):
    a = _f09_momentum_roc(closeadj, 252)
    b = _f09_momentum_roc(closeadj, 21)
    base = (a - b) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 24m-3m momentum
def f09pm_f09_price_momentum_mom24m3m_jerk_v074_signal(closeadj):
    a = _f09_momentum_roc(closeadj, 504)
    b = _f09_momentum_roc(closeadj, 63)
    base = (a - b) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d ROC × win
def f09pm_f09_price_momentum_rocxwin_21d_jerk_v075_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 21)
    flag = (_f09_momentum_roc(closeadj, 1) > 0).astype(float)
    win = flag.rolling(21, min_periods=5).mean()
    base = r * win * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ROC × win
def f09pm_f09_price_momentum_rocxwin_252d_jerk_v076_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 252)
    flag = (_f09_momentum_roc(closeadj, 1) > 0).astype(float)
    win = flag.rolling(252, min_periods=63).mean()
    base = r * win * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d max ROC
def f09pm_f09_price_momentum_rocmax_21d_jerk_v077_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 5)
    base = r.rolling(21, min_periods=5).max() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d max ROC
def f09pm_f09_price_momentum_rocmax_63d_jerk_v078_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 21)
    base = r.rolling(63, min_periods=21).max() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d min ROC
def f09pm_f09_price_momentum_rocmin_21d_jerk_v079_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 5)
    base = r.rolling(21, min_periods=5).min() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d min ROC
def f09pm_f09_price_momentum_rocmin_63d_jerk_v080_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 21)
    base = r.rolling(63, min_periods=21).min() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d ROC range
def f09pm_f09_price_momentum_rocrange_63d_jerk_v081_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 21)
    base = (r.rolling(63, min_periods=21).max() - r.rolling(63, min_periods=21).min()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d ROC × ATR
def f09pm_f09_price_momentum_rocxatr_21d_jerk_v082_signal(closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = _f09_momentum_roc(closeadj, 21) * atr * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d ROC × ATR
def f09pm_f09_price_momentum_rocxatr_63d_jerk_v083_signal(closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = _f09_momentum_roc(closeadj, 63) * atr * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ROC × ATR
def f09pm_f09_price_momentum_rocxatr_252d_jerk_v084_signal(closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    base = _f09_momentum_roc(closeadj, 252) * atr * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 5v21 ROC ratio
def f09pm_f09_price_momentum_rocratio_5v21_jerk_v085_signal(closeadj):
    a = _f09_momentum_roc(closeadj, 5)
    b = _f09_momentum_roc(closeadj, 21).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21v63 ROC ratio
def f09pm_f09_price_momentum_rocratio_21v63_jerk_v086_signal(closeadj):
    a = _f09_momentum_roc(closeadj, 21)
    b = _f09_momentum_roc(closeadj, 63).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63v252 ROC ratio
def f09pm_f09_price_momentum_rocratio_63v252_jerk_v087_signal(closeadj):
    a = _f09_momentum_roc(closeadj, 63)
    b = _f09_momentum_roc(closeadj, 252).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 252v504 ROC ratio
def f09pm_f09_price_momentum_rocratio_252v504_jerk_v088_signal(closeadj):
    a = _f09_momentum_roc(closeadj, 252)
    b = _f09_momentum_roc(closeadj, 504).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d ROC × log ret
def f09pm_f09_price_momentum_rocxlog_21d_jerk_v089_signal(closeadj):
    base = _f09_momentum_roc(closeadj, 21) * _f09_momentum_logret(closeadj, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d ROC × log ret
def f09pm_f09_price_momentum_rocxlog_63d_jerk_v090_signal(closeadj):
    base = _f09_momentum_roc(closeadj, 63) * _f09_momentum_logret(closeadj, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ROC × log ret
def f09pm_f09_price_momentum_rocxlog_252d_jerk_v091_signal(closeadj):
    base = _f09_momentum_roc(closeadj, 252) * _f09_momentum_logret(closeadj, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d ROC × skew
def f09pm_f09_price_momentum_rocxskew_63d_jerk_v092_signal(closeadj):
    sk = closeadj.pct_change().rolling(63, min_periods=21).skew()
    base = _f09_momentum_roc(closeadj, 63) * sk * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ROC × skew
def f09pm_f09_price_momentum_rocxskew_252d_jerk_v093_signal(closeadj):
    sk = closeadj.pct_change().rolling(252, min_periods=63).skew()
    base = _f09_momentum_roc(closeadj, 252) * sk * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d ROC × kurt
def f09pm_f09_price_momentum_rocxkurt_63d_jerk_v094_signal(closeadj):
    kt = closeadj.pct_change().rolling(63, min_periods=21).kurt()
    base = _f09_momentum_roc(closeadj, 63) * kt * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ROC × kurt
def f09pm_f09_price_momentum_rocxkurt_252d_jerk_v095_signal(closeadj):
    kt = closeadj.pct_change().rolling(252, min_periods=63).kurt()
    base = _f09_momentum_roc(closeadj, 252) * kt * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d ROC × ret mean
def f09pm_f09_price_momentum_rocxretmean_21d_jerk_v096_signal(closeadj):
    rmean = _mean(closeadj.pct_change(), 21)
    base = _f09_momentum_roc(closeadj, 21) * rmean * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d ROC × ret mean
def f09pm_f09_price_momentum_rocxretmean_63d_jerk_v097_signal(closeadj):
    rmean = _mean(closeadj.pct_change(), 63)
    base = _f09_momentum_roc(closeadj, 63) * rmean * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ROC × ret mean
def f09pm_f09_price_momentum_rocxretmean_252d_jerk_v098_signal(closeadj):
    rmean = _mean(closeadj.pct_change(), 252)
    base = _f09_momentum_roc(closeadj, 252) * rmean * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d ROC × retvol
def f09pm_f09_price_momentum_rocxretvol_21d_jerk_v099_signal(closeadj):
    rv = _std(closeadj.pct_change(), 21)
    base = _f09_momentum_roc(closeadj, 21) * rv * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d ROC × retvol
def f09pm_f09_price_momentum_rocxretvol_63d_jerk_v100_signal(closeadj):
    rv = _std(closeadj.pct_change(), 63)
    base = _f09_momentum_roc(closeadj, 63) * rv * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ROC × retvol
def f09pm_f09_price_momentum_rocxretvol_252d_jerk_v101_signal(closeadj):
    rv = _std(closeadj.pct_change(), 63)
    base = _f09_momentum_roc(closeadj, 252) * rv * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d ROC pct rank
def f09pm_f09_price_momentum_rocpct_252d_jerk_v102_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 21)
    base = r.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d ROC pct rank
def f09pm_f09_price_momentum_rocpct_504d_jerk_v103_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 63)
    base = r.rolling(504, min_periods=126).rank(pct=True) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ROC pct rank
def f09pm_f09_price_momentum_rocpct_252v504_jerk_v104_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 252)
    base = r.rolling(504, min_periods=126).rank(pct=True) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of expanding mean ROC
def f09pm_f09_price_momentum_rocexpmean_21d_jerk_v105_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 21)
    base = r.expanding(min_periods=21).mean() * closeadj + _f09_momentum_roc(closeadj, 252) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of expanding std ROC
def f09pm_f09_price_momentum_rocexpstd_21d_jerk_v106_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 21)
    base = r.expanding(min_periods=21).std() * closeadj + _f09_momentum_roc(closeadj, 252) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d EMA-ROC
def f09pm_f09_price_momentum_emaroc_21d_jerk_v107_signal(closeadj):
    ema = closeadj.ewm(span=21, min_periods=11, adjust=False).mean()
    base = ema.pct_change(21) * closeadj + _f09_momentum_roc(closeadj, 21) * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d EMA-ROC
def f09pm_f09_price_momentum_emaroc_63d_jerk_v108_signal(closeadj):
    ema = closeadj.ewm(span=63, min_periods=32, adjust=False).mean()
    base = ema.pct_change(21) * closeadj + _f09_momentum_roc(closeadj, 63) * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d EMA-ROC
def f09pm_f09_price_momentum_emaroc_252d_jerk_v109_signal(closeadj):
    ema = closeadj.ewm(span=252, min_periods=126, adjust=False).mean()
    base = ema.pct_change(63) * closeadj + _f09_momentum_roc(closeadj, 252) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 504d EMA-ROC
def f09pm_f09_price_momentum_emaroc_504d_jerk_v110_signal(closeadj):
    ema = closeadj.ewm(span=504, min_periods=252, adjust=False).mean()
    base = ema.pct_change(126) * closeadj + _f09_momentum_roc(closeadj, 504) * 0.0
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d ROC × abs return
def f09pm_f09_price_momentum_rocxabsret_21d_jerk_v111_signal(closeadj):
    ar = closeadj.pct_change().abs()
    base = _f09_momentum_roc(closeadj, 21) * ar * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d ROC × mean abs ret
def f09pm_f09_price_momentum_rocxabsret_63d_jerk_v112_signal(closeadj):
    ar = _mean(closeadj.pct_change().abs(), 21)
    base = _f09_momentum_roc(closeadj, 63) * ar * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ROC × mean abs ret
def f09pm_f09_price_momentum_rocxabsret_252d_jerk_v113_signal(closeadj):
    ar = _mean(closeadj.pct_change().abs(), 63)
    base = _f09_momentum_roc(closeadj, 252) * ar * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d ROC × volume change
def f09pm_f09_price_momentum_rocxvolch_21d_jerk_v114_signal(closeadj, volume):
    vc = volume.pct_change(21)
    base = _f09_momentum_roc(closeadj, 21) * vc * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d ROC × volume change
def f09pm_f09_price_momentum_rocxvolch_63d_jerk_v115_signal(closeadj, volume):
    vc = volume.pct_change(63)
    base = _f09_momentum_roc(closeadj, 63) * vc * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ROC × volume change
def f09pm_f09_price_momentum_rocxvolch_252d_jerk_v116_signal(closeadj, volume):
    vc = volume.pct_change(252)
    base = _f09_momentum_roc(closeadj, 252) * vc * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d Sortino
def f09pm_f09_price_momentum_sortino_21d_jerk_v117_signal(closeadj):
    r = closeadj.pct_change()
    m = _mean(r, 21)
    neg = r.where(r < 0, 0.0)
    ds = _std(neg, 21)
    base = (m / ds.replace(0, np.nan)) * np.sqrt(252) * closeadj + _f09_momentum_roc(closeadj, 21) * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d Sortino
def f09pm_f09_price_momentum_sortino_63d_jerk_v118_signal(closeadj):
    r = closeadj.pct_change()
    m = _mean(r, 63)
    neg = r.where(r < 0, 0.0)
    ds = _std(neg, 63)
    base = (m / ds.replace(0, np.nan)) * np.sqrt(252) * closeadj + _f09_momentum_roc(closeadj, 63) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d Sortino
def f09pm_f09_price_momentum_sortino_252d_jerk_v119_signal(closeadj):
    r = closeadj.pct_change()
    m = _mean(r, 252)
    neg = r.where(r < 0, 0.0)
    ds = _std(neg, 252)
    base = (m / ds.replace(0, np.nan)) * np.sqrt(252) * closeadj + _f09_momentum_roc(closeadj, 252) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d up/down ratio
def f09pm_f09_price_momentum_updownratio_21d_jerk_v120_signal(closeadj):
    r = closeadj.pct_change()
    pos = r.where(r > 0, 0.0).rolling(21, min_periods=5).sum()
    neg = r.where(r < 0, 0.0).abs().rolling(21, min_periods=5).sum().replace(0, np.nan)
    base = (pos / neg) * closeadj + _f09_momentum_roc(closeadj, 21) * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d up/down ratio
def f09pm_f09_price_momentum_updownratio_63d_jerk_v121_signal(closeadj):
    r = closeadj.pct_change()
    pos = r.where(r > 0, 0.0).rolling(63, min_periods=21).sum()
    neg = r.where(r < 0, 0.0).abs().rolling(63, min_periods=21).sum().replace(0, np.nan)
    base = (pos / neg) * closeadj + _f09_momentum_roc(closeadj, 63) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d up/down ratio
def f09pm_f09_price_momentum_updownratio_252d_jerk_v122_signal(closeadj):
    r = closeadj.pct_change()
    pos = r.where(r > 0, 0.0).rolling(252, min_periods=63).sum()
    neg = r.where(r < 0, 0.0).abs().rolling(252, min_periods=63).sum().replace(0, np.nan)
    base = (pos / neg) * closeadj + _f09_momentum_roc(closeadj, 252) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 14d jerk of RSI 14d
def f09pm_f09_price_momentum_rsi_14d_jerk_v123_signal(closeadj):
    r = closeadj.pct_change()
    pos = r.where(r > 0, 0.0).rolling(14, min_periods=7).mean()
    neg = r.where(r < 0, 0.0).abs().rolling(14, min_periods=7).mean()
    rs = pos / neg.replace(0, np.nan)
    base = (100 - 100 / (1 + rs)) * closeadj + _f09_momentum_roc(closeadj, 14) * 0.0
    result = _jerk(base, 14)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of RSI 21d
def f09pm_f09_price_momentum_rsi_21d_jerk_v124_signal(closeadj):
    r = closeadj.pct_change()
    pos = r.where(r > 0, 0.0).rolling(21, min_periods=11).mean()
    neg = r.where(r < 0, 0.0).abs().rolling(21, min_periods=11).mean()
    rs = pos / neg.replace(0, np.nan)
    base = (100 - 100 / (1 + rs)) * closeadj + _f09_momentum_roc(closeadj, 21) * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of RSI 63d
def f09pm_f09_price_momentum_rsi_63d_jerk_v125_signal(closeadj):
    r = closeadj.pct_change()
    pos = r.where(r > 0, 0.0).rolling(63, min_periods=21).mean()
    neg = r.where(r < 0, 0.0).abs().rolling(63, min_periods=21).mean()
    rs = pos / neg.replace(0, np.nan)
    base = (100 - 100 / (1 + rs)) * closeadj + _f09_momentum_roc(closeadj, 63) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d ROC sum (63d)
def f09pm_f09_price_momentum_rocsum_63d_jerk_v126_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 21)
    base = r.rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d ROC sum (252d)
def f09pm_f09_price_momentum_rocsum_252d_jerk_v127_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 63)
    base = r.rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 252d ROC sum (504d)
def f09pm_f09_price_momentum_rocsum_504d_jerk_v128_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 252)
    base = r.rolling(504, min_periods=126).sum() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d ROC × ATR ratio
def f09pm_f09_price_momentum_rocxatrratio_21d_jerk_v129_signal(closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean() / closeadj.replace(0, np.nan)
    base = _f09_momentum_roc(closeadj, 21) * atr * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ROC × ATR ratio
def f09pm_f09_price_momentum_rocxatrratio_252d_jerk_v130_signal(closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean() / closeadj.replace(0, np.nan)
    base = _f09_momentum_roc(closeadj, 252) * atr * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d ROC × short return
def f09pm_f09_price_momentum_rocxshort_21d_jerk_v131_signal(closeadj):
    r5 = closeadj.pct_change(5)
    base = _f09_momentum_roc(closeadj, 21) * r5 * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63 × 21 ROC product
def f09pm_f09_price_momentum_rocprod_63x21_jerk_v132_signal(closeadj):
    a = _f09_momentum_roc(closeadj, 63)
    b = _f09_momentum_roc(closeadj, 21)
    base = a * b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252 × 63 ROC product
def f09pm_f09_price_momentum_rocprod_252x63_jerk_v133_signal(closeadj):
    a = _f09_momentum_roc(closeadj, 252)
    b = _f09_momentum_roc(closeadj, 63)
    base = a * b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 504 × 252 ROC product
def f09pm_f09_price_momentum_rocprod_504x252_jerk_v134_signal(closeadj):
    a = _f09_momentum_roc(closeadj, 504)
    b = _f09_momentum_roc(closeadj, 252)
    base = a * b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d ROC × volume mean
def f09pm_f09_price_momentum_rocxvolmean_21d_jerk_v135_signal(closeadj, volume):
    vm = _mean(volume, 21)
    base = _f09_momentum_roc(closeadj, 21) * vm * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d ROC × volume mean
def f09pm_f09_price_momentum_rocxvolmean_63d_jerk_v136_signal(closeadj, volume):
    vm = _mean(volume, 63)
    base = _f09_momentum_roc(closeadj, 63) * vm * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ROC × volume mean
def f09pm_f09_price_momentum_rocxvolmean_252d_jerk_v137_signal(closeadj, volume):
    vm = _mean(volume, 252)
    base = _f09_momentum_roc(closeadj, 252) * vm * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d signed ROC
def f09pm_f09_price_momentum_signedroc_21d_jerk_v138_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 21)
    base = np.sign(r) * r.abs() * closeadj * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d signed ROC
def f09pm_f09_price_momentum_signedroc_63d_jerk_v139_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 63)
    base = np.sign(r) * r.abs() * closeadj * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d signed ROC
def f09pm_f09_price_momentum_signedroc_252d_jerk_v140_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 252)
    base = np.sign(r) * r.abs() * closeadj * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d ROC z × volume z
def f09pm_f09_price_momentum_rocz_volz_21d_jerk_v141_signal(closeadj, volume):
    rz = _z(_f09_momentum_roc(closeadj, 21), 63)
    vz = _z(volume, 21)
    base = rz * vz * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d ROC z × volume z
def f09pm_f09_price_momentum_rocz_volz_63d_jerk_v142_signal(closeadj, volume):
    rz = _z(_f09_momentum_roc(closeadj, 63), 252)
    vz = _z(volume, 63)
    base = rz * vz * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ROC z × dollar volume mean
def f09pm_f09_price_momentum_rocz_dv_252d_jerk_v143_signal(closeadj, volume):
    dv = closeadj * volume
    rz = _z(_f09_momentum_roc(closeadj, 252), 504)
    base = rz * _mean(dv, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d ROC × intraday range
def f09pm_f09_price_momentum_rocxrange_21d_jerk_v144_signal(closeadj, high, low):
    rng = (high - low)
    base = _f09_momentum_roc(closeadj, 21) * rng * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d ROC × range mean
def f09pm_f09_price_momentum_rocxrange_63d_jerk_v145_signal(closeadj, high, low):
    rng = _mean((high - low), 21)
    base = _f09_momentum_roc(closeadj, 63) * rng * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ROC × range mean
def f09pm_f09_price_momentum_rocxrange_252d_jerk_v146_signal(closeadj, high, low):
    rng = _mean((high - low), 63)
    base = _f09_momentum_roc(closeadj, 252) * rng * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d ROC × overnight gap
def f09pm_f09_price_momentum_rocxocgap_21d_jerk_v147_signal(closeadj, open, close):
    gap = (open - close.shift(1)) / close.shift(1).abs().replace(0, np.nan)
    base = _f09_momentum_roc(closeadj, 21) * gap * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d ROC × gap z-score
def f09pm_f09_price_momentum_rocxocgapz_63d_jerk_v148_signal(closeadj, open, close):
    gap = (open - close.shift(1)) / close.shift(1).abs().replace(0, np.nan)
    base = _f09_momentum_roc(closeadj, 63) * _z(gap, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ROC × gap mean
def f09pm_f09_price_momentum_rocxocgapmean_252d_jerk_v149_signal(closeadj, open, close):
    gap = (open - close.shift(1)) / close.shift(1).abs().replace(0, np.nan)
    base = _f09_momentum_roc(closeadj, 252) * _mean(gap, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of composite long-term momentum
def f09pm_f09_price_momentum_composite_long_jerk_v150_signal(closeadj):
    a = _f09_momentum_roc(closeadj, 252)
    b = _f09_momentum_roc(closeadj, 504)
    base = (a + b) * closeadj * closeadj * 0.5
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f09pm_f09_price_momentum_roc_5d_jerk_v001_signal,
    f09pm_f09_price_momentum_roc_21d_jerk_v002_signal,
    f09pm_f09_price_momentum_roc_21d_jerk_v003_signal,
    f09pm_f09_price_momentum_roc_63d_jerk_v004_signal,
    f09pm_f09_price_momentum_roc_63d_jerk_v005_signal,
    f09pm_f09_price_momentum_roc_126d_jerk_v006_signal,
    f09pm_f09_price_momentum_roc_126d_jerk_v007_signal,
    f09pm_f09_price_momentum_roc_252d_jerk_v008_signal,
    f09pm_f09_price_momentum_roc_252d_jerk_v009_signal,
    f09pm_f09_price_momentum_roc_252d_jerk_v010_signal,
    f09pm_f09_price_momentum_roc_504d_jerk_v011_signal,
    f09pm_f09_price_momentum_roc_504d_jerk_v012_signal,
    f09pm_f09_price_momentum_logret_5d_jerk_v013_signal,
    f09pm_f09_price_momentum_logret_21d_jerk_v014_signal,
    f09pm_f09_price_momentum_logret_63d_jerk_v015_signal,
    f09pm_f09_price_momentum_logret_252d_jerk_v016_signal,
    f09pm_f09_price_momentum_logret_504d_jerk_v017_signal,
    f09pm_f09_price_momentum_riskadj_21d_jerk_v018_signal,
    f09pm_f09_price_momentum_riskadj_63d_jerk_v019_signal,
    f09pm_f09_price_momentum_riskadj_126d_jerk_v020_signal,
    f09pm_f09_price_momentum_riskadj_252d_jerk_v021_signal,
    f09pm_f09_price_momentum_riskadj_504d_jerk_v022_signal,
    f09pm_f09_price_momentum_rocz_21d_jerk_v023_signal,
    f09pm_f09_price_momentum_rocz_63d_jerk_v024_signal,
    f09pm_f09_price_momentum_rocz_252d_jerk_v025_signal,
    f09pm_f09_price_momentum_rocsq_21d_jerk_v026_signal,
    f09pm_f09_price_momentum_rocsq_63d_jerk_v027_signal,
    f09pm_f09_price_momentum_rocsq_252d_jerk_v028_signal,
    f09pm_f09_price_momentum_rocmean_5d_jerk_v029_signal,
    f09pm_f09_price_momentum_rocmean_21d_jerk_v030_signal,
    f09pm_f09_price_momentum_rocmean_63d_jerk_v031_signal,
    f09pm_f09_price_momentum_rocmean_252d_jerk_v032_signal,
    f09pm_f09_price_momentum_rocstd_21d_jerk_v033_signal,
    f09pm_f09_price_momentum_rocstd_63d_jerk_v034_signal,
    f09pm_f09_price_momentum_rocxprice_21d_jerk_v035_signal,
    f09pm_f09_price_momentum_rocxprice_63d_jerk_v036_signal,
    f09pm_f09_price_momentum_rocxprice_252d_jerk_v037_signal,
    f09pm_f09_price_momentum_rocxprice_504d_jerk_v038_signal,
    f09pm_f09_price_momentum_rocdiff_252m21_jerk_v039_signal,
    f09pm_f09_price_momentum_rocdiff_63m21_jerk_v040_signal,
    f09pm_f09_price_momentum_rocdiff_252m63_jerk_v041_signal,
    f09pm_f09_price_momentum_rocdiff_504m252_jerk_v042_signal,
    f09pm_f09_price_momentum_rocxvolz_21d_jerk_v043_signal,
    f09pm_f09_price_momentum_rocxvolz_63d_jerk_v044_signal,
    f09pm_f09_price_momentum_rocxdv_252d_jerk_v045_signal,
    f09pm_f09_price_momentum_rocxdv_5d_jerk_v046_signal,
    f09pm_f09_price_momentum_winstreak_21d_jerk_v047_signal,
    f09pm_f09_price_momentum_winstreak_63d_jerk_v048_signal,
    f09pm_f09_price_momentum_winstreak_252d_jerk_v049_signal,
    f09pm_f09_price_momentum_lossstreak_21d_jerk_v050_signal,
    f09pm_f09_price_momentum_lossstreak_63d_jerk_v051_signal,
    f09pm_f09_price_momentum_lossstreak_252d_jerk_v052_signal,
    f09pm_f09_price_momentum_winrate_21d_jerk_v053_signal,
    f09pm_f09_price_momentum_winrate_63d_jerk_v054_signal,
    f09pm_f09_price_momentum_winrate_252d_jerk_v055_signal,
    f09pm_f09_price_momentum_winrate_504d_jerk_v056_signal,
    f09pm_f09_price_momentum_avgupret_21d_jerk_v057_signal,
    f09pm_f09_price_momentum_avgupret_63d_jerk_v058_signal,
    f09pm_f09_price_momentum_avgupret_252d_jerk_v059_signal,
    f09pm_f09_price_momentum_avgdownret_21d_jerk_v060_signal,
    f09pm_f09_price_momentum_avgdownret_63d_jerk_v061_signal,
    f09pm_f09_price_momentum_avgdownret_252d_jerk_v062_signal,
    f09pm_f09_price_momentum_sharpe_21d_jerk_v063_signal,
    f09pm_f09_price_momentum_sharpe_63d_jerk_v064_signal,
    f09pm_f09_price_momentum_sharpe_252d_jerk_v065_signal,
    f09pm_f09_price_momentum_sharpe_504d_jerk_v066_signal,
    f09pm_f09_price_momentum_rocautocorr_21d_jerk_v067_signal,
    f09pm_f09_price_momentum_rocautocorr_63d_jerk_v068_signal,
    f09pm_f09_price_momentum_rocautocorr_252d_jerk_v069_signal,
    f09pm_f09_price_momentum_monthlyroc_21d_jerk_v070_signal,
    f09pm_f09_price_momentum_monthlyroc_63d_jerk_v071_signal,
    f09pm_f09_price_momentum_quarterlyroc_252d_jerk_v072_signal,
    f09pm_f09_price_momentum_mom12m1m_jerk_v073_signal,
    f09pm_f09_price_momentum_mom24m3m_jerk_v074_signal,
    f09pm_f09_price_momentum_rocxwin_21d_jerk_v075_signal,
    f09pm_f09_price_momentum_rocxwin_252d_jerk_v076_signal,
    f09pm_f09_price_momentum_rocmax_21d_jerk_v077_signal,
    f09pm_f09_price_momentum_rocmax_63d_jerk_v078_signal,
    f09pm_f09_price_momentum_rocmin_21d_jerk_v079_signal,
    f09pm_f09_price_momentum_rocmin_63d_jerk_v080_signal,
    f09pm_f09_price_momentum_rocrange_63d_jerk_v081_signal,
    f09pm_f09_price_momentum_rocxatr_21d_jerk_v082_signal,
    f09pm_f09_price_momentum_rocxatr_63d_jerk_v083_signal,
    f09pm_f09_price_momentum_rocxatr_252d_jerk_v084_signal,
    f09pm_f09_price_momentum_rocratio_5v21_jerk_v085_signal,
    f09pm_f09_price_momentum_rocratio_21v63_jerk_v086_signal,
    f09pm_f09_price_momentum_rocratio_63v252_jerk_v087_signal,
    f09pm_f09_price_momentum_rocratio_252v504_jerk_v088_signal,
    f09pm_f09_price_momentum_rocxlog_21d_jerk_v089_signal,
    f09pm_f09_price_momentum_rocxlog_63d_jerk_v090_signal,
    f09pm_f09_price_momentum_rocxlog_252d_jerk_v091_signal,
    f09pm_f09_price_momentum_rocxskew_63d_jerk_v092_signal,
    f09pm_f09_price_momentum_rocxskew_252d_jerk_v093_signal,
    f09pm_f09_price_momentum_rocxkurt_63d_jerk_v094_signal,
    f09pm_f09_price_momentum_rocxkurt_252d_jerk_v095_signal,
    f09pm_f09_price_momentum_rocxretmean_21d_jerk_v096_signal,
    f09pm_f09_price_momentum_rocxretmean_63d_jerk_v097_signal,
    f09pm_f09_price_momentum_rocxretmean_252d_jerk_v098_signal,
    f09pm_f09_price_momentum_rocxretvol_21d_jerk_v099_signal,
    f09pm_f09_price_momentum_rocxretvol_63d_jerk_v100_signal,
    f09pm_f09_price_momentum_rocxretvol_252d_jerk_v101_signal,
    f09pm_f09_price_momentum_rocpct_252d_jerk_v102_signal,
    f09pm_f09_price_momentum_rocpct_504d_jerk_v103_signal,
    f09pm_f09_price_momentum_rocpct_252v504_jerk_v104_signal,
    f09pm_f09_price_momentum_rocexpmean_21d_jerk_v105_signal,
    f09pm_f09_price_momentum_rocexpstd_21d_jerk_v106_signal,
    f09pm_f09_price_momentum_emaroc_21d_jerk_v107_signal,
    f09pm_f09_price_momentum_emaroc_63d_jerk_v108_signal,
    f09pm_f09_price_momentum_emaroc_252d_jerk_v109_signal,
    f09pm_f09_price_momentum_emaroc_504d_jerk_v110_signal,
    f09pm_f09_price_momentum_rocxabsret_21d_jerk_v111_signal,
    f09pm_f09_price_momentum_rocxabsret_63d_jerk_v112_signal,
    f09pm_f09_price_momentum_rocxabsret_252d_jerk_v113_signal,
    f09pm_f09_price_momentum_rocxvolch_21d_jerk_v114_signal,
    f09pm_f09_price_momentum_rocxvolch_63d_jerk_v115_signal,
    f09pm_f09_price_momentum_rocxvolch_252d_jerk_v116_signal,
    f09pm_f09_price_momentum_sortino_21d_jerk_v117_signal,
    f09pm_f09_price_momentum_sortino_63d_jerk_v118_signal,
    f09pm_f09_price_momentum_sortino_252d_jerk_v119_signal,
    f09pm_f09_price_momentum_updownratio_21d_jerk_v120_signal,
    f09pm_f09_price_momentum_updownratio_63d_jerk_v121_signal,
    f09pm_f09_price_momentum_updownratio_252d_jerk_v122_signal,
    f09pm_f09_price_momentum_rsi_14d_jerk_v123_signal,
    f09pm_f09_price_momentum_rsi_21d_jerk_v124_signal,
    f09pm_f09_price_momentum_rsi_63d_jerk_v125_signal,
    f09pm_f09_price_momentum_rocsum_63d_jerk_v126_signal,
    f09pm_f09_price_momentum_rocsum_252d_jerk_v127_signal,
    f09pm_f09_price_momentum_rocsum_504d_jerk_v128_signal,
    f09pm_f09_price_momentum_rocxatrratio_21d_jerk_v129_signal,
    f09pm_f09_price_momentum_rocxatrratio_252d_jerk_v130_signal,
    f09pm_f09_price_momentum_rocxshort_21d_jerk_v131_signal,
    f09pm_f09_price_momentum_rocprod_63x21_jerk_v132_signal,
    f09pm_f09_price_momentum_rocprod_252x63_jerk_v133_signal,
    f09pm_f09_price_momentum_rocprod_504x252_jerk_v134_signal,
    f09pm_f09_price_momentum_rocxvolmean_21d_jerk_v135_signal,
    f09pm_f09_price_momentum_rocxvolmean_63d_jerk_v136_signal,
    f09pm_f09_price_momentum_rocxvolmean_252d_jerk_v137_signal,
    f09pm_f09_price_momentum_signedroc_21d_jerk_v138_signal,
    f09pm_f09_price_momentum_signedroc_63d_jerk_v139_signal,
    f09pm_f09_price_momentum_signedroc_252d_jerk_v140_signal,
    f09pm_f09_price_momentum_rocz_volz_21d_jerk_v141_signal,
    f09pm_f09_price_momentum_rocz_volz_63d_jerk_v142_signal,
    f09pm_f09_price_momentum_rocz_dv_252d_jerk_v143_signal,
    f09pm_f09_price_momentum_rocxrange_21d_jerk_v144_signal,
    f09pm_f09_price_momentum_rocxrange_63d_jerk_v145_signal,
    f09pm_f09_price_momentum_rocxrange_252d_jerk_v146_signal,
    f09pm_f09_price_momentum_rocxocgap_21d_jerk_v147_signal,
    f09pm_f09_price_momentum_rocxocgapz_63d_jerk_v148_signal,
    f09pm_f09_price_momentum_rocxocgapmean_252d_jerk_v149_signal,
    f09pm_f09_price_momentum_composite_long_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F09_PRICE_MOMENTUM_REGISTRY_JERK = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    open_ = closeadj * (1.0 + np.random.normal(0, 0.005, n))
    open_ = pd.Series(open_, name="open")
    close = closeadj.copy()
    close.name = "close"
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    cols = {"closeadj": closeadj, "open": open_, "close": close, "high": high, "low": low, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f09_momentum_roc", "_f09_momentum_logret", "_f09_momentum_riskadj")
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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f09_price_momentum_3rd_derivatives_001_150_claude: {n_features} features pass")
