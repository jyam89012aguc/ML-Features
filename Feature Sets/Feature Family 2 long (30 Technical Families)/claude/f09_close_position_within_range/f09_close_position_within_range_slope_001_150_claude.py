"""f09 slope (1st derivative): base.diff(k). Derivative inlined."""
from __future__ import annotations

import numpy as np
import pandas as pd


def _ols_slope(x):
    if np.isnan(x).any():
        return np.nan
    n = len(x)
    t = np.arange(n, dtype=float)
    tm = t.mean()
    xm = x.mean()
    num = np.sum((t - tm) * (x - xm))
    den = np.sum((t - tm) ** 2)
    return float(num / den) if den != 0.0 else np.nan


def _ols_r2(x):
    if np.isnan(x).any():
        return np.nan
    n = len(x)
    t = np.arange(n, dtype=float)
    tm = t.mean()
    xm = x.mean()
    num = np.sum((t - tm) * (x - xm))
    dt = np.sum((t - tm) ** 2)
    dx = np.sum((x - xm) ** 2)
    if dt == 0.0 or dx == 0.0:
        return np.nan
    r = num / np.sqrt(dt * dx)
    return float(r * r)


def _hurst_rs(x):
    x = x[~np.isnan(x)]
    if len(x) < 30:
        return np.nan
    y = x - x.mean()
    z = y.cumsum()
    r = z.max() - z.min()
    s = x.std()
    if s == 0.0 or r == 0.0:
        return np.nan
    return float(np.log(r / s) / np.log(len(x)))


def _entropy5(x):
    x = x[~np.isnan(x)]
    if len(x) < 5:
        return np.nan
    h, _ = np.histogram(x, bins=5, range=(0.0, 1.0))
    p = h / h.sum() if h.sum() > 0 else h
    nz = p[p > 0]
    return float(-(nz * np.log(nz)).sum())
