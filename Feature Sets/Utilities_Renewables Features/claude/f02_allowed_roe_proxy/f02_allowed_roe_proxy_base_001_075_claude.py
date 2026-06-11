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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f02_roe_proxy(netinc, equity):
    return netinc / equity.replace(0, np.nan)


def _f02_roe_dynamics(netinc, equity, w):
    roe = netinc / equity.replace(0, np.nan)
    return roe - roe.rolling(w, min_periods=max(1, w // 2)).mean()


def _f02_roe_durability(roe, w):
    m = roe.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = roe.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan)


# 21d ROE proxy × close
def f02arp_f02_allowed_roe_proxy_roeproxy_21d_base_v001_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROE proxy × close
def f02arp_f02_allowed_roe_proxy_roeproxy_63d_base_v002_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ROE proxy × close
def f02arp_f02_allowed_roe_proxy_roeproxy_126d_base_v003_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROE proxy × close
def f02arp_f02_allowed_roe_proxy_roeproxy_252d_base_v004_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ROE proxy × close
def f02arp_f02_allowed_roe_proxy_roeproxy_504d_base_v005_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROE dynamics × close
def f02arp_f02_allowed_roe_proxy_roedyn_21d_base_v006_signal(netinc, equity, closeadj):
    result = _f02_roe_dynamics(netinc, equity, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROE dynamics × close
def f02arp_f02_allowed_roe_proxy_roedyn_63d_base_v007_signal(netinc, equity, closeadj):
    result = _f02_roe_dynamics(netinc, equity, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ROE dynamics × close
def f02arp_f02_allowed_roe_proxy_roedyn_126d_base_v008_signal(netinc, equity, closeadj):
    result = _f02_roe_dynamics(netinc, equity, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROE dynamics × close
def f02arp_f02_allowed_roe_proxy_roedyn_252d_base_v009_signal(netinc, equity, closeadj):
    result = _f02_roe_dynamics(netinc, equity, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ROE dynamics × close
def f02arp_f02_allowed_roe_proxy_roedyn_504d_base_v010_signal(netinc, equity, closeadj):
    result = _f02_roe_dynamics(netinc, equity, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROE durability × close (using reported roe)
def f02arp_f02_allowed_roe_proxy_roedur_63d_base_v011_signal(roe, closeadj):
    result = _f02_roe_durability(roe, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ROE durability × close
def f02arp_f02_allowed_roe_proxy_roedur_126d_base_v012_signal(roe, closeadj):
    result = _f02_roe_durability(roe, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROE durability × close
def f02arp_f02_allowed_roe_proxy_roedur_252d_base_v013_signal(roe, closeadj):
    result = _f02_roe_durability(roe, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ROE durability × close
def f02arp_f02_allowed_roe_proxy_roedur_504d_base_v014_signal(roe, closeadj):
    result = _f02_roe_durability(roe, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROE proxy z-score over 252d
def f02arp_f02_allowed_roe_proxy_roez_21d_base_v015_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    result = _z(base, 252) + closeadj * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROE proxy z-score over 504d
def f02arp_f02_allowed_roe_proxy_roez_63d_base_v016_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    result = _z(base, 504) + closeadj * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROE proxy z-score
def f02arp_f02_allowed_roe_proxy_roez_252d_base_v017_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROE proxy std × close
def f02arp_f02_allowed_roe_proxy_roestd_21d_base_v018_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROE proxy std × close
def f02arp_f02_allowed_roe_proxy_roestd_63d_base_v019_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROE proxy std × close
def f02arp_f02_allowed_roe_proxy_roestd_252d_base_v020_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROE proxy * close (raw)
def f02arp_f02_allowed_roe_proxy_roeraw_21d_base_v021_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROE proxy EMA × close
def f02arp_f02_allowed_roe_proxy_roeema_63d_base_v022_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    result = base.ewm(span=63, min_periods=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROE proxy EMA × close
def f02arp_f02_allowed_roe_proxy_roeema_252d_base_v023_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    result = base.ewm(span=252, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d reported roe × close
def f02arp_f02_allowed_roe_proxy_roereported_21d_base_v024_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 21)
    result = _mean(roe, 21) * closeadj + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d reported roe × close
def f02arp_f02_allowed_roe_proxy_roereported_63d_base_v025_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 63)
    result = _mean(roe, 63) * closeadj + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d reported roe × close
def f02arp_f02_allowed_roe_proxy_roereported_252d_base_v026_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 252)
    result = _mean(roe, 252) * closeadj + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d roe std × close
def f02arp_f02_allowed_roe_proxy_roeisstd_21d_base_v027_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 21)
    result = _std(roe, 21) * closeadj + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roe std × close
def f02arp_f02_allowed_roe_proxy_roeisstd_63d_base_v028_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 63)
    result = _std(roe, 63) * closeadj + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roe std × close
def f02arp_f02_allowed_roe_proxy_roeisstd_252d_base_v029_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 252)
    result = _std(roe, 252) * closeadj + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d reported roe z-score
def f02arp_f02_allowed_roe_proxy_roeisz_21d_base_v030_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 21)
    result = _z(roe, 252) * closeadj + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d reported roe z-score × close
def f02arp_f02_allowed_roe_proxy_roeisz_63d_base_v031_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 63)
    result = _z(roe, 504) * closeadj + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d roe gap (current vs 252d mean) × close
def f02arp_f02_allowed_roe_proxy_roegap_21d_base_v032_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 21)
    result = (roe - _mean(roe, 252)) * closeadj + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roe gap × close
def f02arp_f02_allowed_roe_proxy_roegap_63d_base_v033_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 63)
    result = (roe - _mean(roe, 504)) * closeadj + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d reported roe EMA × close
def f02arp_f02_allowed_roe_proxy_roeisema_63d_base_v034_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 63)
    result = roe.ewm(span=63, min_periods=21).mean() * closeadj + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d reported roe EMA × close
def f02arp_f02_allowed_roe_proxy_roeisema_252d_base_v035_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 252)
    result = roe.ewm(span=252, min_periods=63).mean() * closeadj + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d roe rank × close
