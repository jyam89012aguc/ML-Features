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


def _f06_capital_ratio(equity, assets):
    return equity / assets.replace(0, np.nan)


def _f06_capital_dynamics(equity, assets, w):
    cr = equity / assets.replace(0, np.nan)
    return cr.rolling(w, min_periods=max(1, w // 2)).mean()


def _f06_capital_buffer(equity, debt, w):
    buf = equity / (equity + debt).replace(0, np.nan)
    return buf.rolling(w, min_periods=max(1, w // 2)).mean()


def f06bca_f06_bank_capital_adequacy_capratio_5d_base_v001_signal(equity, assets, closeadj):
    base = _f06_capital_ratio(equity, assets) * _mean(closeadj, 5)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_10d_base_v002_signal(equity, assets, closeadj):
    base = _f06_capital_ratio(equity, assets) * _mean(closeadj, 10)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_21d_base_v003_signal(equity, assets, closeadj):
    base = _f06_capital_ratio(equity, assets) * _mean(closeadj, 21)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_42d_base_v004_signal(equity, assets, closeadj):
    base = _f06_capital_ratio(equity, assets) * _mean(closeadj, 42)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_63d_base_v005_signal(equity, assets, closeadj):
    base = _f06_capital_ratio(equity, assets) * _mean(closeadj, 63)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_126d_base_v006_signal(equity, assets, closeadj):
    base = _f06_capital_ratio(equity, assets) * _mean(closeadj, 126)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_189d_base_v007_signal(equity, assets, closeadj):
    base = _f06_capital_ratio(equity, assets) * _mean(closeadj, 189)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_252d_base_v008_signal(equity, assets, closeadj):
    base = _f06_capital_ratio(equity, assets) * _mean(closeadj, 252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_378d_base_v009_signal(equity, assets, closeadj):
    base = _f06_capital_ratio(equity, assets) * _mean(closeadj, 378)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_504d_base_v010_signal(equity, assets, closeadj):
    base = _f06_capital_ratio(equity, assets) * _mean(closeadj, 504)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdyn_5d_base_v011_signal(equity, assets, closeadj):
    base = _f06_capital_dynamics(equity, assets, 5) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdyn_10d_base_v012_signal(equity, assets, closeadj):
    base = _f06_capital_dynamics(equity, assets, 10) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdyn_21d_base_v013_signal(equity, assets, closeadj):
    base = _f06_capital_dynamics(equity, assets, 21) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdyn_42d_base_v014_signal(equity, assets, closeadj):
    base = _f06_capital_dynamics(equity, assets, 42) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdyn_63d_base_v015_signal(equity, assets, closeadj):
    base = _f06_capital_dynamics(equity, assets, 63) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdyn_126d_base_v016_signal(equity, assets, closeadj):
    base = _f06_capital_dynamics(equity, assets, 126) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdyn_189d_base_v017_signal(equity, assets, closeadj):
    base = _f06_capital_dynamics(equity, assets, 189) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdyn_252d_base_v018_signal(equity, assets, closeadj):
    base = _f06_capital_dynamics(equity, assets, 252) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdyn_378d_base_v019_signal(equity, assets, closeadj):
    base = _f06_capital_dynamics(equity, assets, 378) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdyn_504d_base_v020_signal(equity, assets, closeadj):
    base = _f06_capital_dynamics(equity, assets, 504) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_5d_base_v021_signal(equity, debt, closeadj):
    base = _f06_capital_buffer(equity, debt, 5) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_10d_base_v022_signal(equity, debt, closeadj):
    base = _f06_capital_buffer(equity, debt, 10) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_21d_base_v023_signal(equity, debt, closeadj):
    base = _f06_capital_buffer(equity, debt, 21) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_42d_base_v024_signal(equity, debt, closeadj):
    base = _f06_capital_buffer(equity, debt, 42) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_63d_base_v025_signal(equity, debt, closeadj):
    base = _f06_capital_buffer(equity, debt, 63) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_126d_base_v026_signal(equity, debt, closeadj):
    base = _f06_capital_buffer(equity, debt, 126) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_189d_base_v027_signal(equity, debt, closeadj):
    base = _f06_capital_buffer(equity, debt, 189) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_252d_base_v028_signal(equity, debt, closeadj):
    base = _f06_capital_buffer(equity, debt, 252) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_378d_base_v029_signal(equity, debt, closeadj):
    base = _f06_capital_buffer(equity, debt, 378) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_504d_base_v030_signal(equity, debt, closeadj):
    base = _f06_capital_buffer(equity, debt, 504) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratioz_21d_base_v031_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = _z(cr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratioz_63d_base_v032_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = _z(cr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratioz_126d_base_v033_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = _z(cr, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratioz_252d_base_v034_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = _z(cr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiostd_21d_base_v035_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = _std(cr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiostd_63d_base_v036_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = _std(cr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiostd_126d_base_v037_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = _std(cr, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiostd_252d_base_v038_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = _std(cr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdynz_21d_base_v039_signal(equity, assets, closeadj):
    cd = _f06_capital_dynamics(equity, assets, 21)
    result = _z(cd, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdynz_63d_base_v040_signal(equity, assets, closeadj):
    cd = _f06_capital_dynamics(equity, assets, 63)
    result = _z(cd, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdynz_126d_base_v041_signal(equity, assets, closeadj):
    cd = _f06_capital_dynamics(equity, assets, 126)
    result = _z(cd, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdynz_252d_base_v042_signal(equity, assets, closeadj):
    cd = _f06_capital_dynamics(equity, assets, 252)
    result = _z(cd, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufz_21d_base_v043_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 21)
    result = _z(cb, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufz_63d_base_v044_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 63)
    result = _z(cb, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufz_126d_base_v045_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 126)
    result = _z(cb, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufz_252d_base_v046_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 252)
    result = _z(cb, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratioema_10d_base_v047_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = _ema(cr, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratioema_21d_base_v048_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = _ema(cr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratioema_63d_base_v049_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = _ema(cr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratioema_126d_base_v050_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = _ema(cr, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratioema_252d_base_v051_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = _ema(cr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiolog_21d_base_v052_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = np.log(cr.replace(0, np.nan).abs()) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiolog_63d_base_v053_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = np.log(cr.replace(0, np.nan).abs()) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiolog_252d_base_v054_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = np.log(cr.replace(0, np.nan).abs()) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuflog_21d_base_v055_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 21)
    result = np.log(cb.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuflog_63d_base_v056_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 63)
    result = np.log(cb.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuflog_252d_base_v057_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 252)
    result = np.log(cb.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratioxcdv_21d_base_v058_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = cr * _mean(closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratioxcdv_63d_base_v059_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = cr * _mean(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratioxcdv_126d_base_v060_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = cr * _mean(closeadj, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdynxbuf_21d_base_v061_signal(equity, assets, debt, closeadj):
    cd = _f06_capital_dynamics(equity, assets, 21)
    cb = _f06_capital_buffer(equity, debt, 21)
    result = cd * cb * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdynxbuf_63d_base_v062_signal(equity, assets, debt, closeadj):
    cd = _f06_capital_dynamics(equity, assets, 63)
    cb = _f06_capital_buffer(equity, debt, 63)
    result = cd * cb * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdynxbuf_126d_base_v063_signal(equity, assets, debt, closeadj):
    cd = _f06_capital_dynamics(equity, assets, 126)
    cb = _f06_capital_buffer(equity, debt, 126)
    result = cd * cb * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdynxbuf_252d_base_v064_signal(equity, assets, debt, closeadj):
    cd = _f06_capital_dynamics(equity, assets, 252)
    cb = _f06_capital_buffer(equity, debt, 252)
    result = cd * cb * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiochg_5d_base_v065_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = cr.diff(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiochg_21d_base_v066_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = cr.diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiochg_63d_base_v067_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = cr.diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiochg_126d_base_v068_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = cr.diff(periods=126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiochg_252d_base_v069_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = cr.diff(periods=252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufchg_5d_base_v070_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 5)
    result = cb.diff(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufchg_21d_base_v071_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 21)
    result = cb.diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufchg_63d_base_v072_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 63)
    result = cb.diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufchg_126d_base_v073_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 126)
    result = cb.diff(periods=126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufchg_252d_base_v074_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 252)
    result = cb.diff(periods=252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiorange_21d_base_v075_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    rng = cr.rolling(21, min_periods=max(1, 21//2)).max() - cr.rolling(21, min_periods=max(1, 21//2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f06bca_f06_bank_capital_adequacy_capratio_5d_base_v001_signal,
    f06bca_f06_bank_capital_adequacy_capratio_10d_base_v002_signal,
    f06bca_f06_bank_capital_adequacy_capratio_21d_base_v003_signal,
    f06bca_f06_bank_capital_adequacy_capratio_42d_base_v004_signal,
    f06bca_f06_bank_capital_adequacy_capratio_63d_base_v005_signal,
    f06bca_f06_bank_capital_adequacy_capratio_126d_base_v006_signal,
    f06bca_f06_bank_capital_adequacy_capratio_189d_base_v007_signal,
    f06bca_f06_bank_capital_adequacy_capratio_252d_base_v008_signal,
    f06bca_f06_bank_capital_adequacy_capratio_378d_base_v009_signal,
    f06bca_f06_bank_capital_adequacy_capratio_504d_base_v010_signal,
    f06bca_f06_bank_capital_adequacy_capdyn_5d_base_v011_signal,
    f06bca_f06_bank_capital_adequacy_capdyn_10d_base_v012_signal,
    f06bca_f06_bank_capital_adequacy_capdyn_21d_base_v013_signal,
    f06bca_f06_bank_capital_adequacy_capdyn_42d_base_v014_signal,
    f06bca_f06_bank_capital_adequacy_capdyn_63d_base_v015_signal,
    f06bca_f06_bank_capital_adequacy_capdyn_126d_base_v016_signal,
    f06bca_f06_bank_capital_adequacy_capdyn_189d_base_v017_signal,
    f06bca_f06_bank_capital_adequacy_capdyn_252d_base_v018_signal,
    f06bca_f06_bank_capital_adequacy_capdyn_378d_base_v019_signal,
    f06bca_f06_bank_capital_adequacy_capdyn_504d_base_v020_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_5d_base_v021_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_10d_base_v022_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_21d_base_v023_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_42d_base_v024_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_63d_base_v025_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_126d_base_v026_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_189d_base_v027_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_252d_base_v028_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_378d_base_v029_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_504d_base_v030_signal,
    f06bca_f06_bank_capital_adequacy_capratioz_21d_base_v031_signal,
    f06bca_f06_bank_capital_adequacy_capratioz_63d_base_v032_signal,
    f06bca_f06_bank_capital_adequacy_capratioz_126d_base_v033_signal,
    f06bca_f06_bank_capital_adequacy_capratioz_252d_base_v034_signal,
    f06bca_f06_bank_capital_adequacy_capratiostd_21d_base_v035_signal,
    f06bca_f06_bank_capital_adequacy_capratiostd_63d_base_v036_signal,
    f06bca_f06_bank_capital_adequacy_capratiostd_126d_base_v037_signal,
    f06bca_f06_bank_capital_adequacy_capratiostd_252d_base_v038_signal,
    f06bca_f06_bank_capital_adequacy_capdynz_21d_base_v039_signal,
    f06bca_f06_bank_capital_adequacy_capdynz_63d_base_v040_signal,
    f06bca_f06_bank_capital_adequacy_capdynz_126d_base_v041_signal,
    f06bca_f06_bank_capital_adequacy_capdynz_252d_base_v042_signal,
    f06bca_f06_bank_capital_adequacy_capbufz_21d_base_v043_signal,
    f06bca_f06_bank_capital_adequacy_capbufz_63d_base_v044_signal,
    f06bca_f06_bank_capital_adequacy_capbufz_126d_base_v045_signal,
    f06bca_f06_bank_capital_adequacy_capbufz_252d_base_v046_signal,
    f06bca_f06_bank_capital_adequacy_capratioema_10d_base_v047_signal,
    f06bca_f06_bank_capital_adequacy_capratioema_21d_base_v048_signal,
    f06bca_f06_bank_capital_adequacy_capratioema_63d_base_v049_signal,
    f06bca_f06_bank_capital_adequacy_capratioema_126d_base_v050_signal,
    f06bca_f06_bank_capital_adequacy_capratioema_252d_base_v051_signal,
    f06bca_f06_bank_capital_adequacy_capratiolog_21d_base_v052_signal,
    f06bca_f06_bank_capital_adequacy_capratiolog_63d_base_v053_signal,
    f06bca_f06_bank_capital_adequacy_capratiolog_252d_base_v054_signal,
    f06bca_f06_bank_capital_adequacy_capbuflog_21d_base_v055_signal,
    f06bca_f06_bank_capital_adequacy_capbuflog_63d_base_v056_signal,
    f06bca_f06_bank_capital_adequacy_capbuflog_252d_base_v057_signal,
    f06bca_f06_bank_capital_adequacy_capratioxcdv_21d_base_v058_signal,
    f06bca_f06_bank_capital_adequacy_capratioxcdv_63d_base_v059_signal,
    f06bca_f06_bank_capital_adequacy_capratioxcdv_126d_base_v060_signal,
    f06bca_f06_bank_capital_adequacy_capdynxbuf_21d_base_v061_signal,
    f06bca_f06_bank_capital_adequacy_capdynxbuf_63d_base_v062_signal,
    f06bca_f06_bank_capital_adequacy_capdynxbuf_126d_base_v063_signal,
    f06bca_f06_bank_capital_adequacy_capdynxbuf_252d_base_v064_signal,
    f06bca_f06_bank_capital_adequacy_capratiochg_5d_base_v065_signal,
    f06bca_f06_bank_capital_adequacy_capratiochg_21d_base_v066_signal,
    f06bca_f06_bank_capital_adequacy_capratiochg_63d_base_v067_signal,
    f06bca_f06_bank_capital_adequacy_capratiochg_126d_base_v068_signal,
    f06bca_f06_bank_capital_adequacy_capratiochg_252d_base_v069_signal,
    f06bca_f06_bank_capital_adequacy_capbufchg_5d_base_v070_signal,
    f06bca_f06_bank_capital_adequacy_capbufchg_21d_base_v071_signal,
    f06bca_f06_bank_capital_adequacy_capbufchg_63d_base_v072_signal,
    f06bca_f06_bank_capital_adequacy_capbufchg_126d_base_v073_signal,
    f06bca_f06_bank_capital_adequacy_capbufchg_252d_base_v074_signal,
    f06bca_f06_bank_capital_adequacy_capratiorange_21d_base_v075_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F06_BANK_CAPITAL_ADEQUACY_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f06_bank_capital_adequacy_base_001_075_claude: {n_features} features pass")
