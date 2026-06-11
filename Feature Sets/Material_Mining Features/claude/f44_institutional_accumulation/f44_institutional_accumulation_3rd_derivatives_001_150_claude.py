import inspect
import numpy as np
import pandas as pd

# 3rd-derivative file (2nd MATH derivative = JERK of a base feature).
# Each function fully expands its base quantity inline, then takes the 2nd
# difference (acceleration of the base trend) over windows scaled to the base horizon.

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _logroc(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


def _own_pct(totalvalue, marketcap):
    return totalvalue / marketcap.replace(0, np.nan)


def _vph(totalvalue, shrholders):
    return totalvalue / shrholders.replace(0, np.nan)


def _uph(shrunits, shrholders):
    return shrunits / shrholders.replace(0, np.nan)


def _implpx(totalvalue, shrunits):
    return totalvalue / shrunits.replace(0, np.nan)


# jerk (2nd deriv) of log holder count via j_a
def f44ia_f44_institutional_accumulation_holdlog_j_a_jerk_v001_signal(shrholders):
    base = np.log(shrholders.replace(0, np.nan))
    d = base - base.shift(21)
    b = d - d.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log holder count via j_b
def f44ia_f44_institutional_accumulation_holdlog_j_b_jerk_v002_signal(shrholders):
    base = np.log(shrholders.replace(0, np.nan))
    d = base - base.shift(63)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log holder count via j_c
def f44ia_f44_institutional_accumulation_holdlog_j_c_jerk_v003_signal(shrholders):
    base = np.log(shrholders.replace(0, np.nan))
    d = base - base.shift(126)
    b = d - d.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log holder count via zj_a
def f44ia_f44_institutional_accumulation_holdlog_zj_a_jerk_v004_signal(shrholders):
    base = np.log(shrholders.replace(0, np.nan))
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = _z(jk, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log holder count via zj_b
def f44ia_f44_institutional_accumulation_holdlog_zj_b_jerk_v005_signal(shrholders):
    base = np.log(shrholders.replace(0, np.nan))
    d = base - base.shift(63)
    jk = d - d.shift(63)
    b = _z(jk, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log holder count via rankj_a
def f44ia_f44_institutional_accumulation_holdlog_rankj_a_jerk_v006_signal(shrholders):
    base = np.log(shrholders.replace(0, np.nan))
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = jk.rolling(126, min_periods=42).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log holder count via normj_b
def f44ia_f44_institutional_accumulation_holdlog_normj_b_jerk_v007_signal(shrholders):
    base = np.log(shrholders.replace(0, np.nan))
    d = base - base.shift(126)
    jk = d - d.shift(21)
    sd = base.diff().rolling(126, min_periods=63).std()
    b = jk / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log holder count via tanhj_a
def f44ia_f44_institutional_accumulation_holdlog_tanhj_a_jerk_v008_signal(shrholders):
    base = np.log(shrholders.replace(0, np.nan))
    d = base - base.shift(21)
    jk = d - d.shift(21)
    sc = jk.rolling(126, min_periods=63).std()
    b = np.tanh(1.5 * jk / sc.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log holder count via emaj_a
def f44ia_f44_institutional_accumulation_holdlog_emaj_a_jerk_v009_signal(shrholders):
    base = np.log(shrholders.replace(0, np.nan))
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = jk.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log holder count via jmix
def f44ia_f44_institutional_accumulation_holdlog_jmix_jerk_v010_signal(shrholders):
    base = np.log(shrholders.replace(0, np.nan))
    d1 = base - base.shift(21)
    d2 = base - base.shift(63)
    b = (d1 - d1.shift(21)) - 0.5 * (d2 - d2.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log inst value via j_a
def f44ia_f44_institutional_accumulation_vallog_j_a_jerk_v011_signal(totalvalue):
    base = np.log(totalvalue.replace(0, np.nan))
    d = base - base.shift(21)
    b = d - d.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log inst value via j_b
def f44ia_f44_institutional_accumulation_vallog_j_b_jerk_v012_signal(totalvalue):
    base = np.log(totalvalue.replace(0, np.nan))
    d = base - base.shift(63)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log inst value via j_c
def f44ia_f44_institutional_accumulation_vallog_j_c_jerk_v013_signal(totalvalue):
    base = np.log(totalvalue.replace(0, np.nan))
    d = base - base.shift(126)
    b = d - d.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log inst value via zj_a
def f44ia_f44_institutional_accumulation_vallog_zj_a_jerk_v014_signal(totalvalue):
    base = np.log(totalvalue.replace(0, np.nan))
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = _z(jk, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log inst value via zj_b
def f44ia_f44_institutional_accumulation_vallog_zj_b_jerk_v015_signal(totalvalue):
    base = np.log(totalvalue.replace(0, np.nan))
    d = base - base.shift(63)
    jk = d - d.shift(63)
    b = _z(jk, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log inst value via rankj_a
def f44ia_f44_institutional_accumulation_vallog_rankj_a_jerk_v016_signal(totalvalue):
    base = np.log(totalvalue.replace(0, np.nan))
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = jk.rolling(126, min_periods=42).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log inst value via normj_b
def f44ia_f44_institutional_accumulation_vallog_normj_b_jerk_v017_signal(totalvalue):
    base = np.log(totalvalue.replace(0, np.nan))
    d = base - base.shift(126)
    jk = d - d.shift(21)
    sd = base.diff().rolling(126, min_periods=63).std()
    b = jk / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log inst value via tanhj_a
def f44ia_f44_institutional_accumulation_vallog_tanhj_a_jerk_v018_signal(totalvalue):
    base = np.log(totalvalue.replace(0, np.nan))
    d = base - base.shift(21)
    jk = d - d.shift(21)
    sc = jk.rolling(126, min_periods=63).std()
    b = np.tanh(1.5 * jk / sc.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log inst value via emaj_a
def f44ia_f44_institutional_accumulation_vallog_emaj_a_jerk_v019_signal(totalvalue):
    base = np.log(totalvalue.replace(0, np.nan))
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = jk.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log inst value via jmix
def f44ia_f44_institutional_accumulation_vallog_jmix_jerk_v020_signal(totalvalue):
    base = np.log(totalvalue.replace(0, np.nan))
    d1 = base - base.shift(21)
    d2 = base - base.shift(63)
    b = (d1 - d1.shift(21)) - 0.5 * (d2 - d2.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log inst units via j_a
def f44ia_f44_institutional_accumulation_unitlog_j_a_jerk_v021_signal(shrunits):
    base = np.log(shrunits.replace(0, np.nan))
    d = base - base.shift(21)
    b = d - d.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log inst units via j_b
def f44ia_f44_institutional_accumulation_unitlog_j_b_jerk_v022_signal(shrunits):
    base = np.log(shrunits.replace(0, np.nan))
    d = base - base.shift(63)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log inst units via j_c
def f44ia_f44_institutional_accumulation_unitlog_j_c_jerk_v023_signal(shrunits):
    base = np.log(shrunits.replace(0, np.nan))
    d = base - base.shift(126)
    b = d - d.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log inst units via zj_a
def f44ia_f44_institutional_accumulation_unitlog_zj_a_jerk_v024_signal(shrunits):
    base = np.log(shrunits.replace(0, np.nan))
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = _z(jk, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log inst units via zj_b
def f44ia_f44_institutional_accumulation_unitlog_zj_b_jerk_v025_signal(shrunits):
    base = np.log(shrunits.replace(0, np.nan))
    d = base - base.shift(63)
    jk = d - d.shift(63)
    b = _z(jk, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log inst units via rankj_a
def f44ia_f44_institutional_accumulation_unitlog_rankj_a_jerk_v026_signal(shrunits):
    base = np.log(shrunits.replace(0, np.nan))
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = jk.rolling(126, min_periods=42).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log inst units via normj_b
def f44ia_f44_institutional_accumulation_unitlog_normj_b_jerk_v027_signal(shrunits):
    base = np.log(shrunits.replace(0, np.nan))
    d = base - base.shift(126)
    jk = d - d.shift(21)
    sd = base.diff().rolling(126, min_periods=63).std()
    b = jk / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log inst units via tanhj_a
def f44ia_f44_institutional_accumulation_unitlog_tanhj_a_jerk_v028_signal(shrunits):
    base = np.log(shrunits.replace(0, np.nan))
    d = base - base.shift(21)
    jk = d - d.shift(21)
    sc = jk.rolling(126, min_periods=63).std()
    b = np.tanh(1.5 * jk / sc.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log inst units via emaj_a
def f44ia_f44_institutional_accumulation_unitlog_emaj_a_jerk_v029_signal(shrunits):
    base = np.log(shrunits.replace(0, np.nan))
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = jk.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log inst units via jmix
def f44ia_f44_institutional_accumulation_unitlog_jmix_jerk_v030_signal(shrunits):
    base = np.log(shrunits.replace(0, np.nan))
    d1 = base - base.shift(21)
    d2 = base - base.shift(63)
    b = (d1 - d1.shift(21)) - 0.5 * (d2 - d2.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of inst ownership pct via j_a
def f44ia_f44_institutional_accumulation_ownpct_j_a_jerk_v031_signal(totalvalue, marketcap):
    base = _own_pct(totalvalue, marketcap)
    d = base - base.shift(21)
    b = d - d.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of inst ownership pct via j_b
def f44ia_f44_institutional_accumulation_ownpct_j_b_jerk_v032_signal(totalvalue, marketcap):
    base = _own_pct(totalvalue, marketcap)
    d = base - base.shift(63)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of inst ownership pct via j_c
def f44ia_f44_institutional_accumulation_ownpct_j_c_jerk_v033_signal(totalvalue, marketcap):
    base = _own_pct(totalvalue, marketcap)
    d = base - base.shift(126)
    b = d - d.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of inst ownership pct via zj_a
def f44ia_f44_institutional_accumulation_ownpct_zj_a_jerk_v034_signal(totalvalue, marketcap):
    base = _own_pct(totalvalue, marketcap)
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = _z(jk, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of inst ownership pct via zj_b
def f44ia_f44_institutional_accumulation_ownpct_zj_b_jerk_v035_signal(totalvalue, marketcap):
    base = _own_pct(totalvalue, marketcap)
    d = base - base.shift(63)
    jk = d - d.shift(63)
    b = _z(jk, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of inst ownership pct via rankj_a
def f44ia_f44_institutional_accumulation_ownpct_rankj_a_jerk_v036_signal(totalvalue, marketcap):
    base = _own_pct(totalvalue, marketcap)
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = jk.rolling(126, min_periods=42).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of inst ownership pct via normj_b
def f44ia_f44_institutional_accumulation_ownpct_normj_b_jerk_v037_signal(totalvalue, marketcap):
    base = _own_pct(totalvalue, marketcap)
    d = base - base.shift(126)
    jk = d - d.shift(21)
    sd = base.diff().rolling(126, min_periods=63).std()
    b = jk / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of inst ownership pct via tanhj_a
def f44ia_f44_institutional_accumulation_ownpct_tanhj_a_jerk_v038_signal(totalvalue, marketcap):
    base = _own_pct(totalvalue, marketcap)
    d = base - base.shift(21)
    jk = d - d.shift(21)
    sc = jk.rolling(126, min_periods=63).std()
    b = np.tanh(1.5 * jk / sc.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of inst ownership pct via emaj_a
def f44ia_f44_institutional_accumulation_ownpct_emaj_a_jerk_v039_signal(totalvalue, marketcap):
    base = _own_pct(totalvalue, marketcap)
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = jk.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of inst ownership pct via jmix
def f44ia_f44_institutional_accumulation_ownpct_jmix_jerk_v040_signal(totalvalue, marketcap):
    base = _own_pct(totalvalue, marketcap)
    d1 = base - base.shift(21)
    d2 = base - base.shift(63)
    b = (d1 - d1.shift(21)) - 0.5 * (d2 - d2.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log value per holder via j_a
def f44ia_f44_institutional_accumulation_vphlog_j_a_jerk_v041_signal(totalvalue, shrholders):
    base = np.log(_vph(totalvalue, shrholders).replace(0, np.nan))
    d = base - base.shift(21)
    b = d - d.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log value per holder via j_b
def f44ia_f44_institutional_accumulation_vphlog_j_b_jerk_v042_signal(totalvalue, shrholders):
    base = np.log(_vph(totalvalue, shrholders).replace(0, np.nan))
    d = base - base.shift(63)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log value per holder via j_c
def f44ia_f44_institutional_accumulation_vphlog_j_c_jerk_v043_signal(totalvalue, shrholders):
    base = np.log(_vph(totalvalue, shrholders).replace(0, np.nan))
    d = base - base.shift(126)
    b = d - d.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log value per holder via zj_a
def f44ia_f44_institutional_accumulation_vphlog_zj_a_jerk_v044_signal(totalvalue, shrholders):
    base = np.log(_vph(totalvalue, shrholders).replace(0, np.nan))
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = _z(jk, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log value per holder via zj_b
def f44ia_f44_institutional_accumulation_vphlog_zj_b_jerk_v045_signal(totalvalue, shrholders):
    base = np.log(_vph(totalvalue, shrholders).replace(0, np.nan))
    d = base - base.shift(63)
    jk = d - d.shift(63)
    b = _z(jk, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log value per holder via rankj_a
def f44ia_f44_institutional_accumulation_vphlog_rankj_a_jerk_v046_signal(totalvalue, shrholders):
    base = np.log(_vph(totalvalue, shrholders).replace(0, np.nan))
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = jk.rolling(126, min_periods=42).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log value per holder via normj_b
def f44ia_f44_institutional_accumulation_vphlog_normj_b_jerk_v047_signal(totalvalue, shrholders):
    base = np.log(_vph(totalvalue, shrholders).replace(0, np.nan))
    d = base - base.shift(126)
    jk = d - d.shift(21)
    sd = base.diff().rolling(126, min_periods=63).std()
    b = jk / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log value per holder via tanhj_a
def f44ia_f44_institutional_accumulation_vphlog_tanhj_a_jerk_v048_signal(totalvalue, shrholders):
    base = np.log(_vph(totalvalue, shrholders).replace(0, np.nan))
    d = base - base.shift(21)
    jk = d - d.shift(21)
    sc = jk.rolling(126, min_periods=63).std()
    b = np.tanh(1.5 * jk / sc.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log value per holder via emaj_a
def f44ia_f44_institutional_accumulation_vphlog_emaj_a_jerk_v049_signal(totalvalue, shrholders):
    base = np.log(_vph(totalvalue, shrholders).replace(0, np.nan))
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = jk.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log value per holder via jmix
def f44ia_f44_institutional_accumulation_vphlog_jmix_jerk_v050_signal(totalvalue, shrholders):
    base = np.log(_vph(totalvalue, shrholders).replace(0, np.nan))
    d1 = base - base.shift(21)
    d2 = base - base.shift(63)
    b = (d1 - d1.shift(21)) - 0.5 * (d2 - d2.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log units per holder via j_a
def f44ia_f44_institutional_accumulation_uphlog_j_a_jerk_v051_signal(shrunits, shrholders):
    base = np.log(_uph(shrunits, shrholders).replace(0, np.nan))
    d = base - base.shift(21)
    b = d - d.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log units per holder via j_b
def f44ia_f44_institutional_accumulation_uphlog_j_b_jerk_v052_signal(shrunits, shrholders):
    base = np.log(_uph(shrunits, shrholders).replace(0, np.nan))
    d = base - base.shift(63)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log units per holder via j_c
def f44ia_f44_institutional_accumulation_uphlog_j_c_jerk_v053_signal(shrunits, shrholders):
    base = np.log(_uph(shrunits, shrholders).replace(0, np.nan))
    d = base - base.shift(126)
    b = d - d.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log units per holder via zj_a
def f44ia_f44_institutional_accumulation_uphlog_zj_a_jerk_v054_signal(shrunits, shrholders):
    base = np.log(_uph(shrunits, shrholders).replace(0, np.nan))
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = _z(jk, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log units per holder via zj_b
def f44ia_f44_institutional_accumulation_uphlog_zj_b_jerk_v055_signal(shrunits, shrholders):
    base = np.log(_uph(shrunits, shrholders).replace(0, np.nan))
    d = base - base.shift(63)
    jk = d - d.shift(63)
    b = _z(jk, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log units per holder via rankj_a
def f44ia_f44_institutional_accumulation_uphlog_rankj_a_jerk_v056_signal(shrunits, shrholders):
    base = np.log(_uph(shrunits, shrholders).replace(0, np.nan))
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = jk.rolling(126, min_periods=42).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log units per holder via normj_b
def f44ia_f44_institutional_accumulation_uphlog_normj_b_jerk_v057_signal(shrunits, shrholders):
    base = np.log(_uph(shrunits, shrholders).replace(0, np.nan))
    d = base - base.shift(126)
    jk = d - d.shift(21)
    sd = base.diff().rolling(126, min_periods=63).std()
    b = jk / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log units per holder via tanhj_a
def f44ia_f44_institutional_accumulation_uphlog_tanhj_a_jerk_v058_signal(shrunits, shrholders):
    base = np.log(_uph(shrunits, shrholders).replace(0, np.nan))
    d = base - base.shift(21)
    jk = d - d.shift(21)
    sc = jk.rolling(126, min_periods=63).std()
    b = np.tanh(1.5 * jk / sc.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log units per holder via emaj_a
def f44ia_f44_institutional_accumulation_uphlog_emaj_a_jerk_v059_signal(shrunits, shrholders):
    base = np.log(_uph(shrunits, shrholders).replace(0, np.nan))
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = jk.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log units per holder via jmix
def f44ia_f44_institutional_accumulation_uphlog_jmix_jerk_v060_signal(shrunits, shrholders):
    base = np.log(_uph(shrunits, shrholders).replace(0, np.nan))
    d1 = base - base.shift(21)
    d2 = base - base.shift(63)
    b = (d1 - d1.shift(21)) - 0.5 * (d2 - d2.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log implied price (value/units) via j_a
def f44ia_f44_institutional_accumulation_implpxlog_j_a_jerk_v061_signal(totalvalue, shrunits):
    base = np.log(_implpx(totalvalue, shrunits).replace(0, np.nan))
    d = base - base.shift(21)
    b = d - d.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log implied price (value/units) via j_b
def f44ia_f44_institutional_accumulation_implpxlog_j_b_jerk_v062_signal(totalvalue, shrunits):
    base = np.log(_implpx(totalvalue, shrunits).replace(0, np.nan))
    d = base - base.shift(63)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log implied price (value/units) via j_c
def f44ia_f44_institutional_accumulation_implpxlog_j_c_jerk_v063_signal(totalvalue, shrunits):
    base = np.log(_implpx(totalvalue, shrunits).replace(0, np.nan))
    d = base - base.shift(126)
    b = d - d.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log implied price (value/units) via zj_a
def f44ia_f44_institutional_accumulation_implpxlog_zj_a_jerk_v064_signal(totalvalue, shrunits):
    base = np.log(_implpx(totalvalue, shrunits).replace(0, np.nan))
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = _z(jk, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log implied price (value/units) via zj_b
def f44ia_f44_institutional_accumulation_implpxlog_zj_b_jerk_v065_signal(totalvalue, shrunits):
    base = np.log(_implpx(totalvalue, shrunits).replace(0, np.nan))
    d = base - base.shift(63)
    jk = d - d.shift(63)
    b = _z(jk, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log implied price (value/units) via rankj_a
def f44ia_f44_institutional_accumulation_implpxlog_rankj_a_jerk_v066_signal(totalvalue, shrunits):
    base = np.log(_implpx(totalvalue, shrunits).replace(0, np.nan))
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = jk.rolling(126, min_periods=42).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log implied price (value/units) via normj_b
def f44ia_f44_institutional_accumulation_implpxlog_normj_b_jerk_v067_signal(totalvalue, shrunits):
    base = np.log(_implpx(totalvalue, shrunits).replace(0, np.nan))
    d = base - base.shift(126)
    jk = d - d.shift(21)
    sd = base.diff().rolling(126, min_periods=63).std()
    b = jk / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log implied price (value/units) via tanhj_a
def f44ia_f44_institutional_accumulation_implpxlog_tanhj_a_jerk_v068_signal(totalvalue, shrunits):
    base = np.log(_implpx(totalvalue, shrunits).replace(0, np.nan))
    d = base - base.shift(21)
    jk = d - d.shift(21)
    sc = jk.rolling(126, min_periods=63).std()
    b = np.tanh(1.5 * jk / sc.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log implied price (value/units) via emaj_a
def f44ia_f44_institutional_accumulation_implpxlog_emaj_a_jerk_v069_signal(totalvalue, shrunits):
    base = np.log(_implpx(totalvalue, shrunits).replace(0, np.nan))
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = jk.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log implied price (value/units) via jmix
def f44ia_f44_institutional_accumulation_implpxlog_jmix_jerk_v070_signal(totalvalue, shrunits):
    base = np.log(_implpx(totalvalue, shrunits).replace(0, np.nan))
    d1 = base - base.shift(21)
    d2 = base - base.shift(63)
    b = (d1 - d1.shift(21)) - 0.5 * (d2 - d2.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log per-filing shrvalue via j_a
def f44ia_f44_institutional_accumulation_shrvallog_j_a_jerk_v071_signal(shrvalue):
    base = np.log(shrvalue.replace(0, np.nan))
    d = base - base.shift(21)
    b = d - d.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log per-filing shrvalue via j_b
def f44ia_f44_institutional_accumulation_shrvallog_j_b_jerk_v072_signal(shrvalue):
    base = np.log(shrvalue.replace(0, np.nan))
    d = base - base.shift(63)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log per-filing shrvalue via j_c
def f44ia_f44_institutional_accumulation_shrvallog_j_c_jerk_v073_signal(shrvalue):
    base = np.log(shrvalue.replace(0, np.nan))
    d = base - base.shift(126)
    b = d - d.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log per-filing shrvalue via zj_a
def f44ia_f44_institutional_accumulation_shrvallog_zj_a_jerk_v074_signal(shrvalue):
    base = np.log(shrvalue.replace(0, np.nan))
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = _z(jk, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log per-filing shrvalue via zj_b
def f44ia_f44_institutional_accumulation_shrvallog_zj_b_jerk_v075_signal(shrvalue):
    base = np.log(shrvalue.replace(0, np.nan))
    d = base - base.shift(63)
    jk = d - d.shift(63)
    b = _z(jk, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log per-filing shrvalue via rankj_a
def f44ia_f44_institutional_accumulation_shrvallog_rankj_a_jerk_v076_signal(shrvalue):
    base = np.log(shrvalue.replace(0, np.nan))
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = jk.rolling(126, min_periods=42).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log per-filing shrvalue via normj_b
def f44ia_f44_institutional_accumulation_shrvallog_normj_b_jerk_v077_signal(shrvalue):
    base = np.log(shrvalue.replace(0, np.nan))
    d = base - base.shift(126)
    jk = d - d.shift(21)
    sd = base.diff().rolling(126, min_periods=63).std()
    b = jk / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log per-filing shrvalue via tanhj_a
def f44ia_f44_institutional_accumulation_shrvallog_tanhj_a_jerk_v078_signal(shrvalue):
    base = np.log(shrvalue.replace(0, np.nan))
    d = base - base.shift(21)
    jk = d - d.shift(21)
    sc = jk.rolling(126, min_periods=63).std()
    b = np.tanh(1.5 * jk / sc.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log per-filing shrvalue via emaj_a
def f44ia_f44_institutional_accumulation_shrvallog_emaj_a_jerk_v079_signal(shrvalue):
    base = np.log(shrvalue.replace(0, np.nan))
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = jk.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log per-filing shrvalue via jmix
def f44ia_f44_institutional_accumulation_shrvallog_jmix_jerk_v080_signal(shrvalue):
    base = np.log(shrvalue.replace(0, np.nan))
    d1 = base - base.shift(21)
    d2 = base - base.shift(63)
    b = (d1 - d1.shift(21)) - 0.5 * (d2 - d2.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of shrvalue concentration share via j_a
def f44ia_f44_institutional_accumulation_shrvalshare_j_a_jerk_v081_signal(shrvalue, totalvalue):
    base = shrvalue / totalvalue.replace(0, np.nan)
    d = base - base.shift(21)
    b = d - d.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of shrvalue concentration share via j_b
def f44ia_f44_institutional_accumulation_shrvalshare_j_b_jerk_v082_signal(shrvalue, totalvalue):
    base = shrvalue / totalvalue.replace(0, np.nan)
    d = base - base.shift(63)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of shrvalue concentration share via j_c
def f44ia_f44_institutional_accumulation_shrvalshare_j_c_jerk_v083_signal(shrvalue, totalvalue):
    base = shrvalue / totalvalue.replace(0, np.nan)
    d = base - base.shift(126)
    b = d - d.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of shrvalue concentration share via zj_a
def f44ia_f44_institutional_accumulation_shrvalshare_zj_a_jerk_v084_signal(shrvalue, totalvalue):
    base = shrvalue / totalvalue.replace(0, np.nan)
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = _z(jk, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of shrvalue concentration share via zj_b
def f44ia_f44_institutional_accumulation_shrvalshare_zj_b_jerk_v085_signal(shrvalue, totalvalue):
    base = shrvalue / totalvalue.replace(0, np.nan)
    d = base - base.shift(63)
    jk = d - d.shift(63)
    b = _z(jk, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of shrvalue concentration share via rankj_a
def f44ia_f44_institutional_accumulation_shrvalshare_rankj_a_jerk_v086_signal(shrvalue, totalvalue):
    base = shrvalue / totalvalue.replace(0, np.nan)
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = jk.rolling(126, min_periods=42).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of shrvalue concentration share via normj_b
def f44ia_f44_institutional_accumulation_shrvalshare_normj_b_jerk_v087_signal(shrvalue, totalvalue):
    base = shrvalue / totalvalue.replace(0, np.nan)
    d = base - base.shift(126)
    jk = d - d.shift(21)
    sd = base.diff().rolling(126, min_periods=63).std()
    b = jk / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of shrvalue concentration share via tanhj_a
def f44ia_f44_institutional_accumulation_shrvalshare_tanhj_a_jerk_v088_signal(shrvalue, totalvalue):
    base = shrvalue / totalvalue.replace(0, np.nan)
    d = base - base.shift(21)
    jk = d - d.shift(21)
    sc = jk.rolling(126, min_periods=63).std()
    b = np.tanh(1.5 * jk / sc.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of shrvalue concentration share via emaj_a
def f44ia_f44_institutional_accumulation_shrvalshare_emaj_a_jerk_v089_signal(shrvalue, totalvalue):
    base = shrvalue / totalvalue.replace(0, np.nan)
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = jk.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of shrvalue concentration share via jmix
def f44ia_f44_institutional_accumulation_shrvalshare_jmix_jerk_v090_signal(shrvalue, totalvalue):
    base = shrvalue / totalvalue.replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = base - base.shift(63)
    b = (d1 - d1.shift(21)) - 0.5 * (d2 - d2.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log per-filing value vs marketcap via j_a
def f44ia_f44_institutional_accumulation_shrvalmkt_j_a_jerk_v091_signal(shrvalue, marketcap):
    base = np.log((shrvalue / marketcap.replace(0, np.nan)).replace(0, np.nan))
    d = base - base.shift(21)
    b = d - d.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log per-filing value vs marketcap via j_b
def f44ia_f44_institutional_accumulation_shrvalmkt_j_b_jerk_v092_signal(shrvalue, marketcap):
    base = np.log((shrvalue / marketcap.replace(0, np.nan)).replace(0, np.nan))
    d = base - base.shift(63)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log per-filing value vs marketcap via j_c
def f44ia_f44_institutional_accumulation_shrvalmkt_j_c_jerk_v093_signal(shrvalue, marketcap):
    base = np.log((shrvalue / marketcap.replace(0, np.nan)).replace(0, np.nan))
    d = base - base.shift(126)
    b = d - d.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log per-filing value vs marketcap via zj_a
def f44ia_f44_institutional_accumulation_shrvalmkt_zj_a_jerk_v094_signal(shrvalue, marketcap):
    base = np.log((shrvalue / marketcap.replace(0, np.nan)).replace(0, np.nan))
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = _z(jk, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log per-filing value vs marketcap via zj_b
def f44ia_f44_institutional_accumulation_shrvalmkt_zj_b_jerk_v095_signal(shrvalue, marketcap):
    base = np.log((shrvalue / marketcap.replace(0, np.nan)).replace(0, np.nan))
    d = base - base.shift(63)
    jk = d - d.shift(63)
    b = _z(jk, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log per-filing value vs marketcap via rankj_a
def f44ia_f44_institutional_accumulation_shrvalmkt_rankj_a_jerk_v096_signal(shrvalue, marketcap):
    base = np.log((shrvalue / marketcap.replace(0, np.nan)).replace(0, np.nan))
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = jk.rolling(126, min_periods=42).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log per-filing value vs marketcap via normj_b
def f44ia_f44_institutional_accumulation_shrvalmkt_normj_b_jerk_v097_signal(shrvalue, marketcap):
    base = np.log((shrvalue / marketcap.replace(0, np.nan)).replace(0, np.nan))
    d = base - base.shift(126)
    jk = d - d.shift(21)
    sd = base.diff().rolling(126, min_periods=63).std()
    b = jk / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log per-filing value vs marketcap via tanhj_a
def f44ia_f44_institutional_accumulation_shrvalmkt_tanhj_a_jerk_v098_signal(shrvalue, marketcap):
    base = np.log((shrvalue / marketcap.replace(0, np.nan)).replace(0, np.nan))
    d = base - base.shift(21)
    jk = d - d.shift(21)
    sc = jk.rolling(126, min_periods=63).std()
    b = np.tanh(1.5 * jk / sc.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log per-filing value vs marketcap via emaj_a
def f44ia_f44_institutional_accumulation_shrvalmkt_emaj_a_jerk_v099_signal(shrvalue, marketcap):
    base = np.log((shrvalue / marketcap.replace(0, np.nan)).replace(0, np.nan))
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = jk.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of log per-filing value vs marketcap via jmix
def f44ia_f44_institutional_accumulation_shrvalmkt_jmix_jerk_v100_signal(shrvalue, marketcap):
    base = np.log((shrvalue / marketcap.replace(0, np.nan)).replace(0, np.nan))
    d1 = base - base.shift(21)
    d2 = base - base.shift(63)
    b = (d1 - d1.shift(21)) - 0.5 * (d2 - d2.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of ownership-pct z-score via j_a
def f44ia_f44_institutional_accumulation_ownpctz_j_a_jerk_v101_signal(totalvalue, marketcap):
    op = _own_pct(totalvalue, marketcap)
    base = _z(op, 252)
    d = base - base.shift(21)
    b = d - d.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of ownership-pct z-score via j_b
def f44ia_f44_institutional_accumulation_ownpctz_j_b_jerk_v102_signal(totalvalue, marketcap):
    op = _own_pct(totalvalue, marketcap)
    base = _z(op, 252)
    d = base - base.shift(63)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of ownership-pct z-score via j_c
def f44ia_f44_institutional_accumulation_ownpctz_j_c_jerk_v103_signal(totalvalue, marketcap):
    op = _own_pct(totalvalue, marketcap)
    base = _z(op, 252)
    d = base - base.shift(126)
    b = d - d.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of ownership-pct z-score via zj_a
def f44ia_f44_institutional_accumulation_ownpctz_zj_a_jerk_v104_signal(totalvalue, marketcap):
    op = _own_pct(totalvalue, marketcap)
    base = _z(op, 252)
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = _z(jk, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of ownership-pct z-score via zj_b
def f44ia_f44_institutional_accumulation_ownpctz_zj_b_jerk_v105_signal(totalvalue, marketcap):
    op = _own_pct(totalvalue, marketcap)
    base = _z(op, 252)
    d = base - base.shift(63)
    jk = d - d.shift(63)
    b = _z(jk, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of ownership-pct z-score via rankj_a
def f44ia_f44_institutional_accumulation_ownpctz_rankj_a_jerk_v106_signal(totalvalue, marketcap):
    op = _own_pct(totalvalue, marketcap)
    base = _z(op, 252)
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = jk.rolling(126, min_periods=42).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of ownership-pct z-score via normj_b
def f44ia_f44_institutional_accumulation_ownpctz_normj_b_jerk_v107_signal(totalvalue, marketcap):
    op = _own_pct(totalvalue, marketcap)
    base = _z(op, 252)
    d = base - base.shift(126)
    jk = d - d.shift(21)
    sd = base.diff().rolling(126, min_periods=63).std()
    b = jk / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of ownership-pct z-score via tanhj_a
def f44ia_f44_institutional_accumulation_ownpctz_tanhj_a_jerk_v108_signal(totalvalue, marketcap):
    op = _own_pct(totalvalue, marketcap)
    base = _z(op, 252)
    d = base - base.shift(21)
    jk = d - d.shift(21)
    sc = jk.rolling(126, min_periods=63).std()
    b = np.tanh(1.5 * jk / sc.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of ownership-pct z-score via emaj_a
def f44ia_f44_institutional_accumulation_ownpctz_emaj_a_jerk_v109_signal(totalvalue, marketcap):
    op = _own_pct(totalvalue, marketcap)
    base = _z(op, 252)
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = jk.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of ownership-pct z-score via jmix
def f44ia_f44_institutional_accumulation_ownpctz_jmix_jerk_v110_signal(totalvalue, marketcap):
    op = _own_pct(totalvalue, marketcap)
    base = _z(op, 252)
    d1 = base - base.shift(21)
    d2 = base - base.shift(63)
    b = (d1 - d1.shift(21)) - 0.5 * (d2 - d2.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of inst-value 504d range position via j_a
def f44ia_f44_institutional_accumulation_valrngpos_j_a_jerk_v111_signal(totalvalue):
    hi = _rmax(totalvalue, 504)
    lo = _rmin(totalvalue, 504)
    base = (totalvalue - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(21)
    b = d - d.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of inst-value 504d range position via j_b
def f44ia_f44_institutional_accumulation_valrngpos_j_b_jerk_v112_signal(totalvalue):
    hi = _rmax(totalvalue, 504)
    lo = _rmin(totalvalue, 504)
    base = (totalvalue - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(63)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of inst-value 504d range position via j_c
def f44ia_f44_institutional_accumulation_valrngpos_j_c_jerk_v113_signal(totalvalue):
    hi = _rmax(totalvalue, 504)
    lo = _rmin(totalvalue, 504)
    base = (totalvalue - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(126)
    b = d - d.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of inst-value 504d range position via zj_a
def f44ia_f44_institutional_accumulation_valrngpos_zj_a_jerk_v114_signal(totalvalue):
    hi = _rmax(totalvalue, 504)
    lo = _rmin(totalvalue, 504)
    base = (totalvalue - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = _z(jk, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of inst-value 504d range position via zj_b
def f44ia_f44_institutional_accumulation_valrngpos_zj_b_jerk_v115_signal(totalvalue):
    hi = _rmax(totalvalue, 504)
    lo = _rmin(totalvalue, 504)
    base = (totalvalue - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(63)
    jk = d - d.shift(63)
    b = _z(jk, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of inst-value 504d range position via rankj_a
def f44ia_f44_institutional_accumulation_valrngpos_rankj_a_jerk_v116_signal(totalvalue):
    hi = _rmax(totalvalue, 504)
    lo = _rmin(totalvalue, 504)
    base = (totalvalue - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = jk.rolling(126, min_periods=42).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of inst-value 504d range position via normj_b
def f44ia_f44_institutional_accumulation_valrngpos_normj_b_jerk_v117_signal(totalvalue):
    hi = _rmax(totalvalue, 504)
    lo = _rmin(totalvalue, 504)
    base = (totalvalue - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(126)
    jk = d - d.shift(21)
    sd = base.diff().rolling(126, min_periods=63).std()
    b = jk / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of inst-value 504d range position via tanhj_a
def f44ia_f44_institutional_accumulation_valrngpos_tanhj_a_jerk_v118_signal(totalvalue):
    hi = _rmax(totalvalue, 504)
    lo = _rmin(totalvalue, 504)
    base = (totalvalue - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(21)
    jk = d - d.shift(21)
    sc = jk.rolling(126, min_periods=63).std()
    b = np.tanh(1.5 * jk / sc.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of inst-value 504d range position via emaj_a
def f44ia_f44_institutional_accumulation_valrngpos_emaj_a_jerk_v119_signal(totalvalue):
    hi = _rmax(totalvalue, 504)
    lo = _rmin(totalvalue, 504)
    base = (totalvalue - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = jk.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of inst-value 504d range position via jmix
def f44ia_f44_institutional_accumulation_valrngpos_jmix_jerk_v120_signal(totalvalue):
    hi = _rmax(totalvalue, 504)
    lo = _rmin(totalvalue, 504)
    base = (totalvalue - lo) / (hi - lo).replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = base - base.shift(63)
    b = (d1 - d1.shift(21)) - 0.5 * (d2 - d2.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of holder 252d range position via j_a
def f44ia_f44_institutional_accumulation_holdrngpos_j_a_jerk_v121_signal(shrholders):
    hi = _rmax(shrholders, 252)
    lo = _rmin(shrholders, 252)
    base = (shrholders - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(21)
    b = d - d.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of holder 252d range position via j_b
def f44ia_f44_institutional_accumulation_holdrngpos_j_b_jerk_v122_signal(shrholders):
    hi = _rmax(shrholders, 252)
    lo = _rmin(shrholders, 252)
    base = (shrholders - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(63)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of holder 252d range position via j_c
def f44ia_f44_institutional_accumulation_holdrngpos_j_c_jerk_v123_signal(shrholders):
    hi = _rmax(shrholders, 252)
    lo = _rmin(shrholders, 252)
    base = (shrholders - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(126)
    b = d - d.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of holder 252d range position via zj_a
def f44ia_f44_institutional_accumulation_holdrngpos_zj_a_jerk_v124_signal(shrholders):
    hi = _rmax(shrholders, 252)
    lo = _rmin(shrholders, 252)
    base = (shrholders - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = _z(jk, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of holder 252d range position via zj_b
def f44ia_f44_institutional_accumulation_holdrngpos_zj_b_jerk_v125_signal(shrholders):
    hi = _rmax(shrholders, 252)
    lo = _rmin(shrholders, 252)
    base = (shrholders - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(63)
    jk = d - d.shift(63)
    b = _z(jk, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of holder 252d range position via rankj_a
def f44ia_f44_institutional_accumulation_holdrngpos_rankj_a_jerk_v126_signal(shrholders):
    hi = _rmax(shrholders, 252)
    lo = _rmin(shrholders, 252)
    base = (shrholders - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = jk.rolling(126, min_periods=42).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of holder 252d range position via normj_b
def f44ia_f44_institutional_accumulation_holdrngpos_normj_b_jerk_v127_signal(shrholders):
    hi = _rmax(shrholders, 252)
    lo = _rmin(shrholders, 252)
    base = (shrholders - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(126)
    jk = d - d.shift(21)
    sd = base.diff().rolling(126, min_periods=63).std()
    b = jk / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of holder 252d range position via tanhj_a
def f44ia_f44_institutional_accumulation_holdrngpos_tanhj_a_jerk_v128_signal(shrholders):
    hi = _rmax(shrholders, 252)
    lo = _rmin(shrholders, 252)
    base = (shrholders - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(21)
    jk = d - d.shift(21)
    sc = jk.rolling(126, min_periods=63).std()
    b = np.tanh(1.5 * jk / sc.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of holder 252d range position via emaj_a
def f44ia_f44_institutional_accumulation_holdrngpos_emaj_a_jerk_v129_signal(shrholders):
    hi = _rmax(shrholders, 252)
    lo = _rmin(shrholders, 252)
    base = (shrholders - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = jk.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of holder 252d range position via jmix
def f44ia_f44_institutional_accumulation_holdrngpos_jmix_jerk_v130_signal(shrholders):
    hi = _rmax(shrholders, 252)
    lo = _rmin(shrholders, 252)
    base = (shrholders - lo) / (hi - lo).replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = base - base.shift(63)
    b = (d1 - d1.shift(21)) - 0.5 * (d2 - d2.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of units 504d range position via j_a
def f44ia_f44_institutional_accumulation_unitrngpos_j_a_jerk_v131_signal(shrunits):
    hi = _rmax(shrunits, 504)
    lo = _rmin(shrunits, 504)
    base = (shrunits - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(21)
    b = d - d.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of units 504d range position via j_b
def f44ia_f44_institutional_accumulation_unitrngpos_j_b_jerk_v132_signal(shrunits):
    hi = _rmax(shrunits, 504)
    lo = _rmin(shrunits, 504)
    base = (shrunits - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(63)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of units 504d range position via j_c
def f44ia_f44_institutional_accumulation_unitrngpos_j_c_jerk_v133_signal(shrunits):
    hi = _rmax(shrunits, 504)
    lo = _rmin(shrunits, 504)
    base = (shrunits - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(126)
    b = d - d.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of units 504d range position via zj_a
def f44ia_f44_institutional_accumulation_unitrngpos_zj_a_jerk_v134_signal(shrunits):
    hi = _rmax(shrunits, 504)
    lo = _rmin(shrunits, 504)
    base = (shrunits - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = _z(jk, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of units 504d range position via zj_b
def f44ia_f44_institutional_accumulation_unitrngpos_zj_b_jerk_v135_signal(shrunits):
    hi = _rmax(shrunits, 504)
    lo = _rmin(shrunits, 504)
    base = (shrunits - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(63)
    jk = d - d.shift(63)
    b = _z(jk, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of units 504d range position via rankj_a
def f44ia_f44_institutional_accumulation_unitrngpos_rankj_a_jerk_v136_signal(shrunits):
    hi = _rmax(shrunits, 504)
    lo = _rmin(shrunits, 504)
    base = (shrunits - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = jk.rolling(126, min_periods=42).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of units 504d range position via normj_b
def f44ia_f44_institutional_accumulation_unitrngpos_normj_b_jerk_v137_signal(shrunits):
    hi = _rmax(shrunits, 504)
    lo = _rmin(shrunits, 504)
    base = (shrunits - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(126)
    jk = d - d.shift(21)
    sd = base.diff().rolling(126, min_periods=63).std()
    b = jk / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of units 504d range position via tanhj_a
def f44ia_f44_institutional_accumulation_unitrngpos_tanhj_a_jerk_v138_signal(shrunits):
    hi = _rmax(shrunits, 504)
    lo = _rmin(shrunits, 504)
    base = (shrunits - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(21)
    jk = d - d.shift(21)
    sc = jk.rolling(126, min_periods=63).std()
    b = np.tanh(1.5 * jk / sc.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of units 504d range position via emaj_a
def f44ia_f44_institutional_accumulation_unitrngpos_emaj_a_jerk_v139_signal(shrunits):
    hi = _rmax(shrunits, 504)
    lo = _rmin(shrunits, 504)
    base = (shrunits - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = jk.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of units 504d range position via jmix
def f44ia_f44_institutional_accumulation_unitrngpos_jmix_jerk_v140_signal(shrunits):
    hi = _rmax(shrunits, 504)
    lo = _rmin(shrunits, 504)
    base = (shrunits - lo) / (hi - lo).replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = base - base.shift(63)
    b = (d1 - d1.shift(21)) - 0.5 * (d2 - d2.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of ownership-pct 504d rank via j_a
def f44ia_f44_institutional_accumulation_ownpctrank_j_a_jerk_v141_signal(totalvalue, marketcap):
    op = _own_pct(totalvalue, marketcap)
    base = _rank(op, 504)
    d = base - base.shift(21)
    b = d - d.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of ownership-pct 504d rank via j_b
def f44ia_f44_institutional_accumulation_ownpctrank_j_b_jerk_v142_signal(totalvalue, marketcap):
    op = _own_pct(totalvalue, marketcap)
    base = _rank(op, 504)
    d = base - base.shift(63)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of ownership-pct 504d rank via j_c
def f44ia_f44_institutional_accumulation_ownpctrank_j_c_jerk_v143_signal(totalvalue, marketcap):
    op = _own_pct(totalvalue, marketcap)
    base = _rank(op, 504)
    d = base - base.shift(126)
    b = d - d.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of ownership-pct 504d rank via zj_a
def f44ia_f44_institutional_accumulation_ownpctrank_zj_a_jerk_v144_signal(totalvalue, marketcap):
    op = _own_pct(totalvalue, marketcap)
    base = _rank(op, 504)
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = _z(jk, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of ownership-pct 504d rank via zj_b
def f44ia_f44_institutional_accumulation_ownpctrank_zj_b_jerk_v145_signal(totalvalue, marketcap):
    op = _own_pct(totalvalue, marketcap)
    base = _rank(op, 504)
    d = base - base.shift(63)
    jk = d - d.shift(63)
    b = _z(jk, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of ownership-pct 504d rank via rankj_a
def f44ia_f44_institutional_accumulation_ownpctrank_rankj_a_jerk_v146_signal(totalvalue, marketcap):
    op = _own_pct(totalvalue, marketcap)
    base = _rank(op, 504)
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = jk.rolling(126, min_periods=42).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of ownership-pct 504d rank via normj_b
def f44ia_f44_institutional_accumulation_ownpctrank_normj_b_jerk_v147_signal(totalvalue, marketcap):
    op = _own_pct(totalvalue, marketcap)
    base = _rank(op, 504)
    d = base - base.shift(126)
    jk = d - d.shift(21)
    sd = base.diff().rolling(126, min_periods=63).std()
    b = jk / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of ownership-pct 504d rank via tanhj_a
def f44ia_f44_institutional_accumulation_ownpctrank_tanhj_a_jerk_v148_signal(totalvalue, marketcap):
    op = _own_pct(totalvalue, marketcap)
    base = _rank(op, 504)
    d = base - base.shift(21)
    jk = d - d.shift(21)
    sc = jk.rolling(126, min_periods=63).std()
    b = np.tanh(1.5 * jk / sc.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of ownership-pct 504d rank via emaj_a
def f44ia_f44_institutional_accumulation_ownpctrank_emaj_a_jerk_v149_signal(totalvalue, marketcap):
    op = _own_pct(totalvalue, marketcap)
    base = _rank(op, 504)
    d = base - base.shift(21)
    jk = d - d.shift(21)
    b = jk.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv) of ownership-pct 504d rank via jmix
def f44ia_f44_institutional_accumulation_ownpctrank_jmix_jerk_v150_signal(totalvalue, marketcap):
    op = _own_pct(totalvalue, marketcap)
    base = _rank(op, 504)
    d1 = base - base.shift(21)
    d2 = base - base.shift(63)
    b = (d1 - d1.shift(21)) - 0.5 * (d2 - d2.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f44ia_f44_institutional_accumulation_holdlog_j_a_jerk_v001_signal,
    f44ia_f44_institutional_accumulation_holdlog_j_b_jerk_v002_signal,
    f44ia_f44_institutional_accumulation_holdlog_j_c_jerk_v003_signal,
    f44ia_f44_institutional_accumulation_holdlog_zj_a_jerk_v004_signal,
    f44ia_f44_institutional_accumulation_holdlog_zj_b_jerk_v005_signal,
    f44ia_f44_institutional_accumulation_holdlog_rankj_a_jerk_v006_signal,
    f44ia_f44_institutional_accumulation_holdlog_normj_b_jerk_v007_signal,
    f44ia_f44_institutional_accumulation_holdlog_tanhj_a_jerk_v008_signal,
    f44ia_f44_institutional_accumulation_holdlog_emaj_a_jerk_v009_signal,
    f44ia_f44_institutional_accumulation_holdlog_jmix_jerk_v010_signal,
    f44ia_f44_institutional_accumulation_vallog_j_a_jerk_v011_signal,
    f44ia_f44_institutional_accumulation_vallog_j_b_jerk_v012_signal,
    f44ia_f44_institutional_accumulation_vallog_j_c_jerk_v013_signal,
    f44ia_f44_institutional_accumulation_vallog_zj_a_jerk_v014_signal,
    f44ia_f44_institutional_accumulation_vallog_zj_b_jerk_v015_signal,
    f44ia_f44_institutional_accumulation_vallog_rankj_a_jerk_v016_signal,
    f44ia_f44_institutional_accumulation_vallog_normj_b_jerk_v017_signal,
    f44ia_f44_institutional_accumulation_vallog_tanhj_a_jerk_v018_signal,
    f44ia_f44_institutional_accumulation_vallog_emaj_a_jerk_v019_signal,
    f44ia_f44_institutional_accumulation_vallog_jmix_jerk_v020_signal,
    f44ia_f44_institutional_accumulation_unitlog_j_a_jerk_v021_signal,
    f44ia_f44_institutional_accumulation_unitlog_j_b_jerk_v022_signal,
    f44ia_f44_institutional_accumulation_unitlog_j_c_jerk_v023_signal,
    f44ia_f44_institutional_accumulation_unitlog_zj_a_jerk_v024_signal,
    f44ia_f44_institutional_accumulation_unitlog_zj_b_jerk_v025_signal,
    f44ia_f44_institutional_accumulation_unitlog_rankj_a_jerk_v026_signal,
    f44ia_f44_institutional_accumulation_unitlog_normj_b_jerk_v027_signal,
    f44ia_f44_institutional_accumulation_unitlog_tanhj_a_jerk_v028_signal,
    f44ia_f44_institutional_accumulation_unitlog_emaj_a_jerk_v029_signal,
    f44ia_f44_institutional_accumulation_unitlog_jmix_jerk_v030_signal,
    f44ia_f44_institutional_accumulation_ownpct_j_a_jerk_v031_signal,
    f44ia_f44_institutional_accumulation_ownpct_j_b_jerk_v032_signal,
    f44ia_f44_institutional_accumulation_ownpct_j_c_jerk_v033_signal,
    f44ia_f44_institutional_accumulation_ownpct_zj_a_jerk_v034_signal,
    f44ia_f44_institutional_accumulation_ownpct_zj_b_jerk_v035_signal,
    f44ia_f44_institutional_accumulation_ownpct_rankj_a_jerk_v036_signal,
    f44ia_f44_institutional_accumulation_ownpct_normj_b_jerk_v037_signal,
    f44ia_f44_institutional_accumulation_ownpct_tanhj_a_jerk_v038_signal,
    f44ia_f44_institutional_accumulation_ownpct_emaj_a_jerk_v039_signal,
    f44ia_f44_institutional_accumulation_ownpct_jmix_jerk_v040_signal,
    f44ia_f44_institutional_accumulation_vphlog_j_a_jerk_v041_signal,
    f44ia_f44_institutional_accumulation_vphlog_j_b_jerk_v042_signal,
    f44ia_f44_institutional_accumulation_vphlog_j_c_jerk_v043_signal,
    f44ia_f44_institutional_accumulation_vphlog_zj_a_jerk_v044_signal,
    f44ia_f44_institutional_accumulation_vphlog_zj_b_jerk_v045_signal,
    f44ia_f44_institutional_accumulation_vphlog_rankj_a_jerk_v046_signal,
    f44ia_f44_institutional_accumulation_vphlog_normj_b_jerk_v047_signal,
    f44ia_f44_institutional_accumulation_vphlog_tanhj_a_jerk_v048_signal,
    f44ia_f44_institutional_accumulation_vphlog_emaj_a_jerk_v049_signal,
    f44ia_f44_institutional_accumulation_vphlog_jmix_jerk_v050_signal,
    f44ia_f44_institutional_accumulation_uphlog_j_a_jerk_v051_signal,
    f44ia_f44_institutional_accumulation_uphlog_j_b_jerk_v052_signal,
    f44ia_f44_institutional_accumulation_uphlog_j_c_jerk_v053_signal,
    f44ia_f44_institutional_accumulation_uphlog_zj_a_jerk_v054_signal,
    f44ia_f44_institutional_accumulation_uphlog_zj_b_jerk_v055_signal,
    f44ia_f44_institutional_accumulation_uphlog_rankj_a_jerk_v056_signal,
    f44ia_f44_institutional_accumulation_uphlog_normj_b_jerk_v057_signal,
    f44ia_f44_institutional_accumulation_uphlog_tanhj_a_jerk_v058_signal,
    f44ia_f44_institutional_accumulation_uphlog_emaj_a_jerk_v059_signal,
    f44ia_f44_institutional_accumulation_uphlog_jmix_jerk_v060_signal,
    f44ia_f44_institutional_accumulation_implpxlog_j_a_jerk_v061_signal,
    f44ia_f44_institutional_accumulation_implpxlog_j_b_jerk_v062_signal,
    f44ia_f44_institutional_accumulation_implpxlog_j_c_jerk_v063_signal,
    f44ia_f44_institutional_accumulation_implpxlog_zj_a_jerk_v064_signal,
    f44ia_f44_institutional_accumulation_implpxlog_zj_b_jerk_v065_signal,
    f44ia_f44_institutional_accumulation_implpxlog_rankj_a_jerk_v066_signal,
    f44ia_f44_institutional_accumulation_implpxlog_normj_b_jerk_v067_signal,
    f44ia_f44_institutional_accumulation_implpxlog_tanhj_a_jerk_v068_signal,
    f44ia_f44_institutional_accumulation_implpxlog_emaj_a_jerk_v069_signal,
    f44ia_f44_institutional_accumulation_implpxlog_jmix_jerk_v070_signal,
    f44ia_f44_institutional_accumulation_shrvallog_j_a_jerk_v071_signal,
    f44ia_f44_institutional_accumulation_shrvallog_j_b_jerk_v072_signal,
    f44ia_f44_institutional_accumulation_shrvallog_j_c_jerk_v073_signal,
    f44ia_f44_institutional_accumulation_shrvallog_zj_a_jerk_v074_signal,
    f44ia_f44_institutional_accumulation_shrvallog_zj_b_jerk_v075_signal,
    f44ia_f44_institutional_accumulation_shrvallog_rankj_a_jerk_v076_signal,
    f44ia_f44_institutional_accumulation_shrvallog_normj_b_jerk_v077_signal,
    f44ia_f44_institutional_accumulation_shrvallog_tanhj_a_jerk_v078_signal,
    f44ia_f44_institutional_accumulation_shrvallog_emaj_a_jerk_v079_signal,
    f44ia_f44_institutional_accumulation_shrvallog_jmix_jerk_v080_signal,
    f44ia_f44_institutional_accumulation_shrvalshare_j_a_jerk_v081_signal,
    f44ia_f44_institutional_accumulation_shrvalshare_j_b_jerk_v082_signal,
    f44ia_f44_institutional_accumulation_shrvalshare_j_c_jerk_v083_signal,
    f44ia_f44_institutional_accumulation_shrvalshare_zj_a_jerk_v084_signal,
    f44ia_f44_institutional_accumulation_shrvalshare_zj_b_jerk_v085_signal,
    f44ia_f44_institutional_accumulation_shrvalshare_rankj_a_jerk_v086_signal,
    f44ia_f44_institutional_accumulation_shrvalshare_normj_b_jerk_v087_signal,
    f44ia_f44_institutional_accumulation_shrvalshare_tanhj_a_jerk_v088_signal,
    f44ia_f44_institutional_accumulation_shrvalshare_emaj_a_jerk_v089_signal,
    f44ia_f44_institutional_accumulation_shrvalshare_jmix_jerk_v090_signal,
    f44ia_f44_institutional_accumulation_shrvalmkt_j_a_jerk_v091_signal,
    f44ia_f44_institutional_accumulation_shrvalmkt_j_b_jerk_v092_signal,
    f44ia_f44_institutional_accumulation_shrvalmkt_j_c_jerk_v093_signal,
    f44ia_f44_institutional_accumulation_shrvalmkt_zj_a_jerk_v094_signal,
    f44ia_f44_institutional_accumulation_shrvalmkt_zj_b_jerk_v095_signal,
    f44ia_f44_institutional_accumulation_shrvalmkt_rankj_a_jerk_v096_signal,
    f44ia_f44_institutional_accumulation_shrvalmkt_normj_b_jerk_v097_signal,
    f44ia_f44_institutional_accumulation_shrvalmkt_tanhj_a_jerk_v098_signal,
    f44ia_f44_institutional_accumulation_shrvalmkt_emaj_a_jerk_v099_signal,
    f44ia_f44_institutional_accumulation_shrvalmkt_jmix_jerk_v100_signal,
    f44ia_f44_institutional_accumulation_ownpctz_j_a_jerk_v101_signal,
    f44ia_f44_institutional_accumulation_ownpctz_j_b_jerk_v102_signal,
    f44ia_f44_institutional_accumulation_ownpctz_j_c_jerk_v103_signal,
    f44ia_f44_institutional_accumulation_ownpctz_zj_a_jerk_v104_signal,
    f44ia_f44_institutional_accumulation_ownpctz_zj_b_jerk_v105_signal,
    f44ia_f44_institutional_accumulation_ownpctz_rankj_a_jerk_v106_signal,
    f44ia_f44_institutional_accumulation_ownpctz_normj_b_jerk_v107_signal,
    f44ia_f44_institutional_accumulation_ownpctz_tanhj_a_jerk_v108_signal,
    f44ia_f44_institutional_accumulation_ownpctz_emaj_a_jerk_v109_signal,
    f44ia_f44_institutional_accumulation_ownpctz_jmix_jerk_v110_signal,
    f44ia_f44_institutional_accumulation_valrngpos_j_a_jerk_v111_signal,
    f44ia_f44_institutional_accumulation_valrngpos_j_b_jerk_v112_signal,
    f44ia_f44_institutional_accumulation_valrngpos_j_c_jerk_v113_signal,
    f44ia_f44_institutional_accumulation_valrngpos_zj_a_jerk_v114_signal,
    f44ia_f44_institutional_accumulation_valrngpos_zj_b_jerk_v115_signal,
    f44ia_f44_institutional_accumulation_valrngpos_rankj_a_jerk_v116_signal,
    f44ia_f44_institutional_accumulation_valrngpos_normj_b_jerk_v117_signal,
    f44ia_f44_institutional_accumulation_valrngpos_tanhj_a_jerk_v118_signal,
    f44ia_f44_institutional_accumulation_valrngpos_emaj_a_jerk_v119_signal,
    f44ia_f44_institutional_accumulation_valrngpos_jmix_jerk_v120_signal,
    f44ia_f44_institutional_accumulation_holdrngpos_j_a_jerk_v121_signal,
    f44ia_f44_institutional_accumulation_holdrngpos_j_b_jerk_v122_signal,
    f44ia_f44_institutional_accumulation_holdrngpos_j_c_jerk_v123_signal,
    f44ia_f44_institutional_accumulation_holdrngpos_zj_a_jerk_v124_signal,
    f44ia_f44_institutional_accumulation_holdrngpos_zj_b_jerk_v125_signal,
    f44ia_f44_institutional_accumulation_holdrngpos_rankj_a_jerk_v126_signal,
    f44ia_f44_institutional_accumulation_holdrngpos_normj_b_jerk_v127_signal,
    f44ia_f44_institutional_accumulation_holdrngpos_tanhj_a_jerk_v128_signal,
    f44ia_f44_institutional_accumulation_holdrngpos_emaj_a_jerk_v129_signal,
    f44ia_f44_institutional_accumulation_holdrngpos_jmix_jerk_v130_signal,
    f44ia_f44_institutional_accumulation_unitrngpos_j_a_jerk_v131_signal,
    f44ia_f44_institutional_accumulation_unitrngpos_j_b_jerk_v132_signal,
    f44ia_f44_institutional_accumulation_unitrngpos_j_c_jerk_v133_signal,
    f44ia_f44_institutional_accumulation_unitrngpos_zj_a_jerk_v134_signal,
    f44ia_f44_institutional_accumulation_unitrngpos_zj_b_jerk_v135_signal,
    f44ia_f44_institutional_accumulation_unitrngpos_rankj_a_jerk_v136_signal,
    f44ia_f44_institutional_accumulation_unitrngpos_normj_b_jerk_v137_signal,
    f44ia_f44_institutional_accumulation_unitrngpos_tanhj_a_jerk_v138_signal,
    f44ia_f44_institutional_accumulation_unitrngpos_emaj_a_jerk_v139_signal,
    f44ia_f44_institutional_accumulation_unitrngpos_jmix_jerk_v140_signal,
    f44ia_f44_institutional_accumulation_ownpctrank_j_a_jerk_v141_signal,
    f44ia_f44_institutional_accumulation_ownpctrank_j_b_jerk_v142_signal,
    f44ia_f44_institutional_accumulation_ownpctrank_j_c_jerk_v143_signal,
    f44ia_f44_institutional_accumulation_ownpctrank_zj_a_jerk_v144_signal,
    f44ia_f44_institutional_accumulation_ownpctrank_zj_b_jerk_v145_signal,
    f44ia_f44_institutional_accumulation_ownpctrank_rankj_a_jerk_v146_signal,
    f44ia_f44_institutional_accumulation_ownpctrank_normj_b_jerk_v147_signal,
    f44ia_f44_institutional_accumulation_ownpctrank_tanhj_a_jerk_v148_signal,
    f44ia_f44_institutional_accumulation_ownpctrank_emaj_a_jerk_v149_signal,
    f44ia_f44_institutional_accumulation_ownpctrank_jmix_jerk_v150_signal
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F44_INSTITUTIONAL_ACCUMULATION_REGISTRY_DERIV = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.0, vol=0.08, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.5
        return pd.Series(s, name=None)

    shrholders = _fund(301, base=120.0, drift=0.03, vol=0.06).rename("shrholders")
    shrunits = _fund(302, base=5.0e6, drift=0.04, vol=0.09).rename("shrunits")
    totalvalue = _fund(303, base=8.0e7, drift=0.05, vol=0.10).rename("totalvalue")
    shrvalue = _fund(304, base=9.0e6, drift=0.04, vol=0.11).rename("shrvalue")
    marketcap = _fund(305, base=3.0e8, drift=0.02, vol=0.08).rename("marketcap")

    cols = {
        "shrholders": shrholders,
        "shrunits": shrunits,
        "totalvalue": totalvalue,
        "shrvalue": shrvalue,
        "marketcap": marketcap,
    }

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

    print("OK f44_institutional_accumulation_3rd_derivatives_001_150_claude: %d features pass" % n_features)
