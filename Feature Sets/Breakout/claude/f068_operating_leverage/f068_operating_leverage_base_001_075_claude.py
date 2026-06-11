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
def _f068_revenue_growth(revenue, w):
    return revenue.pct_change(periods=w)


def _f068_opex_growth(opex, w):
    return opex.pct_change(periods=w)


def _f068_operating_leverage(revenue, opex, w):
    # gap between revenue growth and opex growth — operating leverage
    rg = revenue.pct_change(periods=w)
    og = opex.pct_change(periods=w)
    return rg - og


# revgrow_5d_x_close base
def f068opl_f068_operating_leverage_revgrow_5d_x_close_base_v001_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_10d_x_close base
def f068opl_f068_operating_leverage_revgrow_10d_x_close_base_v002_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_21d_x_close base
def f068opl_f068_operating_leverage_revgrow_21d_x_close_base_v003_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_42d_x_close base
def f068opl_f068_operating_leverage_revgrow_42d_x_close_base_v004_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_63d_x_close base
def f068opl_f068_operating_leverage_revgrow_63d_x_close_base_v005_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_126d_x_close base
def f068opl_f068_operating_leverage_revgrow_126d_x_close_base_v006_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_189d_x_close base
def f068opl_f068_operating_leverage_revgrow_189d_x_close_base_v007_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_252d_x_close base
def f068opl_f068_operating_leverage_revgrow_252d_x_close_base_v008_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_378d_x_close base
def f068opl_f068_operating_leverage_revgrow_378d_x_close_base_v009_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_504d_x_close base
def f068opl_f068_operating_leverage_revgrow_504d_x_close_base_v010_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_5d_x_close base
def f068opl_f068_operating_leverage_opexgrow_5d_x_close_base_v011_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_10d_x_close base
def f068opl_f068_operating_leverage_opexgrow_10d_x_close_base_v012_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_21d_x_close base
def f068opl_f068_operating_leverage_opexgrow_21d_x_close_base_v013_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_42d_x_close base
def f068opl_f068_operating_leverage_opexgrow_42d_x_close_base_v014_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_63d_x_close base
def f068opl_f068_operating_leverage_opexgrow_63d_x_close_base_v015_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_126d_x_close base
def f068opl_f068_operating_leverage_opexgrow_126d_x_close_base_v016_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_189d_x_close base
def f068opl_f068_operating_leverage_opexgrow_189d_x_close_base_v017_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_252d_x_close base
def f068opl_f068_operating_leverage_opexgrow_252d_x_close_base_v018_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_378d_x_close base
def f068opl_f068_operating_leverage_opexgrow_378d_x_close_base_v019_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_504d_x_close base
def f068opl_f068_operating_leverage_opexgrow_504d_x_close_base_v020_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_5d_x_close base
def f068opl_f068_operating_leverage_oplev_5d_x_close_base_v021_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_10d_x_close base
def f068opl_f068_operating_leverage_oplev_10d_x_close_base_v022_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_21d_x_close base
def f068opl_f068_operating_leverage_oplev_21d_x_close_base_v023_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_42d_x_close base
def f068opl_f068_operating_leverage_oplev_42d_x_close_base_v024_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_63d_x_close base
def f068opl_f068_operating_leverage_oplev_63d_x_close_base_v025_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_126d_x_close base
def f068opl_f068_operating_leverage_oplev_126d_x_close_base_v026_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_189d_x_close base
def f068opl_f068_operating_leverage_oplev_189d_x_close_base_v027_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_252d_x_close base
def f068opl_f068_operating_leverage_oplev_252d_x_close_base_v028_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_378d_x_close base
def f068opl_f068_operating_leverage_oplev_378d_x_close_base_v029_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_504d_x_close base
def f068opl_f068_operating_leverage_oplev_504d_x_close_base_v030_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_5d_x_logclose base
def f068opl_f068_operating_leverage_revgrow_5d_x_logclose_base_v031_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 5)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_10d_x_logclose base
def f068opl_f068_operating_leverage_revgrow_10d_x_logclose_base_v032_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 10)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_21d_x_logclose base
def f068opl_f068_operating_leverage_revgrow_21d_x_logclose_base_v033_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 21)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_42d_x_logclose base
def f068opl_f068_operating_leverage_revgrow_42d_x_logclose_base_v034_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 42)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_63d_x_logclose base
def f068opl_f068_operating_leverage_revgrow_63d_x_logclose_base_v035_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 63)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_126d_x_logclose base
def f068opl_f068_operating_leverage_revgrow_126d_x_logclose_base_v036_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 126)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_189d_x_logclose base
def f068opl_f068_operating_leverage_revgrow_189d_x_logclose_base_v037_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 189)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_252d_x_logclose base
def f068opl_f068_operating_leverage_revgrow_252d_x_logclose_base_v038_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 252)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_378d_x_logclose base
def f068opl_f068_operating_leverage_revgrow_378d_x_logclose_base_v039_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 378)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_504d_x_logclose base
def f068opl_f068_operating_leverage_revgrow_504d_x_logclose_base_v040_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 504)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_5d_x_logclose base
def f068opl_f068_operating_leverage_opexgrow_5d_x_logclose_base_v041_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 5)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_10d_x_logclose base
def f068opl_f068_operating_leverage_opexgrow_10d_x_logclose_base_v042_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 10)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_21d_x_logclose base
def f068opl_f068_operating_leverage_opexgrow_21d_x_logclose_base_v043_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 21)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_42d_x_logclose base
def f068opl_f068_operating_leverage_opexgrow_42d_x_logclose_base_v044_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 42)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_63d_x_logclose base
def f068opl_f068_operating_leverage_opexgrow_63d_x_logclose_base_v045_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 63)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_126d_x_logclose base
def f068opl_f068_operating_leverage_opexgrow_126d_x_logclose_base_v046_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 126)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_189d_x_logclose base
def f068opl_f068_operating_leverage_opexgrow_189d_x_logclose_base_v047_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 189)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_252d_x_logclose base
def f068opl_f068_operating_leverage_opexgrow_252d_x_logclose_base_v048_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 252)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_378d_x_logclose base
def f068opl_f068_operating_leverage_opexgrow_378d_x_logclose_base_v049_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 378)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_504d_x_logclose base
def f068opl_f068_operating_leverage_opexgrow_504d_x_logclose_base_v050_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 504)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_5d_x_logclose base
def f068opl_f068_operating_leverage_oplev_5d_x_logclose_base_v051_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 5)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_10d_x_logclose base
def f068opl_f068_operating_leverage_oplev_10d_x_logclose_base_v052_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 10)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_21d_x_logclose base
def f068opl_f068_operating_leverage_oplev_21d_x_logclose_base_v053_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 21)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_42d_x_logclose base
def f068opl_f068_operating_leverage_oplev_42d_x_logclose_base_v054_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 42)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_63d_x_logclose base
def f068opl_f068_operating_leverage_oplev_63d_x_logclose_base_v055_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 63)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_126d_x_logclose base
def f068opl_f068_operating_leverage_oplev_126d_x_logclose_base_v056_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 126)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_189d_x_logclose base
def f068opl_f068_operating_leverage_oplev_189d_x_logclose_base_v057_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 189)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_252d_x_logclose base
def f068opl_f068_operating_leverage_oplev_252d_x_logclose_base_v058_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 252)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_378d_x_logclose base
def f068opl_f068_operating_leverage_oplev_378d_x_logclose_base_v059_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 378)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_504d_x_logclose base
def f068opl_f068_operating_leverage_oplev_504d_x_logclose_base_v060_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 504)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_5d_x_meanclose base
def f068opl_f068_operating_leverage_revgrow_5d_x_meanclose_base_v061_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 5)
    result = base * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_10d_x_meanclose base
