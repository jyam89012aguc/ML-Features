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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _f04_drawdown(close, w):
    peak = close.rolling(w, min_periods=max(1, w // 2)).max()
    return close / peak.replace(0, np.nan) - 1.0


def _f04_maxdd(close, w):
    uw = _f04_drawdown(close, w)
    return uw.rolling(w, min_periods=max(1, w // 2)).min()


def _f04_recovery_off_trough(close, w):
    trough = close.rolling(w, min_periods=max(1, w // 2)).min()
    return close / trough.replace(0, np.nan) - 1.0


def _f04_pain_index(close, w):
    uw = _f04_drawdown(close, w)
    return (-uw).rolling(w, min_periods=max(1, w // 2)).mean()


def _f04_ulcer(close, w):
    uw = _f04_drawdown(close, w)
    return np.sqrt((uw ** 2).rolling(w, min_periods=max(1, w // 2)).mean())


def _f04_ret(close):
    return close.pct_change()


def f04dr_f04_drawdown_recovery_uw21d_21d_jerk_v001_signal(closeadj):
    base = _f04_drawdown(closeadj, 21)
    feat = base.ewm(span=10, min_periods=max(5, 10 // 2)).mean()
    d1 = feat.diff(5) / float(5)
    deriv = d1.diff(5) / float(5)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uw42d_42d_jerk_v002_signal(closeadj):
    base = _f04_drawdown(closeadj, 42)
    feat = _z(base, 42)
    d1 = feat.diff(8) / float(8)
    deriv = d1.diff(8) / float(8)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uw63d_63d_jerk_v003_signal(closeadj):
    base = _f04_drawdown(closeadj, 63)
    feat = base - base.rolling(15, min_periods=max(1, 15 // 2)).mean()
    d1 = feat.diff(12) / float(12)
    deriv = d1.diff(12) / float(12)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uw84d_84d_jerk_v004_signal(closeadj):
    base = _f04_drawdown(closeadj, 84)
    feat = np.tanh(base - base.rolling(21, min_periods=max(1, 21 // 2)).median())
    d1 = feat.diff(16) / float(16)
    deriv = d1.diff(16) / float(16)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uw126d_126d_jerk_v005_signal(closeadj):
    base = _f04_drawdown(closeadj, 126)
    feat = base
    d1 = feat.diff(25) / float(25)
    deriv = d1.diff(25) / float(25)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uw168d_168d_jerk_v006_signal(closeadj):
    base = _f04_drawdown(closeadj, 168)
    feat = base.ewm(span=42, min_periods=max(5, 42 // 2)).mean()
    d1 = feat.diff(33) / float(33)
    deriv = d1.diff(33) / float(33)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uw189d_189d_jerk_v007_signal(closeadj):
    base = _f04_drawdown(closeadj, 189)
    feat = _z(base, 189)
    d1 = feat.diff(37) / float(37)
    deriv = d1.diff(37) / float(37)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uw210d_210d_jerk_v008_signal(closeadj):
    base = _f04_drawdown(closeadj, 210)
    feat = base - base.rolling(52, min_periods=max(1, 52 // 2)).mean()
    d1 = feat.diff(42) / float(42)
    deriv = d1.diff(42) / float(42)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uw252d_252d_jerk_v009_signal(closeadj):
    base = _f04_drawdown(closeadj, 252)
    feat = np.tanh(base - base.rolling(63, min_periods=max(1, 63 // 2)).median())
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uw315d_315d_jerk_v010_signal(closeadj):
    base = _f04_drawdown(closeadj, 315)
    feat = base
    d1 = feat.diff(63) / float(63)
    deriv = d1.diff(63) / float(63)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uw378d_378d_jerk_v011_signal(closeadj):
    base = _f04_drawdown(closeadj, 378)
    feat = base.ewm(span=94, min_periods=max(5, 94 // 2)).mean()
    d1 = feat.diff(75) / float(75)
    deriv = d1.diff(75) / float(75)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uw441d_441d_jerk_v012_signal(closeadj):
    base = _f04_drawdown(closeadj, 441)
    feat = _z(base, 441)
    d1 = feat.diff(88) / float(88)
    deriv = d1.diff(88) / float(88)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uw504d_504d_jerk_v013_signal(closeadj):
    base = _f04_drawdown(closeadj, 504)
    feat = base - base.rolling(126, min_periods=max(1, 126 // 2)).mean()
    d1 = feat.diff(100) / float(100)
    deriv = d1.diff(100) / float(100)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_maxdd63d_63d_jerk_v014_signal(closeadj):
    base = _f04_maxdd(closeadj, 63)
    feat = np.tanh(base - base.rolling(15, min_periods=max(1, 15 // 2)).median())
    d1 = feat.diff(12) / float(12)
    deriv = d1.diff(12) / float(12)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_maxdd126d_126d_jerk_v015_signal(closeadj):
    base = _f04_maxdd(closeadj, 126)
    feat = base
    d1 = feat.diff(25) / float(25)
    deriv = d1.diff(25) / float(25)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_maxdd189d_189d_jerk_v016_signal(closeadj):
    base = _f04_maxdd(closeadj, 189)
    feat = base.ewm(span=47, min_periods=max(5, 47 // 2)).mean()
    d1 = feat.diff(37) / float(37)
    deriv = d1.diff(37) / float(37)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_maxdd252d_252d_jerk_v017_signal(closeadj):
    base = _f04_maxdd(closeadj, 252)
    feat = _z(base, 252)
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_maxdd378d_378d_jerk_v018_signal(closeadj):
    base = _f04_maxdd(closeadj, 378)
    feat = base - base.rolling(94, min_periods=max(1, 94 // 2)).mean()
    d1 = feat.diff(75) / float(75)
    deriv = d1.diff(75) / float(75)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_maxdd504d_504d_jerk_v019_signal(closeadj):
    base = _f04_maxdd(closeadj, 504)
    feat = np.tanh(base - base.rolling(126, min_periods=max(1, 126 // 2)).median())
    d1 = feat.diff(100) / float(100)
    deriv = d1.diff(100) / float(100)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_recov42d_42d_jerk_v020_signal(closeadj):
    base = _f04_recovery_off_trough(closeadj, 42)
    feat = base
    d1 = feat.diff(8) / float(8)
    deriv = d1.diff(8) / float(8)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_recov63d_63d_jerk_v021_signal(closeadj):
    base = _f04_recovery_off_trough(closeadj, 63)
    feat = base.ewm(span=15, min_periods=max(5, 15 // 2)).mean()
    d1 = feat.diff(12) / float(12)
    deriv = d1.diff(12) / float(12)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_recov126d_126d_jerk_v022_signal(closeadj):
    base = _f04_recovery_off_trough(closeadj, 126)
    feat = _z(base, 126)
    d1 = feat.diff(25) / float(25)
    deriv = d1.diff(25) / float(25)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_recov189d_189d_jerk_v023_signal(closeadj):
    base = _f04_recovery_off_trough(closeadj, 189)
    feat = base - base.rolling(47, min_periods=max(1, 47 // 2)).mean()
    d1 = feat.diff(37) / float(37)
    deriv = d1.diff(37) / float(37)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_recov252d_252d_jerk_v024_signal(closeadj):
    base = _f04_recovery_off_trough(closeadj, 252)
    feat = np.tanh(base - base.rolling(63, min_periods=max(1, 63 // 2)).median())
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_recov378d_378d_jerk_v025_signal(closeadj):
    base = _f04_recovery_off_trough(closeadj, 378)
    feat = base
    d1 = feat.diff(75) / float(75)
    deriv = d1.diff(75) / float(75)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_recov504d_504d_jerk_v026_signal(closeadj):
    base = _f04_recovery_off_trough(closeadj, 504)
    feat = base.ewm(span=126, min_periods=max(5, 126 // 2)).mean()
    d1 = feat.diff(100) / float(100)
    deriv = d1.diff(100) / float(100)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_pain63d_63d_jerk_v027_signal(closeadj):
    base = _f04_pain_index(closeadj, 63)
    feat = _z(base, 63)
    d1 = feat.diff(12) / float(12)
    deriv = d1.diff(12) / float(12)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_pain126d_126d_jerk_v028_signal(closeadj):
    base = _f04_pain_index(closeadj, 126)
    feat = base - base.rolling(31, min_periods=max(1, 31 // 2)).mean()
    d1 = feat.diff(25) / float(25)
    deriv = d1.diff(25) / float(25)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_pain252d_252d_jerk_v029_signal(closeadj):
    base = _f04_pain_index(closeadj, 252)
    feat = np.tanh(base - base.rolling(63, min_periods=max(1, 63 // 2)).median())
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_pain504d_504d_jerk_v030_signal(closeadj):
    base = _f04_pain_index(closeadj, 504)
    feat = base
    d1 = feat.diff(100) / float(100)
    deriv = d1.diff(100) / float(100)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_ulcer63d_63d_jerk_v031_signal(closeadj):
    base = _f04_ulcer(closeadj, 63)
    feat = base.ewm(span=15, min_periods=max(5, 15 // 2)).mean()
    d1 = feat.diff(12) / float(12)
    deriv = d1.diff(12) / float(12)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_ulcer126d_126d_jerk_v032_signal(closeadj):
    base = _f04_ulcer(closeadj, 126)
    feat = _z(base, 126)
    d1 = feat.diff(25) / float(25)
    deriv = d1.diff(25) / float(25)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_ulcer252d_252d_jerk_v033_signal(closeadj):
    base = _f04_ulcer(closeadj, 252)
    feat = base - base.rolling(63, min_periods=max(1, 63 // 2)).mean()
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_ulcer504d_504d_jerk_v034_signal(closeadj):
    base = _f04_ulcer(closeadj, 504)
    feat = np.tanh(base - base.rolling(126, min_periods=max(1, 126 // 2)).median())
    d1 = feat.diff(100) / float(100)
    deriv = d1.diff(100) / float(100)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uwdur05126d_126d_jerk_v035_signal(closeadj):
    uw = _f04_drawdown(closeadj, 126)
    base = (uw <= -0.05).astype(float).rolling(126, min_periods=max(1, 126 // 2)).mean()
    feat = base
    d1 = feat.diff(25) / float(25)
    deriv = d1.diff(25) / float(25)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uwdur10126d_126d_jerk_v036_signal(closeadj):
    uw = _f04_drawdown(closeadj, 126)
    base = (uw <= -0.1).astype(float).rolling(126, min_periods=max(1, 126 // 2)).mean()
    feat = base.ewm(span=31, min_periods=max(5, 31 // 2)).mean()
    d1 = feat.diff(25) / float(25)
    deriv = d1.diff(25) / float(25)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uwdur20126d_126d_jerk_v037_signal(closeadj):
    uw = _f04_drawdown(closeadj, 126)
    base = (uw <= -0.2).astype(float).rolling(126, min_periods=max(1, 126 // 2)).mean()
    feat = _z(base, 126)
    d1 = feat.diff(25) / float(25)
    deriv = d1.diff(25) / float(25)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uwdur05252d_252d_jerk_v038_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    base = (uw <= -0.05).astype(float).rolling(252, min_periods=max(1, 252 // 2)).mean()
    feat = base - base.rolling(63, min_periods=max(1, 63 // 2)).mean()
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uwdur10252d_252d_jerk_v039_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    base = (uw <= -0.1).astype(float).rolling(252, min_periods=max(1, 252 // 2)).mean()
    feat = np.tanh(base - base.rolling(63, min_periods=max(1, 63 // 2)).median())
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uwdur20252d_252d_jerk_v040_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    base = (uw <= -0.2).astype(float).rolling(252, min_periods=max(1, 252 // 2)).mean()
    feat = base
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uwdur05504d_504d_jerk_v041_signal(closeadj):
    uw = _f04_drawdown(closeadj, 504)
    base = (uw <= -0.05).astype(float).rolling(504, min_periods=max(1, 504 // 2)).mean()
    feat = base.ewm(span=126, min_periods=max(5, 126 // 2)).mean()
    d1 = feat.diff(100) / float(100)
    deriv = d1.diff(100) / float(100)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uwdur10504d_504d_jerk_v042_signal(closeadj):
    uw = _f04_drawdown(closeadj, 504)
    base = (uw <= -0.1).astype(float).rolling(504, min_periods=max(1, 504 // 2)).mean()
    feat = _z(base, 504)
    d1 = feat.diff(100) / float(100)
    deriv = d1.diff(100) / float(100)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uwdur20504d_504d_jerk_v043_signal(closeadj):
    uw = _f04_drawdown(closeadj, 504)
    base = (uw <= -0.2).astype(float).rolling(504, min_periods=max(1, 504 // 2)).mean()
    feat = base - base.rolling(126, min_periods=max(1, 126 // 2)).mean()
    d1 = feat.diff(100) / float(100)
    deriv = d1.diff(100) / float(100)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_recovfrac126d_126d_jerk_v044_signal(closeadj):
    peak = _rmax(closeadj, 126)
    trough = _rmin(closeadj, 126)
    base = (closeadj - trough) / (peak - trough).replace(0, np.nan)
    feat = np.tanh(base - base.rolling(31, min_periods=max(1, 31 // 2)).median())
    d1 = feat.diff(25) / float(25)
    deriv = d1.diff(25) / float(25)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_recovfrac252d_252d_jerk_v045_signal(closeadj):
    peak = _rmax(closeadj, 252)
    trough = _rmin(closeadj, 252)
    base = (closeadj - trough) / (peak - trough).replace(0, np.nan)
    feat = base
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_recovfrac504d_504d_jerk_v046_signal(closeadj):
    peak = _rmax(closeadj, 504)
    trough = _rmin(closeadj, 504)
    base = (closeadj - trough) / (peak - trough).replace(0, np.nan)
    feat = base.ewm(span=126, min_periods=max(5, 126 // 2)).mean()
    d1 = feat.diff(100) / float(100)
    deriv = d1.diff(100) / float(100)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_ddhalflife63d_63d_jerk_v047_signal(closeadj):
    uw = (-_f04_drawdown(closeadj, 63)).replace(0, np.nan)
    base = uw / uw.shift(21)
    feat = _z(base, 63)
    d1 = feat.diff(12) / float(12)
    deriv = d1.diff(12) / float(12)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_ddhalflife126d_126d_jerk_v048_signal(closeadj):
    uw = (-_f04_drawdown(closeadj, 126)).replace(0, np.nan)
    base = uw / uw.shift(21)
    feat = base - base.rolling(31, min_periods=max(1, 31 // 2)).mean()
    d1 = feat.diff(25) / float(25)
    deriv = d1.diff(25) / float(25)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_ddhalflife252d_252d_jerk_v049_signal(closeadj):
    uw = (-_f04_drawdown(closeadj, 252)).replace(0, np.nan)
    base = uw / uw.shift(21)
    feat = np.tanh(base - base.rolling(63, min_periods=max(1, 63 // 2)).median())
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_ddhalflife504d_504d_jerk_v050_signal(closeadj):
    uw = (-_f04_drawdown(closeadj, 504)).replace(0, np.nan)
    base = uw / uw.shift(21)
    feat = base
    d1 = feat.diff(100) / float(100)
    deriv = d1.diff(100) / float(100)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_downdev21d_21d_jerk_v051_signal(closeadj):
    r = _f04_ret(closeadj)
    neg = r.where(r < 0, 0.0)
    base = np.sqrt((neg ** 2).rolling(21, min_periods=max(1, 21 // 2)).mean())
    feat = base.ewm(span=10, min_periods=max(5, 10 // 2)).mean()
    d1 = feat.diff(5) / float(5)
    deriv = d1.diff(5) / float(5)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_downdev63d_63d_jerk_v052_signal(closeadj):
    r = _f04_ret(closeadj)
    neg = r.where(r < 0, 0.0)
    base = np.sqrt((neg ** 2).rolling(63, min_periods=max(1, 63 // 2)).mean())
    feat = _z(base, 63)
    d1 = feat.diff(12) / float(12)
    deriv = d1.diff(12) / float(12)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_downdev126d_126d_jerk_v053_signal(closeadj):
    r = _f04_ret(closeadj)
    neg = r.where(r < 0, 0.0)
    base = np.sqrt((neg ** 2).rolling(126, min_periods=max(1, 126 // 2)).mean())
    feat = base - base.rolling(31, min_periods=max(1, 31 // 2)).mean()
    d1 = feat.diff(25) / float(25)
    deriv = d1.diff(25) / float(25)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_downdev252d_252d_jerk_v054_signal(closeadj):
    r = _f04_ret(closeadj)
    neg = r.where(r < 0, 0.0)
    base = np.sqrt((neg ** 2).rolling(252, min_periods=max(1, 252 // 2)).mean())
    feat = np.tanh(base - base.rolling(63, min_periods=max(1, 63 // 2)).median())
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_calmar126d_126d_jerk_v055_signal(closeadj):
    ann = closeadj / closeadj.shift(126) - 1.0
    mdd = (-_f04_maxdd(closeadj, 126)).replace(0, np.nan)
    base = ann / mdd
    feat = base
    d1 = feat.diff(25) / float(25)
    deriv = d1.diff(25) / float(25)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_calmar252d_252d_jerk_v056_signal(closeadj):
    ann = closeadj / closeadj.shift(252) - 1.0
    mdd = (-_f04_maxdd(closeadj, 252)).replace(0, np.nan)
    base = ann / mdd
    feat = base.ewm(span=63, min_periods=max(5, 63 // 2)).mean()
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_calmar504d_504d_jerk_v057_signal(closeadj):
    ann = closeadj / closeadj.shift(504) - 1.0
    mdd = (-_f04_maxdd(closeadj, 504)).replace(0, np.nan)
    base = ann / mdd
    feat = _z(base, 504)
    d1 = feat.diff(100) / float(100)
    deriv = d1.diff(100) / float(100)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_painconc126d_126d_jerk_v058_signal(closeadj):
    ul = _f04_ulcer(closeadj, 126)
    pn = _f04_pain_index(closeadj, 126).replace(0, np.nan)
    base = ul / pn
    feat = base - base.rolling(31, min_periods=max(1, 31 // 2)).mean()
    d1 = feat.diff(25) / float(25)
    deriv = d1.diff(25) / float(25)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_painconc252d_252d_jerk_v059_signal(closeadj):
    ul = _f04_ulcer(closeadj, 252)
    pn = _f04_pain_index(closeadj, 252).replace(0, np.nan)
    base = ul / pn
    feat = np.tanh(base - base.rolling(63, min_periods=max(1, 63 // 2)).median())
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_painconc504d_504d_jerk_v060_signal(closeadj):
    ul = _f04_ulcer(closeadj, 504)
    pn = _f04_pain_index(closeadj, 504).replace(0, np.nan)
    base = ul / pn
    feat = base
    d1 = feat.diff(100) / float(100)
    deriv = d1.diff(100) / float(100)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_gainpain63d_63d_jerk_v061_signal(closeadj):
    r = _f04_ret(closeadj)
    pos = r.where(r > 0, 0.0).rolling(63, min_periods=max(1, 63 // 2)).sum()
    neg = (-r.where(r < 0, 0.0)).rolling(63, min_periods=max(1, 63 // 2)).sum().replace(0, np.nan)
    base = pos / neg - 1.0
    feat = base.ewm(span=15, min_periods=max(5, 15 // 2)).mean()
    d1 = feat.diff(12) / float(12)
    deriv = d1.diff(12) / float(12)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_gainpain126d_126d_jerk_v062_signal(closeadj):
    r = _f04_ret(closeadj)
    pos = r.where(r > 0, 0.0).rolling(126, min_periods=max(1, 126 // 2)).sum()
    neg = (-r.where(r < 0, 0.0)).rolling(126, min_periods=max(1, 126 // 2)).sum().replace(0, np.nan)
    base = pos / neg - 1.0
    feat = _z(base, 126)
    d1 = feat.diff(25) / float(25)
    deriv = d1.diff(25) / float(25)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_gainpain252d_252d_jerk_v063_signal(closeadj):
    r = _f04_ret(closeadj)
    pos = r.where(r > 0, 0.0).rolling(252, min_periods=max(1, 252 // 2)).sum()
    neg = (-r.where(r < 0, 0.0)).rolling(252, min_periods=max(1, 252 // 2)).sum().replace(0, np.nan)
    base = pos / neg - 1.0
    feat = base - base.rolling(63, min_periods=max(1, 63 // 2)).mean()
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_dar126d_126d_jerk_v064_signal(closeadj):
    uw = _f04_drawdown(closeadj, 126)
    base = uw.rolling(126, min_periods=max(1, 126 // 2)).quantile(0.05)
    feat = np.tanh(base - base.rolling(31, min_periods=max(1, 31 // 2)).median())
    d1 = feat.diff(25) / float(25)
    deriv = d1.diff(25) / float(25)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_dar252d_252d_jerk_v065_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    base = uw.rolling(252, min_periods=max(1, 252 // 2)).quantile(0.05)
    feat = base
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_dar504d_504d_jerk_v066_signal(closeadj):
    uw = _f04_drawdown(closeadj, 504)
    base = uw.rolling(504, min_periods=max(1, 504 // 2)).quantile(0.05)
    feat = base.ewm(span=126, min_periods=max(5, 126 // 2)).mean()
    d1 = feat.diff(100) / float(100)
    deriv = d1.diff(100) / float(100)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uwstd63d_63d_jerk_v067_signal(closeadj):
    uw = _f04_drawdown(closeadj, 63)
    base = uw.rolling(63, min_periods=max(1, 63 // 2)).std()
    feat = _z(base, 63)
    d1 = feat.diff(12) / float(12)
    deriv = d1.diff(12) / float(12)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uwstd126d_126d_jerk_v068_signal(closeadj):
    uw = _f04_drawdown(closeadj, 126)
    base = uw.rolling(126, min_periods=max(1, 126 // 2)).std()
    feat = base - base.rolling(31, min_periods=max(1, 31 // 2)).mean()
    d1 = feat.diff(25) / float(25)
    deriv = d1.diff(25) / float(25)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uwstd252d_252d_jerk_v069_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    base = uw.rolling(252, min_periods=max(1, 252 // 2)).std()
    feat = np.tanh(base - base.rolling(63, min_periods=max(1, 63 // 2)).median())
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_troughprox63d_63d_jerk_v070_signal(closeadj):
    trough = _rmin(closeadj, 63)
    base = trough.replace(0, np.nan) / closeadj.replace(0, np.nan)
    feat = base
    d1 = feat.diff(12) / float(12)
    deriv = d1.diff(12) / float(12)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_troughprox126d_126d_jerk_v071_signal(closeadj):
    trough = _rmin(closeadj, 126)
    base = trough.replace(0, np.nan) / closeadj.replace(0, np.nan)
    feat = base.ewm(span=31, min_periods=max(5, 31 // 2)).mean()
    d1 = feat.diff(25) / float(25)
    deriv = d1.diff(25) / float(25)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_troughprox252d_252d_jerk_v072_signal(closeadj):
    trough = _rmin(closeadj, 252)
    base = trough.replace(0, np.nan) / closeadj.replace(0, np.nan)
    feat = _z(base, 252)
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_troughprox504d_504d_jerk_v073_signal(closeadj):
    trough = _rmin(closeadj, 504)
    base = trough.replace(0, np.nan) / closeadj.replace(0, np.nan)
    feat = base - base.rolling(126, min_periods=max(1, 126 // 2)).mean()
    d1 = feat.diff(100) / float(100)
    deriv = d1.diff(100) / float(100)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_emadist63d_63d_jerk_v074_signal(closeadj):
    ema = closeadj.ewm(span=63, min_periods=max(5, 63 // 2)).mean()
    mdd = (-_f04_maxdd(closeadj, 63)).replace(0, np.nan)
    base = (closeadj / ema.replace(0, np.nan) - 1.0) / mdd
    feat = np.tanh(base - base.rolling(15, min_periods=max(1, 15 // 2)).median())
    d1 = feat.diff(12) / float(12)
    deriv = d1.diff(12) / float(12)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_emadist126d_126d_jerk_v075_signal(closeadj):
    ema = closeadj.ewm(span=126, min_periods=max(5, 126 // 2)).mean()
    mdd = (-_f04_maxdd(closeadj, 126)).replace(0, np.nan)
    base = (closeadj / ema.replace(0, np.nan) - 1.0) / mdd
    feat = base
    d1 = feat.diff(25) / float(25)
    deriv = d1.diff(25) / float(25)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_emadist252d_252d_jerk_v076_signal(closeadj):
    ema = closeadj.ewm(span=252, min_periods=max(5, 252 // 2)).mean()
    mdd = (-_f04_maxdd(closeadj, 252)).replace(0, np.nan)
    base = (closeadj / ema.replace(0, np.nan) - 1.0) / mdd
    feat = base.ewm(span=63, min_periods=max(5, 63 // 2)).mean()
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_emadist504d_504d_jerk_v077_signal(closeadj):
    ema = closeadj.ewm(span=504, min_periods=max(5, 504 // 2)).mean()
    mdd = (-_f04_maxdd(closeadj, 504)).replace(0, np.nan)
    base = (closeadj / ema.replace(0, np.nan) - 1.0) / mdd
    feat = _z(base, 504)
    d1 = feat.diff(100) / float(100)
    deriv = d1.diff(100) / float(100)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_worst5cum126d_126d_jerk_v078_signal(closeadj):
    cum = closeadj / closeadj.shift(5) - 1.0
    q = cum.rolling(126, min_periods=max(1, 126 // 2)).quantile(0.05)
    tail = cum.where(cum <= q)
    base = tail.rolling(126, min_periods=5).mean()
    feat = base - base.rolling(31, min_periods=max(1, 31 // 2)).mean()
    d1 = feat.diff(25) / float(25)
    deriv = d1.diff(25) / float(25)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_worst21cum252d_252d_jerk_v079_signal(closeadj):
    cum = closeadj / closeadj.shift(21) - 1.0
    q = cum.rolling(252, min_periods=max(1, 252 // 2)).quantile(0.05)
    tail = cum.where(cum <= q)
    base = tail.rolling(252, min_periods=5).mean()
    feat = np.tanh(base - base.rolling(63, min_periods=max(1, 63 // 2)).median())
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_worst63cum252d_252d_jerk_v080_signal(closeadj):
    cum = closeadj / closeadj.shift(63) - 1.0
    q = cum.rolling(252, min_periods=max(1, 252 // 2)).quantile(0.05)
    tail = cum.where(cum <= q)
    base = tail.rolling(252, min_periods=5).mean()
    feat = base
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_worst63cum504d_504d_jerk_v081_signal(closeadj):
    cum = closeadj / closeadj.shift(63) - 1.0
    q = cum.rolling(504, min_periods=max(1, 504 // 2)).quantile(0.05)
    tail = cum.where(cum <= q)
    base = tail.rolling(504, min_periods=5).mean()
    feat = base.ewm(span=126, min_periods=max(5, 126 // 2)).mean()
    d1 = feat.diff(100) / float(100)
    deriv = d1.diff(100) / float(100)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_meduw126d_126d_jerk_v082_signal(closeadj):
    uw = _f04_drawdown(closeadj, 126)
    base = uw.rolling(126, min_periods=max(1, 126 // 2)).median()
    feat = _z(base, 126)
    d1 = feat.diff(25) / float(25)
    deriv = d1.diff(25) / float(25)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_meduw252d_252d_jerk_v083_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    base = uw.rolling(252, min_periods=max(1, 252 // 2)).median()
    feat = base - base.rolling(63, min_periods=max(1, 63 // 2)).mean()
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_meduw504d_504d_jerk_v084_signal(closeadj):
    uw = _f04_drawdown(closeadj, 504)
    base = uw.rolling(504, min_periods=max(1, 504 // 2)).median()
    feat = np.tanh(base - base.rolling(126, min_periods=max(1, 126 // 2)).median())
    d1 = feat.diff(100) / float(100)
    deriv = d1.diff(100) / float(100)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uwiqr126d_126d_jerk_v085_signal(closeadj):
    uw = _f04_drawdown(closeadj, 126)
    q75 = uw.rolling(126, min_periods=max(1, 126 // 2)).quantile(0.75)
    q25 = uw.rolling(126, min_periods=max(1, 126 // 2)).quantile(0.25)
    base = q75 - q25
    feat = base
    d1 = feat.diff(25) / float(25)
    deriv = d1.diff(25) / float(25)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uwiqr252d_252d_jerk_v086_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    q75 = uw.rolling(252, min_periods=max(1, 252 // 2)).quantile(0.75)
    q25 = uw.rolling(252, min_periods=max(1, 252 // 2)).quantile(0.25)
    base = q75 - q25
    feat = base.ewm(span=63, min_periods=max(5, 63 // 2)).mean()
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uwiqr504d_504d_jerk_v087_signal(closeadj):
    uw = _f04_drawdown(closeadj, 504)
    q75 = uw.rolling(504, min_periods=max(1, 504 // 2)).quantile(0.75)
    q25 = uw.rolling(504, min_periods=max(1, 504 // 2)).quantile(0.25)
    base = q75 - q25
    feat = _z(base, 504)
    d1 = feat.diff(100) / float(100)
    deriv = d1.diff(100) / float(100)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_amp63d_63d_jerk_v088_signal(closeadj):
    peak = _rmax(closeadj, 63)
    trough = _rmin(closeadj, 63)
    base = (peak - trough) / closeadj.replace(0, np.nan)
    feat = base - base.rolling(15, min_periods=max(1, 15 // 2)).mean()
    d1 = feat.diff(12) / float(12)
    deriv = d1.diff(12) / float(12)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_amp126d_126d_jerk_v089_signal(closeadj):
    peak = _rmax(closeadj, 126)
    trough = _rmin(closeadj, 126)
    base = (peak - trough) / closeadj.replace(0, np.nan)
    feat = np.tanh(base - base.rolling(31, min_periods=max(1, 31 // 2)).median())
    d1 = feat.diff(25) / float(25)
    deriv = d1.diff(25) / float(25)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_amp252d_252d_jerk_v090_signal(closeadj):
    peak = _rmax(closeadj, 252)
    trough = _rmin(closeadj, 252)
    base = (peak - trough) / closeadj.replace(0, np.nan)
    feat = base
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_amp504d_504d_jerk_v091_signal(closeadj):
    peak = _rmax(closeadj, 504)
    trough = _rmin(closeadj, 504)
    base = (peak - trough) / closeadj.replace(0, np.nan)
    feat = base.ewm(span=126, min_periods=max(5, 126 // 2)).mean()
    d1 = feat.diff(100) / float(100)
    deriv = d1.diff(100) / float(100)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_retskew63d_63d_jerk_v092_signal(closeadj):
    r = _f04_ret(closeadj)
    base = r.rolling(63, min_periods=max(1, 63 // 2)).skew()
    feat = _z(base, 63)
    d1 = feat.diff(12) / float(12)
    deriv = d1.diff(12) / float(12)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_retskew126d_126d_jerk_v093_signal(closeadj):
    r = _f04_ret(closeadj)
    base = r.rolling(126, min_periods=max(1, 126 // 2)).skew()
    feat = base - base.rolling(31, min_periods=max(1, 31 // 2)).mean()
    d1 = feat.diff(25) / float(25)
    deriv = d1.diff(25) / float(25)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_retskew252d_252d_jerk_v094_signal(closeadj):
    r = _f04_ret(closeadj)
    base = r.rolling(252, min_periods=max(1, 252 // 2)).skew()
    feat = np.tanh(base - base.rolling(63, min_periods=max(1, 63 // 2)).median())
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_vqual126d_126d_jerk_v095_signal(closeadj):
    rec = _f04_recovery_off_trough(closeadj, 126)
    dd = (-_f04_maxdd(closeadj, 126))
    base = (rec - dd) / (rec + dd).replace(0, np.nan)
    feat = base
    d1 = feat.diff(25) / float(25)
    deriv = d1.diff(25) / float(25)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_vqual252d_252d_jerk_v096_signal(closeadj):
    rec = _f04_recovery_off_trough(closeadj, 252)
    dd = (-_f04_maxdd(closeadj, 252))
    base = (rec - dd) / (rec + dd).replace(0, np.nan)
    feat = base.ewm(span=63, min_periods=max(5, 63 // 2)).mean()
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_vqual504d_504d_jerk_v097_signal(closeadj):
    rec = _f04_recovery_off_trough(closeadj, 504)
    dd = (-_f04_maxdd(closeadj, 504))
    base = (rec - dd) / (rec + dd).replace(0, np.nan)
    feat = _z(base, 504)
    d1 = feat.diff(100) / float(100)
    deriv = d1.diff(100) / float(100)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_sortino126d_126d_jerk_v098_signal(closeadj):
    ann = closeadj / closeadj.shift(126) - 1.0
    r = _f04_ret(closeadj)
    neg = r.where(r < 0, 0.0)
    dd = (np.sqrt((neg ** 2).rolling(126, min_periods=max(1, 126 // 2)).mean()) * np.sqrt(252.0)).replace(0, np.nan)
    base = ann / dd
    feat = base - base.rolling(31, min_periods=max(1, 31 // 2)).mean()
    d1 = feat.diff(25) / float(25)
    deriv = d1.diff(25) / float(25)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_sortino252d_252d_jerk_v099_signal(closeadj):
    ann = closeadj / closeadj.shift(252) - 1.0
    r = _f04_ret(closeadj)
    neg = r.where(r < 0, 0.0)
    dd = (np.sqrt((neg ** 2).rolling(252, min_periods=max(1, 252 // 2)).mean()) * np.sqrt(252.0)).replace(0, np.nan)
    base = ann / dd
    feat = np.tanh(base - base.rolling(63, min_periods=max(1, 63 // 2)).median())
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_cdar252d_252d_jerk_v100_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    q = uw.rolling(252, min_periods=max(1, 252 // 2)).quantile(0.10)
    tail = uw.where(uw <= q)
    base = tail.rolling(252, min_periods=10).mean()
    feat = base
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_cdar504d_504d_jerk_v101_signal(closeadj):
    uw = _f04_drawdown(closeadj, 504)
    q = uw.rolling(504, min_periods=max(1, 504 // 2)).quantile(0.10)
    tail = uw.where(uw <= q)
    base = tail.rolling(504, min_periods=10).mean()
    feat = base.ewm(span=126, min_periods=max(5, 126 // 2)).mean()
    d1 = feat.diff(100) / float(100)
    deriv = d1.diff(100) / float(100)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_ddvsrng126d_126d_jerk_v102_signal(closeadj):
    mdd = (-_f04_maxdd(closeadj, 126))
    rng = (_rmax(closeadj, 63) / _rmin(closeadj, 63) - 1.0).replace(0, np.nan)
    base = mdd / rng
    feat = _z(base, 126)
    d1 = feat.diff(25) / float(25)
    deriv = d1.diff(25) / float(25)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_ddvsrng252d_252d_jerk_v103_signal(closeadj):
    mdd = (-_f04_maxdd(closeadj, 252))
    rng = (_rmax(closeadj, 63) / _rmin(closeadj, 63) - 1.0).replace(0, np.nan)
    base = mdd / rng
    feat = base - base.rolling(63, min_periods=max(1, 63 // 2)).mean()
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_painperrecov126d_126d_jerk_v104_signal(closeadj):
    pain = _f04_pain_index(closeadj, 126)
    rec = _f04_recovery_off_trough(closeadj, 126).replace(0, np.nan)
    base = pain / rec
    feat = np.tanh(base - base.rolling(31, min_periods=max(1, 31 // 2)).median())
    d1 = feat.diff(25) / float(25)
    deriv = d1.diff(25) / float(25)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_painperrecov252d_252d_jerk_v105_signal(closeadj):
    pain = _f04_pain_index(closeadj, 252)
    rec = _f04_recovery_off_trough(closeadj, 252).replace(0, np.nan)
    base = pain / rec
    feat = base
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_painperrecov504d_504d_jerk_v106_signal(closeadj):
    pain = _f04_pain_index(closeadj, 504)
    rec = _f04_recovery_off_trough(closeadj, 504).replace(0, np.nan)
    base = pain / rec
    feat = base.ewm(span=126, min_periods=max(5, 126 // 2)).mean()
    d1 = feat.diff(100) / float(100)
    deriv = d1.diff(100) / float(100)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uwconvex126d_126d_jerk_v107_signal(closeadj):
    uw = _f04_drawdown(closeadj, 126)
    base = -(uw ** 2)
    feat = _z(base, 126)
    d1 = feat.diff(25) / float(25)
    deriv = d1.diff(25) / float(25)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uwconvex252d_252d_jerk_v108_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    base = -(uw ** 2)
    feat = base - base.rolling(63, min_periods=max(1, 63 // 2)).mean()
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uwconvex504d_504d_jerk_v109_signal(closeadj):
    uw = _f04_drawdown(closeadj, 504)
    base = -(uw ** 2)
    feat = np.tanh(base - base.rolling(126, min_periods=max(1, 126 // 2)).median())
    d1 = feat.diff(100) / float(100)
    deriv = d1.diff(100) / float(100)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_recovqual252d_252d_jerk_v110_signal(closeadj):
    rec = _f04_recovery_off_trough(closeadj, 252)
    ul = _f04_ulcer(closeadj, 252).replace(0, np.nan)
    base = rec / ul
    feat = base
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_recovqual504d_504d_jerk_v111_signal(closeadj):
    rec = _f04_recovery_off_trough(closeadj, 504)
    ul = _f04_ulcer(closeadj, 504).replace(0, np.nan)
    base = rec / ul
    feat = base.ewm(span=126, min_periods=max(5, 126 // 2)).mean()
    d1 = feat.diff(100) / float(100)
    deriv = d1.diff(100) / float(100)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uwcross63d_63d_jerk_v112_signal(closeadj):
    uw = _f04_drawdown(closeadj, 63)
    fast = uw.ewm(span=max(5, 63 // 8), min_periods=5).mean()
    slow = uw.ewm(span=max(10, 63 // 3), min_periods=5).mean()
    sd = uw.rolling(63, min_periods=max(1, 63 // 2)).std().replace(0, np.nan)
    base = (fast - slow) / sd
    feat = _z(base, 63)
    d1 = feat.diff(12) / float(12)
    deriv = d1.diff(12) / float(12)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uwcross126d_126d_jerk_v113_signal(closeadj):
    uw = _f04_drawdown(closeadj, 126)
    fast = uw.ewm(span=max(5, 126 // 8), min_periods=5).mean()
    slow = uw.ewm(span=max(10, 126 // 3), min_periods=5).mean()
    sd = uw.rolling(126, min_periods=max(1, 126 // 2)).std().replace(0, np.nan)
    base = (fast - slow) / sd
    feat = base - base.rolling(31, min_periods=max(1, 31 // 2)).mean()
    d1 = feat.diff(25) / float(25)
    deriv = d1.diff(25) / float(25)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uwcross252d_252d_jerk_v114_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    fast = uw.ewm(span=max(5, 252 // 8), min_periods=5).mean()
    slow = uw.ewm(span=max(10, 252 // 3), min_periods=5).mean()
    sd = uw.rolling(252, min_periods=max(1, 252 // 2)).std().replace(0, np.nan)
    base = (fast - slow) / sd
    feat = np.tanh(base - base.rolling(63, min_periods=max(1, 63 // 2)).median())
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uwcross504d_504d_jerk_v115_signal(closeadj):
    uw = _f04_drawdown(closeadj, 504)
    fast = uw.ewm(span=max(5, 504 // 8), min_periods=5).mean()
    slow = uw.ewm(span=max(10, 504 // 3), min_periods=5).mean()
    sd = uw.rolling(504, min_periods=max(1, 504 // 2)).std().replace(0, np.nan)
    base = (fast - slow) / sd
    feat = base
    d1 = feat.diff(100) / float(100)
    deriv = d1.diff(100) / float(100)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_painadjret126d_126d_jerk_v116_signal(closeadj):
    ret = closeadj / closeadj.shift(126) - 1.0
    pain = _f04_pain_index(closeadj, 126)
    base = ret - 3.0 * pain
    feat = base.ewm(span=31, min_periods=max(5, 31 // 2)).mean()
    d1 = feat.diff(25) / float(25)
    deriv = d1.diff(25) / float(25)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_painadjret252d_252d_jerk_v117_signal(closeadj):
    ret = closeadj / closeadj.shift(252) - 1.0
    pain = _f04_pain_index(closeadj, 252)
    base = ret - 3.0 * pain
    feat = _z(base, 252)
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uwmean189d_189d_jerk_v118_signal(closeadj):
    uw = _f04_drawdown(closeadj, 189)
    base = uw.rolling(189, min_periods=max(1, 189 // 2)).mean()
    feat = base - base.rolling(47, min_periods=max(1, 47 // 2)).mean()
    d1 = feat.diff(37) / float(37)
    deriv = d1.diff(37) / float(37)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uwmean378d_378d_jerk_v119_signal(closeadj):
    uw = _f04_drawdown(closeadj, 378)
    base = uw.rolling(378, min_periods=max(1, 378 // 2)).mean()
    feat = np.tanh(base - base.rolling(94, min_periods=max(1, 94 // 2)).median())
    d1 = feat.diff(75) / float(75)
    deriv = d1.diff(75) / float(75)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_recovperulcer126d_126d_jerk_v120_signal(closeadj):
    rec = _f04_recovery_off_trough(closeadj, 126)
    ul = _f04_ulcer(closeadj, 126).replace(0, np.nan)
    base = rec / ul
    feat = base
    d1 = feat.diff(25) / float(25)
    deriv = d1.diff(25) / float(25)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_recovperulcer252d_252d_jerk_v121_signal(closeadj):
    rec = _f04_recovery_off_trough(closeadj, 252)
    ul = _f04_ulcer(closeadj, 252).replace(0, np.nan)
    base = rec / ul
    feat = base.ewm(span=63, min_periods=max(5, 63 // 2)).mean()
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_recovperulcer504d_504d_jerk_v122_signal(closeadj):
    rec = _f04_recovery_off_trough(closeadj, 504)
    ul = _f04_ulcer(closeadj, 504).replace(0, np.nan)
    base = rec / ul
    feat = _z(base, 504)
    d1 = feat.diff(100) / float(100)
    deriv = d1.diff(100) / float(100)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uwarea126d_126d_jerk_v123_signal(closeadj):
    uw = _f04_drawdown(closeadj, 126)
    base = uw.rolling(63, min_periods=21).sum()
    feat = base - base.rolling(31, min_periods=max(1, 31 // 2)).mean()
    d1 = feat.diff(25) / float(25)
    deriv = d1.diff(25) / float(25)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uwarea252d_252d_jerk_v124_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    base = uw.rolling(63, min_periods=21).sum()
    feat = np.tanh(base - base.rolling(63, min_periods=max(1, 63 // 2)).median())
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uwarea504d_504d_jerk_v125_signal(closeadj):
    uw = _f04_drawdown(closeadj, 504)
    base = uw.rolling(63, min_periods=21).sum()
    feat = base
    d1 = feat.diff(100) / float(100)
    deriv = d1.diff(100) / float(100)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_ddtail252d_252d_jerk_v126_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    p01 = uw.rolling(252, min_periods=max(1, 252 // 2)).quantile(0.01)
    p25 = uw.rolling(252, min_periods=max(1, 252 // 2)).quantile(0.25).replace(0, np.nan)
    base = p01 / p25
    feat = base.ewm(span=63, min_periods=max(5, 63 // 2)).mean()
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_ddtail504d_504d_jerk_v127_signal(closeadj):
    uw = _f04_drawdown(closeadj, 504)
    p01 = uw.rolling(504, min_periods=max(1, 504 // 2)).quantile(0.01)
    p25 = uw.rolling(504, min_periods=max(1, 504 // 2)).quantile(0.25).replace(0, np.nan)
    base = p01 / p25
    feat = _z(base, 504)
    d1 = feat.diff(100) / float(100)
    deriv = d1.diff(100) / float(100)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_crashmag126d_126d_jerk_v128_signal(closeadj):
    r = _f04_ret(closeadj)
    excess = (-r - 0.05).clip(lower=0)
    base = excess.rolling(126, min_periods=max(1, 126 // 2)).sum()
    feat = base - base.rolling(31, min_periods=max(1, 31 // 2)).mean()
    d1 = feat.diff(25) / float(25)
    deriv = d1.diff(25) / float(25)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_crashmag252d_252d_jerk_v129_signal(closeadj):
    r = _f04_ret(closeadj)
    excess = (-r - 0.05).clip(lower=0)
    base = excess.rolling(252, min_periods=max(1, 252 // 2)).sum()
    feat = np.tanh(base - base.rolling(63, min_periods=max(1, 63 // 2)).median())
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_semiratio63d_63d_jerk_v130_signal(closeadj):
    r = _f04_ret(closeadj)
    dn = np.sqrt((r.where(r < 0, 0.0) ** 2).rolling(63, min_periods=max(1, 63 // 2)).mean())
    up = np.sqrt((r.where(r > 0, 0.0) ** 2).rolling(63, min_periods=max(1, 63 // 2)).mean()).replace(0, np.nan)
    base = dn / up
    feat = base
    d1 = feat.diff(12) / float(12)
    deriv = d1.diff(12) / float(12)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_semiratio126d_126d_jerk_v131_signal(closeadj):
    r = _f04_ret(closeadj)
    dn = np.sqrt((r.where(r < 0, 0.0) ** 2).rolling(126, min_periods=max(1, 126 // 2)).mean())
    up = np.sqrt((r.where(r > 0, 0.0) ** 2).rolling(126, min_periods=max(1, 126 // 2)).mean()).replace(0, np.nan)
    base = dn / up
    feat = base.ewm(span=31, min_periods=max(5, 31 // 2)).mean()
    d1 = feat.diff(25) / float(25)
    deriv = d1.diff(25) / float(25)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_semiratio252d_252d_jerk_v132_signal(closeadj):
    r = _f04_ret(closeadj)
    dn = np.sqrt((r.where(r < 0, 0.0) ** 2).rolling(252, min_periods=max(1, 252 // 2)).mean())
    up = np.sqrt((r.where(r > 0, 0.0) ** 2).rolling(252, min_periods=max(1, 252 // 2)).mean()).replace(0, np.nan)
    base = dn / up
    feat = _z(base, 252)
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_recovrng126d_126d_jerk_v133_signal(closeadj):
    lo = _rmin(closeadj, 126)
    hi = _rmax(closeadj, 126)
    base = (closeadj - lo) / (hi - lo).replace(0, np.nan) * (closeadj / lo.replace(0, np.nan) - 1.0)
    feat = base - base.rolling(31, min_periods=max(1, 31 // 2)).mean()
    d1 = feat.diff(25) / float(25)
    deriv = d1.diff(25) / float(25)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_recovrng252d_252d_jerk_v134_signal(closeadj):
    lo = _rmin(closeadj, 252)
    hi = _rmax(closeadj, 252)
    base = (closeadj - lo) / (hi - lo).replace(0, np.nan) * (closeadj / lo.replace(0, np.nan) - 1.0)
    feat = np.tanh(base - base.rolling(63, min_periods=max(1, 63 // 2)).median())
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_recovrng504d_504d_jerk_v135_signal(closeadj):
    lo = _rmin(closeadj, 504)
    hi = _rmax(closeadj, 504)
    base = (closeadj - lo) / (hi - lo).replace(0, np.nan) * (closeadj / lo.replace(0, np.nan) - 1.0)
    feat = base
    d1 = feat.diff(100) / float(100)
    deriv = d1.diff(100) / float(100)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_worstday126d_126d_jerk_v136_signal(closeadj):
    r = _f04_ret(closeadj)
    q = r.rolling(126, min_periods=max(1, 126 // 2)).quantile(0.05)
    tail = r.where(r <= q)
    base = tail.rolling(126, min_periods=5).mean()
    feat = base.ewm(span=31, min_periods=max(5, 31 // 2)).mean()
    d1 = feat.diff(25) / float(25)
    deriv = d1.diff(25) / float(25)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_worstday252d_252d_jerk_v137_signal(closeadj):
    r = _f04_ret(closeadj)
    q = r.rolling(252, min_periods=max(1, 252 // 2)).quantile(0.05)
    tail = r.where(r <= q)
    base = tail.rolling(252, min_periods=5).mean()
    feat = _z(base, 252)
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_ddvol126d_126d_jerk_v138_signal(closeadj):
    mdd = (-_f04_maxdd(closeadj, 126))
    vol = _f04_ret(closeadj).rolling(63, min_periods=21).std()
    base = mdd / (vol * np.sqrt(252.0)).replace(0, np.nan)
    feat = base - base.rolling(31, min_periods=max(1, 31 // 2)).mean()
    d1 = feat.diff(25) / float(25)
    deriv = d1.diff(25) / float(25)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_ddvol252d_252d_jerk_v139_signal(closeadj):
    mdd = (-_f04_maxdd(closeadj, 252))
    vol = _f04_ret(closeadj).rolling(63, min_periods=21).std()
    base = mdd / (vol * np.sqrt(252.0)).replace(0, np.nan)
    feat = np.tanh(base - base.rolling(63, min_periods=max(1, 63 // 2)).median())
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uwdurdepth252d_252d_jerk_v140_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    under = (uw < -0.02).astype(float)
    grp = (under == 0).cumsum()
    run = under.groupby(grp).cumsum()
    base = uw * (run / float(252))
    feat = base
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uwdurdepth504d_504d_jerk_v141_signal(closeadj):
    uw = _f04_drawdown(closeadj, 504)
    under = (uw < -0.02).astype(float)
    grp = (under == 0).cumsum()
    run = under.groupby(grp).cumsum()
    base = uw * (run / float(504))
    feat = base.ewm(span=126, min_periods=max(5, 126 // 2)).mean()
    d1 = feat.diff(100) / float(100)
    deriv = d1.diff(100) / float(100)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_worstqtr252d_252d_jerk_v142_signal(closeadj):
    q = closeadj / closeadj.shift(63) - 1.0
    base = q.rolling(252, min_periods=max(1, 252 // 2)).min()
    feat = _z(base, 252)
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_worstqtr504d_504d_jerk_v143_signal(closeadj):
    q = closeadj / closeadj.shift(63) - 1.0
    base = q.rolling(504, min_periods=max(1, 504 // 2)).min()
    feat = base - base.rolling(126, min_periods=max(1, 126 // 2)).mean()
    d1 = feat.diff(100) / float(100)
    deriv = d1.diff(100) / float(100)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_arearatio378d_378d_jerk_v144_signal(closeadj):
    uw = _f04_drawdown(closeadj, 378)
    rec = _f04_recovery_off_trough(closeadj, 378)
    a_dd = (-uw).rolling(252, min_periods=126).sum().replace(0, np.nan)
    a_rec = rec.rolling(252, min_periods=126).sum()
    base = a_rec / a_dd
    feat = np.tanh(base - base.rolling(94, min_periods=max(1, 94 // 2)).median())
    d1 = feat.diff(75) / float(75)
    deriv = d1.diff(75) / float(75)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_arearatio504d_504d_jerk_v145_signal(closeadj):
    uw = _f04_drawdown(closeadj, 504)
    rec = _f04_recovery_off_trough(closeadj, 504)
    a_dd = (-uw).rolling(252, min_periods=126).sum().replace(0, np.nan)
    a_rec = rec.rolling(252, min_periods=126).sum()
    base = a_rec / a_dd
    feat = base
    d1 = feat.diff(100) / float(100)
    deriv = d1.diff(100) / float(100)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uwmad126d_126d_jerk_v146_signal(closeadj):
    uw = _f04_drawdown(closeadj, 126)
    med = uw.rolling(126, min_periods=max(1, 126 // 2)).median()
    base = (uw - med).abs().rolling(126, min_periods=max(1, 126 // 2)).median()
    feat = base.ewm(span=31, min_periods=max(5, 31 // 2)).mean()
    d1 = feat.diff(25) / float(25)
    deriv = d1.diff(25) / float(25)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uwmad252d_252d_jerk_v147_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    med = uw.rolling(252, min_periods=max(1, 252 // 2)).median()
    base = (uw - med).abs().rolling(252, min_periods=max(1, 252 // 2)).median()
    feat = _z(base, 252)
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uwmad504d_504d_jerk_v148_signal(closeadj):
    uw = _f04_drawdown(closeadj, 504)
    med = uw.rolling(504, min_periods=max(1, 504 // 2)).median()
    base = (uw - med).abs().rolling(504, min_periods=max(1, 504 // 2)).median()
    feat = base - base.rolling(126, min_periods=max(1, 126 // 2)).mean()
    d1 = feat.diff(100) / float(100)
    deriv = d1.diff(100) / float(100)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_logspan126d_126d_jerk_v149_signal(closeadj):
    hi = _rmax(closeadj, 126)
    lo = _rmin(closeadj, 126)
    base = np.log(hi.replace(0, np.nan) / lo.replace(0, np.nan))
    feat = np.tanh(base - base.rolling(31, min_periods=max(1, 31 // 2)).median())
    d1 = feat.diff(25) / float(25)
    deriv = d1.diff(25) / float(25)
    return deriv.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_logspan252d_252d_jerk_v150_signal(closeadj):
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 252)
    base = np.log(hi.replace(0, np.nan) / lo.replace(0, np.nan))
    feat = base
    d1 = feat.diff(50) / float(50)
    deriv = d1.diff(50) / float(50)
    return deriv.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f04dr_f04_drawdown_recovery_uw21d_21d_jerk_v001_signal,
    f04dr_f04_drawdown_recovery_uw42d_42d_jerk_v002_signal,
    f04dr_f04_drawdown_recovery_uw63d_63d_jerk_v003_signal,
    f04dr_f04_drawdown_recovery_uw84d_84d_jerk_v004_signal,
    f04dr_f04_drawdown_recovery_uw126d_126d_jerk_v005_signal,
    f04dr_f04_drawdown_recovery_uw168d_168d_jerk_v006_signal,
    f04dr_f04_drawdown_recovery_uw189d_189d_jerk_v007_signal,
    f04dr_f04_drawdown_recovery_uw210d_210d_jerk_v008_signal,
    f04dr_f04_drawdown_recovery_uw252d_252d_jerk_v009_signal,
    f04dr_f04_drawdown_recovery_uw315d_315d_jerk_v010_signal,
    f04dr_f04_drawdown_recovery_uw378d_378d_jerk_v011_signal,
    f04dr_f04_drawdown_recovery_uw441d_441d_jerk_v012_signal,
    f04dr_f04_drawdown_recovery_uw504d_504d_jerk_v013_signal,
    f04dr_f04_drawdown_recovery_maxdd63d_63d_jerk_v014_signal,
    f04dr_f04_drawdown_recovery_maxdd126d_126d_jerk_v015_signal,
    f04dr_f04_drawdown_recovery_maxdd189d_189d_jerk_v016_signal,
    f04dr_f04_drawdown_recovery_maxdd252d_252d_jerk_v017_signal,
    f04dr_f04_drawdown_recovery_maxdd378d_378d_jerk_v018_signal,
    f04dr_f04_drawdown_recovery_maxdd504d_504d_jerk_v019_signal,
    f04dr_f04_drawdown_recovery_recov42d_42d_jerk_v020_signal,
    f04dr_f04_drawdown_recovery_recov63d_63d_jerk_v021_signal,
    f04dr_f04_drawdown_recovery_recov126d_126d_jerk_v022_signal,
    f04dr_f04_drawdown_recovery_recov189d_189d_jerk_v023_signal,
    f04dr_f04_drawdown_recovery_recov252d_252d_jerk_v024_signal,
    f04dr_f04_drawdown_recovery_recov378d_378d_jerk_v025_signal,
    f04dr_f04_drawdown_recovery_recov504d_504d_jerk_v026_signal,
    f04dr_f04_drawdown_recovery_pain63d_63d_jerk_v027_signal,
    f04dr_f04_drawdown_recovery_pain126d_126d_jerk_v028_signal,
    f04dr_f04_drawdown_recovery_pain252d_252d_jerk_v029_signal,
    f04dr_f04_drawdown_recovery_pain504d_504d_jerk_v030_signal,
    f04dr_f04_drawdown_recovery_ulcer63d_63d_jerk_v031_signal,
    f04dr_f04_drawdown_recovery_ulcer126d_126d_jerk_v032_signal,
    f04dr_f04_drawdown_recovery_ulcer252d_252d_jerk_v033_signal,
    f04dr_f04_drawdown_recovery_ulcer504d_504d_jerk_v034_signal,
    f04dr_f04_drawdown_recovery_uwdur05126d_126d_jerk_v035_signal,
    f04dr_f04_drawdown_recovery_uwdur10126d_126d_jerk_v036_signal,
    f04dr_f04_drawdown_recovery_uwdur20126d_126d_jerk_v037_signal,
    f04dr_f04_drawdown_recovery_uwdur05252d_252d_jerk_v038_signal,
    f04dr_f04_drawdown_recovery_uwdur10252d_252d_jerk_v039_signal,
    f04dr_f04_drawdown_recovery_uwdur20252d_252d_jerk_v040_signal,
    f04dr_f04_drawdown_recovery_uwdur05504d_504d_jerk_v041_signal,
    f04dr_f04_drawdown_recovery_uwdur10504d_504d_jerk_v042_signal,
    f04dr_f04_drawdown_recovery_uwdur20504d_504d_jerk_v043_signal,
    f04dr_f04_drawdown_recovery_recovfrac126d_126d_jerk_v044_signal,
    f04dr_f04_drawdown_recovery_recovfrac252d_252d_jerk_v045_signal,
    f04dr_f04_drawdown_recovery_recovfrac504d_504d_jerk_v046_signal,
    f04dr_f04_drawdown_recovery_ddhalflife63d_63d_jerk_v047_signal,
    f04dr_f04_drawdown_recovery_ddhalflife126d_126d_jerk_v048_signal,
    f04dr_f04_drawdown_recovery_ddhalflife252d_252d_jerk_v049_signal,
    f04dr_f04_drawdown_recovery_ddhalflife504d_504d_jerk_v050_signal,
    f04dr_f04_drawdown_recovery_downdev21d_21d_jerk_v051_signal,
    f04dr_f04_drawdown_recovery_downdev63d_63d_jerk_v052_signal,
    f04dr_f04_drawdown_recovery_downdev126d_126d_jerk_v053_signal,
    f04dr_f04_drawdown_recovery_downdev252d_252d_jerk_v054_signal,
    f04dr_f04_drawdown_recovery_calmar126d_126d_jerk_v055_signal,
    f04dr_f04_drawdown_recovery_calmar252d_252d_jerk_v056_signal,
    f04dr_f04_drawdown_recovery_calmar504d_504d_jerk_v057_signal,
    f04dr_f04_drawdown_recovery_painconc126d_126d_jerk_v058_signal,
    f04dr_f04_drawdown_recovery_painconc252d_252d_jerk_v059_signal,
    f04dr_f04_drawdown_recovery_painconc504d_504d_jerk_v060_signal,
    f04dr_f04_drawdown_recovery_gainpain63d_63d_jerk_v061_signal,
    f04dr_f04_drawdown_recovery_gainpain126d_126d_jerk_v062_signal,
    f04dr_f04_drawdown_recovery_gainpain252d_252d_jerk_v063_signal,
    f04dr_f04_drawdown_recovery_dar126d_126d_jerk_v064_signal,
    f04dr_f04_drawdown_recovery_dar252d_252d_jerk_v065_signal,
    f04dr_f04_drawdown_recovery_dar504d_504d_jerk_v066_signal,
    f04dr_f04_drawdown_recovery_uwstd63d_63d_jerk_v067_signal,
    f04dr_f04_drawdown_recovery_uwstd126d_126d_jerk_v068_signal,
    f04dr_f04_drawdown_recovery_uwstd252d_252d_jerk_v069_signal,
    f04dr_f04_drawdown_recovery_troughprox63d_63d_jerk_v070_signal,
    f04dr_f04_drawdown_recovery_troughprox126d_126d_jerk_v071_signal,
    f04dr_f04_drawdown_recovery_troughprox252d_252d_jerk_v072_signal,
    f04dr_f04_drawdown_recovery_troughprox504d_504d_jerk_v073_signal,
    f04dr_f04_drawdown_recovery_emadist63d_63d_jerk_v074_signal,
    f04dr_f04_drawdown_recovery_emadist126d_126d_jerk_v075_signal,
    f04dr_f04_drawdown_recovery_emadist252d_252d_jerk_v076_signal,
    f04dr_f04_drawdown_recovery_emadist504d_504d_jerk_v077_signal,
    f04dr_f04_drawdown_recovery_worst5cum126d_126d_jerk_v078_signal,
    f04dr_f04_drawdown_recovery_worst21cum252d_252d_jerk_v079_signal,
    f04dr_f04_drawdown_recovery_worst63cum252d_252d_jerk_v080_signal,
    f04dr_f04_drawdown_recovery_worst63cum504d_504d_jerk_v081_signal,
    f04dr_f04_drawdown_recovery_meduw126d_126d_jerk_v082_signal,
    f04dr_f04_drawdown_recovery_meduw252d_252d_jerk_v083_signal,
    f04dr_f04_drawdown_recovery_meduw504d_504d_jerk_v084_signal,
    f04dr_f04_drawdown_recovery_uwiqr126d_126d_jerk_v085_signal,
    f04dr_f04_drawdown_recovery_uwiqr252d_252d_jerk_v086_signal,
    f04dr_f04_drawdown_recovery_uwiqr504d_504d_jerk_v087_signal,
    f04dr_f04_drawdown_recovery_amp63d_63d_jerk_v088_signal,
    f04dr_f04_drawdown_recovery_amp126d_126d_jerk_v089_signal,
    f04dr_f04_drawdown_recovery_amp252d_252d_jerk_v090_signal,
    f04dr_f04_drawdown_recovery_amp504d_504d_jerk_v091_signal,
    f04dr_f04_drawdown_recovery_retskew63d_63d_jerk_v092_signal,
    f04dr_f04_drawdown_recovery_retskew126d_126d_jerk_v093_signal,
    f04dr_f04_drawdown_recovery_retskew252d_252d_jerk_v094_signal,
    f04dr_f04_drawdown_recovery_vqual126d_126d_jerk_v095_signal,
    f04dr_f04_drawdown_recovery_vqual252d_252d_jerk_v096_signal,
    f04dr_f04_drawdown_recovery_vqual504d_504d_jerk_v097_signal,
    f04dr_f04_drawdown_recovery_sortino126d_126d_jerk_v098_signal,
    f04dr_f04_drawdown_recovery_sortino252d_252d_jerk_v099_signal,
    f04dr_f04_drawdown_recovery_cdar252d_252d_jerk_v100_signal,
    f04dr_f04_drawdown_recovery_cdar504d_504d_jerk_v101_signal,
    f04dr_f04_drawdown_recovery_ddvsrng126d_126d_jerk_v102_signal,
    f04dr_f04_drawdown_recovery_ddvsrng252d_252d_jerk_v103_signal,
    f04dr_f04_drawdown_recovery_painperrecov126d_126d_jerk_v104_signal,
    f04dr_f04_drawdown_recovery_painperrecov252d_252d_jerk_v105_signal,
    f04dr_f04_drawdown_recovery_painperrecov504d_504d_jerk_v106_signal,
    f04dr_f04_drawdown_recovery_uwconvex126d_126d_jerk_v107_signal,
    f04dr_f04_drawdown_recovery_uwconvex252d_252d_jerk_v108_signal,
    f04dr_f04_drawdown_recovery_uwconvex504d_504d_jerk_v109_signal,
    f04dr_f04_drawdown_recovery_recovqual252d_252d_jerk_v110_signal,
    f04dr_f04_drawdown_recovery_recovqual504d_504d_jerk_v111_signal,
    f04dr_f04_drawdown_recovery_uwcross63d_63d_jerk_v112_signal,
    f04dr_f04_drawdown_recovery_uwcross126d_126d_jerk_v113_signal,
    f04dr_f04_drawdown_recovery_uwcross252d_252d_jerk_v114_signal,
    f04dr_f04_drawdown_recovery_uwcross504d_504d_jerk_v115_signal,
    f04dr_f04_drawdown_recovery_painadjret126d_126d_jerk_v116_signal,
    f04dr_f04_drawdown_recovery_painadjret252d_252d_jerk_v117_signal,
    f04dr_f04_drawdown_recovery_uwmean189d_189d_jerk_v118_signal,
    f04dr_f04_drawdown_recovery_uwmean378d_378d_jerk_v119_signal,
    f04dr_f04_drawdown_recovery_recovperulcer126d_126d_jerk_v120_signal,
    f04dr_f04_drawdown_recovery_recovperulcer252d_252d_jerk_v121_signal,
    f04dr_f04_drawdown_recovery_recovperulcer504d_504d_jerk_v122_signal,
    f04dr_f04_drawdown_recovery_uwarea126d_126d_jerk_v123_signal,
    f04dr_f04_drawdown_recovery_uwarea252d_252d_jerk_v124_signal,
    f04dr_f04_drawdown_recovery_uwarea504d_504d_jerk_v125_signal,
    f04dr_f04_drawdown_recovery_ddtail252d_252d_jerk_v126_signal,
    f04dr_f04_drawdown_recovery_ddtail504d_504d_jerk_v127_signal,
    f04dr_f04_drawdown_recovery_crashmag126d_126d_jerk_v128_signal,
    f04dr_f04_drawdown_recovery_crashmag252d_252d_jerk_v129_signal,
    f04dr_f04_drawdown_recovery_semiratio63d_63d_jerk_v130_signal,
    f04dr_f04_drawdown_recovery_semiratio126d_126d_jerk_v131_signal,
    f04dr_f04_drawdown_recovery_semiratio252d_252d_jerk_v132_signal,
    f04dr_f04_drawdown_recovery_recovrng126d_126d_jerk_v133_signal,
    f04dr_f04_drawdown_recovery_recovrng252d_252d_jerk_v134_signal,
    f04dr_f04_drawdown_recovery_recovrng504d_504d_jerk_v135_signal,
    f04dr_f04_drawdown_recovery_worstday126d_126d_jerk_v136_signal,
    f04dr_f04_drawdown_recovery_worstday252d_252d_jerk_v137_signal,
    f04dr_f04_drawdown_recovery_ddvol126d_126d_jerk_v138_signal,
    f04dr_f04_drawdown_recovery_ddvol252d_252d_jerk_v139_signal,
    f04dr_f04_drawdown_recovery_uwdurdepth252d_252d_jerk_v140_signal,
    f04dr_f04_drawdown_recovery_uwdurdepth504d_504d_jerk_v141_signal,
    f04dr_f04_drawdown_recovery_worstqtr252d_252d_jerk_v142_signal,
    f04dr_f04_drawdown_recovery_worstqtr504d_504d_jerk_v143_signal,
    f04dr_f04_drawdown_recovery_arearatio378d_378d_jerk_v144_signal,
    f04dr_f04_drawdown_recovery_arearatio504d_504d_jerk_v145_signal,
    f04dr_f04_drawdown_recovery_uwmad126d_126d_jerk_v146_signal,
    f04dr_f04_drawdown_recovery_uwmad252d_252d_jerk_v147_signal,
    f04dr_f04_drawdown_recovery_uwmad504d_504d_jerk_v148_signal,
    f04dr_f04_drawdown_recovery_logspan126d_126d_jerk_v149_signal,
    f04dr_f04_drawdown_recovery_logspan252d_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F04_DRAWDOWN_RECOVERY_REGISTRY_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0004, 0.032, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.012, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1.2e6, 7e5, n)) + 5e4, name="volume")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume}

    ALLOW = {"open", "high", "low", "close", "closeadj", "volume"}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs %s" % (name, meta["inputs"])
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

    print("OK f04_drawdown_recovery_3rd_derivatives_001_150_claude: %d features pass" % n_features)
