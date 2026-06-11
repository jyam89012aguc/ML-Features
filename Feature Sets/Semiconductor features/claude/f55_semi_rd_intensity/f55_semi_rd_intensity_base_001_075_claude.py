import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


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


def _z(s, w):
    return (s - _mean(s, w)) / _std(s, w).replace(0, np.nan)



# ===== folder domain primitives =====
def _f55_build_metric(*args):
    return None  # placeholder (helper unused; metric built inline per feature)


def _f55_safe_pct(x, n):
    return x.pct_change(n)


def _f55_safe_log(x):
    return np.log(x.replace(0, np.nan).abs())


def _f55_zscore(s, w):
    return (s - s.rolling(w, min_periods=max(1, w // 2)).mean()) / s.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)

# 21d R&D intensity (rnd / revenue) level minus its 21d mean
def f55rdi_f55_semi_rd_intensity_rdi_21d_base_v001_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = m - _mean(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d R&D intensity (rnd / revenue) level minus its 63d mean
def f55rdi_f55_semi_rd_intensity_rdi_63d_base_v002_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = m - _mean(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d R&D intensity (rnd / revenue) level minus its 126d mean
def f55rdi_f55_semi_rd_intensity_rdi_126d_base_v003_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = m - _mean(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d R&D intensity (rnd / revenue) level minus its 252d mean
def f55rdi_f55_semi_rd_intensity_rdi_252d_base_v004_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = m - _mean(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d R&D intensity (rnd / revenue) level minus its 504d mean
def f55rdi_f55_semi_rd_intensity_rdi_504d_base_v005_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = m - _mean(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_21d_base_v006_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = _z(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_63d_base_v007_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = _z(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_126d_base_v008_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = _z(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_252d_base_v009_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = _z(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_504d_base_v010_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = _z(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d robust z-score (median/MAD) of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_21d_base_v011_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    med = m.rolling(21, min_periods=10).median()
    mad = (m - med).abs().rolling(21, min_periods=10).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d robust z-score (median/MAD) of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_63d_base_v012_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    med = m.rolling(63, min_periods=31).median()
    mad = (m - med).abs().rolling(63, min_periods=31).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d robust z-score (median/MAD) of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_126d_base_v013_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    med = m.rolling(126, min_periods=63).median()
    mad = (m - med).abs().rolling(126, min_periods=63).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d robust z-score (median/MAD) of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_252d_base_v014_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    med = m.rolling(252, min_periods=126).median()
    mad = (m - med).abs().rolling(252, min_periods=126).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d robust z-score (median/MAD) of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_504d_base_v015_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    med = m.rolling(504, min_periods=252).median()
    mad = (m - med).abs().rolling(504, min_periods=252).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling max of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_21d_base_v016_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = _max(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling max of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_63d_base_v017_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = _max(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling max of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_126d_base_v018_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = _max(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_252d_base_v019_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = _max(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_504d_base_v020_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = _max(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling min of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_21d_base_v021_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = _min(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling min of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_63d_base_v022_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = _min(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling min of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_126d_base_v023_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = _min(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_252d_base_v024_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = _min(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_504d_base_v025_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = _min(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d range of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_21d_base_v026_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = _max(m, 21) - _min(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d range of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_63d_base_v027_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = _max(m, 63) - _min(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d range of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_126d_base_v028_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = _max(m, 126) - _min(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d range of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_252d_base_v029_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = _max(m, 252) - _min(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d range of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_504d_base_v030_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = _max(m, 504) - _min(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d position-in-range of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_21d_base_v031_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    lo = _min(m, 21)
    hi = _max(m, 21)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d position-in-range of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_63d_base_v032_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    lo = _min(m, 63)
    hi = _max(m, 63)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d position-in-range of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_126d_base_v033_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    lo = _min(m, 126)
    hi = _max(m, 126)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d position-in-range of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_252d_base_v034_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    lo = _min(m, 252)
    hi = _max(m, 252)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d position-in-range of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_504d_base_v035_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    lo = _min(m, 504)
    hi = _max(m, 504)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d drawdown of R&D intensity (rnd / revenue) from rolling peak
def f55rdi_f55_semi_rd_intensity_rdi_21d_base_v036_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    peak = _max(m, 21)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)

# 63d drawdown of R&D intensity (rnd / revenue) from rolling peak
def f55rdi_f55_semi_rd_intensity_rdi_63d_base_v037_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    peak = _max(m, 63)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)

# 126d drawdown of R&D intensity (rnd / revenue) from rolling peak
def f55rdi_f55_semi_rd_intensity_rdi_126d_base_v038_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    peak = _max(m, 126)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)

# 252d drawdown of R&D intensity (rnd / revenue) from rolling peak
def f55rdi_f55_semi_rd_intensity_rdi_252d_base_v039_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    peak = _max(m, 252)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)

# 504d drawdown of R&D intensity (rnd / revenue) from rolling peak
def f55rdi_f55_semi_rd_intensity_rdi_504d_base_v040_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    peak = _max(m, 504)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)

# 21d run-up of R&D intensity (rnd / revenue) above rolling trough
def f55rdi_f55_semi_rd_intensity_rdi_21d_base_v041_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    trough = _min(m, 21)
    result = m - trough
    return result.replace([np.inf, -np.inf], np.nan)

# 63d run-up of R&D intensity (rnd / revenue) above rolling trough
def f55rdi_f55_semi_rd_intensity_rdi_63d_base_v042_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    trough = _min(m, 63)
    result = m - trough
    return result.replace([np.inf, -np.inf], np.nan)

# 126d run-up of R&D intensity (rnd / revenue) above rolling trough
def f55rdi_f55_semi_rd_intensity_rdi_126d_base_v043_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    trough = _min(m, 126)
    result = m - trough
    return result.replace([np.inf, -np.inf], np.nan)

# 252d run-up of R&D intensity (rnd / revenue) above rolling trough
def f55rdi_f55_semi_rd_intensity_rdi_252d_base_v044_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    trough = _min(m, 252)
    result = m - trough
    return result.replace([np.inf, -np.inf], np.nan)

# 504d run-up of R&D intensity (rnd / revenue) above rolling trough
def f55rdi_f55_semi_rd_intensity_rdi_504d_base_v045_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    trough = _min(m, 504)
    result = m - trough
    return result.replace([np.inf, -np.inf], np.nan)

# 21d std of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_21d_base_v046_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = _std(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d std of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_63d_base_v047_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = _std(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d std of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_126d_base_v048_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = _std(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d std of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_252d_base_v049_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = _std(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d std of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_504d_base_v050_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = _std(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d skew of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_21d_base_v051_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = m.rolling(21, min_periods=10).skew()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d skew of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_63d_base_v052_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = m.rolling(63, min_periods=31).skew()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d skew of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_126d_base_v053_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = m.rolling(126, min_periods=63).skew()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d skew of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_252d_base_v054_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = m.rolling(252, min_periods=126).skew()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d skew of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_504d_base_v055_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = m.rolling(504, min_periods=252).skew()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d kurtosis of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_21d_base_v056_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = m.rolling(21, min_periods=10).kurt()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d kurtosis of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_63d_base_v057_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = m.rolling(63, min_periods=31).kurt()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d kurtosis of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_126d_base_v058_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = m.rolling(126, min_periods=63).kurt()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d kurtosis of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_252d_base_v059_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = m.rolling(252, min_periods=126).kurt()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d kurtosis of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_504d_base_v060_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = m.rolling(504, min_periods=252).kurt()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d hit-ratio of R&D intensity (rnd / revenue) positivity
def f55rdi_f55_semi_rd_intensity_rdi_21d_base_v061_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = (m > 0).astype(float).rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d hit-ratio of R&D intensity (rnd / revenue) positivity
def f55rdi_f55_semi_rd_intensity_rdi_63d_base_v062_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = (m > 0).astype(float).rolling(63, min_periods=31).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d hit-ratio of R&D intensity (rnd / revenue) positivity
def f55rdi_f55_semi_rd_intensity_rdi_126d_base_v063_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = (m > 0).astype(float).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d hit-ratio of R&D intensity (rnd / revenue) positivity
def f55rdi_f55_semi_rd_intensity_rdi_252d_base_v064_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = (m > 0).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d hit-ratio of R&D intensity (rnd / revenue) positivity
def f55rdi_f55_semi_rd_intensity_rdi_504d_base_v065_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = (m > 0).astype(float).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d signed cumsum of R&D intensity (rnd / revenue) changes
def f55rdi_f55_semi_rd_intensity_rdi_21d_base_v066_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    d = m.diff()
    result = pd.Series(np.sign(d), index=m.index).rolling(21, min_periods=10).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d signed cumsum of R&D intensity (rnd / revenue) changes
def f55rdi_f55_semi_rd_intensity_rdi_63d_base_v067_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    d = m.diff()
    result = pd.Series(np.sign(d), index=m.index).rolling(63, min_periods=31).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d signed cumsum of R&D intensity (rnd / revenue) changes
def f55rdi_f55_semi_rd_intensity_rdi_126d_base_v068_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    d = m.diff()
    result = pd.Series(np.sign(d), index=m.index).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d signed cumsum of R&D intensity (rnd / revenue) changes
def f55rdi_f55_semi_rd_intensity_rdi_252d_base_v069_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    d = m.diff()
    result = pd.Series(np.sign(d), index=m.index).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d signed cumsum of R&D intensity (rnd / revenue) changes
def f55rdi_f55_semi_rd_intensity_rdi_504d_base_v070_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    d = m.diff()
    result = pd.Series(np.sign(d), index=m.index).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# EMA crossover 5 vs 21 of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_5d_base_v071_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = m.ewm(span=5, adjust=False).mean() - m.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# EMA crossover 21 vs 63 of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_21d_base_v072_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = m.ewm(span=21, adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# EMA crossover 63 vs 126 of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_63d_base_v073_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = m.ewm(span=63, adjust=False).mean() - m.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# EMA crossover 126 vs 252 of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_126d_base_v074_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = m.ewm(span=126, adjust=False).mean() - m.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# EMA crossover 252 vs 504 of R&D intensity (rnd / revenue)
def f55rdi_f55_semi_rd_intensity_rdi_252d_base_v075_signal(rnd, revenue, closeadj):
    m = rnd / revenue.replace(0, np.nan)
    result = m.ewm(span=252, adjust=False).mean() - m.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)
