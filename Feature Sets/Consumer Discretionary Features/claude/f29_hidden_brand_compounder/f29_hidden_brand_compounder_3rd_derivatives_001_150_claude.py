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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)

# ===== folder domain primitives =====
def _f29_quiet_fcf_growth(fcf, w):
    g = fcf.pct_change(periods=w)
    return _mean(g, w) - _std(g, w)


def _f29_low_attention_growth(closeadj, volume, fcf, w):
    dv = closeadj * volume
    attn = _mean(dv, w)
    g = fcf.pct_change(periods=w)
    return _mean(g, w) / np.log(attn.replace(0, np.nan).abs() + 1.0)


def _f29_hidden_compounder_score(fcf, roic, w):
    g = fcf.pct_change(periods=w)
    return _mean(g, w) * _mean(roic, w)


# ===== features =====

def f29hbc_f29_hidden_brand_compounder_qfcfg_5d_jerk_v001_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 5)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_5d_jerk_v002_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 5)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_5d_jerk_v003_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 5)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_5d_jerk_v004_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 5)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_5d_jerk_v005_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 5)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_10d_jerk_v006_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 10)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_10d_jerk_v007_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 10)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_10d_jerk_v008_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 10)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_10d_jerk_v009_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 10)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_10d_jerk_v010_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 10)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_21d_jerk_v011_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 21)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_21d_jerk_v012_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 21)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_21d_jerk_v013_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 21)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_21d_jerk_v014_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 21)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_21d_jerk_v015_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 21)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_42d_jerk_v016_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 42)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_42d_jerk_v017_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 42)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_42d_jerk_v018_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 42)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_42d_jerk_v019_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 42)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_42d_jerk_v020_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 42)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_63d_jerk_v021_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 63)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_63d_jerk_v022_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 63)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_63d_jerk_v023_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 63)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_63d_jerk_v024_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 63)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_63d_jerk_v025_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 63)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_126d_jerk_v026_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 126)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_126d_jerk_v027_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 126)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_126d_jerk_v028_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 126)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_126d_jerk_v029_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 126)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_126d_jerk_v030_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 126)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_189d_jerk_v031_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 189)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_189d_jerk_v032_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 189)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_189d_jerk_v033_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 189)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_189d_jerk_v034_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 189)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_189d_jerk_v035_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 189)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_252d_jerk_v036_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 252)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_252d_jerk_v037_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 252)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_252d_jerk_v038_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 252)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_252d_jerk_v039_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 252)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_252d_jerk_v040_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 252)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_378d_jerk_v041_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 378)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_378d_jerk_v042_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 378)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_378d_jerk_v043_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 378)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_378d_jerk_v044_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 378)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_378d_jerk_v045_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 378)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_504d_jerk_v046_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 504)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_504d_jerk_v047_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 504)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_504d_jerk_v048_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 504)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_504d_jerk_v049_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 504)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_504d_jerk_v050_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 504)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_5d_jerk_v051_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 5)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_5d_jerk_v052_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 5)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_5d_jerk_v053_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 5)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_5d_jerk_v054_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 5)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_5d_jerk_v055_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 5)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_10d_jerk_v056_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 10)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_10d_jerk_v057_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 10)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_10d_jerk_v058_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 10)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_10d_jerk_v059_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 10)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_10d_jerk_v060_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 10)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_21d_jerk_v061_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 21)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_21d_jerk_v062_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 21)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_21d_jerk_v063_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 21)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_21d_jerk_v064_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 21)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_21d_jerk_v065_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 21)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_42d_jerk_v066_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 42)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_42d_jerk_v067_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 42)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_42d_jerk_v068_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 42)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_42d_jerk_v069_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 42)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_42d_jerk_v070_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 42)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_63d_jerk_v071_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 63)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_63d_jerk_v072_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 63)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_63d_jerk_v073_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 63)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_63d_jerk_v074_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 63)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_63d_jerk_v075_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 63)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_126d_jerk_v076_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 126)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_126d_jerk_v077_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 126)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_126d_jerk_v078_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 126)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_126d_jerk_v079_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 126)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_126d_jerk_v080_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 126)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_189d_jerk_v081_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 189)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_189d_jerk_v082_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 189)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_189d_jerk_v083_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 189)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_189d_jerk_v084_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 189)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_189d_jerk_v085_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 189)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_252d_jerk_v086_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 252)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_252d_jerk_v087_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 252)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_252d_jerk_v088_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 252)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_252d_jerk_v089_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 252)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_252d_jerk_v090_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 252)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_378d_jerk_v091_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 378)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_378d_jerk_v092_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 378)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_378d_jerk_v093_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 378)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_378d_jerk_v094_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 378)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_378d_jerk_v095_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 378)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_504d_jerk_v096_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 504)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_504d_jerk_v097_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 504)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_504d_jerk_v098_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 504)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_504d_jerk_v099_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 504)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_504d_jerk_v100_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 504)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_5d_jerk_v101_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 5)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_5d_jerk_v102_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 5)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_5d_jerk_v103_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 5)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_5d_jerk_v104_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 5)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_5d_jerk_v105_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 5)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_10d_jerk_v106_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 10)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_10d_jerk_v107_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 10)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_10d_jerk_v108_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 10)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_10d_jerk_v109_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 10)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_10d_jerk_v110_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 10)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_21d_jerk_v111_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 21)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_21d_jerk_v112_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 21)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_21d_jerk_v113_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 21)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_21d_jerk_v114_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 21)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_21d_jerk_v115_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 21)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_42d_jerk_v116_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 42)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_42d_jerk_v117_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 42)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_42d_jerk_v118_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 42)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_42d_jerk_v119_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 42)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_42d_jerk_v120_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 42)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_63d_jerk_v121_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 63)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_63d_jerk_v122_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 63)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_63d_jerk_v123_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 63)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_63d_jerk_v124_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 63)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_63d_jerk_v125_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 63)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_126d_jerk_v126_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 126)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_126d_jerk_v127_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 126)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_126d_jerk_v128_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 126)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_126d_jerk_v129_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 126)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_126d_jerk_v130_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 126)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_189d_jerk_v131_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 189)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_189d_jerk_v132_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 189)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_189d_jerk_v133_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 189)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_189d_jerk_v134_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 189)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_189d_jerk_v135_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 189)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_252d_jerk_v136_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 252)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_252d_jerk_v137_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 252)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_252d_jerk_v138_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 252)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_252d_jerk_v139_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 252)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_252d_jerk_v140_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 252)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_378d_jerk_v141_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 378)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_378d_jerk_v142_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 378)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_378d_jerk_v143_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 378)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_378d_jerk_v144_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 378)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_378d_jerk_v145_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 378)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_504d_jerk_v146_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 504)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_504d_jerk_v147_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 504)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_504d_jerk_v148_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 504)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_504d_jerk_v149_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 504)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_504d_jerk_v150_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 504)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f29hbc_f29_hidden_brand_compounder_qfcfg_5d_jerk_v001_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_5d_jerk_v002_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_5d_jerk_v003_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_5d_jerk_v004_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_5d_jerk_v005_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_10d_jerk_v006_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_10d_jerk_v007_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_10d_jerk_v008_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_10d_jerk_v009_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_10d_jerk_v010_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_21d_jerk_v011_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_21d_jerk_v012_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_21d_jerk_v013_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_21d_jerk_v014_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_21d_jerk_v015_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_42d_jerk_v016_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_42d_jerk_v017_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_42d_jerk_v018_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_42d_jerk_v019_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_42d_jerk_v020_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_63d_jerk_v021_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_63d_jerk_v022_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_63d_jerk_v023_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_63d_jerk_v024_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_63d_jerk_v025_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_126d_jerk_v026_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_126d_jerk_v027_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_126d_jerk_v028_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_126d_jerk_v029_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_126d_jerk_v030_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_189d_jerk_v031_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_189d_jerk_v032_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_189d_jerk_v033_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_189d_jerk_v034_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_189d_jerk_v035_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_252d_jerk_v036_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_252d_jerk_v037_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_252d_jerk_v038_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_252d_jerk_v039_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_252d_jerk_v040_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_378d_jerk_v041_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_378d_jerk_v042_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_378d_jerk_v043_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_378d_jerk_v044_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_378d_jerk_v045_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_504d_jerk_v046_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_504d_jerk_v047_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_504d_jerk_v048_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_504d_jerk_v049_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_504d_jerk_v050_signal,
    f29hbc_f29_hidden_brand_compounder_attn_5d_jerk_v051_signal,
    f29hbc_f29_hidden_brand_compounder_attn_5d_jerk_v052_signal,
    f29hbc_f29_hidden_brand_compounder_attn_5d_jerk_v053_signal,
    f29hbc_f29_hidden_brand_compounder_attn_5d_jerk_v054_signal,
    f29hbc_f29_hidden_brand_compounder_attn_5d_jerk_v055_signal,
    f29hbc_f29_hidden_brand_compounder_attn_10d_jerk_v056_signal,
    f29hbc_f29_hidden_brand_compounder_attn_10d_jerk_v057_signal,
    f29hbc_f29_hidden_brand_compounder_attn_10d_jerk_v058_signal,
    f29hbc_f29_hidden_brand_compounder_attn_10d_jerk_v059_signal,
    f29hbc_f29_hidden_brand_compounder_attn_10d_jerk_v060_signal,
    f29hbc_f29_hidden_brand_compounder_attn_21d_jerk_v061_signal,
    f29hbc_f29_hidden_brand_compounder_attn_21d_jerk_v062_signal,
    f29hbc_f29_hidden_brand_compounder_attn_21d_jerk_v063_signal,
    f29hbc_f29_hidden_brand_compounder_attn_21d_jerk_v064_signal,
    f29hbc_f29_hidden_brand_compounder_attn_21d_jerk_v065_signal,
    f29hbc_f29_hidden_brand_compounder_attn_42d_jerk_v066_signal,
    f29hbc_f29_hidden_brand_compounder_attn_42d_jerk_v067_signal,
    f29hbc_f29_hidden_brand_compounder_attn_42d_jerk_v068_signal,
    f29hbc_f29_hidden_brand_compounder_attn_42d_jerk_v069_signal,
    f29hbc_f29_hidden_brand_compounder_attn_42d_jerk_v070_signal,
    f29hbc_f29_hidden_brand_compounder_attn_63d_jerk_v071_signal,
    f29hbc_f29_hidden_brand_compounder_attn_63d_jerk_v072_signal,
    f29hbc_f29_hidden_brand_compounder_attn_63d_jerk_v073_signal,
    f29hbc_f29_hidden_brand_compounder_attn_63d_jerk_v074_signal,
    f29hbc_f29_hidden_brand_compounder_attn_63d_jerk_v075_signal,
    f29hbc_f29_hidden_brand_compounder_attn_126d_jerk_v076_signal,
    f29hbc_f29_hidden_brand_compounder_attn_126d_jerk_v077_signal,
    f29hbc_f29_hidden_brand_compounder_attn_126d_jerk_v078_signal,
    f29hbc_f29_hidden_brand_compounder_attn_126d_jerk_v079_signal,
    f29hbc_f29_hidden_brand_compounder_attn_126d_jerk_v080_signal,
    f29hbc_f29_hidden_brand_compounder_attn_189d_jerk_v081_signal,
    f29hbc_f29_hidden_brand_compounder_attn_189d_jerk_v082_signal,
    f29hbc_f29_hidden_brand_compounder_attn_189d_jerk_v083_signal,
    f29hbc_f29_hidden_brand_compounder_attn_189d_jerk_v084_signal,
    f29hbc_f29_hidden_brand_compounder_attn_189d_jerk_v085_signal,
    f29hbc_f29_hidden_brand_compounder_attn_252d_jerk_v086_signal,
    f29hbc_f29_hidden_brand_compounder_attn_252d_jerk_v087_signal,
    f29hbc_f29_hidden_brand_compounder_attn_252d_jerk_v088_signal,
    f29hbc_f29_hidden_brand_compounder_attn_252d_jerk_v089_signal,
    f29hbc_f29_hidden_brand_compounder_attn_252d_jerk_v090_signal,
    f29hbc_f29_hidden_brand_compounder_attn_378d_jerk_v091_signal,
    f29hbc_f29_hidden_brand_compounder_attn_378d_jerk_v092_signal,
    f29hbc_f29_hidden_brand_compounder_attn_378d_jerk_v093_signal,
    f29hbc_f29_hidden_brand_compounder_attn_378d_jerk_v094_signal,
    f29hbc_f29_hidden_brand_compounder_attn_378d_jerk_v095_signal,
    f29hbc_f29_hidden_brand_compounder_attn_504d_jerk_v096_signal,
    f29hbc_f29_hidden_brand_compounder_attn_504d_jerk_v097_signal,
    f29hbc_f29_hidden_brand_compounder_attn_504d_jerk_v098_signal,
    f29hbc_f29_hidden_brand_compounder_attn_504d_jerk_v099_signal,
    f29hbc_f29_hidden_brand_compounder_attn_504d_jerk_v100_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_5d_jerk_v101_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_5d_jerk_v102_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_5d_jerk_v103_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_5d_jerk_v104_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_5d_jerk_v105_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_10d_jerk_v106_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_10d_jerk_v107_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_10d_jerk_v108_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_10d_jerk_v109_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_10d_jerk_v110_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_21d_jerk_v111_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_21d_jerk_v112_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_21d_jerk_v113_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_21d_jerk_v114_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_21d_jerk_v115_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_42d_jerk_v116_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_42d_jerk_v117_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_42d_jerk_v118_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_42d_jerk_v119_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_42d_jerk_v120_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_63d_jerk_v121_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_63d_jerk_v122_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_63d_jerk_v123_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_63d_jerk_v124_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_63d_jerk_v125_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_126d_jerk_v126_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_126d_jerk_v127_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_126d_jerk_v128_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_126d_jerk_v129_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_126d_jerk_v130_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_189d_jerk_v131_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_189d_jerk_v132_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_189d_jerk_v133_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_189d_jerk_v134_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_189d_jerk_v135_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_252d_jerk_v136_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_252d_jerk_v137_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_252d_jerk_v138_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_252d_jerk_v139_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_252d_jerk_v140_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_378d_jerk_v141_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_378d_jerk_v142_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_378d_jerk_v143_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_378d_jerk_v144_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_378d_jerk_v145_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_504d_jerk_v146_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_504d_jerk_v147_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_504d_jerk_v148_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_504d_jerk_v149_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_504d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values() if p.default is inspect.Parameter.empty]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F29_HIDDEN_BRAND_COMPOUNDER_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    fcf    = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    roic   = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    cols = {"closeadj": closeadj, "fcf": fcf, "volume": volume, "roic": roic}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f29_quiet_fcf_growth", "_f29_low_attention_growth", "_f29_hidden_compounder_score",)
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
    print(f"OK f29_hidden_brand_compounder_3rd_derivatives_001_150_claude: {n_features} features pass")
