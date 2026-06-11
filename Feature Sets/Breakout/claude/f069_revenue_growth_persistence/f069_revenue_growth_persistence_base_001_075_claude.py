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


def _ema(s, w):
    return s.ewm(span=max(2, w), adjust=False, min_periods=max(1, w // 2)).mean()


def _signlike(s):
    return np.tanh(s)



# ===== folder domain primitives =====
def _f069_growth_rate(revenue, w):
    return revenue.pct_change(periods=w)


def _f069_consec_accelerating(revenue, w):
    # count of periods within window where growth is accelerating
    g = revenue.pct_change(periods=max(2, w // 4))
    accel = (g.diff() > 0).astype(float)
    return accel.rolling(w, min_periods=max(1, w // 2)).sum()


def _f069_persistence_count(revenue, w):
    # rolling fraction of periods with positive growth, scaled
    g = revenue.pct_change(periods=max(2, w // 4))
    pos = (g > 0).astype(float)
    sm = pos.rolling(w, min_periods=max(1, w // 2)).mean()
    return sm * g.rolling(w, min_periods=max(1, w // 2)).mean()


# growth_5d_x_close base
def f069rgp_f069_revenue_growth_persistence_growth_5d_x_close_base_v001_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# growth_10d_x_close base
def f069rgp_f069_revenue_growth_persistence_growth_10d_x_close_base_v002_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# growth_21d_x_close base
def f069rgp_f069_revenue_growth_persistence_growth_21d_x_close_base_v003_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# growth_42d_x_close base
def f069rgp_f069_revenue_growth_persistence_growth_42d_x_close_base_v004_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# growth_63d_x_close base
def f069rgp_f069_revenue_growth_persistence_growth_63d_x_close_base_v005_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# growth_126d_x_close base
def f069rgp_f069_revenue_growth_persistence_growth_126d_x_close_base_v006_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# growth_189d_x_close base
def f069rgp_f069_revenue_growth_persistence_growth_189d_x_close_base_v007_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# growth_252d_x_close base
def f069rgp_f069_revenue_growth_persistence_growth_252d_x_close_base_v008_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# growth_378d_x_close base
def f069rgp_f069_revenue_growth_persistence_growth_378d_x_close_base_v009_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# growth_504d_x_close base
def f069rgp_f069_revenue_growth_persistence_growth_504d_x_close_base_v010_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# accel_5d_x_close base
def f069rgp_f069_revenue_growth_persistence_accel_5d_x_close_base_v011_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# accel_10d_x_close base
def f069rgp_f069_revenue_growth_persistence_accel_10d_x_close_base_v012_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# accel_21d_x_close base
def f069rgp_f069_revenue_growth_persistence_accel_21d_x_close_base_v013_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# accel_42d_x_close base
def f069rgp_f069_revenue_growth_persistence_accel_42d_x_close_base_v014_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# accel_63d_x_close base
def f069rgp_f069_revenue_growth_persistence_accel_63d_x_close_base_v015_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# accel_126d_x_close base
def f069rgp_f069_revenue_growth_persistence_accel_126d_x_close_base_v016_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# accel_189d_x_close base
def f069rgp_f069_revenue_growth_persistence_accel_189d_x_close_base_v017_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# accel_252d_x_close base
def f069rgp_f069_revenue_growth_persistence_accel_252d_x_close_base_v018_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# accel_378d_x_close base
def f069rgp_f069_revenue_growth_persistence_accel_378d_x_close_base_v019_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# accel_504d_x_close base
def f069rgp_f069_revenue_growth_persistence_accel_504d_x_close_base_v020_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# persist_5d_x_close base
def f069rgp_f069_revenue_growth_persistence_persist_5d_x_close_base_v021_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# persist_10d_x_close base
def f069rgp_f069_revenue_growth_persistence_persist_10d_x_close_base_v022_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# persist_21d_x_close base
def f069rgp_f069_revenue_growth_persistence_persist_21d_x_close_base_v023_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# persist_42d_x_close base
def f069rgp_f069_revenue_growth_persistence_persist_42d_x_close_base_v024_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# persist_63d_x_close base
def f069rgp_f069_revenue_growth_persistence_persist_63d_x_close_base_v025_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# persist_126d_x_close base
def f069rgp_f069_revenue_growth_persistence_persist_126d_x_close_base_v026_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# persist_189d_x_close base
def f069rgp_f069_revenue_growth_persistence_persist_189d_x_close_base_v027_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# persist_252d_x_close base
def f069rgp_f069_revenue_growth_persistence_persist_252d_x_close_base_v028_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# persist_378d_x_close base
def f069rgp_f069_revenue_growth_persistence_persist_378d_x_close_base_v029_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# persist_504d_x_close base
def f069rgp_f069_revenue_growth_persistence_persist_504d_x_close_base_v030_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# growth_5d_x_logclose base
def f069rgp_f069_revenue_growth_persistence_growth_5d_x_logclose_base_v031_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 5)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_10d_x_logclose base
def f069rgp_f069_revenue_growth_persistence_growth_10d_x_logclose_base_v032_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 10)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_21d_x_logclose base
def f069rgp_f069_revenue_growth_persistence_growth_21d_x_logclose_base_v033_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 21)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_42d_x_logclose base
def f069rgp_f069_revenue_growth_persistence_growth_42d_x_logclose_base_v034_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 42)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_63d_x_logclose base
def f069rgp_f069_revenue_growth_persistence_growth_63d_x_logclose_base_v035_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 63)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_126d_x_logclose base
def f069rgp_f069_revenue_growth_persistence_growth_126d_x_logclose_base_v036_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 126)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_189d_x_logclose base
def f069rgp_f069_revenue_growth_persistence_growth_189d_x_logclose_base_v037_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 189)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_252d_x_logclose base
def f069rgp_f069_revenue_growth_persistence_growth_252d_x_logclose_base_v038_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 252)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_378d_x_logclose base
def f069rgp_f069_revenue_growth_persistence_growth_378d_x_logclose_base_v039_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 378)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_504d_x_logclose base
def f069rgp_f069_revenue_growth_persistence_growth_504d_x_logclose_base_v040_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 504)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_5d_x_logclose base
def f069rgp_f069_revenue_growth_persistence_accel_5d_x_logclose_base_v041_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 5)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_10d_x_logclose base
def f069rgp_f069_revenue_growth_persistence_accel_10d_x_logclose_base_v042_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 10)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_21d_x_logclose base
def f069rgp_f069_revenue_growth_persistence_accel_21d_x_logclose_base_v043_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 21)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_42d_x_logclose base
def f069rgp_f069_revenue_growth_persistence_accel_42d_x_logclose_base_v044_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 42)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_63d_x_logclose base
def f069rgp_f069_revenue_growth_persistence_accel_63d_x_logclose_base_v045_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 63)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_126d_x_logclose base
def f069rgp_f069_revenue_growth_persistence_accel_126d_x_logclose_base_v046_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 126)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_189d_x_logclose base
def f069rgp_f069_revenue_growth_persistence_accel_189d_x_logclose_base_v047_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 189)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_252d_x_logclose base
def f069rgp_f069_revenue_growth_persistence_accel_252d_x_logclose_base_v048_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 252)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_378d_x_logclose base
def f069rgp_f069_revenue_growth_persistence_accel_378d_x_logclose_base_v049_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 378)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_504d_x_logclose base
def f069rgp_f069_revenue_growth_persistence_accel_504d_x_logclose_base_v050_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 504)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_5d_x_logclose base
def f069rgp_f069_revenue_growth_persistence_persist_5d_x_logclose_base_v051_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 5)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_10d_x_logclose base
def f069rgp_f069_revenue_growth_persistence_persist_10d_x_logclose_base_v052_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 10)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_21d_x_logclose base
def f069rgp_f069_revenue_growth_persistence_persist_21d_x_logclose_base_v053_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 21)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_42d_x_logclose base
def f069rgp_f069_revenue_growth_persistence_persist_42d_x_logclose_base_v054_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 42)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_63d_x_logclose base
def f069rgp_f069_revenue_growth_persistence_persist_63d_x_logclose_base_v055_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 63)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_126d_x_logclose base
def f069rgp_f069_revenue_growth_persistence_persist_126d_x_logclose_base_v056_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 126)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_189d_x_logclose base
def f069rgp_f069_revenue_growth_persistence_persist_189d_x_logclose_base_v057_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 189)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_252d_x_logclose base
def f069rgp_f069_revenue_growth_persistence_persist_252d_x_logclose_base_v058_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 252)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_378d_x_logclose base
def f069rgp_f069_revenue_growth_persistence_persist_378d_x_logclose_base_v059_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 378)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_504d_x_logclose base
def f069rgp_f069_revenue_growth_persistence_persist_504d_x_logclose_base_v060_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 504)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_5d_x_meanclose base
def f069rgp_f069_revenue_growth_persistence_growth_5d_x_meanclose_base_v061_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 5)
    result = base * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_10d_x_meanclose base