def f02arp_f02_allowed_roe_proxy_roerank_63d_base_v036_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 63)
    result = roe.rolling(252, min_periods=63).rank(pct=True) * closeadj + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roe rank × close
def f02arp_f02_allowed_roe_proxy_roerank_252d_base_v037_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 252)
    result = roe.rolling(504, min_periods=126).rank(pct=True) * closeadj + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d roe acceleration × close
def f02arp_f02_allowed_roe_proxy_roeaccel_63d_base_v038_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 63)
    result = (_mean(roe, 21) - _mean(roe, 63)) * closeadj + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roe acceleration × close
def f02arp_f02_allowed_roe_proxy_roeaccel_252d_base_v039_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 252)
    result = (_mean(roe, 63) - _mean(roe, 252)) * closeadj + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROE proxy × volume mean × close
def f02arp_f02_allowed_roe_proxy_roexvol_21d_base_v040_signal(netinc, equity, closeadj, volume):
    base = _f02_roe_proxy(netinc, equity)
    result = base * _mean(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROE proxy × volume × close
def f02arp_f02_allowed_roe_proxy_roexvol_63d_base_v041_signal(netinc, equity, closeadj, volume):
    base = _f02_roe_proxy(netinc, equity)
    result = base * _mean(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROE proxy × dollar volume
def f02arp_f02_allowed_roe_proxy_roexdv_21d_base_v042_signal(netinc, equity, closeadj, volume):
    base = _f02_roe_proxy(netinc, equity)
    dv = closeadj * volume
    result = base * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROE proxy × dollar volume
def f02arp_f02_allowed_roe_proxy_roexdv_63d_base_v043_signal(netinc, equity, closeadj, volume):
    base = _f02_roe_proxy(netinc, equity)
    dv = closeadj * volume
    result = base * _mean(dv, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d ROE proxy × close
def f02arp_f02_allowed_roe_proxy_roeproxy_5d_base_v044_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d ROE proxy × close
def f02arp_f02_allowed_roe_proxy_roeproxy_10d_base_v045_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d ROE proxy × close
def f02arp_f02_allowed_roe_proxy_roeproxy_42d_base_v046_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d ROE proxy × close
def f02arp_f02_allowed_roe_proxy_roeproxy_189d_base_v047_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d ROE proxy × close
def f02arp_f02_allowed_roe_proxy_roeproxy_378d_base_v048_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROE proxy × close (pct change)
def f02arp_f02_allowed_roe_proxy_roechg_21d_base_v049_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    result = base.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROE proxy pct change × close
def f02arp_f02_allowed_roe_proxy_roechg_63d_base_v050_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    result = base.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROE proxy pct change × close
def f02arp_f02_allowed_roe_proxy_roechg_252d_base_v051_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    result = base.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ROE proxy × netinc log × close
def f02arp_f02_allowed_roe_proxy_roexsize_63d_base_v052_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    s = np.log(netinc.abs().replace(0, np.nan))
    result = base * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ROE proxy × equity log × close
def f02arp_f02_allowed_roe_proxy_roexeqsize_63d_base_v053_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    s = np.log(equity.replace(0, np.nan))
    result = base * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ROE proxy × netinc × close (income-weighted)
def f02arp_f02_allowed_roe_proxy_roexnetinc_63d_base_v054_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    result = base * _mean(netinc, 63) / _mean(netinc, 252).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ROE proxy × equity ratio × close
def f02arp_f02_allowed_roe_proxy_roexeqratio_252d_base_v055_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    er = _mean(equity, 63) / _mean(equity, 252).replace(0, np.nan)
    result = base * er * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ROE proxy mean × ATR × close
def f02arp_f02_allowed_roe_proxy_roexatr_63d_base_v056_signal(netinc, equity, closeadj, high, low):
    base = _f02_roe_proxy(netinc, equity)
    atr = (high - low).rolling(21, min_periods=5).mean()
    result = _mean(base, 63) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# ROE proxy × ATR × close (252d)
def f02arp_f02_allowed_roe_proxy_roexatr_252d_base_v057_signal(netinc, equity, closeadj, high, low):
    base = _f02_roe_proxy(netinc, equity)
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = _mean(base, 252) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROE dynamics × close pct
def f02arp_f02_allowed_roe_proxy_roedynxret_63d_base_v058_signal(netinc, equity, closeadj):
    base = _f02_roe_dynamics(netinc, equity, 63)
    p = closeadj.pct_change(21)
    result = base * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROE dynamics × close pct
def f02arp_f02_allowed_roe_proxy_roedynxret_252d_base_v059_signal(netinc, equity, closeadj):
    base = _f02_roe_dynamics(netinc, equity, 252)
    p = closeadj.pct_change(63)
    result = base * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROE dynamics squared × close
def f02arp_f02_allowed_roe_proxy_roedynsq_63d_base_v060_signal(netinc, equity, closeadj):
    base = _f02_roe_dynamics(netinc, equity, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROE dynamics squared × close
def f02arp_f02_allowed_roe_proxy_roedynsq_252d_base_v061_signal(netinc, equity, closeadj):
    base = _f02_roe_dynamics(netinc, equity, 252)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roe durability × volume
def f02arp_f02_allowed_roe_proxy_durxvol_252d_base_v062_signal(roe, closeadj, volume):
    base = _f02_roe_durability(roe, 252)
    result = base * _mean(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roe durability × volume × close
def f02arp_f02_allowed_roe_proxy_durxvol_63d_base_v063_signal(roe, closeadj, volume):
    base = _f02_roe_durability(roe, 63)
    result = base * _mean(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roe durability × ATR
def f02arp_f02_allowed_roe_proxy_durxatr_63d_base_v064_signal(roe, closeadj, high, low):
    base = _f02_roe_durability(roe, 63)
    atr = (high - low).rolling(21, min_periods=5).mean()
    result = base * atr
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roe durability × ATR
def f02arp_f02_allowed_roe_proxy_durxatr_252d_base_v065_signal(roe, closeadj, high, low):
    base = _f02_roe_durability(roe, 252)
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = base * atr
    return result.replace([np.inf, -np.inf], np.nan)


# ROE proxy × closeadj (raw signal scaled)
def f02arp_f02_allowed_roe_proxy_roeraw_252d_base_v066_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    result = base.ewm(span=126, min_periods=42).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ROE realization spread vs target × close
def f02arp_f02_allowed_roe_proxy_roespread_63d_base_v067_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    target = 0.10
    result = (base - target) * closeadj * _mean(base, 63) / _mean(base, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# ROE realization spread 252d × close
def f02arp_f02_allowed_roe_proxy_roespread_252d_base_v068_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    target = 0.10
    result = (base - target) * closeadj * _mean(base, 252) / _mean(base, 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROE dynamics × volume × close
def f02arp_f02_allowed_roe_proxy_dynxvol_63d_base_v069_signal(netinc, equity, closeadj, volume):
    base = _f02_roe_dynamics(netinc, equity, 63)
    result = base * _mean(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROE dynamics × volume × close
def f02arp_f02_allowed_roe_proxy_dynxvol_252d_base_v070_signal(netinc, equity, closeadj, volume):
    base = _f02_roe_dynamics(netinc, equity, 252)
    result = base * _mean(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROE proxy rank × close
def f02arp_f02_allowed_roe_proxy_proxyrank_63d_base_v071_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROE proxy rank × close
def f02arp_f02_allowed_roe_proxy_proxyrank_252d_base_v072_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    result = base.rolling(504, min_periods=126).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROE proxy log × close
def f02arp_f02_allowed_roe_proxy_proxylog_63d_base_v073_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    result = np.log(base.abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROE proxy log × close
def f02arp_f02_allowed_roe_proxy_proxylog_252d_base_v074_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    result = np.log(base.abs().replace(0, np.nan)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROE proxy × abs(close pct) × close
def f02arp_f02_allowed_roe_proxy_proxyxabsret_63d_base_v075_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    p = closeadj.pct_change(21).abs()
    result = base * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f02arp_f02_allowed_roe_proxy_roeproxy_21d_base_v001_signal,
    f02arp_f02_allowed_roe_proxy_roeproxy_63d_base_v002_signal,
    f02arp_f02_allowed_roe_proxy_roeproxy_126d_base_v003_signal,
    f02arp_f02_allowed_roe_proxy_roeproxy_252d_base_v004_signal,
    f02arp_f02_allowed_roe_proxy_roeproxy_504d_base_v005_signal,
    f02arp_f02_allowed_roe_proxy_roedyn_21d_base_v006_signal,
    f02arp_f02_allowed_roe_proxy_roedyn_63d_base_v007_signal,
    f02arp_f02_allowed_roe_proxy_roedyn_126d_base_v008_signal,
    f02arp_f02_allowed_roe_proxy_roedyn_252d_base_v009_signal,
    f02arp_f02_allowed_roe_proxy_roedyn_504d_base_v010_signal,
    f02arp_f02_allowed_roe_proxy_roedur_63d_base_v011_signal,
    f02arp_f02_allowed_roe_proxy_roedur_126d_base_v012_signal,
    f02arp_f02_allowed_roe_proxy_roedur_252d_base_v013_signal,
    f02arp_f02_allowed_roe_proxy_roedur_504d_base_v014_signal,
    f02arp_f02_allowed_roe_proxy_roez_21d_base_v015_signal,
    f02arp_f02_allowed_roe_proxy_roez_63d_base_v016_signal,
    f02arp_f02_allowed_roe_proxy_roez_252d_base_v017_signal,
    f02arp_f02_allowed_roe_proxy_roestd_21d_base_v018_signal,
    f02arp_f02_allowed_roe_proxy_roestd_63d_base_v019_signal,
    f02arp_f02_allowed_roe_proxy_roestd_252d_base_v020_signal,
    f02arp_f02_allowed_roe_proxy_roeraw_21d_base_v021_signal,
    f02arp_f02_allowed_roe_proxy_roeema_63d_base_v022_signal,
    f02arp_f02_allowed_roe_proxy_roeema_252d_base_v023_signal,
    f02arp_f02_allowed_roe_proxy_roereported_21d_base_v024_signal,
    f02arp_f02_allowed_roe_proxy_roereported_63d_base_v025_signal,
    f02arp_f02_allowed_roe_proxy_roereported_252d_base_v026_signal,
    f02arp_f02_allowed_roe_proxy_roeisstd_21d_base_v027_signal,
    f02arp_f02_allowed_roe_proxy_roeisstd_63d_base_v028_signal,
    f02arp_f02_allowed_roe_proxy_roeisstd_252d_base_v029_signal,
    f02arp_f02_allowed_roe_proxy_roeisz_21d_base_v030_signal,
    f02arp_f02_allowed_roe_proxy_roeisz_63d_base_v031_signal,
    f02arp_f02_allowed_roe_proxy_roegap_21d_base_v032_signal,
    f02arp_f02_allowed_roe_proxy_roegap_63d_base_v033_signal,
    f02arp_f02_allowed_roe_proxy_roeisema_63d_base_v034_signal,
    f02arp_f02_allowed_roe_proxy_roeisema_252d_base_v035_signal,
    f02arp_f02_allowed_roe_proxy_roerank_63d_base_v036_signal,
    f02arp_f02_allowed_roe_proxy_roerank_252d_base_v037_signal,
    f02arp_f02_allowed_roe_proxy_roeaccel_63d_base_v038_signal,
    f02arp_f02_allowed_roe_proxy_roeaccel_252d_base_v039_signal,
    f02arp_f02_allowed_roe_proxy_roexvol_21d_base_v040_signal,
    f02arp_f02_allowed_roe_proxy_roexvol_63d_base_v041_signal,
    f02arp_f02_allowed_roe_proxy_roexdv_21d_base_v042_signal,
    f02arp_f02_allowed_roe_proxy_roexdv_63d_base_v043_signal,
    f02arp_f02_allowed_roe_proxy_roeproxy_5d_base_v044_signal,
    f02arp_f02_allowed_roe_proxy_roeproxy_10d_base_v045_signal,
    f02arp_f02_allowed_roe_proxy_roeproxy_42d_base_v046_signal,
    f02arp_f02_allowed_roe_proxy_roeproxy_189d_base_v047_signal,
    f02arp_f02_allowed_roe_proxy_roeproxy_378d_base_v048_signal,
    f02arp_f02_allowed_roe_proxy_roechg_21d_base_v049_signal,
    f02arp_f02_allowed_roe_proxy_roechg_63d_base_v050_signal,
    f02arp_f02_allowed_roe_proxy_roechg_252d_base_v051_signal,
    f02arp_f02_allowed_roe_proxy_roexsize_63d_base_v052_signal,
    f02arp_f02_allowed_roe_proxy_roexeqsize_63d_base_v053_signal,
    f02arp_f02_allowed_roe_proxy_roexnetinc_63d_base_v054_signal,
    f02arp_f02_allowed_roe_proxy_roexeqratio_252d_base_v055_signal,
    f02arp_f02_allowed_roe_proxy_roexatr_63d_base_v056_signal,
    f02arp_f02_allowed_roe_proxy_roexatr_252d_base_v057_signal,
    f02arp_f02_allowed_roe_proxy_roedynxret_63d_base_v058_signal,
    f02arp_f02_allowed_roe_proxy_roedynxret_252d_base_v059_signal,
    f02arp_f02_allowed_roe_proxy_roedynsq_63d_base_v060_signal,
    f02arp_f02_allowed_roe_proxy_roedynsq_252d_base_v061_signal,
    f02arp_f02_allowed_roe_proxy_durxvol_252d_base_v062_signal,
    f02arp_f02_allowed_roe_proxy_durxvol_63d_base_v063_signal,
    f02arp_f02_allowed_roe_proxy_durxatr_63d_base_v064_signal,
    f02arp_f02_allowed_roe_proxy_durxatr_252d_base_v065_signal,
    f02arp_f02_allowed_roe_proxy_roeraw_252d_base_v066_signal,
    f02arp_f02_allowed_roe_proxy_roespread_63d_base_v067_signal,
    f02arp_f02_allowed_roe_proxy_roespread_252d_base_v068_signal,
    f02arp_f02_allowed_roe_proxy_dynxvol_63d_base_v069_signal,
    f02arp_f02_allowed_roe_proxy_dynxvol_252d_base_v070_signal,
    f02arp_f02_allowed_roe_proxy_proxyrank_63d_base_v071_signal,
    f02arp_f02_allowed_roe_proxy_proxyrank_252d_base_v072_signal,
    f02arp_f02_allowed_roe_proxy_proxylog_63d_base_v073_signal,
    f02arp_f02_allowed_roe_proxy_proxylog_252d_base_v074_signal,
    f02arp_f02_allowed_roe_proxy_proxyxabsret_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F02_ALLOWED_ROE_PROXY_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f02_allowed_roe_proxy_base_001_075_claude: {n_features} features pass")
