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


def _slope(s, w):
    return s.diff(periods=w)


def _jerk(s, w):
    sl = s.diff(periods=w)
    return sl.diff(periods=w)


# ===== folder domain primitives =====

def _f14_balsheet_de(debt, equity):
    return debt / equity.replace(0, np.nan).abs()


def _f14_solvency_cr(currentratio):
    return currentratio


def _f14_balsheet_da(debt, assets):
    return debt / assets.replace(0, np.nan).abs()

# 5d slope of raw 21d primitive
def f14bss_f14_balance_sheet_snapshot_raw_21d_roc5_21d_slope_v001_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of raw 21d primitive
def f14bss_f14_balance_sheet_snapshot_raw_21d_roc21_21d_slope_v002_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of mean21 21d primitive
def f14bss_f14_balance_sheet_snapshot_mean21_21d_roc5_21d_slope_v003_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 21) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of mean21 21d primitive
def f14bss_f14_balance_sheet_snapshot_mean21_21d_roc21_21d_slope_v004_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 21) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of mean63 21d primitive
def f14bss_f14_balance_sheet_snapshot_mean63_21d_roc5_21d_slope_v005_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of mean63 21d primitive
def f14bss_f14_balance_sheet_snapshot_mean63_21d_roc21_21d_slope_v006_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of std63 21d primitive
def f14bss_f14_balance_sheet_snapshot_std63_21d_roc5_21d_slope_v007_signal(debt, equity, assets, currentratio, closeadj):
    base = _std(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of std63 21d primitive
def f14bss_f14_balance_sheet_snapshot_std63_21d_roc21_21d_slope_v008_signal(debt, equity, assets, currentratio, closeadj):
    base = _std(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of z63 21d primitive
def f14bss_f14_balance_sheet_snapshot_z63_21d_roc5_21d_slope_v009_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of z63 21d primitive
def f14bss_f14_balance_sheet_snapshot_z63_21d_roc21_21d_slope_v010_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of z252 21d primitive
def f14bss_f14_balance_sheet_snapshot_z252_21d_roc5_21d_slope_v011_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 252) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of z252 21d primitive
def f14bss_f14_balance_sheet_snapshot_z252_21d_roc21_21d_slope_v012_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 252) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of ema21 21d primitive
def f14bss_f14_balance_sheet_snapshot_ema21_21d_roc5_21d_slope_v013_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ema21 21d primitive
def f14bss_f14_balance_sheet_snapshot_ema21_21d_roc21_21d_slope_v014_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of ema63 21d primitive
def f14bss_f14_balance_sheet_snapshot_ema63_21d_roc5_21d_slope_v015_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ema63 21d primitive
def f14bss_f14_balance_sheet_snapshot_ema63_21d_roc21_21d_slope_v016_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of absmean63 21d primitive
def f14bss_f14_balance_sheet_snapshot_absmean63_21d_roc5_21d_slope_v017_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of absmean63 21d primitive
def f14bss_f14_balance_sheet_snapshot_absmean63_21d_roc21_21d_slope_v018_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of sqrmean63 21d primitive
def f14bss_f14_balance_sheet_snapshot_sqrmean63_21d_roc5_21d_slope_v019_signal(debt, equity, assets, currentratio, closeadj):
    base = ((_f14_balsheet_de(debt, equity)) * (_f14_balsheet_de(debt, equity)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sqrmean63 21d primitive
def f14bss_f14_balance_sheet_snapshot_sqrmean63_21d_roc21_21d_slope_v020_signal(debt, equity, assets, currentratio, closeadj):
    base = ((_f14_balsheet_de(debt, equity)) * (_f14_balsheet_de(debt, equity)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of raw 63d primitive
def f14bss_f14_balance_sheet_snapshot_raw_63d_roc5_63d_slope_v021_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of raw 63d primitive
def f14bss_f14_balance_sheet_snapshot_raw_63d_roc21_63d_slope_v022_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of raw 63d primitive
def f14bss_f14_balance_sheet_snapshot_raw_63d_roc63_63d_slope_v023_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of mean21 63d primitive
def f14bss_f14_balance_sheet_snapshot_mean21_63d_roc5_63d_slope_v024_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 21) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of mean21 63d primitive
def f14bss_f14_balance_sheet_snapshot_mean21_63d_roc21_63d_slope_v025_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 21) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of mean21 63d primitive
def f14bss_f14_balance_sheet_snapshot_mean21_63d_roc63_63d_slope_v026_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 21) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of mean63 63d primitive
def f14bss_f14_balance_sheet_snapshot_mean63_63d_roc5_63d_slope_v027_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of mean63 63d primitive
def f14bss_f14_balance_sheet_snapshot_mean63_63d_roc21_63d_slope_v028_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of mean63 63d primitive
def f14bss_f14_balance_sheet_snapshot_mean63_63d_roc63_63d_slope_v029_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of std63 63d primitive
def f14bss_f14_balance_sheet_snapshot_std63_63d_roc5_63d_slope_v030_signal(debt, equity, assets, currentratio, closeadj):
    base = _std(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of std63 63d primitive
def f14bss_f14_balance_sheet_snapshot_std63_63d_roc21_63d_slope_v031_signal(debt, equity, assets, currentratio, closeadj):
    base = _std(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of std63 63d primitive
def f14bss_f14_balance_sheet_snapshot_std63_63d_roc63_63d_slope_v032_signal(debt, equity, assets, currentratio, closeadj):
    base = _std(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of z63 63d primitive
def f14bss_f14_balance_sheet_snapshot_z63_63d_roc5_63d_slope_v033_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of z63 63d primitive
def f14bss_f14_balance_sheet_snapshot_z63_63d_roc21_63d_slope_v034_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of z63 63d primitive
def f14bss_f14_balance_sheet_snapshot_z63_63d_roc63_63d_slope_v035_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of z252 63d primitive
def f14bss_f14_balance_sheet_snapshot_z252_63d_roc5_63d_slope_v036_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 252) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of z252 63d primitive
def f14bss_f14_balance_sheet_snapshot_z252_63d_roc21_63d_slope_v037_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 252) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of z252 63d primitive
def f14bss_f14_balance_sheet_snapshot_z252_63d_roc63_63d_slope_v038_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 252) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of ema21 63d primitive
def f14bss_f14_balance_sheet_snapshot_ema21_63d_roc5_63d_slope_v039_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ema21 63d primitive
def f14bss_f14_balance_sheet_snapshot_ema21_63d_roc21_63d_slope_v040_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ema21 63d primitive
def f14bss_f14_balance_sheet_snapshot_ema21_63d_roc63_63d_slope_v041_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of ema63 63d primitive
def f14bss_f14_balance_sheet_snapshot_ema63_63d_roc5_63d_slope_v042_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ema63 63d primitive
def f14bss_f14_balance_sheet_snapshot_ema63_63d_roc21_63d_slope_v043_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ema63 63d primitive
def f14bss_f14_balance_sheet_snapshot_ema63_63d_roc63_63d_slope_v044_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of absmean63 63d primitive
def f14bss_f14_balance_sheet_snapshot_absmean63_63d_roc5_63d_slope_v045_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of absmean63 63d primitive
def f14bss_f14_balance_sheet_snapshot_absmean63_63d_roc21_63d_slope_v046_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of absmean63 63d primitive
def f14bss_f14_balance_sheet_snapshot_absmean63_63d_roc63_63d_slope_v047_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of sqrmean63 63d primitive
def f14bss_f14_balance_sheet_snapshot_sqrmean63_63d_roc5_63d_slope_v048_signal(debt, equity, assets, currentratio, closeadj):
    base = ((_f14_balsheet_de(debt, equity)) * (_f14_balsheet_de(debt, equity)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sqrmean63 63d primitive
def f14bss_f14_balance_sheet_snapshot_sqrmean63_63d_roc21_63d_slope_v049_signal(debt, equity, assets, currentratio, closeadj):
    base = ((_f14_balsheet_de(debt, equity)) * (_f14_balsheet_de(debt, equity)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sqrmean63 63d primitive
def f14bss_f14_balance_sheet_snapshot_sqrmean63_63d_roc63_63d_slope_v050_signal(debt, equity, assets, currentratio, closeadj):
    base = ((_f14_balsheet_de(debt, equity)) * (_f14_balsheet_de(debt, equity)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of raw 126d primitive
def f14bss_f14_balance_sheet_snapshot_raw_126d_roc21_126d_slope_v051_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of raw 126d primitive
def f14bss_f14_balance_sheet_snapshot_raw_126d_roc63_126d_slope_v052_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of mean21 126d primitive
def f14bss_f14_balance_sheet_snapshot_mean21_126d_roc21_126d_slope_v053_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 21) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of mean21 126d primitive
def f14bss_f14_balance_sheet_snapshot_mean21_126d_roc63_126d_slope_v054_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 21) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of mean63 126d primitive
def f14bss_f14_balance_sheet_snapshot_mean63_126d_roc21_126d_slope_v055_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of mean63 126d primitive
def f14bss_f14_balance_sheet_snapshot_mean63_126d_roc63_126d_slope_v056_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of std63 126d primitive
def f14bss_f14_balance_sheet_snapshot_std63_126d_roc21_126d_slope_v057_signal(debt, equity, assets, currentratio, closeadj):
    base = _std(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of std63 126d primitive
def f14bss_f14_balance_sheet_snapshot_std63_126d_roc63_126d_slope_v058_signal(debt, equity, assets, currentratio, closeadj):
    base = _std(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of z63 126d primitive
def f14bss_f14_balance_sheet_snapshot_z63_126d_roc21_126d_slope_v059_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of z63 126d primitive
def f14bss_f14_balance_sheet_snapshot_z63_126d_roc63_126d_slope_v060_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of z252 126d primitive
def f14bss_f14_balance_sheet_snapshot_z252_126d_roc21_126d_slope_v061_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 252) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of z252 126d primitive
def f14bss_f14_balance_sheet_snapshot_z252_126d_roc63_126d_slope_v062_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 252) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ema21 126d primitive
def f14bss_f14_balance_sheet_snapshot_ema21_126d_roc21_126d_slope_v063_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ema21 126d primitive
def f14bss_f14_balance_sheet_snapshot_ema21_126d_roc63_126d_slope_v064_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ema63 126d primitive
def f14bss_f14_balance_sheet_snapshot_ema63_126d_roc21_126d_slope_v065_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ema63 126d primitive
def f14bss_f14_balance_sheet_snapshot_ema63_126d_roc63_126d_slope_v066_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of absmean63 126d primitive
def f14bss_f14_balance_sheet_snapshot_absmean63_126d_roc21_126d_slope_v067_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of absmean63 126d primitive
def f14bss_f14_balance_sheet_snapshot_absmean63_126d_roc63_126d_slope_v068_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sqrmean63 126d primitive
def f14bss_f14_balance_sheet_snapshot_sqrmean63_126d_roc21_126d_slope_v069_signal(debt, equity, assets, currentratio, closeadj):
    base = ((_f14_balsheet_de(debt, equity)) * (_f14_balsheet_de(debt, equity)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sqrmean63 126d primitive
def f14bss_f14_balance_sheet_snapshot_sqrmean63_126d_roc63_126d_slope_v070_signal(debt, equity, assets, currentratio, closeadj):
    base = ((_f14_balsheet_de(debt, equity)) * (_f14_balsheet_de(debt, equity)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of raw 252d primitive
def f14bss_f14_balance_sheet_snapshot_raw_252d_roc21_252d_slope_v071_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of raw 252d primitive
def f14bss_f14_balance_sheet_snapshot_raw_252d_roc63_252d_slope_v072_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of mean21 252d primitive
def f14bss_f14_balance_sheet_snapshot_mean21_252d_roc21_252d_slope_v073_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 21) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of mean21 252d primitive
def f14bss_f14_balance_sheet_snapshot_mean21_252d_roc63_252d_slope_v074_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 21) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of mean63 252d primitive
def f14bss_f14_balance_sheet_snapshot_mean63_252d_roc21_252d_slope_v075_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of mean63 252d primitive
def f14bss_f14_balance_sheet_snapshot_mean63_252d_roc63_252d_slope_v076_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of std63 252d primitive
def f14bss_f14_balance_sheet_snapshot_std63_252d_roc21_252d_slope_v077_signal(debt, equity, assets, currentratio, closeadj):
    base = _std(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of std63 252d primitive
def f14bss_f14_balance_sheet_snapshot_std63_252d_roc63_252d_slope_v078_signal(debt, equity, assets, currentratio, closeadj):
    base = _std(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of z63 252d primitive
def f14bss_f14_balance_sheet_snapshot_z63_252d_roc21_252d_slope_v079_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of z63 252d primitive
def f14bss_f14_balance_sheet_snapshot_z63_252d_roc63_252d_slope_v080_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of z252 252d primitive
def f14bss_f14_balance_sheet_snapshot_z252_252d_roc21_252d_slope_v081_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 252) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of z252 252d primitive
def f14bss_f14_balance_sheet_snapshot_z252_252d_roc63_252d_slope_v082_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 252) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ema21 252d primitive
def f14bss_f14_balance_sheet_snapshot_ema21_252d_roc21_252d_slope_v083_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ema21 252d primitive
def f14bss_f14_balance_sheet_snapshot_ema21_252d_roc63_252d_slope_v084_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ema63 252d primitive
def f14bss_f14_balance_sheet_snapshot_ema63_252d_roc21_252d_slope_v085_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ema63 252d primitive
def f14bss_f14_balance_sheet_snapshot_ema63_252d_roc63_252d_slope_v086_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of absmean63 252d primitive
def f14bss_f14_balance_sheet_snapshot_absmean63_252d_roc21_252d_slope_v087_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of absmean63 252d primitive
def f14bss_f14_balance_sheet_snapshot_absmean63_252d_roc63_252d_slope_v088_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sqrmean63 252d primitive
def f14bss_f14_balance_sheet_snapshot_sqrmean63_252d_roc21_252d_slope_v089_signal(debt, equity, assets, currentratio, closeadj):
    base = ((_f14_balsheet_de(debt, equity)) * (_f14_balsheet_de(debt, equity)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sqrmean63 252d primitive
def f14bss_f14_balance_sheet_snapshot_sqrmean63_252d_roc63_252d_slope_v090_signal(debt, equity, assets, currentratio, closeadj):
    base = ((_f14_balsheet_de(debt, equity)) * (_f14_balsheet_de(debt, equity)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of raw 504d primitive
def f14bss_f14_balance_sheet_snapshot_raw_504d_roc21_504d_slope_v091_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of raw 504d primitive
def f14bss_f14_balance_sheet_snapshot_raw_504d_roc63_504d_slope_v092_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of raw 504d primitive
def f14bss_f14_balance_sheet_snapshot_raw_504d_roc126_504d_slope_v093_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)) * closeadj
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of mean21 504d primitive
def f14bss_f14_balance_sheet_snapshot_mean21_504d_roc21_504d_slope_v094_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 21) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of mean21 504d primitive
def f14bss_f14_balance_sheet_snapshot_mean21_504d_roc63_504d_slope_v095_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 21) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of mean21 504d primitive
def f14bss_f14_balance_sheet_snapshot_mean21_504d_roc126_504d_slope_v096_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 21) * closeadj
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of mean63 504d primitive
def f14bss_f14_balance_sheet_snapshot_mean63_504d_roc21_504d_slope_v097_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of mean63 504d primitive
def f14bss_f14_balance_sheet_snapshot_mean63_504d_roc63_504d_slope_v098_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of mean63 504d primitive
def f14bss_f14_balance_sheet_snapshot_mean63_504d_roc126_504d_slope_v099_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of std63 504d primitive
def f14bss_f14_balance_sheet_snapshot_std63_504d_roc21_504d_slope_v100_signal(debt, equity, assets, currentratio, closeadj):
    base = _std(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of std63 504d primitive
def f14bss_f14_balance_sheet_snapshot_std63_504d_roc63_504d_slope_v101_signal(debt, equity, assets, currentratio, closeadj):
    base = _std(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of std63 504d primitive
def f14bss_f14_balance_sheet_snapshot_std63_504d_roc126_504d_slope_v102_signal(debt, equity, assets, currentratio, closeadj):
    base = _std(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of z63 504d primitive
def f14bss_f14_balance_sheet_snapshot_z63_504d_roc21_504d_slope_v103_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of z63 504d primitive
def f14bss_f14_balance_sheet_snapshot_z63_504d_roc63_504d_slope_v104_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of z63 504d primitive
def f14bss_f14_balance_sheet_snapshot_z63_504d_roc126_504d_slope_v105_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of z252 504d primitive
def f14bss_f14_balance_sheet_snapshot_z252_504d_roc21_504d_slope_v106_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 252) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of z252 504d primitive
def f14bss_f14_balance_sheet_snapshot_z252_504d_roc63_504d_slope_v107_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 252) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of z252 504d primitive
def f14bss_f14_balance_sheet_snapshot_z252_504d_roc126_504d_slope_v108_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 252) * closeadj
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ema21 504d primitive
def f14bss_f14_balance_sheet_snapshot_ema21_504d_roc21_504d_slope_v109_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ema21 504d primitive
def f14bss_f14_balance_sheet_snapshot_ema21_504d_roc63_504d_slope_v110_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ema21 504d primitive
def f14bss_f14_balance_sheet_snapshot_ema21_504d_roc126_504d_slope_v111_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ema63 504d primitive
def f14bss_f14_balance_sheet_snapshot_ema63_504d_roc21_504d_slope_v112_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ema63 504d primitive
def f14bss_f14_balance_sheet_snapshot_ema63_504d_roc63_504d_slope_v113_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ema63 504d primitive
def f14bss_f14_balance_sheet_snapshot_ema63_504d_roc126_504d_slope_v114_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of absmean63 504d primitive
def f14bss_f14_balance_sheet_snapshot_absmean63_504d_roc21_504d_slope_v115_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of absmean63 504d primitive
def f14bss_f14_balance_sheet_snapshot_absmean63_504d_roc63_504d_slope_v116_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of absmean63 504d primitive
def f14bss_f14_balance_sheet_snapshot_absmean63_504d_roc126_504d_slope_v117_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sqrmean63 504d primitive
def f14bss_f14_balance_sheet_snapshot_sqrmean63_504d_roc21_504d_slope_v118_signal(debt, equity, assets, currentratio, closeadj):
    base = ((_f14_balsheet_de(debt, equity)) * (_f14_balsheet_de(debt, equity)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sqrmean63 504d primitive
def f14bss_f14_balance_sheet_snapshot_sqrmean63_504d_roc63_504d_slope_v119_signal(debt, equity, assets, currentratio, closeadj):
    base = ((_f14_balsheet_de(debt, equity)) * (_f14_balsheet_de(debt, equity)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sqrmean63 504d primitive
def f14bss_f14_balance_sheet_snapshot_sqrmean63_504d_roc126_504d_slope_v120_signal(debt, equity, assets, currentratio, closeadj):
    base = ((_f14_balsheet_de(debt, equity)) * (_f14_balsheet_de(debt, equity)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of raw 21d primitive
def f14bss_f14_balance_sheet_snapshot_raw_21d_roc5_21d_slope_v121_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of raw 21d primitive
def f14bss_f14_balance_sheet_snapshot_raw_21d_roc21_21d_slope_v122_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of raw 21d primitive
def f14bss_f14_balance_sheet_snapshot_raw_21d_roc63_21d_slope_v123_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of mean21 21d primitive
def f14bss_f14_balance_sheet_snapshot_mean21_21d_roc5_21d_slope_v124_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 21) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of mean21 21d primitive
def f14bss_f14_balance_sheet_snapshot_mean21_21d_roc21_21d_slope_v125_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 21) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of mean21 21d primitive
def f14bss_f14_balance_sheet_snapshot_mean21_21d_roc63_21d_slope_v126_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 21) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of mean63 21d primitive
def f14bss_f14_balance_sheet_snapshot_mean63_21d_roc5_21d_slope_v127_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of mean63 21d primitive
def f14bss_f14_balance_sheet_snapshot_mean63_21d_roc21_21d_slope_v128_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of mean63 21d primitive
def f14bss_f14_balance_sheet_snapshot_mean63_21d_roc63_21d_slope_v129_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of std63 21d primitive
def f14bss_f14_balance_sheet_snapshot_std63_21d_roc5_21d_slope_v130_signal(debt, equity, assets, currentratio, closeadj):
    base = _std(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of std63 21d primitive
def f14bss_f14_balance_sheet_snapshot_std63_21d_roc21_21d_slope_v131_signal(debt, equity, assets, currentratio, closeadj):
    base = _std(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of std63 21d primitive
def f14bss_f14_balance_sheet_snapshot_std63_21d_roc63_21d_slope_v132_signal(debt, equity, assets, currentratio, closeadj):
    base = _std(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of z63 21d primitive
def f14bss_f14_balance_sheet_snapshot_z63_21d_roc5_21d_slope_v133_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of z63 21d primitive
def f14bss_f14_balance_sheet_snapshot_z63_21d_roc21_21d_slope_v134_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of z63 21d primitive
def f14bss_f14_balance_sheet_snapshot_z63_21d_roc63_21d_slope_v135_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 63) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of z252 21d primitive
def f14bss_f14_balance_sheet_snapshot_z252_21d_roc5_21d_slope_v136_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 252) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of z252 21d primitive
def f14bss_f14_balance_sheet_snapshot_z252_21d_roc21_21d_slope_v137_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 252) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of z252 21d primitive
def f14bss_f14_balance_sheet_snapshot_z252_21d_roc63_21d_slope_v138_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 252) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of ema21 21d primitive
def f14bss_f14_balance_sheet_snapshot_ema21_21d_roc5_21d_slope_v139_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ema21 21d primitive
def f14bss_f14_balance_sheet_snapshot_ema21_21d_roc21_21d_slope_v140_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ema21 21d primitive
def f14bss_f14_balance_sheet_snapshot_ema21_21d_roc63_21d_slope_v141_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of ema63 21d primitive
def f14bss_f14_balance_sheet_snapshot_ema63_21d_roc5_21d_slope_v142_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ema63 21d primitive
def f14bss_f14_balance_sheet_snapshot_ema63_21d_roc21_21d_slope_v143_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ema63 21d primitive
def f14bss_f14_balance_sheet_snapshot_ema63_21d_roc63_21d_slope_v144_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of absmean63 21d primitive
def f14bss_f14_balance_sheet_snapshot_absmean63_21d_roc5_21d_slope_v145_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of absmean63 21d primitive
def f14bss_f14_balance_sheet_snapshot_absmean63_21d_roc21_21d_slope_v146_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of absmean63 21d primitive
def f14bss_f14_balance_sheet_snapshot_absmean63_21d_roc63_21d_slope_v147_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of sqrmean63 21d primitive
def f14bss_f14_balance_sheet_snapshot_sqrmean63_21d_roc5_21d_slope_v148_signal(debt, equity, assets, currentratio, closeadj):
    base = ((_f14_balsheet_de(debt, equity)) * (_f14_balsheet_de(debt, equity)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sqrmean63 21d primitive
def f14bss_f14_balance_sheet_snapshot_sqrmean63_21d_roc21_21d_slope_v149_signal(debt, equity, assets, currentratio, closeadj):
    base = ((_f14_balsheet_de(debt, equity)) * (_f14_balsheet_de(debt, equity)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sqrmean63 21d primitive
def f14bss_f14_balance_sheet_snapshot_sqrmean63_21d_roc63_21d_slope_v150_signal(debt, equity, assets, currentratio, closeadj):
    base = ((_f14_balsheet_de(debt, equity)) * (_f14_balsheet_de(debt, equity)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [v for k, v in list(globals().items()) if k.startswith("f14bss_") and callable(v)]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    debt = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.005, n))), name="debt")
    equity = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.004, n))), name="equity")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.003, n))), name="assets")
    currentratio = pd.Series(1.8 * np.exp(np.cumsum(np.random.normal(0.0, 0.003, n))), name="currentratio")
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    cols = {"debt": debt, "equity": equity, "assets": assets, "currentratio": currentratio, "closeadj": closeadj}
    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f14_balsheet_de", "_f14_solvency_cr", "_f14_balsheet_da",)
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
        if y1.iloc[504:].isna().mean() < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f14_balance_sheet_snapshot_2nd_derivatives_001_150_claude: {n_features} features pass")
