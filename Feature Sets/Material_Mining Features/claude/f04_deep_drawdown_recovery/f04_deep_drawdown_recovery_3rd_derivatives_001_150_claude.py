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
    m = s.rolling(w, min_periods=min(252, max(1, w // 2))).mean()
    sd = s.rolling(w, min_periods=min(252, max(1, w // 2))).std()
    return (s - m) / sd.replace(0, np.nan)


def _rmax(s, w):
    return s.rolling(w, min_periods=min(252, max(1, w // 2))).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=min(252, max(1, w // 2))).min()


def _drawdown(close, w):
    peak = close.rolling(w, min_periods=min(252, max(1, w // 2))).max()
    return close / peak.replace(0, np.nan) - 1.0


def _recovery(close, w):
    trough = close.rolling(w, min_periods=min(252, max(1, w // 2))).min()
    return close / trough.replace(0, np.nan) - 1.0


def _ulcer(close, w):
    peak = close.rolling(w, min_periods=min(252, max(1, w // 2))).max()
    dd = close / peak.replace(0, np.nan) - 1.0
    return np.sqrt((dd ** 2).rolling(w, min_periods=min(252, max(1, w // 2))).mean())


def _pain(close, w):
    peak = close.rolling(w, min_periods=min(252, max(1, w // 2))).max()
    dd = close / peak.replace(0, np.nan) - 1.0
    return (-dd).rolling(w, min_periods=min(252, max(1, w // 2))).mean()


def _uwfrac(close, w, thr):
    peak = close.rolling(w, min_periods=min(252, max(1, w // 2))).max()
    uw = close / peak.replace(0, np.nan) - 1.0
    deep = (uw <= thr).astype(float)
    return deep.rolling(w, min_periods=min(252, max(1, w // 2))).mean()


def _recovfrac(close, w):
    peak = _rmax(close, w)
    trough = _rmin(close, w)
    return (close - trough) / (peak - trough).replace(0, np.nan)


def _survmult(close, w):
    trough = _rmin(close, w)
    return close / trough.replace(0, np.nan)


def _semidev(close, w):
    ret = close.pct_change()
    neg = ret.clip(upper=0.0)
    return np.sqrt((neg ** 2).rolling(w, min_periods=min(252, max(1, w // 2))).mean())


def _maxdd(close, w):
    def _f(a):
        run = np.maximum.accumulate(a)
        return np.min(a / run - 1.0)
    return close.rolling(w, min_periods=min(252, max(1, w // 2))).apply(_f, raw=True)


def _logsurv(close, w):
    trough = _rmin(close, w)
    return np.log(close.replace(0, np.nan) / trough.replace(0, np.nan))


def f04dd_f04_deep_drawdown_recovery_dd_50d_jerk_v001_signal(closeadj):
    base = _drawdown(closeadj, 50)
    sl = base.diff(10) / float(10)
    j = sl.diff(10) / float(10)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_dd_50d_jerk_v002_signal(closeadj):
    base = _drawdown(closeadj, 50)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_dd_63d_jerk_v003_signal(closeadj):
    base = _drawdown(closeadj, 63)
    sl = base.diff(5) / float(5)
    j = sl.diff(5) / float(5)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_dd_63d_jerk_v004_signal(closeadj):
    base = _drawdown(closeadj, 63)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_dd_126d_jerk_v005_signal(closeadj):
    base = _drawdown(closeadj, 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_dd_126d_jerk_v006_signal(closeadj):
    base = _drawdown(closeadj, 126)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_dd_252d_jerk_v007_signal(closeadj):
    base = _drawdown(closeadj, 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_dd_252d_jerk_v008_signal(closeadj):
    base = _drawdown(closeadj, 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_dd_504d_jerk_v009_signal(closeadj):
    base = _drawdown(closeadj, 504)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_dd_504d_jerk_v010_signal(closeadj):
    base = _drawdown(closeadj, 504)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_recov_50d_jerk_v011_signal(closeadj):
    base = _recovery(closeadj, 50)
    sl = base.diff(10) / float(10)
    j = sl.diff(10) / float(10)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_recov_50d_jerk_v012_signal(closeadj):
    base = _recovery(closeadj, 50)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_recov_63d_jerk_v013_signal(closeadj):
    base = _recovery(closeadj, 63)
    sl = base.diff(5) / float(5)
    j = sl.diff(5) / float(5)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_recov_63d_jerk_v014_signal(closeadj):
    base = _recovery(closeadj, 63)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_recov_126d_jerk_v015_signal(closeadj):
    base = _recovery(closeadj, 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_recov_126d_jerk_v016_signal(closeadj):
    base = _recovery(closeadj, 126)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_recov_252d_jerk_v017_signal(closeadj):
    base = _recovery(closeadj, 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_recov_252d_jerk_v018_signal(closeadj):
    base = _recovery(closeadj, 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_recov_504d_jerk_v019_signal(closeadj):
    base = _recovery(closeadj, 504)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_recov_504d_jerk_v020_signal(closeadj):
    base = _recovery(closeadj, 504)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_recov_1260d_jerk_v021_signal(closeadj):
    base = _recovery(closeadj, 1260)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_recov_1260d_jerk_v022_signal(closeadj):
    base = _recovery(closeadj, 1260)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_ulcer_50d_jerk_v023_signal(closeadj):
    base = _ulcer(closeadj, 50)
    sl = base.diff(10) / float(10)
    j = sl.diff(10) / float(10)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_ulcer_50d_jerk_v024_signal(closeadj):
    base = _ulcer(closeadj, 50)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_ulcer_63d_jerk_v025_signal(closeadj):
    base = _ulcer(closeadj, 63)
    sl = base.diff(5) / float(5)
    j = sl.diff(5) / float(5)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_ulcer_63d_jerk_v026_signal(closeadj):
    base = _ulcer(closeadj, 63)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_ulcer_126d_jerk_v027_signal(closeadj):
    base = _ulcer(closeadj, 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_ulcer_126d_jerk_v028_signal(closeadj):
    base = _ulcer(closeadj, 126)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_ulcer_252d_jerk_v029_signal(closeadj):
    base = _ulcer(closeadj, 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_ulcer_252d_jerk_v030_signal(closeadj):
    base = _ulcer(closeadj, 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_ulcer_504d_jerk_v031_signal(closeadj):
    base = _ulcer(closeadj, 504)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_ulcer_504d_jerk_v032_signal(closeadj):
    base = _ulcer(closeadj, 504)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_ulcer_1260d_jerk_v033_signal(closeadj):
    base = _ulcer(closeadj, 1260)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_ulcer_1260d_jerk_v034_signal(closeadj):
    base = _ulcer(closeadj, 1260)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_pain_63d_jerk_v035_signal(closeadj):
    base = _pain(closeadj, 63)
    sl = base.diff(5) / float(5)
    j = sl.diff(5) / float(5)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_pain_504d_jerk_v036_signal(closeadj):
    base = _pain(closeadj, 504)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_pain_504d_jerk_v037_signal(closeadj):
    base = _pain(closeadj, 504)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_recovfrac_63d_jerk_v038_signal(closeadj):
    base = _recovfrac(closeadj, 63)
    sl = base.diff(5) / float(5)
    j = sl.diff(5) / float(5)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_recovfrac_63d_jerk_v039_signal(closeadj):
    base = _recovfrac(closeadj, 63)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_recovfrac_126d_jerk_v040_signal(closeadj):
    base = _recovfrac(closeadj, 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_recovfrac_126d_jerk_v041_signal(closeadj):
    base = _recovfrac(closeadj, 126)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_recovfrac_252d_jerk_v042_signal(closeadj):
    base = _recovfrac(closeadj, 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_recovfrac_252d_jerk_v043_signal(closeadj):
    base = _recovfrac(closeadj, 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_uwf10_126d_jerk_v044_signal(closeadj):
    base = _uwfrac(closeadj, 126, -0.10)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_uwf10_126d_jerk_v045_signal(closeadj):
    base = _uwfrac(closeadj, 126, -0.10)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_uwf10_252d_jerk_v046_signal(closeadj):
    base = _uwfrac(closeadj, 252, -0.10)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_uwf10_252d_jerk_v047_signal(closeadj):
    base = _uwfrac(closeadj, 252, -0.10)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_uwf10_504d_jerk_v048_signal(closeadj):
    base = _uwfrac(closeadj, 504, -0.10)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_uwf10_504d_jerk_v049_signal(closeadj):
    base = _uwfrac(closeadj, 504, -0.10)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_uwf10_1260d_jerk_v050_signal(closeadj):
    base = _uwfrac(closeadj, 1260, -0.10)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_uwf10_1260d_jerk_v051_signal(closeadj):
    base = _uwfrac(closeadj, 1260, -0.10)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_uwf25_252d_jerk_v052_signal(closeadj):
    base = _uwfrac(closeadj, 252, -0.25)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_uwf25_1260d_jerk_v053_signal(closeadj):
    base = _uwfrac(closeadj, 1260, -0.25)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_uwf25_1260d_jerk_v054_signal(closeadj):
    base = _uwfrac(closeadj, 1260, -0.25)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_ddz_63d_jerk_v055_signal(closeadj):
    base = _z(_drawdown(closeadj, 63), 63)
    sl = base.diff(5) / float(5)
    j = sl.diff(5) / float(5)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_ddz_63d_jerk_v056_signal(closeadj):
    base = _z(_drawdown(closeadj, 63), 63)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_ddz_126d_jerk_v057_signal(closeadj):
    base = _z(_drawdown(closeadj, 126), 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_ddz_126d_jerk_v058_signal(closeadj):
    base = _z(_drawdown(closeadj, 126), 126)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_ddz_252d_jerk_v059_signal(closeadj):
    base = _z(_drawdown(closeadj, 252), 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_ddz_252d_jerk_v060_signal(closeadj):
    base = _z(_drawdown(closeadj, 252), 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_ddz_504d_jerk_v061_signal(closeadj):
    base = _z(_drawdown(closeadj, 504), 504)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_ddz_504d_jerk_v062_signal(closeadj):
    base = _z(_drawdown(closeadj, 504), 504)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_recovz_63d_jerk_v063_signal(closeadj):
    base = _z(_recovery(closeadj, 63), 63)
    sl = base.diff(5) / float(5)
    j = sl.diff(5) / float(5)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_recovz_63d_jerk_v064_signal(closeadj):
    base = _z(_recovery(closeadj, 63), 63)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_recovz_126d_jerk_v065_signal(closeadj):
    base = _z(_recovery(closeadj, 126), 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_recovz_126d_jerk_v066_signal(closeadj):
    base = _z(_recovery(closeadj, 126), 126)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_recovz_252d_jerk_v067_signal(closeadj):
    base = _z(_recovery(closeadj, 252), 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_recovz_252d_jerk_v068_signal(closeadj):
    base = _z(_recovery(closeadj, 252), 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_recovz_504d_jerk_v069_signal(closeadj):
    base = _z(_recovery(closeadj, 504), 504)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_recovz_504d_jerk_v070_signal(closeadj):
    base = _z(_recovery(closeadj, 504), 504)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_maxdd_63d_jerk_v071_signal(closeadj):
    base = _maxdd(closeadj, 63)
    sl = base.diff(5) / float(5)
    j = sl.diff(5) / float(5)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_maxdd_63d_jerk_v072_signal(closeadj):
    base = _maxdd(closeadj, 63)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_maxdd_126d_jerk_v073_signal(closeadj):
    base = _maxdd(closeadj, 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_maxdd_126d_jerk_v074_signal(closeadj):
    base = _maxdd(closeadj, 126)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_maxdd_252d_jerk_v075_signal(closeadj):
    base = _maxdd(closeadj, 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_maxdd_252d_jerk_v076_signal(closeadj):
    base = _maxdd(closeadj, 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_maxdd_504d_jerk_v077_signal(closeadj):
    base = _maxdd(closeadj, 504)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_maxdd_504d_jerk_v078_signal(closeadj):
    base = _maxdd(closeadj, 504)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_semidev_63d_jerk_v079_signal(closeadj):
    base = _semidev(closeadj, 63)
    sl = base.diff(5) / float(5)
    j = sl.diff(5) / float(5)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_semidev_63d_jerk_v080_signal(closeadj):
    base = _semidev(closeadj, 63)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_semidev_126d_jerk_v081_signal(closeadj):
    base = _semidev(closeadj, 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_semidev_126d_jerk_v082_signal(closeadj):
    base = _semidev(closeadj, 126)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_semidev_252d_jerk_v083_signal(closeadj):
    base = _semidev(closeadj, 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_semidev_252d_jerk_v084_signal(closeadj):
    base = _semidev(closeadj, 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_semidev_504d_jerk_v085_signal(closeadj):
    base = _semidev(closeadj, 504)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_semidev_504d_jerk_v086_signal(closeadj):
    base = _semidev(closeadj, 504)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_logsurv_126d_jerk_v087_signal(closeadj):
    base = _logsurv(closeadj, 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_logsurv_252d_jerk_v088_signal(closeadj):
    base = _logsurv(closeadj, 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_logsurv_252d_jerk_v089_signal(closeadj):
    base = _logsurv(closeadj, 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_logsurv_504d_jerk_v090_signal(closeadj):
    base = _logsurv(closeadj, 504)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_logsurv_504d_jerk_v091_signal(closeadj):
    base = _logsurv(closeadj, 504)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_logsurv_1260d_jerk_v092_signal(closeadj):
    base = _logsurv(closeadj, 1260)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_logsurv_1260d_jerk_v093_signal(closeadj):
    base = _logsurv(closeadj, 1260)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_painz_126d_jerk_v094_signal(closeadj):
    base = _z(_pain(closeadj, 126), 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_painz_126d_jerk_v095_signal(closeadj):
    base = _z(_pain(closeadj, 126), 126)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_painz_252d_jerk_v096_signal(closeadj):
    base = _z(_pain(closeadj, 252), 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_painz_252d_jerk_v097_signal(closeadj):
    base = _z(_pain(closeadj, 252), 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_painz_504d_jerk_v098_signal(closeadj):
    base = _z(_pain(closeadj, 504), 504)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_painz_504d_jerk_v099_signal(closeadj):
    base = _z(_pain(closeadj, 504), 504)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_painz_1260d_jerk_v100_signal(closeadj):
    base = _z(_pain(closeadj, 1260), 1260)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_painz_1260d_jerk_v101_signal(closeadj):
    base = _z(_pain(closeadj, 1260), 1260)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_recovfz_126d_jerk_v102_signal(closeadj):
    base = _z(_recovfrac(closeadj, 126), 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_recovfz_126d_jerk_v103_signal(closeadj):
    base = _z(_recovfrac(closeadj, 126), 126)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_recovfz_252d_jerk_v104_signal(closeadj):
    base = _z(_recovfrac(closeadj, 252), 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_recovfz_252d_jerk_v105_signal(closeadj):
    base = _z(_recovfrac(closeadj, 252), 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_uwf40_252d_jerk_v106_signal(closeadj):
    base = _uwfrac(closeadj, 252, -0.40)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_uwf40_252d_jerk_v107_signal(closeadj):
    base = _uwfrac(closeadj, 252, -0.40)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_uwf40_504d_jerk_v108_signal(closeadj):
    base = _uwfrac(closeadj, 504, -0.40)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_uwf40_1260d_jerk_v109_signal(closeadj):
    base = _uwfrac(closeadj, 1260, -0.40)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_maxddz_126d_jerk_v110_signal(closeadj):
    base = _z(_maxdd(closeadj, 126), 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_maxddz_126d_jerk_v111_signal(closeadj):
    base = _z(_maxdd(closeadj, 126), 126)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_maxddz_252d_jerk_v112_signal(closeadj):
    base = _z(_maxdd(closeadj, 252), 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_maxddz_252d_jerk_v113_signal(closeadj):
    base = _z(_maxdd(closeadj, 252), 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_maxddz_504d_jerk_v114_signal(closeadj):
    base = _z(_maxdd(closeadj, 504), 504)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_maxddz_504d_jerk_v115_signal(closeadj):
    base = _z(_maxdd(closeadj, 504), 504)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_maxddz_1260d_jerk_v116_signal(closeadj):
    base = _z(_maxdd(closeadj, 1260), 1260)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_maxddz_1260d_jerk_v117_signal(closeadj):
    base = _z(_maxdd(closeadj, 1260), 1260)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_ulcerz_126d_jerk_v118_signal(closeadj):
    base = _z(_ulcer(closeadj, 126), 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_ulcerz_126d_jerk_v119_signal(closeadj):
    base = _z(_ulcer(closeadj, 126), 126)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_ulcerz_252d_jerk_v120_signal(closeadj):
    base = _z(_ulcer(closeadj, 252), 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_ulcerz_504d_jerk_v121_signal(closeadj):
    base = _z(_ulcer(closeadj, 504), 504)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_survz_1260d_jerk_v122_signal(closeadj):
    base = _z(_survmult(closeadj, 1260), 1260)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_semidevz_126d_jerk_v123_signal(closeadj):
    base = _z(_semidev(closeadj, 126), 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_semidevz_126d_jerk_v124_signal(closeadj):
    base = _z(_semidev(closeadj, 126), 126)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_semidevz_252d_jerk_v125_signal(closeadj):
    base = _z(_semidev(closeadj, 252), 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_semidevz_252d_jerk_v126_signal(closeadj):
    base = _z(_semidev(closeadj, 252), 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_semidevz_504d_jerk_v127_signal(closeadj):
    base = _z(_semidev(closeadj, 504), 504)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_semidevz_504d_jerk_v128_signal(closeadj):
    base = _z(_semidev(closeadj, 504), 504)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_semidevz_1260d_jerk_v129_signal(closeadj):
    base = _z(_semidev(closeadj, 1260), 1260)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_semidevz_1260d_jerk_v130_signal(closeadj):
    base = _z(_semidev(closeadj, 1260), 1260)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_uwf15_126d_jerk_v131_signal(closeadj):
    base = _uwfrac(closeadj, 126, -0.15)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_uwf15_126d_jerk_v132_signal(closeadj):
    base = _uwfrac(closeadj, 126, -0.15)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_uwf15_252d_jerk_v133_signal(closeadj):
    base = _uwfrac(closeadj, 252, -0.15)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_uwf15_252d_jerk_v134_signal(closeadj):
    base = _uwfrac(closeadj, 252, -0.15)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_logsurvz_504d_jerk_v135_signal(closeadj):
    base = _z(_logsurv(closeadj, 504), 504)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_logsurvz_1260d_jerk_v136_signal(closeadj):
    base = _z(_logsurv(closeadj, 1260), 1260)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_logsurvz_1260d_jerk_v137_signal(closeadj):
    base = _z(_logsurv(closeadj, 1260), 1260)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_painratio_126d_jerk_v138_signal(closeadj):
    base = (_ulcer(closeadj, 126) / _pain(closeadj, 126).replace(0, np.nan))
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_painratio_126d_jerk_v139_signal(closeadj):
    base = (_ulcer(closeadj, 126) / _pain(closeadj, 126).replace(0, np.nan))
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_painratio_252d_jerk_v140_signal(closeadj):
    base = (_ulcer(closeadj, 252) / _pain(closeadj, 252).replace(0, np.nan))
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_painratio_252d_jerk_v141_signal(closeadj):
    base = (_ulcer(closeadj, 252) / _pain(closeadj, 252).replace(0, np.nan))
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_painratio_504d_jerk_v142_signal(closeadj):
    base = (_ulcer(closeadj, 504) / _pain(closeadj, 504).replace(0, np.nan))
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_painratio_504d_jerk_v143_signal(closeadj):
    base = (_ulcer(closeadj, 504) / _pain(closeadj, 504).replace(0, np.nan))
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_recovsd_63d_jerk_v144_signal(closeadj):
    base = (_recovery(closeadj, 63) / _semidev(closeadj, 63).replace(0, np.nan))
    sl = base.diff(5) / float(5)
    j = sl.diff(5) / float(5)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_recovfrac2_126d_jerk_v145_signal(closeadj):
    base = (_recovfrac(closeadj, 126) ** 2)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_recovfrac2_126d_jerk_v146_signal(closeadj):
    base = (_recovfrac(closeadj, 126) ** 2)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_recovfrac2_252d_jerk_v147_signal(closeadj):
    base = (_recovfrac(closeadj, 252) ** 2)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_recovfrac2_252d_jerk_v148_signal(closeadj):
    base = (_recovfrac(closeadj, 252) ** 2)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_recovfrac2_504d_jerk_v149_signal(closeadj):
    base = (_recovfrac(closeadj, 504) ** 2)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


def f04dd_f04_deep_drawdown_recovery_ddsq_126d_jerk_v150_signal(closeadj):
    base = (_drawdown(closeadj, 126) ** 2)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f04dd_f04_deep_drawdown_recovery_dd_50d_jerk_v001_signal,
    f04dd_f04_deep_drawdown_recovery_dd_50d_jerk_v002_signal,
    f04dd_f04_deep_drawdown_recovery_dd_63d_jerk_v003_signal,
    f04dd_f04_deep_drawdown_recovery_dd_63d_jerk_v004_signal,
    f04dd_f04_deep_drawdown_recovery_dd_126d_jerk_v005_signal,
    f04dd_f04_deep_drawdown_recovery_dd_126d_jerk_v006_signal,
    f04dd_f04_deep_drawdown_recovery_dd_252d_jerk_v007_signal,
    f04dd_f04_deep_drawdown_recovery_dd_252d_jerk_v008_signal,
    f04dd_f04_deep_drawdown_recovery_dd_504d_jerk_v009_signal,
    f04dd_f04_deep_drawdown_recovery_dd_504d_jerk_v010_signal,
    f04dd_f04_deep_drawdown_recovery_recov_50d_jerk_v011_signal,
    f04dd_f04_deep_drawdown_recovery_recov_50d_jerk_v012_signal,
    f04dd_f04_deep_drawdown_recovery_recov_63d_jerk_v013_signal,
    f04dd_f04_deep_drawdown_recovery_recov_63d_jerk_v014_signal,
    f04dd_f04_deep_drawdown_recovery_recov_126d_jerk_v015_signal,
    f04dd_f04_deep_drawdown_recovery_recov_126d_jerk_v016_signal,
    f04dd_f04_deep_drawdown_recovery_recov_252d_jerk_v017_signal,
    f04dd_f04_deep_drawdown_recovery_recov_252d_jerk_v018_signal,
    f04dd_f04_deep_drawdown_recovery_recov_504d_jerk_v019_signal,
    f04dd_f04_deep_drawdown_recovery_recov_504d_jerk_v020_signal,
    f04dd_f04_deep_drawdown_recovery_recov_1260d_jerk_v021_signal,
    f04dd_f04_deep_drawdown_recovery_recov_1260d_jerk_v022_signal,
    f04dd_f04_deep_drawdown_recovery_ulcer_50d_jerk_v023_signal,
    f04dd_f04_deep_drawdown_recovery_ulcer_50d_jerk_v024_signal,
    f04dd_f04_deep_drawdown_recovery_ulcer_63d_jerk_v025_signal,
    f04dd_f04_deep_drawdown_recovery_ulcer_63d_jerk_v026_signal,
    f04dd_f04_deep_drawdown_recovery_ulcer_126d_jerk_v027_signal,
    f04dd_f04_deep_drawdown_recovery_ulcer_126d_jerk_v028_signal,
    f04dd_f04_deep_drawdown_recovery_ulcer_252d_jerk_v029_signal,
    f04dd_f04_deep_drawdown_recovery_ulcer_252d_jerk_v030_signal,
    f04dd_f04_deep_drawdown_recovery_ulcer_504d_jerk_v031_signal,
    f04dd_f04_deep_drawdown_recovery_ulcer_504d_jerk_v032_signal,
    f04dd_f04_deep_drawdown_recovery_ulcer_1260d_jerk_v033_signal,
    f04dd_f04_deep_drawdown_recovery_ulcer_1260d_jerk_v034_signal,
    f04dd_f04_deep_drawdown_recovery_pain_63d_jerk_v035_signal,
    f04dd_f04_deep_drawdown_recovery_pain_504d_jerk_v036_signal,
    f04dd_f04_deep_drawdown_recovery_pain_504d_jerk_v037_signal,
    f04dd_f04_deep_drawdown_recovery_recovfrac_63d_jerk_v038_signal,
    f04dd_f04_deep_drawdown_recovery_recovfrac_63d_jerk_v039_signal,
    f04dd_f04_deep_drawdown_recovery_recovfrac_126d_jerk_v040_signal,
    f04dd_f04_deep_drawdown_recovery_recovfrac_126d_jerk_v041_signal,
    f04dd_f04_deep_drawdown_recovery_recovfrac_252d_jerk_v042_signal,
    f04dd_f04_deep_drawdown_recovery_recovfrac_252d_jerk_v043_signal,
    f04dd_f04_deep_drawdown_recovery_uwf10_126d_jerk_v044_signal,
    f04dd_f04_deep_drawdown_recovery_uwf10_126d_jerk_v045_signal,
    f04dd_f04_deep_drawdown_recovery_uwf10_252d_jerk_v046_signal,
    f04dd_f04_deep_drawdown_recovery_uwf10_252d_jerk_v047_signal,
    f04dd_f04_deep_drawdown_recovery_uwf10_504d_jerk_v048_signal,
    f04dd_f04_deep_drawdown_recovery_uwf10_504d_jerk_v049_signal,
    f04dd_f04_deep_drawdown_recovery_uwf10_1260d_jerk_v050_signal,
    f04dd_f04_deep_drawdown_recovery_uwf10_1260d_jerk_v051_signal,
    f04dd_f04_deep_drawdown_recovery_uwf25_252d_jerk_v052_signal,
    f04dd_f04_deep_drawdown_recovery_uwf25_1260d_jerk_v053_signal,
    f04dd_f04_deep_drawdown_recovery_uwf25_1260d_jerk_v054_signal,
    f04dd_f04_deep_drawdown_recovery_ddz_63d_jerk_v055_signal,
    f04dd_f04_deep_drawdown_recovery_ddz_63d_jerk_v056_signal,
    f04dd_f04_deep_drawdown_recovery_ddz_126d_jerk_v057_signal,
    f04dd_f04_deep_drawdown_recovery_ddz_126d_jerk_v058_signal,
    f04dd_f04_deep_drawdown_recovery_ddz_252d_jerk_v059_signal,
    f04dd_f04_deep_drawdown_recovery_ddz_252d_jerk_v060_signal,
    f04dd_f04_deep_drawdown_recovery_ddz_504d_jerk_v061_signal,
    f04dd_f04_deep_drawdown_recovery_ddz_504d_jerk_v062_signal,
    f04dd_f04_deep_drawdown_recovery_recovz_63d_jerk_v063_signal,
    f04dd_f04_deep_drawdown_recovery_recovz_63d_jerk_v064_signal,
    f04dd_f04_deep_drawdown_recovery_recovz_126d_jerk_v065_signal,
    f04dd_f04_deep_drawdown_recovery_recovz_126d_jerk_v066_signal,
    f04dd_f04_deep_drawdown_recovery_recovz_252d_jerk_v067_signal,
    f04dd_f04_deep_drawdown_recovery_recovz_252d_jerk_v068_signal,
    f04dd_f04_deep_drawdown_recovery_recovz_504d_jerk_v069_signal,
    f04dd_f04_deep_drawdown_recovery_recovz_504d_jerk_v070_signal,
    f04dd_f04_deep_drawdown_recovery_maxdd_63d_jerk_v071_signal,
    f04dd_f04_deep_drawdown_recovery_maxdd_63d_jerk_v072_signal,
    f04dd_f04_deep_drawdown_recovery_maxdd_126d_jerk_v073_signal,
    f04dd_f04_deep_drawdown_recovery_maxdd_126d_jerk_v074_signal,
    f04dd_f04_deep_drawdown_recovery_maxdd_252d_jerk_v075_signal,
    f04dd_f04_deep_drawdown_recovery_maxdd_252d_jerk_v076_signal,
    f04dd_f04_deep_drawdown_recovery_maxdd_504d_jerk_v077_signal,
    f04dd_f04_deep_drawdown_recovery_maxdd_504d_jerk_v078_signal,
    f04dd_f04_deep_drawdown_recovery_semidev_63d_jerk_v079_signal,
    f04dd_f04_deep_drawdown_recovery_semidev_63d_jerk_v080_signal,
    f04dd_f04_deep_drawdown_recovery_semidev_126d_jerk_v081_signal,
    f04dd_f04_deep_drawdown_recovery_semidev_126d_jerk_v082_signal,
    f04dd_f04_deep_drawdown_recovery_semidev_252d_jerk_v083_signal,
    f04dd_f04_deep_drawdown_recovery_semidev_252d_jerk_v084_signal,
    f04dd_f04_deep_drawdown_recovery_semidev_504d_jerk_v085_signal,
    f04dd_f04_deep_drawdown_recovery_semidev_504d_jerk_v086_signal,
    f04dd_f04_deep_drawdown_recovery_logsurv_126d_jerk_v087_signal,
    f04dd_f04_deep_drawdown_recovery_logsurv_252d_jerk_v088_signal,
    f04dd_f04_deep_drawdown_recovery_logsurv_252d_jerk_v089_signal,
    f04dd_f04_deep_drawdown_recovery_logsurv_504d_jerk_v090_signal,
    f04dd_f04_deep_drawdown_recovery_logsurv_504d_jerk_v091_signal,
    f04dd_f04_deep_drawdown_recovery_logsurv_1260d_jerk_v092_signal,
    f04dd_f04_deep_drawdown_recovery_logsurv_1260d_jerk_v093_signal,
    f04dd_f04_deep_drawdown_recovery_painz_126d_jerk_v094_signal,
    f04dd_f04_deep_drawdown_recovery_painz_126d_jerk_v095_signal,
    f04dd_f04_deep_drawdown_recovery_painz_252d_jerk_v096_signal,
    f04dd_f04_deep_drawdown_recovery_painz_252d_jerk_v097_signal,
    f04dd_f04_deep_drawdown_recovery_painz_504d_jerk_v098_signal,
    f04dd_f04_deep_drawdown_recovery_painz_504d_jerk_v099_signal,
    f04dd_f04_deep_drawdown_recovery_painz_1260d_jerk_v100_signal,
    f04dd_f04_deep_drawdown_recovery_painz_1260d_jerk_v101_signal,
    f04dd_f04_deep_drawdown_recovery_recovfz_126d_jerk_v102_signal,
    f04dd_f04_deep_drawdown_recovery_recovfz_126d_jerk_v103_signal,
    f04dd_f04_deep_drawdown_recovery_recovfz_252d_jerk_v104_signal,
    f04dd_f04_deep_drawdown_recovery_recovfz_252d_jerk_v105_signal,
    f04dd_f04_deep_drawdown_recovery_uwf40_252d_jerk_v106_signal,
    f04dd_f04_deep_drawdown_recovery_uwf40_252d_jerk_v107_signal,
    f04dd_f04_deep_drawdown_recovery_uwf40_504d_jerk_v108_signal,
    f04dd_f04_deep_drawdown_recovery_uwf40_1260d_jerk_v109_signal,
    f04dd_f04_deep_drawdown_recovery_maxddz_126d_jerk_v110_signal,
    f04dd_f04_deep_drawdown_recovery_maxddz_126d_jerk_v111_signal,
    f04dd_f04_deep_drawdown_recovery_maxddz_252d_jerk_v112_signal,
    f04dd_f04_deep_drawdown_recovery_maxddz_252d_jerk_v113_signal,
    f04dd_f04_deep_drawdown_recovery_maxddz_504d_jerk_v114_signal,
    f04dd_f04_deep_drawdown_recovery_maxddz_504d_jerk_v115_signal,
    f04dd_f04_deep_drawdown_recovery_maxddz_1260d_jerk_v116_signal,
    f04dd_f04_deep_drawdown_recovery_maxddz_1260d_jerk_v117_signal,
    f04dd_f04_deep_drawdown_recovery_ulcerz_126d_jerk_v118_signal,
    f04dd_f04_deep_drawdown_recovery_ulcerz_126d_jerk_v119_signal,
    f04dd_f04_deep_drawdown_recovery_ulcerz_252d_jerk_v120_signal,
    f04dd_f04_deep_drawdown_recovery_ulcerz_504d_jerk_v121_signal,
    f04dd_f04_deep_drawdown_recovery_survz_1260d_jerk_v122_signal,
    f04dd_f04_deep_drawdown_recovery_semidevz_126d_jerk_v123_signal,
    f04dd_f04_deep_drawdown_recovery_semidevz_126d_jerk_v124_signal,
    f04dd_f04_deep_drawdown_recovery_semidevz_252d_jerk_v125_signal,
    f04dd_f04_deep_drawdown_recovery_semidevz_252d_jerk_v126_signal,
    f04dd_f04_deep_drawdown_recovery_semidevz_504d_jerk_v127_signal,
    f04dd_f04_deep_drawdown_recovery_semidevz_504d_jerk_v128_signal,
    f04dd_f04_deep_drawdown_recovery_semidevz_1260d_jerk_v129_signal,
    f04dd_f04_deep_drawdown_recovery_semidevz_1260d_jerk_v130_signal,
    f04dd_f04_deep_drawdown_recovery_uwf15_126d_jerk_v131_signal,
    f04dd_f04_deep_drawdown_recovery_uwf15_126d_jerk_v132_signal,
    f04dd_f04_deep_drawdown_recovery_uwf15_252d_jerk_v133_signal,
    f04dd_f04_deep_drawdown_recovery_uwf15_252d_jerk_v134_signal,
    f04dd_f04_deep_drawdown_recovery_logsurvz_504d_jerk_v135_signal,
    f04dd_f04_deep_drawdown_recovery_logsurvz_1260d_jerk_v136_signal,
    f04dd_f04_deep_drawdown_recovery_logsurvz_1260d_jerk_v137_signal,
    f04dd_f04_deep_drawdown_recovery_painratio_126d_jerk_v138_signal,
    f04dd_f04_deep_drawdown_recovery_painratio_126d_jerk_v139_signal,
    f04dd_f04_deep_drawdown_recovery_painratio_252d_jerk_v140_signal,
    f04dd_f04_deep_drawdown_recovery_painratio_252d_jerk_v141_signal,
    f04dd_f04_deep_drawdown_recovery_painratio_504d_jerk_v142_signal,
    f04dd_f04_deep_drawdown_recovery_painratio_504d_jerk_v143_signal,
    f04dd_f04_deep_drawdown_recovery_recovsd_63d_jerk_v144_signal,
    f04dd_f04_deep_drawdown_recovery_recovfrac2_126d_jerk_v145_signal,
    f04dd_f04_deep_drawdown_recovery_recovfrac2_126d_jerk_v146_signal,
    f04dd_f04_deep_drawdown_recovery_recovfrac2_252d_jerk_v147_signal,
    f04dd_f04_deep_drawdown_recovery_recovfrac2_252d_jerk_v148_signal,
    f04dd_f04_deep_drawdown_recovery_recovfrac2_504d_jerk_v149_signal,
    f04dd_f04_deep_drawdown_recovery_ddsq_126d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F04_DEEP_DRAWDOWN_RECOVERY_REGISTRY_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0003, 0.035, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.01, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(8e5, 5e5, n)) + 1e4, name="volume")

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

    print("OK f04_deep_drawdown_recovery_3rd_derivatives_001_150_claude: %d features pass" % n_features)
