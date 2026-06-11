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


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _logret(s, w):
    return np.log(s.replace(0, np.nan)).diff(periods=w)


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _f06_capital_ratio(equity, assets):
    return equity / assets.replace(0, np.nan)


def _f06_capital_dynamics(equity, assets, w):
    cr = equity / assets.replace(0, np.nan)
    return cr.rolling(w, min_periods=max(1, w // 2)).mean()


def _f06_capital_buffer(equity, debt, w):
    buf = equity / (equity + debt).replace(0, np.nan)
    return buf.rolling(w, min_periods=max(1, w // 2)).mean()


def f06bca_f06_bank_capital_adequacy_capratio_5d_slope_v001_signal(equity, assets, closeadj):
    base = _f06_capital_ratio(equity, assets) * _mean(closeadj, 5)
    base_series = base
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_10d_slope_v002_signal(equity, assets, closeadj):
    base = _f06_capital_ratio(equity, assets) * _mean(closeadj, 10)
    base_series = base
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_21d_slope_v003_signal(equity, assets, closeadj):
    base = _f06_capital_ratio(equity, assets) * _mean(closeadj, 21)
    base_series = base
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_42d_slope_v004_signal(equity, assets, closeadj):
    base = _f06_capital_ratio(equity, assets) * _mean(closeadj, 42)
    base_series = base
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_63d_slope_v005_signal(equity, assets, closeadj):
    base = _f06_capital_ratio(equity, assets) * _mean(closeadj, 63)
    base_series = base
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_126d_slope_v006_signal(equity, assets, closeadj):
    base = _f06_capital_ratio(equity, assets) * _mean(closeadj, 126)
    base_series = base
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_189d_slope_v007_signal(equity, assets, closeadj):
    base = _f06_capital_ratio(equity, assets) * _mean(closeadj, 189)
    base_series = base
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_252d_slope_v008_signal(equity, assets, closeadj):
    base = _f06_capital_ratio(equity, assets) * _mean(closeadj, 252)
    base_series = base
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_378d_slope_v009_signal(equity, assets, closeadj):
    base = _f06_capital_ratio(equity, assets) * _mean(closeadj, 378)
    base_series = base
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_504d_slope_v010_signal(equity, assets, closeadj):
    base = _f06_capital_ratio(equity, assets) * _mean(closeadj, 504)
    base_series = base
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdyn_5d_slope_v011_signal(equity, assets, closeadj):
    base = _f06_capital_dynamics(equity, assets, 5) * closeadj
    base_series = base
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdyn_10d_slope_v012_signal(equity, assets, closeadj):
    base = _f06_capital_dynamics(equity, assets, 10) * closeadj
    base_series = base
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdyn_21d_slope_v013_signal(equity, assets, closeadj):
    base = _f06_capital_dynamics(equity, assets, 21) * closeadj
    base_series = base
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdyn_42d_slope_v014_signal(equity, assets, closeadj):
    base = _f06_capital_dynamics(equity, assets, 42) * closeadj
    base_series = base
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdyn_63d_slope_v015_signal(equity, assets, closeadj):
    base = _f06_capital_dynamics(equity, assets, 63) * closeadj
    base_series = base
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdyn_126d_slope_v016_signal(equity, assets, closeadj):
    base = _f06_capital_dynamics(equity, assets, 126) * closeadj
    base_series = base
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdyn_189d_slope_v017_signal(equity, assets, closeadj):
    base = _f06_capital_dynamics(equity, assets, 189) * closeadj
    base_series = base
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdyn_252d_slope_v018_signal(equity, assets, closeadj):
    base = _f06_capital_dynamics(equity, assets, 252) * closeadj
    base_series = base
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdyn_378d_slope_v019_signal(equity, assets, closeadj):
    base = _f06_capital_dynamics(equity, assets, 378) * closeadj
    base_series = base
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdyn_504d_slope_v020_signal(equity, assets, closeadj):
    base = _f06_capital_dynamics(equity, assets, 504) * closeadj
    base_series = base
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_5d_slope_v021_signal(equity, debt, closeadj):
    base = _f06_capital_buffer(equity, debt, 5) * closeadj
    base_series = base
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_10d_slope_v022_signal(equity, debt, closeadj):
    base = _f06_capital_buffer(equity, debt, 10) * closeadj
    base_series = base
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_21d_slope_v023_signal(equity, debt, closeadj):
    base = _f06_capital_buffer(equity, debt, 21) * closeadj
    base_series = base
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_42d_slope_v024_signal(equity, debt, closeadj):
    base = _f06_capital_buffer(equity, debt, 42) * closeadj
    base_series = base
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_63d_slope_v025_signal(equity, debt, closeadj):
    base = _f06_capital_buffer(equity, debt, 63) * closeadj
    base_series = base
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_126d_slope_v026_signal(equity, debt, closeadj):
    base = _f06_capital_buffer(equity, debt, 126) * closeadj
    base_series = base
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_189d_slope_v027_signal(equity, debt, closeadj):
    base = _f06_capital_buffer(equity, debt, 189) * closeadj
    base_series = base
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_252d_slope_v028_signal(equity, debt, closeadj):
    base = _f06_capital_buffer(equity, debt, 252) * closeadj
    base_series = base
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_378d_slope_v029_signal(equity, debt, closeadj):
    base = _f06_capital_buffer(equity, debt, 378) * closeadj
    base_series = base
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_504d_slope_v030_signal(equity, debt, closeadj):
    base = _f06_capital_buffer(equity, debt, 504) * closeadj
    base_series = base
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratioz_21d_slope_v031_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = _z(cr, 21) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratioz_63d_slope_v032_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = _z(cr, 63) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratioz_126d_slope_v033_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = _z(cr, 126) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratioz_252d_slope_v034_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = _z(cr, 252) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiostd_21d_slope_v035_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = _std(cr, 21) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiostd_63d_slope_v036_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = _std(cr, 63) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiostd_126d_slope_v037_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = _std(cr, 126) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiostd_252d_slope_v038_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = _std(cr, 252) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdynz_21d_slope_v039_signal(equity, assets, closeadj):
    cd = _f06_capital_dynamics(equity, assets, 21)
    base_series = _z(cd, 21) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdynz_63d_slope_v040_signal(equity, assets, closeadj):
    cd = _f06_capital_dynamics(equity, assets, 63)
    base_series = _z(cd, 63) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdynz_126d_slope_v041_signal(equity, assets, closeadj):
    cd = _f06_capital_dynamics(equity, assets, 126)
    base_series = _z(cd, 126) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdynz_252d_slope_v042_signal(equity, assets, closeadj):
    cd = _f06_capital_dynamics(equity, assets, 252)
    base_series = _z(cd, 252) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufz_21d_slope_v043_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 21)
    base_series = _z(cb, 21) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufz_63d_slope_v044_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 63)
    base_series = _z(cb, 63) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufz_126d_slope_v045_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 126)
    base_series = _z(cb, 126) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufz_252d_slope_v046_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 252)
    base_series = _z(cb, 252) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratioema_10d_slope_v047_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = _ema(cr, 10) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratioema_21d_slope_v048_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = _ema(cr, 21) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratioema_63d_slope_v049_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = _ema(cr, 63) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratioema_126d_slope_v050_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = _ema(cr, 126) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratioema_252d_slope_v051_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = _ema(cr, 252) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiolog_21d_slope_v052_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = np.log(cr.replace(0, np.nan).abs()) * _mean(closeadj, 21)
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiolog_63d_slope_v053_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = np.log(cr.replace(0, np.nan).abs()) * _mean(closeadj, 63)
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiolog_252d_slope_v054_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = np.log(cr.replace(0, np.nan).abs()) * _mean(closeadj, 252)
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuflog_21d_slope_v055_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 21)
    base_series = np.log(cb.replace(0, np.nan).abs()) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuflog_63d_slope_v056_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 63)
    base_series = np.log(cb.replace(0, np.nan).abs()) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuflog_252d_slope_v057_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 252)
    base_series = np.log(cb.replace(0, np.nan).abs()) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratioxcdv_21d_slope_v058_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = cr * _mean(closeadj, 21) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratioxcdv_63d_slope_v059_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = cr * _mean(closeadj, 63) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratioxcdv_126d_slope_v060_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = cr * _mean(closeadj, 126) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdynxbuf_21d_slope_v061_signal(equity, assets, debt, closeadj):
    cd = _f06_capital_dynamics(equity, assets, 21)
    cb = _f06_capital_buffer(equity, debt, 21)
    base_series = cd * cb * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdynxbuf_63d_slope_v062_signal(equity, assets, debt, closeadj):
    cd = _f06_capital_dynamics(equity, assets, 63)
    cb = _f06_capital_buffer(equity, debt, 63)
    base_series = cd * cb * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdynxbuf_126d_slope_v063_signal(equity, assets, debt, closeadj):
    cd = _f06_capital_dynamics(equity, assets, 126)
    cb = _f06_capital_buffer(equity, debt, 126)
    base_series = cd * cb * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdynxbuf_252d_slope_v064_signal(equity, assets, debt, closeadj):
    cd = _f06_capital_dynamics(equity, assets, 252)
    cb = _f06_capital_buffer(equity, debt, 252)
    base_series = cd * cb * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiochg_5d_slope_v065_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = cr.diff(periods=5) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiochg_21d_slope_v066_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = cr.diff(periods=21) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiochg_63d_slope_v067_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = cr.diff(periods=63) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiochg_126d_slope_v068_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = cr.diff(periods=126) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiochg_252d_slope_v069_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = cr.diff(periods=252) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufchg_5d_slope_v070_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 5)
    base_series = cb.diff(periods=5) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufchg_21d_slope_v071_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 21)
    base_series = cb.diff(periods=21) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufchg_63d_slope_v072_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 63)
    base_series = cb.diff(periods=63) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufchg_126d_slope_v073_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 126)
    base_series = cb.diff(periods=126) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufchg_252d_slope_v074_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 252)
    base_series = cb.diff(periods=252) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiorange_21d_slope_v075_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    rng = cr.rolling(21, min_periods=max(1, 21//2)).max() - cr.rolling(21, min_periods=max(1, 21//2)).min()
    base_series = rng * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiorange_63d_slope_v076_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    rng = cr.rolling(63, min_periods=max(1, 63//2)).max() - cr.rolling(63, min_periods=max(1, 63//2)).min()
    base_series = rng * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiorange_126d_slope_v077_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    rng = cr.rolling(126, min_periods=max(1, 126//2)).max() - cr.rolling(126, min_periods=max(1, 126//2)).min()
    base_series = rng * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiorange_252d_slope_v078_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    rng = cr.rolling(252, min_periods=max(1, 252//2)).max() - cr.rolling(252, min_periods=max(1, 252//2)).min()
    base_series = rng * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdynxretvol_21d_slope_v079_signal(equity, assets, closeadj):
    cd = _f06_capital_dynamics(equity, assets, 21)
    rv = _std(closeadj.pct_change(), 21)
    base_series = cd * rv * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdynxretvol_63d_slope_v080_signal(equity, assets, closeadj):
    cd = _f06_capital_dynamics(equity, assets, 63)
    rv = _std(closeadj.pct_change(), 63)
    base_series = cd * rv * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdynxretvol_126d_slope_v081_signal(equity, assets, closeadj):
    cd = _f06_capital_dynamics(equity, assets, 126)
    rv = _std(closeadj.pct_change(), 126)
    base_series = cd * rv * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufxretvol_21d_slope_v082_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 21)
    rv = _std(closeadj.pct_change(), 21)
    base_series = cb * rv * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufxretvol_63d_slope_v083_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 63)
    rv = _std(closeadj.pct_change(), 63)
    base_series = cb * rv * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufxretvol_126d_slope_v084_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 126)
    rv = _std(closeadj.pct_change(), 126)
    base_series = cb * rv * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiorank_63d_slope_v085_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    rnk = cr.rolling(63, min_periods=max(1, 63//2)).rank(pct=True)
    base_series = rnk * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiorank_126d_slope_v086_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    rnk = cr.rolling(126, min_periods=max(1, 126//2)).rank(pct=True)
    base_series = rnk * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiorank_252d_slope_v087_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    rnk = cr.rolling(252, min_periods=max(1, 252//2)).rank(pct=True)
    base_series = rnk * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufrank_63d_slope_v088_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 63)
    rnk = cb.rolling(63, min_periods=max(1, 63//2)).rank(pct=True)
    base_series = rnk * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufrank_126d_slope_v089_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 126)
    rnk = cb.rolling(126, min_periods=max(1, 126//2)).rank(pct=True)
    base_series = rnk * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufrank_252d_slope_v090_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 252)
    rnk = cb.rolling(252, min_periods=max(1, 252//2)).rank(pct=True)
    base_series = rnk * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiochgsign_21d_slope_v091_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = np.sign(cr.diff(periods=21)) * _mean(closeadj, 21)
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiochgsign_63d_slope_v092_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = np.sign(cr.diff(periods=63)) * _mean(closeadj, 63)
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiochgsign_252d_slope_v093_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = np.sign(cr.diff(periods=252)) * _mean(closeadj, 252)
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_mean_10d_slope_v094_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = _mean(cr, 10) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_mean_10d_slope_v095_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 10)
    base_series = _mean(cb, 10) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_std_10d_slope_v096_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = _std(cr, 10) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_std_10d_slope_v097_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 10)
    base_series = _std(cb, 10) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_z_10d_slope_v098_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = _z(cr, 10) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_z_10d_slope_v099_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 10)
    base_series = _z(cb, 10) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_ema_10d_slope_v100_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = _ema(cr, 10) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_ema_10d_slope_v101_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 10)
    base_series = _ema(cb, 10) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_mean_42d_slope_v102_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = _mean(cr, 42) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_mean_42d_slope_v103_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 42)
    base_series = _mean(cb, 42) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_std_42d_slope_v104_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = _std(cr, 42) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_std_42d_slope_v105_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 42)
    base_series = _std(cb, 42) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_z_42d_slope_v106_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = _z(cr, 42) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_z_42d_slope_v107_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 42)
    base_series = _z(cb, 42) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_ema_42d_slope_v108_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = _ema(cr, 42) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_ema_42d_slope_v109_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 42)
    base_series = _ema(cb, 42) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_mean_189d_slope_v110_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = _mean(cr, 189) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_mean_189d_slope_v111_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 189)
    base_series = _mean(cb, 189) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_std_189d_slope_v112_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = _std(cr, 189) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_std_189d_slope_v113_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 189)
    base_series = _std(cb, 189) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_z_189d_slope_v114_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = _z(cr, 189) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_z_189d_slope_v115_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 189)
    base_series = _z(cb, 189) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_ema_189d_slope_v116_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = _ema(cr, 189) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_ema_189d_slope_v117_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 189)
    base_series = _ema(cb, 189) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_mean_378d_slope_v118_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = _mean(cr, 378) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_mean_378d_slope_v119_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 378)
    base_series = _mean(cb, 378) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_std_378d_slope_v120_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = _std(cr, 378) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_std_378d_slope_v121_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 378)
    base_series = _std(cb, 378) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_z_378d_slope_v122_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = _z(cr, 378) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_z_378d_slope_v123_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 378)
    base_series = _z(cb, 378) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_ema_378d_slope_v124_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    base_series = _ema(cr, 378) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_ema_378d_slope_v125_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 378)
    base_series = _ema(cb, 378) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdynratio_21v63_slope_v126_signal(equity, assets, closeadj):
    a = _f06_capital_dynamics(equity, assets, 21)
    b = _f06_capital_dynamics(equity, assets, 63)
    base_series = (a / b.replace(0, np.nan)) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufratio_21v63_slope_v127_signal(equity, debt, closeadj):
    a = _f06_capital_buffer(equity, debt, 21)
    b = _f06_capital_buffer(equity, debt, 63)
    base_series = (a / b.replace(0, np.nan)) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdynratio_63v252_slope_v128_signal(equity, assets, closeadj):
    a = _f06_capital_dynamics(equity, assets, 63)
    b = _f06_capital_dynamics(equity, assets, 252)
    base_series = (a / b.replace(0, np.nan)) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufratio_63v252_slope_v129_signal(equity, debt, closeadj):
    a = _f06_capital_buffer(equity, debt, 63)
    b = _f06_capital_buffer(equity, debt, 252)
    base_series = (a / b.replace(0, np.nan)) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdynratio_21v252_slope_v130_signal(equity, assets, closeadj):
    a = _f06_capital_dynamics(equity, assets, 21)
    b = _f06_capital_dynamics(equity, assets, 252)
    base_series = (a / b.replace(0, np.nan)) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufratio_21v252_slope_v131_signal(equity, debt, closeadj):
    a = _f06_capital_buffer(equity, debt, 21)
    b = _f06_capital_buffer(equity, debt, 252)
    base_series = (a / b.replace(0, np.nan)) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdynratio_126v504_slope_v132_signal(equity, assets, closeadj):
    a = _f06_capital_dynamics(equity, assets, 126)
    b = _f06_capital_dynamics(equity, assets, 504)
    base_series = (a / b.replace(0, np.nan)) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufratio_126v504_slope_v133_signal(equity, debt, closeadj):
    a = _f06_capital_buffer(equity, debt, 126)
    b = _f06_capital_buffer(equity, debt, 504)
    base_series = (a / b.replace(0, np.nan)) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdynratio_42v189_slope_v134_signal(equity, assets, closeadj):
    a = _f06_capital_dynamics(equity, assets, 42)
    b = _f06_capital_dynamics(equity, assets, 189)
    base_series = (a / b.replace(0, np.nan)) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufratio_42v189_slope_v135_signal(equity, debt, closeadj):
    a = _f06_capital_buffer(equity, debt, 42)
    b = _f06_capital_buffer(equity, debt, 189)
    base_series = (a / b.replace(0, np.nan)) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdyndiff_21m63_slope_v136_signal(equity, assets, closeadj):
    a = _f06_capital_dynamics(equity, assets, 21)
    b = _f06_capital_dynamics(equity, assets, 63)
    base_series = (a - b) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufdiff_21m63_slope_v137_signal(equity, debt, closeadj):
    a = _f06_capital_buffer(equity, debt, 21)
    b = _f06_capital_buffer(equity, debt, 63)
    base_series = (a - b) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdyndiff_63m252_slope_v138_signal(equity, assets, closeadj):
    a = _f06_capital_dynamics(equity, assets, 63)
    b = _f06_capital_dynamics(equity, assets, 252)
    base_series = (a - b) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufdiff_63m252_slope_v139_signal(equity, debt, closeadj):
    a = _f06_capital_buffer(equity, debt, 63)
    b = _f06_capital_buffer(equity, debt, 252)
    base_series = (a - b) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdyndiff_126m504_slope_v140_signal(equity, assets, closeadj):
    a = _f06_capital_dynamics(equity, assets, 126)
    b = _f06_capital_dynamics(equity, assets, 504)
    base_series = (a - b) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufdiff_126m504_slope_v141_signal(equity, debt, closeadj):
    a = _f06_capital_buffer(equity, debt, 126)
    b = _f06_capital_buffer(equity, debt, 504)
    base_series = (a - b) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capcompound_21d_slope_v142_signal(equity, assets, debt, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    cb = _f06_capital_buffer(equity, debt, 21)
    base_series = (cr + cb) * _mean(closeadj, 21)
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capcompound_63d_slope_v143_signal(equity, assets, debt, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    cb = _f06_capital_buffer(equity, debt, 63)
    base_series = (cr + cb) * _mean(closeadj, 63)
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capcompound_126d_slope_v144_signal(equity, assets, debt, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    cb = _f06_capital_buffer(equity, debt, 126)
    base_series = (cr + cb) * _mean(closeadj, 126)
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capcompound_252d_slope_v145_signal(equity, assets, debt, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    cb = _f06_capital_buffer(equity, debt, 252)
    base_series = (cr + cb) * _mean(closeadj, 252)
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capcompound_504d_slope_v146_signal(equity, assets, debt, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    cb = _f06_capital_buffer(equity, debt, 504)
    base_series = (cr + cb) * _mean(closeadj, 504)
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdynpct_21d_slope_v147_signal(equity, assets, closeadj):
    cd = _f06_capital_dynamics(equity, assets, 21)
    base_series = cd.pct_change(periods=21) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdynpct_63d_slope_v148_signal(equity, assets, closeadj):
    cd = _f06_capital_dynamics(equity, assets, 63)
    base_series = cd.pct_change(periods=63) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdynpct_126d_slope_v149_signal(equity, assets, closeadj):
    cd = _f06_capital_dynamics(equity, assets, 126)
    base_series = cd.pct_change(periods=126) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdynpct_252d_slope_v150_signal(equity, assets, closeadj):
    cd = _f06_capital_dynamics(equity, assets, 252)
    base_series = cd.pct_change(periods=252) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f06bca_f06_bank_capital_adequacy_capratio_5d_slope_v001_signal,
    f06bca_f06_bank_capital_adequacy_capratio_10d_slope_v002_signal,
    f06bca_f06_bank_capital_adequacy_capratio_21d_slope_v003_signal,
    f06bca_f06_bank_capital_adequacy_capratio_42d_slope_v004_signal,
    f06bca_f06_bank_capital_adequacy_capratio_63d_slope_v005_signal,
    f06bca_f06_bank_capital_adequacy_capratio_126d_slope_v006_signal,
    f06bca_f06_bank_capital_adequacy_capratio_189d_slope_v007_signal,
    f06bca_f06_bank_capital_adequacy_capratio_252d_slope_v008_signal,
    f06bca_f06_bank_capital_adequacy_capratio_378d_slope_v009_signal,
    f06bca_f06_bank_capital_adequacy_capratio_504d_slope_v010_signal,
    f06bca_f06_bank_capital_adequacy_capdyn_5d_slope_v011_signal,
    f06bca_f06_bank_capital_adequacy_capdyn_10d_slope_v012_signal,
    f06bca_f06_bank_capital_adequacy_capdyn_21d_slope_v013_signal,
    f06bca_f06_bank_capital_adequacy_capdyn_42d_slope_v014_signal,
    f06bca_f06_bank_capital_adequacy_capdyn_63d_slope_v015_signal,
    f06bca_f06_bank_capital_adequacy_capdyn_126d_slope_v016_signal,
    f06bca_f06_bank_capital_adequacy_capdyn_189d_slope_v017_signal,
    f06bca_f06_bank_capital_adequacy_capdyn_252d_slope_v018_signal,
    f06bca_f06_bank_capital_adequacy_capdyn_378d_slope_v019_signal,
    f06bca_f06_bank_capital_adequacy_capdyn_504d_slope_v020_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_5d_slope_v021_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_10d_slope_v022_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_21d_slope_v023_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_42d_slope_v024_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_63d_slope_v025_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_126d_slope_v026_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_189d_slope_v027_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_252d_slope_v028_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_378d_slope_v029_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_504d_slope_v030_signal,
    f06bca_f06_bank_capital_adequacy_capratioz_21d_slope_v031_signal,
    f06bca_f06_bank_capital_adequacy_capratioz_63d_slope_v032_signal,
    f06bca_f06_bank_capital_adequacy_capratioz_126d_slope_v033_signal,
    f06bca_f06_bank_capital_adequacy_capratioz_252d_slope_v034_signal,
    f06bca_f06_bank_capital_adequacy_capratiostd_21d_slope_v035_signal,
    f06bca_f06_bank_capital_adequacy_capratiostd_63d_slope_v036_signal,
    f06bca_f06_bank_capital_adequacy_capratiostd_126d_slope_v037_signal,
    f06bca_f06_bank_capital_adequacy_capratiostd_252d_slope_v038_signal,
    f06bca_f06_bank_capital_adequacy_capdynz_21d_slope_v039_signal,
    f06bca_f06_bank_capital_adequacy_capdynz_63d_slope_v040_signal,
    f06bca_f06_bank_capital_adequacy_capdynz_126d_slope_v041_signal,
    f06bca_f06_bank_capital_adequacy_capdynz_252d_slope_v042_signal,
    f06bca_f06_bank_capital_adequacy_capbufz_21d_slope_v043_signal,
    f06bca_f06_bank_capital_adequacy_capbufz_63d_slope_v044_signal,
    f06bca_f06_bank_capital_adequacy_capbufz_126d_slope_v045_signal,
    f06bca_f06_bank_capital_adequacy_capbufz_252d_slope_v046_signal,
    f06bca_f06_bank_capital_adequacy_capratioema_10d_slope_v047_signal,
    f06bca_f06_bank_capital_adequacy_capratioema_21d_slope_v048_signal,
    f06bca_f06_bank_capital_adequacy_capratioema_63d_slope_v049_signal,
    f06bca_f06_bank_capital_adequacy_capratioema_126d_slope_v050_signal,
    f06bca_f06_bank_capital_adequacy_capratioema_252d_slope_v051_signal,
    f06bca_f06_bank_capital_adequacy_capratiolog_21d_slope_v052_signal,
    f06bca_f06_bank_capital_adequacy_capratiolog_63d_slope_v053_signal,
    f06bca_f06_bank_capital_adequacy_capratiolog_252d_slope_v054_signal,
    f06bca_f06_bank_capital_adequacy_capbuflog_21d_slope_v055_signal,
    f06bca_f06_bank_capital_adequacy_capbuflog_63d_slope_v056_signal,
    f06bca_f06_bank_capital_adequacy_capbuflog_252d_slope_v057_signal,
    f06bca_f06_bank_capital_adequacy_capratioxcdv_21d_slope_v058_signal,
    f06bca_f06_bank_capital_adequacy_capratioxcdv_63d_slope_v059_signal,
    f06bca_f06_bank_capital_adequacy_capratioxcdv_126d_slope_v060_signal,
    f06bca_f06_bank_capital_adequacy_capdynxbuf_21d_slope_v061_signal,
    f06bca_f06_bank_capital_adequacy_capdynxbuf_63d_slope_v062_signal,
    f06bca_f06_bank_capital_adequacy_capdynxbuf_126d_slope_v063_signal,
    f06bca_f06_bank_capital_adequacy_capdynxbuf_252d_slope_v064_signal,
    f06bca_f06_bank_capital_adequacy_capratiochg_5d_slope_v065_signal,
    f06bca_f06_bank_capital_adequacy_capratiochg_21d_slope_v066_signal,
    f06bca_f06_bank_capital_adequacy_capratiochg_63d_slope_v067_signal,
    f06bca_f06_bank_capital_adequacy_capratiochg_126d_slope_v068_signal,
    f06bca_f06_bank_capital_adequacy_capratiochg_252d_slope_v069_signal,
    f06bca_f06_bank_capital_adequacy_capbufchg_5d_slope_v070_signal,
    f06bca_f06_bank_capital_adequacy_capbufchg_21d_slope_v071_signal,
    f06bca_f06_bank_capital_adequacy_capbufchg_63d_slope_v072_signal,
    f06bca_f06_bank_capital_adequacy_capbufchg_126d_slope_v073_signal,
    f06bca_f06_bank_capital_adequacy_capbufchg_252d_slope_v074_signal,
    f06bca_f06_bank_capital_adequacy_capratiorange_21d_slope_v075_signal,
    f06bca_f06_bank_capital_adequacy_capratiorange_63d_slope_v076_signal,
    f06bca_f06_bank_capital_adequacy_capratiorange_126d_slope_v077_signal,
    f06bca_f06_bank_capital_adequacy_capratiorange_252d_slope_v078_signal,
    f06bca_f06_bank_capital_adequacy_capdynxretvol_21d_slope_v079_signal,
    f06bca_f06_bank_capital_adequacy_capdynxretvol_63d_slope_v080_signal,
    f06bca_f06_bank_capital_adequacy_capdynxretvol_126d_slope_v081_signal,
    f06bca_f06_bank_capital_adequacy_capbufxretvol_21d_slope_v082_signal,
    f06bca_f06_bank_capital_adequacy_capbufxretvol_63d_slope_v083_signal,
    f06bca_f06_bank_capital_adequacy_capbufxretvol_126d_slope_v084_signal,
    f06bca_f06_bank_capital_adequacy_capratiorank_63d_slope_v085_signal,
    f06bca_f06_bank_capital_adequacy_capratiorank_126d_slope_v086_signal,
    f06bca_f06_bank_capital_adequacy_capratiorank_252d_slope_v087_signal,
    f06bca_f06_bank_capital_adequacy_capbufrank_63d_slope_v088_signal,
    f06bca_f06_bank_capital_adequacy_capbufrank_126d_slope_v089_signal,
    f06bca_f06_bank_capital_adequacy_capbufrank_252d_slope_v090_signal,
    f06bca_f06_bank_capital_adequacy_capratiochgsign_21d_slope_v091_signal,
    f06bca_f06_bank_capital_adequacy_capratiochgsign_63d_slope_v092_signal,
    f06bca_f06_bank_capital_adequacy_capratiochgsign_252d_slope_v093_signal,
    f06bca_f06_bank_capital_adequacy_capratio_mean_10d_slope_v094_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_mean_10d_slope_v095_signal,
    f06bca_f06_bank_capital_adequacy_capratio_std_10d_slope_v096_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_std_10d_slope_v097_signal,
    f06bca_f06_bank_capital_adequacy_capratio_z_10d_slope_v098_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_z_10d_slope_v099_signal,
    f06bca_f06_bank_capital_adequacy_capratio_ema_10d_slope_v100_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_ema_10d_slope_v101_signal,
    f06bca_f06_bank_capital_adequacy_capratio_mean_42d_slope_v102_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_mean_42d_slope_v103_signal,
    f06bca_f06_bank_capital_adequacy_capratio_std_42d_slope_v104_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_std_42d_slope_v105_signal,
    f06bca_f06_bank_capital_adequacy_capratio_z_42d_slope_v106_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_z_42d_slope_v107_signal,
    f06bca_f06_bank_capital_adequacy_capratio_ema_42d_slope_v108_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_ema_42d_slope_v109_signal,
    f06bca_f06_bank_capital_adequacy_capratio_mean_189d_slope_v110_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_mean_189d_slope_v111_signal,
    f06bca_f06_bank_capital_adequacy_capratio_std_189d_slope_v112_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_std_189d_slope_v113_signal,
    f06bca_f06_bank_capital_adequacy_capratio_z_189d_slope_v114_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_z_189d_slope_v115_signal,
    f06bca_f06_bank_capital_adequacy_capratio_ema_189d_slope_v116_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_ema_189d_slope_v117_signal,
    f06bca_f06_bank_capital_adequacy_capratio_mean_378d_slope_v118_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_mean_378d_slope_v119_signal,
    f06bca_f06_bank_capital_adequacy_capratio_std_378d_slope_v120_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_std_378d_slope_v121_signal,
    f06bca_f06_bank_capital_adequacy_capratio_z_378d_slope_v122_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_z_378d_slope_v123_signal,
    f06bca_f06_bank_capital_adequacy_capratio_ema_378d_slope_v124_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_ema_378d_slope_v125_signal,
    f06bca_f06_bank_capital_adequacy_capdynratio_21v63_slope_v126_signal,
    f06bca_f06_bank_capital_adequacy_capbufratio_21v63_slope_v127_signal,
    f06bca_f06_bank_capital_adequacy_capdynratio_63v252_slope_v128_signal,
    f06bca_f06_bank_capital_adequacy_capbufratio_63v252_slope_v129_signal,
    f06bca_f06_bank_capital_adequacy_capdynratio_21v252_slope_v130_signal,
    f06bca_f06_bank_capital_adequacy_capbufratio_21v252_slope_v131_signal,
    f06bca_f06_bank_capital_adequacy_capdynratio_126v504_slope_v132_signal,
    f06bca_f06_bank_capital_adequacy_capbufratio_126v504_slope_v133_signal,
    f06bca_f06_bank_capital_adequacy_capdynratio_42v189_slope_v134_signal,
    f06bca_f06_bank_capital_adequacy_capbufratio_42v189_slope_v135_signal,
    f06bca_f06_bank_capital_adequacy_capdyndiff_21m63_slope_v136_signal,
    f06bca_f06_bank_capital_adequacy_capbufdiff_21m63_slope_v137_signal,
    f06bca_f06_bank_capital_adequacy_capdyndiff_63m252_slope_v138_signal,
    f06bca_f06_bank_capital_adequacy_capbufdiff_63m252_slope_v139_signal,
    f06bca_f06_bank_capital_adequacy_capdyndiff_126m504_slope_v140_signal,
    f06bca_f06_bank_capital_adequacy_capbufdiff_126m504_slope_v141_signal,
    f06bca_f06_bank_capital_adequacy_capcompound_21d_slope_v142_signal,
    f06bca_f06_bank_capital_adequacy_capcompound_63d_slope_v143_signal,
    f06bca_f06_bank_capital_adequacy_capcompound_126d_slope_v144_signal,
    f06bca_f06_bank_capital_adequacy_capcompound_252d_slope_v145_signal,
    f06bca_f06_bank_capital_adequacy_capcompound_504d_slope_v146_signal,
    f06bca_f06_bank_capital_adequacy_capdynpct_21d_slope_v147_signal,
    f06bca_f06_bank_capital_adequacy_capdynpct_63d_slope_v148_signal,
    f06bca_f06_bank_capital_adequacy_capdynpct_126d_slope_v149_signal,
    f06bca_f06_bank_capital_adequacy_capdynpct_252d_slope_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F06_BANK_CAPITAL_ADEQUACY_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    netinc = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    equity = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    debt = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    intangibles = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    roa = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    cols = {
        "closeadj": closeadj, "volume": volume, "revenue": revenue,
        "netinc": netinc, "assets": assets, "equity": equity, "debt": debt,
        "intangibles": intangibles, "sharesbas": sharesbas, "roa": roa, "roe": roe,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f06_capital_ratio', '_f06_capital_dynamics', '_f06_capital_buffer')
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
    print(f"OK f06_bank_capital_adequacy_2nd_derivatives_001_150_claude: {n_features} features pass")
