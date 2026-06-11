"""f25_vwap_deviation slope features 001-150 (1st derivative).
Each function computes its own VWAP-deviation base formula inline, then
returns base.diff(k) (or a normalized variant) and replace([inf,-inf],nan).
k follows the ROC bracket of the base's primary window:
<=5d:k=5;  6-21d:k=5 or 10;  22-63d:k=10 or 21;  64-200d:k=21 or 63;
>200d:k=63. NaN policy: only the final replace().
"""
from __future__ import annotations
import numpy as np
import pandas as pd

_HLCV = ["high", "low", "close", "volume"]
_HLAV = ["high", "low", "closeadj", "volume"]
_OHLAV = ["open", "high", "low", "closeadj", "volume"]

# Helpers

def _sma(s, n):
    return s.rolling(n, min_periods=n).mean()

def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=n).mean()

def _vwap(t, v, n):
    return (t * v).rolling(n, n).sum() / v.rolling(n, n).sum().replace(0.0, np.nan)

def _typ(h, l, c): return (h + l + c) / 3.0

_INF = [np.inf, -np.inf]



def _avwap_lo_hi(typ, vol, n):
    al = pd.Series(np.nan, index=typ.index, dtype=float)
    ah = pd.Series(np.nan, index=typ.index, dtype=float)
    tv = (typ * vol).values; vv = vol.values; tyv = typ.values
    for i in range(n - 1, len(typ)):
        s0 = i - n + 1; w = tyv[s0:i + 1]
        if not np.all(np.isfinite(w)): continue
        a_lo = s0 + int(np.argmin(w)); a_hi = s0 + int(np.argmax(w))
        dlo = float(np.nansum(vv[a_lo:i + 1])); dhi = float(np.nansum(vv[a_hi:i + 1]))
        if dlo != 0.0 and dhi != 0.0:
            al.iat[i] = float(np.nansum(tv[a_lo:i + 1])) / dlo
            ah.iat[i] = float(np.nansum(tv[a_hi:i + 1])) / dhi
    return al, ah

def _avwap_lo(typ, vol, n):
    avw = pd.Series(np.nan, index=typ.index, dtype=float)
    tv = (typ * vol).values; vv = vol.values; tyv = typ.values
    for i in range(n - 1, len(typ)):
        s0 = i - n + 1; w = tyv[s0:i + 1]
        if not np.all(np.isfinite(w)): continue
        a = s0 + int(np.argmin(w)); den = float(np.nansum(vv[a:i + 1]))
        if den != 0.0: avw.iat[i] = float(np.nansum(tv[a:i + 1])) / den
    return avw


def _avwap_hi(typ, vol, n):
    avw = pd.Series(np.nan, index=typ.index, dtype=float)
    tv = (typ * vol).values; vv = vol.values; tyv = typ.values
    for i in range(n - 1, len(typ)):
        s0 = i - n + 1; w = tyv[s0:i + 1]
        if not np.all(np.isfinite(w)): continue
        a = s0 + int(np.argmax(w)); den = float(np.nansum(vv[a:i + 1]))
        if den != 0.0: avw.iat[i] = float(np.nansum(tv[a:i + 1])) / den
    return avw

def _atr(h, l, c, n):
    pc = c.shift(1); tr = pd.concat([(h - l), (h - pc).abs(), (l - pc).abs()], axis=1).max(axis=1)
    return tr.ewm(alpha=1.0/float(n), adjust=False, min_periods=n).mean()

# Features 001-150 (slopes)

