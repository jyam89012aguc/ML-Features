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

# raw of 21d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_raw_21d_21d_base_v001_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity))
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean21 of 21d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_mean21_21d_21d_base_v002_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean63 of 21d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_mean63_21d_21d_base_v003_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# std63 of 21d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_std63_21d_21d_base_v004_signal(debt, equity, assets, currentratio, closeadj):
    base = _std(_f14_balsheet_de(debt, equity), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z63 of 21d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_z63_21d_21d_base_v005_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z252 of 21d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_z252_21d_21d_base_v006_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema21 of 21d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_ema21_21d_21d_base_v007_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=21, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema63 of 21d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_ema63_21d_21d_base_v008_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=63, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# absmean63 of 21d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_absmean63_21d_21d_base_v009_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).abs().rolling(63, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sqrmean63 of 21d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_sqrmean63_21d_21d_base_v010_signal(debt, equity, assets, currentratio, closeadj):
    base = ((_f14_balsheet_de(debt, equity)) * (_f14_balsheet_de(debt, equity)).abs()).rolling(63, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# raw of 63d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_raw_63d_63d_base_v011_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity))
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean21 of 63d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_mean21_63d_63d_base_v012_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean63 of 63d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_mean63_63d_63d_base_v013_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# std63 of 63d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_std63_63d_63d_base_v014_signal(debt, equity, assets, currentratio, closeadj):
    base = _std(_f14_balsheet_de(debt, equity), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z63 of 63d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_z63_63d_63d_base_v015_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z252 of 63d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_z252_63d_63d_base_v016_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema21 of 63d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_ema21_63d_63d_base_v017_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=21, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema63 of 63d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_ema63_63d_63d_base_v018_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=63, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# absmean63 of 63d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_absmean63_63d_63d_base_v019_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).abs().rolling(63, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sqrmean63 of 63d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_sqrmean63_63d_63d_base_v020_signal(debt, equity, assets, currentratio, closeadj):
    base = ((_f14_balsheet_de(debt, equity)) * (_f14_balsheet_de(debt, equity)).abs()).rolling(63, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# raw of 126d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_raw_126d_126d_base_v021_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity))
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean21 of 126d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_mean21_126d_126d_base_v022_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean63 of 126d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_mean63_126d_126d_base_v023_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# std63 of 126d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_std63_126d_126d_base_v024_signal(debt, equity, assets, currentratio, closeadj):
    base = _std(_f14_balsheet_de(debt, equity), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z63 of 126d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_z63_126d_126d_base_v025_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z252 of 126d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_z252_126d_126d_base_v026_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema21 of 126d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_ema21_126d_126d_base_v027_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=21, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema63 of 126d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_ema63_126d_126d_base_v028_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=63, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# absmean63 of 126d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_absmean63_126d_126d_base_v029_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).abs().rolling(63, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sqrmean63 of 126d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_sqrmean63_126d_126d_base_v030_signal(debt, equity, assets, currentratio, closeadj):
    base = ((_f14_balsheet_de(debt, equity)) * (_f14_balsheet_de(debt, equity)).abs()).rolling(63, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# raw of 252d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_raw_252d_252d_base_v031_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity))
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean21 of 252d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_mean21_252d_252d_base_v032_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean63 of 252d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_mean63_252d_252d_base_v033_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# std63 of 252d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_std63_252d_252d_base_v034_signal(debt, equity, assets, currentratio, closeadj):
    base = _std(_f14_balsheet_de(debt, equity), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z63 of 252d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_z63_252d_252d_base_v035_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z252 of 252d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_z252_252d_252d_base_v036_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema21 of 252d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_ema21_252d_252d_base_v037_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=21, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema63 of 252d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_ema63_252d_252d_base_v038_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=63, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# absmean63 of 252d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_absmean63_252d_252d_base_v039_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).abs().rolling(63, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sqrmean63 of 252d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_sqrmean63_252d_252d_base_v040_signal(debt, equity, assets, currentratio, closeadj):
    base = ((_f14_balsheet_de(debt, equity)) * (_f14_balsheet_de(debt, equity)).abs()).rolling(63, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# raw of 504d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_raw_504d_504d_base_v041_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity))
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean21 of 504d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_mean21_504d_504d_base_v042_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean63 of 504d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_mean63_504d_504d_base_v043_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# std63 of 504d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_std63_504d_504d_base_v044_signal(debt, equity, assets, currentratio, closeadj):
    base = _std(_f14_balsheet_de(debt, equity), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z63 of 504d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_z63_504d_504d_base_v045_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z252 of 504d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_z252_504d_504d_base_v046_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema21 of 504d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_ema21_504d_504d_base_v047_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=21, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema63 of 504d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_ema63_504d_504d_base_v048_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=63, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# absmean63 of 504d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_absmean63_504d_504d_base_v049_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).abs().rolling(63, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sqrmean63 of 504d primitive for f14_balance_sheet_snapshot
def f14bss_f14_balance_sheet_snapshot_sqrmean63_504d_504d_base_v050_signal(debt, equity, assets, currentratio, closeadj):
    base = ((_f14_balsheet_de(debt, equity)) * (_f14_balsheet_de(debt, equity)).abs()).rolling(63, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema126 of 21d primitive
def f14bss_f14_balance_sheet_snapshot_ema126_21d_21d_base_v051_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=126, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema252 of 63d primitive
def f14bss_f14_balance_sheet_snapshot_ema252_63d_63d_base_v052_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=252, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean126 of 126d primitive
def f14bss_f14_balance_sheet_snapshot_mean126_126d_126d_base_v053_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean252 of 252d primitive
def f14bss_f14_balance_sheet_snapshot_mean252_252d_252d_base_v054_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# std126 of 504d primitive
def f14bss_f14_balance_sheet_snapshot_std126_504d_504d_base_v055_signal(debt, equity, assets, currentratio, closeadj):
    base = _std(_f14_balsheet_de(debt, equity), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# std21 of 21d primitive
def f14bss_f14_balance_sheet_snapshot_std21_21d_21d_base_v056_signal(debt, equity, assets, currentratio, closeadj):
    base = _std(_f14_balsheet_de(debt, equity), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z126 of 63d primitive
def f14bss_f14_balance_sheet_snapshot_z126_63d_63d_base_v057_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z504 of 126d primitive
def f14bss_f14_balance_sheet_snapshot_z504_126d_126d_base_v058_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# absmean21 of 252d primitive
def f14bss_f14_balance_sheet_snapshot_absmean21_252d_252d_base_v059_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).abs().rolling(21, min_periods=5).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# absmean252 of 504d primitive
def f14bss_f14_balance_sheet_snapshot_absmean252_504d_504d_base_v060_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).abs().rolling(252, min_periods=63).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema126 of 21d primitive
def f14bss_f14_balance_sheet_snapshot_ema126_21d_21d_base_v061_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=126, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema252 of 63d primitive
def f14bss_f14_balance_sheet_snapshot_ema252_63d_63d_base_v062_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=252, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean126 of 126d primitive
def f14bss_f14_balance_sheet_snapshot_mean126_126d_126d_base_v063_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean252 of 252d primitive
def f14bss_f14_balance_sheet_snapshot_mean252_252d_252d_base_v064_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# std126 of 504d primitive
def f14bss_f14_balance_sheet_snapshot_std126_504d_504d_base_v065_signal(debt, equity, assets, currentratio, closeadj):
    base = _std(_f14_balsheet_de(debt, equity), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# std21 of 21d primitive
def f14bss_f14_balance_sheet_snapshot_std21_21d_21d_base_v066_signal(debt, equity, assets, currentratio, closeadj):
    base = _std(_f14_balsheet_de(debt, equity), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z126 of 63d primitive
def f14bss_f14_balance_sheet_snapshot_z126_63d_63d_base_v067_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z504 of 126d primitive
def f14bss_f14_balance_sheet_snapshot_z504_126d_126d_base_v068_signal(debt, equity, assets, currentratio, closeadj):
    base = _z(_f14_balsheet_de(debt, equity), 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# absmean21 of 252d primitive
def f14bss_f14_balance_sheet_snapshot_absmean21_252d_252d_base_v069_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).abs().rolling(21, min_periods=5).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# absmean252 of 504d primitive
def f14bss_f14_balance_sheet_snapshot_absmean252_504d_504d_base_v070_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).abs().rolling(252, min_periods=63).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema126 of 21d primitive
def f14bss_f14_balance_sheet_snapshot_ema126_21d_21d_base_v071_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=126, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema252 of 63d primitive
def f14bss_f14_balance_sheet_snapshot_ema252_63d_63d_base_v072_signal(debt, equity, assets, currentratio, closeadj):
    base = (_f14_balsheet_de(debt, equity)).ewm(span=252, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean126 of 126d primitive
def f14bss_f14_balance_sheet_snapshot_mean126_126d_126d_base_v073_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean252 of 252d primitive
def f14bss_f14_balance_sheet_snapshot_mean252_252d_252d_base_v074_signal(debt, equity, assets, currentratio, closeadj):
    base = _mean(_f14_balsheet_de(debt, equity), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# std126 of 504d primitive
def f14bss_f14_balance_sheet_snapshot_std126_504d_504d_base_v075_signal(debt, equity, assets, currentratio, closeadj):
    base = _std(_f14_balsheet_de(debt, equity), 126)
    result = base * closeadj
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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f14_balance_sheet_snapshot_base_001_075_claude: {n_features} features pass")
