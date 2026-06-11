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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _f16_dollar_vol(closeadj, volume):
    return (closeadj * volume).replace(0, np.nan)


def _f16_logret(closeadj):
    return np.log(closeadj.replace(0, np.nan) / closeadj.shift(1).replace(0, np.nan))


def _f16_amihud_daily(closeadj, volume):
    dv = _f16_dollar_vol(closeadj, volume)
    r = _f16_logret(closeadj).abs()
    return (r / dv) * 1e9


def _f16_amihud(closeadj, volume, w):
    d = _f16_amihud_daily(closeadj, volume)
    return d.rolling(w, min_periods=max(1, w // 2)).mean()


def _f16_turnover(volume, w):
    return volume / _mean(volume, w).replace(0, np.nan)


def _f16_cs_spread(high, low):
    hl = np.log(high.replace(0, np.nan) / low.replace(0, np.nan)) ** 2
    beta = hl + hl.shift(1)
    h2 = pd.concat([high, high.shift(1)], axis=1).max(axis=1)
    l2 = pd.concat([low, low.shift(1)], axis=1).min(axis=1)
    gamma = np.log(h2.replace(0, np.nan) / l2.replace(0, np.nan)) ** 2
    k = 3.0 - 2.0 * np.sqrt(2.0)
    alpha = (np.sqrt(2.0 * beta) - np.sqrt(beta)) / k - np.sqrt(gamma / k)
    alpha = alpha.clip(lower=0)
    spread = 2.0 * (np.exp(alpha) - 1.0) / (1.0 + np.exp(alpha))
    return spread


def _f16_roll_spread(closeadj, w):
    dp = closeadj.diff()
    cov = dp.rolling(w, min_periods=max(1, w // 2)).cov(dp.shift(1))
    return 2.0 * np.sqrt((-cov).clip(lower=0)) / closeadj.replace(0, np.nan)


def _f16_kyle(closeadj, volume, w):
    r = _f16_logret(closeadj).abs()
    dv = _f16_dollar_vol(closeadj, volume)
    lam = (r / np.sqrt(dv)) * 1e4
    return lam.rolling(w, min_periods=max(1, w // 2)).mean()


def _f16_amivest(closeadj, volume, w):
    dv = _f16_dollar_vol(closeadj, volume)
    r = _f16_logret(closeadj).abs()
    liq = dv / (r * 1e9 + 1.0)
    return liq.rolling(w, min_periods=max(1, w // 2)).mean()

def f16lq_f16_liquidity_profile_amihud21raw_10d_jerk_v001_signal(closeadj, volume):
    base = np.log1p(_f16_amihud(closeadj, volume, 21))
    sl = base.diff(10) / float(10)
    deriv = sl.diff(10) / float(10)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_amihud21z_21d_jerk_v002_signal(closeadj, volume):
    base = np.log1p(_f16_amihud(closeadj, volume, 21))
    sl = base.diff(21) / float(21)
    deriv = sl.diff(21) / float(21)
    result = _z(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_amihud21rank_42d_jerk_v003_signal(closeadj, volume):
    base = np.log1p(_f16_amihud(closeadj, volume, 21))
    sl = base.diff(42) / float(42)
    deriv = sl.diff(42) / float(42)
    result = _rank(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_amihud21smag_68d_jerk_v004_signal(closeadj, volume):
    base = np.log1p(_f16_amihud(closeadj, volume, 21))
    sl = base.diff(68) / float(68)
    deriv = sl.diff(68) / float(68)
    result = np.sign(deriv) * (deriv.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_amihud63raw_15d_jerk_v005_signal(closeadj, volume):
    base = np.log1p(_f16_amihud(closeadj, volume, 63))
    sl = base.diff(15) / float(15)
    deriv = sl.diff(15) / float(15)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_amihud63z_26d_jerk_v006_signal(closeadj, volume):
    base = np.log1p(_f16_amihud(closeadj, volume, 63))
    sl = base.diff(26) / float(26)
    deriv = sl.diff(26) / float(26)
    result = _z(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_amihud63rank_47d_jerk_v007_signal(closeadj, volume):
    base = np.log1p(_f16_amihud(closeadj, volume, 63))
    sl = base.diff(47) / float(47)
    deriv = sl.diff(47) / float(47)
    result = _rank(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_amihud63smag_73d_jerk_v008_signal(closeadj, volume):
    base = np.log1p(_f16_amihud(closeadj, volume, 63))
    sl = base.diff(73) / float(73)
    deriv = sl.diff(73) / float(73)
    result = np.sign(deriv) * (deriv.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_amihud126raw_21d_jerk_v009_signal(closeadj, volume):
    base = np.log1p(_f16_amihud(closeadj, volume, 126))
    sl = base.diff(21) / float(21)
    deriv = sl.diff(21) / float(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_amihud126z_32d_jerk_v010_signal(closeadj, volume):
    base = np.log1p(_f16_amihud(closeadj, volume, 126))
    sl = base.diff(32) / float(32)
    deriv = sl.diff(32) / float(32)
    result = _z(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_amihud126rank_53d_jerk_v011_signal(closeadj, volume):
    base = np.log1p(_f16_amihud(closeadj, volume, 126))
    sl = base.diff(53) / float(53)
    deriv = sl.diff(53) / float(53)
    result = _rank(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_amihud126smag_79d_jerk_v012_signal(closeadj, volume):
    base = np.log1p(_f16_amihud(closeadj, volume, 126))
    sl = base.diff(79) / float(79)
    deriv = sl.diff(79) / float(79)
    result = np.sign(deriv) * (deriv.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_amihud252raw_31d_jerk_v013_signal(closeadj, volume):
    base = np.log1p(_f16_amihud(closeadj, volume, 252))
    sl = base.diff(31) / float(31)
    deriv = sl.diff(31) / float(31)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_amihud252z_42d_jerk_v014_signal(closeadj, volume):
    base = np.log1p(_f16_amihud(closeadj, volume, 252))
    sl = base.diff(42) / float(42)
    deriv = sl.diff(42) / float(42)
    result = _z(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_amihud252rank_63d_jerk_v015_signal(closeadj, volume):
    base = np.log1p(_f16_amihud(closeadj, volume, 252))
    sl = base.diff(63) / float(63)
    deriv = sl.diff(63) / float(63)
    result = _rank(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_amihud252smag_89d_jerk_v016_signal(closeadj, volume):
    base = np.log1p(_f16_amihud(closeadj, volume, 252))
    sl = base.diff(89) / float(89)
    deriv = sl.diff(89) / float(89)
    result = np.sign(deriv) * (deriv.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_amihudz63raw_13d_jerk_v017_signal(closeadj, volume):
    base = _z(np.log1p(_f16_amihud(closeadj, volume, 63)), 252)
    sl = base.diff(13) / float(13)
    deriv = sl.diff(13) / float(13)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_amihudz63z_24d_jerk_v018_signal(closeadj, volume):
    base = _z(np.log1p(_f16_amihud(closeadj, volume, 63)), 252)
    sl = base.diff(24) / float(24)
    deriv = sl.diff(24) / float(24)
    result = _z(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_amihudz63rank_45d_jerk_v019_signal(closeadj, volume):
    base = _z(np.log1p(_f16_amihud(closeadj, volume, 63)), 252)
    sl = base.diff(45) / float(45)
    deriv = sl.diff(45) / float(45)
    result = _rank(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_amihudz63smag_71d_jerk_v020_signal(closeadj, volume):
    base = _z(np.log1p(_f16_amihud(closeadj, volume, 63)), 252)
    sl = base.diff(71) / float(71)
    deriv = sl.diff(71) / float(71)
    result = np.sign(deriv) * (deriv.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_amihudrank63raw_18d_jerk_v021_signal(closeadj, volume):
    base = _rank(_f16_amihud(closeadj, volume, 63), 252)
    sl = base.diff(18) / float(18)
    deriv = sl.diff(18) / float(18)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_amihudrank63z_29d_jerk_v022_signal(closeadj, volume):
    base = _rank(_f16_amihud(closeadj, volume, 63), 252)
    sl = base.diff(29) / float(29)
    deriv = sl.diff(29) / float(29)
    result = _z(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_amihudrank63rank_50d_jerk_v023_signal(closeadj, volume):
    base = _rank(_f16_amihud(closeadj, volume, 63), 252)
    sl = base.diff(50) / float(50)
    deriv = sl.diff(50) / float(50)
    result = _rank(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_amihudrank63smag_76d_jerk_v024_signal(closeadj, volume):
    base = _rank(_f16_amihud(closeadj, volume, 63), 252)
    sl = base.diff(76) / float(76)
    deriv = sl.diff(76) / float(76)
    result = np.sign(deriv) * (deriv.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_amihudratioraw_26d_jerk_v025_signal(closeadj, volume):
    base = _f16_amihud(closeadj, volume, 21) / _f16_amihud(closeadj, volume, 126).replace(0, np.nan)
    sl = base.diff(26) / float(26)
    deriv = sl.diff(26) / float(26)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_amihudratioz_37d_jerk_v026_signal(closeadj, volume):
    base = _f16_amihud(closeadj, volume, 21) / _f16_amihud(closeadj, volume, 126).replace(0, np.nan)
    sl = base.diff(37) / float(37)
    deriv = sl.diff(37) / float(37)
    result = _z(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_amihudratiorank_58d_jerk_v027_signal(closeadj, volume):
    base = _f16_amihud(closeadj, volume, 21) / _f16_amihud(closeadj, volume, 126).replace(0, np.nan)
    sl = base.diff(58) / float(58)
    deriv = sl.diff(58) / float(58)
    result = _rank(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_amihudratiosmag_84d_jerk_v028_signal(closeadj, volume):
    base = _f16_amihud(closeadj, volume, 21) / _f16_amihud(closeadj, volume, 126).replace(0, np.nan)
    sl = base.diff(84) / float(84)
    deriv = sl.diff(84) / float(84)
    result = np.sign(deriv) * (deriv.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_illiqdispraw_41d_jerk_v029_signal(closeadj, volume):
    d = _f16_amihud_daily(closeadj, volume)
    base = d.rolling(63, min_periods=31).std() / d.rolling(63, min_periods=31).mean().replace(0, np.nan)
    sl = base.diff(41) / float(41)
    deriv = sl.diff(41) / float(41)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_illiqdispz_52d_jerk_v030_signal(closeadj, volume):
    d = _f16_amihud_daily(closeadj, volume)
    base = d.rolling(63, min_periods=31).std() / d.rolling(63, min_periods=31).mean().replace(0, np.nan)
    sl = base.diff(52) / float(52)
    deriv = sl.diff(52) / float(52)
    result = _z(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_illiqdisprank_73d_jerk_v031_signal(closeadj, volume):
    d = _f16_amihud_daily(closeadj, volume)
    base = d.rolling(63, min_periods=31).std() / d.rolling(63, min_periods=31).mean().replace(0, np.nan)
    sl = base.diff(73) / float(73)
    deriv = sl.diff(73) / float(73)
    result = _rank(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_illiqdispsmag_99d_jerk_v032_signal(closeadj, volume):
    d = _f16_amihud_daily(closeadj, volume)
    base = d.rolling(63, min_periods=31).std() / d.rolling(63, min_periods=31).mean().replace(0, np.nan)
    sl = base.diff(99) / float(99)
    deriv = sl.diff(99) / float(99)
    result = np.sign(deriv) * (deriv.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_illiqtailraw_12d_jerk_v033_signal(closeadj, volume):
    d = _f16_amihud_daily(closeadj, volume)
    q95 = d.rolling(126, min_periods=63).quantile(0.95)
    med = d.rolling(126, min_periods=63).median().replace(0, np.nan)
    base = np.log1p(q95 / med)
    sl = base.diff(12) / float(12)
    deriv = sl.diff(12) / float(12)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_illiqtailz_23d_jerk_v034_signal(closeadj, volume):
    d = _f16_amihud_daily(closeadj, volume)
    q95 = d.rolling(126, min_periods=63).quantile(0.95)
    med = d.rolling(126, min_periods=63).median().replace(0, np.nan)
    base = np.log1p(q95 / med)
    sl = base.diff(23) / float(23)
    deriv = sl.diff(23) / float(23)
    result = _z(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_illiqtailrank_44d_jerk_v035_signal(closeadj, volume):
    d = _f16_amihud_daily(closeadj, volume)
    q95 = d.rolling(126, min_periods=63).quantile(0.95)
    med = d.rolling(126, min_periods=63).median().replace(0, np.nan)
    base = np.log1p(q95 / med)
    sl = base.diff(44) / float(44)
    deriv = sl.diff(44) / float(44)
    result = _rank(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_illiqtailsmag_70d_jerk_v036_signal(closeadj, volume):
    d = _f16_amihud_daily(closeadj, volume)
    q95 = d.rolling(126, min_periods=63).quantile(0.95)
    med = d.rolling(126, min_periods=63).median().replace(0, np.nan)
    base = np.log1p(q95 / med)
    sl = base.diff(70) / float(70)
    deriv = sl.diff(70) / float(70)
    result = np.sign(deriv) * (deriv.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_amihudewmaraw_17d_jerk_v037_signal(closeadj, volume):
    d = np.log1p(_f16_amihud_daily(closeadj, volume))
    base = d.ewm(span=21, min_periods=10).mean() - d.ewm(span=126, min_periods=63).mean()
    sl = base.diff(17) / float(17)
    deriv = sl.diff(17) / float(17)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_amihudewmaz_28d_jerk_v038_signal(closeadj, volume):
    d = np.log1p(_f16_amihud_daily(closeadj, volume))
    base = d.ewm(span=21, min_periods=10).mean() - d.ewm(span=126, min_periods=63).mean()
    sl = base.diff(28) / float(28)
    deriv = sl.diff(28) / float(28)
    result = _z(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_amihudewmarank_49d_jerk_v039_signal(closeadj, volume):
    d = np.log1p(_f16_amihud_daily(closeadj, volume))
    base = d.ewm(span=21, min_periods=10).mean() - d.ewm(span=126, min_periods=63).mean()
    sl = base.diff(49) / float(49)
    deriv = sl.diff(49) / float(49)
    result = _rank(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_amihudewmasmag_75d_jerk_v040_signal(closeadj, volume):
    d = np.log1p(_f16_amihud_daily(closeadj, volume))
    base = d.ewm(span=21, min_periods=10).mean() - d.ewm(span=126, min_periods=63).mean()
    sl = base.diff(75) / float(75)
    deriv = sl.diff(75) / float(75)
    result = np.sign(deriv) * (deriv.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_amivest63raw_23d_jerk_v041_signal(closeadj, volume):
    base = np.log1p(_f16_amivest(closeadj, volume, 63))
    sl = base.diff(23) / float(23)
    deriv = sl.diff(23) / float(23)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_amivest63z_34d_jerk_v042_signal(closeadj, volume):
    base = np.log1p(_f16_amivest(closeadj, volume, 63))
    sl = base.diff(34) / float(34)
    deriv = sl.diff(34) / float(34)
    result = _z(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_amivest63rank_55d_jerk_v043_signal(closeadj, volume):
    base = np.log1p(_f16_amivest(closeadj, volume, 63))
    sl = base.diff(55) / float(55)
    deriv = sl.diff(55) / float(55)
    result = _rank(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_amivest63smag_81d_jerk_v044_signal(closeadj, volume):
    base = np.log1p(_f16_amivest(closeadj, volume, 63))
    sl = base.diff(81) / float(81)
    deriv = sl.diff(81) / float(81)
    result = np.sign(deriv) * (deriv.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_amivestrankraw_36d_jerk_v045_signal(closeadj, volume):
    base = _rank(_f16_amivest(closeadj, volume, 63), 504)
    sl = base.diff(36) / float(36)
    deriv = sl.diff(36) / float(36)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_amivestrankz_47d_jerk_v046_signal(closeadj, volume):
    base = _rank(_f16_amivest(closeadj, volume, 63), 504)
    sl = base.diff(47) / float(47)
    deriv = sl.diff(47) / float(47)
    result = _z(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_amivestrankrank_68d_jerk_v047_signal(closeadj, volume):
    base = _rank(_f16_amivest(closeadj, volume, 63), 504)
    sl = base.diff(68) / float(68)
    deriv = sl.diff(68) / float(68)
    result = _rank(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_amivestranksmag_94d_jerk_v048_signal(closeadj, volume):
    base = _rank(_f16_amivest(closeadj, volume, 63), 504)
    sl = base.diff(94) / float(94)
    deriv = sl.diff(94) / float(94)
    result = np.sign(deriv) * (deriv.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_kyle63raw_14d_jerk_v049_signal(closeadj, volume):
    base = np.log1p(_f16_kyle(closeadj, volume, 63))
    sl = base.diff(14) / float(14)
    deriv = sl.diff(14) / float(14)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_kyle63z_25d_jerk_v050_signal(closeadj, volume):
    base = np.log1p(_f16_kyle(closeadj, volume, 63))
    sl = base.diff(25) / float(25)
    deriv = sl.diff(25) / float(25)
    result = _z(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_kyle63rank_46d_jerk_v051_signal(closeadj, volume):
    base = np.log1p(_f16_kyle(closeadj, volume, 63))
    sl = base.diff(46) / float(46)
    deriv = sl.diff(46) / float(46)
    result = _rank(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_kyle63smag_72d_jerk_v052_signal(closeadj, volume):
    base = np.log1p(_f16_kyle(closeadj, volume, 63))
    sl = base.diff(72) / float(72)
    deriv = sl.diff(72) / float(72)
    result = np.sign(deriv) * (deriv.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_kyle126raw_19d_jerk_v053_signal(closeadj, volume):
    base = np.log1p(_f16_kyle(closeadj, volume, 126))
    sl = base.diff(19) / float(19)
    deriv = sl.diff(19) / float(19)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_kyle126z_30d_jerk_v054_signal(closeadj, volume):
    base = np.log1p(_f16_kyle(closeadj, volume, 126))
    sl = base.diff(30) / float(30)
    deriv = sl.diff(30) / float(30)
    result = _z(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_kyle126rank_51d_jerk_v055_signal(closeadj, volume):
    base = np.log1p(_f16_kyle(closeadj, volume, 126))
    sl = base.diff(51) / float(51)
    deriv = sl.diff(51) / float(51)
    result = _rank(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_kyle126smag_77d_jerk_v056_signal(closeadj, volume):
    base = np.log1p(_f16_kyle(closeadj, volume, 126))
    sl = base.diff(77) / float(77)
    deriv = sl.diff(77) / float(77)
    result = np.sign(deriv) * (deriv.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_kylezraw_29d_jerk_v057_signal(closeadj, volume):
    base = _z(np.log1p(_f16_kyle(closeadj, volume, 63)), 252)
    sl = base.diff(29) / float(29)
    deriv = sl.diff(29) / float(29)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_kylezz_40d_jerk_v058_signal(closeadj, volume):
    base = _z(np.log1p(_f16_kyle(closeadj, volume, 63)), 252)
    sl = base.diff(40) / float(40)
    deriv = sl.diff(40) / float(40)
    result = _z(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_kylezrank_61d_jerk_v059_signal(closeadj, volume):
    base = _z(np.log1p(_f16_kyle(closeadj, volume, 63)), 252)
    sl = base.diff(61) / float(61)
    deriv = sl.diff(61) / float(61)
    result = _rank(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_kylezsmag_87d_jerk_v060_signal(closeadj, volume):
    base = _z(np.log1p(_f16_kyle(closeadj, volume, 63)), 252)
    sl = base.diff(87) / float(87)
    deriv = sl.diff(87) / float(87)
    result = np.sign(deriv) * (deriv.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_illiqclusterraw_52d_jerk_v061_signal(closeadj, volume):
    d = np.log1p(_f16_amihud_daily(closeadj, volume))
    base = d.rolling(126, min_periods=63).corr(d.shift(1))
    sl = base.diff(52) / float(52)
    deriv = sl.diff(52) / float(52)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_illiqclusterz_63d_jerk_v062_signal(closeadj, volume):
    d = np.log1p(_f16_amihud_daily(closeadj, volume))
    base = d.rolling(126, min_periods=63).corr(d.shift(1))
    sl = base.diff(63) / float(63)
    deriv = sl.diff(63) / float(63)
    result = _z(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_illiqclusterrank_84d_jerk_v063_signal(closeadj, volume):
    d = np.log1p(_f16_amihud_daily(closeadj, volume))
    base = d.rolling(126, min_periods=63).corr(d.shift(1))
    sl = base.diff(84) / float(84)
    deriv = sl.diff(84) / float(84)
    result = _rank(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_illiqclustersmag_110d_jerk_v064_signal(closeadj, volume):
    d = np.log1p(_f16_amihud_daily(closeadj, volume))
    base = d.rolling(126, min_periods=63).corr(d.shift(1))
    sl = base.diff(110) / float(110)
    deriv = sl.diff(110) / float(110)
    result = np.sign(deriv) * (deriv.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_illiqpremraw_16d_jerk_v065_signal(closeadj, volume):
    a = np.log1p(_f16_amihud(closeadj, volume, 63))
    vol = _f16_logret(closeadj).rolling(63, min_periods=31).std()
    base = a / vol.replace(0, np.nan)
    sl = base.diff(16) / float(16)
    deriv = sl.diff(16) / float(16)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_illiqpremz_27d_jerk_v066_signal(closeadj, volume):
    a = np.log1p(_f16_amihud(closeadj, volume, 63))
    vol = _f16_logret(closeadj).rolling(63, min_periods=31).std()
    base = a / vol.replace(0, np.nan)
    sl = base.diff(27) / float(27)
    deriv = sl.diff(27) / float(27)
    result = _z(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_illiqpremrank_48d_jerk_v067_signal(closeadj, volume):
    a = np.log1p(_f16_amihud(closeadj, volume, 63))
    vol = _f16_logret(closeadj).rolling(63, min_periods=31).std()
    base = a / vol.replace(0, np.nan)
    sl = base.diff(48) / float(48)
    deriv = sl.diff(48) / float(48)
    result = _rank(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_illiqpremsmag_74d_jerk_v068_signal(closeadj, volume):
    a = np.log1p(_f16_amihud(closeadj, volume, 63))
    vol = _f16_logret(closeadj).rolling(63, min_periods=31).std()
    base = a / vol.replace(0, np.nan)
    sl = base.diff(74) / float(74)
    deriv = sl.diff(74) / float(74)
    result = np.sign(deriv) * (deriv.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_turnoverraw_22d_jerk_v069_signal(volume):
    base = np.log1p(_f16_turnover(volume, 63))
    sl = base.diff(22) / float(22)
    deriv = sl.diff(22) / float(22)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_turnoverz_33d_jerk_v070_signal(volume):
    base = np.log1p(_f16_turnover(volume, 63))
    sl = base.diff(33) / float(33)
    deriv = sl.diff(33) / float(33)
    result = _z(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_turnoverrank_54d_jerk_v071_signal(volume):
    base = np.log1p(_f16_turnover(volume, 63))
    sl = base.diff(54) / float(54)
    deriv = sl.diff(54) / float(54)
    result = _rank(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_turnoversmag_80d_jerk_v072_signal(volume):
    base = np.log1p(_f16_turnover(volume, 63))
    sl = base.diff(80) / float(80)
    deriv = sl.diff(80) / float(80)
    result = np.sign(deriv) * (deriv.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_turnzraw_33d_jerk_v073_signal(volume):
    base = _z(_f16_turnover(volume, 21).rolling(63, min_periods=31).mean(), 252)
    sl = base.diff(33) / float(33)
    deriv = sl.diff(33) / float(33)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_turnzz_44d_jerk_v074_signal(volume):
    base = _z(_f16_turnover(volume, 21).rolling(63, min_periods=31).mean(), 252)
    sl = base.diff(44) / float(44)
    deriv = sl.diff(44) / float(44)
    result = _z(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_turnzrank_65d_jerk_v075_signal(volume):
    base = _z(_f16_turnover(volume, 21).rolling(63, min_periods=31).mean(), 252)
    sl = base.diff(65) / float(65)
    deriv = sl.diff(65) / float(65)
    result = _rank(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_turnzsmag_91d_jerk_v076_signal(volume):
    base = _z(_f16_turnover(volume, 21).rolling(63, min_periods=31).mean(), 252)
    sl = base.diff(91) / float(91)
    deriv = sl.diff(91) / float(91)
    result = np.sign(deriv) * (deriv.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_turnrankraw_11d_jerk_v077_signal(volume):
    base = _rank(_f16_turnover(volume, 21).rolling(10, min_periods=5).mean(), 252)
    sl = base.diff(11) / float(11)
    deriv = sl.diff(11) / float(11)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_turnrankz_22d_jerk_v078_signal(volume):
    base = _rank(_f16_turnover(volume, 21).rolling(10, min_periods=5).mean(), 252)
    sl = base.diff(22) / float(22)
    deriv = sl.diff(22) / float(22)
    result = _z(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_turnrankrank_43d_jerk_v079_signal(volume):
    base = _rank(_f16_turnover(volume, 21).rolling(10, min_periods=5).mean(), 252)
    sl = base.diff(43) / float(43)
    deriv = sl.diff(43) / float(43)
    result = _rank(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_turnranksmag_69d_jerk_v080_signal(volume):
    base = _rank(_f16_turnover(volume, 21).rolling(10, min_periods=5).mean(), 252)
    sl = base.diff(69) / float(69)
    deriv = sl.diff(69) / float(69)
    result = np.sign(deriv) * (deriv.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_turnthinraw_20d_jerk_v081_signal(volume):
    t = _f16_turnover(volume, 21)
    base = ((1.0 - t).clip(lower=0) ** 1.5).rolling(63, min_periods=31).mean()
    sl = base.diff(20) / float(20)
    deriv = sl.diff(20) / float(20)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_turnthinz_31d_jerk_v082_signal(volume):
    t = _f16_turnover(volume, 21)
    base = ((1.0 - t).clip(lower=0) ** 1.5).rolling(63, min_periods=31).mean()
    sl = base.diff(31) / float(31)
    deriv = sl.diff(31) / float(31)
    result = _z(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_turnthinrank_52d_jerk_v083_signal(volume):
    t = _f16_turnover(volume, 21)
    base = ((1.0 - t).clip(lower=0) ** 1.5).rolling(63, min_periods=31).mean()
    sl = base.diff(52) / float(52)
    deriv = sl.diff(52) / float(52)
    result = _rank(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_turnthinsmag_78d_jerk_v084_signal(volume):
    t = _f16_turnover(volume, 21)
    base = ((1.0 - t).clip(lower=0) ** 1.5).rolling(63, min_periods=31).mean()
    sl = base.diff(78) / float(78)
    deriv = sl.diff(78) / float(78)
    result = np.sign(deriv) * (deriv.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_freezedepthraw_27d_jerk_v085_signal(volume):
    avg = _mean(volume, 252)
    base = (1.0 - volume / avg.replace(0, np.nan)).clip(lower=0).rolling(63, min_periods=31).mean()
    sl = base.diff(27) / float(27)
    deriv = sl.diff(27) / float(27)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_freezedepthz_38d_jerk_v086_signal(volume):
    avg = _mean(volume, 252)
    base = (1.0 - volume / avg.replace(0, np.nan)).clip(lower=0).rolling(63, min_periods=31).mean()
    sl = base.diff(38) / float(38)
    deriv = sl.diff(38) / float(38)
    result = _z(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_freezedepthrank_59d_jerk_v087_signal(volume):
    avg = _mean(volume, 252)
    base = (1.0 - volume / avg.replace(0, np.nan)).clip(lower=0).rolling(63, min_periods=31).mean()
    sl = base.diff(59) / float(59)
    deriv = sl.diff(59) / float(59)
    result = _rank(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_freezedepthsmag_85d_jerk_v088_signal(volume):
    avg = _mean(volume, 252)
    base = (1.0 - volume / avg.replace(0, np.nan)).clip(lower=0).rolling(63, min_periods=31).mean()
    sl = base.diff(85) / float(85)
    deriv = sl.diff(85) / float(85)
    result = np.sign(deriv) * (deriv.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_csspread21raw_43d_jerk_v089_signal(high, low):
    base = _f16_cs_spread(high, low).rolling(21, min_periods=10).mean()
    sl = base.diff(43) / float(43)
    deriv = sl.diff(43) / float(43)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_csspread21z_54d_jerk_v090_signal(high, low):
    base = _f16_cs_spread(high, low).rolling(21, min_periods=10).mean()
    sl = base.diff(54) / float(54)
    deriv = sl.diff(54) / float(54)
    result = _z(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_csspread21rank_75d_jerk_v091_signal(high, low):
    base = _f16_cs_spread(high, low).rolling(21, min_periods=10).mean()
    sl = base.diff(75) / float(75)
    deriv = sl.diff(75) / float(75)
    result = _rank(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_csspread21smag_101d_jerk_v092_signal(high, low):
    base = _f16_cs_spread(high, low).rolling(21, min_periods=10).mean()
    sl = base.diff(101) / float(101)
    deriv = sl.diff(101) / float(101)
    result = np.sign(deriv) * (deriv.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_csspread63raw_24d_jerk_v093_signal(high, low):
    base = _f16_cs_spread(high, low).rolling(63, min_periods=31).mean()
    sl = base.diff(24) / float(24)
    deriv = sl.diff(24) / float(24)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_csspread63z_35d_jerk_v094_signal(high, low):
    base = _f16_cs_spread(high, low).rolling(63, min_periods=31).mean()
    sl = base.diff(35) / float(35)
    deriv = sl.diff(35) / float(35)
    result = _z(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_csspread63rank_56d_jerk_v095_signal(high, low):
    base = _f16_cs_spread(high, low).rolling(63, min_periods=31).mean()
    sl = base.diff(56) / float(56)
    deriv = sl.diff(56) / float(56)
    result = _rank(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_csspread63smag_82d_jerk_v096_signal(high, low):
    base = _f16_cs_spread(high, low).rolling(63, min_periods=31).mean()
    sl = base.diff(82) / float(82)
    deriv = sl.diff(82) / float(82)
    result = np.sign(deriv) * (deriv.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_csspread126raw_30d_jerk_v097_signal(high, low):
    base = _f16_cs_spread(high, low).rolling(126, min_periods=63).mean()
    sl = base.diff(30) / float(30)
    deriv = sl.diff(30) / float(30)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_csspread126z_41d_jerk_v098_signal(high, low):
    base = _f16_cs_spread(high, low).rolling(126, min_periods=63).mean()
    sl = base.diff(41) / float(41)
    deriv = sl.diff(41) / float(41)
    result = _z(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_csspread126rank_62d_jerk_v099_signal(high, low):
    base = _f16_cs_spread(high, low).rolling(126, min_periods=63).mean()
    sl = base.diff(62) / float(62)
    deriv = sl.diff(62) / float(62)
    result = _rank(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_csspread126smag_88d_jerk_v100_signal(high, low):
    base = _f16_cs_spread(high, low).rolling(126, min_periods=63).mean()
    sl = base.diff(88) / float(88)
    deriv = sl.diff(88) / float(88)
    result = np.sign(deriv) * (deriv.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_csspreadzraw_38d_jerk_v101_signal(high, low):
    base = _z(_f16_cs_spread(high, low).rolling(21, min_periods=10).mean(), 252)
    sl = base.diff(38) / float(38)
    deriv = sl.diff(38) / float(38)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_csspreadzz_49d_jerk_v102_signal(high, low):
    base = _z(_f16_cs_spread(high, low).rolling(21, min_periods=10).mean(), 252)
    sl = base.diff(49) / float(49)
    deriv = sl.diff(49) / float(49)
    result = _z(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_csspreadzrank_70d_jerk_v103_signal(high, low):
    base = _z(_f16_cs_spread(high, low).rolling(21, min_periods=10).mean(), 252)
    sl = base.diff(70) / float(70)
    deriv = sl.diff(70) / float(70)
    result = _rank(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_csspreadzsmag_96d_jerk_v104_signal(high, low):
    base = _z(_f16_cs_spread(high, low).rolling(21, min_periods=10).mean(), 252)
    sl = base.diff(96) / float(96)
    deriv = sl.diff(96) / float(96)
    result = np.sign(deriv) * (deriv.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_csspreadrankraw_25d_jerk_v105_signal(high, low):
    base = _rank(_f16_cs_spread(high, low).rolling(21, min_periods=10).mean(), 252)
    sl = base.diff(25) / float(25)
    deriv = sl.diff(25) / float(25)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_csspreadrankz_36d_jerk_v106_signal(high, low):
    base = _rank(_f16_cs_spread(high, low).rolling(21, min_periods=10).mean(), 252)
    sl = base.diff(36) / float(36)
    deriv = sl.diff(36) / float(36)
    result = _z(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_csspreadrankrank_57d_jerk_v107_signal(high, low):
    base = _rank(_f16_cs_spread(high, low).rolling(21, min_periods=10).mean(), 252)
    sl = base.diff(57) / float(57)
    deriv = sl.diff(57) / float(57)
    result = _rank(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_csspreadranksmag_83d_jerk_v108_signal(high, low):
    base = _rank(_f16_cs_spread(high, low).rolling(21, min_periods=10).mean(), 252)
    sl = base.diff(83) / float(83)
    deriv = sl.diff(83) / float(83)
    result = np.sign(deriv) * (deriv.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_csspreadratioraw_34d_jerk_v109_signal(high, low):
    s = _f16_cs_spread(high, low)
    base = s.rolling(21, min_periods=10).mean() / s.rolling(126, min_periods=63).mean().replace(0, np.nan)
    sl = base.diff(34) / float(34)
    deriv = sl.diff(34) / float(34)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_csspreadratioz_45d_jerk_v110_signal(high, low):
    s = _f16_cs_spread(high, low)
    base = s.rolling(21, min_periods=10).mean() / s.rolling(126, min_periods=63).mean().replace(0, np.nan)
    sl = base.diff(45) / float(45)
    deriv = sl.diff(45) / float(45)
    result = _z(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_csspreadratiorank_66d_jerk_v111_signal(high, low):
    s = _f16_cs_spread(high, low)
    base = s.rolling(21, min_periods=10).mean() / s.rolling(126, min_periods=63).mean().replace(0, np.nan)
    sl = base.diff(66) / float(66)
    deriv = sl.diff(66) / float(66)
    result = _rank(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_csspreadratiosmag_92d_jerk_v112_signal(high, low):
    s = _f16_cs_spread(high, low)
    base = s.rolling(21, min_periods=10).mean() / s.rolling(126, min_periods=63).mean().replace(0, np.nan)
    sl = base.diff(92) / float(92)
    deriv = sl.diff(92) / float(92)
    result = np.sign(deriv) * (deriv.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_rollspread63raw_48d_jerk_v113_signal(closeadj):
    base = _f16_roll_spread(closeadj, 63)
    sl = base.diff(48) / float(48)
    deriv = sl.diff(48) / float(48)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_rollspread63z_59d_jerk_v114_signal(closeadj):
    base = _f16_roll_spread(closeadj, 63)
    sl = base.diff(59) / float(59)
    deriv = sl.diff(59) / float(59)
    result = _z(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_rollspread63rank_80d_jerk_v115_signal(closeadj):
    base = _f16_roll_spread(closeadj, 63)
    sl = base.diff(80) / float(80)
    deriv = sl.diff(80) / float(80)
    result = _rank(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_rollspread63smag_106d_jerk_v116_signal(closeadj):
    base = _f16_roll_spread(closeadj, 63)
    sl = base.diff(106) / float(106)
    deriv = sl.diff(106) / float(106)
    result = np.sign(deriv) * (deriv.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_rollspread126raw_28d_jerk_v117_signal(closeadj):
    base = _f16_roll_spread(closeadj, 126)
    sl = base.diff(28) / float(28)
    deriv = sl.diff(28) / float(28)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_rollspread126z_39d_jerk_v118_signal(closeadj):
    base = _f16_roll_spread(closeadj, 126)
    sl = base.diff(39) / float(39)
    deriv = sl.diff(39) / float(39)
    result = _z(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_rollspread126rank_60d_jerk_v119_signal(closeadj):
    base = _f16_roll_spread(closeadj, 126)
    sl = base.diff(60) / float(60)
    deriv = sl.diff(60) / float(60)
    result = _rank(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_rollspread126smag_86d_jerk_v120_signal(closeadj):
    base = _f16_roll_spread(closeadj, 126)
    sl = base.diff(86) / float(86)
    deriv = sl.diff(86) / float(86)
    result = np.sign(deriv) * (deriv.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_rollspreadzraw_37d_jerk_v121_signal(closeadj):
    base = _z(_f16_roll_spread(closeadj, 63), 252)
    sl = base.diff(37) / float(37)
    deriv = sl.diff(37) / float(37)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_rollspreadzz_48d_jerk_v122_signal(closeadj):
    base = _z(_f16_roll_spread(closeadj, 63), 252)
    sl = base.diff(48) / float(48)
    deriv = sl.diff(48) / float(48)
    result = _z(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_rollspreadzrank_69d_jerk_v123_signal(closeadj):
    base = _z(_f16_roll_spread(closeadj, 63), 252)
    sl = base.diff(69) / float(69)
    deriv = sl.diff(69) / float(69)
    result = _rank(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_rollspreadzsmag_95d_jerk_v124_signal(closeadj):
    base = _z(_f16_roll_spread(closeadj, 63), 252)
    sl = base.diff(95) / float(95)
    deriv = sl.diff(95) / float(95)
    result = np.sign(deriv) * (deriv.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_retac1raw_57d_jerk_v125_signal(closeadj):
    r = _f16_logret(closeadj)
    base = -r.rolling(63, min_periods=31).corr(r.shift(1))
    sl = base.diff(57) / float(57)
    deriv = sl.diff(57) / float(57)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_retac1z_68d_jerk_v126_signal(closeadj):
    r = _f16_logret(closeadj)
    base = -r.rolling(63, min_periods=31).corr(r.shift(1))
    sl = base.diff(68) / float(68)
    deriv = sl.diff(68) / float(68)
    result = _z(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_retac1rank_89d_jerk_v127_signal(closeadj):
    r = _f16_logret(closeadj)
    base = -r.rolling(63, min_periods=31).corr(r.shift(1))
    sl = base.diff(89) / float(89)
    deriv = sl.diff(89) / float(89)
    result = _rank(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_retac1smag_115d_jerk_v128_signal(closeadj):
    r = _f16_logret(closeadj)
    base = -r.rolling(63, min_periods=31).corr(r.shift(1))
    sl = base.diff(115) / float(115)
    deriv = sl.diff(115) / float(115)
    result = np.sign(deriv) * (deriv.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_staleretraw_32d_jerk_v129_signal(closeadj):
    r = _f16_logret(closeadj).abs()
    typ = r.rolling(252, min_periods=126).median().replace(0, np.nan)
    base = (1.0 - r / typ).clip(lower=0).rolling(63, min_periods=31).mean()
    sl = base.diff(32) / float(32)
    deriv = sl.diff(32) / float(32)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_staleretz_43d_jerk_v130_signal(closeadj):
    r = _f16_logret(closeadj).abs()
    typ = r.rolling(252, min_periods=126).median().replace(0, np.nan)
    base = (1.0 - r / typ).clip(lower=0).rolling(63, min_periods=31).mean()
    sl = base.diff(43) / float(43)
    deriv = sl.diff(43) / float(43)
    result = _z(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_staleretrank_64d_jerk_v131_signal(closeadj):
    r = _f16_logret(closeadj).abs()
    typ = r.rolling(252, min_periods=126).median().replace(0, np.nan)
    base = (1.0 - r / typ).clip(lower=0).rolling(63, min_periods=31).mean()
    sl = base.diff(64) / float(64)
    deriv = sl.diff(64) / float(64)
    result = _rank(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_staleretsmag_90d_jerk_v132_signal(closeadj):
    r = _f16_logret(closeadj).abs()
    typ = r.rolling(252, min_periods=126).median().replace(0, np.nan)
    base = (1.0 - r / typ).clip(lower=0).rolling(63, min_periods=31).mean()
    sl = base.diff(90) / float(90)
    deriv = sl.diff(90) / float(90)
    result = np.sign(deriv) * (deriv.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_varratioraw_40d_jerk_v133_signal(closeadj):
    r = _f16_logret(closeadj)
    v1 = r.rolling(126, min_periods=63).var()
    r5 = np.log(closeadj.replace(0, np.nan) / closeadj.shift(5).replace(0, np.nan))
    v5 = r5.rolling(126, min_periods=63).var()
    base = v5 / (5.0 * v1).replace(0, np.nan) - 1.0
    sl = base.diff(40) / float(40)
    deriv = sl.diff(40) / float(40)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_varratioz_51d_jerk_v134_signal(closeadj):
    r = _f16_logret(closeadj)
    v1 = r.rolling(126, min_periods=63).var()
    r5 = np.log(closeadj.replace(0, np.nan) / closeadj.shift(5).replace(0, np.nan))
    v5 = r5.rolling(126, min_periods=63).var()
    base = v5 / (5.0 * v1).replace(0, np.nan) - 1.0
    sl = base.diff(51) / float(51)
    deriv = sl.diff(51) / float(51)
    result = _z(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_varratiorank_72d_jerk_v135_signal(closeadj):
    r = _f16_logret(closeadj)
    v1 = r.rolling(126, min_periods=63).var()
    r5 = np.log(closeadj.replace(0, np.nan) / closeadj.shift(5).replace(0, np.nan))
    v5 = r5.rolling(126, min_periods=63).var()
    base = v5 / (5.0 * v1).replace(0, np.nan) - 1.0
    sl = base.diff(72) / float(72)
    deriv = sl.diff(72) / float(72)
    result = _rank(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_varratiosmag_98d_jerk_v136_signal(closeadj):
    r = _f16_logret(closeadj)
    v1 = r.rolling(126, min_periods=63).var()
    r5 = np.log(closeadj.replace(0, np.nan) / closeadj.shift(5).replace(0, np.nan))
    v5 = r5.rolling(126, min_periods=63).var()
    base = v5 / (5.0 * v1).replace(0, np.nan) - 1.0
    sl = base.diff(98) / float(98)
    deriv = sl.diff(98) / float(98)
    result = np.sign(deriv) * (deriv.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_spreadpervolraw_63d_jerk_v137_signal(high, low, closeadj):
    sp = _f16_cs_spread(high, low).rolling(21, min_periods=10).mean()
    vol = _f16_logret(closeadj).rolling(63, min_periods=31).std()
    base = sp / vol.replace(0, np.nan)
    sl = base.diff(63) / float(63)
    deriv = sl.diff(63) / float(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_spreadpervolz_74d_jerk_v138_signal(high, low, closeadj):
    sp = _f16_cs_spread(high, low).rolling(21, min_periods=10).mean()
    vol = _f16_logret(closeadj).rolling(63, min_periods=31).std()
    base = sp / vol.replace(0, np.nan)
    sl = base.diff(74) / float(74)
    deriv = sl.diff(74) / float(74)
    result = _z(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_spreadpervolrank_95d_jerk_v139_signal(high, low, closeadj):
    sp = _f16_cs_spread(high, low).rolling(21, min_periods=10).mean()
    vol = _f16_logret(closeadj).rolling(63, min_periods=31).std()
    base = sp / vol.replace(0, np.nan)
    sl = base.diff(95) / float(95)
    deriv = sl.diff(95) / float(95)
    result = _rank(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_spreadpervolsmag_121d_jerk_v140_signal(high, low, closeadj):
    sp = _f16_cs_spread(high, low).rolling(21, min_periods=10).mean()
    vol = _f16_logret(closeadj).rolling(63, min_periods=31).std()
    base = sp / vol.replace(0, np.nan)
    sl = base.diff(121) / float(121)
    deriv = sl.diff(121) / float(121)
    result = np.sign(deriv) * (deriv.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_costtriadraw_35d_jerk_v141_signal(closeadj, volume, high, low):
    ra = _rank(_f16_amihud(closeadj, volume, 63), 252)
    rc = _rank(_f16_cs_spread(high, low).rolling(21, min_periods=10).mean(), 252)
    rr = _rank(_f16_roll_spread(closeadj, 63), 252)
    base = (ra + rc + rr) / 3.0
    sl = base.diff(35) / float(35)
    deriv = sl.diff(35) / float(35)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_costtriadz_46d_jerk_v142_signal(closeadj, volume, high, low):
    ra = _rank(_f16_amihud(closeadj, volume, 63), 252)
    rc = _rank(_f16_cs_spread(high, low).rolling(21, min_periods=10).mean(), 252)
    rr = _rank(_f16_roll_spread(closeadj, 63), 252)
    base = (ra + rc + rr) / 3.0
    sl = base.diff(46) / float(46)
    deriv = sl.diff(46) / float(46)
    result = _z(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_costtriadrank_67d_jerk_v143_signal(closeadj, volume, high, low):
    ra = _rank(_f16_amihud(closeadj, volume, 63), 252)
    rc = _rank(_f16_cs_spread(high, low).rolling(21, min_periods=10).mean(), 252)
    rr = _rank(_f16_roll_spread(closeadj, 63), 252)
    base = (ra + rc + rr) / 3.0
    sl = base.diff(67) / float(67)
    deriv = sl.diff(67) / float(67)
    result = _rank(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_costtriadsmag_93d_jerk_v144_signal(closeadj, volume, high, low):
    ra = _rank(_f16_amihud(closeadj, volume, 63), 252)
    rc = _rank(_f16_cs_spread(high, low).rolling(21, min_periods=10).mean(), 252)
    rr = _rank(_f16_roll_spread(closeadj, 63), 252)
    base = (ra + rc + rr) / 3.0
    sl = base.diff(93) / float(93)
    deriv = sl.diff(93) / float(93)
    result = np.sign(deriv) * (deriv.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_illiqchronicraw_45d_jerk_v145_signal(closeadj, volume):
    a = _f16_amihud(closeadj, volume, 21)
    med = a.rolling(504, min_periods=252).median()
    base = (a > med).astype(float).rolling(252, min_periods=126).mean() - 0.5
    sl = base.diff(45) / float(45)
    deriv = sl.diff(45) / float(45)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_illiqchronicz_56d_jerk_v146_signal(closeadj, volume):
    a = _f16_amihud(closeadj, volume, 21)
    med = a.rolling(504, min_periods=252).median()
    base = (a > med).astype(float).rolling(252, min_periods=126).mean() - 0.5
    sl = base.diff(56) / float(56)
    deriv = sl.diff(56) / float(56)
    result = _z(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_illiqchronicrank_77d_jerk_v147_signal(closeadj, volume):
    a = _f16_amihud(closeadj, volume, 21)
    med = a.rolling(504, min_periods=252).median()
    base = (a > med).astype(float).rolling(252, min_periods=126).mean() - 0.5
    sl = base.diff(77) / float(77)
    deriv = sl.diff(77) / float(77)
    result = _rank(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_illiqchronicsmag_103d_jerk_v148_signal(closeadj, volume):
    a = _f16_amihud(closeadj, volume, 21)
    med = a.rolling(504, min_periods=252).median()
    base = (a > med).astype(float).rolling(252, min_periods=126).mean() - 0.5
    sl = base.diff(103) / float(103)
    deriv = sl.diff(103) / float(103)
    result = np.sign(deriv) * (deriv.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_paidcostraw_73d_jerk_v149_signal(high, low, volume):
    sp = np.log1p(_f16_cs_spread(high, low).rolling(5, min_periods=3).mean())
    turn = np.log1p(_f16_turnover(volume, 21))
    base = sp.rolling(63, min_periods=31).corr(turn)
    sl = base.diff(73) / float(73)
    deriv = sl.diff(73) / float(73)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)
def f16lq_f16_liquidity_profile_paidcostz_84d_jerk_v150_signal(high, low, volume):
    sp = np.log1p(_f16_cs_spread(high, low).rolling(5, min_periods=3).mean())
    turn = np.log1p(_f16_turnover(volume, 21))
    base = sp.rolling(63, min_periods=31).corr(turn)
    sl = base.diff(84) / float(84)
    deriv = sl.diff(84) / float(84)
    result = _z(deriv, 252)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f16lq_f16_liquidity_profile_amihud21raw_10d_jerk_v001_signal,
    f16lq_f16_liquidity_profile_amihud21z_21d_jerk_v002_signal,
    f16lq_f16_liquidity_profile_amihud21rank_42d_jerk_v003_signal,
    f16lq_f16_liquidity_profile_amihud21smag_68d_jerk_v004_signal,
    f16lq_f16_liquidity_profile_amihud63raw_15d_jerk_v005_signal,
    f16lq_f16_liquidity_profile_amihud63z_26d_jerk_v006_signal,
    f16lq_f16_liquidity_profile_amihud63rank_47d_jerk_v007_signal,
    f16lq_f16_liquidity_profile_amihud63smag_73d_jerk_v008_signal,
    f16lq_f16_liquidity_profile_amihud126raw_21d_jerk_v009_signal,
    f16lq_f16_liquidity_profile_amihud126z_32d_jerk_v010_signal,
    f16lq_f16_liquidity_profile_amihud126rank_53d_jerk_v011_signal,
    f16lq_f16_liquidity_profile_amihud126smag_79d_jerk_v012_signal,
    f16lq_f16_liquidity_profile_amihud252raw_31d_jerk_v013_signal,
    f16lq_f16_liquidity_profile_amihud252z_42d_jerk_v014_signal,
    f16lq_f16_liquidity_profile_amihud252rank_63d_jerk_v015_signal,
    f16lq_f16_liquidity_profile_amihud252smag_89d_jerk_v016_signal,
    f16lq_f16_liquidity_profile_amihudz63raw_13d_jerk_v017_signal,
    f16lq_f16_liquidity_profile_amihudz63z_24d_jerk_v018_signal,
    f16lq_f16_liquidity_profile_amihudz63rank_45d_jerk_v019_signal,
    f16lq_f16_liquidity_profile_amihudz63smag_71d_jerk_v020_signal,
    f16lq_f16_liquidity_profile_amihudrank63raw_18d_jerk_v021_signal,
    f16lq_f16_liquidity_profile_amihudrank63z_29d_jerk_v022_signal,
    f16lq_f16_liquidity_profile_amihudrank63rank_50d_jerk_v023_signal,
    f16lq_f16_liquidity_profile_amihudrank63smag_76d_jerk_v024_signal,
    f16lq_f16_liquidity_profile_amihudratioraw_26d_jerk_v025_signal,
    f16lq_f16_liquidity_profile_amihudratioz_37d_jerk_v026_signal,
    f16lq_f16_liquidity_profile_amihudratiorank_58d_jerk_v027_signal,
    f16lq_f16_liquidity_profile_amihudratiosmag_84d_jerk_v028_signal,
    f16lq_f16_liquidity_profile_illiqdispraw_41d_jerk_v029_signal,
    f16lq_f16_liquidity_profile_illiqdispz_52d_jerk_v030_signal,
    f16lq_f16_liquidity_profile_illiqdisprank_73d_jerk_v031_signal,
    f16lq_f16_liquidity_profile_illiqdispsmag_99d_jerk_v032_signal,
    f16lq_f16_liquidity_profile_illiqtailraw_12d_jerk_v033_signal,
    f16lq_f16_liquidity_profile_illiqtailz_23d_jerk_v034_signal,
    f16lq_f16_liquidity_profile_illiqtailrank_44d_jerk_v035_signal,
    f16lq_f16_liquidity_profile_illiqtailsmag_70d_jerk_v036_signal,
    f16lq_f16_liquidity_profile_amihudewmaraw_17d_jerk_v037_signal,
    f16lq_f16_liquidity_profile_amihudewmaz_28d_jerk_v038_signal,
    f16lq_f16_liquidity_profile_amihudewmarank_49d_jerk_v039_signal,
    f16lq_f16_liquidity_profile_amihudewmasmag_75d_jerk_v040_signal,
    f16lq_f16_liquidity_profile_amivest63raw_23d_jerk_v041_signal,
    f16lq_f16_liquidity_profile_amivest63z_34d_jerk_v042_signal,
    f16lq_f16_liquidity_profile_amivest63rank_55d_jerk_v043_signal,
    f16lq_f16_liquidity_profile_amivest63smag_81d_jerk_v044_signal,
    f16lq_f16_liquidity_profile_amivestrankraw_36d_jerk_v045_signal,
    f16lq_f16_liquidity_profile_amivestrankz_47d_jerk_v046_signal,
    f16lq_f16_liquidity_profile_amivestrankrank_68d_jerk_v047_signal,
    f16lq_f16_liquidity_profile_amivestranksmag_94d_jerk_v048_signal,
    f16lq_f16_liquidity_profile_kyle63raw_14d_jerk_v049_signal,
    f16lq_f16_liquidity_profile_kyle63z_25d_jerk_v050_signal,
    f16lq_f16_liquidity_profile_kyle63rank_46d_jerk_v051_signal,
    f16lq_f16_liquidity_profile_kyle63smag_72d_jerk_v052_signal,
    f16lq_f16_liquidity_profile_kyle126raw_19d_jerk_v053_signal,
    f16lq_f16_liquidity_profile_kyle126z_30d_jerk_v054_signal,
    f16lq_f16_liquidity_profile_kyle126rank_51d_jerk_v055_signal,
    f16lq_f16_liquidity_profile_kyle126smag_77d_jerk_v056_signal,
    f16lq_f16_liquidity_profile_kylezraw_29d_jerk_v057_signal,
    f16lq_f16_liquidity_profile_kylezz_40d_jerk_v058_signal,
    f16lq_f16_liquidity_profile_kylezrank_61d_jerk_v059_signal,
    f16lq_f16_liquidity_profile_kylezsmag_87d_jerk_v060_signal,
    f16lq_f16_liquidity_profile_illiqclusterraw_52d_jerk_v061_signal,
    f16lq_f16_liquidity_profile_illiqclusterz_63d_jerk_v062_signal,
    f16lq_f16_liquidity_profile_illiqclusterrank_84d_jerk_v063_signal,
    f16lq_f16_liquidity_profile_illiqclustersmag_110d_jerk_v064_signal,
    f16lq_f16_liquidity_profile_illiqpremraw_16d_jerk_v065_signal,
    f16lq_f16_liquidity_profile_illiqpremz_27d_jerk_v066_signal,
    f16lq_f16_liquidity_profile_illiqpremrank_48d_jerk_v067_signal,
    f16lq_f16_liquidity_profile_illiqpremsmag_74d_jerk_v068_signal,
    f16lq_f16_liquidity_profile_turnoverraw_22d_jerk_v069_signal,
    f16lq_f16_liquidity_profile_turnoverz_33d_jerk_v070_signal,
    f16lq_f16_liquidity_profile_turnoverrank_54d_jerk_v071_signal,
    f16lq_f16_liquidity_profile_turnoversmag_80d_jerk_v072_signal,
    f16lq_f16_liquidity_profile_turnzraw_33d_jerk_v073_signal,
    f16lq_f16_liquidity_profile_turnzz_44d_jerk_v074_signal,
    f16lq_f16_liquidity_profile_turnzrank_65d_jerk_v075_signal,
    f16lq_f16_liquidity_profile_turnzsmag_91d_jerk_v076_signal,
    f16lq_f16_liquidity_profile_turnrankraw_11d_jerk_v077_signal,
    f16lq_f16_liquidity_profile_turnrankz_22d_jerk_v078_signal,
    f16lq_f16_liquidity_profile_turnrankrank_43d_jerk_v079_signal,
    f16lq_f16_liquidity_profile_turnranksmag_69d_jerk_v080_signal,
    f16lq_f16_liquidity_profile_turnthinraw_20d_jerk_v081_signal,
    f16lq_f16_liquidity_profile_turnthinz_31d_jerk_v082_signal,
    f16lq_f16_liquidity_profile_turnthinrank_52d_jerk_v083_signal,
    f16lq_f16_liquidity_profile_turnthinsmag_78d_jerk_v084_signal,
    f16lq_f16_liquidity_profile_freezedepthraw_27d_jerk_v085_signal,
    f16lq_f16_liquidity_profile_freezedepthz_38d_jerk_v086_signal,
    f16lq_f16_liquidity_profile_freezedepthrank_59d_jerk_v087_signal,
    f16lq_f16_liquidity_profile_freezedepthsmag_85d_jerk_v088_signal,
    f16lq_f16_liquidity_profile_csspread21raw_43d_jerk_v089_signal,
    f16lq_f16_liquidity_profile_csspread21z_54d_jerk_v090_signal,
    f16lq_f16_liquidity_profile_csspread21rank_75d_jerk_v091_signal,
    f16lq_f16_liquidity_profile_csspread21smag_101d_jerk_v092_signal,
    f16lq_f16_liquidity_profile_csspread63raw_24d_jerk_v093_signal,
    f16lq_f16_liquidity_profile_csspread63z_35d_jerk_v094_signal,
    f16lq_f16_liquidity_profile_csspread63rank_56d_jerk_v095_signal,
    f16lq_f16_liquidity_profile_csspread63smag_82d_jerk_v096_signal,
    f16lq_f16_liquidity_profile_csspread126raw_30d_jerk_v097_signal,
    f16lq_f16_liquidity_profile_csspread126z_41d_jerk_v098_signal,
    f16lq_f16_liquidity_profile_csspread126rank_62d_jerk_v099_signal,
    f16lq_f16_liquidity_profile_csspread126smag_88d_jerk_v100_signal,
    f16lq_f16_liquidity_profile_csspreadzraw_38d_jerk_v101_signal,
    f16lq_f16_liquidity_profile_csspreadzz_49d_jerk_v102_signal,
    f16lq_f16_liquidity_profile_csspreadzrank_70d_jerk_v103_signal,
    f16lq_f16_liquidity_profile_csspreadzsmag_96d_jerk_v104_signal,
    f16lq_f16_liquidity_profile_csspreadrankraw_25d_jerk_v105_signal,
    f16lq_f16_liquidity_profile_csspreadrankz_36d_jerk_v106_signal,
    f16lq_f16_liquidity_profile_csspreadrankrank_57d_jerk_v107_signal,
    f16lq_f16_liquidity_profile_csspreadranksmag_83d_jerk_v108_signal,
    f16lq_f16_liquidity_profile_csspreadratioraw_34d_jerk_v109_signal,
    f16lq_f16_liquidity_profile_csspreadratioz_45d_jerk_v110_signal,
    f16lq_f16_liquidity_profile_csspreadratiorank_66d_jerk_v111_signal,
    f16lq_f16_liquidity_profile_csspreadratiosmag_92d_jerk_v112_signal,
    f16lq_f16_liquidity_profile_rollspread63raw_48d_jerk_v113_signal,
    f16lq_f16_liquidity_profile_rollspread63z_59d_jerk_v114_signal,
    f16lq_f16_liquidity_profile_rollspread63rank_80d_jerk_v115_signal,
    f16lq_f16_liquidity_profile_rollspread63smag_106d_jerk_v116_signal,
    f16lq_f16_liquidity_profile_rollspread126raw_28d_jerk_v117_signal,
    f16lq_f16_liquidity_profile_rollspread126z_39d_jerk_v118_signal,
    f16lq_f16_liquidity_profile_rollspread126rank_60d_jerk_v119_signal,
    f16lq_f16_liquidity_profile_rollspread126smag_86d_jerk_v120_signal,
    f16lq_f16_liquidity_profile_rollspreadzraw_37d_jerk_v121_signal,
    f16lq_f16_liquidity_profile_rollspreadzz_48d_jerk_v122_signal,
    f16lq_f16_liquidity_profile_rollspreadzrank_69d_jerk_v123_signal,
    f16lq_f16_liquidity_profile_rollspreadzsmag_95d_jerk_v124_signal,
    f16lq_f16_liquidity_profile_retac1raw_57d_jerk_v125_signal,
    f16lq_f16_liquidity_profile_retac1z_68d_jerk_v126_signal,
    f16lq_f16_liquidity_profile_retac1rank_89d_jerk_v127_signal,
    f16lq_f16_liquidity_profile_retac1smag_115d_jerk_v128_signal,
    f16lq_f16_liquidity_profile_staleretraw_32d_jerk_v129_signal,
    f16lq_f16_liquidity_profile_staleretz_43d_jerk_v130_signal,
    f16lq_f16_liquidity_profile_staleretrank_64d_jerk_v131_signal,
    f16lq_f16_liquidity_profile_staleretsmag_90d_jerk_v132_signal,
    f16lq_f16_liquidity_profile_varratioraw_40d_jerk_v133_signal,
    f16lq_f16_liquidity_profile_varratioz_51d_jerk_v134_signal,
    f16lq_f16_liquidity_profile_varratiorank_72d_jerk_v135_signal,
    f16lq_f16_liquidity_profile_varratiosmag_98d_jerk_v136_signal,
    f16lq_f16_liquidity_profile_spreadpervolraw_63d_jerk_v137_signal,
    f16lq_f16_liquidity_profile_spreadpervolz_74d_jerk_v138_signal,
    f16lq_f16_liquidity_profile_spreadpervolrank_95d_jerk_v139_signal,
    f16lq_f16_liquidity_profile_spreadpervolsmag_121d_jerk_v140_signal,
    f16lq_f16_liquidity_profile_costtriadraw_35d_jerk_v141_signal,
    f16lq_f16_liquidity_profile_costtriadz_46d_jerk_v142_signal,
    f16lq_f16_liquidity_profile_costtriadrank_67d_jerk_v143_signal,
    f16lq_f16_liquidity_profile_costtriadsmag_93d_jerk_v144_signal,
    f16lq_f16_liquidity_profile_illiqchronicraw_45d_jerk_v145_signal,
    f16lq_f16_liquidity_profile_illiqchronicz_56d_jerk_v146_signal,
    f16lq_f16_liquidity_profile_illiqchronicrank_77d_jerk_v147_signal,
    f16lq_f16_liquidity_profile_illiqchronicsmag_103d_jerk_v148_signal,
    f16lq_f16_liquidity_profile_paidcostraw_73d_jerk_v149_signal,
    f16lq_f16_liquidity_profile_paidcostz_84d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F16_LIQUIDITY_PROFILE_REGISTRY_001_150 = REGISTRY


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

    print("OK f16_liquidity_profile_3rd_derivatives_001_150_claude: %d features pass" % n_features)
