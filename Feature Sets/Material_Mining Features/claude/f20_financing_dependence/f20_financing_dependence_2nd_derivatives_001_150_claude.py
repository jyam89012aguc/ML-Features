import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_FIVEYEAR = 1260
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


def _rsum(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 3)).rank(pct=True) - 0.5


def _f20_burn(ncfo):
    return (-ncfo).clip(lower=0)


def _f20_raise(ncff):
    return ncff.clip(lower=0)


def _f20_fin_cover(ncff, ncfo, w):
    burn = _rsum(_f20_burn(ncfo), w)
    fin = _rsum(_f20_raise(ncff), w)
    return fin / burn.replace(0, np.nan)


def _f20_dependence(ncff, ncfo, w):
    a = _rsum(ncff.abs(), w)
    b = _rsum(ncfo.abs(), w)
    return a / b.replace(0, np.nan)


def _f20_eqdebt_mix(ncfcommon, ncfdebt, w):
    eq = _rsum(ncfcommon.clip(lower=0), w)
    dt = _rsum(ncfdebt.clip(lower=0), w)
    return (eq - dt) / (eq + dt).replace(0, np.nan)


def _f20_selffund_gap(ncfo, ncfi, ncff, w):
    internal = _rsum(ncfo + ncfi, w)
    external = _rsum(ncff, w)
    return external / (internal.abs() + external.abs()).replace(0, np.nan)