def f25vw_f25_vwap_deviation_logclose_vwap_8d_slope_v001_signal(high, low, close, volume):
    typ = _typ(high, low, close); vwap = _vwap(typ, volume, 8)
    return np.log(close / vwap).diff(5).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_logclose_vwap_63d_slope_v002_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 63)
    return np.log(closeadj / vwap).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_logclose_vwap_200d_slope_v003_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 200)
    return np.log(closeadj / vwap).diff(63).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap5_vwap21_diff_slope_v004_signal(high, low, close, volume):
    typ = _typ(high, low, close)
    v1 = _vwap(typ, volume, 5)
    v2 = _vwap(typ, volume, 21)
    return np.log(v1 / v2).diff(5).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap21_vwap252_diff_slope_v005_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj)
    v1 = _vwap(typ, volume, 21)
    v2 = _vwap(typ, volume, 252)
    return np.log(v1 / v2).diff(63).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap10_vwap40_diff_slope_v006_signal(high, low, close, volume):
    typ = _typ(high, low, close)
    v1 = _vwap(typ, volume, 10)
    v2 = _vwap(typ, volume, 40)
    return np.log(v1 / v2).diff(10).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_sign_close_vwap_15d_slope_v007_signal(high, low, close, volume):
    typ = _typ(high, low, close); vwap = _vwap(typ, volume, 15)
    return np.sign(close - vwap).diff(5).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_sign_close_vwap_45d_slope_v008_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 45)
    return np.sign(closeadj - vwap).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_sign_close_vwap_120d_slope_v009_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 120)
    return np.sign(closeadj - vwap).diff(63).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_sign_vwap_shift_30_60d_slope_v010_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 30)
    return np.sign(vwap - vwap.shift(60)).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_sign_vwap10_vwap50_slope_v011_signal(high, low, close, volume):
    typ = _typ(high, low, close)
    v1 = _vwap(typ, volume, 10)
    v2 = _vwap(typ, volume, 50)
    return np.sign(v1 - v2).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_zscore_close_vwap_30d_slope_v012_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 30)
    dev = closeadj - vwap
    mu = dev.rolling(60, 60).mean()
    sd = dev.rolling(60, 60).std().replace(0.0, np.nan)
    return ((dev - mu) / sd).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_zscore_close_vwap_90d_slope_v013_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 90)
    dev = closeadj - vwap
    mu = dev.rolling(90, 90).mean()
    sd = dev.rolling(90, 90).std().replace(0.0, np.nan)
    return ((dev - mu) / sd).diff(63).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_logclose_avwap_low_30d_slope_v014_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj)
    avw = _avwap_lo(typ, volume, 30)
    return np.log(closeadj / avw).diff(10).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_logclose_avwap_high_30d_slope_v015_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj)
    avw = _avwap_hi(typ, volume, 30)
    return np.log(closeadj / avw).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_logclose_avwap_low_90d_slope_v016_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj)
    avw = _avwap_lo(typ, volume, 90)
    return np.log(closeadj / avw).diff(63).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_sign_avwap_low_high_60d_slope_v017_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj)
    al, ah = _avwap_lo_hi(typ, volume, 60)
    return np.sign(al - ah).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_avwap_convergence_45d_slope_v018_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj)
    al, ah = _avwap_lo_hi(typ, volume, 45)
    vwap = _vwap(typ, volume, 45)
    return ((al - ah).abs() / vwap).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_slope_20d_slope_v019_signal(high, low, close, volume):
    typ = _typ(high, low, close); vwap = _vwap(typ, volume, 20)
    return (vwap.diff(10) / vwap).diff(10).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_slope_100d_slope_v020_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 100)
    return (vwap.diff(21) / vwap).diff(63).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_curvature_50d_slope_v021_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 50)
    return ((vwap - 2.0 * vwap.shift(10) + vwap.shift(20)) / vwap).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_sign_vwap_slope_25d_slope_v022_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 25)
    return np.sign(vwap.diff(10)).diff(10).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_streak_above_vwap_30d_slope_v023_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 30)
    cond = (closeadj > vwap).astype(float).where(~vwap.isna())
    out = pd.Series(np.nan, index=cond.index, dtype=float)
    run = 0; started = False
    for i in range(len(cond)):
        v = cond.iat[i]
        if not np.isfinite(v):
            run = 0; continue
        started = True
        run = run + 1 if v > 0.5 else 0
        if started: out.iat[i] = float(run)
    return out.diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_streak_below_vwap_75d_slope_v024_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 75)
    cond = (closeadj < vwap).astype(float).where(~vwap.isna())
    out = pd.Series(np.nan, index=cond.index, dtype=float)
    run = 0; started = False
    for i in range(len(cond)):
        v = cond.iat[i]
        if not np.isfinite(v):
            run = 0; continue
        started = True
        run = run + 1 if v > 0.5 else 0
        if started: out.iat[i] = float(run)
    return out.diff(63).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_dayssince_vwap_cross_40d_slope_v025_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 40)
    sgn = np.sign(closeadj - vwap)
    out = pd.Series(np.nan, index=sgn.index, dtype=float)
    last = None; prev = np.nan
    for i in range(len(sgn)):
        v = sgn.iat[i]
        if not np.isfinite(v): continue
        if not np.isfinite(prev):
            prev = v; last = i; out.iat[i] = 0.0; continue
        if v != prev: last = i
        prev = v; out.iat[i] = float(i - last)
    return out.diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_dayssince_vwap_xover_30_90d_slope_v026_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj)
    v1 = _vwap(typ, volume, 30)
    v2 = _vwap(typ, volume, 90)
    sgn = np.sign(v1 - v2)
    out = pd.Series(np.nan, index=sgn.index, dtype=float)
    last = None; prev = np.nan
    for i in range(len(sgn)):
        v = sgn.iat[i]
        if not np.isfinite(v): continue
        if not np.isfinite(prev):
            prev = v; last = i; out.iat[i] = 0.0; continue
        if v != prev: last = i
        prev = v; out.iat[i] = float(i - last)
    return out.diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_band_position_20d_slope_v027_signal(high, low, close, volume):
    typ = _typ(high, low, close); vwap = _vwap(typ, volume, 20)
    sigma = (typ - vwap).rolling(20, 20).std().replace(0.0, np.nan)
    return ((close - (vwap - sigma)) / (2.0 * sigma)).diff(5).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_band_position_60d_slope_v028_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 60)
    sigma = (typ - vwap).rolling(60, 60).std().replace(0.0, np.nan)
    return ((closeadj - (vwap - 2.0 * sigma)) / (4.0 * sigma)).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_outside_vwap_2sigma_30d_slope_v029_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 30)
    dev = closeadj - vwap
    sigma = (typ - vwap).rolling(30, 30).std()
    above = (dev > 2.0 * sigma).astype(float)
    below = (dev < -2.0 * sigma).astype(float)
    return (above - below).where(~sigma.isna()).diff(10).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_days_outside_vwap_band_60d_slope_v030_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 60)
    sigma = (typ - vwap).rolling(60, 60).std()
    outside = ((closeadj - vwap).abs() > sigma).astype(float).where(~sigma.isna())
    return outside.rolling(60, 60).sum().diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_residual_atr_25d_slope_v031_signal(high, low, close, volume):
    typ = _typ(high, low, close); vwap = _vwap(typ, volume, 25)
    atr = _atr(high, low, close, 25).replace(0.0, np.nan)
    return ((close - vwap) / atr).diff(10).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_resid_skew_75d_slope_v032_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 75)
    return (closeadj - vwap).rolling(75, 75).skew().diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_gap_rank_50d_slope_v033_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 50)
    return (closeadj - vwap).rolling(50, 50).rank(pct=True).diff(10).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_gap_rank_120d_slope_v034_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 120)
    return (closeadj - vwap).rolling(120, 120).rank(pct=True).diff(63).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_twap_diff_20d_slope_v035_signal(high, low, close, volume):
    typ = _typ(high, low, close); vwap = _vwap(typ, volume, 20)
    twap = typ.rolling(20, 20).mean()
    return np.log(vwap / twap).diff(5).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_twap_diff_80d_slope_v036_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 80)
    twap = typ.rolling(80, 80).mean()
    return np.log(vwap / twap).diff(63).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_sign_vwap_twap_45d_slope_v037_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 45)
    twap = typ.rolling(45, 45).mean()
    return np.sign(vwap - twap).diff(10).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_smoothed_vwap_diff_30d_slope_v038_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 30)
    sm = vwap.rolling(30, 30).mean()
    return np.log(vwap / sm).diff(10).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_ema_vwap_diff_60d_slope_v039_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 60)
    sm = vwap.ewm(span=30, adjust=False, min_periods=30).mean()
    return np.log(vwap / sm).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_max_min_resid_ratio_50d_slope_v040_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 50)
    dev = closeadj - vwap
    mx = dev.rolling(50, 50).max()
    mn = dev.rolling(50, 50).min().abs().replace(0.0, np.nan)
    return (mx / mn).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_net_direction_vwap_30d_slope_v041_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 30)
    sgn = np.sign(closeadj - vwap)
    return (sgn.rolling(30, 30).sum() / 30.0).diff(10).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_arctan_vwap_resid_120d_slope_v042_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 120)
    sigma = (typ - vwap).rolling(120, 120).std().replace(0.0, np.nan)
    return np.arctan((closeadj - vwap) / sigma).diff(63).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_tanh_vwap_zscore_70d_slope_v043_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 70)
    dev = closeadj - vwap
    mu = dev.rolling(70, 70).mean()
    sd = dev.rolling(70, 70).std().replace(0.0, np.nan)
    return np.tanh((dev - mu) / sd).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_sigmoid_vwap_resid_atr_40d_slope_v044_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 40)
    atr = _atr(high, low, closeadj, 40).replace(0.0, np.nan)
    x = (closeadj - vwap) / atr
    return (1.0 / (1.0 + np.exp(-x)) - 0.5).diff(10).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_regime_strong_bull_40d_slope_v045_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 40)
    sigma = (typ - vwap).rolling(40, 40).std().replace(0.0, np.nan)
    cond1 = (closeadj > (vwap + sigma)).astype(float)
    cond2 = (vwap.diff(10) > 0).astype(float)
    return (cond1 * cond2).where(~sigma.isna() & ~vwap.diff(10).isna()).diff(10).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_regime_strong_bear_50d_slope_v046_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 50)
    sigma = (typ - vwap).rolling(50, 50).std().replace(0.0, np.nan)
    cond1 = (closeadj < (vwap - sigma)).astype(float)
    cond2 = (vwap.diff(10) < 0).astype(float)
    return (cond1 * cond2).where(~sigma.isna() & ~vwap.diff(10).isna()).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_band_kurt_60d_slope_v047_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 60)
    return (closeadj - vwap).rolling(60, 60).kurt().diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_high_vs_vwap_15d_slope_v048_signal(high, low, close, volume):
    typ = _typ(high, low, close); vwap = _vwap(typ, volume, 15)
    return np.log(high / vwap).diff(5).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_hl_minus_vwap_15d_slope_v049_signal(high, low, close, volume):
    typ = _typ(high, low, close); vwap = _vwap(typ, volume, 15)
    mid = 0.5 * (high + low)
    rng = (high - low).replace(0.0, np.nan)
    return ((mid - vwap) / rng).diff(10).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_open_close_vs_vwap_55d_slope_v050_signal(open_, high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 55)
    dev = (closeadj - vwap).abs().replace(0.0, np.nan)
    return ((closeadj - open_) / dev).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_slope_flip_freq_60d_slope_v051_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 35)
    sgn = np.sign(vwap.diff(10))
    flip = (sgn != sgn.shift(1)).astype(float).where(~sgn.isna() & ~sgn.shift(1).isna())
    return flip.rolling(60, 60).sum().diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_xover_freq_120d_slope_v052_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 20)
    sgn = np.sign(closeadj - vwap)
    flip = (sgn != sgn.shift(1)).astype(float).where(~sgn.isna() & ~sgn.shift(1).isna())
    return flip.rolling(120, 120).sum().diff(63).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_corr_close_vwap_45d_slope_v053_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 30)
    return closeadj.rolling(45, 45).corr(vwap).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_corr_close_vwap_lag10_80d_slope_v054_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 40)
    return closeadj.rolling(80, 80).corr(vwap.shift(10)).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_avwap_low_slope_40d_slope_v055_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj)
    avw = _avwap_lo(typ, volume, 40)
    return np.log(avw).diff(10).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_avwap_high_streak_150d_slope_v056_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj)
    avw = _avwap_hi(typ, volume, 150)
    cond = (closeadj > avw).astype(float).where(~avw.isna())
    out = pd.Series(np.nan, index=cond.index, dtype=float)
    run = 0; started = False
    for i in range(len(cond)):
        v = cond.iat[i]
        if not np.isfinite(v):
            run = 0; continue
        started = True
        run = run + 1 if v > 0.5 else 0
        if started: out.iat[i] = float(run)
    return out.diff(63).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_sigma_norm_35d_slope_v057_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 35)
    sigma = (typ - vwap).rolling(35, 35).std()
    return (sigma / vwap).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_sigma_ratio_30_90d_slope_v058_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj)
    v1 = _vwap(typ, volume, 30)
    v2 = _vwap(typ, volume, 90)
    s1 = (typ - v1).rolling(30, 30).std()
    s2 = (typ - v2).rolling(90, 90).std().replace(0.0, np.nan)
    return (s1 / s2).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_resid_slope_45d_slope_v059_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 45)
    return ((closeadj - vwap).diff(10) / vwap).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_avwap_high_resid_slope_45d_slope_v060_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj)
    avw = _avwap_hi(typ, volume, 45)
    return np.log(closeadj / avw).diff(10).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_above_band_count_45d_slope_v061_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 45)
    sigma = (typ - vwap).rolling(45, 45).std().replace(0.0, np.nan)
    above = (closeadj > (vwap + sigma)).astype(float).where(~sigma.isna())
    return above.rolling(45, 45).sum().diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_below_band_count_90d_slope_v062_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 90)
    sigma = (typ - vwap).rolling(90, 90).std().replace(0.0, np.nan)
    below = (closeadj < (vwap - sigma)).astype(float).where(~sigma.isna())
    return below.rolling(90, 90).sum().diff(63).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_avwap_low_age_norm_60d_slope_v063_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj)
    out = pd.Series(np.nan, index=typ.index, dtype=float)
    tyv = typ.values
    n = 60
    for i in range(n - 1, len(typ)):
        s0 = i - n + 1; w = tyv[s0:i + 1]
        if not np.all(np.isfinite(w)): continue
        out.iat[i] = float(n - 1 - int(np.argmin(w))) / float(n)
    return out.diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_dist_avwap_high_pct_60d_slope_v064_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj)
    avw = _avwap_hi(typ, volume, 60)
    return ((closeadj - avw) / closeadj).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_rank_vwap_50d_slope_v065_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 20)
    return vwap.rolling(50, 50).rank(pct=True).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_rank_vwap_slope_100d_slope_v066_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 40)
    return vwap.diff(21).rolling(100, 100).rank(pct=True).diff(63).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_sign_close_above_both_30d_slope_v067_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 30)
    twap = typ.rolling(30, 30).mean()
    return ((closeadj > vwap).astype(float) + (closeadj > twap).astype(float) - 1.0).where(~vwap.isna() & ~twap.isna()).diff(10).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_resid_autocorr_lag5_60d_slope_v068_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 30)
    dev = closeadj - vwap
    return dev.rolling(60, 60).corr(dev.shift(5)).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_resid_autocorr_lag21_120d_slope_v069_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 80)
    dev = closeadj - vwap
    return dev.rolling(120, 120).corr(dev.shift(21)).diff(63).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_curv_norm_100d_slope_v070_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 100)
    return ((vwap - 2.0 * vwap.shift(21) + vwap.shift(42)) / vwap).diff(63).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_high_above_vwap_band_22d_slope_v071_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 22)
    sigma = (typ - vwap).rolling(22, 22).std().replace(0.0, np.nan)
    above = ((high - vwap) > 2.0 * sigma).astype(float)
    below = ((low - vwap) < -2.0 * sigma).astype(float)
    return (above - below).where(~sigma.isna()).diff(10).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_lag_corr_80d_slope_v072_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 20)
    return vwap.rolling(80, 80).corr(vwap.shift(40)).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_slope_spread_15_60d_slope_v073_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj)
    v1 = _vwap(typ, volume, 15)
    v2 = _vwap(typ, volume, 60)
    return ((v1.diff(5) / v1) - (v2.diff(21) / v2)).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_majority_above_vwap_55d_slope_v074_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj)
    sigs = []; mask = pd.Series(True, index=typ.index)
    for n in (20, 40, 60, 80, 100):
        vwap = _vwap(typ, volume, n); sigs.append(np.sign(closeadj - vwap))
        mask = mask & ~vwap.isna()
    total = pd.concat(sigs, axis=1).sum(axis=1)
    return (total.where(mask).rolling(55, 55).sum() / (5.0 * 55.0)).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_diff_std_70d_slope_v075_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 50)
    return (vwap.diff(1).rolling(70, 70).std() / vwap).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_diff_4_12d_slope_v076_signal(high, low, close, volume):
    typ = _typ(high, low, close)
    v1 = _vwap(typ, volume, 4)
    v2 = _vwap(typ, volume, 12)
    return np.log(v1 / v2).diff(5).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_diff_30_180d_slope_v077_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj)
    v1 = _vwap(typ, volume, 30)
    v2 = _vwap(typ, volume, 180)
    return np.log(v1 / v2).diff(63).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_resid_mad_40d_slope_v078_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 40)
    dev = closeadj - vwap
    med = dev.rolling(40, 40).median()
    mad = (dev - med).abs().rolling(40, 40).median()
    return (mad / vwap).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_resid_iqr_75d_slope_v079_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 75)
    dev = closeadj - vwap
    q1 = dev.rolling(75, 75).quantile(0.25)
    q3 = dev.rolling(75, 75).quantile(0.75)
    return ((q3 - q1) / vwap).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_resid_median_norm_60d_slope_v080_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 60)
    dev = closeadj - vwap
    return (dev.rolling(60, 60).median() / vwap).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_resid_qrank_30d_slope_v081_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 30)
    dev = closeadj - vwap
    return (dev.rolling(30, 30).rank(pct=True) - 0.5).diff(10).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_resid_qrank_180d_slope_v082_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 150)
    dev = closeadj - vwap
    return (dev.rolling(180, 180).rank(pct=True) - 0.5).diff(63).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_ema_diff_15d_slope_v083_signal(high, low, close, volume):
    typ = _typ(high, low, close); vwap = _vwap(typ, volume, 15)
    ema = close.ewm(span=15, adjust=False, min_periods=15).mean()
    return np.log(vwap / ema).diff(5).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_ema_diff_100d_slope_v084_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 100)
    ema = closeadj.ewm(span=100, adjust=False, min_periods=100).mean()
    return np.log(vwap / ema).diff(63).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_corr_vwap_slopes_60d_slope_v085_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj)
    v1 = _vwap(typ, volume, 20)
    v2 = _vwap(typ, volume, 60)
    return v1.diff(5).rolling(60, 60).corr(v2.diff(21)).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_dayssince_vwap_slope_flip_50d_slope_v086_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 50)
    sgn = np.sign(vwap.diff(10))
    out = pd.Series(np.nan, index=sgn.index, dtype=float)
    last = None; prev = np.nan
    for i in range(len(sgn)):
        v = sgn.iat[i]
        if not np.isfinite(v): continue
        if not np.isfinite(prev):
            prev = v; last = i; out.iat[i] = 0.0; continue
        if v != prev: last = i
        prev = v; out.iat[i] = float(i - last)
    return out.diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_dayssince_vwap_band_break_50d_slope_v087_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 50)
    sigma = (typ - vwap).rolling(50, 50).std().replace(0.0, np.nan)
    dev = closeadj - vwap
    is_outside = (dev.abs() > 2.0 * sigma).astype(float).where(~sigma.isna())
    out = pd.Series(np.nan, index=is_outside.index, dtype=float)
    last = None
    for i in range(len(is_outside)):
        v = is_outside.iat[i]
        if not np.isfinite(v): continue
        if v > 0.5: last = i
        out.iat[i] = float(i - last) if last is not None else float(i)
    return out.diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_range_30d_slope_v088_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 15)
    mx = vwap.rolling(30, 30).max(); mn = vwap.rolling(30, 30).min()
    return ((mx - mn) / vwap).diff(10).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_range_120d_slope_v089_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 40)
    mx = vwap.rolling(120, 120).max(); mn = vwap.rolling(120, 120).min()
    return ((mx - mn) / vwap).diff(63).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_close_pos_vs_vwap_range_50d_slope_v090_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 20)
    mx = vwap.rolling(50, 50).max(); mn = vwap.rolling(50, 50).min()
    rng = (mx - mn).replace(0.0, np.nan)
    return ((closeadj - mn) / rng - 0.5).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_signed_dev_sum_45d_slope_v091_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 45)
    dev = closeadj - vwap
    s = dev.rolling(45, 45).sum()
    a = dev.abs().rolling(45, 45).sum().replace(0.0, np.nan)
    return (s / a).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_avwap_high_age_norm_90d_slope_v092_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj)
    out = pd.Series(np.nan, index=typ.index, dtype=float)
    tyv = typ.values
    n = 90
    for i in range(n - 1, len(typ)):
        s0 = i - n + 1; w = tyv[s0:i + 1]
        if not np.all(np.isfinite(w)): continue
        out.iat[i] = float(n - 1 - int(np.argmax(w))) / float(n)
    return out.diff(63).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_resid_above_frac_55d_slope_v093_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 45)
    above = (closeadj > vwap).astype(float).where(~vwap.isna())
    return above.rolling(55, 55).mean().diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_max_run_above_vwap_60d_slope_v094_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 35)
    above = (closeadj > vwap).astype(float).where(~vwap.isna()).values
    out = pd.Series(np.nan, index=closeadj.index, dtype=float)
    n = 60
    for i in range(len(closeadj)):
        if i < n - 1: continue
        window = above[i - n + 1:i + 1]
        if np.any(~np.isfinite(window)): continue
        run = 0; mx = 0
        for v in window:
            if v > 0.5:
                run += 1
                if run > mx: mx = run
            else:
                run = 0
        out.iat[i] = float(mx)
    return out.diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_xover_short_45d_slope_v095_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 35)
    sgn = np.sign(closeadj - vwap)
    flip = (sgn != sgn.shift(1)).astype(float).where(~sgn.isna() & ~sgn.shift(1).isna())
    return flip.rolling(45, 45).sum().diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_sign_concord_short_long_30d_slope_v096_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj)
    v1 = _vwap(typ, volume, 10)
    v2 = _vwap(typ, volume, 60)
    return (np.sign(closeadj - v1) * np.sign(closeadj - v2)).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_sign_dev_slope_xor_50d_slope_v097_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 50)
    return (np.sign(closeadj - vwap) - np.sign(vwap.diff(10))).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_jerk_proxy_35d_slope_v098_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 35)
    slope = vwap.diff(5)
    return ((slope - slope.shift(5)) / vwap).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_high_minus_vwap_norm_50d_slope_v099_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 50)
    sigma = (typ - vwap).rolling(50, 50).std().replace(0.0, np.nan)
    raw = (high - vwap) / sigma
    norm = raw.abs().rolling(10, 10).mean().replace(0.0, np.nan)
    return (raw.diff(10) / norm).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_hl_range_vs_vwap_band_50d_slope_v100_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 50)
    sigma = (typ - vwap).rolling(50, 50).std().replace(0.0, np.nan)
    return ((high - low) / sigma).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_post_cross_return_30d_slope_v101_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 20)
    sgn = np.sign(closeadj - vwap); ret = closeadj.pct_change()
    return (sgn.shift(1) * ret).rolling(30, 30).mean().diff(10).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_gap_volnorm_25d_slope_v102_signal(high, low, close, volume):
    typ = _typ(high, low, close); vwap = _vwap(typ, volume, 25)
    vm = volume.rolling(25, 25).mean().replace(0.0, np.nan)
    return ((close - vwap) / vwap * (volume / vm)).diff(10).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_signed_vol_25d_slope_v103_signal(high, low, close, volume):
    typ = _typ(high, low, close); vwap = _vwap(typ, volume, 25)
    sgn = np.sign(close - vwap)
    sv = (sgn * volume).rolling(25, 25).sum()
    tot = volume.rolling(25, 25).sum().replace(0.0, np.nan)
    return (sv / tot).diff(10).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_avwap_channel_pos_75d_slope_v104_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj)
    al, ah = _avwap_lo_hi(typ, volume, 75)
    return ((closeadj - al) / (ah - al) - 0.5).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_band_width_diff_45d_slope_v105_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj)
    v1 = _vwap(typ, volume, 45)
    v2 = _vwap(typ, volume, 150)
    s1 = (typ - v1).rolling(45, 45).std()
    s2 = (typ - v2).rolling(150, 150).std()
    return ((s1 / v1) - (s2 / v2)).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_resid_when_up_60d_slope_v106_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 30)
    slope = vwap.diff(10)
    dev = (closeadj - vwap) / vwap
    masked = dev.where(slope > 0)
    return masked.rolling(60, min_periods=20).mean().diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_resid_ar1_60d_slope_v107_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 45)
    dev = closeadj - vwap
    lag1 = dev.shift(1)
    cov = dev.rolling(60, 60).cov(lag1)
    var = lag1.rolling(60, 60).var().replace(0.0, np.nan)
    return (cov / var).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_sign_change_density_120d_slope_v108_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 40)
    sgn = np.sign(closeadj - vwap)
    flip = (sgn != sgn.shift(1)).astype(float).where(~sgn.isna() & ~sgn.shift(1).isna())
    return flip.rolling(120, 120).mean().diff(63).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_dist_avwap_low_vs_high_60d_slope_v109_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj)
    al, ah = _avwap_lo_hi(typ, volume, 60)
    return ((closeadj - al).abs() / (closeadj - ah).abs().replace(0.0, np.nan)).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_beta_close_vwap_45d_slope_v110_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 20)
    rc = closeadj.diff(1); rv = vwap.diff(1)
    cov = rc.rolling(45, 45).cov(rv)
    var = rv.rolling(45, 45).var().replace(0.0, np.nan)
    return (cov / var).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_trend_strength_60d_slope_v111_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 60)
    sigma = (typ - vwap).rolling(60, 60).std().replace(0.0, np.nan)
    return (vwap.diff(21) / sigma).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_max_abs_dev_30d_slope_v112_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 30)
    dev = (closeadj - vwap).abs()
    return (dev.rolling(30, 30).max() / vwap).diff(10).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_resid_mad_z_70d_slope_v113_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 70)
    dev = closeadj - vwap
    med = dev.rolling(70, 70).median()
    mad = (dev - med).abs().rolling(70, 70).median().replace(0.0, np.nan)
    return ((dev - med) / mad).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_slope_z_70d_slope_v114_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 40)
    slope = vwap.diff(21)
    mu = slope.rolling(70, 70).mean()
    sd = slope.rolling(70, 70).std().replace(0.0, np.nan)
    return ((slope - mu) / sd).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_close_slope_agree_50d_slope_v115_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 50)
    return (np.sign(vwap.diff(21)) * np.sign(closeadj.diff(21))).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_band_pos_rolling_zscore_35d_slope_v116_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 35)
    sigma = (typ - vwap).rolling(35, 35).std().replace(0.0, np.nan)
    pos = (closeadj - vwap) / sigma
    mu = pos.rolling(120, 120).mean()
    sd = pos.rolling(120, 120).std().replace(0.0, np.nan)
    return ((pos - mu) / sd).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_avwap_low_resid_z_60d_slope_v117_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj)
    avw = _avwap_lo(typ, volume, 60)
    r = np.log(closeadj / avw)
    mu = r.rolling(60, 60).mean()
    sd = r.rolling(60, 60).std().replace(0.0, np.nan)
    return ((r - mu) / sd).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_avwap_high_curv_55d_slope_v118_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj)
    avw = _avwap_hi(typ, volume, 55)
    return ((avw - 2.0 * avw.shift(10) + avw.shift(20)) / avw).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_avg_above_kvwap_50d_slope_v119_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj)
    sigs = []
    for n in (15, 30, 60, 120):
        vwap = (typ * volume).rolling(n, min_periods=n).sum() / volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
        sigs.append((closeadj > vwap).astype(float).where(~vwap.isna()))
    return pd.concat(sigs, axis=1).mean(axis=1).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_resid_skew_100d_slope_v120_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 35)
    return (closeadj - vwap).rolling(100, 100).skew().diff(63).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_multi_vwap_dispersion_45d_slope_v121_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj)
    series = []
    for n in (15, 30, 60, 90, 120):
        v = (typ * volume).rolling(n, min_periods=n).sum() / volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
        series.append(v)
    mat = pd.concat(series, axis=1)
    return (mat.std(axis=1) / mat.mean(axis=1)).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_multi_vwap_descord_count_slope_v122_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj)
    series = []
    for n in (8, 16, 32, 64, 128):
        v = (typ * volume).rolling(n, min_periods=n).sum() / volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
        series.append(v)
    cnt = pd.Series(0.0, index=typ.index)
    mask = ~series[0].isna()
    for i in range(len(series)):
        for j in range(i + 1, len(series)):
            cnt = cnt + (series[i] < series[j]).astype(float)
            mask = mask & ~series[i].isna() & ~series[j].isna()
    return cnt.where(mask).diff(63).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_reversion_rate_vwap_40d_slope_v123_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 40)
    dev = closeadj - vwap
    sigma = dev.rolling(40, 40).std().replace(0.0, np.nan)
    react = (-np.sign(dev.shift(1)) * dev.diff(1)) / sigma
    return react.rolling(40, 40).mean().diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_resid_rs_70d_slope_v124_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 30)
    dev = closeadj - vwap

    def _rs(x):
        if not np.all(np.isfinite(x)): return np.nan
        m = x.mean(); z = np.cumsum(x - m)
        r = z.max() - z.min(); s = x.std(ddof=0)
        if s == 0 or not np.isfinite(r / s) or r / s <= 0: return np.nan
        return float(np.log(r / s) / np.log(len(x)))

    return dev.rolling(70, 70).apply(_rs, raw=True).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_resid_var_ratio_60d_slope_v125_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 35)
    dev = closeadj - vwap
    v5 = dev.diff(5).rolling(60, 60).var()
    v1 = dev.diff(1).rolling(60, 60).var().replace(0.0, np.nan)
    return (v5 / (5.0 * v1)).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_resid_autocorr_ratio_80d_slope_v126_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 40)
    dev = closeadj - vwap
    a5 = dev.rolling(80, 80).corr(dev.shift(5))
    a21 = dev.rolling(80, 80).corr(dev.shift(21))
    return (a5 - a21).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_sign_resid_skew_50d_slope_v127_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 50)
    return np.sign((closeadj - vwap).rolling(50, 50).skew()).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_mean_abs_resid_norm_25d_slope_v128_signal(high, low, close, volume):
    typ = _typ(high, low, close); vwap = _vwap(typ, volume, 25)
    return ((close - vwap).abs().rolling(25, 25).mean() / vwap).diff(10).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_high_vs_vwap_rank_60d_slope_v129_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 60)
    return (high - vwap).rolling(60, 60).rank(pct=True).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_hl_vwap_rank_diff_60d_slope_v130_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 60)
    rh = (high - vwap).rolling(60, 60).rank(pct=True)
    rl = (low - vwap).rolling(60, 60).rank(pct=True)
    return (rh - rl).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_side_prob_80d_slope_v131_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 25)
    s = np.sign(closeadj - vwap)
    return (s * s.shift(1)).rolling(80, 80).mean().diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_resid_kurt_120d_slope_v132_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 25)
    return (closeadj - vwap).rolling(120, 120).kurt().diff(63).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_composite_state_50d_slope_v133_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 50)
    return (np.sign(closeadj - vwap) + 0.5 * np.sign(vwap.diff(10))).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_resid_time_rsq_40d_slope_v134_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 40)
    dev = closeadj - vwap

    def _r2(x):
        if not np.all(np.isfinite(x)): return np.nan
        t = np.arange(len(x), dtype=float)
        tm = t.mean(); xm = x.mean()
        cov = np.mean((t - tm) * (x - xm))
        vt = np.mean((t - tm) ** 2); vx = np.mean((x - xm) ** 2)
        if vt == 0 or vx == 0: return np.nan
        return float(cov ** 2 / (vt * vx))

    return dev.rolling(40, 40).apply(_r2, raw=True).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_convergence_rate_60d_slope_v135_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj)
    v1 = _vwap(typ, volume, 20)
    v2 = _vwap(typ, volume, 60)
    return (v1 - v2).abs().diff(21).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_dayssince_above_vwap_band_60d_slope_v136_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 50)
    sigma = (typ - vwap).rolling(50, 50).std().replace(0.0, np.nan)
    cond = (closeadj > (vwap + sigma)).astype(float).where(~sigma.isna())
    out = pd.Series(np.nan, index=cond.index, dtype=float)
    last = None
    for i in range(len(cond)):
        v = cond.iat[i]
        if not np.isfinite(v): continue
        if v > 0.5: last = i
        out.iat[i] = float(i - last) if last is not None else float(i)
    return out.diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_resid_efficiency_50d_slope_v137_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 35)
    dev = closeadj - vwap
    direction = (dev - dev.shift(50)).abs()
    pathlen = dev.diff(1).abs().rolling(50, 50).sum().replace(0.0, np.nan)
    return (direction / pathlen).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_dev_quantile_spread_60d_slope_v138_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 45)
    dev = closeadj - vwap
    q90 = dev.rolling(60, 60).quantile(0.9)
    q10 = dev.rolling(60, 60).quantile(0.1)
    return ((q90 - q10) / vwap).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_band_xover_count_90d_slope_v139_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 40)
    sigma = (typ - vwap).rolling(40, 40).std().replace(0.0, np.nan)
    state = ((closeadj > vwap + sigma).astype(float) - (closeadj < vwap - sigma).astype(float)).where(~sigma.isna())
    change = (state != state.shift(1)).astype(float).where(~state.isna() & ~state.shift(1).isna())
    return change.rolling(90, 90).sum().diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_dir_persistence_45d_slope_v140_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 30)
    d = np.sign(vwap.diff(1))
    return (d * d.shift(1)).rolling(45, 45).mean().diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_logclose_vwap_3d_slope_v141_signal(high, low, close, volume):
    typ = _typ(high, low, close); vwap = _vwap(typ, volume, 3)
    return np.log(close / vwap).diff(5).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_resid_vol_corr_60d_slope_v142_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 30)
    dev = closeadj - vwap
    return dev.rolling(60, 60).corr(volume).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_band_width_atr_ratio_40d_slope_v143_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 40)
    sigma = (typ - vwap).rolling(40, 40).std()
    atr = _atr(high, low, closeadj, 40).replace(0.0, np.nan)
    return (sigma / atr).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_intraday_range_vs_vwap_sigma_30d_slope_v144_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 30)
    sigma = (typ - vwap).rolling(30, 30).std().replace(0.0, np.nan)
    rng = (high - low).rolling(30, 30).mean()
    return (rng / sigma).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_dominant_side_strength_90d_slope_v145_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 50)
    above = (closeadj > vwap).astype(float).where(~vwap.isna()).rolling(90, 90).mean()
    return (2.0 * above - 1.0).abs().diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_up_day_ratio_70d_slope_v146_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 25)
    up = (vwap.diff(1) > 0).astype(float).where(~vwap.diff(1).isna())
    return up.rolling(70, 70).mean().diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_vwap_lead_corr_55d_slope_v147_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 30)
    return vwap.diff(5).rolling(55, 55).corr(closeadj.diff(5).shift(-5)).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_resid_tail_count_45d_slope_v148_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 45)
    sigma = (typ - vwap).rolling(45, 45).std().replace(0.0, np.nan)
    dev = closeadj - vwap
    tail = (dev.abs() > 1.5 * sigma).astype(float).where(~sigma.isna())
    return tail.rolling(45, 45).sum().diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_resid_halflife_proxy_50d_slope_v149_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 40)
    dev = closeadj - vwap
    lag1 = dev.shift(1)
    cov = dev.rolling(50, 50).cov(lag1)
    var = lag1.rolling(50, 50).var().replace(0.0, np.nan)
    ar1 = (cov / var).clip(-0.999, 0.999).abs().replace(0.0, np.nan)
    return (-np.log(2.0) / np.log(ar1)).diff(21).replace(_INF, np.nan)