def f068opl_f068_operating_leverage_revgrow_10d_x_meanclose_base_v062_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 10)
    result = base * _mean(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_21d_x_meanclose base
def f068opl_f068_operating_leverage_revgrow_21d_x_meanclose_base_v063_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 21)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_42d_x_meanclose base
def f068opl_f068_operating_leverage_revgrow_42d_x_meanclose_base_v064_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 42)
    result = base * _mean(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_63d_x_meanclose base
def f068opl_f068_operating_leverage_revgrow_63d_x_meanclose_base_v065_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_126d_x_meanclose base
def f068opl_f068_operating_leverage_revgrow_126d_x_meanclose_base_v066_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 126)
    result = base * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_189d_x_meanclose base
def f068opl_f068_operating_leverage_revgrow_189d_x_meanclose_base_v067_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 189)
    result = base * _mean(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_252d_x_meanclose base
def f068opl_f068_operating_leverage_revgrow_252d_x_meanclose_base_v068_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 252)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_378d_x_meanclose base
def f068opl_f068_operating_leverage_revgrow_378d_x_meanclose_base_v069_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 378)
    result = base * _mean(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_504d_x_meanclose base
def f068opl_f068_operating_leverage_revgrow_504d_x_meanclose_base_v070_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 504)
    result = base * _mean(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_5d_x_meanclose base
def f068opl_f068_operating_leverage_opexgrow_5d_x_meanclose_base_v071_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 5)
    result = base * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_10d_x_meanclose base
