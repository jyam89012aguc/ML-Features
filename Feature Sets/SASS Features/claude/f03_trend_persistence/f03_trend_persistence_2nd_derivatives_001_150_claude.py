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


def _logret(close):
    return np.log(close.replace(0, np.nan)).diff()


def _eff(close, w):
    net = (close - close.shift(w)).abs()
    path = close.diff().abs().rolling(w, min_periods=max(2, w // 2)).sum()
    return net / path.replace(0, np.nan)


def _seff(close, w):
    net = close - close.shift(w)
    path = close.diff().abs().rolling(w, min_periods=max(2, w // 2)).sum()
    return net / path.replace(0, np.nan)


def _hurst(close, w):
    r = _logret(close)

    def _rs(a):
        a = a[~np.isnan(a)]
        if a.size < 8:
            return np.nan
        y = np.cumsum(a - a.mean())
        R = y.max() - y.min()
        S = a.std()
        if S == 0 or R == 0:
            return np.nan
        return np.log(R / S) / np.log(a.size)

    return r.rolling(w, min_periods=max(8, w // 2)).apply(_rs, raw=True)


def _acf(close, w, lag):
    r = _logret(close)

    def _a(a):
        a = a[~np.isnan(a)]
        if a.size <= lag + 2:
            return np.nan
        x0 = a[:-lag]
        x1 = a[lag:]
        if x0.std() == 0 or x1.std() == 0:
            return np.nan
        return np.corrcoef(x0, x1)[0, 1]

    return r.rolling(w, min_periods=max(lag + 3, w // 2)).apply(_a, raw=True)


def _vr(close, k, w):
    r = _logret(close)
    rk = np.log(close.replace(0, np.nan)).diff(k)
    v1 = r.rolling(w, min_periods=max(k + 2, w // 2)).var()
    vk = rk.rolling(w, min_periods=max(k + 2, w // 2)).var()
    return vk / (k * v1).replace(0, np.nan)


def _cont(close, w):
    r = _logret(close)

    def _c(a):
        a = a[~np.isnan(a)]
        if a.size < 5:
            return np.nan
        w0 = np.abs(a[1:])
        tot = np.sum(w0)
        if tot == 0:
            return np.nan
        same = np.sign(a[1:]) == np.sign(a[:-1])
        return np.sum(w0[same]) / tot

    return r.rolling(w, min_periods=max(5, w // 2)).apply(_c, raw=True)


def _r2(close, w):
    lp = np.log(close.replace(0, np.nan))

    def _f(a):
        a = a[~np.isnan(a)]
        if a.size < max(8, w // 4):
            return np.nan
        x = np.arange(a.size)
        b1 = np.polyfit(x, a, 1)
        pred = b1[0] * x + b1[1]
        sr = np.sum((a - pred) ** 2)
        st = np.sum((a - a.mean()) ** 2)
        if st == 0:
            return np.nan
        return 1.0 - sr / st

    return lp.rolling(w, min_periods=max(8, w // 2)).apply(_f, raw=True)


def _flip(close, w):
    r = _logret(close)

    def _fl(a):
        a = a[~np.isnan(a)]
        if a.size < 4:
            return np.nan
        flips = np.sign(a[1:]) != np.sign(a[:-1])
        cf = np.mean(flips)
        tm = np.mean(np.abs(a))
        if tm == 0:
            return cf
        jit = 0.05 * np.tanh((np.mean(np.abs(a[1:])[flips]) - tm) / tm) if flips.any() else 0.0
        return cf + jit

    return r.rolling(w, min_periods=max(4, w // 2)).apply(_fl, raw=True)


def _dfa(close, w):
    r = _logret(close)

    def _f(a):
        a = a[~np.isnan(a)]
        if a.size < 8:
            return np.nan
        y = np.cumsum(a - a.mean())
        x = np.arange(a.size)
        b = np.polyfit(x, y, 1)
        resid = y - (b[0] * x + b[1])
        return resid.std() / (a.std() * np.sqrt(a.size) + 1e-12)

    return r.rolling(w, min_periods=max(8, w // 2)).apply(_f, raw=True)


def _jumpshare(close, w):
    ar = _logret(close).abs()
    mx = ar.rolling(w, min_periods=max(8, w // 2)).max()
    tot = ar.rolling(w, min_periods=max(8, w // 2)).sum()
    return 1.0 - mx / tot.replace(0, np.nan)


# 5d-ROC slope (1st derivative) of the effr persistence base (42d window)
def f03tp_f03_trend_persistence_effr_42d_slope_v001_signal(closeadj):
    bs = _eff(closeadj, 42)
    d = (bs - bs.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope (1st derivative) of the effr persistence base (63d window)
def f03tp_f03_trend_persistence_effr_63d_slope_v002_signal(closeadj):
    bs = _eff(closeadj, 63)
    d = (bs - bs.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope (1st derivative) of the effr persistence base (126d window)
def f03tp_f03_trend_persistence_effr_126d_slope_v003_signal(closeadj):
    bs = _eff(closeadj, 126)
    d = (bs - bs.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope (1st derivative) of the effr persistence base (189d window)
def f03tp_f03_trend_persistence_effr_189d_slope_v004_signal(closeadj):
    bs = _eff(closeadj, 189)
    d = (bs - bs.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope (1st derivative) of the effr persistence base (252d window)
def f03tp_f03_trend_persistence_effr_252d_slope_v005_signal(closeadj):
    bs = _eff(closeadj, 252)
    d = (bs - bs.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 5d-ROC slope (1st derivative) of the seffr persistence base (42d window)
def f03tp_f03_trend_persistence_seffr_42d_slope_v006_signal(closeadj):
    bs = _seff(closeadj, 42)
    d = (bs - bs.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope (1st derivative) of the seffr persistence base (63d window)
def f03tp_f03_trend_persistence_seffr_63d_slope_v007_signal(closeadj):
    bs = _seff(closeadj, 63)
    d = (bs - bs.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope (1st derivative) of the seffr persistence base (126d window)
def f03tp_f03_trend_persistence_seffr_126d_slope_v008_signal(closeadj):
    bs = _seff(closeadj, 126)
    d = (bs - bs.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope (1st derivative) of the seffr persistence base (189d window)
def f03tp_f03_trend_persistence_seffr_189d_slope_v009_signal(closeadj):
    bs = _seff(closeadj, 189)
    d = (bs - bs.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope (1st derivative) of the seffr persistence base (252d window)
def f03tp_f03_trend_persistence_seffr_252d_slope_v010_signal(closeadj):
    bs = _seff(closeadj, 252)
    d = (bs - bs.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 5d-ROC slope (1st derivative) of the hurst persistence base (42d window)
def f03tp_f03_trend_persistence_hurst_42d_slope_v011_signal(closeadj):
    bs = _hurst(closeadj, 42)
    d = (bs - bs.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope (1st derivative) of the hurst persistence base (63d window)
def f03tp_f03_trend_persistence_hurst_63d_slope_v012_signal(closeadj):
    bs = _hurst(closeadj, 63)
    d = (bs - bs.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope (1st derivative) of the hurst persistence base (126d window)
def f03tp_f03_trend_persistence_hurst_126d_slope_v013_signal(closeadj):
    bs = _hurst(closeadj, 126)
    d = (bs - bs.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope (1st derivative) of the hurst persistence base (189d window)
def f03tp_f03_trend_persistence_hurst_189d_slope_v014_signal(closeadj):
    bs = _hurst(closeadj, 189)
    d = (bs - bs.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope (1st derivative) of the hurst persistence base (252d window)
def f03tp_f03_trend_persistence_hurst_252d_slope_v015_signal(closeadj):
    bs = _hurst(closeadj, 252)
    d = (bs - bs.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 5d-ROC slope (1st derivative) of the acf1 persistence base (42d window)
def f03tp_f03_trend_persistence_acf1_42d_slope_v016_signal(closeadj):
    bs = _acf(closeadj, 42, 1)
    d = (bs - bs.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope (1st derivative) of the acf1 persistence base (63d window)
def f03tp_f03_trend_persistence_acf1_63d_slope_v017_signal(closeadj):
    bs = _acf(closeadj, 63, 1)
    d = (bs - bs.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope (1st derivative) of the acf1 persistence base (126d window)
def f03tp_f03_trend_persistence_acf1_126d_slope_v018_signal(closeadj):
    bs = _acf(closeadj, 126, 1)
    d = (bs - bs.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope (1st derivative) of the acf1 persistence base (189d window)
def f03tp_f03_trend_persistence_acf1_189d_slope_v019_signal(closeadj):
    bs = _acf(closeadj, 189, 1)
    d = (bs - bs.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope (1st derivative) of the acf1 persistence base (252d window)
def f03tp_f03_trend_persistence_acf1_252d_slope_v020_signal(closeadj):
    bs = _acf(closeadj, 252, 1)
    d = (bs - bs.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 5d-ROC slope (1st derivative) of the acf2 persistence base (42d window)
def f03tp_f03_trend_persistence_acf2_42d_slope_v021_signal(closeadj):
    bs = _acf(closeadj, 42, 2)
    d = (bs - bs.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope (1st derivative) of the acf2 persistence base (63d window)
def f03tp_f03_trend_persistence_acf2_63d_slope_v022_signal(closeadj):
    bs = _acf(closeadj, 63, 2)
    d = (bs - bs.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope (1st derivative) of the acf2 persistence base (126d window)
def f03tp_f03_trend_persistence_acf2_126d_slope_v023_signal(closeadj):
    bs = _acf(closeadj, 126, 2)
    d = (bs - bs.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope (1st derivative) of the acf2 persistence base (189d window)
def f03tp_f03_trend_persistence_acf2_189d_slope_v024_signal(closeadj):
    bs = _acf(closeadj, 189, 2)
    d = (bs - bs.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope (1st derivative) of the acf2 persistence base (252d window)
def f03tp_f03_trend_persistence_acf2_252d_slope_v025_signal(closeadj):
    bs = _acf(closeadj, 252, 2)
    d = (bs - bs.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 5d-ROC slope (1st derivative) of the vr5 persistence base (42d window)
def f03tp_f03_trend_persistence_vr5_42d_slope_v026_signal(closeadj):
    bs = _vr(closeadj, 5, 42)
    d = (bs - bs.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope (1st derivative) of the vr5 persistence base (63d window)
def f03tp_f03_trend_persistence_vr5_63d_slope_v027_signal(closeadj):
    bs = _vr(closeadj, 5, 63)
    d = (bs - bs.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope (1st derivative) of the vr5 persistence base (126d window)
def f03tp_f03_trend_persistence_vr5_126d_slope_v028_signal(closeadj):
    bs = _vr(closeadj, 5, 126)
    d = (bs - bs.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope (1st derivative) of the vr5 persistence base (189d window)
def f03tp_f03_trend_persistence_vr5_189d_slope_v029_signal(closeadj):
    bs = _vr(closeadj, 5, 189)
    d = (bs - bs.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope (1st derivative) of the vr5 persistence base (252d window)
def f03tp_f03_trend_persistence_vr5_252d_slope_v030_signal(closeadj):
    bs = _vr(closeadj, 5, 252)
    d = (bs - bs.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 5d-ROC slope (1st derivative) of the vr10 persistence base (42d window)
def f03tp_f03_trend_persistence_vr10_42d_slope_v031_signal(closeadj):
    bs = _vr(closeadj, 10, 42)
    d = (bs - bs.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope (1st derivative) of the vr10 persistence base (63d window)
def f03tp_f03_trend_persistence_vr10_63d_slope_v032_signal(closeadj):
    bs = _vr(closeadj, 10, 63)
    d = (bs - bs.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope (1st derivative) of the vr10 persistence base (126d window)
def f03tp_f03_trend_persistence_vr10_126d_slope_v033_signal(closeadj):
    bs = _vr(closeadj, 10, 126)
    d = (bs - bs.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope (1st derivative) of the vr10 persistence base (189d window)
def f03tp_f03_trend_persistence_vr10_189d_slope_v034_signal(closeadj):
    bs = _vr(closeadj, 10, 189)
    d = (bs - bs.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope (1st derivative) of the vr10 persistence base (252d window)
def f03tp_f03_trend_persistence_vr10_252d_slope_v035_signal(closeadj):
    bs = _vr(closeadj, 10, 252)
    d = (bs - bs.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 5d-ROC slope (1st derivative) of the cont persistence base (42d window)
def f03tp_f03_trend_persistence_cont_42d_slope_v036_signal(closeadj):
    bs = _cont(closeadj, 42)
    d = (bs - bs.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope (1st derivative) of the cont persistence base (63d window)
def f03tp_f03_trend_persistence_cont_63d_slope_v037_signal(closeadj):
    bs = _cont(closeadj, 63)
    d = (bs - bs.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope (1st derivative) of the cont persistence base (126d window)
def f03tp_f03_trend_persistence_cont_126d_slope_v038_signal(closeadj):
    bs = _cont(closeadj, 126)
    d = (bs - bs.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope (1st derivative) of the cont persistence base (189d window)
def f03tp_f03_trend_persistence_cont_189d_slope_v039_signal(closeadj):
    bs = _cont(closeadj, 189)
    d = (bs - bs.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope (1st derivative) of the cont persistence base (252d window)
def f03tp_f03_trend_persistence_cont_252d_slope_v040_signal(closeadj):
    bs = _cont(closeadj, 252)
    d = (bs - bs.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 5d-ROC slope (1st derivative) of the r2 persistence base (42d window)
def f03tp_f03_trend_persistence_r2_42d_slope_v041_signal(closeadj):
    bs = _r2(closeadj, 42)
    d = (bs - bs.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope (1st derivative) of the r2 persistence base (63d window)
def f03tp_f03_trend_persistence_r2_63d_slope_v042_signal(closeadj):
    bs = _r2(closeadj, 63)
    d = (bs - bs.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope (1st derivative) of the r2 persistence base (126d window)
def f03tp_f03_trend_persistence_r2_126d_slope_v043_signal(closeadj):
    bs = _r2(closeadj, 126)
    d = (bs - bs.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope (1st derivative) of the r2 persistence base (189d window)
def f03tp_f03_trend_persistence_r2_189d_slope_v044_signal(closeadj):
    bs = _r2(closeadj, 189)
    d = (bs - bs.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope (1st derivative) of the r2 persistence base (252d window)
def f03tp_f03_trend_persistence_r2_252d_slope_v045_signal(closeadj):
    bs = _r2(closeadj, 252)
    d = (bs - bs.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 5d-ROC slope (1st derivative) of the flip persistence base (42d window)
def f03tp_f03_trend_persistence_flip_42d_slope_v046_signal(closeadj):
    bs = _flip(closeadj, 42)
    d = (bs - bs.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope (1st derivative) of the flip persistence base (63d window)
def f03tp_f03_trend_persistence_flip_63d_slope_v047_signal(closeadj):
    bs = _flip(closeadj, 63)
    d = (bs - bs.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope (1st derivative) of the flip persistence base (126d window)
def f03tp_f03_trend_persistence_flip_126d_slope_v048_signal(closeadj):
    bs = _flip(closeadj, 126)
    d = (bs - bs.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope (1st derivative) of the flip persistence base (189d window)
def f03tp_f03_trend_persistence_flip_189d_slope_v049_signal(closeadj):
    bs = _flip(closeadj, 189)
    d = (bs - bs.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope (1st derivative) of the flip persistence base (252d window)
def f03tp_f03_trend_persistence_flip_252d_slope_v050_signal(closeadj):
    bs = _flip(closeadj, 252)
    d = (bs - bs.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 5d-ROC slope (1st derivative) of the dfa persistence base (42d window)
def f03tp_f03_trend_persistence_dfa_42d_slope_v051_signal(closeadj):
    bs = _dfa(closeadj, 42)
    d = (bs - bs.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope (1st derivative) of the dfa persistence base (63d window)
def f03tp_f03_trend_persistence_dfa_63d_slope_v052_signal(closeadj):
    bs = _dfa(closeadj, 63)
    d = (bs - bs.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope (1st derivative) of the dfa persistence base (126d window)
def f03tp_f03_trend_persistence_dfa_126d_slope_v053_signal(closeadj):
    bs = _dfa(closeadj, 126)
    d = (bs - bs.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope (1st derivative) of the dfa persistence base (189d window)
def f03tp_f03_trend_persistence_dfa_189d_slope_v054_signal(closeadj):
    bs = _dfa(closeadj, 189)
    d = (bs - bs.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope (1st derivative) of the dfa persistence base (252d window)
def f03tp_f03_trend_persistence_dfa_252d_slope_v055_signal(closeadj):
    bs = _dfa(closeadj, 252)
    d = (bs - bs.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 5d-ROC slope (1st derivative) of the jump persistence base (42d window)
def f03tp_f03_trend_persistence_jump_42d_slope_v056_signal(closeadj):
    bs = _jumpshare(closeadj, 42)
    d = (bs - bs.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope (1st derivative) of the jump persistence base (63d window)
def f03tp_f03_trend_persistence_jump_63d_slope_v057_signal(closeadj):
    bs = _jumpshare(closeadj, 63)
    d = (bs - bs.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope (1st derivative) of the jump persistence base (126d window)
def f03tp_f03_trend_persistence_jump_126d_slope_v058_signal(closeadj):
    bs = _jumpshare(closeadj, 126)
    d = (bs - bs.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope (1st derivative) of the jump persistence base (189d window)
def f03tp_f03_trend_persistence_jump_189d_slope_v059_signal(closeadj):
    bs = _jumpshare(closeadj, 189)
    d = (bs - bs.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope (1st derivative) of the jump persistence base (252d window)
def f03tp_f03_trend_persistence_jump_252d_slope_v060_signal(closeadj):
    bs = _jumpshare(closeadj, 252)
    d = (bs - bs.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 5d-ROC slope (1st derivative) of the effz persistence base (42d window)
def f03tp_f03_trend_persistence_effz_42d_slope_v061_signal(closeadj):
    bs = _z(_eff(closeadj, 42), 42)
    d = (bs - bs.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope (1st derivative) of the effz persistence base (63d window)
def f03tp_f03_trend_persistence_effz_63d_slope_v062_signal(closeadj):
    bs = _z(_eff(closeadj, 63), 63)
    d = (bs - bs.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope (1st derivative) of the effz persistence base (126d window)
def f03tp_f03_trend_persistence_effz_126d_slope_v063_signal(closeadj):
    bs = _z(_eff(closeadj, 126), 126)
    d = (bs - bs.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope (1st derivative) of the effz persistence base (189d window)
def f03tp_f03_trend_persistence_effz_189d_slope_v064_signal(closeadj):
    bs = _z(_eff(closeadj, 189), 189)
    d = (bs - bs.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope (1st derivative) of the effz persistence base (252d window)
def f03tp_f03_trend_persistence_effz_252d_slope_v065_signal(closeadj):
    bs = _z(_eff(closeadj, 252), 252)
    d = (bs - bs.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 5d-ROC slope (1st derivative) of the vr21 persistence base (42d window)
def f03tp_f03_trend_persistence_vr21_42d_slope_v066_signal(closeadj):
    bs = _vr(closeadj, 21, 42)
    d = (bs - bs.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope (1st derivative) of the vr21 persistence base (63d window)
def f03tp_f03_trend_persistence_vr21_63d_slope_v067_signal(closeadj):
    bs = _vr(closeadj, 21, 63)
    d = (bs - bs.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope (1st derivative) of the vr21 persistence base (126d window)
def f03tp_f03_trend_persistence_vr21_126d_slope_v068_signal(closeadj):
    bs = _vr(closeadj, 21, 126)
    d = (bs - bs.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope (1st derivative) of the vr21 persistence base (189d window)
def f03tp_f03_trend_persistence_vr21_189d_slope_v069_signal(closeadj):
    bs = _vr(closeadj, 21, 189)
    d = (bs - bs.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope (1st derivative) of the vr21 persistence base (252d window)
def f03tp_f03_trend_persistence_vr21_252d_slope_v070_signal(closeadj):
    bs = _vr(closeadj, 21, 252)
    d = (bs - bs.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 5d-ROC slope (1st derivative) of the acf5 persistence base (42d window)
def f03tp_f03_trend_persistence_acf5_42d_slope_v071_signal(closeadj):
    bs = _acf(closeadj, 42, 5)
    d = (bs - bs.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope (1st derivative) of the acf5 persistence base (63d window)
def f03tp_f03_trend_persistence_acf5_63d_slope_v072_signal(closeadj):
    bs = _acf(closeadj, 63, 5)
    d = (bs - bs.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope (1st derivative) of the acf5 persistence base (126d window)
def f03tp_f03_trend_persistence_acf5_126d_slope_v073_signal(closeadj):
    bs = _acf(closeadj, 126, 5)
    d = (bs - bs.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope (1st derivative) of the acf5 persistence base (189d window)
def f03tp_f03_trend_persistence_acf5_189d_slope_v074_signal(closeadj):
    bs = _acf(closeadj, 189, 5)
    d = (bs - bs.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope (1st derivative) of the acf5 persistence base (252d window)
def f03tp_f03_trend_persistence_acf5_252d_slope_v075_signal(closeadj):
    bs = _acf(closeadj, 252, 5)
    d = (bs - bs.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 5d-ROC slope of the EMA-smoothed effr persistence base (42d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_effrs_42d_slope_v076_signal(closeadj):
    bs = _eff(closeadj, 42)
    sm = bs.ewm(span=15, min_periods=max(3, 15 // 2)).mean()
    d = (sm - sm.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope of the EMA-smoothed effr persistence base (63d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_effrs_63d_slope_v077_signal(closeadj):
    bs = _eff(closeadj, 63)
    sm = bs.ewm(span=63, min_periods=max(3, 63 // 2)).mean()
    d = (sm - sm.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope of the EMA-smoothed effr persistence base (126d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_effrs_126d_slope_v078_signal(closeadj):
    bs = _eff(closeadj, 126)
    sm = bs.ewm(span=63, min_periods=max(3, 63 // 2)).mean()
    d = (sm - sm.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope of the EMA-smoothed effr persistence base (189d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_effrs_189d_slope_v079_signal(closeadj):
    bs = _eff(closeadj, 189)
    sm = bs.ewm(span=189, min_periods=max(3, 189 // 2)).mean()
    d = (sm - sm.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope of the EMA-smoothed effr persistence base (252d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_effrs_252d_slope_v080_signal(closeadj):
    bs = _eff(closeadj, 252)
    sm = bs.ewm(span=189, min_periods=max(3, 189 // 2)).mean()
    d = (sm - sm.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 5d-ROC slope of the EMA-smoothed seffr persistence base (42d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_seffrs_42d_slope_v081_signal(closeadj):
    bs = _seff(closeadj, 42)
    sm = bs.ewm(span=15, min_periods=max(3, 15 // 2)).mean()
    d = (sm - sm.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope of the EMA-smoothed seffr persistence base (63d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_seffrs_63d_slope_v082_signal(closeadj):
    bs = _seff(closeadj, 63)
    sm = bs.ewm(span=63, min_periods=max(3, 63 // 2)).mean()
    d = (sm - sm.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope of the EMA-smoothed seffr persistence base (126d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_seffrs_126d_slope_v083_signal(closeadj):
    bs = _seff(closeadj, 126)
    sm = bs.ewm(span=63, min_periods=max(3, 63 // 2)).mean()
    d = (sm - sm.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope of the EMA-smoothed seffr persistence base (189d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_seffrs_189d_slope_v084_signal(closeadj):
    bs = _seff(closeadj, 189)
    sm = bs.ewm(span=189, min_periods=max(3, 189 // 2)).mean()
    d = (sm - sm.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope of the EMA-smoothed seffr persistence base (252d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_seffrs_252d_slope_v085_signal(closeadj):
    bs = _seff(closeadj, 252)
    sm = bs.ewm(span=189, min_periods=max(3, 189 // 2)).mean()
    d = (sm - sm.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 5d-ROC slope of the EMA-smoothed hurst persistence base (42d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_hursts_42d_slope_v086_signal(closeadj):
    bs = _hurst(closeadj, 42)
    sm = bs.ewm(span=15, min_periods=max(3, 15 // 2)).mean()
    d = (sm - sm.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope of the EMA-smoothed hurst persistence base (63d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_hursts_63d_slope_v087_signal(closeadj):
    bs = _hurst(closeadj, 63)
    sm = bs.ewm(span=63, min_periods=max(3, 63 // 2)).mean()
    d = (sm - sm.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope of the EMA-smoothed hurst persistence base (126d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_hursts_126d_slope_v088_signal(closeadj):
    bs = _hurst(closeadj, 126)
    sm = bs.ewm(span=63, min_periods=max(3, 63 // 2)).mean()
    d = (sm - sm.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope of the EMA-smoothed hurst persistence base (189d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_hursts_189d_slope_v089_signal(closeadj):
    bs = _hurst(closeadj, 189)
    sm = bs.ewm(span=189, min_periods=max(3, 189 // 2)).mean()
    d = (sm - sm.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope of the EMA-smoothed hurst persistence base (252d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_hursts_252d_slope_v090_signal(closeadj):
    bs = _hurst(closeadj, 252)
    sm = bs.ewm(span=189, min_periods=max(3, 189 // 2)).mean()
    d = (sm - sm.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 5d-ROC slope of the EMA-smoothed acf1 persistence base (42d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_acf1s_42d_slope_v091_signal(closeadj):
    bs = _acf(closeadj, 42, 1)
    sm = bs.ewm(span=15, min_periods=max(3, 15 // 2)).mean()
    d = (sm - sm.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope of the EMA-smoothed acf1 persistence base (63d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_acf1s_63d_slope_v092_signal(closeadj):
    bs = _acf(closeadj, 63, 1)
    sm = bs.ewm(span=63, min_periods=max(3, 63 // 2)).mean()
    d = (sm - sm.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope of the EMA-smoothed acf1 persistence base (126d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_acf1s_126d_slope_v093_signal(closeadj):
    bs = _acf(closeadj, 126, 1)
    sm = bs.ewm(span=63, min_periods=max(3, 63 // 2)).mean()
    d = (sm - sm.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope of the EMA-smoothed acf1 persistence base (189d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_acf1s_189d_slope_v094_signal(closeadj):
    bs = _acf(closeadj, 189, 1)
    sm = bs.ewm(span=189, min_periods=max(3, 189 // 2)).mean()
    d = (sm - sm.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope of the EMA-smoothed acf1 persistence base (252d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_acf1s_252d_slope_v095_signal(closeadj):
    bs = _acf(closeadj, 252, 1)
    sm = bs.ewm(span=189, min_periods=max(3, 189 // 2)).mean()
    d = (sm - sm.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 5d-ROC slope of the EMA-smoothed acf2 persistence base (42d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_acf2s_42d_slope_v096_signal(closeadj):
    bs = _acf(closeadj, 42, 2)
    sm = bs.ewm(span=15, min_periods=max(3, 15 // 2)).mean()
    d = (sm - sm.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope of the EMA-smoothed acf2 persistence base (63d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_acf2s_63d_slope_v097_signal(closeadj):
    bs = _acf(closeadj, 63, 2)
    sm = bs.ewm(span=63, min_periods=max(3, 63 // 2)).mean()
    d = (sm - sm.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope of the EMA-smoothed acf2 persistence base (126d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_acf2s_126d_slope_v098_signal(closeadj):
    bs = _acf(closeadj, 126, 2)
    sm = bs.ewm(span=63, min_periods=max(3, 63 // 2)).mean()
    d = (sm - sm.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope of the EMA-smoothed acf2 persistence base (189d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_acf2s_189d_slope_v099_signal(closeadj):
    bs = _acf(closeadj, 189, 2)
    sm = bs.ewm(span=189, min_periods=max(3, 189 // 2)).mean()
    d = (sm - sm.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope of the EMA-smoothed acf2 persistence base (252d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_acf2s_252d_slope_v100_signal(closeadj):
    bs = _acf(closeadj, 252, 2)
    sm = bs.ewm(span=189, min_periods=max(3, 189 // 2)).mean()
    d = (sm - sm.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 5d-ROC slope of the EMA-smoothed vr5 persistence base (42d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_vr5s_42d_slope_v101_signal(closeadj):
    bs = _vr(closeadj, 5, 42)
    sm = bs.ewm(span=15, min_periods=max(3, 15 // 2)).mean()
    d = (sm - sm.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope of the EMA-smoothed vr5 persistence base (63d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_vr5s_63d_slope_v102_signal(closeadj):
    bs = _vr(closeadj, 5, 63)
    sm = bs.ewm(span=63, min_periods=max(3, 63 // 2)).mean()
    d = (sm - sm.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope of the EMA-smoothed vr5 persistence base (126d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_vr5s_126d_slope_v103_signal(closeadj):
    bs = _vr(closeadj, 5, 126)
    sm = bs.ewm(span=63, min_periods=max(3, 63 // 2)).mean()
    d = (sm - sm.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope of the EMA-smoothed vr5 persistence base (189d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_vr5s_189d_slope_v104_signal(closeadj):
    bs = _vr(closeadj, 5, 189)
    sm = bs.ewm(span=189, min_periods=max(3, 189 // 2)).mean()
    d = (sm - sm.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope of the EMA-smoothed vr5 persistence base (252d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_vr5s_252d_slope_v105_signal(closeadj):
    bs = _vr(closeadj, 5, 252)
    sm = bs.ewm(span=189, min_periods=max(3, 189 // 2)).mean()
    d = (sm - sm.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 5d-ROC slope of the EMA-smoothed vr10 persistence base (42d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_vr10s_42d_slope_v106_signal(closeadj):
    bs = _vr(closeadj, 10, 42)
    sm = bs.ewm(span=15, min_periods=max(3, 15 // 2)).mean()
    d = (sm - sm.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope of the EMA-smoothed vr10 persistence base (63d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_vr10s_63d_slope_v107_signal(closeadj):
    bs = _vr(closeadj, 10, 63)
    sm = bs.ewm(span=63, min_periods=max(3, 63 // 2)).mean()
    d = (sm - sm.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope of the EMA-smoothed vr10 persistence base (126d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_vr10s_126d_slope_v108_signal(closeadj):
    bs = _vr(closeadj, 10, 126)
    sm = bs.ewm(span=63, min_periods=max(3, 63 // 2)).mean()
    d = (sm - sm.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope of the EMA-smoothed vr10 persistence base (189d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_vr10s_189d_slope_v109_signal(closeadj):
    bs = _vr(closeadj, 10, 189)
    sm = bs.ewm(span=189, min_periods=max(3, 189 // 2)).mean()
    d = (sm - sm.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope of the EMA-smoothed vr10 persistence base (252d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_vr10s_252d_slope_v110_signal(closeadj):
    bs = _vr(closeadj, 10, 252)
    sm = bs.ewm(span=189, min_periods=max(3, 189 // 2)).mean()
    d = (sm - sm.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 5d-ROC slope of the EMA-smoothed cont persistence base (42d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_conts_42d_slope_v111_signal(closeadj):
    bs = _cont(closeadj, 42)
    sm = bs.ewm(span=15, min_periods=max(3, 15 // 2)).mean()
    d = (sm - sm.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope of the EMA-smoothed cont persistence base (63d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_conts_63d_slope_v112_signal(closeadj):
    bs = _cont(closeadj, 63)
    sm = bs.ewm(span=63, min_periods=max(3, 63 // 2)).mean()
    d = (sm - sm.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope of the EMA-smoothed cont persistence base (126d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_conts_126d_slope_v113_signal(closeadj):
    bs = _cont(closeadj, 126)
    sm = bs.ewm(span=63, min_periods=max(3, 63 // 2)).mean()
    d = (sm - sm.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope of the EMA-smoothed cont persistence base (189d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_conts_189d_slope_v114_signal(closeadj):
    bs = _cont(closeadj, 189)
    sm = bs.ewm(span=189, min_periods=max(3, 189 // 2)).mean()
    d = (sm - sm.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope of the EMA-smoothed cont persistence base (252d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_conts_252d_slope_v115_signal(closeadj):
    bs = _cont(closeadj, 252)
    sm = bs.ewm(span=189, min_periods=max(3, 189 // 2)).mean()
    d = (sm - sm.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 5d-ROC slope of the EMA-smoothed r2 persistence base (42d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_r2s_42d_slope_v116_signal(closeadj):
    bs = _r2(closeadj, 42)
    sm = bs.ewm(span=15, min_periods=max(3, 15 // 2)).mean()
    d = (sm - sm.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope of the EMA-smoothed r2 persistence base (63d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_r2s_63d_slope_v117_signal(closeadj):
    bs = _r2(closeadj, 63)
    sm = bs.ewm(span=63, min_periods=max(3, 63 // 2)).mean()
    d = (sm - sm.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope of the EMA-smoothed r2 persistence base (126d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_r2s_126d_slope_v118_signal(closeadj):
    bs = _r2(closeadj, 126)
    sm = bs.ewm(span=63, min_periods=max(3, 63 // 2)).mean()
    d = (sm - sm.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope of the EMA-smoothed r2 persistence base (189d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_r2s_189d_slope_v119_signal(closeadj):
    bs = _r2(closeadj, 189)
    sm = bs.ewm(span=189, min_periods=max(3, 189 // 2)).mean()
    d = (sm - sm.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope of the EMA-smoothed r2 persistence base (252d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_r2s_252d_slope_v120_signal(closeadj):
    bs = _r2(closeadj, 252)
    sm = bs.ewm(span=189, min_periods=max(3, 189 // 2)).mean()
    d = (sm - sm.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 5d-ROC slope of the EMA-smoothed flip persistence base (42d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_flips_42d_slope_v121_signal(closeadj):
    bs = _flip(closeadj, 42)
    sm = bs.ewm(span=15, min_periods=max(3, 15 // 2)).mean()
    d = (sm - sm.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope of the EMA-smoothed flip persistence base (63d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_flips_63d_slope_v122_signal(closeadj):
    bs = _flip(closeadj, 63)
    sm = bs.ewm(span=63, min_periods=max(3, 63 // 2)).mean()
    d = (sm - sm.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope of the EMA-smoothed flip persistence base (126d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_flips_126d_slope_v123_signal(closeadj):
    bs = _flip(closeadj, 126)
    sm = bs.ewm(span=63, min_periods=max(3, 63 // 2)).mean()
    d = (sm - sm.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope of the EMA-smoothed flip persistence base (189d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_flips_189d_slope_v124_signal(closeadj):
    bs = _flip(closeadj, 189)
    sm = bs.ewm(span=189, min_periods=max(3, 189 // 2)).mean()
    d = (sm - sm.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope of the EMA-smoothed flip persistence base (252d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_flips_252d_slope_v125_signal(closeadj):
    bs = _flip(closeadj, 252)
    sm = bs.ewm(span=189, min_periods=max(3, 189 // 2)).mean()
    d = (sm - sm.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 5d-ROC slope of the EMA-smoothed dfa persistence base (42d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_dfas_42d_slope_v126_signal(closeadj):
    bs = _dfa(closeadj, 42)
    sm = bs.ewm(span=15, min_periods=max(3, 15 // 2)).mean()
    d = (sm - sm.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope of the EMA-smoothed dfa persistence base (63d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_dfas_63d_slope_v127_signal(closeadj):
    bs = _dfa(closeadj, 63)
    sm = bs.ewm(span=63, min_periods=max(3, 63 // 2)).mean()
    d = (sm - sm.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope of the EMA-smoothed dfa persistence base (126d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_dfas_126d_slope_v128_signal(closeadj):
    bs = _dfa(closeadj, 126)
    sm = bs.ewm(span=63, min_periods=max(3, 63 // 2)).mean()
    d = (sm - sm.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope of the EMA-smoothed dfa persistence base (189d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_dfas_189d_slope_v129_signal(closeadj):
    bs = _dfa(closeadj, 189)
    sm = bs.ewm(span=189, min_periods=max(3, 189 // 2)).mean()
    d = (sm - sm.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope of the EMA-smoothed dfa persistence base (252d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_dfas_252d_slope_v130_signal(closeadj):
    bs = _dfa(closeadj, 252)
    sm = bs.ewm(span=189, min_periods=max(3, 189 // 2)).mean()
    d = (sm - sm.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 5d-ROC slope of the EMA-smoothed jump persistence base (42d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_jumps_42d_slope_v131_signal(closeadj):
    bs = _jumpshare(closeadj, 42)
    sm = bs.ewm(span=15, min_periods=max(3, 15 // 2)).mean()
    d = (sm - sm.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope of the EMA-smoothed jump persistence base (63d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_jumps_63d_slope_v132_signal(closeadj):
    bs = _jumpshare(closeadj, 63)
    sm = bs.ewm(span=63, min_periods=max(3, 63 // 2)).mean()
    d = (sm - sm.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope of the EMA-smoothed jump persistence base (126d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_jumps_126d_slope_v133_signal(closeadj):
    bs = _jumpshare(closeadj, 126)
    sm = bs.ewm(span=63, min_periods=max(3, 63 // 2)).mean()
    d = (sm - sm.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope of the EMA-smoothed jump persistence base (189d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_jumps_189d_slope_v134_signal(closeadj):
    bs = _jumpshare(closeadj, 189)
    sm = bs.ewm(span=189, min_periods=max(3, 189 // 2)).mean()
    d = (sm - sm.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope of the EMA-smoothed jump persistence base (252d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_jumps_252d_slope_v135_signal(closeadj):
    bs = _jumpshare(closeadj, 252)
    sm = bs.ewm(span=189, min_periods=max(3, 189 // 2)).mean()
    d = (sm - sm.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 5d-ROC slope of the EMA-smoothed effz persistence base (42d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_effzs_42d_slope_v136_signal(closeadj):
    bs = _z(_eff(closeadj, 42), 42)
    sm = bs.ewm(span=15, min_periods=max(3, 15 // 2)).mean()
    d = (sm - sm.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope of the EMA-smoothed effz persistence base (63d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_effzs_63d_slope_v137_signal(closeadj):
    bs = _z(_eff(closeadj, 63), 63)
    sm = bs.ewm(span=63, min_periods=max(3, 63 // 2)).mean()
    d = (sm - sm.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope of the EMA-smoothed effz persistence base (126d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_effzs_126d_slope_v138_signal(closeadj):
    bs = _z(_eff(closeadj, 126), 126)
    sm = bs.ewm(span=63, min_periods=max(3, 63 // 2)).mean()
    d = (sm - sm.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope of the EMA-smoothed effz persistence base (189d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_effzs_189d_slope_v139_signal(closeadj):
    bs = _z(_eff(closeadj, 189), 189)
    sm = bs.ewm(span=189, min_periods=max(3, 189 // 2)).mean()
    d = (sm - sm.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope of the EMA-smoothed effz persistence base (252d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_effzs_252d_slope_v140_signal(closeadj):
    bs = _z(_eff(closeadj, 252), 252)
    sm = bs.ewm(span=189, min_periods=max(3, 189 // 2)).mean()
    d = (sm - sm.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 5d-ROC slope of the EMA-smoothed vr21 persistence base (42d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_vr21s_42d_slope_v141_signal(closeadj):
    bs = _vr(closeadj, 21, 42)
    sm = bs.ewm(span=15, min_periods=max(3, 15 // 2)).mean()
    d = (sm - sm.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope of the EMA-smoothed vr21 persistence base (63d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_vr21s_63d_slope_v142_signal(closeadj):
    bs = _vr(closeadj, 21, 63)
    sm = bs.ewm(span=63, min_periods=max(3, 63 // 2)).mean()
    d = (sm - sm.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope of the EMA-smoothed vr21 persistence base (126d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_vr21s_126d_slope_v143_signal(closeadj):
    bs = _vr(closeadj, 21, 126)
    sm = bs.ewm(span=63, min_periods=max(3, 63 // 2)).mean()
    d = (sm - sm.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope of the EMA-smoothed vr21 persistence base (189d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_vr21s_189d_slope_v144_signal(closeadj):
    bs = _vr(closeadj, 21, 189)
    sm = bs.ewm(span=189, min_periods=max(3, 189 // 2)).mean()
    d = (sm - sm.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope of the EMA-smoothed vr21 persistence base (252d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_vr21s_252d_slope_v145_signal(closeadj):
    bs = _vr(closeadj, 21, 252)
    sm = bs.ewm(span=189, min_periods=max(3, 189 // 2)).mean()
    d = (sm - sm.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 5d-ROC slope of the EMA-smoothed acf5 persistence base (42d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_acf5s_42d_slope_v146_signal(closeadj):
    bs = _acf(closeadj, 42, 5)
    sm = bs.ewm(span=15, min_periods=max(3, 15 // 2)).mean()
    d = (sm - sm.shift(5)) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope of the EMA-smoothed acf5 persistence base (63d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_acf5s_63d_slope_v147_signal(closeadj):
    bs = _acf(closeadj, 63, 5)
    sm = bs.ewm(span=63, min_periods=max(3, 63 // 2)).mean()
    d = (sm - sm.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 21d-ROC slope of the EMA-smoothed acf5 persistence base (126d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_acf5s_126d_slope_v148_signal(closeadj):
    bs = _acf(closeadj, 126, 5)
    sm = bs.ewm(span=63, min_periods=max(3, 63 // 2)).mean()
    d = (sm - sm.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope of the EMA-smoothed acf5 persistence base (189d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_acf5s_189d_slope_v149_signal(closeadj):
    bs = _acf(closeadj, 189, 5)
    sm = bs.ewm(span=189, min_periods=max(3, 189 // 2)).mean()
    d = (sm - sm.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# 63d-ROC slope of the EMA-smoothed acf5 persistence base (252d window); smooth-then-differentiate gives a distinct trajectory
def f03tp_f03_trend_persistence_acf5s_252d_slope_v150_signal(closeadj):
    bs = _acf(closeadj, 252, 5)
    sm = bs.ewm(span=189, min_periods=max(3, 189 // 2)).mean()
    d = (sm - sm.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f03tp_f03_trend_persistence_effr_42d_slope_v001_signal,
    f03tp_f03_trend_persistence_effr_63d_slope_v002_signal,
    f03tp_f03_trend_persistence_effr_126d_slope_v003_signal,
    f03tp_f03_trend_persistence_effr_189d_slope_v004_signal,
    f03tp_f03_trend_persistence_effr_252d_slope_v005_signal,
    f03tp_f03_trend_persistence_seffr_42d_slope_v006_signal,
    f03tp_f03_trend_persistence_seffr_63d_slope_v007_signal,
    f03tp_f03_trend_persistence_seffr_126d_slope_v008_signal,
    f03tp_f03_trend_persistence_seffr_189d_slope_v009_signal,
    f03tp_f03_trend_persistence_seffr_252d_slope_v010_signal,
    f03tp_f03_trend_persistence_hurst_42d_slope_v011_signal,
    f03tp_f03_trend_persistence_hurst_63d_slope_v012_signal,
    f03tp_f03_trend_persistence_hurst_126d_slope_v013_signal,
    f03tp_f03_trend_persistence_hurst_189d_slope_v014_signal,
    f03tp_f03_trend_persistence_hurst_252d_slope_v015_signal,
    f03tp_f03_trend_persistence_acf1_42d_slope_v016_signal,
    f03tp_f03_trend_persistence_acf1_63d_slope_v017_signal,
    f03tp_f03_trend_persistence_acf1_126d_slope_v018_signal,
    f03tp_f03_trend_persistence_acf1_189d_slope_v019_signal,
    f03tp_f03_trend_persistence_acf1_252d_slope_v020_signal,
    f03tp_f03_trend_persistence_acf2_42d_slope_v021_signal,
    f03tp_f03_trend_persistence_acf2_63d_slope_v022_signal,
    f03tp_f03_trend_persistence_acf2_126d_slope_v023_signal,
    f03tp_f03_trend_persistence_acf2_189d_slope_v024_signal,
    f03tp_f03_trend_persistence_acf2_252d_slope_v025_signal,
    f03tp_f03_trend_persistence_vr5_42d_slope_v026_signal,
    f03tp_f03_trend_persistence_vr5_63d_slope_v027_signal,
    f03tp_f03_trend_persistence_vr5_126d_slope_v028_signal,
    f03tp_f03_trend_persistence_vr5_189d_slope_v029_signal,
    f03tp_f03_trend_persistence_vr5_252d_slope_v030_signal,
    f03tp_f03_trend_persistence_vr10_42d_slope_v031_signal,
    f03tp_f03_trend_persistence_vr10_63d_slope_v032_signal,
    f03tp_f03_trend_persistence_vr10_126d_slope_v033_signal,
    f03tp_f03_trend_persistence_vr10_189d_slope_v034_signal,
    f03tp_f03_trend_persistence_vr10_252d_slope_v035_signal,
    f03tp_f03_trend_persistence_cont_42d_slope_v036_signal,
    f03tp_f03_trend_persistence_cont_63d_slope_v037_signal,
    f03tp_f03_trend_persistence_cont_126d_slope_v038_signal,
    f03tp_f03_trend_persistence_cont_189d_slope_v039_signal,
    f03tp_f03_trend_persistence_cont_252d_slope_v040_signal,
    f03tp_f03_trend_persistence_r2_42d_slope_v041_signal,
    f03tp_f03_trend_persistence_r2_63d_slope_v042_signal,
    f03tp_f03_trend_persistence_r2_126d_slope_v043_signal,
    f03tp_f03_trend_persistence_r2_189d_slope_v044_signal,
    f03tp_f03_trend_persistence_r2_252d_slope_v045_signal,
    f03tp_f03_trend_persistence_flip_42d_slope_v046_signal,
    f03tp_f03_trend_persistence_flip_63d_slope_v047_signal,
    f03tp_f03_trend_persistence_flip_126d_slope_v048_signal,
    f03tp_f03_trend_persistence_flip_189d_slope_v049_signal,
    f03tp_f03_trend_persistence_flip_252d_slope_v050_signal,
    f03tp_f03_trend_persistence_dfa_42d_slope_v051_signal,
    f03tp_f03_trend_persistence_dfa_63d_slope_v052_signal,
    f03tp_f03_trend_persistence_dfa_126d_slope_v053_signal,
    f03tp_f03_trend_persistence_dfa_189d_slope_v054_signal,
    f03tp_f03_trend_persistence_dfa_252d_slope_v055_signal,
    f03tp_f03_trend_persistence_jump_42d_slope_v056_signal,
    f03tp_f03_trend_persistence_jump_63d_slope_v057_signal,
    f03tp_f03_trend_persistence_jump_126d_slope_v058_signal,
    f03tp_f03_trend_persistence_jump_189d_slope_v059_signal,
    f03tp_f03_trend_persistence_jump_252d_slope_v060_signal,
    f03tp_f03_trend_persistence_effz_42d_slope_v061_signal,
    f03tp_f03_trend_persistence_effz_63d_slope_v062_signal,
    f03tp_f03_trend_persistence_effz_126d_slope_v063_signal,
    f03tp_f03_trend_persistence_effz_189d_slope_v064_signal,
    f03tp_f03_trend_persistence_effz_252d_slope_v065_signal,
    f03tp_f03_trend_persistence_vr21_42d_slope_v066_signal,
    f03tp_f03_trend_persistence_vr21_63d_slope_v067_signal,
    f03tp_f03_trend_persistence_vr21_126d_slope_v068_signal,
    f03tp_f03_trend_persistence_vr21_189d_slope_v069_signal,
    f03tp_f03_trend_persistence_vr21_252d_slope_v070_signal,
    f03tp_f03_trend_persistence_acf5_42d_slope_v071_signal,
    f03tp_f03_trend_persistence_acf5_63d_slope_v072_signal,
    f03tp_f03_trend_persistence_acf5_126d_slope_v073_signal,
    f03tp_f03_trend_persistence_acf5_189d_slope_v074_signal,
    f03tp_f03_trend_persistence_acf5_252d_slope_v075_signal,
    f03tp_f03_trend_persistence_effrs_42d_slope_v076_signal,
    f03tp_f03_trend_persistence_effrs_63d_slope_v077_signal,
    f03tp_f03_trend_persistence_effrs_126d_slope_v078_signal,
    f03tp_f03_trend_persistence_effrs_189d_slope_v079_signal,
    f03tp_f03_trend_persistence_effrs_252d_slope_v080_signal,
    f03tp_f03_trend_persistence_seffrs_42d_slope_v081_signal,
    f03tp_f03_trend_persistence_seffrs_63d_slope_v082_signal,
    f03tp_f03_trend_persistence_seffrs_126d_slope_v083_signal,
    f03tp_f03_trend_persistence_seffrs_189d_slope_v084_signal,
    f03tp_f03_trend_persistence_seffrs_252d_slope_v085_signal,
    f03tp_f03_trend_persistence_hursts_42d_slope_v086_signal,
    f03tp_f03_trend_persistence_hursts_63d_slope_v087_signal,
    f03tp_f03_trend_persistence_hursts_126d_slope_v088_signal,
    f03tp_f03_trend_persistence_hursts_189d_slope_v089_signal,
    f03tp_f03_trend_persistence_hursts_252d_slope_v090_signal,
    f03tp_f03_trend_persistence_acf1s_42d_slope_v091_signal,
    f03tp_f03_trend_persistence_acf1s_63d_slope_v092_signal,
    f03tp_f03_trend_persistence_acf1s_126d_slope_v093_signal,
    f03tp_f03_trend_persistence_acf1s_189d_slope_v094_signal,
    f03tp_f03_trend_persistence_acf1s_252d_slope_v095_signal,
    f03tp_f03_trend_persistence_acf2s_42d_slope_v096_signal,
    f03tp_f03_trend_persistence_acf2s_63d_slope_v097_signal,
    f03tp_f03_trend_persistence_acf2s_126d_slope_v098_signal,
    f03tp_f03_trend_persistence_acf2s_189d_slope_v099_signal,
    f03tp_f03_trend_persistence_acf2s_252d_slope_v100_signal,
    f03tp_f03_trend_persistence_vr5s_42d_slope_v101_signal,
    f03tp_f03_trend_persistence_vr5s_63d_slope_v102_signal,
    f03tp_f03_trend_persistence_vr5s_126d_slope_v103_signal,
    f03tp_f03_trend_persistence_vr5s_189d_slope_v104_signal,
    f03tp_f03_trend_persistence_vr5s_252d_slope_v105_signal,
    f03tp_f03_trend_persistence_vr10s_42d_slope_v106_signal,
    f03tp_f03_trend_persistence_vr10s_63d_slope_v107_signal,
    f03tp_f03_trend_persistence_vr10s_126d_slope_v108_signal,
    f03tp_f03_trend_persistence_vr10s_189d_slope_v109_signal,
    f03tp_f03_trend_persistence_vr10s_252d_slope_v110_signal,
    f03tp_f03_trend_persistence_conts_42d_slope_v111_signal,
    f03tp_f03_trend_persistence_conts_63d_slope_v112_signal,
    f03tp_f03_trend_persistence_conts_126d_slope_v113_signal,
    f03tp_f03_trend_persistence_conts_189d_slope_v114_signal,
    f03tp_f03_trend_persistence_conts_252d_slope_v115_signal,
    f03tp_f03_trend_persistence_r2s_42d_slope_v116_signal,
    f03tp_f03_trend_persistence_r2s_63d_slope_v117_signal,
    f03tp_f03_trend_persistence_r2s_126d_slope_v118_signal,
    f03tp_f03_trend_persistence_r2s_189d_slope_v119_signal,
    f03tp_f03_trend_persistence_r2s_252d_slope_v120_signal,
    f03tp_f03_trend_persistence_flips_42d_slope_v121_signal,
    f03tp_f03_trend_persistence_flips_63d_slope_v122_signal,
    f03tp_f03_trend_persistence_flips_126d_slope_v123_signal,
    f03tp_f03_trend_persistence_flips_189d_slope_v124_signal,
    f03tp_f03_trend_persistence_flips_252d_slope_v125_signal,
    f03tp_f03_trend_persistence_dfas_42d_slope_v126_signal,
    f03tp_f03_trend_persistence_dfas_63d_slope_v127_signal,
    f03tp_f03_trend_persistence_dfas_126d_slope_v128_signal,
    f03tp_f03_trend_persistence_dfas_189d_slope_v129_signal,
    f03tp_f03_trend_persistence_dfas_252d_slope_v130_signal,
    f03tp_f03_trend_persistence_jumps_42d_slope_v131_signal,
    f03tp_f03_trend_persistence_jumps_63d_slope_v132_signal,
    f03tp_f03_trend_persistence_jumps_126d_slope_v133_signal,
    f03tp_f03_trend_persistence_jumps_189d_slope_v134_signal,
    f03tp_f03_trend_persistence_jumps_252d_slope_v135_signal,
    f03tp_f03_trend_persistence_effzs_42d_slope_v136_signal,
    f03tp_f03_trend_persistence_effzs_63d_slope_v137_signal,
    f03tp_f03_trend_persistence_effzs_126d_slope_v138_signal,
    f03tp_f03_trend_persistence_effzs_189d_slope_v139_signal,
    f03tp_f03_trend_persistence_effzs_252d_slope_v140_signal,
    f03tp_f03_trend_persistence_vr21s_42d_slope_v141_signal,
    f03tp_f03_trend_persistence_vr21s_63d_slope_v142_signal,
    f03tp_f03_trend_persistence_vr21s_126d_slope_v143_signal,
    f03tp_f03_trend_persistence_vr21s_189d_slope_v144_signal,
    f03tp_f03_trend_persistence_vr21s_252d_slope_v145_signal,
    f03tp_f03_trend_persistence_acf5s_42d_slope_v146_signal,
    f03tp_f03_trend_persistence_acf5s_63d_slope_v147_signal,
    f03tp_f03_trend_persistence_acf5s_126d_slope_v148_signal,
    f03tp_f03_trend_persistence_acf5s_189d_slope_v149_signal,
    f03tp_f03_trend_persistence_acf5s_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F03_TREND_PERSISTENCE_REGISTRY_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.005, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.01, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.01, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)) + 1e5, name="volume")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, "%s nunique=%d" % (name, q.nunique())
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

    print("OK f03_trend_persistence_2nd_derivatives_001_150_claude: %d features pass" % n_features)
