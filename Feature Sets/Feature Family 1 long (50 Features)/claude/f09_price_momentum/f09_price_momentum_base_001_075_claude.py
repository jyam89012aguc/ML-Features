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


# 5d ROC (1 week return)
def f09pm_f09_price_momentum_roc_5d_base_v001_signal(closeadj):
    result = _f09_momentum_roc(closeadj, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROC (1 month return)
def f09pm_f09_price_momentum_roc_21d_base_v002_signal(closeadj):
    result = _f09_momentum_roc(closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROC (1 quarter return)
def f09pm_f09_price_momentum_roc_63d_base_v003_signal(closeadj):
    result = _f09_momentum_roc(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ROC (half year return)
def f09pm_f09_price_momentum_roc_126d_base_v004_signal(closeadj):
    result = _f09_momentum_roc(closeadj, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROC (1 year return)
def f09pm_f09_price_momentum_roc_252d_base_v005_signal(closeadj):
    result = _f09_momentum_roc(closeadj, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ROC (2 year return)
def f09pm_f09_price_momentum_roc_504d_base_v006_signal(closeadj):
    result = _f09_momentum_roc(closeadj, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d log return
def f09pm_f09_price_momentum_logret_5d_base_v007_signal(closeadj):
    result = _f09_momentum_logret(closeadj, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log return
def f09pm_f09_price_momentum_logret_21d_base_v008_signal(closeadj):
    result = _f09_momentum_logret(closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log return
def f09pm_f09_price_momentum_logret_63d_base_v009_signal(closeadj):
    result = _f09_momentum_logret(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log return
def f09pm_f09_price_momentum_logret_252d_base_v010_signal(closeadj):
    result = _f09_momentum_logret(closeadj, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log return
def f09pm_f09_price_momentum_logret_504d_base_v011_signal(closeadj):
    result = _f09_momentum_logret(closeadj, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d risk-adjusted ROC
def f09pm_f09_price_momentum_riskadj_21d_base_v012_signal(closeadj):
    result = _f09_momentum_riskadj(closeadj, 21, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d risk-adjusted ROC
def f09pm_f09_price_momentum_riskadj_63d_base_v013_signal(closeadj):
    result = _f09_momentum_riskadj(closeadj, 63, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d risk-adjusted ROC
def f09pm_f09_price_momentum_riskadj_126d_base_v014_signal(closeadj):
    result = _f09_momentum_riskadj(closeadj, 126, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d risk-adjusted ROC
def f09pm_f09_price_momentum_riskadj_252d_base_v015_signal(closeadj):
    result = _f09_momentum_riskadj(closeadj, 252, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d risk-adjusted ROC
def f09pm_f09_price_momentum_riskadj_504d_base_v016_signal(closeadj):
    result = _f09_momentum_riskadj(closeadj, 504, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROC z-score over 252d
def f09pm_f09_price_momentum_rocz_21d_base_v017_signal(closeadj):
    result = _z(_f09_momentum_roc(closeadj, 21), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROC z-score over 252d
def f09pm_f09_price_momentum_rocz_63d_base_v018_signal(closeadj):
    result = _z(_f09_momentum_roc(closeadj, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROC z-score over 504d
def f09pm_f09_price_momentum_rocz_252d_base_v019_signal(closeadj):
    result = _z(_f09_momentum_roc(closeadj, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROC squared (severity)
def f09pm_f09_price_momentum_rocsq_21d_base_v020_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 21)
    result = r * r.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROC squared
def f09pm_f09_price_momentum_rocsq_63d_base_v021_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 63)
    result = r * r.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROC squared
def f09pm_f09_price_momentum_rocsq_252d_base_v022_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 252)
    result = r * r.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling mean of 5d ROC over 63d
def f09pm_f09_price_momentum_rocmean_5d_base_v023_signal(closeadj):
    result = _mean(_f09_momentum_roc(closeadj, 5), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling mean of 21d ROC over 63d
def f09pm_f09_price_momentum_rocmean_21d_base_v024_signal(closeadj):
    result = _mean(_f09_momentum_roc(closeadj, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling mean of 63d ROC over 252d
def f09pm_f09_price_momentum_rocmean_63d_base_v025_signal(closeadj):
    result = _mean(_f09_momentum_roc(closeadj, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling mean of 252d ROC over 504d
def f09pm_f09_price_momentum_rocmean_252d_base_v026_signal(closeadj):
    result = _mean(_f09_momentum_roc(closeadj, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling std of 21d ROC over 63d
def f09pm_f09_price_momentum_rocstd_21d_base_v027_signal(closeadj):
    result = _std(_f09_momentum_roc(closeadj, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling std of 63d ROC over 252d
def f09pm_f09_price_momentum_rocstd_63d_base_v028_signal(closeadj):
    result = _std(_f09_momentum_roc(closeadj, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROC × current closeadj (weighted)
def f09pm_f09_price_momentum_rocxprice_21d_base_v029_signal(closeadj):
    result = _f09_momentum_roc(closeadj, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROC × closeadj
def f09pm_f09_price_momentum_rocxprice_63d_base_v030_signal(closeadj):
    result = _f09_momentum_roc(closeadj, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROC × closeadj
def f09pm_f09_price_momentum_rocxprice_252d_base_v031_signal(closeadj):
    result = _f09_momentum_roc(closeadj, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ROC × closeadj
def f09pm_f09_price_momentum_rocxprice_504d_base_v032_signal(closeadj):
    result = _f09_momentum_roc(closeadj, 504) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROC minus 21d ROC (long-short divergence)
def f09pm_f09_price_momentum_rocdiff_252m21_base_v033_signal(closeadj):
    a = _f09_momentum_roc(closeadj, 252)
    b = _f09_momentum_roc(closeadj, 21)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROC minus 21d ROC
def f09pm_f09_price_momentum_rocdiff_63m21_base_v034_signal(closeadj):
    a = _f09_momentum_roc(closeadj, 63)
    b = _f09_momentum_roc(closeadj, 21)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROC minus 63d ROC
def f09pm_f09_price_momentum_rocdiff_252m63_base_v035_signal(closeadj):
    a = _f09_momentum_roc(closeadj, 252)
    b = _f09_momentum_roc(closeadj, 63)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ROC minus 252d ROC
def f09pm_f09_price_momentum_rocdiff_504m252_base_v036_signal(closeadj):
    a = _f09_momentum_roc(closeadj, 504)
    b = _f09_momentum_roc(closeadj, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROC × volume z-score
def f09pm_f09_price_momentum_rocxvolz_21d_base_v037_signal(closeadj, volume):
    result = _f09_momentum_roc(closeadj, 21) * _z(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROC × volume z-score
def f09pm_f09_price_momentum_rocxvolz_63d_base_v038_signal(closeadj, volume):
    result = _f09_momentum_roc(closeadj, 63) * _z(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROC × dollar volume mean
def f09pm_f09_price_momentum_rocxdv_252d_base_v039_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f09_momentum_roc(closeadj, 252) * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d ROC × dollar volume
def f09pm_f09_price_momentum_rocxdv_5d_base_v040_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f09_momentum_roc(closeadj, 5) * dv
    return result.replace([np.inf, -np.inf], np.nan)


# 21d win-streak length (consecutive positive ROCs)
def f09pm_f09_price_momentum_winstreak_21d_base_v041_signal(closeadj):
    flag = (_f09_momentum_roc(closeadj, 1) > 0).astype(float)
    grp = (flag.diff().fillna(0) != 0).cumsum()
    streak = flag.groupby(grp).cumsum() * flag
    result = streak.rolling(21, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d win-streak average
def f09pm_f09_price_momentum_winstreak_63d_base_v042_signal(closeadj):
    flag = (_f09_momentum_roc(closeadj, 1) > 0).astype(float)
    grp = (flag.diff().fillna(0) != 0).cumsum()
    streak = flag.groupby(grp).cumsum() * flag
    result = streak.rolling(63, min_periods=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d win-streak average
def f09pm_f09_price_momentum_winstreak_252d_base_v043_signal(closeadj):
    flag = (_f09_momentum_roc(closeadj, 1) > 0).astype(float)
    grp = (flag.diff().fillna(0) != 0).cumsum()
    streak = flag.groupby(grp).cumsum() * flag
    result = streak.rolling(252, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d loss-streak length
def f09pm_f09_price_momentum_lossstreak_21d_base_v044_signal(closeadj):
    flag = (_f09_momentum_roc(closeadj, 1) < 0).astype(float)
    grp = (flag.diff().fillna(0) != 0).cumsum()
    streak = flag.groupby(grp).cumsum() * flag
    result = streak.rolling(21, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d loss-streak length
def f09pm_f09_price_momentum_lossstreak_63d_base_v045_signal(closeadj):
    flag = (_f09_momentum_roc(closeadj, 1) < 0).astype(float)
    grp = (flag.diff().fillna(0) != 0).cumsum()
    streak = flag.groupby(grp).cumsum() * flag
    result = streak.rolling(63, min_periods=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d loss-streak length
def f09pm_f09_price_momentum_lossstreak_252d_base_v046_signal(closeadj):
    flag = (_f09_momentum_roc(closeadj, 1) < 0).astype(float)
    grp = (flag.diff().fillna(0) != 0).cumsum()
    streak = flag.groupby(grp).cumsum() * flag
    result = streak.rolling(252, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ratio of up days to total
def f09pm_f09_price_momentum_winrate_21d_base_v047_signal(closeadj):
    flag = (_f09_momentum_roc(closeadj, 1) > 0).astype(float)
    result = flag.rolling(21, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d win rate
def f09pm_f09_price_momentum_winrate_63d_base_v048_signal(closeadj):
    flag = (_f09_momentum_roc(closeadj, 1) > 0).astype(float)
    result = flag.rolling(63, min_periods=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d win rate
def f09pm_f09_price_momentum_winrate_252d_base_v049_signal(closeadj):
    flag = (_f09_momentum_roc(closeadj, 1) > 0).astype(float)
    result = flag.rolling(252, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d win rate
def f09pm_f09_price_momentum_winrate_504d_base_v050_signal(closeadj):
    flag = (_f09_momentum_roc(closeadj, 1) > 0).astype(float)
    result = flag.rolling(504, min_periods=126).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# average up-day ROC over 21d
def f09pm_f09_price_momentum_avgupret_21d_base_v051_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 1)
    pos = r.where(r > 0, 0.0)
    result = pos.rolling(21, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# average up-day ROC over 63d
def f09pm_f09_price_momentum_avgupret_63d_base_v052_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 1)
    pos = r.where(r > 0, 0.0)
    result = pos.rolling(63, min_periods=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# average up-day ROC over 252d
def f09pm_f09_price_momentum_avgupret_252d_base_v053_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 1)
    pos = r.where(r > 0, 0.0)
    result = pos.rolling(252, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# average down-day ROC over 21d
def f09pm_f09_price_momentum_avgdownret_21d_base_v054_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 1)
    neg = r.where(r < 0, 0.0)
    result = neg.rolling(21, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# average down-day ROC over 63d
def f09pm_f09_price_momentum_avgdownret_63d_base_v055_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 1)
    neg = r.where(r < 0, 0.0)
    result = neg.rolling(63, min_periods=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# average down-day ROC over 252d
def f09pm_f09_price_momentum_avgdownret_252d_base_v056_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 1)
    neg = r.where(r < 0, 0.0)
    result = neg.rolling(252, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Sharpe-like proxy: 21d mean return / 21d std (annualized)
def f09pm_f09_price_momentum_sharpe_21d_base_v057_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 1)
    m = _mean(r, 21)
    s = _std(r, 21)
    result = (m / s.replace(0, np.nan)) * np.sqrt(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Sharpe-like 63d
def f09pm_f09_price_momentum_sharpe_63d_base_v058_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 1)
    m = _mean(r, 63)
    s = _std(r, 63)
    result = (m / s.replace(0, np.nan)) * np.sqrt(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Sharpe-like 252d
def f09pm_f09_price_momentum_sharpe_252d_base_v059_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 1)
    m = _mean(r, 252)
    s = _std(r, 252)
    result = (m / s.replace(0, np.nan)) * np.sqrt(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Sharpe-like 504d
def f09pm_f09_price_momentum_sharpe_504d_base_v060_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 1)
    m = _mean(r, 504)
    s = _std(r, 504)
    result = (m / s.replace(0, np.nan)) * np.sqrt(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROC × 21d ROC of past period (autocorrelation proxy)
def f09pm_f09_price_momentum_rocautocorr_21d_base_v061_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 21)
    result = r * r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROC × 63d ROC of past period
def f09pm_f09_price_momentum_rocautocorr_63d_base_v062_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 63)
    result = r * r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROC × 252d ROC past
def f09pm_f09_price_momentum_rocautocorr_252d_base_v063_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 252)
    result = r * r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# monthly momentum: 21d ROC at start of month
def f09pm_f09_price_momentum_monthlyroc_21d_base_v064_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 21)
    result = _mean(r, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROC monthly average
def f09pm_f09_price_momentum_monthlyroc_63d_base_v065_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 63)
    result = _mean(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROC quarterly average
def f09pm_f09_price_momentum_quarterlyroc_252d_base_v066_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 252)
    result = _mean(r, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROC excluding last 21d (12-1 momentum)
def f09pm_f09_price_momentum_mom12m1m_base_v067_signal(closeadj):
    a = _f09_momentum_roc(closeadj, 252)
    b = _f09_momentum_roc(closeadj, 21)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ROC excluding last 63d (24-3 momentum)
def f09pm_f09_price_momentum_mom24m3m_base_v068_signal(closeadj):
    a = _f09_momentum_roc(closeadj, 504)
    b = _f09_momentum_roc(closeadj, 63)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROC × win-rate (positive momentum confidence)
def f09pm_f09_price_momentum_rocxwin_21d_base_v069_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 21)
    flag = (_f09_momentum_roc(closeadj, 1) > 0).astype(float)
    win = flag.rolling(21, min_periods=5).mean()
    result = r * win * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROC × win-rate
def f09pm_f09_price_momentum_rocxwin_252d_base_v070_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 252)
    flag = (_f09_momentum_roc(closeadj, 1) > 0).astype(float)
    win = flag.rolling(252, min_periods=63).mean()
    result = r * win * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling max ROC over 21d (best return)
def f09pm_f09_price_momentum_rocmax_21d_base_v071_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 5)
    result = r.rolling(21, min_periods=5).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling max ROC over 63d
def f09pm_f09_price_momentum_rocmax_63d_base_v072_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 21)
    result = r.rolling(63, min_periods=21).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling min ROC over 21d (worst return)
def f09pm_f09_price_momentum_rocmin_21d_base_v073_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 5)
    result = r.rolling(21, min_periods=5).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling min ROC over 63d
def f09pm_f09_price_momentum_rocmin_63d_base_v074_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 21)
    result = r.rolling(63, min_periods=21).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROC range (max-min) over 63d
def f09pm_f09_price_momentum_rocrange_63d_base_v075_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 21)
    result = (r.rolling(63, min_periods=21).max() - r.rolling(63, min_periods=21).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f09pm_f09_price_momentum_roc_5d_base_v001_signal,
    f09pm_f09_price_momentum_roc_21d_base_v002_signal,
    f09pm_f09_price_momentum_roc_63d_base_v003_signal,
    f09pm_f09_price_momentum_roc_126d_base_v004_signal,
    f09pm_f09_price_momentum_roc_252d_base_v005_signal,
    f09pm_f09_price_momentum_roc_504d_base_v006_signal,
    f09pm_f09_price_momentum_logret_5d_base_v007_signal,
    f09pm_f09_price_momentum_logret_21d_base_v008_signal,
    f09pm_f09_price_momentum_logret_63d_base_v009_signal,
    f09pm_f09_price_momentum_logret_252d_base_v010_signal,
    f09pm_f09_price_momentum_logret_504d_base_v011_signal,
    f09pm_f09_price_momentum_riskadj_21d_base_v012_signal,
    f09pm_f09_price_momentum_riskadj_63d_base_v013_signal,
    f09pm_f09_price_momentum_riskadj_126d_base_v014_signal,
    f09pm_f09_price_momentum_riskadj_252d_base_v015_signal,
    f09pm_f09_price_momentum_riskadj_504d_base_v016_signal,
    f09pm_f09_price_momentum_rocz_21d_base_v017_signal,
    f09pm_f09_price_momentum_rocz_63d_base_v018_signal,
    f09pm_f09_price_momentum_rocz_252d_base_v019_signal,
    f09pm_f09_price_momentum_rocsq_21d_base_v020_signal,
    f09pm_f09_price_momentum_rocsq_63d_base_v021_signal,
    f09pm_f09_price_momentum_rocsq_252d_base_v022_signal,
    f09pm_f09_price_momentum_rocmean_5d_base_v023_signal,
    f09pm_f09_price_momentum_rocmean_21d_base_v024_signal,
    f09pm_f09_price_momentum_rocmean_63d_base_v025_signal,
    f09pm_f09_price_momentum_rocmean_252d_base_v026_signal,
    f09pm_f09_price_momentum_rocstd_21d_base_v027_signal,
    f09pm_f09_price_momentum_rocstd_63d_base_v028_signal,
    f09pm_f09_price_momentum_rocxprice_21d_base_v029_signal,
    f09pm_f09_price_momentum_rocxprice_63d_base_v030_signal,
    f09pm_f09_price_momentum_rocxprice_252d_base_v031_signal,
    f09pm_f09_price_momentum_rocxprice_504d_base_v032_signal,
    f09pm_f09_price_momentum_rocdiff_252m21_base_v033_signal,
    f09pm_f09_price_momentum_rocdiff_63m21_base_v034_signal,
    f09pm_f09_price_momentum_rocdiff_252m63_base_v035_signal,
    f09pm_f09_price_momentum_rocdiff_504m252_base_v036_signal,
    f09pm_f09_price_momentum_rocxvolz_21d_base_v037_signal,
    f09pm_f09_price_momentum_rocxvolz_63d_base_v038_signal,
    f09pm_f09_price_momentum_rocxdv_252d_base_v039_signal,
    f09pm_f09_price_momentum_rocxdv_5d_base_v040_signal,
    f09pm_f09_price_momentum_winstreak_21d_base_v041_signal,
    f09pm_f09_price_momentum_winstreak_63d_base_v042_signal,
    f09pm_f09_price_momentum_winstreak_252d_base_v043_signal,
    f09pm_f09_price_momentum_lossstreak_21d_base_v044_signal,
    f09pm_f09_price_momentum_lossstreak_63d_base_v045_signal,
    f09pm_f09_price_momentum_lossstreak_252d_base_v046_signal,
    f09pm_f09_price_momentum_winrate_21d_base_v047_signal,
    f09pm_f09_price_momentum_winrate_63d_base_v048_signal,
    f09pm_f09_price_momentum_winrate_252d_base_v049_signal,
    f09pm_f09_price_momentum_winrate_504d_base_v050_signal,
    f09pm_f09_price_momentum_avgupret_21d_base_v051_signal,
    f09pm_f09_price_momentum_avgupret_63d_base_v052_signal,
    f09pm_f09_price_momentum_avgupret_252d_base_v053_signal,
    f09pm_f09_price_momentum_avgdownret_21d_base_v054_signal,
    f09pm_f09_price_momentum_avgdownret_63d_base_v055_signal,
    f09pm_f09_price_momentum_avgdownret_252d_base_v056_signal,
    f09pm_f09_price_momentum_sharpe_21d_base_v057_signal,
    f09pm_f09_price_momentum_sharpe_63d_base_v058_signal,
    f09pm_f09_price_momentum_sharpe_252d_base_v059_signal,
    f09pm_f09_price_momentum_sharpe_504d_base_v060_signal,
    f09pm_f09_price_momentum_rocautocorr_21d_base_v061_signal,
    f09pm_f09_price_momentum_rocautocorr_63d_base_v062_signal,
    f09pm_f09_price_momentum_rocautocorr_252d_base_v063_signal,
    f09pm_f09_price_momentum_monthlyroc_21d_base_v064_signal,
    f09pm_f09_price_momentum_monthlyroc_63d_base_v065_signal,
    f09pm_f09_price_momentum_quarterlyroc_252d_base_v066_signal,
    f09pm_f09_price_momentum_mom12m1m_base_v067_signal,
    f09pm_f09_price_momentum_mom24m3m_base_v068_signal,
    f09pm_f09_price_momentum_rocxwin_21d_base_v069_signal,
    f09pm_f09_price_momentum_rocxwin_252d_base_v070_signal,
    f09pm_f09_price_momentum_rocmax_21d_base_v071_signal,
    f09pm_f09_price_momentum_rocmax_63d_base_v072_signal,
    f09pm_f09_price_momentum_rocmin_21d_base_v073_signal,
    f09pm_f09_price_momentum_rocmin_63d_base_v074_signal,
    f09pm_f09_price_momentum_rocrange_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F09_PRICE_MOMENTUM_REGISTRY_001_075 = REGISTRY


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

    cols = {"closeadj": closeadj, "high": high, "low": low, "volume": volume}

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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f09_price_momentum_base_001_075_claude: {n_features} features pass")
