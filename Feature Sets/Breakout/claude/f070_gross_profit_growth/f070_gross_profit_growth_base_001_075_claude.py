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
def _f070_gp_yoy(gp, w):
    return gp.pct_change(periods=w)


def _f070_gp_acceleration(gp, w):
    # acceleration of gross profit growth
    sw = max(2, w // 4)
    short = gp.pct_change(periods=sw)
    long = gp.pct_change(periods=w)
    return short - long


def _f070_quality_growth(gp, revenue, w):
    # gp growth minus revenue growth — quality of growth (margin expansion)
    gg = gp.pct_change(periods=w)
    rg = revenue.pct_change(periods=w)
    return gg - rg


# gpyoy_5d_x_close base
def f070gpg_f070_gross_profit_growth_gpyoy_5d_x_close_base_v001_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_10d_x_close base
def f070gpg_f070_gross_profit_growth_gpyoy_10d_x_close_base_v002_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_21d_x_close base
def f070gpg_f070_gross_profit_growth_gpyoy_21d_x_close_base_v003_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_42d_x_close base
def f070gpg_f070_gross_profit_growth_gpyoy_42d_x_close_base_v004_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_63d_x_close base
def f070gpg_f070_gross_profit_growth_gpyoy_63d_x_close_base_v005_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_126d_x_close base
def f070gpg_f070_gross_profit_growth_gpyoy_126d_x_close_base_v006_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_189d_x_close base
def f070gpg_f070_gross_profit_growth_gpyoy_189d_x_close_base_v007_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_252d_x_close base
def f070gpg_f070_gross_profit_growth_gpyoy_252d_x_close_base_v008_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_378d_x_close base
def f070gpg_f070_gross_profit_growth_gpyoy_378d_x_close_base_v009_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_504d_x_close base
def f070gpg_f070_gross_profit_growth_gpyoy_504d_x_close_base_v010_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_5d_x_close base
def f070gpg_f070_gross_profit_growth_gpaccel_5d_x_close_base_v011_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_10d_x_close base
def f070gpg_f070_gross_profit_growth_gpaccel_10d_x_close_base_v012_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_21d_x_close base
def f070gpg_f070_gross_profit_growth_gpaccel_21d_x_close_base_v013_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_42d_x_close base
def f070gpg_f070_gross_profit_growth_gpaccel_42d_x_close_base_v014_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_63d_x_close base
def f070gpg_f070_gross_profit_growth_gpaccel_63d_x_close_base_v015_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_126d_x_close base
def f070gpg_f070_gross_profit_growth_gpaccel_126d_x_close_base_v016_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_189d_x_close base
def f070gpg_f070_gross_profit_growth_gpaccel_189d_x_close_base_v017_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_252d_x_close base
def f070gpg_f070_gross_profit_growth_gpaccel_252d_x_close_base_v018_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_378d_x_close base
def f070gpg_f070_gross_profit_growth_gpaccel_378d_x_close_base_v019_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_504d_x_close base
def f070gpg_f070_gross_profit_growth_gpaccel_504d_x_close_base_v020_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_5d_x_close base
def f070gpg_f070_gross_profit_growth_qualgrow_5d_x_close_base_v021_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_10d_x_close base
def f070gpg_f070_gross_profit_growth_qualgrow_10d_x_close_base_v022_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_21d_x_close base
def f070gpg_f070_gross_profit_growth_qualgrow_21d_x_close_base_v023_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_42d_x_close base
def f070gpg_f070_gross_profit_growth_qualgrow_42d_x_close_base_v024_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_63d_x_close base
def f070gpg_f070_gross_profit_growth_qualgrow_63d_x_close_base_v025_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_126d_x_close base
def f070gpg_f070_gross_profit_growth_qualgrow_126d_x_close_base_v026_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_189d_x_close base
def f070gpg_f070_gross_profit_growth_qualgrow_189d_x_close_base_v027_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_252d_x_close base
def f070gpg_f070_gross_profit_growth_qualgrow_252d_x_close_base_v028_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_378d_x_close base
def f070gpg_f070_gross_profit_growth_qualgrow_378d_x_close_base_v029_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_504d_x_close base
def f070gpg_f070_gross_profit_growth_qualgrow_504d_x_close_base_v030_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_5d_x_logclose base
def f070gpg_f070_gross_profit_growth_gpyoy_5d_x_logclose_base_v031_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 5)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_10d_x_logclose base
def f070gpg_f070_gross_profit_growth_gpyoy_10d_x_logclose_base_v032_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 10)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_21d_x_logclose base
def f070gpg_f070_gross_profit_growth_gpyoy_21d_x_logclose_base_v033_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 21)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_42d_x_logclose base
def f070gpg_f070_gross_profit_growth_gpyoy_42d_x_logclose_base_v034_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 42)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_63d_x_logclose base
def f070gpg_f070_gross_profit_growth_gpyoy_63d_x_logclose_base_v035_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 63)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_126d_x_logclose base
def f070gpg_f070_gross_profit_growth_gpyoy_126d_x_logclose_base_v036_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 126)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_189d_x_logclose base
def f070gpg_f070_gross_profit_growth_gpyoy_189d_x_logclose_base_v037_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 189)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_252d_x_logclose base
def f070gpg_f070_gross_profit_growth_gpyoy_252d_x_logclose_base_v038_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 252)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_378d_x_logclose base
def f070gpg_f070_gross_profit_growth_gpyoy_378d_x_logclose_base_v039_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 378)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_504d_x_logclose base
def f070gpg_f070_gross_profit_growth_gpyoy_504d_x_logclose_base_v040_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 504)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_5d_x_logclose base
def f070gpg_f070_gross_profit_growth_gpaccel_5d_x_logclose_base_v041_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 5)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_10d_x_logclose base
def f070gpg_f070_gross_profit_growth_gpaccel_10d_x_logclose_base_v042_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 10)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_21d_x_logclose base
def f070gpg_f070_gross_profit_growth_gpaccel_21d_x_logclose_base_v043_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 21)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_42d_x_logclose base
def f070gpg_f070_gross_profit_growth_gpaccel_42d_x_logclose_base_v044_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 42)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_63d_x_logclose base
def f070gpg_f070_gross_profit_growth_gpaccel_63d_x_logclose_base_v045_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 63)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_126d_x_logclose base
def f070gpg_f070_gross_profit_growth_gpaccel_126d_x_logclose_base_v046_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 126)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_189d_x_logclose base
def f070gpg_f070_gross_profit_growth_gpaccel_189d_x_logclose_base_v047_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 189)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_252d_x_logclose base
def f070gpg_f070_gross_profit_growth_gpaccel_252d_x_logclose_base_v048_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 252)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_378d_x_logclose base
def f070gpg_f070_gross_profit_growth_gpaccel_378d_x_logclose_base_v049_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 378)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_504d_x_logclose base
def f070gpg_f070_gross_profit_growth_gpaccel_504d_x_logclose_base_v050_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 504)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_5d_x_logclose base
def f070gpg_f070_gross_profit_growth_qualgrow_5d_x_logclose_base_v051_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 5)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_10d_x_logclose base
def f070gpg_f070_gross_profit_growth_qualgrow_10d_x_logclose_base_v052_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 10)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_21d_x_logclose base
def f070gpg_f070_gross_profit_growth_qualgrow_21d_x_logclose_base_v053_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 21)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_42d_x_logclose base
def f070gpg_f070_gross_profit_growth_qualgrow_42d_x_logclose_base_v054_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 42)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_63d_x_logclose base
def f070gpg_f070_gross_profit_growth_qualgrow_63d_x_logclose_base_v055_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 63)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_126d_x_logclose base
def f070gpg_f070_gross_profit_growth_qualgrow_126d_x_logclose_base_v056_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 126)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_189d_x_logclose base
def f070gpg_f070_gross_profit_growth_qualgrow_189d_x_logclose_base_v057_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 189)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_252d_x_logclose base
def f070gpg_f070_gross_profit_growth_qualgrow_252d_x_logclose_base_v058_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 252)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_378d_x_logclose base
def f070gpg_f070_gross_profit_growth_qualgrow_378d_x_logclose_base_v059_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 378)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_504d_x_logclose base
def f070gpg_f070_gross_profit_growth_qualgrow_504d_x_logclose_base_v060_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 504)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_5d_x_meanclose base
def f070gpg_f070_gross_profit_growth_gpyoy_5d_x_meanclose_base_v061_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 5)
    result = base * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_10d_x_meanclose base