def f09cp_f09_close_position_within_range_cpdisp_1d_slope_v002_signal(close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    b = (2.0 * cp - 1.0) ** 2
    out = b.diff(5) / b.abs().rolling(5, min_periods=5).mean().replace(0.0, np.nan)
    return out.replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpprior_1d_slope_v004_signal(close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    b = cp - cp.shift(3)
    return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_logodds_1d_slope_v005_signal(close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    eps = rng * 0.001 + 1e-9
    lo = np.log((close - low) + eps) - np.log((high - close) + eps)
    b = lo - lo.ewm(span=5, adjust=False, min_periods=5).mean()
    return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpop_1d_slope_v006_signal(close, open, high, low):
    rng = (high - low).replace(0.0, np.nan)
    b = (close - open) / rng
    return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_op_1d_slope_v007_signal(open, high, low):
    rng = (high - low).replace(0.0, np.nan)
    b = (open - low) / rng
    return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpopabs_5d_slope_v008_signal(close, open, high, low):
    rng = (high - low).replace(0.0, np.nan)
    d = ((close - open) / rng).abs()
    b = d.rolling(5, min_periods=5).mean()
    return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpopsgn_10d_slope_v009_signal(close, open, high, low):
    drift = close - open
    pos = (drift > 0).astype(float)
    neg = (drift < 0).astype(float)
    pos = pos.where(~(high - low).eq(0.0), np.nan)
    neg = neg.where(~(high - low).eq(0.0), np.nan)
    b = (pos - neg).rolling(10, min_periods=10).sum() / 10.0
    return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_oppos_21d_slope_v010_signal(open, high, low):
    rng = (high - low).replace(0.0, np.nan)
    op = (open - low) / rng
    b = op.rolling(21, min_periods=21).mean()
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpmean_5d_slope_v011_signal(close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    b = cp.rolling(5, min_periods=5).mean()
    return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpmean_21d_slope_v012_signal(close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    b = cp.rolling(21, min_periods=21).mean()
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpmed_63d_slope_v013_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    b = cp.rolling(63, min_periods=63).median()
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpstd_21d_slope_v014_signal(close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    b = cp.rolling(21, min_periods=21).std()
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpstd_63d_slope_v015_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    b = cp.rolling(63, min_periods=63).std()
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpskew_42d_slope_v016_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    b = cp.rolling(42, min_periods=42).skew()
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpkurt_50d_slope_v017_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    b = cp.rolling(50, min_periods=50).kurt()
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpmax_15d_slope_v018_signal(close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    b = cp.rolling(15, min_periods=15).max()
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpmin_30d_slope_v019_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    b = cp.rolling(30, min_periods=30).min()
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cprange_45d_slope_v020_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    b = cp.rolling(45, min_periods=45).max() - cp.rolling(45, min_periods=45).min()
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_hicnt_20d_slope_v021_signal(close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    hi = (cp > 0.7).astype(float).where(cp.notna(), np.nan)
    b = hi.rolling(20, min_periods=20).sum() / 20.0
    return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_locnt_30d_slope_v022_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    lo = (cp < 0.3).astype(float).where(cp.notna(), np.nan)
    b = lo.rolling(30, min_periods=30).sum() / 30.0
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_hilodif_40d_slope_v023_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    hi = (cp > 0.7).astype(float).where(cp.notna(), np.nan)
    lo = (cp < 0.3).astype(float).where(cp.notna(), np.nan)
    b = (hi - lo).rolling(40, min_periods=40).sum() / 40.0
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_extrhi_50d_slope_v024_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    flag = (cp > 0.9).astype(float).where(cp.notna(), np.nan)
    b = flag.rolling(50, min_periods=50).sum() / 50.0
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_extrlo_50d_slope_v025_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    flag = (cp < 0.1).astype(float).where(cp.notna(), np.nan)
    b = flag.rolling(50, min_periods=50).sum() / 50.0
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_midcnt_60d_slope_v026_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    flag = ((cp >= 0.4) & (cp <= 0.6)).astype(float).where(cp.notna(), np.nan)
    b = flag.rolling(60, min_periods=60).sum() / 60.0
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_hilorat_30d_slope_v027_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    hi = (cp > 0.6).astype(float).where(cp.notna(), np.nan)
    lo = (cp < 0.4).astype(float).where(cp.notna(), np.nan)
    hs = hi.rolling(30, min_periods=30).sum()
    ls = lo.rolling(30, min_periods=30).sum()
    b = (hs - ls) / (hs + ls + 1.0)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_consechi_10d_slope_v028_signal(close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    pair = ((cp > 0.7) & (cp.shift(1) > 0.7)).astype(float).where(
        cp.notna() & cp.shift(1).notna(), np.nan
    )
    b = pair.rolling(10, min_periods=10).sum() / 10.0
    return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_streakhi_15d_slope_v029_signal(close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    above = (cp > 0.5).astype(float).where(cp.notna(), np.nan)
    out_vals = np.full(len(close), np.nan)
    prev = 0.0
    for i in range(len(close)):
        v = above.iloc[i]
        if np.isnan(v):
            prev = 0.0
            out_vals[i] = np.nan
            continue
        if v > 0.5:
            prev = prev + 1.0
        else:
            prev = 0.0
        out_vals[i] = min(prev, 15.0)
    b = pd.Series(out_vals, index=close.index)
    return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_streaklo_15d_slope_v030_signal(close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    below = (cp < 0.5).astype(float).where(cp.notna(), np.nan)
    out_vals = np.full(len(close), np.nan)
    prev = 0.0
    for i in range(len(close)):
        v = below.iloc[i]
        if np.isnan(v):
            prev = 0.0
            out_vals[i] = np.nan
            continue
        if v > 0.5:
            prev = prev + 1.0
        else:
            prev = 0.0
        out_vals[i] = min(prev, 15.0)
    b = pd.Series(out_vals, index=close.index)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_dayssincehi_50d_slope_v031_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    flag = (cp > 0.9).astype(float).where(cp.notna(), np.nan)
    out_vals = np.full(len(close), np.nan)
    days = np.nan
    for i in range(len(close)):
        v = flag.iloc[i]
        if np.isnan(v):
            out_vals[i] = np.nan
            continue
        if v > 0.5:
            days = 0.0
        elif np.isnan(days):
            days = np.nan
        else:
            days = days + 1.0
        out_vals[i] = min(days, 50.0) if not np.isnan(days) else np.nan
    b = pd.Series(out_vals, index=close.index)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_dayssincelo_50d_slope_v032_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    flag = (cp < 0.1).astype(float).where(cp.notna(), np.nan)
    out_vals = np.full(len(close), np.nan)
    days = np.nan
    for i in range(len(close)):
        v = flag.iloc[i]
        if np.isnan(v):
            out_vals[i] = np.nan
            continue
        if v > 0.5:
            days = 0.0
        elif np.isnan(days):
            days = np.nan
        else:
            days = days + 1.0
        out_vals[i] = min(days, 50.0) if not np.isnan(days) else np.nan
    b = pd.Series(out_vals, index=close.index)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_midstreak_15d_slope_v033_signal(close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    sign = np.sign(cp - 0.5).where(cp.notna(), np.nan)
    out_vals = np.full(len(close), np.nan)
    prev_sign = 0.0
    cnt = 0.0
    for i in range(len(close)):
        v = sign.iloc[i]
        if np.isnan(v):
            prev_sign = 0.0
            cnt = 0.0
            out_vals[i] = np.nan
            continue
        if v == prev_sign and v != 0.0:
            cnt = cnt + 1.0
        else:
            cnt = 1.0
        prev_sign = v
        out_vals[i] = min(cnt, 15.0) * v
    b = pd.Series(out_vals, index=close.index)
    return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_flipfreq_30d_slope_v034_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    side = np.sign(cp - 0.5)
    flip = (side != side.shift(1)).astype(float).where(side.notna() & side.shift(1).notna(), np.nan)
    b = flip.rolling(30, min_periods=30).sum() / 30.0
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpdiff_1d_slope_v035_signal(close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    b = cp.diff(1)
    return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpdiff_5d_slope_v036_signal(close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    b = cp - cp.shift(5)
    return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpchgabs_10d_slope_v037_signal(close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    b = cp.diff(1).abs().rolling(10, min_periods=10).mean()
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpchgsgn_20d_slope_v038_signal(close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    s = np.sign(cp.diff(1))
    b = s.rolling(20, min_periods=20).sum() / 20.0
    return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpaccdir_15d_slope_v039_signal(close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    d = cp.diff(1)
    s = np.sign(d)
    same = (s == s.shift(1)).astype(float).where(s.notna() & s.shift(1).notna(), np.nan)
    b = same.rolling(15, min_periods=15).sum() / 15.0
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpslope_30d_slope_v040_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    b = cp.rolling(5, min_periods=5).mean() - cp.rolling(30, min_periods=30).mean()
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_volwcp_21d_slope_v041_signal(close, high, low, volume):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    num = (cp * volume).rolling(21, min_periods=21).sum()
    den = volume.rolling(21, min_periods=21).sum().replace(0.0, np.nan)
    b = num / den
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_rngwcp_30d_slope_v042_signal(closeadj, close, high, low):
    rngraw = high - low
    rng = rngraw.replace(0.0, np.nan)
    cp = (close - low) / rng
    num = (cp * rngraw).rolling(30, min_periods=30).sum()
    den = rngraw.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    b = num / den
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_dollwcp_40d_slope_v043_signal(closeadj, close, high, low, volume):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    dv = close * volume
    num = (cp * dv).rolling(40, min_periods=40).sum()
    den = dv.rolling(40, min_periods=40).sum().replace(0.0, np.nan)
    b = num / den
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_expwcp_10d_slope_v044_signal(close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    b = cp.ewm(span=10, adjust=False, min_periods=10).mean()
    return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_expwcp_50d_slope_v045_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    b = cp.ewm(span=50, adjust=False, min_periods=50).mean() - cp.ewm(span=10, adjust=False, min_periods=10).mean()
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_trimcp_30d_slope_v046_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    q10 = cp.rolling(30, min_periods=30).quantile(0.10)
    q90 = cp.rolling(30, min_periods=30).quantile(0.90)
    mid = cp.where((cp >= q10) & (cp <= q90))
    b = mid.rolling(30, min_periods=15).mean()
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_disprk_60d_slope_v047_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    disp = (2.0 * cp - 1.0) ** 2
    b = disp.rolling(60, min_periods=30).rank(pct=True) - 0.5
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpabsdrk_120d_slope_v048_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    d = cp.diff(1).abs()
    b = d.rolling(120, min_periods=60).rank(pct=True) - 0.5
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpmidvol_30d_slope_v049_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    b = (cp - 0.5).rolling(30, min_periods=30).std()
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpd10zsc_90d_slope_v050_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    d = cp.diff(10)
    m = d.rolling(90, min_periods=45).mean()
    sd = d.rolling(90, min_periods=45).std().replace(0.0, np.nan)
    b = (d - m) / sd
    return b.diff(63).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpiqr_50d_slope_v051_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    q3 = cp.rolling(50, min_periods=25).quantile(0.75)
    q1 = cp.rolling(50, min_periods=25).quantile(0.25)
    b = q3 - q1
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpquint_30d_slope_v052_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    q20 = cp.rolling(30, min_periods=15).quantile(0.20)
    q40 = cp.rolling(30, min_periods=15).quantile(0.40)
    q60 = cp.rolling(30, min_periods=15).quantile(0.60)
    q80 = cp.rolling(30, min_periods=15).quantile(0.80)
    bucket = pd.Series(np.nan, index=cp.index, dtype=float)
    bucket = bucket.where(cp.isna(), 3.0)
    bucket = bucket.where(cp.isna() | (cp > q20), 1.0)
    bucket = bucket.where(cp.isna() | (cp <= q20) | (cp > q40), 2.0)
    bucket = bucket.where(cp.isna() | (cp <= q60) | (cp > q80), 4.0)
    bucket = bucket.where(cp.isna() | (cp <= q80), 5.0)
    b = bucket - 3.0
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_midabs_5d_slope_v053_signal(close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    b = (cp - 0.5).abs().rolling(5, min_periods=5).mean()
    return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_midabs_50d_slope_v054_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    b = (cp - 0.5).abs().rolling(50, min_periods=50).mean()
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_asymabs_20d_slope_v055_signal(close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    asym = (high + low - 2.0 * close).abs() / rng
    b = asym.rolling(20, min_periods=20).mean()
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_tdvol_30d_slope_v056_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    td = (high - close) / rng
    vol = (np.log(close.replace(0.0, np.nan)) - np.log(close.shift(1).replace(0.0, np.nan))).abs()
    b = td.rolling(30, min_periods=15).corr(vol)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_topdistabs_45d_slope_v057_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    tri = (high - close) * (close - low) / (rng * rng)
    b = tri.rolling(45, min_periods=45).mean()
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_extrabs_30d_slope_v058_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    flag = ((cp - 0.5).abs() > 0.4).astype(float).where(cp.notna(), np.nan)
    b = flag.rolling(30, min_periods=30).sum() / 30.0
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpxabsret_15d_slope_v059_signal(close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    r = close.pct_change()
    b = (cp * r.abs()).rolling(15, min_periods=15).mean()
    return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpxret_25d_slope_v060_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    r = close.pct_change()
    b = ((cp - 0.5) * r).rolling(25, min_periods=25).mean()
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cphighrng_20d_slope_v061_signal(close, high, low):
    rngraw = high - low
    rng = rngraw.replace(0.0, np.nan)
    cp = (close - low) / rng
    med = rngraw.rolling(20, min_periods=20).median()
    big = cp.where(rngraw > med)
    b = big.rolling(20, min_periods=10).mean()
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cplowrng_20d_slope_v062_signal(close, high, low):
    rngraw = high - low
    rng = rngraw.replace(0.0, np.nan)
    cp = (close - low) / rng
    med = rngraw.rolling(20, min_periods=20).median()
    small = cp.where(rngraw <= med)
    b = small.rolling(20, min_periods=10).mean()
    return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpcondvol_30d_slope_v063_signal(closeadj, close, high, low):
    rngraw = high - low
    rng = rngraw.replace(0.0, np.nan)
    cp = (close - low) / rng
    med = rngraw.rolling(30, min_periods=30).median()
    big = cp.where(rngraw > med).rolling(30, min_periods=15).mean()
    small = cp.where(rngraw <= med).rolling(30, min_periods=15).mean()
    b = big - small
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpac1_60d_slope_v064_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    b = cp.rolling(60, min_periods=30).corr(cp.shift(1))
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpac5_80d_slope_v065_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    b = cp.rolling(80, min_periods=40).corr(cp.shift(5))
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_three_hi_25d_slope_v066_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    a = (cp > 0.7).astype(float).where(cp.notna(), np.nan)
    triple = (a * a.shift(1) * a.shift(2)).where(
        a.notna() & a.shift(1).notna() & a.shift(2).notna(), np.nan
    )
    b = triple.rolling(25, min_periods=25).sum() / 25.0
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_three_lo_25d_slope_v067_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    a = (cp < 0.3).astype(float).where(cp.notna(), np.nan)
    triple = (a * a.shift(1) * a.shift(2)).where(
        a.notna() & a.shift(1).notna() & a.shift(2).notna(), np.nan
    )
    b = triple.rolling(25, min_periods=25).sum() / 25.0
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpspan_5d_slope_v069_signal(close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    b = cp.rolling(5, min_periods=5).max() - cp.rolling(5, min_periods=5).min()
    return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpcormid_40d_slope_v070_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    rngraw = high - low
    b = cp.rolling(40, min_periods=20).corr(rngraw)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_revpat_30d_slope_v071_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    pat = ((cp.shift(1) > 0.7) & (cp < 0.3)).astype(float).where(
        cp.notna() & cp.shift(1).notna(), np.nan
    )
    b = pat.rolling(30, min_periods=30).sum() / 30.0
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_dispsma_25d_slope_v072_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    b = ((2.0 * cp - 1.0) ** 2).rolling(25, min_periods=25).mean()
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpvolvscp_45d_slope_v073_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    relrng = (high - low) / close.replace(0.0, np.nan)
    b = cp.rolling(45, min_periods=22).corr(relrng)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpregr_50d_slope_v074_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng

    b = cp.rolling(50, min_periods=50).apply(_ols_slope, raw=True)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpmad_35d_slope_v075_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    med = cp.rolling(35, min_periods=35).median()
    b = (cp - med).abs().rolling(35, min_periods=35).mean()
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_sinpi_1d_slope_v076_signal(close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    # use the smoothed base shape's diff at k=5
    b = np.sin(np.pi * cp).ewm(span=3, adjust=False, min_periods=3).mean()
    return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpsmallrng_1d_slope_v077_signal(close, high, low):
    rngraw = high - low
    rng = rngraw.replace(0.0, np.nan)
    cp = (close - low) / rng
    relrng = rngraw / close.replace(0.0, np.nan)
    b = (cp / (1.0 + 50.0 * relrng)).ewm(span=5, adjust=False, min_periods=5).mean()
    return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cubed_1d_slope_v078_signal(close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    b = (2.0 * cp - 1.0) ** 3
    return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_relu_top_1d_slope_v079_signal(close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    b = (cp - 0.5).clip(lower=0.0).where(cp.notna(), np.nan)
    return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_relu_bot_1d_slope_v080_signal(close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    b = (0.5 - cp).clip(lower=0.0).where(cp.notna(), np.nan)
    return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpwma_15d_slope_v081_signal(close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    n = 15
    w = np.arange(1, n + 1, dtype=float)
    w /= w.sum()
    b = cp.rolling(n, min_periods=n).apply(lambda x: float(np.dot(x, w)), raw=True)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpgeo_30d_slope_v082_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    shifted = (cp + 0.01).replace(0.0, np.nan)
    lcp = np.log(shifted)
    b = np.exp(lcp.rolling(30, min_periods=30).mean()) - 0.01
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cphar_25d_slope_v083_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    inv = 1.0 / (cp + 0.01).replace(0.0, np.nan)
    b = 1.0 / inv.rolling(25, min_periods=25).mean() - 0.01
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpqr10_50d_slope_v084_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    b = cp.rolling(50, min_periods=25).quantile(0.10)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpqr90_50d_slope_v085_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    b = cp.rolling(50, min_periods=25).quantile(0.90)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpq90mid_60d_slope_v086_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    q90 = cp.rolling(60, min_periods=30).quantile(0.90)
    q10 = cp.rolling(60, min_periods=30).quantile(0.10)
    b = q90 - q10
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpmedabs_45d_slope_v087_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    b = (cp - 0.5).abs().rolling(45, min_periods=45).median()
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpentropy_60d_slope_v088_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng

    b = cp.rolling(60, min_periods=30).apply(_entropy5, raw=True)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_q60cnt_30d_slope_v089_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    flag = (cp > 0.6).astype(float).where(cp.notna(), np.nan)
    b = flag.rolling(30, min_periods=30).sum() / 30.0
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_q40cnt_30d_slope_v090_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    flag = (cp < 0.4).astype(float).where(cp.notna(), np.nan)
    b = flag.rolling(30, min_periods=30).sum() / 30.0
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_q80cnt_60d_slope_v091_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    flag = (cp > 0.8).astype(float).where(cp.notna(), np.nan)
    b = flag.rolling(60, min_periods=60).sum() / 60.0
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_q20cnt_60d_slope_v092_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    flag = (cp < 0.2).astype(float).where(cp.notna(), np.nan)
    b = flag.rolling(60, min_periods=60).sum() / 60.0
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_topbal_40d_slope_v093_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    hi = (cp > 0.8).astype(float).where(cp.notna(), np.nan)
    lo = (cp < 0.2).astype(float).where(cp.notna(), np.nan)
    hs = hi.rolling(40, min_periods=40).sum()
    ls = lo.rolling(40, min_periods=40).sum()
    b = (hs - ls) / (hs + ls + 2.0)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_extrhi_10d_slope_v094_signal(close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    flag = (cp > 0.95).astype(float).where(cp.notna(), np.nan)
    b = flag.rolling(10, min_periods=10).sum() / 10.0
    return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_extrlo_10d_slope_v095_signal(close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    flag = (cp < 0.05).astype(float).where(cp.notna(), np.nan)
    b = flag.rolling(10, min_periods=10).sum() / 10.0
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_inside_70d_slope_v096_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    flag = ((cp >= 0.2) & (cp <= 0.8)).astype(float).where(cp.notna(), np.nan)
    b = flag.rolling(70, min_periods=70).sum() / 70.0
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_streakextrhi_20d_slope_v097_signal(close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    above = (cp > 0.8).astype(float).where(cp.notna(), np.nan)
    out_vals = np.full(len(close), np.nan)
    prev = 0.0
    for i in range(len(close)):
        v = above.iloc[i]
        if np.isnan(v):
            prev = 0.0
            out_vals[i] = np.nan
            continue
        if v > 0.5:
            prev = prev + 1.0
        else:
            prev = 0.0
        out_vals[i] = min(prev, 20.0)
    b = pd.Series(out_vals, index=close.index)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_dayslastflip_30d_slope_v098_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    side = np.sign(cp - 0.5)
    flip = (side != side.shift(1)) & side.notna() & side.shift(1).notna()
    out_vals = np.full(len(close), np.nan)
    days = np.nan
    for i in range(len(close)):
        v = flip.iloc[i]
        s = side.iloc[i]
        if np.isnan(s):
            out_vals[i] = np.nan
            continue
        if v:
            days = 0.0
        elif np.isnan(days):
            days = np.nan
        else:
            days = days + 1.0
        out_vals[i] = min(days, 30.0) if not np.isnan(days) else np.nan
    b = pd.Series(out_vals, index=close.index)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_dayssincextrhi_100d_slope_v099_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    flag = (cp > 0.8).astype(float).where(cp.notna(), np.nan)
    out_vals = np.full(len(close), np.nan)
    days = np.nan
    for i in range(len(close)):
        v = flag.iloc[i]
        if np.isnan(v):
            out_vals[i] = np.nan
            continue
        if v > 0.5:
            days = 0.0
        elif np.isnan(days):
            days = np.nan
        else:
            days = days + 1.0
        out_vals[i] = min(days, 100.0) if not np.isnan(days) else np.nan
    b = pd.Series(out_vals, index=close.index)
    return b.diff(63).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_runlen_above_30d_slope_v100_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    above = (cp > 0.5).astype(int).where(cp.notna(), np.nan)
    streaks = []
    prev = 0
    for i in range(len(close)):
        v = above.iloc[i]
        if np.isnan(v):
            streaks.append(np.nan)
            prev = 0
            continue
        if v >= 1:
            prev = prev + 1
        else:
            prev = 0
        streaks.append(prev)
    s = pd.Series(streaks, index=close.index, dtype=float)
    b = s.rolling(30, min_periods=15).max()
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_runlen_below_30d_slope_v101_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    below = (cp < 0.5).astype(int).where(cp.notna(), np.nan)
    streaks = []
    prev = 0
    for i in range(len(close)):
        v = below.iloc[i]
        if np.isnan(v):
            streaks.append(np.nan)
            prev = 0
            continue
        if v >= 1:
            prev = prev + 1
        else:
            prev = 0
        streaks.append(prev)
    s = pd.Series(streaks, index=close.index, dtype=float)
    b = s.rolling(30, min_periods=15).max()
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpmom_10d_slope_v102_signal(close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    b = cp - cp.shift(10)
    return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpmom_21d_slope_v103_signal(close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    b = cp - cp.shift(21)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpaccdir_30d_slope_v104_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    short_dir = np.sign(cp.diff(1))
    long_dir = np.sign(cp.diff(5))
    agree = (short_dir == long_dir).astype(float).where(
        short_dir.notna() & long_dir.notna() & (short_dir != 0) & (long_dir != 0), np.nan
    )
    b = agree.rolling(30, min_periods=30).sum() / 30.0 - 0.5
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpaccel_25d_slope_v105_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    j = cp - 2.0 * cp.shift(5) + cp.shift(10)
    b = j.rolling(25, min_periods=25).mean()
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpup10_30d_slope_v106_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    up = (cp > cp.shift(1)).astype(float).where(cp.notna() & cp.shift(1).notna(), np.nan)
    b = up.rolling(30, min_periods=30).sum() / 30.0
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpzigzag_45d_slope_v107_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    pk = ((cp.shift(1) > cp.shift(2)) & (cp < cp.shift(1))).astype(float).where(
        cp.notna() & cp.shift(1).notna() & cp.shift(2).notna(), np.nan
    )
    b = pk.rolling(45, min_periods=45).sum() / 45.0
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpdrift_60d_slope_v108_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    b = cp.diff(1).rolling(60, min_periods=60).mean()
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_voldot_30d_slope_v109_signal(closeadj, close, high, low, volume):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    lv = np.log(volume.replace(0.0, np.nan))
    b = (cp - 0.5).rolling(30, min_periods=15).corr(lv)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cphivol_40d_slope_v110_signal(closeadj, close, high, low, volume):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    med = volume.rolling(40, min_periods=20).median()
    big = cp.where(volume > med)
    b = big.rolling(40, min_periods=15).mean()
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cplowvol_40d_slope_v111_signal(closeadj, close, high, low, volume):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    med = volume.rolling(40, min_periods=20).median()
    small = cp.where(volume <= med)
    b = small.rolling(40, min_periods=15).mean()
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpcondvret_50d_slope_v112_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    r = close.pct_change()
    up = cp.where(r > 0)
    dn = cp.where(r < 0)
    b = up.rolling(50, min_periods=20).mean() - dn.rolling(50, min_periods=20).mean()
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpgap_30d_slope_v113_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    prev_c = close.shift(1)
    up_gap = cp.where(low > prev_c)
    dn_gap = cp.where(high < prev_c)
    b = up_gap.rolling(30, min_periods=10).mean() - dn_gap.rolling(30, min_periods=10).mean()
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpwgttd_50d_slope_v114_signal(closeadj, close, high, low):
    rngraw = high - low
    rng = rngraw.replace(0.0, np.nan)
    cp = (close - low) / rng
    num = ((cp - 0.5) * rngraw).rolling(50, min_periods=50).sum()
    den = rngraw.rolling(50, min_periods=50).sum().replace(0.0, np.nan)
    b = num / den
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpvar_15d_slope_v115_signal(close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    b = cp.rolling(15, min_periods=15).var()
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpskewsg_30d_slope_v116_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    sk = cp.rolling(30, min_periods=30).skew()
    b = np.sign(sk).where(sk.notna(), np.nan)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpkurtsg_50d_slope_v117_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    k = cp.rolling(50, min_periods=50).kurt()
    b = np.sign(k).where(k.notna(), np.nan)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpmadrel_40d_slope_v118_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    med = cp.rolling(40, min_periods=40).median()
    mad = (cp - med).abs().rolling(40, min_periods=40).mean()
    iqr = (cp.rolling(40, min_periods=20).quantile(0.75) - cp.rolling(40, min_periods=20).quantile(0.25)).replace(0.0, np.nan)
    b = mad / iqr
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpcv_50d_slope_v119_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    m = cp.rolling(50, min_periods=50).mean().replace(0.0, np.nan)
    sd = cp.rolling(50, min_periods=50).std()
    b = sd / m
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpoctile_75d_slope_v120_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    rk = cp.rolling(75, min_periods=38).rank(pct=True)
    oct_ = np.ceil(rk * 8.0).where(rk.notna(), np.nan)
    b = oct_ - 4.5
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpac3_70d_slope_v121_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    b = cp.rolling(70, min_periods=35).corr(cp.shift(3))
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpac10_100d_slope_v122_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    b = cp.rolling(100, min_periods=50).corr(cp.shift(10))
    return b.diff(63).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_revpatlo_45d_slope_v123_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    pat = ((cp.shift(1) < 0.3) & (cp > 0.7)).astype(float).where(
        cp.notna() & cp.shift(1).notna(), np.nan
    )
    b = pat.rolling(45, min_periods=45).sum() / 45.0
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_threein_40d_slope_v124_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    flag = ((cp >= 0.4) & (cp <= 0.6)).astype(float).where(cp.notna(), np.nan)
    triple = (flag * flag.shift(1) * flag.shift(2)).where(
        flag.notna() & flag.shift(1).notna() & flag.shift(2).notna(), np.nan
    )
    b = triple.rolling(40, min_periods=40).sum() / 40.0
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpparity_30d_slope_v125_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    idx = pd.Series(np.arange(len(cp)), index=cp.index, dtype=float)
    even = cp.where(idx % 2 == 0)
    odd = cp.where(idx % 2 == 1)
    b = even.rolling(30, min_periods=15).mean() - odd.rolling(30, min_periods=15).mean()
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpsd2bar_50d_slope_v126_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    sm = (cp + cp.shift(1)) / 2.0
    b = sm.rolling(50, min_periods=50).std()
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_prevrngavg_20d_slope_v127_signal(close, high, low):
    prng = (high.shift(1) - low.shift(1)).replace(0.0, np.nan)
    p = (close - low.shift(1)) / prng
    b = p.rolling(20, min_periods=20).mean()
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_prevrngabv_30d_slope_v128_signal(closeadj, close, high, low):
    above = (close > high.shift(1)).astype(float).where(close.shift(1).notna(), np.nan)
    b = above.rolling(30, min_periods=30).sum() / 30.0
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_prevrngblw_30d_slope_v129_signal(closeadj, close, high, low):
    below = (close < low.shift(1)).astype(float).where(close.shift(1).notna(), np.nan)
    b = below.rolling(30, min_periods=30).sum() / 30.0
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_2barhilo_50d_slope_v130_signal(closeadj, close, high, low):
    h2 = high.rolling(2, min_periods=2).max()
    l2 = low.rolling(2, min_periods=2).min()
    pp = (close - l2) / (h2 - l2).replace(0.0, np.nan)
    b = pp.rolling(50, min_periods=50).mean()
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_3barhilo_30d_slope_v131_signal(closeadj, close, high, low):
    h3 = high.rolling(3, min_periods=3).max()
    l3 = low.rolling(3, min_periods=3).min()
    pp = (close - l3) / (h3 - l3).replace(0.0, np.nan)
    b = pp.rolling(30, min_periods=30).std()
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpregr_25d_slope_v132_signal(close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng

    b = cp.rolling(25, min_periods=25).apply(_ols_slope, raw=True)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpr2_40d_slope_v133_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng

    b = cp.rolling(40, min_periods=40).apply(_ols_r2, raw=True)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cphurst_80d_slope_v134_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng

    b = cp.rolling(80, min_periods=40).apply(_hurst_rs, raw=True)
    return b.diff(63).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpdrawup_60d_slope_v135_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    cum = (cp - 0.5).cumsum()
    drawup = cum - cum.rolling(60, min_periods=60).min()
    b = drawup / 60.0
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpdrawdn_60d_slope_v136_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    cum = (cp - 0.5).cumsum()
    drawdn = cum.rolling(60, min_periods=60).max() - cum
    b = drawdn / 60.0
    return b.diff(63).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpsharpe_45d_slope_v137_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    m = (cp - 0.5).rolling(45, min_periods=45).mean()
    sd = cp.rolling(45, min_periods=45).std().replace(0.0, np.nan)
    b = m / sd
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpvxret_30d_slope_v138_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    r = close.pct_change()
    b = cp.rolling(30, min_periods=15).corr(r)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpvxnret_25d_slope_v139_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    rfwd = close.pct_change().shift(-1)
    b = cp.rolling(25, min_periods=15).corr(rfwd)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpemavar_40d_slope_v140_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    b = cp.ewm(span=20, adjust=False, min_periods=20).var()
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpsignmom_45d_slope_v141_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    s = np.sign(cp - 0.5).where(cp.notna(), np.nan)
    b = s.rolling(45, min_periods=45).mean()
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpvolclip_60d_slope_v142_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    clipped = (cp - 0.5).clip(-0.25, 0.25)
    b = clipped.rolling(60, min_periods=60).mean()
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_midcross_50d_slope_v143_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    s = np.sign(cp - 0.5)
    cross = (s != s.shift(1)).astype(float).where(s.notna() & s.shift(1).notna(), np.nan)
    b = cross.rolling(50, min_periods=50).sum() / 50.0
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_clipupsum_25d_slope_v144_signal(close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    score = (cp - 0.7).clip(lower=0.0).where(cp.notna(), np.nan)
    b = score.rolling(25, min_periods=25).mean()
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_clipdnsum_25d_slope_v145_signal(close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    score = (0.3 - cp).clip(lower=0.0).where(cp.notna(), np.nan)
    b = score.rolling(25, min_periods=25).mean()
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_extremes_70d_slope_v146_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    hi = (cp > 0.9).astype(float).where(cp.notna(), np.nan)
    lo = (cp < 0.1).astype(float).where(cp.notna(), np.nan)
    b = (hi - lo).rolling(70, min_periods=70).sum() / 70.0
    return b.diff(63).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_csmix_30d_slope_v147_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    r = close.pct_change()
    s = np.sign(r)
    b = (cp * s).rolling(30, min_periods=30).mean()
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_csmix_lo_30d_slope_v148_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    r = close.pct_change()
    mask = (r < 0).astype(float).where(r.notna(), np.nan)
    b = ((1.0 - cp) * mask).rolling(30, min_periods=30).mean()
    return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpprdsign_45d_slope_v149_signal(closeadj, close, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out_vals = ((close > close.shift(1)) & (cp > 0.6)).astype(float).where(cp.notna(), np.nan)
    b = out_vals.rolling(45, min_periods=45).sum() / 45.0
    return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f09cp_f09_close_position_within_range_cpcorrop_40d_slope_v150_signal(closeadj, close, open, high, low):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    op = (open - low) / rng
    b = cp.rolling(40, min_periods=20).corr(op)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def _e(fn, *inputs):
    return fn.__name__, {"inputs": list(inputs), "func": fn}

f09_close_position_within_range_slope_001_150_REGISTRY = dict([
    _e(f09cp_f09_close_position_within_range_cpdisp_1d_slope_v002_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpprior_1d_slope_v004_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_logodds_1d_slope_v005_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpop_1d_slope_v006_signal, "close", "open", "high", "low"),
    _e(f09cp_f09_close_position_within_range_op_1d_slope_v007_signal, "open", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpopabs_5d_slope_v008_signal, "close", "open", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpopsgn_10d_slope_v009_signal, "close", "open", "high", "low"),
    _e(f09cp_f09_close_position_within_range_oppos_21d_slope_v010_signal, "open", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpmean_5d_slope_v011_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpmean_21d_slope_v012_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpmed_63d_slope_v013_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpstd_21d_slope_v014_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpstd_63d_slope_v015_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpskew_42d_slope_v016_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpkurt_50d_slope_v017_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpmax_15d_slope_v018_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpmin_30d_slope_v019_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cprange_45d_slope_v020_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_hicnt_20d_slope_v021_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_locnt_30d_slope_v022_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_hilodif_40d_slope_v023_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_extrhi_50d_slope_v024_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_extrlo_50d_slope_v025_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_midcnt_60d_slope_v026_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_hilorat_30d_slope_v027_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_consechi_10d_slope_v028_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_streakhi_15d_slope_v029_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_streaklo_15d_slope_v030_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_dayssincehi_50d_slope_v031_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_dayssincelo_50d_slope_v032_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_midstreak_15d_slope_v033_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_flipfreq_30d_slope_v034_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpdiff_1d_slope_v035_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpdiff_5d_slope_v036_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpchgabs_10d_slope_v037_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpchgsgn_20d_slope_v038_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpaccdir_15d_slope_v039_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpslope_30d_slope_v040_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_volwcp_21d_slope_v041_signal, "close", "high", "low", "volume"),
    _e(f09cp_f09_close_position_within_range_rngwcp_30d_slope_v042_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_dollwcp_40d_slope_v043_signal, "closeadj", "close", "high", "low", "volume"),
    _e(f09cp_f09_close_position_within_range_expwcp_10d_slope_v044_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_expwcp_50d_slope_v045_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_trimcp_30d_slope_v046_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_disprk_60d_slope_v047_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpabsdrk_120d_slope_v048_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpmidvol_30d_slope_v049_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpd10zsc_90d_slope_v050_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpiqr_50d_slope_v051_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpquint_30d_slope_v052_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_midabs_5d_slope_v053_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_midabs_50d_slope_v054_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_asymabs_20d_slope_v055_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_tdvol_30d_slope_v056_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_topdistabs_45d_slope_v057_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_extrabs_30d_slope_v058_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpxabsret_15d_slope_v059_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpxret_25d_slope_v060_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cphighrng_20d_slope_v061_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cplowrng_20d_slope_v062_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpcondvol_30d_slope_v063_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpac1_60d_slope_v064_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpac5_80d_slope_v065_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_three_hi_25d_slope_v066_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_three_lo_25d_slope_v067_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpspan_5d_slope_v069_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpcormid_40d_slope_v070_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_revpat_30d_slope_v071_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_dispsma_25d_slope_v072_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpvolvscp_45d_slope_v073_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpregr_50d_slope_v074_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpmad_35d_slope_v075_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_sinpi_1d_slope_v076_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpsmallrng_1d_slope_v077_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cubed_1d_slope_v078_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_relu_top_1d_slope_v079_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_relu_bot_1d_slope_v080_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpwma_15d_slope_v081_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpgeo_30d_slope_v082_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cphar_25d_slope_v083_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpqr10_50d_slope_v084_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpqr90_50d_slope_v085_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpq90mid_60d_slope_v086_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpmedabs_45d_slope_v087_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpentropy_60d_slope_v088_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_q60cnt_30d_slope_v089_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_q40cnt_30d_slope_v090_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_q80cnt_60d_slope_v091_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_q20cnt_60d_slope_v092_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_topbal_40d_slope_v093_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_extrhi_10d_slope_v094_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_extrlo_10d_slope_v095_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_inside_70d_slope_v096_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_streakextrhi_20d_slope_v097_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_dayslastflip_30d_slope_v098_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_dayssincextrhi_100d_slope_v099_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_runlen_above_30d_slope_v100_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_runlen_below_30d_slope_v101_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpmom_10d_slope_v102_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpmom_21d_slope_v103_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpaccdir_30d_slope_v104_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpaccel_25d_slope_v105_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpup10_30d_slope_v106_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpzigzag_45d_slope_v107_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpdrift_60d_slope_v108_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_voldot_30d_slope_v109_signal, "closeadj", "close", "high", "low", "volume"),
    _e(f09cp_f09_close_position_within_range_cphivol_40d_slope_v110_signal, "closeadj", "close", "high", "low", "volume"),
    _e(f09cp_f09_close_position_within_range_cplowvol_40d_slope_v111_signal, "closeadj", "close", "high", "low", "volume"),
    _e(f09cp_f09_close_position_within_range_cpcondvret_50d_slope_v112_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpgap_30d_slope_v113_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpwgttd_50d_slope_v114_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpvar_15d_slope_v115_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpskewsg_30d_slope_v116_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpkurtsg_50d_slope_v117_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpmadrel_40d_slope_v118_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpcv_50d_slope_v119_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpoctile_75d_slope_v120_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpac3_70d_slope_v121_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpac10_100d_slope_v122_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_revpatlo_45d_slope_v123_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_threein_40d_slope_v124_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpparity_30d_slope_v125_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpsd2bar_50d_slope_v126_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_prevrngavg_20d_slope_v127_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_prevrngabv_30d_slope_v128_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_prevrngblw_30d_slope_v129_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_2barhilo_50d_slope_v130_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_3barhilo_30d_slope_v131_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpregr_25d_slope_v132_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpr2_40d_slope_v133_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cphurst_80d_slope_v134_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpdrawup_60d_slope_v135_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpdrawdn_60d_slope_v136_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpsharpe_45d_slope_v137_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpvxret_30d_slope_v138_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpvxnret_25d_slope_v139_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpemavar_40d_slope_v140_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpsignmom_45d_slope_v141_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpvolclip_60d_slope_v142_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_midcross_50d_slope_v143_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_clipupsum_25d_slope_v144_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_clipdnsum_25d_slope_v145_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_extremes_70d_slope_v146_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_csmix_30d_slope_v147_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_csmix_lo_30d_slope_v148_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpprdsign_45d_slope_v149_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpcorrop_40d_slope_v150_signal, "closeadj", "close", "open", "high", "low"),
])


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
    for name, entry in f09_close_position_within_range_slope_001_150_REGISTRY.items():
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
    assert max_corr <= 0.95 + 1e-9, f"max pairwise |corr|={max_corr:.4f} exceeds 0.95"
    print(f"OK slope_001_150: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")

if __name__ == "__main__":
    _self_test()
