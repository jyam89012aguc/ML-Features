"""f25_vwap_deviation base features 001-075.

Domain: VWAP DEVIATION - features about deviations of price from VWAP
(volume-weighted typical-price average) and anchored-VWAP variants.

VWAP(N) = sum(typical_price * volume, N) / sum(volume, N)
typical_price = (high + low + close) / 3
AVWAP_from_low(N) = anchored VWAP starting at the N-day rolling low
AVWAP_from_high(N) = anchored VWAP starting at the N-day rolling high

Every feature references VWAP or anchored-VWAP. Structural classes mixed:
raw distances, log-ratios, z-scores, signs, streaks, days-since-cross,
percentile ranks, std-band positions, OHLC anchors, slopes, curvatures,
TWAP-contrast, bounded transforms, regime states, sum/count statistics.

NaN policy: never fillna(<value>); only replace([inf,-inf],nan) at the
final return. Window > 21d uses closeadj; <= 21d uses close.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Helpers (each function spells the VWAP formula fully inline below)
# ---------------------------------------------------------------------------


def _typ(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return (high + low + close) / 3.0


def _vwap(typ: pd.Series, volume: pd.Series, n: int) -> pd.Series:
    num = (typ * volume).rolling(n, min_periods=n).sum()
    den = volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return num / den


def _sma(s: pd.Series, n: int) -> pd.Series:
    return s.rolling(n, min_periods=n).mean()


def _ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False, min_periods=n).mean()


def _atr(high: pd.Series, low: pd.Series, close: pd.Series, n: int) -> pd.Series:
    pc = close.shift(1)
    tr = pd.concat([(high - low), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    return tr.ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()


def _avwap_from_low(typ: pd.Series, volume: pd.Series, n: int) -> pd.Series:
    """Anchored VWAP starting at the day of rolling N-day low of typ."""
    out = pd.Series(np.nan, index=typ.index, dtype=float)
    tv = (typ * volume).values
    vv = volume.values
    tyv = typ.values
    for i in range(len(typ)):
        if i < n - 1:
            continue
        s0 = i - n + 1
        window = tyv[s0:i + 1]
        if not np.all(np.isfinite(window)):
            continue
        anchor = s0 + int(np.argmin(window))
        num = float(np.nansum(tv[anchor:i + 1]))
        den = float(np.nansum(vv[anchor:i + 1]))
        if den != 0.0 and np.isfinite(num) and np.isfinite(den):
            out.iat[i] = num / den
    return out


def _avwap_from_high(typ: pd.Series, volume: pd.Series, n: int) -> pd.Series:
    """Anchored VWAP starting at the day of rolling N-day high of typ."""
    out = pd.Series(np.nan, index=typ.index, dtype=float)
    tv = (typ * volume).values
    vv = volume.values
    tyv = typ.values
    for i in range(len(typ)):
        if i < n - 1:
            continue
        s0 = i - n + 1
        window = tyv[s0:i + 1]
        if not np.all(np.isfinite(window)):
            continue
        anchor = s0 + int(np.argmax(window))
        num = float(np.nansum(tv[anchor:i + 1]))
        den = float(np.nansum(vv[anchor:i + 1]))
        if den != 0.0 and np.isfinite(num) and np.isfinite(den):
            out.iat[i] = num / den
    return out


def _streak_above(cond: pd.Series) -> pd.Series:
    """Number of consecutive bars with cond True up to and including today."""
    out = pd.Series(np.nan, index=cond.index, dtype=float)
    cv = cond.values
    run = 0
    seen = False
    for i in range(len(cond)):
        v = cv[i]
        if not np.isfinite(v) if isinstance(v, float) else v is None:
            run = 0
            continue
        if bool(v):
            run = run + 1
            seen = True
        else:
            run = 0
            seen = True
        if seen:
            out.iat[i] = float(run)
    return out


def _days_since_cross(sign_series: pd.Series) -> pd.Series:
    """Days since the sign last flipped (changed value vs prior bar)."""
    out = pd.Series(np.nan, index=sign_series.index, dtype=float)
    sv = sign_series.values
    last_flip = None
    prev = np.nan
    for i in range(len(sign_series)):
        v = sv[i]
        if not np.isfinite(v):
            continue
        if not np.isfinite(prev):
            prev = v
            last_flip = i
            out.iat[i] = 0.0
            continue
        if v != prev:
            last_flip = i
        prev = v
        out.iat[i] = float(i - last_flip)
    return out


# ---------------------------------------------------------------------------
# Features 001-075
# ---------------------------------------------------------------------------


# === Raw VWAP distances (sparse: only a few, widely-spaced windows) =========


def f25vw_f25_vwap_deviation_logclose_vwap_8d_base_v001_signal(high, low, close, volume):
    """log(close / VWAP(8))."""
    typ = (high + low + close) / 3.0
    num = (typ * volume).rolling(8, min_periods=8).sum()
    den = volume.rolling(8, min_periods=8).sum().replace(0.0, np.nan)
    vwap = num / den
    return np.log(close / vwap).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_logclose_vwap_63d_base_v002_signal(high, low, closeadj, volume):
    """log(close / VWAP(63))."""
    typ = (high + low + closeadj) / 3.0
    num = (typ * volume).rolling(63, min_periods=63).sum()
    den = volume.rolling(63, min_periods=63).sum().replace(0.0, np.nan)
    vwap = num / den
    return np.log(closeadj / vwap).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_logclose_vwap_200d_base_v003_signal(high, low, closeadj, volume):
    """log(close / VWAP(200))."""
    typ = (high + low + closeadj) / 3.0
    num = (typ * volume).rolling(200, min_periods=200).sum()
    den = volume.rolling(200, min_periods=200).sum().replace(0.0, np.nan)
    vwap = num / den
    return np.log(closeadj / vwap).replace([np.inf, -np.inf], np.nan)


# === Multi-window VWAP differentials (decorrelate via cross-window ratios) ==


def f25vw_f25_vwap_deviation_vwap5_vwap21_diff_base_v004_signal(high, low, close, volume):
    """log(VWAP(5) / VWAP(21)) - short-vs-medium VWAP differential."""
    typ = (high + low + close) / 3.0
    n1 = 5; n2 = 21
    v1 = (typ * volume).rolling(n1, min_periods=n1).sum() / volume.rolling(n1, min_periods=n1).sum().replace(0.0, np.nan)
    v2 = (typ * volume).rolling(n2, min_periods=n2).sum() / volume.rolling(n2, min_periods=n2).sum().replace(0.0, np.nan)
    return np.log(v1 / v2).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_vwap21_vwap252_diff_base_v005_signal(high, low, closeadj, volume):
    """log(VWAP(21) / VWAP(252)) - medium-vs-long VWAP differential."""
    typ = (high + low + closeadj) / 3.0
    n1 = 21; n2 = 252
    v1 = (typ * volume).rolling(n1, min_periods=n1).sum() / volume.rolling(n1, min_periods=n1).sum().replace(0.0, np.nan)
    v2 = (typ * volume).rolling(n2, min_periods=n2).sum() / volume.rolling(n2, min_periods=n2).sum().replace(0.0, np.nan)
    return np.log(v1 / v2).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_vwap10_vwap40_diff_base_v006_signal(high, low, close, volume):
    """log(VWAP(10) / VWAP(40)) - VWAP cross-window log-ratio."""
    typ = (high + low + close) / 3.0
    v1 = (typ * volume).rolling(10, min_periods=10).sum() / volume.rolling(10, min_periods=10).sum().replace(0.0, np.nan)
    v2 = (typ * volume).rolling(40, min_periods=40).sum() / volume.rolling(40, min_periods=40).sum().replace(0.0, np.nan)
    return np.log(v1 / v2).replace([np.inf, -np.inf], np.nan)


# === SIGN-based VWAP filters (discrete, decorrelates from continuous) =======


def f25vw_f25_vwap_deviation_sign_close_vwap_15d_base_v007_signal(high, low, close, volume):
    """sign(close - VWAP(15)) - discrete VWAP-side filter."""
    typ = (high + low + close) / 3.0
    vwap = (typ * volume).rolling(15, min_periods=15).sum() / volume.rolling(15, min_periods=15).sum().replace(0.0, np.nan)
    return np.sign(close - vwap).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_sign_close_vwap_45d_base_v008_signal(high, low, closeadj, volume):
    """sign(close - VWAP(45)) - discrete VWAP-side filter."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(45, min_periods=45).sum() / volume.rolling(45, min_periods=45).sum().replace(0.0, np.nan)
    return np.sign(closeadj - vwap).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_sign_close_vwap_120d_base_v009_signal(high, low, closeadj, volume):
    """sign(close - VWAP(120)) - long-term VWAP-side filter."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(120, min_periods=120).sum() / volume.rolling(120, min_periods=120).sum().replace(0.0, np.nan)
    return np.sign(closeadj - vwap).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_sign_vwap_shift_30_60d_base_v010_signal(high, low, closeadj, volume):
    """sign(VWAP(30) - VWAP(30).shift(60)) - VWAP trend sign."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(30, min_periods=30).sum() / volume.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    return np.sign(vwap - vwap.shift(60)).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_sign_vwap10_vwap50_base_v011_signal(high, low, close, volume):
    """sign(VWAP(10) - VWAP(50)) - VWAP crossover sign."""
    typ = (high + low + close) / 3.0
    v1 = (typ * volume).rolling(10, min_periods=10).sum() / volume.rolling(10, min_periods=10).sum().replace(0.0, np.nan)
    v2 = (typ * volume).rolling(50, min_periods=50).sum() / volume.rolling(50, min_periods=50).sum().replace(0.0, np.nan)
    return np.sign(v1 - v2).replace([np.inf, -np.inf], np.nan)


