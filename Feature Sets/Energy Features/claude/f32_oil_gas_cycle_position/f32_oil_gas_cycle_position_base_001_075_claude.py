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

# ===== folder domain primitives =====
def _f32_revenue_cycle(revenue, w):
    m = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    mn = revenue.rolling(w, min_periods=max(1, w // 2)).min()
    mx = revenue.rolling(w, min_periods=max(1, w // 2)).max()
    return (revenue - m) / (mx - mn).replace(0, np.nan)

def _f32_margin_cycle_pos(ebitdamargin, w):
    mn = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).min()
    mx = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).max()
    return (ebitdamargin - mn) / (mx - mn).replace(0, np.nan)

def _f32_cycle_composite(revenue, ebitdamargin, w):
    rm = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    mm = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    z_r = (revenue - rm) / revenue.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)
    z_m = (ebitdamargin - mm) / ebitdamargin.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)
    return (z_r + z_m) / 2.0


def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xc_5d_base_v001_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc21_5d_base_v002_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 5)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc63_5d_base_v003_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 5)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc252_5d_base_v004_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 5)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xema21c_5d_base_v005_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 5)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xema63c_5d_base_v006_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 5)
    result = base * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xc_10d_base_v007_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc21_10d_base_v008_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 10)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc63_10d_base_v009_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 10)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc252_10d_base_v010_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 10)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xema21c_10d_base_v011_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 10)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xema63c_10d_base_v012_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 10)
    result = base * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xc_21d_base_v013_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc21_21d_base_v014_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 21)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc63_21d_base_v015_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc252_21d_base_v016_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 21)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xema21c_21d_base_v017_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 21)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xema63c_21d_base_v018_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 21)
    result = base * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xc_42d_base_v019_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc21_42d_base_v020_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 42)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc63_42d_base_v021_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 42)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc252_42d_base_v022_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 42)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xema21c_42d_base_v023_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 42)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xema63c_42d_base_v024_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 42)
    result = base * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xc_63d_base_v025_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc21_63d_base_v026_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 63)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc63_63d_base_v027_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc252_63d_base_v028_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 63)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xema21c_63d_base_v029_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 63)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xema63c_63d_base_v030_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 63)
    result = base * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xc_126d_base_v031_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc21_126d_base_v032_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 126)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc63_126d_base_v033_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 126)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc252_126d_base_v034_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 126)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xema21c_126d_base_v035_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 126)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xema63c_126d_base_v036_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 126)
    result = base * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xc_189d_base_v037_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc21_189d_base_v038_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 189)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc63_189d_base_v039_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 189)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc252_189d_base_v040_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 189)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xema21c_189d_base_v041_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 189)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xema63c_189d_base_v042_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 189)
    result = base * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xc_252d_base_v043_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc21_252d_base_v044_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 252)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc63_252d_base_v045_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 252)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc252_252d_base_v046_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 252)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xema21c_252d_base_v047_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 252)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xema63c_252d_base_v048_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 252)
    result = base * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xc_378d_base_v049_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc21_378d_base_v050_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 378)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc63_378d_base_v051_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 378)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc252_378d_base_v052_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 378)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xema21c_378d_base_v053_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 378)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xema63c_378d_base_v054_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 378)
    result = base * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xc_5d_base_v055_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 5)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xmc21_5d_base_v056_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 5)
    result = base.abs() * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xmc63_5d_base_v057_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 5)
    result = base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xmc252_5d_base_v058_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 5)
    result = base.abs() * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xema21c_5d_base_v059_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 5)
    result = base.abs() * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xema63c_5d_base_v060_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 5)
    result = base.abs() * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xc_10d_base_v061_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 10)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xmc21_10d_base_v062_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 10)
    result = base.abs() * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xmc63_10d_base_v063_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 10)
    result = base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xmc252_10d_base_v064_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 10)
    result = base.abs() * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xema21c_10d_base_v065_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 10)
    result = base.abs() * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xema63c_10d_base_v066_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 10)
    result = base.abs() * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xc_21d_base_v067_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xmc21_21d_base_v068_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 21)
    result = base.abs() * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xmc63_21d_base_v069_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 21)
    result = base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xmc252_21d_base_v070_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 21)
    result = base.abs() * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xema21c_21d_base_v071_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 21)
    result = base.abs() * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xema63c_21d_base_v072_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 21)
    result = base.abs() * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xc_42d_base_v073_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xmc21_42d_base_v074_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 42)
    result = base.abs() * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xmc63_42d_base_v075_signal(revenue, closeadj):
    base = _f32_revenue_cycle(revenue, 42)
    result = base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xc_5d_base_v001_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc21_5d_base_v002_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc63_5d_base_v003_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc252_5d_base_v004_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xema21c_5d_base_v005_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xema63c_5d_base_v006_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xc_10d_base_v007_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc21_10d_base_v008_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc63_10d_base_v009_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc252_10d_base_v010_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xema21c_10d_base_v011_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xema63c_10d_base_v012_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xc_21d_base_v013_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc21_21d_base_v014_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc63_21d_base_v015_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc252_21d_base_v016_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xema21c_21d_base_v017_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xema63c_21d_base_v018_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xc_42d_base_v019_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc21_42d_base_v020_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc63_42d_base_v021_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc252_42d_base_v022_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xema21c_42d_base_v023_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xema63c_42d_base_v024_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xc_63d_base_v025_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc21_63d_base_v026_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc63_63d_base_v027_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc252_63d_base_v028_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xema21c_63d_base_v029_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xema63c_63d_base_v030_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xc_126d_base_v031_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc21_126d_base_v032_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc63_126d_base_v033_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc252_126d_base_v034_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xema21c_126d_base_v035_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xema63c_126d_base_v036_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xc_189d_base_v037_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc21_189d_base_v038_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc63_189d_base_v039_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc252_189d_base_v040_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xema21c_189d_base_v041_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xema63c_189d_base_v042_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xc_252d_base_v043_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc21_252d_base_v044_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc63_252d_base_v045_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc252_252d_base_v046_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xema21c_252d_base_v047_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xema63c_252d_base_v048_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xc_378d_base_v049_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc21_378d_base_v050_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc63_378d_base_v051_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xmc252_378d_base_v052_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xema21c_378d_base_v053_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_ident_xema63c_378d_base_v054_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xc_5d_base_v055_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xmc21_5d_base_v056_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xmc63_5d_base_v057_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xmc252_5d_base_v058_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xema21c_5d_base_v059_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xema63c_5d_base_v060_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xc_10d_base_v061_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xmc21_10d_base_v062_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xmc63_10d_base_v063_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xmc252_10d_base_v064_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xema21c_10d_base_v065_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xema63c_10d_base_v066_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xc_21d_base_v067_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xmc21_21d_base_v068_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xmc63_21d_base_v069_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xmc252_21d_base_v070_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xema21c_21d_base_v071_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xema63c_21d_base_v072_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xc_42d_base_v073_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xmc21_42d_base_v074_signal,
    f32ogc_f32_oil_gas_cycle_position_revcyc_absv_xmc63_42d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F32_OIL_GAS_CYCLE_POSITION_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    debt    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    de = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")

    cols = {
        "closeadj": closeadj,
        "revenue": revenue,
        "ebitda": ebitda,
        "netinc": netinc,
        "fcf": fcf,
        "capex": capex,
        "debt": debt,
        "ebitdamargin": ebitdamargin,
        "de": de,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f32_revenue_cycle", "_f32_margin_cycle_pos", "_f32_cycle_composite",)
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
    print(f"OK f32_oil_gas_cycle_position_001_075_claude: {n_features} features pass")
