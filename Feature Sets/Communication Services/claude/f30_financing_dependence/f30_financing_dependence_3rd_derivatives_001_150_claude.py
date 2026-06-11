import inspect
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# f30_financing_dependence -- 3rd-derivative file: JERK features.
# Each feature is the 2nd math derivative (jerk / curvature) of a distinct
# financing-dependence base expression, fully expanded (no factories/loops/exec).
# Each derivative window is chosen appropriate to the base window.
# ---------------------------------------------------------------------------

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
def _z(s, w):
    m = s.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(2, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _slope(s, w):
    # 1st discrete derivative over w days, scaled per-day
    return (s - s.shift(w)) / float(w)


def _ext_reliance(ncff, ncfo, w):
    f = _mean(ncff, w)
    o = _mean(ncfo, w)
    return f / (f.abs() + o.abs()).replace(0, np.nan)


def _burn_cover(ncff, ncfo, w):
    burn = (-ncfo).clip(lower=0)
    inflow = ncff.clip(lower=0)
    return _mean(inflow, w) / _mean(burn, w).replace(0, np.nan)


def _self_fund_gap(ncfo, ncfi, w):
    fcf_pre = _mean(ncfo + ncfi, w)
    scale = (_mean(ncfo.abs(), w) + _mean(ncfi.abs(), w)).replace(0, np.nan)
    return fcf_pre / scale


def _eq_debt_mix(ncfcommon, ncfdebt, w):
    e = _mean(ncfcommon, w)
    d = _mean(ncfdebt, w)
    return (e - d) / (e.abs() + d.abs()).replace(0, np.nan)


def _rollcorr(a, b, w):
    am = a - _mean(a, w)
    bm = b - _mean(b, w)
    cov = _mean(am * bm, w)
    denom = (_std(a, w) * _std(b, w)).replace(0, np.nan)
    return cov / denom


def _raise_intensity(ncff, w):
    inflow = _mean(ncff.clip(lower=0), w)
    turn = _mean(ncff.abs(), w).replace(0, np.nan)
    return inflow / turn


def f30fd_f30_financing_dependence_extrel_63d_jerk_v001_signal(ncff, ncfo):
    base = _ext_reliance(ncff, ncfo, 63)
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_burncov_63d_jerk_v002_signal(ncff, ncfo):
    base = _burn_cover(ncff, ncfo, 63)
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_selffund_63d_jerk_v003_signal(ncfo, ncfi):
    base = _self_fund_gap(ncfo, ncfi, 63)
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_mix_63d_jerk_v004_signal(ncfcommon, ncfdebt):
    base = _eq_debt_mix(ncfcommon, ncfdebt, 63)
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_raiseint_63d_jerk_v005_signal(ncff):
    base = _raise_intensity(ncff, 63)
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_overfund_63d_jerk_v006_signal(ncff, ncfo, ncfi):
    deficit = _mean((-(ncfo + ncfi)).clip(lower=0), 63)
    fin = _mean(ncff.clip(lower=0), 63)
    base = (fin - deficit) / (fin + deficit).replace(0, np.nan)
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_eqraise_63d_jerk_v007_signal(ncfcommon, ncfo):
    base = _safe_div(_mean(ncfcommon.clip(lower=0), 63), _mean(ncfcommon.abs(), 63) + _mean(ncfo.abs(), 63))
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_debtdraw_63d_jerk_v008_signal(ncfdebt, ncfo):
    base = _safe_div(_mean(ncfdebt.clip(lower=0), 63), _mean(ncfdebt.abs(), 63) + _mean(ncfo.abs(), 63))
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_extdep_63d_jerk_v009_signal(ncff, ncfo, ncfi):
    need = (_mean((-ncfo).clip(lower=0), 63) + _mean((-ncfi).clip(lower=0), 63)).replace(0, np.nan)
    base = _mean(ncff.clip(lower=0), 63) / need
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_finopcorr_63d_jerk_v010_signal(ncff, ncfo):
    base = _rollcorr(ncff, ncfo, 63)
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_eqdebtcorr_63d_jerk_v011_signal(ncfcommon, ncfdebt):
    base = _rollcorr(ncfcommon, ncfdebt, 63)
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_fininvcorr_63d_jerk_v012_signal(ncff, ncfi):
    base = -_rollcorr(ncff, ncfi, 63)
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_opinvcorr_63d_jerk_v013_signal(ncfo, ncfi):
    base = _rollcorr(ncfo, ncfi, 63)
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_extfrac_63d_jerk_v014_signal(ncff, ncfo):
    fin = _mean(ncff.clip(lower=0), 63)
    op = _mean(ncfo.clip(lower=0), 63)
    base = fin / (fin + op).replace(0, np.nan)
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_eqshare_63d_jerk_v015_signal(ncfcommon, ncfdebt):
    e = _mean(ncfcommon.clip(lower=0), 63)
    tot = (e + _mean(ncfdebt.clip(lower=0), 63)).replace(0, np.nan)
    base = e / tot
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_eqburn_63d_jerk_v016_signal(ncfcommon, ncfo):
    base = np.tanh(_safe_div(_mean(ncfcommon.clip(lower=0), 63), _mean((-ncfo).clip(lower=0), 63)))
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_debtburn_63d_jerk_v017_signal(ncfdebt, ncfo):
    base = np.tanh(_safe_div(_mean(ncfdebt.clip(lower=0), 63), _mean((-ncfo).clip(lower=0), 63)))
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_invfund_63d_jerk_v018_signal(ncff, ncfi):
    base = np.tanh(_safe_div(_mean((-ncfi).clip(lower=0), 63), _mean(ncff.clip(lower=0), 63)))
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_opshareflip_63d_jerk_v019_signal(ncfo, ncff, ncfi):
    op = _mean(ncfo.clip(lower=0), 63)
    fin = _mean(ncff.clip(lower=0), 63)
    tot = _mean(ncfo.abs() + ncff.abs() + ncfi.abs(), 63).replace(0, np.nan)
    base = (op - fin) / tot
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_netextdep_63d_jerk_v020_signal(ncff, ncfo, ncfi):
    pre = _mean(ncfo + ncfi, 63)
    fin = _mean(ncff, 63)
    base = (fin - pre) / (fin.abs() + pre.abs()).replace(0, np.nan)
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_eqchannel_63d_jerk_v021_signal(ncfcommon, ncff):
    base = _safe_div(_mean(ncfcommon.clip(lower=0), 63), _mean(ncff.clip(lower=0), 63)).clip(upper=3.0)
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_debtchannel_63d_jerk_v022_signal(ncfdebt, ncff):
    base = _safe_div(_mean(ncfdebt.clip(lower=0), 63), _mean(ncff.clip(lower=0), 63)).clip(upper=3.0)
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_finturn_63d_jerk_v023_signal(ncff, ncfo):
    base = _safe_div(_mean(ncff.abs(), 63), _mean(ncfo.abs(), 63))
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_opsuff_63d_jerk_v024_signal(ncfo, ncfi, ncff):
    tot = (_mean(ncfo.abs(), 63) + _mean(ncfi.abs(), 63) + _mean(ncff.abs(), 63)).replace(0, np.nan)
    base = _mean(ncfo, 63) / tot
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_eqnetbal_63d_jerk_v025_signal(ncfcommon):
    q = _mean(ncfcommon, 21)
    flip = (np.sign(q) != np.sign(q.shift(21))).astype(float)
    base = flip.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_debtnetbal_63d_jerk_v026_signal(ncfdebt):
    q = _mean(ncfdebt, 21)
    flip = (np.sign(q) != np.sign(q.shift(21))).astype(float)
    base = flip.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_finivnet_63d_jerk_v027_signal(ncff, ncfi):
    net = _mean(ncff + ncfi, 63)
    sc = (_mean(ncff.abs(), 63) + _mean(ncfi.abs(), 63)).replace(0, np.nan)
    base = _z(net / sc, 63)
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_repay_63d_jerk_v028_signal(ncfdebt, ncfo):
    base = _safe_div(_mean((-ncfdebt).clip(lower=0), 63), _mean(ncfo.abs(), 63))
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_buyback_63d_jerk_v029_signal(ncfcommon, ncfo):
    base = np.tanh(_safe_div(_mean((-ncfcommon).clip(lower=0), 63), _mean(ncfo.clip(lower=0), 63)))
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_totraise_63d_jerk_v030_signal(ncfcommon, ncfdebt, ncfo):
    raises = _mean(ncfcommon.clip(lower=0) + ncfdebt.clip(lower=0), 63)
    eng = (raises.abs() + _mean(ncfo.abs(), 63)).replace(0, np.nan)
    base = raises / eng
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_finskew_63d_jerk_v031_signal(ncff):
    sc = _std(ncff, 63).replace(0, np.nan)
    centered = ncff - _mean(ncff, 63)
    base = _mean((centered / sc) ** 3, 63)
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_gapstreak_63d_jerk_v032_signal(ncfo, ncfi):
    deficit = (-(ncfo + ncfi)).clip(lower=0)
    monthly = _mean(deficit, 21)
    peak = monthly.rolling(63, min_periods=max(2, 63 // 2)).max()
    avg = monthly.rolling(63, min_periods=max(2, 63 // 2)).mean().replace(0, np.nan)
    base = peak / avg
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_finled_63d_jerk_v033_signal(ncff, ncfo):
    led = (ncff.clip(lower=0) > ncfo.clip(lower=0)).astype(float)
    base = led.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_plugrate_63d_jerk_v034_signal(ncff, ncfo):
    plug = ((ncff > 0) & (ncfo < 0)).astype(float)
    base = plug.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_finivstreak_63d_jerk_v035_signal(ncff, ncfi):
    co = ((ncff > 0) & (ncfi < 0)).astype(float)
    base = co.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_finmix3_63d_jerk_v036_signal(ncfcommon, ncfdebt, ncfo):
    e = _mean(ncfcommon.clip(lower=0), 63)
    src = _mean(ncfcommon.clip(lower=0) + ncfdebt.clip(lower=0) + ncfo.clip(lower=0), 63).replace(0, np.nan)
    base = e / src
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_raisevinv_63d_jerk_v037_signal(ncfcommon, ncfdebt, ncfi):
    raises = _mean(ncfcommon.clip(lower=0) + ncfdebt.clip(lower=0), 63)
    inv = _mean((-ncfi).clip(lower=0), 63).replace(0, np.nan)
    base = np.tanh(raises / inv)
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_finpersist_63d_jerk_v038_signal(ncff):
    x = ncff - _mean(ncff, 63)
    cov = _mean(x * x.shift(21), 63)
    base = cov / (_std(ncff, 63).replace(0, np.nan) ** 2)
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_debtpersist_63d_jerk_v039_signal(ncfdebt):
    x = ncfdebt - _mean(ncfdebt, 63)
    cov = _mean(x * x.shift(21), 63)
    base = cov / (_std(ncfdebt, 63).replace(0, np.nan) ** 2)
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_oppersist_63d_jerk_v040_signal(ncfo):
    x = ncfo - _mean(ncfo, 63)
    cov = _mean(x * x.shift(21), 63)
    base = cov / (_std(ncfo, 63).replace(0, np.nan) ** 2)
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_reldisp_63d_jerk_v041_signal(ncff, ncfo):
    r = _ext_reliance(ncff, ncfo, 21)
    base = _std(r, 63)
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_mixdisp_63d_jerk_v042_signal(ncfcommon, ncfdebt):
    mm = _eq_debt_mix(ncfcommon, ncfdebt, 21)
    base = _std(mm, 63)
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_gapvol_63d_jerk_v043_signal(ncfo, ncfi):
    g = _self_fund_gap(ncfo, ncfi, 21)
    base = _std(g, 63)
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_finvol_63d_jerk_v044_signal(ncff, ncfo):
    v = _std(ncff, 63)
    base = _mean(v, 63) / _mean(ncfo.abs(), 63).replace(0, np.nan)
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_eqconc_63d_jerk_v045_signal(ncfcommon):
    monthly = _mean(ncfcommon.clip(lower=0), 21)
    peak = monthly.rolling(63, min_periods=max(2, 63 // 2)).max()
    avg = monthly.rolling(63, min_periods=max(2, 63 // 2)).mean().replace(0, np.nan)
    base = peak / avg
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_debtconc_63d_jerk_v046_signal(ncfdebt):
    monthly = _mean(ncfdebt.clip(lower=0), 21)
    peak = monthly.rolling(63, min_periods=max(2, 63 // 2)).max()
    avg = monthly.rolling(63, min_periods=max(2, 63 // 2)).mean().replace(0, np.nan)
    base = peak / avg
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_raiseburnsync_63d_jerk_v047_signal(ncff, ncfo):
    base = _rollcorr(ncff.clip(lower=0), (-ncfo).clip(lower=0), 63)
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_debtopcorr_63d_jerk_v048_signal(ncfo, ncfdebt):
    base = _rollcorr(ncfo, ncfdebt, 63)
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_eqopcorr_63d_jerk_v049_signal(ncfo, ncfcommon):
    base = _rollcorr(ncfo, ncfcommon, 63)
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_debtsrc3_63d_jerk_v050_signal(ncfdebt, ncfcommon, ncfo):
    d = _mean(ncfdebt.clip(lower=0), 63)
    src = _mean(ncfcommon.clip(lower=0) + ncfdebt.clip(lower=0) + ncfo.clip(lower=0), 63).replace(0, np.nan)
    base = d / src
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_totburncov_63d_jerk_v051_signal(ncff, ncfo, ncfi):
    deficit = (-(ncfo + ncfi)).clip(lower=0)
    cov = _safe_div(_mean(ncff.clip(lower=0), 63), _mean(deficit, 63))
    base = cov.rolling(252, min_periods=max(2, 252 // 2)).rank(pct=True) - 0.5
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_invselffund_63d_jerk_v052_signal(ncfo, ncfi):
    base = np.tanh(_safe_div(_mean(ncfo.clip(lower=0), 63), _mean((-ncfi).clip(lower=0), 63)))
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_returntilt_63d_jerk_v053_signal(ncfcommon, ncfdebt, ncfo):
    returns = _mean((-ncfcommon).clip(lower=0) + (-ncfdebt).clip(lower=0), 63)
    base = np.tanh(_safe_div(returns, _mean(ncfo.clip(lower=0), 63)))
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_debttilt_63d_jerk_v054_signal(ncfdebt, ncfcommon):
    dturn = _mean(ncfdebt.abs(), 63)
    eturn = _mean(ncfcommon.abs(), 63)
    base = (dturn - eturn) / (dturn + eturn).replace(0, np.nan)
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_eqdebtspread_63d_jerk_v055_signal(ncfcommon, ncfdebt):
    intake = _mean(ncfcommon.clip(lower=0) + ncfdebt.clip(lower=0), 63)
    outgo = _mean((-ncfcommon).clip(lower=0) + (-ncfdebt).clip(lower=0), 63)
    base = (intake - outgo) / (intake + outgo).replace(0, np.nan)
    d1 = (base - base.shift(21)) / float(21)
    d2 = (d1 - d1.shift(21)) / float(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_extrel_126d_jerk_v056_signal(ncff, ncfo):
    base = _ext_reliance(ncff, ncfo, 126)
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_burncov_126d_jerk_v057_signal(ncff, ncfo):
    base = _burn_cover(ncff, ncfo, 126)
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_selffund_126d_jerk_v058_signal(ncfo, ncfi):
    base = _self_fund_gap(ncfo, ncfi, 126)
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_mix_126d_jerk_v059_signal(ncfcommon, ncfdebt):
    base = _eq_debt_mix(ncfcommon, ncfdebt, 126)
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_raiseint_126d_jerk_v060_signal(ncff):
    base = _raise_intensity(ncff, 126)
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_overfund_126d_jerk_v061_signal(ncff, ncfo, ncfi):
    deficit = _mean((-(ncfo + ncfi)).clip(lower=0), 126)
    fin = _mean(ncff.clip(lower=0), 126)
    base = (fin - deficit) / (fin + deficit).replace(0, np.nan)
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_eqraise_126d_jerk_v062_signal(ncfcommon, ncfo):
    base = _safe_div(_mean(ncfcommon.clip(lower=0), 126), _mean(ncfcommon.abs(), 126) + _mean(ncfo.abs(), 126))
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_debtdraw_126d_jerk_v063_signal(ncfdebt, ncfo):
    base = _safe_div(_mean(ncfdebt.clip(lower=0), 126), _mean(ncfdebt.abs(), 126) + _mean(ncfo.abs(), 126))
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_extdep_126d_jerk_v064_signal(ncff, ncfo, ncfi):
    need = (_mean((-ncfo).clip(lower=0), 126) + _mean((-ncfi).clip(lower=0), 126)).replace(0, np.nan)
    base = _mean(ncff.clip(lower=0), 126) / need
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_finopcorr_126d_jerk_v065_signal(ncff, ncfo):
    base = _rollcorr(ncff, ncfo, 126)
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_eqdebtcorr_126d_jerk_v066_signal(ncfcommon, ncfdebt):
    base = _rollcorr(ncfcommon, ncfdebt, 126)
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_fininvcorr_126d_jerk_v067_signal(ncff, ncfi):
    base = -_rollcorr(ncff, ncfi, 126)
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_opinvcorr_126d_jerk_v068_signal(ncfo, ncfi):
    base = _rollcorr(ncfo, ncfi, 126)
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_extfrac_126d_jerk_v069_signal(ncff, ncfo):
    fin = _mean(ncff.clip(lower=0), 126)
    op = _mean(ncfo.clip(lower=0), 126)
    base = fin / (fin + op).replace(0, np.nan)
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_eqshare_126d_jerk_v070_signal(ncfcommon, ncfdebt):
    e = _mean(ncfcommon.clip(lower=0), 126)
    tot = (e + _mean(ncfdebt.clip(lower=0), 126)).replace(0, np.nan)
    base = e / tot
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_eqburn_126d_jerk_v071_signal(ncfcommon, ncfo):
    base = np.tanh(_safe_div(_mean(ncfcommon.clip(lower=0), 126), _mean((-ncfo).clip(lower=0), 126)))
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_debtburn_126d_jerk_v072_signal(ncfdebt, ncfo):
    base = np.tanh(_safe_div(_mean(ncfdebt.clip(lower=0), 126), _mean((-ncfo).clip(lower=0), 126)))
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_invfund_126d_jerk_v073_signal(ncff, ncfi):
    base = np.tanh(_safe_div(_mean((-ncfi).clip(lower=0), 126), _mean(ncff.clip(lower=0), 126)))
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_opshareflip_126d_jerk_v074_signal(ncfo, ncff, ncfi):
    op = _mean(ncfo.clip(lower=0), 126)
    fin = _mean(ncff.clip(lower=0), 126)
    tot = _mean(ncfo.abs() + ncff.abs() + ncfi.abs(), 126).replace(0, np.nan)
    base = (op - fin) / tot
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_netextdep_126d_jerk_v075_signal(ncff, ncfo, ncfi):
    pre = _mean(ncfo + ncfi, 126)
    fin = _mean(ncff, 126)
    base = (fin - pre) / (fin.abs() + pre.abs()).replace(0, np.nan)
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_eqchannel_126d_jerk_v076_signal(ncfcommon, ncff):
    base = _safe_div(_mean(ncfcommon.clip(lower=0), 126), _mean(ncff.clip(lower=0), 126)).clip(upper=3.0)
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_debtchannel_126d_jerk_v077_signal(ncfdebt, ncff):
    base = _safe_div(_mean(ncfdebt.clip(lower=0), 126), _mean(ncff.clip(lower=0), 126)).clip(upper=3.0)
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_finturn_126d_jerk_v078_signal(ncff, ncfo):
    base = _safe_div(_mean(ncff.abs(), 126), _mean(ncfo.abs(), 126))
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_opsuff_126d_jerk_v079_signal(ncfo, ncfi, ncff):
    tot = (_mean(ncfo.abs(), 126) + _mean(ncfi.abs(), 126) + _mean(ncff.abs(), 126)).replace(0, np.nan)
    base = _mean(ncfo, 126) / tot
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_eqnetbal_126d_jerk_v080_signal(ncfcommon):
    q = _mean(ncfcommon, 21)
    flip = (np.sign(q) != np.sign(q.shift(21))).astype(float)
    base = flip.rolling(126, min_periods=max(2, 126 // 2)).mean()
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_debtnetbal_126d_jerk_v081_signal(ncfdebt):
    q = _mean(ncfdebt, 21)
    flip = (np.sign(q) != np.sign(q.shift(21))).astype(float)
    base = flip.rolling(126, min_periods=max(2, 126 // 2)).mean()
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_finivnet_126d_jerk_v082_signal(ncff, ncfi):
    net = _mean(ncff + ncfi, 126)
    sc = (_mean(ncff.abs(), 126) + _mean(ncfi.abs(), 126)).replace(0, np.nan)
    base = _z(net / sc, 126)
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_repay_126d_jerk_v083_signal(ncfdebt, ncfo):
    base = _safe_div(_mean((-ncfdebt).clip(lower=0), 126), _mean(ncfo.abs(), 126))
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_buyback_126d_jerk_v084_signal(ncfcommon, ncfo):
    base = np.tanh(_safe_div(_mean((-ncfcommon).clip(lower=0), 126), _mean(ncfo.clip(lower=0), 126)))
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_totraise_126d_jerk_v085_signal(ncfcommon, ncfdebt, ncfo):
    raises = _mean(ncfcommon.clip(lower=0) + ncfdebt.clip(lower=0), 126)
    eng = (raises.abs() + _mean(ncfo.abs(), 126)).replace(0, np.nan)
    base = raises / eng
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_finskew_126d_jerk_v086_signal(ncff):
    sc = _std(ncff, 126).replace(0, np.nan)
    centered = ncff - _mean(ncff, 126)
    base = _mean((centered / sc) ** 3, 126)
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_gapstreak_126d_jerk_v087_signal(ncfo, ncfi):
    deficit = (-(ncfo + ncfi)).clip(lower=0)
    monthly = _mean(deficit, 21)
    peak = monthly.rolling(126, min_periods=max(2, 126 // 2)).max()
    avg = monthly.rolling(126, min_periods=max(2, 126 // 2)).mean().replace(0, np.nan)
    base = peak / avg
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_finled_126d_jerk_v088_signal(ncff, ncfo):
    led = (ncff.clip(lower=0) > ncfo.clip(lower=0)).astype(float)
    base = led.rolling(126, min_periods=max(2, 126 // 2)).mean()
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_plugrate_126d_jerk_v089_signal(ncff, ncfo):
    plug = ((ncff > 0) & (ncfo < 0)).astype(float)
    base = plug.rolling(126, min_periods=max(2, 126 // 2)).mean()
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_finivstreak_126d_jerk_v090_signal(ncff, ncfi):
    co = ((ncff > 0) & (ncfi < 0)).astype(float)
    base = co.rolling(126, min_periods=max(2, 126 // 2)).mean()
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_finmix3_126d_jerk_v091_signal(ncfcommon, ncfdebt, ncfo):
    e = _mean(ncfcommon.clip(lower=0), 126)
    src = _mean(ncfcommon.clip(lower=0) + ncfdebt.clip(lower=0) + ncfo.clip(lower=0), 126).replace(0, np.nan)
    base = e / src
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_raisevinv_126d_jerk_v092_signal(ncfcommon, ncfdebt, ncfi):
    raises = _mean(ncfcommon.clip(lower=0) + ncfdebt.clip(lower=0), 126)
    inv = _mean((-ncfi).clip(lower=0), 126).replace(0, np.nan)
    base = np.tanh(raises / inv)
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_finpersist_126d_jerk_v093_signal(ncff):
    x = ncff - _mean(ncff, 126)
    cov = _mean(x * x.shift(21), 126)
    base = cov / (_std(ncff, 126).replace(0, np.nan) ** 2)
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_debtpersist_126d_jerk_v094_signal(ncfdebt):
    x = ncfdebt - _mean(ncfdebt, 126)
    cov = _mean(x * x.shift(21), 126)
    base = cov / (_std(ncfdebt, 126).replace(0, np.nan) ** 2)
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_oppersist_126d_jerk_v095_signal(ncfo):
    x = ncfo - _mean(ncfo, 126)
    cov = _mean(x * x.shift(21), 126)
    base = cov / (_std(ncfo, 126).replace(0, np.nan) ** 2)
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_reldisp_126d_jerk_v096_signal(ncff, ncfo):
    r = _ext_reliance(ncff, ncfo, 21)
    base = _std(r, 126)
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_mixdisp_126d_jerk_v097_signal(ncfcommon, ncfdebt):
    mm = _eq_debt_mix(ncfcommon, ncfdebt, 21)
    base = _std(mm, 126)
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_gapvol_126d_jerk_v098_signal(ncfo, ncfi):
    g = _self_fund_gap(ncfo, ncfi, 21)
    base = _std(g, 126)
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_finvol_126d_jerk_v099_signal(ncff, ncfo):
    v = _std(ncff, 63)
    base = _mean(v, 126) / _mean(ncfo.abs(), 126).replace(0, np.nan)
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_eqconc_126d_jerk_v100_signal(ncfcommon):
    monthly = _mean(ncfcommon.clip(lower=0), 21)
    peak = monthly.rolling(126, min_periods=max(2, 126 // 2)).max()
    avg = monthly.rolling(126, min_periods=max(2, 126 // 2)).mean().replace(0, np.nan)
    base = peak / avg
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_debtconc_126d_jerk_v101_signal(ncfdebt):
    monthly = _mean(ncfdebt.clip(lower=0), 21)
    peak = monthly.rolling(126, min_periods=max(2, 126 // 2)).max()
    avg = monthly.rolling(126, min_periods=max(2, 126 // 2)).mean().replace(0, np.nan)
    base = peak / avg
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_raiseburnsync_126d_jerk_v102_signal(ncff, ncfo):
    base = _rollcorr(ncff.clip(lower=0), (-ncfo).clip(lower=0), 126)
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_debtopcorr_126d_jerk_v103_signal(ncfo, ncfdebt):
    base = _rollcorr(ncfo, ncfdebt, 126)
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_eqopcorr_126d_jerk_v104_signal(ncfo, ncfcommon):
    base = _rollcorr(ncfo, ncfcommon, 126)
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_debtsrc3_126d_jerk_v105_signal(ncfdebt, ncfcommon, ncfo):
    d = _mean(ncfdebt.clip(lower=0), 126)
    src = _mean(ncfcommon.clip(lower=0) + ncfdebt.clip(lower=0) + ncfo.clip(lower=0), 126).replace(0, np.nan)
    base = d / src
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_totburncov_126d_jerk_v106_signal(ncff, ncfo, ncfi):
    deficit = (-(ncfo + ncfi)).clip(lower=0)
    cov = _safe_div(_mean(ncff.clip(lower=0), 126), _mean(deficit, 126))
    base = cov.rolling(252, min_periods=max(2, 252 // 2)).rank(pct=True) - 0.5
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_invselffund_126d_jerk_v107_signal(ncfo, ncfi):
    base = np.tanh(_safe_div(_mean(ncfo.clip(lower=0), 126), _mean((-ncfi).clip(lower=0), 126)))
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_returntilt_126d_jerk_v108_signal(ncfcommon, ncfdebt, ncfo):
    returns = _mean((-ncfcommon).clip(lower=0) + (-ncfdebt).clip(lower=0), 126)
    base = np.tanh(_safe_div(returns, _mean(ncfo.clip(lower=0), 126)))
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_debttilt_126d_jerk_v109_signal(ncfdebt, ncfcommon):
    dturn = _mean(ncfdebt.abs(), 126)
    eturn = _mean(ncfcommon.abs(), 126)
    base = (dturn - eturn) / (dturn + eturn).replace(0, np.nan)
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_eqdebtspread_126d_jerk_v110_signal(ncfcommon, ncfdebt):
    intake = _mean(ncfcommon.clip(lower=0) + ncfdebt.clip(lower=0), 126)
    outgo = _mean((-ncfcommon).clip(lower=0) + (-ncfdebt).clip(lower=0), 126)
    base = (intake - outgo) / (intake + outgo).replace(0, np.nan)
    d1 = (base - base.shift(42)) / float(42)
    d2 = (d1 - d1.shift(42)) / float(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_extrel_252d_jerk_v111_signal(ncff, ncfo):
    base = _ext_reliance(ncff, ncfo, 252)
    d1 = (base - base.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_burncov_252d_jerk_v112_signal(ncff, ncfo):
    base = _burn_cover(ncff, ncfo, 252)
    d1 = (base - base.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_selffund_252d_jerk_v113_signal(ncfo, ncfi):
    base = _self_fund_gap(ncfo, ncfi, 252)
    d1 = (base - base.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_mix_252d_jerk_v114_signal(ncfcommon, ncfdebt):
    base = _eq_debt_mix(ncfcommon, ncfdebt, 252)
    d1 = (base - base.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_raiseint_252d_jerk_v115_signal(ncff):
    base = _raise_intensity(ncff, 252)
    d1 = (base - base.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_overfund_252d_jerk_v116_signal(ncff, ncfo, ncfi):
    deficit = _mean((-(ncfo + ncfi)).clip(lower=0), 252)
    fin = _mean(ncff.clip(lower=0), 252)
    base = (fin - deficit) / (fin + deficit).replace(0, np.nan)
    d1 = (base - base.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_eqraise_252d_jerk_v117_signal(ncfcommon, ncfo):
    base = _safe_div(_mean(ncfcommon.clip(lower=0), 252), _mean(ncfcommon.abs(), 252) + _mean(ncfo.abs(), 252))
    d1 = (base - base.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_debtdraw_252d_jerk_v118_signal(ncfdebt, ncfo):
    base = _safe_div(_mean(ncfdebt.clip(lower=0), 252), _mean(ncfdebt.abs(), 252) + _mean(ncfo.abs(), 252))
    d1 = (base - base.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_extdep_252d_jerk_v119_signal(ncff, ncfo, ncfi):
    need = (_mean((-ncfo).clip(lower=0), 252) + _mean((-ncfi).clip(lower=0), 252)).replace(0, np.nan)
    base = _mean(ncff.clip(lower=0), 252) / need
    d1 = (base - base.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_finopcorr_252d_jerk_v120_signal(ncff, ncfo):
    base = _rollcorr(ncff, ncfo, 252)
    d1 = (base - base.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_eqdebtcorr_252d_jerk_v121_signal(ncfcommon, ncfdebt):
    base = _rollcorr(ncfcommon, ncfdebt, 252)
    d1 = (base - base.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_fininvcorr_252d_jerk_v122_signal(ncff, ncfi):
    base = -_rollcorr(ncff, ncfi, 252)
    d1 = (base - base.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_opinvcorr_252d_jerk_v123_signal(ncfo, ncfi):
    base = _rollcorr(ncfo, ncfi, 252)
    d1 = (base - base.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_extfrac_252d_jerk_v124_signal(ncff, ncfo):
    fin = _mean(ncff.clip(lower=0), 252)
    op = _mean(ncfo.clip(lower=0), 252)
    base = fin / (fin + op).replace(0, np.nan)
    d1 = (base - base.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_eqshare_252d_jerk_v125_signal(ncfcommon, ncfdebt):
    e = _mean(ncfcommon.clip(lower=0), 252)
    tot = (e + _mean(ncfdebt.clip(lower=0), 252)).replace(0, np.nan)
    base = e / tot
    d1 = (base - base.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_eqburn_252d_jerk_v126_signal(ncfcommon, ncfo):
    base = np.tanh(_safe_div(_mean(ncfcommon.clip(lower=0), 252), _mean((-ncfo).clip(lower=0), 252)))
    d1 = (base - base.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_debtburn_252d_jerk_v127_signal(ncfdebt, ncfo):
    base = np.tanh(_safe_div(_mean(ncfdebt.clip(lower=0), 252), _mean((-ncfo).clip(lower=0), 252)))
    d1 = (base - base.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_invfund_252d_jerk_v128_signal(ncff, ncfi):
    base = np.tanh(_safe_div(_mean((-ncfi).clip(lower=0), 252), _mean(ncff.clip(lower=0), 252)))
    d1 = (base - base.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_opshareflip_252d_jerk_v129_signal(ncfo, ncff, ncfi):
    op = _mean(ncfo.clip(lower=0), 252)
    fin = _mean(ncff.clip(lower=0), 252)
    tot = _mean(ncfo.abs() + ncff.abs() + ncfi.abs(), 252).replace(0, np.nan)
    base = (op - fin) / tot
    d1 = (base - base.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_netextdep_252d_jerk_v130_signal(ncff, ncfo, ncfi):
    pre = _mean(ncfo + ncfi, 252)
    fin = _mean(ncff, 252)
    base = (fin - pre) / (fin.abs() + pre.abs()).replace(0, np.nan)
    d1 = (base - base.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_eqchannel_252d_jerk_v131_signal(ncfcommon, ncff):
    base = _safe_div(_mean(ncfcommon.clip(lower=0), 252), _mean(ncff.clip(lower=0), 252)).clip(upper=3.0)
    d1 = (base - base.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_debtchannel_252d_jerk_v132_signal(ncfdebt, ncff):
    base = _safe_div(_mean(ncfdebt.clip(lower=0), 252), _mean(ncff.clip(lower=0), 252)).clip(upper=3.0)
    d1 = (base - base.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_finturn_252d_jerk_v133_signal(ncff, ncfo):
    base = _safe_div(_mean(ncff.abs(), 252), _mean(ncfo.abs(), 252))
    d1 = (base - base.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_opsuff_252d_jerk_v134_signal(ncfo, ncfi, ncff):
    tot = (_mean(ncfo.abs(), 252) + _mean(ncfi.abs(), 252) + _mean(ncff.abs(), 252)).replace(0, np.nan)
    base = _mean(ncfo, 252) / tot
    d1 = (base - base.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_eqnetbal_252d_jerk_v135_signal(ncfcommon):
    q = _mean(ncfcommon, 21)
    flip = (np.sign(q) != np.sign(q.shift(21))).astype(float)
    base = flip.rolling(252, min_periods=max(2, 252 // 2)).mean()
    d1 = (base - base.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_debtnetbal_252d_jerk_v136_signal(ncfdebt):
    q = _mean(ncfdebt, 21)
    flip = (np.sign(q) != np.sign(q.shift(21))).astype(float)
    base = flip.rolling(252, min_periods=max(2, 252 // 2)).mean()
    d1 = (base - base.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_finivnet_252d_jerk_v137_signal(ncff, ncfi):
    net = _mean(ncff + ncfi, 252)
    sc = (_mean(ncff.abs(), 252) + _mean(ncfi.abs(), 252)).replace(0, np.nan)
    base = _z(net / sc, 252)
    d1 = (base - base.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_repay_252d_jerk_v138_signal(ncfdebt, ncfo):
    base = _safe_div(_mean((-ncfdebt).clip(lower=0), 252), _mean(ncfo.abs(), 252))
    d1 = (base - base.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_buyback_252d_jerk_v139_signal(ncfcommon, ncfo):
    base = np.tanh(_safe_div(_mean((-ncfcommon).clip(lower=0), 252), _mean(ncfo.clip(lower=0), 252)))
    d1 = (base - base.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_totraise_252d_jerk_v140_signal(ncfcommon, ncfdebt, ncfo):
    raises = _mean(ncfcommon.clip(lower=0) + ncfdebt.clip(lower=0), 252)
    eng = (raises.abs() + _mean(ncfo.abs(), 252)).replace(0, np.nan)
    base = raises / eng
    d1 = (base - base.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_finskew_252d_jerk_v141_signal(ncff):
    sc = _std(ncff, 252).replace(0, np.nan)
    centered = ncff - _mean(ncff, 252)
    base = _mean((centered / sc) ** 3, 252)
    d1 = (base - base.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_gapstreak_252d_jerk_v142_signal(ncfo, ncfi):
    deficit = (-(ncfo + ncfi)).clip(lower=0)
    monthly = _mean(deficit, 21)
    peak = monthly.rolling(252, min_periods=max(2, 252 // 2)).max()
    avg = monthly.rolling(252, min_periods=max(2, 252 // 2)).mean().replace(0, np.nan)
    base = peak / avg
    d1 = (base - base.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_finled_252d_jerk_v143_signal(ncff, ncfo):
    led = (ncff.clip(lower=0) > ncfo.clip(lower=0)).astype(float)
    base = led.rolling(252, min_periods=max(2, 252 // 2)).mean()
    d1 = (base - base.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_plugrate_252d_jerk_v144_signal(ncff, ncfo):
    plug = ((ncff > 0) & (ncfo < 0)).astype(float)
    base = plug.rolling(252, min_periods=max(2, 252 // 2)).mean()
    d1 = (base - base.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_finivstreak_252d_jerk_v145_signal(ncff, ncfi):
    co = ((ncff > 0) & (ncfi < 0)).astype(float)
    base = co.rolling(252, min_periods=max(2, 252 // 2)).mean()
    d1 = (base - base.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_finmix3_252d_jerk_v146_signal(ncfcommon, ncfdebt, ncfo):
    e = _mean(ncfcommon.clip(lower=0), 252)
    src = _mean(ncfcommon.clip(lower=0) + ncfdebt.clip(lower=0) + ncfo.clip(lower=0), 252).replace(0, np.nan)
    base = e / src
    d1 = (base - base.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_raisevinv_252d_jerk_v147_signal(ncfcommon, ncfdebt, ncfi):
    raises = _mean(ncfcommon.clip(lower=0) + ncfdebt.clip(lower=0), 252)
    inv = _mean((-ncfi).clip(lower=0), 252).replace(0, np.nan)
    base = np.tanh(raises / inv)
    d1 = (base - base.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_finpersist_252d_jerk_v148_signal(ncff):
    x = ncff - _mean(ncff, 252)
    cov = _mean(x * x.shift(21), 252)
    base = cov / (_std(ncff, 252).replace(0, np.nan) ** 2)
    d1 = (base - base.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_debtpersist_252d_jerk_v149_signal(ncfdebt):
    x = ncfdebt - _mean(ncfdebt, 252)
    cov = _mean(x * x.shift(21), 252)
    base = cov / (_std(ncfdebt, 252).replace(0, np.nan) ** 2)
    d1 = (base - base.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f30fd_f30_financing_dependence_oppersist_252d_jerk_v150_signal(ncfo):
    x = ncfo - _mean(ncfo, 252)
    cov = _mean(x * x.shift(21), 252)
    base = cov / (_std(ncfo, 252).replace(0, np.nan) ** 2)
    d1 = (base - base.shift(63)) / float(63)
    d2 = (d1 - d1.shift(63)) / float(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f30fd_f30_financing_dependence_extrel_63d_jerk_v001_signal,
    f30fd_f30_financing_dependence_burncov_63d_jerk_v002_signal,
    f30fd_f30_financing_dependence_selffund_63d_jerk_v003_signal,
    f30fd_f30_financing_dependence_mix_63d_jerk_v004_signal,
    f30fd_f30_financing_dependence_raiseint_63d_jerk_v005_signal,
    f30fd_f30_financing_dependence_overfund_63d_jerk_v006_signal,
    f30fd_f30_financing_dependence_eqraise_63d_jerk_v007_signal,
    f30fd_f30_financing_dependence_debtdraw_63d_jerk_v008_signal,
    f30fd_f30_financing_dependence_extdep_63d_jerk_v009_signal,
    f30fd_f30_financing_dependence_finopcorr_63d_jerk_v010_signal,
    f30fd_f30_financing_dependence_eqdebtcorr_63d_jerk_v011_signal,
    f30fd_f30_financing_dependence_fininvcorr_63d_jerk_v012_signal,
    f30fd_f30_financing_dependence_opinvcorr_63d_jerk_v013_signal,
    f30fd_f30_financing_dependence_extfrac_63d_jerk_v014_signal,
    f30fd_f30_financing_dependence_eqshare_63d_jerk_v015_signal,
    f30fd_f30_financing_dependence_eqburn_63d_jerk_v016_signal,
    f30fd_f30_financing_dependence_debtburn_63d_jerk_v017_signal,
    f30fd_f30_financing_dependence_invfund_63d_jerk_v018_signal,
    f30fd_f30_financing_dependence_opshareflip_63d_jerk_v019_signal,
    f30fd_f30_financing_dependence_netextdep_63d_jerk_v020_signal,
    f30fd_f30_financing_dependence_eqchannel_63d_jerk_v021_signal,
    f30fd_f30_financing_dependence_debtchannel_63d_jerk_v022_signal,
    f30fd_f30_financing_dependence_finturn_63d_jerk_v023_signal,
    f30fd_f30_financing_dependence_opsuff_63d_jerk_v024_signal,
    f30fd_f30_financing_dependence_eqnetbal_63d_jerk_v025_signal,
    f30fd_f30_financing_dependence_debtnetbal_63d_jerk_v026_signal,
    f30fd_f30_financing_dependence_finivnet_63d_jerk_v027_signal,
    f30fd_f30_financing_dependence_repay_63d_jerk_v028_signal,
    f30fd_f30_financing_dependence_buyback_63d_jerk_v029_signal,
    f30fd_f30_financing_dependence_totraise_63d_jerk_v030_signal,
    f30fd_f30_financing_dependence_finskew_63d_jerk_v031_signal,
    f30fd_f30_financing_dependence_gapstreak_63d_jerk_v032_signal,
    f30fd_f30_financing_dependence_finled_63d_jerk_v033_signal,
    f30fd_f30_financing_dependence_plugrate_63d_jerk_v034_signal,
    f30fd_f30_financing_dependence_finivstreak_63d_jerk_v035_signal,
    f30fd_f30_financing_dependence_finmix3_63d_jerk_v036_signal,
    f30fd_f30_financing_dependence_raisevinv_63d_jerk_v037_signal,
    f30fd_f30_financing_dependence_finpersist_63d_jerk_v038_signal,
    f30fd_f30_financing_dependence_debtpersist_63d_jerk_v039_signal,
    f30fd_f30_financing_dependence_oppersist_63d_jerk_v040_signal,
    f30fd_f30_financing_dependence_reldisp_63d_jerk_v041_signal,
    f30fd_f30_financing_dependence_mixdisp_63d_jerk_v042_signal,
    f30fd_f30_financing_dependence_gapvol_63d_jerk_v043_signal,
    f30fd_f30_financing_dependence_finvol_63d_jerk_v044_signal,
    f30fd_f30_financing_dependence_eqconc_63d_jerk_v045_signal,
    f30fd_f30_financing_dependence_debtconc_63d_jerk_v046_signal,
    f30fd_f30_financing_dependence_raiseburnsync_63d_jerk_v047_signal,
    f30fd_f30_financing_dependence_debtopcorr_63d_jerk_v048_signal,
    f30fd_f30_financing_dependence_eqopcorr_63d_jerk_v049_signal,
    f30fd_f30_financing_dependence_debtsrc3_63d_jerk_v050_signal,
    f30fd_f30_financing_dependence_totburncov_63d_jerk_v051_signal,
    f30fd_f30_financing_dependence_invselffund_63d_jerk_v052_signal,
    f30fd_f30_financing_dependence_returntilt_63d_jerk_v053_signal,
    f30fd_f30_financing_dependence_debttilt_63d_jerk_v054_signal,
    f30fd_f30_financing_dependence_eqdebtspread_63d_jerk_v055_signal,
    f30fd_f30_financing_dependence_extrel_126d_jerk_v056_signal,
    f30fd_f30_financing_dependence_burncov_126d_jerk_v057_signal,
    f30fd_f30_financing_dependence_selffund_126d_jerk_v058_signal,
    f30fd_f30_financing_dependence_mix_126d_jerk_v059_signal,
    f30fd_f30_financing_dependence_raiseint_126d_jerk_v060_signal,
    f30fd_f30_financing_dependence_overfund_126d_jerk_v061_signal,
    f30fd_f30_financing_dependence_eqraise_126d_jerk_v062_signal,
    f30fd_f30_financing_dependence_debtdraw_126d_jerk_v063_signal,
    f30fd_f30_financing_dependence_extdep_126d_jerk_v064_signal,
    f30fd_f30_financing_dependence_finopcorr_126d_jerk_v065_signal,
    f30fd_f30_financing_dependence_eqdebtcorr_126d_jerk_v066_signal,
    f30fd_f30_financing_dependence_fininvcorr_126d_jerk_v067_signal,
    f30fd_f30_financing_dependence_opinvcorr_126d_jerk_v068_signal,
    f30fd_f30_financing_dependence_extfrac_126d_jerk_v069_signal,
    f30fd_f30_financing_dependence_eqshare_126d_jerk_v070_signal,
    f30fd_f30_financing_dependence_eqburn_126d_jerk_v071_signal,
    f30fd_f30_financing_dependence_debtburn_126d_jerk_v072_signal,
    f30fd_f30_financing_dependence_invfund_126d_jerk_v073_signal,
    f30fd_f30_financing_dependence_opshareflip_126d_jerk_v074_signal,
    f30fd_f30_financing_dependence_netextdep_126d_jerk_v075_signal,
    f30fd_f30_financing_dependence_eqchannel_126d_jerk_v076_signal,
    f30fd_f30_financing_dependence_debtchannel_126d_jerk_v077_signal,
    f30fd_f30_financing_dependence_finturn_126d_jerk_v078_signal,
    f30fd_f30_financing_dependence_opsuff_126d_jerk_v079_signal,
    f30fd_f30_financing_dependence_eqnetbal_126d_jerk_v080_signal,
    f30fd_f30_financing_dependence_debtnetbal_126d_jerk_v081_signal,
    f30fd_f30_financing_dependence_finivnet_126d_jerk_v082_signal,
    f30fd_f30_financing_dependence_repay_126d_jerk_v083_signal,
    f30fd_f30_financing_dependence_buyback_126d_jerk_v084_signal,
    f30fd_f30_financing_dependence_totraise_126d_jerk_v085_signal,
    f30fd_f30_financing_dependence_finskew_126d_jerk_v086_signal,
    f30fd_f30_financing_dependence_gapstreak_126d_jerk_v087_signal,
    f30fd_f30_financing_dependence_finled_126d_jerk_v088_signal,
    f30fd_f30_financing_dependence_plugrate_126d_jerk_v089_signal,
    f30fd_f30_financing_dependence_finivstreak_126d_jerk_v090_signal,
    f30fd_f30_financing_dependence_finmix3_126d_jerk_v091_signal,
    f30fd_f30_financing_dependence_raisevinv_126d_jerk_v092_signal,
    f30fd_f30_financing_dependence_finpersist_126d_jerk_v093_signal,
    f30fd_f30_financing_dependence_debtpersist_126d_jerk_v094_signal,
    f30fd_f30_financing_dependence_oppersist_126d_jerk_v095_signal,
    f30fd_f30_financing_dependence_reldisp_126d_jerk_v096_signal,
    f30fd_f30_financing_dependence_mixdisp_126d_jerk_v097_signal,
    f30fd_f30_financing_dependence_gapvol_126d_jerk_v098_signal,
    f30fd_f30_financing_dependence_finvol_126d_jerk_v099_signal,
    f30fd_f30_financing_dependence_eqconc_126d_jerk_v100_signal,
    f30fd_f30_financing_dependence_debtconc_126d_jerk_v101_signal,
    f30fd_f30_financing_dependence_raiseburnsync_126d_jerk_v102_signal,
    f30fd_f30_financing_dependence_debtopcorr_126d_jerk_v103_signal,
    f30fd_f30_financing_dependence_eqopcorr_126d_jerk_v104_signal,
    f30fd_f30_financing_dependence_debtsrc3_126d_jerk_v105_signal,
    f30fd_f30_financing_dependence_totburncov_126d_jerk_v106_signal,
    f30fd_f30_financing_dependence_invselffund_126d_jerk_v107_signal,
    f30fd_f30_financing_dependence_returntilt_126d_jerk_v108_signal,
    f30fd_f30_financing_dependence_debttilt_126d_jerk_v109_signal,
    f30fd_f30_financing_dependence_eqdebtspread_126d_jerk_v110_signal,
    f30fd_f30_financing_dependence_extrel_252d_jerk_v111_signal,
    f30fd_f30_financing_dependence_burncov_252d_jerk_v112_signal,
    f30fd_f30_financing_dependence_selffund_252d_jerk_v113_signal,
    f30fd_f30_financing_dependence_mix_252d_jerk_v114_signal,
    f30fd_f30_financing_dependence_raiseint_252d_jerk_v115_signal,
    f30fd_f30_financing_dependence_overfund_252d_jerk_v116_signal,
    f30fd_f30_financing_dependence_eqraise_252d_jerk_v117_signal,
    f30fd_f30_financing_dependence_debtdraw_252d_jerk_v118_signal,
    f30fd_f30_financing_dependence_extdep_252d_jerk_v119_signal,
    f30fd_f30_financing_dependence_finopcorr_252d_jerk_v120_signal,
    f30fd_f30_financing_dependence_eqdebtcorr_252d_jerk_v121_signal,
    f30fd_f30_financing_dependence_fininvcorr_252d_jerk_v122_signal,
    f30fd_f30_financing_dependence_opinvcorr_252d_jerk_v123_signal,
    f30fd_f30_financing_dependence_extfrac_252d_jerk_v124_signal,
    f30fd_f30_financing_dependence_eqshare_252d_jerk_v125_signal,
    f30fd_f30_financing_dependence_eqburn_252d_jerk_v126_signal,
    f30fd_f30_financing_dependence_debtburn_252d_jerk_v127_signal,
    f30fd_f30_financing_dependence_invfund_252d_jerk_v128_signal,
    f30fd_f30_financing_dependence_opshareflip_252d_jerk_v129_signal,
    f30fd_f30_financing_dependence_netextdep_252d_jerk_v130_signal,
    f30fd_f30_financing_dependence_eqchannel_252d_jerk_v131_signal,
    f30fd_f30_financing_dependence_debtchannel_252d_jerk_v132_signal,
    f30fd_f30_financing_dependence_finturn_252d_jerk_v133_signal,
    f30fd_f30_financing_dependence_opsuff_252d_jerk_v134_signal,
    f30fd_f30_financing_dependence_eqnetbal_252d_jerk_v135_signal,
    f30fd_f30_financing_dependence_debtnetbal_252d_jerk_v136_signal,
    f30fd_f30_financing_dependence_finivnet_252d_jerk_v137_signal,
    f30fd_f30_financing_dependence_repay_252d_jerk_v138_signal,
    f30fd_f30_financing_dependence_buyback_252d_jerk_v139_signal,
    f30fd_f30_financing_dependence_totraise_252d_jerk_v140_signal,
    f30fd_f30_financing_dependence_finskew_252d_jerk_v141_signal,
    f30fd_f30_financing_dependence_gapstreak_252d_jerk_v142_signal,
    f30fd_f30_financing_dependence_finled_252d_jerk_v143_signal,
    f30fd_f30_financing_dependence_plugrate_252d_jerk_v144_signal,
    f30fd_f30_financing_dependence_finivstreak_252d_jerk_v145_signal,
    f30fd_f30_financing_dependence_finmix3_252d_jerk_v146_signal,
    f30fd_f30_financing_dependence_raisevinv_252d_jerk_v147_signal,
    f30fd_f30_financing_dependence_finpersist_252d_jerk_v148_signal,
    f30fd_f30_financing_dependence_debtpersist_252d_jerk_v149_signal,
    f30fd_f30_financing_dependence_oppersist_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F30_FINANCING_DEPENDENCE_REGISTRY_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    ALLOW = {
        "open", "high", "low", "close", "closeadj", "volume",
        "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc", "opex",
        "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc",
        "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff",
        "ncfi", "ncfcommon", "ncfdebt", "ncfbus", "capex", "depamor", "sharesbas",
        "shareswa", "shareswadil", "assets", "assetsc", "tangibles", "intangibles",
        "ppnenet", "investments", "inventory", "receivables", "payables", "equity",
        "retearn", "workingcapital", "debt", "debtc", "debtnc", "liabilities",
        "liabilitiesc", "cashneq", "currentratio", "roic", "roe", "roa", "ros",
        "assetturnover", "invcap", "intexp", "taxexp", "ebt", "sps", "bvps", "de",
        "ncfdiv", "dps", "divyield", "payoutratio", "prefdivis",
        "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
        "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal",
        "fndholders", "undholders", "prfholders", "dbtholders", "putholders",
        "putvalue", "cllholders", "cllvalue", "wntholders", "wntvalue", "dbtvalue",
    }

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    # Signed cash flows via _fund (ALL of ncff/ncfcommon/ncfdebt/ncfo/ncfi,
    # allow_neg=True), built to genuinely swing sign (centered level + funding cycle).
    def _signed(seed, base, phase, amp, period):
        raw = _fund(seed, base=base, drift=0.0, vol=0.08, allow_neg=True)
        centered = raw - raw.rolling(252, min_periods=1).mean()
        gn = np.random.default_rng(seed + 9000)
        cyc = amp * base * 0.4 * np.sin(np.arange(n) / period * 2 * np.pi + phase)
        jitter = gn.normal(0.0, base * 0.10, n)
        return (centered + pd.Series(cyc) + pd.Series(jitter))

    ncfo = _signed(101, 8e7, 0.0, 1.0, 71.0).rename("ncfo")
    ncff = _signed(102, 9e7, 1.0, 1.1, 53.0).rename("ncff")
    ncfi = _signed(103, 6e7, 2.0, 0.9, 89.0).rename("ncfi")
    ncfcommon = _signed(104, 7e7, 3.0, 1.0, 47.0).rename("ncfcommon")
    ncfdebt = _signed(105, 5e7, 4.0, 1.2, 101.0).rename("ncfdebt")

    cols = {"ncfo": ncfo, "ncff": ncff, "ncfi": ncfi,
            "ncfcommon": ncfcommon, "ncfdebt": ncfdebt}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "BADCOL %s: %s" % (name, meta["inputs"])
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
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

    print("OK f30_financing_dependence_3rd_derivatives_001_150_claude: %d features pass" % n_features)
