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
def _f057_trend_fit(close, w):
    lp = np.log(close.replace(0, np.nan).abs())
    m = lp.rolling(w, min_periods=max(1, w // 2)).mean()
    slope = (lp - lp.shift(w)) / float(w)
    return m + slope * (w / 2.0)


def _f057_trend_r2(close, w):
    lp = np.log(close.replace(0, np.nan).abs())
    var_total = lp.rolling(w, min_periods=max(1, w // 2)).var()
    slope = (lp - lp.shift(w)) / float(w)
    explained = (slope * slope) * (w * w - 1) / 12.0
    return 1.0 - (var_total - explained) / var_total.replace(0, np.nan)


def _f057_smoothness_score(close, w):
    ret = close.pct_change()
    sd = ret.rolling(w, min_periods=max(1, w // 2)).std()
    m_abs = ret.abs().rolling(w, min_periods=max(1, w // 2)).mean()
    return m_abs / sd.replace(0, np.nan)


def f057trq_f057_trend_r2_tfitxclose_5d_base_v001_signal(closeadj):
    result = _safe_div(_f057_trend_fit(closeadj, 5), _mean(_f057_trend_fit(closeadj, 5), 252).abs()) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitxclose_10d_base_v002_signal(closeadj):
    result = _safe_div(_f057_trend_fit(closeadj, 10), _mean(_f057_trend_fit(closeadj, 10), 252).abs()) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitxclose_21d_base_v003_signal(closeadj):
    result = _safe_div(_f057_trend_fit(closeadj, 21), _mean(_f057_trend_fit(closeadj, 21), 252).abs()) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitxclose_42d_base_v004_signal(closeadj):
    result = _safe_div(_f057_trend_fit(closeadj, 42), _mean(_f057_trend_fit(closeadj, 42), 252).abs()) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitxclose_63d_base_v005_signal(closeadj):
    result = _safe_div(_f057_trend_fit(closeadj, 63), _mean(_f057_trend_fit(closeadj, 63), 252).abs()) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitxclose_126d_base_v006_signal(closeadj):
    result = _safe_div(_f057_trend_fit(closeadj, 126), _mean(_f057_trend_fit(closeadj, 126), 252).abs()) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitxclose_189d_base_v007_signal(closeadj):
    result = _safe_div(_f057_trend_fit(closeadj, 189), _mean(_f057_trend_fit(closeadj, 189), 252).abs()) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitxclose_252d_base_v008_signal(closeadj):
    result = _safe_div(_f057_trend_fit(closeadj, 252), _mean(_f057_trend_fit(closeadj, 252), 252).abs()) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitxclose_378d_base_v009_signal(closeadj):
    result = _safe_div(_f057_trend_fit(closeadj, 378), _mean(_f057_trend_fit(closeadj, 378), 252).abs()) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitxclose_504d_base_v010_signal(closeadj):
    result = _safe_div(_f057_trend_fit(closeadj, 504), _mean(_f057_trend_fit(closeadj, 504), 252).abs()) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndxclose_5d_base_v011_signal(closeadj):
    result = _f057_trend_r2(closeadj, 5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndxclose_10d_base_v012_signal(closeadj):
    result = _f057_trend_r2(closeadj, 10) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndxclose_21d_base_v013_signal(closeadj):
    result = _f057_trend_r2(closeadj, 21) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndxclose_42d_base_v014_signal(closeadj):
    result = _f057_trend_r2(closeadj, 42) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndxclose_63d_base_v015_signal(closeadj):
    result = _f057_trend_r2(closeadj, 63) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndxclose_126d_base_v016_signal(closeadj):
    result = _f057_trend_r2(closeadj, 126) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndxclose_189d_base_v017_signal(closeadj):
    result = _f057_trend_r2(closeadj, 189) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndxclose_252d_base_v018_signal(closeadj):
    result = _f057_trend_r2(closeadj, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndxclose_378d_base_v019_signal(closeadj):
    result = _f057_trend_r2(closeadj, 378) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndxclose_504d_base_v020_signal(closeadj):
    result = _f057_trend_r2(closeadj, 504) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_smthxclose_5d_base_v021_signal(closeadj):
    result = _f057_smoothness_score(closeadj, 5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_smthxclose_10d_base_v022_signal(closeadj):
    result = _f057_smoothness_score(closeadj, 10) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_smthxclose_21d_base_v023_signal(closeadj):
    result = _f057_smoothness_score(closeadj, 21) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_smthxclose_42d_base_v024_signal(closeadj):
    result = _f057_smoothness_score(closeadj, 42) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_smthxclose_63d_base_v025_signal(closeadj):
    result = _f057_smoothness_score(closeadj, 63) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_smthxclose_126d_base_v026_signal(closeadj):
    result = _f057_smoothness_score(closeadj, 126) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_smthxclose_189d_base_v027_signal(closeadj):
    result = _f057_smoothness_score(closeadj, 189) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_smthxclose_252d_base_v028_signal(closeadj):
    result = _f057_smoothness_score(closeadj, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_smthxclose_378d_base_v029_signal(closeadj):
    result = _f057_smoothness_score(closeadj, 378) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_smthxclose_504d_base_v030_signal(closeadj):
    result = _f057_smoothness_score(closeadj, 504) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitzc252_5d_base_v031_signal(closeadj):
    result = _z(_f057_trend_fit(closeadj, 5), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitzc252_10d_base_v032_signal(closeadj):
    result = _z(_f057_trend_fit(closeadj, 10), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitzc252_21d_base_v033_signal(closeadj):
    result = _z(_f057_trend_fit(closeadj, 21), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitzc252_42d_base_v034_signal(closeadj):
    result = _z(_f057_trend_fit(closeadj, 42), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitzc252_63d_base_v035_signal(closeadj):
    result = _z(_f057_trend_fit(closeadj, 63), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitzc252_126d_base_v036_signal(closeadj):
    result = _z(_f057_trend_fit(closeadj, 126), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitzc252_189d_base_v037_signal(closeadj):
    result = _z(_f057_trend_fit(closeadj, 189), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitzc252_252d_base_v038_signal(closeadj):
    result = _z(_f057_trend_fit(closeadj, 252), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitzc252_378d_base_v039_signal(closeadj):
    result = _z(_f057_trend_fit(closeadj, 378), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitzc252_504d_base_v040_signal(closeadj):
    result = _z(_f057_trend_fit(closeadj, 504), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndzc252_5d_base_v041_signal(closeadj):
    result = _z(_f057_trend_r2(closeadj, 5), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndzc252_10d_base_v042_signal(closeadj):
    result = _z(_f057_trend_r2(closeadj, 10), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndzc252_21d_base_v043_signal(closeadj):
    result = _z(_f057_trend_r2(closeadj, 21), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndzc252_42d_base_v044_signal(closeadj):
    result = _z(_f057_trend_r2(closeadj, 42), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndzc252_63d_base_v045_signal(closeadj):
    result = _z(_f057_trend_r2(closeadj, 63), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndzc252_126d_base_v046_signal(closeadj):
    result = _z(_f057_trend_r2(closeadj, 126), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndzc252_189d_base_v047_signal(closeadj):
    result = _z(_f057_trend_r2(closeadj, 189), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndzc252_252d_base_v048_signal(closeadj):
    result = _z(_f057_trend_r2(closeadj, 252), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndzc252_378d_base_v049_signal(closeadj):
    result = _z(_f057_trend_r2(closeadj, 378), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndzc252_504d_base_v050_signal(closeadj):
    result = _z(_f057_trend_r2(closeadj, 504), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_smthzc252_5d_base_v051_signal(closeadj):
    result = _z(_f057_smoothness_score(closeadj, 5), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_smthzc252_10d_base_v052_signal(closeadj):
    result = _z(_f057_smoothness_score(closeadj, 10), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_smthzc252_21d_base_v053_signal(closeadj):
    result = _z(_f057_smoothness_score(closeadj, 21), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_smthzc252_42d_base_v054_signal(closeadj):
    result = _z(_f057_smoothness_score(closeadj, 42), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_smthzc252_63d_base_v055_signal(closeadj):
    result = _z(_f057_smoothness_score(closeadj, 63), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_smthzc252_126d_base_v056_signal(closeadj):
    result = _z(_f057_smoothness_score(closeadj, 126), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_smthzc252_189d_base_v057_signal(closeadj):
    result = _z(_f057_smoothness_score(closeadj, 189), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_smthzc252_252d_base_v058_signal(closeadj):
    result = _z(_f057_smoothness_score(closeadj, 252), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_smthzc252_378d_base_v059_signal(closeadj):
    result = _z(_f057_smoothness_score(closeadj, 378), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_smthzc252_504d_base_v060_signal(closeadj):
    result = _z(_f057_smoothness_score(closeadj, 504), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfittanh_5d_base_v061_signal(closeadj):
    result = np.tanh(_z(_f057_trend_fit(closeadj, 5), 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfittanh_10d_base_v062_signal(closeadj):
    result = np.tanh(_z(_f057_trend_fit(closeadj, 10), 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfittanh_21d_base_v063_signal(closeadj):
    result = np.tanh(_z(_f057_trend_fit(closeadj, 21), 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfittanh_42d_base_v064_signal(closeadj):
    result = np.tanh(_z(_f057_trend_fit(closeadj, 42), 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfittanh_63d_base_v065_signal(closeadj):
    result = np.tanh(_z(_f057_trend_fit(closeadj, 63), 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfittanh_126d_base_v066_signal(closeadj):
    result = np.tanh(_z(_f057_trend_fit(closeadj, 126), 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfittanh_189d_base_v067_signal(closeadj):
    result = np.tanh(_z(_f057_trend_fit(closeadj, 189), 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfittanh_252d_base_v068_signal(closeadj):
    result = np.tanh(_z(_f057_trend_fit(closeadj, 252), 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfittanh_378d_base_v069_signal(closeadj):
    result = np.tanh(_z(_f057_trend_fit(closeadj, 378), 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfittanh_504d_base_v070_signal(closeadj):
    result = np.tanh(_z(_f057_trend_fit(closeadj, 504), 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndtanh_5d_base_v071_signal(closeadj):
    result = np.tanh(_z(_f057_trend_r2(closeadj, 5), 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndtanh_10d_base_v072_signal(closeadj):
    result = np.tanh(_z(_f057_trend_r2(closeadj, 10), 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndtanh_21d_base_v073_signal(closeadj):
    result = np.tanh(_z(_f057_trend_r2(closeadj, 21), 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndtanh_42d_base_v074_signal(closeadj):
    result = np.tanh(_z(_f057_trend_r2(closeadj, 42), 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndtanh_63d_base_v075_signal(closeadj):
    result = np.tanh(_z(_f057_trend_r2(closeadj, 63), 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f057trq_f057_trend_r2_tfitxclose_5d_base_v001_signal,
    f057trq_f057_trend_r2_tfitxclose_10d_base_v002_signal,
    f057trq_f057_trend_r2_tfitxclose_21d_base_v003_signal,
    f057trq_f057_trend_r2_tfitxclose_42d_base_v004_signal,
    f057trq_f057_trend_r2_tfitxclose_63d_base_v005_signal,
    f057trq_f057_trend_r2_tfitxclose_126d_base_v006_signal,
    f057trq_f057_trend_r2_tfitxclose_189d_base_v007_signal,
    f057trq_f057_trend_r2_tfitxclose_252d_base_v008_signal,
    f057trq_f057_trend_r2_tfitxclose_378d_base_v009_signal,
    f057trq_f057_trend_r2_tfitxclose_504d_base_v010_signal,
    f057trq_f057_trend_r2_trndxclose_5d_base_v011_signal,
    f057trq_f057_trend_r2_trndxclose_10d_base_v012_signal,
    f057trq_f057_trend_r2_trndxclose_21d_base_v013_signal,
    f057trq_f057_trend_r2_trndxclose_42d_base_v014_signal,
    f057trq_f057_trend_r2_trndxclose_63d_base_v015_signal,
    f057trq_f057_trend_r2_trndxclose_126d_base_v016_signal,
    f057trq_f057_trend_r2_trndxclose_189d_base_v017_signal,
    f057trq_f057_trend_r2_trndxclose_252d_base_v018_signal,
    f057trq_f057_trend_r2_trndxclose_378d_base_v019_signal,
    f057trq_f057_trend_r2_trndxclose_504d_base_v020_signal,
    f057trq_f057_trend_r2_smthxclose_5d_base_v021_signal,
    f057trq_f057_trend_r2_smthxclose_10d_base_v022_signal,
    f057trq_f057_trend_r2_smthxclose_21d_base_v023_signal,
    f057trq_f057_trend_r2_smthxclose_42d_base_v024_signal,
    f057trq_f057_trend_r2_smthxclose_63d_base_v025_signal,
    f057trq_f057_trend_r2_smthxclose_126d_base_v026_signal,
    f057trq_f057_trend_r2_smthxclose_189d_base_v027_signal,
    f057trq_f057_trend_r2_smthxclose_252d_base_v028_signal,
    f057trq_f057_trend_r2_smthxclose_378d_base_v029_signal,
    f057trq_f057_trend_r2_smthxclose_504d_base_v030_signal,
    f057trq_f057_trend_r2_tfitzc252_5d_base_v031_signal,
    f057trq_f057_trend_r2_tfitzc252_10d_base_v032_signal,
    f057trq_f057_trend_r2_tfitzc252_21d_base_v033_signal,
    f057trq_f057_trend_r2_tfitzc252_42d_base_v034_signal,
    f057trq_f057_trend_r2_tfitzc252_63d_base_v035_signal,
    f057trq_f057_trend_r2_tfitzc252_126d_base_v036_signal,
    f057trq_f057_trend_r2_tfitzc252_189d_base_v037_signal,
    f057trq_f057_trend_r2_tfitzc252_252d_base_v038_signal,
    f057trq_f057_trend_r2_tfitzc252_378d_base_v039_signal,
    f057trq_f057_trend_r2_tfitzc252_504d_base_v040_signal,
    f057trq_f057_trend_r2_trndzc252_5d_base_v041_signal,
    f057trq_f057_trend_r2_trndzc252_10d_base_v042_signal,
    f057trq_f057_trend_r2_trndzc252_21d_base_v043_signal,
    f057trq_f057_trend_r2_trndzc252_42d_base_v044_signal,
    f057trq_f057_trend_r2_trndzc252_63d_base_v045_signal,
    f057trq_f057_trend_r2_trndzc252_126d_base_v046_signal,
    f057trq_f057_trend_r2_trndzc252_189d_base_v047_signal,
    f057trq_f057_trend_r2_trndzc252_252d_base_v048_signal,
    f057trq_f057_trend_r2_trndzc252_378d_base_v049_signal,
    f057trq_f057_trend_r2_trndzc252_504d_base_v050_signal,
    f057trq_f057_trend_r2_smthzc252_5d_base_v051_signal,
    f057trq_f057_trend_r2_smthzc252_10d_base_v052_signal,
    f057trq_f057_trend_r2_smthzc252_21d_base_v053_signal,
    f057trq_f057_trend_r2_smthzc252_42d_base_v054_signal,
    f057trq_f057_trend_r2_smthzc252_63d_base_v055_signal,
    f057trq_f057_trend_r2_smthzc252_126d_base_v056_signal,
    f057trq_f057_trend_r2_smthzc252_189d_base_v057_signal,
    f057trq_f057_trend_r2_smthzc252_252d_base_v058_signal,
    f057trq_f057_trend_r2_smthzc252_378d_base_v059_signal,
    f057trq_f057_trend_r2_smthzc252_504d_base_v060_signal,
    f057trq_f057_trend_r2_tfittanh_5d_base_v061_signal,
    f057trq_f057_trend_r2_tfittanh_10d_base_v062_signal,
    f057trq_f057_trend_r2_tfittanh_21d_base_v063_signal,
    f057trq_f057_trend_r2_tfittanh_42d_base_v064_signal,
    f057trq_f057_trend_r2_tfittanh_63d_base_v065_signal,
    f057trq_f057_trend_r2_tfittanh_126d_base_v066_signal,
    f057trq_f057_trend_r2_tfittanh_189d_base_v067_signal,
    f057trq_f057_trend_r2_tfittanh_252d_base_v068_signal,
    f057trq_f057_trend_r2_tfittanh_378d_base_v069_signal,
    f057trq_f057_trend_r2_tfittanh_504d_base_v070_signal,
    f057trq_f057_trend_r2_trndtanh_5d_base_v071_signal,
    f057trq_f057_trend_r2_trndtanh_10d_base_v072_signal,
    f057trq_f057_trend_r2_trndtanh_21d_base_v073_signal,
    f057trq_f057_trend_r2_trndtanh_42d_base_v074_signal,
    f057trq_f057_trend_r2_trndtanh_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F057_TREND_R2_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    cols = {"closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f057_trend_fit", "_f057_trend_r2", "_f057_smoothness_score",)
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
    print(f"OK f057_trend_r2_base_001_075_claude: {n_features} features pass")
