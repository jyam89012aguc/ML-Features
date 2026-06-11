import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
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


def _diff(s, n):
    return s.diff(periods=n)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


def _f02_roe_proxy(netinc, equity):
    return netinc / equity.replace(0, np.nan)


def _f02_roe_dynamics(netinc, equity, w):
    roe = netinc / equity.replace(0, np.nan)
    return roe - roe.rolling(w, min_periods=max(1, w // 2)).mean()


def _f02_roe_durability(roe, w):
    m = roe.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = roe.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan)


def f02arp_f02_allowed_roe_proxy_proxy_5d_jerk_v001_signal(netinc, equity, closeadj):
    base = _mean(_f02_roe_proxy(netinc, equity), 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_proxy_5d_jerk_v002_signal(netinc, equity, closeadj):
    base = _mean(_f02_roe_proxy(netinc, equity), 5) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_proxy_21d_jerk_v003_signal(netinc, equity, closeadj):
    base = _mean(_f02_roe_proxy(netinc, equity), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_proxy_21d_jerk_v004_signal(netinc, equity, closeadj):
    base = _mean(_f02_roe_proxy(netinc, equity), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_proxy_21d_jerk_v005_signal(netinc, equity, closeadj):
    base = _mean(_f02_roe_proxy(netinc, equity), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_proxy_63d_jerk_v006_signal(netinc, equity, closeadj):
    base = _mean(_f02_roe_proxy(netinc, equity), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_proxy_63d_jerk_v007_signal(netinc, equity, closeadj):
    base = _mean(_f02_roe_proxy(netinc, equity), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_proxy_63d_jerk_v008_signal(netinc, equity, closeadj):
    base = _mean(_f02_roe_proxy(netinc, equity), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_proxy_126d_jerk_v009_signal(netinc, equity, closeadj):
    base = _mean(_f02_roe_proxy(netinc, equity), 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_proxy_126d_jerk_v010_signal(netinc, equity, closeadj):
    base = _mean(_f02_roe_proxy(netinc, equity), 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_proxy_252d_jerk_v011_signal(netinc, equity, closeadj):
    base = _mean(_f02_roe_proxy(netinc, equity), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_proxy_252d_jerk_v012_signal(netinc, equity, closeadj):
    base = _mean(_f02_roe_proxy(netinc, equity), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_proxy_252d_jerk_v013_signal(netinc, equity, closeadj):
    base = _mean(_f02_roe_proxy(netinc, equity), 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_proxy_504d_jerk_v014_signal(netinc, equity, closeadj):
    base = _mean(_f02_roe_proxy(netinc, equity), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_proxy_504d_jerk_v015_signal(netinc, equity, closeadj):
    base = _mean(_f02_roe_proxy(netinc, equity), 504) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# Dyn jerks
def f02arp_f02_allowed_roe_proxy_dyn_21d_jerk_v016_signal(netinc, equity, closeadj):
    base = _f02_roe_dynamics(netinc, equity, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dyn_21d_jerk_v017_signal(netinc, equity, closeadj):
    base = _f02_roe_dynamics(netinc, equity, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dyn_63d_jerk_v018_signal(netinc, equity, closeadj):
    base = _f02_roe_dynamics(netinc, equity, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dyn_63d_jerk_v019_signal(netinc, equity, closeadj):
    base = _f02_roe_dynamics(netinc, equity, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dyn_126d_jerk_v020_signal(netinc, equity, closeadj):
    base = _f02_roe_dynamics(netinc, equity, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dyn_126d_jerk_v021_signal(netinc, equity, closeadj):
    base = _f02_roe_dynamics(netinc, equity, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dyn_252d_jerk_v022_signal(netinc, equity, closeadj):
    base = _f02_roe_dynamics(netinc, equity, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dyn_252d_jerk_v023_signal(netinc, equity, closeadj):
    base = _f02_roe_dynamics(netinc, equity, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dyn_252d_jerk_v024_signal(netinc, equity, closeadj):
    base = _f02_roe_dynamics(netinc, equity, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dyn_504d_jerk_v025_signal(netinc, equity, closeadj):
    base = _f02_roe_dynamics(netinc, equity, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dyn_504d_jerk_v026_signal(netinc, equity, closeadj):
    base = _f02_roe_dynamics(netinc, equity, 504) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# Dur jerks
def f02arp_f02_allowed_roe_proxy_dur_63d_jerk_v027_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dur_63d_jerk_v028_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dur_252d_jerk_v029_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dur_252d_jerk_v030_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dur_252d_jerk_v031_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dur_504d_jerk_v032_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dur_504d_jerk_v033_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 504) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# Volume × close jerks
def f02arp_f02_allowed_roe_proxy_proxyxvol_63d_jerk_v034_signal(netinc, equity, closeadj, volume):
    base = _mean(_f02_roe_proxy(netinc, equity), 63) * closeadj * _mean(volume, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_proxyxvol_252d_jerk_v035_signal(netinc, equity, closeadj, volume):
    base = _mean(_f02_roe_proxy(netinc, equity), 252) * closeadj * _mean(volume, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dynxvol_63d_jerk_v036_signal(netinc, equity, closeadj, volume):
    base = _f02_roe_dynamics(netinc, equity, 63) * closeadj * _mean(volume, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dynxvol_252d_jerk_v037_signal(netinc, equity, closeadj, volume):
    base = _f02_roe_dynamics(netinc, equity, 252) * closeadj * _mean(volume, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_durxvol_63d_jerk_v038_signal(roe, closeadj, volume):
    base = _f02_roe_durability(roe, 63) * closeadj * _mean(volume, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_durxvol_252d_jerk_v039_signal(roe, closeadj, volume):
    base = _f02_roe_durability(roe, 252) * closeadj * _mean(volume, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# ATR jerks
def f02arp_f02_allowed_roe_proxy_proxyxatr_63d_jerk_v040_signal(netinc, equity, closeadj, high, low):
    base = _mean(_f02_roe_proxy(netinc, equity), 63) * (high - low).rolling(21, min_periods=5).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_proxyxatr_252d_jerk_v041_signal(netinc, equity, closeadj, high, low):
    base = _mean(_f02_roe_proxy(netinc, equity), 252) * (high - low).rolling(63, min_periods=21).mean()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dynxatr_63d_jerk_v042_signal(netinc, equity, closeadj, high, low):
    base = _f02_roe_dynamics(netinc, equity, 63) * (high - low).rolling(21, min_periods=5).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dynxatr_252d_jerk_v043_signal(netinc, equity, closeadj, high, low):
    base = _f02_roe_dynamics(netinc, equity, 252) * (high - low).rolling(63, min_periods=21).mean()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_durxatr_63d_jerk_v044_signal(roe, closeadj, high, low):
    base = _f02_roe_durability(roe, 63) * (high - low).rolling(21, min_periods=5).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_durxatr_252d_jerk_v045_signal(roe, closeadj, high, low):
    base = _f02_roe_durability(roe, 252) * (high - low).rolling(63, min_periods=21).mean()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# EMA jerks
def f02arp_f02_allowed_roe_proxy_proxyema_63d_jerk_v046_signal(netinc, equity, closeadj):
    p = _f02_roe_proxy(netinc, equity)
    base = p.ewm(span=63, min_periods=21).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_proxyema_252d_jerk_v047_signal(netinc, equity, closeadj):
    p = _f02_roe_proxy(netinc, equity)
    base = p.ewm(span=252, min_periods=63).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_durema_63d_jerk_v048_signal(roe, closeadj):
    d = _f02_roe_durability(roe, 63)
    base = d.ewm(span=21, min_periods=5).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_durema_252d_jerk_v049_signal(roe, closeadj):
    d = _f02_roe_durability(roe, 252)
    base = d.ewm(span=63, min_periods=21).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Squared jerks
def f02arp_f02_allowed_roe_proxy_proxysq_63d_jerk_v050_signal(netinc, equity, closeadj):
    p = _f02_roe_proxy(netinc, equity)
    base = p * p.abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_proxysq_252d_jerk_v051_signal(netinc, equity, closeadj):
    p = _mean(_f02_roe_proxy(netinc, equity), 252)
    base = p * p.abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dynsq_63d_jerk_v052_signal(netinc, equity, closeadj):
    d = _f02_roe_dynamics(netinc, equity, 63)
    base = d * d.abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dynsq_252d_jerk_v053_signal(netinc, equity, closeadj):
    d = _f02_roe_dynamics(netinc, equity, 252)
    base = d * d.abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dursq_63d_jerk_v054_signal(roe, closeadj):
    d = _f02_roe_durability(roe, 63)
    base = d * d.abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dursq_252d_jerk_v055_signal(roe, closeadj):
    d = _f02_roe_durability(roe, 252)
    base = d * d.abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Z-score jerks
def f02arp_f02_allowed_roe_proxy_proxyz_63d_jerk_v056_signal(netinc, equity, closeadj):
    p = _f02_roe_proxy(netinc, equity)
    base = _z(p, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_proxyz_252d_jerk_v057_signal(netinc, equity, closeadj):
    p = _f02_roe_proxy(netinc, equity)
    base = _z(p, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dynz_63d_jerk_v058_signal(netinc, equity, closeadj):
    d = _f02_roe_dynamics(netinc, equity, 63)
    base = _z(d, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dynz_252d_jerk_v059_signal(netinc, equity, closeadj):
    d = _f02_roe_dynamics(netinc, equity, 252)
    base = _z(d, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_durz_63d_jerk_v060_signal(roe, closeadj):
    d = _f02_roe_durability(roe, 63)
    base = _z(d, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_durz_252d_jerk_v061_signal(roe, closeadj):
    d = _f02_roe_durability(roe, 252)
    base = _z(d, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Rank jerks
def f02arp_f02_allowed_roe_proxy_proxyrank_63d_jerk_v062_signal(netinc, equity, closeadj):
    p = _f02_roe_proxy(netinc, equity)
    base = p.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_proxyrank_252d_jerk_v063_signal(netinc, equity, closeadj):
    p = _f02_roe_proxy(netinc, equity)
    base = p.rolling(504, min_periods=126).rank(pct=True) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_durrank_63d_jerk_v064_signal(roe, closeadj):
    d = _f02_roe_durability(roe, 63)
    base = d.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_durrank_252d_jerk_v065_signal(roe, closeadj):
    d = _f02_roe_durability(roe, 252)
    base = d.rolling(504, min_periods=126).rank(pct=True) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Gap jerks
def f02arp_f02_allowed_roe_proxy_proxygap_63d_jerk_v066_signal(netinc, equity, closeadj):
    p = _f02_roe_proxy(netinc, equity)
    base = (p - _mean(p, 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_proxygap_252d_jerk_v067_signal(netinc, equity, closeadj):
    p = _f02_roe_proxy(netinc, equity)
    base = (p - _mean(p, 504)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_durgap_63d_jerk_v068_signal(roe, closeadj):
    d = _f02_roe_durability(roe, 63)
    base = (d - _mean(d, 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_durgap_252d_jerk_v069_signal(roe, closeadj):
    d = _f02_roe_durability(roe, 252)
    base = (d - _mean(d, 504)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Log jerks
def f02arp_f02_allowed_roe_proxy_proxylog_63d_jerk_v070_signal(netinc, equity, closeadj):
    p = _f02_roe_proxy(netinc, equity)
    base = np.log(p.abs().replace(0, np.nan)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_proxylog_252d_jerk_v071_signal(netinc, equity, closeadj):
    p = _f02_roe_proxy(netinc, equity)
    base = np.log(p.abs().replace(0, np.nan)) * _mean(closeadj, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Combined proxy × dur jerks
def f02arp_f02_allowed_roe_proxy_proxydur_63d_jerk_v072_signal(netinc, equity, roe, closeadj):
    p = _f02_roe_proxy(netinc, equity)
    d = _f02_roe_durability(roe, 63)
    base = p * d * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_proxydur_252d_jerk_v073_signal(netinc, equity, roe, closeadj):
    p = _mean(_f02_roe_proxy(netinc, equity), 252)
    d = _f02_roe_durability(roe, 252)
    base = p * d * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_proxydyn_63d_jerk_v074_signal(netinc, equity, closeadj):
    p = _f02_roe_proxy(netinc, equity)
    d = _f02_roe_dynamics(netinc, equity, 63)
    base = p * d * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_proxydyn_252d_jerk_v075_signal(netinc, equity, closeadj):
    p = _mean(_f02_roe_proxy(netinc, equity), 252)
    d = _f02_roe_dynamics(netinc, equity, 252)
    base = p * d * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Dollar volume
def f02arp_f02_allowed_roe_proxy_proxyxdv_63d_jerk_v076_signal(netinc, equity, closeadj, volume):
    p = _f02_roe_proxy(netinc, equity)
    dv = closeadj * volume
    base = _mean(p, 63) * _mean(dv, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_proxyxdv_252d_jerk_v077_signal(netinc, equity, closeadj, volume):
    p = _f02_roe_proxy(netinc, equity)
    dv = closeadj * volume
    base = _mean(p, 252) * _mean(dv, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dynxdv_63d_jerk_v078_signal(netinc, equity, closeadj, volume):
    d = _f02_roe_dynamics(netinc, equity, 63)
    dv = closeadj * volume
    base = d * _mean(dv, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dynxdv_252d_jerk_v079_signal(netinc, equity, closeadj, volume):
    d = _f02_roe_dynamics(netinc, equity, 252)
    dv = closeadj * volume
    base = d * _mean(dv, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_durxdv_63d_jerk_v080_signal(roe, closeadj, volume):
    d = _f02_roe_durability(roe, 63)
    dv = closeadj * volume
    base = d * _mean(dv, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_durxdv_252d_jerk_v081_signal(roe, closeadj, volume):
    d = _f02_roe_durability(roe, 252)
    dv = closeadj * volume
    base = d * _mean(dv, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Std jerks
def f02arp_f02_allowed_roe_proxy_proxystd_63d_jerk_v082_signal(netinc, equity, closeadj):
    p = _f02_roe_proxy(netinc, equity)
    base = _std(p, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_proxystd_252d_jerk_v083_signal(netinc, equity, closeadj):
    p = _f02_roe_proxy(netinc, equity)
    base = _std(p, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dynstd_63d_jerk_v084_signal(netinc, equity, closeadj):
    d = _f02_roe_dynamics(netinc, equity, 63)
    base = _std(d, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dynstd_252d_jerk_v085_signal(netinc, equity, closeadj):
    d = _f02_roe_dynamics(netinc, equity, 252)
    base = _std(d, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Size-weighted jerks
def f02arp_f02_allowed_roe_proxy_proxyxsize_63d_jerk_v086_signal(netinc, equity, closeadj):
    p = _f02_roe_proxy(netinc, equity)
    base = p * np.log(netinc.abs().replace(0, np.nan)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_proxyxsize_252d_jerk_v087_signal(netinc, equity, closeadj):
    p = _mean(_f02_roe_proxy(netinc, equity), 252)
    base = p * np.log(netinc.abs().replace(0, np.nan)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_proxyxeqsize_63d_jerk_v088_signal(netinc, equity, closeadj):
    p = _f02_roe_proxy(netinc, equity)
    base = p * np.log(equity.replace(0, np.nan)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_proxyxeqsize_252d_jerk_v089_signal(netinc, equity, closeadj):
    p = _mean(_f02_roe_proxy(netinc, equity), 252)
    base = p * np.log(equity.replace(0, np.nan)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Close-z jerks
def f02arp_f02_allowed_roe_proxy_proxyxclosez_63d_jerk_v090_signal(netinc, equity, closeadj):
    p = _f02_roe_proxy(netinc, equity)
    base = p * _z(closeadj, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_proxyxclosez_252d_jerk_v091_signal(netinc, equity, closeadj):
    p = _mean(_f02_roe_proxy(netinc, equity), 252)
    base = p * _z(closeadj, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dynxclosez_63d_jerk_v092_signal(netinc, equity, closeadj):
    d = _f02_roe_dynamics(netinc, equity, 63)
    base = d * _z(closeadj, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dynxclosez_252d_jerk_v093_signal(netinc, equity, closeadj):
    d = _f02_roe_dynamics(netinc, equity, 252)
    base = d * _z(closeadj, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_durxclosez_63d_jerk_v094_signal(roe, closeadj):
    d = _f02_roe_durability(roe, 63)
    base = d * _z(closeadj, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_durxclosez_252d_jerk_v095_signal(roe, closeadj):
    d = _f02_roe_durability(roe, 252)
    base = d * _z(closeadj, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Return interactions
def f02arp_f02_allowed_roe_proxy_proxyxret_63d_jerk_v096_signal(netinc, equity, closeadj):
    p = _f02_roe_proxy(netinc, equity)
    base = p * closeadj.pct_change(21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_proxyxret_252d_jerk_v097_signal(netinc, equity, closeadj):
    p = _mean(_f02_roe_proxy(netinc, equity), 252)
    base = p * closeadj.pct_change(63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dynxret_63d_jerk_v098_signal(netinc, equity, closeadj):
    d = _f02_roe_dynamics(netinc, equity, 63)
    base = d * closeadj.pct_change(21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dynxret_252d_jerk_v099_signal(netinc, equity, closeadj):
    d = _f02_roe_dynamics(netinc, equity, 252)
    base = d * closeadj.pct_change(63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_durxret_63d_jerk_v100_signal(roe, closeadj):
    d = _f02_roe_durability(roe, 63)
    base = d * closeadj.pct_change(21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_durxret_252d_jerk_v101_signal(roe, closeadj):
    d = _f02_roe_durability(roe, 252)
    base = d * closeadj.pct_change(63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Abs return interactions
def f02arp_f02_allowed_roe_proxy_proxyxabsret_63d_jerk_v102_signal(netinc, equity, closeadj):
    p = _f02_roe_proxy(netinc, equity)
    base = p * closeadj.pct_change(21).abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_proxyxabsret_252d_jerk_v103_signal(netinc, equity, closeadj):
    p = _mean(_f02_roe_proxy(netinc, equity), 252)
    base = p * closeadj.pct_change(63).abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dynxabsret_63d_jerk_v104_signal(netinc, equity, closeadj):
    d = _f02_roe_dynamics(netinc, equity, 63)
    base = d * closeadj.pct_change(21).abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dynxabsret_252d_jerk_v105_signal(netinc, equity, closeadj):
    d = _f02_roe_dynamics(netinc, equity, 252)
    base = d * closeadj.pct_change(63).abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_durxabsret_63d_jerk_v106_signal(roe, closeadj):
    d = _f02_roe_durability(roe, 63)
    base = d * closeadj.pct_change(21).abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_durxabsret_252d_jerk_v107_signal(roe, closeadj):
    d = _f02_roe_durability(roe, 252)
    base = d * closeadj.pct_change(63).abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Acceleration jerks
def f02arp_f02_allowed_roe_proxy_proxyaccel_63d_jerk_v108_signal(netinc, equity, closeadj):
    p = _mean(_f02_roe_proxy(netinc, equity), 63)
    accel = p - p.shift(21)
    base = accel * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_proxyaccel_252d_jerk_v109_signal(netinc, equity, closeadj):
    p = _mean(_f02_roe_proxy(netinc, equity), 252)
    accel = p - p.shift(63)
    base = accel * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_duraccel_63d_jerk_v110_signal(roe, closeadj):
    d = _f02_roe_durability(roe, 63)
    accel = d - d.shift(21)
    base = accel * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_duraccel_252d_jerk_v111_signal(roe, closeadj):
    d = _f02_roe_durability(roe, 252)
    accel = d - d.shift(63)
    base = accel * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Inv-price jerks
def f02arp_f02_allowed_roe_proxy_proxyxinvprice_63d_jerk_v112_signal(netinc, equity, closeadj):
    p = _mean(_f02_roe_proxy(netinc, equity), 63)
    base = p * _mean(closeadj, 21) * _mean(closeadj, 21) / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_proxyxinvprice_252d_jerk_v113_signal(netinc, equity, closeadj):
    p = _mean(_f02_roe_proxy(netinc, equity), 252)
    base = p * _mean(closeadj, 63) * _mean(closeadj, 63) / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# MA cross jerks
def f02arp_f02_allowed_roe_proxy_proxycross_5_63_jerk_v114_signal(netinc, equity, closeadj):
    p = _f02_roe_proxy(netinc, equity)
    base = (_mean(p, 5) - _mean(p, 63)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_proxycross_21_252_jerk_v115_signal(netinc, equity, closeadj):
    p = _f02_roe_proxy(netinc, equity)
    base = (_mean(p, 21) - _mean(p, 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_proxycross_63_252_jerk_v116_signal(netinc, equity, closeadj):
    p = _f02_roe_proxy(netinc, equity)
    base = (_mean(p, 63) - _mean(p, 252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Spread jerks
def f02arp_f02_allowed_roe_proxy_proxyspread_63d_jerk_v117_signal(netinc, equity, closeadj):
    p = _f02_roe_proxy(netinc, equity)
    base = (p - 0.10) * closeadj * _mean(p, 63) / _mean(p, 252).replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_proxyspread_252d_jerk_v118_signal(netinc, equity, closeadj):
    p = _f02_roe_proxy(netinc, equity)
    base = (p - 0.10) * closeadj * _mean(p, 252) / _mean(p, 504).replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Combo dyn × dur
def f02arp_f02_allowed_roe_proxy_dyndur_63d_jerk_v119_signal(netinc, equity, roe, closeadj):
    d1 = _f02_roe_dynamics(netinc, equity, 63)
    d2 = _f02_roe_durability(roe, 63)
    base = d1 * d2 * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dyndur_252d_jerk_v120_signal(netinc, equity, roe, closeadj):
    d1 = _f02_roe_dynamics(netinc, equity, 252)
    d2 = _f02_roe_durability(roe, 252)
    base = d1 * d2 * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d window
def f02arp_f02_allowed_roe_proxy_dyn_5d_jerk_v121_signal(netinc, equity, closeadj):
    base = _f02_roe_dynamics(netinc, equity, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dur_5d_jerk_v122_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d
def f02arp_f02_allowed_roe_proxy_proxy_10d_jerk_v123_signal(netinc, equity, closeadj):
    base = _mean(_f02_roe_proxy(netinc, equity), 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dyn_10d_jerk_v124_signal(netinc, equity, closeadj):
    base = _f02_roe_dynamics(netinc, equity, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dur_10d_jerk_v125_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d
def f02arp_f02_allowed_roe_proxy_proxy_42d_jerk_v126_signal(netinc, equity, closeadj):
    base = _mean(_f02_roe_proxy(netinc, equity), 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dyn_42d_jerk_v127_signal(netinc, equity, closeadj):
    base = _f02_roe_dynamics(netinc, equity, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dur_42d_jerk_v128_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d
def f02arp_f02_allowed_roe_proxy_proxy_189d_jerk_v129_signal(netinc, equity, closeadj):
    base = _mean(_f02_roe_proxy(netinc, equity), 252) * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dyn_189d_jerk_v130_signal(netinc, equity, closeadj):
    base = _f02_roe_dynamics(netinc, equity, 252) * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dur_189d_jerk_v131_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 252) * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# Combo with ATR
def f02arp_f02_allowed_roe_proxy_combo_atr_63d_jerk_v132_signal(netinc, equity, roe, closeadj, high, low):
    p = _f02_roe_proxy(netinc, equity)
    d = _f02_roe_durability(roe, 63)
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = p * d * atr
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_combo_atr_252d_jerk_v133_signal(netinc, equity, roe, closeadj, high, low):
    p = _mean(_f02_roe_proxy(netinc, equity), 252)
    d = _f02_roe_durability(roe, 252)
    atr = (high - low).rolling(63, min_periods=21).mean()
    base = p * d * atr
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Combo with dv
def f02arp_f02_allowed_roe_proxy_combo_dv_63d_jerk_v134_signal(netinc, equity, closeadj, volume):
    p = _f02_roe_proxy(netinc, equity)
    d = _f02_roe_dynamics(netinc, equity, 63)
    dv = closeadj * volume
    base = p * d * _mean(dv, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_combo_dv_252d_jerk_v135_signal(netinc, equity, closeadj, volume):
    p = _mean(_f02_roe_proxy(netinc, equity), 252)
    d = _f02_roe_dynamics(netinc, equity, 252)
    dv = closeadj * volume
    base = p * d * _mean(dv, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Dur × roe
def f02arp_f02_allowed_roe_proxy_durxroe_63d_jerk_v136_signal(roe, closeadj):
    d = _f02_roe_durability(roe, 63)
    base = d * _mean(roe, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_durxroe_252d_jerk_v137_signal(roe, closeadj):
    d = _f02_roe_durability(roe, 252)
    base = d * _mean(roe, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Sum jerks
def f02arp_f02_allowed_roe_proxy_dynsum_63d_jerk_v138_signal(netinc, equity, closeadj):
    d = _f02_roe_dynamics(netinc, equity, 63)
    base = d.rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dynsum_252d_jerk_v139_signal(netinc, equity, closeadj):
    d = _f02_roe_dynamics(netinc, equity, 252)
    base = d.rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Sign × volume jerks
def f02arp_f02_allowed_roe_proxy_proxysignxvol_63d_jerk_v140_signal(netinc, equity, closeadj, volume):
    p = _f02_roe_proxy(netinc, equity)
    base = np.sign(p - _mean(p, 252)) * _mean(volume, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_proxysignxvol_252d_jerk_v141_signal(netinc, equity, closeadj, volume):
    p = _f02_roe_proxy(netinc, equity)
    base = np.sign(p - _mean(p, 504)) * _mean(volume, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Cube
def f02arp_f02_allowed_roe_proxy_proxycube_63d_jerk_v142_signal(netinc, equity, closeadj):
    p = _f02_roe_proxy(netinc, equity)
    base = p * p * p.abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_proxycube_252d_jerk_v143_signal(netinc, equity, closeadj):
    p = _mean(_f02_roe_proxy(netinc, equity), 252)
    base = p * p * p.abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Diff-norm jerks
def f02arp_f02_allowed_roe_proxy_proxydn_63d_jerk_v144_signal(netinc, equity, closeadj):
    p = _f02_roe_proxy(netinc, equity)
    base = p.diff(21) / p.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_proxydn_252d_jerk_v145_signal(netinc, equity, closeadj):
    p = _f02_roe_proxy(netinc, equity)
    base = p.diff(63) / p.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dyndn_63d_jerk_v146_signal(netinc, equity, closeadj):
    d = _f02_roe_dynamics(netinc, equity, 63)
    base = d.diff(21) / d.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_dyndn_252d_jerk_v147_signal(netinc, equity, closeadj):
    d = _f02_roe_dynamics(netinc, equity, 252)
    base = d.diff(63) / d.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_durdn_63d_jerk_v148_signal(roe, closeadj):
    d = _f02_roe_durability(roe, 63)
    base = d.diff(21) / d.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02arp_f02_allowed_roe_proxy_durdn_252d_jerk_v149_signal(roe, closeadj):
    d = _f02_roe_durability(roe, 252)
    base = d.diff(63) / d.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Proxy EMA long span × close
def f02arp_f02_allowed_roe_proxy_proxyemalong_252d_jerk_v150_signal(netinc, equity, closeadj):
    p = _f02_roe_proxy(netinc, equity)
    base = p.ewm(span=504, min_periods=126).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f02arp_f02_allowed_roe_proxy_proxy_5d_jerk_v001_signal,
    f02arp_f02_allowed_roe_proxy_proxy_5d_jerk_v002_signal,
    f02arp_f02_allowed_roe_proxy_proxy_21d_jerk_v003_signal,
    f02arp_f02_allowed_roe_proxy_proxy_21d_jerk_v004_signal,
    f02arp_f02_allowed_roe_proxy_proxy_21d_jerk_v005_signal,
    f02arp_f02_allowed_roe_proxy_proxy_63d_jerk_v006_signal,
    f02arp_f02_allowed_roe_proxy_proxy_63d_jerk_v007_signal,
    f02arp_f02_allowed_roe_proxy_proxy_63d_jerk_v008_signal,
    f02arp_f02_allowed_roe_proxy_proxy_126d_jerk_v009_signal,
    f02arp_f02_allowed_roe_proxy_proxy_126d_jerk_v010_signal,
    f02arp_f02_allowed_roe_proxy_proxy_252d_jerk_v011_signal,
    f02arp_f02_allowed_roe_proxy_proxy_252d_jerk_v012_signal,
    f02arp_f02_allowed_roe_proxy_proxy_252d_jerk_v013_signal,
    f02arp_f02_allowed_roe_proxy_proxy_504d_jerk_v014_signal,
    f02arp_f02_allowed_roe_proxy_proxy_504d_jerk_v015_signal,
    f02arp_f02_allowed_roe_proxy_dyn_21d_jerk_v016_signal,
    f02arp_f02_allowed_roe_proxy_dyn_21d_jerk_v017_signal,
    f02arp_f02_allowed_roe_proxy_dyn_63d_jerk_v018_signal,
    f02arp_f02_allowed_roe_proxy_dyn_63d_jerk_v019_signal,
    f02arp_f02_allowed_roe_proxy_dyn_126d_jerk_v020_signal,
    f02arp_f02_allowed_roe_proxy_dyn_126d_jerk_v021_signal,
    f02arp_f02_allowed_roe_proxy_dyn_252d_jerk_v022_signal,
    f02arp_f02_allowed_roe_proxy_dyn_252d_jerk_v023_signal,
    f02arp_f02_allowed_roe_proxy_dyn_252d_jerk_v024_signal,
    f02arp_f02_allowed_roe_proxy_dyn_504d_jerk_v025_signal,
    f02arp_f02_allowed_roe_proxy_dyn_504d_jerk_v026_signal,
    f02arp_f02_allowed_roe_proxy_dur_63d_jerk_v027_signal,
    f02arp_f02_allowed_roe_proxy_dur_63d_jerk_v028_signal,
    f02arp_f02_allowed_roe_proxy_dur_252d_jerk_v029_signal,
    f02arp_f02_allowed_roe_proxy_dur_252d_jerk_v030_signal,
    f02arp_f02_allowed_roe_proxy_dur_252d_jerk_v031_signal,
    f02arp_f02_allowed_roe_proxy_dur_504d_jerk_v032_signal,
    f02arp_f02_allowed_roe_proxy_dur_504d_jerk_v033_signal,
    f02arp_f02_allowed_roe_proxy_proxyxvol_63d_jerk_v034_signal,
    f02arp_f02_allowed_roe_proxy_proxyxvol_252d_jerk_v035_signal,
    f02arp_f02_allowed_roe_proxy_dynxvol_63d_jerk_v036_signal,
    f02arp_f02_allowed_roe_proxy_dynxvol_252d_jerk_v037_signal,
    f02arp_f02_allowed_roe_proxy_durxvol_63d_jerk_v038_signal,
    f02arp_f02_allowed_roe_proxy_durxvol_252d_jerk_v039_signal,
    f02arp_f02_allowed_roe_proxy_proxyxatr_63d_jerk_v040_signal,
    f02arp_f02_allowed_roe_proxy_proxyxatr_252d_jerk_v041_signal,
    f02arp_f02_allowed_roe_proxy_dynxatr_63d_jerk_v042_signal,
    f02arp_f02_allowed_roe_proxy_dynxatr_252d_jerk_v043_signal,
    f02arp_f02_allowed_roe_proxy_durxatr_63d_jerk_v044_signal,
    f02arp_f02_allowed_roe_proxy_durxatr_252d_jerk_v045_signal,
    f02arp_f02_allowed_roe_proxy_proxyema_63d_jerk_v046_signal,
    f02arp_f02_allowed_roe_proxy_proxyema_252d_jerk_v047_signal,
    f02arp_f02_allowed_roe_proxy_durema_63d_jerk_v048_signal,
    f02arp_f02_allowed_roe_proxy_durema_252d_jerk_v049_signal,
    f02arp_f02_allowed_roe_proxy_proxysq_63d_jerk_v050_signal,
    f02arp_f02_allowed_roe_proxy_proxysq_252d_jerk_v051_signal,
    f02arp_f02_allowed_roe_proxy_dynsq_63d_jerk_v052_signal,
    f02arp_f02_allowed_roe_proxy_dynsq_252d_jerk_v053_signal,
    f02arp_f02_allowed_roe_proxy_dursq_63d_jerk_v054_signal,
    f02arp_f02_allowed_roe_proxy_dursq_252d_jerk_v055_signal,
    f02arp_f02_allowed_roe_proxy_proxyz_63d_jerk_v056_signal,
    f02arp_f02_allowed_roe_proxy_proxyz_252d_jerk_v057_signal,
    f02arp_f02_allowed_roe_proxy_dynz_63d_jerk_v058_signal,
    f02arp_f02_allowed_roe_proxy_dynz_252d_jerk_v059_signal,
    f02arp_f02_allowed_roe_proxy_durz_63d_jerk_v060_signal,
    f02arp_f02_allowed_roe_proxy_durz_252d_jerk_v061_signal,
    f02arp_f02_allowed_roe_proxy_proxyrank_63d_jerk_v062_signal,
    f02arp_f02_allowed_roe_proxy_proxyrank_252d_jerk_v063_signal,
    f02arp_f02_allowed_roe_proxy_durrank_63d_jerk_v064_signal,
    f02arp_f02_allowed_roe_proxy_durrank_252d_jerk_v065_signal,
    f02arp_f02_allowed_roe_proxy_proxygap_63d_jerk_v066_signal,
    f02arp_f02_allowed_roe_proxy_proxygap_252d_jerk_v067_signal,
    f02arp_f02_allowed_roe_proxy_durgap_63d_jerk_v068_signal,
    f02arp_f02_allowed_roe_proxy_durgap_252d_jerk_v069_signal,
    f02arp_f02_allowed_roe_proxy_proxylog_63d_jerk_v070_signal,
    f02arp_f02_allowed_roe_proxy_proxylog_252d_jerk_v071_signal,
    f02arp_f02_allowed_roe_proxy_proxydur_63d_jerk_v072_signal,
    f02arp_f02_allowed_roe_proxy_proxydur_252d_jerk_v073_signal,
    f02arp_f02_allowed_roe_proxy_proxydyn_63d_jerk_v074_signal,
    f02arp_f02_allowed_roe_proxy_proxydyn_252d_jerk_v075_signal,
    f02arp_f02_allowed_roe_proxy_proxyxdv_63d_jerk_v076_signal,
    f02arp_f02_allowed_roe_proxy_proxyxdv_252d_jerk_v077_signal,
    f02arp_f02_allowed_roe_proxy_dynxdv_63d_jerk_v078_signal,
    f02arp_f02_allowed_roe_proxy_dynxdv_252d_jerk_v079_signal,
    f02arp_f02_allowed_roe_proxy_durxdv_63d_jerk_v080_signal,
    f02arp_f02_allowed_roe_proxy_durxdv_252d_jerk_v081_signal,
    f02arp_f02_allowed_roe_proxy_proxystd_63d_jerk_v082_signal,
    f02arp_f02_allowed_roe_proxy_proxystd_252d_jerk_v083_signal,
    f02arp_f02_allowed_roe_proxy_dynstd_63d_jerk_v084_signal,
    f02arp_f02_allowed_roe_proxy_dynstd_252d_jerk_v085_signal,
    f02arp_f02_allowed_roe_proxy_proxyxsize_63d_jerk_v086_signal,
    f02arp_f02_allowed_roe_proxy_proxyxsize_252d_jerk_v087_signal,
    f02arp_f02_allowed_roe_proxy_proxyxeqsize_63d_jerk_v088_signal,
    f02arp_f02_allowed_roe_proxy_proxyxeqsize_252d_jerk_v089_signal,
    f02arp_f02_allowed_roe_proxy_proxyxclosez_63d_jerk_v090_signal,
    f02arp_f02_allowed_roe_proxy_proxyxclosez_252d_jerk_v091_signal,
    f02arp_f02_allowed_roe_proxy_dynxclosez_63d_jerk_v092_signal,
    f02arp_f02_allowed_roe_proxy_dynxclosez_252d_jerk_v093_signal,
    f02arp_f02_allowed_roe_proxy_durxclosez_63d_jerk_v094_signal,
    f02arp_f02_allowed_roe_proxy_durxclosez_252d_jerk_v095_signal,
    f02arp_f02_allowed_roe_proxy_proxyxret_63d_jerk_v096_signal,
    f02arp_f02_allowed_roe_proxy_proxyxret_252d_jerk_v097_signal,
    f02arp_f02_allowed_roe_proxy_dynxret_63d_jerk_v098_signal,
    f02arp_f02_allowed_roe_proxy_dynxret_252d_jerk_v099_signal,
    f02arp_f02_allowed_roe_proxy_durxret_63d_jerk_v100_signal,
    f02arp_f02_allowed_roe_proxy_durxret_252d_jerk_v101_signal,
    f02arp_f02_allowed_roe_proxy_proxyxabsret_63d_jerk_v102_signal,
    f02arp_f02_allowed_roe_proxy_proxyxabsret_252d_jerk_v103_signal,
    f02arp_f02_allowed_roe_proxy_dynxabsret_63d_jerk_v104_signal,
    f02arp_f02_allowed_roe_proxy_dynxabsret_252d_jerk_v105_signal,
    f02arp_f02_allowed_roe_proxy_durxabsret_63d_jerk_v106_signal,
    f02arp_f02_allowed_roe_proxy_durxabsret_252d_jerk_v107_signal,
    f02arp_f02_allowed_roe_proxy_proxyaccel_63d_jerk_v108_signal,
    f02arp_f02_allowed_roe_proxy_proxyaccel_252d_jerk_v109_signal,
    f02arp_f02_allowed_roe_proxy_duraccel_63d_jerk_v110_signal,
    f02arp_f02_allowed_roe_proxy_duraccel_252d_jerk_v111_signal,
    f02arp_f02_allowed_roe_proxy_proxyxinvprice_63d_jerk_v112_signal,
    f02arp_f02_allowed_roe_proxy_proxyxinvprice_252d_jerk_v113_signal,
    f02arp_f02_allowed_roe_proxy_proxycross_5_63_jerk_v114_signal,
    f02arp_f02_allowed_roe_proxy_proxycross_21_252_jerk_v115_signal,
    f02arp_f02_allowed_roe_proxy_proxycross_63_252_jerk_v116_signal,
    f02arp_f02_allowed_roe_proxy_proxyspread_63d_jerk_v117_signal,
    f02arp_f02_allowed_roe_proxy_proxyspread_252d_jerk_v118_signal,
    f02arp_f02_allowed_roe_proxy_dyndur_63d_jerk_v119_signal,
    f02arp_f02_allowed_roe_proxy_dyndur_252d_jerk_v120_signal,
    f02arp_f02_allowed_roe_proxy_dyn_5d_jerk_v121_signal,
    f02arp_f02_allowed_roe_proxy_dur_5d_jerk_v122_signal,
    f02arp_f02_allowed_roe_proxy_proxy_10d_jerk_v123_signal,
    f02arp_f02_allowed_roe_proxy_dyn_10d_jerk_v124_signal,
    f02arp_f02_allowed_roe_proxy_dur_10d_jerk_v125_signal,
    f02arp_f02_allowed_roe_proxy_proxy_42d_jerk_v126_signal,
    f02arp_f02_allowed_roe_proxy_dyn_42d_jerk_v127_signal,
    f02arp_f02_allowed_roe_proxy_dur_42d_jerk_v128_signal,
    f02arp_f02_allowed_roe_proxy_proxy_189d_jerk_v129_signal,
    f02arp_f02_allowed_roe_proxy_dyn_189d_jerk_v130_signal,
    f02arp_f02_allowed_roe_proxy_dur_189d_jerk_v131_signal,
    f02arp_f02_allowed_roe_proxy_combo_atr_63d_jerk_v132_signal,
    f02arp_f02_allowed_roe_proxy_combo_atr_252d_jerk_v133_signal,
    f02arp_f02_allowed_roe_proxy_combo_dv_63d_jerk_v134_signal,
    f02arp_f02_allowed_roe_proxy_combo_dv_252d_jerk_v135_signal,
    f02arp_f02_allowed_roe_proxy_durxroe_63d_jerk_v136_signal,
    f02arp_f02_allowed_roe_proxy_durxroe_252d_jerk_v137_signal,
    f02arp_f02_allowed_roe_proxy_dynsum_63d_jerk_v138_signal,
    f02arp_f02_allowed_roe_proxy_dynsum_252d_jerk_v139_signal,
    f02arp_f02_allowed_roe_proxy_proxysignxvol_63d_jerk_v140_signal,
    f02arp_f02_allowed_roe_proxy_proxysignxvol_252d_jerk_v141_signal,
    f02arp_f02_allowed_roe_proxy_proxycube_63d_jerk_v142_signal,
    f02arp_f02_allowed_roe_proxy_proxycube_252d_jerk_v143_signal,
    f02arp_f02_allowed_roe_proxy_proxydn_63d_jerk_v144_signal,
    f02arp_f02_allowed_roe_proxy_proxydn_252d_jerk_v145_signal,
    f02arp_f02_allowed_roe_proxy_dyndn_63d_jerk_v146_signal,
    f02arp_f02_allowed_roe_proxy_dyndn_252d_jerk_v147_signal,
    f02arp_f02_allowed_roe_proxy_durdn_63d_jerk_v148_signal,
    f02arp_f02_allowed_roe_proxy_durdn_252d_jerk_v149_signal,
    f02arp_f02_allowed_roe_proxy_proxyemalong_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F02_ALLOWED_ROE_PROXY_REGISTRY_JERK_001_150 = REGISTRY


def _build_cols():
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = pd.Series(closeadj.values * (1.0 + np.abs(np.random.normal(0, 0.01, n))), name="high")
    low = pd.Series(closeadj.values * (1.0 - np.abs(np.random.normal(0, 0.01, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    netinc = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    equity = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    roe = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    return {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "netinc": netinc, "equity": equity, "roe": roe,
    }


if __name__ == "__main__":
    cols = _build_cols()
    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f02_roe_proxy", "_f02_roe_dynamics", "_f02_roe_durability")
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
    print(f"OK f02_allowed_roe_proxy_3rd_derivatives_001_150_claude: {n_features} features pass")