def f070gpg_f070_gross_profit_growth_gpyoy_10d_x_meanclose_base_v062_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 10)
    result = base * _mean(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_21d_x_meanclose base
def f070gpg_f070_gross_profit_growth_gpyoy_21d_x_meanclose_base_v063_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 21)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_42d_x_meanclose base
def f070gpg_f070_gross_profit_growth_gpyoy_42d_x_meanclose_base_v064_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 42)
    result = base * _mean(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_63d_x_meanclose base
def f070gpg_f070_gross_profit_growth_gpyoy_63d_x_meanclose_base_v065_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_126d_x_meanclose base
def f070gpg_f070_gross_profit_growth_gpyoy_126d_x_meanclose_base_v066_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 126)
    result = base * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_189d_x_meanclose base
def f070gpg_f070_gross_profit_growth_gpyoy_189d_x_meanclose_base_v067_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 189)
    result = base * _mean(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_252d_x_meanclose base
def f070gpg_f070_gross_profit_growth_gpyoy_252d_x_meanclose_base_v068_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 252)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_378d_x_meanclose base
def f070gpg_f070_gross_profit_growth_gpyoy_378d_x_meanclose_base_v069_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 378)
    result = base * _mean(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_504d_x_meanclose base
def f070gpg_f070_gross_profit_growth_gpyoy_504d_x_meanclose_base_v070_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 504)
    result = base * _mean(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_5d_x_meanclose base
def f070gpg_f070_gross_profit_growth_gpaccel_5d_x_meanclose_base_v071_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 5)
    result = base * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_10d_x_meanclose base