def f069rgp_f069_revenue_growth_persistence_growth_10d_x_meanclose_base_v062_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 10)
    result = base * _mean(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_21d_x_meanclose base
def f069rgp_f069_revenue_growth_persistence_growth_21d_x_meanclose_base_v063_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 21)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_42d_x_meanclose base
def f069rgp_f069_revenue_growth_persistence_growth_42d_x_meanclose_base_v064_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 42)
    result = base * _mean(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_63d_x_meanclose base
def f069rgp_f069_revenue_growth_persistence_growth_63d_x_meanclose_base_v065_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_126d_x_meanclose base
def f069rgp_f069_revenue_growth_persistence_growth_126d_x_meanclose_base_v066_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 126)
    result = base * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_189d_x_meanclose base
def f069rgp_f069_revenue_growth_persistence_growth_189d_x_meanclose_base_v067_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 189)
    result = base * _mean(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_252d_x_meanclose base
def f069rgp_f069_revenue_growth_persistence_growth_252d_x_meanclose_base_v068_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 252)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_378d_x_meanclose base
def f069rgp_f069_revenue_growth_persistence_growth_378d_x_meanclose_base_v069_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 378)
    result = base * _mean(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_504d_x_meanclose base
def f069rgp_f069_revenue_growth_persistence_growth_504d_x_meanclose_base_v070_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 504)
    result = base * _mean(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_5d_x_meanclose base
def f069rgp_f069_revenue_growth_persistence_accel_5d_x_meanclose_base_v071_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 5)
    result = base * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_10d_x_meanclose base
