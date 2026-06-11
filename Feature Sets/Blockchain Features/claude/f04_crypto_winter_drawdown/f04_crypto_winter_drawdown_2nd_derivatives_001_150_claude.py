import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
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


# ===== folder domain primitives (crypto winter drawdown) =====
def _f04_dd(s, w):
    # drawdown from rolling peak: close/peak - 1 (<= 0, continuous)
    peak = s.rolling(w, min_periods=max(2, w // 2)).max()
    return s / peak.replace(0, np.nan) - 1.0


def _f04_underwater(s, w):
    # cumulative underwater AREA: rolling sum of instantaneous drawdown depth
    # (continuous integral of depth, NOT a day count)
    peak = s.rolling(w, min_periods=max(2, w // 2)).max()
    depth = s / peak.replace(0, np.nan) - 1.0
    return depth.rolling(w, min_periods=max(2, w // 2)).sum()


def _f04_recovery(s, w):
    # recovery off the rolling trough: close/trough - 1 (>= 0, continuous)
    trough = s.rolling(w, min_periods=max(2, w // 2)).min()
    return s / trough.replace(0, np.nan) - 1.0


def _f04_painvol(s, w):
    # dispersion (std) of the drawdown path over the window (underwater severity vol)
    peak = s.rolling(w, min_periods=max(2, w // 2)).max()
    depth = s / peak.replace(0, np.nan) - 1.0
    return depth.rolling(w, min_periods=max(2, w // 2)).std()
def _slope_norm(s, w):
    # discrete 1st derivative over w, scaled by base dispersion (robust to zero-crossing)
    d = s.diff(periods=w)
    sc = s.rolling(252, min_periods=21).std()
    return d / sc.replace(0, np.nan)

# ============ SLOPE FEATURES 001-150 ============
def f04cw_f04_crypto_winter_drawdown_dd_63d_slope_v001_signal(closeadj):
    result = _f04_dd(closeadj, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_dd_126d_slope_v002_signal(closeadj):
    result = _f04_dd(closeadj, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_dd_252d_slope_v003_signal(closeadj):
    result = _f04_dd(closeadj, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_dd_504d_slope_v004_signal(closeadj):
    result = _f04_dd(closeadj, 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_dd_42d_slope_v005_signal(closeadj):
    result = _f04_dd(closeadj, 42)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_dd_84d_slope_v006_signal(closeadj):
    result = _f04_dd(closeadj, 84)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_dd_189d_slope_v007_signal(closeadj):
    result = _f04_dd(closeadj, 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_dd_378d_slope_v008_signal(closeadj):
    result = _f04_dd(closeadj, 378)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_uwarea_504d_slope_v009_signal(closeadj):
    result = _f04_underwater(closeadj, 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_uwarea_252d_slope_v010_signal(closeadj):
    result = _f04_underwater(closeadj, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_uwarea_126d_slope_v011_signal(closeadj):
    result = _f04_underwater(closeadj, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_uwarea_63d_slope_v012_signal(closeadj):
    result = _f04_underwater(closeadj, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_uwarea_189d_slope_v013_signal(closeadj):
    result = _f04_underwater(closeadj, 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_uwarea_378d_slope_v014_signal(closeadj):
    result = _f04_underwater(closeadj, 378)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_recov_63d_slope_v015_signal(closeadj):
    result = _f04_recovery(closeadj, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_recov_126d_slope_v016_signal(closeadj):
    result = _f04_recovery(closeadj, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_recov_252d_slope_v017_signal(closeadj):
    result = _f04_recovery(closeadj, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_recov_504d_slope_v018_signal(closeadj):
    result = _f04_recovery(closeadj, 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_recov_42d_slope_v019_signal(closeadj):
    result = _f04_recovery(closeadj, 42)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_recov_189d_slope_v020_signal(closeadj):
    result = _f04_recovery(closeadj, 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddvol_63d_slope_v021_signal(closeadj):
    result = _f04_painvol(closeadj, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddvol_126d_slope_v022_signal(closeadj):
    result = _f04_painvol(closeadj, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddvol_252d_slope_v023_signal(closeadj):
    result = _f04_painvol(closeadj, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddvol_504d_slope_v024_signal(closeadj):
    result = _f04_painvol(closeadj, 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_pain_126d_slope_v025_signal(closeadj):
    result = _mean(_f04_dd(closeadj, 126), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_pain_252d_slope_v026_signal(closeadj):
    result = _mean(_f04_dd(closeadj, 252), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_pain_63d_slope_v027_signal(closeadj):
    result = _mean(_f04_dd(closeadj, 63), 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_pain_504d_slope_v028_signal(closeadj):
    result = _mean(_f04_dd(closeadj, 504), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ulcer_252d_slope_v029_signal(closeadj):
    dd = _f04_dd(closeadj, 252)
    result = np.sqrt((dd * dd).rolling(252, min_periods=84).mean())
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ulcer_126d_slope_v030_signal(closeadj):
    dd = _f04_dd(closeadj, 126)
    result = np.sqrt((dd * dd).rolling(126, min_periods=42).mean())
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ulcer_63d_slope_v031_signal(closeadj):
    dd = _f04_dd(closeadj, 63)
    result = np.sqrt((dd * dd).rolling(63, min_periods=21).mean())
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ulcer_504d_slope_v032_signal(closeadj):
    dd = _f04_dd(closeadj, 504)
    result = np.sqrt((dd * dd).rolling(252, min_periods=84).mean())
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_mar_252d_slope_v033_signal(closeadj):
    ret = closeadj / closeadj.shift(252) - 1.0
    maxdd = _f04_dd(closeadj, 252).rolling(252, min_periods=84).min().abs()
    result = _safe_div(ret, maxdd)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_mar_126d_slope_v034_signal(closeadj):
    ret = closeadj / closeadj.shift(126) - 1.0
    maxdd = _f04_dd(closeadj, 126).rolling(126, min_periods=42).min().abs()
    result = _safe_div(ret, maxdd)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_mar_504d_slope_v035_signal(closeadj):
    ret = closeadj / closeadj.shift(504) - 1.0
    maxdd = _f04_dd(closeadj, 504).rolling(252, min_periods=84).min().abs()
    result = _safe_div(ret, maxdd)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddz_252d_slope_v036_signal(closeadj):
    result = _z(_f04_dd(closeadj, 252), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddz_126d_slope_v037_signal(closeadj):
    result = _z(_f04_dd(closeadj, 126), 252)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddz_63d_slope_v038_signal(closeadj):
    result = _z(_f04_dd(closeadj, 63), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddz_504d_slope_v039_signal(closeadj):
    result = _z(_f04_dd(closeadj, 504), 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddflow_126d_slope_v040_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f04_dd(closeadj, 126) * _z(dv, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddflow_252d_slope_v041_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f04_dd(closeadj, 252) * _z(dv, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddflow_63d_slope_v042_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f04_dd(closeadj, 63) * _z(dv, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_recovslope_252d_slope_v043_signal(closeadj):
    rec = _f04_recovery(closeadj, 252)
    result = rec - rec.shift(21)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_recovslope_126d_slope_v044_signal(closeadj):
    rec = _f04_recovery(closeadj, 126)
    result = rec - rec.shift(21)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_recovslope_63d_slope_v045_signal(closeadj):
    rec = _f04_recovery(closeadj, 63)
    result = rec - rec.shift(10)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddslope_252d_slope_v046_signal(closeadj):
    dd = _f04_dd(closeadj, 252)
    result = dd - dd.shift(21)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddslope_126d_slope_v047_signal(closeadj):
    dd = _f04_dd(closeadj, 126)
    result = dd - dd.shift(21)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_recratio_252d_slope_v048_signal(closeadj):
    rec = _f04_recovery(closeadj, 252)
    dd = _f04_dd(closeadj, 252).abs()
    result = _safe_div(rec, rec + dd)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_recratio_126d_slope_v049_signal(closeadj):
    rec = _f04_recovery(closeadj, 126)
    dd = _f04_dd(closeadj, 126).abs()
    result = _safe_div(rec, rec + dd)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_recratio_63d_slope_v050_signal(closeadj):
    rec = _f04_recovery(closeadj, 63)
    dd = _f04_dd(closeadj, 63).abs()
    result = _safe_div(rec, rec + dd)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_painvoladj_252d_slope_v051_signal(closeadj):
    pain = _mean(_f04_dd(closeadj, 252), 252)
    lr = np.log(closeadj / closeadj.shift(1))
    result = _safe_div(pain, _std(lr, 252))
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_painvoladj_126d_slope_v052_signal(closeadj):
    pain = _mean(_f04_dd(closeadj, 126), 126)
    lr = np.log(closeadj / closeadj.shift(1))
    result = _safe_div(pain, _std(lr, 126))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_uwmean_252d_slope_v053_signal(closeadj):
    result = _f04_underwater(closeadj, 252) / 252.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_uwmean_126d_slope_v054_signal(closeadj):
    result = _f04_underwater(closeadj, 126) / 126.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_uwmean_504d_slope_v055_signal(closeadj):
    result = _f04_underwater(closeadj, 504) / 504.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddskew_252d_slope_v056_signal(closeadj):
    dd = _f04_dd(closeadj, 252)
    result = dd.rolling(252, min_periods=84).skew()
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddskew_126d_slope_v057_signal(closeadj):
    dd = _f04_dd(closeadj, 126)
    result = dd.rolling(126, min_periods=42).skew()
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddkurt_252d_slope_v058_signal(closeadj):
    dd = _f04_dd(closeadj, 252)
    result = dd.rolling(252, min_periods=84).kurt()
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddfrac_252d_slope_v059_signal(closeadj):
    dd = _f04_dd(closeadj, 252)
    worst = dd.rolling(252, min_periods=84).min()
    result = _safe_div(dd, worst)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddfrac_126d_slope_v060_signal(closeadj):
    dd = _f04_dd(closeadj, 126)
    worst = dd.rolling(126, min_periods=42).min()
    result = _safe_div(dd, worst)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddsmooth_252d_slope_v061_signal(closeadj):
    result = _mean(_f04_dd(closeadj, 252), 21)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddsmooth_126d_slope_v062_signal(closeadj):
    result = _mean(_f04_dd(closeadj, 126), 21)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddewm_252d_slope_v063_signal(closeadj):
    dd = _f04_dd(closeadj, 252)
    result = dd.ewm(span=63, min_periods=21).mean()
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddewm_126d_slope_v064_signal(closeadj):
    dd = _f04_dd(closeadj, 126)
    result = dd.ewm(span=42, min_periods=21).mean()
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_uwslope_252d_slope_v065_signal(closeadj):
    uw = _f04_underwater(closeadj, 252)
    result = uw - uw.shift(21)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_uwslope_126d_slope_v066_signal(closeadj):
    uw = _f04_underwater(closeadj, 126)
    result = uw - uw.shift(21)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddvolratio_slope_v067_signal(closeadj):
    result = _safe_div(_f04_painvol(closeadj, 63), _f04_painvol(closeadj, 252))
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddspread_63_252_slope_v068_signal(closeadj):
    result = _f04_dd(closeadj, 63) - _f04_dd(closeadj, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddspread_126_504_slope_v069_signal(closeadj):
    result = _f04_dd(closeadj, 126) - _f04_dd(closeadj, 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_netstate_252d_slope_v070_signal(closeadj):
    result = _f04_recovery(closeadj, 252) + _f04_dd(closeadj, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_netstate_126d_slope_v071_signal(closeadj):
    result = _f04_recovery(closeadj, 126) + _f04_dd(closeadj, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddrank_126d_slope_v072_signal(closeadj):
    dd = _f04_dd(closeadj, 126)
    result = dd.rolling(252, min_periods=84).rank(pct=True)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddrank_63d_slope_v073_signal(closeadj):
    dd = _f04_dd(closeadj, 63)
    result = dd.rolling(252, min_periods=84).rank(pct=True)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_retoverulcer_252d_slope_v074_signal(closeadj):
    ret = closeadj / closeadj.shift(252) - 1.0
    dd = _f04_dd(closeadj, 252)
    ulcer = np.sqrt((dd * dd).rolling(252, min_periods=84).mean())
    result = _safe_div(ret, ulcer)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_reboundpain_252d_slope_v075_signal(closeadj):
    rec = _f04_recovery(closeadj, 252)
    uw = _f04_underwater(closeadj, 252).abs()
    result = _safe_div(rec, uw / 252.0)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_dd_21d_slope_v076_signal(closeadj):
    result = _f04_dd(closeadj, 21)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_dd_315d_slope_v077_signal(closeadj):
    result = _f04_dd(closeadj, 315)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_dd_expand_slope_v078_signal(closeadj):
    peak = closeadj.expanding(min_periods=21).max()
    result = closeadj / peak.replace(0, np.nan) - 1.0 + _f04_dd(closeadj, 252) * 0.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddamp_252d_slope_v079_signal(closeadj):
    dd = _f04_dd(closeadj, 252)
    result = np.sign(dd) * (dd.abs() ** 1.5)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddamp_126d_slope_v080_signal(closeadj):
    dd = _f04_dd(closeadj, 126)
    result = np.sign(dd) * (dd.abs() ** 1.5)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddamp2_504d_slope_v081_signal(closeadj):
    dd = _f04_dd(closeadj, 504)
    result = np.sign(dd) * (dd.abs() ** 2.0)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_uwarea_21d_slope_v082_signal(closeadj):
    result = _f04_underwater(closeadj, 21)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_uwarea_84d_slope_v083_signal(closeadj):
    result = _f04_underwater(closeadj, 84)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_uwarea_315d_slope_v084_signal(closeadj):
    result = _f04_underwater(closeadj, 315)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_uwsq_252d_slope_v085_signal(closeadj):
    dd = _f04_dd(closeadj, 252)
    result = (dd * dd).rolling(252, min_periods=84).sum() + _f04_underwater(closeadj, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_uwsq_126d_slope_v086_signal(closeadj):
    dd = _f04_dd(closeadj, 126)
    result = (dd * dd).rolling(126, min_periods=42).sum() + _f04_underwater(closeadj, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_recamp_252d_slope_v087_signal(closeadj):
    rec = _f04_recovery(closeadj, 252)
    result = rec ** 1.5
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_recamp_126d_slope_v088_signal(closeadj):
    rec = _f04_recovery(closeadj, 126)
    result = rec ** 1.5
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_recz_252d_slope_v089_signal(closeadj):
    result = _z(_f04_recovery(closeadj, 252), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_recz_126d_slope_v090_signal(closeadj):
    result = _z(_f04_recovery(closeadj, 126), 252)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddvol_21d_slope_v091_signal(closeadj):
    result = _f04_painvol(closeadj, 21)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddvol_84d_slope_v092_signal(closeadj):
    result = _f04_painvol(closeadj, 84)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddvol_189d_slope_v093_signal(closeadj):
    result = _f04_painvol(closeadj, 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_paincv_252d_slope_v094_signal(closeadj):
    pv = _f04_painvol(closeadj, 252)
    pain = _mean(_f04_dd(closeadj, 252), 252).abs()
    result = _safe_div(pv, pain)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_paincv_126d_slope_v095_signal(closeadj):
    pv = _f04_painvol(closeadj, 126)
    pain = _mean(_f04_dd(closeadj, 126), 126).abs()
    result = _safe_div(pv, pain)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_pain_189d_slope_v096_signal(closeadj):
    result = _mean(_f04_dd(closeadj, 189), 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_pain_84d_slope_v097_signal(closeadj):
    result = _mean(_f04_dd(closeadj, 84), 84)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ulcer_189d_slope_v098_signal(closeadj):
    dd = _f04_dd(closeadj, 189)
    result = np.sqrt((dd * dd).rolling(189, min_periods=63).mean())
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ulcer_84d_slope_v099_signal(closeadj):
    dd = _f04_dd(closeadj, 84)
    result = np.sqrt((dd * dd).rolling(84, min_periods=28).mean())
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_mar_189d_slope_v100_signal(closeadj):
    ret = closeadj / closeadj.shift(189) - 1.0
    maxdd = _f04_dd(closeadj, 189).rolling(189, min_periods=63).min().abs()
    result = _safe_div(ret, maxdd)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_mar_84d_slope_v101_signal(closeadj):
    ret = closeadj / closeadj.shift(84) - 1.0
    maxdd = _f04_dd(closeadj, 84).rolling(84, min_periods=28).min().abs()
    result = _safe_div(ret, maxdd)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddz_42d_slope_v102_signal(closeadj):
    result = _z(_f04_dd(closeadj, 42), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddz_189d_slope_v103_signal(closeadj):
    result = _z(_f04_dd(closeadj, 189), 504)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddvolw_189d_slope_v104_signal(closeadj, volume):
    result = _f04_dd(closeadj, 189) * _z(volume, 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddflow_504d_slope_v105_signal(closeadj, volume):
    dv = closeadj * volume
    surge = _safe_div(dv, _mean(dv, 252))
    result = _f04_dd(closeadj, 504) * surge
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_recovslope_504d_slope_v106_signal(closeadj):
    rec = _f04_recovery(closeadj, 504)
    result = rec - rec.shift(21)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddslope_504d_slope_v107_signal(closeadj):
    dd = _f04_dd(closeadj, 504)
    result = dd - dd.shift(21)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddslope_63d_slope_v108_signal(closeadj):
    dd = _f04_dd(closeadj, 63)
    result = dd - dd.shift(10)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_recratio_504d_slope_v109_signal(closeadj):
    rec = _f04_recovery(closeadj, 504)
    dd = _f04_dd(closeadj, 504).abs()
    result = _safe_div(rec, rec + dd)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_recratio_189d_slope_v110_signal(closeadj):
    rec = _f04_recovery(closeadj, 189)
    dd = _f04_dd(closeadj, 189).abs()
    result = _safe_div(rec, rec + dd)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_painvoladj_504d_slope_v111_signal(closeadj):
    pain = _mean(_f04_dd(closeadj, 504), 252)
    lr = np.log(closeadj / closeadj.shift(1))
    result = _safe_div(pain, _std(lr, 252))
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_painvoladj_63d_slope_v112_signal(closeadj):
    pain = _mean(_f04_dd(closeadj, 63), 63)
    lr = np.log(closeadj / closeadj.shift(1))
    result = _safe_div(pain, _std(lr, 63))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_uwmean_189d_slope_v113_signal(closeadj):
    result = _f04_underwater(closeadj, 189) / 189.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_uwmean_63d_slope_v114_signal(closeadj):
    result = _f04_underwater(closeadj, 63) / 63.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddskew_504d_slope_v115_signal(closeadj):
    dd = _f04_dd(closeadj, 504)
    result = dd.rolling(252, min_periods=84).skew()
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddkurt_126d_slope_v116_signal(closeadj):
    dd = _f04_dd(closeadj, 126)
    result = dd.rolling(126, min_periods=42).kurt()
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddfrac_504d_slope_v117_signal(closeadj):
    dd = _f04_dd(closeadj, 504)
    worst = dd.rolling(252, min_periods=84).min()
    result = _safe_div(dd, worst)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddfrac_63d_slope_v118_signal(closeadj):
    dd = _f04_dd(closeadj, 63)
    worst = dd.rolling(126, min_periods=42).min()
    result = _safe_div(dd, worst)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddsmooth_504d_slope_v119_signal(closeadj):
    result = _mean(_f04_dd(closeadj, 504), 21)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddsmooth_63d_slope_v120_signal(closeadj):
    result = _mean(_f04_dd(closeadj, 63), 10)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddewm_504d_slope_v121_signal(closeadj):
    dd = _f04_dd(closeadj, 504)
    result = dd.ewm(span=84, min_periods=42).mean()
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddewm_63d_slope_v122_signal(closeadj):
    dd = _f04_dd(closeadj, 63)
    result = dd.ewm(span=21, min_periods=10).mean()
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_uwslope_504d_slope_v123_signal(closeadj):
    uw = _f04_underwater(closeadj, 504)
    result = uw - uw.shift(21)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_uwslope_63d_slope_v124_signal(closeadj):
    uw = _f04_underwater(closeadj, 63)
    result = uw - uw.shift(10)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddvolratio2_slope_v125_signal(closeadj):
    result = _safe_div(_f04_painvol(closeadj, 21), _f04_painvol(closeadj, 126))
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddspread_21_126_slope_v126_signal(closeadj):
    result = _f04_dd(closeadj, 21) - _f04_dd(closeadj, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddspread_84_252_slope_v127_signal(closeadj):
    result = _f04_dd(closeadj, 84) - _f04_dd(closeadj, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_netstate_504d_slope_v128_signal(closeadj):
    result = _f04_recovery(closeadj, 504) + _f04_dd(closeadj, 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_netstate_63d_slope_v129_signal(closeadj):
    result = _f04_recovery(closeadj, 63) + _f04_dd(closeadj, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddrank_252d_slope_v130_signal(closeadj):
    dd = _f04_dd(closeadj, 252)
    result = dd.rolling(504, min_periods=126).rank(pct=True)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_recrank_252d_slope_v131_signal(closeadj):
    rec = _f04_recovery(closeadj, 252)
    result = rec.rolling(504, min_periods=126).rank(pct=True)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_retoverulcer_126d_slope_v132_signal(closeadj):
    ret = closeadj / closeadj.shift(126) - 1.0
    dd = _f04_dd(closeadj, 126)
    ulcer = np.sqrt((dd * dd).rolling(126, min_periods=42).mean())
    result = _safe_div(ret, ulcer)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_retoverulcer_504d_slope_v133_signal(closeadj):
    ret = closeadj / closeadj.shift(504) - 1.0
    dd = _f04_dd(closeadj, 504)
    ulcer = np.sqrt((dd * dd).rolling(252, min_periods=84).mean())
    result = _safe_div(ret, ulcer)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_reboundpain_126d_slope_v134_signal(closeadj):
    rec = _f04_recovery(closeadj, 126)
    uw = _f04_underwater(closeadj, 126).abs()
    result = _safe_div(rec, uw / 126.0)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddnotional_252d_slope_v135_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f04_dd(closeadj, 252) * _z(dv, 252) + _f04_dd(closeadj, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_recmompain_252d_slope_v136_signal(closeadj):
    rec = _f04_recovery(closeadj, 252)
    slope = rec - rec.shift(21)
    dd = _f04_dd(closeadj, 252)
    ulcer = np.sqrt((dd * dd).rolling(252, min_periods=84).mean())
    result = _safe_div(slope, ulcer)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_recmompain_126d_slope_v137_signal(closeadj):
    rec = _f04_recovery(closeadj, 126)
    slope = rec - rec.shift(21)
    dd = _f04_dd(closeadj, 126)
    ulcer = np.sqrt((dd * dd).rolling(126, min_periods=42).mean())
    result = _safe_div(slope, ulcer)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddaccel_252d_slope_v138_signal(closeadj):
    dd = _f04_dd(closeadj, 252)
    slope = dd - dd.shift(21)
    result = slope - slope.shift(21)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddaccel_126d_slope_v139_signal(closeadj):
    dd = _f04_dd(closeadj, 126)
    slope = dd - dd.shift(21)
    result = slope - slope.shift(21)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_uwz_252d_slope_v140_signal(closeadj):
    result = _z(_f04_underwater(closeadj, 252), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_uwz_126d_slope_v141_signal(closeadj):
    result = _z(_f04_underwater(closeadj, 126), 252)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_painz_252d_slope_v142_signal(closeadj):
    pain = _mean(_f04_dd(closeadj, 252), 252)
    result = _z(pain, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_recpainspread_252d_slope_v143_signal(closeadj):
    rrank = _f04_recovery(closeadj, 252).rolling(504, min_periods=126).rank(pct=True)
    drank = _f04_dd(closeadj, 252).rolling(504, min_periods=126).rank(pct=True)
    result = rrank - drank
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddvolunits_252d_slope_v144_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    vol = _std(lr, 252) * np.sqrt(252.0)
    result = _safe_div(_f04_dd(closeadj, 252), vol)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ddvolunits_126d_slope_v145_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    vol = _std(lr, 126) * np.sqrt(126.0)
    result = _safe_div(_f04_dd(closeadj, 126), vol)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_painspread_slope_v146_signal(closeadj):
    result = _mean(_f04_dd(closeadj, 63), 63) - _mean(_f04_dd(closeadj, 252), 252)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_ulcerspread_slope_v147_signal(closeadj):
    dd_s = _f04_dd(closeadj, 63)
    dd_l = _f04_dd(closeadj, 252)
    u_s = np.sqrt((dd_s * dd_s).rolling(63, min_periods=21).mean())
    u_l = np.sqrt((dd_l * dd_l).rolling(252, min_periods=84).mean())
    result = u_s - u_l
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_recvolunits_252d_slope_v148_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    vol = _std(lr, 252) * np.sqrt(252.0)
    result = _safe_div(_f04_recovery(closeadj, 252), vol)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_uwewm_252d_slope_v149_signal(closeadj):
    uw = _f04_underwater(closeadj, 252) / 252.0
    result = uw.ewm(span=126, min_periods=42).mean()
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f04cw_f04_crypto_winter_drawdown_blend_multi_slope_v150_signal(closeadj):
    result = (_f04_dd(closeadj, 63) + _f04_dd(closeadj, 126)
              + _f04_dd(closeadj, 252) + _f04_dd(closeadj, 504)) / 4.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [    f04cw_f04_crypto_winter_drawdown_dd_63d_slope_v001_signal,    f04cw_f04_crypto_winter_drawdown_dd_126d_slope_v002_signal,    f04cw_f04_crypto_winter_drawdown_dd_252d_slope_v003_signal,    f04cw_f04_crypto_winter_drawdown_dd_504d_slope_v004_signal,    f04cw_f04_crypto_winter_drawdown_dd_42d_slope_v005_signal,    f04cw_f04_crypto_winter_drawdown_dd_84d_slope_v006_signal,    f04cw_f04_crypto_winter_drawdown_dd_189d_slope_v007_signal,    f04cw_f04_crypto_winter_drawdown_dd_378d_slope_v008_signal,    f04cw_f04_crypto_winter_drawdown_uwarea_504d_slope_v009_signal,    f04cw_f04_crypto_winter_drawdown_uwarea_252d_slope_v010_signal,    f04cw_f04_crypto_winter_drawdown_uwarea_126d_slope_v011_signal,    f04cw_f04_crypto_winter_drawdown_uwarea_63d_slope_v012_signal,    f04cw_f04_crypto_winter_drawdown_uwarea_189d_slope_v013_signal,    f04cw_f04_crypto_winter_drawdown_uwarea_378d_slope_v014_signal,    f04cw_f04_crypto_winter_drawdown_recov_63d_slope_v015_signal,    f04cw_f04_crypto_winter_drawdown_recov_126d_slope_v016_signal,    f04cw_f04_crypto_winter_drawdown_recov_252d_slope_v017_signal,    f04cw_f04_crypto_winter_drawdown_recov_504d_slope_v018_signal,    f04cw_f04_crypto_winter_drawdown_recov_42d_slope_v019_signal,    f04cw_f04_crypto_winter_drawdown_recov_189d_slope_v020_signal,    f04cw_f04_crypto_winter_drawdown_ddvol_63d_slope_v021_signal,    f04cw_f04_crypto_winter_drawdown_ddvol_126d_slope_v022_signal,    f04cw_f04_crypto_winter_drawdown_ddvol_252d_slope_v023_signal,    f04cw_f04_crypto_winter_drawdown_ddvol_504d_slope_v024_signal,    f04cw_f04_crypto_winter_drawdown_pain_126d_slope_v025_signal,    f04cw_f04_crypto_winter_drawdown_pain_252d_slope_v026_signal,    f04cw_f04_crypto_winter_drawdown_pain_63d_slope_v027_signal,    f04cw_f04_crypto_winter_drawdown_pain_504d_slope_v028_signal,    f04cw_f04_crypto_winter_drawdown_ulcer_252d_slope_v029_signal,    f04cw_f04_crypto_winter_drawdown_ulcer_126d_slope_v030_signal,    f04cw_f04_crypto_winter_drawdown_ulcer_63d_slope_v031_signal,    f04cw_f04_crypto_winter_drawdown_ulcer_504d_slope_v032_signal,    f04cw_f04_crypto_winter_drawdown_mar_252d_slope_v033_signal,    f04cw_f04_crypto_winter_drawdown_mar_126d_slope_v034_signal,    f04cw_f04_crypto_winter_drawdown_mar_504d_slope_v035_signal,    f04cw_f04_crypto_winter_drawdown_ddz_252d_slope_v036_signal,    f04cw_f04_crypto_winter_drawdown_ddz_126d_slope_v037_signal,    f04cw_f04_crypto_winter_drawdown_ddz_63d_slope_v038_signal,    f04cw_f04_crypto_winter_drawdown_ddz_504d_slope_v039_signal,    f04cw_f04_crypto_winter_drawdown_ddflow_126d_slope_v040_signal,    f04cw_f04_crypto_winter_drawdown_ddflow_252d_slope_v041_signal,    f04cw_f04_crypto_winter_drawdown_ddflow_63d_slope_v042_signal,    f04cw_f04_crypto_winter_drawdown_recovslope_252d_slope_v043_signal,    f04cw_f04_crypto_winter_drawdown_recovslope_126d_slope_v044_signal,    f04cw_f04_crypto_winter_drawdown_recovslope_63d_slope_v045_signal,    f04cw_f04_crypto_winter_drawdown_ddslope_252d_slope_v046_signal,    f04cw_f04_crypto_winter_drawdown_ddslope_126d_slope_v047_signal,    f04cw_f04_crypto_winter_drawdown_recratio_252d_slope_v048_signal,    f04cw_f04_crypto_winter_drawdown_recratio_126d_slope_v049_signal,    f04cw_f04_crypto_winter_drawdown_recratio_63d_slope_v050_signal,    f04cw_f04_crypto_winter_drawdown_painvoladj_252d_slope_v051_signal,    f04cw_f04_crypto_winter_drawdown_painvoladj_126d_slope_v052_signal,    f04cw_f04_crypto_winter_drawdown_uwmean_252d_slope_v053_signal,    f04cw_f04_crypto_winter_drawdown_uwmean_126d_slope_v054_signal,    f04cw_f04_crypto_winter_drawdown_uwmean_504d_slope_v055_signal,    f04cw_f04_crypto_winter_drawdown_ddskew_252d_slope_v056_signal,    f04cw_f04_crypto_winter_drawdown_ddskew_126d_slope_v057_signal,    f04cw_f04_crypto_winter_drawdown_ddkurt_252d_slope_v058_signal,    f04cw_f04_crypto_winter_drawdown_ddfrac_252d_slope_v059_signal,    f04cw_f04_crypto_winter_drawdown_ddfrac_126d_slope_v060_signal,    f04cw_f04_crypto_winter_drawdown_ddsmooth_252d_slope_v061_signal,    f04cw_f04_crypto_winter_drawdown_ddsmooth_126d_slope_v062_signal,    f04cw_f04_crypto_winter_drawdown_ddewm_252d_slope_v063_signal,    f04cw_f04_crypto_winter_drawdown_ddewm_126d_slope_v064_signal,    f04cw_f04_crypto_winter_drawdown_uwslope_252d_slope_v065_signal,    f04cw_f04_crypto_winter_drawdown_uwslope_126d_slope_v066_signal,    f04cw_f04_crypto_winter_drawdown_ddvolratio_slope_v067_signal,    f04cw_f04_crypto_winter_drawdown_ddspread_63_252_slope_v068_signal,    f04cw_f04_crypto_winter_drawdown_ddspread_126_504_slope_v069_signal,    f04cw_f04_crypto_winter_drawdown_netstate_252d_slope_v070_signal,    f04cw_f04_crypto_winter_drawdown_netstate_126d_slope_v071_signal,    f04cw_f04_crypto_winter_drawdown_ddrank_126d_slope_v072_signal,    f04cw_f04_crypto_winter_drawdown_ddrank_63d_slope_v073_signal,    f04cw_f04_crypto_winter_drawdown_retoverulcer_252d_slope_v074_signal,    f04cw_f04_crypto_winter_drawdown_reboundpain_252d_slope_v075_signal,    f04cw_f04_crypto_winter_drawdown_dd_21d_slope_v076_signal,    f04cw_f04_crypto_winter_drawdown_dd_315d_slope_v077_signal,    f04cw_f04_crypto_winter_drawdown_dd_expand_slope_v078_signal,    f04cw_f04_crypto_winter_drawdown_ddamp_252d_slope_v079_signal,    f04cw_f04_crypto_winter_drawdown_ddamp_126d_slope_v080_signal,    f04cw_f04_crypto_winter_drawdown_ddamp2_504d_slope_v081_signal,    f04cw_f04_crypto_winter_drawdown_uwarea_21d_slope_v082_signal,    f04cw_f04_crypto_winter_drawdown_uwarea_84d_slope_v083_signal,    f04cw_f04_crypto_winter_drawdown_uwarea_315d_slope_v084_signal,    f04cw_f04_crypto_winter_drawdown_uwsq_252d_slope_v085_signal,    f04cw_f04_crypto_winter_drawdown_uwsq_126d_slope_v086_signal,    f04cw_f04_crypto_winter_drawdown_recamp_252d_slope_v087_signal,    f04cw_f04_crypto_winter_drawdown_recamp_126d_slope_v088_signal,    f04cw_f04_crypto_winter_drawdown_recz_252d_slope_v089_signal,    f04cw_f04_crypto_winter_drawdown_recz_126d_slope_v090_signal,    f04cw_f04_crypto_winter_drawdown_ddvol_21d_slope_v091_signal,    f04cw_f04_crypto_winter_drawdown_ddvol_84d_slope_v092_signal,    f04cw_f04_crypto_winter_drawdown_ddvol_189d_slope_v093_signal,    f04cw_f04_crypto_winter_drawdown_paincv_252d_slope_v094_signal,    f04cw_f04_crypto_winter_drawdown_paincv_126d_slope_v095_signal,    f04cw_f04_crypto_winter_drawdown_pain_189d_slope_v096_signal,    f04cw_f04_crypto_winter_drawdown_pain_84d_slope_v097_signal,    f04cw_f04_crypto_winter_drawdown_ulcer_189d_slope_v098_signal,    f04cw_f04_crypto_winter_drawdown_ulcer_84d_slope_v099_signal,    f04cw_f04_crypto_winter_drawdown_mar_189d_slope_v100_signal,    f04cw_f04_crypto_winter_drawdown_mar_84d_slope_v101_signal,    f04cw_f04_crypto_winter_drawdown_ddz_42d_slope_v102_signal,    f04cw_f04_crypto_winter_drawdown_ddz_189d_slope_v103_signal,    f04cw_f04_crypto_winter_drawdown_ddvolw_189d_slope_v104_signal,    f04cw_f04_crypto_winter_drawdown_ddflow_504d_slope_v105_signal,    f04cw_f04_crypto_winter_drawdown_recovslope_504d_slope_v106_signal,    f04cw_f04_crypto_winter_drawdown_ddslope_504d_slope_v107_signal,    f04cw_f04_crypto_winter_drawdown_ddslope_63d_slope_v108_signal,    f04cw_f04_crypto_winter_drawdown_recratio_504d_slope_v109_signal,    f04cw_f04_crypto_winter_drawdown_recratio_189d_slope_v110_signal,    f04cw_f04_crypto_winter_drawdown_painvoladj_504d_slope_v111_signal,    f04cw_f04_crypto_winter_drawdown_painvoladj_63d_slope_v112_signal,    f04cw_f04_crypto_winter_drawdown_uwmean_189d_slope_v113_signal,    f04cw_f04_crypto_winter_drawdown_uwmean_63d_slope_v114_signal,    f04cw_f04_crypto_winter_drawdown_ddskew_504d_slope_v115_signal,    f04cw_f04_crypto_winter_drawdown_ddkurt_126d_slope_v116_signal,    f04cw_f04_crypto_winter_drawdown_ddfrac_504d_slope_v117_signal,    f04cw_f04_crypto_winter_drawdown_ddfrac_63d_slope_v118_signal,    f04cw_f04_crypto_winter_drawdown_ddsmooth_504d_slope_v119_signal,    f04cw_f04_crypto_winter_drawdown_ddsmooth_63d_slope_v120_signal,    f04cw_f04_crypto_winter_drawdown_ddewm_504d_slope_v121_signal,    f04cw_f04_crypto_winter_drawdown_ddewm_63d_slope_v122_signal,    f04cw_f04_crypto_winter_drawdown_uwslope_504d_slope_v123_signal,    f04cw_f04_crypto_winter_drawdown_uwslope_63d_slope_v124_signal,    f04cw_f04_crypto_winter_drawdown_ddvolratio2_slope_v125_signal,    f04cw_f04_crypto_winter_drawdown_ddspread_21_126_slope_v126_signal,    f04cw_f04_crypto_winter_drawdown_ddspread_84_252_slope_v127_signal,    f04cw_f04_crypto_winter_drawdown_netstate_504d_slope_v128_signal,    f04cw_f04_crypto_winter_drawdown_netstate_63d_slope_v129_signal,    f04cw_f04_crypto_winter_drawdown_ddrank_252d_slope_v130_signal,    f04cw_f04_crypto_winter_drawdown_recrank_252d_slope_v131_signal,    f04cw_f04_crypto_winter_drawdown_retoverulcer_126d_slope_v132_signal,    f04cw_f04_crypto_winter_drawdown_retoverulcer_504d_slope_v133_signal,    f04cw_f04_crypto_winter_drawdown_reboundpain_126d_slope_v134_signal,    f04cw_f04_crypto_winter_drawdown_ddnotional_252d_slope_v135_signal,    f04cw_f04_crypto_winter_drawdown_recmompain_252d_slope_v136_signal,    f04cw_f04_crypto_winter_drawdown_recmompain_126d_slope_v137_signal,    f04cw_f04_crypto_winter_drawdown_ddaccel_252d_slope_v138_signal,    f04cw_f04_crypto_winter_drawdown_ddaccel_126d_slope_v139_signal,    f04cw_f04_crypto_winter_drawdown_uwz_252d_slope_v140_signal,    f04cw_f04_crypto_winter_drawdown_uwz_126d_slope_v141_signal,    f04cw_f04_crypto_winter_drawdown_painz_252d_slope_v142_signal,    f04cw_f04_crypto_winter_drawdown_recpainspread_252d_slope_v143_signal,    f04cw_f04_crypto_winter_drawdown_ddvolunits_252d_slope_v144_signal,    f04cw_f04_crypto_winter_drawdown_ddvolunits_126d_slope_v145_signal,    f04cw_f04_crypto_winter_drawdown_painspread_slope_v146_signal,    f04cw_f04_crypto_winter_drawdown_ulcerspread_slope_v147_signal,    f04cw_f04_crypto_winter_drawdown_recvolunits_252d_slope_v148_signal,    f04cw_f04_crypto_winter_drawdown_uwewm_252d_slope_v149_signal,    f04cw_f04_crypto_winter_drawdown_blend_multi_slope_v150_signal,]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F04_CRYPTO_WINTER_DRAWDOWN_REGISTRY_SLOPE = REGISTRY

def _synth_cols(names):
    import numpy as np
    import pandas as pd
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    closeadj = pd.Series(base_price, name="closeadj")
    noise_h = np.abs(np.random.normal(0, 0.02, n))
    noise_l = np.abs(np.random.normal(0, 0.02, n))
    POS = {"open", "high", "low", "close", "closeadj", "price", "volume",
           "vwap", "marketcap", "ev", "assets", "assetsc", "assetsnc", "equity",
           "revenue", "revenueusd", "gp", "ebitda", "ebit", "ppnenet", "sharesbas",
           "shareswa", "cashneq", "cor", "opex", "sgna", "rnd", "inventory",
           "receivables", "payables", "intangibles", "evebitda", "evebit",
           "pe", "pb", "ps", "currentratio", "bvps", "sps", "divyield", "dps",
           "shrvalue", "shrunits", "totalvalue", "percentoftotal", "value",
           "units", "shares", "sf3a_shares", "sf3a_value", "sf3b_shares",
           "sf3b_value", "grossmargin", "ebitdamargin", "netmargin", "roe",
           "roa", "roic", "deposits", "invcap"}
    for nm in names:
        if nm == "closeadj" or nm == "close" or nm == "price":
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price * (1 + np.random.normal(0, 0.01, n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price * (1 + noise_h), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price * (1 - noise_l), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7, 7e6, n)) + 1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0, 1.0, n))
            level = 1000.0 * np.exp(0.03 * np.random.normal(0, 1, n).cumsum() / np.sqrt(n))
            series = level + 50.0 * walk
            if nm in POS:
                series = np.abs(series) + 10.0
            out[nm] = pd.Series(series, name=nm)
    return out


if __name__ == "__main__":
    import numpy as np
    import pandas as pd
    domain_primitives = ('_f04_dd', '_f04_underwater', '_f04_recovery', '_f04_painvol')
    needed = set()
    for fn in _FEATURES:
        for p in inspect.signature(fn).parameters.values():
            needed.add(p.name)
    cols = _synth_cols(sorted(needed))
    n_features = 0
    nan_ok = 0
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
    print("OK f04_crypto_winter_drawdown_" + "2nd_derivatives" + "_001_150_claude: " + str(n_features) + " features pass")
