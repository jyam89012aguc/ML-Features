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
def _f002_max_age(close, w):
    ath = close.rolling(w, min_periods=max(1, w // 2)).max()
    at_peak = (close >= ath).astype(float)
    grp = at_peak.cumsum()
    age = (~at_peak.astype(bool)).astype(float).groupby(grp).cumsum()
    return age


def _f002_time_since_ath(close, w):
    ath = close.rolling(w, min_periods=max(1, w // 2)).max()
    at_peak = (close >= ath).astype(float)
    grp = at_peak.cumsum()
    tsa = (~at_peak.astype(bool)).astype(float).groupby(grp).cumsum()
    return tsa / float(w)


def _f002_base_age_score(close, w):
    ath = close.rolling(w, min_periods=max(1, w // 2)).max()
    at_peak = (close >= ath).astype(float)
    grp = at_peak.cumsum()
    age = (~at_peak.astype(bool)).astype(float).groupby(grp).cumsum()
    dd = (close - ath) / ath.replace(0, np.nan).abs()
    return age * (1.0 + dd.abs())


def f002tsa_f002_time_since_ath_mage_5d_base_v076_signal(closeadj):
    base = _f002_max_age(closeadj, 5)
    result = ((base) * (base) * (base)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_10d_base_v077_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 10)
    result = ((base) * (base) * (base)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_21d_base_v078_signal(closeadj):
    base = _f002_base_age_score(closeadj, 21)
    result = ((base) * (base) * (base)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_42d_base_v079_signal(closeadj):
    base = _f002_max_age(closeadj, 42)
    result = ((base) * (base) * (base)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_63d_base_v080_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 63)
    result = ((base) * (base) * (base)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_126d_base_v081_signal(closeadj):
    base = _f002_base_age_score(closeadj, 126)
    result = (_mean(base, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_189d_base_v082_signal(closeadj):
    base = _f002_max_age(closeadj, 189)
    result = (_mean(base, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_252d_base_v083_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 252)
    result = (_mean(base, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_378d_base_v084_signal(closeadj):
    base = _f002_base_age_score(closeadj, 378)
    result = (_mean(base, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_504d_base_v085_signal(closeadj):
    base = _f002_max_age(closeadj, 504)
    result = (_mean(base, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_5d_base_v086_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 5)
    result = (_std(base, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_10d_base_v087_signal(closeadj):
    base = _f002_base_age_score(closeadj, 10)
    result = (_std(base, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_21d_base_v088_signal(closeadj):
    base = _f002_max_age(closeadj, 21)
    result = (_std(base, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_42d_base_v089_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 42)
    result = (_std(base, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_63d_base_v090_signal(closeadj):
    base = _f002_base_age_score(closeadj, 63)
    result = (_std(base, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_126d_base_v091_signal(closeadj):
    base = _f002_max_age(closeadj, 126)
    result = (_z(base, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_189d_base_v092_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 189)
    result = (_z(base, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_252d_base_v093_signal(closeadj):
    base = _f002_base_age_score(closeadj, 252)
    result = (_z(base, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_378d_base_v094_signal(closeadj):
    base = _f002_max_age(closeadj, 378)
    result = (_z(base, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_504d_base_v095_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 504)
    result = (_z(base, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_5d_base_v096_signal(closeadj):
    base = _f002_base_age_score(closeadj, 5)
    result = (np.tanh(_z(base, 126))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_10d_base_v097_signal(closeadj):
    base = _f002_max_age(closeadj, 10)
    result = (np.tanh(_z(base, 126))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_21d_base_v098_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 21)
    result = (np.tanh(_z(base, 126))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_42d_base_v099_signal(closeadj):
    base = _f002_base_age_score(closeadj, 42)
    result = (np.tanh(_z(base, 126))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_63d_base_v100_signal(closeadj):
    base = _f002_max_age(closeadj, 63)
    result = (np.tanh(_z(base, 126))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_126d_base_v101_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 126)
    result = ((base).ewm(span=63, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_189d_base_v102_signal(closeadj):
    base = _f002_base_age_score(closeadj, 189)
    result = ((base).ewm(span=63, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_252d_base_v103_signal(closeadj):
    base = _f002_max_age(closeadj, 252)
    result = ((base).ewm(span=63, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_378d_base_v104_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 378)
    result = ((base).ewm(span=63, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_504d_base_v105_signal(closeadj):
    base = _f002_base_age_score(closeadj, 504)
    result = ((base).ewm(span=63, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_5d_base_v106_signal(closeadj):
    base = _f002_max_age(closeadj, 5)
    result = ((base).ewm(span=63, adjust=False).std()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_10d_base_v107_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 10)
    result = ((base).ewm(span=63, adjust=False).std()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_21d_base_v108_signal(closeadj):
    base = _f002_base_age_score(closeadj, 21)
    result = ((base).ewm(span=63, adjust=False).std()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_42d_base_v109_signal(closeadj):
    base = _f002_max_age(closeadj, 42)
    result = ((base).ewm(span=63, adjust=False).std()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_63d_base_v110_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 63)
    result = ((base).ewm(span=63, adjust=False).std()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_126d_base_v111_signal(closeadj):
    base = _f002_base_age_score(closeadj, 126)
    result = ((base).diff(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_189d_base_v112_signal(closeadj):
    base = _f002_max_age(closeadj, 189)
    result = ((base).diff(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_252d_base_v113_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 252)
    result = ((base).diff(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_378d_base_v114_signal(closeadj):
    base = _f002_base_age_score(closeadj, 378)
    result = ((base).diff(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_504d_base_v115_signal(closeadj):
    base = _f002_max_age(closeadj, 504)
    result = ((base).diff(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_5d_base_v116_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 5)
    result = ((base).rolling(126, min_periods=max(1, 126 // 2)).sum()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_10d_base_v117_signal(closeadj):
    base = _f002_base_age_score(closeadj, 10)
    result = ((base).rolling(126, min_periods=max(1, 126 // 2)).sum()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_21d_base_v118_signal(closeadj):
    base = _f002_max_age(closeadj, 21)
    result = ((base).rolling(126, min_periods=max(1, 126 // 2)).sum()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_42d_base_v119_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 42)
    result = ((base).rolling(126, min_periods=max(1, 126 // 2)).sum()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_63d_base_v120_signal(closeadj):
    base = _f002_base_age_score(closeadj, 63)
    result = ((base).rolling(126, min_periods=max(1, 126 // 2)).sum()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_126d_base_v121_signal(closeadj):
    base = _f002_max_age(closeadj, 126)
    result = ((base).rolling(126, min_periods=max(1, 126 // 2)).median()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_189d_base_v122_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 189)
    result = ((base).rolling(126, min_periods=max(1, 126 // 2)).median()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_252d_base_v123_signal(closeadj):
    base = _f002_base_age_score(closeadj, 252)
    result = ((base).rolling(126, min_periods=max(1, 126 // 2)).median()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_378d_base_v124_signal(closeadj):
    base = _f002_max_age(closeadj, 378)
    result = ((base).rolling(126, min_periods=max(1, 126 // 2)).median()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_504d_base_v125_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 504)
    result = ((base).rolling(126, min_periods=max(1, 126 // 2)).median()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_5d_base_v126_signal(closeadj):
    base = _f002_base_age_score(closeadj, 5)
    result = ((base).rolling(126, min_periods=max(2, 126 // 2)).skew()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_10d_base_v127_signal(closeadj):
    base = _f002_max_age(closeadj, 10)
    result = ((base).rolling(126, min_periods=max(2, 126 // 2)).skew()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_21d_base_v128_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 21)
    result = ((base).rolling(126, min_periods=max(2, 126 // 2)).skew()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_42d_base_v129_signal(closeadj):
    base = _f002_base_age_score(closeadj, 42)
    result = ((base).rolling(126, min_periods=max(2, 126 // 2)).skew()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_63d_base_v130_signal(closeadj):
    base = _f002_max_age(closeadj, 63)
    result = ((base).rolling(126, min_periods=max(2, 126 // 2)).skew()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_126d_base_v131_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 126)
    result = ((base).rolling(252, min_periods=max(4, 252 // 2)).kurt()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_189d_base_v132_signal(closeadj):
    base = _f002_base_age_score(closeadj, 189)
    result = ((base).rolling(252, min_periods=max(4, 252 // 2)).kurt()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_252d_base_v133_signal(closeadj):
    base = _f002_max_age(closeadj, 252)
    result = ((base).rolling(252, min_periods=max(4, 252 // 2)).kurt()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_378d_base_v134_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 378)
    result = ((base).rolling(252, min_periods=max(4, 252 // 2)).kurt()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_504d_base_v135_signal(closeadj):
    base = _f002_base_age_score(closeadj, 504)
    result = ((base).rolling(252, min_periods=max(4, 252 // 2)).kurt()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_5d_base_v136_signal(closeadj):
    base = _f002_max_age(closeadj, 5)
    result = (_mean(base, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_10d_base_v137_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 10)
    result = (_mean(base, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_21d_base_v138_signal(closeadj):
    base = _f002_base_age_score(closeadj, 21)
    result = (_mean(base, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_42d_base_v139_signal(closeadj):
    base = _f002_max_age(closeadj, 42)
    result = (_mean(base, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_63d_base_v140_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 63)
    result = (_mean(base, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_126d_base_v141_signal(closeadj):
    base = _f002_base_age_score(closeadj, 126)
    result = (_std(base, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_189d_base_v142_signal(closeadj):
    base = _f002_max_age(closeadj, 189)
    result = (_std(base, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_252d_base_v143_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 252)
    result = (_std(base, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_378d_base_v144_signal(closeadj):
    base = _f002_base_age_score(closeadj, 378)
    result = (_std(base, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_504d_base_v145_signal(closeadj):
    base = _f002_max_age(closeadj, 504)
    result = (_std(base, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_5d_base_v146_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 5)
    result = ((base).ewm(span=126, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_10d_base_v147_signal(closeadj):
    base = _f002_base_age_score(closeadj, 10)
    result = ((base).ewm(span=126, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_mage_21d_base_v148_signal(closeadj):
    base = _f002_max_age(closeadj, 21)
    result = ((base).ewm(span=126, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_tsa_42d_base_v149_signal(closeadj):
    base = _f002_time_since_ath(closeadj, 42)
    result = ((base).ewm(span=126, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f002tsa_f002_time_since_ath_bas_63d_base_v150_signal(closeadj):
    base = _f002_base_age_score(closeadj, 63)
    result = ((base).ewm(span=126, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f002tsa_f002_time_since_ath_mage_5d_base_v076_signal,
    f002tsa_f002_time_since_ath_tsa_10d_base_v077_signal,
    f002tsa_f002_time_since_ath_bas_21d_base_v078_signal,
    f002tsa_f002_time_since_ath_mage_42d_base_v079_signal,
    f002tsa_f002_time_since_ath_tsa_63d_base_v080_signal,
    f002tsa_f002_time_since_ath_bas_126d_base_v081_signal,
    f002tsa_f002_time_since_ath_mage_189d_base_v082_signal,
    f002tsa_f002_time_since_ath_tsa_252d_base_v083_signal,
    f002tsa_f002_time_since_ath_bas_378d_base_v084_signal,
    f002tsa_f002_time_since_ath_mage_504d_base_v085_signal,
    f002tsa_f002_time_since_ath_tsa_5d_base_v086_signal,
    f002tsa_f002_time_since_ath_bas_10d_base_v087_signal,
    f002tsa_f002_time_since_ath_mage_21d_base_v088_signal,
    f002tsa_f002_time_since_ath_tsa_42d_base_v089_signal,
    f002tsa_f002_time_since_ath_bas_63d_base_v090_signal,
    f002tsa_f002_time_since_ath_mage_126d_base_v091_signal,
    f002tsa_f002_time_since_ath_tsa_189d_base_v092_signal,
    f002tsa_f002_time_since_ath_bas_252d_base_v093_signal,
    f002tsa_f002_time_since_ath_mage_378d_base_v094_signal,
    f002tsa_f002_time_since_ath_tsa_504d_base_v095_signal,
    f002tsa_f002_time_since_ath_bas_5d_base_v096_signal,
    f002tsa_f002_time_since_ath_mage_10d_base_v097_signal,
    f002tsa_f002_time_since_ath_tsa_21d_base_v098_signal,
    f002tsa_f002_time_since_ath_bas_42d_base_v099_signal,
    f002tsa_f002_time_since_ath_mage_63d_base_v100_signal,
    f002tsa_f002_time_since_ath_tsa_126d_base_v101_signal,
    f002tsa_f002_time_since_ath_bas_189d_base_v102_signal,
    f002tsa_f002_time_since_ath_mage_252d_base_v103_signal,
    f002tsa_f002_time_since_ath_tsa_378d_base_v104_signal,
    f002tsa_f002_time_since_ath_bas_504d_base_v105_signal,
    f002tsa_f002_time_since_ath_mage_5d_base_v106_signal,
    f002tsa_f002_time_since_ath_tsa_10d_base_v107_signal,
    f002tsa_f002_time_since_ath_bas_21d_base_v108_signal,
    f002tsa_f002_time_since_ath_mage_42d_base_v109_signal,
    f002tsa_f002_time_since_ath_tsa_63d_base_v110_signal,
    f002tsa_f002_time_since_ath_bas_126d_base_v111_signal,
    f002tsa_f002_time_since_ath_mage_189d_base_v112_signal,
    f002tsa_f002_time_since_ath_tsa_252d_base_v113_signal,
    f002tsa_f002_time_since_ath_bas_378d_base_v114_signal,
    f002tsa_f002_time_since_ath_mage_504d_base_v115_signal,
    f002tsa_f002_time_since_ath_tsa_5d_base_v116_signal,
    f002tsa_f002_time_since_ath_bas_10d_base_v117_signal,
    f002tsa_f002_time_since_ath_mage_21d_base_v118_signal,
    f002tsa_f002_time_since_ath_tsa_42d_base_v119_signal,
    f002tsa_f002_time_since_ath_bas_63d_base_v120_signal,
    f002tsa_f002_time_since_ath_mage_126d_base_v121_signal,
    f002tsa_f002_time_since_ath_tsa_189d_base_v122_signal,
    f002tsa_f002_time_since_ath_bas_252d_base_v123_signal,
    f002tsa_f002_time_since_ath_mage_378d_base_v124_signal,
    f002tsa_f002_time_since_ath_tsa_504d_base_v125_signal,
    f002tsa_f002_time_since_ath_bas_5d_base_v126_signal,
    f002tsa_f002_time_since_ath_mage_10d_base_v127_signal,
    f002tsa_f002_time_since_ath_tsa_21d_base_v128_signal,
    f002tsa_f002_time_since_ath_bas_42d_base_v129_signal,
    f002tsa_f002_time_since_ath_mage_63d_base_v130_signal,
    f002tsa_f002_time_since_ath_tsa_126d_base_v131_signal,
    f002tsa_f002_time_since_ath_bas_189d_base_v132_signal,
    f002tsa_f002_time_since_ath_mage_252d_base_v133_signal,
    f002tsa_f002_time_since_ath_tsa_378d_base_v134_signal,
    f002tsa_f002_time_since_ath_bas_504d_base_v135_signal,
    f002tsa_f002_time_since_ath_mage_5d_base_v136_signal,
    f002tsa_f002_time_since_ath_tsa_10d_base_v137_signal,
    f002tsa_f002_time_since_ath_bas_21d_base_v138_signal,
    f002tsa_f002_time_since_ath_mage_42d_base_v139_signal,
    f002tsa_f002_time_since_ath_tsa_63d_base_v140_signal,
    f002tsa_f002_time_since_ath_bas_126d_base_v141_signal,
    f002tsa_f002_time_since_ath_mage_189d_base_v142_signal,
    f002tsa_f002_time_since_ath_tsa_252d_base_v143_signal,
    f002tsa_f002_time_since_ath_bas_378d_base_v144_signal,
    f002tsa_f002_time_since_ath_mage_504d_base_v145_signal,
    f002tsa_f002_time_since_ath_tsa_5d_base_v146_signal,
    f002tsa_f002_time_since_ath_bas_10d_base_v147_signal,
    f002tsa_f002_time_since_ath_mage_21d_base_v148_signal,
    f002tsa_f002_time_since_ath_tsa_42d_base_v149_signal,
    f002tsa_f002_time_since_ath_bas_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F002_TIME_SINCE_ATH_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    cols = {"closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f002_max_age", "_f002_time_since_ath", "_f002_base_age_score")
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
    print(f"OK f002_time_since_ath_base_076_150_claude: {n_features} features pass")