def f069rgp_f069_revenue_growth_persistence_accel_10d_x_meanclose_base_v072_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 10)
    result = base * _mean(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_21d_x_meanclose base
def f069rgp_f069_revenue_growth_persistence_accel_21d_x_meanclose_base_v073_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 21)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_42d_x_meanclose base
def f069rgp_f069_revenue_growth_persistence_accel_42d_x_meanclose_base_v074_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 42)
    result = base * _mean(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_63d_x_meanclose base
def f069rgp_f069_revenue_growth_persistence_accel_63d_x_meanclose_base_v075_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f069rgp_f069_revenue_growth_persistence_growth_5d_x_close_base_v001_signal,
    f069rgp_f069_revenue_growth_persistence_growth_10d_x_close_base_v002_signal,
    f069rgp_f069_revenue_growth_persistence_growth_21d_x_close_base_v003_signal,
    f069rgp_f069_revenue_growth_persistence_growth_42d_x_close_base_v004_signal,
    f069rgp_f069_revenue_growth_persistence_growth_63d_x_close_base_v005_signal,
    f069rgp_f069_revenue_growth_persistence_growth_126d_x_close_base_v006_signal,
    f069rgp_f069_revenue_growth_persistence_growth_189d_x_close_base_v007_signal,
    f069rgp_f069_revenue_growth_persistence_growth_252d_x_close_base_v008_signal,
    f069rgp_f069_revenue_growth_persistence_growth_378d_x_close_base_v009_signal,
    f069rgp_f069_revenue_growth_persistence_growth_504d_x_close_base_v010_signal,
    f069rgp_f069_revenue_growth_persistence_accel_5d_x_close_base_v011_signal,
    f069rgp_f069_revenue_growth_persistence_accel_10d_x_close_base_v012_signal,
    f069rgp_f069_revenue_growth_persistence_accel_21d_x_close_base_v013_signal,
    f069rgp_f069_revenue_growth_persistence_accel_42d_x_close_base_v014_signal,
    f069rgp_f069_revenue_growth_persistence_accel_63d_x_close_base_v015_signal,
    f069rgp_f069_revenue_growth_persistence_accel_126d_x_close_base_v016_signal,
    f069rgp_f069_revenue_growth_persistence_accel_189d_x_close_base_v017_signal,
    f069rgp_f069_revenue_growth_persistence_accel_252d_x_close_base_v018_signal,
    f069rgp_f069_revenue_growth_persistence_accel_378d_x_close_base_v019_signal,
    f069rgp_f069_revenue_growth_persistence_accel_504d_x_close_base_v020_signal,
    f069rgp_f069_revenue_growth_persistence_persist_5d_x_close_base_v021_signal,
    f069rgp_f069_revenue_growth_persistence_persist_10d_x_close_base_v022_signal,
    f069rgp_f069_revenue_growth_persistence_persist_21d_x_close_base_v023_signal,
    f069rgp_f069_revenue_growth_persistence_persist_42d_x_close_base_v024_signal,
    f069rgp_f069_revenue_growth_persistence_persist_63d_x_close_base_v025_signal,
    f069rgp_f069_revenue_growth_persistence_persist_126d_x_close_base_v026_signal,
    f069rgp_f069_revenue_growth_persistence_persist_189d_x_close_base_v027_signal,
    f069rgp_f069_revenue_growth_persistence_persist_252d_x_close_base_v028_signal,
    f069rgp_f069_revenue_growth_persistence_persist_378d_x_close_base_v029_signal,
    f069rgp_f069_revenue_growth_persistence_persist_504d_x_close_base_v030_signal,
    f069rgp_f069_revenue_growth_persistence_growth_5d_x_logclose_base_v031_signal,
    f069rgp_f069_revenue_growth_persistence_growth_10d_x_logclose_base_v032_signal,
    f069rgp_f069_revenue_growth_persistence_growth_21d_x_logclose_base_v033_signal,
    f069rgp_f069_revenue_growth_persistence_growth_42d_x_logclose_base_v034_signal,
    f069rgp_f069_revenue_growth_persistence_growth_63d_x_logclose_base_v035_signal,
    f069rgp_f069_revenue_growth_persistence_growth_126d_x_logclose_base_v036_signal,
    f069rgp_f069_revenue_growth_persistence_growth_189d_x_logclose_base_v037_signal,
    f069rgp_f069_revenue_growth_persistence_growth_252d_x_logclose_base_v038_signal,
    f069rgp_f069_revenue_growth_persistence_growth_378d_x_logclose_base_v039_signal,
    f069rgp_f069_revenue_growth_persistence_growth_504d_x_logclose_base_v040_signal,
    f069rgp_f069_revenue_growth_persistence_accel_5d_x_logclose_base_v041_signal,
    f069rgp_f069_revenue_growth_persistence_accel_10d_x_logclose_base_v042_signal,
    f069rgp_f069_revenue_growth_persistence_accel_21d_x_logclose_base_v043_signal,
    f069rgp_f069_revenue_growth_persistence_accel_42d_x_logclose_base_v044_signal,
    f069rgp_f069_revenue_growth_persistence_accel_63d_x_logclose_base_v045_signal,
    f069rgp_f069_revenue_growth_persistence_accel_126d_x_logclose_base_v046_signal,
    f069rgp_f069_revenue_growth_persistence_accel_189d_x_logclose_base_v047_signal,
    f069rgp_f069_revenue_growth_persistence_accel_252d_x_logclose_base_v048_signal,
    f069rgp_f069_revenue_growth_persistence_accel_378d_x_logclose_base_v049_signal,
    f069rgp_f069_revenue_growth_persistence_accel_504d_x_logclose_base_v050_signal,
    f069rgp_f069_revenue_growth_persistence_persist_5d_x_logclose_base_v051_signal,
    f069rgp_f069_revenue_growth_persistence_persist_10d_x_logclose_base_v052_signal,
    f069rgp_f069_revenue_growth_persistence_persist_21d_x_logclose_base_v053_signal,
    f069rgp_f069_revenue_growth_persistence_persist_42d_x_logclose_base_v054_signal,
    f069rgp_f069_revenue_growth_persistence_persist_63d_x_logclose_base_v055_signal,
    f069rgp_f069_revenue_growth_persistence_persist_126d_x_logclose_base_v056_signal,
    f069rgp_f069_revenue_growth_persistence_persist_189d_x_logclose_base_v057_signal,
    f069rgp_f069_revenue_growth_persistence_persist_252d_x_logclose_base_v058_signal,
    f069rgp_f069_revenue_growth_persistence_persist_378d_x_logclose_base_v059_signal,
    f069rgp_f069_revenue_growth_persistence_persist_504d_x_logclose_base_v060_signal,
    f069rgp_f069_revenue_growth_persistence_growth_5d_x_meanclose_base_v061_signal,
    f069rgp_f069_revenue_growth_persistence_growth_10d_x_meanclose_base_v062_signal,
    f069rgp_f069_revenue_growth_persistence_growth_21d_x_meanclose_base_v063_signal,
    f069rgp_f069_revenue_growth_persistence_growth_42d_x_meanclose_base_v064_signal,
    f069rgp_f069_revenue_growth_persistence_growth_63d_x_meanclose_base_v065_signal,
    f069rgp_f069_revenue_growth_persistence_growth_126d_x_meanclose_base_v066_signal,
    f069rgp_f069_revenue_growth_persistence_growth_189d_x_meanclose_base_v067_signal,
    f069rgp_f069_revenue_growth_persistence_growth_252d_x_meanclose_base_v068_signal,
    f069rgp_f069_revenue_growth_persistence_growth_378d_x_meanclose_base_v069_signal,
    f069rgp_f069_revenue_growth_persistence_growth_504d_x_meanclose_base_v070_signal,
    f069rgp_f069_revenue_growth_persistence_accel_5d_x_meanclose_base_v071_signal,
    f069rgp_f069_revenue_growth_persistence_accel_10d_x_meanclose_base_v072_signal,
    f069rgp_f069_revenue_growth_persistence_accel_21d_x_meanclose_base_v073_signal,
    f069rgp_f069_revenue_growth_persistence_accel_42d_x_meanclose_base_v074_signal,
    f069rgp_f069_revenue_growth_persistence_accel_63d_x_meanclose_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F069_REVENUE_GROWTH_PERSISTENCE_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="revenue")
    cols = {
        "closeadj": closeadj,
        "revenue": revenue,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f069_growth_rate', '_f069_consec_accelerating', '_f069_persistence_count')
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
    print(f"OK f069_revenue_growth_persistence_base_001_075_claude: {n_features} features pass")