def f070gpg_f070_gross_profit_growth_gpaccel_10d_x_meanclose_base_v072_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 10)
    result = base * _mean(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_21d_x_meanclose base
def f070gpg_f070_gross_profit_growth_gpaccel_21d_x_meanclose_base_v073_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 21)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_42d_x_meanclose base
def f070gpg_f070_gross_profit_growth_gpaccel_42d_x_meanclose_base_v074_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 42)
    result = base * _mean(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_63d_x_meanclose base
def f070gpg_f070_gross_profit_growth_gpaccel_63d_x_meanclose_base_v075_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f070gpg_f070_gross_profit_growth_gpyoy_5d_x_close_base_v001_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_10d_x_close_base_v002_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_21d_x_close_base_v003_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_42d_x_close_base_v004_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_63d_x_close_base_v005_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_126d_x_close_base_v006_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_189d_x_close_base_v007_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_252d_x_close_base_v008_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_378d_x_close_base_v009_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_504d_x_close_base_v010_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_5d_x_close_base_v011_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_10d_x_close_base_v012_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_21d_x_close_base_v013_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_42d_x_close_base_v014_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_63d_x_close_base_v015_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_126d_x_close_base_v016_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_189d_x_close_base_v017_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_252d_x_close_base_v018_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_378d_x_close_base_v019_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_504d_x_close_base_v020_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_5d_x_close_base_v021_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_10d_x_close_base_v022_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_21d_x_close_base_v023_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_42d_x_close_base_v024_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_63d_x_close_base_v025_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_126d_x_close_base_v026_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_189d_x_close_base_v027_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_252d_x_close_base_v028_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_378d_x_close_base_v029_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_504d_x_close_base_v030_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_5d_x_logclose_base_v031_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_10d_x_logclose_base_v032_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_21d_x_logclose_base_v033_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_42d_x_logclose_base_v034_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_63d_x_logclose_base_v035_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_126d_x_logclose_base_v036_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_189d_x_logclose_base_v037_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_252d_x_logclose_base_v038_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_378d_x_logclose_base_v039_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_504d_x_logclose_base_v040_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_5d_x_logclose_base_v041_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_10d_x_logclose_base_v042_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_21d_x_logclose_base_v043_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_42d_x_logclose_base_v044_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_63d_x_logclose_base_v045_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_126d_x_logclose_base_v046_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_189d_x_logclose_base_v047_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_252d_x_logclose_base_v048_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_378d_x_logclose_base_v049_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_504d_x_logclose_base_v050_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_5d_x_logclose_base_v051_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_10d_x_logclose_base_v052_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_21d_x_logclose_base_v053_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_42d_x_logclose_base_v054_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_63d_x_logclose_base_v055_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_126d_x_logclose_base_v056_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_189d_x_logclose_base_v057_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_252d_x_logclose_base_v058_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_378d_x_logclose_base_v059_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_504d_x_logclose_base_v060_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_5d_x_meanclose_base_v061_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_10d_x_meanclose_base_v062_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_21d_x_meanclose_base_v063_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_42d_x_meanclose_base_v064_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_63d_x_meanclose_base_v065_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_126d_x_meanclose_base_v066_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_189d_x_meanclose_base_v067_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_252d_x_meanclose_base_v068_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_378d_x_meanclose_base_v069_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_504d_x_meanclose_base_v070_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_5d_x_meanclose_base_v071_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_10d_x_meanclose_base_v072_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_21d_x_meanclose_base_v073_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_42d_x_meanclose_base_v074_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_63d_x_meanclose_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F070_GROSS_PROFIT_GROWTH_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    gp = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.007, n))), name="gp")
    revenue = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="revenue")
    cols = {
        "closeadj": closeadj,
        "gp": gp,
        "revenue": revenue,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f070_gp_yoy', '_f070_gp_acceleration', '_f070_quality_growth')
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
    print(f"OK f070_gross_profit_growth_base_001_075_claude: {n_features} features pass")