def f25vw_f25_vwap_deviation_resid_sign_volsum_50d_slope_v150_signal(high, low, closeadj, volume):
    typ = _typ(high, low, closeadj); vwap = _vwap(typ, volume, 25)
    sgn = np.sign(closeadj - vwap)
    sv = (sgn * volume).rolling(50, 50).sum()
    tv = volume.rolling(50, 50).sum().replace(0.0, np.nan)
    return (sv / tv).diff(21).replace(_INF, np.nan)

# Registry

f25_vwap_deviation_slope_001_150_REGISTRY = {f.__name__: {"inputs": ins, "func": f} for f, ins in [
    (f25vw_f25_vwap_deviation_logclose_vwap_8d_slope_v001_signal, _HLCV),
    (f25vw_f25_vwap_deviation_logclose_vwap_63d_slope_v002_signal, _HLAV),
    (f25vw_f25_vwap_deviation_logclose_vwap_200d_slope_v003_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap5_vwap21_diff_slope_v004_signal, _HLCV),
    (f25vw_f25_vwap_deviation_vwap21_vwap252_diff_slope_v005_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap10_vwap40_diff_slope_v006_signal, _HLCV),
    (f25vw_f25_vwap_deviation_sign_close_vwap_15d_slope_v007_signal, _HLCV),
    (f25vw_f25_vwap_deviation_sign_close_vwap_45d_slope_v008_signal, _HLAV),
    (f25vw_f25_vwap_deviation_sign_close_vwap_120d_slope_v009_signal, _HLAV),
    (f25vw_f25_vwap_deviation_sign_vwap_shift_30_60d_slope_v010_signal, _HLAV),
    (f25vw_f25_vwap_deviation_sign_vwap10_vwap50_slope_v011_signal, _HLCV),
    (f25vw_f25_vwap_deviation_zscore_close_vwap_30d_slope_v012_signal, _HLAV),
    (f25vw_f25_vwap_deviation_zscore_close_vwap_90d_slope_v013_signal, _HLAV),
    (f25vw_f25_vwap_deviation_logclose_avwap_low_30d_slope_v014_signal, _HLAV),
    (f25vw_f25_vwap_deviation_logclose_avwap_high_30d_slope_v015_signal, _HLAV),
    (f25vw_f25_vwap_deviation_logclose_avwap_low_90d_slope_v016_signal, _HLAV),
    (f25vw_f25_vwap_deviation_sign_avwap_low_high_60d_slope_v017_signal, _HLAV),
    (f25vw_f25_vwap_deviation_avwap_convergence_45d_slope_v018_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_slope_20d_slope_v019_signal, _HLCV),
    (f25vw_f25_vwap_deviation_vwap_slope_100d_slope_v020_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_curvature_50d_slope_v021_signal, _HLAV),
    (f25vw_f25_vwap_deviation_sign_vwap_slope_25d_slope_v022_signal, _HLAV),
    (f25vw_f25_vwap_deviation_streak_above_vwap_30d_slope_v023_signal, _HLAV),
    (f25vw_f25_vwap_deviation_streak_below_vwap_75d_slope_v024_signal, _HLAV),
    (f25vw_f25_vwap_deviation_dayssince_vwap_cross_40d_slope_v025_signal, _HLAV),
    (f25vw_f25_vwap_deviation_dayssince_vwap_xover_30_90d_slope_v026_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_band_position_20d_slope_v027_signal, _HLCV),
    (f25vw_f25_vwap_deviation_vwap_band_position_60d_slope_v028_signal, _HLAV),
    (f25vw_f25_vwap_deviation_outside_vwap_2sigma_30d_slope_v029_signal, _HLAV),
    (f25vw_f25_vwap_deviation_days_outside_vwap_band_60d_slope_v030_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_residual_atr_25d_slope_v031_signal, _HLCV),
    (f25vw_f25_vwap_deviation_vwap_resid_skew_75d_slope_v032_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_gap_rank_50d_slope_v033_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_gap_rank_120d_slope_v034_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_twap_diff_20d_slope_v035_signal, _HLCV),
    (f25vw_f25_vwap_deviation_vwap_twap_diff_80d_slope_v036_signal, _HLAV),
    (f25vw_f25_vwap_deviation_sign_vwap_twap_45d_slope_v037_signal, _HLAV),
    (f25vw_f25_vwap_deviation_smoothed_vwap_diff_30d_slope_v038_signal, _HLAV),
    (f25vw_f25_vwap_deviation_ema_vwap_diff_60d_slope_v039_signal, _HLAV),
    (f25vw_f25_vwap_deviation_max_min_resid_ratio_50d_slope_v040_signal, _HLAV),
    (f25vw_f25_vwap_deviation_net_direction_vwap_30d_slope_v041_signal, _HLAV),
    (f25vw_f25_vwap_deviation_arctan_vwap_resid_120d_slope_v042_signal, _HLAV),
    (f25vw_f25_vwap_deviation_tanh_vwap_zscore_70d_slope_v043_signal, _HLAV),
    (f25vw_f25_vwap_deviation_sigmoid_vwap_resid_atr_40d_slope_v044_signal, _HLAV),
    (f25vw_f25_vwap_deviation_regime_strong_bull_40d_slope_v045_signal, _HLAV),
    (f25vw_f25_vwap_deviation_regime_strong_bear_50d_slope_v046_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_band_kurt_60d_slope_v047_signal, _HLAV),
    (f25vw_f25_vwap_deviation_high_vs_vwap_15d_slope_v048_signal, _HLCV),
    (f25vw_f25_vwap_deviation_hl_minus_vwap_15d_slope_v049_signal, _HLCV),
    (f25vw_f25_vwap_deviation_open_close_vs_vwap_55d_slope_v050_signal, _OHLAV),
    (f25vw_f25_vwap_deviation_vwap_slope_flip_freq_60d_slope_v051_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_xover_freq_120d_slope_v052_signal, _HLAV),
    (f25vw_f25_vwap_deviation_corr_close_vwap_45d_slope_v053_signal, _HLAV),
    (f25vw_f25_vwap_deviation_corr_close_vwap_lag10_80d_slope_v054_signal, _HLAV),
    (f25vw_f25_vwap_deviation_avwap_low_slope_40d_slope_v055_signal, _HLAV),
    (f25vw_f25_vwap_deviation_avwap_high_streak_150d_slope_v056_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_sigma_norm_35d_slope_v057_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_sigma_ratio_30_90d_slope_v058_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_resid_slope_45d_slope_v059_signal, _HLAV),
    (f25vw_f25_vwap_deviation_avwap_high_resid_slope_45d_slope_v060_signal, _HLAV),
    (f25vw_f25_vwap_deviation_above_band_count_45d_slope_v061_signal, _HLAV),
    (f25vw_f25_vwap_deviation_below_band_count_90d_slope_v062_signal, _HLAV),
    (f25vw_f25_vwap_deviation_avwap_low_age_norm_60d_slope_v063_signal, _HLAV),
    (f25vw_f25_vwap_deviation_dist_avwap_high_pct_60d_slope_v064_signal, _HLAV),
    (f25vw_f25_vwap_deviation_rank_vwap_50d_slope_v065_signal, _HLAV),
    (f25vw_f25_vwap_deviation_rank_vwap_slope_100d_slope_v066_signal, _HLAV),
    (f25vw_f25_vwap_deviation_sign_close_above_both_30d_slope_v067_signal, _HLAV),
    (f25vw_f25_vwap_deviation_resid_autocorr_lag5_60d_slope_v068_signal, _HLAV),
    (f25vw_f25_vwap_deviation_resid_autocorr_lag21_120d_slope_v069_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_curv_norm_100d_slope_v070_signal, _HLAV),
    (f25vw_f25_vwap_deviation_high_above_vwap_band_22d_slope_v071_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_lag_corr_80d_slope_v072_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_slope_spread_15_60d_slope_v073_signal, _HLAV),
    (f25vw_f25_vwap_deviation_majority_above_vwap_55d_slope_v074_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_diff_std_70d_slope_v075_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_diff_4_12d_slope_v076_signal, _HLCV),
    (f25vw_f25_vwap_deviation_vwap_diff_30_180d_slope_v077_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_resid_mad_40d_slope_v078_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_resid_iqr_75d_slope_v079_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_resid_median_norm_60d_slope_v080_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_resid_qrank_30d_slope_v081_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_resid_qrank_180d_slope_v082_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_ema_diff_15d_slope_v083_signal, _HLCV),
    (f25vw_f25_vwap_deviation_vwap_ema_diff_100d_slope_v084_signal, _HLAV),
    (f25vw_f25_vwap_deviation_corr_vwap_slopes_60d_slope_v085_signal, _HLAV),
    (f25vw_f25_vwap_deviation_dayssince_vwap_slope_flip_50d_slope_v086_signal, _HLAV),
    (f25vw_f25_vwap_deviation_dayssince_vwap_band_break_50d_slope_v087_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_range_30d_slope_v088_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_range_120d_slope_v089_signal, _HLAV),
    (f25vw_f25_vwap_deviation_close_pos_vs_vwap_range_50d_slope_v090_signal, _HLAV),
    (f25vw_f25_vwap_deviation_signed_dev_sum_45d_slope_v091_signal, _HLAV),
    (f25vw_f25_vwap_deviation_avwap_high_age_norm_90d_slope_v092_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_resid_above_frac_55d_slope_v093_signal, _HLAV),
    (f25vw_f25_vwap_deviation_max_run_above_vwap_60d_slope_v094_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_xover_short_45d_slope_v095_signal, _HLAV),
    (f25vw_f25_vwap_deviation_sign_concord_short_long_30d_slope_v096_signal, _HLAV),
    (f25vw_f25_vwap_deviation_sign_dev_slope_xor_50d_slope_v097_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_jerk_proxy_35d_slope_v098_signal, _HLAV),
    (f25vw_f25_vwap_deviation_high_minus_vwap_norm_50d_slope_v099_signal, _HLAV),
    (f25vw_f25_vwap_deviation_hl_range_vs_vwap_band_50d_slope_v100_signal, _HLAV),
    (f25vw_f25_vwap_deviation_post_cross_return_30d_slope_v101_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_gap_volnorm_25d_slope_v102_signal, _HLCV),
    (f25vw_f25_vwap_deviation_vwap_signed_vol_25d_slope_v103_signal, _HLCV),
    (f25vw_f25_vwap_deviation_avwap_channel_pos_75d_slope_v104_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_band_width_diff_45d_slope_v105_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_resid_when_up_60d_slope_v106_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_resid_ar1_60d_slope_v107_signal, _HLAV),
    (f25vw_f25_vwap_deviation_sign_change_density_120d_slope_v108_signal, _HLAV),
    (f25vw_f25_vwap_deviation_dist_avwap_low_vs_high_60d_slope_v109_signal, _HLAV),
    (f25vw_f25_vwap_deviation_beta_close_vwap_45d_slope_v110_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_trend_strength_60d_slope_v111_signal, _HLAV),
    (f25vw_f25_vwap_deviation_max_abs_dev_30d_slope_v112_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_resid_mad_z_70d_slope_v113_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_slope_z_70d_slope_v114_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_close_slope_agree_50d_slope_v115_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_band_pos_rolling_zscore_35d_slope_v116_signal, _HLAV),
    (f25vw_f25_vwap_deviation_avwap_low_resid_z_60d_slope_v117_signal, _HLAV),
    (f25vw_f25_vwap_deviation_avwap_high_curv_55d_slope_v118_signal, _HLAV),
    (f25vw_f25_vwap_deviation_avg_above_kvwap_50d_slope_v119_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_resid_skew_100d_slope_v120_signal, _HLAV),
    (f25vw_f25_vwap_deviation_multi_vwap_dispersion_45d_slope_v121_signal, _HLAV),
    (f25vw_f25_vwap_deviation_multi_vwap_descord_count_slope_v122_signal, _HLAV),
    (f25vw_f25_vwap_deviation_reversion_rate_vwap_40d_slope_v123_signal, _HLAV),
    (f25vw_f25_vwap_deviation_resid_rs_70d_slope_v124_signal, _HLAV),
    (f25vw_f25_vwap_deviation_resid_var_ratio_60d_slope_v125_signal, _HLAV),
    (f25vw_f25_vwap_deviation_resid_autocorr_ratio_80d_slope_v126_signal, _HLAV),
    (f25vw_f25_vwap_deviation_sign_resid_skew_50d_slope_v127_signal, _HLAV),
    (f25vw_f25_vwap_deviation_mean_abs_resid_norm_25d_slope_v128_signal, _HLCV),
    (f25vw_f25_vwap_deviation_high_vs_vwap_rank_60d_slope_v129_signal, _HLAV),
    (f25vw_f25_vwap_deviation_hl_vwap_rank_diff_60d_slope_v130_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_side_prob_80d_slope_v131_signal, _HLAV),
    (f25vw_f25_vwap_deviation_resid_kurt_120d_slope_v132_signal, _HLAV),
    (f25vw_f25_vwap_deviation_composite_state_50d_slope_v133_signal, _HLAV),
    (f25vw_f25_vwap_deviation_resid_time_rsq_40d_slope_v134_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_convergence_rate_60d_slope_v135_signal, _HLAV),
    (f25vw_f25_vwap_deviation_dayssince_above_vwap_band_60d_slope_v136_signal, _HLAV),
    (f25vw_f25_vwap_deviation_resid_efficiency_50d_slope_v137_signal, _HLAV),
    (f25vw_f25_vwap_deviation_dev_quantile_spread_60d_slope_v138_signal, _HLAV),
    (f25vw_f25_vwap_deviation_band_xover_count_90d_slope_v139_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_dir_persistence_45d_slope_v140_signal, _HLAV),
    (f25vw_f25_vwap_deviation_logclose_vwap_3d_slope_v141_signal, _HLCV),
    (f25vw_f25_vwap_deviation_resid_vol_corr_60d_slope_v142_signal, _HLAV),
    (f25vw_f25_vwap_deviation_band_width_atr_ratio_40d_slope_v143_signal, _HLAV),
    (f25vw_f25_vwap_deviation_intraday_range_vs_vwap_sigma_30d_slope_v144_signal, _HLAV),
    (f25vw_f25_vwap_deviation_dominant_side_strength_90d_slope_v145_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_up_day_ratio_70d_slope_v146_signal, _HLAV),
    (f25vw_f25_vwap_deviation_vwap_lead_corr_55d_slope_v147_signal, _HLAV),
    (f25vw_f25_vwap_deviation_resid_tail_count_45d_slope_v148_signal, _HLAV),
    (f25vw_f25_vwap_deviation_resid_halflife_proxy_50d_slope_v149_signal, _HLAV),
    (f25vw_f25_vwap_deviation_resid_sign_volsum_50d_slope_v150_signal, _HLAV),
]}

