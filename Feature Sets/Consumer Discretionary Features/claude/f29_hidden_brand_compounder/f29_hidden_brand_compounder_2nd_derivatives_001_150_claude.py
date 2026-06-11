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

def f29hbc_f29_hidden_brand_compounder_qfcfg_5d_slope_v001_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 5)
    base = b * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_5d_slope_v002_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 5)
    base = b * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_5d_slope_v003_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 5)
    base = b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_5d_slope_v004_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 5)
    base = b * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_5d_slope_v005_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 5)
    base = b * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_10d_slope_v006_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 10)
    base = b * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_10d_slope_v007_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 10)
    base = b * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_10d_slope_v008_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 10)
    base = b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_10d_slope_v009_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 10)
    base = b * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_10d_slope_v010_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 10)
    base = b * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_21d_slope_v011_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 21)
    base = b * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_21d_slope_v012_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 21)
    base = b * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_21d_slope_v013_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 21)
    base = b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_21d_slope_v014_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 21)
    base = b * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_21d_slope_v015_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 21)
    base = b * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_42d_slope_v016_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 42)
    base = b * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_42d_slope_v017_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 42)
    base = b * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_42d_slope_v018_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 42)
    base = b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_42d_slope_v019_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 42)
    base = b * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_42d_slope_v020_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 42)
    base = b * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_63d_slope_v021_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 63)
    base = b * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_63d_slope_v022_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 63)
    base = b * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_63d_slope_v023_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 63)
    base = b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_63d_slope_v024_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 63)
    base = b * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_63d_slope_v025_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 63)
    base = b * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_126d_slope_v026_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 126)
    base = b * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_126d_slope_v027_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 126)
    base = b * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_126d_slope_v028_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 126)
    base = b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_126d_slope_v029_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 126)
    base = b * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_126d_slope_v030_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 126)
    base = b * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_189d_slope_v031_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 189)
    base = b * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_189d_slope_v032_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 189)
    base = b * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_189d_slope_v033_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 189)
    base = b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_189d_slope_v034_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 189)
    base = b * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_189d_slope_v035_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 189)
    base = b * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_252d_slope_v036_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 252)
    base = b * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_252d_slope_v037_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 252)
    base = b * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_252d_slope_v038_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 252)
    base = b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_252d_slope_v039_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 252)
    base = b * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_252d_slope_v040_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 252)
    base = b * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_378d_slope_v041_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 378)
    base = b * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_378d_slope_v042_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 378)
    base = b * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_378d_slope_v043_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 378)
    base = b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_378d_slope_v044_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 378)
    base = b * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_378d_slope_v045_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 378)
    base = b * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_504d_slope_v046_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 504)
    base = b * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_504d_slope_v047_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 504)
    base = b * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_504d_slope_v048_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 504)
    base = b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_504d_slope_v049_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 504)
    base = b * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_qfcfg_504d_slope_v050_signal(fcf, closeadj):
    b = _f29_quiet_fcf_growth(fcf, 504)
    base = b * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_5d_slope_v051_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 5)
    base = b * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_5d_slope_v052_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 5)
    base = b * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_5d_slope_v053_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 5)
    base = b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_5d_slope_v054_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 5)
    base = b * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_5d_slope_v055_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 5)
    base = b * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_10d_slope_v056_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 10)
    base = b * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_10d_slope_v057_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 10)
    base = b * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_10d_slope_v058_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 10)
    base = b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_10d_slope_v059_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 10)
    base = b * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_10d_slope_v060_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 10)
    base = b * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_21d_slope_v061_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 21)
    base = b * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_21d_slope_v062_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 21)
    base = b * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_21d_slope_v063_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 21)
    base = b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_21d_slope_v064_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 21)
    base = b * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_21d_slope_v065_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 21)
    base = b * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_42d_slope_v066_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 42)
    base = b * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_42d_slope_v067_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 42)
    base = b * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_42d_slope_v068_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 42)
    base = b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_42d_slope_v069_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 42)
    base = b * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_42d_slope_v070_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 42)
    base = b * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_63d_slope_v071_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 63)
    base = b * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_63d_slope_v072_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 63)
    base = b * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_63d_slope_v073_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 63)
    base = b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_63d_slope_v074_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 63)
    base = b * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_63d_slope_v075_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 63)
    base = b * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_126d_slope_v076_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 126)
    base = b * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_126d_slope_v077_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 126)
    base = b * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_126d_slope_v078_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 126)
    base = b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_126d_slope_v079_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 126)
    base = b * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_126d_slope_v080_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 126)
    base = b * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_189d_slope_v081_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 189)
    base = b * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_189d_slope_v082_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 189)
    base = b * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_189d_slope_v083_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 189)
    base = b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_189d_slope_v084_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 189)
    base = b * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_189d_slope_v085_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 189)
    base = b * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_252d_slope_v086_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 252)
    base = b * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_252d_slope_v087_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 252)
    base = b * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_252d_slope_v088_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 252)
    base = b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_252d_slope_v089_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 252)
    base = b * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_252d_slope_v090_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 252)
    base = b * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_378d_slope_v091_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 378)
    base = b * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_378d_slope_v092_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 378)
    base = b * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_378d_slope_v093_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 378)
    base = b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_378d_slope_v094_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 378)
    base = b * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_378d_slope_v095_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 378)
    base = b * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_504d_slope_v096_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 504)
    base = b * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_504d_slope_v097_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 504)
    base = b * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_504d_slope_v098_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 504)
    base = b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_504d_slope_v099_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 504)
    base = b * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_attn_504d_slope_v100_signal(closeadj, volume, fcf):
    b = _f29_low_attention_growth(closeadj, volume, fcf, 504)
    base = b * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_5d_slope_v101_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 5)
    base = b * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_5d_slope_v102_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 5)
    base = b * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_5d_slope_v103_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 5)
    base = b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_5d_slope_v104_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 5)
    base = b * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_5d_slope_v105_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 5)
    base = b * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_10d_slope_v106_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 10)
    base = b * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_10d_slope_v107_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 10)
    base = b * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_10d_slope_v108_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 10)
    base = b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_10d_slope_v109_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 10)
    base = b * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_10d_slope_v110_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 10)
    base = b * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_21d_slope_v111_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 21)
    base = b * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_21d_slope_v112_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 21)
    base = b * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_21d_slope_v113_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 21)
    base = b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_21d_slope_v114_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 21)
    base = b * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_21d_slope_v115_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 21)
    base = b * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_42d_slope_v116_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 42)
    base = b * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_42d_slope_v117_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 42)
    base = b * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_42d_slope_v118_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 42)
    base = b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_42d_slope_v119_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 42)
    base = b * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_42d_slope_v120_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 42)
    base = b * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_63d_slope_v121_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 63)
    base = b * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_63d_slope_v122_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 63)
    base = b * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_63d_slope_v123_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 63)
    base = b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_63d_slope_v124_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 63)
    base = b * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_63d_slope_v125_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 63)
    base = b * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_126d_slope_v126_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 126)
    base = b * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_126d_slope_v127_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 126)
    base = b * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_126d_slope_v128_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 126)
    base = b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_126d_slope_v129_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 126)
    base = b * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_126d_slope_v130_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 126)
    base = b * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_189d_slope_v131_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 189)
    base = b * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_189d_slope_v132_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 189)
    base = b * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_189d_slope_v133_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 189)
    base = b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_189d_slope_v134_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 189)
    base = b * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_189d_slope_v135_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 189)
    base = b * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_252d_slope_v136_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 252)
    base = b * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_252d_slope_v137_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 252)
    base = b * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_252d_slope_v138_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 252)
    base = b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_252d_slope_v139_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 252)
    base = b * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_252d_slope_v140_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 252)
    base = b * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_378d_slope_v141_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 378)
    base = b * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_378d_slope_v142_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 378)
    base = b * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_378d_slope_v143_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 378)
    base = b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_378d_slope_v144_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 378)
    base = b * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_378d_slope_v145_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 378)
    base = b * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_504d_slope_v146_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 504)
    base = b * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_504d_slope_v147_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 504)
    base = b * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_504d_slope_v148_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 504)
    base = b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_504d_slope_v149_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 504)
    base = b * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f29hbc_f29_hidden_brand_compounder_hcs_504d_slope_v150_signal(fcf, roic, closeadj):
    b = _f29_hidden_compounder_score(fcf, roic, 504)
    base = b * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f29hbc_f29_hidden_brand_compounder_qfcfg_5d_slope_v001_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_5d_slope_v002_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_5d_slope_v003_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_5d_slope_v004_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_5d_slope_v005_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_10d_slope_v006_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_10d_slope_v007_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_10d_slope_v008_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_10d_slope_v009_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_10d_slope_v010_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_21d_slope_v011_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_21d_slope_v012_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_21d_slope_v013_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_21d_slope_v014_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_21d_slope_v015_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_42d_slope_v016_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_42d_slope_v017_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_42d_slope_v018_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_42d_slope_v019_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_42d_slope_v020_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_63d_slope_v021_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_63d_slope_v022_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_63d_slope_v023_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_63d_slope_v024_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_63d_slope_v025_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_126d_slope_v026_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_126d_slope_v027_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_126d_slope_v028_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_126d_slope_v029_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_126d_slope_v030_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_189d_slope_v031_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_189d_slope_v032_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_189d_slope_v033_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_189d_slope_v034_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_189d_slope_v035_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_252d_slope_v036_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_252d_slope_v037_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_252d_slope_v038_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_252d_slope_v039_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_252d_slope_v040_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_378d_slope_v041_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_378d_slope_v042_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_378d_slope_v043_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_378d_slope_v044_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_378d_slope_v045_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_504d_slope_v046_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_504d_slope_v047_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_504d_slope_v048_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_504d_slope_v049_signal,
    f29hbc_f29_hidden_brand_compounder_qfcfg_504d_slope_v050_signal,
    f29hbc_f29_hidden_brand_compounder_attn_5d_slope_v051_signal,
    f29hbc_f29_hidden_brand_compounder_attn_5d_slope_v052_signal,
    f29hbc_f29_hidden_brand_compounder_attn_5d_slope_v053_signal,
    f29hbc_f29_hidden_brand_compounder_attn_5d_slope_v054_signal,
    f29hbc_f29_hidden_brand_compounder_attn_5d_slope_v055_signal,
    f29hbc_f29_hidden_brand_compounder_attn_10d_slope_v056_signal,
    f29hbc_f29_hidden_brand_compounder_attn_10d_slope_v057_signal,
    f29hbc_f29_hidden_brand_compounder_attn_10d_slope_v058_signal,
    f29hbc_f29_hidden_brand_compounder_attn_10d_slope_v059_signal,
    f29hbc_f29_hidden_brand_compounder_attn_10d_slope_v060_signal,
    f29hbc_f29_hidden_brand_compounder_attn_21d_slope_v061_signal,
    f29hbc_f29_hidden_brand_compounder_attn_21d_slope_v062_signal,
    f29hbc_f29_hidden_brand_compounder_attn_21d_slope_v063_signal,
    f29hbc_f29_hidden_brand_compounder_attn_21d_slope_v064_signal,
    f29hbc_f29_hidden_brand_compounder_attn_21d_slope_v065_signal,
    f29hbc_f29_hidden_brand_compounder_attn_42d_slope_v066_signal,
    f29hbc_f29_hidden_brand_compounder_attn_42d_slope_v067_signal,
    f29hbc_f29_hidden_brand_compounder_attn_42d_slope_v068_signal,
    f29hbc_f29_hidden_brand_compounder_attn_42d_slope_v069_signal,
    f29hbc_f29_hidden_brand_compounder_attn_42d_slope_v070_signal,
    f29hbc_f29_hidden_brand_compounder_attn_63d_slope_v071_signal,
    f29hbc_f29_hidden_brand_compounder_attn_63d_slope_v072_signal,
    f29hbc_f29_hidden_brand_compounder_attn_63d_slope_v073_signal,
    f29hbc_f29_hidden_brand_compounder_attn_63d_slope_v074_signal,
    f29hbc_f29_hidden_brand_compounder_attn_63d_slope_v075_signal,
    f29hbc_f29_hidden_brand_compounder_attn_126d_slope_v076_signal,
    f29hbc_f29_hidden_brand_compounder_attn_126d_slope_v077_signal,
    f29hbc_f29_hidden_brand_compounder_attn_126d_slope_v078_signal,
    f29hbc_f29_hidden_brand_compounder_attn_126d_slope_v079_signal,
    f29hbc_f29_hidden_brand_compounder_attn_126d_slope_v080_signal,
    f29hbc_f29_hidden_brand_compounder_attn_189d_slope_v081_signal,
    f29hbc_f29_hidden_brand_compounder_attn_189d_slope_v082_signal,
    f29hbc_f29_hidden_brand_compounder_attn_189d_slope_v083_signal,
    f29hbc_f29_hidden_brand_compounder_attn_189d_slope_v084_signal,
    f29hbc_f29_hidden_brand_compounder_attn_189d_slope_v085_signal,
    f29hbc_f29_hidden_brand_compounder_attn_252d_slope_v086_signal,
    f29hbc_f29_hidden_brand_compounder_attn_252d_slope_v087_signal,
    f29hbc_f29_hidden_brand_compounder_attn_252d_slope_v088_signal,
    f29hbc_f29_hidden_brand_compounder_attn_252d_slope_v089_signal,
    f29hbc_f29_hidden_brand_compounder_attn_252d_slope_v090_signal,
    f29hbc_f29_hidden_brand_compounder_attn_378d_slope_v091_signal,
    f29hbc_f29_hidden_brand_compounder_attn_378d_slope_v092_signal,
    f29hbc_f29_hidden_brand_compounder_attn_378d_slope_v093_signal,
    f29hbc_f29_hidden_brand_compounder_attn_378d_slope_v094_signal,
    f29hbc_f29_hidden_brand_compounder_attn_378d_slope_v095_signal,
    f29hbc_f29_hidden_brand_compounder_attn_504d_slope_v096_signal,
    f29hbc_f29_hidden_brand_compounder_attn_504d_slope_v097_signal,
    f29hbc_f29_hidden_brand_compounder_attn_504d_slope_v098_signal,
    f29hbc_f29_hidden_brand_compounder_attn_504d_slope_v099_signal,
    f29hbc_f29_hidden_brand_compounder_attn_504d_slope_v100_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_5d_slope_v101_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_5d_slope_v102_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_5d_slope_v103_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_5d_slope_v104_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_5d_slope_v105_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_10d_slope_v106_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_10d_slope_v107_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_10d_slope_v108_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_10d_slope_v109_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_10d_slope_v110_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_21d_slope_v111_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_21d_slope_v112_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_21d_slope_v113_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_21d_slope_v114_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_21d_slope_v115_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_42d_slope_v116_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_42d_slope_v117_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_42d_slope_v118_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_42d_slope_v119_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_42d_slope_v120_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_63d_slope_v121_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_63d_slope_v122_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_63d_slope_v123_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_63d_slope_v124_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_63d_slope_v125_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_126d_slope_v126_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_126d_slope_v127_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_126d_slope_v128_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_126d_slope_v129_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_126d_slope_v130_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_189d_slope_v131_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_189d_slope_v132_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_189d_slope_v133_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_189d_slope_v134_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_189d_slope_v135_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_252d_slope_v136_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_252d_slope_v137_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_252d_slope_v138_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_252d_slope_v139_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_252d_slope_v140_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_378d_slope_v141_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_378d_slope_v142_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_378d_slope_v143_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_378d_slope_v144_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_378d_slope_v145_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_504d_slope_v146_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_504d_slope_v147_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_504d_slope_v148_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_504d_slope_v149_signal,
    f29hbc_f29_hidden_brand_compounder_hcs_504d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values() if p.default is inspect.Parameter.empty]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F29_HIDDEN_BRAND_COMPOUNDER_REGISTRY_SLOPE_001_150 = REGISTRY


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
    print(f"OK f29_hidden_brand_compounder_2nd_derivatives_001_150_claude: {n_features} features pass")
