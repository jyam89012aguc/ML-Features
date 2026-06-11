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


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


# ===== folder domain primitives =====
def _f47_quiet_fcf_growth(fcf, w):
    m = fcf.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = fcf.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)
    return m / sd


def _f47_low_attention_growth(closeadj, volume, fcf, w):
    dv = (closeadj * volume).rolling(w, min_periods=max(1, w // 2)).mean()
    g = fcf.rolling(w, min_periods=max(1, w // 2)).mean()
    return g * closeadj / dv.replace(0, np.nan)


def _f47_hidden_quality_score(fcf, roic, w):
    fg = fcf.rolling(w, min_periods=max(1, w // 2)).mean()
    rq = roic.rolling(w, min_periods=max(1, w // 2)).mean()
    return fg * rq


# ===== features =====
def f47hrc_f47_hidden_renewable_compounder_qf_fcf_5d_s00_base_v001_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_5d_s00_base_v002_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_5d_s00_base_v003_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_10d_s00_base_v004_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_10d_s00_base_v005_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_10d_s00_base_v006_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_21d_s00_base_v007_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_21d_s00_base_v008_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_21d_s00_base_v009_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_42d_s00_base_v010_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_42d_s00_base_v011_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_42d_s00_base_v012_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_63d_s00_base_v013_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_63d_s00_base_v014_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_63d_s00_base_v015_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_84d_s00_base_v016_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 84)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_84d_s00_base_v017_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 84)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_84d_s00_base_v018_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 84)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_105d_s00_base_v019_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 105)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_105d_s00_base_v020_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 105)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_105d_s00_base_v021_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 105)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_126d_s00_base_v022_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_126d_s00_base_v023_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_126d_s00_base_v024_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_147d_s00_base_v025_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 147)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_147d_s00_base_v026_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 147)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_147d_s00_base_v027_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 147)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_168d_s00_base_v028_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 168)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_168d_s00_base_v029_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 168)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_168d_s00_base_v030_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 168)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_189d_s00_base_v031_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_189d_s00_base_v032_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_189d_s00_base_v033_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_210d_s00_base_v034_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 210)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_210d_s00_base_v035_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 210)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_210d_s00_base_v036_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 210)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_231d_s00_base_v037_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 231)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_231d_s00_base_v038_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 231)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_231d_s00_base_v039_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 231)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_252d_s00_base_v040_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_252d_s00_base_v041_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_252d_s00_base_v042_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_294d_s00_base_v043_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 294)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_294d_s00_base_v044_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 294)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_294d_s00_base_v045_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 294)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_336d_s00_base_v046_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 336)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_336d_s00_base_v047_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 336)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_336d_s00_base_v048_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 336)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_378d_s00_base_v049_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_378d_s00_base_v050_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_378d_s00_base_v051_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_420d_s00_base_v052_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 420)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_420d_s00_base_v053_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 420)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_420d_s00_base_v054_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 420)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_462d_s00_base_v055_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 462)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_462d_s00_base_v056_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 462)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_462d_s00_base_v057_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 462)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_504d_s00_base_v058_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_504d_s00_base_v059_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_504d_s00_base_v060_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_5d_s01_base_v061_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 5)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_5d_s01_base_v062_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 5)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_5d_s01_base_v063_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 5)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_5d_s01_base_v064_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 5)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_5d_s01_base_v065_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 5)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_5d_s01_base_v066_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 5)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_5d_s01_base_v067_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 5)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_5d_s01_base_v068_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 5)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_5d_s01_base_v069_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 5)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_5d_s01_base_v070_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 5)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_5d_s01_base_v071_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 5)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_5d_s01_base_v072_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 5)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_5d_s01_base_v073_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 5)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_5d_s01_base_v074_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 5)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_5d_s01_base_v075_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 5)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_5d_s00_base_v001_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_5d_s00_base_v002_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_5d_s00_base_v003_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_10d_s00_base_v004_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_10d_s00_base_v005_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_10d_s00_base_v006_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_21d_s00_base_v007_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_21d_s00_base_v008_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_21d_s00_base_v009_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_42d_s00_base_v010_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_42d_s00_base_v011_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_42d_s00_base_v012_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_63d_s00_base_v013_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_63d_s00_base_v014_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_63d_s00_base_v015_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_84d_s00_base_v016_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_84d_s00_base_v017_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_84d_s00_base_v018_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_105d_s00_base_v019_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_105d_s00_base_v020_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_105d_s00_base_v021_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_126d_s00_base_v022_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_126d_s00_base_v023_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_126d_s00_base_v024_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_147d_s00_base_v025_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_147d_s00_base_v026_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_147d_s00_base_v027_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_168d_s00_base_v028_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_168d_s00_base_v029_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_168d_s00_base_v030_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_189d_s00_base_v031_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_189d_s00_base_v032_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_189d_s00_base_v033_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_210d_s00_base_v034_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_210d_s00_base_v035_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_210d_s00_base_v036_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_231d_s00_base_v037_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_231d_s00_base_v038_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_231d_s00_base_v039_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_252d_s00_base_v040_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_252d_s00_base_v041_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_252d_s00_base_v042_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_294d_s00_base_v043_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_294d_s00_base_v044_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_294d_s00_base_v045_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_336d_s00_base_v046_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_336d_s00_base_v047_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_336d_s00_base_v048_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_378d_s00_base_v049_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_378d_s00_base_v050_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_378d_s00_base_v051_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_420d_s00_base_v052_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_420d_s00_base_v053_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_420d_s00_base_v054_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_462d_s00_base_v055_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_462d_s00_base_v056_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_462d_s00_base_v057_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_504d_s00_base_v058_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_504d_s00_base_v059_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_504d_s00_base_v060_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_5d_s01_base_v061_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_5d_s01_base_v062_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_5d_s01_base_v063_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_5d_s01_base_v064_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_5d_s01_base_v065_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_5d_s01_base_v066_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_5d_s01_base_v067_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_5d_s01_base_v068_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_5d_s01_base_v069_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_5d_s01_base_v070_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_5d_s01_base_v071_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_5d_s01_base_v072_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_5d_s01_base_v073_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_5d_s01_base_v074_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_5d_s01_base_v075_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F47_HIDDEN_RENEWABLE_COMPOUNDER_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    roic    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    cols = {"closeadj": closeadj, "fcf": fcf, "roic": roic, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f47_quiet_fcf_growth", "_f47_low_attention_growth", "_f47_hidden_quality_score",)
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
    print(f"OK f47_hidden_renewable_compounder_base_001_075_claude: {n_features} features pass")