# Self-test

def _synthetic_inputs(n: int = 800, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    seg = n // 4
    rest = n - 3 * seg
    ret = np.concatenate([
        rng.normal(0.0012, 0.011, seg),
        rng.normal(-0.0005, 0.018, seg),
        rng.normal(-0.0010, 0.014, seg),
        rng.normal(0.0008, 0.012, rest),
    ])
    close = 50.0 * np.exp(np.cumsum(ret))
    adj_drift = rng.normal(0.0, 0.0003, size=n).cumsum()
    closeadj = close * np.exp(adj_drift)
    intraday = rng.normal(0.0, 0.008, size=n)
    open_ = close * np.exp(-intraday * 0.5)
    high = np.maximum(close, open_) * np.exp(np.abs(rng.normal(0.0, 0.006, size=n)))
    low = np.minimum(close, open_) * np.exp(-np.abs(rng.normal(0.0, 0.006, size=n)))
    volume = rng.lognormal(mean=13.0, sigma=0.6, size=n)
    idx = pd.RangeIndex(n)
    return pd.DataFrame({
        "open": pd.Series(open_, index=idx, dtype=float),
        "high": pd.Series(high, index=idx, dtype=float),
        "low": pd.Series(low, index=idx, dtype=float),
        "close": pd.Series(close, index=idx, dtype=float),
        "closeadj": pd.Series(closeadj, index=idx, dtype=float),
        "volume": pd.Series(volume, index=idx, dtype=float),
    })

def _self_test() -> None:
    df = _synthetic_inputs(n=800, seed=42)
    results: dict[str, pd.Series] = {}
    for name, entry in f25_vwap_deviation_slope_001_150_REGISTRY.items():
        args = [df[col] for col in entry["inputs"]]
        out = entry["func"](*args)
        assert isinstance(out, pd.Series), f"{name}: not a Series"
        assert len(out) == len(df), f"{name}: length mismatch"
        clean = out.dropna()
        assert len(clean) > 0, f"{name}: all NaN"
        assert float(clean.std()) > 0.0 or clean.nunique() > 1, f"{name}: constant/all-zero"
        results[name] = out

    warm = 252
    coverage_ok = sum(1 for s in results.values() if s.iloc[warm:].isna().mean() < 0.5)
    frac = coverage_ok / len(results)
    assert frac >= 0.80, f"NaN-coverage too low: {frac:.2%} have <50% NaN after warm-up"

    aligned = pd.concat({n: results[n] for n in results}, axis=1).iloc[warm:]
    aligned = aligned.replace(_INF, np.nan)
    corr = aligned.corr(min_periods=50).abs()
    np.fill_diagonal(corr.values, 0.0)
    max_corr = float(corr.max().max())
    if max_corr > 0.95:
        print(f"FAILING max |corr| = {max_corr:.4f}. Top pairs:")
        for i, a in enumerate(corr.columns):
            for j, b in enumerate(corr.columns):
                if j > i and corr.iloc[i, j] > 0.94:
                    print(f"  {a}  vs  {b}  ->  {corr.iloc[i, j]:.4f}")
    assert max_corr <= 0.95 + 1e-9, f"max pairwise |corr|={max_corr:.4f} exceeds 0.95"
    print(f"OK slope_001_150: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")

if __name__ == "__main__":
    _self_test()