# === Z-score of close-vs-VWAP deviation =====================================


def f25vw_f25_vwap_deviation_zscore_close_vwap_30d_base_v012_signal(high, low, closeadj, volume):
    """z-score of (close - VWAP(30)) over trailing 60d."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(30, min_periods=30).sum() / volume.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    dev = closeadj - vwap
    mu = dev.rolling(60, min_periods=60).mean()
    sd = dev.rolling(60, min_periods=60).std()
    return ((dev - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_zscore_close_vwap_90d_base_v013_signal(high, low, closeadj, volume):
    """z-score of (close - VWAP(90)) over trailing 90d."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(90, min_periods=90).sum() / volume.rolling(90, min_periods=90).sum().replace(0.0, np.nan)
    dev = closeadj - vwap
    mu = dev.rolling(90, min_periods=90).mean()
    sd = dev.rolling(90, min_periods=90).std()
    return ((dev - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Anchored VWAP features =================================================


def f25vw_f25_vwap_deviation_logclose_avwap_low_30d_base_v014_signal(high, low, closeadj, volume):
    """log(close / AVWAP-from-rolling-30d-low)."""
    typ = (high + low + closeadj) / 3.0
    out = pd.Series(np.nan, index=typ.index, dtype=float)
    tv = (typ * volume).values; vv = volume.values; tyv = typ.values
    n = 30
    for i in range(len(typ)):
        if i < n - 1: continue
        s0 = i - n + 1
        w = tyv[s0:i + 1]
        if not np.all(np.isfinite(w)): continue
        anchor = s0 + int(np.argmin(w))
        num = float(np.nansum(tv[anchor:i + 1]))
        den = float(np.nansum(vv[anchor:i + 1]))
        if den != 0.0 and np.isfinite(num) and np.isfinite(den):
            out.iat[i] = num / den
    return np.log(closeadj / out).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_logclose_avwap_high_30d_base_v015_signal(high, low, closeadj, volume):
    """log(close / AVWAP-from-rolling-30d-high)."""
    typ = (high + low + closeadj) / 3.0
    out = pd.Series(np.nan, index=typ.index, dtype=float)
    tv = (typ * volume).values; vv = volume.values; tyv = typ.values
    n = 30
    for i in range(len(typ)):
        if i < n - 1: continue
        s0 = i - n + 1
        w = tyv[s0:i + 1]
        if not np.all(np.isfinite(w)): continue
        anchor = s0 + int(np.argmax(w))
        num = float(np.nansum(tv[anchor:i + 1]))
        den = float(np.nansum(vv[anchor:i + 1]))
        if den != 0.0 and np.isfinite(num) and np.isfinite(den):
            out.iat[i] = num / den
    return np.log(closeadj / out).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_logclose_avwap_low_90d_base_v016_signal(high, low, closeadj, volume):
    """log(close / AVWAP-from-rolling-90d-low)."""
    typ = (high + low + closeadj) / 3.0
    out = pd.Series(np.nan, index=typ.index, dtype=float)
    tv = (typ * volume).values; vv = volume.values; tyv = typ.values
    n = 90
    for i in range(len(typ)):
        if i < n - 1: continue
        s0 = i - n + 1
        w = tyv[s0:i + 1]
        if not np.all(np.isfinite(w)): continue
        anchor = s0 + int(np.argmin(w))
        num = float(np.nansum(tv[anchor:i + 1]))
        den = float(np.nansum(vv[anchor:i + 1]))
        if den != 0.0 and np.isfinite(num) and np.isfinite(den):
            out.iat[i] = num / den
    return np.log(closeadj / out).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_sign_avwap_low_high_60d_base_v017_signal(high, low, closeadj, volume):
    """sign(AVWAP-from-low(60) - AVWAP-from-high(60)) - which anchor is on top."""
    typ = (high + low + closeadj) / 3.0
    al = pd.Series(np.nan, index=typ.index, dtype=float)
    ah = pd.Series(np.nan, index=typ.index, dtype=float)
    tv = (typ * volume).values; vv = volume.values; tyv = typ.values
    n = 60
    for i in range(len(typ)):
        if i < n - 1: continue
        s0 = i - n + 1
        w = tyv[s0:i + 1]
        if not np.all(np.isfinite(w)): continue
        a_lo = s0 + int(np.argmin(w))
        a_hi = s0 + int(np.argmax(w))
        nlo = float(np.nansum(tv[a_lo:i + 1])); dlo = float(np.nansum(vv[a_lo:i + 1]))
        nhi = float(np.nansum(tv[a_hi:i + 1])); dhi = float(np.nansum(vv[a_hi:i + 1]))
        if dlo != 0.0 and dhi != 0.0:
            al.iat[i] = nlo / dlo
            ah.iat[i] = nhi / dhi
    return np.sign(al - ah).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_avwap_convergence_45d_base_v018_signal(high, low, closeadj, volume):
    """|AVWAP_low - AVWAP_high| / VWAP(45) - convergence of two anchors."""
    typ = (high + low + closeadj) / 3.0
    al = pd.Series(np.nan, index=typ.index, dtype=float)
    ah = pd.Series(np.nan, index=typ.index, dtype=float)
    tv = (typ * volume).values; vv = volume.values; tyv = typ.values
    n = 45
    for i in range(len(typ)):
        if i < n - 1: continue
        s0 = i - n + 1
        w = tyv[s0:i + 1]
        if not np.all(np.isfinite(w)): continue
        a_lo = s0 + int(np.argmin(w))
        a_hi = s0 + int(np.argmax(w))
        nlo = float(np.nansum(tv[a_lo:i + 1])); dlo = float(np.nansum(vv[a_lo:i + 1]))
        nhi = float(np.nansum(tv[a_hi:i + 1])); dhi = float(np.nansum(vv[a_hi:i + 1]))
        if dlo != 0.0 and dhi != 0.0:
            al.iat[i] = nlo / dlo
            ah.iat[i] = nhi / dhi
    vwap = (typ * volume).rolling(n, min_periods=n).sum() / volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return ((al - ah).abs() / vwap).replace([np.inf, -np.inf], np.nan)


# === VWAP slope (continuous + sign) =========================================


def f25vw_f25_vwap_deviation_vwap_slope_20d_base_v019_signal(high, low, close, volume):
    """VWAP(20).diff(10) / VWAP(20) - normalized VWAP slope."""
    typ = (high + low + close) / 3.0
    vwap = (typ * volume).rolling(20, min_periods=20).sum() / volume.rolling(20, min_periods=20).sum().replace(0.0, np.nan)
    return (vwap.diff(10) / vwap).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_vwap_slope_100d_base_v020_signal(high, low, closeadj, volume):
    """VWAP(100).diff(21) / VWAP(100) - long-term normalized VWAP slope."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(100, min_periods=100).sum() / volume.rolling(100, min_periods=100).sum().replace(0.0, np.nan)
    return (vwap.diff(21) / vwap).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_vwap_curvature_50d_base_v021_signal(high, low, closeadj, volume):
    """VWAP(50) - 2*VWAP(50).shift(10) + VWAP(50).shift(20), normalized by VWAP."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(50, min_periods=50).sum() / volume.rolling(50, min_periods=50).sum().replace(0.0, np.nan)
    return ((vwap - 2.0 * vwap.shift(10) + vwap.shift(20)) / vwap).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_sign_vwap_slope_25d_base_v022_signal(high, low, closeadj, volume):
    """sign(VWAP(25).diff(10)) - discrete VWAP-up/down indicator."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(25, min_periods=25).sum() / volume.rolling(25, min_periods=25).sum().replace(0.0, np.nan)
    return np.sign(vwap.diff(10)).replace([np.inf, -np.inf], np.nan)


# === Streaks and days-since-cross relative to VWAP ==========================


def f25vw_f25_vwap_deviation_streak_above_vwap_30d_base_v023_signal(high, low, closeadj, volume):
    """Streak length: bars closing above VWAP(30) consecutively up to today."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(30, min_periods=30).sum() / volume.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    cond = (closeadj > vwap).astype(float).where(~vwap.isna())
    out = pd.Series(np.nan, index=cond.index, dtype=float)
    run = 0
    started = False
    for i in range(len(cond)):
        v = cond.iat[i]
        if not np.isfinite(v):
            run = 0
            continue
        started = True
        if v > 0.5:
            run = run + 1
        else:
            run = 0
        if started:
            out.iat[i] = float(run)
    return out.replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_streak_below_vwap_75d_base_v024_signal(high, low, closeadj, volume):
    """Streak length: bars closing below VWAP(75) consecutively."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(75, min_periods=75).sum() / volume.rolling(75, min_periods=75).sum().replace(0.0, np.nan)
    cond = (closeadj < vwap).astype(float).where(~vwap.isna())
    out = pd.Series(np.nan, index=cond.index, dtype=float)
    run = 0
    started = False
    for i in range(len(cond)):
        v = cond.iat[i]
        if not np.isfinite(v):
            run = 0
            continue
        started = True
        if v > 0.5:
            run = run + 1
        else:
            run = 0
        if started:
            out.iat[i] = float(run)
    return out.replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_dayssince_vwap_cross_40d_base_v025_signal(high, low, closeadj, volume):
    """Days since last sign(close - VWAP(40)) change."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(40, min_periods=40).sum() / volume.rolling(40, min_periods=40).sum().replace(0.0, np.nan)
    sgn = np.sign(closeadj - vwap)
    out = pd.Series(np.nan, index=sgn.index, dtype=float)
    last = None
    prev = np.nan
    for i in range(len(sgn)):
        v = sgn.iat[i]
        if not np.isfinite(v): continue
        if not np.isfinite(prev):
            prev = v; last = i; out.iat[i] = 0.0; continue
        if v != prev: last = i
        prev = v
        out.iat[i] = float(i - last)
    return out.replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_dayssince_vwap_xover_30_90d_base_v026_signal(high, low, closeadj, volume):
    """Days since sign(VWAP(30) - VWAP(90)) changed."""
    typ = (high + low + closeadj) / 3.0
    v1 = (typ * volume).rolling(30, min_periods=30).sum() / volume.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    v2 = (typ * volume).rolling(90, min_periods=90).sum() / volume.rolling(90, min_periods=90).sum().replace(0.0, np.nan)
    sgn = np.sign(v1 - v2)
    out = pd.Series(np.nan, index=sgn.index, dtype=float)
    last = None
    prev = np.nan
    for i in range(len(sgn)):
        v = sgn.iat[i]
        if not np.isfinite(v): continue
        if not np.isfinite(prev):
            prev = v; last = i; out.iat[i] = 0.0; continue
        if v != prev: last = i
        prev = v
        out.iat[i] = float(i - last)
    return out.replace([np.inf, -np.inf], np.nan)


# === Std-band (VWAP +/- k*sigma) positions ==================================


def f25vw_f25_vwap_deviation_vwap_band_position_20d_base_v027_signal(high, low, close, volume):
    """(close - VWAP(20) + sigma) / (2*sigma) - relative position in +-1sigma band."""
    typ = (high + low + close) / 3.0
    vwap = (typ * volume).rolling(20, min_periods=20).sum() / volume.rolling(20, min_periods=20).sum().replace(0.0, np.nan)
    dev = (typ - vwap)
    sigma = dev.rolling(20, min_periods=20).std()
    return ((close - (vwap - sigma)) / (2.0 * sigma.replace(0.0, np.nan))).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_vwap_band_position_60d_base_v028_signal(high, low, closeadj, volume):
    """+-2sigma band relative position for VWAP(60)."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(60, min_periods=60).sum() / volume.rolling(60, min_periods=60).sum().replace(0.0, np.nan)
    dev = (typ - vwap)
    sigma = dev.rolling(60, min_periods=60).std()
    return ((closeadj - (vwap - 2.0 * sigma)) / (4.0 * sigma.replace(0.0, np.nan))).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_outside_vwap_2sigma_30d_base_v029_signal(high, low, closeadj, volume):
    """sign( (close - VWAP) - sign * 2*sigma ) - binary outside-+-2sigma indicator."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(30, min_periods=30).sum() / volume.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    dev = closeadj - vwap
    sigma = (typ - vwap).rolling(30, min_periods=30).std()
    above = (dev > 2.0 * sigma).astype(float)
    below = (dev < -2.0 * sigma).astype(float)
    out = (above - below).where(~sigma.isna())
    return out.replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_days_outside_vwap_band_60d_base_v030_signal(high, low, closeadj, volume):
    """Count over 60d of bars where |close - VWAP(60)| > 1sigma."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(60, min_periods=60).sum() / volume.rolling(60, min_periods=60).sum().replace(0.0, np.nan)
    dev = closeadj - vwap
    sigma = (typ - vwap).rolling(60, min_periods=60).std()
    outside = (dev.abs() > sigma).astype(float).where(~sigma.isna())
    return outside.rolling(60, min_periods=60).sum().replace([np.inf, -np.inf], np.nan)


# === VWAP residual in ATR units (volatility-normalized deviation) ===========


def f25vw_f25_vwap_deviation_vwap_residual_atr_25d_base_v031_signal(high, low, close, volume):
    """(close - VWAP(25)) / ATR(25)."""
    typ = (high + low + close) / 3.0
    vwap = (typ * volume).rolling(25, min_periods=25).sum() / volume.rolling(25, min_periods=25).sum().replace(0.0, np.nan)
    pc = close.shift(1)
    tr = pd.concat([(high - low), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 25.0, adjust=False, min_periods=25).mean()
    return ((close - vwap) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_vwap_resid_skew_75d_base_v032_signal(high, low, closeadj, volume):
    """rolling skewness of (close - VWAP(75)) over 75d - tail asymmetry of VWAP residual."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(75, min_periods=75).sum() / volume.rolling(75, min_periods=75).sum().replace(0.0, np.nan)
    dev = closeadj - vwap
    return dev.rolling(75, min_periods=75).skew().replace([np.inf, -np.inf], np.nan)


# === VWAP gap percentile rank ===============================================


def f25vw_f25_vwap_deviation_vwap_gap_rank_50d_base_v033_signal(high, low, closeadj, volume):
    """Percentile rank of (close - VWAP(50)) over trailing 50d."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(50, min_periods=50).sum() / volume.rolling(50, min_periods=50).sum().replace(0.0, np.nan)
    dev = closeadj - vwap
    return dev.rolling(50, min_periods=50).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_vwap_gap_rank_120d_base_v034_signal(high, low, closeadj, volume):
    """Percentile rank of (close - VWAP(120)) over trailing 120d."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(120, min_periods=120).sum() / volume.rolling(120, min_periods=120).sum().replace(0.0, np.nan)
    dev = closeadj - vwap
    return dev.rolling(120, min_periods=120).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# === VWAP vs TWAP (volume-weighted vs equal-weighted, decorrelates) =========


def f25vw_f25_vwap_deviation_vwap_twap_diff_20d_base_v035_signal(high, low, close, volume):
    """log(VWAP(20) / TWAP(20)) - volume-weighted vs equal-weighted typical price."""
    typ = (high + low + close) / 3.0
    vwap = (typ * volume).rolling(20, min_periods=20).sum() / volume.rolling(20, min_periods=20).sum().replace(0.0, np.nan)
    twap = typ.rolling(20, min_periods=20).mean()
    return np.log(vwap / twap).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_vwap_twap_diff_80d_base_v036_signal(high, low, closeadj, volume):
    """log(VWAP(80) / TWAP(80))."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(80, min_periods=80).sum() / volume.rolling(80, min_periods=80).sum().replace(0.0, np.nan)
    twap = typ.rolling(80, min_periods=80).mean()
    return np.log(vwap / twap).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_sign_vwap_twap_45d_base_v037_signal(high, low, closeadj, volume):
    """sign(VWAP(45) - TWAP(45)) - which is higher: volume-weighted or equal-weighted."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(45, min_periods=45).sum() / volume.rolling(45, min_periods=45).sum().replace(0.0, np.nan)
    twap = typ.rolling(45, min_periods=45).mean()
    return np.sign(vwap - twap).replace([np.inf, -np.inf], np.nan)


# === Smoothed VWAP-of-VWAPs =================================================


def f25vw_f25_vwap_deviation_smoothed_vwap_diff_30d_base_v038_signal(high, low, closeadj, volume):
    """log(VWAP(30) / SMA(VWAP(30), 30)) - VWAP vs smoothed self."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(30, min_periods=30).sum() / volume.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    smoothed = vwap.rolling(30, min_periods=30).mean()
    return np.log(vwap / smoothed).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_ema_vwap_diff_60d_base_v039_signal(high, low, closeadj, volume):
    """log(VWAP(60) / EMA(VWAP(60), 30))."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(60, min_periods=60).sum() / volume.rolling(60, min_periods=60).sum().replace(0.0, np.nan)
    smoothed = vwap.ewm(span=30, adjust=False, min_periods=30).mean()
    return np.log(vwap / smoothed).replace([np.inf, -np.inf], np.nan)


# === Cumulative deviation features ==========================================


def f25vw_f25_vwap_deviation_vwap_resid_max_min_ratio_50d_base_v040_signal(high, low, closeadj, volume):
    """max(close-VWAP) / |min(close-VWAP)| over 50d - up/down asymmetry of VWAP residual extremes."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(50, min_periods=50).sum() / volume.rolling(50, min_periods=50).sum().replace(0.0, np.nan)
    dev = closeadj - vwap
    mx = dev.rolling(50, min_periods=50).max()
    mn = dev.rolling(50, min_periods=50).min().abs().replace(0.0, np.nan)
    return (mx / mn).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_net_direction_vwap_30d_base_v041_signal(high, low, closeadj, volume):
    """Sum of sign(close - VWAP(30)) over 30d / 30 - fraction-net-direction."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(30, min_periods=30).sum() / volume.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    sgn = np.sign(closeadj - vwap)
    return (sgn.rolling(30, min_periods=30).sum() / 30.0).replace([np.inf, -np.inf], np.nan)


# === Bounded transforms of VWAP deviation ===================================


def f25vw_f25_vwap_deviation_arctan_vwap_resid_120d_base_v042_signal(high, low, closeadj, volume):
    """arctan((close - VWAP(120)) / sigma_120) - bounded long-term VWAP-residual."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(120, min_periods=120).sum() / volume.rolling(120, min_periods=120).sum().replace(0.0, np.nan)
    dev = closeadj - vwap
    sigma = (typ - vwap).rolling(120, min_periods=120).std().replace(0.0, np.nan)
    return np.arctan(dev / sigma).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_tanh_vwap_zscore_70d_base_v043_signal(high, low, closeadj, volume):
    """tanh(z-score of (close - VWAP(70))) - bounded long-window VWAP signal."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(70, min_periods=70).sum() / volume.rolling(70, min_periods=70).sum().replace(0.0, np.nan)
    dev = closeadj - vwap
    mu = dev.rolling(70, min_periods=70).mean()
    sd = dev.rolling(70, min_periods=70).std().replace(0.0, np.nan)
    return np.tanh(((dev - mu) / sd)).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_sigmoid_vwap_resid_atr_40d_base_v044_signal(high, low, closeadj, volume):
    """1/(1+exp(-(close-VWAP)/ATR)) - 0.5 - bounded VWAP-ATR residual."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(40, min_periods=40).sum() / volume.rolling(40, min_periods=40).sum().replace(0.0, np.nan)
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 40.0, adjust=False, min_periods=40).mean().replace(0.0, np.nan)
    x = (closeadj - vwap) / atr
    return (1.0 / (1.0 + np.exp(-x)) - 0.5).replace([np.inf, -np.inf], np.nan)


# === Discrete regime states based on VWAP-band ==============================


def f25vw_f25_vwap_deviation_regime_strong_bull_40d_base_v045_signal(high, low, closeadj, volume):
    """close > VWAP + 1sigma AND VWAP-slope > 0 -> strong bull."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(40, min_periods=40).sum() / volume.rolling(40, min_periods=40).sum().replace(0.0, np.nan)
    sigma = (typ - vwap).rolling(40, min_periods=40).std().replace(0.0, np.nan)
    cond1 = (closeadj > (vwap + sigma)).astype(float)
    cond2 = (vwap.diff(10) > 0).astype(float)
    return (cond1 * cond2).where(~sigma.isna() & ~vwap.diff(10).isna()).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_regime_strong_bear_50d_base_v046_signal(high, low, closeadj, volume):
    """close < VWAP - 1sigma AND VWAP-slope < 0 -> strong bear."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(50, min_periods=50).sum() / volume.rolling(50, min_periods=50).sum().replace(0.0, np.nan)
    sigma = (typ - vwap).rolling(50, min_periods=50).std().replace(0.0, np.nan)
    cond1 = (closeadj < (vwap - sigma)).astype(float)
    cond2 = (vwap.diff(10) < 0).astype(float)
    return (cond1 * cond2).where(~sigma.isna() & ~vwap.diff(10).isna()).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_vwap_band_kurt_60d_base_v047_signal(high, low, closeadj, volume):
    """Rolling kurtosis of (close - VWAP(60)) over 60d - VWAP-residual tail-heaviness."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(60, min_periods=60).sum() / volume.rolling(60, min_periods=60).sum().replace(0.0, np.nan)
    dev = closeadj - vwap
    return dev.rolling(60, min_periods=60).kurt().replace([np.inf, -np.inf], np.nan)


# === OHLC-anchored VWAP variants (intraday-typ-price contrast) ==============


def f25vw_f25_vwap_deviation_high_vs_vwap_15d_base_v048_signal(high, low, close, volume):
    """log(high / VWAP(15)) - intra-bar upside-vs-VWAP."""
    typ = (high + low + close) / 3.0
    vwap = (typ * volume).rolling(15, min_periods=15).sum() / volume.rolling(15, min_periods=15).sum().replace(0.0, np.nan)
    return np.log(high / vwap).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_hl_minus_vwap_15d_base_v049_signal(high, low, close, volume):
    """((high+low)/2 - VWAP(15)) / (high - low) - midpoint-vs-VWAP normalized by bar range."""
    typ = (high + low + close) / 3.0
    vwap = (typ * volume).rolling(15, min_periods=15).sum() / volume.rolling(15, min_periods=15).sum().replace(0.0, np.nan)
    mid = 0.5 * (high + low)
    rng = (high - low).replace(0.0, np.nan)
    return ((mid - vwap) / rng).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_open_close_vs_vwap_55d_base_v050_signal(open_, high, low, closeadj, volume):
    """(close - open) / (close - VWAP(55)) magnitude - bar-direction relative to VWAP-deviation."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(55, min_periods=55).sum() / volume.rolling(55, min_periods=55).sum().replace(0.0, np.nan)
    dev = (closeadj - vwap).abs().replace(0.0, np.nan)
    return ((closeadj - open_) / dev).replace([np.inf, -np.inf], np.nan)


# === VWAP slope sign change frequency =======================================


def f25vw_f25_vwap_deviation_vwap_slope_flip_freq_60d_base_v051_signal(high, low, closeadj, volume):
    """Count of VWAP(35) slope-sign flips over last 60d."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(35, min_periods=35).sum() / volume.rolling(35, min_periods=35).sum().replace(0.0, np.nan)
    slope = vwap.diff(10)
    sgn = np.sign(slope)
    flip = (sgn != sgn.shift(1)).astype(float).where(~sgn.isna() & ~sgn.shift(1).isna())
    return flip.rolling(60, min_periods=60).sum().replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_vwap_xover_freq_120d_base_v052_signal(high, low, closeadj, volume):
    """Count of close-vs-VWAP(20) crossovers over 120d."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(20, min_periods=20).sum() / volume.rolling(20, min_periods=20).sum().replace(0.0, np.nan)
    sgn = np.sign(closeadj - vwap)
    flip = (sgn != sgn.shift(1)).astype(float).where(~sgn.isna() & ~sgn.shift(1).isna())
    return flip.rolling(120, min_periods=120).sum().replace([np.inf, -np.inf], np.nan)


# === Rolling correlation of close with VWAP =================================


def f25vw_f25_vwap_deviation_corr_close_vwap_45d_base_v053_signal(high, low, closeadj, volume):
    """Pearson correlation of close with VWAP(30) over 45d window."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(30, min_periods=30).sum() / volume.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    return closeadj.rolling(45, min_periods=45).corr(vwap).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_corr_close_vwap_lag10_80d_base_v054_signal(high, low, closeadj, volume):
    """Corr of close with VWAP(40).shift(10) over 80d - lagged VWAP relation."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(40, min_periods=40).sum() / volume.rolling(40, min_periods=40).sum().replace(0.0, np.nan)
    return closeadj.rolling(80, min_periods=80).corr(vwap.shift(10)).replace([np.inf, -np.inf], np.nan)


# === AVWAP from period-start (rolling-reset) ================================


def f25vw_f25_vwap_deviation_avwap_low_slope_40d_base_v055_signal(high, low, closeadj, volume):
    """slope: log(AVWAP-from-low(40)).diff(10) - anchored VWAP velocity."""
    typ = (high + low + closeadj) / 3.0
    out = pd.Series(np.nan, index=typ.index, dtype=float)
    tv = (typ * volume).values; vv = volume.values; tyv = typ.values
    n = 40
    for i in range(len(typ)):
        if i < n - 1: continue
        s0 = i - n + 1
        w = tyv[s0:i + 1]
        if not np.all(np.isfinite(w)): continue
        a = s0 + int(np.argmin(w))
        num = float(np.nansum(tv[a:i + 1]))
        den = float(np.nansum(vv[a:i + 1]))
        if den != 0.0:
            out.iat[i] = num / den
    return np.log(out).diff(10).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_avwap_high_streak_150d_base_v056_signal(high, low, closeadj, volume):
    """streak: bars in a row where close > AVWAP-from-high(150)."""
    typ = (high + low + closeadj) / 3.0
    avw = pd.Series(np.nan, index=typ.index, dtype=float)
    tv = (typ * volume).values; vv = volume.values; tyv = typ.values
    n = 150
    for i in range(len(typ)):
        if i < n - 1: continue
        s0 = i - n + 1
        w = tyv[s0:i + 1]
        if not np.all(np.isfinite(w)): continue
        a = s0 + int(np.argmax(w))
        num = float(np.nansum(tv[a:i + 1]))
        den = float(np.nansum(vv[a:i + 1]))
        if den != 0.0:
            avw.iat[i] = num / den
    cond = (closeadj > avw).astype(float).where(~avw.isna())
    out = pd.Series(np.nan, index=cond.index, dtype=float)
    run = 0
    started = False
    for i in range(len(cond)):
        v = cond.iat[i]
        if not np.isfinite(v):
            run = 0
            continue
        started = True
        if v > 0.5:
            run = run + 1
        else:
            run = 0
        if started:
            out.iat[i] = float(run)
    return out.replace([np.inf, -np.inf], np.nan)


# === Distance from VWAP std (volatility around VWAP) ========================


def f25vw_f25_vwap_deviation_vwap_sigma_norm_35d_base_v057_signal(high, low, closeadj, volume):
    """sigma_vwap / VWAP(35) - VWAP-relative volatility."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(35, min_periods=35).sum() / volume.rolling(35, min_periods=35).sum().replace(0.0, np.nan)
    sigma = (typ - vwap).rolling(35, min_periods=35).std()
    return (sigma / vwap).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_vwap_sigma_ratio_30_90d_base_v058_signal(high, low, closeadj, volume):
    """sigma_vwap(30) / sigma_vwap(90) - VWAP-vol regime."""
    typ = (high + low + closeadj) / 3.0
    v1 = (typ * volume).rolling(30, min_periods=30).sum() / volume.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    v2 = (typ * volume).rolling(90, min_periods=90).sum() / volume.rolling(90, min_periods=90).sum().replace(0.0, np.nan)
    s1 = (typ - v1).rolling(30, min_periods=30).std()
    s2 = (typ - v2).rolling(90, min_periods=90).std().replace(0.0, np.nan)
    return (s1 / s2).replace([np.inf, -np.inf], np.nan)


# === VWAP-residual slope ====================================================


def f25vw_f25_vwap_deviation_vwap_resid_slope_45d_base_v059_signal(high, low, closeadj, volume):
    """(close - VWAP(45)).diff(10) / VWAP(45) - residual slope."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(45, min_periods=45).sum() / volume.rolling(45, min_periods=45).sum().replace(0.0, np.nan)
    dev = closeadj - vwap
    return (dev.diff(10) / vwap).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_avwap_high_resid_slope_45d_base_v060_signal(high, low, closeadj, volume):
    """slope of log(close/AVWAP-from-high(45))."""
    typ = (high + low + closeadj) / 3.0
    out = pd.Series(np.nan, index=typ.index, dtype=float)
    tv = (typ * volume).values; vv = volume.values; tyv = typ.values
    n = 45
    for i in range(len(typ)):
        if i < n - 1: continue
        s0 = i - n + 1
        w = tyv[s0:i + 1]
        if not np.all(np.isfinite(w)): continue
        a_hi = s0 + int(np.argmax(w))
        num = float(np.nansum(tv[a_hi:i + 1]))
        den = float(np.nansum(vv[a_hi:i + 1]))
        if den != 0.0:
            out.iat[i] = num / den
    resid = np.log(closeadj / out)
    return resid.diff(10).replace([np.inf, -np.inf], np.nan)


# === Frequency of close inside band over different windows ==================


def f25vw_f25_vwap_deviation_above_band_count_45d_base_v061_signal(high, low, closeadj, volume):
    """Count over 45d of bars where close > VWAP(45) + 1sigma."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(45, min_periods=45).sum() / volume.rolling(45, min_periods=45).sum().replace(0.0, np.nan)
    sigma = (typ - vwap).rolling(45, min_periods=45).std().replace(0.0, np.nan)
    above = (closeadj > (vwap + sigma)).astype(float).where(~sigma.isna())
    return above.rolling(45, min_periods=45).sum().replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_below_band_count_90d_base_v062_signal(high, low, closeadj, volume):
    """Count over 90d of bars where close < VWAP(90) - 1sigma."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(90, min_periods=90).sum() / volume.rolling(90, min_periods=90).sum().replace(0.0, np.nan)
    sigma = (typ - vwap).rolling(90, min_periods=90).std().replace(0.0, np.nan)
    below = (closeadj < (vwap - sigma)).astype(float).where(~sigma.isna())
    return below.rolling(90, min_periods=90).sum().replace([np.inf, -np.inf], np.nan)


# === Distance from AVWAP-low / AVWAP-high in normalized units ===============


def f25vw_f25_vwap_deviation_avwap_low_age_norm_60d_base_v063_signal(high, low, closeadj, volume):
    """Days since the rolling-60d low (anchor age for AVWAP-low) / 60."""
    typ = (high + low + closeadj) / 3.0
    out = pd.Series(np.nan, index=typ.index, dtype=float)
    tyv = typ.values
    n = 60
    for i in range(len(typ)):
        if i < n - 1: continue
        s0 = i - n + 1
        w = tyv[s0:i + 1]
        if not np.all(np.isfinite(w)): continue
        a = int(np.argmin(w))
        out.iat[i] = float(n - 1 - a) / float(n)
    return out.replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_dist_avwap_high_pct_60d_base_v064_signal(high, low, closeadj, volume):
    """(close - AVWAP-from-high(60)) / close - percentage below-anchor."""
    typ = (high + low + closeadj) / 3.0
    out = pd.Series(np.nan, index=typ.index, dtype=float)
    tv = (typ * volume).values; vv = volume.values; tyv = typ.values
    n = 60
    for i in range(len(typ)):
        if i < n - 1: continue
        s0 = i - n + 1
        w = tyv[s0:i + 1]
        if not np.all(np.isfinite(w)): continue
        a_hi = s0 + int(np.argmax(w))
        num = float(np.nansum(tv[a_hi:i + 1]))
        den = float(np.nansum(vv[a_hi:i + 1]))
        if den != 0.0:
            out.iat[i] = num / den
    return ((closeadj - out) / closeadj).replace([np.inf, -np.inf], np.nan)


# === Rolling rank-based features ============================================


def f25vw_f25_vwap_deviation_rank_vwap_50d_base_v065_signal(high, low, closeadj, volume):
    """Percentile rank of VWAP(20) within trailing 50d."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(20, min_periods=20).sum() / volume.rolling(20, min_periods=20).sum().replace(0.0, np.nan)
    return vwap.rolling(50, min_periods=50).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_rank_vwap_slope_100d_base_v066_signal(high, low, closeadj, volume):
    """Percentile rank of VWAP(40)-slope within trailing 100d."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(40, min_periods=40).sum() / volume.rolling(40, min_periods=40).sum().replace(0.0, np.nan)
    slope = vwap.diff(21)
    return slope.rolling(100, min_periods=100).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# === Sign-based VWAP-vs-TWAP discrete classes ===============================


def f25vw_f25_vwap_deviation_sign_close_above_both_30d_base_v067_signal(high, low, closeadj, volume):
    """sign( close>VWAP(30) AND close>TWAP(30) ) discrete combined-side regime."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(30, min_periods=30).sum() / volume.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    twap = typ.rolling(30, min_periods=30).mean()
    above_v = (closeadj > vwap).astype(float)
    above_t = (closeadj > twap).astype(float)
    return (above_v + above_t - 1.0).where(~vwap.isna() & ~twap.isna()).replace([np.inf, -np.inf], np.nan)


# === VWAP-residual autocorrelation ==========================================


def f25vw_f25_vwap_deviation_resid_autocorr_lag5_60d_base_v068_signal(high, low, closeadj, volume):
    """Autocorrelation of (close-VWAP(30)) at lag 5 over 60d."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(30, min_periods=30).sum() / volume.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    dev = closeadj - vwap
    return dev.rolling(60, min_periods=60).corr(dev.shift(5)).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_resid_autocorr_lag21_120d_base_v069_signal(high, low, closeadj, volume):
    """Autocorrelation of (close-VWAP(80)) at lag 21 over 120d."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(80, min_periods=80).sum() / volume.rolling(80, min_periods=80).sum().replace(0.0, np.nan)
    dev = closeadj - vwap
    return dev.rolling(120, min_periods=120).corr(dev.shift(21)).replace([np.inf, -np.inf], np.nan)


# === VWAP slope curvature (2nd deriv proxy) =================================


def f25vw_f25_vwap_deviation_vwap_curv_norm_100d_base_v070_signal(high, low, closeadj, volume):
    """(VWAP(100) - 2*VWAP(100).shift(21) + VWAP(100).shift(42)) / VWAP(100) - curvature."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(100, min_periods=100).sum() / volume.rolling(100, min_periods=100).sum().replace(0.0, np.nan)
    return ((vwap - 2.0 * vwap.shift(21) + vwap.shift(42)) / vwap).replace([np.inf, -np.inf], np.nan)


# === Range positions relative to VWAP =======================================


def f25vw_f25_vwap_deviation_high_above_vwap_band_22d_base_v071_signal(high, low, closeadj, volume):
    """sign((high - VWAP(22)) - 2*sigma) - binary intra-bar VWAP-band breakout indicator."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(22, min_periods=22).sum() / volume.rolling(22, min_periods=22).sum().replace(0.0, np.nan)
    sigma = (typ - vwap).rolling(22, min_periods=22).std().replace(0.0, np.nan)
    above = ((high - vwap) > 2.0 * sigma).astype(float)
    below = ((low - vwap) < -2.0 * sigma).astype(float)
    return (above - below).where(~sigma.isna()).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_vwap_lag_corr_80d_base_v072_signal(high, low, closeadj, volume):
    """rolling corr of VWAP(20) with VWAP(20).shift(40) over 80d - VWAP self-persistence."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(20, min_periods=20).sum() / volume.rolling(20, min_periods=20).sum().replace(0.0, np.nan)
    return vwap.rolling(80, min_periods=80).corr(vwap.shift(40)).replace([np.inf, -np.inf], np.nan)


# === Cross-window VWAP slope spread =========================================


def f25vw_f25_vwap_deviation_vwap_slope_spread_15_60d_base_v073_signal(high, low, closeadj, volume):
    """short-VWAP-slope - long-VWAP-slope - regime divergence."""
    typ = (high + low + closeadj) / 3.0
    v1 = (typ * volume).rolling(15, min_periods=15).sum() / volume.rolling(15, min_periods=15).sum().replace(0.0, np.nan)
    v2 = (typ * volume).rolling(60, min_periods=60).sum() / volume.rolling(60, min_periods=60).sum().replace(0.0, np.nan)
    return ((v1.diff(5) / v1) - (v2.diff(21) / v2)).replace([np.inf, -np.inf], np.nan)


# === Discrete majority-vote across multiple VWAP windows ====================


def f25vw_f25_vwap_deviation_majority_above_vwap_55d_base_v074_signal(high, low, closeadj, volume):
    """Sum over 55d of sign(close - VWAP(n)) for n in {20,40,60,80,100} divided by 5*55."""
    typ = (high + low + closeadj) / 3.0
    sigs = []
    mask = pd.Series(True, index=typ.index)
    for n in (20, 40, 60, 80, 100):
        vwap = (typ * volume).rolling(n, min_periods=n).sum() / volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
        sigs.append(np.sign(closeadj - vwap))
        mask = mask & ~vwap.isna()
    total = pd.concat(sigs, axis=1).sum(axis=1)
    s = total.where(mask)
    return (s.rolling(55, min_periods=55).sum() / (5.0 * 55.0)).replace([np.inf, -np.inf], np.nan)


# === VWAP slope std (dispersion of VWAP changes) ============================


def f25vw_f25_vwap_deviation_vwap_diff_std_70d_base_v075_signal(high, low, closeadj, volume):
    """std of VWAP(50).diff(1) over 70d - smoothness of VWAP path."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(50, min_periods=50).sum() / volume.rolling(50, min_periods=50).sum().replace(0.0, np.nan)
    return (vwap.diff(1).rolling(70, min_periods=70).std() / vwap).replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f25_vwap_deviation_base_001_075_REGISTRY = {
    "f25vw_f25_vwap_deviation_logclose_vwap_8d_base_v001_signal": {"inputs": ["high", "low", "close", "volume"], "func": f25vw_f25_vwap_deviation_logclose_vwap_8d_base_v001_signal},
    "f25vw_f25_vwap_deviation_logclose_vwap_63d_base_v002_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_logclose_vwap_63d_base_v002_signal},
    "f25vw_f25_vwap_deviation_logclose_vwap_200d_base_v003_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_logclose_vwap_200d_base_v003_signal},
    "f25vw_f25_vwap_deviation_vwap5_vwap21_diff_base_v004_signal": {"inputs": ["high", "low", "close", "volume"], "func": f25vw_f25_vwap_deviation_vwap5_vwap21_diff_base_v004_signal},
    "f25vw_f25_vwap_deviation_vwap21_vwap252_diff_base_v005_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap21_vwap252_diff_base_v005_signal},
    "f25vw_f25_vwap_deviation_vwap10_vwap40_diff_base_v006_signal": {"inputs": ["high", "low", "close", "volume"], "func": f25vw_f25_vwap_deviation_vwap10_vwap40_diff_base_v006_signal},
    "f25vw_f25_vwap_deviation_sign_close_vwap_15d_base_v007_signal": {"inputs": ["high", "low", "close", "volume"], "func": f25vw_f25_vwap_deviation_sign_close_vwap_15d_base_v007_signal},
    "f25vw_f25_vwap_deviation_sign_close_vwap_45d_base_v008_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_sign_close_vwap_45d_base_v008_signal},
    "f25vw_f25_vwap_deviation_sign_close_vwap_120d_base_v009_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_sign_close_vwap_120d_base_v009_signal},
    "f25vw_f25_vwap_deviation_sign_vwap_shift_30_60d_base_v010_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_sign_vwap_shift_30_60d_base_v010_signal},
    "f25vw_f25_vwap_deviation_sign_vwap10_vwap50_base_v011_signal": {"inputs": ["high", "low", "close", "volume"], "func": f25vw_f25_vwap_deviation_sign_vwap10_vwap50_base_v011_signal},
    "f25vw_f25_vwap_deviation_zscore_close_vwap_30d_base_v012_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_zscore_close_vwap_30d_base_v012_signal},
    "f25vw_f25_vwap_deviation_zscore_close_vwap_90d_base_v013_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_zscore_close_vwap_90d_base_v013_signal},
    "f25vw_f25_vwap_deviation_logclose_avwap_low_30d_base_v014_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_logclose_avwap_low_30d_base_v014_signal},
    "f25vw_f25_vwap_deviation_logclose_avwap_high_30d_base_v015_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_logclose_avwap_high_30d_base_v015_signal},
    "f25vw_f25_vwap_deviation_logclose_avwap_low_90d_base_v016_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_logclose_avwap_low_90d_base_v016_signal},
    "f25vw_f25_vwap_deviation_sign_avwap_low_high_60d_base_v017_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_sign_avwap_low_high_60d_base_v017_signal},
    "f25vw_f25_vwap_deviation_avwap_convergence_45d_base_v018_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_avwap_convergence_45d_base_v018_signal},
    "f25vw_f25_vwap_deviation_vwap_slope_20d_base_v019_signal": {"inputs": ["high", "low", "close", "volume"], "func": f25vw_f25_vwap_deviation_vwap_slope_20d_base_v019_signal},
    "f25vw_f25_vwap_deviation_vwap_slope_100d_base_v020_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_slope_100d_base_v020_signal},
    "f25vw_f25_vwap_deviation_vwap_curvature_50d_base_v021_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_curvature_50d_base_v021_signal},
    "f25vw_f25_vwap_deviation_sign_vwap_slope_25d_base_v022_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_sign_vwap_slope_25d_base_v022_signal},
    "f25vw_f25_vwap_deviation_streak_above_vwap_30d_base_v023_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_streak_above_vwap_30d_base_v023_signal},
    "f25vw_f25_vwap_deviation_streak_below_vwap_75d_base_v024_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_streak_below_vwap_75d_base_v024_signal},
    "f25vw_f25_vwap_deviation_dayssince_vwap_cross_40d_base_v025_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_dayssince_vwap_cross_40d_base_v025_signal},
    "f25vw_f25_vwap_deviation_dayssince_vwap_xover_30_90d_base_v026_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_dayssince_vwap_xover_30_90d_base_v026_signal},
    "f25vw_f25_vwap_deviation_vwap_band_position_20d_base_v027_signal": {"inputs": ["high", "low", "close", "volume"], "func": f25vw_f25_vwap_deviation_vwap_band_position_20d_base_v027_signal},
    "f25vw_f25_vwap_deviation_vwap_band_position_60d_base_v028_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_band_position_60d_base_v028_signal},
    "f25vw_f25_vwap_deviation_outside_vwap_2sigma_30d_base_v029_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_outside_vwap_2sigma_30d_base_v029_signal},
    "f25vw_f25_vwap_deviation_days_outside_vwap_band_60d_base_v030_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_days_outside_vwap_band_60d_base_v030_signal},
    "f25vw_f25_vwap_deviation_vwap_residual_atr_25d_base_v031_signal": {"inputs": ["high", "low", "close", "volume"], "func": f25vw_f25_vwap_deviation_vwap_residual_atr_25d_base_v031_signal},
    "f25vw_f25_vwap_deviation_vwap_resid_skew_75d_base_v032_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_resid_skew_75d_base_v032_signal},
    "f25vw_f25_vwap_deviation_vwap_gap_rank_50d_base_v033_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_gap_rank_50d_base_v033_signal},
    "f25vw_f25_vwap_deviation_vwap_gap_rank_120d_base_v034_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_gap_rank_120d_base_v034_signal},
    "f25vw_f25_vwap_deviation_vwap_twap_diff_20d_base_v035_signal": {"inputs": ["high", "low", "close", "volume"], "func": f25vw_f25_vwap_deviation_vwap_twap_diff_20d_base_v035_signal},
    "f25vw_f25_vwap_deviation_vwap_twap_diff_80d_base_v036_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_twap_diff_80d_base_v036_signal},
    "f25vw_f25_vwap_deviation_sign_vwap_twap_45d_base_v037_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_sign_vwap_twap_45d_base_v037_signal},
    "f25vw_f25_vwap_deviation_smoothed_vwap_diff_30d_base_v038_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_smoothed_vwap_diff_30d_base_v038_signal},
    "f25vw_f25_vwap_deviation_ema_vwap_diff_60d_base_v039_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_ema_vwap_diff_60d_base_v039_signal},
    "f25vw_f25_vwap_deviation_vwap_resid_max_min_ratio_50d_base_v040_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_resid_max_min_ratio_50d_base_v040_signal},
    "f25vw_f25_vwap_deviation_net_direction_vwap_30d_base_v041_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_net_direction_vwap_30d_base_v041_signal},
    "f25vw_f25_vwap_deviation_arctan_vwap_resid_120d_base_v042_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_arctan_vwap_resid_120d_base_v042_signal},
    "f25vw_f25_vwap_deviation_tanh_vwap_zscore_70d_base_v043_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_tanh_vwap_zscore_70d_base_v043_signal},
    "f25vw_f25_vwap_deviation_sigmoid_vwap_resid_atr_40d_base_v044_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_sigmoid_vwap_resid_atr_40d_base_v044_signal},
    "f25vw_f25_vwap_deviation_regime_strong_bull_40d_base_v045_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_regime_strong_bull_40d_base_v045_signal},
    "f25vw_f25_vwap_deviation_regime_strong_bear_50d_base_v046_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_regime_strong_bear_50d_base_v046_signal},
    "f25vw_f25_vwap_deviation_vwap_band_kurt_60d_base_v047_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_band_kurt_60d_base_v047_signal},
    "f25vw_f25_vwap_deviation_high_vs_vwap_15d_base_v048_signal": {"inputs": ["high", "low", "close", "volume"], "func": f25vw_f25_vwap_deviation_high_vs_vwap_15d_base_v048_signal},
    "f25vw_f25_vwap_deviation_hl_minus_vwap_15d_base_v049_signal": {"inputs": ["high", "low", "close", "volume"], "func": f25vw_f25_vwap_deviation_hl_minus_vwap_15d_base_v049_signal},
    "f25vw_f25_vwap_deviation_open_close_vs_vwap_55d_base_v050_signal": {"inputs": ["open", "high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_open_close_vs_vwap_55d_base_v050_signal},
    "f25vw_f25_vwap_deviation_vwap_slope_flip_freq_60d_base_v051_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_slope_flip_freq_60d_base_v051_signal},
    "f25vw_f25_vwap_deviation_vwap_xover_freq_120d_base_v052_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_xover_freq_120d_base_v052_signal},
    "f25vw_f25_vwap_deviation_corr_close_vwap_45d_base_v053_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_corr_close_vwap_45d_base_v053_signal},
    "f25vw_f25_vwap_deviation_corr_close_vwap_lag10_80d_base_v054_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_corr_close_vwap_lag10_80d_base_v054_signal},
    "f25vw_f25_vwap_deviation_avwap_low_slope_40d_base_v055_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_avwap_low_slope_40d_base_v055_signal},
    "f25vw_f25_vwap_deviation_avwap_high_streak_150d_base_v056_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_avwap_high_streak_150d_base_v056_signal},
    "f25vw_f25_vwap_deviation_vwap_sigma_norm_35d_base_v057_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_sigma_norm_35d_base_v057_signal},
    "f25vw_f25_vwap_deviation_vwap_sigma_ratio_30_90d_base_v058_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_sigma_ratio_30_90d_base_v058_signal},
    "f25vw_f25_vwap_deviation_vwap_resid_slope_45d_base_v059_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_resid_slope_45d_base_v059_signal},
    "f25vw_f25_vwap_deviation_avwap_high_resid_slope_45d_base_v060_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_avwap_high_resid_slope_45d_base_v060_signal},
    "f25vw_f25_vwap_deviation_above_band_count_45d_base_v061_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_above_band_count_45d_base_v061_signal},
    "f25vw_f25_vwap_deviation_below_band_count_90d_base_v062_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_below_band_count_90d_base_v062_signal},
    "f25vw_f25_vwap_deviation_avwap_low_age_norm_60d_base_v063_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_avwap_low_age_norm_60d_base_v063_signal},
    "f25vw_f25_vwap_deviation_dist_avwap_high_pct_60d_base_v064_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_dist_avwap_high_pct_60d_base_v064_signal},
    "f25vw_f25_vwap_deviation_rank_vwap_50d_base_v065_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_rank_vwap_50d_base_v065_signal},
    "f25vw_f25_vwap_deviation_rank_vwap_slope_100d_base_v066_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_rank_vwap_slope_100d_base_v066_signal},
    "f25vw_f25_vwap_deviation_sign_close_above_both_30d_base_v067_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_sign_close_above_both_30d_base_v067_signal},
    "f25vw_f25_vwap_deviation_resid_autocorr_lag5_60d_base_v068_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_resid_autocorr_lag5_60d_base_v068_signal},
    "f25vw_f25_vwap_deviation_resid_autocorr_lag21_120d_base_v069_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_resid_autocorr_lag21_120d_base_v069_signal},
    "f25vw_f25_vwap_deviation_vwap_curv_norm_100d_base_v070_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_curv_norm_100d_base_v070_signal},
    "f25vw_f25_vwap_deviation_high_above_vwap_band_22d_base_v071_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_high_above_vwap_band_22d_base_v071_signal},
    "f25vw_f25_vwap_deviation_vwap_lag_corr_80d_base_v072_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_lag_corr_80d_base_v072_signal},
    "f25vw_f25_vwap_deviation_vwap_slope_spread_15_60d_base_v073_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_slope_spread_15_60d_base_v073_signal},
    "f25vw_f25_vwap_deviation_majority_above_vwap_55d_base_v074_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_majority_above_vwap_55d_base_v074_signal},
    "f25vw_f25_vwap_deviation_vwap_diff_std_70d_base_v075_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_diff_std_70d_base_v075_signal},
}


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------


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
    for name, entry in f25_vwap_deviation_base_001_075_REGISTRY.items():
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
    aligned = aligned.replace([np.inf, -np.inf], np.nan)
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
    print(f"OK base_001_075: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