def f20fd_f20_financing_dependence_relid_252d_slope_v001_signal(ncff, ncfo):
    base = _f20_dependence(ncff, ncfo, 252)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_relidz_126d_slope_v002_signal(ncff, ncfo):
    base = _f20_dependence(ncff, ncfo, 126)
    deriv = _z(base - base.shift(21), 63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_relidn_504d_slope_v003_signal(ncff, ncfo):
    base = _f20_dependence(ncff, ncfo, 504)
    sc = base.rolling(504, min_periods=252).std().replace(0, np.nan)
    deriv = (base - base.shift(63)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_relid_189d_slope_v004_signal(ncff, ncfo):
    base = _f20_dependence(ncff, ncfo, 189)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_coverdz_252d_slope_v005_signal(ncff, ncfo):
    base = _f20_fin_cover(ncff, ncfo, 252)
    deriv = _z(base - base.shift(21), 126)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_coverdn_126d_slope_v006_signal(ncff, ncfo):
    base = _f20_fin_cover(ncff, ncfo, 126)
    sc = base.rolling(126, min_periods=63).std().replace(0, np.nan)
    deriv = (base - base.shift(21)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_coverd_504d_slope_v007_signal(ncff, ncfo):
    base = _f20_fin_cover(ncff, ncfo, 504)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_coverdz_189d_slope_v008_signal(ncff, ncfo):
    base = _f20_fin_cover(ncff, ncfo, 189)
    deriv = _z(base - base.shift(21), 94)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_eqdebtdn_252d_slope_v009_signal(ncfcommon, ncfdebt):
    base = _f20_eqdebt_mix(ncfcommon, ncfdebt, 252)
    sc = base.rolling(252, min_periods=126).std().replace(0, np.nan)
    deriv = (base - base.shift(21)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_eqdebtd_126d_slope_v010_signal(ncfcommon, ncfdebt):
    base = _f20_eqdebt_mix(ncfcommon, ncfdebt, 126)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_eqdebtdz_504d_slope_v011_signal(ncfcommon, ncfdebt):
    base = _f20_eqdebt_mix(ncfcommon, ncfdebt, 504)
    deriv = _z(base - base.shift(63), 252)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_eqdebtdn_189d_slope_v012_signal(ncfcommon, ncfdebt):
    base = _f20_eqdebt_mix(ncfcommon, ncfdebt, 189)
    sc = base.rolling(189, min_periods=94).std().replace(0, np.nan)
    deriv = (base - base.shift(21)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_selfgapd_252d_slope_v013_signal(ncfo, ncfi, ncff):
    base = _f20_selffund_gap(ncfo, ncfi, ncff, 252)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_selfgapdz_126d_slope_v014_signal(ncfo, ncfi, ncff):
    base = _f20_selffund_gap(ncfo, ncfi, ncff, 126)
    deriv = _z(base - base.shift(21), 63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_selfgapdn_504d_slope_v015_signal(ncfo, ncfi, ncff):
    base = _f20_selffund_gap(ncfo, ncfi, ncff, 504)
    sc = base.rolling(504, min_periods=252).std().replace(0, np.nan)
    deriv = (base - base.shift(63)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_selfgapd_189d_slope_v016_signal(ncfo, ncfi, ncff):
    base = _f20_selffund_gap(ncfo, ncfi, ncff, 189)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_raisesharedz_252d_slope_v017_signal(ncff, ncfo, ncfi):
    rz = _rsum(_f20_raise(ncff), 252)
    inflow = _rsum(ncfo.clip(lower=0) + ncfi.clip(lower=0), 252)
    base = rz / (rz + inflow).replace(0, np.nan)
    deriv = _z(base - base.shift(21), 126)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_raisesharedn_126d_slope_v018_signal(ncff, ncfo, ncfi):
    rz = _rsum(_f20_raise(ncff), 126)
    inflow = _rsum(ncfo.clip(lower=0) + ncfi.clip(lower=0), 126)
    base = rz / (rz + inflow).replace(0, np.nan)
    sc = base.rolling(126, min_periods=63).std().replace(0, np.nan)
    deriv = (base - base.shift(21)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_raiseshared_504d_slope_v019_signal(ncff, ncfo, ncfi):
    rz = _rsum(_f20_raise(ncff), 504)
    inflow = _rsum(ncfo.clip(lower=0) + ncfi.clip(lower=0), 504)
    base = rz / (rz + inflow).replace(0, np.nan)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_raisesharedz_189d_slope_v020_signal(ncff, ncfo, ncfi):
    rz = _rsum(_f20_raise(ncff), 189)
    inflow = _rsum(ncfo.clip(lower=0) + ncfi.clip(lower=0), 189)
    base = rz / (rz + inflow).replace(0, np.nan)
    deriv = _z(base - base.shift(21), 94)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_netfinturndn_252d_slope_v021_signal(ncff, ncfo, ncfi):
    nf = _rsum(ncff, 252)
    turn = _rsum(ncff.abs() + ncfo.abs() + ncfi.abs(), 252)
    base = nf / turn.replace(0, np.nan)
    sc = base.rolling(252, min_periods=126).std().replace(0, np.nan)
    deriv = (base - base.shift(21)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_netfinturnd_126d_slope_v022_signal(ncff, ncfo, ncfi):
    nf = _rsum(ncff, 126)
    turn = _rsum(ncff.abs() + ncfo.abs() + ncfi.abs(), 126)
    base = nf / turn.replace(0, np.nan)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_netfinturndz_504d_slope_v023_signal(ncff, ncfo, ncfi):
    nf = _rsum(ncff, 504)
    turn = _rsum(ncff.abs() + ncfo.abs() + ncfi.abs(), 504)
    base = nf / turn.replace(0, np.nan)
    deriv = _z(base - base.shift(63), 252)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_netfinturndn_189d_slope_v024_signal(ncff, ncfo, ncfi):
    nf = _rsum(ncff, 189)
    turn = _rsum(ncff.abs() + ncfo.abs() + ncfi.abs(), 189)
    base = nf / turn.replace(0, np.nan)
    sc = base.rolling(189, min_periods=94).std().replace(0, np.nan)
    deriv = (base - base.shift(21)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_eqburnd_252d_slope_v025_signal(ncfcommon, ncfo):
    eq = _rsum(ncfcommon.clip(lower=0), 252)
    burn = _rsum(_f20_burn(ncfo), 252)
    base = eq / (eq + burn).replace(0, np.nan)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_eqburndz_126d_slope_v026_signal(ncfcommon, ncfo):
    eq = _rsum(ncfcommon.clip(lower=0), 126)
    burn = _rsum(_f20_burn(ncfo), 126)
    base = eq / (eq + burn).replace(0, np.nan)
    deriv = _z(base - base.shift(21), 63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_eqburndn_504d_slope_v027_signal(ncfcommon, ncfo):
    eq = _rsum(ncfcommon.clip(lower=0), 504)
    burn = _rsum(_f20_burn(ncfo), 504)
    base = eq / (eq + burn).replace(0, np.nan)
    sc = base.rolling(504, min_periods=252).std().replace(0, np.nan)
    deriv = (base - base.shift(63)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_eqburnd_189d_slope_v028_signal(ncfcommon, ncfo):
    eq = _rsum(ncfcommon.clip(lower=0), 189)
    burn = _rsum(_f20_burn(ncfo), 189)
    base = eq / (eq + burn).replace(0, np.nan)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_dtburndz_252d_slope_v029_signal(ncfdebt, ncfo):
    dt = _rsum(ncfdebt.clip(lower=0), 252)
    burn = _rsum(_f20_burn(ncfo), 252)
    base = (dt - burn) / (dt + burn).replace(0, np.nan)
    deriv = _z(base - base.shift(21), 126)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_dtburndn_126d_slope_v030_signal(ncfdebt, ncfo):
    dt = _rsum(ncfdebt.clip(lower=0), 126)
    burn = _rsum(_f20_burn(ncfo), 126)
    base = (dt - burn) / (dt + burn).replace(0, np.nan)
    sc = base.rolling(126, min_periods=63).std().replace(0, np.nan)
    deriv = (base - base.shift(21)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_dtburnd_504d_slope_v031_signal(ncfdebt, ncfo):
    dt = _rsum(ncfdebt.clip(lower=0), 504)
    burn = _rsum(_f20_burn(ncfo), 504)
    base = (dt - burn) / (dt + burn).replace(0, np.nan)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_dtburndz_189d_slope_v032_signal(ncfdebt, ncfo):
    dt = _rsum(ncfdebt.clip(lower=0), 189)
    burn = _rsum(_f20_burn(ncfo), 189)
    base = (dt - burn) / (dt + burn).replace(0, np.nan)
    deriv = _z(base - base.shift(21), 94)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_debtrelidn_252d_slope_v033_signal(ncfdebt, ncfo):
    base = _rsum(ncfdebt.abs(), 252) / _rsum(ncfo.abs(), 252).replace(0, np.nan)
    sc = base.rolling(252, min_periods=126).std().replace(0, np.nan)
    deriv = (base - base.shift(21)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_debtrelid_126d_slope_v034_signal(ncfdebt, ncfo):
    base = _rsum(ncfdebt.abs(), 126) / _rsum(ncfo.abs(), 126).replace(0, np.nan)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_debtrelidz_504d_slope_v035_signal(ncfdebt, ncfo):
    base = _rsum(ncfdebt.abs(), 504) / _rsum(ncfo.abs(), 504).replace(0, np.nan)
    deriv = _z(base - base.shift(63), 252)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_debtrelidn_189d_slope_v036_signal(ncfdebt, ncfo):
    base = _rsum(ncfdebt.abs(), 189) / _rsum(ncfo.abs(), 189).replace(0, np.nan)
    sc = base.rolling(189, min_periods=94).std().replace(0, np.nan)
    deriv = (base - base.shift(21)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_eqrelid_252d_slope_v037_signal(ncfcommon, ncfo):
    r = _rsum(ncfcommon.abs(), 252) / _rsum(ncfo.abs(), 252).replace(0, np.nan)
    base = np.log1p(r)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_eqrelidz_126d_slope_v038_signal(ncfcommon, ncfo):
    r = _rsum(ncfcommon.abs(), 126) / _rsum(ncfo.abs(), 126).replace(0, np.nan)
    base = np.log1p(r)
    deriv = _z(base - base.shift(21), 63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_eqrelidn_504d_slope_v039_signal(ncfcommon, ncfo):
    r = _rsum(ncfcommon.abs(), 504) / _rsum(ncfo.abs(), 504).replace(0, np.nan)
    base = np.log1p(r)
    sc = base.rolling(504, min_periods=252).std().replace(0, np.nan)
    deriv = (base - base.shift(63)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_eqrelid_189d_slope_v040_signal(ncfcommon, ncfo):
    r = _rsum(ncfcommon.abs(), 189) / _rsum(ncfo.abs(), 189).replace(0, np.nan)
    base = np.log1p(r)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_netdebtflowdz_252d_slope_v041_signal(ncfdebt, ncff):
    base = _rsum(ncfdebt, 252) / _rsum(ncff.abs(), 252).replace(0, np.nan)
    deriv = _z(base - base.shift(21), 126)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_netdebtflowdn_126d_slope_v042_signal(ncfdebt, ncff):
    base = _rsum(ncfdebt, 126) / _rsum(ncff.abs(), 126).replace(0, np.nan)
    sc = base.rolling(126, min_periods=63).std().replace(0, np.nan)
    deriv = (base - base.shift(21)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_netdebtflowd_504d_slope_v043_signal(ncfdebt, ncff):
    base = _rsum(ncfdebt, 504) / _rsum(ncff.abs(), 504).replace(0, np.nan)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_netdebtflowdz_189d_slope_v044_signal(ncfdebt, ncff):
    base = _rsum(ncfdebt, 189) / _rsum(ncff.abs(), 189).replace(0, np.nan)
    deriv = _z(base - base.shift(21), 94)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_neteqflowdn_252d_slope_v045_signal(ncfcommon, ncff):
    base = _rsum(ncfcommon, 252) / _rsum(ncff.abs(), 252).replace(0, np.nan)
    sc = base.rolling(252, min_periods=126).std().replace(0, np.nan)
    deriv = (base - base.shift(21)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_neteqflowd_126d_slope_v046_signal(ncfcommon, ncff):
    base = _rsum(ncfcommon, 126) / _rsum(ncff.abs(), 126).replace(0, np.nan)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_neteqflowdz_504d_slope_v047_signal(ncfcommon, ncff):
    base = _rsum(ncfcommon, 504) / _rsum(ncff.abs(), 504).replace(0, np.nan)
    deriv = _z(base - base.shift(63), 252)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_neteqflowdn_189d_slope_v048_signal(ncfcommon, ncff):
    base = _rsum(ncfcommon, 189) / _rsum(ncff.abs(), 189).replace(0, np.nan)
    sc = base.rolling(189, min_periods=94).std().replace(0, np.nan)
    deriv = (base - base.shift(21)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_finvsinvd_252d_slope_v049_signal(ncff, ncfi):
    fin = _rsum(_f20_raise(ncff), 252)
    inv = _rsum((-ncfi).clip(lower=0), 252)
    base = fin / (fin + inv).replace(0, np.nan)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_finvsinvdz_126d_slope_v050_signal(ncff, ncfi):
    fin = _rsum(_f20_raise(ncff), 126)
    inv = _rsum((-ncfi).clip(lower=0), 126)
    base = fin / (fin + inv).replace(0, np.nan)
    deriv = _z(base - base.shift(21), 63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_finvsinvdn_504d_slope_v051_signal(ncff, ncfi):
    fin = _rsum(_f20_raise(ncff), 504)
    inv = _rsum((-ncfi).clip(lower=0), 504)
    base = fin / (fin + inv).replace(0, np.nan)
    sc = base.rolling(504, min_periods=252).std().replace(0, np.nan)
    deriv = (base - base.shift(63)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_finvsinvd_189d_slope_v052_signal(ncff, ncfi):
    fin = _rsum(_f20_raise(ncff), 189)
    inv = _rsum((-ncfi).clip(lower=0), 189)
    base = fin / (fin + inv).replace(0, np.nan)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_extvsneeddz_252d_slope_v053_signal(ncfcommon, ncfdebt, ncfo, ncfi):
    raises = _rsum(ncfcommon.clip(lower=0) + ncfdebt.clip(lower=0), 252)
    needs = _rsum(_f20_burn(ncfo) + (-ncfi).clip(lower=0), 252)
    base = raises / needs.replace(0, np.nan)
    deriv = _z(base - base.shift(21), 126)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_extvsneeddn_126d_slope_v054_signal(ncfcommon, ncfdebt, ncfo, ncfi):
    raises = _rsum(ncfcommon.clip(lower=0) + ncfdebt.clip(lower=0), 126)
    needs = _rsum(_f20_burn(ncfo) + (-ncfi).clip(lower=0), 126)
    base = raises / needs.replace(0, np.nan)
    sc = base.rolling(126, min_periods=63).std().replace(0, np.nan)
    deriv = (base - base.shift(21)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_extvsneedd_504d_slope_v055_signal(ncfcommon, ncfdebt, ncfo, ncfi):
    raises = _rsum(ncfcommon.clip(lower=0) + ncfdebt.clip(lower=0), 504)
    needs = _rsum(_f20_burn(ncfo) + (-ncfi).clip(lower=0), 504)
    base = raises / needs.replace(0, np.nan)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_extvsneeddz_189d_slope_v056_signal(ncfcommon, ncfdebt, ncfo, ncfi):
    raises = _rsum(ncfcommon.clip(lower=0) + ncfdebt.clip(lower=0), 189)
    needs = _rsum(_f20_burn(ncfo) + (-ncfi).clip(lower=0), 189)
    base = raises / needs.replace(0, np.nan)
    deriv = _z(base - base.shift(21), 94)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_netfinburndn_252d_slope_v057_signal(ncff, ncfo):
    nf = _rsum(ncff, 252)
    burn = _rsum(_f20_burn(ncfo), 252)
    base = np.arctan(nf / (burn + 1.0))
    sc = base.rolling(252, min_periods=126).std().replace(0, np.nan)
    deriv = (base - base.shift(21)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_netfinburnd_126d_slope_v058_signal(ncff, ncfo):
    nf = _rsum(ncff, 126)
    burn = _rsum(_f20_burn(ncfo), 126)
    base = np.arctan(nf / (burn + 1.0))
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_netfinburndz_504d_slope_v059_signal(ncff, ncfo):
    nf = _rsum(ncff, 504)
    burn = _rsum(_f20_burn(ncfo), 504)
    base = np.arctan(nf / (burn + 1.0))
    deriv = _z(base - base.shift(63), 252)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_netfinburndn_189d_slope_v060_signal(ncff, ncfo):
    nf = _rsum(ncff, 189)
    burn = _rsum(_f20_burn(ncfo), 189)
    base = np.arctan(nf / (burn + 1.0))
    sc = base.rolling(189, min_periods=94).std().replace(0, np.nan)
    deriv = (base - base.shift(21)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_findird_252d_slope_v061_signal(ncff):
    base = _rsum(ncff, 252) / _rsum(ncff.abs(), 252).replace(0, np.nan)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_findirdz_126d_slope_v062_signal(ncff):
    base = _rsum(ncff, 126) / _rsum(ncff.abs(), 126).replace(0, np.nan)
    deriv = _z(base - base.shift(21), 63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_findirdn_504d_slope_v063_signal(ncff):
    base = _rsum(ncff, 504) / _rsum(ncff.abs(), 504).replace(0, np.nan)
    sc = base.rolling(504, min_periods=252).std().replace(0, np.nan)
    deriv = (base - base.shift(63)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_findird_189d_slope_v064_signal(ncff):
    base = _rsum(ncff, 189) / _rsum(ncff.abs(), 189).replace(0, np.nan)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_opcoversinvdz_252d_slope_v065_signal(ncfo, ncfi):
    op = _rsum(ncfo.clip(lower=0), 252)
    inv = _rsum((-ncfi).clip(lower=0), 252)
    base = op / (op + inv).replace(0, np.nan)
    deriv = _z(base - base.shift(21), 126)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_opcoversinvdn_126d_slope_v066_signal(ncfo, ncfi):
    op = _rsum(ncfo.clip(lower=0), 126)
    inv = _rsum((-ncfi).clip(lower=0), 126)
    base = op / (op + inv).replace(0, np.nan)
    sc = base.rolling(126, min_periods=63).std().replace(0, np.nan)
    deriv = (base - base.shift(21)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_opcoversinvd_504d_slope_v067_signal(ncfo, ncfi):
    op = _rsum(ncfo.clip(lower=0), 504)
    inv = _rsum((-ncfi).clip(lower=0), 504)
    base = op / (op + inv).replace(0, np.nan)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_opcoversinvdz_189d_slope_v068_signal(ncfo, ncfi):
    op = _rsum(ncfo.clip(lower=0), 189)
    inv = _rsum((-ncfi).clip(lower=0), 189)
    base = op / (op + inv).replace(0, np.nan)
    deriv = _z(base - base.shift(21), 94)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_mixbalancedn_252d_slope_v069_signal(ncfcommon, ncfdebt):
    eq = _rsum(ncfcommon.clip(lower=0), 252)
    dt = _rsum(ncfdebt.clip(lower=0), 252)
    p = (eq / (eq + dt).replace(0, np.nan)).clip(1e-6, 1 - 1e-6)
    base = -(p * np.log(p) + (1 - p) * np.log(1 - p))
    sc = base.rolling(252, min_periods=126).std().replace(0, np.nan)
    deriv = (base - base.shift(21)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_mixbalanced_126d_slope_v070_signal(ncfcommon, ncfdebt):
    eq = _rsum(ncfcommon.clip(lower=0), 126)
    dt = _rsum(ncfdebt.clip(lower=0), 126)
    p = (eq / (eq + dt).replace(0, np.nan)).clip(1e-6, 1 - 1e-6)
    base = -(p * np.log(p) + (1 - p) * np.log(1 - p))
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_mixbalancedz_504d_slope_v071_signal(ncfcommon, ncfdebt):
    eq = _rsum(ncfcommon.clip(lower=0), 504)
    dt = _rsum(ncfdebt.clip(lower=0), 504)
    p = (eq / (eq + dt).replace(0, np.nan)).clip(1e-6, 1 - 1e-6)
    base = -(p * np.log(p) + (1 - p) * np.log(1 - p))
    deriv = _z(base - base.shift(63), 252)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_mixbalancedn_189d_slope_v072_signal(ncfcommon, ncfdebt):
    eq = _rsum(ncfcommon.clip(lower=0), 189)
    dt = _rsum(ncfdebt.clip(lower=0), 189)
    p = (eq / (eq + dt).replace(0, np.nan)).clip(1e-6, 1 - 1e-6)
    base = -(p * np.log(p) + (1 - p) * np.log(1 - p))
    sc = base.rolling(189, min_periods=94).std().replace(0, np.nan)
    deriv = (base - base.shift(21)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_finfootprintd_252d_slope_v073_signal(ncff, ncfo, ncfi):
    fin = _rsum(ncff.abs(), 252)
    tot = _rsum(ncff.abs() + ncfo.abs() + ncfi.abs(), 252)
    base = fin / tot.replace(0, np.nan)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_finfootprintdz_126d_slope_v074_signal(ncff, ncfo, ncfi):
    fin = _rsum(ncff.abs(), 126)
    tot = _rsum(ncff.abs() + ncfo.abs() + ncfi.abs(), 126)
    base = fin / tot.replace(0, np.nan)
    deriv = _z(base - base.shift(21), 63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_finfootprintdn_504d_slope_v075_signal(ncff, ncfo, ncfi):
    fin = _rsum(ncff.abs(), 504)
    tot = _rsum(ncff.abs() + ncfo.abs() + ncfi.abs(), 504)
    base = fin / tot.replace(0, np.nan)
    sc = base.rolling(504, min_periods=252).std().replace(0, np.nan)
    deriv = (base - base.shift(63)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_finfootprintd_189d_slope_v076_signal(ncff, ncfo, ncfi):
    fin = _rsum(ncff.abs(), 189)
    tot = _rsum(ncff.abs() + ncfo.abs() + ncfi.abs(), 189)
    base = fin / tot.replace(0, np.nan)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_extofraiseddz_252d_slope_v077_signal(ncff, ncfo):
    ext = _rsum(_f20_raise(ncff), 252)
    op_in = _rsum(ncfo.clip(lower=0), 252)
    base = ext / (ext + op_in).replace(0, np.nan)
    deriv = _z(base - base.shift(21), 126)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_extofraiseddn_126d_slope_v078_signal(ncff, ncfo):
    ext = _rsum(_f20_raise(ncff), 126)
    op_in = _rsum(ncfo.clip(lower=0), 126)
    base = ext / (ext + op_in).replace(0, np.nan)
    sc = base.rolling(126, min_periods=63).std().replace(0, np.nan)
    deriv = (base - base.shift(21)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_extofraisedd_504d_slope_v079_signal(ncff, ncfo):
    ext = _rsum(_f20_raise(ncff), 504)
    op_in = _rsum(ncfo.clip(lower=0), 504)
    base = ext / (ext + op_in).replace(0, np.nan)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_extofraiseddz_189d_slope_v080_signal(ncff, ncfo):
    ext = _rsum(_f20_raise(ncff), 189)
    op_in = _rsum(ncfo.clip(lower=0), 189)
    base = ext / (ext + op_in).replace(0, np.nan)
    deriv = _z(base - base.shift(21), 94)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_dtopsdn_252d_slope_v081_signal(ncfdebt, ncfo):
    base = _rsum(ncfdebt, 252) / _rsum(ncfo.abs(), 252).replace(0, np.nan)
    sc = base.rolling(252, min_periods=126).std().replace(0, np.nan)
    deriv = (base - base.shift(21)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_dtopsd_126d_slope_v082_signal(ncfdebt, ncfo):
    base = _rsum(ncfdebt, 126) / _rsum(ncfo.abs(), 126).replace(0, np.nan)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_dtopsdz_504d_slope_v083_signal(ncfdebt, ncfo):
    base = _rsum(ncfdebt, 504) / _rsum(ncfo.abs(), 504).replace(0, np.nan)
    deriv = _z(base - base.shift(63), 252)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_dtopsdn_189d_slope_v084_signal(ncfdebt, ncfo):
    base = _rsum(ncfdebt, 189) / _rsum(ncfo.abs(), 189).replace(0, np.nan)
    sc = base.rolling(189, min_periods=94).std().replace(0, np.nan)
    deriv = (base - base.shift(21)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_eqopsd_252d_slope_v085_signal(ncfcommon, ncfo):
    base = _rsum(ncfcommon, 252) / _rsum(ncfo.abs(), 252).replace(0, np.nan)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_eqopsdz_126d_slope_v086_signal(ncfcommon, ncfo):
    base = _rsum(ncfcommon, 126) / _rsum(ncfo.abs(), 126).replace(0, np.nan)
    deriv = _z(base - base.shift(21), 63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_eqopsdn_504d_slope_v087_signal(ncfcommon, ncfo):
    base = _rsum(ncfcommon, 504) / _rsum(ncfo.abs(), 504).replace(0, np.nan)
    sc = base.rolling(504, min_periods=252).std().replace(0, np.nan)
    deriv = (base - base.shift(63)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_eqopsd_189d_slope_v088_signal(ncfcommon, ncfo):
    base = _rsum(ncfcommon, 189) / _rsum(ncfo.abs(), 189).replace(0, np.nan)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_finperopdz_252d_slope_v089_signal(ncff, ncfo):
    nf = _rsum(ncff, 252)
    op = _rsum(ncfo, 252)
    base = nf / (nf.abs() + op.abs()).replace(0, np.nan)
    deriv = _z(base - base.shift(21), 126)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_finperopdn_126d_slope_v090_signal(ncff, ncfo):
    nf = _rsum(ncff, 126)
    op = _rsum(ncfo, 126)
    base = nf / (nf.abs() + op.abs()).replace(0, np.nan)
    sc = base.rolling(126, min_periods=63).std().replace(0, np.nan)
    deriv = (base - base.shift(21)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_finperopd_504d_slope_v091_signal(ncff, ncfo):
    nf = _rsum(ncff, 504)
    op = _rsum(ncfo, 504)
    base = nf / (nf.abs() + op.abs()).replace(0, np.nan)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_finperopdz_189d_slope_v092_signal(ncff, ncfo):
    nf = _rsum(ncff, 189)
    op = _rsum(ncfo, 189)
    base = nf / (nf.abs() + op.abs()).replace(0, np.nan)
    deriv = _z(base - base.shift(21), 94)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_intfundsharedn_252d_slope_v093_signal(ncfo, ncff, ncfi):
    op_in = _rsum(ncfo.clip(lower=0), 252)
    ext_in = _rsum(ncff.clip(lower=0) + ncfi.clip(lower=0), 252)
    base = np.log((op_in + 1.0) / (ext_in + 1.0))
    sc = base.rolling(252, min_periods=126).std().replace(0, np.nan)
    deriv = (base - base.shift(21)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_intfundshared_126d_slope_v094_signal(ncfo, ncff, ncfi):
    op_in = _rsum(ncfo.clip(lower=0), 126)
    ext_in = _rsum(ncff.clip(lower=0) + ncfi.clip(lower=0), 126)
    base = np.log((op_in + 1.0) / (ext_in + 1.0))
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_intfundsharedz_504d_slope_v095_signal(ncfo, ncff, ncfi):
    op_in = _rsum(ncfo.clip(lower=0), 504)
    ext_in = _rsum(ncff.clip(lower=0) + ncfi.clip(lower=0), 504)
    base = np.log((op_in + 1.0) / (ext_in + 1.0))
    deriv = _z(base - base.shift(63), 252)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_intfundsharedn_189d_slope_v096_signal(ncfo, ncff, ncfi):
    op_in = _rsum(ncfo.clip(lower=0), 189)
    ext_in = _rsum(ncff.clip(lower=0) + ncfi.clip(lower=0), 189)
    base = np.log((op_in + 1.0) / (ext_in + 1.0))
    sc = base.rolling(189, min_periods=94).std().replace(0, np.nan)
    deriv = (base - base.shift(21)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_finasymd_252d_slope_v097_signal(ncff, ncfo):
    inflow = _rsum(ncff.clip(lower=0), 252)
    outflow = _rsum((-ncff).clip(lower=0), 252)
    burn = _rsum(_f20_burn(ncfo), 252)
    base = (inflow - outflow) / (inflow + outflow + burn).replace(0, np.nan)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_finasymdz_126d_slope_v098_signal(ncff, ncfo):
    inflow = _rsum(ncff.clip(lower=0), 126)
    outflow = _rsum((-ncff).clip(lower=0), 126)
    burn = _rsum(_f20_burn(ncfo), 126)
    base = (inflow - outflow) / (inflow + outflow + burn).replace(0, np.nan)
    deriv = _z(base - base.shift(21), 63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_finasymdn_504d_slope_v099_signal(ncff, ncfo):
    inflow = _rsum(ncff.clip(lower=0), 504)
    outflow = _rsum((-ncff).clip(lower=0), 504)
    burn = _rsum(_f20_burn(ncfo), 504)
    base = (inflow - outflow) / (inflow + outflow + burn).replace(0, np.nan)
    sc = base.rolling(504, min_periods=252).std().replace(0, np.nan)
    deriv = (base - base.shift(63)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_finasymd_189d_slope_v100_signal(ncff, ncfo):
    inflow = _rsum(ncff.clip(lower=0), 189)
    outflow = _rsum((-ncff).clip(lower=0), 189)
    burn = _rsum(_f20_burn(ncfo), 189)
    base = (inflow - outflow) / (inflow + outflow + burn).replace(0, np.nan)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_dtrepaydz_252d_slope_v101_signal(ncfdebt, ncfo):
    repay = _rsum((-ncfdebt).clip(lower=0), 252)
    burn = _rsum(_f20_burn(ncfo), 252)
    base = repay / (repay + burn).replace(0, np.nan)
    deriv = _z(base - base.shift(21), 126)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_dtrepaydn_126d_slope_v102_signal(ncfdebt, ncfo):
    repay = _rsum((-ncfdebt).clip(lower=0), 126)
    burn = _rsum(_f20_burn(ncfo), 126)
    base = repay / (repay + burn).replace(0, np.nan)
    sc = base.rolling(126, min_periods=63).std().replace(0, np.nan)
    deriv = (base - base.shift(21)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_dtrepayd_504d_slope_v103_signal(ncfdebt, ncfo):
    repay = _rsum((-ncfdebt).clip(lower=0), 504)
    burn = _rsum(_f20_burn(ncfo), 504)
    base = repay / (repay + burn).replace(0, np.nan)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_dtrepaydz_189d_slope_v104_signal(ncfdebt, ncfo):
    repay = _rsum((-ncfdebt).clip(lower=0), 189)
    burn = _rsum(_f20_burn(ncfo), 189)
    base = repay / (repay + burn).replace(0, np.nan)
    deriv = _z(base - base.shift(21), 94)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_eqnetdirdn_252d_slope_v105_signal(ncfcommon):
    base = _rsum(ncfcommon, 252) / _rsum(ncfcommon.abs(), 252).replace(0, np.nan)
    sc = base.rolling(252, min_periods=126).std().replace(0, np.nan)
    deriv = (base - base.shift(21)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_eqnetdird_126d_slope_v106_signal(ncfcommon):
    base = _rsum(ncfcommon, 126) / _rsum(ncfcommon.abs(), 126).replace(0, np.nan)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_eqnetdirdz_504d_slope_v107_signal(ncfcommon):
    base = _rsum(ncfcommon, 504) / _rsum(ncfcommon.abs(), 504).replace(0, np.nan)
    deriv = _z(base - base.shift(63), 252)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_eqnetdirdn_189d_slope_v108_signal(ncfcommon):
    base = _rsum(ncfcommon, 189) / _rsum(ncfcommon.abs(), 189).replace(0, np.nan)
    sc = base.rolling(189, min_periods=94).std().replace(0, np.nan)
    deriv = (base - base.shift(21)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_extcushiond_252d_slope_v109_signal(ncff, ncfo, ncfi):
    cushion = _rsum(ncff + ncfi, 252)
    scale = _rsum(ncff.abs() + ncfi.abs(), 252).replace(0, np.nan)
    base = np.tanh(cushion / scale) - _z(_rsum(_f20_burn(ncfo), 252), 252)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_extcushiondz_126d_slope_v110_signal(ncff, ncfo, ncfi):
    cushion = _rsum(ncff + ncfi, 126)
    scale = _rsum(ncff.abs() + ncfi.abs(), 126).replace(0, np.nan)
    base = np.tanh(cushion / scale) - _z(_rsum(_f20_burn(ncfo), 126), 126)
    deriv = _z(base - base.shift(21), 63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_extcushiondn_504d_slope_v111_signal(ncff, ncfo, ncfi):
    cushion = _rsum(ncff + ncfi, 504)
    scale = _rsum(ncff.abs() + ncfi.abs(), 504).replace(0, np.nan)
    base = np.tanh(cushion / scale) - _z(_rsum(_f20_burn(ncfo), 504), 504)
    sc = base.rolling(504, min_periods=252).std().replace(0, np.nan)
    deriv = (base - base.shift(63)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_extcushiond_189d_slope_v112_signal(ncff, ncfo, ncfi):
    cushion = _rsum(ncff + ncfi, 189)
    scale = _rsum(ncff.abs() + ncfi.abs(), 189).replace(0, np.nan)
    base = np.tanh(cushion / scale) - _z(_rsum(_f20_burn(ncfo), 189), 189)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_srchhidz_252d_slope_v113_signal(ncfcommon, ncfdebt):
    eq = _rsum(ncfcommon.clip(lower=0), 252)
    dt = _rsum(ncfdebt.clip(lower=0), 252)
    tot = (eq + dt).replace(0, np.nan)
    base = (eq / tot) ** 2 + (dt / tot) ** 2
    deriv = _z(base - base.shift(21), 126)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_srchhidn_126d_slope_v114_signal(ncfcommon, ncfdebt):
    eq = _rsum(ncfcommon.clip(lower=0), 126)
    dt = _rsum(ncfdebt.clip(lower=0), 126)
    tot = (eq + dt).replace(0, np.nan)
    base = (eq / tot) ** 2 + (dt / tot) ** 2
    sc = base.rolling(126, min_periods=63).std().replace(0, np.nan)
    deriv = (base - base.shift(21)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_srchhid_504d_slope_v115_signal(ncfcommon, ncfdebt):
    eq = _rsum(ncfcommon.clip(lower=0), 504)
    dt = _rsum(ncfdebt.clip(lower=0), 504)
    tot = (eq + dt).replace(0, np.nan)
    base = (eq / tot) ** 2 + (dt / tot) ** 2
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_srchhidz_189d_slope_v116_signal(ncfcommon, ncfdebt):
    eq = _rsum(ncfcommon.clip(lower=0), 189)
    dt = _rsum(ncfdebt.clip(lower=0), 189)
    tot = (eq + dt).replace(0, np.nan)
    base = (eq / tot) ** 2 + (dt / tot) ** 2
    deriv = _z(base - base.shift(21), 94)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_coverlogdn_252d_slope_v117_signal(ncff, ncfo):
    fin = _rsum(_f20_raise(ncff), 252)
    burn = _rsum(_f20_burn(ncfo), 252)
    base = np.log((fin + 1.0) / (burn + 1.0))
    sc = base.rolling(252, min_periods=126).std().replace(0, np.nan)
    deriv = (base - base.shift(21)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_coverlogd_126d_slope_v118_signal(ncff, ncfo):
    fin = _rsum(_f20_raise(ncff), 126)
    burn = _rsum(_f20_burn(ncfo), 126)
    base = np.log((fin + 1.0) / (burn + 1.0))
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_coverlogdz_504d_slope_v119_signal(ncff, ncfo):
    fin = _rsum(_f20_raise(ncff), 504)
    burn = _rsum(_f20_burn(ncfo), 504)
    base = np.log((fin + 1.0) / (burn + 1.0))
    deriv = _z(base - base.shift(63), 252)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_coverlogdn_189d_slope_v120_signal(ncff, ncfo):
    fin = _rsum(_f20_raise(ncff), 189)
    burn = _rsum(_f20_burn(ncfo), 189)
    base = np.log((fin + 1.0) / (burn + 1.0))
    sc = base.rolling(189, min_periods=94).std().replace(0, np.nan)
    deriv = (base - base.shift(21)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_finchurnd_252d_slope_v121_signal(ncff, ncfcommon, ncfdebt):
    gf = _rsum(ncff.abs(), 252)
    src = _rsum(ncfcommon.abs() + ncfdebt.abs(), 252)
    base = np.log((gf + 1.0) / (src + 1.0))
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_finchurndz_126d_slope_v122_signal(ncff, ncfcommon, ncfdebt):
    gf = _rsum(ncff.abs(), 126)
    src = _rsum(ncfcommon.abs() + ncfdebt.abs(), 126)
    base = np.log((gf + 1.0) / (src + 1.0))
    deriv = _z(base - base.shift(21), 63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_finchurndn_504d_slope_v123_signal(ncff, ncfcommon, ncfdebt):
    gf = _rsum(ncff.abs(), 504)
    src = _rsum(ncfcommon.abs() + ncfdebt.abs(), 504)
    base = np.log((gf + 1.0) / (src + 1.0))
    sc = base.rolling(504, min_periods=252).std().replace(0, np.nan)
    deriv = (base - base.shift(63)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_finchurnd_189d_slope_v124_signal(ncff, ncfcommon, ncfdebt):
    gf = _rsum(ncff.abs(), 189)
    src = _rsum(ncfcommon.abs() + ncfdebt.abs(), 189)
    base = np.log((gf + 1.0) / (src + 1.0))
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_levtiltdz_252d_slope_v125_signal(ncfdebt, ncfcommon, ncff):
    nd = _rsum(ncfdebt, 252)
    ne = _rsum(ncfcommon, 252)
    gross = _rsum(ncff.abs(), 252).replace(0, np.nan)
    base = (nd - ne) / gross
    deriv = _z(base - base.shift(21), 126)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_levtiltdn_126d_slope_v126_signal(ncfdebt, ncfcommon, ncff):
    nd = _rsum(ncfdebt, 126)
    ne = _rsum(ncfcommon, 126)
    gross = _rsum(ncff.abs(), 126).replace(0, np.nan)
    base = (nd - ne) / gross
    sc = base.rolling(126, min_periods=63).std().replace(0, np.nan)
    deriv = (base - base.shift(21)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_levtiltd_504d_slope_v127_signal(ncfdebt, ncfcommon, ncff):
    nd = _rsum(ncfdebt, 504)
    ne = _rsum(ncfcommon, 504)
    gross = _rsum(ncff.abs(), 504).replace(0, np.nan)
    base = (nd - ne) / gross
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_levtiltdz_189d_slope_v128_signal(ncfdebt, ncfcommon, ncff):
    nd = _rsum(ncfdebt, 189)
    ne = _rsum(ncfcommon, 189)
    gross = _rsum(ncff.abs(), 189).replace(0, np.nan)
    base = (nd - ne) / gross
    deriv = _z(base - base.shift(21), 94)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_residextdn_252d_slope_v129_signal(ncff, ncfo, ncfi):
    resid = _rsum(ncff + ncfo + ncfi, 252)
    scale = _rsum(ncff.abs() + ncfo.abs() + ncfi.abs(), 252).replace(0, np.nan)
    base = resid / scale
    sc = base.rolling(252, min_periods=126).std().replace(0, np.nan)
    deriv = (base - base.shift(21)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_residextd_126d_slope_v130_signal(ncff, ncfo, ncfi):
    resid = _rsum(ncff + ncfo + ncfi, 126)
    scale = _rsum(ncff.abs() + ncfo.abs() + ncfi.abs(), 126).replace(0, np.nan)
    base = resid / scale
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_residextdz_504d_slope_v131_signal(ncff, ncfo, ncfi):
    resid = _rsum(ncff + ncfo + ncfi, 504)
    scale = _rsum(ncff.abs() + ncfo.abs() + ncfi.abs(), 504).replace(0, np.nan)
    base = resid / scale
    deriv = _z(base - base.shift(63), 252)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_residextdn_189d_slope_v132_signal(ncff, ncfo, ncfi):
    resid = _rsum(ncff + ncfo + ncfi, 189)
    scale = _rsum(ncff.abs() + ncfo.abs() + ncfi.abs(), 189).replace(0, np.nan)
    base = resid / scale
    sc = base.rolling(189, min_periods=94).std().replace(0, np.nan)
    deriv = (base - base.shift(21)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_eqinshared_252d_slope_v133_signal(ncfcommon, ncff):
    base = _rsum(ncfcommon.clip(lower=0), 252) / _rsum(_f20_raise(ncff), 252).replace(0, np.nan)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_eqinsharedz_126d_slope_v134_signal(ncfcommon, ncff):
    base = _rsum(ncfcommon.clip(lower=0), 126) / _rsum(_f20_raise(ncff), 126).replace(0, np.nan)
    deriv = _z(base - base.shift(21), 63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_eqinsharedn_504d_slope_v135_signal(ncfcommon, ncff):
    base = _rsum(ncfcommon.clip(lower=0), 504) / _rsum(_f20_raise(ncff), 504).replace(0, np.nan)
    sc = base.rolling(504, min_periods=252).std().replace(0, np.nan)
    deriv = (base - base.shift(63)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_eqinshared_189d_slope_v136_signal(ncfcommon, ncff):
    base = _rsum(ncfcommon.clip(lower=0), 189) / _rsum(_f20_raise(ncff), 189).replace(0, np.nan)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_dtinsharedz_252d_slope_v137_signal(ncfdebt, ncfcommon, ncff):
    dt = _rsum(ncfdebt.clip(lower=0), 252)
    fin = _rsum(_f20_raise(ncff), 252).replace(0, np.nan)
    base = dt / fin - _rsum(ncfcommon.clip(lower=0), 252) / fin
    deriv = _z(base - base.shift(21), 126)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_dtinsharedn_126d_slope_v138_signal(ncfdebt, ncfcommon, ncff):
    dt = _rsum(ncfdebt.clip(lower=0), 126)
    fin = _rsum(_f20_raise(ncff), 126).replace(0, np.nan)
    base = dt / fin - _rsum(ncfcommon.clip(lower=0), 126) / fin
    sc = base.rolling(126, min_periods=63).std().replace(0, np.nan)
    deriv = (base - base.shift(21)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_dtinshared_504d_slope_v139_signal(ncfdebt, ncfcommon, ncff):
    dt = _rsum(ncfdebt.clip(lower=0), 504)
    fin = _rsum(_f20_raise(ncff), 504).replace(0, np.nan)
    base = dt / fin - _rsum(ncfcommon.clip(lower=0), 504) / fin
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_dtinsharedz_189d_slope_v140_signal(ncfdebt, ncfcommon, ncff):
    dt = _rsum(ncfdebt.clip(lower=0), 189)
    fin = _rsum(_f20_raise(ncff), 189).replace(0, np.nan)
    base = dt / fin - _rsum(ncfcommon.clip(lower=0), 189) / fin
    deriv = _z(base - base.shift(21), 94)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_extneedcovdn_252d_slope_v141_signal(ncff, ncfi):
    nf = _rsum(ncff, 252)
    need = _rsum((-ncfi).clip(lower=0), 252)
    base = nf / (nf.abs() + need).replace(0, np.nan)
    sc = base.rolling(252, min_periods=126).std().replace(0, np.nan)
    deriv = (base - base.shift(21)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_extneedcovd_126d_slope_v142_signal(ncff, ncfi):
    nf = _rsum(ncff, 126)
    need = _rsum((-ncfi).clip(lower=0), 126)
    base = nf / (nf.abs() + need).replace(0, np.nan)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_extneedcovdz_504d_slope_v143_signal(ncff, ncfi):
    nf = _rsum(ncff, 504)
    need = _rsum((-ncfi).clip(lower=0), 504)
    base = nf / (nf.abs() + need).replace(0, np.nan)
    deriv = _z(base - base.shift(63), 252)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_extneedcovdn_189d_slope_v144_signal(ncff, ncfi):
    nf = _rsum(ncff, 189)
    need = _rsum((-ncfi).clip(lower=0), 189)
    base = nf / (nf.abs() + need).replace(0, np.nan)
    sc = base.rolling(189, min_periods=94).std().replace(0, np.nan)
    deriv = (base - base.shift(21)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_netrelind_252d_slope_v145_signal(ncff, ncfo):
    base = _rsum(ncff, 252) / _rsum(ncfo.abs(), 252).replace(0, np.nan)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_netrelindz_126d_slope_v146_signal(ncff, ncfo):
    base = _rsum(ncff, 126) / _rsum(ncfo.abs(), 126).replace(0, np.nan)
    deriv = _z(base - base.shift(21), 63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_netrelindn_504d_slope_v147_signal(ncff, ncfo):
    base = _rsum(ncff, 504) / _rsum(ncfo.abs(), 504).replace(0, np.nan)
    sc = base.rolling(504, min_periods=252).std().replace(0, np.nan)
    deriv = (base - base.shift(63)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_netrelind_189d_slope_v148_signal(ncff, ncfo):
    base = _rsum(ncff, 189) / _rsum(ncfo.abs(), 189).replace(0, np.nan)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_dtveqmixdz_252d_slope_v149_signal(ncfdebt, ncfcommon):
    dt = _rsum(ncfdebt.abs(), 252)
    eq = _rsum(ncfcommon.abs(), 252)
    base = (dt - eq) / (dt + eq).replace(0, np.nan)
    deriv = _z(base - base.shift(21), 126)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f20fd_f20_financing_dependence_dtveqmixdn_126d_slope_v150_signal(ncfdebt, ncfcommon):
    dt = _rsum(ncfdebt.abs(), 126)
    eq = _rsum(ncfcommon.abs(), 126)
    base = (dt - eq) / (dt + eq).replace(0, np.nan)
    sc = base.rolling(126, min_periods=63).std().replace(0, np.nan)
    deriv = (base - base.shift(21)) / sc
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f20fd_f20_financing_dependence_relid_252d_slope_v001_signal,
    f20fd_f20_financing_dependence_relidz_126d_slope_v002_signal,
    f20fd_f20_financing_dependence_relidn_504d_slope_v003_signal,
    f20fd_f20_financing_dependence_relid_189d_slope_v004_signal,
    f20fd_f20_financing_dependence_coverdz_252d_slope_v005_signal,
    f20fd_f20_financing_dependence_coverdn_126d_slope_v006_signal,
    f20fd_f20_financing_dependence_coverd_504d_slope_v007_signal,
    f20fd_f20_financing_dependence_coverdz_189d_slope_v008_signal,
    f20fd_f20_financing_dependence_eqdebtdn_252d_slope_v009_signal,
    f20fd_f20_financing_dependence_eqdebtd_126d_slope_v010_signal,
    f20fd_f20_financing_dependence_eqdebtdz_504d_slope_v011_signal,
    f20fd_f20_financing_dependence_eqdebtdn_189d_slope_v012_signal,
    f20fd_f20_financing_dependence_selfgapd_252d_slope_v013_signal,
    f20fd_f20_financing_dependence_selfgapdz_126d_slope_v014_signal,
    f20fd_f20_financing_dependence_selfgapdn_504d_slope_v015_signal,
    f20fd_f20_financing_dependence_selfgapd_189d_slope_v016_signal,
    f20fd_f20_financing_dependence_raisesharedz_252d_slope_v017_signal,
    f20fd_f20_financing_dependence_raisesharedn_126d_slope_v018_signal,
    f20fd_f20_financing_dependence_raiseshared_504d_slope_v019_signal,
    f20fd_f20_financing_dependence_raisesharedz_189d_slope_v020_signal,
    f20fd_f20_financing_dependence_netfinturndn_252d_slope_v021_signal,
    f20fd_f20_financing_dependence_netfinturnd_126d_slope_v022_signal,
    f20fd_f20_financing_dependence_netfinturndz_504d_slope_v023_signal,
    f20fd_f20_financing_dependence_netfinturndn_189d_slope_v024_signal,
    f20fd_f20_financing_dependence_eqburnd_252d_slope_v025_signal,
    f20fd_f20_financing_dependence_eqburndz_126d_slope_v026_signal,
    f20fd_f20_financing_dependence_eqburndn_504d_slope_v027_signal,
    f20fd_f20_financing_dependence_eqburnd_189d_slope_v028_signal,
    f20fd_f20_financing_dependence_dtburndz_252d_slope_v029_signal,
    f20fd_f20_financing_dependence_dtburndn_126d_slope_v030_signal,
    f20fd_f20_financing_dependence_dtburnd_504d_slope_v031_signal,
    f20fd_f20_financing_dependence_dtburndz_189d_slope_v032_signal,
    f20fd_f20_financing_dependence_debtrelidn_252d_slope_v033_signal,
    f20fd_f20_financing_dependence_debtrelid_126d_slope_v034_signal,
    f20fd_f20_financing_dependence_debtrelidz_504d_slope_v035_signal,
    f20fd_f20_financing_dependence_debtrelidn_189d_slope_v036_signal,
    f20fd_f20_financing_dependence_eqrelid_252d_slope_v037_signal,
    f20fd_f20_financing_dependence_eqrelidz_126d_slope_v038_signal,
    f20fd_f20_financing_dependence_eqrelidn_504d_slope_v039_signal,
    f20fd_f20_financing_dependence_eqrelid_189d_slope_v040_signal,
    f20fd_f20_financing_dependence_netdebtflowdz_252d_slope_v041_signal,
    f20fd_f20_financing_dependence_netdebtflowdn_126d_slope_v042_signal,
    f20fd_f20_financing_dependence_netdebtflowd_504d_slope_v043_signal,
    f20fd_f20_financing_dependence_netdebtflowdz_189d_slope_v044_signal,
    f20fd_f20_financing_dependence_neteqflowdn_252d_slope_v045_signal,
    f20fd_f20_financing_dependence_neteqflowd_126d_slope_v046_signal,
    f20fd_f20_financing_dependence_neteqflowdz_504d_slope_v047_signal,
    f20fd_f20_financing_dependence_neteqflowdn_189d_slope_v048_signal,
    f20fd_f20_financing_dependence_finvsinvd_252d_slope_v049_signal,
    f20fd_f20_financing_dependence_finvsinvdz_126d_slope_v050_signal,
    f20fd_f20_financing_dependence_finvsinvdn_504d_slope_v051_signal,
    f20fd_f20_financing_dependence_finvsinvd_189d_slope_v052_signal,
    f20fd_f20_financing_dependence_extvsneeddz_252d_slope_v053_signal,
    f20fd_f20_financing_dependence_extvsneeddn_126d_slope_v054_signal,
    f20fd_f20_financing_dependence_extvsneedd_504d_slope_v055_signal,
    f20fd_f20_financing_dependence_extvsneeddz_189d_slope_v056_signal,
    f20fd_f20_financing_dependence_netfinburndn_252d_slope_v057_signal,
    f20fd_f20_financing_dependence_netfinburnd_126d_slope_v058_signal,
    f20fd_f20_financing_dependence_netfinburndz_504d_slope_v059_signal,
    f20fd_f20_financing_dependence_netfinburndn_189d_slope_v060_signal,
    f20fd_f20_financing_dependence_findird_252d_slope_v061_signal,
    f20fd_f20_financing_dependence_findirdz_126d_slope_v062_signal,
    f20fd_f20_financing_dependence_findirdn_504d_slope_v063_signal,
    f20fd_f20_financing_dependence_findird_189d_slope_v064_signal,
    f20fd_f20_financing_dependence_opcoversinvdz_252d_slope_v065_signal,
    f20fd_f20_financing_dependence_opcoversinvdn_126d_slope_v066_signal,
    f20fd_f20_financing_dependence_opcoversinvd_504d_slope_v067_signal,
    f20fd_f20_financing_dependence_opcoversinvdz_189d_slope_v068_signal,
    f20fd_f20_financing_dependence_mixbalancedn_252d_slope_v069_signal,
    f20fd_f20_financing_dependence_mixbalanced_126d_slope_v070_signal,
    f20fd_f20_financing_dependence_mixbalancedz_504d_slope_v071_signal,
    f20fd_f20_financing_dependence_mixbalancedn_189d_slope_v072_signal,
    f20fd_f20_financing_dependence_finfootprintd_252d_slope_v073_signal,
    f20fd_f20_financing_dependence_finfootprintdz_126d_slope_v074_signal,
    f20fd_f20_financing_dependence_finfootprintdn_504d_slope_v075_signal,
    f20fd_f20_financing_dependence_finfootprintd_189d_slope_v076_signal,
    f20fd_f20_financing_dependence_extofraiseddz_252d_slope_v077_signal,
    f20fd_f20_financing_dependence_extofraiseddn_126d_slope_v078_signal,
    f20fd_f20_financing_dependence_extofraisedd_504d_slope_v079_signal,
    f20fd_f20_financing_dependence_extofraiseddz_189d_slope_v080_signal,
    f20fd_f20_financing_dependence_dtopsdn_252d_slope_v081_signal,
    f20fd_f20_financing_dependence_dtopsd_126d_slope_v082_signal,
    f20fd_f20_financing_dependence_dtopsdz_504d_slope_v083_signal,
    f20fd_f20_financing_dependence_dtopsdn_189d_slope_v084_signal,
    f20fd_f20_financing_dependence_eqopsd_252d_slope_v085_signal,
    f20fd_f20_financing_dependence_eqopsdz_126d_slope_v086_signal,
    f20fd_f20_financing_dependence_eqopsdn_504d_slope_v087_signal,
    f20fd_f20_financing_dependence_eqopsd_189d_slope_v088_signal,
    f20fd_f20_financing_dependence_finperopdz_252d_slope_v089_signal,
    f20fd_f20_financing_dependence_finperopdn_126d_slope_v090_signal,
    f20fd_f20_financing_dependence_finperopd_504d_slope_v091_signal,
    f20fd_f20_financing_dependence_finperopdz_189d_slope_v092_signal,
    f20fd_f20_financing_dependence_intfundsharedn_252d_slope_v093_signal,
    f20fd_f20_financing_dependence_intfundshared_126d_slope_v094_signal,
    f20fd_f20_financing_dependence_intfundsharedz_504d_slope_v095_signal,
    f20fd_f20_financing_dependence_intfundsharedn_189d_slope_v096_signal,
    f20fd_f20_financing_dependence_finasymd_252d_slope_v097_signal,
    f20fd_f20_financing_dependence_finasymdz_126d_slope_v098_signal,
    f20fd_f20_financing_dependence_finasymdn_504d_slope_v099_signal,
    f20fd_f20_financing_dependence_finasymd_189d_slope_v100_signal,
    f20fd_f20_financing_dependence_dtrepaydz_252d_slope_v101_signal,
    f20fd_f20_financing_dependence_dtrepaydn_126d_slope_v102_signal,
    f20fd_f20_financing_dependence_dtrepayd_504d_slope_v103_signal,
    f20fd_f20_financing_dependence_dtrepaydz_189d_slope_v104_signal,
    f20fd_f20_financing_dependence_eqnetdirdn_252d_slope_v105_signal,
    f20fd_f20_financing_dependence_eqnetdird_126d_slope_v106_signal,
    f20fd_f20_financing_dependence_eqnetdirdz_504d_slope_v107_signal,
    f20fd_f20_financing_dependence_eqnetdirdn_189d_slope_v108_signal,
    f20fd_f20_financing_dependence_extcushiond_252d_slope_v109_signal,
    f20fd_f20_financing_dependence_extcushiondz_126d_slope_v110_signal,
    f20fd_f20_financing_dependence_extcushiondn_504d_slope_v111_signal,
    f20fd_f20_financing_dependence_extcushiond_189d_slope_v112_signal,
    f20fd_f20_financing_dependence_srchhidz_252d_slope_v113_signal,
    f20fd_f20_financing_dependence_srchhidn_126d_slope_v114_signal,
    f20fd_f20_financing_dependence_srchhid_504d_slope_v115_signal,
    f20fd_f20_financing_dependence_srchhidz_189d_slope_v116_signal,
    f20fd_f20_financing_dependence_coverlogdn_252d_slope_v117_signal,
    f20fd_f20_financing_dependence_coverlogd_126d_slope_v118_signal,
    f20fd_f20_financing_dependence_coverlogdz_504d_slope_v119_signal,
    f20fd_f20_financing_dependence_coverlogdn_189d_slope_v120_signal,
    f20fd_f20_financing_dependence_finchurnd_252d_slope_v121_signal,
    f20fd_f20_financing_dependence_finchurndz_126d_slope_v122_signal,
    f20fd_f20_financing_dependence_finchurndn_504d_slope_v123_signal,
    f20fd_f20_financing_dependence_finchurnd_189d_slope_v124_signal,
    f20fd_f20_financing_dependence_levtiltdz_252d_slope_v125_signal,
    f20fd_f20_financing_dependence_levtiltdn_126d_slope_v126_signal,
    f20fd_f20_financing_dependence_levtiltd_504d_slope_v127_signal,
    f20fd_f20_financing_dependence_levtiltdz_189d_slope_v128_signal,
    f20fd_f20_financing_dependence_residextdn_252d_slope_v129_signal,
    f20fd_f20_financing_dependence_residextd_126d_slope_v130_signal,
    f20fd_f20_financing_dependence_residextdz_504d_slope_v131_signal,
    f20fd_f20_financing_dependence_residextdn_189d_slope_v132_signal,
    f20fd_f20_financing_dependence_eqinshared_252d_slope_v133_signal,
    f20fd_f20_financing_dependence_eqinsharedz_126d_slope_v134_signal,
    f20fd_f20_financing_dependence_eqinsharedn_504d_slope_v135_signal,
    f20fd_f20_financing_dependence_eqinshared_189d_slope_v136_signal,
    f20fd_f20_financing_dependence_dtinsharedz_252d_slope_v137_signal,
    f20fd_f20_financing_dependence_dtinsharedn_126d_slope_v138_signal,
    f20fd_f20_financing_dependence_dtinshared_504d_slope_v139_signal,
    f20fd_f20_financing_dependence_dtinsharedz_189d_slope_v140_signal,
    f20fd_f20_financing_dependence_extneedcovdn_252d_slope_v141_signal,
    f20fd_f20_financing_dependence_extneedcovd_126d_slope_v142_signal,
    f20fd_f20_financing_dependence_extneedcovdz_504d_slope_v143_signal,
    f20fd_f20_financing_dependence_extneedcovdn_189d_slope_v144_signal,
    f20fd_f20_financing_dependence_netrelind_252d_slope_v145_signal,
    f20fd_f20_financing_dependence_netrelindz_126d_slope_v146_signal,
    f20fd_f20_financing_dependence_netrelindn_504d_slope_v147_signal,
    f20fd_f20_financing_dependence_netrelind_189d_slope_v148_signal,
    f20fd_f20_financing_dependence_dtveqmixdz_252d_slope_v149_signal,
    f20fd_f20_financing_dependence_dtveqmixdn_126d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F20_FINANCING_DEPENDENCE_REGISTRY_2ND_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.0, vol=0.08, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.5
        return pd.Series(s, name=None)

    def _flow(seed, center, amp=1.0, vol=0.09):
        f = _fund(seed, base=1e8, drift=0.0, vol=vol, allow_neg=False)
        osc = f - f.rolling(189, min_periods=20).mean()
        osc = osc.bfill()
        return center + amp * osc

    ncff = _flow(201, 8e6, 1.0).rename("ncff")
    ncfcommon = _flow(202, 0.0, 1.1).rename("ncfcommon")
    ncfdebt = _flow(203, 4e6, 0.9).rename("ncfdebt")
    ncfo = _flow(204, -6e6, 1.2).rename("ncfo")
    ncfi = _flow(205, -10e6, 1.3).rename("ncfi")

    cols = {"ncff": ncff, "ncfcommon": ncfcommon, "ncfdebt": ncfdebt,
            "ncfo": ncfo, "ncfi": ncfi}

    fundamental_cols = set(cols.keys())
    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        ins = meta["inputs"]
        assert any(c in fundamental_cols for c in ins), "no fundamental input: %s" % name
        fn = meta["func"]
        args = [cols[c] for c in ins]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 20, "%s nunique=%d" % (name, q.nunique())
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        results[name] = y1.iloc[504:]
        n_features += 1

    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), "nan_ok=%d/%d" % (nan_ok, n_features)

    items = list(results.items())
    for i in range(len(items)):
        ni, si = items[i]
        ai = si.dropna()
        for j in range(i + 1, len(items)):
            nj, sj = items[j]
            aj = sj.dropna()
            idx = ai.index.intersection(aj.index)
            if len(idx) < 30:
                continue
            c = ai.loc[idx].corr(aj.loc[idx])
            if c is None or np.isnan(c):
                continue
            assert abs(c) <= 0.97, "CORR %s vs %s = %.4f" % (ni, nj, c)

    print("OK f20_financing_dependence_2nd_derivatives_001_150_claude: %d features pass" % n_features)