def f068opl_f068_operating_leverage_opexgrow_10d_x_meanclose_base_v072_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 10)
    result = base * _mean(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_21d_x_meanclose base
def f068opl_f068_operating_leverage_opexgrow_21d_x_meanclose_base_v073_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 21)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_42d_x_meanclose base
def f068opl_f068_operating_leverage_opexgrow_42d_x_meanclose_base_v074_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 42)
    result = base * _mean(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_63d_x_meanclose base
def f068opl_f068_operating_leverage_opexgrow_63d_x_meanclose_base_v075_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f068opl_f068_operating_leverage_revgrow_5d_x_close_base_v001_signal,
    f068opl_f068_operating_leverage_revgrow_10d_x_close_base_v002_signal,
    f068opl_f068_operating_leverage_revgrow_21d_x_close_base_v003_signal,
    f068opl_f068_operating_leverage_revgrow_42d_x_close_base_v004_signal,
    f068opl_f068_operating_leverage_revgrow_63d_x_close_base_v005_signal,
    f068opl_f068_operating_leverage_revgrow_126d_x_close_base_v006_signal,
    f068opl_f068_operating_leverage_revgrow_189d_x_close_base_v007_signal,
    f068opl_f068_operating_leverage_revgrow_252d_x_close_base_v008_signal,
    f068opl_f068_operating_leverage_revgrow_378d_x_close_base_v009_signal,
    f068opl_f068_operating_leverage_revgrow_504d_x_close_base_v010_signal,
    f068opl_f068_operating_leverage_opexgrow_5d_x_close_base_v011_signal,
    f068opl_f068_operating_leverage_opexgrow_10d_x_close_base_v012_signal,
    f068opl_f068_operating_leverage_opexgrow_21d_x_close_base_v013_signal,
    f068opl_f068_operating_leverage_opexgrow_42d_x_close_base_v014_signal,
    f068opl_f068_operating_leverage_opexgrow_63d_x_close_base_v015_signal,
    f068opl_f068_operating_leverage_opexgrow_126d_x_close_base_v016_signal,
    f068opl_f068_operating_leverage_opexgrow_189d_x_close_base_v017_signal,
    f068opl_f068_operating_leverage_opexgrow_252d_x_close_base_v018_signal,
    f068opl_f068_operating_leverage_opexgrow_378d_x_close_base_v019_signal,
    f068opl_f068_operating_leverage_opexgrow_504d_x_close_base_v020_signal,
    f068opl_f068_operating_leverage_oplev_5d_x_close_base_v021_signal,
    f068opl_f068_operating_leverage_oplev_10d_x_close_base_v022_signal,
    f068opl_f068_operating_leverage_oplev_21d_x_close_base_v023_signal,
    f068opl_f068_operating_leverage_oplev_42d_x_close_base_v024_signal,
    f068opl_f068_operating_leverage_oplev_63d_x_close_base_v025_signal,
    f068opl_f068_operating_leverage_oplev_126d_x_close_base_v026_signal,
    f068opl_f068_operating_leverage_oplev_189d_x_close_base_v027_signal,
    f068opl_f068_operating_leverage_oplev_252d_x_close_base_v028_signal,
    f068opl_f068_operating_leverage_oplev_378d_x_close_base_v029_signal,
    f068opl_f068_operating_leverage_oplev_504d_x_close_base_v030_signal,
    f068opl_f068_operating_leverage_revgrow_5d_x_logclose_base_v031_signal,
    f068opl_f068_operating_leverage_revgrow_10d_x_logclose_base_v032_signal,
    f068opl_f068_operating_leverage_revgrow_21d_x_logclose_base_v033_signal,
    f068opl_f068_operating_leverage_revgrow_42d_x_logclose_base_v034_signal,
    f068opl_f068_operating_leverage_revgrow_63d_x_logclose_base_v035_signal,
    f068opl_f068_operating_leverage_revgrow_126d_x_logclose_base_v036_signal,
    f068opl_f068_operating_leverage_revgrow_189d_x_logclose_base_v037_signal,
    f068opl_f068_operating_leverage_revgrow_252d_x_logclose_base_v038_signal,
    f068opl_f068_operating_leverage_revgrow_378d_x_logclose_base_v039_signal,
    f068opl_f068_operating_leverage_revgrow_504d_x_logclose_base_v040_signal,
    f068opl_f068_operating_leverage_opexgrow_5d_x_logclose_base_v041_signal,
    f068opl_f068_operating_leverage_opexgrow_10d_x_logclose_base_v042_signal,
    f068opl_f068_operating_leverage_opexgrow_21d_x_logclose_base_v043_signal,
    f068opl_f068_operating_leverage_opexgrow_42d_x_logclose_base_v044_signal,
    f068opl_f068_operating_leverage_opexgrow_63d_x_logclose_base_v045_signal,
    f068opl_f068_operating_leverage_opexgrow_126d_x_logclose_base_v046_signal,
    f068opl_f068_operating_leverage_opexgrow_189d_x_logclose_base_v047_signal,
    f068opl_f068_operating_leverage_opexgrow_252d_x_logclose_base_v048_signal,
    f068opl_f068_operating_leverage_opexgrow_378d_x_logclose_base_v049_signal,
    f068opl_f068_operating_leverage_opexgrow_504d_x_logclose_base_v050_signal,
    f068opl_f068_operating_leverage_oplev_5d_x_logclose_base_v051_signal,
    f068opl_f068_operating_leverage_oplev_10d_x_logclose_base_v052_signal,
    f068opl_f068_operating_leverage_oplev_21d_x_logclose_base_v053_signal,
    f068opl_f068_operating_leverage_oplev_42d_x_logclose_base_v054_signal,
    f068opl_f068_operating_leverage_oplev_63d_x_logclose_base_v055_signal,
    f068opl_f068_operating_leverage_oplev_126d_x_logclose_base_v056_signal,
    f068opl_f068_operating_leverage_oplev_189d_x_logclose_base_v057_signal,
    f068opl_f068_operating_leverage_oplev_252d_x_logclose_base_v058_signal,
    f068opl_f068_operating_leverage_oplev_378d_x_logclose_base_v059_signal,
    f068opl_f068_operating_leverage_oplev_504d_x_logclose_base_v060_signal,
    f068opl_f068_operating_leverage_revgrow_5d_x_meanclose_base_v061_signal,
    f068opl_f068_operating_leverage_revgrow_10d_x_meanclose_base_v062_signal,
    f068opl_f068_operating_leverage_revgrow_21d_x_meanclose_base_v063_signal,
    f068opl_f068_operating_leverage_revgrow_42d_x_meanclose_base_v064_signal,
    f068opl_f068_operating_leverage_revgrow_63d_x_meanclose_base_v065_signal,
    f068opl_f068_operating_leverage_revgrow_126d_x_meanclose_base_v066_signal,
    f068opl_f068_operating_leverage_revgrow_189d_x_meanclose_base_v067_signal,
    f068opl_f068_operating_leverage_revgrow_252d_x_meanclose_base_v068_signal,
    f068opl_f068_operating_leverage_revgrow_378d_x_meanclose_base_v069_signal,
    f068opl_f068_operating_leverage_revgrow_504d_x_meanclose_base_v070_signal,
    f068opl_f068_operating_leverage_opexgrow_5d_x_meanclose_base_v071_signal,
    f068opl_f068_operating_leverage_opexgrow_10d_x_meanclose_base_v072_signal,
    f068opl_f068_operating_leverage_opexgrow_21d_x_meanclose_base_v073_signal,
    f068opl_f068_operating_leverage_opexgrow_42d_x_meanclose_base_v074_signal,
    f068opl_f068_operating_leverage_opexgrow_63d_x_meanclose_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F068_OPERATING_LEVERAGE_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="revenue")
    opex = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="opex")
    cols = {
        "closeadj": closeadj,
        "revenue": revenue,
        "opex": opex,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f068_revenue_growth', '_f068_opex_growth', '_f068_operating_leverage')
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
    print(f"OK f068_operating_leverage_base_001_075_claude: {n_features} features pass")
